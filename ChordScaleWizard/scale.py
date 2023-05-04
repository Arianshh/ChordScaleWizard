import enum

from .note import Note, NOTE_LIST


class ScaleName(enum.Enum):
    PENTATONIC = 'pentatonic'
    MAJOR = 'major'
    NATURAL_MINOR = 'natural_minor'
    HARMONIC_MINOR = 'harmonic_minor'
    MELODIC_MINOR = 'melodic_minor'
    BLUES = 'blues'
    DORIAN = 'dorian'
    DORIANB2 = 'dorian_b2'
    MIXOLYDIAN = 'mixolydian'
    PHRYGIAN = 'phrygian'
    LYDIAN = 'lydian'
    LYDIAN_DOMINANT = 'lydian_dominant'
    BEPOP_DOMINANT = 'bebop_dominant'
    ALTERED = 'altered_scale'
    DIMINISHED_SCALE = 'diminished_scale'
    WHOLE_TUNE = ' whole_tone'


class Scale:
    def __init__(self, name, note):
        self.name = name
        if isinstance(note, Note):
            note = note.value
        self.note = Note(name=note)
        self.set_notes()

    def set_notes(self):
        if self.name == ScaleName.PENTATONIC:
            self.notes = self.generate_scale([2, 2, 3, 2, 3])
        elif self.name == ScaleName.MAJOR:
            self.notes = self.generate_scale([2, 2, 1, 2, 2, 2, 1])
        elif self.name == ScaleName.NATURAL_MINOR:
            self.notes = self.generate_scale([2, 1, 2, 2, 1, 2, 2])
        elif self.name == ScaleName.HARMONIC_MINOR:
            self.notes = self.generate_scale([3, 2, 1, 1, 3, 2])
        elif self.name == ScaleName.MELODIC_MINOR:
            self.notes = self.generate_scale([3, 2, 1, 1, 3, 2])
        elif self.name == ScaleName.BLUES:
            self.notes = self.generate_scale([3, 2, 1, 1, 3, 2])
        elif self.name == ScaleName.DORIAN:
            self.notes = self.generate_scale([2, 1, 2, 2, 2, 1, 2])
        elif self.name == ScaleName.MIXOLYDIAN:
            self.notes = self.generate_scale([2, 2, 1, 2, 2, 1, 2])

        # JAZZY
        elif self.name == ScaleName.BEPOP_DOMINANT:
            self.notes = self.generate_scale([2, 2, 1, 2, 1, 1, 1, 2])
        elif self.name == ScaleName.ALTERED:
            self.notes = self.generate_scale([1, 2, 1, 2, 2, 2, 1])
        elif self.name == ScaleName.DORIANB2:
            self.notes = self.generate_scale([1, 2, 1, 2, 2, 1, 2])
        elif self.name == ScaleName.LYDIAN_DOMINANT:
            self.notes = self.generate_scale([2, 2, 2, 1, 2, 1, 1])
        elif self.name == ScaleName.DIMINISHED_SCALE:
            self.notes = self.generate_scale([1, 2, 1, 2, 1, 2, 1, 2])
        elif self.name == ScaleName.WHOLE_TUNE:
            self.notes = self.generate_scale([2, 2, 2, 2, 2, 2])

    def generate_scale(self, intervals):
        start_index = NOTE_LIST.index(self.note.name)
        scale = [self.note]
        for interval in intervals:
            next_index = (start_index + interval) % len(NOTE_LIST)
            if NOTE_LIST[next_index] != self.note.name:
                scale.append(Note(NOTE_LIST[next_index]))
            start_index = next_index
        return scale

    @staticmethod
    def validate_scale_entry(scale):
        if scale not in [s.value for s in ScaleName]:
            print('Wrong Scale Entry.')
            return False
        return True


def get_scale_notes(note, scale):
    scale_obj = Scale(scale, note.upper())
    notes = []
    for note in scale_obj.notes:
        notes += [note.name]
    return notes
