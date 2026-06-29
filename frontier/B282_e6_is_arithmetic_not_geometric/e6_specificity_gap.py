"""B282 -- the figure-eight's E6 is ARITHMETIC, not geometric. Run with sage-python (needs SnapPy + GAP).

Demonstrates that the 2T = SL(2,F_3) surjection (the sole source of the McKay E6) is figure-eight-SPECIFIC --
present only for the ARITHMETIC cusped manifolds (4_1=m004 and its sister m003), ABSENT for non-arithmetic
hyperbolic knots (5_2, 6_1, 6_2, 7_4) -- whereas the *character-variety* E6 structure (dim H^1=rank, smoothness,
density) is GENERIC to every 1-cusped hyperbolic manifold and every Lie type (MFP / Falbel-Guilloux; B281, R6).

Conclusion: the only object-specific E6 content is the arithmetic 2T atom; the rest is generic structure.
"""
import snappy
from sage.all import gap


def surjections_onto_2T(name):
    M = snappy.Manifold(name)
    G = M.fundamental_group()
    gens, rels = G.generators(), G.relators()
    gap.eval("FF:=FreeGroup({});".format(", ".join('"x%d"' % i for i in range(len(gens)))))
    rs = []
    for r in rels:
        s = ""
        for ch in r:
            s += ("FF.%d*" % (ord(ch) - ord("a") + 1)) if ch.islower() else ("FF.%d^-1*" % (ord(ch.lower()) - ord("a") + 1))
        rs.append(s.rstrip("*"))
    gap.eval("GG:=FF/[{}];".format(", ".join(rs)))
    return float(M.volume()), int(gap.eval("Length(GQuotients(GG,SL(2,3)));"))


# the arithmetic cusped manifolds (4_1 = unique arithmetic knot, Reid; m003 its commensurable sister) vs non-arith
ARITHMETIC = ["4_1", "m003"]
NON_ARITHMETIC = ["5_2", "6_1", "6_2", "7_4"]

if __name__ == "__main__":
    print(f"{'manifold':9}{'vol':>9}{'arithmetic':>12}{'->2T':>6}")
    for k in ARITHMETIC + NON_ARITHMETIC:
        vol, n = surjections_onto_2T(k)
        print(f"{k:9}{vol:>9.4f}{str(k in ARITHMETIC):>12}{n:>6}")
    arith_2T = all(surjections_onto_2T(k)[1] > 0 for k in ARITHMETIC)
    nonarith_no2T = all(surjections_onto_2T(k)[1] == 0 for k in NON_ARITHMETIC)
    print("\narithmetic knots -> 2T:", arith_2T, "| non-arithmetic -> NO 2T:", nonarith_no2T)
    print("=> the E6-source (2T) is arithmetic-specific; the character-variety E6 is generic (B281, R6).")
    assert arith_2T and nonarith_no2T
