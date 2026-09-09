"""Reidemeister-Schreier by hand for H = ker(w) < G = <a,b | aabbAB>, w(a)=w(b)=1, transversal {1,a}.
Then the 2T count on MY presentation of H, and the restriction image, with no use of codex's Tietze map."""
import itertools
rel="aabbAB"; gens="ab"
w={'a':1,'b':1}
# cosets 0 (=1) and 1 (=a); action of a letter flips the coset (w=1 for both generators)
# Schreier generator gamma(t,x) = t x (bar(tx))^-1 ; name them
names={}
def schreier(t,x):   # t in {0,1}, x letter
    return (t,x)
# free reduction helper on lists of (sym, exp)
def reduce_(word):
    out=[]
    for s,e in word:
        if out and out[-1][0]==s and out[-1][1]==-e: out.pop()
        else: out.append((s,e))
    return out
def rewrite(word_letters, start=0):
    """rewrite the word (as G-word) read from coset `start` into Schreier generators."""
    t=start; out=[]
    for ch in word_letters:
        x=ch.lower()
        if ch.islower():
            out.append(((t,x),+1)); t^=1
        else:
            t^=1; out.append(((t,x),-1))
    return reduce_(out), t
# the trivial Schreier generator: gamma(0,'a') = a * bar(a)^-1 = a a^-1 = 1
trivial={(0,'a')}
def strip(word): return [(s,e) for s,e in word if s not in trivial]
R=[]
for t in (0,1):
    wd,end=rewrite(rel,t); assert end==t
    R.append(strip(wd))
label={(0,'b'):'u',(1,'a'):'v',(1,'b'):'w'}
def show(word): return "".join(label[s] if e>0 else label[s].upper() for s,e in word)
Hrels=[show(r) for r in R]
print("H = <u,v,w |", Hrels, ">   with u=b a^-1, v=a^2, w=a b")

# --- 2T on H directly --------------------------------------------------------------------------------
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%3 for j in range(2)) for i in range(2))
def det(A): return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%3
I=((1,0),(0,1))
GL=[((a,b),(c,d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if det(((a,b),(c,d)))!=0]
Q=[A for A in GL if det(A)==1]
def inv(A):
    for B in GL:
        if mul(A,B)==I: return B
def gen(S):
    seen={I}; fr=[I]
    while fr:
        x=fr.pop()
        for s in S:
            y=mul(x,s)
            if y not in seen: seen.add(y); fr.append(y)
    return seen
def evalword(word,img):
    X=I
    for ch in word:
        A=img[ch.lower()]; X=mul(X,A if ch.islower() else inv(A))
    return X
auts=set()
for g in GL:
    gi=inv(g); auts.add(tuple(mul(mul(g,A),gi) for A in Q))
qidx={A:i for i,A in enumerate(Q)}
SH=[imgs for imgs in itertools.product(Q,repeat=3) if all(evalword(r,dict(zip("uvw",imgs)))==I for r in Hrels) and len(gen(list(imgs)))==24]
print("Surj(H,2T) on my R-S presentation:", len(SH))
def orbits(S):
    S=set(S); orbs=[]
    while S:
        s=next(iter(S)); orb={tuple(aut[qidx[x]] for x in s) for aut in auts}; assert orb<=S; S-=orb; orbs.append(orb)
    return orbs
OH=orbits(SH); print("Aut-orbits on H:", [len(o) for o in OH])
SG=[imgs for imgs in itertools.product(Q,repeat=2) if evalword(rel,dict(zip("ab",imgs)))==I and len(gen(list(imgs)))==24]
Rset=set()
for A,B in SG:
    img={'a':A,'b':B}
    Rset.add((evalword("bA",img), evalword("aa",img), evalword("ab",img)))
print("restricted maps on (u,v,w):", len(Rset), " equals which H-orbit:", [Rset==o for o in OH])
z=[A for A in Q if A!=I and all(mul(A,B)==mul(B,A) for B in Q)][0]
# H^1(H;C2): characters on u,v,w killing the relators
chars=[c for c in itertools.product((0,1),repeat=3) if any(c) and all(sum(c["uvw".index(ch.lower())] for ch in r)%2==0 for r in Hrels)]
print("nonzero mod-2 characters of H:", chars, " (H_1(m004)=Z => exactly one)")
for c in chars:
    tw={tuple(mul(z,x) if c[i] else x for i,x in enumerate(s)) for s in Rset}
    print("central twist by", c, "-> the other orbit?", [tw==o for o in OH])
# sanity: the Tietze map codex used, checked as a map of presentations on MY H: c=w^-1, d=w u^-1 should satisfy m004's relator aaabABBAb for every 2T rep of H
m004rel="aaabABBAb"
ok=all(evalword(m004rel,{'a':inv(s[2]),'b':mul(s[2],inv(s[0]))})==I for s in SH)
print("codex's Tietze map sends m004's relator to 1 under all", len(SH), "2T reps of H:", ok)
