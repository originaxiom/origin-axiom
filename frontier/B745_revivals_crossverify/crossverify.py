"""B745 -- independent cross-verify of B742's two revivals (B58, B225).

Prereg (SEALED, hash in ARTIFACT_HASHES.txt): per revival (1) the audit seat's
recompute.py was re-executed in THIS seat (check-lines byte-identical -- recorded
in FINDINGS); (2) this script holds the INDEPENDENT checks not present in the
audit seat's artifacts.  Independent = my own implementation touching different
banked ground truth (B65's exact J(m) json; B48's declared trace-map convention),
not a re-run of the audit seat's code.

B58 checks
  C1  charpoly(B65 exact J(1)) == char(A^-1)char(A)char(A^2)char(A^3)char(A^4)
      char(-A^2)(t-1)^2(t+1) with A = [[1,1],[1,0]] the Fibonacci matrix
      (det -1; the spectrum's +-phi^k pairs force this convention -- the cat map
      [[2,1],[1,1]] FAILS this identity, a useful negative control kept below).
  C2  the closure lemma: no root of any char(A^k), |k|<=12, nor +-1, is within
      1 of -phi^2 over the positive-root family (margin here 1.618... >= 1;
      monotone in |k| beyond the window).
  C3  the exact SL(3) anchor: MY OWN 8x8 Jacobian of the m=1 trace map built
      from B48's declared convention (x1..x8, CH recurrences), evaluated on the
      fixed line at c=3; charpoly == (t-1)(t+1)(t^2-3t+1)(t^2+t-1)(t^2-4t-1).

B225 checks
  C4  the vacuity theorem, empirically: 30 seeded random monic-in-z polynomials
      over Z[x] -- disc_z mod 2 is a SQUARE in F_2[x] every time (can the
      criterion ever fail?  No: Vandermonde mod 2 / Stickelberger).
  C5  the 11a3 control re-derived: y^2+y=x^3-x^2 has Weierstrass Delta = -11
      (odd => good reduction at 2) yet the branch-locus extraction reports 2
      (lc = 4).  False positive at 2 on a 2-good curve, independently.

Deterministic (seed 42), stdlib + sympy only, no network.  Gate 5: pure algebra.
"""
from __future__ import annotations

import json
import os
import random

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

t, m, x, z = sp.symbols("t m x z")
PHI = (1 + sp.sqrt(5)) / 2


def fib_char(k: int) -> sp.Expr:
    """Exact char poly of A^k for the Fibonacci matrix A=[[1,1],[1,0]] (det -1)."""
    A = sp.Matrix([[1, 1], [1, 0]])
    Ak = A**k if k >= 0 else A.inv() ** (-k)
    return sp.expand(t**2 - sp.trace(Ak) * t + Ak.det())


def check_c1() -> bool:
    data = json.load(open(os.path.join(ROOT, "frontier/B65_sl4_symbolic_jacobian/jacobian_m.json")))
    J = sp.Matrix(15, 15, lambda i, j: sp.sympify(data["J"][i][j]))
    J1 = J.subs(m, 1)
    A2 = sp.Matrix([[1, 1], [1, 0]]) ** 2
    target = (fib_char(-1) * fib_char(1) * fib_char(2) * fib_char(3) * fib_char(4)
              * sp.expand(t**2 + sp.trace(A2) * t + A2.det()) * (t - 1) ** 2 * (t + 1))
    ok = sp.expand(J1.charpoly(t).as_expr() - sp.expand(target)) == 0
    # negative control: the SAME identity with the cat map [[2,1],[1,1]] must FAIL
    M = sp.Matrix([[2, 1], [1, 1]])

    def cat_char(k: int) -> sp.Expr:
        Mk = M**k if k >= 0 else M.inv() ** (-k)
        return sp.expand(t**2 - sp.trace(Mk) * t + 1)

    wrong = (cat_char(-1) * cat_char(1) * cat_char(2) * cat_char(3) * cat_char(4)
             * sp.expand(t**2 + sp.trace(M**2) * t + 1) * (t - 1) ** 2 * (t + 1))
    control = sp.expand(J1.charpoly(t).as_expr() - sp.expand(wrong)) != 0
    print(f"[C1 ] charpoly(B65 exact J(1)) == Fibonacci 7-factor product: {ok}"
          f"   (cat-map control fails as it must: {control})")
    return bool(ok and control)


def check_c2() -> bool:
    cands = [PHI ** (2 * k) for k in range(-12, 13)] + [sp.Integer(1), sp.Integer(-1)]
    dist = min(abs(sp.N(c - (-PHI**2), 30)) for c in cands)
    ok = dist >= 1
    print(f"[C2 ] closure lemma: min dist(char(A^k) positive roots & +-1, -phi^2) = {dist} >= 1: {ok}")
    return bool(ok)


def check_c3() -> bool:
    xs = sp.symbols("x1:9")
    x1, x2, x3, x4, x5, x6, x7, x8 = xs
    # B48's declared m=1 (Fibonacci) trace map on the eight SL(3) coordinates
    F = (x3, x1, sp.expand(x1 * x3 - x4 * x2 + x6), x8, x4, x5, x2,
         sp.expand(x4 * x8 - x1 * x5 + x7))
    J = sp.Matrix(8, 8, lambda i, j: sp.diff(F[i], xs[j])).subs({v: 3 for v in xs})
    target = sp.expand((t - 1) * (t + 1) * (t**2 - 3 * t + 1) * (t**2 + t - 1) * (t**2 - 4 * t - 1))
    ok = sp.expand(J.charpoly(t).as_expr() - target) == 0
    print(f"[C3 ] my SL(3) fixed-line Jacobian (from B48 conventions, c=3) charpoly "
          f"== (t-1)(t+1)(t^2-3t+1)(t^2+t-1)(t^2-4t-1): {ok}")
    return bool(ok)


def is_square_f2(poly_expr: sp.Expr) -> bool:
    p = sp.Poly(poly_expr, x, modulus=2)
    if p.is_zero:
        return True
    return all(mult % 2 == 0 for _, mult in sp.factor_list(p.as_expr(), modulus=2)[1])


def check_c4() -> bool:
    rng = random.Random(42)
    n_tested = 0
    for _ in range(30):
        dz = rng.randint(2, 5)
        f = z**dz + sum(rng.randint(-9, 9) * x ** rng.randint(0, 4) * z**k for k in range(dz))
        D = sp.discriminant(sp.Poly(f, z), z)
        if D == 0 or sp.Poly(D, x).degree() <= 0:
            continue
        n_tested += 1
        if not is_square_f2(D):
            print(f"[C4 ] COUNTEREXAMPLE: {f}")
            return False
    print(f"[C4 ] disc_z mod 2 is a square in F_2[x] for all {n_tested} random monic-in-z inputs "
          f"(seed 42): True  -- the criterion can never fail (vacuous)")
    return n_tested >= 20


def check_c5() -> bool:
    # 11a3: y^2 + y = x^3 - x^2; Weierstrass Delta computed from scratch
    a1, a2b, a3, a4, a6 = 0, -1, 1, 0, 0
    b2 = a1**2 + 4 * a2b
    b4 = 2 * a4 + a1 * a3
    b6 = a3**2 + 4 * a6
    b8 = (a1**2) * a6 + 4 * a2b * a6 - a1 * a3 * a4 + a2b * a3**2 - a4**2
    delta = -b2**2 * b8 - 8 * b4**3 - 27 * b6**2 + 9 * b2 * b4 * b6
    good_at_2 = delta % 2 != 0
    Phi = z**2 + z - x**3 + x**2
    D = sp.expand(sp.discriminant(sp.Poly(Phi, z), z))
    lc = sp.LC(sp.Poly(D, x))
    fires = (lc % 2 == 0) or (not sp.Poly(D, x, modulus=2).is_squarefree)
    ok = good_at_2 and fires and delta == -11
    print(f"[C5 ] 11a3 control: Delta = {delta} (odd => good at 2), branch locus {D}, "
          f"lc = {lc} even => extraction reports 2 anyway: {ok}  <-- FALSE POSITIVE confirmed")
    return bool(ok)


def main() -> None:
    print("=" * 88)
    print("B745 -- independent cross-verify of the B742 revivals (banking seat)")
    print("=" * 88)
    results = [check_c1(), check_c2(), check_c3(), check_c4(), check_c5()]
    print("=" * 88)
    if all(results):
        print("ALL 5 INDEPENDENT CHECKS PASS -- verdict CONFIRMED x2 (B58, B225)")
    else:
        print(f"FAILURES: {[i + 1 for i, r in enumerate(results) if not r]}")
        raise SystemExit(1)


main()
