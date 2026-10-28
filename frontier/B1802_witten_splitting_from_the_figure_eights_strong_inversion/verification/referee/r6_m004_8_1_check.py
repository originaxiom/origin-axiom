"""Referee B1802, r6: is the 'not isometric' verdict for m004(8,1) real or a SnapPy closed-manifold failure?
Compare homology, volume, Chern-Simons, short geodesic spectrum; retry is_isometric_to on retriangulations."""
import snappy
Q = snappy.Manifold("m004"); Q.dehn_fill((8, 1))
def summary(X):
    try: cs = float(X.chern_simons())
    except Exception: cs = None
    try: ls = [round(float(g['length'].real), 6) for g in X.length_spectrum(1.5)]
    except Exception as e: ls = "err %s" % e
    return str(X.homology()), round(float(X.volume()), 9), cs, ls[:8] if isinstance(ls, list) else ls
print("Q = m004(8,1):", summary(Q))
cands = {}
O = snappy.Manifold("L6a2"); O.dehn_fill([(2, 0), (8, 2)])
cands["P-quotient L6a2[(2,0),(8,2)]"] = O
for name, k in (("L10n55", 2), ("K9n7", 1), ("K11n118", 1)):
    X = snappy.Manifold(name); X.dehn_fill([(2, 0)] * k); cands[name] = X
for label, O in cands.items():
    for C in O.covers(2):
        f = C.cusp_info("filling")
        if all(abs(x[0] - 1) < 1e-9 and abs(x[1]) < 1e-9 for x in f):
            Cf = C.filled_triangulation()
            res = []
            for trial in range(6):
                A = Cf.copy(); A.randomize()
                B = Q.filled_triangulation(); B.randomize()
                try: res.append(bool(snappy.Manifold(A).is_isometric_to(snappy.Manifold(B))))
                except Exception as e: res.append("err")
            print("  %-30s Sigma_2: %s | isometric trials %s" % (label, summary(C), res))
