from math import ceil

class constants:
    def __init__(self,backsteps,title=''):
        self.navbar = f'''
<nav class="navbar navbar-expand-lg bg-dark navbar-dark fixed-top shadow">
    <div class="container-fluid">
        <a class="navbar-brand mb-0 h1" href="{backsteps}index.html"><img src="{backsteps}Logo.svg" width="20px" height="20px"></img> Coro Milites Christi</a>

        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapse_navbar" aria-controls="collapse_navbar" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span> <!--This is the hamburger icon for the menu-->
        </button>

        <div class="collapse navbar-collapse" id="collapse_navbar">
            <ul class="navbar-nav ms-auto">
                <li class="nav-item">
                    <a href="{backsteps}Misa/index.html" class="nav-link">Misa</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}María/index.html" class="nav-link">María</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Hora Santa/index.html" class="nav-link">Hora Santa</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Alabanzas/index.html" class="nav-link">Alabanzas</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Semana Santa/index.html" class="nav-link">Semana Santa</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Villancicos/index.html" class="nav-link">Villancicos</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Originales/index.html" class="nav-link">Originales</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Niños/index.html" class="nav-link">Niños</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}Salmos/index.html" class="nav-link">Salmos</a>
                </li>
                <li class="nav-item">
                    <a href="{backsteps}index.html" class="nav-link">Todos los Cantos</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
<body class="p-4 content pt-5">
<br>
            '''

        self.header = f'''
<html>
<head>
    <title>{title}</title>
    <link rel="icon" type="image/x-icon" href="{backsteps}Logo.svg">
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <meta http-equiv="Content-Style-Type" content="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='https://fonts.googleapis.com/css?family=Nunito' rel='stylesheet'>
    <link rel="stylesheet" href="{backsteps}css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
</head>
                '''

        self.comunion_header = f'''
<html>
<head>
    <title>{title}</title>
    <link rel="icon" type="image/x-icon" href="{backsteps}Logo.svg">
    <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
    <meta http-equiv="Content-Style-Type" content="text/css">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href='https://fonts.googleapis.com/css?family=Nunito' rel='stylesheet'>
    <link rel="stylesheet" href="{backsteps}css/style.css">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.1/jquery.min.js"></script>
    <script>
        $(document).ready(
            function () {{
            $("#alma-de-cristo").load("AlmaDeCristo.xd");
        }});
    </script>
</head>
                '''

        self.html_footer = f'''
<br><br><br><br>
<div class="btn-group btn-group-lg fixed-bottom mx-auto shadow toolbar" role="group" aria-label="Basic example">
    <button type="button" class="btn btn-dark" id="up" onclick="tpup()"><span class="icon">+1</span></button>
    <button type="button" class="btn btn-dark" id="down" onclick="tpdown()"><span class="icon">-1</span></button>
    <button type="button" class="btn btn-dark" onclick="tr_capo()"><span class="icon" id="tr-capo">Tp</span><sup class="super" id="count"></sup></button>
    <button type="button" class="btn btn-dark" onclick="startInverval()" id="play-but"><span class="icon">&#9654;</span></button>
    <button type="button" class="btn btn-dark" onclick="toggleDark()" id="dark-toggle"><span class="icon">&#9788;</span></button>
    <button type="button" class="btn btn-dark" onclick="ft_sp()" id="b_but"><span class="icon">&flat;</span></button>
</div>
<script src="{backsteps}js/abcweb-1.js"></script>
<script src="{backsteps}js/abc2svg-1.js"></script>
<script src="{backsteps}js/snd-1.js"></script>
<script src="{backsteps}js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
</body>
</html>
        '''

        self.html_comunion_footer = f'''
<br><br>
<div id="alma-de-cristo"></div>
<br><br><br><br>
<div class="btn-group btn-group-lg fixed-bottom mx-auto shadow toolbar" role="group" aria-label="Basic example">
    <button type="button" class="btn btn-dark" id="up" onclick="tpup()"><span class="icon">+1</span></button>
    <button type="button" class="btn btn-dark" id="down" onclick="tpdown()"><span class="icon">-1</span></button>
    <button type="button" class="btn btn-dark" onclick="tr_capo()"><span class="icon" id="tr-capo">Tp</span><sup class="super" id="count"></sup></button>
    <button type="button" class="btn btn-dark" onclick="startInverval()" id="play-but"><span class="icon">&#9654;</span></button>
    <button type="button" class="btn btn-dark" onclick="toggleDark()" id="dark-toggle"><span class="icon">&#9788;</span></button>
    <button type="button" class="btn btn-dark" onclick="ft_sp()" id="b_but"><span class="icon">&flat;</span></button>
</div>
<script src="{backsteps}js/abcweb-1.js"></script>
<script src="{backsteps}js/abc2svg-1.js"></script>
<script src="{backsteps}js/snd-1.js"></script>
<script src="{backsteps}js/script.js"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
</body>
</html>
        '''


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
            try:
                bass = chord.split('_')[1]
                qual = chord.split('_')[0].replace(og_root,'').replace('^','Δ').replace('*','/') # Remove root from chord
                return {'root' : root, 'svg' : qual.replace('#','s') + '_' + bass,
                        'flat' : FLAT, 'og_root' : og_root,
                        'quality' : (qual + '/' + iterate_key(og_root,bass)).replace('b','♭').replace('#','♯') + ('' if len(root)==1 else root[1]), 'bass' : bass} # Root + Quality

            except:
                qual = chord.replace(og_root,'').replace('^','Δ').replace('*','/') # Remove root from chord
                return {'root' : root, 'svg' : qual.replace('#','s'),
                        'flat' : FLAT, 'og_root' : og_root,
                        'quality' : qual.replace('b','♭').replace('#','♯')} # Root + Quality
        except:
            return {'root' : root,'svg' : '', 'flat' : FLAT, 'og_root' : og_root, 'quality' : ''} # For Major Chords
    except:
        return {'root' : '', 'flat' : False} # Blank Chords

def iterate(root):
    return chr((ord(root)-ord('A')+1)%7+ord('A'))

circle_of_fifths = ['Fb','Cb','Gb','Db','Ab','Eb','Bb','F','C','G','D','A','E','B','F#','C#','G#','D#','A#']

def iterate_key(root,num):
    if len(num) == 1:
        quality , num = None , int(num)
    else:
        quality , num = num[0] , int(num[1])
    key = circle_of_fifths[circle_of_fifths.index(root)-1:circle_of_fifths.index(root)+6]
    key.sort()
    suf = key[(key.index(root)+num-1)%7]
    return ((suf+'b') if len(suf)==1 else suf.replace('#','')) if quality=='m' else suf # for minor intervals

class line:
    def __init__(self,raw,backsteps=0,instrumental=False):
        if instrumental:
            self.add_class = 'px-1'
        else:
            self.add_class = ''
        if len(raw)!=0 and raw[0]!='[':
            raw='[]'+raw
        lst = [spt.split(']') for spt in raw.split('[')] # Separate chords from text
        lst.pop(0)
        lst = [list(i) for i in zip(*lst)] # Transpose algorithm
        chords = [chordify(chord) for chord in lst[0]]
        self.set_c_line(chords,backsteps)
        # Chord line table
        self._l_line = self.set_line(lst[1])

    def set_c_line(self,chords,backsteps):
        self._c_line = ''.join([f'''
        <td class="chord {self.add_class}">
            <span class="root">{chord["root"]}</span><span class="quality">{chord["quality"]}</span>
            <div class="diagram">
                <span class="chord_name">{chord["root"]}{chord["quality"]}</span>
                <img class="fig" src="{backsteps}chords/{chord["og_root"]}{chord["svg"]}.svg">
            </div>
        </td>''' if chord["flat"] else f'''
        <td class="chord">
            <span class="root">{chord["root"]}</span><span class="quality">{chord["svg"]}</span>
            <div class="diagram">
                <span class="chord_name">{chord["root"]}{chord["svg"]}</span>
                <img class="fig" src="{backsteps}chords/{iterate(chord["root"][0])}b{chord["svg"]}.svg">
            </div>
        </td>''' if chord["root"]!='' else f'<td></td>' for chord in chords])

    def set_line(self,lst):
        return ''.join([f'<td>{frag}</td>' for frag in lst])

    def table(self):
        return f'''
        <table class="linewithchord" border="0" cellpadding="0" cellspacing="0">
            <tr class="chordline">{self._c_line}</tr>
            <tr class="lyricsline">{self._l_line}</tr>
        </table>
        '''
    
class double_line(line):
    def __init__(self,raw,backsteps=0):
        raw = raw.replace('{','')
        self.add_class = ''
        if list(raw)[0]!='[':
            raw='[]'+raw
        lst = [spt.split(']') for spt in raw.split('[')] # Separate chords from text
        lst.pop(0)
        for i in range(len(lst)):
            app = lst[i].pop(1)
            for a in app.split('|'):
                lst[i].append(a)
        for i in range(len(lst)):
            lst[i].append('') if len(lst[i])!=3 else None # Add empty spaces in the second voice line
        lst = [list(i) for i in zip(*lst)] # Transpose algorithm
        chords = [chordify(chord) for chord in lst[0]]
        self.set_c_line(chords,backsteps)
        self._l_line = self.set_line(lst[1])
        self._second_line = self.set_line(lst[2])

    def table(self):
        return f'''
        <table class="linewithchord" border="0" cellpadding="0" cellspacing="0">
            <tr class="chordline">{self._c_line}</tr>
            <tr class="lyricsline">{self._l_line}</tr>
            <tr class="second_voice">{self._second_line}</tr>
        </table>
        '''


class Chorus:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;') # Spaces in html
    
    def to_html(self,backsteps):
        head = f'''
        <br>
        <span class="fs-2 fw-bold">Coro</span>
        <br>
        <table class="chorus" border="0" cellpadding="0" cellspacing="0">
        <tr>
        <td>
                '''
        foot = '''
        </td>
        </tr>
        </table>
        <br>
        '''
        lines = [double_line(raw,backsteps) if raw[0]=='{' else line(raw,backsteps) for raw in self.raw.split('\n') if len(raw)!=0]
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
        self.instrumental = False
    
    def to_html(self,backsteps):
        head = f'''
        <br>
        <span class="fs-2 fw-bold">{self.title}</span>
        <br>
        <table class="{self.klass}" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td>
        '''
        foot = '''
                </td>
            </tr>
        </table>
        '''
        lines = [double_line(raw,backsteps) if raw[0]=='{' else line(raw,backsteps,self.instrumental) for raw in self.raw.split('\n') if len(raw)!=0]
        html = '\n'.join([lin.table() for lin in lines])
        return head + html + foot

class general:
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;')
        self.klass = 'verse'
        self.instrumental = False
    
    def to_html(self,backsteps):
        head = f'''
        <br>
        <table class="{self.klass}" border="0" cellpadding="0" cellspacing="0">
            <tr>
                <td>
        '''
        foot = '''
                </td>
            </tr>
        </table>
        '''
        lines = [double_line(raw,backsteps) if raw[0]=='{' else line(raw,backsteps,self.instrumental) for raw in self.raw.split('\n') if len(raw)!=0]
        html = '\n'.join([lin.table() for lin in lines])
        return head + html + foot


class prechorus(verse):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Pre-coro'

class bridge(verse):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Puente'

class resp(verse):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Respuesta'

class intermedio(verse):
    def __init__(self,raw):
        self.raw = raw.replace(' ','&nbsp;&nbsp;')
        self.title = 'Intermedio'
        self.klass = 'inst'
        self.instrumental = True

class intro(intermedio):
    def __init__(self,raw):
        super().__init__(raw)
        self.raw = raw.replace(' ','&nbsp;&nbsp;')
        self.instrumental = True
        self.title = 'Intro'
    
class outro(intermedio):
    def __init__(self,raw):
        super().__init__(raw)
        self.title = 'Outro'

class locutor:
    def __init__(self,raw):
        self.title = 'Locutor'
        self.raw = raw
    
    def to_html(self,backsteps):
        html = f'''
        <br>
        <span class="fs-2 fw-bold">{self.title}</span>
        <br>
        <p class="locutor">{self.raw}</p>
        '''
        return html

class salmo:
    def __init__(self,raw):
        self.lines = raw.replace('\n','\n<br>')
        if self.lines[-4:]=='<br>':
            self.lines = self.lines[:-5]
    def to_html(self,backsteps):
        foot = '<b>&nbsp;&nbsp;R.</b>\n<br>\n'
        return self.lines + foot



parts = {'Coro':Chorus,'coro':chorus,'verse':verse,'verso':verse,'prechorus':prechorus,'intermedio':intermedio,'intro':intro,'outro':outro,'bridge':bridge,'locutor':locutor,'resp':resp,'respuesta':resp,'salmo':salmo,'gen':general}

# colors
GOLD = '#d9b225'
GREEN = '#1ba640'
LILA = '#a421b5'
RED = '#d93a25'
BLUE = '#3b71db'
BLACK = '#242424'

liturgy_colors = {
    'Ordinario': GREEN, # green

    'Adviento': LILA, 'Cuaresma':LILA, # purple

    'Pascua': GOLD, 'Navidad':GOLD, 'Domingo de Resurrección':GOLD, 'Santa María, Madre de Dios': GOLD, 'Sagrada Familia':GOLD, 'San José':GOLD, 'Anunciación del Señor':GOLD, 'Jueves Santo':GOLD, 'Vigilia Pascual':GOLD, # gold

    'Viernes Santo':RED, 'Semana Santa' : RED, 'Domingo de Ramos' : RED, 'Viernes Santo':RED, # red

    'Difuntos':BLACK, # black

    'Vírgen de Guadalupe':BLUE # blue
}

def subtitle_from_folder(folder):
    mid = folder.split('/')
    try:
        mid[1] = mid[1][4:]
    except:
        pass
    return ' - '.join(mid)

class song:
    def __init__(self,file_name,backsteps,folder='',abc_sheet=None,comunion=False):
        self.raw = open(file_name,'r',encoding='utf-8').read()
        # spt = self.raw.split('\n')
        meta = self.raw.split('{song}')[0].split('\n')[:-1]
        self.meta = {}
        # print(file_name)
        for entry in meta:
            self.meta[entry.split(' : ')[0]] = entry.split(' : ')[1]
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
        try:
            self.meta['subtitle']
        except:
            self.meta['subtitle'] = subtitle_from_folder(folder)
        if abc_sheet:
            abc_sheet = f'''
            <script type="text/vnd.abc" id="abc-score">
            {abc_sheet}
            </script>
            '''
        else:
            abc_sheet = ''
        # print(f'{folder}/{file_name}') # For debugging
        metadata = f'<h1>{self.meta["title"]}</h1><h2>{self.meta["subtitle"]}</h2>'
        try:
            metadata += f'<h2>Clave: {self.meta["key"]}</h2>'
        except:
            pass
        try:
            metadata += f'<h4>Autor: {self.meta["composer"]}</h4>'
        except:
            pass
        try:
            metadata += f'<h4 style="color:{liturgy_colors[self.meta["liturgy"]]};">Tiempo: {self.meta["liturgy"]}</h4>'
        except:
            try:
                print(f'missed {self.meta["liturgy"]}')
            except:
                pass
        html_constants = constants(backsteps,title=self.meta['title'])
        if comunion:
            self.html_preamble = html_constants.comunion_header + html_constants.navbar + metadata
            self.html_footer = abc_sheet + html_constants.html_comunion_footer
        else:
            self.html_preamble = html_constants.header + html_constants.navbar + metadata
            self.html_footer = abc_sheet + html_constants.html_footer
    def to_html(self,backsteps):
        html = '\n'.join([teil.to_html(backsteps) for teil in self.teile])
        return self.html_preamble + '\n' + html + '\n'+ self.html_footer

def create_html(file_path,comunion = False):
    backsteps = rech_backsteps(path,file_path,is_file=True)
    file_name = file_path.split('/')[-1][:-4]
    name_ext = '/'.join(file_path.split('/')[:-1])
    try:
        with open(f'{name_ext}/{file_name}.abc','r') as abc_file:
            abc_sheet = abc_file.read()
    except:
        abc_sheet = None
    newfile = open(f'{name_ext}/{file_name}.html','w',encoding='utf-8')
    newfile.write(song(file_path,backsteps,folder=name_ext.split('.io/')[1],abc_sheet=abc_sheet,comunion=comunion).to_html(backsteps))
    # "name_ext.split('.io/')[1]" retrieves the relative path, i.e. only the part next to DiegoRdz99.github.io
    newfile.close()

def create_index(folder_path):
    backsteps = rech_backsteps(path,folder_path)
    folder_name = folder_path.split('/')[-1]
    html_constants = constants(backsteps,title=folder_name)
    head = html_constants.header
    preamble = head + html_constants.navbar.replace(f'">{folder_name}',f' active">{folder_name}') + f'''
    <div class="container-fluid">
      <p class="text-center fs-1 fw-bolder pt-2">{folder_name}</p>
    </div>
    '''
    dirs = sorted(os.listdir(folder_path))
    folders = [i for i in dirs if i.find('.')==-1]
    if folders==[]:
        preamble += '<div class="list-group">'
        songs = [i for i in dirs if i[-5:]=='.html']
        if songs!=[]:
            try:
                songs.remove('index.html')
            except:
                pass
            # preamble += '<ul>\n'
            for song in songs:
                preamble += f'<a href="{song}" class="list-group-item list-group-item-action">{song[:-5]}</a>\n'
            footer = '''
                    </div>
                </body>
                <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
            </html>
            '''
            html = preamble + footer
            newfile = open(f'{folder_path}/index.html','w',encoding='utf-8')
            newfile.write(html)
            newfile.close()
    else:
        preamble += '<div class="accordion accordion-flush" id="accordionFolders">'
        # jscript = 'function show(x) {\nif (x.style.display === "none") {\nx.style.display = "block";\n} else {\nx.style.display = "none";\n}\n}'
        for folder in folders:
            dirs = sorted(os.listdir(folder_path+'/'+folder))
            songs = [i for i in dirs if i[-5:]=='.html']
            if songs!=[]:
                try:
                    songs.remove('index.html')
                except:
                    pass
                ID = folder[4:7]
                # funName = 'show'+'_'.join(folder[4:].split(' '))
                # preamble += f'<ul class="order">\n<label onclick="{funName}()"><li class="folder">{folder}</li></label>\n</ul>'

                # preamble += f'<ul style="display:none;" id="{ID}">\n'
                preamble += f'''
                <div class="accordion-item">
                    <h2 class="accordion-header" id="heading{ID}">
                    <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse{ID}" aria-expanded="true" aria-controls="collapse{ID}">
                    <div class="fs-5 fw-bold">{folder}</div>
                    </button>
                    </h2>
                    <div id="collapse{ID}" class="accordion-collapse collapse" aria-labelledby="heading{ID}" data-bs-parent="#accordionFolders">
                    <div class="accordion-body">
                    <div class="list-group">
                '''
                for song in songs:
                    preamble += f'<a href="{folder}/{song}" class="list-group-item list-group-item-action">{song[:-5]}</a>\n'
                preamble += '''
                    </div>
                    </div>
                    </div>
                </div>'''
                # preamble += '</ul>\n'
                # jscript += f'function {funName}() {{\nvar x = document.getElementById("{ID}");\nshow(x)}}\n'
                footer = f'''
                    </div>
                    </body>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
                </html>
                '''
                html = preamble + footer
                newfile = open(f'{folder_path}/index.html','w',encoding='utf-8')
                newfile.write(html)
                newfile.close()

if __name__=='__main__':
    import os
    import pathlib
    path = pathlib.Path(__file__).parent.resolve() # Automated path retriever
    dirs = sorted(os.listdir(path))
    print(f'curent path: {path}')
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
                    if sub_folder == '8 - Comunión':
                        comunion = True
                    else:
                        comunion = False
                    create_html(folder+'/'+sub_folder+'/'+s,comunion=comunion)
                    abc_songs+=[(s,folder.split('/')[-1]+'/'+sub_folder+'/')]
                create_index(folder)


    def create_global_index(songs,path):
        backsteps = rech_backsteps(path,path)
        head = f'''
        <head>
            <title>Global Index</title>
            <link rel="icon" type="image/x-icon" href="{backsteps}Logo.svg">
            <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
            <meta http-equiv="Content-Style-Type" content="text/css">
            <meta name="viewport" content="width=device-width, initial-scale=1">
            <link href='https://fonts.googleapis.com/css?family=Nunito' rel='stylesheet'>
            <link rel="stylesheet" href="{backsteps}css/style.css">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" 
        </head>
        '''
        html_constants = constants(backsteps)
        preamble = head + html_constants.navbar + f'''
        <div class="container-fluid">
        <p class="text-center fs-1 fw-bolder pt-2">Índice General</p>
        </div>
        <div class="list-group">
    '''
        for song in songs:
            preamble += f'<a href="{song[1]}{song[0]}" class="list-group-item list-group-item-action">{song[0][:-5]}</a>\n'
        footer = '''
                </div>
            </body>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-kenU1KFdBIe4zVF0s0G1M5b4hcpxyD9F7jL+jjXkk+Q2h455rYXK/7HAuoJl+0I4" crossorigin="anonymous"></script>
        </html>
        '''
        html = preamble + footer
        newfile = open(f'{path}/index.html','w',encoding='utf-8')
        newfile.write(html)
        newfile.close()

    abc_songs.sort(key=lambda tup: tup[0])
    abc_songs = [(i[0].replace('.txt','.html'),i[1]) for i in abc_songs]
    create_global_index(abc_songs,path)
    print('Done!')

