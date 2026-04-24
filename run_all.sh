#!/usr/bin/env bash

set -euo pipefail

if ! command -v snakemake >/dev/null 2>&1; then
  echo "snakemake is not installed. Install dependencies with 'python3 -m pip install -r requirements.txt' first." >&2
  exit 1
fi

mkdir -p .cache/snakemake-runtime .cache/matplotlib
export XDG_CACHE_HOME="${PWD}/.cache"
export MPLCONFIGDIR="${PWD}/.cache/matplotlib"

snakemake --runtime-source-cache-path "${PWD}/.cache/snakemake-runtime" --cores 1 all
