"""Main's own check of BANK-1's topology (2026-11-24; data-free; SnapPy + brute force, no seat code)."""
import snappy, itertools
G = snappy.Manifold("m000"); F = snappy.Manifold("m004")
print("m000: orientable", G.is_orientable(), "| volume", G.volume(), "| H1", G.homology(), "| cusps", G.num_cusps())
print("m004: volume", F.volume(), "| H1", F.homology())
c2 = G.covers(2)
print("m000's 2-fold covers:", len(c2), [ (C.is_orientable(), str(C.homology()), C.is_isometric_to(F)) for C in c2 ])
# brute force: homomorphisms of pi1(m004) onto small permutation groups
pi = F.fundamental_group(); gens = pi.generators(); rels = pi.relators()
print("pi1(m004):", gens, rels)
def perm_mul(p, q): return tuple(p[q[i]] for i in range(len(q)))   # p after q
def perm_inv(p):
    r = [0] * len(p)
    for i, x in enumerate(p): r[x] = i
    return tuple(r)
def evalword(w, img, n):
    r = tuple(range(n))
    for ch in w:
        g = img[ch.lower()]; r = perm_mul(r, g if ch.islower() else perm_inv(g))
    return r
def group_gen(gs, n):
    S = {tuple(range(n))}; frontier = list(S)
    while frontier:
        new = []
        for x in frontier:
            for g in gs:
                y = perm_mul(g, x)
                if y not in S: S.add(y); new.append(y)
        frontier = new
    return S
for n in (3, 4, 5):
    allp = list(itertools.permutations(range(n))); found = {}
    for a, b in itertools.product(allp, repeat=2):
        img = {"a": a, "b": b}
        if all(evalword(r, img, n) == tuple(range(n)) for r in rels):
            H = group_gen([a, b], n)
            if len(H) > 2 and any(perm_mul(x, y) != perm_mul(y, x) for x in H for y in H):
                found.setdefault(len(H), 0); found[len(H)] += 1
    print("non-abelian images of pi1(m004) in S_%d, by order: %s" % (n, found))
for deg in (5, 10):
    cs = F.covers(deg)
    print("m004's %d-fold covers: %d; cusps per cover: %s" % (deg, len(cs), [C.num_cusps() for C in cs]))
L = snappy.Manifold("8^3_4"); print("8^3_4: volume", L.volume(), "| cusps", L.num_cusps(), "| H1", L.homology())
for C in F.covers(5):
    if C.num_cusps() == 3:
        print("  the 3-cusp 5-fold cover: volume", C.volume(), "| H1", C.homology(), "| isometric to 8^3_4:", C.is_isometric_to(L), "| cover type", C.cover_info().get("type"))
for C in F.covers(10):
    print("  a 10-fold cover: cusps", C.num_cusps(), "| H1", C.homology(), "| type", C.cover_info().get("type"))
