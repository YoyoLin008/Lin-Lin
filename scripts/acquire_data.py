import argparse
import os
import urllib.request
from __future__ import annotations
from pathlib import Path
from common import ensure_parent

HEALTH_URL = "https://data.cityofchicago.org/api/views/iqnk-2tcu/rows.csv?accessType=DOWNLOAD"
VIOLENCE_URL = "https://data.cityofchicago.org/api/views/gumc-mgzr/rows.csv?accessType=DOWNLOAD"

def download_if_missing(url: str, output_path: Path) -> None:
    ensure_parent(output_path)
    if output_path.exists():
        return

    request = urllib.request.Request(url)
    app_token = os.getenv("SOCRATA_APP_TOKEN")
    if app_token:
        request.add_header("X-App-Token", app_token)

    with urllib.request.urlopen(request) as response, output_path.open("wb") as handle:
        handle.write(response.read())

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--health-out", required=True)
    parser.add_argument("--violence-out", required=True)
    args = parser.parse_args()

    download_if_missing(HEALTH_URL, Path(args.health_out))
    download_if_missing(VIOLENCE_URL, Path(args.violence_out))

if __name__ == "__main__":
    main()
