"""Independent re-derivation of codex R037: restriction of 2T quotients from pi_1(m000) to pi_1(m004).
Own implementation: SL(2,3) as 2x2 matrices over F_3; Aut(2T) as GL(2,3)-conjugation (Aut(SL(2,3)) = S4,
all induced by GL(2,3)); presentations taken from SnapPy directly, and the orientation double cover of
m000 checked to be m004 by SnapPy's own isometry test."""
import itertools, snappy, hashlib

# --- the groups from the manifolds themselves --------------------------------------------------------
m000 = snappy.Manifold("m000"); m004 = snappy.Manifold("m004")
print("m000 orientable?", m000.is_orientable(), " m004 orientable?", m004.is_orientable())
covers = m000.covers(2)
print("index-2 covers of m000:", [(c.name(), c.is_orientable(), c.is_isometric_to(m004)) for c in covers])
G = m000.fundamental_group(); M = m004.fundamental_group()
print("pi_1(m000):", G.generators(), G.relators())
print("pi_1(m004):", M.generators(), M.relators())

# --- SL(2,3) over F_3 ---------------------------------------------------------------------------------
def mul(A,B): return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))%3 for j in range(2)) for i in range(2))
def det(A): return (A[0][0]*A[1][1]-A[0][1]*A[1][0])%3
I=((1,0),(0,1))
GL=[((a,b),(c,d)) for a in range(3) for b in range(3) for c in range(3) for d in range(3) if det(((a,b),(c,d)))!=0]
Q=[A for A in GL if det(A)==1]
def inv(A):
    for B in GL:
        if mul(A,B)==I: return B
assert len(Q)==24 and len(GL)==48
Z=[A for A in Q if all(mul(A,B)==mul(B,A) for B in Q)]
assert len(Z)==2, "center C2"
def gen(S):
    seen={I}; frontier=[I]
    while frontier:
        x=frontier.pop(); 
        for s in S:
            y=mul(x,s)
            if y not in seen: seen.add(y); frontier.append(y)
    return seen
# abelianization order via commutator subgroup
comm=gen([mul(mul(A,B),mul(inv(A),inv(B))) for A in Q for B in Q])
print("|Q|=24, |Z|=2, |Q_ab|=", 24//len(comm))
# Aut(Q) as conjugation by GL(2,3): distinct maps
auts=set()
for g in GL:
    gi=inv(g); auts.add(tuple(mul(mul(g,A),gi) for A in Q))
print("|Aut(Q)| via GL(2,3)-conjugation:", len(auts))
qidx={A:i for i,A in enumerate(Q)}

# --- words -> matrices ---------------------------------------------------------------------------------
def evalword(word, img):   # img: dict letter->matrix, uppercase = inverse
    X=I
    for ch in word:
        A=img[ch.lower()]; X=mul(X, A if ch.islower() else inv(A))
    return X
def surjections(gens, rels):
    out=[]
    for imgs in itertools.product(Q, repeat=len(gens)):
        img=dict(zip(gens,imgs))
        if all(evalword(r,img)==I for r in rels) and len(gen(list(imgs)))==24:
            out.append(imgs)
    return out
SG=surjections(G.generators(), G.relators()); SM=surjections(M.generators(), M.relators())
print("Surj(pi1 m000, 2T):", len(SG), " Surj(pi1 m004, 2T):", len(SM))
def orbits(S, ngens):
    S=set(S); orbs=[]
    while S:
        s=next(iter(S)); orb={tuple(aut[qidx[x]] for x in s) for aut in auts}
        assert orb<=S; S-=orb; orbs.append(orb)
    return orbs
OG=orbits(SG,2); OM=orbits(SM,2)
print("Aut-orbits: m000", [len(o) for o in OG], " m004", [len(o) for o in OM])

# --- the orientation subgroup, by hand (Reidemeister-Schreier, transversal {1,a}) -----------------------
# orientation character of m000: the unique nonzero mod-2 character; check it on the relator.
ga,gb = G.generators()
def char_ok(w):  # w: dict gen->0/1
    return all(sum(w[ch.lower()] for ch in r)%2==0 for r in G.relators())
chars=[w for w in [{ga:0,gb:1},{ga:1,gb:0},{ga:1,gb:1}] if char_ok(w)]
print("nonzero mod-2 characters of pi1(m000):", chars)
# Schreier generators for transversal {1,a} with w(a)=w(b)=1: u = b a^-1, v = a^2, w = a b  (as in R037)
# Codex's Tietze map to M's generators: c = w^-1, d = w u^-1 => c = (ab)^-1 = B A,  d = a b a b^-1  ... compute as words in a,b
def restrict(phi):        # phi = (A,B) images of a,b
    img={ga:phi[0], gb:phi[1]}
    u=evalword(gb+ga.upper(), img); v=evalword(ga+ga, img); w=evalword(ga+gb, img)
    c=inv(w); d=mul(w,inv(u))
    return (c,d)
mc,md = M.generators()
R=[]
for phi in SG:
    c,d=restrict(phi); img={mc:c, md:d}
    assert all(evalword(r,img)==I for r in M.relators()), "restricted map must satisfy m004's relators"
    assert len(gen([c,d]))==24, "restriction must stay surjective"
    R.append((c,d))
Rset=set(R)
print("distinct restricted maps:", len(Rset), " fibre sizes:", sorted({R.count(x) for x in Rset}))
print("restricted image is one of m004's orbits?", [Rset==o for o in OM])
# the non-extendable orbit = central twist of the extendable one by the nonzero class of H^1(m004;C2)
z=[A for A in Z if A!=I][0]
mchars=[w for w in [{mc:0,md:1},{mc:1,md:0},{mc:1,md:1}] if all(sum(w[ch.lower()] for ch in r)%2==0 for r in M.relators())]
print("nonzero mod-2 characters of pi1(m004):", mchars)
for w in mchars:
    twist={ (mul(z,c) if w[mc] else c, mul(z,d) if w[md] else d) for (c,d) in Rset}
    print("central twist by", w, "maps the extendable orbit onto the other orbit?", [twist==o for o in OM])
# also: the two m000 orbits both restrict onto the same m004 orbit
for o in OG:
    print("m000 orbit of size", len(o), "restricts onto", [ {restrict(p) for p in o}==om for om in OM])
h=hashlib.sha256(repr(sorted(Rset)).encode()).hexdigest()[:16]
print("digest of restricted image:", h)
