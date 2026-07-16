"""F1 — upgrade the uniform jump law (Q3 L3, verified only at float precision,
300/300 PASS) to EXACT integer certificates.

Machinery reused verbatim (read, not imported wholesale, to avoid re-running the
p1_milgram.py side effects / json overwrite):
  - gauss_exact(B, r) and cyc_reduce(...) from
    promotion_queue/p1_milgram/p1_milgram.py — class Gauss sum G_w(r) as an exact
    integer-coefficient polynomial mod Phi_N (sympy Poly over QQ), plus (N, absdet).
  - bucket construction (25 Weyl classes) via next_queue/n1_counting/n1_jeffrey_terms
    (n1_jeffrey_terms.weyl_group/hnf_column/C6/P_WORD), identical to both
    p1_milgram.py and proof_queue/q3_proofs/q3_lemmas.py so bucket indices line up.
  - elem_divisors(B) and vp(n, p) from proof_queue/q3_proofs/q3_lemmas.py — Smith
    normal form elementary divisors of A_w = Z^6 / B_w Z^6.

NEW in this script: |G_w(r)|^2 computed EXACTLY (not just abs() at float
precision). Conjugate = negate exponents mod N (zeta^e -> zeta^{N-e}); multiply
G * conjugate(G) as polynomials, reduce mod Phi_N; assert the remainder is a
degree-0 (or zero) polynomial with integer value. Compare against the
elementary-divisor certificate: |G_w(r)|^2 = prod over elementary divisors
d = p1^a1*p2^a2*... of prod_p p^(a_p + min(v_p(r), a_p)).

GATES:
 (1) r = 13 (generic, coprime to 2*3*5*7*11*19): |G|^2 must equal |det B_w|
     exactly for every class (a + min(v_p(13), a) = a + 0 = a for every prime).
 (2) The full 25 x 13 table must reproduce the Q3 L3 300/300 float verdicts,
     now as an EXACT statement: |G(r)|^2 / |G(13)|^2 = prod_p p^{min(v_p(r), a)}
     (an integer identity, no sqrt / no float).
 Plus: a 2-representative spot check on the 3 largest classes (buckets 0, 1, 2)
 at r = 16 and r = 25 — a second group element in the same conjugacy class must
 give the identical |G|^2 (class-function sanity, exact).
"""
import itertools
import json
import sys
import time
from fractions import Fraction

sys.path.insert(0, '<seat-workdir>/seat-work/next_queue/n1_counting')
import numpy as np
import sympy as sp
from sympy.matrices.normalforms import smith_normal_form

import n1_jeffrey_terms as J

OUTDIR = '<seat-workdir>/seat-work/finisher_queue/f1_jump'
PRIMES = (2, 3, 5, 7, 11, 19)
RS = list(range(13, 26))  # 13..25 inclusive

x = sp.symbols('x')

# ---------------------------------------------------------------------------
# bucket construction — identical to p1_milgram.py / q3_lemmas.py so indices
# line up with the banked FINDINGS (b0 sz6480 divs[7,35] ... b24 sz1 divs[]).
# ---------------------------------------------------------------------------
W, eps = J.weyl_group()
buckets = {}
for idx in range(len(W)):
    w = W[idx]
    winv = np.rint(np.linalg.inv(w)).astype(np.int64)
    B = J.P_WORD * np.eye(6, dtype=np.int64) - w - winv
    cp = tuple(np.rint(np.poly(w.astype(float))).astype(np.int64))
    spec = tuple(sorted(np.linalg.eigvals(B.astype(float)).real.round(6)))
    buckets.setdefault((cp, spec), []).append((idx, B, int(eps[idx])))
ordered = sorted(buckets.items(), key=lambda kv: -len(kv[1]))
assert len(ordered) == 25, f"expected 25 classes, got {len(ordered)}"


# ---------------------------------------------------------------------------
# gauss_exact / cyc_reduce — verbatim from p1_milgram.py
# ---------------------------------------------------------------------------
def cyc_reduce(vec_dict, N):
    """integer dict {exponent mod N: count} -> canonical coeff Poly mod Phi_N"""
    coeffs = [0] * N
    for e, c in vec_dict.items():
        coeffs[e % N] += c
    p = sp.Poly(list(reversed(coeffs)), x, domain='QQ')
    rem = p.rem(sp.Poly(sp.cyclotomic_poly(N, x), x))
    return rem


def gauss_exact(B, r):
    """G_w(r) as (Poly mod Phi_N, N, absdet): sum of zeta_{2b}^{-a} over cosets."""
    Bs = sp.Matrix(B.tolist())
    ad = abs(int(Bs.det()))
    M = sp.Matrix(J.C6.tolist()) * Bs.inv()
    H = J.hnf_column(B)
    diag = [int(H[i, i]) for i in range(6)]
    Mf = [[Fraction(M[i, j]) for j in range(6)] for i in range(6)]
    terms = {}
    dens = set()
    raw = []
    for xx in itertools.product(*[range(d) for d in diag]):
        q = Fraction(0)
        for i in range(6):
            if xx[i]:
                for jj in range(6):
                    if xx[jj]:
                        q += xx[i] * Mf[i][jj] * xx[jj]
        e = (r * q) % 2
        raw.append(e)
        dens.add(e.denominator)
    N = 2 * np.lcm.reduce([int(d) for d in dens]) if dens else 2
    N = int(N)
    for e in raw:
        expo = int(-(e * N // 2)) % N  # e^{-i pi e} = zeta_N^{-e*N/2}
        terms[expo] = terms.get(expo, 0) + 1
    return cyc_reduce(terms, N), N, ad


# ---------------------------------------------------------------------------
# elem_divisors / vp — verbatim from q3_lemmas.py
# ---------------------------------------------------------------------------
def elem_divisors(B):
    M = sp.Matrix(B.tolist())
    snf = smith_normal_form(M)
    return [abs(int(snf[i, i])) for i in range(6) if abs(int(snf[i, i])) != 1]


def vp(n, p):
    v = 0
    while n % p == 0:
        v += 1
        n //= p
    return v


# ---------------------------------------------------------------------------
# NEW: exact |G|^2 via conjugate-and-multiply mod Phi_N
# ---------------------------------------------------------------------------
def conjugate_mod(Gp, N):
    """zeta^e -> zeta^{N-e} (exponents mod N, NOT mod deg Phi_N), then reduce
    back to canonical form mod Phi_N."""
    d = {}
    for (e,), c in Gp.as_dict().items():
        ne = (N - e) % N
        d[ne] = d.get(ne, 0) + c
    return cyc_reduce(d, N)


def abs_sq_exact(Gp, N):
    """|G|^2 EXACTLY: G * conjugate(G) mod Phi_N must reduce to a rational
    constant (degree-0 remainder, integer value). Returns the integer."""
    Gconj = conjugate_mod(Gp, N)
    prod = Gp * Gconj
    PhiN = sp.Poly(sp.cyclotomic_poly(N, x), x)
    rem = prod.rem(PhiN)
    if rem.is_zero:
        return 0
    assert rem.degree() == 0, (
        f"|G|^2 reduction is NOT a rational constant: degree {rem.degree()} "
        f"remainder {rem.as_expr()} (N={N})")
    c = rem.all_coeffs()[0]
    cr = sp.nsimplify(c)
    assert cr.is_Integer or (cr.is_Rational and cr.q == 1), (
        f"|G|^2 is not an integer: {c} (N={N})")
    val = int(cr)
    assert val >= 0, f"|G|^2 came out negative: {val} (N={N})"
    return val


def predicted_g2(divs, r):
    """prod over elementary divisors d = p1^a1*p2^a2*... of
    prod_p p^(a_p + min(v_p(r), a_p))."""
    pred = 1
    for d in divs:
        for p in PRIMES:
            a = vp(d, p)
            if a:
                v = vp(r, p)
                pred *= p ** (a + min(v, a))
    return pred


# ---------------------------------------------------------------------------
# main computation: 25 classes x 13 r-values = 325 cells
# ---------------------------------------------------------------------------
def main():
    t_start = time.time()
    certs = {}
    tally = {"total": 0, "match": 0, "mismatches": []}
    gate1 = {"total": 0, "match": 0, "mismatches": []}
    gate2_ratio_checks = 0
    gate2_ratio_fail = []
    spot_checks = []

    print(f"25 classes, r in {RS[0]}..{RS[-1]} -> {len(RS)} rungs, "
          f"{25 * len(RS)} cells total", flush=True)

    for bi, (key, members) in enumerate(ordered):
        idx0, B0, sgn = members[0]
        divs = elem_divisors(B0)
        det = 1
        for d in divs:
            det *= d
        size = len(members)
        certs[str(bi)] = {"size": size, "sign": sgn, "divs": divs, "det": det,
                           "cells": {}}
        t_b0 = time.time()
        g2_at_13 = None
        for r in RS:
            Gp, N, ad = gauss_exact(B0, r)
            assert ad == det, (
                f"bucket {bi} r={r}: gauss_exact absdet {ad} != SNF det {det}")
            g2 = abs_sq_exact(Gp, N)
            pred = predicted_g2(divs, r)
            match = (g2 == pred)
            tally["total"] += 1
            if match:
                tally["match"] += 1
            else:
                tally["mismatches"].append((bi, r, g2, pred))
            if r == 13:
                gate1["total"] += 1
                g13_ok = (g2 == det)
                if g13_ok:
                    gate1["match"] += 1
                else:
                    gate1["mismatches"].append((bi, g2, det))
                g2_at_13 = g2
            else:
                # gate 2: exact squared-ratio statement vs r=13
                ratio_pred = 1
                for d in divs:
                    for p in PRIMES:
                        a = vp(d, p)
                        if a:
                            v = vp(r, p)
                            ratio_pred *= p ** min(v, a)
                gate2_ratio_checks += 1
                if g2_at_13 and g2 % g2_at_13 == 0:
                    ratio_obs = g2 // g2_at_13
                else:
                    ratio_obs = None
                if ratio_obs != ratio_pred:
                    gate2_ratio_fail.append((bi, r, ratio_obs, ratio_pred))
            certs[str(bi)]["cells"][str(r)] = {
                "G2": g2, "predicted": pred, "match": match}
        dt = time.time() - t_b0
        print(f"b{bi:2d} sz{size:5d} sgn{sgn:+d} det{det:5d} divs{divs} "
              f"13 rungs done in {dt:.2f}s  ({tally['match']}/{tally['total']} "
              f"cumulative)", flush=True)

    # 2-representative spot check on the 3 largest classes at r=16, 25
    print("\n--- 2-rep spot check (3 largest classes, r=16 and r=25) ---",
          flush=True)
    for bi in (0, 1, 2):
        key, members = ordered[bi]
        assert len(members) > 1, f"bucket {bi} has only one member"
        idx1, B1, sgn1 = members[1]
        for r in (16, 25):
            Gp0, N0, ad0 = gauss_exact(members[0][1], r)
            g2_0 = abs_sq_exact(Gp0, N0)
            Gp1, N1, ad1 = gauss_exact(B1, r)
            g2_1 = abs_sq_exact(Gp1, N1)
            ok = (g2_0 == g2_1) and (ad0 == ad1)
            spot_checks.append({"bucket": bi, "r": r, "rep0_G2": g2_0,
                                 "rep1_G2": g2_1, "match": ok})
            print(f"  bucket {bi} r={r}: rep0 |G|^2={g2_0}  rep1 |G|^2={g2_1}  "
                  f"match={ok}", flush=True)
            assert ok, f"spot check FAILED bucket {bi} r={r}: {g2_0} vs {g2_1}"

    total_time = time.time() - t_start
    print(f"\n=== TOTALS ===", flush=True)
    print(f"cell tally: {tally['match']}/{tally['total']} exact matches "
          f"(certificate == observed |G|^2)", flush=True)
    print(f"GATE 1 (r=13 generic, |G|^2 == |det B_w|): "
          f"{gate1['match']}/{gate1['total']}", flush=True)
    print(f"GATE 2 (exact squared jump ratio vs r=13, all r=14..25): "
          f"{gate2_ratio_checks - len(gate2_ratio_fail)}/{gate2_ratio_checks}",
          flush=True)
    print(f"spot checks (2-rep, 3 largest classes, r=16,25): "
          f"{sum(1 for s in spot_checks if s['match'])}/{len(spot_checks)}",
          flush=True)
    if tally["mismatches"]:
        print(f"MISMATCHES (cert): {tally['mismatches']}", flush=True)
    if gate1["mismatches"]:
        print(f"GATE1 MISMATCHES: {gate1['mismatches']}", flush=True)
    if gate2_ratio_fail:
        print(f"GATE2 MISMATCHES: {gate2_ratio_fail}", flush=True)
    print(f"total wall time: {total_time:.2f}s", flush=True)

    out = {
        "classes": certs,
        "gates": {
            "gate1_r13_equals_absdet": {
                "total": gate1["total"], "match": gate1["match"],
                "mismatches": gate1["mismatches"]},
            "gate2_exact_squared_jump_ratio": {
                "total": gate2_ratio_checks,
                "match": gate2_ratio_checks - len(gate2_ratio_fail),
                "mismatches": gate2_ratio_fail},
        },
        "cell_tally": {"total": tally["total"], "match": tally["match"],
                       "mismatches": tally["mismatches"]},
        "spot_checks": spot_checks,
        "total_wall_time_s": total_time,
    }
    with open(f"{OUTDIR}/f1_certificates.json", "w") as f:
        json.dump(out, f, indent=1)
    print("DONE — f1_certificates.json", flush=True)

    all_pass = (tally["match"] == tally["total"] == 325 and
                gate1["match"] == gate1["total"] and
                not gate2_ratio_fail and
                all(s["match"] for s in spot_checks))
    print(f"\nALL GATES PASS: {all_pass}", flush=True)
    return 0 if all_pass else 1


if __name__ == '__main__':
    sys.exit(main())
