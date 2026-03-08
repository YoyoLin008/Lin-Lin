# Milestone 2 Project Plan

## Project title
Public health indicators and gun violence victimization across Chicago community areas

## Overview
This project examines how community level public health and socioeconomic conditions relate to gun violence outcomes across Chicago community areas. We will integrate a community area dataset of selected public health indicators with victim level records of homicide and nonfatal shooting victimizations. Our goal is to identify patterns and associations that are directly supported by the data, and to communicate results responsibly. We will avoid causal claims and we will avoid language that stigmatizes communities.

Planned approach
1. Inspect and clean both datasets, then create a clear data dictionary.
2. Remove direct identifiers from the violence dataset before any analysis.
3. Aggregate violence records into community area by year outcomes.
4. Standardize community area keys and join yearly outcomes to community indicators.
5. Perform exploratory analysis and interpretable modeling.
6. Produce a short report and figures that emphasize limitations, uncertainty, and ethical use.

## Team
Vivian Lin, Member A  
Primary responsibilities:
* Build ingestion and cleaning scripts.
* Create community area standardization rules and a mapping table for name inconsistencies.
* Aggregate victimizations into community area by year outcomes.
* Build baseline models and document evaluation results.
* Produce the final integrated dataset in processed form.

Yoyo Lin, Member B  
Primary responsibilities:
* Lead exploratory analysis and visualization.
* Create figure exports and write figure captions.
* Draft the narrative for methods, results, constraints, and ethics.
* Perform quality checks on outputs and confirm that privacy rules are followed.

Shared responsibilities
* Finalize research questions and scope decisions.
* Review each other’s work through pull requests.
* Ensure the repository can run from raw data to final outputs.
* Prepare the project plan release and submit the release link.

## Research questions
Primary question
1. Which community level public health and socioeconomic indicators are most strongly associated with higher gun violence victimization burden across Chicago community areas?

Secondary questions
* How does gun violence burden vary across community areas, and how stable are high burden areas over time?
* Are poverty, unemployment, education, and income indicators associated with higher violence burden after considering other indicators in the dataset?
* Do aggregated victim demographics such as age, sex, and race distributions differ across community areas with different indicator profiles?
* Can an explainable model identify community area years that fall into a high burden group using a small set of indicators?

Key outcomes we will create
1. Homicide victim count by community area by year.
2. Nonfatal shooting victim count by community area by year.
3. Total gun violence victim count by community area by year.
4. Optional aggregated demographic summaries by community area by year, reported only at safe aggregation levels.

## Datasets and sources
We use two datasets from the City of Chicago Data Portal. We are including the source links here because they directly support transparency, provenance, and reproducibility.

Dataset A  
Name  
Public Health Statistics, Selected public health indicators by Chicago community area, historical.  

Source page  
https://data.cityofchicago.org/Health-Human-Services/Public-Health-Statistics-Selected-public-health-in/iqnk-2tcu/about_data  

Level of observation  
One row per community area.

What it contains  
Selected public health and socioeconomic indicators by community area. This includes measures such as poverty, unemployment, education, and income, plus multiple health related indicators. The dataset is labeled historical, so indicators may reflect a specific time window or summary period rather than annual values. We will confirm indicator units and time windows using the dataset metadata and document them in our data dictionary.

Key fields for integration  
* Community area number.
* Community area name.

Dataset B  
Name  
Violence Reduction, Victims of Homicides and Nonfatal Shootings.  

Source page  
https://data.cityofchicago.org/Public-Safety/Violence-Reduction-Victims-of-Homicides-and-Non-Fa/gumc-mgzr/about_data  

Level of observation  
One row per victimization record.

What it contains  
Victim level records for homicide and nonfatal shooting victimizations, including event date, community area, and victim demographics such as age, sex, and race. The dataset includes fields that can contain direct identifiers for some homicide records. We will remove direct identifiers during ingestion and we will not publish any row level data.

Key fields for integration  
* Date field that can be used to derive year.
* Community area field.
* Victimization type field.

## Integration plan
Shared identifier  
Both datasets reference Chicago community areas, so we will integrate through community area.

Integration steps
1. Standardize community area names in both datasets using consistent casing and whitespace rules.
2. Create a crosswalk from community area number to standardized community area name using Dataset A.
3. Identify name mismatches between datasets and fix them using a small mapping table stored in the repository with short documentation of each change.
4. Parse the date field in Dataset B, then derive a year field.
5. Aggregate Dataset B into community area by year outcomes.
   
   Homicide victim count.
   Nonfatal shooting victim count.
   Total victim count.
6. Join the aggregated violence outcomes to Dataset A using standardized community area name, and retain community area number as a reference.
7. Validate the join.
   
   Confirm the final table includes all community areas.
   Confirm totals match the pre join aggregates.
   Confirm each community area by year appears once.

## Kaggle clause response
We are not using Kaggle datasets. Both datasets come directly from the City of Chicago Data Portal, with clear dataset pages and metadata. This supports traceability, ethical use, and reproducibility. In addition, they share a clear geographic key, Chicago community areas, which makes integration feasible.

## Analysis plan
Data wrangling and quality checks  
1. Create a data dictionary for both datasets, including variable meanings, units, and known missingness.
2. Run missingness profiling by year and by community area.
3. Check for out of range values in age, invalid dates, and inconsistent categories for sex, race, and victimization type.
4. Confirm that identifier columns with direct personal information are removed before analysis outputs are saved.

Exploratory analysis  
We will mix descriptive statistics with visuals to understand structure and risk.
* Citywide trend plots by year for homicide victims, nonfatal shooting victims, and total victims.
* Community area distributions and rankings using multi year averages.
* Scatter and correlation style summaries between indicators and violence outcomes, with careful interpretation.

Modeling plan  
We will prioritize interpretable models.
* Regression using a transformed count outcome such as log of total victims plus 1 to reduce skew.
* If covered in course topics, explore count models as a robustness check.
* Classification for high burden area years, evaluated with cross validation and reported using clear metrics such as precision, recall, and confusion matrix summaries.

Ethics and interpretation  
* We will avoid causal wording and will describe results as associations.
* We will avoid stigmatizing language about communities.
* We will publish only aggregated outputs and will suppress risky small cell counts when needed.

## Timeline
Milestone 2 due date is March 8, 2026. We plan roughly eight weeks of work after submission.

March 4, 2026 to March 8, 2026  
Milestone 2 tasks, owners Vivian Lin and Yoyo Lin
1. Finalize this project plan and repository structure.
2. Add raw data files and short dataset notes in the repository.
3. Create the project plan tag and release, then submit the release link.

Week 1, March 9, 2026 to March 15, 2026  
Owner Vivian Lin leads, Yoyo Lin reviews
1. Build ingestion scripts for both datasets.
2. Remove direct identifiers from Dataset B during ingestion.
3. Draft the first data dictionary.

Week 2, March 16, 2026 to March 22, 2026  
Owner Vivian Lin leads, Yoyo Lin reviews
1. Implement community area standardization and mapping table.
2. Parse date and create year field.
3. Produce community area by year aggregates for outcomes.

Week 3, March 23, 2026 to March 29, 2026  
Owner Yoyo Lin leads, Vivian Lin reviews
1. Join aggregated outcomes with community indicators.
2. Validate join quality and totals.
3. Produce initial descriptive figures and tables.

Week 4, March 30, 2026 to April 5, 2026  
Owners Vivian Lin and Yoyo Lin
1. Expand exploratory analysis, including stability of high burden areas over time.
2. Decide on the main analysis window for comparisons, such as focusing on overlapping years for homicide and nonfatal shootings.
3. Update documentation of key decisions and assumptions.

Week 5, April 6, 2026 to April 12, 2026  
Owner Vivian Lin leads, Yoyo Lin reviews
1. Build baseline models and evaluate performance.
2. Run sensitivity checks, such as excluding partial recent years if needed.
3. Document modeling choices and interpretability.

Week 6, April 13, 2026 to April 19, 2026  
Owner Yoyo Lin leads, Vivian Lin reviews
1. Improve visualization quality and draft the final figure set.
2. Draft methods and results text aligned with course expectations.
3. Draft constraints and ethics sections using evidence from the analysis.

Week 7, April 20, 2026 to April 26, 2026  
Owners Vivian Lin and Yoyo Lin
1. Reproducibility polish, including a clear run order from raw to processed outputs.
2. Prepare a report outline and a presentation outline, if required later.
3. Confirm file organization and update README.

Week 8, April 27, 2026 to May 3, 2026  
Owners Vivian Lin and Yoyo Lin
1. Final checks for privacy, clarity, and limitations.
2. Finalize deliverables and prepare final release notes based on course instructions available at that time.

## Constraints
1. Temporal alignment. Dataset A is historical and may not provide annual values. This limits year matched inference. We will document indicator time windows and treat indicators as area characteristics when annual alignment is not possible.
2. Counts versus rates. Without population denominators, counts can reflect community size. We may add a population dataset later if time allows and if it aligns to community areas with clear provenance.
3. Coverage differences. Nonfatal shooting data begins later than homicide data, which can limit comparisons across the full timeline.
4. Reporting and measurement bias. Changes in reporting practices and data refresh patterns can affect trends.
5. Ecological inference risk. Community level indicators cannot support individual level causal claims.
6. Privacy and harm risk. Victim level data must remain aggregated, and we must avoid outputs that could enable re identification.

## Gaps and needed input
* Confirm indicator definitions, units, and time windows for Dataset A using the portal metadata.
* Decide whether to add a population denominator dataset and confirm it can be matched to community areas.
* Confirm any later milestone requirements, then update the timeline after feedback.
* Decide whether mapping is required and, if so, locate community area boundary data with clear reuse terms.

## Repository and reproducibility plan
Planned folders
* data_raw for original files.
* data_processed for cleaned and integrated outputs.
* src for ingestion, cleaning, aggregation, and join scripts.
* notebooks for exploratory analysis and modeling.
* docs for data dictionary and assumptions.
* assets for exported figures.

We will keep assumptions explicit in docs and code comments. We will also ensure both members contribute through commits so individual contributions are visible in the commit history.
