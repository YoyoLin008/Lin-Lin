# Milestone 3 Status Report

## Project Overview
Our project, **Public health indicators and gun violence victimization across Chicago community areas**, examines how community-level public health and socioeconomic conditions relate to violence burden across Chicago community areas. The original project scope, timeline, research questions, and team responsibilities are documented in [ProjectPlan.md](ProjectPlan.md). For Milestone 3, our goal was to move beyond planning and assemble a working exploratory analysis that shows clear progress toward the final project.

The main project artifacts used at this stage are:
- [ProjectPlan.md](ProjectPlan.md), which records the Milestone 2 plan.
- [Datasets/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv](Datasets/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv), the public health source dataset.
- [Datasets/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv](Datasets/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv), the violence source dataset.
- [Datasets/merged.csv](Datasets/merged.csv), the merged dataset currently used for the shared analysis workflow.
- [Datasets/Combined.ipynb](Datasets/Combined.ipynb), the main notebook containing both the earlier exploratory work and the added community-indicator analysis.

## Progress on Planned Tasks
The Milestone 2 setup tasks are complete. We finalized the topic, clarified the research questions, saved the raw data files in the repository, and documented the intended workflow in [ProjectPlan.md](ProjectPlan.md). This provided a clear structure for the milestone work that followed.

The Week 1 ingestion and cleaning tasks are partially complete. We have working raw data files and a notebook-based data-preparation flow in [Datasets/Combined.ipynb](Datasets/Combined.ipynb). The notebook standardizes column names, parses date fields, and prepares the data for downstream analysis. In the merged-file analysis section, direct homicide victim name fields are dropped before aggregation. However, we still do not have a separate reusable ingestion script or a completed data dictionary, so those tasks remain open.

The Week 2 integration tasks are substantially complete in interim form. The public health and violence datasets were combined into [Datasets/merged.csv](Datasets/merged.csv), which is now the shared artifact used in the later analysis sections of the notebook. The current integrated analysis window is the shared `2005-2011` overlap used by the team for this milestone. This means the project now has a concrete combined artifact instead of only a proposed integration plan.

The Week 3 exploratory analysis tasks show the most visible progress. The top and middle sections of [Datasets/Combined.ipynb](Datasets/Combined.ipynb) preserve the broader exploratory work already completed by the team. These sections include incident trend plots, geospatial mapping, victim demographic summaries, temporal heatmaps, homicide summaries by community area and year, gun violence summaries, and aggregated demographic summaries at safe reporting levels. Together, these sections show that the project has moved beyond data merging and into actual descriptive analysis.

The later section of the notebook extends that work with a cleaner community-indicator analysis based on [Datasets/merged.csv](Datasets/merged.csv). In that section, the merged records are filtered to the shared `2005-2011` period, aggregated to community-level averages, and compared to selected socioeconomic indicators. The main comparison plot examines the relationship between average annual gun violence burden and three indicators: below-poverty level, unemployment, and per-capita income. A correlation summary is also reported at the end of the section.

The current descriptive results are useful for the project’s primary question. In the merged `2005-2011` analysis, `teen_birth_rate` has the strongest positive association with average annual gun violence burden at approximately `0.72`. `below_poverty_level` and `unemployment` are also positively associated at about `0.47`, while `per_capita_income` is negatively associated at about `-0.40`. These findings are being interpreted carefully as community-level associations rather than causal effects.

The Week 4 scope-refinement tasks are in progress. One important decision was to preserve the existing notebook structure rather than replace it with only one new analysis. This allows the notebook to show both the original exploratory sections and the newer indicator-focused extension. It also better reflects the actual division of work completed so far.

The Week 5 modeling tasks have not started yet. We have not yet built the regression or classification models described in the project plan, and we have not yet documented model evaluation results. This remains one of the most important next steps after the exploratory notebook is finalized.

The Week 6 writing and figure-polish tasks are partially complete. The notebook has clearer Markdown structure than before, and the figures now have more explicit titles and axis labels. This report is part of that same writing phase, since it documents progress, scope changes, and remaining work for the milestone review.

## Updated Timeline

| Time block | Planned task | Current status | Expected completion |
| --- | --- | --- | --- |
| March 4-March 8 | Finalize plan, organize repo, add raw data | Completed | Completed |
| March 9-March 15 | Build ingestion workflow and first data dictionary | Partially complete | April 7, 2026 |
| March 16-March 22 | Standardize fields, derive year, and integrate the datasets | Completed in interim form through [Datasets/merged.csv](Datasets/merged.csv) | Completed |
| March 23-March 29 | Validate merged data and create first descriptive figures | Completed in interim form through [Datasets/Combined.ipynb](Datasets/Combined.ipynb) | Completed |
| March 30-April 5 | Expand exploratory analysis and refine scope | In progress | April 5, 2026 |
| April 6-April 12 | Build baseline models and sensitivity checks | Not started | April 12, 2026 |
| April 13-April 19 | Improve figures and draft methods/results text | In progress | April 19, 2026 |
| April 20-May 3 | Reproducibility polish, release preparation, and final checks | Not started | May 3, 2026 |

## Changes to the Project Plan
The most important practical change is that the notebook now reflects two layers of work rather than one narrow workflow. Earlier in the project, there was a risk of collapsing the notebook into only the newest indicator-analysis section. Instead, we preserved the original exploratory sections and added the new correlation-based analysis after them. This makes the notebook a better record of the project’s actual progress and ensures that earlier work is still visible.

Another important change is that the current integrated analysis is centered on the shared `2005-2011` overlap represented in [Datasets/merged.csv](Datasets/merged.csv). This is narrower than a full raw-data workflow, but it is the most defensible scope for the current merged artifact and therefore the most appropriate basis for Milestone 3.

We also made presentational changes to the notebook itself. Some earlier headings contained placeholder text, and several figures needed clearer labeling. We revised the Markdown and plot labels so the notebook reads more like a coherent project artifact rather than a collection of disconnected exploratory cells.

We did not receive a formal Milestone 2 feedback memo requiring direct revisions to the written plan. However, based on our own review of the project and notebook, we simplified the presentation, clarified the overlap window we are actually using, and made the organization of the work more explicit.

## Challenges and How We Addressed Them
One challenge was notebook organization. The existing notebook contained useful analysis, but some sections were difficult to follow because of placeholder text or limited explanation. We addressed this by keeping the structure intact while improving the Markdown and figure labels so the notebook better explains what each section is doing.

A second challenge was balancing cleanup with preservation. A cleaner notebook was desirable, but removing too much would have hidden work already completed by the team. We resolved this by preserving the existing exploratory sections and then appending the newer indicator-focused analysis after them.

A third challenge was dependency setup. Some packages used by the geospatial and seaborn-based notebook cells were missing from the current environment. We addressed this by installing the missing packages directly into the existing Python environment so the notebook can run without creating a separate virtual environment.

A fourth challenge was privacy and responsible reporting. The merged file includes direct homicide victim name fields that should not remain in the active analysis workflow. In the merged-file section, we explicitly drop those columns before aggregating and plotting the data.

Finally, coordination has been a practical challenge. Because both team members contribute to the same notebook and report, there is a risk that one person’s visible edits can overshadow the other’s work. Our current approach is to preserve both the earlier exploratory work and the later added section in the same notebook, while also documenting both members’ contributions more evenly in this report.

## Team Member Contributions
**Vivian Lin** contributed substantially to the data preparation and exploratory notebook foundation for this milestone. Her work is reflected in the original integration-oriented and descriptive sections of [Datasets/Combined.ipynb](Datasets/Combined.ipynb), including the merge-related workflow, incident trend plots, homicide summaries, demographic summaries, and the broader exploratory structure built from the combined data.

**Yoyo Lin** contributed substantially to the later notebook refinement and the added community-indicator analysis. Her work is reflected in the clearer Markdown organization, the cleanup of plot labels and explanations, the appended merged-file indicator analysis, and the drafting and revision of this status report.

Both members contributed to scope decisions, milestone direction, and the overall progress of the project.
