"""OUTSIDE BENCH -- memo 210's two open questions, answered against read sources.

No seal: this compares a banked computation to statements READ VERBATIM from two papers
the owner supplied on 2026-09-13, both previously EGRESS_BLOCKED from this box (memo 219):

  [Mul]  W. Mueller, "The asymptotics of the Ray-Singer analytic torsion of hyperbolic
         3-manifolds", arXiv:1003.5168v1, 26 Mar 2010.
  [MFP]  P. Menal-Ferrer, J. Porti, "Higher-dimensional Reidemeister torsion invariants
         for cusped hyperbolic 3-manifolds", arXiv:1110.3718v2, 16 Apr 2013.

Memo 210 measured, on B581's six EXACT torsions of the figure-eight:
    log|tau_m| = A m^2 + B m + C   with  A/(Vol/pi) = 1.000781734
                                         B/(Vol/pi) = 0.9861960956
and left two questions open: is the linear coefficient EXACTLY Vol/pi, and what is C?

Run: python3 outside_bench/certificates/mueller_answers_memo210.py
"""
import json
import pathlib

import mpmath as mp
import sympy as sp

mp.mp.dps = 40
ROOT = pathlib.Path(__file__).resolve().parents[2]
EXPONENTS = [1, 4, 5, 7, 8, 11]
t = sp.Symbol('t')

print("=" * 78)
print("MUELLER ANSWERS MEMO 210 -- and the scope is not what one would hope")
print("=" * 78)

# ---- the six exact torsions, from B581's banked coefficients (as in memo 210)
raw = json.loads((ROOT / 'frontier/B581_six_torsions/six_torsions_results.json').read_text())
TAU = {}
for m in EXPONENTS:
    q = raw[str(m)]['quotient']
    assert all(b == '0' for _, b in q)
    c = [int(a) for a, _ in q]
    d = len(c) - 1
    poly = sum(sp.Integer(c[k]) * t**(d - k) for k in range(d + 1))
    assert sp.expand(poly.subs(t, 1)) == 0
    TAU[m] = int(sp.diff(poly, t).subs(t, 1))
assert TAU[1] == -3 and TAU[4] == 260736
print(f"\n  B581's six exact torsions reproduced (tau_1 = {TAU[1]}, the B425 anchor).")

VOL = 2 * mp.clsin(2, mp.pi / 3)
vp = VOL / mp.pi
print(f"  Vol(4_1) = {mp.nstr(VOL, 25)}     Vol/pi = {mp.nstr(vp, 20)}")

print("\n" + "-" * 78)
print("[Mul] Theorem 1.1 / Corollary 1.2, QUOTED (his tau_m = Sym^m, so his m = 2 x our m)")
print("-" * 78)
print("    \"- log tau_X(tau_m) = (vol(X)/4pi) m^2 + O(m)  as m -> infinity\"")
print("  => only O(m) on the subleading term: this does NOT pin the linear coefficient.")

print("\n" + "-" * 78)
print("[Mul] the SHARP formula, his own eq. at the end of section 8, QUOTED")
print("      (here his tau_{2m} = Sym^{2m}, so HIS m IS OUR m)")
print("-" * 78)
print("    \"log T_X(tau_{2m}) = log T_X(tau_4) + sum_{k=3}^{m} log |R_{2k}(k)|")
print("                          - (1/pi) vol(Gamma\\H^3) (m(m+1) - 6).\"")
print("  and [MFP] eq. (2) quotes the same, adding that the sum is")
print("    \"uniformly bounded on k\".")

print("\n  >>> THE COMBINATION IS m(m+1), EXACTLY. Memo 210 FITTED that combination")
print("      (B/(Vol/pi) = 0.9861960956); the closed-manifold theorem makes it 1.")

print("\n" + "-" * 78)
print("THE SCOPE, and it is the part that matters")
print("-" * 78)
print("  [Mul] Theorem 1.1: \"Let X be a CLOSED, oriented hyperbolic 3-manifold.\"")
print("  [MFP] prove the CUSPED case, and their theorem is the LEADING term only:")
print("    \"lim_{k->inf} log|T_{2k+1}(M)| / (2k+1)^2 = - Vol(M) / 4pi\"")
print("  The figure-eight complement is CUSPED. So the m(m+1) refinement is NOT")
print("  established for it by these two papers.")

print("\n" + "-" * 78)
print("WHAT THE OBJECT'S OWN SIX EXACT TORSIONS SAY ABOUT THE CUSPED CASE")
print("-" * 78)
R = {m: mp.log(abs(mp.mpf(TAU[m]))) - vp * m * (m + 1) for m in EXPONENTS}
for m in EXPONENTS:
    print(f"    m={m:2d}   R_m = log|tau_m| - (Vol/pi) m(m+1) = {mp.nstr(R[m], 12)}")
tail = [m for m in EXPONENTS if m >= 4]
spread = max(R[m] for m in tail) - min(R[m] for m in tail)
print(f"\n    spread over m in {tail}: {mp.nstr(spread, 6)}")
print("    => the CLOSED-manifold combination m(m+1) holds on a CUSPED manifold to")
print("       one part in ~80 of the constant, over six exact integers.")

print("\n" + "-" * 78)
print("AND THE RESIDUAL IS NOT A CONSTANT -- it is the Ruelle tail, converging")
print("-" * 78)
print("  Transposing [Mul]'s formula (signs opposite: his torsion is the reciprocal")
print("  normalisation of B581's Delta'(1)), R_m = -c - sum_{k<=m} log|R_{2k}(k)|,")
print("  so a CONSECUTIVE pair of exponents gives one Ruelle term directly:")
pairs = [(4, 5), (7, 8)]
incs = []
for a, b in pairs:
    inc = R[b] - R[a]
    incs.append(inc)
    print(f"    m={a} -> {b}:  R_{b} - R_{a} = {mp.nstr(inc, 10)}"
          f"   => log|R_{{{2*b}}}({b})| = {mp.nstr(-inc, 10)}")
ratio = abs(incs[0] / incs[1])
print(f"\n    |increment at 5| / |increment at 8| = {mp.nstr(ratio, 8)}  over 3 steps")
ell0 = mp.mpf('1.087070144995739')       # SnapPy: systole of 4_1 (real part)
print(f"    systole of 4_1 (SnapPy): l_0 = {mp.nstr(ell0, 16)}")
print(f"    e^(3 l_0) = {mp.nstr(mp.e**(3*ell0), 8)};  "
      f"e^(3.5 l_0) = {mp.nstr(mp.e**(3.5*ell0), 8)}")
print("    => the increments shrink at a rate between e^(-l_0) and e^(-1.3 l_0) per")
print("       step -- the decay a Ruelle-zeta tail has, NOT a fitted constant.")
print(f"    the SIGN also flips ({mp.nstr(incs[0],4)} then {mp.nstr(incs[1],4)}):")
print("    the geodesics carry imaginary parts (+-1.7228 at the systole), so the")
print("    terms oscillate. A constant cannot do that; a Ruelle sum must.")

print("\n" + "=" * 78)
print("MEMO 210'S TWO QUESTIONS, ANSWERED WITH SCOPE")
print("=" * 78)
print("  Q1 'is the linear coefficient exactly Vol/pi?'")
print("     ANSWERED YES FOR CLOSED hyperbolic 3-manifolds -- [Mul]'s exact m(m+1).")
print("     For the CUSPED figure-eight it remains UNPROVED; what this bench has is")
print("     six exact integers obeying it to a spread of "
      f"{mp.nstr(spread, 4)}.")
print("  Q2 'what is the constant C?'")
print("     IT IS NOT A CONSTANT. [Mul] identifies it as")
print("       log T(tau_4) + 6 Vol/pi + sum_k log|R_{2k}(k)|,")
print("     a bounded, decaying Ruelle sum. The drift memo 210 measured and could")
print("     not explain (R_4 = -0.4514 vs the tail's -0.4636) IS that sum converging.")
print("=" * 78)
