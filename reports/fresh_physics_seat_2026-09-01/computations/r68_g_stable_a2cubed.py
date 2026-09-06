"""R68 -- g-stable A2^3 subsystems of the icosian E6: count triples of mutually orthogonal g-orbit planes."""
import io, contextlib, itertools
src = open('r64_founding_ratio_type.py').read().split("# ---- E8 conjugacy type")[0]
buf = io.StringIO()
with contextlib.redirect_stdout(buf): exec(src)
E6r = E6                                           # the 72 roots orthogonal to {1, g}
# g-orbits on E6 roots (left multiplication)
orbits, seen = [], set()
for r in E6r:
    if r in seen: continue
    o = [r, qmul(g, r), qmul(g, qmul(g, r))]; seen |= set(o); orbits.append(o)
print("g-orbits on the 72 E6 roots:", len(orbits))
# each orbit spans an A2 plane iff B(r, g r) = -1/2 and the three roots sum to zero (r + gr + g^2 r = (1+g+g^2) r = 0)
one = (ONE5, ZERO5, ZERO5, ZERO5)
assert all(B(o[0], o[1]) == Fr(-1, 2) for o in orbits)
assert all(tuple(fadd(fadd(a, b), c) for a, b, c in zip(*o)) == (ZERO5,)*4 for o in orbits)
print("every orbit spans an A2 plane (B(r,gr) = -1/2, r + gr + g^2 r = 0): True")
# the plane's six roots: +-r, +-gr, +-g^2 r ; planes as frozensets of the 6 roots
planes = []
for o in orbits:
    six = frozenset(o + [tuple(fneg(c) for c in r) for r in o])
    if six not in planes: planes.append(six)
print("distinct A2 planes:", len(planes))
def orth(P, Q): return all(B(p, q) == 0 for p in P for q in Q)
triples = [(i, j, k) for i, j, k in itertools.combinations(range(len(planes)), 3) if orth(planes[i], planes[j]) and orth(planes[i], planes[k]) and orth(planes[j], planes[k])]
print("mutually orthogonal triples of g-planes (g-stable A2^3 subsystems of E6):", len(triples))
# and the total number of A2^3 subsystems of E6 (control): count triples of mutually orthogonal A2's among ALL A2 subsystems
roots6 = E6r
rset = set(roots6)
def qadd(p, q): return tuple(fadd(a, b) for a, b in zip(p, q))
allA2 = set()
for a in roots6:
    for b in roots6:
        if B(a, b) == Fr(-1, 2):
            c = tuple(fneg(x) for x in qadd(a, b))   # a + b + c = 0 with c a root
            if c in rset:
                allA2.add(frozenset([a, b, c] + [tuple(fneg(x) for x in r) for r in (a, b, c)]))
allA2 = list(allA2)
print("all A2 subsystems of E6:", len(allA2), "(E6 has 120)")
allTriples = 0
for i, j, k in itertools.combinations(range(len(allA2)), 3):
    if orth(allA2[i], allA2[j]) and orth(allA2[i], allA2[k]) and orth(allA2[j], allA2[k]): allTriples += 1
print("all A2^3 subsystems of E6:", allTriples, "(= 51840/1296 = 40 expected)")
# also: is every g-plane among the A2 subsystems, and does each g-stable A2^3 contain only g-planes (by construction yes)
print("g-planes are A2 subsystems:", all(p in set(allA2) for p in planes))

# ---- structure of the 4 triples
cover = collections.Counter(i for t in triples for i in t) if 'collections' in dir() else None
import collections
cover = collections.Counter(i for t in triples for i in t)
print("each plane lies in how many triples:", dict(sorted(collections.Counter(cover.values()).items())), "-> partition of the 12 planes into 4 frames:", set(cover.values()) == {1} and len(cover) == 12)
# symmetries commuting with left-g and preserving the plane {1,g}: right multiplication by units of Z[g] (+-1, +-g, +-g^2), and quaternion conjugation
def plane_index(P):
    return next(i for i, Q in enumerate(planes) if Q == P)
def act_on_triples(fmap, name):
    perm = []
    for t in triples:
        imgs = tuple(sorted(plane_index(frozenset(fmap(r) for r in planes[i])) for i in t))
        perm.append(triples.index(imgs) if imgs in triples else None)
    print(f"  {name:38s}: triples -> {perm}")
    return perm
g2 = qmul(g, g)
units_Zg = [one, g, g2, tuple(fneg(c) for c in one), tuple(fneg(c) for c in g), tuple(fneg(c) for c in g2)]
print("action on the 4 triples:")
perms = [act_on_triples(lambda r, u=u: qmul(r, u), f"right mult by {'1' if u == one else 'unit'}") for u in units_Zg[1:3]]
try:
    pc = act_on_triples(qconj, "quaternion conjugation (B1270's mirror)")
except RuntimeError:
    pc = None; print("  quaternion conjugation: maps left-g-planes to right-g-planes -- does NOT act on this set")
# does conjugation preserve E6 = {1,g}^perp?  conj maps g -> g^-1 = g^2, plane preserved, so yes
# orbits of the group generated
gens = [p for p in perms + [pc] if p is not None and None not in p]
orb, seen = [], set()
for t in range(len(triples)):
    if t in seen: continue
    o = {t}; fr = [t]
    while fr:
        x = fr.pop()
        for p in gens:
            y = p[x]
            if y not in o: o.add(y); fr.append(y)
    seen |= o; orb.append(sorted(o))
print("orbits of the 4 triples under <right units, conjugation>:", orb)

# ---- direct enumeration over ALL 40 A2^3 subsystems: stability under left-g, right-g, both
A2triples = [(i, j, k) for i, j, k in itertools.combinations(range(len(allA2)), 3) if orth(allA2[i], allA2[j]) and orth(allA2[i], allA2[k]) and orth(allA2[j], allA2[k])]
assert len(A2triples) == 40
def subsystem_roots(t): return frozenset().union(*[allA2[i] for i in t])
def stable(t, fmap):
    S = subsystem_roots(t); return frozenset(fmap(r) for r in S) == S
Lstable = [t for t in A2triples if stable(t, lambda r: qmul(g, r))]
Rstable = [t for t in A2triples if stable(t, lambda r: qmul(r, g))]
both = [t for t in A2triples if stable(t, lambda r: qmul(g, r)) and stable(t, lambda r: qmul(r, g))]
print(f"of the 40 A2^3 subsystems of E6: left-g-stable {len(Lstable)}, right-g-stable {len(Rstable)}, two-sided {len(both)}")
if len(both) == 1:
    t = both[0]; S = subsystem_roots(t)
    print("the unique two-sided A2^3: 18 roots; its three planes each two-sided?", [stable((i,), lambda r: qmul(r, g)) and stable((i,), lambda r: qmul(g, r)) for i in t])
    # is it the frame fixed above? compare with planes[] indexing
    fr_planes = [plane_index(allA2[i]) if allA2[i] in planes else None for i in t]
    print("as g-plane indices:", fr_planes, "-> matches the fixed triple", triples[1] if len(triples) > 1 else None)
    # the roots of the selected frame, as quaternions (first plane)
    print("first plane's roots:", [tuple(f"{c[0]}+{c[1]}r5" for c in r) for r in sorted(allA2[t[0]])][:3])
S_sel = subsystem_roots(both[0])
conj_inv = frozenset(qconj(r) for r in S_sel) == S_sel
print("selected frame invariant under quaternion conjugation (the mirror):", conj_inv)
open('r68_result.txt', 'w').write(f"{len(Lstable)} {len(Rstable)} {len(both)} {conj_inv}\n")
