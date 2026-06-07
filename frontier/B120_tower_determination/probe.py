"""B120 -- the trivial-point tower as a fully-determined object: it depends only on (n; trace, det).

Banks the Chat-2 exploration interlude (Q2/Q3) + the computed Supplement (S1-S5), verify-don't-trust. Three of the
handoff's stated formulas were WRONG and are corrected here (S1 off-by-2; S5's guess + its 'no closed form' claim;
the Chat-2 theta/Sym 'n=3 divergence' was a units error). The surviving picture: the (n^2-1)-dim trivial-point
tower (the Sym two-sequence, B117/B103) is fixed by two inputs -- the unfolding depth n and the abelianization seed
(trace, det) -- and nothing else enters.

THE RESULTS (all re-derived + locked).
  Q3  tower char poly = f(n; trace, det). Distinct integer matrices with EQUAL (trace,det) give IDENTICAL towers
      (forced: tower = (+)Sym^d(M); Sym^d eigenvalues are degree-d monomials in M's eigenvalues, fixed by the char
      poly = (trace,det)). twist-count -> trace (the seed m), swap-count mod 2 -> det (the parity sector).
  S2  m-universality: the Sym CONTENT mu_d is m-INDEPENDENT -- it depends only on (n, det). Verified n=4, m=1,2,3
      (the char(+-M^k) MULTIPLICITIES coincide; only the eigenvalue VALUES phi_m change). = B103's Q[m]-iso at n=4.
      WHY (the dig): the tower is a GL(2,Z)-rep rho_n (B103); mu_d are its plethysm/branching multiplicities under
      the principal SL(2), which see only the abstract rep (n) and the parity (det), never the trace. HONEST SCOPE:
      this REFRAMES the prize as a plethysm and is proved only n=3,4 (same trace-ring wall) -- a reduction, NOT a
      closure.
  S1  the doubling range {2..n-3} is FORCED. The extra dims from doubling Sym^2..Sym^{n-3} EQUAL the dimension
      deficit |(n+1)(n+2)/2 - (n^2-1)| = (n-4)(n+1)/2, and {2..n-3} is the unique contiguous-from-Sym^2 fill. So the
      two-sequence's doubling band is DERIVED from B117's dimension identity. CORRECTION: the handoff's (n^2-3n)/2
      is off by 2; the correct value is (n-4)(n+1)/2.
  S3  count(n,0) = n-1 (the eigenvalue count at height 0 = #even-d Sym modules, mult-weighted).
  S5  the full height profile has a CLEAN closed form (heights run 0..n -- the top, Sym^n's extremes, is height n):
        count(n,0)=n-1;  count(n,h)=2(n-2) for h in {1,2};  2(n-h) for 3<=h<=n-1;  2 for h=n.
      sum over h = n^2-1. CORRECTION: the handoff's 2*max(1,n-h-1) is wrong, and a closed form DOES exist.
  Q2  degree=rank SPLITS: (I) SPECTRAL char(M^n) is a tower factor <=> mu_n=1, ALL n (Sym^n presence, B117);
      (II) GEOMETRIC longitude=meridian^n at an irreducible boundary-unipotent rep, n in {3,4} only (the forced
      principal a+1/a=3-n has root-of-unity order {4,3,2,inf}; n=5 the A^2=I edge -- B95/B119).
  S4  the B116 theta-split vs Sym comparison is at the FACTOR level (char(+-M^h) multiplicity); it agrees n<=5 and
      diverges at n=6. The Chat-2 'divergence at n=3' was an eigenvalue-vs-factor UNITS error, not a repo issue.

Standalone trace-map / Lie theory; NO physics; no CLAIMS.md promotion; the rho_n / Sym-mu_d proof stays the prize;
P1-P16 untouched.
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys

import numpy as np
import sympy as sp

_ROOT = pathlib.Path(__file__).resolve().parents[2]


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


_B103 = _load("b120_b103", "frontier/B103_tower_equivariance/probe.py")
_B95 = _load("b120_b95", "frontier/B95_degree_rank_mechanism/probe.py")
_B116 = _load("b120_b116", "frontier/B116_reconcile_theta_sym/probe.py")

_t, _m = sp.symbols("t m")


def _mu(n):
    return _B103.two_sequence_mult(n)


# --------------------------------------------------------------------------- #
# Q3 -- the tower is determined by (n; trace, det)
# --------------------------------------------------------------------------- #
def _tower_roots(M, n):
    """The multiset of tower eigenvalues = {Sym^d eigenvalues with mult mu_d}; a 2x2 M with eigenvalues a,b gives
    Sym^d eigenvalues a^{d-j} b^j (j=0..d)."""
    ev = np.linalg.eigvals(np.array(M.tolist(), dtype=complex))
    a, b = ev
    roots = []
    for d, mult in _mu(n).items():
        for j in range(d + 1):
            roots += [a ** (d - j) * b ** j] * mult
    return sorted(np.round(np.real(roots), 6).tolist())


def tower_determined_by_trace_det():
    """Q3: distinct integer matrices with EQUAL (trace,det) give IDENTICAL towers (n=3,4,5)."""
    M1 = sp.Matrix([[2, 1], [1, 0]])         # trace 2, det -1
    M2 = sp.Matrix([[1, 2], [1, 1]])         # trace 2, det 1-2 = -1, distinct
    same_invariants = (M1.trace() == M2.trace() and M1.det() == M2.det())
    distinct = (M1 != M2)
    eq = {n: bool(np.allclose(_tower_roots(M1, n), _tower_roots(M2, n))) for n in (3, 4, 5)}
    return {"M1_tr_det": (int(M1.trace()), int(M1.det())), "M2_tr_det": (int(M2.trace()), int(M2.det())),
            "same_invariants": bool(same_invariants), "distinct_matrices": bool(distinct),
            "towers_identical": eq, "all_identical": all(eq.values())}


# --------------------------------------------------------------------------- #
# S2 -- m-universality of the Sym content (the deep lead)
# --------------------------------------------------------------------------- #
def _lucas(k, mval):
    return int((sp.Matrix([[mval, 1], [1, 0]]) ** k).trace())


def _sym_content(mval):
    """The char(+-M^k) multiplicities of the n=4 tower (B103 Jacobian over Q[m]) at a given integer m."""
    Jm = _B103._Jm_n4_exact().subs(_m, mval)
    cp = Jm.charpoly(_t).as_expr()
    content = {}
    for fac, e in sp.factor_list(sp.expand(cp))[1]:
        P = sp.Poly(fac, _t)
        if P.degree() == 2:
            a2, a1, a0 = P.all_coeffs()
            b, c = sp.nsimplify(-a1 / a2), sp.nsimplify(a0 / a2)
            for k in range(1, 5):
                if sp.simplify(b - _lucas(k, mval)) == 0 and sp.simplify(c - (-1) ** k) == 0:
                    content[f"M^{k}"] = content.get(f"M^{k}", 0) + e
                if sp.simplify(b + _lucas(k, mval)) == 0 and sp.simplify(c - (-1) ** k) == 0:
                    content[f"-M^{k}"] = content.get(f"-M^{k}", 0) + e
    return dict(sorted(content.items()))


def m_universality_of_sym_content():
    """S2: the Sym content (char(+-M^k) multiplicities) of the n=4 tower is IDENTICAL for m=1,2,3 -- only the
    eigenvalue VALUES change. The module structure depends only on (n, det). REFRAMES the prize as a plethysm; a
    reduction, not a closure (proved only n=3,4, the same trace-ring wall)."""
    contents = {mval: _sym_content(mval) for mval in (1, 2, 3)}
    universal = all(contents[mv] == contents[1] for mv in (2, 3))
    return {"content_per_m": contents, "m_universal": universal,
            "why": "tower = GL(2,Z)-rep rho_n (B103); mu_d are plethysm/branching multiplicities of the principal "
                   "SL(2), trace-blind (only n + parity det enter).",
            "scope": "PROVED n=3,4 (B103 Q[m]-iso); reframes the prize as a plethysm; does NOT lower the trace-ring "
                     "wall (all-n m-universality is the same wall) -- a reduction, not a closure."}


# --------------------------------------------------------------------------- #
# S1 -- the doubling range is forced (corrected formula)
# --------------------------------------------------------------------------- #
def doubling_range_forced(nmax=10):
    """S1: the extra dims from doubling Sym^2..Sym^{n-3} EQUAL the dimension deficit (n-4)(n+1)/2 (n=4..nmax), so
    the contiguous-from-Sym^2 range {2..n-3} is the unique fill -> derives the two-sequence band. CORRECTION: the
    handoff's (n^2-3n)/2 is off by 2; the correct value is (n-4)(n+1)/2."""
    rows = []
    for n in range(4, nmax + 1):
        doubling_sum = sum(d + 1 for d in range(2, n - 3 + 1))     # extra dims from the doubled band
        deficit_mag = (n - 4) * (n + 1) // 2                        # |(n+1)(n+2)/2 - (n^2-1)|
        handoff_wrong = (n * n - 3 * n) // 2                        # the handoff's stated (n^2-3n)/2
        rows.append((n, doubling_sum, deficit_mag, handoff_wrong))
    offsets = {hw - dm for _, _, dm, hw in rows}                    # handoff - correct, should be constant 2
    return {"rows": rows,
            "doubling_equals_deficit": all(ds == dm for _, ds, dm, _ in rows),
            "correct_formula": "(n-4)(n+1)/2",
            "handoff_formula_off_by": offsets,                      # {2}: off by exactly 2 everywhere
            "handoff_formula_wrong": all(hw != dm for _, _, dm, hw in rows)}


# --------------------------------------------------------------------------- #
# S3 + S5 -- the height-count closed form (corrected)
# --------------------------------------------------------------------------- #
def _count(n, h):
    """Eigenvalue count at height h: h=0 -> #even-d Sym (mult-weighted); h>=1 -> 2*sum mu_d over d>=h, d==h mod 2."""
    if h == 0:
        return sum(v for d, v in _mu(n).items() if d % 2 == 0)
    return 2 * sum(v for d, v in _mu(n).items() if d >= h and (d - h) % 2 == 0)


def _count_closed_form(n, h):
    """The closed form: n-1 (h=0); 2(n-2) (h in {1,2}); 2(n-h) (3<=h<=n-1); 2 (h=n)."""
    if h == 0:
        return n - 1
    if h == n:
        return 2
    if h in (1, 2):
        return 2 * (n - 2)
    return 2 * (n - h)


def height_count_closed_form(nmax=8):
    """S3+S5: the full height profile (h=0..n) matches the closed form, and sums to n^2-1. CORRECTION: heights run
    0..n (the top h=n was missed); the handoff's 2*max(1,n-h-1) is wrong; a clean closed form DOES exist."""
    rows, cf_ok, sum_ok, guess_bad = [], True, True, []
    for n in range(2, nmax + 1):
        prof = [_count(n, h) for h in range(0, n + 1)]
        cf = [_count_closed_form(n, h) for h in range(0, n + 1)]
        rows.append((n, prof))
        if prof != cf:
            cf_ok = False
        if sum(prof) != n * n - 1:
            sum_ok = False
        for h in range(1, n + 1):                                  # the handoff's guess 2*max(1,n-h-1)
            if _count(n, h) != 2 * max(1, n - h - 1):
                guess_bad.append((n, h))
    return {"profiles": rows, "closed_form_matches": cf_ok, "sums_to_n2_minus_1": sum_ok,
            "count0_is_n_minus_1": all(_count(n, 0) == n - 1 for n in range(2, nmax + 1)),
            "handoff_guess_fails": len(guess_bad) > 0,
            "closed_form": "count(n,0)=n-1; 2(n-2) for h in {1,2}; 2(n-h) for 3<=h<=n-1; 2 for h=n"}


# --------------------------------------------------------------------------- #
# Q2 -- the degree=rank split (I spectral / II geometric)
# --------------------------------------------------------------------------- #
def degree_rank_split(nmax=8):
    """Q2: (I) SPECTRAL char(M^n) factor <=> mu_n=1, ALL n; (II) GEOMETRIC longitude=meridian^n at an irreducible
    boundary-unipotent rep, n in {3,4} (the forced principal a+1/a=3-n has order {4,3,2,inf})."""
    spectral = {n: _mu(n).get(n, 0) for n in range(2, nmax + 1)}
    geometric = {}
    for n in range(3, 7):
        _, is_rou, apa = _B95.forced_principal_spectrum(n)
        twocos = 3 - n                                              # a + 1/a = 2cos(theta) = 3-n
        order = (4 if twocos == 0 else 3 if twocos == -1 else 2 if twocos == -2 else None)
        geometric[n] = {"a_plus_ainv": apa, "root_of_unity": bool(is_rou), "order": order}
    return {"spectral_mu_n": spectral, "spectral_all_n": all(v == 1 for v in spectral.values()),
            "geometric_order": {n: geometric[n]["order"] for n in geometric},
            "geometric_n_in_3_4": (geometric[3]["order"] == 4 and geometric[4]["order"] == 3
                                   and geometric[5]["order"] == 2 and geometric[6]["order"] is None)}


# --------------------------------------------------------------------------- #
# S4 -- B116 is factor-level; the Chat-2 eigenvalue recount was the units error
# --------------------------------------------------------------------------- #
def b116_factor_level_confirm():
    """S4: B116's theta-split vs Sym comparison is at the FACTOR level (char multiplicity); it agrees n<=5 and
    diverges at n=6. The Chat-2 'divergence at n=3' was an eigenvalue-vs-factor UNITS error -- B116 stands."""
    agree = {n: _B116.differ_by_single_promotion(n) for n in (3, 4, 5)}
    div6 = not _B116.differ_by_single_promotion(6)
    return {"agree_through_n5": all(agree.values()), "diverges_at_n6": div6,
            "note": "factor-level (char(+-M^h) multiplicity); the Chat-2 'n=3 divergence' was eigenvalue-vs-factor "
                    "units, not a repo issue -- B116's n=6 divergence stands."}


def main():
    print("=" * 78)
    print("B120 -- the trivial-point tower is determined by (n; trace, det)")
    print("=" * 78)
    q3 = tower_determined_by_trace_det()
    print(f"\n[Q3] distinct same-(tr,det) matrices {q3['M1_tr_det']} vs {q3['M2_tr_det']}: towers identical "
          f"{q3['towers_identical']} -> all {q3['all_identical']}")
    s2 = m_universality_of_sym_content()
    print(f"\n[S2] Sym content m-universal (m=1,2,3): {s2['m_universal']}; content={s2['content_per_m'][1]}")
    print(f"     WHY: {s2['why']}")
    print(f"     SCOPE: {s2['scope']}")
    s1 = doubling_range_forced()
    print(f"\n[S1] doubling-sum == deficit (n-4)(n+1)/2 (n=4..10): {s1['doubling_equals_deficit']}; "
          f"handoff (n^2-3n)/2 wrong (off by {s1['handoff_formula_off_by']}): {s1['handoff_formula_wrong']}")  # off by {2}
    s35 = height_count_closed_form()
    print(f"\n[S3+S5] count(n,0)=n-1: {s35['count0_is_n_minus_1']}; closed form matches + sums to n^2-1: "
          f"{s35['closed_form_matches']} / {s35['sums_to_n2_minus_1']}; handoff guess fails: {s35['handoff_guess_fails']}")
    print(f"        closed form: {s35['closed_form']}")
    q2 = degree_rank_split()
    print(f"\n[Q2] (I) spectral mu_n=1 ALL n: {q2['spectral_all_n']}; (II) geometric order {q2['geometric_order']} "
          f"-> n in {{3,4}}: {q2['geometric_n_in_3_4']}")
    s4 = b116_factor_level_confirm()
    print(f"\n[S4] B116 factor-level: agree n<=5 {s4['agree_through_n5']}, diverge n=6 {s4['diverges_at_n6']} "
          f"(the Chat-2 'n=3 divergence' was a units error)")
    print("\nThe tower = ONE object fixed by (n ; trace, det). The prize is unchanged: prove the Sym two-sequence")
    print("mu_d for all n (B103). NO physics.")


if __name__ == "__main__":
    main()
