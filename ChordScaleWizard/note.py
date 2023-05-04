import enum

BASE_FREQ = 440

NOTE_MIDI_DICT = {'C': 24, 'D': 26, 'E': 28, 'F': 29, 'G': 31, 'A': 33, 'B': 35, 'C#': 25, 'D#': 27, 'F#': 30, 'G#': 32,
                  'A#': 34}

NOTE_LIST = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']


class NoteSymbol(enum.Enum):
    C = 'C'
    D = 'D'
    E = 'E'
    F = 'F'
    G = 'G'
    A = 'A'
    B = 'B'
    C_DIEZ = 'C#'
    D_DIEZ = 'D#'
    F_DIEZ = 'F#'
    G_DIEZ = 'G#'
    A_DIEZ = 'A#'


class Note:
    def __init__(self, name, octave=3):
        self.name = self.get_name(name)
        self.midi_code = NOTE_MIDI_DICT[self.name] + octave * 12

    def get_name(self, name):
        if isinstance(name, str):
            return name
        return name.value

    def __str__(self):
        return self.name

    @staticmethod
    def validate_note_entry(note):
        if not note:
            print('Music Note Must Be Provided.')
            return False
        elif len(note) > 2 or (len(note) == 2 and note[-1] != '#') or note[0].upper() not in NOTE_LIST:
            print('Invalid Music Note.')
            return False
        return True
