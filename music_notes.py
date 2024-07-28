#!/usr/bin/env python3

class MusicNotes:
    """
    A class to represent musical notes for treble and bass clefs.

    Attributes:
        treble (ClefNotes): An instance of the ClefNotes class for the treble
                clef.
        bass (ClefNotes): An instance of the ClefNotes class for the bass clef.
    """
    
    class ClefNotes:
        """
        Inner class to represent notes for a clef.

        Attributes:
            _scale_notes (list): List of notes in the scale.
            _altered_notes (list): List of notes with alterations.
        """
        def __init__(self, scale_notes, altered_notes):
            """
            Initializes the ClefNotes with scale and altered notes.

            Args:
                scale_notes (list): List of notes in the scale.
                altered_notes (list): List of notes with alterations.
            """
            self._scale_notes = scale_notes
            self._altered_notes = altered_notes

        def scale_notes(self):
            """
            Retrieves the scale notes.

            Returns:
                list: The list of scale notes.
            """
            return self._scale_notes

        def altered_notes(self):
            """
            Retrieves the altered notes.

            Returns:
                list: The list of altered notes.
            """
            return self._altered_notes

        def __repr__(self):
            """
            Returns a string representation of the ClefNotes.

            Returns:
                str: String representation of the ClefNotes.
            """
            return (f"  Scale Notes: {self._scale_notes}\n"
                    f"  Altered Notes: {self._altered_notes}")

    def __init__(self, name, treble_scale_notes, treble_altered_notes,
            bass_scale_notes, bass_altered_notes):
        """
        Initializes the MusicNotes with treble and bass clef notes.

        Args:
            name: name of the key.
            treble_scale_notes (list): List of scale notes for the treble clef.
            treble_altered_notes (list): List of altered notes for the treble
                    clef.
            bass_scale_notes (list): List of scale notes for the bass clef.
            bass_altered_notes (list): List of altered notes for the bass clef.
        """
        self.name = name
        self.treble = self.ClefNotes(treble_scale_notes, treble_altered_notes)
        self.bass = self.ClefNotes(bass_scale_notes, bass_altered_notes)
    
    def treble_scale_notes(self):
        """
        Retrieves the treble clef scale notes.

        Returns:
            list: The list of treble clef scale notes.
        """
        return self.treble.scale_notes()

    def treble_altered_notes(self):
        """
        Retrieves the treble clef altered notes.

        Returns:
            list: The list of treble clef altered notes.
        """
        return self.treble.altered_notes()

    def bass_scale_notes(self):
        """
        Retrieves the bass clef scale notes.

        Returns:
            list: The list of bass clef scale notes.
        """
        return self.bass.scale_notes()

    def bass_altered_notes(self):
        """
        Retrieves the bass clef altered notes.

        Returns:
            list: The list of bass clef altered notes.
        """
        return self.bass.altered_notes()

    def __repr__(self):
        """
        Returns a string representation of the MusicNotes.

        Returns:
            str: String representation of the MusicNotes.
        """
        return (f"Name: {self.name}\n"
                f"Treble Clef:\n{self.treble}\n"
                f"Bass Clef:\n{self.bass}")
