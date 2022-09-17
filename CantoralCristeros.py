from math import ceil

class constants:
    def __init__(self,backsteps):
        self.navbar = f'<body><div><div class="navbar">\n<a href="{backsteps}Misa/index.html">Misa</a>\n<a href="{backsteps}María/index.html">María</a>\n<a href="{backsteps}Hora Santa/index.html">Hora Santa</a>\n<a href="{backsteps}Himnos/index.html">Himnos</a>\n<a href="{backsteps}Alabanzas/index.html">Alabanzas</a>\n<a href="{backsteps}Semana Santa/index.html">Semana Santa</a>\n<a href="{backsteps}Villancicos/index.html">Villancicos</a>\n<a href="{backsteps}Adicionales/index.html">Adicionales</a>\n<a href="{backsteps}Niños/index.html">Niños</a>\n<a href="{backsteps}index.html">Todos los Cantos</a></div></div>\n<div class="main">\n'

def chordify(chord):
    try:
        root = chord[0] # Root 根
        og_root = chord[0] # Root with # and b (kept for removing)
        FLAT = True
        try:
            if chord[1]=='#':
                root += '♯' # Sharp accidental
                og_root += '#'
                FLAT = False
            elif chord[1]=='b':
                root+= '♭' # Flat accidental
                og_root+= 'b'
            qual = chord.replace(og_root,'') # Remove root from chord
            return [root,qual,FLAT,og_root,qual.replace('b','♭')] # Root + Quality
        except:
            return [root,'',FLAT,og_root,''] # For Major Chords
    except:
        return ['','',False,'',''] # Blank Chords

def iterate(root):
    return chr((ord(root)-ord('A')+1)%7+ord('A'))

class line:
    def __init__(self,raw,backsteps):
        lst = [raw.split('[')[i].split(']') for i in range(len(raw.split('[')))] # Separate chords from text
        if len(lst[0])==1:
            lst[0]=['']+lst[0] # For lines beginning with chords
        lst = [list(i) for i in zip(*lst)] # Transpose algorithm
        chords = [chordify(chord) for chord in lst[0]]
        self.c_line = ''.join([f'<td class="chord"><span class="root">{chord[0]}</span><span class="quality">{chord[-1]}</span><div class="diagram"><span class="chord_name">{chord[0]}{chord[-1]}</span><img class="fig" src="{backsteps}chords/{chord[3]}{chord[1]}.svg"></div></td>' if chord[2] else f'<td class="chord"><span class="root">{chord[0]}</span><span class="quality">{chord[1]}</span><div class="diagram"><span class="chord_name">{chord[0]}{chord[1]}</span><img class="fig" src="{backsteps}chords/{iterate(chord[0][0])}b{chord[1]}.svg"></div></td>' if chord[0]!='' else f'<td class="chord">{chord[0]}</td>' for chord in chords])
        # Chord line table
        self.l_line = ''.join([f'<td>{frag}</td>' for frag in lst[1]])

    def table(self):
        return f'\n<table class="linewithchord" border="0" cellpadding="0" cellspacing="0">\n<tr class="chordline">{self.c_line}</tr>\n<tr class="lyricsline">{self.l_line}</tr>\n</table>'


class Chorus:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;') # Spaces in html
    
    def to_html(self,backsteps):
        head = f'\n<br><span class="header chorus">Coro</span><br>\n<table class="chorus" border="0" cellpadding="0" cellspacing="0"><tr><td>'
        foot = '</td></tr></table>\n<br>\n'
        lines = [line(raw,backsteps) for raw in self.raw.split('\n')]
        html = '\n'.join([lin.table() for lin in lines])
        return head + html + foot

class chorus:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;')

    def include_coro(self,Coro):
        self.coro = Coro
    
    def to_html(self,backsteps):
        return self.coro.to_html(backsteps)

class verse:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;')
        self.title = 'Verso'
        self.klass = 'verse'
    
    def to_html(self,backsteps):
        head = f'\n<br><span class="header {self.klass}">{self.title}</span><br>\n<table class="{self.klass}" border="0" cellpadding="0" cellspacing="0"><tr><td>'
        foot = '</td></tr></table>'
        lines = [line(raw,backsteps) for raw in self.raw.split('\n')]
        html = '\n'.join([lin.table() for lin in lines])
        return head + html + foot

class prechorus(verse):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Pre-coro'
        self.klass = 'pre-chorus'

class bridge(verse):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Puente'
        self.klass = 'pre-chorus'

class intermedio(verse):
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;&nbsp;')
        self.title = 'Intermedio'
        self.klass = 'inst'

class intro(intermedio):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Intro'
    
class outro(intermedio):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Outro'


parts = {'Coro':Chorus,'coro':chorus,'verse':verse,'verso':verse,'prechorus':prechorus,'intermedio':intermedio,'intro':intro,'outro':outro,'bridge':bridge}

class song:
    def __init__(self,file_name,backsteps):
        self.raw = open(file_name,'r',encoding='utf-8').read()
        spt = self.raw.split('\n')
        self.title = spt[0]
        self.subtitle = spt[1]
        self.key = spt[2]
        self.composer = spt[3]
        self.parts = self.raw.split('/')
        self.groups = [(self.parts[2*i-1],self.parts[2*i]) for i in range(1,ceil(len(self.parts)/2))]
        self.teile = [parts[group[0]](group[1]) for group in self.groups]
        try:
            self.Coro = [teil for teil in self.teile if isinstance(teil,Chorus)][0]
        except:
            pass
        for teil in self.teile:
            try:
                teil.include_coro(self.Coro)
            except:
                pass
        head = f'<html><head>\n<title>{self.title}</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<link rel="stylesheet" href="{backsteps}css/style.css"></head>'
        title_table = f'<table class="main" border=0px width="100%">\n<col style="width:25%"><col style="width:30%"><col style="width:20%"><col style="width:20%"><tr><th colspan="3"><h1>{self.title}</h1></th></tr><tr><th><h2>{self.composer}</h2></th><th><h2>{self.subtitle}</h2></th><th><h2>Clave: {self.key}</h2></th></tr>\n</table>'
        control_bar = f'<div>\n<div class="control_bar">\n<label id="up" onclick="tpup()"><div class="icon">+1</div></label>\n<label id="down" onclick="tpdown()"><div class="icon">-1</div></label>\n<label onclick="tr_capo()"><span class="icon" id="tr-capo">Transpose</span><sup id="count" class="super"></sup></label>\n<label onclick="ft_sp()" id="b_but"><span class="icon">&nbsp;&flat;&nbsp;</span></label>\n</div>\n</div>'
        html_constants = constants(backsteps)
        self.html_preamble = head + html_constants.navbar + title_table + control_bar
        self.html_footer = f'<script src="{backsteps}js/script.js"></script></body></html>'
    def to_html(self,backsteps):
        html = '\n'.join([teil.to_html(backsteps) for teil in self.teile])
        return self.html_preamble + '\n' + html + '\n'+ self.html_footer

def create_html(file_path):
    backsteps = rech_backsteps(path,file_path,is_file=True)
    file_name = file_path.split('/')[-1][:-4]
    name_ext = '/'.join(file_path.split('/')[:-1])
    newfile = open(f'{name_ext}/{file_name}.html','w',encoding='utf-8')
    newfile.write(song(file_path,backsteps).to_html(backsteps))
    newfile.close()

def create_index(folder_path):
    backsteps = rech_backsteps(path,folder_path)
    html_constants = constants(backsteps)
    folder_name = folder_path.split('/')[-1]
    head = f'<html><head>\n<title>{folder_name}</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<link rel="stylesheet" href="{backsteps}css/style.css"></head>'
    preamble = head + html_constants.navbar + f'<h1 style="text-align: center;">{folder_name}</h1>\n<div class="listing">\n'
    dirs = sorted(os.listdir(folder_path))
    folders = [i for i in dirs if i.find('.')==-1]
    if folders==[]:
        songs = [i for i in dirs if i[-5:]=='.html']
        if songs!=[]:
            try:
                songs.remove('index.html')
            except:
                pass
            preamble += '<ul>\n'
            for song in songs:
                preamble += f'<a href="{song}"><li>{song[:-5]}</li></a>\n'
            footer = '</ul>\n</div>\n</div>\n</body>\n</html>'
            html = preamble + footer
            newfile = open(f'{folder_path}/index.html','w',encoding='utf-8')
            newfile.write(html)
            newfile.close()
    else:
        jscript = 'function show(x) {\nif (x.style.display === "none") {\nx.style.display = "block";\n} else {\nx.style.display = "none";\n}\n}'
        for folder in folders:
            dirs = sorted(os.listdir(folder_path+'/'+folder))
            songs = [i for i in dirs if i[-5:]=='.html']
            if songs!=[]:
                try:
                    songs.remove('index.html')
                except:
                    pass
                ID = folder[4:7]
                funName = 'show'+'_'.join(folder[4:].split(' '))
                preamble += f'<ul class="order">\n<label onclick="{funName}()"><li class="folder">{folder}</li></label>\n</ul>'
                preamble += f'<ul style="display:none;" id="{ID}">\n'
                for song in songs:
                    preamble += f'<a href="{folder}/{song}"><li>{song[:-5]}</li></a>\n'
                preamble += '</ul>\n'
                jscript += f'function {funName}() {{\nvar x = document.getElementById("{ID}");\nshow(x)}}\n'
                footer = f'\n</div>\n</div>\n</body>\n<script>\n{jscript}\n</script></html>'
                html = preamble + footer
                newfile = open(f'{folder_path}/index.html','w',encoding='utf-8')
                newfile.write(html)
                newfile.close()


import os
import pathlib
path = pathlib.Path(__file__).parent.resolve() # Automated path retriever
dirs = sorted(os.listdir(path))
print(path)
def rech_backsteps(path,sub_path,is_file=False):
    if str(path)==str(sub_path):
        return ''
    else:
        backsteps = len(str(sub_path).split('/'))-len(str(path).split('/'))
        if is_file:
            backsteps -= 1
        pre = ''
        for i in range(backsteps):
            pre+='../'
        return pre
folders = [str(path)+'/'+i for i in dirs if i.find('.')==-1]
abc_songs = []
for folder in folders:
    dirs = sorted(os.listdir(folder))
    songs = [i for i in dirs if i[-4:]=='.txt']
    sub_dirs = sorted(os.listdir(folder))
    sub_folders = [i for i in dirs if i.find('.')==-1]
    if sub_folders==[]:
        for s in songs:
            create_html(folder+'/'+s)
            abc_songs+=[(s,folder.split('/')[-1]+'/')]
        create_index(folder)
    else:
        for sub_folder in sub_folders:
            dirs = sorted(os.listdir(folder+'/'+sub_folder))
            songs = [i for i in dirs if i[-4:]=='.txt']
            for s in songs:
                create_html(folder+'/'+sub_folder+'/'+s)
                abc_songs+=[(s,folder.split('/')[-1]+'/'+sub_folder+'/')]
            create_index(folder)


def create_global_index(songs,path):
    backsteps = rech_backsteps(path,path)
    head = f'<html><head>\n<title>Global Index</title>\n<meta http-equiv="Content-Type" content="text/html;charset=utf-8">\n<meta http-equiv="Content-Style-Type" content="text/css">\n<link rel="stylesheet" href="{backsteps}css/style.css"></head>'
    html_constants = constants(backsteps)
    preamble = head + html_constants.navbar + '<h1 style="text-align: center;">Índice General</h1>\n<div class="listing">\n<ul>\n'
    for song in songs:
        preamble += f'<a href="{song[1]}{song[0]}"><li>{song[0][:-5]}</li></a>\n'
    footer = '</ul>\n</div>\n</div>\n</body>\n</html>'
    html = preamble + footer
    newfile = open(f'{path}/index.html','w',encoding='utf-8')
    newfile.write(html)
    newfile.close()

abc_songs.sort(key=lambda tup: tup[0])
abc_songs = [(i[0].replace('.txt','.html'),i[1]) for i in abc_songs]
create_global_index(abc_songs,path)