"""Is there a surjection pi_1(m004) -> 2O (binary octahedral)? Build 2O as an abstract group."""
import snappy, warnings, itertools; warnings.filterwarnings("ignore")
from snappy import Manifold
from fractions import Fraction

# 2O as 48 unit quaternions over Z[1/2, sqrt2] -- represent exactly as tuples over Q[sqrt2]:
# element = (a + b*s, ...) with s = 1/sqrt2. Use pairs (rational_part, sqrt2_part) with s^2 = 1/2.
class E:  # a + b*sqrt(2)
    __slots__=('a','b')
    def __init__(s,a=0,b=0): s.a=Fraction(a); s.b=Fraction(b)
    def __add__(s,o): return E(s.a+o.a, s.b+o.b)
    def __sub__(s,o): return E(s.a-o.a, s.b-o.b)
    def __mul__(s,o): return E(s.a*o.a+2*s.b*o.b, s.a*o.b+s.b*o.a)
    def __eq__(s,o): return s.a==o.a and s.b==o.b
    def __hash__(s): return hash((s.a,s.b))
    def __repr__(s): return f"({s.a}+{s.b}r2)"
def q(a,b,c,d): return (a,b,c,d)
def qmul(x,y):
    a1,b1,c1,d1=x; a2,b2,c2,d2=y
    return (a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2,
            a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2)
Z=E(0); ONE=E(1); H=E(Fraction(1,2)); S=E(0,Fraction(1,2))   # S = sqrt2/2 = 1/sqrt2
elts=set()
for sgn in [ONE,E(-1)]:
    for pos in range(4):
        v=[Z,Z,Z,Z]; v[pos]=sgn; elts.add(tuple(v))
for sgns in itertools.product([H,E(Fraction(-1,2))],repeat=4): elts.add(tuple(sgns))
T=set(elts)
for i in range(4):
    for j in range(i+1,4):
        for s1 in (S,E(0,Fraction(-1,2))):
            for s2 in (S,E(0,Fraction(-1,2))):
                v=[Z,Z,Z,Z]; v[i]=s1; v[j]=s2; elts.add(tuple(v))
G=sorted(elts, key=lambda t: str(t))
print("|2T| =",len(T)," |2O| =",len(G))
idx={g:i for i,g in enumerate(G)}; n=len(G)
MUL=[[idx[qmul(G[i],G[j])] for j in range(n)] for i in range(n)]
ID=idx[(ONE,Z,Z,Z)]
INV=[next(j for j in range(n) if MUL[i][j]==ID) for i in range(n)]
# verify group / order structure
from collections import Counter
ords=Counter()
for i in range(n):
    k=1; x=i
    while x!=ID: x=MUL[x][i]; k+=1
    ords[k]+=1
print("  element order distribution of 2O:",dict(sorted(ords.items())),"(2O: 1,1,1,6? classical: orders 1,2,3,4,6,8)")
print("  number of involutions:",ords[2],"(binary polyhedral groups have exactly one)")

M=Manifold('m004'); fg=M.fundamental_group()
rels=[[(ord(ch)-97,1) if ch.islower() else (ord(ch)-65,-1) for ch in r] for r in fg.relators()]
ng=fg.num_generators(); print("  m004: gens",ng,"rels",fg.relators())
ns=0
for imgs in itertools.product(range(n),repeat=ng):
    ok=True
    for w in rels:
        r=ID
        for gi,e in w:
            x=imgs[gi]
            if e<0: x=INV[x]
            r=MUL[r][x]
        if r!=ID: ok=False;break
    if not ok: continue
    seen={ID}; st=[ID]
    while st:
        x=st.pop()
        for s in imgs:
            y=MUL[x][s]
            if y not in seen: seen.add(y); st.append(y)
    if len(seen)==n: ns+=1
print("  surjections m004 -> 2O:", ns, "  (paper claims NONE)")
