#!/usr/bin/env bash

set -euo pipefail

PYTHON_BIN="${PYTHON_BIN:-python3}"
VENV_DIR="${VENV_DIR:-.venv}"

if ! command -v "${PYTHON_BIN}" >/dev/null 2>&1; then
  echo "Could not find ${PYTHON_BIN}. Install Python 3 and rerun this script." >&2
  exit 1
fi

if [ ! -x "${VENV_DIR}/bin/python" ]; then
  "${PYTHON_BIN}" -m venv "${VENV_DIR}"
fi

"${VENV_DIR}/bin/python" -m pip install -r requirements.txt

mkdir -p .cache/snakemake-runtime .cache/matplotlib
export XDG_CACHE_HOME="${PWD}/.cache"
export MPLCONFIGDIR="${PWD}/.cache/matplotlib"

"${VENV_DIR}/bin/snakemake" --runtime-source-cache-path "${PWD}/.cache/snakemake-runtime" --cores 1 all
