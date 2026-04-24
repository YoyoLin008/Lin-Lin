from __future__ import annotations

import argparse
import hashlib
from pathlib import Path

from common import ensure_parent


def sha256sum(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--health", required=True)
    parser.add_argument("--violence", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    output_path = Path(args.output)
    ensure_parent(output_path)
    lines = []
    for file_path in [Path(args.health), Path(args.violence)]:
        lines.append(f"{sha256sum(file_path)}  {file_path.as_posix()}")
    output_path.write_text("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
