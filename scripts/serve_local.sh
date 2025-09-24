#!/usr/bin/env bash
set -euo pipefail

if ! command -v mdbook >/dev/null 2>&1; then
  echo "mdbook not found. Run scripts/bootstrap_mdbook.sh first." >&2
  exit 1
fi

exec mdbook serve -n 127.0.0.1 -p 3000 -o

