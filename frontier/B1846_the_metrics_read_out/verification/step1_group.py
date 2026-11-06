"""Step 1 (data-free): the excursion member's holonomy group from SnapPy (cusp at infinity), its homology (b1 must be 1),
and the abelianisation chi on the generators; the figure-eight as the control (B1295's Riley group: chi = 1 on both)."""
import warnings; warnings.filterwarnings("ignore")
import snappy, numpy as np
for name in ("m004", "b++LLLLLLRLR"):
    M = snappy.Manifold(name)
    G = M.fundamental_group()
    gens = G.generators(); rels = G.relators()
    H = M.homology()
    print("%s: vol %.6f  homology %s  generators %s  relators %s" % (name, float(M.volume()), H, gens, rels))
    # the abelianisation chi: Z^n / relators; for b1 = 1 find the integer vector chi with chi . (exponent sums of each relator) = 0
    n = len(gens); E = []
    for r in rels:
        e = [0]*n
        for ch in r:
            i = gens.index(ch.lower()); e[i] += 1 if ch.islower() else -1
        E.append(e)
    E = np.array(E, dtype=float)
    _, s, vt = np.linalg.svd(E) if len(E) else (None, np.array([]), np.eye(n))
    null = vt[np.sum(s > 1e-9):] if len(E) else np.eye(n)
    print("   relator exponent sums", E.astype(int).tolist(), " -> null space of chi:", np.round(null, 6).tolist())
    for g in gens:
        m = G.SL2C(g); a = np.array([[complex(m[0,0]), complex(m[0,1])], [complex(m[1,0]), complex(m[1,1])]])
        print("   holonomy %s = %s  (tr %s, det %s)" % (g, np.round(a, 6).tolist(), np.round(np.trace(a), 6), np.round(np.linalg.det(a), 9)))
    print("   peripheral (meridian, longitude) words:", G.peripheral_curves())
