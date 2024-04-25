from math import ceil


class line:
    def __init__(self, raw, instrumental=False):
        if instrumental:
            self.space_between_chords = '\\qquad'
        else:
            self.space_between_chords = '\\,'
        if len(raw) != 0 and raw[0] != '[':
            raw = '[]'+raw
        lst = [spt.split(']')
               for spt in raw.split('[')]  # Separate chords from text
        # print(f'lst: {lst}')
        lst.pop(0)
        chords = [i[0] for i in lst]  # Transpose algorithm
        lyrics = [i[1] for i in lst]  # Transpose algorithm
        # print(f'chords: {chords}')
        # print(f'lyrics: {lyrics}')
        self.set_c_line(chords)
        # Chord line table
        self._l_line = self.set_line(lyrics)

    def set_c_line(self, chords):
        self._c_line = '&'.join(
            [chord.replace('#', r'{\textsharp}').replace('b', r'{\flat}').replace('^',r'{\Major}').replace('_', r'{/}') for chord in chords])

    def set_line(self, lst):
        return '&'.join(lst)

    def table(self):
        return f'\\noindent\n\\begin{{tabular}}{{llllllllllll}}\n{self._c_line}\\\\\n{self._l_line}\n\\end{{tabular}}\n'


class double_line(line):
    def __init__(self, raw):
        raw = raw.replace('{', '')
        self.add_class = ''
        if list(raw)[0] != '[':
            raw = '[]'+raw
        lst = [spt.split(']')
               for spt in raw.split('[')]  # Separate chords from text
        lst.pop(0)
        for i in range(len(lst)):
            app = lst[i].pop(1)
            for a in app.split('|'):
                lst[i].append(a)
        for i in range(len(lst)):
            # Add empty spaces in the second voice line
            lst[i].append('') if len(lst[i]) != 3 else None
        chords = [list(i) for i in zip(*lst)]  # Transpose algorithm
        self.set_c_line(chords)
        self._l_line = self.set_line(lst[1])
        self._second_line = self.set_line(lst[2])

    def table(self):
        return f'\\begin{{tabular}}{{llllllllllll}}\n{self._c_line}\n{self._l_line}\n{self._l_line}\n\\end{{tabular}}'


class Chorus:
    def __init__(self, raw, part_id=''):
        self.raw = raw.replace(' ', r'\,')  # Spaces in html
        self.id = (' ' + part_id) if part_id != '' else ''
        self.color = 'chorus'
        self.title = 'Coro'
        self.repeat_counter = 1

    def to_latex(self):
        lines = [double_line(raw) if raw[0] == '{' else line(
            raw) for raw in self.raw.split('\n') if len(raw) != 0]
        latex = '\n'.join([lin.table() for lin in lines])
        return f'\\noindent\n\\begin{{minipage}}{{\\columnwidth}}\n\\tit{{{self.title}}}{{{self.color}}}\n\\noindent\n{latex}\\end{{minipage}}\\\\\n'


class chorus:
    def __init__(self, raw, part_id=''):
        self.repeat_counter = 1
        self.title = 'Coro'

    def to_latex(self):
        repeat_marker = f'\\,(\\texttimes{self.repeat_counter})' if self.repeat_counter > 1 else ''
        latex = f'\\chorus{{{repeat_marker}}}'
        return f'\n{latex}\n'


class verse:
    def __init__(self, raw, part_id=''):
        self.raw = raw.replace(' ', r'\,')
        self.title = 'Estrofa'
        self.color = 'verse'
        self.instrumental = False
        self.id = (' ' + part_id) if part_id != '' else ''
        self.repeat_counter = 1

    def to_latex(self):
        repeat_marker = f'\\,(\\texttimes{self.repeat_counter})' if self.repeat_counter > 1 else ''
        lines = [double_line(raw) if raw[0] == '{' else line(
            raw, self.instrumental) for raw in self.raw.split('\n') if len(raw) != 0]
        latex = '\n'.join([lin.table() for lin in lines])
        return f'\\noindent\n\\begin{{minipage}}{{\\columnwidth}}\n\\tit{{{self.title}}}{{{self.color}}}{repeat_marker}\n\\noindent\n{latex}\\end{{minipage}}\\\\\n'


class general:
    def __init__(self, raw, part_id=''):
        self.raw = raw.replace(' ', r'\,')
        self.klass = 'verse'
        self.instrumental = False

    def to_latex(self):
        lines = [double_line(raw) if raw[0] == '{' else line(
            raw, self.instrumental) for raw in self.raw.split('\n') if len(raw) != 0]
        latex = '\n'.join([lin.table() for lin in lines])
        return latex


class prechorus(verse):
    def __init__(self, raw, part_id=''):
        super().__init__(raw, part_id)
        self.title = 'Pre-coro'
        self.color = 'prechorus'


class bridge(verse):
    def __init__(self, raw, part_id=''):
        super().__init__(raw, part_id)
        self.title = 'Puente'
        self.color = 'bridge'


class outro_verse(verse):
    def __init__(self, raw, part_id=''):
        super().__init__(raw, part_id)
        self.title = 'Outro'
        self.color = 'outro'


class intro_verse(verse):
    def __init__(self, raw, part_id=''):
        super().__init__(raw, part_id)
        self.title = 'Intro'
        self.color = 'intro'


class intermedio(verse):
    def __init__(self, raw, part_id=''):
        self.raw = raw.replace(' ', '\\quad')
        self.title = 'Intermedio'
        self.klass = 'inst'
        self.instrumental = True
        self.id = (' ' + part_id) if part_id != '' else ''
        self.color = 'intermedio'
        self.repeat_counter = 1


class intro(intermedio):
    def __init__(self, raw, part_id=''):
        super().__init__(raw, part_id)
        self.raw = raw.replace(' ', '\\quad')
        self.instrumental = True
        self.title = 'Intro'
        self.color = 'intro'


class outro(intermedio):
    def __init__(self, raw, part_id=''):
        super().__init__(raw, part_id)
        self.title = 'Outro'
        self.color = 'outro'


parts = {'Coro': Chorus, 'coro': chorus, 'verse': verse, 'verso': verse, 'prechorus': prechorus, 'intermedio': intermedio, 'intro': intro,
         'intro_verse': intro_verse, 'outro': outro, 'bridge': bridge, 'gen': general, 'outro_verse': outro_verse}


class song:
    def __init__(self, file_name, folder=''):
        raw = open(file_name, 'r', encoding='utf-8').read()
        meta = raw.split('{song}')[0].split('\n')[:-1]
        self.meta = {}
        # print(file_name)
        for entry in meta:
            self.meta[entry.split(' : ')[0]] = entry.split(' : ')[1]
        for entry in ['capo','composer','liturgy']:
            if entry not in self.meta.keys():
                self.meta[entry] = ''
        self.parts = raw.split('/')
        groups = [(self.parts[2*i-1], self.parts[2*i])
                       for i in range(1, ceil(len(self.parts)/2))]
        self.teile = [parts[group[0].split('-')[0]](group[1], '' if len(
            group[0].split('-')) == 1 else group[0].split('-')[1]) for group in groups]
        part_counter = {}
        # repeated chorus
        x = 0 # counter
        while x < (len(self.teile)-1):
            if isinstance(self.teile[x],chorus) and isinstance(self.teile[x+1],chorus):
                self.teile.pop(x+1)
                self.teile[x].repeat_counter += 1
            else:
                try:
                    part_counter[type(self.teile[x])] += 1
                except:
                    part_counter[type(self.teile[x])] = 1
                self.teile[x].part_counter = part_counter[type(self.teile[x])]
                x += 1
        for teil in self.teile:
            try:
                if part_counter[type(teil)] > 1:
                    teil.title += f' {teil.part_counter}'
            except:
                pass
        metadata = '\\noindent'

    def to_latex(self):
        latex = '\n'.join([teil.to_latex() for teil in self.teile])
        try:
            metadata = f'{self.meta["composer"]}\hfill{self.meta["capo"]}'
        except:
            metadata = f'{self.meta["composer"]}'
        
        preamble = f'\\section*{{{self.meta["title"]}}}\n{metadata}\n\\begin{{multicols}}{{2}}\n'
        footer = f'\n\\end{{multicols}}'
        return preamble + latex + footer


def create_latex(file_path):
    file_name = file_path.split('/')[-1][:-4] # FILE NAME
    name_ext = '/'.join(file_path.split('/')[:-1]) # FOLDER NAME
    newfile = open(f'CantoralLatex/{name_ext}/{file_name}.tex', 'w', encoding='utf-8')
    newfile.write(song(file_path, folder=name_ext).to_latex())
    newfile.close()

import os
import pathlib
path = pathlib.Path(__file__).parent.resolve()  # Automated path retriever
dirs = sorted(os.listdir(path))
print(f'curent path: {path}')

create_latex('María/Contigo María.txt')
create_latex('María/Un Mundo Hizo Dios.txt')
create_latex('Hora Santa/5 - Eucarísticos/Jesús está vivo.txt')
create_latex('Hora Santa/5 - Eucarísticos/Vida en Abundancia.txt')


if __name__ == '__main__' and False:
    import os
    import pathlib
    path = pathlib.Path(__file__).parent.resolve()  # Automated path retriever
    dirs = sorted(os.listdir(path))
    print(f'curent path: {path}')

    def rech_backsteps(path, sub_path, is_file=False):
        if str(path) == str(sub_path):
            return ''
        else:
            backsteps = len(str(sub_path).split('/'))-len(str(path).split('/'))
            if is_file:
                backsteps -= 1
            pre = ''
            for i in range(backsteps):
                pre += '../'
            return pre
    folders = [str(path)+'/'+i for i in dirs if i.find('.') == -1]
    abc_songs = []
    for folder in folders:
        dirs = sorted(os.listdir(folder))
        songs = [i for i in dirs if i[-4:] == '.txt']
        sub_dirs = sorted(os.listdir(folder))
        sub_folders = [i for i in dirs if i.find('.') == -1]
        if sub_folders == []:
            for s in songs:
                create_html(folder+'/'+s)
                abc_songs += [(s, folder.split('/')[-1]+'/')]
            create_index(folder)
        else:
            for sub_folder in sub_folders:
                dirs = sorted(os.listdir(folder+'/'+sub_folder))
                songs = [i for i in dirs if i[-4:] == '.txt']
                for s in songs:
                    if sub_folder == '8 - Comunión':
                        comunion = True
                    else:
                        comunion = False
                    create_html(folder+'/'+sub_folder+'/'+s, comunion=comunion)
                    abc_songs += [(s, folder.split('/')
                                   [-1]+'/'+sub_folder+'/')]
                create_index(folder)
