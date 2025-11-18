#!/usr/bin/env python3

from music_notes import MusicNotes
import re


# Treble clef range (G3 → C6 in LilyPond-ish notation)
BASE_TREBLE = [
    "g", "a", "b",
    "c'", "d'", "e'", "f'", "g'", "a'", "b'",
    "c''", "d''", "e''", "f''", "g''", "a''", "b''",
    "c'''",
]

# Bass clef range (C2 → F4)
BASE_BASS = [
    "c,", "d,", "e,", "f,", "g,", "a,", "b,",
    "c", "d", "e", "f", "g", "a", "b",
    "c'", "d'", "e'", "f'",
]

# Helper for parsing pitch names into (letter, accidental, octave)
PITCH_RE = re.compile(r"^([a-g])(es|is|eses|isis)?(,+|'*)$")

def parse_pitch(p):
    """
    Converts something like "aes''" or "c," into:
    (letter='a', accidental='es', octave="''")
    """
    m = PITCH_RE.match(p)
    if not m:
        raise ValueError(f"Invalid pitch: {p}")
    return m.group(1), m.group(2) or "", m.group(3)

def same_letter(p, letter):
    """True if pitch p has the same letter (ignores octave & accidental)."""
    L, _, _ = parse_pitch(p)
    return L == letter


def apply_key_signature(base_list, sharps_or_flats):
    """
    Replace notes in base_list if their letter appears in sharps_or_flats.

    sharps_or_flats: dict { "f": "is", "b": "es", ... }
        meaning F♯ or B♭, etc.
    """
    result = []
    for p in base_list:
        letter, _, octave = parse_pitch(p)
        if letter in sharps_or_flats:
            accidental = sharps_or_flats[letter]   # "is" or "es"
            result.append(f"{letter}{accidental}{octave}")
        else:
            result.append(p)
    return result


def clamp_range(notes, base):
    """
    Remove first note if it's flat (accidental ends with 'es').
    Remove last note if it's sharp (accidental ends with 'is').
    """
    if not notes:
        return []

    # First note clamp
    first_letter, first_acc, first_octave = parse_pitch(notes[0])
    first_letter_base, _, first_octave_base = parse_pitch(base[0])
    if (first_letter == first_letter_base and
            first_octave == first_octave_base and
            first_acc and first_acc.startswith("es")):
           notes = notes[1:]

    if not notes:
        return []

    # Last note clamp
    last_letter, last_acc, last_octave = parse_pitch(notes[-1])
    last_letter_base, _, last_octave_base = parse_pitch(base[-1])
    if (last_letter == last_letter_base and
            last_octave == last_octave_base and
            last_acc and last_acc.startswith("is")):
        notes = notes[:-1]

    return notes


def expand_accidentals(base_list, accidental_letters):
    """
    Given e.g. accidental_letters = ["des", "ees", "fis"]
    Generate correct octaves FROM base_list's pitch range.
    """
    expanded = []

    # Pre-extract the octave band from base_list
    parsed_base = [parse_pitch(p) for p in base_list]

    for base_letter, _, octave in parsed_base:
        if base_letter in accidental_letters:
            accidental = accidental_letters[base_letter]
            expanded.append(f"{base_letter}{accidental}{octave}")

    return clamp_range(expanded, base_list)


def make_key(name, sig, accidentals):
    """
    name: "C Major / A minor"
    sig: dict { "f": "is", "b": "es" } for key signature (diatonic)
    accidentals: list ["des", "ees", ...] for chromatic notes

    Returns MusicNotes instance.
    """
    diatonic_treble = clamp_range(apply_key_signature(BASE_TREBLE, sig), BASE_TREBLE)
    diatonic_bass = clamp_range(apply_key_signature(BASE_BASS, sig), BASE_BASS)

    accidental_treble = [
        *clamp_range(expand_accidentals(BASE_TREBLE, accidentals[0]), BASE_TREBLE),
        *clamp_range(expand_accidentals(BASE_TREBLE, accidentals[1]), BASE_TREBLE),
    ]
    accidental_bass = [
        *clamp_range(expand_accidentals(BASE_BASS, accidentals[0]), BASE_BASS),
        *clamp_range(expand_accidentals(BASE_BASS, accidentals[1]), BASE_BASS),
    ]
    return MusicNotes(name, diatonic_treble, accidental_treble, diatonic_bass, accidental_bass)


key_c = make_key(
    "C Major / A minor",
    sig={},  # No sharps or flats
    accidentals=[
        # ra, me, se, le, te
        {"d": "es", "e": "es", "g": "es", "a": "es", "b": "es"},
        # di, ri, fi, si, li
        {"c": "is", "d": "is", "f": "is", "g": "is", "a": "is"},
    ]
)

key_g = make_key(
    "G Major / E minor",
    sig={"f": "is"},
    accidentals=[
        # ra, me, se, le, te
        {"a": "es", "b": "es", "d": "es", "e": "es", "f": ""},
        # di, ri, fi, si, li
        {"g": "is", "a": "is", "c": "is", "d": "is", "e": "is"},
    ]
)

key_f = make_key(
    "F Major / D minor",
    sig={"b": "es"},
    accidentals=[
        # ra, me, se, le, te
        {"g": "es", "a": "es", "c": "es", "d": "es", "e": "es"},
        # di, ri, fi, si, li
        {"f": "is", "g": "is", "b": "", "c": "is", "d": "is"},
    ]
)

key_d = make_key(
    "D Major / B minor",
    sig={"f": "is", "c": "is"},
    accidentals=[
        # ra, me, se, le, te
        {"e": "es", "f": "", "a": "es", "b": "es", "c": ""},
        # di, ri, fi, si, li
        {"d": "is", "e": "is", "g": "is", "a": "is", "b": "is"},
    ]
)

key_bes = make_key(
    "\u266dB Major / G minor",
    sig={"b": "es", "e": "es"},
    accidentals=[
        # ra, me, se, le, te
        {"c": "es", "d": "es", "f": "es", "g": "es", "a": "es"},
        # di, ri, fi, si, li
        {"b": "", "c": "is", "e": "", "f": "is", "g": "is"},
    ]
)

key_a = make_key(
    "A Major / \u266fF minor",
    sig={"f": "is", "c": "is", "g": "is"},
    accidentals=[
        # ra, me, se, le, te
        {"b": "es", "c": "", "e": "es", "f": "", "g": ""},
        # di, ri, fi, si, li
        {"a": "is", "b": "is", "d": "is", "e": "is", "f": "isis"},
    ]
)

key_ees = make_key(
    "\u266dE Major / C minor",
    sig={"b": "es", "e": "es", "a": "es"},
    accidentals=[
        # ra, me, se, le, te
        {"f": "es", "g": "es", "b": "eses", "c": "es", "d": "es"},
        # di, ri, fi, si, li
        {"e": "", "f": "is", "a": "", "b": "", "c": "is"},
    ]
)

key_e = make_key(
    "E Major / \u266fC minor",
    sig={"f": "is", "c": "is", "g": "is", "d": "is"},
    accidentals=[
        # ra, me, se, le, te
        {"f": "", "g": "", "b": "es", "c": "", "d": ""},
        # di, ri, fi, si, li
        {"e": "is", "f": "isis", "a": "is", "b": "is", "c": "isis"},
    ]
)

key_aes = make_key(
    "\u266dA Major / F minor",
    sig={"b": "es", "e": "es", "a": "es", "d": "es"},
    accidentals=[
        # ra, me, se, le, te
        {"b": "eses", "c": "es", "e": "eses", "f": "es", "g": "es"},
        # di, ri, fi, si, li
        {"a": "", "b": "", "d": "", "e": "", "f": "is"},
    ]
)

key_b = make_key(
    "B Major / \u266fG minor",
    sig={"f": "is", "c": "is", "g": "is", "d": "is", "a": "is"},
    accidentals=[
        # ra, me, se, le, te
        {"c": "", "d": "", "f": "", "g": "", "a": ""},
        # di, ri, fi, si, li
        {"b": "is", "c": "isis", "e": "is", "f": "isis", "g": "isis"},
    ]
)

key_des = make_key(
    "\u266dD Major / \u266dB minor",
    sig={"b": "es", "e": "es", "a": "es", "d": "es", "g": "es"},
    accidentals=[
        # ra, me, se, le, te
        {"e": "eses", "f": "es", "a": "eses", "b": "eses", "c": "es"},
        # di, ri, fi, si, li
        {"d": "", "e": "", "g": "", "a": "", "b": ""},
    ]
)
