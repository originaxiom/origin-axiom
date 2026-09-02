"""Independent check of codex R039: project 2T -> A4 = PSL(2,3) through the center and compute the lift square.
Uses my own R-S presentation of H (r037_rs.py) and SnapPy's presentations."""
import itertools
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%3 for j in range(2)) for i in range(2))
def det(A): return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%3
I=((1,0),(0,1))
GL=[((a,b),(c,d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if det(((a,b),(c,d)))!=0]
Q=[A for A in GL if det(A)==1]
def inv(A):
    for B in GL:
        if mul(A,B)==I: return B
def neg(A): return tuple(tuple((-x)%3 for x in r) for r in A)
proj={A:min(A,neg(A)) for A in Q}          # A4 = 2T/{+-I}: canonical rep of each pair
A4=sorted(set(proj.values())); assert len(A4)==12
def a4mul(x,y): return proj[mul(x,y)]
def gen(S, m):
    e=proj[I] if m is a4mul else I
    seen={e}; fr=[e]
    while fr:
        x=fr.pop()
        for s in S:
            y=m(x,s)
            if y not in seen: seen.add(y); fr.append(y)
    return seen
def evalword(word,img,m,e,invf):
    X=e
    for ch in word:
        A=img[ch.lower()]; X=m(X,A if ch.islower() else invf(A))
    return X
def a4inv(x):
    for y in A4:
        if a4mul(x,y)==proj[I]: return y
# presentations: G = pi1(m000) = <a,b | aabbAB> (SnapPy); H = <u,v,w | vuwVU, vwuW> (my R-S), u=bA, v=aa, w=ab
Grel=["aabbAB"]; Hrel=["vuwVU","vwuW"]
def surj(gens, rels, grp, m, e, invf, order):
    return [imgs for imgs in itertools.product(grp,repeat=len(gens))
            if all(evalword(r,dict(zip(gens,imgs)),m,e,invf)==e for r in rels) and len(gen(list(imgs),m))==order]
SG2=surj("ab",Grel,Q,mul,I,inv,24); SH2=surj("uvw",Hrel,Q,mul,I,inv,24)
SGA=surj("ab",Grel,A4,a4mul,proj[I],a4inv,12); SHA=surj("uvw",Hrel,A4,a4mul,proj[I],a4inv,12)
print("Surj to 2T: m000", len(SG2), " m004", len(SH2), " | Surj to A4: m000", len(SGA), " m004", len(SHA))
# Aut(A4) = S4 = conjugation by GL(2,3) mod center  (Aut(A4) ~ S4, order 24)
autsA=set()
for g in GL:
    gi=inv(g); autsA.add(tuple(proj[mul(mul(g,x),gi)] for x in A4))
aidx={x:i for i,x in enumerate(A4)}
def orbitsA(S):
    S=set(S); orbs=[]
    while S:
        s=next(iter(S)); orb={tuple(aut[aidx[x]] for x in s) for aut in autsA}; assert orb<=S; S-=orb; orbs.append(orb)
    return orbs
print("|Aut(A4)| =", len(autsA), " A4-orbits: m000", [len(o) for o in orbitsA(SGA)], " m004", [len(o) for o in orbitsA(SHA)])
# lifts: each A4 surjection's preimages among the 2T surjections
def lifts(S2, SA, n):
    from collections import defaultdict
    L=defaultdict(list)
    for s in S2: L[tuple(proj[x] for x in s)].append(s)
    assert set(L)==set(SA), "every A4 surjection must lift and every lift projects to a surjection"
    return L
LG=lifts(SG2,SGA,2); LH=lifts(SH2,SHA,3)
print("lifts per A4 map: m000", sorted({len(v) for v in LG.values()}), " m004", sorted({len(v) for v in LH.values()}))
# restriction G -> H on A4 maps and on 2T maps
def restr(phi, m, invf):   # phi=(A,B) images of a,b -> (u,v,w)=(bA, aa, ab)
    A,B=phi; return (m(B,invf(A)), m(A,A), m(A,B))
RA={restr(p,a4mul,a4inv) for p in SGA}
print("A4 restriction: distinct images", len(RA), " = all of Surj(m004,A4)?", RA==set(SHA), " (bijective on 24 maps)")
R2=[restr(p,mul,inv) for p in SG2]
ext=set(R2)
per=[sum(1 for l in LH[a] if l in ext) for a in SHA]
print("per m004 A4-map, number of its two 2T lifts that extend over m000:", sorted(set(per)))
# the two m000 lifts of one A4 map differ by the orientation character (w(a)=w(b)=1) and restrict to the same map
z=neg(I)
ok=all( (set(LG[a])=={LG[a][0], (mul(z,LG[a][0][0]), mul(z,LG[a][0][1]))}) and len({restr(l,mul,inv) for l in LG[a]})==1 for a in SGA)
print("m000: the two lifts differ by the orientation twist and restrict to the same 2T map:", ok)
# the non-extending m004 lift is the H^1(m004;C2) twist (character (1,1,0) on u,v,w) of the extending one
tw=lambda s:(mul(z,s[0]),mul(z,s[1]),s[2])
ok2=all( any(l in ext for l in LH[a]) and all((l in ext)!=(tw(l) in ext) for l in LH[a]) for a in SHA)
print("m004: the second lift is the H^1 twist of the extendable one and does not extend:", ok2)
