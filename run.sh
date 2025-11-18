#!/usr/bin/env bash
set -euo pipefail

# run.sh
# Iterate through keys defined in key_generator.py, generate LilyPond (.ly),
# then produce PDF/MIDI (via lilypond) and WAV/MP3 (via timidity + lame).


ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"
cd "$ROOT_DIR"

# Determine keys list by parsing `key_generator.py` only.
if [ ! -f key_generator.py ]; then
  echo "Error: key_generator.py not found in repository root; cannot discover keys."
  exit 1
fi

KEYS=$(grep -oE 'key_[A-Za-z]+' key_generator.py 2>/dev/null | sort -u | sed 's/^key_//') || true
KEYS=$(echo "$KEYS" | xargs) || true
if [ -z "$KEYS" ]; then
  echo "No keys found in key_generator.py (looking for variables named key_*)"
  exit 1
fi

echo "Found keys: $KEYS"

for cmd in python3 lilypond timidity lame; do
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "Warning: $cmd not found in PATH; some steps may be skipped."
  fi
done

for k in $KEYS; do
  echo
  echo "=== Processing key: $k ==="
  ly="key_${k}.ly"
  midi="key_${k}.midi"
  wav="key_${k}.wav"
  mp3="key_${k}.mp3"

  echo "Generating LilyPond source: $ly"
  if ! python3 sight_reading.py --key="$k" > "$ly"; then
    echo "ERROR: sight_reading.py failed for key $k"
    continue
  fi

  echo "Running lilypond to create PDF & MIDI"
  if ! lilypond --version >/dev/null 2>&1; then
    echo "lilypond not available; skipping lilypond step for $k"
    continue
  fi

  if ! lilypond "$ly"; then
    echo "lilypond failed for $ly"
    continue
  fi

  if [ ! -f "$midi" ]; then
    echo "No MIDI produced for $k (expected $midi); skipping audio conversion"
    continue
  fi

  if command -v timidity >/dev/null 2>&1; then
    echo "Converting MIDI -> WAV: $midi -> $wav"
    if ! timidity -Ow -o "$wav" "$midi"; then
      echo "timidity failed for $midi"
      continue
    fi
  else
    echo "timidity not found; skipping WAV/MP3 generation for $k"
    continue
  fi

  if command -v lame >/dev/null 2>&1; then
    echo "Encoding WAV -> MP3: $wav -> $mp3"
    if ! lame -V2 "$wav" "$mp3"; then
      echo "lame failed for $wav"
      continue
    fi
    rm -f "$wav"
  else
    echo "lame not found; keeping WAV file: $wav"
  fi

  echo "Finished $k: PDF and audio (if tools available)"
done

echo
echo "All done."
