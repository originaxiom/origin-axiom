"""Referee B1802, r1: the isometries of m004 and their action on the cusp homology; the symmetry groups of
fillings (is_full_group); which isometries act by -1 on the cusp (strong inversions) vs +1 (period/free)."""
import snappy, math
M = snappy.Manifold("m004")
G = M.symmetry_group()
print("m004 symmetry group:", G, "| order", G.order(), "| amphicheiral", G.is_amphicheiral(), "| invertible", G.is_invertible_knot(), "| full", G.is_full_group())
for k, iso in enumerate(G.isometries()):
    cm = iso.cusp_maps()[0]
    print("  iso %d: cusp map %s | det %d" % (k, [list(r) for r in cm], int(cm[0][0]*cm[1][1]-cm[0][1]*cm[1][0])))
# orientation-preserving isometries of the cusped manifold that act by -1 on H1(cusp):
print()
for (p, q) in [(6, 1), (8, 1), (2, 3), (4, 3), (10, 1), (2, 5), (8, 3), (5, 1), (3, 2), (7, 1), (6, 5), (2, 7), (4, 5)]:
    N = snappy.Manifold("m004"); N.dehn_fill((p, q))
    try:
        S = N.symmetry_group()
        print("m004(%d,%d): sol %s vol %.6f H1 %s | Sym %s full %s amph %s" % (p, q, N.solution_type()[:12], float(N.volume()), N.homology(), S, S.is_full_group(), S.is_amphicheiral()))
    except Exception as e:
        print("m004(%d,%d): err %s" % (p, q, e))
