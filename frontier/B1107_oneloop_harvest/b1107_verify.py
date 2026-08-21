#!/usr/bin/env python3
"""B1107 -- independent verification bench for the audit seat's one-loop chain
(B8100 oneloop_geodesic -> B8104 pfaff_formula -> B8112 graviton_torsion_dictionary ->
B8113 abscissa_residue), run BEFORE that chain harvests to main.

Everything here is written fresh against the object's own data (SnapPy's m004) and the
Pfaff arXiv:1206.0228 definitions as independently read from the source. It does not import
or execute any of the audit seat's code. Three things are checked, matching the harvest
verification brief:

  1. THE ALGEBRAIC IDENTITY.  For the 1-dim rep sigma_k of M=SO(2) with highest weight k,
     R(k,sigma_k) at s=k collapses to prod_gamma (1-q_gamma^k), q_gamma=e^{-l_gamma+i theta_gamma}
     -- the Giombi-Maloney-Yin nome. Checked two ways: (a) direct substitution from Pfaff's own
     definitions (see NOTES), (b) numerically, by building sigma_k NOT as a typed-in phase but as
     the eigenvalue of an actual diagonalized SO(2) rotation matrix raised to the k-th power, on
     500 random synthetic (l,theta,k) triples AND on m004's own geodesic data.

  2. THE NUMBERS.  m004's complex length spectrum, fetched fresh via SnapPy
     (full_rigor=True, the library default), used to independently compute:
       a. log Z_geod at increasing cutoffs, via TWO structurally different summation orders
          (n-outer/gamma-product-inner vs gamma-outer/n-sum-inner), cross-checked against a
          50-digit mpmath recomputation to separate "true" mathematical agreement from float64
          roundoff.
       b. the n=2-term vs n>=3-tail cutoff-instability table at cutoffs 4.0/4.5/5.0 (+5.5 bonus).
       c. B8113's S(2), S(3) Dirichlet-type sums at cutoffs 4.0/4.5 (+5.0/5.5 extension).

  3. THE SCOPE FACTS.  (Read/quote-check only -- see b1107_NOTES.md for the primary-source
     verification against the actual Pfaff paper, fetched live from arXiv.)

Run from anywhere; writes b1107_results.json next to this file. No absolute machine paths are
used -- manifold names are SnapPy census identifiers ('m004'), not filesystem paths, and the
only file path used is this script's own directory.
"""
import cmath
import json
import math
import os
import random
import time

import mpmath as mp
import numpy as np
import snappy

HERE = os.path.dirname(os.path.abspath(__file__))
T_START = time.time()

FAILS = []


def gate(label, ok, detail=""):
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}" + (f"   {detail}" if detail else ""))
    if not ok:
        FAILS.append(label)


# ======================================================================================
# DATA: the object's own complex length spectrum, fetched fresh (not read from any B81xx file)
# ======================================================================================
print("=" * 84)
print("FETCHING m004's complex length spectrum fresh via SnapPy (full_rigor default = True)")
print("=" * 84)

MANIFOLD_NAME = "m004"
M = snappy.Manifold(MANIFOLD_NAME)
FAST_CUTOFFS = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0]
SLOW_CUTOFF = 5.5  # matches B8100/B8112's own headline cutoff; ~100s, budgeted for

SPECTRA = {}       # cutoff -> list[(complex_length, multiplicity)]
CLASS_COUNTS = {}  # cutoff -> (n_classes, n_geodesics_with_multiplicity)
TIMINGS = {}

for c in FAST_CUTOFFS + [SLOW_CUTOFF]:
    t0 = time.time()
    ls = M.length_spectrum(c)
    t1 = time.time()
    sp = [(complex(g.length), g.multiplicity) for g in ls]
    SPECTRA[c] = sp
    CLASS_COUNTS[c] = (len(sp), sum(m for _, m in sp))
    TIMINGS[c] = t1 - t0
    print(f"  cutoff {c:4}: {len(sp):4} classes, {sum(m for _, m in sp):5} geodesics(mult)"
          f"   [{t1-t0:6.2f}s]")

sys_ = min(L.real for L, _ in SPECTRA[2.0])
gate("systole reproduces the known 1.087070144995739", abs(sys_ - 1.087070144995739) < 1e-9,
     f"{sys_:.15f}")
gate("independent cross-check: '4_1' (B8100's manifold name) has the same volume as 'm004'",
     abs(snappy.Manifold("4_1").volume() - M.volume()) < 1e-9,
     f"vol={M.volume()}")


# ======================================================================================
# CLAIM 1 -- THE ALGEBRAIC IDENTITY
#   R(k, sigma_k) = prod_gamma (1 - q_gamma^k),  q_gamma = e^{-l_gamma + i*theta_gamma}
#
# Checked NOT by typing in e^{i k theta} and calling it done, but by constructing sigma_k from
# an actual 2x2 SO(2) rotation matrix, diagonalizing it over C, and raising the extracted
# weight-1 eigenvalue to the k-th power -- i.e. rebuilding the character from linear algebra.
# ======================================================================================
print()
print("=" * 84)
print("CLAIM 1 -- the algebraic identity (independent construction via matrix diagonalization)")
print("=" * 84)


def so2_matrix(theta):
    """The actual defining 2-dim real representation of M = SO(2) (Pfaff Sec.2: M = SO_2(R)),
    not a hand-written phase."""
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s], [s, c]], dtype=complex)


def sigma_k_from_matrix(theta, k):
    """sigma_k(m_gamma) built by diagonalizing the rotation matrix over C and taking the
    eigenvalue continuously connected to e^{+i theta}, raised to the k-th power. Since M is
    abelian, weight is additive under tensor power, so this reconstructs the weight-k character
    sigma_k without ever writing cmath.exp(1j*k*theta) directly."""
    w, _ = np.linalg.eig(so2_matrix(theta))
    target = cmath.exp(1j * theta)
    w1 = min(w, key=lambda z: abs(z - target))
    return w1 ** k


def pfaff_factor_via_matrix(l, theta, k):
    """det(Id_1 - sigma_k(m_gamma) e^{-k*l(gamma)}) for the 1-dim rep sigma_k -- literally
    Pfaff's (3.4) factor with s set to k, det of a 1x1 matrix is just the scalar."""
    return 1 - sigma_k_from_matrix(theta, k) * cmath.exp(-k * l)


random.seed(20260821)
max_err_synth = 0.0
for _ in range(500):
    l = random.uniform(0.05, 6.0)
    theta = random.uniform(-math.pi, math.pi)
    k = random.randint(2, 12)
    lhs = pfaff_factor_via_matrix(l, theta, k)
    q = cmath.exp(-l + 1j * theta)
    rhs = 1 - q ** k
    max_err_synth = max(max_err_synth, abs(lhs - rhs))
gate("R(k,sigma_k) factor (matrix-built) == 1-q^k (GMY factor), 500 random (l,theta,k)",
     max_err_synth < 1e-9, f"max|lhs-rhs|={max_err_synth:.3e}")

max_err_real = 0.0
for L, _mult in SPECTRA[3.5]:
    for n in range(2, 9):
        lhs = pfaff_factor_via_matrix(L.real, L.imag, n)
        q = cmath.exp(-L.real + 1j * L.imag)
        rhs = 1 - q ** n
        max_err_real = max(max_err_real, abs(lhs - rhs))
gate("same identity on m004's own geodesic data (50 classes below l=3.5, n=2..8)",
     max_err_real < 1e-9, f"max|lhs-rhs|={max_err_real:.3e}")

CLAIM1 = {
    "identity_checked": "R(k,sigma_k) = prod_[gamma] prime (1 - q_gamma^k), q=e^{-l+i*theta}",
    "method": "sigma_k built from eigen-decomposition of an actual SO(2) rotation matrix, "
              "not from typing e^{i k theta} directly",
    "max_err_synthetic_500_trials": max_err_synth,
    "max_err_real_m004_data": max_err_real,
}


# ======================================================================================
# CLAIM 2a -- log Z_geod from scratch, two summation orders, mpmath cross-check
# ======================================================================================
print()
print("=" * 84)
print("CLAIM 2a -- log Z_geod, independently computed, two summation orders")
print("=" * 84)


def R_of_n(n, sp):
    """R(n, sigma_n) = prod_[gamma] prime (1-q_gamma^n)^multiplicity, complex arithmetic
    throughout (the 'n outer, gamma-product inner' route)."""
    tot = 1.0 + 0j
    for L, mult in sp:
        q = cmath.exp(-L.real + 1j * L.imag)
        tot *= (1 - q ** n) ** mult
    return tot


def logZ_n_outer(sp, nmax=400):
    """For each n: form the FULL complex product over all gamma first, THEN take -2*log|.|,
    THEN sum over n. log|prod z_i| computed from one big complex accumulator."""
    total = 0.0
    for n in range(2, nmax):
        total += -2.0 * math.log(abs(R_of_n(n, sp)))
    return total


def logZ_gamma_outer(sp, nmax=400):
    """For each gamma: sum -2*log|1-q^n| over n (real arithmetic) first, weight by multiplicity,
    THEN sum over gamma. Mathematically log|prod|=sum log|.| makes this equal to the n-outer
    route, but the FLOATING-POINT algorithm is entirely different (no big complex products)."""
    total = 0.0
    for L, mult in sp:
        q = cmath.exp(-L.real + 1j * L.imag)
        aq = abs(q)
        s = 0.0
        for n in range(2, nmax):
            s += -2.0 * math.log(abs(1 - q ** n))
            if aq ** n < 1e-17:
                break
        total += mult * s
    return total


logZ_by_cutoff = {}
for c in FAST_CUTOFFS + [SLOW_CUTOFF]:
    logZ_by_cutoff[c] = logZ_gamma_outer(SPECTRA[c])
    print(f"  cutoff {c:4}: log Z_geod = {logZ_by_cutoff[c]:.13f}")

a_top = logZ_n_outer(SPECTRA[SLOW_CUTOFF])
b_top = logZ_gamma_outer(SPECTRA[SLOW_CUTOFF])
gate(f"the two summation orders agree at cutoff {SLOW_CUTOFF} (float64)",
     abs(a_top - b_top) < 1e-12, f"n-outer={a_top:.15f}  gamma-outer={b_top:.15f}  "
     f"|diff|={abs(a_top-b_top):.3e}  (audit seat claimed 8.2e-14)")

BANKED_LOGZ = -0.2729771708384004
gate(f"reproduces the banked log Z_geod = {BANKED_LOGZ} at cutoff {SLOW_CUTOFF}",
     abs(b_top - BANKED_LOGZ) < 1e-9, f"mine={b_top:.15f}  |diff|={abs(b_top-BANKED_LOGZ):.3e}")

# mpmath 50-digit cross-check: is the float64 8e-14 order-dependence real math or pure roundoff?
print("\n  mpmath(dps=50) cross-check at cutoff", SLOW_CUTOFF, "(this is the slow part, ~15-25s)...")
mp.mp.dps = 50


def R_of_n_mp(n, sp):
    tot = mp.mpc(1, 0)
    for L, mult in sp:
        q = mp.e ** (mp.mpc(-L.real, L.imag))
        tot *= (1 - q ** n) ** mult
    return tot


def logZ_n_outer_mp(sp, nmax=400):
    total = mp.mpf(0)
    for n in range(2, nmax):
        total += -2 * mp.log(abs(R_of_n_mp(n, sp)))
    return total


def logZ_gamma_outer_mp(sp, nmax=400):
    total = mp.mpf(0)
    for L, mult in sp:
        q = mp.e ** (mp.mpc(-L.real, L.imag))
        aq = abs(q)
        s = mp.mpf(0)
        for n in range(2, nmax):
            s += -2 * mp.log(abs(1 - q ** n))
            if aq ** n < mp.mpf('1e-40'):
                break
        total += mult * s
    return total


t0 = time.time()
a_mp = logZ_n_outer_mp(SPECTRA[SLOW_CUTOFF])
b_mp = logZ_gamma_outer_mp(SPECTRA[SLOW_CUTOFF])
t1 = time.time()
mp_diff = abs(a_mp - b_mp)
gate("mpmath(50dps): the two orders agree to ~machine precision of mpmath itself",
     mp_diff < mp.mpf('1e-30'), f"|diff|={mp.nstr(mp_diff, 4)}   [{t1-t0:.1f}s]")
float_vs_mp = abs(float(b_mp) - b_top)
gate("float64 result agrees with the mpmath 'true' value to float64 precision",
     float_vs_mp < 1e-12, f"|float64 - mpmath| = {float_vs_mp:.3e} "
     "(expected ~1e-13, accumulated float64 roundoff over ~2800 geodesic terms)")

CLAIM2A = {
    "cutoffs": FAST_CUTOFFS + [SLOW_CUTOFF],
    "logZ_by_cutoff": logZ_by_cutoff,
    "top_cutoff": SLOW_CUTOFF,
    "logZ_n_outer_float64": a_top,
    "logZ_gamma_outer_float64": b_top,
    "order_agreement_float64": abs(a_top - b_top),
    "banked_value": BANKED_LOGZ,
    "agreement_with_banked": abs(b_top - BANKED_LOGZ),
    "mpmath_dps": 50,
    "logZ_n_outer_mpmath": mp.nstr(a_mp, 45),
    "logZ_gamma_outer_mpmath": mp.nstr(b_mp, 45),
    "order_agreement_mpmath": mp.nstr(mp_diff, 6),
    "float64_vs_mpmath": float_vs_mp,
}


# ======================================================================================
# CLAIM 2b -- cutoff-instability table: n=2 term vs n>=3 tail
# ======================================================================================
print()
print("=" * 84)
print("CLAIM 2b -- cutoff-instability table: the n=2 term vs the n>=3 tail")
print("=" * 84)

TABLE_CUTOFFS = [4.0, 4.5, 5.0, SLOW_CUTOFF]  # 5.5 is a bonus beyond the requested 4.0/4.5/5.0
rows_2b = []
for c in TABLE_CUTOFFS:
    sp = SPECTRA[c]
    t2 = -2.0 * math.log(abs(R_of_n(2, sp)))
    t3p = sum(-2.0 * math.log(abs(R_of_n(n, sp))) for n in range(3, 400))
    rows_2b.append((c, t2, t3p))
    print(f"  cutoff {c:4}: n=2 term {t2:+.9f}   n>=3 tail {t3p:+.9f}")

TARGET_2B = {4.0: (-0.346991558, 0.080909800), 4.5: (-0.354912150, 0.080817660),
             5.0: (-0.351949899, 0.080934784)}
ok_2b = True
for c, t2, t3p in rows_2b:
    if c in TARGET_2B:
        tt2, tt3 = TARGET_2B[c]
        ok = abs(t2 - tt2) < 5e-7 and abs(t3p - tt3) < 5e-7
        ok_2b &= ok
        print(f"    vs target @ {c}: n2 diff {abs(t2-tt2):.2e}, tail diff {abs(t3p-tt3):.2e}"
              f"  {'MATCH' if ok else 'DIFFERS'}")
gate("all three targeted cutoffs (4.0/4.5/5.0) reproduce within 5e-7", ok_2b)

d2 = [abs(rows_2b[i + 1][1] - rows_2b[i][1]) for i in range(len(rows_2b) - 1)]
d3 = [abs(rows_2b[i + 1][2] - rows_2b[i][2]) for i in range(len(rows_2b) - 1)]
ratio_last = d2[-1] / d3[-1]
gate("last-step (5.0->5.5) instability ratio ~202x reproduced",
     190 < ratio_last < 215, f"ratio={ratio_last:.1f}x  (n2 delta={d2[-1]:.3e}, tail delta={d3[-1]:.3e})")

CLAIM2B = {"cutoffs": TABLE_CUTOFFS,
           "n2_term": {str(c): t2 for c, t2, _ in rows_2b},
           "n3plus_tail": {str(c): t3p for c, _, t3p in rows_2b},
           "last_step_ratio_n2_over_tail": ratio_last,
           "reproduces_targets_4.0_4.5_5.0": ok_2b}


# ======================================================================================
# CLAIM 2c -- B8113's S(2), S(3) Dirichlet-type sums
# ======================================================================================
print()
print("=" * 84)
print("CLAIM 2c -- S(2)=sum e^{-2l}, S(3)=sum e^{-3l} (B8113's abscissa-residue check)")
print("=" * 84)

S_CUTOFFS = [4.0, 4.5, 5.0, SLOW_CUTOFF]
rows_2c = []
prev2 = prev3 = None
for c in S_CUTOFFS:
    sp = SPECTRA[c]
    s2 = sum(mult * math.exp(-2 * L.real) for L, mult in sp)
    s3 = sum(mult * math.exp(-3 * L.real) for L, mult in sp)
    d2s = None if prev2 is None else s2 - prev2
    d3s = None if prev3 is None else s3 - prev3
    rows_2c.append({"cutoff": c, "S2": s2, "S3": s3, "dS2": d2s, "dS3": d3s})
    d2p = "" if d2s is None else f"  step {d2s:+.6f}"
    d3p = "" if d3s is None else f"  step {d3s:+.8f}"
    print(f"  cutoff {c:4}: S2={s2:.6f}{d2p}   S3={s3:.6f}{d3p}")
    prev2, prev3 = s2, s3

TARGET_2C = {4.0: (0.746569, 0.133744), 4.5: (0.796785, 0.134429)}
ok_2c = True
for r in rows_2c:
    if r["cutoff"] in TARGET_2C:
        tS2, tS3 = TARGET_2C[r["cutoff"]]
        ok = abs(r["S2"] - tS2) < 1e-5 and abs(r["S3"] - tS3) < 1e-5
        ok_2c &= ok
gate("S(2)/S(3) reproduce B8113's table at cutoffs 4.0/4.5", ok_2c)

CLAIM2C = {"rows": rows_2c, "reproduces_targets_4.0_4.5": ok_2c,
           "extended_to": S_CUTOFFS[2:]}


# ======================================================================================
# ASSEMBLE + WRITE
# ======================================================================================
elapsed = time.time() - T_START
print()
print("=" * 84)
print(f"DONE in {elapsed:.1f}s total.  {'ALL CHECKS PASS' if not FAILS else 'FAILURES: ' + str(FAILS)}")
print("=" * 84)

RESULTS = {
    "manifold": MANIFOLD_NAME,
    "cross_checked_manifold_name": "4_1",
    "class_geodesic_counts_by_cutoff": {str(c): {"classes": CLASS_COUNTS[c][0],
                                                  "geodesics_with_multiplicity": CLASS_COUNTS[c][1]}
                                         for c in CLASS_COUNTS},
    "fetch_timings_seconds": {str(c): TIMINGS[c] for c in TIMINGS},
    "systole": sys_,
    "claim1_algebraic_identity": CLAIM1,
    "claim2a_logZ_geod": CLAIM2A,
    "claim2b_cutoff_instability_table": CLAIM2B,
    "claim2c_S2_S3_dirichlet_sums": CLAIM2C,
    "failures": FAILS,
    "total_runtime_seconds": elapsed,
}
with open(os.path.join(HERE, "b1107_results.json"), "w") as fh:
    json.dump(RESULTS, fh, indent=1, sort_keys=True, default=str)
print("b1107_results.json written")

if FAILS:
    raise SystemExit(f"FAILED: {FAILS}")
