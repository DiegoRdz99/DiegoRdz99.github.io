from CantoralCristeros import *

st1 = r'A[E]cércate y toma tu lugar en la [D]fiesta  [A]'
st2 = r'{A[E]cércate y toma tu lugar en la [D]fiesta|Toma tu lugar en la[A]|fiesta'
ln1 = line(st1)
ln2 = double_line(st2)

# st1=st1.replace('{','')
# tst = [spt.split(']') for spt in st1.split('[')]
# tst[0].insert(0,'')
# for i in range(len(tst)):
#     app = tst[i].pop(1)
#     for a in app.split('|'):
#         tst[i].append(a)
# print(tst)