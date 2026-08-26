"""Paper II, Proposition 1.3: the four degrees are FORCED, not selected.

Checks that (a) t and Phi really are binary tetrahedral invariants, (b) 2T's invariant
degrees meet E6's principal-sl2 summand degrees in exactly {8,14,16,22}, and (c) each
such degree is realised by a unique monomial in the generators.

Controls are included so the checks can fail: 2O and 2I are run through the same
degree-intersection and must give DIFFERENT answers, and a deliberately wrong form is
tested for invariance and must be rejected.

Run: python3 check_forcing.py
"""
import sys
import sympy as sp

FAIL = []


def check(name, got, want):
    ok = got == want
    print(("  PASS  " if ok else "  FAIL  ") + name)
    if not ok:
        print("          got  %r\n          want %r" % (got, want))
        FAIL.append(name)


x, y = sp.symbols("x y")
t_form = x**5 * y - x * y**5                    # degree 6
Phi = x**8 + 14 * x**4 * y**4 + y**8            # degree 8
i = sp.I

# ---- generators of 2T = SL(2,3) inside SU(2) ------------------------------------------
g4 = sp.Matrix([[i, 0], [0, -i]])
g3 = sp.Rational(1, 2) * sp.Matrix([[1 + i, -1 + i], [1 + i, 1 - i]])


def act(f, M):
    X = M[0, 0] * x + M[0, 1] * y
    Y = M[1, 0] * x + M[1, 1] * y
    return sp.expand(sp.simplify(f.subs({x: X, y: Y}, simultaneous=True)))


def invariant(f):
    return all(sp.simplify(act(f, g) - f) == 0 for g in (g4, g3))


print("A  t and Phi are 2T-invariant")
check("t = x^5 y - x y^5 is invariant under both 2T generators", invariant(t_form), True)
check("Phi = x^8 + 14 x^4 y^4 + y^8 is invariant under both", invariant(Phi), True)
# CONTROL: a form of the right degree that is NOT invariant must be rejected, else the
# invariance test is passing everything.
check("CONTROL a non-invariant degree-8 form is rejected", invariant(x**8 + y**8), False)


print("\nB  degree matching leaves no freedom")


def degrees(gens, bound=40):
    """Degrees realisable as non-negative integer combinations of the generator degrees."""
    out = set()
    a_max = bound // gens[0] + 1
    for a in range(a_max + 1):
        for b in range(bound // gens[1] + 2):
            for c in range(bound // gens[2] + 2):
                d = a * gens[0] + b * gens[1] + c * gens[2]
                if 0 < d <= bound:
                    out.add(d)
    return out


E6_SUMMAND_DEGS = {2, 8, 10, 14, 16, 22}        # 2m for exponents 1,4,5,7,8,11
D_2T = degrees((6, 8, 12))                      # McKay partner of E6
check("2T invariant degrees omit 2 and 10", {2, 10} & D_2T, set())
check("D(2T) meets E6's summand degrees in exactly {8,14,16,22}",
      sorted(D_2T & E6_SUMMAND_DEGS), [8, 14, 16, 22])
check("the excluded degrees are exactly exponents 1 and 5",
      sorted(d // 2 for d in E6_SUMMAND_DEGS - D_2T), [1, 5])

# CONTROL: the other two binary polyhedral groups must NOT reproduce this intersection.
# If they did, the "McKay partner" framing would be doing no work.
D_2O = degrees((8, 12, 18))
D_2I = degrees((12, 20, 30))
check("CONTROL 2O (E7 partner) gives a different intersection",
      sorted(D_2O & E6_SUMMAND_DEGS) != [8, 14, 16, 22], True)
check("CONTROL 2I (E8 partner) gives a different intersection",
      sorted(D_2I & E6_SUMMAND_DEGS) != [8, 14, 16, 22], True)
print("            2O -> %s ;  2I -> %s"
      % (sorted(D_2O & E6_SUMMAND_DEGS), sorted(D_2I & E6_SUMMAND_DEGS)))


print("\nC  each matching degree is realised by a UNIQUE monomial")
mono = {}
for a in range(0, 6):
    for b in range(0, 6):
        for c in range(0, 6):
            d = 6 * a + 8 * b + 12 * c
            if d in (8, 14, 16, 22):
                mono.setdefault(d, []).append((a, b, c))
check("degree 8  is only Phi",      mono.get(8),  [(0, 1, 0)])
check("degree 14 is only t Phi",    mono.get(14), [(1, 1, 0)])
check("degree 16 is only Phi^2",    mono.get(16), [(0, 2, 0)])
check("degree 22 is only t Phi^2",  mono.get(22), [(1, 2, 0)])
check("the degree-12 generator never appears",
      {c for v in mono.values() for (_, _, c) in v}, {0})

print("\n%d/%d checks passed" % (13 - len(FAIL), 13))
sys.exit(1 if FAIL else 0)
