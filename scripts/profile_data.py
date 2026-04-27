from __future__ import annotations
from common import IDENTIFIER_COLUMNS, STUDY_END_YEAR, STUDY_START_YEAR, ensure_parent
from pathlib import Path
import argparse
import json
import pandas as pd

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--health", required=True)
    parser.add_argument("--violence", required=True)
    parser.add_argument("--metrics-out", required=True)
    parser.add_argument("--findings-out", required=True)
    args = parser.parse_args()

    health = pd.read_csv(args.health)
    violence = pd.read_csv(args.violence)
    violence_dates = pd.to_datetime(violence["DATE"], format="%m/%d/%Y %I:%M:%S %p", errors="coerce")
    study_window = violence_dates.dt.year.between(STUDY_START_YEAR, STUDY_END_YEAR)

    metrics = pd.DataFrame(
        [
            {"dataset": "health", "metric": "rows", "value": int(len(health))},
            {"dataset": "health", "metric": "columns", "value": int(len(health.columns))},
            {
                "dataset": "health",
                "metric": "placeholder_dot_cells",
                "value": int((health == ".").sum().sum()),
            },
            {
                "dataset": "health",
                "metric": "communities",
                "value": int(health["Community Area"].nunique(dropna=True)),
            },
            {"dataset": "violence", "metric": "rows", "value": int(len(violence))},
            {"dataset": "violence", "metric": "columns", "value": int(len(violence.columns))},
            {
                "dataset": "violence",
                "metric": "study_window_rows_2005_2010",
                "value": int(study_window.sum()),
            },
            {
                "dataset": "violence",
                "metric": "study_window_communities",
                "value": int(violence.loc[study_window, "COMMUNITY_AREA"].nunique(dropna=True)),
            },
            {
                "dataset": "violence",
                "metric": "identifier_columns_in_raw",
                "value": int(sum(column in violence.columns for column in IDENTIFIER_COLUMNS)),
            },
        ]
    )

    findings = {
        "study_window": f"{STUDY_START_YEAR}-{STUDY_END_YEAR}",
        "issues_detected": [
            "Raw violence data contains direct homicide victim name fields and must not be published in processed outputs.",
            "The raw violence dataset uses community-area names and includes the spelling variant MONTCLARE, which needs to map to the official MONTCLAIRE crosswalk entry.",
            "The violence study window does not contain Edison Park incidents, so zero-count rows must be preserved after panel construction.",
            "The public-health dataset includes '.' placeholders that require numeric coercion to missing values before analysis.",
        ],
    }

    metrics_path = Path(args.metrics_out)
    findings_path = Path(args.findings_out)
    ensure_parent(metrics_path)
    ensure_parent(findings_path)
    metrics.to_csv(metrics_path, index=False)
    findings_path.write_text(json.dumps(findings, indent=2) + "\n")

if __name__ == "__main__":
    main()
