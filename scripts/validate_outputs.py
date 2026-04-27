from __future__ import annotations
from pathlib import Path
from common import STUDY_END_YEAR, STUDY_START_YEAR, ensure_parent
import argparse
import json
import pandas as pd

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--panel", required=True)
    parser.add_argument("--community", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    panel = pd.read_csv(args.panel)
    community = pd.read_csv(args.community)

    required_panel_columns = {
        "year",
        "community_area_number",
        "community_area_name",
        "homicide_victims",
        "nonfatal_shooting_victims",
        "total_gun_violence_victims",
    }
    required_community_columns = {
        "community_area_number",
        "community_area_name",
        "mean_annual_homicide_victims",
        "mean_annual_nonfatal_shooting_victims",
        "mean_annual_total_victims",
    }
    forbidden_columns = {
        "homicide_victim_first_name",
        "homicide_victim_mi",
        "homicide_victim_last_name",
    }

    errors = []
    if missing := sorted(required_panel_columns - set(panel.columns)):
        errors.append(f"Missing required panel columns: {missing}")
    if missing := sorted(required_community_columns - set(community.columns)):
        errors.append(f"Missing required community columns: {missing}")
    if forbidden_present := sorted(forbidden_columns & set(panel.columns)):
        errors.append(f"Forbidden identifier columns present in panel: {forbidden_present}")
    if forbidden_present := sorted(forbidden_columns & set(community.columns)):
        errors.append(f"Forbidden identifier columns present in community table: {forbidden_present}")
    if int(panel["community_area_number"].nunique()) != 77:
        errors.append("Community coverage is not exactly 77 in the panel output.")
    years = sorted(int(year) for year in panel["year"].unique())
    if years != list(range(STUDY_START_YEAR, STUDY_END_YEAR + 1)):
        errors.append(f"Unexpected study-year coverage: {years}")

    report = {"valid": not errors, "errors": errors}
    output_path = Path(args.output)
    ensure_parent(output_path)
    output_path.write_text(json.dumps(report, indent=2) + "\n")

    if errors:
        raise SystemExit("\n".join(errors))

if __name__ == "__main__":
    main()
