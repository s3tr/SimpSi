
import sys, random

mode, infile, outfile = sys.argv[1], sys.argv[2], sys.argv[3]

KEY = 12345
ROT = 7
A, R = 32, 95

data = open(infile).read()

def rot(c,r):
    o=ord(c)
    return chr(A+(o-A+r)%R) if 32<=o<=126 else c

random.seed(KEY)
idx=list(range(len(data)))
random.shuffle(idx)

if mode=="e":
    d=[rot(c,ROT) for c in data]
    out=['']*len(d)
    for i,j in enumerate(idx): out[j]=d[i]
else:
    tmp=['']*len(data)
    for i,j in enumerate(idx): tmp[i]=data[j]
    out=[rot(c,-ROT) for c in tmp]

open(outfile,"w").write("".join(out))

