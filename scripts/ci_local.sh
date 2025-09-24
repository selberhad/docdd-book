#!/usr/bin/env bash
set -euo pipefail

echo "[ci] Running local checks..."

if ! command -v mdbook >/dev/null 2>&1; then
  echo "mdbook not found. Run scripts/bootstrap_mdbook.sh first." >&2
  exit 1
fi

# If mdbook-linkcheck is installed and configured in book.toml, it runs during build.
mdbook build

echo "[ci] Build OK. Output in ./book"

