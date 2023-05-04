# Chord Scale Wizard

ChordScaleWizard is a Python project that generates music notes of a scale or a chord, based on user input.

## Installation
To install ChordScaleWizard, you have to approches:
### First Approch
Install package using `pip install ChordScaleWizard` command.
#### How to Use
##### To get a chord's notes
`from ChordScaleWizard.chord import get_chords_notes`
`notes = get_chords_notes('C', 'm7') # returns ['C', 'D#', 'G', 'A#']`
##### To get a scale's notes
`from ChordScaleWizard.scale import get_scale_notes, ScaleName`
`notes = get_scale_notes('C', ScaleName.PENTATONIC) # returns ['C', 'D', 'E', 'G', 'A']`
### Second Approch
By cloning repository:
- Clone the project from Github to your local machine.
- Python 3 must be installed in your enviroment.
- Open a terminal and navigate to the /ChordScaleWizard directory.
### Usage
To use ChordScaleWizard, you can run the following commands in your terminal:

#### Get a scale notes:
To get a scale's notes simply use:

`python harmony_wizard.py -note [music_note] -scale [music_scale]`
##### Example
To get C Pentatonic scale notes:

`python harmony_wizard.py -note C -scale pentatonic`

NOTE: The scales should be chosen from the following list:

###### Possible scale values: 
- pentatonic
- major
- natural_minor
- harmonic_minor
- melodic_minor
- blues
- dorian
- dorian_b2
- mixolydian
- phrygian
- lydian
- lydian_dominant
- bebop_dominant
- altered_scale
- diminished_scale
- whole_tone

NOTE: The music note value should be chosen from the following list:
- C, C#, D, D#, E, F, F#, G, G#, A, A#, B

#### Get a chord notes:
To get a chord notes simple use:

`python harmony_wizard.py -note [root_note] -chord [chord_name]`
##### Example
To generate C#m7b5 chord notes:

`python harmony_wizard.py -note C# -chord m7b5`

NOTE: To get major note write major in chord_name part:

`python harmony_wizard.py -note C# -chord major`

## Conclusion
ChordScaleWizard is a simple yet useful Python project that generates music notes of a scale or a chord. With its easy-to-use commands and detailed instructions, you can easily create your own music scales and chords.

