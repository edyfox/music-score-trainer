#!/usr/bin/env python3

from music_notes import MusicNotes

key_c = MusicNotes(
    "C Major / A minor", [
        "g", "a", "b",
        "c'", "d'", "e'", "f'", "g'", "a'", "b'",
        "c''", "d''", "e''", "f''", "g''", "a''", "b''",
        "c'''",
    ], [
        "aes", "bes",
        "des'", "ees'",
        "ges'", "aes'", "bes'",
        "des''", "ees''",
        "ges''", "aes''", "bes''",

        "ais",
        "cis'", "dis'",
        "fis'", "gis'", "ais'",
        "cis''", "dis''",
        "fis''", "gis''", "ais''",
    ], [
        "c,", "d,", "e,", "f,", "g,", "a,", "b,",
        "c", "d", "e", "f", "g", "a", "b",
        "c'", "d'", "e'", "f'",
    ], [
        "des,", "ees,",
        "ges,", "aes,", "bes,",
        "des", "ees",
        "ges", "aes", "bes",
        "des'", "ees'",

        "cis,", "dis,",
        "fis,", "gis,", "ais,",
        "cis", "dis",
        "fis", "gis", "ais",
        "cis'", "dis'",
    ])

key_g = MusicNotes(
    "G Major / E minor", [
        "g", "a", "b", "c'", "d'", "e'", "fis'",
        "g'", "a'", "b'", "c''", "d''", "e''", "fis''",
        "g''", "a''", "b''", "c'''",
    ], [
        "aes", "bes",
        "des'", "ees'", "f'",
        "aes'", "bes'",
        "des''", "ees''", "f''",
        "aes''", "bes''",

        "ais",
        "cis'", "dis'", "eis'",
        "gis'", "ais'",
        "cis''", "dis''", "eis''",
        "gis''", "ais''",
    ], [
        "c,", "d,", "e,", "fis,",
        "g,", "a,", "b,", "c", "d", "e", "fis",
        "g", "a", "b", "c'", "d'", "e'",
    ], [
        "des,", "ees,", "f,",
        "aes,", "bes,",
        "des", "ees", "f",
        "aes", "bes",
        "des'", "ees'", "f'",

        "cis,", "dis,", "eis,",
        "gis,", "ais,",
        "cis", "dis", "eis",
        "gis", "ais",
        "cis'", "dis'", "eis'",
    ])

key_d = MusicNotes(
    "D Major / B minor", [
        "g", "a", "b", "cis'",
        "d'", "e'", "fis'", "g'", "a'", "b'", "cis''",
        "d''", "e''", "fis''", "g''", "a''", "b''",
    ], [
        "aes", "bes", "c'",
        "ees'", "f'",
        "aes'", "bes'", "c''",
        "ees''", "f''",
        "aes''", "bes''", "c'''",

        "ais", "bis",
        "dis'", "eis'",
        "gis'", "ais'", "bis'",
        "dis''", "eis''",
        "gis''", "ais''", "bis''",
    ], [
        "cis,",
        "d,", "e,", "fis,", "g,", "a,", "b,", "cis",
        "d", "e", "fis", "g", "a", "b", "cis'",
        "d'", "e'",
    ], [
        "ees,", "f,",
        "aes,", "bes,", "c",
        "ees", "f",
        "aes", "bes", "c'",
        "ees'", "f'",

        "dis,", "eis,",
        "gis,", "ais,", "bis,",
        "dis", "eis",
        "gis", "ais", "bis",
        "dis'", "eis'",
    ])

key_a = MusicNotes(
    "A Major / \u266fF minor", [
        "gis",
        "a", "b", "cis'", "d'", "e'", "fis'", "gis'",
        "a'", "b'", "cis''", "d''", "e''", "fis''", "gis''",
        "a''", "b''",
    ], [
        "bes", "c'",
        "ees'", "f'", "g'",
        "bes'", "c''",
        "ees''", "f''", "g''",
        "bes''", "c'''",

        "ais", "bis",
        "dis'", "eis'", "fisis'",
        "ais'", "bis'",
        "dis''", "eis''", "fisis''",
        "ais''", "bis''",
    ], [
        "cis,", "d,", "e,", "fis,", "gis,",
        "a,", "b,", "cis", "d", "e", "fis", "gis",
        "a", "b", "cis'", "d'", "e'",
    ], [
        "c,", "ees,", "f,", "g,",
        "bes,", "c",
        "ees", "f", "g",
        "bes", "c'",
        "ees'", "f'",

        "dis,", "eis,", "fisis,",
        "ais,", "bis,",
        "dis", "eis", "fisis",
        "ais", "bis",
        "dis'", "eis'",
    ])

key_e = MusicNotes(
    "E Major / \u266fC minor", [
        "gis", "a", "b", "cis'", "dis'",
        "e'", "fis'", "gis'", "a'", "b'", "cis''", "dis''",
        "e''", "fis''", "gis''", "a''", "b''",
    ], [
        "g",
        "bes", "c'", "d'",
        "f'", "g'",
        "bes'", "c''", "d''",
        "f''", "g''",
        "bes''", "c'''",

        "ais", "bis", "cisis'",
        "eis'", "fisis'",
        "ais'", "bis'", "cisis''",
        "eis''", "fisis''",
        "ais''", "bis''",
    ], [
        "cis,", "dis,",
        "e,", "fis,", "gis,", "a,", "b,", "cis", "dis",
        "e", "fis", "gis", "a", "b", "cis'", "dis'",
        "e'",
    ], [
        "c,", "d,",
        "f,", "g,",
        "bes,", "c", "d",
        "f", "g",
        "bes", "c'", "d'",
        "f'",

        "cisis,",
        "eis,", "fisis,",
        "ais,", "bis,", "cisis",
        "eis", "fisis",
        "ais", "bis", "cisis'",
        "eis'", "fisis'",
    ])
