"""B87 (Task 3) -- the m=3 metallic curve genus: the sequence is 3, 1, NOT decreasing to 0; and a
refinement of V33's m=3 bound.

CONTEXT. The CC-web handoff asked for the m=3 spectral-curve genus ("the sequence is 3, 1, ?"), hoping
for a decreasing 3->1->0 ("gauge theories of decreasing rank"). This was ALREADY answered by V33 /
physics_probes/SPECTRAL_CURVE_GATE1: the spectral-curve genus is 3, 1, >=2 -- m=2 is a genus MINIMUM,
not part of a decreasing family; the "decreasing rank" reading is REFUTED (and this is the physics-
probe thread, closed). This stage reconfirms it exactly and REFINES the m=3 bound.

THE SPECTRAL CURVE (hyperelliptic double cover w^2 = disc_L(M) of the degree-2-in-L A-polynomial):
  * m=1 (figure-eight): genus 3 -- branch (M^2-M-1)(M^2-M+1)(M^2+M-1)(M^2+M+1) (golden + 6th-root factors).
  * m=2 (m136, silver): genus 1 -- branch (M^2-2M-1)(M^2+2M-1); j=1728, CM by Z[i] (forced + isolated, V34).

THE m=3 REFINEMENT (NEW). m=3 (R^3 L^3) is degree-2 in kappa (an irrational double cover). The
trace-relation curve F_3(x,kappa) is the double cover w^2 = disc3(x) with
   disc3 = 5x^4 - 10x^3 - x^2 + 6x + 1 = (x^2 - x - 1)(5x^2 - 5x - 1)   (squarefree, two quadratics).
A squarefree QUARTIC gives a genus-1 (elliptic) double cover -- so the m=3 TRACE-RELATION curve F_3 is
GENUS 1, NOT genus >=2. This REFINES V33/Gate1, which argued "irrational -> genus >= 2" -- but an
irrational squarefree quartic is genus 1, not >=2 (the "irrational" argument was too loose). Notably the
GOLDEN factor (x^2-x-1) appears in disc3, shared with m=1's branch locus.

HONEST SCOPE. The SPECTRAL curve (M,L) genus for m=3 -- the analogue of the m=1,2 spectral genus 3,1 --
needs the full m=3 (M,L) A-polynomial, whose elimination B69 flagged as "too slow"; it is a cover of the
genus-1 base F_3, so its genus is >= the base ramification contributes (open, computer-assisted-pending).
What is SETTLED: the genus sequence does NOT decrease to 0 (m=1 genus 3, m=2 genus 1 is a MINIMUM); the
m=3 trace-relation curve is genus 1 (refining the loose >=2). Standalone low-dim topology / number
theory; no physics claim (the physics reading is closed); proven core P1-P16 untouched.
"""
from __future__ import annotations

import sympy as sp

M, L, x = sp.symbols("M L x")


def _sqfree(expr, var):
    return sp.prod([f for f, e in sp.factor_list(sp.expand(expr))[1] if e % 2 == 1])


def hyperelliptic_genus(branch, var):
    """genus of w^2 = (squarefree part of branch in var): floor((deg sqfree - 1)/2). Returns (g, sqfree)."""
    sq = _sqfree(branch, var)
    d = sp.degree(sp.Poly(sp.expand(sq), var))
    return (d - 1) // 2, sp.factor(sq)


def spectral_genus_from_apoly(A):
    """genus of the spectral curve w^2 = disc_L(A) of a degree-2-in-L A-polynomial A(M,L)."""
    a, b, c = sp.Poly(A, L).all_coeffs()
    return hyperelliptic_genus(b**2 - 4 * a * c, M)


# exact A-polynomials (B67 figure-eight; B69/V32 m136)
APOLY = {
    1: M**4 * L**2 + (-M**8 + M**6 + 2 * M**4 + M**2 - 1) * L + M**4,
    2: M**2 * L**2 - (M**4 - 4 * M**2 + 1) * L + M**2,
}
DISC3 = 5 * x**4 - 10 * x**3 - x**2 + 6 * x + 1   # m=3 trace-relation discriminant (CS_INVARIANT_FAMILY)


def main():
    print("B87 (Task 3) -- the m=3 metallic curve genus\n")
    print("Spectral-curve genus (w^2 = disc_L(M), degree-2-in-L A-polynomial):")
    for m in (1, 2):
        g, sq = spectral_genus_from_apoly(APOLY[m])
        print(f"  m={m}: genus {g}   branch {sq}")
    print("\nm=3 trace-relation double cover F_3 = (w^2 = disc3), disc3 = 5x^4-10x^3-x^2+6x+1:")
    g3, sq3 = hyperelliptic_genus(DISC3, x)
    print(f"  disc3 factors = {sq3}  (squarefree quartic)")
    print(f"  => F_3 genus = {g3}  (ELLIPTIC) -- NOT >=2; refines V33's loose 'irrational -> >=2'.")
    print(f"  golden factor (x^2-x-1) present (shared with m=1's branch).")
    print("\nSEQUENCE: spectral genus m=1,2 = 3, 1 (a MINIMUM at m=2); the m=3 SPECTRAL (M,L) genus needs")
    print("  the 'too-slow' (M,L) elimination (open). SETTLED: the sequence does NOT decrease to 0 --")
    print("  the web's '3,1,0 decreasing gauge ranks' is REFUTED (V34); the m=3 trace-relation curve is")
    print("  genus 1. (Physics reading closed; this is curve geometry only.)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
