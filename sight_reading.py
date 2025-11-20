#!/usr/bin/env python3

import random
import argparse
import sys

from key_generator import key_c, key_g, key_f, key_d, key_bes, key_a, key_ees, key_e, key_aes, key_b, key_des, key_fis

def generate_sight_reading_exercise(key, shuffle):
    """
    Generates a LilyPond score for a sight-reading exercise.
    """
    if key.name[0].isalpha():
        key_text = key.name[0]
    else:
        key_text = key.name[:2]

    if key_text[0] == '\u266d':  # Flat symbol
        key_name = key_text[1].lower() + "es"
    elif key_text[0] == '\u266f':  # Sharp symbol
        key_name = key_text[1].lower() + "is"
    else:
        key_name = key_text[0].lower()
    title = "Key of " + key_text
    subtitle = key.name

    treble_notes = (key.treble_scale_notes() * (3 if shuffle else 1) +
            key.treble_altered_notes())
    bass_notes = (key.bass_scale_notes() * (3  if shuffle else 1) +
            key.bass_altered_notes())

    # Shuffle both lists
    if shuffle:
        random.shuffle(treble_notes)
        random.shuffle(bass_notes)

    treble_score = []
    bass_score = []

    while treble_notes or bass_notes:
        # Choose randomly from which list to pop, with consideration for empty lists
        if treble_notes and bass_notes:
            choice = random.choice(['treble', 'bass']) if shuffle else 'treble'
        elif treble_notes:
            choice = 'treble'
        else:
            choice = 'bass'

        if choice == 'treble':
            treble_score.append(treble_notes.pop(0))
            bass_score.append("r")
        else:
            treble_score.append("r")
            bass_score.append(bass_notes.pop(0))

    if treble_score:
        treble_score[0] = treble_score[0] + "1"
    if bass_score:
        bass_score[0] = bass_score[0] + "1"

    print(r"""\version "2.24.3"
\header {""")
    print('  title = "' + title + '"')
    print('  subtitle = "' + subtitle + '"')
    print(r"""
  tagline = ""
}
upper = {
  \clef treble""")
    print(r"  \key " + key_name + r" \major")
    print(r"  \time 4/4""")

    for item in treble_score:
        print(f"  {item}")

    print(r"""  \bar "|."
}
lower = {
  \clef bass""")
    print(r"  \key " + key_name + r" \major")
    print(r"  \time 4/4""")

    for item in bass_score:
        print(f"  {item}")

    print(r"""  \bar "|."
}
\score {
  \new PianoStaff
  <<
    \new Staff = "upper" \upper
    \new Staff = "lower" \lower
  >>
  \layout { }
  \midi { }
}
""")

def main():
    """
    Main function to generate the sight-reading exercise.
    """
    parser = argparse.ArgumentParser(description="Generate a sight-reading exercise.")
    parser.add_argument("--key", dest="key", default="c",
                        help="Key to generate: c, g, f, d, bes, a, ees, e, aes, b, des, fis (defaults to c)")
    # allow explicit enable/disable of shuffle
    parser.add_argument("--shuffle", dest="shuffle", action=argparse.BooleanOptionalAction,
                        default=True,
                        help="Enable or disable shuffling of notes (default: enabled)")

    args = parser.parse_args()

    # Map common names to the imported key objects
    key_map = {
        "c": key_c,
        "g": key_g,
        "f": key_f,
        "d": key_d,
        "bes": key_bes,
        "bb": key_bes,
        "a": key_a,
        "ees": key_ees,
        "eb": key_ees,
        "e": key_e,
        "aes": key_aes,
        "ab": key_aes,
        "b": key_b,
        "des": key_des,
        "db": key_des,
        "fis": key_fis,
        "f#": key_fis,
    }

    key_name = args.key.lower()
    if key_name not in key_map:
        print(f"Unknown key '{args.key}'. Valid keys: {', '.join(sorted(key_map.keys()))}")
        sys.exit(2)

    selected_key = key_map[key_name]

    generate_sight_reading_exercise(selected_key, args.shuffle)

if __name__ == "__main__":
    main()
