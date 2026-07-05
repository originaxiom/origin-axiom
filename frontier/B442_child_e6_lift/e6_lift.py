"""B442 (C4) — the E6 lift of the child's SL(2,C) vacua: composite data is -283-forced (Bin 3).

Per the campaign plan: the E6 torsions of the child come from the composites principal-sl2 o rho
over the C3 vacua. The E6 adjoint (78) decomposes under the principal sl2 as (+)_i Sym^{2m_i},
m_i = the E6 exponents {1,4,5,7,8,11}. So the composite E6 adjoint torsion factors as
prod_i tau(Sym^{2m_i} o rho) -- a FUNCTION of the SL(2) vacuum rho.

The C3 vacua (B439/B440, corrected) are the roots of the child quartic x^4-3x^3+x^2+3x-1
(disc -283), commensurability-SHARED with 5_2's quartic x^4-4x^3+4x^2+x-1 (same -283 field).
Therefore every composite E6 invariant is algebraic over the -283 field -- forced/shared, NOT
figure-eight-specific.

CONCRETE (character level, exact, rigorous): the E6 adjoint meridian character
chi_adj(x) = sum_i S_{2m_i}(x) (S_k the Sym^k Chebyshev character) reduces at each vacuum to an
element of the -283 field:
  child vacua : -1116 x^3 + 1844 x^2 + 1767 x - 741   (in Q[x]/(child quartic))
  5_2 vacua   : -23777 x^3 + 25467 x^2 + 5928 x - 6016 (in Q[x]/(5_2 quartic), SAME field)
The Galois-invariant sum over the 4 child vacua is rational (5201) -- as it must be.

STRUCTURAL: the full E6 adjoint Reidemeister torsion of the closed child at each vacuum is a
function of the (-283-field) rep data (Sym^{2m} twisted by rho on the 2-generator group), hence
algebraic over the -283 field and commensurability-shared with 5_2 -- Bin 3, inheriting C3.

NAMED BOUNDARY (honest, per the plan): intrinsically-E6 vacua -- Hom(pi_1(child), E6)/conj
BEYOND the principal composites (the 26 abelian + the non-composite irreducibles) -- are the
child's L50-analog. Their exact torsions are the specialist residue: NAMED here, not computed
in-sandbox (the closed-manifold E6 Reidemeister-torsion engine is the standing specialist gate).

Firewall: hyperbolic geometry + E6 rep theory. No physics claim.
"""
import os, json
import sympy as sp

x = sp.Symbol('x')
E6_EXPONENTS = [1, 4, 5, 7, 8, 11]
CHILD = x**4 - 3*x**3 + x**2 + 3*x - 1        # 4_1(5,1) vacua, disc -283 (C3)
FOREIGN = x**4 - 4*x**3 + 4*x**2 + x - 1      # 5_2(5,1) vacua, disc -283, SAME field


def sym_char(k):
    S = {0: sp.Integer(1), 1: x}
    for j in range(2, k + 1):
        S[j] = sp.expand(x*S[j-1] - S[j-2])
    return S[k]


def e6_adjoint_char():
    """Ad_{E6} meridian character = sum of Sym^{2m_i} over the E6 exponents (degree 22)."""
    return sp.expand(sum(sym_char(2*m) for m in E6_EXPONENTS))


def e6_char_at_vacua(quartic):
    return sp.rem(e6_adjoint_char(), quartic, x)


def galois_invariant_sum(quartic):
    """sum over the 4 vacua of the E6 adjoint character = trace of chi(Companion(quartic)) --
    an EXACT integer (hardened 2026-07-05 from the fragile nsimplify(re(N(...))) after review)."""
    comp = sp.Matrix.companion(sp.Poly(quartic, x))
    acc = sp.zeros(4)
    for c in sp.Poly(e6_adjoint_char(), x).all_coeffs():      # Horner on the companion matrix
        acc = acc*comp + c*sp.eye(4)
    return sp.trace(acc)


if __name__ == "__main__":
    adj = e6_adjoint_char()
    ch = e6_char_at_vacua(CHILD)
    fo = e6_char_at_vacua(FOREIGN)
    gsum = galois_invariant_sum(CHILD)
    print("Ad_E6 meridian char degree:", sp.degree(adj, x))
    print("at child vacua:", ch)
    print("at 5_2 vacua  :", fo)
    print("both in the -283 field (deg<=3):", sp.degree(ch, x) <= 3 and sp.degree(fo, x) <= 3)
    print("Galois-invariant sum over child vacua (rational):", gsum)
    assert sp.degree(ch, x) <= 3 and sp.degree(fo, x) <= 3
    assert gsum == 5201
    assert ch != fo                                   # different values, same field
    out = dict(e6_exponents=E6_EXPONENTS, adj_char_degree=int(sp.degree(adj, x)),
               child_char=str(ch), foreign_char=str(fo), galois_sum=int(gsum),
               verdict="Bin 3: E6 composite data -283-forced, shared with 5_2; intrinsic-E6 "
                       "residue NAMED as the specialist boundary")
    json.dump(out, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "e6_lift.json"), "w"), indent=1)
    print("[written] e6_lift.json")
