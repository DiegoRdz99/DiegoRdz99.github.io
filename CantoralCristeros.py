from math import ceil

class constants:
    def __init__(self):
        self.navbar = f'<body><div><div class="navbar">\n<a href="../Misa/index.html">Misa</a>\n<a href="../Hora Santa/index.html">Hora Santa</a>\n<a href="../index.html">Todos los Cantos</a></div></div>\n<div class="main">\n'

html_constants = constants()

def chordify(chord):
    try:
        root = chord[0] # Root　根
        og_root = chord[0] # Root with # and b (kept for removing)
        try:
            if chord[1]=='#':
                root += '♯' # Sharp accidental
                og_root += '#'
            elif chord[1]=='b':
                root+= '♭' # Flat accidental
                og_root+= 'b'
            qual = chord.replace(og_root,'') # Remove root from chord
            return [root,qual] # Root + Quality
        except:
            return [root,''] # For Major Chords
    except:
        return ['',''] # Blank Chords

class line:
    def __init__(self,raw):
        lst = [raw.split('[')[i].split(']') for i in range(len(raw.split('[')))] # Separate chords from text
        if len(lst[0])==1:
            lst[0]=['']+lst[0] # For lines beginning with chords
        lst = [list(i) for i in zip(*lst)] # Transpose algorithm
        chords = [chordify(chord) for chord in lst[0]]
        self.c_line = ''.join([f'<td class="chord"><span class="root">{chord[0]}</span><span class="quality">{chord[1]}</span><div class="diagram"><span class="chord_name">{chord[0]}{chord[1]}</span><img class="fig" src="../chords/{chord[0]}{chord[1]}.svg"></div></td>' if chord[0]!='' else f'<td class="chord">{chord[0]}</td>' for chord in chords])
        # Chord line table
        self.l_line = ''.join([f'<td>{frag}</td>' for frag in lst[1]])

    def table(self):
        return f'\n<table class="linewithchord" border="0" cellpadding="0" cellspacing="0">\n<tr class="chordline">{self.c_line}</tr>\n<tr class="lyricsline">{self.l_line}</tr>\n</table>'

class chord_line(line):
    def __init__(self,raw):
        super().__init__(raw)

# print(line('[E] [A] [B] [C]').c_line)

class Chorus:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;') # Spaces in html
    
    def to_html(self):
        head = f'\n<br><span class="header chorus">Coro</span><br>\n<table class="chorus" border="0" cellpadding="0" cellspacing="0"><tr><td>'
        foot = '</td></tr></table>\n<br>\n'
        lines = [line(raw) for raw in self.raw.split('\n')]
        html = '\n'.join([lin.table() for lin in lines])
        return head + html + foot

class verse:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;')
    
    def to_html(self):
        head = f'\n<br><span class="header verse">Verso</span><br>\n<table class="verse" border="0" cellpadding="0" cellspacing="0"><tr><td>'
        foot = '</td></tr></table>'
        lines = [line(raw) for raw in self.raw.split('\n')]
        html = '\n'.join([lin.table() for lin in lines])
        return head + html + foot

class chorus:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;')

    def include_coro(self,Coro):
        self.coro = Coro
    
    def to_html(self):
        return self.coro.to_html()

class intro:
    def __init__(self,raw):
        self.raw = raw.replace(' ','$nbsp;')


parts = {'Coro':Chorus,'coro':chorus,'verse':verse}

class song:
    def __init__(self,file_name):
        self.raw = open(file_name,'r',encoding='utf-8').read()
        spt = self.raw.split('\n')
        self.title = spt[0]
        self.subtitle = spt[1]
        self.key = spt[2]
        self.composer = spt[3]
        self.parts = self.raw.split('/')
        self.groups = [(self.parts[2*i-1],self.parts[2*i]) for i in range(1,ceil(len(self.parts)/2))]
        self.teile = [parts[group[0]](group[1]) for group in self.groups]
        self.Coro = [teil for teil in self.teile if isinstance(teil,Chorus)][0]
        for teil in self.teile:
            try:
                teil.include_coro(self.Coro)
            except:
                pass
        head = f'<html><head>\n<title>{self.title}</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<link rel="stylesheet" href="../css/style.css"></head>'
        title_table = f'<table class="main" border=0px width="100%">\n<col style="width:25%"><col style="width:30%"><col style="width:20%"><col style="width:20%"><tr><th colspan="3"><h1>{self.title}</h1></th></tr><tr><th><h2>{self.composer}</h2></th><th><h2>{self.subtitle}</h2></th><th><h2>Clave: {self.key}</h2></th></tr>\n</table>'
        control_bar = f'<div>\n<div class="control_bar">\n<label id="up" onclick="tpup()"><div class="icon">+1</div></label>\n<label id="down" onclick="tpdown()"><div class="icon">-1</div></label>\n<label onclick="tr_capo()"><span class="icon" id="tr-capo">Transpose</span><sup id="count" class="super"></sup></label>\n<label onclick="ft_sp()" id="b_but"><span class="icon">&nbsp;&flat;&nbsp;</span></label>\n</div>\n</div>'
        self.html_preamble = head + html_constants.navbar + title_table + control_bar
        self.html_footer = r'<script src="../js/script.js"></script></body></html>'
    def to_html(self):
        html = '\n'.join([teil.to_html() for teil in self.teile])
        return self.html_preamble + '\n' + html + '\n'+ self.html_footer

def create_html(file_path):
    file_name = file_path.split('\\')[-1][:-4]
    # name_ext = file_name.split('.')[0]
    name_ext = '\\'.join(file_path.split('\\')[:-1])
    newfile = open(f'{name_ext}\\{file_name}.html','w',encoding='utf-8')
    newfile.write(song(file_path).to_html())
    newfile.close()

def create_index(folder_path):
    folder_name = folder_path.split('\\')[-1]
    head = f'<html><head>\n<title>{folder_name}</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<link rel="stylesheet" href="../css/style.css"></head>'
    preamble = head + html_constants.navbar + f'<h1 style="text-align: center;">{folder_name}</h1>\n<div class="listing">\n<ul>\n'
    dirs = os.listdir(folder_path)
    songs = [i for i in dirs if i[-5:]=='.html']
    if songs!=[]:
        try:
            songs.remove('index.html')
        except:
            pass
        for song in songs:
            preamble += f'<a href="{song}"><li>{song[:-5]}</li></a>\n'
        footer = '</ul>\n</div>\n</div>\n</body>\n</html>'
        html = preamble + footer
        newfile = open(f'{folder_path}\\index.html','w',encoding='utf-8')
        newfile.write(html)
        newfile.close()


import os
import pathlib
path = pathlib.Path(__file__).parent.resolve() # Automated path retriever
dirs = os.listdir(path)
# files = [i for i in dirs if i.find('.')!=-1]
folders = [str(path)+'\\'+i for i in dirs if i.find('.')==-1]
abc_songs = []
for folder in folders:
    dirs = os.listdir(folder)
    songs = [i for i in dirs if i[-4:]=='.txt']
    for s in songs:
        create_html(folder+'\\'+s)
        abc_songs+=[(s,folder.split('\\')[-1]+'\\')]
    create_index(folder)

def create_global_index(songs,path):
    head = f'<html><head>\n<title>Global Index</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<link rel="stylesheet" href="./css/style.css"></head>'
    navbar = f'<body><div><div class="navbar">\n<a href="./Misa/index.html">Misa</a>\n<a href="./Hora Santa/index.html">Hora Santa</a>\n<a href="index.html">Todos los Cantos</a></div></div>\n<div class="main">\n<h1 style="text-align: center;">Índice Alfabético </h1>\n<div class="listing">\n<ul>\n'
    preamble = head + navbar
    for song in songs:
        preamble += f'<a href="{song[1]}{song[0]}"><li>{song[0][:-5]}</li></a>\n'
    footer = '</ul>\n</div>\n</div>\n</body>\n</html>'
    html = preamble + footer
    newfile = open(f'{path}\\index.html','w',encoding='utf-8')
    newfile.write(html)
    newfile.close()

abc_songs.sort(key=lambda tup: tup[0])
abc_songs = [(i[0].replace('.txt','.html'),i[1]) for i in abc_songs]
create_global_index(abc_songs,path)

# for s in songs:
#     create_html(s)