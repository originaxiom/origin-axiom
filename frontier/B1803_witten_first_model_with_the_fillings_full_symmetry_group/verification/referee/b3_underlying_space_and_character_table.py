"""Referee B1803, b3: a lift-free route to Claim C.
(1) The singular locus of Q/F' (underlying space S^3 = |Q/h1| / Pbar) is a trivalent graph whose vertices are the F'-fixed
    points E+, E- (images of +-e1) and C1, C2 (core points), edges labelled h1, h2, P.  Claim A forces the P-edges E+E-
    and C1C2, the h1-edges E+Ci, E-Ci', and two cases for h2: (I) h2-edges E+Ci, E-Ci' (two bigons with the h1-edges) or
    (II) h2-edges E+Ci', E-Ci (a 4-cycle).
(2) |Q/P| is the 2-fold cover of |Q/F'| = S^3 branched along B = (h1-edges) u (h2-edges): two circles in (I), one in (II).
    dim H1(Sigma_2(S^3, B); Z/2) = #B - 1.  But |Q/P| = |L6a2[(2,0),(p,2q)]| = L6a2[(1,0),(p/2,q)] = (p/2)/q surgery on
    a knot in S^3, H1 = Z/(p/2).  So case (I) iff 4 | p.  Computed below on the fillings.
(3) The characters: Hom(pi1^orb(Q/F'), Z/2) = Z/2 1-cycles of the graph; those vanishing on pi1(Q) are lambda o Phi
    (Phi = edge labels); any other cycle rho restricts to chi.  A vertex's character is rho on its (h1, h2, P) edges.
    Enumerated for both graphs, normalised at E+."""
import snappy, itertools, math
print("(2) H1 of |Q/P| = L6a2[(1,0),(p/2,q)] and the predicted case")
bad = 0
for p in range(2, 41, 2):
    for q in [1, 3, 5, 7, -1, -3]:
        if math.gcd(p, abs(q)) != 1:
            continue
        U = snappy.Manifold("L6a2"); U.dehn_fill([(1, 0), (p // 2, q)])
        H = U.homology()
        z2 = sum(1 for c in H.elementary_divisors() if c % 2 == 0)
        expect = "Z/%d" % (p // 2) if p // 2 > 1 else "0"
        ok = (str(H) == expect)
        bad += (not ok)
        if q in (1, -3):
            print("  m004(%d,%d): H1|Q/P| = %-5s dim H1(;Z/2) = %d -> #B = %d -> case %s%s" % (
                p, q, H, z2, z2 + 1, "I (bigons)" if z2 else "II (4-cycle)", "" if ok else " MISMATCH"))
print("  H1 mismatches against Z/(p/2): %d" % bad)

print("(3) characters from the graph")
V = ["E+", "E-", "C1", "C2"]
def graph(case):
    E = [("E+", "E-", "P"), ("C1", "C2", "P"), ("E+", "C1", "h1"), ("E-", "C2", "h1")]
    E += [("E+", "C1", "h2"), ("E-", "C2", "h2")] if case == "I" else [("E+", "C2", "h2"), ("E-", "C1", "h2")]
    return E
lab = {"h1": (1, 0), "P": (0, 1), "h2": (1, 1)}         # F' = <h1, P>, written additively
for case in ("I", "II"):
    E = graph(case)
    cycles = []
    for vals in itertools.product((0, 1), repeat=len(E)):
        if all(sum(v for v, e in zip(vals, E) if x in e[:2]) % 2 == 0 for x in V):
            cycles.append(vals)
    phi = [tuple(sum(a * b for a, b in zip(lam, lab[e[2]])) % 2 for e in E) for lam in [(0, 0), (1, 0), (0, 1), (1, 1)]]
    others = [c for c in cycles if c not in phi]
    tables = set()
    for rho in others:
        ch = {}
        for x in V:
            d = {e[2]: v for v, e in zip(rho, E) if x in e[:2]}
            ch[x] = (d["h1"], d["h2"], d["P"])
        base = ch["E+"]
        tables.add(tuple((x, tuple((a + b) % 2 for a, b in zip(ch[x], base))) for x in V))
    print("  case %s: cycle space dim %d, Phi-span %d, rho choices %d; tables (h1,h2,P) normalised at E+: %s" % (
        case, int(math.log2(len(cycles))), len(set(phi)), len(others), sorted(tables)))
print("b3 exit 0")
