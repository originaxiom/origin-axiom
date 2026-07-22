"""QP-2 -- private states (prereg 6bbc78aa).

Double-method design: every claim backed by two independent computations.
A cross-validation failure HALTS the verdict — never silent wrong output.

Method A (self-contained): numpy Fox calculus on the Riley presentation.
Method B (imported):       B264's mpmath Fox calculus (80 dps, tol=1e-50).
Method C (imported, k=1):  B357's full boundary restriction (SnapPy presentation).

For boundary restriction, the K-functional gives a single scalar per block
(phi_mu = f_a[0]). This is cross-validated against B357 at k=1, and the
algebraic guarantee (first row of Sym(A)-I = 0) is verified per block.
All singular value spectra are printed so a human can audit every rank claim.

Nothing to CLAIMS. Gate 5-Q.
"""
import importlib.util
import math
import pathlib
import sys

import numpy as np

FRONTIER = pathlib.Path(__file__).resolve().parent.parent
HALT = False


def halt(msg):
    global HALT
    HALT = True
    print(f"\n  *** HALT: {msg} ***\n", file=sys.stderr)
    print(f"\n  *** HALT: {msg} ***")


# ======================================================================
# SETUP
# ======================================================================

T = (1 + 1j * math.sqrt(3)) / 2
A_mat = np.array([[1, 1], [0, 1]], dtype=complex)
B_mat = np.array([[1, 0], [T, 1]], dtype=complex)
BASE = {"a": A_mat, "b": B_mat,
        "A": np.linalg.inv(A_mat), "B": np.linalg.inv(B_mat)}
REL = "abABaBAbaB"


def _mul(poly, c0, c1):
    new = {}
    for yp, co in poly.items():
        new[yp] = new.get(yp, 0j) + co * c0
        new[yp + 1] = new.get(yp + 1, 0j) + co * c1
    return new


def symn(M, n):
    p, q, r, s = M[0, 0], M[0, 1], M[1, 0], M[1, 1]
    out = np.zeros((n + 1, n + 1), dtype=complex)
    for j in range(n + 1):
        poly = {0: 1.0 + 0j}
        for _ in range(n - j):
            poly = _mul(poly, p, q)
        for _ in range(j):
            poly = _mul(poly, r, s)
        for yp, co in poly.items():
            out[yp, j] = co
    return out.T


# ======================================================================
# METHOD A: numpy Fox calculus
# ======================================================================

def fox_block_numpy(k):
    n = 2 * k
    dim = n + 1
    S = {ch: symn(BASE[ch], n) for ch in "abAB"}
    seq = [(ch.lower(), 1 if ch.islower() else -1) for ch in REL]

    def fox(j):
        tot = np.zeros((dim, dim), dtype=complex)
        pre = np.eye(dim, dtype=complex)
        for g, s in seq:
            Mg = S[g] if s == 1 else S[g.upper()]
            if g == j:
                tot += pre if s == 1 else -(pre @ Mg)
            pre = pre @ Mg
        return tot

    fa, fb = fox("a"), fox("b")
    d1 = np.hstack([fa, fb])
    d0 = np.vstack([S["a"] - np.eye(dim, dtype=complex),
                    S["b"] - np.eye(dim, dtype=complex)])

    sv_d1 = sorted(np.linalg.svd(d1, compute_uv=False), reverse=True)
    sv_d0 = sorted(np.linalg.svd(d0, compute_uv=False), reverse=True)

    rank_d1 = sum(1 for s in sv_d1 if s > 1e-8)
    rank_d0 = sum(1 for s in sv_d0 if s > 1e-8)

    gap_d1 = (sv_d1[rank_d1 - 1] / max(sv_d1[rank_d1], 1e-300)
              if 0 < rank_d1 < len(sv_d1) else float('inf'))
    gap_d0 = (sv_d0[rank_d0 - 1] / max(sv_d0[rank_d0], 1e-300)
              if 0 < rank_d0 < len(sv_d0) else float('inf'))

    dim_Z1 = 2 * dim - rank_d1
    dim_B1 = rank_d0
    dim_H1 = dim_Z1 - dim_B1

    cocycle_norm = np.linalg.norm(d1 @ d0)

    _, s_vals, Vh = np.linalg.svd(d1, full_matrices=True)
    tol = max(s_vals) * 1e-10
    null_vecs = [Vh[i] for i in range(Vh.shape[0])
                 if (s_vals[i] if i < len(s_vals) else 0) < tol]

    # K(f_a, h) = f_a[dim-1] in the transposed convention:
    #   h = e_0 (fixed vector of S_a), K(v, e_0) = v[2k] via K_{i,0} = delta_{i,2k}
    phi_per_nv = [nv[dim - 1] for nv in null_vecs]
    best_idx = max(range(len(phi_per_nv)), key=lambda i: abs(phi_per_nv[i])) \
        if phi_per_nv else -1
    phi_mu = phi_per_nv[best_idx] if best_idx >= 0 else 0

    # Algebraic guarantee: last row of (S_a - I) = 0 (transposed convention)
    last_row_norm = np.linalg.norm((S["a"] - np.eye(dim, dtype=complex))[dim - 1, :])

    return dict(
        k=k, dim_H1=dim_H1,
        sv_d1=sv_d1, sv_d0=sv_d0,
        gap_d1=gap_d1, gap_d0=gap_d0,
        cocycle_norm=cocycle_norm,
        phi_mu=phi_mu,
        phi_all=[complex(p) for p in phi_per_nv],
        last_row_norm=last_row_norm,
        null_count=len(null_vecs),
    )


# ======================================================================
# METHOD B: B264 mpmath Fox calculus (imported)
# ======================================================================

def _load_b264():
    spec = importlib.util.spec_from_file_location(
        "b264", FRONTIER / "B264_e6_character_variety" / "e6_charvar_tangent.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ======================================================================
# METHOD C: B357 boundary restriction (imported)
# ======================================================================

def _load_b357():
    spec = importlib.util.spec_from_file_location(
        "b357", FRONTIER / "B357_e6_boundary_restriction" / "boundary_restriction.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


# ======================================================================
# MAIN COMPUTATION
# ======================================================================

print("=" * 80)
print("QP-2: PRIVATE STATES  (prereg 6bbc78aa)")
print("Double-method design — every claim cross-validated")
print("=" * 80)

# ---- Part 1: gates ----

print("\n" + "-" * 80)
print("PART 1 — setup gates")
print("-" * 80)

P = np.eye(2, dtype=complex)
for ch in REL:
    P = P @ BASE[ch]
rep_err = np.linalg.norm(P - np.eye(2))
print(f"  Riley relator ||P-I|| = {rep_err:.2e}  {'OK' if rep_err < 1e-12 else '*** FAIL ***'}")
if rep_err >= 1e-12:
    halt("Riley rep does not satisfy relator")

for nn in [2, 4, 6]:
    AB = A_mat @ B_mat
    err = np.linalg.norm(symn(A_mat, nn) @ symn(B_mat, nn) - symn(AB, nn))
    print(f"  Sym^{nn} homomorphism err = {err:.2e}  {'OK' if err < 1e-10 else '*** FAIL ***'}")
    if err >= 1e-10:
        halt(f"Sym^{nn} is not a homomorphism")

# ---- Part 2: dim H^1 — TWO METHODS ----

print("\n" + "-" * 80)
print("PART 2 — dim H^1(Sym^{2k}): method A (numpy) vs method B (B264 mpmath)")
print("-" * 80)

b264 = _load_b264()
blocks = {}

for k in range(1, 4):
    r = fox_block_numpy(k)
    blocks[k] = r

    h1_b264 = b264.H1_sym(k)
    match = (r["dim_H1"] == h1_b264)

    print(f"\n  Sym^{2*k}:")
    print(f"    dim H^1 = {r['dim_H1']} (numpy)  /  {h1_b264} (B264)")
    print(f"    cross-check: {'PASS' if match else '*** FAIL ***'}")
    print(f"    d1 singular values: {['%.4e' % s for s in r['sv_d1']]}")
    rank_d1 = sum(1 for s in r['sv_d1'] if s > 1e-8)
    print(f"    d1 rank = {rank_d1},  "
          f"gap = {r['gap_d1']:.2e}  "
          f"({'clean' if r['gap_d1'] > 1e4 else '*** NARROW ***'})")
    print(f"    d0 singular values: {['%.4e' % s for s in r['sv_d0']]}")
    print(f"    d0 gap = {r['gap_d0']:.2e}")
    print(f"    ||d1 @ d0|| = {r['cocycle_norm']:.2e}  (cocycle identity)")

    if not match:
        halt(f"dim H^1 cross-validation failed at k={k}: numpy={r['dim_H1']}, B264={h1_b264}")
    if r["dim_H1"] != 1:
        halt(f"dim H^1(Sym^{2*k}) = {r['dim_H1']} != 1 (Menal-Ferrer-Porti violated)")
    if r["gap_d1"] < 1e4:
        halt(f"d1 gap ratio {r['gap_d1']:.2e} < 10^4 at k={k}: rank claim unreliable")

# ---- Part 3: boundary restriction — K-functional ----

print("\n" + "-" * 80)
print("PART 3 — boundary restriction per block (K-functional)")
print("-" * 80)
print()
print("  In the transposed convention (S = Q^T): the fixed vector of S_a is e_0.")
print("  K(v, e_0) = v[2k] (last component), via the antidiagonal invariant pairing.")
print("  The last row of (S_a - I) is identically zero (upper-triangular unipotent).")
print("  So coboundaries have f_a[last] = 0. A cocycle with f_a[last] != 0")
print("  is NOT a coboundary => restriction rank >= 1.")

for k in range(1, 4):
    r = blocks[k]
    print(f"\n  Sym^{2*k}:")
    print(f"    ||last row of S_a - I|| = {r['last_row_norm']:.2e}  "
          f"({'zero as required' if r['last_row_norm'] < 1e-12 else '*** NOT ZERO ***'})")
    print(f"    null space dim = {r['null_count']}")
    print(f"    |f_a[last]| per null vector: {['%.8f' % abs(p) for p in r['phi_all']]}")
    print(f"    best phi_mu = {r['phi_mu']:.10f}  (|phi_mu| = {abs(r['phi_mu']):.10f})")
    detected = abs(r["phi_mu"]) > 1e-8
    print(f"    restriction detected: {detected}")

    if r["last_row_norm"] >= 1e-12:
        halt(f"last row of S_a - I is not zero at k={k}")
    if not detected:
        halt(f"K-functional is zero at k={k}: boundary restriction not detected")

# ---- Part 4: B357 cross-validation ----

print("\n" + "-" * 80)
print("PART 4 — B357 cross-validation (exponent m = 1, independent code + presentation)")
print("-" * 80)

b357_ok = False
try:
    b357 = _load_b357()
    r357 = b357.restriction(1)
    phi_mu_357 = complex(r357["phi_mu"])
    rank_357 = r357["rank"]
    resid_357 = float(r357["resid"])

    print(f"  B357 phi_mu = {phi_mu_357:.10f}  (|phi_mu| = {abs(phi_mu_357):.10f})")
    print(f"  B357 rank   = {rank_357}")
    print(f"  B357 resid  = {resid_357:.2e}")
    print(f"  numpy phi_mu = {blocks[1]['phi_mu']:.10f}  (|phi_mu| = {abs(blocks[1]['phi_mu']):.10f})")
    print()
    print(f"  Note: numeric values differ (Riley vs SnapPy presentation).")
    print(f"  The structural claim 'rank = 1' must agree in both.")

    both_detect = (rank_357 == 1) and (abs(blocks[1]["phi_mu"]) > 1e-8)
    print(f"  Both detect restriction: {both_detect}")
    b357_ok = both_detect
    if not both_detect:
        halt("B357 and numpy disagree on boundary restriction at k=1")
except Exception as e:
    print(f"  B357 import failed: {e}")
    print(f"  Cannot cross-validate boundary restriction.")
    print(f"  Proceeding with K-functional alone (reduced confidence).")

# ---- Part 5: fiber dimension table ----

print("\n" + "-" * 80)
print("PART 5 — fiber dimension per SL(n)")
print("-" * 80)

print()
print("  ad(sl(n)) decomposes under principal sl(2) as:")
print("  ad(sl(n)) = (+)_{k=1}^{n-1} Sym^{2k}")
print()

all_flat = True
for n in [2, 3, 4]:
    exps = list(range(1, n))
    dim_tot = sum(blocks[k]["dim_H1"] for k in exps)
    rank_tot = sum(1 for k in exps if abs(blocks[k]["phi_mu"]) > 1e-8)
    fd = dim_tot - rank_tot
    if fd > 0:
        all_flat = False
    print(f"  SL({n}):  exponents {exps}")
    print(f"    dim H^1(ad_{n}) = {' + '.join(str(blocks[k]['dim_H1']) for k in exps)} = {dim_tot}")
    print(f"    rank(r_{n})     = {rank_tot}")
    print(f"    fiber_dim({n})   = {dim_tot} - {rank_tot} = {fd}")
    if fd != 0:
        halt(f"fiber_dim({n}) = {fd} != 0")

# ---- Part 6: summary table ----

print("\n" + "-" * 80)
print("PART 6 — summary table")
print("-" * 80)
print()
print(f"  {'k':>4}  {'|phi_mu|':>12}  {'dim H^1':>8}  {'d1 gap':>10}")
for k in range(1, 4):
    r = blocks[k]
    print(f"  {k:>4}  {abs(r['phi_mu']):>12.8f}  {r['dim_H1']:>8}  {r['gap_d1']:>10.1e}")
print()
print(f"  {'n':>4}  {'dim H^1':>8}  {'rank(r)':>8}  {'fiber':>6}  {'verdict':>8}")
for n in [2, 3, 4]:
    exps = list(range(1, n))
    d = sum(blocks[k]["dim_H1"] for k in exps)
    rk = sum(1 for k in exps if abs(blocks[k]["phi_mu"]) > 1e-8)
    fd = d - rk
    print(f"  {n:>4}  {d:>8}  {rk:>8}  {fd:>6}  {'FLAT' if fd == 0 else 'GROWS':>8}")

# ---- Part 7: Q2 controls ----

print("\n" + "-" * 80)
print("PART 7 — Q2 controls")
print("-" * 80)

print("\n  --- Menal-Ferrer-Porti: dim H^1(Sym^{2k}) = 1 for k = 1..6 ---")
for k in range(1, 7):
    h1 = b264.H1_sym(k)
    tag = "PASS" if h1 == 1 else "*** FAIL ***"
    print(f"    Sym^{2*k:>2}: dim H^1 = {h1}  [{tag}]")
    if h1 != 1:
        halt(f"Menal-Ferrer-Porti fails at k={k}")

print("\n  --- Dehn-filling A-variety (cited from B71/B73/B83) ---")
print("    SL(n): L = (-1)^{n-1} M^n on principal component")
print("    1D variety -> 1D A-variety curve -> fiber_dim = 0")

print("\n  --- B357 Lagrangian certificate (cited) ---")
print("    rank(r) = 6/6 over all E6 exponents {1,4,5,7,8,11}")
print("    image = 6-dim = half of 12 -> Lagrangian (half-lives-half-dies)")

# ======================================================================
# VERDICT
# ======================================================================

print("\n" + "=" * 80)
print("VERDICT")
print("=" * 80)

if HALT:
    print("\n  *** VERDICT SUPPRESSED — cross-validation failure above ***")
    print("  Fix the failure before reading off a verdict.")
    sys.exit(1)

verdict = "GROWS" if not all_flat else "FLAT"
print(f"\n  {verdict}")
print()
print("  fiber_dim(2) = fiber_dim(3) = fiber_dim(4) = 0")
print("  Every deformation direction is visible from the cusp torus.")
print("  The object has NO private states at any rank.")
print()
print("  Verification chain:")
print("    (1) dim H^1: numpy and B264 mpmath agree on all 3 blocks  [double-method]")
print(f"    (2) K-functional: last row of S_a-I is zero (norms "
      f"{', '.join('%.0e' % blocks[k]['last_row_norm'] for k in [1,2,3])})")
print(f"    (3) phi_mu nonzero: |phi_mu| = "
      f"{', '.join('%.6f' % abs(blocks[k]['phi_mu']) for k in [1,2,3])}")
print(f"    (4) B357 cross-check at k=1: {'PASS' if b357_ok else 'SKIPPED'}")
print(f"    (5) d1 gap ratios: "
      f"{', '.join('%.1e' % blocks[k]['gap_d1'] for k in [1,2,3])}")
print(f"    (6) Menal-Ferrer-Porti: 6/6 pass (k=1..6, via B264)")
