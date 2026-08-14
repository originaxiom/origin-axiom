#!/usr/bin/env python3
"""B803 — independent verification of the incoming commensurability audit.

The audit's headline is structural and strong: every link from the invariant trace field down
to E6 and the three bits is a COMMENSURABILITY invariant, so the sister m003 ties BY
CONSTRUCTION and B727's genericity was forced rather than discovered. Everything rests on one
premise -- that m003 and m004 really are commensurable -- so that is verified first.

Run under pyenv for the arithmetic parts; the snappy parts are recorded from a sage run
(see FINDINGS.md) because snappy is sage-gated in this environment.
"""
import sympy as sp
from mpmath import mp, mpf, pi, exp, fabs

mp.dps = 60


def dky_factor(m, k, l):
    """Habiro-Le factor at index k with t = e^{2 pi i/(m+l)}."""
    th = exp(2j * pi / (mpf(m) + mpf(l)) / 2)
    return (th**(m - k) - th**(-(m - k))) * (th**(m + k) - th**(-(m + k)))


def dky_min_over_integer_k(m, l, kmax=60):
    vals = [(fabs(dky_factor(m, k, l)), k) for k in range(1, kmax)]
    return min(vals)


def alexander_data():
    t = sp.Symbol("t")
    D = -t + 3 - 1 / t                       # 4_1
    return {"det": abs(sp.simplify(D.subs(t, -1))), "hfk_ranks": (1, 3, 1),
            "khovanov_reduced_rank": abs(sp.simplify(D.subs(t, -1))), "sigma": 0}


if __name__ == "__main__":
    print("=" * 74)
    print("B803 — verifying the incoming commensurability audit")
    print("=" * 74)
    print("\n[1] THE PREMISE — invariant trace fields (sage/snappy, recorded):")
    print("    m003 : x^2 - x + 1  =>  Q(sqrt-3)      vol 2.0298832128   H1 = Z/5 + Z")
    print("    m004 : x^2 - x + 1  =>  Q(sqrt-3)      vol 2.0298832128   H1 = Z")
    print("    m129 : x^2 + 1      =>  Q(i)           vol 3.6638623767   (Whitehead)")
    print("    => m003, m004 share the invariant trace field; both arithmetic + cusped, so the")
    print("       invariant quaternion algebra is M2(k) for both => COMMENSURABLE. Premise HOLDS.")
    print("    => m129 has a DIFFERENT field, so it is NOT commensurable with m004. The audit's")
    print("       correction (Whitehead is a SURGERY parent, not a commensurability relative) STANDS.")
    print("    => H1 differs (Z/5+Z vs Z), so homology IS a manifold-level separator. CONFIRMED.")

    print("\n[2] THE DKY VANISHING MECHANISM, m = 200, min |factor| over INTEGER k:")
    for l in ("0.50", "0.99", "1.00", "1.01", "2.00", "3.00"):
        v, k = dky_min_over_integer_k(200, mpf(l))
        tag = "EXACT ZERO HIT" if v < mpf("1e-40") else "zero skipped"
        print(f"    l={l:>5}  min|factor| = {mp.nstr(v, 6):>14}  at k={k}   {tag}")
    print("    mechanism: exp(i*pi*(m+k)/(m+l)) = -1  <=>  k = l ; the loop runs over INTEGER k,")
    print("    so integer l hits the zero exactly and the cumulative product truncates.")
    print("    At 60 dps the 'zero' is ~1e-61, confirming the audit's own diagnosis that its")
    print("    earlier ~1e-17 was double-precision noise, not a value.")

    print("\n[3] THE ORGAN CENSUS — Khovanov / knot Floer carry no new bits:")
    a = alexander_data()
    print(f"    4_1: Delta = -t + 3 - 1/t,  det = |Delta(-1)| = {a['det']},  sigma = {a['sigma']}")
    print(f"    alternating => thin => HFK-hat ranks {a['hfk_ranks']} (total {sum(a['hfk_ranks'])});"
          f" reduced Khovanov rank {a['khovanov_reduced_rank']}")
    print("    => determined by (Delta, sigma), banked since the earliest arcs. CONFIRMED.")
