#!/usr/bin/env bash
set -euo pipefail

# clean.sh - remove generated artifacts

echo "Cleaning generated files..."
# Remove all generated files; ignore missing files
rm -f *.ly *.wav *.midi *.mp3 *.pdf *.zip 2>/dev/null || true
echo "Clean complete."
