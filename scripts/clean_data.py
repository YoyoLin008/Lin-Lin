from __future__ import annotations
from common import (
    IDENTIFIER_COLUMNS,
    STUDY_END_YEAR,
    STUDY_START_YEAR,
    classify_record,
    ensure_parent,
    load_health,
    snake_case,
    standardize_area_name,
)
import argparse
import pandas as pd

def clean_violence(path: str) -> pd.DataFrame:
    violence = pd.read_csv(path)
    violence.columns = [snake_case(column) for column in violence.columns]

    violence["date"] = pd.to_datetime(
        violence["date"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce"
    )
    violence["year"] = violence["date"].dt.year
    violence["community_area_name"] = violence["community_area"].map(standardize_area_name)
    violence["gunshot_injury_i"] = violence["gunshot_injury_i"].fillna("NO").str.upper()
    violence["victimization_primary"] = violence["victimization_primary"].fillna("").str.upper()

    study_window = violence["year"].between(STUDY_START_YEAR, STUDY_END_YEAR)
    violence = violence.loc[study_window].copy()

    is_homicide = violence["victimization_primary"].eq("HOMICIDE")
    gunshot = violence["gunshot_injury_i"].eq("YES")
    violence[["is_homicide_victim", "is_nonfatal_shooting_victim"]] = classify_record(
        is_homicide, gunshot
    )
    violence["is_gun_violence_victim"] = (
        violence["is_homicide_victim"] + violence["is_nonfatal_shooting_victim"]
    )
    violence = violence.loc[violence["is_gun_violence_victim"] > 0].copy()

    columns_to_drop = [snake_case(column) for column in IDENTIFIER_COLUMNS]
    existing_drop_columns = [column for column in columns_to_drop if column in violence.columns]
    violence = violence.drop(columns=existing_drop_columns)

    keep_columns = [
        "case_number", "date", "year", "month",
        "day_of_week", "hour", "community_area_name", "victimization_primary",
        "incident_primary", "gunshot_injury_i", "age", "sex",
        "race", "is_homicide_victim", "is_nonfatal_shooting_victim", "is_gun_violence_victim",
    ]
    violence = violence[keep_columns].sort_values(["year", "community_area_name", "date"]).reset_index(
        drop=True
    )
    return violence

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--health", required=True)
    parser.add_argument("--violence", required=True)
    parser.add_argument("--health-out", required=True)
    parser.add_argument("--violence-out", required=True)
    args = parser.parse_args()

    health = load_health(args.health)
    violence = clean_violence(args.violence)

    ensure_parent(args.health_out)
    ensure_parent(args.violence_out)
    health.to_csv(args.health_out, index=False)
    violence.to_csv(args.violence_out, index=False)

if __name__ == "__main__":
    main()
