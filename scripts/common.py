from __future__ import annotations
from pathlib import Path
import pandas as pd
import re

STUDY_START_YEAR = 2005
STUDY_END_YEAR = 2010
STUDY_YEARS = list(range(STUDY_START_YEAR, STUDY_END_YEAR + 1))

HEALTH_ID_COLUMNS = ["Community Area", "Community Area Name"]
IDENTIFIER_COLUMNS = [
    "HOMICIDE_VICTIM_FIRST_NAME",
    "HOMICIDE_VICTIM_MI",
    "HOMICIDE_VICTIM_LAST_NAME",
]

PROJECT_ROOT = Path(__file__).resolve().parents[1]

def ensure_parent(path: str | Path) -> None:
    Path(path).parent.mkdir(parents=True, exist_ok=True)

def snake_case(name: str) -> str:
    slug = name.strip().lower()
    slug = re.sub(r"[^a-z0-9]+", "_", slug)
    return slug.strip("_")

def standardize_area_name(value: object) -> str | None:
    if pd.isna(value):
        return None
    text = str(value).strip().upper()
    if not text:
        return None
    fixes = {
        "MONTCLARE": "MONTCLAIRE",
        "OHARE": "O'HARE",
    }
    return fixes.get(text, text)

def load_health(path: str | Path) -> pd.DataFrame:
    health = pd.read_csv(path)
    health.columns = [snake_case(col) for col in health.columns]
    health = health.rename(
        columns={
            "community_area": "community_area_number",
            "community_area_name": "community_area_name",
        }
    )
    health["community_area_number"] = pd.to_numeric(
        health["community_area_number"], errors="coerce"
    ).astype("Int64")
    health["community_area_name"] = health["community_area_name"].map(standardize_area_name)

    indicator_columns = [
        column
        for column in health.columns
        if column not in {"community_area_number", "community_area_name"}
    ]
    for column in indicator_columns:
        health[column] = pd.to_numeric(health[column].replace(".", pd.NA), errors="coerce")

    return health.sort_values("community_area_number").reset_index(drop=True)

def classify_record(is_homicide: pd.Series, gunshot: pd.Series) -> pd.DataFrame:
    return pd.DataFrame(
        {
            "is_homicide_victim": is_homicide.astype(int),
            "is_nonfatal_shooting_victim": ((~is_homicide) & gunshot).astype(int),
        }
    )
