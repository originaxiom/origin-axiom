"""Referee B1802, r3: find, in the Hoste-Thistlethwaite link table, the branch link L with Q = Sigma_2(S^3, L) for some
fillings Q = m004(p,q): the orbifold (S^3, L, cone angle pi) has volume vol(Q)/2; confirm by computing the orbifold's
2-fold cover in which every meridian is nontrivial (all lifted fillings (1,0)) and testing isometry with Q.
Count L's components: the arc predicts 2 for p even, 1 (a knot) for p odd."""
import snappy, sys, time, json
maxcross = int(sys.argv[1]) if len(sys.argv) > 1 else 11
targets = {}
for (p, q) in [(6, 1), (8, 1), (2, 3), (4, 3), (10, 1), (5, 1), (3, 2), (7, 1), (6, 5), (2, 5), (8, 3)]:
    N = snappy.Manifold("m004"); N.dehn_fill((p, q)); targets[(p, q)] = (float(N.volume()) / 2, N)
print("targets (vol/2):", {k: round(v[0], 6) for k, v in targets.items()})
t0 = time.time(); hits = []; n = 0
for cusps in (1, 2, 3):
    for c in range(3, maxcross + 1):
        for L in snappy.HTLinkExteriors(num_cusps=cusps, crossings=c):
            n += 1
            try:
                L.dehn_fill([(2, 0)] * cusps)
                v = float(L.volume())
            except Exception:
                continue
            for k, (tv, N) in targets.items():
                if abs(v - tv) < 1e-6:
                    hits.append((k, L.name(), cusps, v))
print("scanned %d links up to %d crossings in %.0fs" % (n, maxcross, time.time() - t0))
confirmed = []
for k, name, cusps, v in hits:
    L = snappy.Manifold(name); L.dehn_fill([(2, 0)] * cusps)
    N = targets[k][1]
    ok = False
    for C in L.covers(2):
        fills = C.cusp_info("filling")
        if all(abs(f[0] - 1) < 1e-9 and abs(f[1]) < 1e-9 for f in fills):
            try:
                ok = bool(C.is_isometric_to(N))
            except Exception as e:
                ok = "err %s" % e
    print("  m004%s: L = %-10s components %d  orbifold vol %.9f  Sigma_2(L) isometric to Q: %s" % (k, name, cusps, v, ok))
    confirmed.append((k, name, cusps, ok))
print("r3 exit 0")
