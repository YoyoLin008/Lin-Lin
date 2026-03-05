# Milestone 2 Project Plan

## Project title
Public health indicators and gun violence victimization across Chicago community areas

## Overview
This project examines how community level public health and socioeconomic conditions relate to gun violence outcomes across Chicago. We will integrate a community area dataset of selected public health indicators with individual level victimization records for homicides and nonfatal shootings. Our goal is to measure and describe associations, not to claim causality, and to communicate findings in a way that is careful about ethics and community harm.

Planned approach
1. Clean both datasets, verify column meanings, and document assumptions in a data dictionary.
2. Remove direct identifiers and keep only fields required for analysis.
3. Aggregate victimization records into community area by year outcomes, including homicide victims, nonfatal shooting victims, and combined gun violence victims.
4. Standardize community area keys and join yearly outcomes to community level indicators.
5. Conduct exploratory analysis and build interpretable models to identify which indicators best explain variation in violence burden.
6. Produce clear tables and figures, plus a short written narrative that highlights uncertainty, limitations, and responsible interpretation.

## Team
Vivian Lin, Member A
Responsibilities
1. Data ingestion scripts and cleaning pipeline.
2. Community area standardization and crosswalk rules.
3. Aggregation to community area by year outcomes.
4. Baseline modeling and evaluation.
5. Integration of final processed datasets into the repository.

Yoyo Lin, Member B
Responsibilities
1. Exploratory analysis and visualization.
2. Figure production and documentation of visual choices.
3. Writing the methods, results, and limitations sections for the final deliverables.
4. Review of ethics and privacy decisions, including what we do and do not publish.

Shared responsibilities
1. Final research questions and scope decisions.
2. Code review through pull requests.
3. Reproducibility checks, including running the pipeline from raw to processed outputs.
4. Final release notes and submission steps.

## Research questions
Primary question
1. Which community level public health and socioeconomic indicators are most strongly associated with higher gun violence victimization burden across Chicago community areas?

Secondary questions
2. How does gun violence burden vary across community areas, and how stable are high burden areas over time?
3. Are poverty, unemployment, education, and income indicators associated with higher violence burden after accounting for other indicators in the dataset?
4. Do aggregated victim demographics, such as age, sex, and race distributions, differ across community areas with different public health profiles?
5. Can an explainable model identify community area years in the highest burden group using a small set of indicators?

Operational definitions and outcomes we will create
1. Homicide victim count, community area by year.
2. Nonfatal shooting victim count, community area by year.
3. Total gun violence victim count, community area by year.
4. Optional demographic summaries, community area by year, such as median age and category distributions, reported only in aggregated form.

## Datasets
We will use two non Kaggle datasets hosted on the City of Chicago Data Portal.

Dataset A
Title
Public Health Statistics, Selected public health indicators by Chicago community area, historical.

What it contains
A selection of public health indicators by Chicago community area. Indicators include rates, percents, or other measures related to natality, mortality, infectious disease, lead poisoning, and economic status. The dataset description also notes it is historical and intended for earlier time periods rather than continuously updated recent years. :contentReference[oaicite:0]{index=0}

Level of observation
One row per community area.

Key fields for integration
Community area number and community area name.

Expected integration use
We will treat these indicators as community area characteristics and join them to violence outcomes after we aggregate violence records to community area level.

Dataset B
Title
Violence Reduction, Victims of Homicides and Nonfatal Shootings.

What it contains
Individual level victimization records for homicide and nonfatal shootings, including homicide records from 1991 to the present and nonfatal shooting records from 2010 to the present in the public dataset. :contentReference[oaicite:1]{index=1}

Level of observation
One row per victimization record. A person can appear more than once if victimized multiple times across events.

Key fields for integration
Date, community area, victimization type, and basic demographics such as age, sex, and race.

Privacy handling
The dataset includes fields that can contain direct identifiers for homicide records. We will remove direct identifiers during ingestion and will not publish any row level data or small cell counts that risk re identification.

## Integration plan
Shared identifier
Both datasets are organized around Chicago community areas. Dataset A provides community area number and name. Dataset B includes community area values that we will standardize to match Dataset A.

Steps
1. Normalize community area names in both datasets using consistent casing and whitespace rules.
2. Build a crosswalk using Dataset A from community area number to normalized community area name.
3. Identify and fix name mismatches by creating a small mapping table stored in the repository, with each change documented.
4. Parse dates in Dataset B and extract year.
5. Aggregate Dataset B into community area by year victim counts, separated by homicide and nonfatal shooting.
6. Join aggregated outcomes to Dataset A using the normalized community area name and preserve community area number as a reference field.
7. Validate joins by checking that the final dataset contains all community areas, that totals match pre join aggregates, and that no community area is duplicated after joining.

## Kaggle clause response
We are not using Kaggle datasets. Our datasets come directly from the City of Chicago Data Portal, which provides a clearer path for provenance, licensing context, and reproducibility than many Kaggle mirrors. :contentReference[oaicite:2]{index=2}

Why these datasets were selected
1. They share a strong geographic key, Chicago community areas, which makes integration feasible and meaningful.
2. Dataset B provides long time coverage for homicide and meaningful coverage for nonfatal shootings, enabling trends and stability analysis. :contentReference[oaicite:3]{index=3}
3. Dataset A provides community level public health and socioeconomic indicators that support hypothesis driven interpretation rather than only descriptive violence counts. :contentReference[oaicite:4]{index=4}

Alternative sources considered, and why they were not selected as core datasets
1. Kaggle mirrors of Chicago public health or violence data were considered but rejected due to unclear provenance, duplicated cleaning, and unclear licensing context compared with pulling directly from the Chicago portal.
2. National sources such as CDC or FBI summaries were considered, but they often do not align cleanly to Chicago community areas, which would block integration without a complex geographic translation step.
3. Chicago Health Atlas was noted in dataset documentation as a source for more recent health information, but the project scope emphasizes data wrangling and integration using our selected portal datasets, and we will keep the project feasible within the remaining semester. :contentReference[oaicite:5]{index=5}

## Analysis plan
Data quality and wrangling
1. Column auditing and data dictionary creation for both datasets.
2. Missingness profiling, including which fields are missing by year and by community area.
3. Standardization for community area fields and date fields.
4. Duplicate checks and consistency checks for victimization type categories.

Exploratory analysis
1. Citywide trend plots by year for homicide victims, nonfatal shooting victims, and total victims.
2. Community area comparisons using multi year averages and distributions.
3. Indicator comparisons using correlation style summaries and simple association plots, with careful language about what is and is not supported by the data.

Modeling plan, interpretable focus
1. Regression using a transformed count outcome, such as natural log of total victims plus one, to reduce skew.
2. If appropriate for the course content, count models will be explored as a sensitivity check.
3. Classification for whether a community area year is in a high burden group, evaluated with cross validation and reported with clear metrics such as precision, recall, and confusion matrix summaries.

Ethics and interpretation
1. We will avoid framing that stigmatizes communities.
2. We will not publish row level records.
3. We will avoid causal language and will highlight structural and measurement limitations.

## Timeline and task plan
Milestone 2 due date
March 8, 2026.

We assume about eight weeks of work after Milestone 2, ending in early May.

March 4, 2026 to March 8, 2026
Task 1. Finalize this project plan, repository structure, and initial documentation.
Task 2. Add raw data files to a data folder and include a short README describing each dataset.
Task 3. Create a release for the project plan submission.
Owner. Vivian Lin and Yoyo Lin.

Week 1, March 9, 2026 to March 15, 2026
Task 1. Build ingestion scripts for both datasets.
Task 2. Remove direct identifiers during ingestion and document what was removed.
Task 3. Create a first version of the data dictionary.
Owner. Vivian Lin leads, Yoyo Lin reviews.

Week 2, March 16, 2026 to March 22, 2026
Task 1. Implement community area normalization rules and crosswalk mapping table.
Task 2. Parse dates and create year field in the violence dataset.
Task 3. Produce aggregated victim counts by community area and year.
Owner. Vivian Lin leads, Yoyo Lin reviews.

Week 3, March 23, 2026 to March 29, 2026
Task 1. Join aggregated violence outcomes with community indicators.
Task 2. Validate join quality and totals.
Task 3. Produce initial descriptive figures and community area summaries.
Owner. Yoyo Lin leads, Vivian Lin reviews.

Week 4, March 30, 2026 to April 5, 2026
Task 1. Expand exploratory analysis, including stability of high burden areas over time.
Task 2. Decide on the main analysis time window, such as focusing on years with both homicide and nonfatal data.
Task 3. Update documentation of key decisions.
Owner. Vivian Lin and Yoyo Lin.

Week 5, April 6, 2026 to April 12, 2026
Task 1. Build baseline models for association analysis.
Task 2. Evaluate models and document interpretability tradeoffs.
Task 3. Perform sensitivity checks, such as excluding partial recent years if needed.
Owner. Vivian Lin leads, Yoyo Lin reviews.

Week 6, April 13, 2026 to April 19, 2026
Task 1. Improve visualizations and create final figure set drafts.
Task 2. Draft methods and results text, aligned with course expectations.
Owner. Yoyo Lin leads, Vivian Lin reviews.

Week 7, April 20, 2026 to April 26, 2026
Task 1. Reproducibility polish, including one command pipeline from raw to processed outputs.
Task 2. Draft final report and presentation outline, plus captions and figure references.
Owner. Vivian Lin and Yoyo Lin.

Week 8, April 27, 2026 to May 3, 2026
Task 1. Final checks for privacy, limitations, and clarity.
Task 2. Finalize deliverables, write release notes, and submit per course instructions.
Owner. Vivian Lin and Yoyo Lin.

## Constraints and limitations
1. Temporal alignment. Dataset A is historical and may not provide year specific indicator values, which can limit time matched causal interpretation. We will document indicator time windows from official metadata and treat indicators as area characteristics when annual alignment is not possible. :contentReference[oaicite:6]{index=6}
2. Counts versus rates. Without population denominators, counts can reflect community size. We may add a population dataset later if time allows, but the project remains answerable with counts and careful interpretation.
3. Coverage differences. Nonfatal shooting records begin later than homicide records, which may require focusing some analyses on the overlapping time period. :contentReference[oaicite:7]{index=7}
4. Reporting bias and system changes. Changes in reporting practices and data refresh patterns can affect trends.
5. Ecological inference risk. Community level indicators cannot establish individual level causation.
6. Privacy and harm. Victim level records require strict aggregation, suppression of risky small counts, and careful narrative framing.

## Gaps and input needed
1. Confirm indicator definitions, units, and time windows for Dataset A using portal documentation and metadata assets. :contentReference[oaicite:8]{index=8}
2. Decide whether to include population denominators for rates, and if so, select a non Kaggle population source aligned to community areas.
3. Decide whether to include mapping, and if so, locate community area boundary files with clear reuse terms.
4. Confirm what Milestone 3 and Milestone 4 expect in this course, then revise the timeline and deliverables accordingly after feedback.

## Data source pages
The datasets are hosted on the City of Chicago Data Portal. Use the portal search with the exact titles below.

Dataset A title to search
Public Health Statistics, Selected public health indicators by Chicago community area, historical. :contentReference[oaicite:9]{index=9}

Dataset B title to search
Violence Reduction, Victims of Homicides and Nonfatal Shootings. :contentReference[oaicite:10]{index=10}

Chicago Data Portal home page
https://data.cityofchicago.org

## Submission steps
1. Add and commit ProjectPlan.md and any related artifacts.
2. Push to GitHub.
3. Create the required project plan tag and release using the exact naming in the assignment instructions.
4. Submit the release URL to Canvas.