# Milestone 2 Project Plan

## Project title
Public health indicators and gun violence victimization across Chicago community areas

## 1 Overview
This project studies how community level public health and socioeconomic conditions relate to gun violence outcomes across the 77 Chicago community areas. We will integrate a community area dataset of selected public health indicators with victim level records of homicides and non fatal shootings. Our goal is to quantify associations and communicate results clearly while avoiding causal claims.

Planned approach
1 Clean both datasets, document columns, and record assumptions
2 Aggregate victimizations into community area by year outcomes for homicide victims, non fatal shooting victims, and combined gun violence victims
3 Standardize community area keys and join yearly outcomes to community level indicators
4 Conduct exploratory analysis and interpretable modeling
5 Deliver a short report and visuals with an ethics aware discussion

## 2 Team
Vivian Lin is Member A and will lead ingestion, cleaning, integration, and baseline modeling.
Yoyo Lin is Member B and will lead exploratory analysis, visualization, and writing.
Both members will co own research questions, review pull requests, and ensure the repository is reproducible.

## 3 Research questions
Primary question
1 Which community level public health and socioeconomic indicators are most strongly associated with higher gun violence victimization burden across Chicago community areas

Secondary questions
2 How does gun violence burden vary across community areas and how stable are high burden areas over time
3 Are poverty, unemployment, education, and income indicators associated with higher violence burden after accounting for other indicators
4 Do aggregated victim demographics such as age, sex, and race distributions differ across areas with different public health profiles

## 4 Data sources
Dataset A Public Health Statistics selected public health indicators by Chicago community area historical is hosted on the City of Chicago Data Portal.
Dataset B Violence Reduction victims of homicides and non fatal shootings is hosted on the City of Chicago Data Portal.
Dataset A dataset id iqnk 2tcu
Dataset B dataset id gumc mgzr

## 5 Datasets and integration plan

### Dataset A Selected public health indicators by community area
Level of observation
One row per community area

What it contains
Indicators that include natality, mortality, infectious disease, lead screening, and socioeconomic measures such as poverty, crowded housing, education, income, and unemployment.

Keys for integration
Community area number and community area name

Important limitation
The dataset is described as historical and may represent multi year summary indicators. We will document units and time windows from official metadata and treat indicators as area characteristics when annual alignment is not possible.

### Dataset B Victims of homicides and non fatal shootings
Level of observation
One row per victimization event. A person can appear multiple times if victimized multiple times.

Time coverage
Homicide victimizations span 1991 to present. Non fatal shooting victimizations begin in 2010 in the public dataset.

Keys for integration
Community area, date, and demographics such as age, sex, and race

Privacy plan
We will drop victim name and any other direct identifier fields on ingest and publish only aggregated results.

### Integration steps
1 Normalize community area names in both datasets
2 Build a crosswalk from community area number to normalized name using dataset A
3 Aggregate dataset B into community area by year counts for homicide, non fatal shooting, and total
4 Join aggregated outcomes to dataset A using normalized community area name
5 Validate that the final panel covers all 77 areas and preserves totals

## 6 Analysis plan and methods

Data quality checks
1 Missingness and type validation
2 Outlier checks for age and date ranges
3 Basic consistency checks for duplicates in ids where relevant

Exploratory analysis
1 Citywide yearly trends for homicide and non fatal shooting victims
2 Community area rankings by multi year average burden
3 Correlation views between indicators and outcomes with careful interpretation

Modeling plan
1 Regression on transformed counts such as log of total victims plus one
2 Alternative count models if covered in the course
3 Classification of high burden area years using cross validation and clear metrics

Communication plan
1 Figures with captions that define measures and limits
2 Narrative that emphasizes association rather than causation
3 Ethics section on privacy, bias, and potential misuse

## 7 Timeline and task plan
Milestone 2 is due March 8 2026. We plan eight additional weeks of project work after submission.

March 4 to March 8
1 Finalize ProjectPlan.md and repository structure
2 Add raw datasets and a short data description
3 Create a release that follows the assignment instructions
Owners Vivian Lin and Yoyo Lin

Week 1 March 9 to March 15
1 Ingestion scripts and identifier removal
2 First data dictionary
Owner Vivian Lin leads, Yoyo Lin reviews

Week 2 March 16 to March 22
1 Crosswalk and name normalization
2 Area year aggregation and integrated panel export
Owner Vivian Lin leads, Yoyo Lin reviews

Week 3 March 23 to March 29
1 Join validation and descriptive figures
2 Community area ranking summaries
Owner Yoyo Lin leads, Vivian Lin reviews

Week 4 March 30 to April 5
1 Trend analysis and association analysis
2 Update questions and plan if needed
Owners Vivian Lin and Yoyo Lin

Week 5 April 6 to April 12
1 Baseline models and evaluation
2 Sensitivity checks such as excluding partial year 2026 or focusing on 2010 onward
Owner Vivian Lin leads, Yoyo Lin reviews

Week 6 April 13 to April 19
1 Improve visuals and write methods and results drafts
Owner Yoyo Lin leads, Vivian Lin reviews

Week 7 April 20 to April 26
1 Reproducibility polish and documentation
2 Draft final report and presentation
Owners Vivian Lin and Yoyo Lin

Week 8 April 27 to May 3
1 Final checks, final figures, and final narrative edits
2 Final release and submission materials per course instructions
Owners Vivian Lin and Yoyo Lin

## 8 Constraints and limitations
1 Temporal alignment may limit year by year interpretation if indicators are multi year summaries
2 Counts versus rates: without population denominators, counts can reflect community size
3 Measurement and refresh changes may affect recent records
4 Ecological inference risk: community level indicators cannot establish individual causation
5 Privacy and harm: we will publish only aggregated outputs and avoid stigmatizing language

## 9 Gaps and inputs needed
1 Confirm time window and units for each indicator in dataset A
2 Decide whether to add population denominators for per capita rates
3 Decide whether to add community area boundaries for mapping and confirm licensing
4 Decide how to handle year 2026 if incomplete
5 Confirm later course deliverables and required release points

## 10 Reproducibility plan and repository organization
Planned folders
1 data_raw for original files
2 data_processed for cleaned and integrated outputs
3 src for cleaning and aggregation scripts
4 notebooks for analysis
5 docs for data dictionary and notes
6 assets for exported figures

We will keep assumptions in docs and in code comments and ensure the pipeline can be run from raw data to final outputs.