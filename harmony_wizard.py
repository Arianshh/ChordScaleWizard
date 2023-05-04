import sys

from ChordScaleWizard.note import Note
from ChordScaleWizard.scale import Scale, ScaleName
from ChordScaleWizard.chord import Chord

VALID_REQUESTS = ['scale', 'chord']


def main():
    args = {}
    for i in range(1, len(sys.argv), 2):
        if i + 1 < len(sys.argv):
            args[sys.argv[i][1:]] = sys.argv[i + 1]

    note = args.get('root_note', None)
    if Note.validate_note_entry(note):
        scale = args.get('scale', None)
        chord = args.get('chord', None)
        if not scale and not chord:
            print('No Command Found.')
        elif scale and chord:
            print('Use one of two -scale and -chord commands only.')
        elif scale:
            if Scale.validate_scale_entry(scale):
                scale_obj = Scale([s for s in ScaleName if s.value == scale][0], note.upper())
                print('{} {} Scale Notes: '.format(note.upper(), scale))
                notes = []
                for note in scale_obj.notes:
                    notes += [note.name]
                print(' '.join(notes))
        elif chord:
            chord_obj = Chord(chord, note)
            print('Extracting {} chord notes...'.format(note + chord))
            print(chord_obj.get_chord_notes())


if __name__ == '__main__':
    main()
