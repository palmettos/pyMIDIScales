DEPENDENCIES: mechanize
```
>>> browser = scraper.Scraper()
```
```
>>> browser.get_scale_notes('c', 'major')
['C', 'D', 'E', 'F', 'G', 'A', 'B']
```
```
>>> browser.get_scale_chord_links('c', 'major')
{'Dm13': '/showchord.php?ch=Dm13', 'Gsus4': '/showchord.php?ch=Gsus4', 'Bdim': '
/showchord.php?ch=Bdim', 'Gsus2': '/showchord.php?ch=Gsus2', 'Fmaj9': '/showchor
d.php?ch=Fmaj9', 'Fmaj7': '/showchord.php?ch=Fmaj7', 'Csus4': '/showchord.php?ch
=Csus4', 'Cmaj7\\G': '/showchord.php?ch=Cmaj7\\G', 'Csus2': '/showchord.php?ch=C
sus2', 'Em7': '/showchord.php?ch=Em7', 'Dm11': '/showchord.php?ch=Dm11', 'Fmaj13
': '/showchord.php?ch=Fmaj13', 'Cmaj7': '/showchord.php?ch=Cmaj7', 'Dm6': '/show
chord.php?ch=Dm6', 'Dm7': '/showchord.php?ch=Dm7', 'Dm9': '/showchord.php?ch=Dm9
', 'Cmaj9': '/showchord.php?ch=Cmaj9', 'G7': '/showchord.php?ch=G7', 'Esus4': '/
showchord.php?ch=Esus4', 'Dm': '/showchord.php?ch=Dm', 'Fsus2': '/showchord.php?
ch=Fsus2', 'Asus4': '/showchord.php?ch=Asus4', 'A7sus4': '/showchord.php?ch=A7su
s4', 'G9': '/showchord.php?ch=G9', 'E7sus4': '/showchord.php?ch=E7sus4', 'Dsus4'
: '/showchord.php?ch=Dsus4', 'G7sus2': '/showchord.php?ch=G7sus2', 'G7sus4': '/s
howchord.php?ch=G7sus4', 'Dsus2': '/showchord.php?ch=Dsus2', 'Bm7b5': '/showchor
d.php?ch=Bm7b5', 'C6': '/showchord.php?ch=C6', 'Em11': '/showchord.php?ch=Em11',
 'C6\\G': '/showchord.php?ch=C6\\G', 'C': '/showchord.php?ch=C', 'A9sus2': '/sho
wchord.php?ch=A9sus2', 'G': '/showchord.php?ch=G', 'F': '/showchord.php?ch=F', '
D7sus2': '/showchord.php?ch=D7sus2', 'C6/9': '/showchord.php?ch=C6/9', 'D7sus4':
 '/showchord.php?ch=D7sus4', 'A9sus4': '/showchord.php?ch=A9sus4', 'C6/9\\E': '/
showchord.php?ch=C6/9\\E', 'D9sus4': '/showchord.php?ch=D9sus4', 'Asus2': '/show
chord.php?ch=Asus2', 'D9sus2': '/showchord.php?ch=D9sus2', 'G13': '/showchord.ph
p?ch=G13', 'G6/9': '/showchord.php?ch=G6/9', 'A7sus2': '/showchord.php?ch=A7sus2
', 'Em': '/showchord.php?ch=Em', 'Cmaj9\\E': '/showchord.php?ch=Cmaj9\\E', 'G9su
s4': '/showchord.php?ch=G9sus4', 'G6': '/showchord.php?ch=G6', 'F6': '/showchord
.php?ch=F6', 'Am': '/showchord.php?ch=Am', 'C6/9\\G': '/showchord.php?ch=C6/9\\G
', 'Am9': '/showchord.php?ch=Am9', 'Am11': '/showchord.php?ch=Am11', 'F6/9': '/s
howchord.php?ch=F6/9', 'Csus4\\G': '/showchord.php?ch=Csus4\\G', 'Cmaj13': '/sho
wchord.php?ch=Cmaj13', 'C\\E': '/showchord.php?ch=C\\E', 'C\\G': '/showchord.php
?ch=C\\G', 'G9sus2': '/showchord.php?ch=G9sus2', 'Am7': '/showchord.php?ch=Am7',
 'Csus4\\F': '/showchord.php?ch=Csus4\\F'}
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