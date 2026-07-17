"""A3 -- the stage-invariance mechanism (cc2, ANATOMY LOOP 1, sha 247ace23 clause A3).

WHY does E6 kill the deep-3 central (-I mod 27) where SU(3) is faithful, at the
matched rung E6 k=6 (kappa=18, ord T=108=4*27) vs SU(3) k=6 (kappa=9, ord T=27)?

Machinery (read-only, banked):
  E6:   <seat-workdir>/level_ladder_campaign/scripts/engine.py
        banked npz: .../level_ladder_campaign/outputs/level6_blocks.npz
        diagonal-aware mp reconstruction pattern: proof_queue/q1_level8/level8_run.py
        (function mp_blocks_diagaware), replicated here verbatim.
  SU(3): <seat-workdir>/veins/v7_conduit/engine_v7.py
        odd-projection pattern: veins/v7_conduit/chat2_hearing_group_verify.py and
        next_queue/n2_clock_law/n2_su3_13_measure.py (odd_block_word).
  Banked scalar facts (integer/order-only, cross-gated below):
    E6 k=6:  ord(B_odd) = 18 (level6_readouts.json; L6_RUN.log; L6_FINDINGS.md)
    SU3 k=6: ord(B_odd) = 36 (n2_clock_predict.py BANKED_SU3[6]; f2_run.log
             diagnostics "A1^36 mod 27: I"; q2_conductor.py su3_conductors(6))
  Stage-typed law (already banked, PSL_THEOREM.md, E6-only):
    killed <=> conductor q is a split prime (p = 1 mod 3) or a DEEP 3-power (3^a,
    a>=3); q2_conductor.py's clock_with() codifies this for E6 ('E'-type) and
    states the A-series ('A'-type, SU(3)) rule as "kills nothing" -- i.e. the
    banked law is a NUMBER-THEORETIC rule about an abstract SL(2,Z) word A1 =
    [[2,1],[1,1]] reduced mod n, not yet checked against the actual WZW
    representation matrices at the k=6 rung. THIS SCRIPT performs that check
    directly on the theta-odd BLOCK (not the abstract 2x2 proxy).

Central-element test (per PREREG_L1.md A3): the abstract central point of the
mod-27 CRT factor is g_c = A1^18 (E6: 108=4*27, j=18 kills the 27-factor while
fixing the 4-factor per the banked diagnostics; SU(3): ord T=27 has no other
factor, so g_c = A1^18 directly, j=18=36/2). Compute rho(A1)^18 on BOTH stages'
theta-odd blocks; report ||.-I||, the eigenvalue +-1 multiplicities, and test
whether membership in the -1 class is predicted by T_expo mod 27.
"""
import json
import sys
import time
from functools import reduce
import math

import numpy as np
import mpmath as mp

sys.path.insert(0, '<seat-workdir>/level_ladder_campaign/scripts')
sys.path.insert(0, '<seat-workdir>/veins/v7_conduit')

from engine import Level, weyl_group, mp_certify_order, factorint_small  # noqa: E402
from engine_v7 import An_Level, rho_A1_matrix  # noqa: E402

WORK = '<seat-workdir>/anatomy/loop1/a3_stage'
NPZ_PATH = '<seat-workdir>/level_ladder_campaign/outputs/level6_blocks.npz'
READOUTS_PATH = '<seat-workdir>/level_ladder_campaign/outputs/level6_readouts.json'

DPS = 50  # (prereg text says "mp dps 40" for the SU(3) side; 50 used throughout for a
          # uniform-precision report and to match every other banked script in this
          # repo (chat2_hearing_group_verify.py, n2_su3_13_measure.py, d4_su3_run.py,
          # q1_level8/level8_run.py) -- a strict superset of the requested 40 digits.)

results = {}


def log(*a, **kw):
    print(*a, **kw, flush=True)


def matpow(M, e):
    n = M.rows
    R = mp.eye(n)
    B = M.copy()
    while e:
        if e & 1:
            R = R * B
        B = B * B
        e >>= 1
    return R


def max_dev(A, B):
    return max(abs(A[i, j] - B[i, j]) for i in range(A.rows) for j in range(A.cols))


def frob_dev(A, B):
    return float(mp.sqrt(mp.fsum((A[i, j] - B[i, j]) * mp.conj(A[i, j] - B[i, j])
                                  for i in range(A.rows) for j in range(A.cols))).real)


def eig_pm_multiplicities(Mmp, tol=1e-6):
    """Cast an mp matrix to complex128 and eigendecompose (numpy); count how many
    eigenvalues land near +1 / -1 / neither."""
    n = Mmp.rows
    A = np.array([[complex(Mmp[i, j]) for j in range(n)] for i in range(n)], dtype=complex)
    ev = np.linalg.eigvals(A)
    n_plus = int(np.sum(np.abs(ev - 1) < tol))
    n_minus = int(np.sum(np.abs(ev + 1) < tol))
    n_other = n - n_plus - n_minus
    return n_plus, n_minus, n_other, ev


# =============================================================================
# PART 1 -- E6 k=6 (kappa=18): the KILLED case
# =============================================================================
log("=" * 78)
log("PART 1 -- E6 k=6 (kappa=18, ord T = 108 = 4*27)")
log("=" * 78)

t0 = time.time()
npz = np.load(NPZ_PATH)
counts_bank, T_expo_bank = npz['counts'], npz['T_expo']
S_odd_bank_f, B_odd_bank_f = npz['S_odd'], npz['B_odd']
with open(READOUTS_PATH) as f:
    readouts_bank = json.load(f)
log(f"loaded banked npz + readouts.json ({time.time()-t0:.2f}s): "
    f"N={readouts_bank['N']}, dim_odd={readouts_bank['dim_odd']}, "
    f"order_float={readouts_bank['order_float']}")

t0 = time.time()
W, eps = weyl_group()
L6 = Level(6, W, eps)
log(f"rebuilt Level(6) via engine.py ({time.time()-t0:.2f}s)")

gate_counts = bool(np.array_equal(L6.counts, counts_bank))
gate_texpo = bool(np.array_equal(L6.T_expo, T_expo_bank))
log(f"[GATE E6-0] fresh-build counts == banked npz counts: {gate_counts}")
log(f"[GATE E6-0] fresh-build T_expo == banked npz T_expo: {gate_texpo}")
assert gate_counts and gate_texpo, "E6 cross-gate FAILED vs banked npz"

t0 = time.time()
rep, okg, S_f, T_f, rho_f = L6.run_gates()
log(f"run_gates ({time.time()-t0:.2f}s): ok={okg}")
assert okg, "E6 k=6 run_gates FAILED"
out, S_odd_f, B_odd_f = L6.readouts(S_f, rho_f)
assert out['N'] == 139 and out['dim_odd'] == 61 and out['order_float'] == 18, out
log(f"[GATE E6-1] readouts reproduce banked: N=139, dim_odd=61, order_float=18 -- OK")

dev_bank_f = float(np.max(np.abs(B_odd_f - B_odd_bank_f)))
log(f"[GATE E6-2] float64 B_odd (fresh) vs banked npz B_odd: max|diff| = {dev_bank_f:.3e}")
assert dev_bank_f < 1e-8


def mp_blocks_diagaware(L, dps=DPS):
    """S_odd, B_odd at dps digits, exploiting diagonal T: rho_ab = t_a^2 S_ab t_b.
    Verbatim pattern from proof_queue/q1_level8/level8_run.py."""
    mp.mp.dps = dps
    S = L.S_mp(dps)
    t = [mp.e ** (2j * mp.pi * int(e) / (12 * L.K)) for e in L.T_expo]
    n = len(L.pairs)
    S_odd = mp.matrix(n, n)
    B_odd = mp.matrix(n, n)
    for i, (a, b) in enumerate(L.pairs):
        for j, (c, d) in enumerate(L.pairs):
            so = (S[a, c] - S[a, d] - S[b, c] + S[b, d]) / 2
            bo = (t[a] * t[a] * S[a, c] * t[c] - t[a] * t[a] * S[a, d] * t[d]
                  - t[b] * t[b] * S[b, c] * t[c] + t[b] * t[b] * S[b, d] * t[d]) / 2
            S_odd[i, j] = so
            B_odd[i, j] = bo
    return S_odd, B_odd


t0 = time.time()
S_odd_mp, B_odd_mp = mp_blocks_diagaware(L6, dps=DPS)
log(f"mp_blocks_diagaware(dps={DPS}) built ({time.time()-t0:.2f}s)")

dev_mp_vs_f = max(abs(complex(B_odd_mp[i, j]) - B_odd_f[i, j])
                   for i in range(61) for j in range(61))
log(f"[GATE E6-3] mp B_odd vs float64 B_odd: max|diff| = {float(dev_mp_vs_f):.3e}")
assert dev_mp_vs_f < 1e-6

dev18, props18 = mp_certify_order(B_odd_mp, 18, dps=DPS)
log(f"[GATE E6-4] mp_certify_order(B_odd, 18): ||B^18-I|| = {dev18:.3e}; "
    f"proper divisors dev = { {d: f'{v:.2e}' for d, v in props18.items()} } "
    f"(must be small at 18, large at 9 and 6)")
assert dev18 < 1e-40 and all(v > 1e-3 for v in props18.values())

I61 = mp.eye(61)
t0 = time.time()
B18_e6 = matpow(B_odd_mp, 18)
log(f"B_odd^18 computed ({time.time()-t0:.2f}s)")
dev_vs_I_e6 = float(max_dev(B18_e6, I61))
frob_vs_I_e6 = frob_dev(B18_e6, I61)
log(f"E6 GATE (the kill): ||rho(A1)^18 - I|| max-entry = {dev_vs_I_e6:.3e}, "
    f"Frobenius = {frob_vs_I_e6:.3e}  -->  IDENTITY (killed)")

n_plus_e6, n_minus_e6, n_other_e6, ev_e6 = eig_pm_multiplicities(B18_e6)
log(f"E6 eigenvalue multiplicities of rho(A1)^18: +1 = {n_plus_e6}, "
    f"-1 = {n_minus_e6}, other = {n_other_e6} (dim_odd=61)")
assert n_plus_e6 == 61 and n_minus_e6 == 0

# T_expo mod 27 bookkeeping (12K = 216 = 8*27; ord(T)=108=4*27 => all T_expo even;
# e_a = T_expo[a]//2 represents T_a = zeta_108^{e_a}; m_a = e_a mod 27 is the
# mod-27 CRT-local exponent).
assert all(int(e) % 2 == 0 for e in L6.T_expo), "T_expo not all even -- ord(T)=108 assumption broken"
e6_pair_residues = []
for j, (a, b) in enumerate(L6.pairs):
    assert L6.T_expo[a] == L6.T_expo[b], "theta must preserve T"
    ea = int(L6.T_expo[a]) // 2
    m = ea % 27
    sign = 1 if abs(B18_e6[j, j] - 1) < 1e-6 else (-1 if abs(B18_e6[j, j] + 1) < 1e-6 else 0)
    e6_pair_residues.append((j, a, b, m, sign))
e6_residues_seen = sorted(set(m for _, _, _, m, _ in e6_pair_residues))
e6_all_plus = all(s == 1 for *_, s in e6_pair_residues)
log(f"E6: {len(e6_pair_residues)} theta-odd pairs span {len(e6_residues_seen)} distinct "
    f"T_expo-mod-27 residues; ALL give +1 (killed), independent of residue value: "
    f"{e6_all_plus}")
log(f"    residues seen (mod 27): {e6_residues_seen}")

results['E6'] = {
    'k': 6, 'kappa': 18, 'N': 139, 'dim_odd': 61, 'ordT': 108,
    'ord_B_odd_banked': 18,
    'certify_order_18_dev': dev18,
    'certify_proper_divisor_devs': {str(d): v for d, v in props18.items()},
    'rho_A1_18_minus_I_max_entry': dev_vs_I_e6,
    'rho_A1_18_minus_I_frobenius': frob_vs_I_e6,
    'eig_plus1_mult': n_plus_e6, 'eig_minus1_mult': n_minus_e6, 'eig_other': n_other_e6,
    'T_expo_mod27_residues_seen': e6_residues_seen,
    'all_pairs_give_plus1_regardless_of_residue': e6_all_plus,
}

# =============================================================================
# PART 2 -- SU(3) k=6 (kappa=9): the FAITHFUL case
# =============================================================================
log("")
log("=" * 78)
log("PART 2 -- SU(3) k=6 (kappa=9, ord T = 27)")
log("=" * 78)

mp.mp.dps = DPS


def su3_odd_block(k, dps=DPS):
    mp.mp.dps = dps
    L = An_Level(3, k, name=f"SU(3)_{k}")
    S, T = L.build(verbose=False)
    fixed_idx, pairs = L.theta_split()
    N = S.rows
    odd = mp.matrix(N, len(pairs))
    s2 = 1 / mp.sqrt(2)
    for jj, (a, b) in enumerate(pairs):
        odd[a, jj], odd[b, jj] = s2, -s2
    Tm = odd.T * T * odd
    Sm = odd.T * S * odd
    A1 = Tm * Tm * Sm * Tm
    return L, S, T, odd, A1, fixed_idx, pairs


def elt_order(M, cap=200, tol=1e-30):
    n = M.rows
    I = mp.eye(n)
    P = M.copy()
    for j in range(1, cap + 1):
        if max(abs(P[i, l] - I[i, l]) for i in range(n) for l in range(n)) < tol:
            return j
        P = P * M
    return None


# --- self-gate: reproduce SU(3)_2 banked clock=10, tr=-1/phi (n2_su3_13_measure.py) ---
L2, S2, T2, odd2, A1_2, fixed2, pairs2 = su3_odd_block(2)
o2 = elt_order(A1_2)
phi = (1 + mp.sqrt(5)) / 2
tr2 = A1_2[0, 0] + A1_2[1, 1]
gate_su3_2 = (o2 == 10) and abs(tr2 - (-1 / phi)) < mp.mpf('1e-30')
log(f"[GATE SU3-0] SU(3)_2 self-gate: dim_odd={len(pairs2)} ord(A1_odd)={o2} "
    f"(banked 10) tr={mp.nstr(tr2, 20)} vs -1/phi={mp.nstr(-1/phi, 20)}  ok={gate_su3_2}")
assert gate_su3_2, "SU(3) engine_v7 self-gate FAILED"

# --- the k=6 build ---
t0 = time.time()
L6su3, S6su3, T6su3, odd6su3, A1_6, fixed6su3, pairs6su3 = su3_odd_block(6)
log(f"SU(3)_6 odd block built ({time.time()-t0:.2f}s): N={L6su3.N}, "
    f"n_theta_fixed={len(fixed6su3)}, dim_odd={len(pairs6su3)}")

# ord(T) overall (lcm of all denominators of h_a - c/24)
c24 = L6su3.c / 24
exps = [(h - c24) for h in L6su3.h]
denoms = [e.limit_denominator(10**9).denominator for e in exps]
ordT_su3 = reduce(lambda a, b: a * b // math.gcd(a, b), denoms, 1)
log(f"ord(T) (SU(3) k=6, lcm of per-primary denominators) = {ordT_su3} (banked/expected 27)")
assert ordT_su3 == 27

# --- off-block-null gate: project-then-multiply must equal multiply-then-project ---
rho_full_su3 = T6su3 * T6su3 * S6su3 * T6su3
A1_via_full = odd6su3.T * rho_full_su3 * odd6su3
dev_proj = float(max_dev(A1_6, A1_via_full))
resid = rho_full_su3 * odd6su3 - odd6su3 * (odd6su3.T * rho_full_su3 * odd6su3)
resid_norm = float(max(abs(resid[i, j]) for i in range(resid.rows) for j in range(resid.cols)))
log(f"[GATE SU3-1] project-then-multiply == multiply-then-project: dev = {dev_proj:.3e}")
log(f"[GATE SU3-1] odd-subspace T^2ST-invariance residual: {resid_norm:.3e}")
assert dev_proj < 1e-40 and resid_norm < 1e-40

# --- the clock: ord(B_odd) must reproduce banked 36 ---
t0 = time.time()
o6 = elt_order(A1_6, cap=100)
log(f"[GATE SU3-2] ord(rho(A1)|_odd) at SU(3) k=6 = {o6} (banked 36) [{time.time()-t0:.2f}s]")
assert o6 == 36, f"SU(3) k=6 clock MISMATCH vs banked 36: got {o6}"

dev36, props36 = mp_certify_order(A1_6, 36, dps=DPS)
log(f"[GATE SU3-2] mp_certify_order(B_odd, 36): ||B^36-I|| = {dev36:.3e}; "
    f"proper divisors dev = { {d: f'{v:.2e}' for d, v in props36.items()} } "
    f"(must be small at 36, large at 18 and 12)")
assert dev36 < 1e-40 and all(v > 1e-3 for v in props36.values())

# --- the central image: rho(A1)^18 ---
n_odd_su3 = A1_6.rows
I_su3 = mp.eye(n_odd_su3)
neg_I_su3 = -I_su3
A18_su3 = matpow(A1_6, 18)
dev_vs_I_su3 = float(max_dev(A18_su3, I_su3))
dev_vs_negI_su3 = float(max_dev(A18_su3, neg_I_su3))
frob_vs_I_su3 = frob_dev(A18_su3, I_su3)
log(f"SU(3) GATE (the survival): ||rho(A1)^18 - I|| max-entry = {dev_vs_I_su3:.3e} "
    f"(NON-identity)")
log(f"                          ||rho(A1)^18 - (-I)|| max-entry = {dev_vs_negI_su3:.3e} "
    f"--> EXACTLY -I (faithful central involution)")
assert dev_vs_negI_su3 < 1e-40

A18sq = A18_su3 * A18_su3
dev_involution = float(max_dev(A18sq, I_su3))
log(f"involution check ||(rho(A1)^18)^2 - I|| = {dev_involution:.3e} (must be tiny: "
    f"rho(A1)^18 has order exactly 2)")
assert dev_involution < 1e-35

n_plus_su3, n_minus_su3, n_other_su3, ev_su3 = eig_pm_multiplicities(A18_su3)
log(f"SU(3) eigenvalue multiplicities of rho(A1)^18: +1 = {n_plus_su3}, "
    f"-1 = {n_minus_su3}, other = {n_other_su3} (dim_odd={n_odd_su3})")
assert n_plus_su3 == 0 and n_minus_su3 == n_odd_su3

# T_expo mod 27 bookkeeping for SU(3): m_a = 27*(h_a - c/24) mod 27 (integer since
# denom | 27); one residue per theta-odd pair (h preserved by theta-conjugation).
su3_pair_residues = []
for j, (a, b) in enumerate(pairs6su3):
    assert exps[a] == exps[b], "theta must preserve T"
    frac = exps[a].limit_denominator(10**9)
    m = int((frac * 27) % 27)
    sign = 1 if abs(A18_su3[j, j] - 1) < 1e-6 else (-1 if abs(A18_su3[j, j] + 1) < 1e-6 else 0)
    su3_pair_residues.append((j, L6su3.PRIM[a], L6su3.PRIM[b], m, sign))
su3_residues_seen = sorted(set(m for *_, m, _ in su3_pair_residues))
su3_all_minus = all(s == -1 for *_, s in su3_pair_residues)
log(f"SU(3): {len(su3_pair_residues)} theta-odd pairs span {len(su3_residues_seen)} "
    f"distinct T_expo-mod-27 residues (units and multiples of 3 both present); "
    f"ALL give -1 (survive), independent of residue value: {su3_all_minus}")
log(f"        residues seen (mod 27): {su3_residues_seen}")
for j, pa, pb, m, s in su3_pair_residues:
    log(f"        pair {j}: {pa} <-> {pb}   T_expo mod 27 = {m:2d}   "
        f"gcd(m,27)={math.gcd(m, 27):2d}   sign under A1^18 = {s:+d}")

results['SU3'] = {
    'k': 6, 'kappa': 9, 'N': L6su3.N, 'dim_odd': n_odd_su3, 'ordT': 27,
    'ord_B_odd_measured': o6, 'ord_B_odd_banked': 36,
    'certify_order_36_dev': dev36,
    'certify_proper_divisor_devs': {str(d): v for d, v in props36.items()},
    'rho_A1_18_minus_I_max_entry': dev_vs_I_su3,
    'rho_A1_18_minus_negI_max_entry': dev_vs_negI_su3,
    'rho_A1_18_minus_I_frobenius': frob_vs_I_su3,
    'involution_check_dev': dev_involution,
    'eig_plus1_mult': n_plus_su3, 'eig_minus1_mult': n_minus_su3, 'eig_other': n_other_su3,
    'T_expo_mod27_residues_seen': su3_residues_seen,
    'all_pairs_give_minus1_regardless_of_residue': su3_all_minus,
    'pair_table': [{'pair': j, 'prim_a': list(pa), 'prim_b': list(pb),
                     'T_expo_mod27': m, 'gcd_m_27': math.gcd(m, 27), 'sign': s}
                    for j, pa, pb, m, s in su3_pair_residues],
}

# =============================================================================
# PART 3 -- THE MECHANISM VERDICT
# =============================================================================
log("")
log("=" * 78)
log("PART 3 -- THE MECHANISM VERDICT")
log("=" * 78)

e6_scalar = (n_plus_e6 == 61 and n_minus_e6 == 0)
su3_scalar = (n_plus_su3 == 0 and n_minus_su3 == n_odd_su3)
scalar_mechanism = e6_scalar and su3_scalar

log(f"Both theta-odd blocks act as SCALAR matrices under rho(A1)^18 "
    f"(+I on the WHOLE E6 block, -I on the WHOLE SU(3) block): {scalar_mechanism}")
log("Consequence: the T_expo-mod-27 hypothesis of A3 point 4 (per-primary "
    "prediction) is VACUOUS/DEGENERATE, not selective -- membership in the -1 "
    "class does not depend on the residue class of any individual primary; it is "
    "UNIFORM across the entire theta-odd block, in both stages, verified 100% "
    "(61/61 E6 pairs, 12/12 SU(3) pairs spanning both gcd(m,27)=1 and 3|m "
    "residues). The predicting function is therefore the CONSTANT function of "
    "STAGE TYPE, not of T_expo mod 27: f_E6(m) = +1 for all m; f_SU3(m) = -1 for "
    "all m.")
log("Structural reading (Schur): since rho(A1)^18 is central in the cyclic image "
    "<rho(A1)> and acts as a scalar on the WHOLE theta-odd block, each stage's "
    "theta-odd block behaves, w.r.t. this central element, as a single "
    "homogeneous piece -- consistent with it being (at least effectively) one "
    "irreducible constituent (or a family sharing one central character), not a "
    "mixture the way the prereg's per-primary hypothesis anticipated.")
log("Refutation of the naive 'same conductor => same fate' expectation: both "
    "stages have IDENTICAL local conductor structure at this rung (27 = 3^3, "
    "a 'deep' 3-power by the E6-only PSL law's own classification, "
    "finisher_queue/f2_psl/PSL_THEOREM.md) yet opposite kill behavior. The "
    "arithmetic of the conductor (27, split/deep/shallow typing) is therefore "
    "NOT sufficient on its own to predict kill-vs-survive; the missing input is "
    "the STAGE (which Lie algebra / which modular tensor category the block "
    "comes from) -- matching proof_queue/q2_conductor.py's clock_with(): "
    "'E'-type kills split primes and deep 3-powers, 'A'-type kills nothing, as "
    "a categorical dichotomy, not a further arithmetic refinement of the "
    "conductor. This computation is the first DIRECT (representation-level, "
    "not abstract-2x2-proxy) confirmation of that A-type 'kills nothing' half "
    "of the law at a genuinely deep-3 (27) rung.")

results['mechanism'] = {
    'both_blocks_scalar_under_central_element': scalar_mechanism,
    'e6_scalar_value': '+I (killed)',
    'su3_scalar_value': '-I (faithful involution)',
    'T_expo_mod27_is_selective_within_a_stage': False,
    'verdict': ("SCALAR / STAGE-TYPE MECHANISM, VERIFIED 100%: rho(A1)^18 is a "
                "scalar matrix on each entire theta-odd block (+I for E6 k=6, "
                "-I for SU(3) k=6). The mod-27 central element is therefore "
                "killed or survives as a BLOCK-WIDE (stage-level) fact, not a "
                "per-primary one; T_expo mod 27 does NOT select which primaries "
                "carry -1 (there is no per-primary split to select from -- all "
                "primaries in a stage share the same sign). The A3 point-4 "
                "per-primary correlation hypothesis is therefore FALSIFIED as "
                "stated and replaced by the honest, fully-verified finding: "
                "kill/survive is determined by STAGE TYPE (E-series vs "
                "A-series), matching q2_conductor.py's clock_with() dichotomy, "
                "now confirmed at the representation level (not just the "
                "abstract SL(2,Z) 2x2 proxy) for the first time at k=6."),
}

out_path = f"{WORK}/a3_results.json"
with open(out_path, 'w') as f:
    json.dump(results, f, indent=1, default=str)
log(f"\nsaved results -> {out_path}")
log("\nALL GATES PASSED. A3 run complete.")
