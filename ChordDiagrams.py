import drawSvg as draw

pad = 20
sn,fn = 6,6
Δ = 20
w,h = (sn-1)*Δ,(fn-1)*Δ
ver = [Δ*i for i in range(fn)]
hor = [Δ*i for i in range(sn)]
gauge = [109,94,83,75,70,60]
G = 3/max(gauge)

def cross(self,sq,x0=0,y0=0,fill='black'):
    self.append(draw.Line(-sq+x0, -sq+y0, sq+x0, sq+y0,stroke=fill, stroke_width=2, fill='none'))
    self.append(draw.Line(-sq+x0, sq+y0, sq+x0, -sq+y0,stroke=fill, stroke_width=2, fill='none'))

dot = [3,5,7,9,15,17,19,21]
ddot = [12,24]

def fretboard(self,start=0,x0=0,y0=0):
    start = start+1
    frets = list(range(start,start+len(ver)-1)) # Fret span in Diagram
    # Fret Marks
    for fret in frets:
        if fret in dot:
            self.append(draw.Circle(0+x0,(h-Δ)/2-(fret-start)*Δ+y0,3,stroke_width=0,fill='gray',fill_opacity=0.5))
        elif fret in ddot:
            self.append(draw.Circle(-w/4+x0,(h-Δ)/2-(fret-start)*Δ+y0,3,stroke_width=0,fill='gray',fill_opacity=0.5))
            self.append(draw.Circle(w/4+x0,(h-Δ)/2-(fret-start)*Δ+y0,3,stroke_width=0,fill='gray',fill_opacity=0.5))
    if start!=1:
        self.append(draw.Text(str(start), 14, w/2+Δ/4+x0, h/2-Δ/4+y0,fill='#aaa'))
    # Frets
    for dy in ver:
        self.append(draw.Line(-w/2+x0,h/2-dy+y0,w/2+x0,h/2-dy+y0,stroke='gray',stroke_width=1,fill='none'))
    # Strings
    for dx,g in zip(hor,gauge):
        self.append(draw.Line(-w/2+dx+x0,h/2+0.5+y0,-w/2+dx+x0,-h/2-0.5+y0,stroke='#555',stroke_width=G*g,fill='none'))

def fingers(self,positions,x0=0,y0=0):
    for dx,ft in zip(hor,positions):
        try:
            self.append(draw.Circle(-w/2+dx+x0, h/2-20*ft+10+y0, 5,fill='gray', stroke_width=2, stroke='#aaa'))
        except:
            self.cross(5,-w/2+dx+x0,h/2+10+y0,fill='gray')

draw.Drawing.fingers = fingers
draw.Drawing.fretboard = fretboard
draw.Drawing.cross = cross
x = None

chords = {
    'D':[x,x,0,2,3,2],
    'Dmaj7':[x,x,0,2,2,2],
    'D7':[x,x,0,2,1,2],
    'E':[0,2,2,1,0,0],
    'A':[x,0,2,2,2,0],
    'G':[3,2,0,0,3,3],
    'C':[x,3,2,0,1,0],
    'B':[x,2,4,4,4,2],
    'Am':[x,0,2,2,1,0],
    'Em':[0,2,2,0,0,0],
    'F':[1,3,3,2,1,1],
    'Gb':[2,4,4,3,2,2],
    'Ab':[4,6,6,5,4,4],
    'Bb':[6,8,8,7,6,6],
    'Eb':[11,13,13,12,11,11],
    'Db':[9,11,11,10,9,9],
    'Gb':[2,4,4,3,2,2],
    'Ab':[4,6,6,5,4,4],
    'Bb':[6,8,8,7,6,6],
    'Eb':[x,6,5,3,4,3],
    'Db':[x,4,3,1,2,1],
    'Abm':[4,6,6,4,4,4],
    'Bbm':[x,4,6,6,5,4],
    'Gbm':[2,4,4,2,2,2],
    'F7':[2,4,2,3,2,2]
}

roots = ['A','Bb','B','C','Db','D','Eb','E','F','Gb','G','Ab']

ochords = {}
qualities = ['','m', # Regular
'7','9','11', # Extended major
'm7', # Extended minor
'add11', # Add
'm7b5'
]

exchords = {}
chords_by_root = {}

ochords[''] = {
    'A':[x,0,2,2,2,0],
    'C':[x,3,2,0,1,0],
    'D':[x,x,0,2,3,2],
    'E':[0,2,2,1,0,0],
    'G':[3,2,0,0,3,3]
}

ochords['m'] = {
    'Am':[x,0,2,2,1,0],
    'Dm':[x,x,0,2,3,1],
    'Em':[0,2,2,0,0,0]
}

ochords['7'] = {
    'A7':[x,0,2,0,2,0],
    'D7':[x,x,0,2,1,2],
    'E7':[0,2,0,1,0,0],
    'B7':[x,2,1,2,0,2]
}

ochords['9'] = {
    'A9':[x,0,2,0,0,0],
    'B9':[x,2,1,2,2,x],
    'D9':[x,x,0,2,1,0]
}

ochords['11'] = {
    'A11':[x,0,2,0,3,x],
    'D11':[x,x,0,2,1,3],
    'B11':[x,2,1,2,0,0],
    'E11':[0,2,0,2,0,0]
}

ochords['m7'] = {
    'Am7':[x,0,2,0,1,0],
    'Dm7':[x,x,0,2,1,1],
    'Em7':[0,2,0,0,0,0]
}

ochords['add11'] = {
    'Gadd11':[3,2,0,0,1,x]
}

ochords['sus2'] = {
    'Asus2':[x,0,2,2,0,0],
    'Dsus2':[x,x,0,2,3,0]
}

ochords['sus4'] = {
    'Asus4':[x,0,2,2,3,0],
    'Dsus4':[x,x,0,2,3,3]
}

ochords['m7b5'] = {
    'Am7b5':[x,0,1,0,1,x],
    'Em7b5':[0,1,2,0,3,0]
}

ochords['°7'] = {
    'B°7':[x,2,3,1,3,x],
    'D°7':[x,x,0,1,0,1]
}

qualities = [key for key in ochords.keys()]
for q in qualities:
    exchords[q] = {}

def get_chord_variants(ROOT,quality):
    for base in ochords[quality]:
        base_root = base.replace(quality,'')
        indx = roots.index(base_root)
        exchords[quality][base] = {}
        for i in range(12):
            new = roots[(indx+i)%12]
            cd = [st+i if st!=x else x for st in ochords[quality][base]]
            exchords[quality][base][new] = cd

    for root in roots:
        chords_by_root[root] = [exchords[quality][base][root] for base in ochords[quality]]
    prepared = [[i for i in form if i!=None] for form in chords_by_root[ROOT]]
    indices = [min(form) for form in prepared]
    indices_copy = [min(form) for form in prepared]
    indx = []
    for i in range(len(indices)):
        j = min(indices_copy)
        indx+=[indices.index(j)]
        indices_copy.remove(j)
    dic = {ROOT+quality+'_'+str(i):chords_by_root[ROOT][indx[i]] for i in range(len(indx))}
    dic[ROOT+quality] = dic[ROOT+quality+'_0']
    chords[ROOT+quality]=dic[ROOT+quality]

for quality in qualities:
    for ROOT in roots:
        get_chord_variants(ROOT,quality)

# chords = {'Db':[9,11,11,10,9,9]}
#　お名前わ

import pathlib
path = str(pathlib.Path(__file__).parent.resolve()) # Automated path retriever

def create_Diagram(chord):
    d = draw.Drawing(w+2*pad, h+2*pad, origin='center', displayInline=False)
    # d.append(draw.Text(chord, 18, 0, (h+Δ)/2,center=1,fill='#aaa'))
    positions = [pos for pos in chords[chord] if pos!=None]
    if max(positions)<fn:
        MIN = 0
    elif min(positions)!=0:
        MIN = min(positions)-2
    else:
        MIN = list(set(positions))[1]-2
    d.fretboard(MIN,x0=-Δ/2)
    POS = [pos-MIN if pos!=x else x for pos in chords[chord]]
    d.fingers(POS,x0=-Δ/2)
    d.saveSvg(path+'\\chords\\'+f'{chord}.svg')

for chord in chords:
    create_Diagram(chord)