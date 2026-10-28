"""Referee B1802, r4: the third involution P of m004 (cusp map +I, the period-2 symmetry). Find K' u A' with
m004 = the 2-fold cover of (S^3 - K', branched along A'): a 2-component link, A' filled (2,0), volume vol(m004)/2,
the cover (A' meridian nontrivial, K' meridian trivial) isometric to m004."""
import snappy, time
target = float(snappy.Manifold("m004").volume()) / 2
print("target vol(m004)/2 = %.9f" % target)
m004 = snappy.Manifold("m004")
def lkm(L):
    try: return L.link().linking_matrix()
    except Exception: return "?"
t0 = time.time(); n = 0
for c in range(3, 13):
    for L in snappy.HTLinkExteriors(num_cusps=2, crossings=c):
        for j in (0, 1):
            n += 1
            M = snappy.Manifold(L.name())
            fills = [(0, 0), (0, 0)]; fills[j] = (2, 0)
            try:
                M.dehn_fill(fills); v = float(M.volume())
            except Exception:
                continue
            if abs(v - target) < 1e-6:
                res = []
                for C in M.covers(2):
                    if True:
                        f = C.cusp_info("filling")
                        try:
                            iso = C.is_isometric_to(m004) if sum(1 for x in f if x == (0.0, 0.0)) == 1 else None
                        except Exception as e:
                            iso = "err"
                        res.append((str(C.homology()), f, iso))
                print("  %s branch component %d: vol %.9f, lk %s; 2-fold covers: %s" % (L.name(), j, v, lkm(L), res))
print("scanned %d in %.0fs; r4 exit 0" % (n, time.time() - t0))
