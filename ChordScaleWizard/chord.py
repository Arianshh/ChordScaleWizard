from .note import Note, NOTE_LIST

chord_interval = {
    'major': [0, 4, 7],
    'm': [0, 3, 7],
    'dim': [0, 3, 6],
    'dim7': [0, 3, 6, 9],
    'maj7': [0, 4, 7, 11],
    'm7': [0, 3, 7, 10],
    '7': [0, 4, 7, 10],
    'sus2': [0, 2, 7],
    'sus4': [0, 5, 7],
    'aug': [0, 4, 8],
    'maj9': [0, 4, 7, 11, 14],
    'm9': [0, 3, 7, 10, 14],
    '9': [0, 4, 7, 10, 14],
    'maj11': [0, 4, 7, 11, 14, 17],
    'm11': [0, 3, 7, 10, 14, 17],
    '11': [0, 4, 7, 10, 14, 17],
    'maj13': [0, 4, 7, 11, 14, 17, 21],
    '13': [0, 4, 7, 10, 14, 17, 21],
    'm13': [0, 3, 7, 10, 14, 17, 21],
    'minmaj7': [0, 3, 7, 11],
    '6': [0, 4, 7, 9],
    'm6': [0, 3, 7, 9],
    'maj7#11': [0, 4, 7, 11, 18],
    'maj7b5': [0, 4, 6, 11],
    'm7b5': [0, 3, 6, 10],
    '7#5': [0, 4, 8, 10],
    'minmaj11': [0, 3, 7, 11, 14, 17],
    'minmaj13': [0, 3, 7, 11, 14, 17, 21],
    '6/9': [0, 4, 7, 9, 14],
    'add9': [0, 4, 7, 14],
    'add4': [0, 4, 7, 5],
    'aug7': [0, 4, 8, 10],
    'maj7#5': [0, 4, 8, 11],
    'maj7#9': [0, 4, 7, 11, 15],
    'maj7b9': [0, 4, 7, 11, 13],
    'maj7#5#9': [0, 4, 8, 11, 15],
    'maj7b5#9': [0, 4, 6, 11, 15],
    '9#5': [0, 4, 8, 10, 14],
    '9b5': [0, 4, 6, 10, 14],
    '7sus4': [0, 5, 7, 10],
    '7b9': [0, 4, 7, 10, 13],
    '7#9': [0, 4, 7, 10, 15],
    '7b5b9': [0, 4, 6, 10, 13],
    '7b5#9': [0, 4, 6, 10, 15],
    '7#5b9': [0, 4, 8, 10, 13],
    '7#5#9': [0, 4, 8, 10, 15],
    '13b9': [0, 4, 7, 10, 13, 21],
    '13#9': [0, 4, 7, 10, 15, 21],
    '13b5b9': [0, 4, 6, 10, 13, 21],
    '13b5#9': [0, 4, 6, 10, 15, 21],
    '13#5b9': [0, 4, 8, 10, 13, 21],
    '13#5#9': [0, 4, 8, 10, 15, 21],
    'maj13#11': [0, 4, 7, 11, 18, 21],
    'maj13#11#9': [0, 4, 7, 11, 15, 18, 21],
    'maj7add13': [0, 4, 7, 11, 21],
    '6/7': [0, 4, 7, 9, 10]
}


class Chord:
    def __init__(self, name, note):
        self.name = name
        if isinstance(note, Note):
            note = note.value
        self.note = Note(name=note)

    def get_chord_notes(self):
        root_note = self.note.name.upper()
        chord_variation = self.name
        if not chord_variation:
            chord_variation = 'major'
        intervals = chord_interval.get(chord_variation, None)
        if not intervals:
            print('Invalid Chord.')
            exit()
        root_index = NOTE_LIST.index(root_note)
        chord_notes = []
        for interval in intervals:
            note_index = (root_index + interval) % 12
            chord_notes.append(NOTE_LIST[note_index])
        return chord_notes


def get_chords_notes(note, chord):
    chord_obj = Chord(chord, note.upper())
    notes = chord_obj.get_chord_notes()
    return notes
