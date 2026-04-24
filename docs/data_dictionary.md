# Data Dictionary

This codebook documents the main datasets used and produced by the final MS4 workflow. Raw data live in `data/raw/`, cleaned intermediates live in `data/interim/`, processed analysis-ready tables live in `data/processed/`, and reproducible figures and summaries live in `results/`.

## Raw datasets

### `data/raw/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv`
- Unit of observation: one row per Chicago community area.
- Row count: 77.
- Key fields:
  - `Community Area`: official numeric community area identifier.
  - `Community Area Name`: official community area name.
  - Public-health and socioeconomic indicator columns such as `Teen Birth Rate`, `Below Poverty Level`, `Per Capita Income`, and `Unemployment`.
- Notes:
  - The dataset is static by community area rather than yearly.
  - Twelve cells contain `.` placeholders, which are converted to missing values during cleaning.

### `data/raw/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv`
- Unit of observation: one victimization record.
- Row count: 63,245 at acquisition time.
- Key fields:
  - `DATE`: incident timestamp.
  - `COMMUNITY_AREA`: community area name in the violence source.
  - `VICTIMIZATION_PRIMARY`: categorical victimization type.
  - `GUNSHOT_INJURY_I`: gunshot indicator.
  - `AGE`, `SEX`, `RACE`: victim demographics.
- Notes:
  - Raw data include homicide victim name fields that are considered direct identifiers and are dropped from all processed outputs.
  - The final study window is restricted to 2005-2010.

## Intermediate datasets

### `data/interim/health_indicators_clean.csv`
- Unit of observation: one row per Chicago community area.
- Key fields:
  - `community_area_number`
  - `community_area_name`
  - Cleaned numeric indicator fields in snake_case.
- Cleaning actions reflected:
  - standardized column names
  - numeric coercion
  - replacement of `.` placeholders with missing values
  - standardized community names, including `O'HARE`

### `data/interim/violence_records_clean.csv`
- Unit of observation: one gun violence victim record within the final study window.
- Key fields:
  - `case_number`
  - `date`
  - `year`, `month`, `day_of_week`, `hour`
  - `community_area_name`
  - `victimization_primary`, `incident_primary`, `gunshot_injury_i`
  - `age`, `sex`, `race`
  - `is_homicide_victim`
  - `is_nonfatal_shooting_victim`
  - `is_gun_violence_victim`
- Notes:
  - Contains only records that contribute to the project’s homicide or nonfatal-shooting counts.
  - Direct identifier columns are removed.
  - `MONTCLARE` is standardized to `MONTCLAIRE`.

## Processed datasets

### `data/processed/community_year_panel.csv`
- Unit of observation: one community area by year.
- Row count: 462 (`77 communities x 6 years`).
- Key fields:
  - `community_area_number`
  - `community_area_name`
  - `year`
  - `homicide_victims`
  - `nonfatal_shooting_victims`
  - `total_gun_violence_victims`
- Notes:
  - Built by aggregating cleaned violence records and then zero-filling the full community-year panel.
  - Preserves communities with no observed incidents, including `EDISON PARK`.

### `data/processed/community_level_analysis.csv`
- Unit of observation: one community area.
- Row count: 77.
- Key fields:
  - `community_area_number`
  - `community_area_name`
  - `mean_annual_homicide_victims`
  - `mean_annual_nonfatal_shooting_victims`
  - `mean_annual_total_victims`
  - all cleaned public-health indicator columns from the health dataset
- Intended use:
  - descriptive indicator comparisons
  - correlation analysis
  - the final lightweight regression model

## Results files

### Tables
- `results/tables/raw_quality_metrics.csv`: numeric summary of raw-data dimensions and detected quality issues.
- `results/tables/raw_quality_findings.json`: machine-readable list of the main quality issues flagged by the profiling step.
- `results/tables/integration_checks.csv`: confirmation of community coverage, year coverage, panel size, and Edison Park zero-count preservation.
- `results/tables/correlations.csv`: Pearson correlations between selected indicators and `mean_annual_total_victims`.
- `results/tables/top_communities.csv`: top 10 community areas ranked by mean annual total victims.

### Models
- `results/models/linear_model_metrics.json`: regression metrics, coefficients, and p-values.
- `results/models/linear_model_summary.txt`: full statsmodels regression summary table.

### Figures
- `results/figures/annual_totals.png`: citywide yearly homicide, nonfatal shooting, and total gun violence victim counts.
- `results/figures/top_10_communities.png`: top 10 communities by mean annual total victims.
- `results/figures/indicator_relationships.png`: scatterplots with fitted lines for poverty, unemployment, and per-capita income.
