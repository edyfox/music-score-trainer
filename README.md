# Music Score Trainer

**Music Score Trainer** is a Python script that generates a music score of
random notes and an accompanying audio file to aid in practicing note
recognition and sight-reading skills.

## Features
- Generates a music score with random notes.
- Creates an audio file matching the generated score.
- Ideal for practicing note recognition and improving sight-reading skills.

## Dependencies
- [Python 3](https://www.python.org/) - required to run the script.
- [LilyPond](http://lilypond.org/) - used to generate PDF and MIDI files.
- [TiMidity++](https://timidity.sourceforge.net/) - used to convert MIDI files
  to audio.
- [LAME](http://lame.sourceforge.net/) - used to compress the generated audio to
  MP3.

## Usage

1. Command-line usage

   The script accepts command-line options to select the key and to
   enable/disable shuffling of the generated notes. Use the `--key` option
   to choose which `key_` definition from `keys.py` will be used.

   - `--key=<name>`: Choose the key to generate. For example `--key=c` will use
     `key_c` as defined in `keys.py`. Valid values correspond to the
     `key_` variables (for example: `c`, `g`, `f`, `d`, `bes`, `a`, `ees`,
     `e`, `aes`, `b`, etc.).
   - `--shuffle` / `--no-shuffle`: Control whether notes are shuffled. Use
     `--no-shuffle` to produce a deterministic, unshuffled sequence.

   Example: generate LilyPond for C major (shuffled):

   ```bash
   python3 sight_reading.py --key=c > key_c.ly
   ```

   Example: generate LilyPond for A major without shuffling:

   ```bash
   python3 sight_reading.py --key=a --no-shuffle > key_a.ly
   ```

2. Create the Music Score and MIDI File

   - Use LilyPond to generate the PDF and MIDI files:

     ```bash
     lilypond key_c.ly
     ```

   - This command will generate `key_c.pdf` and `key_c.midi` files.

3. Convert MIDI to Audio

   - Use TiMidity++ to convert the MIDI file to a WAV audio file:

     ```bash
     timidity -Ow key_c.midi
     ```

   - This command will generate a `key_c.wav` file.

4. Compress the Audio File

   - Use LAME to compress the WAV file to MP3 format:

     ```bash
     lame key_c.wav
     ```

   - This command will generate a `key_c.mp3` file.

After completing these steps, you will have a PDF music score and an MP3 audio
file for practicing note recognition and sight-reading skills.

## Contributing

We welcome contributions to expand the range of keys supported by the Music
Score Trainer. If you would like to add data for new keys, please update the
`keys.py` file with the necessary information.

### Guidelines for Notes

For each key, provide data for both the treble clef and bass clef:

1. **Treble Clef:**
   - Notes must be within the range of G3 to C6, inclusive.
   - Ensure that all notes in the lists are within this range, considering both
     actual pitch and spelling.

2. **Bass Clef:**
   - Notes must be within the range of C2 to F4, inclusive.
   - Similarly, ensure that all notes are within this range, considering both
     actual pitch and spelling. For instance, B1-sharp is technically C2, but B1
     itself is outside the range, so it should not be included.

Each clef should include the following lists:

1. **Scale Notes:** this list contains all the notes in the scale for the
   specified key. For each key, the scale notes are: do, re, mi, fa, so, la, ti.
2. **Altered Notes:** This list includes all sharp-spelt and flat-spelt notes
   for the key. These are the chromatic notes *not* in the diatonic scale.
   - Sharp-spelt notes: di, ri, fi, si, li
   - Flat-spelt notes: ra, me, se, le, te

#### Key Ordering

The order of keys in `keys.py` should be: 0 sharps/flats (C), 1 sharp (G),
1 flat (F), 2 sharps (D), 2 flats (Bb), and so on.

#### Formatting Scale Notes

- The list should contain all notes of the key's major scale that fall within
  the specified range for the clef.
- Each new octave of the scale should start on a new line, beginning with the
  tonic (e.g., `aes`, `aes'`, `aes''`).
- The very first line may contain notes leading up to the first tonic if the
  range starts below it.

#### Formatting Altered Notes

- The notes should be grouped by spelling: flat-spelt notes first, then
  sharp-spelt notes, separated by a blank line.
- Within each spelling group, the notes are grouped by solfege pairs/triplets
  and by octave.
  - **Flat-spelt:** `ra, me` on one line, and `se, le, te` on the next.
  - **Sharp-spelt:** `di, ri` on one line, and `fi, si, li` on the next.
- This grouping pattern repeats for each octave.
- If a note in a group is out of range, the group is truncated for that octave.

### Steps to Add New Keys

1. **Create the Data:** Follow the provided guidelines to create the
   scale notes and altered notes lists for both treble and bass clefs in
   `keys.py`.
2. **Update the Script:** Modify the `key = key_c` line in `sight_reading.py` to
   reference the newly added key in `keys.py`. Set `shuffle = False` to disable
   random shuffling of notes, which will make it easier to inspect and verify
   the generated results.
3. **Generate and Verify Scores:** Follow the steps in the "Usage" section to
   generate the music scores and ensure that they are correct.
4. **Submit a Pull Request:** Once you have confirmed that everything works as
   expected, commit only the changes to `keys.py`, create a new branch for your
   updates, and submit a pull request.

Thank you for contributing to the Music Score Trainer project!

## License
This project is licensed under GNU General Public License, Version 3. See the
[LICENSE](LICENSE) file for details.

## Acknowledgements
This script is inspired by [Ada](https://github.com/adaext) and is created to
help her with her piano practicing.
