import pathlib
pad = 20  # unillateral pad, real pad is 2x
sn, fn = 6, 6  # sn - string number, fn - fret number
Δ = 20  # Delta
w, h = (sn-1)*Δ, (fn-1)*Δ  # width and height
ver = [Δ*i for i in range(fn)]  # Vertical points
hor = [Δ*i for i in range(sn)]  # Horizontal points
gauge = [109, 94, 83, 75, 70, 60]  # Gauge size of strings
G = 3/max(gauge)  # Normalization for String Gauge size

# Color definitions
STRINGS = '#555'
FRETS = '#828282'
CROSS = '#828282'
FINGER_FILL = '#828282'
FINGER_STROKE = '#aaa'
TEXT = '#aaa'

# Dotted frets
dot = [3, 5, 7, 9, 15, 17, 19, 21]
ddot = [12, 24]
x = None


def head(self):
    width, height = w+2*pad, h+2*pad
    # SVG head
    self.write(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{width}" height="{height}" viewBox="-{width/2} -{height/2} {width} {height}">\n')


def fretboard(self, start=0, x0=0.0, y0=0.0):
    start += 1
    frets = list(range(start, start+len(ver)-1))  # Fret span in Diagram
    # Fret Marks
    for fret in frets:
        if fret in dot:
            self.write(
                f'<circle cx="{x0:.1f}" cy="{(h-Δ)/2-(fret-start)*Δ+y0:.1f}" r="3" stroke-width="0" fill="{FRETS}" fill-opacity="0.5"/>\n')
            # self.append(draw.Circle(0+x0, (h-Δ)/2-(fret-start)*Δ+y0,3, stroke_width=0, fill='gray', fill_opacity=0.5))
        elif fret in ddot:
            self.write(
                f'<circle cx="{-w/4+x0:.1f}" cy="{(h-Δ)/2-(fret-start)*Δ+y0:.1f}" r="3" stroke-width="0" fill="{FRETS}" fill-opacity="0.5"/>\n')
            self.write(
                f'<circle cx="{w/4+x0:.1f}" cy="{(h-Δ)/2-(fret-start)*Δ+y0:.1f}" r="3" stroke-width="0" fill="{FRETS}" fill-opacity="0.5"/>\n')
            # self.append(draw.Circle(-w/4+x0, (h-Δ)/2-(fret-start)*Δ+y0, 3, stroke_width=0, fill='gray', fill_opacity=0.5))
            # self.append(draw.Circle(w/4+x0, (h-Δ)/2-(fret-start)*Δ+y0,3, stroke_width=0, fill='gray', fill_opacity=0.5))
    if start != 1:
        self.write(
            f'<text x="{w/2+Δ/4+x0:.1f}" y="{-(h/2-Δ/4+y0):.1f}" font-size="14" font-family="Nunito" fill="{TEXT}" dy="0em">{str(start)}</text>\n')
        # self.append(draw.Text(str(start), 14, w/2 +Δ/4+x0, h/2-Δ/4+y0, fill='#aaa'))
    # Frets
    for dy in ver:
        self.write(
            f'<path d="M{-w/2+x0:.1f},{h/2-dy+y0:.1f} L{w/2+x0:.1f},{h/2-dy+y0:.1f}" stroke="{FRETS}" stroke-width="1" fill="none"/>\n')
        # self.append(draw.Line(-w/2+x0, h/2-dy+y0, w/2+x0, h/2-dy+y0, stroke='gray', stroke_width=1, fill='none'))
    # Strings
    for dx, g in zip(hor, gauge):
        self.write(
            f'<path d="M{-w/2+dx+x0:.1f},{h/2+0.5+y0:.1f} L{-w/2+dx+x0:.1f},{-h/2-0.5+y0:.1f}" stroke="{STRINGS}" stroke-width="3.0" fill="none"/>\n')
        # self.append(draw.Line(-w/2+dx+x0, h/2+0.5+y0, -w/2+dx+x0, -h/2-0.5+y0, stroke='#555', stroke_width=G*g, fill='none'))


def cross(self, sq, x0=0.0, y0=0.0):
    self.write(
        f'<path d="M{-sq+x0:.1f},{-sq+y0:.1f} L{sq+x0:.1f},{sq+y0:.1f}" stroke="{CROSS}" stroke-width="2" fill="none"/>\n')
    self.write(
        f'<path d="M{-sq+x0:.1f},{sq+y0:.1f} L{sq+x0:.1f},{-sq+y0:.1f}" stroke="{CROSS}" stroke-width="2" fill="none"/>\n')

    # self.append(draw.Line(-sq+x0, -sq+y0, sq+x0, sq+y0,stroke=fill, stroke_width=2, fill='none'))
    # self.append(draw.Line(-sq+x0, sq+y0, sq+x0, -sq+y0,stroke=fill, stroke_width=2, fill='none'))


def fingers(self, positions, x0=0.0, y0=0.0):
    for dx, ft in zip(hor, positions):
        try:
            self.write(
                f'<circle cx="{-w/2+dx+x0:.1f}" cy="{-(h/2-20*ft+10+y0):.1f}" r="5" fill="{FINGER_FILL}" stroke-width="2" stroke="{FINGER_STROKE}"/>\n')
            # self.append(draw.Circle(-w/2+dx+x0, h/2-20*ft+10+y0, 5,fill='gray', stroke_width=2, stroke='#aaa'))
        except:
            cross(self, sq=5, x0=-w/2+dx+x0, y0=-(h/2+10+y0))


chords = {}  # initialize Chord dictionary

roots = ['A', 'Bb', 'B', 'C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab']

ochords = {}
qualities = ['', 'm',  # Regular
             '7', '9', '11',  # Extended major
             'm7',  # Extended minor
             'add11',  # Add
             'm7b5'
             ]

exchords = {}
chords_by_root = {}

##########################################################################
# MAJOR
##########################################################################

ochords[''] = {
    'A': [x, 0, 2, 2, 2, 0],
    'C': [x, 3, 2, 0, 1, 0],
    'D': [x, x, 0, 2, 3, 2],
    'E': [0, 2, 2, 1, 0, 0],
    'G': [3, 2, 0, 0, 3, 3]
}

ochords['_3'] = {
    'D_3': [2, x, 0, 2, 3, 2],
    'G_3': [x, 2, 0, 0, 0, x],
    'F_3': [x, 0, 3, 2, 1, 1]
}

ochords['_5'] = {
    'C_5': [3, 3, 2, 0, 1, 0],
    'D_5': [x, 0, x, 2, 3, 2]
}

ochords['_7'] = {
    'C_7': [x, 2, x, 0, 1, 0],
    'A_7': [x, 4, 2, 2, 2, 0]
}

ochords['_m7'] = {
    'D_m7': [x, 3, x, 2, 3, 2]
}

ochords['_6'] = {
    'D_6': [x, 2, x, 2, 3, 2]
}

# 6 chords

ochords['6'] = {
    'G6': [3, 2, 0, 0, 3, 0],
    'A6': [x, 0, 2, 2, 2, 2]
}

# 7 chords

ochords['Δ7'] = {
    'DΔ7': [x, x, 0, 2, 2, 2],
    'GΔ7': [3, x, 0, 0, 3, 2],
    'AΔ7': [x, 0, 2, 1, 2, 0],
    'FΔ7': [1, x, 2, 2, 1, x],
    'EΔ7': [0, 2, 1, 1, 0, 0],
    'CΔ7': [x, 3, 2, 0, 0, 0]
}

# 9 chords

ochords['add9'] = {
    'Gadd9': [3, 2, 0, 2, 3, x]
}

ochords['Δ9'] = {
    'DΔ9': [x, x, 0, 2, 2, 0]
}

# 11 chords

ochords['add11'] = {
    'Gadd11': [3, 2, 0, 0, 1, x]
}

ochords['Δ11'] = {
    'DΔ11': [x, x, 0, 2, 2, 3]
}

# 13 chords

ochords['Δ13'] = {
    'GΔ13': [3, 2, 4, 0, 3, 0],
    'AΔ13': [x, 0, 2, 1, 2, 2]
}


##########################################################################
# MINOR
##########################################################################

ochords['m'] = {
    'Am': [x, 0, 2, 2, 1, 0],
    'Dm': [x, x, 0, 2, 3, 1],
    'Em': [0, 2, 2, 0, 0, 0]
}

ochords['m_m7'] = {
    'Bm_m7': [x, 0, 4, 4, 3, 2],
    'Dm_m7': [x, 3, x, 2, 3, 1],
    'Am_m7': [3, x, 2, 2, 1, 0]
}

ochords['m_2'] = {
    'Am_2': [x, 2, 2, 2, 1, 0]
}

# 6 chords

ochords['m6'] = {
    'Am6': [x, 0, 2, 2, 1, 2],
    'Em6': [0, 2, 2, 0, 2, 0],
    'Dm6': [x, x, 0, 2, 0, 1]
}

ochords['m6_6'] = {
    'Am6_6': [2, 0, 2, 2, 1, 2],
    'Dm6_6': [x, 2, 0, 2, 0, 1]
}

# 7 chords

ochords['m7'] = {
    'Am7': [x, 0, 2, 0, 1, 0],
    'Dm7': [x, x, 0, 2, 1, 1],
    'Em7': [0, 2, 0, 0, 0, 0]
}

ochords['m7_m7'] = {
    'Bm7_m7': [x, 0, 4, 2, 3, 2],
    'Dm7_m7': [x, 3, x, 2, 1, 1],
    'Am7_m7': [3, x, 2, 0, 1, 0]
}

# Δ7 chords

ochords['mΔ7'] = {
    'EmΔ7': [0, 2, 1, 0, 0, 0],
    'DmΔ7': [x, x, 0, 2, 2, 1],
    'AmΔ7': [x, 0, 2, 1, 1, 0]
}

ochords['mΔ7_7'] = {
    'DmΔ7_7': [x, 4, x, 2, 2, 1]
}

# 9 chords

ochords['madd9'] = {
    'Emadd9': {0, 2, 2, 0, 0, 2}
}

ochords['m9'] = {
    'Em9': [0, 2, 0, 0, 0, 2],
    'Bm9': [x, 2, 0, 2, 2, x]
}

##########################################################################
# DOMINANT
##########################################################################

# 7 chords
ochords['7'] = {
    'A7': [x, 0, 2, 0, 2, 0],
    'D7': [x, x, 0, 2, 1, 2],
    'E7': [0, 2, 0, 1, 0, 0],
    'B7': [x, 2, 1, 2, 0, 2]
}

ochords['7_7'] = {
    'A7_7': [x, 4, 2, 0, 2, 0]
}

# 9 chords

ochords['9'] = {
    'A9': [x, 0, 2, 0, 0, 0],
    'B9': [x, 2, 1, 2, 2, x],
    'D9': [x, x, 0, 2, 1, 0]
}

# 11 chords

ochords['11'] = {
    'A11': [x, 0, 2, 0, 3, x],
    'D11': [x, x, 0, 2, 1, 3],
    'B11': [x, 2, 1, 2, 0, 0],
    'E11': [0, 2, 0, 2, 0, 0]
}

# ♯9 chords

ochords['7s9'] = {
    'E7s9': [x, x, 3, 2, 4, 4]
}


##########################################################################
# SUSPENDED
##########################################################################

# 2 chords

ochords['sus2'] = {
    'Asus2': [x, 0, 2, 2, 0, 0],
    'Dsus2': [x, x, 0, 2, 3, 0]
}

ochords['sus2_3'] = {
    'Dsus2_3': [2, x, 0, 2, 3, 0],
    'Fsus2_3': [x, 0, 3, 5, 6, 3]
}

ochords['sus2_7'] = {
    'Asus2_7': [4, x, 0, 2, 2, 0]
}

ochords['sus2s5'] = {
    'Dsus2s5': [x, x, 0, 3, 3, 0]
}

ochords['sus4'] = {
    'Asus4': [x, 0, 2, 2, 3, 0],
    'Dsus4': [x, x, 0, 2, 3, 3],
    'Esus4': [0, 2, 2, 2, 0, 0]
}

ochords['5'] = {
    'D5': [x, x, 0, 2, 3, 5],
    'E5': [0, 2, 2, x, x, x]
}

ochords['b5'] = {
    'Db5': [x, x, 0, 1, 3, x],
    'Ab5': [x, 0, 1, 2, x, x],
    'Eb5': [0, 1, 2, x, x, x]
}

ochords['sus2b5'] = {
    'Asus2b5': [x, 0, 1, 2, 3, x],
    'Dsus2b5': [x, x, 0, 1, 3, 0]
}


##########################################################################
# DINIMISHED
##########################################################################

ochords['m7b5'] = {
    'Am7b5': [x, 0, 1, 0, 1, x],
    'Em7b5': [0, 1, 2, 0, 3, 0]
}

ochords['°7'] = {
    'Bb°7': [x, 1, 2, 0, 2, x],
    'D°7': [x, x, 0, 1, 0, 1]
}

ochords['°'] = {
    'A°': [x, 0, 1, 2, 1, x],
    'E°': [0, 1, 2, 3, x, x]
}


##########################################################################
# AUGMENTED
##########################################################################

ochords['+'] = {
    'A+': [x, 0, 3, 2, 2, 1],
    'D+': [x, x, 0, 3, 3, 2],
    'G+': [3, 2, x, 0, 4, 3]
}


qualities = [key for key in ochords.keys()]
for q in qualities:
    exchords[q] = {}


def get_chord_variants(ROOT, quality):
    for base in ochords[quality]:
        base_root = base.replace(quality, '')
        indx = roots.index(base_root)
        exchords[quality][base] = {}
        for i in range(12):
            new = roots[(indx+i) % 12]
            cd = [st+i if st != x else x for st in ochords[quality][base]]
            exchords[quality][base][new] = cd

    for root in roots:
        chords_by_root[root] = [exchords[quality][base][root]
                                for base in ochords[quality]]
    prepared = [[i for i in form if i != None]
                for form in chords_by_root[ROOT]]
    indices = [min(form) for form in prepared]
    indices_copy = [min(form) for form in prepared]
    indx = []
    for i in range(len(indices)):
        j = min(indices_copy)
        indx += [indices.index(j)]
        indices_copy.remove(j)
    dic = {ROOT+quality+'_' +
           str(i): chords_by_root[ROOT][indx[i]] for i in range(len(indx))}
    dic[ROOT+quality] = dic[ROOT+quality+'_0']
    chords[ROOT+quality] = dic[ROOT+quality]


for quality in qualities:
    for ROOT in roots:
        get_chord_variants(ROOT, quality)


def createDiagram(chord):
    save_file = open(f'chords/{chord}.svg', 'w')
    head(save_file)
    save_file.close()

    save_file = open(f'chords/{chord}.svg', 'a')
    positions = [pos for pos in chords[chord] if pos != None]
    if max(positions) < fn:
        MIN = 0
    elif min(positions) != 0:
        MIN = min(positions)-2
    else:
        MIN = list(set(positions))[1]-2
    fretboard(save_file, MIN, x0=-Δ/2)
    POS = [pos-MIN if pos != x else x for pos in chords[chord]]
    fingers(save_file, POS, x0=-Δ/2)

    save_file.write('</svg>')

    save_file.close()


for chord in chords:
    createDiagram(chord)
