DEPENDENCIES: mechanize
```
pip install mechanize
```
```
>>> import scraper
>>> browser = scraper.Scraper()
```
```
>>> browser.get_scale_notes('c', 'major')
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```
```
>>> br.get_available_scales()
['major', 'melodic minor', 'ionian', 'harmonic minor', 'natural minor', 'dorian'
, 'phrygian', 'lydian', 'mixolydian', 'aeolian', 'locrian', 'blues', 'diminished
 (halftone - wholetone)', 'diminished (wholetone - halftone)', 'whole tone', 'ma
jor pentatonic', 'minor pentatonic', 'augmented', 'leading whole tone', 'double
harmonic', 'overtone', 'six tone symmetrical', 'altered', 'altered bb7', 'enigma
tic', 'dorian b2', 'augmented lydian', 'lydian b7', 'mixolydian b6', 'locrian 2'
, 'locrian 6', 'augmented ionian', 'dorian #4', 'major phrygian', 'lydian #9', '
diminished lydian', 'minor lydian', 'arabian', 'balinese', 'byzantine', 'chinese
', 'mongolian', 'egyptian', 'eight tone spanish', 'hindu', 'hirajoshi', 'hungari
an major', 'hungarian minor (gipsy)', 'ichikosucho', 'kumoi', 'mohammedan', 'neo
politan', 'neopolitan major', 'neopolitan minor', 'pelog', 'persian', 'prometheu
s', 'prometheus neopolitan', 'purvi theta', 'todi theta']
```
```
>>> browser.get_scale_chords('c', 'major')
['C', 'Dm', 'Em', 'F', 'G', 'Am', 'Bdim', 'Csus4', 'Csus2', 'Dsus4', 'Dsus2', 'E
sus4', 'Fsus2', 'Gsus4', 'Gsus2', 'Asus4', 'Asus2', 'C6', 'Cmaj7', 'Dm6', 'Dm7',
 'D7sus4', 'D7sus2', 'Em7', 'E7sus4', 'F6', 'Fmaj7', 'G6', 'G7', 'G7sus4', 'G7su
s2', 'Am7', 'A7sus4', 'A7sus2', 'Bm7b5', 'C\\E', 'C\\G', 'Csus4\\F', 'Csus4\\G',
 'C6/9', 'Cmaj9', 'Cmaj13', 'Dm9', 'Dm11', 'Dm13', 'D9sus4', 'D9sus2', 'Em11', '
F6/9', 'Fmaj9', 'Fmaj13', 'G6/9', 'G9', 'G13', 'G9sus4', 'G9sus2', 'Am9', 'Am11'
, 'A9sus4', 'A9sus2', 'C6\\G', 'C6/9\\E', 'C6/9\\G', 'Cmaj7\\G', 'Cmaj9\\E']
```
```
>>> for chord in browser.get_scale_chords('c', 'major'):
...  print(chord+': '+str(browser.get_chord_notes(chord)))
...
C: ['C', 'E', 'G']
Dm: ['D', 'F', 'A']
Em: ['E', 'G', 'B']
F: ['F', 'A', 'C']
G: ['G', 'B', 'D']
Am: ['A', 'C', 'E']
Bdim: ['B', 'D', 'F']
Csus4: ['C', 'F', 'G']
Csus2: ['C', 'D', 'G']
Dsus4: ['D', 'G', 'A']
Dsus2: ['D', 'E', 'A']
Esus4: ['E', 'A', 'B']
Fsus2: ['F', 'G', 'C']
Gsus4: ['G', 'C', 'D']
Gsus2: ['G', 'A', 'D']
Asus4: ['A', 'D', 'E']
Asus2: ['A', 'B', 'E']
C6: ['C', 'E', 'G', 'A']
Cmaj7: ['C', 'E', 'G', 'B']
Dm6: ['D', 'F', 'A', 'B']
Dm7: ['D', 'F', 'A', 'C']
D7sus4: ['D', 'G', 'A', 'C']
D7sus2: ['D', 'E', 'A', 'C']
Em7: ['E', 'G', 'B', 'D']
E7sus4: ['E', 'A', 'B', 'D']
F6: ['F', 'A', 'C', 'D']
Fmaj7: ['F', 'A', 'C', 'E']
G6: ['G', 'B', 'D', 'E']
G7: ['G', 'B', 'D', 'F']
G7sus4: ['G', 'C', 'D', 'F']
G7sus2: ['G', 'A', 'D', 'F']
Am7: ['A', 'C', 'E', 'G']
A7sus4: ['A', 'D', 'E', 'G']
A7sus2: ['A', 'B', 'E', 'G']
Bm7b5: ['B', 'D', 'F', 'A']
C\E: ['C', 'E', 'G']
C\G: ['C', 'E', 'G']
Csus4\F: ['C', 'F', 'G']
Csus4\G: ['C', 'F', 'G']
C6/9: ['C', 'E', 'G', 'A', 'D']
Cmaj9: ['C', 'E', 'G', 'B', 'D']
Cmaj13: ['C', 'E', 'G', 'B', 'A']
Dm9: ['D', 'F', 'A', 'C', 'E']
Dm11: ['D', 'F', 'A', 'C', 'G']
Dm13: ['D', 'F', 'A', 'C', 'B']
D9sus4: ['D', 'G', 'A', 'C', 'E']
D9sus2: ['D', 'E', 'A', 'C', 'E']
Em11: ['E', 'G', 'B', 'D', 'A']
F6/9: ['F', 'A', 'C', 'D', 'G']
Fmaj9: ['F', 'A', 'C', 'E', 'G']
Fmaj13: ['F', 'A', 'C', 'E', 'D']
G6/9: ['G', 'B', 'D', 'E', 'A']
G9: ['G', 'B', 'D', 'F', 'A']
G13: ['G', 'B', 'D', 'F', 'E']
G9sus4: ['G', 'C', 'D', 'F', 'A']
G9sus2: ['G', 'A', 'D', 'F', 'A']
Am9: ['A', 'C', 'E', 'G', 'B']
Am11: ['A', 'C', 'E', 'G', 'D']
A9sus4: ['A', 'D', 'E', 'G', 'B']
A9sus2: ['A', 'B', 'E', 'G', 'B']
C6\G: ['C', 'E', 'G', 'A']
C6/9\E: ['C', 'E', 'G', 'A', 'D']
C6/9\G: ['C', 'E', 'G', 'A', 'D']
Cmaj7\G: ['C', 'E', 'G', 'B']
Cmaj9\E: ['C', 'E', 'G', 'B', 'D']
```
```
>>> for note in browser.get_chord_notes('D#m'):
...  print(note+': '+str(browser.get_note_midi_value(note)))
...
D#: 63
Gb: 66
A#: 70
```