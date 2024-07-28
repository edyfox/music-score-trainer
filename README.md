# Music Score Trainer

**Music Score Trainer** is a Python script that generates a music score of
random notes and an accompanying audio file to aid in practicing note
recognition and sight-reading skills.

## Features
- Generates a music score with random notes.
- Creates an audio file matching the generated score.
- Ideal for practicing note recognition and improving sight-reading skills.

## Dependencies
- [LilyPond](http://lilypond.org/) - used to generate PDF and MIDI files.
- [TiMidity++](https://timidity.sourceforge.net/) - used to convert MIDI files
  to audio.
- [LAME](http://lame.sourceforge.net/) - used to compress the generated audio to
  MP3.

## Usage

1. **Modify the Script:**
   - Open `sight_reading.py` in a text editor.
   - Locate the line `key = key_c` and change it to the key you want to
     practice.
     - For example, `key = key_a` for the key of A.
     - Sharp keys are named with an `is` suffix (e.g., key F sharp is
       `key_fis`).
     - Flat keys are named with an `es` suffix (e.g., key B flat is `key_bes`).

2. **Generate the LilyPond File:**
   - Run the script and redirect the output to a `.ly` file:
     ```bash
     python3 sight_reading.py > key_c.ly
     ```
   - Replace `key_c.ly` with the desired key name.

3. **Create the Music Score and MIDI File:**
   - Use LilyPond to generate the PDF and MIDI files:
     ```bash
     lilypond key_c.ly
     ```
   - This command will generate `key_c.pdf` and `key_c.midi` files.

4. **Convert MIDI to Audio:**
   - Use TiMidity++ to convert the MIDI file to a WAV audio file:
     ```bash
     timidity -Ow key_c.midi
     ```
   - This command will generate a `key_c.wav` file.

5. **Compress the Audio File:**
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
   for the key.
   - Sharp-spelt notes: di, ri, fi, si, li
   - Flat-spelt notes: ra, me, se, le, te

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
