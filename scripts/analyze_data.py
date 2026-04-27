from __future__ import annotations
from pathlib import Path
from common import ensure_parent
import argparse
import json
import os
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statsmodels.api as sm

os.environ.setdefault("XDG_CACHE_HOME", str(Path(".cache").resolve()))
os.environ.setdefault("MPLCONFIGDIR", str(Path(".cache/matplotlib").resolve()))

PREDICTORS = [
    "below_poverty_level",
    "unemployment",
    "per_capita_income",
    "teen_birth_rate",
]

def write_correlation_table(community: pd.DataFrame, output_path: str) -> pd.DataFrame:
    rows = []
    for column in PREDICTORS:
        rows.append(
            {
                "indicator": column,
                "pearson_correlation_with_mean_annual_total_victims": community[
                    "mean_annual_total_victims"
                ].corr(community[column]),
            }
        )
    correlations = pd.DataFrame(rows).sort_values(
        "pearson_correlation_with_mean_annual_total_victims", ascending=False
    )
    ensure_parent(output_path)
    correlations.to_csv(output_path, index=False)
    return correlations

def write_top_communities(panel: pd.DataFrame, output_path: str) -> pd.DataFrame:
    top = (
        panel.groupby("community_area_name", as_index=False)["total_gun_violence_victims"]
        .mean()
        .rename(columns={"total_gun_violence_victims": "mean_annual_total_victims"})
        .sort_values("mean_annual_total_victims", ascending=False)
        .head(10)
    )
    ensure_parent(output_path)
    top.to_csv(output_path, index=False)
    return top

def save_annual_totals(panel: pd.DataFrame, output_path: str) -> None:
    totals = (
        panel.groupby("year", as_index=False)[
            ["homicide_victims", "nonfatal_shooting_victims", "total_gun_violence_victims"]
        ].sum()
    )
    plt.figure(figsize=(10, 6))
    plt.plot(totals["year"], totals["homicide_victims"], marker="o", label="Homicide victims")
    plt.plot(
        totals["year"],
        totals["nonfatal_shooting_victims"],
        marker="o",
        label="Nonfatal shooting victims",
    )
    plt.plot(
        totals["year"],
        totals["total_gun_violence_victims"],
        marker="o",
        label="Total gun violence victims",
    )
    plt.title("Chicago gun violence victims by year, 2005-2010")
    plt.xlabel("Year")
    plt.ylabel("Victim count")
    plt.grid(alpha=0.25)
    plt.legend()
    plt.tight_layout()
    ensure_parent(output_path)
    plt.savefig(output_path, dpi=200)
    plt.close()

def save_top_communities(top: pd.DataFrame, output_path: str) -> None:
    plt.figure(figsize=(10, 6))
    plt.barh(top["community_area_name"], top["mean_annual_total_victims"], color="#1f77b4")
    plt.gca().invert_yaxis()
    plt.title("Top 10 community areas by mean annual gun violence victims, 2005-2010")
    plt.xlabel("Mean annual victims")
    plt.ylabel("Community area")
    plt.grid(axis="x", alpha=0.25)
    plt.tight_layout()
    ensure_parent(output_path)
    plt.savefig(output_path, dpi=200)
    plt.close()

def save_indicator_relationships(community: pd.DataFrame, output_path: str) -> None:
    fig, axes = plt.subplots(1, 3, figsize=(15, 4.8), sharey=True)
    plots = [
        ("below_poverty_level", "Below poverty level (%)"),
        ("unemployment", "Unemployment (%)"),
        ("per_capita_income", "Per capita income"),
    ]
    for axis, (column, label) in zip(axes, plots):
        x = community[column]
        y = community["mean_annual_total_victims"]
        axis.scatter(x, y, s=35, alpha=0.8, color="#1f77b4")
        coeffs = np.polyfit(x, y, 1)
        x_line = np.linspace(x.min(), x.max(), 100)
        y_line = coeffs[0] * x_line + coeffs[1]
        axis.plot(x_line, y_line, color="#d62728")
        axis.set_xlabel(label)
        axis.set_ylabel("Mean annual gun violence victims")
        axis.grid(alpha=0.25)
    fig.suptitle("Selected socioeconomic indicators and gun violence burden")
    plt.tight_layout()
    ensure_parent(output_path)
    plt.savefig(output_path, dpi=200)
    plt.close()

def fit_model(community: pd.DataFrame, metrics_path: str, summary_path: str) -> dict:
    model_data = community[["mean_annual_total_victims", *PREDICTORS]].dropna().copy()
    model_data["log_mean_annual_total_victims"] = np.log1p(model_data["mean_annual_total_victims"])
    design = sm.add_constant(model_data[PREDICTORS])
    model = sm.OLS(model_data["log_mean_annual_total_victims"], design).fit()

    metrics = {
        "observations": int(model.nobs),
        "r_squared": float(model.rsquared),
        "adjusted_r_squared": float(model.rsquared_adj),
        "aic": float(model.aic),
        "bic": float(model.bic),
        "coefficients": {key: float(value) for key, value in model.params.items()},
        "p_values": {key: float(value) for key, value in model.pvalues.items()},
    }

    ensure_parent(metrics_path)
    ensure_parent(summary_path)
    Path(metrics_path).write_text(json.dumps(metrics, indent=2) + "\n")
    Path(summary_path).write_text(model.summary().as_text() + "\n")
    return metrics

def write_manifest(
    panel: pd.DataFrame,
    community: pd.DataFrame,
    correlations: pd.DataFrame,
    model_metrics: dict,
    output_path: str,
) -> None:
    manifest = {
        "panel_rows": int(len(panel)),
        "panel_communities": int(panel["community_area_number"].nunique()),
        "panel_years": sorted(int(year) for year in panel["year"].unique()),
        "community_rows": int(len(community)),
        "strongest_positive_correlation": correlations.iloc[0].to_dict(),
        "strongest_negative_correlation": correlations.iloc[-1].to_dict(),
        "model_r_squared": model_metrics["r_squared"],
    }
    ensure_parent(output_path)
    Path(output_path).write_text(json.dumps(manifest, indent=2) + "\n")

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--panel", required=True)
    parser.add_argument("--community", required=True)
    parser.add_argument("--correlations-out", required=True)
    parser.add_argument("--top-out", required=True)
    parser.add_argument("--annual-fig-out", required=True)
    parser.add_argument("--top-fig-out", required=True)
    parser.add_argument("--indicator-fig-out", required=True)
    parser.add_argument("--model-metrics-out", required=True)
    parser.add_argument("--model-summary-out", required=True)
    parser.add_argument("--manifest-out", required=True)
    args = parser.parse_args()

    panel = pd.read_csv(args.panel)
    community = pd.read_csv(args.community)
    correlations = write_correlation_table(community, args.correlations_out)
    top = write_top_communities(panel, args.top_out)
    save_annual_totals(panel, args.annual_fig_out)
    save_top_communities(top, args.top_fig_out)
    save_indicator_relationships(community, args.indicator_fig_out)
    model_metrics = fit_model(community, args.model_metrics_out, args.model_summary_out)
    write_manifest(panel, community, correlations, model_metrics, args.manifest_out)


if __name__ == "__main__":
    main()
