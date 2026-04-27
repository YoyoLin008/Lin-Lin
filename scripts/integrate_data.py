from __future__ import annotations
from common import STUDY_YEARS, ensure_parent
import argparse
import pandas as pd

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--health", required=True)
    parser.add_argument("--violence", required=True)
    parser.add_argument("--panel-out", required=True)
    parser.add_argument("--community-out", required=True)
    parser.add_argument("--checks-out", required=True)
    args = parser.parse_args()

    health = pd.read_csv(args.health)
    violence = pd.read_csv(args.violence)

    crosswalk = health[["community_area_number", "community_area_name"]].drop_duplicates()
    violence = violence.merge(crosswalk, on="community_area_name", how="left", validate="many_to_one")

    if violence["community_area_number"].isna().any():
        missing_areas = sorted(violence.loc[violence["community_area_number"].isna(), "community_area_name"].dropna().unique())
        raise ValueError(f"Unmatched community area names after crosswalk join: {missing_areas}")

    aggregated = (
        violence.groupby(["year", "community_area_number", "community_area_name"], as_index=False)[
            ["is_homicide_victim", "is_nonfatal_shooting_victim", "is_gun_violence_victim"]
        ]
        .sum()
        .rename(
            columns={
                "is_homicide_victim": "homicide_victims",
                "is_nonfatal_shooting_victim": "nonfatal_shooting_victims",
                "is_gun_violence_victim": "total_gun_violence_victims",
            }
        )
    )

    year_frame = pd.DataFrame({"year": STUDY_YEARS})
    full_panel = crosswalk.assign(key=1).merge(year_frame.assign(key=1), on="key").drop(columns="key")
    full_panel = full_panel.merge(
        aggregated,
        on=["year", "community_area_number", "community_area_name"],
        how="left",
    )
    count_columns = [
        "homicide_victims",
        "nonfatal_shooting_victims",
        "total_gun_violence_victims",
    ]
    full_panel[count_columns] = full_panel[count_columns].fillna(0).astype(int)
    full_panel = full_panel.sort_values(["year", "community_area_number"]).reset_index(drop=True)

    community = (
        full_panel.groupby(["community_area_number", "community_area_name"], as_index=False)[count_columns]
        .mean()
        .rename(
            columns={
                "homicide_victims": "mean_annual_homicide_victims",
                "nonfatal_shooting_victims": "mean_annual_nonfatal_shooting_victims",
                "total_gun_violence_victims": "mean_annual_total_victims",
            }
        )
    )
    community = community.merge(health, on=["community_area_number", "community_area_name"], how="left")
    community = community.sort_values("community_area_number").reset_index(drop=True)

    checks = pd.DataFrame(
        [
            {"check": "community_coverage", "value": int(full_panel["community_area_number"].nunique())},
            {"check": "year_coverage", "value": int(full_panel["year"].nunique())},
            {"check": "rows_in_panel", "value": int(len(full_panel))},
            {
                "check": "edison_park_total_victims_2005_2010",
                "value": int(
                    full_panel.loc[
                        full_panel["community_area_name"].eq("EDISON PARK"),
                        "total_gun_violence_victims",
                    ].sum()
                ),
            },
        ]
    )

    ensure_parent(args.panel_out)
    ensure_parent(args.community_out)
    ensure_parent(args.checks_out)
    full_panel.to_csv(args.panel_out, index=False)
    community.to_csv(args.community_out, index=False)
    checks.to_csv(args.checks_out, index=False)

if __name__ == "__main__":
    main()
