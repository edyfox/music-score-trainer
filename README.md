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
   - This command will generate `key_c.pdf` and `key_c.mid` files.

4. **Convert MIDI to Audio:**
   - Use TiMidity++ to convert the MIDI file to a WAV audio file:
     ```bash
     timidity -Ow key_c.mid
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

## License
This project is licensed under GNU General Public License, Version 3. See the
[LICENSE](LICENSE) file for details.

## Acknowledgements
This script is inspired by [Ada](https://github.com/adaext) and is created to
help her with her piano practicing.
