#!/usr/bin/env bash
set -euo pipefail

echo "[bootstrap] Checking prerequisites..."

if ! command -v rustup >/dev/null 2>&1; then
  echo "rustup not found. Install rustup first: https://rustup.rs/"
  exit 1
fi

if ! command -v cargo >/dev/null 2>&1; then
  echo "cargo not found in PATH. Ensure rustup is initialized (source \"$HOME/.cargo/env\")."
  exit 1
fi

echo "[bootstrap] Ensuring stable Rust toolchain..."
rustup toolchain install stable >/dev/null
rustup default stable >/dev/null

echo "[bootstrap] Installing mdbook (if missing)..."
if ! command -v mdbook >/dev/null 2>&1; then
  cargo install mdbook --locked
else
  echo "mdbook already installed: $(mdbook --version)"
fi

echo "[bootstrap] Installing mdbook-linkcheck (if missing)..."
if ! command -v mdbook-linkcheck >/dev/null 2>&1; then
  cargo install mdbook-linkcheck --locked
else
  echo "mdbook-linkcheck already installed: $(mdbook-linkcheck --version || echo present)"
fi

echo "[bootstrap] Done. You can run: make check"

