#!/usr/bin/env python3
"""B1490 (draft): LP01's common cover of m004 and o10_150726, built and measured on main by its own code.

The seat's data: exact holonomies in SL(2, Z[w]) (reps.txt: entries [x, y] = x + y w, w^2 + w + 1 = 0; a matrix as
[a, b, c, d]).  Main's code: the arithmetic in Z[w] and Z[w]/4, the image of the figure-eight group K mod 4 (160 elements
of the 1920 of SL(2, Z[w]/4)/{+-I} -- NOT PSL(2, Z[w]/4), whose order is 960 (the record's E21 guard); index 12 -- level 4 in the
standard sense: K contains the image of the SL kernel), the action of pi_1(target) on the 12 cosets, the orbit containing K and its stabiliser,
the cover built in SnapPy from the permutation representation, and its measures: cusps, H_1, volume, |Sym|, chirality
(an orientation-reversing isometry), and B1418's cusp counts |det(X - I)| over the cusp-fixing orientation-preserving
isometries (the 'three' is a value 3).

  common_cover_main.py controls         relators, determinants, SnapPy's traces, the level, K's conjugacy class
  common_cover_main.py cover TARGET     the cover and its measures  -> cover_<target>.json
"""
import sys, json, pathlib, itertools, collections
HERE = pathlib.Path(__file__).resolve().parent
N = 4

# ---- Z[w] and Z[w]/N
def add(x, y, n=0): return ((x[0]+y[0]) % n, (x[1]+y[1]) % n) if n else (x[0]+y[0], x[1]+y[1])
def mul(x, y, n=0):
    p, q = x; r, s = y; v = (p*r - q*s, p*s + q*r - q*s)
    return (v[0] % n, v[1] % n) if n else v
def neg(x, n=0): return ((-x[0]) % n, (-x[1]) % n) if n else (-x[0], -x[1])
def mmul(A, B, n=0): return tuple(tuple(add(mul(A[i][0], B[0][j], n), mul(A[i][1], B[1][j], n), n) for j in range(2)) for i in range(2))
def det(A, n=0): return add(mul(A[0][0], A[1][1], n), neg(mul(A[0][1], A[1][0], n), n), n)
def minv(A):            # det = 1
    return ((A[1][1], neg(A[0][1])), (neg(A[1][0]), A[0][0]))
def red(A, n): return tuple(tuple((e[0] % n, e[1] % n) for e in r) for r in A)
def canon(A, n): B = tuple(tuple(neg(e, n) for e in r) for r in A); return min(A, B)
def cx(e): import cmath; w = cmath.exp(2j*cmath.pi/3); return e[0] + e[1]*w
ONE, ZERO, W = (1, 0), (0, 0), (0, 1)
I2 = ((ONE, ZERO), (ZERO, ONE))
RILEY = {"a": ((ONE, ONE), (ZERO, ONE)), "b": ((ONE, ZERO), (neg(W), ONE))}
# the LP seat's m004 (its FINDINGS section 1): a = [[w, 1], [-1-w, -1]], b = [[1, 2], [-1-w, -1-2w]]; relator aaabABBAb = -I
M004_SEAT = {"a": ((W, ONE), ((-1, -1), (-1, 0))), "b": ((ONE, (2, 0)), ((-1, -1), (-1, -2)))}


def load(name):
    for line in open(HERE / "lp_reps.txt"):
        nm, js = line.split(" ", 1)
        if nm == name:
            d = json.loads(js); rep = {g: ((tuple(d["rep"][g][0]), tuple(d["rep"][g][1])), (tuple(d["rep"][g][2]), tuple(d["rep"][g][3]))) for g in d["gens"]}
            return d["gens"], d["rels"], rep
    raise KeyError(name)


def word(wd, rep, n=0):
    M = I2
    for ch in wd: M = mmul(M, rep[ch] if ch.islower() else minv(rep[ch.lower()]), n)
    return M


def closure(gens, n):
    seen = {canon(I2, n)}; frontier = list(seen)
    while frontier:
        nxt = []
        for g in frontier:
            for h in gens:
                for p in (mmul(g, h, n), mmul(h, g, n)):
                    c = canon(p, n)
                    if c not in seen: seen.add(c); nxt.append(c)
        frontier = nxt
    return seen


def psl_mod(n):
    """all of SL(2, Z[w]/n) modulo +-I by closure from generators (the canonical form identifies +-A).  For n = 4 this is the
    order-1920 group SL(2, Z[w]/4)/{+-I}, which is NOT PSL(2, Z[w]/4) (order 960; the centre of SL(2, Z[w]/4) has four
    elements) -- the record's E21 class.  The name is kept for the file's history; the docstring is the truth."""
    gens = [((ONE, ONE), (ZERO, ONE)), ((ONE, W), (ZERO, ONE)), ((ONE, ZERO), (ONE, ONE)), ((ONE, ZERO), (W, ONE))]
    return closure(gens, n)


def cosets(Kbar, G):
    """left cosets g Kbar in G, keyed by a canonical representative"""
    Kl = list(Kbar); keys = {}
    for x in G:
        k = min(canon(mmul(x, h, N), N) for h in Kl)
        keys.setdefault(k, x)
    return keys


def perm_action(keys, Kbar, gens_mod):
    """for each generator h: the permutation i -> index of the coset h * (coset i)"""
    Kl = list(Kbar); names = list(keys); index = {k: i for i, k in enumerate(names)}
    def key_of(x): return min(canon(mmul(x, h, N), N) for h in Kl)
    perms = {}
    for g, h in gens_mod.items():
        perms[g] = [index[key_of(mmul(h, keys[k], N))] for k in names]
    return perms, index


def orbit_perms(target, m004=None):
    """(gens, rels, P, number of cosets): P[g] is the LEFT action i -> index of g * coset_i on the orbit of K's coset"""
    m004 = m004 or M004_SEAT
    gens, rels, rep = load(target)
    G4 = psl_mod(4); Kbar = closure([red(m004[g], N) for g in "ab"] + [red(minv(m004[g]), N) for g in "ab"], N)
    keys = cosets(Kbar, G4); assert len(keys) == 12, len(keys)
    perms, index = perm_action(keys, Kbar, {g: red(rep[g], N) for g in gens})
    k0 = min(canon(mmul(I2, h, N), N) for h in Kbar); i0 = index[k0]
    orbit = {i0}; frontier = [i0]
    while frontier:
        nxt = []
        for i in frontier:
            for g in gens:
                j = perms[g][i]
                if j not in orbit: orbit.add(j); nxt.append(j)
        frontier = nxt
    orbit = sorted(orbit); relabel = {c: i for i, c in enumerate(orbit)}
    return gens, rels, {g: [relabel[perms[g][c]] for c in orbit] for g in gens}, len(keys)


if __name__ == "__main__":
    import snappy
    cmd = sys.argv[1]
    if cmd == "controls":
        out = {}
        for name in ("m004", "o10_150726", "m202", "s959"):
            try: gens, rels, rep = load(name)
            except KeyError: continue
            rec = dict(det_one=all(det(rep[g]) == ONE for g in gens),
                       relators_pm_identity=all(word(r, rep) in (I2, tuple(tuple(neg(e) for e in r_) for r_ in I2)) for r in rels))
            M = snappy.Manifold(name); G = M.fundamental_group()
            rec["snappy_presentation_matches"] = (G.generators() == gens and sorted(G.relators()) == sorted(rels))
            # traces squared against SnapPy's holonomy (up to conjugation in PSL the traces squared must agree)
            tr2 = []
            for g in gens:
                t = cx(add(rep[g][0][0], rep[g][1][1])); s = complex(G.SL2C(g).trace()) if hasattr(G.SL2C(g), "trace") else None
                tr2.append((g, round((t*t).real, 6), round((t*t).imag, 6), round((s*s).real, 6) if s is not None else None, round((s*s).imag, 6) if s is not None else None))
            rec["trace_squares (exact vs SnapPy)"] = tr2
            rec["traces_agree"] = all(x[3] is not None and abs(x[1]-x[3]) < 1e-4 and abs(x[2]-x[4]) < 1e-4 for x in tr2)
            out[name] = rec; print(name, json.dumps(rec), flush=True)
        G4 = psl_mod(4); out["|PSL(2, Z[w]/4)|"] = len(G4)
        Kr = closure([red(RILEY[g], N) for g in RILEY] + [red(minv(RILEY[g]), N) for g in RILEY], N)
        m004 = M004_SEAT; gens = ["a", "b"]
        Ks = closure([red(m004[g], N) for g in gens] + [red(minv(m004[g]), N) for g in gens], N)
        out["K_riley_mod4"] = len(Kr); out["K_seat_mod4"] = len(Ks)
        out["index_12_both"] = (len(G4) == 12 * len(Kr) == 12 * len(Ks))
        conj = [x for x in G4 if {canon(mmul(mmul(x, k, N), minv_mod(x) if False else x, N), N) for k in []} == set()][:0]
        # conjugacy of the two images inside PSL(2, Z[w]/4): is there x with x Kr x^-1 = Ks ?
        def inv_mod(A):
            d = det(A, N); assert d == ONE, d; return red(minv(A), N)
        found = None
        for x in G4:
            xi = inv_mod(x)
            if all(canon(mmul(mmul(x, k, N), xi, N), N) in Ks for k in list(Kr)[:40]):
                if {canon(mmul(mmul(x, k, N), xi, N), N) for k in Kr} == Ks: found = x; break
        out["K_seat_conjugate_to_K_riley_mod4"] = found is not None
        json.dump(out, open(HERE / "controls.json", "w"), indent=1, default=str); print(json.dumps({k: v for k, v in out.items() if not isinstance(v, dict)}))
    elif cmd == "cover":
        target = sys.argv[2]; gens, rels, P, ncos = orbit_perms(target, RILEY if "--riley" in sys.argv else M004_SEAT)
        n = len(next(iter(P.values()))); sub_perms = [P[g] for g in gens]
        # SnapPy's cover(perms) composes the permutations in word order (a right action); P is the LEFT action
        # i -> index of h * coset_i, so its INVERSES are passed.  The sealed run passed P itself and built the other
        # stabiliser (the right-action one); subgroup_h1.py found it, and the correction is disclosed.
        inverse_perms = [[P[g].index(i) for i in range(n)] for g in gens]
        out = dict(target=target, cosets=ncos, orbit_size=n, perms_left_action=sub_perms, perms_passed_to_snappy=inverse_perms)
        M = snappy.Manifold(target); G = M.fundamental_group(); assert G.generators() == gens
        C = M.cover(inverse_perms)
        out["cover"] = dict(volume=float(C.volume()), volume_over_m004=float(C.volume()) / float(snappy.Manifold("m004").volume()), volume_over_target=float(C.volume()) / float(M.volume()),
                            cusps=C.num_cusps(), H1=str(C.homology()), tetrahedra=C.num_tetrahedra())
        print(json.dumps(out["cover"]), flush=True)
        # isometries, cusp maps, chirality, B1418's cusp counts
        isos = C.is_isometric_to(C, return_isometries=True)
        rows = []; reversing = 0; dets = collections.Counter()
        for iso in isos:
            maps = iso.cusp_maps(); imgs = iso.cusp_images()
            d0 = int(round(maps[0].det())) if hasattr(maps[0], "det") else int(maps[0][0][0]*maps[0][1][1] - maps[0][0][1]*maps[0][1][0])
            if d0 == -1: reversing += 1; continue
            for i in range(C.num_cusps()):
                if imgs[i] == i:
                    X = maps[i]; a, b, c, d = int(X[0][0]), int(X[0][1]), int(X[1][0]), int(X[1][1])
                    dets[abs((a-1)*(d-1) - b*c)] += 1
        out["isometries"] = dict(total=len(isos), orientation_reversing=reversing, chiral=(reversing == 0), cusp_fixing_det_values=dict(dets), three=(3 in dets))
        out["cusp_shapes"] = [str(s) for s in C.cusp_info("shape")]
        print(json.dumps(out["isometries"]), flush=True)
        json.dump(out, open(HERE / f"cover_{target}.json", "w"), indent=1, default=str)
