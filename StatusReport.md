# Milestone 3 Status Report

## Project overview
Our project, **Public health indicators and gun violence victimization across Chicago community areas**, studies how community-level public health and socioeconomic conditions relate to gun violence burden across Chicago. The original scope, timeline, and task breakdown are documented in [ProjectPlan.md](ProjectPlan.md). For Milestone 3, our goal was to turn that plan into a usable exploratory notebook and document our actual progress through repository artifacts.

The main repository artifacts are:
- [ProjectPlan.md](ProjectPlan.md), which contains our Milestone 2 plan.
- [Datasets/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv](Datasets/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv), the public health source dataset.
- [Datasets/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv](Datasets/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv), the violence source dataset.
- [Datasets/merged.csv](Datasets/merged.csv), the merged dataset produced for the current analysis.
- [Datasets/Combined.ipynb](Datasets/Combined.ipynb), the notebook that now contains both the original exploratory work and the added indicator-correlation analysis.

## Update on planned tasks and current artifacts
The Milestone 2 setup tasks are complete. We finalized the topic, defined the research questions, saved the raw datasets in the repository, and documented the intended workflow in [ProjectPlan.md](ProjectPlan.md). These planning tasks gave us the structure needed to begin the actual exploratory analysis in Milestone 3.

The Week 1 ingestion and cleaning tasks are partially complete. We have working raw data files in the repository and a notebook-based cleaning flow in [Datasets/Combined.ipynb](Datasets/Combined.ipynb). The notebook includes helper functions for standardizing names, parsing dates, and preparing the data for analysis. However, we still do not have a separate production-style ingestion script or a finished data dictionary, so those parts remain in progress.

The Week 2 integration tasks are substantially complete in interim form. The public health and violence datasets were successfully combined into [Datasets/merged.csv](Datasets/merged.csv). The current milestone analysis is centered on the shared `2005-2010` overlap represented in that file.

The Week 3 exploratory analysis tasks are where most of the current milestone work is visible. The top portion of [Datasets/Combined.ipynb](Datasets/Combined.ipynb) preserves the earlier analysis sections already built by the team. These include:
- overall incident trend plots and crime maps,
- demographic summaries for victims by age, sex, and race,
- temporal heatmaps,
- homicide counts by community area and year,
- preliminary gun violence summaries,
- and aggregated demographic summaries at safe levels.

Those sections now have clearer Markdown headings and more readable labels so the notebook is easier to follow. For example, several plots now explicitly label the x-axis, y-axis, and titles rather than relying on default values or leaving sections with placeholder text.

The later part of the notebook now includes an added community-indicator analysis that extends the original work instead of replacing it. That final section loads [Datasets/merged.csv](Datasets/merged.csv), removes direct identifier columns from the working dataframe, keeps the shared `2005-2010` period, aggregates to one row per community area with average annual gun violence burden, and compares that burden against three selected socioeconomic indicators: below-poverty level, unemployment, and per-capita income. It also prints the matching correlation summary for those relationships.

The current descriptive results from that added section are aligned with our main research question. In the merged `2005-2010` analysis, `teen_birth_rate` has the strongest positive association with average annual gun violence burden at about `0.72`. `below_poverty_level` and `unemployment` are also positively associated at about `0.47` each, while `per_capita_income` is negatively associated at about `-0.40`. We treat these as community-level descriptive associations, not causal findings.

The Week 4 scope-refinement tasks are also underway. One important decision we made was to keep the restored notebook structure rather than throwing away earlier exploratory work. Instead of replacing the original notebook with only one analysis, we preserved the earlier sections and added the newer indicator-focused analysis after them. This better reflects the true state of the team’s progress and makes both members’ work visible in one document.

The Week 5 modeling tasks have not started yet. We have not yet built the regression or classification models described in the project plan, and that work remains a major next step after the exploratory notebook and milestone report are stabilized.

The Week 6 writing and figure-polish tasks are partially complete. The notebook now reads more clearly, and the later project stages such as final reproducibility polish, release preparation, and Canvas submission are still pending.

## Updated timeline

| Time block | Planned task | Current status | Expected completion |
| --- | --- | --- | --- |
| March 4-March 8 | Finalize plan, organize repo, add raw data | Completed | Completed |
| March 9-March 15 | Build ingestion workflow and first data dictionary | Partially complete | April 7, 2026 |
| March 16-March 22 | Standardize fields, derive year, and integrate the datasets | Complete in interim form through [Datasets/merged.csv](Datasets/merged.csv) and notebook workflow | Completed |
| March 23-March 29 | Validate the merged data and create first descriptive figures | Complete in interim form through [Datasets/Combined.ipynb](Datasets/Combined.ipynb) | Completed |
| March 30-April 5 | Expand exploratory analysis and refine scope | In progress | April 5, 2026 |
| April 6-April 12 | Build baseline models and sensitivity checks | Not started | April 12, 2026 |
| April 13-April 19 | Improve figures and draft methods/results text | In progress | April 19, 2026 |
| April 20-May 3 | Reproducibility polish, release prep, and final checks | Not started | May 3, 2026 |

## Changes to the project plan
The biggest practical change is that the current milestone notebook now reflects two layers of work rather than a single rewritten flow. Earlier in this turn we considered reducing the notebook to only the final correlation analysis, but that would have hidden part of the existing exploratory work. We corrected that and instead preserved the original notebook sections, cleaned their Markdown, and appended the additional indicator-correlation section at the end. This better matches the reality of the team’s progress.

Another important change is that our current analysis scope is tied to the shared `2005-2010` overlap represented in [Datasets/merged.csv](Datasets/merged.csv). This is narrower than a full raw-data analysis, but it is the most consistent scope for the current merged artifact and for the current milestone notebook.

We also made a presentational change to the notebook itself. Several earlier section headings contained placeholder text or minimal explanation. Those sections are now rewritten with clearer Markdown so reviewers can understand what each block of code is doing.

We did not receive a formal Milestone 2 feedback memo that required a direct response section. However, based on our own review, we improved the notebook structure, preserved both members’ visible work, and added clearer documentation.

## Challenges and how we addressed them
One challenge was notebook organization. The existing notebook contained useful exploratory content, but some of the section headings still had placeholder text and some visualizations were difficult to interpret quickly. We addressed this by keeping the existing structure, improving the Markdown around it, and adding clearer axis labels and titles where needed.

A second challenge was balancing preservation with cleanup. We initially risked oversimplifying the notebook by collapsing it into only the newest analysis section. That would have made the notebook cleaner, but it would also have hidden earlier work already completed by the team. We resolved that by restoring the original notebook structure and placing the new community-indicator analysis after the existing sections instead of replacing them.

A third challenge was dependency setup. Some of the libraries used by the earlier geospatial and seaborn-based cells were not installed in the current environment. We addressed this by installing the missing packages directly into the existing Python environment so the notebook can run without setting up a separate virtual environment.

A fourth challenge was making sure the merged analysis remained privacy-aware. The merged dataset contains homicide victim name fields that should not be carried into the analytic workflow. In the added merged-file section, we explicitly drop those identifier columns before aggregation and plotting.

Finally, coordination itself has been a challenge. Because both members contribute to the same notebook and report, it is easy for the final artifact to overemphasize one person’s visible edits. Our solution was to keep both the earlier exploratory work and the newly added section in the same notebook, and to write contribution summaries that more evenly reflect both members’ work.

## Team member contributions
**Vivian Lin** contributed substantially to the data preparation and exploratory notebook foundation for this milestone. Her work is reflected in the original integration-oriented and exploratory sections of [Datasets/Combined.ipynb](Datasets/Combined.ipynb), including the merge workflow, the early descriptive plots, the homicide summaries, and the broader exploratory setup based on the combined data sources.

**Yoyo Lin** contributed substantially to the notebook refinement, final presentation, and added indicator-analysis section. Her work is reflected in the improved Markdown organization throughout the notebook, the cleanup of plot labels and section explanations, the appended community-indicator correlation analysis based on [Datasets/merged.csv](Datasets/merged.csv), and the drafting of this milestone status report.

Both members contributed to the overall project direction, scope decisions, and milestone planning. For the final Milestone 3 submission, each member should commit her own contribution summary directly so that the Git history clearly shows individual participation, as required by the assignment.
