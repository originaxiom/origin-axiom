#!/usr/bin/env python3
"""WP-1.6: the sector beyond the bound at level 15, EXACTLY.

A two-dimensional module of the three-strand braid group in which the first generator has eigenvalues a and 1/a can be
written (Tuba and Wenzl's normal form)   L = [[a, a], [0, 1/a]],   R^-1 = [[1/a, 0], [-1/a, a]],   so  R = [[a, 0], [1/a, 1/a]].
Level 3's fundamental doublet has a = w (a cube root of unity); level 5's two doublets have a = z and a = z^2 (fifth
roots of unity).  With t a primitive fifteenth root of unity, w = t^5 and z = t^3, everything lies in Q(t), and
arithmetic there is polynomial arithmetic modulo the fifteenth cyclotomic polynomial.  COMPUTED, exactly:
  E1  the braid relation and S^2 = U^3 = -1 in each doublet (so each is an odd sector), and +1 in each join;
  E2  det(x - (L3 x L5 + R3 x R5)) for a = z:    (x^2 + x/phi + 2)^2 - 2 phi^2 x^2
      = x^4 + 2(phi - 1) x^3 + (4 - 3 phi) x^2 + 4(phi - 1) x + 4,  which factors over Q(sqrt5, sqrt2) as
      (x^2 + (1/phi + sqrt2 phi) x + 2)(x^2 + (1/phi - sqrt2 phi) x + 2).
      The first factor has two REAL roots, because (1/phi + sqrt2 phi)^2 > 8, which is phi > sqrt2; their product is 2.
      So the averaged move has the real eigenvalues -(s +- sqrt(s^2 - 8)) / 4 with s = 1/phi + sqrt2 phi, and the
      level's graph has the eigenvalue -s in this sector.
  E3  the same for a = z^2 is the conjugate polynomial under sqrt5 -> -sqrt5, whose two quadratic factors both have
      complex roots: every eigenvalue of the averaged move has modulus 1/sqrt2.
HOW IT COULD FAIL: the planted case uses a = z for level 3's doublet as well (not a cube root): the polynomial is then
another one.  Exact rational arithmetic (sympy); no floating point in E1 to E3."""
import json, pathlib
import sympy as sp
HERE = pathlib.Path(__file__).resolve().parent
t, x = sp.symbols("t x")
PHI15 = sp.Poly(sp.cyclotomic_poly(15, t), t)
red = lambda e: sp.Poly(sp.expand(e), t).rem(PHI15).as_expr()
def redm(M): return M.applyfunc(red)
def doublet(a, ainv):
    return sp.Matrix([[a, a], [0, ainv]]), sp.Matrix([[a, 0], [ainv, ainv]])
def kron(A, B): return sp.Matrix(4, 4, lambda i, j: A[i // 2, j // 2] * B[i % 2, j % 2])
CHECKS = []
def check(name, ok, detail=""):
    CHECKS.append({"check": name, "holds": bool(ok), "detail": str(detail)[:300]}); print("%s  %s%s" % ("ok  " if ok else "FAIL", name, ("  [%s]" % str(detail)[:260]) if detail else ""), flush=True)

w, wi = t ** 5, t ** 10; z, zi = t ** 3, t ** 12; z2, z2i = t ** 6, t ** 9
sqrt5 = red(z + zi - z2 - z2i); phi = (1 + sqrt5) / 2
check("sqrt5 = z + z^-1 - z^2 - z^-2 squares to 5 in Q(t)", red(sqrt5 ** 2 - 5) == 0)
def central(L, R):
    n = L.shape[0]; Ri = redm(R.inv()) if n == 2 else None
    return Ri
def facts(L, R, Ri):
    S = redm(L * Ri * L); U = redm(L * Ri)
    return redm(S * S), redm(U * U * U), redm(L * Ri * L - Ri * L * Ri)
ok = True; cs = {}
for name, (a, ai) in (("level 3", (w, wi)), ("level 5, a = z", (z, zi)), ("level 5, a = z^2", (z2, z2i))):
    L, R = doublet(a, ai); Ri = sp.Matrix([[ai, 0], [-ai, a]])
    assert redm(R * Ri) == sp.eye(2)
    S2, U3, braid = facts(L, R, Ri); cs[name] = S2
    ok &= (S2 == -sp.eye(2)) and (U3 == -sp.eye(2)) and (braid == sp.zeros(2, 2))
check("E1: in each of the three doublets the braid relation holds and S^2 = U^3 = -1", ok)
L3, R3 = doublet(w, wi); R3i = sp.Matrix([[wi, 0], [-wi, w]])
def join(a, ai):
    L5, R5 = doublet(a, ai); R5i = sp.Matrix([[ai, 0], [-ai, a]])
    L, R, Ri = kron(L3, L5), kron(R3, R5), kron(R3i, R5i)
    S2, U3, braid = facts(redm(L), redm(R), redm(Ri))
    poly = sp.Poly(sp.expand((x * sp.eye(4) - (L + R)).det(method="berkowitz")), x)
    return [red(c) for c in poly.all_coeffs()], S2 == sp.eye(4) and U3 == sp.eye(4) and braid == sp.zeros(4, 4)
def target(ph):                                                               # x^4 + 2(ph - 1)x^3 + (4 - 3 ph)x^2 + 4(ph - 1)x + 4
    return [sp.Integer(1), red(2 * (ph - 1)), red(4 - 3 * ph), red(4 * (ph - 1)), sp.Integer(4)]
c1, even1 = join(z, zi); c2, even2 = join(z2, z2i)
check("E1: each join satisfies the braid relation with S^2 = U^3 = +1 (an even sector)", even1 and even2)
check("E2: for a = z the characteristic polynomial of L3 x L5 + R3 x R5 is x^4 + 2(phi - 1)x^3 + (4 - 3 phi)x^2 + 4(phi - 1)x + 4, exactly",
      all(red(a - b) == 0 for a, b in zip(c1, target(phi))), [str(c) for c in c1][:3])
phic = (1 - sqrt5) / 2                                                        # the conjugate of phi
check("E3: for a = z^2 it is the conjugate under sqrt5 -> -sqrt5", all(red(a - b) == 0 for a, b in zip(c2, target(phic))))
# the factorisation over Q(sqrt5, sqrt2), with real radicals
P, r2 = (1 + sp.sqrt(5)) / 2, sp.sqrt(2)
quartic = x ** 4 + 2 * (P - 1) * x ** 3 + (4 - 3 * P) * x ** 2 + 4 * (P - 1) * x + 4
fact = (x ** 2 + (1 / P + r2 * P) * x + 2) * (x ** 2 + (1 / P - r2 * P) * x + 2)
check("E2: that quartic is (x^2 + (1/phi + sqrt2 phi) x + 2)(x^2 + (1/phi - sqrt2 phi) x + 2)", sp.simplify(sp.expand(quartic - fact)) == 0)
s_ = 1 / P + r2 * P
check("E2: the first factor has real roots: (1/phi + sqrt2 phi)^2 - 8 = phi + 2 sqrt2 - 4 > 0; the second has not: (1/phi - sqrt2 phi)^2 - 8 < 0",
      sp.simplify(s_ ** 2 - 8 - (P + 2 * r2 - 4)) == 0 and (P + 2 * r2 - 4) > 0 and sp.simplify((1 / P - r2 * P) ** 2 - 8) < 0, "phi + 2 sqrt2 - 4 = %s" % sp.N(P + 2 * r2 - 4, 12))
Pc = (1 - sp.sqrt(5)) / 2
check("E3: for the twin both factors have complex roots: (1/phi' +- sqrt2 phi')^2 < 8 with phi' = (1 - sqrt5)/2", sp.simplify((1 / Pc + r2 * Pc) ** 2 - 8) < 0 and sp.simplify((1 / Pc - r2 * Pc) ** 2 - 8) < 0)
rate = (s_ + sp.sqrt(s_ ** 2 - 8)) / 4
check("the rate of the sector: (s + sqrt(s^2 - 8)) / 4 with s = 1/phi + sqrt2 phi", abs(sp.N(rate, 30) - sp.Float("0.893614264", 30)) < sp.Float("1e-9"), "%s; s = %s" % (sp.N(rate, 20), sp.N(s_, 20)))
# planted
Lp, Rp = doublet(z, zi)
polyp = sp.Poly(sp.expand((x * sp.eye(4) - (kron(Lp, doublet(z, zi)[0]) + kron(Rp, doublet(z, zi)[1]))).det(method="berkowitz")), x)
check("planted: with a fifth root in place of the cube root the polynomial is another one", not all(red(a - b) == 0 for a, b in zip([red(c) for c in polyp.all_coeffs()], target(phi))))
json.dump({"checks": CHECKS, "failing": [c["check"] for c in CHECKS if not c["holds"]], "the rate": str(sp.N(rate, 30)), "s": str(sp.N(s_, 30))}, open(HERE / "the_join_at_15_exact.json", "w"), indent=1)
print("\n%d checks, %d failing" % (len(CHECKS), sum(1 for c in CHECKS if not c["holds"])))
