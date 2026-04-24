rule all:
    input:
        "metadata/checksums.sha256",
        "results/tables/raw_quality_metrics.csv",
        "results/tables/raw_quality_findings.json",
        "data/interim/health_indicators_clean.csv",
        "data/interim/violence_records_clean.csv",
        "data/processed/community_year_panel.csv",
        "data/processed/community_level_analysis.csv",
        "results/tables/integration_checks.csv",
        "results/tables/correlations.csv",
        "results/tables/top_communities.csv",
        "results/figures/annual_totals.png",
        "results/figures/top_10_communities.png",
        "results/figures/indicator_relationships.png",
        "results/models/linear_model_metrics.json",
        "results/models/linear_model_summary.txt",
        "results/manifest.json",
        "metadata/validation_report.json"


rule acquire_data:
    output:
        health="data/raw/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv",
        violence="data/raw/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv"
    shell:
        "python3 scripts/acquire_data.py --health-out {output.health} --violence-out {output.violence}"


rule generate_checksums:
    input:
        health="data/raw/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv",
        violence="data/raw/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv"
    output:
        "metadata/checksums.sha256"
    shell:
        "python3 scripts/generate_checksums.py --health {input.health} --violence {input.violence} --output {output}"


rule profile_raw_data:
    input:
        health="data/raw/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv",
        violence="data/raw/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv"
    output:
        metrics="results/tables/raw_quality_metrics.csv",
        findings="results/tables/raw_quality_findings.json"
    shell:
        "python3 scripts/profile_data.py --health {input.health} --violence {input.violence} --metrics-out {output.metrics} --findings-out {output.findings}"


rule clean_data:
    input:
        health="data/raw/Public_Health_Statistics_-_Selected_public_health_indicators_by_Chicago_community_area_-_Historical_20260302.csv",
        violence="data/raw/Violence_Reduction_-_Victims_of_Homicides_and_Non-Fatal_Shootings_20260302.csv"
    output:
        health_clean="data/interim/health_indicators_clean.csv",
        violence_clean="data/interim/violence_records_clean.csv"
    shell:
        "python3 scripts/clean_data.py --health {input.health} --violence {input.violence} --health-out {output.health_clean} --violence-out {output.violence_clean}"


rule integrate_data:
    input:
        health_clean="data/interim/health_indicators_clean.csv",
        violence_clean="data/interim/violence_records_clean.csv"
    output:
        panel="data/processed/community_year_panel.csv",
        community="data/processed/community_level_analysis.csv",
        checks="results/tables/integration_checks.csv"
    shell:
        "python3 scripts/integrate_data.py --health {input.health_clean} --violence {input.violence_clean} --panel-out {output.panel} --community-out {output.community} --checks-out {output.checks}"


rule analyze_data:
    input:
        panel="data/processed/community_year_panel.csv",
        community="data/processed/community_level_analysis.csv"
    output:
        correlations="results/tables/correlations.csv",
        top="results/tables/top_communities.csv",
        annual_fig="results/figures/annual_totals.png",
        top_fig="results/figures/top_10_communities.png",
        indicator_fig="results/figures/indicator_relationships.png",
        model_metrics="results/models/linear_model_metrics.json",
        model_summary="results/models/linear_model_summary.txt",
        manifest="results/manifest.json"
    shell:
        "python3 scripts/analyze_data.py --panel {input.panel} --community {input.community} --correlations-out {output.correlations} --top-out {output.top} --annual-fig-out {output.annual_fig} --top-fig-out {output.top_fig} --indicator-fig-out {output.indicator_fig} --model-metrics-out {output.model_metrics} --model-summary-out {output.model_summary} --manifest-out {output.manifest}"


rule validate_outputs:
    input:
        panel="data/processed/community_year_panel.csv",
        community="data/processed/community_level_analysis.csv"
    output:
        "metadata/validation_report.json"
    shell:
        "python3 scripts/validate_outputs.py --panel {input.panel} --community {input.community} --output {output}"
