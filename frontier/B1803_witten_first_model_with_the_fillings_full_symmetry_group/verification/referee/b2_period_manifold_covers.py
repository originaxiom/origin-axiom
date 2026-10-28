"""Referee B1803, b2: an independent code path for epsilon (P's relative lift, axis A vs core C), avoiding c2's abelianised
hom enumeration.  The F'-free argument: with Qt the chi-double cover of Q and P~0 the lift of P trivial over A, the other lift
P~1 = P~0 * deck is FREE iff P~0 is also trivial over C (epsilon = 0).  So epsilon = 0 iff the orbifold O = Q/P has a
second 2-fold cover that is a manifold (besides Q itself).  Enumerate O.covers(2) with SnapPy's permutation-representation
code, call a cover a manifold iff every lifted filling coefficient is primitive, and compare #manifold covers with
1 + [p = 0 mod 4].  On a subset also test that one manifold cover is isometric to Q (the identification Q/P = O)."""
import snappy, math
rows = bad = 0
iso_checked = 0
for p in range(2, 41, 2):
    for q in [1, 3, 5, 7, 9, -1, -3, -5, -7]:
        if math.gcd(p, abs(q)) != 1:
            continue
        O = snappy.Manifold("L6a2"); O.dehn_fill([(2, 0), (p, 2 * q)])
        covs = O.covers(2)
        man = []
        for C in covs:
            fills = C.cusp_info("filling")
            prim = all(math.gcd(int(round(a)), int(round(b))) == 1 for a, b in fills)
            if prim:
                man.append(C)
        pred = 1 + (p % 4 == 0)
        ok = (len(man) == pred and len(covs) == 3)
        isos = ""
        if p <= 12 and abs(q) <= 5 and (p, abs(q)) not in [(2, 1), (4, 1)]:
            Q = snappy.Manifold("m004"); Q.dehn_fill((p, q))
            res = []
            for C in man:
                try:
                    res.append(bool(C.is_isometric_to(Q)))
                except Exception:
                    res.append("err")
            isos = " manifold covers isometric to Q: %s" % res
            iso_checked += 1
            ok = ok and res.count(True) == 1
        rows += 1; bad += (not ok)
        print("m004(%3d,%2d): O has %d double covers, %d manifolds (predicted %d, p mod 4 = %d)%s%s" % (
            p, q, len(covs), len(man), pred, p % 4, isos, "" if ok else "  MISMATCH"))
print("fillings %d (isometry-tested %d), mismatches %d" % (rows, iso_checked, bad))
print("b2 exit 0")
