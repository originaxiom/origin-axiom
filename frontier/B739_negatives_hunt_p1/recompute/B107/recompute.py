#!/usr/bin/env python3
"""B739 Stage-B recompute -- target B107 (physics-connection audit; the headline NEGATIVE).

THE BANKED KILL (Stage-A record): claim_killed = "the metallic tower spectrum is new physics
(operator anomalous dimensions / masses)"; killed as re-presented moduli-space monodromy
carrying the single scale log(phi). evidence_quote (B107 FINDINGS section B):
    { 1, -1, phi^2, phi^-2, phi^3, -phi, phi^-1, -phi^-3 }  ( k in {-3..3}, sign +-1 )

THE DISCRIMINATING FACT (identified): the 8 eigenvalues of the SL(3) Fibonacci (m=1) tower --
the Jacobian of the induced SL(3) trace map at the trivial fixed line -- are EXACTLY the set
above, i.e. every eigenvalue is +-phi^k: ONE geometric scale, fully determined by the SL(2)
seed M_1 = [[1,1],[1,0]] (eigenvalues phi, -1/phi). If true, the tower spectrum carries no
spectral number beyond the SL(2) dilatation -> the kill stands.

E19 (compute-not-cite): B107's probe.py section B CONSTRUCTS this multiset from the cited
B103 factorization  P J(m) P^-1 = (+)_d Sym^d(M_m)  and only then checks it is +-phi^k --
it never computes the spectrum from the tower object itself.  This script therefore:
  PART 1  derives the SL(3) trace map of phi_1: a -> ab, b -> a from FIRST PRINCIPLES:
          8 exact all-matrix polynomial identities (Cayley-Hamilton / adjugate algebra) in
          the 18 free entries of generic 3x3 matrices A, B, det factors explicit; the SL(3)
          specialization (det = 1) yields the polynomial map F1 on the 8 trace coordinates.
  PART 2  cross-checks F1 (and the m=2 map F2) on fixed integer SL(3,Z) matrix pairs (exact).
  PART 3  computes the 8x8 Jacobian J1 = dF1 at the trivial fixed point (all coords = 3),
          its characteristic polynomial, and its EXACT eigenvalues over Q(sqrt5); verifies
          the multiset equals the banked evidence_quote and that every eigenvalue is
          s*phi^k with s in {+-1}, k in {-3..3}  (the single-scale fact).
  PART 4  recomputes (not cites) the m=1, n=3 instance of the B103 catalog:
          char(J1) = char(Sym^0 M_1) * char(Sym^2 M_1) * char(Sym^3 M_1), and
          eig(M_1) = {phi, -1/phi}.
  PART 5  the mechanism / discrimination probe (both directions): the m=2 (silver) tower.
          J2's spectrum is +-lambda^k with lambda = 1+sqrt2 = the SL(2) dilatation of
          M_2 = [[2,1],[1,0]] -- a DIFFERENT single scale, in a different quadratic field.
          So the tower spectrum is a function of exactly ONE number, the SL(2) seed's
          dilatation: it contains no independent spectral content ("SL(2)-determined").

CONVENTIONS DECLARED (E1; implicit in the original arcs, re-derived here):
  * Lawton SL(3) coordinate dictionary (implicit in B103 probe.py's U/L/S maps; re-derived):
      x1=tr(A) x2=tr(B) x3=tr(AB) x4=tr(A^-1) x5=tr(B^-1) x6=tr(A^-1 B) x7=tr(A B^-1)
      x8=tr((AB)^-1);  adjugate form adj(X)=det(X)X^-1 makes every identity all-matrix.
  * Monodromy realized as the automorphism phi_m: a -> a^m b, b -> a (B107 section A),
    acting on a character point (A,B) by (A,B) -> (rho(a^m b), rho(a)) = (A^m B, A).
    Abelianization (column convention on H1 basis (a,b)): M_m = [[m,1],[1,0]] -- exactly
    B107's M_1 at m=1.  (B103's word composite ["U","S"] realizes a GL(2,Z)-conjugate
    automorphism; spectra agree; the direct map is used here and verified from raw matrices.)
  * Trivial fixed line/point: all 8 coordinates = 3 (traces of the trivial SL(3) rep),
    as declared in B103 ("Jacobian ... at the trivial fixed line (all traces = n)").
  * Jacobian convention J[i,j] = d(F_i)/d(x_j) at the fixed point.
  * phi = (1+sqrt5)/2; all eigenvalue comparisons are EXACT (sympy radicals, simplify == 0).
Deterministic: no wall-clock, no randomness, no network. sympy only.
"""
from __future__ import annotations

import sys

import sympy as sp

t = sp.symbols("t")
SQ5 = sp.sqrt(5)
PHI = (1 + SQ5) / 2
SQ2 = sp.sqrt(2)
LAM = 1 + SQ2  # silver mean = dilatation of M_2

FAILURES = []


def check(label, ok):
    print(f"    [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        FAILURES.append(label)
    return ok


# --------------------------------------------------------------------------------------
# The coordinate dictionary (adjugate form -- all-matrix; equals inverse traces at det=1)
# --------------------------------------------------------------------------------------
def coord(A, B):
    adjA, adjB = A.adjugate(), B.adjugate()
    return [A.trace(), B.trace(), (A * B).trace(),
            adjA.trace(), adjB.trace(),
            (adjA * B).trace(), (A * adjB).trace(), (adjB * adjA).trace()]


X = list(sp.symbols("x1:9"))
x1, x2, x3, x4, x5, x6, x7, x8 = X
dAs = sp.Symbol("dA")  # symbolic det(A) in the decorated (all-matrix) identities

# phi_1: a->ab, b->a  == (A,B) -> (AB, A).  Decorated (all-matrix) image formulas:
F1_dec = [x3, x1,
          x1 * x3 - x2 * x4 + x6,                 # tr(A^2 B)   [Cayley-Hamilton]
          x8, x4,
          dAs * x5,                               # tr(adj(AB) A)      = detA * tr(adjB)
          dAs * x2,                               # tr(AB adjA)        = detA * tr(B)
          x4 * x8 + dAs * (x7 - x1 * x5)]         # tr((adjA)^2 adjB)

# phi_2: a->a^2 b, b->a  == (A,B) -> (A^2 B, A).  Decorated image formulas:
F2_dec = [x1 * x3 - x2 * x4 + x6, x1,
          x1 * (x1 * x3 - x2 * x4 + x6) - x4 * x3 + dAs * x2,          # tr(A^3 B)
          x4 * x8 + dAs * (x7 - x1 * x5), x4,
          dAs * x8,                                                     # tr(adj(A^2B) A)
          dAs * x3,                                                     # tr(A^2B adjA)
          x4 * (x4 * x8 + dAs * (x7 - x1 * x5)) - dAs * x1 * x8 + dAs ** 2 * x5]

F1 = [sp.expand(e.subs(dAs, 1)) for e in F1_dec]   # the SL(3) trace map of phi_1
F2 = [sp.expand(e.subs(dAs, 1)) for e in F2_dec]   # the SL(3) trace map of phi_2


def main():
    print("=" * 88)
    print("B739 Stage-B recompute -- B107: the SL(3) metallic-tower single-scale spectrum")
    print("=" * 88)

    # ------------------------------------------------------------------ PART 1
    print("\nPART 1 -- first-principles derivation of the trace maps (exact, symbolic):")
    print("  generic 3x3 matrices A, B (18 free symbols); each image coordinate of")
    print("  (A,B) -> (A^m B, A) equals its decorated polynomial identically (det factors")
    print("  explicit); specializing det=1 gives the SL(3) trace map on (x1..x8).")
    A = sp.Matrix(3, 3, sp.symbols("a1:10"))
    B = sp.Matrix(3, 3, sp.symbols("b1:10"))
    dA = sp.expand(A.det())
    xs = coord(A, B)
    sub = dict(zip(X, xs)); sub[dAs] = dA

    img1 = coord(A * B, A)          # images under phi_1
    img2 = coord(A * A * B, A)      # images under phi_2
    for i in range(8):
        ok = sp.expand(img1[i] - F1_dec[i].subs(sub)) == 0
        check(f"phi_1 identity, coordinate x{i+1}' (all-matrix, 18 vars)", ok)
    for i in range(8):
        ok = sp.expand(img2[i] - F2_dec[i].subs(sub)) == 0
        check(f"phi_2 identity, coordinate x{i+1}' (all-matrix, 18 vars)", ok)
    print("  SL(3) trace map of phi_1 (det=1):")
    for i, e in enumerate(F1):
        print(f"    x{i+1}' = {e}")

    # ------------------------------------------------------------------ PART 2
    print("\nPART 2 -- exact integer cross-check on fixed SL(3,Z) pairs (no randomness):")
    L1 = sp.Matrix([[1, 0, 0], [2, 1, 0], [3, 4, 1]])
    U1 = sp.Matrix([[1, 5, 6], [0, 1, 7], [0, 0, 1]])
    L2 = sp.Matrix([[1, 0, 0], [1, 1, 0], [2, 3, 1]])
    U2 = sp.Matrix([[1, 2, 1], [0, 1, 4], [0, 0, 1]])
    pairs = [(L1 * U1, L2 * U2), (U1 * L2, U2 * L1), (L1 * U2 * L2, U1 * L1)]
    for idx, (A0, B0) in enumerate(pairs):
        assert A0.det() == 1 and B0.det() == 1
        v = dict(zip(X, coord(A0, B0)))
        ok1 = [sp.Integer(e.subs(v)) for e in F1] == coord(A0 * B0, A0)
        ok2 = [sp.Integer(e.subs(v)) for e in F2] == coord(A0 * A0 * B0, A0)
        check(f"pair {idx}: F1(coords) == coords(AB, A) exactly", ok1)
        check(f"pair {idx}: F2(coords) == coords(A^2B, A) exactly", ok2)

    # ------------------------------------------------------------------ PART 3
    print("\nPART 3 -- THE DISCRIMINATING FACT: spectrum of the m=1 (Fibonacci) Jacobian")
    triv = {v: 3 for v in X}
    J1 = sp.Matrix(8, 8, lambda i, j: sp.diff(F1[i], X[j]).subs(triv))
    print("  fixed point: F1(3,...,3) == (3,...,3):",
          all(sp.Integer(e.subs(triv)) == 3 for e in F1))
    print("  J1 (8x8, exact integers):")
    for r in range(8):
        print("    " + str(list(J1.row(r))))
    cp1 = J1.charpoly(t).as_expr()
    print("  char(J1) =", sp.expand(cp1))
    print("  factored :", sp.factor(cp1))
    roots1 = sp.roots(cp1, t)
    got1 = []
    for r, mlt in roots1.items():
        got1.extend([sp.radsimp(r)] * mlt)
    got1.sort(key=lambda e: float(sp.N(e, 30)))
    print("  exact eigenvalues (sorted):", got1)

    target1 = [1, -1, PHI ** 2, PHI ** -2, PHI ** 3, -PHI, PHI ** -1, -PHI ** -3]
    remaining = list(got1)
    matched = True
    for tv in target1:
        hit = next((r for r in remaining if sp.simplify(sp.radsimp(r - tv)) == 0), None)
        if hit is None:
            matched = False
            break
        remaining.remove(hit)
    check("eigenvalue multiset == banked {1,-1,phi^2,phi^-2,phi^3,-phi,phi^-1,-phi^-3}",
          matched and not remaining)

    def power_decomp(r, base, lo=-8, hi=8):
        for k in range(lo, hi + 1):
            for s in (1, -1):
                if sp.simplify(sp.radsimp(r - s * base ** k)) == 0:
                    return s, k
        return None

    decomp = [power_decomp(r, PHI) for r in got1]
    check("every eigenvalue is s*phi^k, s in {+1,-1}, k integer (SINGLE SCALE log phi)",
          all(d is not None for d in decomp))
    print("  (sign, k) table:")
    for r, d in zip(got1, decomp):
        print(f"    {str(r):>22}  =  {d[0]:+d} * phi^{d[1]}")
    ks = sorted(d[1] for d in decomp if d is not None)
    check("k-values are exactly [-3,-2,-1,0,0,1,2,3]", ks == [-3, -2, -1, 0, 0, 1, 2, 3])

    # ------------------------------------------------------------------ PART 4
    print("\nPART 4 -- the B103 catalog RECOMPUTED at m=1, n=3 (not cited):")

    def sym_pow(M, d):
        if d == 0:
            return sp.Matrix([[1]])
        u, v = sp.symbols("u v")
        a, b, c, e = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
        S = sp.zeros(d + 1, d + 1)
        for j in range(d + 1):
            poly = sp.expand((a * u + c * v) ** (d - j) * (b * u + e * v) ** j)
            for i in range(d + 1):
                S[i, j] = poly.coeff(u, d - i).coeff(v, i)
        return S

    M1 = sp.Matrix([[1, 1], [1, 0]])
    eigM1 = sorted(M1.eigenvals().keys(), key=lambda e: float(sp.N(e, 30)))
    print("  M_1 = [[1,1],[1,0]], eigenvalues:", [sp.radsimp(e) for e in eigM1])
    check("eig(M_1) == {phi, -1/phi} exactly",
          all(sp.simplify(sp.radsimp(a - b)) == 0
              for a, b in zip(eigM1, sorted([PHI, -1 / PHI], key=lambda e: float(sp.N(e, 30))))))
    cat1 = sp.expand(sp.prod([sym_pow(M1, d).charpoly(t).as_expr() for d in (0, 2, 3)]))
    print("  char(Sym^0 M1)*char(Sym^2 M1)*char(Sym^3 M1) =", cat1)
    check("char(J1) == char(Sym^0 M1)*char(Sym^2 M1)*char(Sym^3 M1) exactly",
          sp.expand(cp1 - cat1) == 0)

    # ------------------------------------------------------------------ PART 5
    print("\nPART 5 -- mechanism / discrimination probe: the m=2 (silver) tower:")
    J2 = sp.Matrix(8, 8, lambda i, j: sp.diff(F2[i], X[j]).subs(triv))
    print("  fixed point: F2(3,...,3) == (3,...,3):",
          all(sp.Integer(e.subs(triv)) == 3 for e in F2))
    cp2 = J2.charpoly(t).as_expr()
    print("  char(J2) factored:", sp.factor(cp2))
    roots2 = sp.roots(cp2, t)
    got2 = []
    for r, mlt in roots2.items():
        got2.extend([sp.radsimp(r)] * mlt)
    got2.sort(key=lambda e: float(sp.N(e, 30)))
    print("  exact eigenvalues (sorted):", got2)
    decomp2 = [power_decomp(r, LAM) for r in got2]
    check("every m=2 eigenvalue is s*lambda^k, lambda = 1+sqrt2 (SINGLE SCALE log lambda)",
          all(d is not None for d in decomp2))
    ks2 = sorted(d[1] for d in decomp2 if d is not None)
    check("m=2 k-values are exactly [-3,-2,-1,0,0,1,2,3]", ks2 == [-3, -2, -1, 0, 0, 1, 2, 3])
    M2 = sp.Matrix([[2, 1], [1, 0]])
    cat2 = sp.expand(sp.prod([sym_pow(M2, d).charpoly(t).as_expr() for d in (0, 2, 3)]))
    check("char(J2) == char(Sym^0 M2)*char(Sym^2 M2)*char(Sym^3 M2) exactly",
          sp.expand(cp2 - cat2) == 0)
    check("lambda is NOT +-phi^k for any |k|<=8 (the scale MOVES with the SL(2) seed)",
          power_decomp(LAM, PHI) is None)
    print("  minimal polynomials: phi:", sp.minimal_polynomial(PHI, t),
          " lambda:", sp.minimal_polynomial(LAM, t), " (different quadratic fields)")

    # ------------------------------------------------------------------ verdict
    print("\n" + "=" * 88)
    if FAILURES:
        print("RESULT: FAIL --", len(FAILURES), "check(s) failed:")
        for f in FAILURES:
            print("   -", f)
        return 1
    print("RESULT: ALL CHECKS PASS.")
    print("The discriminating fact RECOMPUTED from first principles (no reliance on the")
    print("banked B103 conjugation): the SL(3) Fibonacci tower Jacobian at the trivial")
    print("fixed point has exactly the 8 eigenvalues {1,-1,phi^2,phi^-2,phi^3,-phi,")
    print("phi^-1,-phi^-3} = {s*phi^k}: ONE geometric scale log phi.  The m=2 contrast")
    print("shows the single scale is the SL(2) seed's dilatation (1+sqrt2 there): the")
    print("tower spectrum is a function of exactly one SL(2)-determined number and")
    print("carries no independent spectral content.  The banked kill is upheld.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
