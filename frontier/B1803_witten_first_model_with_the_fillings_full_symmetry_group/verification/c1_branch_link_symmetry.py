"""P-409 check (ii'): on each 2-component branch link L of a strong inversion h1 (Q = Sigma_2(S^3, L), p even), the period
P (= h2 mod h1) descends to an involution of (S^3, L). Claim A needs it to strongly invert BOTH components (cusp maps -I, -I),
so that its axis meets L in 4 points, two on each component = two on each fixed circle of h1. List every symmetry of S^3 - L
with its cusp maps, whether it extends to S^3, and whether it is an involution."""
import snappy

def mat(m):
    return [[int(round(float(m[i][j]))) for j in range(2)] for i in range(2)]

for (p, q), name in [((6, 1), "L11n132"), ((8, 1), "L13n4507"), ((8, 3), "L13n4800"), ((4, 3), "L14n24777")]:
    L = snappy.Manifold(name)
    G = L.symmetry_group()
    print("m004(%d,%d)  %s  Sym(S^3 - L) = %s, order %d, amphicheiral %s" % (p, q, name, G, G.order(), G.is_amphicheiral()))
    for iso in L.is_isometric_to(L, return_isometries=True):
        maps = [mat(m) for m in iso.cusp_maps()]
        dets = [m[0][0] * m[1][1] - m[0][1] * m[1][0] for m in maps]
        print("   cusp perm %s  maps %s  det %s  extends to S^3: %s" % (iso.cusp_images(), maps, dets, iso.extends_to_link()))
print("c1 exit 0")
