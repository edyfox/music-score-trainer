#!/usr/bin/env bash
set -euo pipefail

# release.sh
# Generates PDFs/MP3s via build.sh, then zips them into a versioned archive.

# ---- Configuration ----
# Read version from VERSION file (fallback to v0.0.0)
if [[ -f "./VERSION" ]]; then
  VERSION=$(cat ./VERSION)
else
  VERSION="v0.0.0"
fi
OUTPUT="score-with-audio-${VERSION}.zip"

# ---- Ensure latest assets ----
if [ -f "./build.sh" ]; then
  echo "Running build.sh to (re)generate PDFs and MP3s..."
  ./build.sh
else
  echo "Warning: build.sh not found – proceeding with existing files."
fi

# Remove existing archive if it exists
rm -f "$OUTPUT"

echo "Looking for PDF and MP3 files..."
# Gather files; ignore errors if a type is missing, but require at least one file.
FILES=$(ls *.pdf *.mp3 2>/dev/null || true)

if [ -z "$FILES" ]; then
  echo "Error: No .pdf or .mp3 files found to pack."
  exit 1
fi

echo "Creating $OUTPUT..."
# shellcheck disable=SC2086
zip "$OUTPUT" $FILES

echo "Success! Release artifact created: $OUTPUT"
