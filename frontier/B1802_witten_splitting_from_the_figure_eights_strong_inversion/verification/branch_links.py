"""B1802, main's check of § 2's table without the referee's scan: for each named branch link L, fill every cusp of S^3 - L
at (2, 0) (the orbifold with cone angle pi), take the 2-fold cover in which every lifted filling is (1, 0) (the double
branched cover), and test isometry with Q = m004(p, q). Also print Q's H1 and L's component count (two exactly when p is
even)."""
import snappy

TABLE = [((6, 1), "L11n132"), ((8, 1), "L13n4507"), ((8, 3), "L13n4800"), ((4, 3), "L14n24777"),
         ((5, 1), "K10n31"), ((7, 1), "K12n749"), ((3, 2), "K13n2180")]

for (p, q), name in TABLE:
    Q = snappy.Manifold("m004"); Q.dehn_fill((p, q))
    L = snappy.Manifold(name); k = L.num_cusps(); L.dehn_fill([(2, 0)] * k)
    iso = []
    for C in L.covers(2):
        fills = C.cusp_info("filling")
        if all(abs(f[0] - 1) < 1e-9 and abs(f[1]) < 1e-9 for f in fills):
            iso.append(bool(C.is_isometric_to(Q)))
    print("m004(%d, %d): H1 %s, vol/2 %.9f; %-10s components %d, orbifold vol %.9f; double branched cover isometric to Q: %s"
          % (p, q, Q.homology(), float(Q.volume()) / 2, name, k, float(L.volume()), iso))
print("branch_links exit 0")
