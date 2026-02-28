# Project Plan (Milestone 2)

## Overview
Our project goal is to build an end-to-end, reproducible data workflow that explains and predicts wine quality using physicochemical measurements, while comparing how these relationships differ between red and white wine. We will use the UCI Wine Quality datasets (red and white) to (1) integrate multiple raw sources into a unified analytical table, (2) conduct exploratory analysis to understand distributions, correlations, and quality patterns, and (3) develop interpretable and predictive models that can estimate quality scores from measurable chemical properties.

Planned approach:
1. **Ingest & validate** both datasets, document schema and any assumptions.
2. **Integrate** datasets by adding a `wine_type` variable and concatenating into one “combined” dataset while preserving original sources.
3. **Wrangle**: handle data types, check missingness, outliers, and scaling needs; create derived features if justified (ex:  total acidity proxies).
4. **EDA**: compare red vs white distributions; analyze relationships between features and quality; identify multicollinearity.
5. **Modeling**: train baseline models (ex:  linear / logistic baselines) and improved models (ex:  tree-based methods). Evaluate with clear metrics and robust validation.
6. **Interpretation & communication**: report feature importance and meaningful comparisons between red and white; provide a reproducible pipeline and clear documentation.

Deliverables include a cleaned integrated dataset artifact, analysis notebooks/scripts, and a written report summarizing results and limitations.

---

## Team
**Member 1 (Vivian Lin)**  
Responsibilities:
- Repository setup (folder structure, README updates, data dictionary draft)
- Data ingestion scripts and initial validation checks
- EDA visualizations and summary tables (comparative red vs white)
- Documentation updates (ProjectPlan.md revisions, methodology notes)

**Member 2 (Yoyo Lin)**  
Responsibilities:
- Data cleaning pipeline (type conversions, missingness checks, outlier handling decisions)
- Modeling and evaluation framework (train/test split, cross-validation, metrics)
- Interpretation outputs (feature importance, partial dependence or similar, model comparison)
- Reproducibility polish (requirements, makefile or run instructions, final report integration)

**Shared responsibilities**
- Defining research questions and success criteria
- Designing integration logic (how we combine datasets and track provenance)
- Final narrative and presentation-quality visuals
- Code review for each other’s PRs/commits to ensure consistent style and reproducibility

---

## Research or Business Question(s)
We will address the following analytical questions:

1. **Predictive question**:  
   *How accurately can we predict a wine’s quality score using its physicochemical properties?*  
   - Output: model performance (ex: RMSE/MAE for regression; or accuracy/F1 if reframed as classification such as “high vs not-high quality”).

2. **Comparative question**:  
   *Do the drivers of quality differ between red and white wine?*  
   - Output: side-by-side comparisons of feature effects/importance; interpretation of differences (ex: whether acidity or alcohol has stronger association with quality for one type).

3. **Practical insight question**:  
   *Which measurable factors provide the most actionable insight for quality improvement, and are there thresholds where quality tends to increase?*  
   - Output: interpretable findings (ex: feature importance + plots showing relationships), with clear caveats that correlation ≠ causation.

These questions are directly answerable with the selected datasets because they include consistent physicochemical measurements and a numeric quality label for each observation.

---

## Datasets
We will use the following **two datasets** from the UCI Machine Learning Repository (same domain, complementary categories, integratable by shared attributes):

1. **Wine Quality – Red (UCI ID 186, red wine)**  
   - Description: Observations of Portuguese “Vinho Verde” red wines with physicochemical lab test results and a sensory quality score.
   - Key fields (examples): `fixed acidity`, `volatile acidity`, `citric acid`, `residual sugar`, `chlorides`, `free sulfur dioxide`, `total sulfur dioxide`, `density`, `pH`, `sulphates`, `alcohol`, `quality`.
   - Role in project: Provides the red-wine portion of the study and supports within-type modeling and interpretation.

2. **Wine Quality – White (UCI ID 186, white wine)**  
   - Description: Same format and measurement types, but for white wines.
   - Key fields: same as above (same schema).
   - Role in project: Provides the white-wine portion and enables cross-type comparison.

### Integration plan (how they link)
These datasets can be **meaningfully integrated** because they share the same attributes (identical or near-identical column definitions) and the same target label (`quality`). We will:
- Add a new column `wine_type` with values `{red, white}` based on source file.
- Concatenate rows into one combined dataset for modeling and analysis.
- Preserve provenance by keeping the original file names and documenting the source in the repository.

### Data provenance and licensing notes
We are not using Kaggle. The datasets come from UCI’s repository, which provides a stable reference point for provenance and reproducibility. We will cite the dataset page in our README and document the original publication reference provided by UCI (as available on the dataset page).

---

## Kaggle Clause
We are **not using Kaggle datasets**, so the Kaggle grade penalty clause does not apply. Our datasets are sourced from UCI, and we will maintain clear provenance by linking to the UCI dataset page and documenting exactly which files we used (red and white CSVs) and how we processed them.

---

## Timeline (draft plan with tasks, dates, and owners)

**Milestone 2 (Project Plan) is due: Mar 13.**  
We do not yet have confirmed due dates for Milestone 3 or Milestone 4, so our schedule below is organized by **relative weeks**. Once Milestone 3/4 deadlines are released, we will convert Week-based targets into calendar dates and revise this plan accordingly.

### Now → Milestone 2 submission (through Mar 13)
- **Task A: Finalize project scope + research questions** (Owner: Both)  
  - Lock the primary modeling framing (regression vs classification or both) and define success metrics.  
  - Target: **by Mar 7**
- **Task B: Repo structure + documentation skeleton** (Owner: Member 1)  
  - Create folders (`data/raw`, `data/processed`, `src`, `notebooks`, `docs`) and add/update README run instructions.  
  - Target: **by Mar 8**
- **Task C: Dataset ingestion + schema validation** (Owner: Member 1)  
  - Load red + white datasets, check column consistency, types, missing values, duplicates, basic sanity checks.  
  - Target: **by Mar 10**
- **Task D: Integration pipeline draft** (Owner: Member 2)  
  - Add `wine_type` and concatenate; output a first “combined” dataset artifact in `data/processed`.  
  - Target: **by Mar 11**
- **Task E: Commit + release Milestone 2** (Owner: Both)  
  - Ensure both members contribute commits; tag + GitHub release `project-plan`.  
  - Target: **by Mar 13**

### Week 1 after Milestone 2 feedback (Milestone 3 preparation)
- **Task F: Cleaning decisions + reproducible transformations** (Owner: Member 2)  
  - Outlier policy, scaling/normalization, train/test split approach, any derived features; document decisions.  
- **Task G: Exploratory Data Analysis (EDA) package** (Owner: Member 1)  
  - Distribution comparisons (red vs white), quality distribution, correlation analysis, key bivariate plots.
- **Task H: Update ProjectPlan.md based on grading feedback** (Owner: Both)  
  - Incorporate instructor feedback; adjust scope and timeline.

### Week 2–3 after Milestone 2 feedback (Modeling + evaluation)
- **Task I: Baseline models** (Owner: Member 2)  
  - Simple baselines (mean predictor / linear regression / logistic baseline), establish metrics.
- **Task J: Improved models + validation** (Owner: Member 2)  
  - Compare at least 2 model families (ex:  regularized linear vs tree-based); cross-validation; avoid leakage.
- **Task K: Interpretation + comparison across wine types** (Owner: Both)  
  - Feature importance, effect plots, and “what differs for red vs white” conclusions with caveats.

### Week 4+ after Milestone 2 feedback (Milestone 4 preparation / final report polish)
- **Task L: Final narrative + reproducibility checklist** (Owner: Member 1)  
  - Clean write-up, figure captions, limitations, ethics/reproducibility notes, and “how to rerun.”
- **Task M: Code review + final revisions** (Owner: Both)  
  - Review each other’s code, fix issues, finalize report and outputs.

---

## Constraints (known limitations / challenges)
1. **Label subjectivity and scale**: Quality is a human sensory score (ordinal-ish). Treating it as continuous may be convenient but has interpretive caveats. We will be explicit about whether we model it as regression or classification and why.
2. **No causal claims**: These are observational measurements. We cannot claim that changing a chemical attribute will *cause* quality changes without experimental design.
3. **Limited context variables**: We do not have grape variety, producer practices, vintage, price, region microclimate, or storage conditions. This limits business-style conclusions and may cap predictive performance.
4. **Potential class imbalance**: Quality scores are typically concentrated in mid-range values. We may need metrics robust to imbalance and careful evaluation splits.
5. **Multicollinearity**: Some features may be correlated (ex:  acidity-related measures). Linear models may be unstable without regularization; we will check VIF/correlation and consider regularized models.
6. **Generalizability**: Data represents Portuguese “Vinho Verde” wines and may not generalize to all wines globally.

---

## Gaps (where we need more input)
1. **Course expectations for “integration”**: Our integration uses shared schema (red + white) and concatenation with `wine_type`. If the course expects linking via external IDs (ex:  geography/time/product IDs), we may need to add a third dataset. We will confirm with the instructor/TA early.
2. **Modeling framing**: We need agreement on whether the final primary task is regression on `quality` or a classification threshold (or both). We will decide after EDA based on label distribution and rubric.
3. **Ethics / responsible use framing**: We will clarify which course topics must be explicitly addressed (ex:  transparency, bias, reproducibility) and incorporate them into the write-up.
4. **Tooling standards**: Decide on notebook vs script workflow, dependency management (pip/conda), and CI/testing expectations if any.

---

## Submission checklist (what we will do in GitHub)
1. Add `ProjectPlan.md` to the repository root.
2. Commit with clear messages from both team members so individual contributions are visible in git history.
3. Push to GitHub.
4. Create a tag and release:
   - Tag name: `project-plan`
   - Release title: `Project Plan`
   - Release notes: brief summary + link to `ProjectPlan.md`
5. Submit the release URL in Canvas:
   - `https://github.com/YoyoLin008/Lin-Lin/blob/main/ProjectPlan.md`