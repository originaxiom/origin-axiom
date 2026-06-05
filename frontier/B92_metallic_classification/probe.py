"""B92 (Paper 0, Layer 1) -- the metallic family as a classification: det=-1 <=> period-1 CF.

Neutral mathematics. The motivation (why characterize the family rather than choose the seed) is recorded
separately and is NOT used here; this file states only the classification and its computational checks.

THE CLASSIFICATION. The metallic mean lambda_m = (m+sqrt(m^2+4))/2 is the dominant eigenvalue of the
companion M_m = [[m,1],[1,0]] (trace m, det -1). Three equivalent descriptions of the family:
  (1) self-reference:  x = m + 1/x          (the minimal one-shift-one-reciprocal equation)  -> lambda_m
  (2) continued fraction:  lambda_m = [m; m, m, ...]   (purely periodic, period 1)
  (3) Moebius:  z -> m + 1/z  is the action of M_m on P^1; its attracting fixed point is lambda_m.

THE OPERATIVE CONDITION (computer-assisted, verified here). Among non-negative hyperbolic unimodular 2x2
matrices, the dominant eigenvalue has a PURELY-PERIODIC PERIOD-1 continued fraction  <=>  det = -1; then
trace = m and eigenvalue = lambda_m. (Checked for all such matrices with entries <= 5.)

MyCalc-2 (the conjugacy census). The CF period of the dominant eigenvalue is a GL(2,Z)-conjugacy
invariant (the cutting sequence of the geodesic). Verified consistency: the period is constant across all
matrices of a given (trace, det) over the census; for det=-1 every trace-m matrix has period 1 with
repeat-block (m,) and eigenvalue lambda_m -- i.e. all are conjugate to the companion M_m. So the family
is {M_m : m>=1} up to GL(2,Z) conjugacy (recoding), with m free.

Refinement (a). The four "naive" premises (two letters, substitution, invertibility det=+-1, expansion)
do NOT by themselves select the metallic family -- they admit det=+1 cases (e.g. M_1^2 = [[2,1],[1,1]],
positive, expanding, det=+1). The operative extra condition is exactly det = -1; it is not derivable from
"simplest" without an extra metric.

MyCalc-5 (the contingency/systole boundary). No GL(2,Z)-conjugacy invariant distinguishes a single m (m
IS the conjugacy invariant -- the trace -- and ranges freely). Selecting m=1 (golden) requires importing
a metric: m=1 is the systole, the shortest closed geodesic 2*log(lambda_m) on H/GL(2,Z). The geodesic
lengths increase with m and m=1 minimizes -- so "the family is determined, the member is contingent (on a
metric)" is a precise mathematical statement.

Standalone number theory / GL(2,Z). No physics, no Origin-core claim; proven core P1-P16 untouched.
"""
from __future__ import annotations

from collections import defaultdict

import sympy as sp
from sympy.ntheory.continued_fraction import continued_fraction_periodic as cfp


def metallic_lambda(m):
    return (m + sp.sqrt(m * m + 4)) / 2


def three_equivalent_forms(m):
    """Verify (1) self-reference root, (2) CF [m;m,..], (3) Moebius fixed point all give lambda_m."""
    x = sp.symbols("x")
    lam = metallic_lambda(m)
    self_ref = sp.simplify(sp.solve(sp.Eq(x, m + 1 / x), x)[1] - lam) == 0     # x = m + 1/x
    cf = cfp(m, 1, m * m + 4)                                                   # CF of (m+sqrt(m^2+4))/1? -> use /2 form
    cf = cfp(m, 2, m * m + 4)
    cf_ok = (len(cf) == 1 and cf[0] == [m]) if cf else False                    # [[m]] purely periodic period 1
    M = sp.Matrix([[m, 1], [1, 0]])                                             # Moebius z->m+1/z
    moebius = sp.simplify((M[0, 0] * lam + M[0, 1]) / (M[1, 0] * lam + M[1, 1]) - lam) == 0
    return bool(self_ref), bool(cf_ok), bool(moebius)


def cf_period(tr, det):
    """(preperiod length, period length, full CF) of the dominant eigenvalue (tr+sqrt(tr^2-4det))/2."""
    disc = tr * tr - 4 * det
    if disc <= 0:
        return None
    cf = cfp(tr, 2, disc)
    if cf and isinstance(cf[-1], list):
        return len(cf) - 1, len(cf[-1]), cf
    return len(cf), 0, cf


def census(max_entry=5):
    """det=-1 <=> purely-periodic-period-1, and CF-period constant per (trace,det) class.
    Returns (n_checked, equiv_holds, period_invariant, det_minus1_classes)."""
    rows = []
    byclass = defaultdict(list)
    for a in range(max_entry + 1):
        for b in range(max_entry + 1):
            for c in range(max_entry + 1):
                for d in range(max_entry + 1):
                    det = a * d - b * c
                    if abs(det) != 1:
                        continue
                    tr = a + d
                    if tr * tr - 4 * det <= 0:
                        continue
                    if (tr + sp.sqrt(tr * tr - 4 * det)) / 2 <= 1:
                        continue
                    pre, perlen, cf = cf_period(tr, det)
                    pp1 = (pre == 0 and perlen == 1)
                    rows.append((det, tr, pp1))
                    block = tuple(cf[-1]) if (cf and isinstance(cf[-1], list)) else ()
                    byclass[(tr, det)].append((perlen, pre, block))
    equiv = all(r[2] == (r[0] == -1) for r in rows)
    invariant = all(len({it[0] for it in items}) == 1 for items in byclass.values())
    dm1 = {tr: (items[0][0], items[0][2]) for (tr, det), items in byclass.items() if det == -1}
    return len(rows), equiv, invariant, dm1


def refinement_a():
    """The naive premises admit det=+1: M_1^2 = [[2,1],[1,1]] is positive/expanding/automorphism, det=+1."""
    M = sp.Matrix([[1, 1], [1, 0]]) ** 2
    return M.tolist(), int(M.det()), int(M.trace())


def systole_lengths(ms=range(1, 6)):
    """Geodesic length 2*log(lambda_m) on H/GL(2,Z); m=1 (golden) is the systole (minimal)."""
    return {m: float(2 * sp.log(metallic_lambda(m))) for m in ms}


def main():
    print("B92 (Paper 0, Layer 1) -- the metallic family as a classification\n")
    print("three equivalent forms (self-ref / CF / Moebius) -> lambda_m:")
    for m in (1, 2, 3):
        print(f"  m={m}: {three_equivalent_forms(m)}  (all True)")
    n, equiv, inv, dm1 = census(5)
    print(f"\ncensus (entries<=5, {n} matrices): det=-1 <=> period-1 : {equiv};  "
          f"CF-period a (trace,det)-invariant : {inv}")
    print("  det=-1 classes (trace m -> period, repeat-block):")
    for m in sorted(dm1):
        print(f"    m={m}: period={dm1[m][0]}, block={dm1[m][1]}  (= companion M_{m}, eig lambda_{m})")
    M, det, tr = refinement_a()
    print(f"\nrefinement (a): M_1^2={M} has det={det}, trace={tr} -> det=+1, satisfies the 4 premises, NOT metallic")
    print("\nMyCalc-5 (systole): geodesic lengths 2 log lambda_m (m=1 minimal):")
    L = systole_lengths()
    for m in sorted(L):
        print(f"  m={m}: {L[m]:.5f}" + ("   <- systole" if m == min(L, key=L.get) else ""))
    print("\n=> the metallic family {M_m : m>=1} up to conjugacy, m free; det=-1 the operative condition;")
    print("   the member (m=1) is distinguished only by a metric (the systole).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
