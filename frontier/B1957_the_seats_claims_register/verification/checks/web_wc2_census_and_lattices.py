"""B1957: the web seat's W-C2 (its check of agy-exp's four theorems that use no data), the parts main recomputes here.
Data-free.  The torsion statements (A1, A2: 277 of the 285 members with one unramified and four ramified lines, the
other 8 with monodromy +-I mod 5; torsion moduli 2 sin(pi/5), 2 sin(2 pi/5), product 5) are main's B1939.
 W1  Theorem B: the census of 285 (B1939's own enumeration), its classes up to isometry by SnapPy: oriented, unoriented,
     amphicheiral, chiral with a symmetry group of order at least 4, chiral with order 2; the least volumes.
 W2  Theorem C.2: H = 2 (0,0,0,0,0,1,1,1) in E8: in the lattice, orthogonal to a d5 and an a2, and +3 on 16 roots, -1 on 48.
 W3  Theorem C.3: in A4, the least k = x.x/2 with a coordinate of size N is N(N+1)/2; the count of non-zero vectors
     with k <= 12 (the lane wrote 1020; the seat found 1350, and 1020 in the band 6 < k <= 12).
 W4  the letter-count function on the two words; the arithmetic of dP9's spectral curve; 248 = 24 + 24 + 4 * 50."""
import sys, pathlib, itertools, collections, io, contextlib
from fractions import Fraction as Fr
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())

if __name__ == "__main__":
    # W1
    sys.path.insert(0, str(next((ROOT / "frontier").glob("B1939_*")) / "verification")); argv = sys.argv; sys.argv = [argv[0]]
    with contextlib.redirect_stdout(io.StringIO()): import torsion_census as TC
    sys.argv = argv; import snappy
    members = TC.cT; ori, unori, kinds, vols = set(), {}, collections.Counter(), {}
    for can, (rot, eps) in members:
        M = snappy.Manifold("b+%s%s" % ("+" if eps == 1 else "-", rot)); so = M.isometry_signature(ignore_orientation=False); su = M.isometry_signature(ignore_orientation=True); ori.add(so)
        if su not in unori:
            G = M.symmetry_group(); unori[su] = ("amphicheiral" if G.is_amphicheiral() else ("chiral, group of order >= 4" if G.order() >= 4 else "chiral, group of order 2"), float(M.volume()), M.homology(), "b+%s%s" % ("+" if eps == 1 else "-", rot))
    kinds = collections.Counter(v[0] for v in unori.values())
    print("W1: %d members; oriented classes %d; unoriented classes %d; of the unoriented: %s (the seat and the lane: 285; 228; 124; 20 / 70 / 34)" % (len(members), len(ori), len(unori), dict(kinds)))
    for k in ("amphicheiral", "chiral, group of order >= 4", "chiral, group of order 2"):
        v = min((x for x in unori.values() if x[0] == k), key=lambda x: x[1]); print("    least volume, %s: %.10f, %s, H1 = %s" % (k, v[1], v[3], v[2]))
    # W2
    roots = [tuple(Fr(x) for x in v) for v in itertools.product((-1, 0, 1), repeat=8) if sum(abs(x) for x in v) == 2 and sum(x * x for x in v) == 2]
    roots += [tuple(Fr(s, 2) for s in v) for v in itertools.product((-1, 1), repeat=8) if list(v).count(-1) % 2 == 0]
    H = (0, 0, 0, 0, 0, 2, 2, 2); half = (0, 0, 0, 0, 0, 1, 1, 1); dot = lambda a, b: sum(x * y for x, y in zip(a, b)); pair = collections.Counter(dot(H, r) for r in roots)
    inE8 = lambda v: (all(Fr(x).denominator == 1 for x in v) or all(Fr(2 * x).denominator == 1 and Fr(x).denominator == 2 for x in v)) and sum(v) % 2 == 0
    d5 = [r for r in roots if all(x.denominator == 1 for x in r) and r[5] == r[6] == r[7] == 0]; a2 = [r for r in roots if dot(H, r) == 0 and r not in d5]
    print("W2: 240 roots: %d; (0,0,0,0,0,1,1,1) in E8: %s; H = twice it in E8: %s; H's pairings with the roots: %s; the roots orthogonal to H: a d5 (%d roots) and %d others" % (len(roots), inE8(half), inE8(H), dict(sorted(pair.items())), len(d5), len(a2)))
    # W3
    R = 6; cnt = collections.Counter(); least = {}
    for x in itertools.product(range(-R, R + 1), repeat=4):
        v = x + (-sum(x),); k2 = sum(c * c for c in v)
        if k2 == 0 or k2 % 2: continue
        k = k2 // 2
        if k <= 12: cnt[k] += 1
        N = abs(v[0]); least[N] = min(least.get(N, 10 ** 9), k)
    tot = lambda a, b: sum(c for k, c in cnt.items() if a < k <= b)
    print("W3: A4, non-zero vectors by k = x.x/2: k <= 12: %d; k <= 10: %d; k <= 11: %d; k <= 6: %d; the band 6 < k <= 12: %d; least k with a coordinate of size N = 1..4: %s (N(N+1)/2: %s)" % (tot(0, 12), tot(0, 10), tot(0, 11), tot(0, 6), tot(6, 12), [least[N] for N in (1, 2, 3, 4)], [N * (N + 1) // 2 for N in (1, 2, 3, 4)]))
    # W4
    psi = lambda w: w.count("L") - w.count("R")
    print("W4: letters L minus R: L^6 R L R: %d; L^5 R L^2 R^2: %d. dP9 with C = 5 S + 6 F (S^2 = -1, S.F = 1, F^2 = 0, K = -F): C^2 = %d, C.K = %d, genus %d, ramification over the section %d. 248 = %d" % (psi("LLLLLLRLR"), psi("LLLLLRLLRR"), 25 * -1 + 2 * 30, -5, (35 - 5) // 2 + 1, 2 * 16 - 2 + 10, 24 + 24 + 4 * 50))
