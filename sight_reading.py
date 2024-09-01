#!/usr/bin/env python3

from keys import *
import random

key = key_c
shuffle = True

if key.name[0].isalpha():
    key_text = key.name[0].lower()
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

treble_score[0] = treble_score[0] + "1"
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
print("  \key " + key_name + " \major")
print(r"  \time 4/4""")

for item in treble_score:
    print(f"  {item}")

print(r"""  \bar "|." 
}
lower = {
  \clef bass""")
print("  \key " + key_name + " \major")
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
