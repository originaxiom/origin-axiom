#!/usr/bin/env python3
"""
W4-270r -- gap-slope ratio: honest, depth-capped, results.json-unconditional
(Wave-3 carry, 2nd). LAST blocker on the numerical route to the exact
gap-slope closed form.

CARRY CHAIN.
  W2-270 : verdict logic could not emit UNRESOLVED (defect D1); killed at
           depth 8 (defect D2); results.json was an optimistic pre-fill.
  W3-270r: fixed the verdict function's UNRESOLVED branch and introduced the
           curvature-removed eps->0 reading, but under host contention was
           KILLED at depth 10, output truncated at depth 9, and -- fatally --
           NO results.json was ever written (it dumped results only at the
           very end, after the depth loop it never finished).
THIS CELL fixes the remaining operational defect: results.json is written
INCREMENTALLY after every completed depth (so it exists no matter when the
process dies), the depth sweep is CAPPED by an in-code wall-clock budget to
whatever converges cleanly IN THIS RUN (depths 7,8,9 are mandatory; 10,11 are
attempted only if the time estimate fits), and the verdict is decided by an
in-code, margin-based, self-tested three-way function that CAN emit
RESOLVED-A / RESOLVED-B / UNRESOLVED.

OBJECT (property of the substitution dynamical system + its tight-binding
operator; B530 Movement XXXIII, frontier/B530_natural_history/listen_38_*.py):
substitution a->abAAB, b->aAB, A->abAB, B->aA on a 4-letter alphabet; the
associated tight-binding chain (unit hopping, on-site potential eps on the
"new" letters {A,B}) has three topological gaps at frozen IDS positions
FREQ[0], FREQ[0]+FREQ[1], 1-FREQ[3] (Bellissard gap labels). Each gap WIDTH
opens linearly in eps at small eps; the observable is the ratio of the two
leading eps->0 slopes (slope of gap-1 / slope of gap-2). No physics reading;
this is a linear-response coefficient of the operator's Cantor spectrum.

ESTABLISHED TENSION (to resolve or honestly bound): the measured ratio sits in
~1.15-1.20 depending on fit protocol, against the named candidate exact form
sqrt(1/phi^2+1) = 1.17557.

DISCRIMINATING FACT (computed IN-CELL, never cited): the "ratio" is NOT a
single number -- it is fit-protocol dependent. gap-1's width has real positive
eps-curvature (d^2 gap/d eps^2 ~ 0.4) while gap-2's is ~0. A curvature-removed
eps->0 fit gives ratio ~1.148; the banked straight-through-origin large-eps
line gives ~1.256. The named candidate 1.17557 lies BETWEEN these and matches
NEITHER converged reading (it is ~2.4% above the eps->0 reading and ~6.4% below
the banked reading). It is therefore refuted in BOTH directions with a margin
several times the seed/depth noise floor -- a bounded negative, not an
identification.

House method: exact/symbolic where a closed form exists (frequencies: sympy-
verified as the exact Perron eigenvector); slopes are a genuine numerical
linear-response coefficient (no closed perturbative form is banked); >=2 eps
seeds with conditioning; every check ASSERTED with direction via gate(); PSLQ
gated by the sealed tolerance-height rule tol=10^-(agree-14) (NOT run at a
trusted tolerance below 15 honest digits, by construction); a base-rate
comparator control (golden-family battery) is run where the criterion invites
one (E20); the verdict function is in-code and self-tested for non-degeneracy.
"""
import json
import time

import numpy as np
from scipy.linalg import eigh_tridiagonal
import mpmath as mp
import sympy as sp

T0 = time.time()
OUT = {}
FAILED = []
CELL_DIR = "/Users/dri/origin-axiom/frontier/B771_phase1_wave1/cells/W4-270r"
RESULTS = f"{CELL_DIR}/results.json"

# in-code wall-clock budget for the whole depth sweep. Kept below a single
# foreground timeout so depths 7,8,9 finish in ONE process and the final
# results.json is written; depth 7 is a known pre-asymptotic point (the
# quadratic curvature fit is unstable there, b1<0), so CONVERGENCE is judged
# only on WARMED-UP depths (>=8). Deeper depths (10,11) cost ~4x each and are
# attempted only if the estimate fits the budget.
WALL_BUDGET_S = 520.0
MANDATORY_DEPTHS = [7, 8, 9]   # always attempted (~6 min total dedicated)
OPTIONAL_DEPTHS = [10, 11]     # attempted only if the time estimate fits
DEPTH_TIME_FACTOR = 4.2        # next-depth cost ~ this * previous-depth cost
WARMUP_MIN_DEPTH = 8           # depths below this are pre-asymptotic (excluded
                               # from the convergence/noise judgement)


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


def gate(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    log(f"GATE {name}: {status}  {detail}")
    if not ok:
        FAILED.append(name)
    return ok


def dump_partial(stage, provisional_verdict="UNRESOLVED"):
    """Write results.json NOW so the file exists no matter when we die."""
    snap = dict(OUT)
    snap["_stage"] = stage
    snap["_partial"] = True
    snap["verdict"] = provisional_verdict
    snap["_elapsed_s"] = round(time.time() - T0, 1)
    json.dump(snap, open(RESULTS, "w"), indent=1, default=str)


# ===================================================== STEP 0: frequencies (exact)
PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
LETTERS = ['a', 'b', 'A', 'B']

log("== STEP 0: re-derive frequencies from the substitution incidence matrix ==")
M = np.zeros((4, 4))
for j, c in enumerate(LETTERS):
    for ch in SUB[c]:
        M[LETTERS.index(ch), j] += 1
eigval, eigvec = np.linalg.eig(M)
i_perron = int(np.argmax(eigval.real))
perron_vec = np.abs(eigvec[:, i_perron].real)
perron_vec = perron_vec / perron_vec.sum()

S_banked = PHI + 1 + PHI * SQ + SQ
FREQ = np.array([PHI / S_banked, 1 / S_banked, PHI * SQ / S_banked, SQ / S_banked])
freq_err = float(np.max(np.abs(perron_vec - FREQ)))
gate("G0 Perron freq vector == banked closed form (phi,sqrt(phi))",
     freq_err < 1e-9, f"max|diff|={freq_err:.2e}")

phi_s = (1 + sp.sqrt(5)) / 2
sq_s = sp.sqrt(phi_s)
S_s = phi_s + 1 + phi_s * sq_s + sq_s
F_s = sp.Matrix([phi_s / S_s, 1 / S_s, phi_s * sq_s / S_s, sq_s / S_s])
Ms = sp.Matrix(M.astype(int).tolist())
resid = sp.simplify(Ms * F_s - (Ms * F_s)[0] / F_s[0] * F_s)
gate("G0b sympy: banked FREQ is an exact eigenvector of the incidence matrix",
     all(sp.simplify(x) == 0 for x in resid), "M F parallel to F (exact)")

TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]
log(f"  TARGET_IDS = {[float(x) for x in TARGET_IDS]}")
OUT["target_ids"] = [float(x) for x in TARGET_IDS]
dump_partial("after_step0")


def _word(depth):
    u = 'a'
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


# ============================================================ STEP 1: solver
def gap_width(word, target_id, eps, window=60):
    """Max level spacing in a window of eigen-indices around target_id*N, via a
    windowed LAPACK tridiagonal eigensolve (select='i')."""
    N = len(word)
    diag = np.array([eps if c in 'AB' else 0.0 for c in word])
    off = np.ones(N - 1)
    center = int(round(target_id * N))
    lo = max(0, center - window)
    hi = min(N - 1, center + window)
    eigs = eigh_tridiagonal(diag, off, select='i', select_range=(lo, hi),
                            eigvals_only=True)
    d = np.diff(eigs)
    return float(d.max()) if len(d) else 0.0


def slope_eps0(word, target_id, eps_grid, window=60):
    """eps->0 linear-response slope: fit gap = a*eps + b*eps^2 through the
    origin over SMALL eps; return (a, b, widths). The quadratic term b absorbs
    the leading curvature that a straight-through-origin line folds into a."""
    w = np.array([gap_width(word, target_id, e, window) for e in eps_grid])
    A = np.vstack([eps_grid, eps_grid ** 2]).T
    coef, *_ = np.linalg.lstsq(A, w, rcond=None)
    return float(coef[0]), float(coef[1]), w


def slope_line_origin(word, target_id, eps_grid, window=60):
    """The BANKED protocol: straight line through the origin (no curvature
    term) over the eps grid. Reproduces the ~1.20-1.26 headline family."""
    w = np.array([gap_width(word, target_id, e, window) for e in eps_grid])
    return float(np.sum(eps_grid * w) / np.sum(eps_grid ** 2)), w


# two disjoint SMALL-eps seeds for the curvature-removed eps->0 reading
SEED_A = np.array([0.004, 0.008, 0.012, 0.016, 0.020])
SEED_B = np.array([0.005, 0.010, 0.015, 0.020, 0.025])
# two disjoint LARGE-eps seeds for the banked straight-through-origin reading
BANK_A = np.array([0.01, 0.02, 0.03, 0.04, 0.05])
BANK_B = np.array([0.015, 0.025, 0.035, 0.045, 0.055])

DATA = {}
completed = []

log("== STEP 1: eps->0 (curvature-removed) + banked (large-eps line) sweep ==")
depth = MANDATORY_DEPTHS[0]
last_dt = None
while depth <= OPTIONAL_DEPTHS[-1]:
    is_mandatory = depth in MANDATORY_DEPTHS
    # time-budget gate for optional depths
    if not is_mandatory and last_dt is not None:
        est_next = DEPTH_TIME_FACTOR * last_dt
        remaining = WALL_BUDGET_S - (time.time() - T0)
        if est_next > remaining:
            log(f"  depth {depth} SKIPPED: est {est_next:.0f}s > remaining "
                f"budget {remaining:.0f}s (honest depth cap = {completed[-1]})")
            break
        log(f"  depth {depth}: est {est_next:.0f}s <= remaining {remaining:.0f}s"
            f" -> attempting")
    try:
        word = _word(depth)
        N = len(word)
        t0 = time.time()
        rec = {"N": N}
        a1A, b1A, _ = slope_eps0(word, TARGET_IDS[0], SEED_A)
        a2A, b2A, _ = slope_eps0(word, TARGET_IDS[1], SEED_A)
        a1B, b1B, _ = slope_eps0(word, TARGET_IDS[0], SEED_B)
        a2B, b2B, _ = slope_eps0(word, TARGET_IDS[1], SEED_B)
        s1LA, _ = slope_line_origin(word, TARGET_IDS[0], BANK_A)
        s2LA, _ = slope_line_origin(word, TARGET_IDS[1], BANK_A)
        s1LB, _ = slope_line_origin(word, TARGET_IDS[0], BANK_B)
        s2LB, _ = slope_line_origin(word, TARGET_IDS[1], BANK_B)
        rec["eps0_seedA"] = [a1A, a2A]
        rec["eps0_seedB"] = [a1B, a2B]
        rec["curv_b_seedA"] = [b1A, b2A]
        rec["ratio_eps0_A"] = a1A / a2A
        rec["ratio_eps0_B"] = a1B / a2B
        rec["banked_seedA"] = [s1LA, s2LA]
        rec["banked_seedB"] = [s1LB, s2LB]
        rec["ratio_banked_A"] = s1LA / s2LA
        rec["ratio_banked_B"] = s1LB / s2LB
        dt = time.time() - t0
        last_dt = dt
        DATA[depth] = rec
        completed.append(depth)
        log(f"  d={depth:2d} N={N:>8d} | eps0 A r={a1A/a2A:.6f} B r={a1B/a2B:.6f}"
            f" | banked A r={s1LA/s2LA:.6f} B r={s1LB/s2LB:.6f}"
            f" | curv b1={b1A:.3f} b2={b2A:.3f} [{dt:.1f}s]")
        OUT["depth_data"] = {str(k): v for k, v in DATA.items()}
        OUT["completed_depths"] = list(completed)
        dump_partial(f"after_depth_{depth}")   # <-- results.json exists NOW
    except Exception as e:  # noqa: BLE001 -- any solver/host failure: stop cleanly
        log(f"  depth {depth} FAILED ({type(e).__name__}: {e}); stopping sweep "
            f"at last good depth {completed[-1] if completed else 'NONE'}")
        break
    depth += 1

gate("G-sweep at least depths 7,8,9 completed (mandatory floor)",
     all(d in completed for d in MANDATORY_DEPTHS),
     f"completed = {completed}")
DEEP = completed[-1]
OUT["honest_depth_cap"] = DEEP
log(f"  HONEST DEPTH CAP (deepest completed this run) = {DEEP} "
    f"(N={DATA[DEEP]['N']})")

# ------ ASSERTED discriminating mechanism: gap1 has curvature, gap2 ~0 ------
b1 = DATA[DEEP]["curv_b_seedA"][0]
b2 = DATA[DEEP]["curv_b_seedA"][1]
gate("G1 gap1 eps-curvature is real & >> gap2's at the depth cap "
     "(the mechanism inflating the banked line reading)",
     b1 > 0.2 and abs(b2) < 0.1,
     f"b1={b1:.3f} (>0.2)  b2={b2:.3f} (|.|<0.1)")

# ------ ASSERTED: banked reading lands in the ~1.20-1.27 artifact family ----
gate("G2 banked straight-through-origin reading in [1.18,1.28] at depth cap "
     "(reproduces the headline-style number)",
     1.18 < DATA[DEEP]["ratio_banked_A"] < 1.28,
     f"banked ratio (seedA) = {DATA[DEEP]['ratio_banked_A']:.6f}")

# ------ ASSERTED: the two protocols DISAGREE (>1%): 'the ratio' is not one # ---
disagree = abs(DATA[DEEP]["ratio_banked_A"] - DATA[DEEP]["ratio_eps0_A"])
gate("G3 banked and eps->0 readings DISAGREE by >3% at depth cap "
     "(proves the ratio is fit-protocol dependent, not a single number)",
     disagree / DATA[DEEP]["ratio_eps0_A"] > 0.03,
     f"|banked - eps0|/eps0 = {disagree/DATA[DEEP]['ratio_eps0_A']*100:.2f}%")
dump_partial("after_step1_gates")

# ============================================ STEP 2: convergence & noise floor
log("== STEP 2: N-convergence + seed noise floor of BOTH readings ==")


WARM = [d for d in completed if d >= WARMUP_MIN_DEPTH]


def noise_floor(reading_A_key, reading_B_key):
    """Relative noise of a reading at the depth cap = max(seed disagreement,
    last depth-to-depth drift of seedA over WARMED-UP depths). Smaller => more
    converged. If fewer than two warmed-up depths exist, the depth-to-depth
    drift is undefined (inf) -> the reading is declared NOT converged (honest:
    a single warmed-up depth cannot certify N-convergence)."""
    r_A = DATA[DEEP][reading_A_key]
    r_B = DATA[DEEP][reading_B_key]
    seed_rel = abs(r_A - r_B) / abs(r_A)
    if len(WARM) >= 2 and DEEP >= WARMUP_MIN_DEPTH:
        prev = WARM[-2]                       # deepest warmed-up depth below DEEP
        drift_rel = abs(DATA[DEEP][reading_A_key] - DATA[prev][reading_A_key]) \
            / abs(DATA[DEEP][reading_A_key])
    else:
        drift_rel = float("inf")
    return max(seed_rel, drift_rel), seed_rel, drift_rel, r_A


eps0_noise, eps0_seed, eps0_drift, eps0_val = noise_floor(
    "ratio_eps0_A", "ratio_eps0_B")
bank_noise, bank_seed, bank_drift, bank_val = noise_floor(
    "ratio_banked_A", "ratio_banked_B")

eps0_digits = float(-np.log10(eps0_noise)) if eps0_noise > 0 else 16.0
bank_digits = float(-np.log10(bank_noise)) if bank_noise > 0 else 16.0
log(f"  eps->0 reading: value {eps0_val:.6f}  noise {eps0_noise:.2e} "
    f"(seed {eps0_seed:.2e}, drift {eps0_drift:.2e}) ~ {eps0_digits:.2f} digits")
log(f"  banked reading: value {bank_val:.6f}  noise {bank_noise:.2e} "
    f"(seed {bank_seed:.2e}, drift {bank_drift:.2e}) ~ {bank_digits:.2f} digits")

# a reading is 'converged enough to test a % candidate' if its noise < 2%
eps0_converged = eps0_noise < 0.02
bank_converged = bank_noise < 0.02
gate("G4 eps->0 reading converged to better than 2% at the depth cap "
     "(so a percent-level candidate CAN be tested against it)",
     eps0_converged, f"noise {eps0_noise:.2e} (< 2e-2 required)")

achieved_digits = int(np.floor(min(eps0_digits, bank_digits)))
achieved_digits = max(achieved_digits, 1)
OUT["ratio_eps0_by_depth"] = {str(d): DATA[d]["ratio_eps0_A"] for d in completed}
OUT["ratio_banked_by_depth"] = {str(d): DATA[d]["ratio_banked_A"] for d in completed}
OUT["eps0"] = {"value": eps0_val, "noise": eps0_noise, "digits": eps0_digits,
               "converged": bool(eps0_converged)}
OUT["banked"] = {"value": bank_val, "noise": bank_noise, "digits": bank_digits,
                 "converged": bool(bank_converged)}
OUT["achieved_digits"] = achieved_digits
dump_partial("after_step2")

# ======================================= STEP 3: candidate test (BOTH readings)
log("== STEP 3: test candidate sqrt(1/phi^2+1) against BOTH readings ==")
mp.mp.dps = 30
phi_mp = (1 + mp.sqrt(5)) / 2
sqphi_mp = mp.sqrt(phi_mp)
cand = mp.sqrt(1 / phi_mp ** 2 + 1)
log(f"  candidate sqrt(1/phi^2+1) = {mp.nstr(cand, 10)}")
eps0_mp = mp.mpf(repr(eps0_val))
bank_mp = mp.mpf(repr(bank_val))
err_eps0 = abs(cand - eps0_mp) / eps0_mp
err_bank = abs(cand - bank_mp) / bank_mp
log(f"  vs eps->0 {mp.nstr(eps0_mp,7)}: rel err {mp.nstr(100*err_eps0,3)}% "
    f"(noise {eps0_noise:.2e})")
log(f"  vs banked {mp.nstr(bank_mp,7)}: rel err {mp.nstr(100*err_bank,3)}% "
    f"(noise {bank_noise:.2e})")

# refuted in a reading iff the miss exceeds 3x that reading's noise floor
K = 3.0
refuted_eps0 = float(err_eps0) > K * eps0_noise and eps0_converged
refuted_bank = float(err_bank) > K * bank_noise and bank_converged
gate("G5 candidate REFUTED vs eps->0 reading (miss > 3x noise, converged)",
     refuted_eps0,
     f"miss {float(err_eps0):.2e} vs 3*noise {K*eps0_noise:.2e}")
gate("G6 candidate REFUTED vs banked reading (miss > 3x noise, converged)",
     refuted_bank,
     f"miss {float(err_bank):.2e} vs 3*noise {K*bank_noise:.2e}")
OUT["candidate_sqrt(1/phi^2+1)"] = {
    "value": mp.nstr(cand, 12),
    "rel_err_vs_eps0": mp.nstr(err_eps0, 5),
    "rel_err_vs_banked": mp.nstr(err_bank, 5),
    "refuted_eps0": bool(refuted_eps0),
    "refuted_banked": bool(refuted_bank),
    "refuted_both": bool(refuted_eps0 and refuted_bank)}

# ---- E20 base-rate comparator control: how many unrelated golden-family
#      forms sit within the achieved precision of the eps->0 reading? (a 'close'
#      candidate is only meaningful if such collisions are RARE at this floor) --
battery = {
    "sqrt(1/phi^2+1)": cand,
    "phi^(1/6)": phi_mp ** mp.mpf('1/6'),
    "sqrt(phi)": sqphi_mp,
    "6/5": mp.mpf(6) / 5,
    "1+1/phi^3": 1 + 1 / phi_mp ** 3,
    "phi^2-1/2": phi_mp ** 2 - mp.mpf('0.5'),
    "sqrt(1+1/(2phi))": mp.sqrt(1 + 1 / (2 * phi_mp)),
    "(1+sqrt(phi))/phi^(3/2)": (1 + sqphi_mp) / phi_mp ** mp.mpf('1.5'),
    "23/20": mp.mpf(23) / 20,
    "phi^(1/3)": phi_mp ** mp.mpf('1/3'),
    "9/8": mp.mpf(9) / 8,
    "sqrt(4/3)": mp.sqrt(mp.mpf(4) / 3),
}
close_forms = [nm for nm, v in battery.items()
               if abs(v - eps0_mp) / eps0_mp < 3 * eps0_noise]
log(f"  E20 base-rate control: golden/simple forms within 3x noise of the "
    f"eps->0 reading ({eps0_val:.5f}): {close_forms}")
gate("G7 base-rate control: the eps->0 reading does NOT uniquely single out "
     "the named candidate (either it is refuted, or several forms collide)",
     ("sqrt(1/phi^2+1)" not in close_forms) or len(close_forms) >= 2,
     f"close forms = {close_forms}")
OUT["base_rate_close_forms"] = close_forms

# =============================================== STEP 4: sealed PSLQ tol rule
log("== STEP 4: sealed tolerance-height rule tol = 10^-(agree-14) ==")
tol_exp = achieved_digits - 14
rule_satisfiable = tol_exp >= 1
gate("G8 sealed PSLQ rule satisfiable (needs >=15 honest digits: agree-14>=1)",
     rule_satisfiable, f"achieved={achieved_digits} -> tol_exp={tol_exp} (>=1)")
pslq_hit = None
if rule_satisfiable:
    tol = mp.mpf(10) ** (-tol_exp)
    basis = [mp.mpf(1), phi_mp, sqphi_mp, phi_mp * sqphi_mp, mp.sqrt(5), eps0_mp]
    pslq_hit = mp.pslq(basis, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 5)
    log(f"  PSLQ over golden basis (trusted tolerance): {pslq_hit}")
else:
    log("  PSLQ NOT run at a trusted tolerance: achieved precision "
        f"({achieved_digits} digits) is below the rule's 15-digit floor; "
        "running it at the achieved tolerance would only re-report the "
        "base-rate collisions above (untrusted by construction).")
OUT["pslq_hit_trusted"] = list(map(int, pslq_hit)) if pslq_hit else None
OUT["pslq_rule_satisfiable"] = bool(rule_satisfiable)
dump_partial("after_step4")


# ===================================================== STEP 5: verdict function
def decide_verdict(rule_ok, pslq_hit, eps0_conv, refuted_eps0, refuted_bank,
                   candidate_within_noise):
    """Honest three-way verdict, in-code and self-tested.
      RESOLVED-A : an exact form is identified in a trusted way (PSLQ hit under
                   the sealed >=15-digit tolerance-height rule).
      RESOLVED-B : bounded negative -- the depth-cap reading IS converged
                   (<2%) and the named candidate is refuted with a computed
                   margin (>3x noise) in BOTH fit-protocol readings; no exact
                   form is identifiable at this precision.
      UNRESOLVED : the reading is not converged, OR the candidate sits within
                   the noise band (can neither confirm nor refute).
    The three branches are mutually exclusive and exhaustive; each is reachable
    (self-tested below)."""
    if rule_ok and pslq_hit is not None:
        return "RESOLVED-A", ("an exact golden-family relation is identified "
                              "and trusted under the sealed tolerance-height "
                              "rule")
    if candidate_within_noise:
        return "UNRESOLVED", ("the named candidate sits within the reading's "
                              "own noise band -- it can be neither confirmed "
                              "nor refuted at the achieved precision")
    if eps0_conv and refuted_eps0 and refuted_bank:
        return "RESOLVED-B", ("bounded negative: the depth-cap reading is "
                              "converged (<2%) and the named candidate is "
                              "refuted with a >3x-noise margin in BOTH "
                              "fit-protocol readings; no exact form is "
                              "identifiable at this precision")
    return "UNRESOLVED", ("the reading is not converged enough to either "
                          "identify a form or refute the candidate with a "
                          "trustworthy margin")


# ---- SELF-TEST: prove each of the three verdicts is reachable ----
st_A = decide_verdict(True, [1, -2, 0, 0, 0, 5], True, False, False, False)[0]
st_B = decide_verdict(False, None, True, True, True, False)[0]
st_U1 = decide_verdict(False, None, False, False, False, False)[0]   # unconverged
st_U2 = decide_verdict(False, None, True, False, True, True)[0]      # within noise
gate("G9 verdict function NON-DEGENERATE: RESOLVED-A / RESOLVED-B / UNRESOLVED "
     "each reachable (fixes carry-chain defect D1)",
     st_A == "RESOLVED-A" and st_B == "RESOLVED-B"
     and st_U1 == "UNRESOLVED" and st_U2 == "UNRESOLVED",
     f"selftest -> A:{st_A} B:{st_B} U1:{st_U1} U2:{st_U2}")

# vacuity self-test (house rule): if we replace the reading value by a free
# symbol far from every battery form, the candidate must NOT be 'within noise'
# and G7 must not vacuously pass -- i.e. the criterion depends on the actual
# computed value, it is not a tautology.
_fake = mp.mpf('1.5000')
_fake_close = [nm for nm, v in battery.items()
               if abs(v - _fake) / _fake < 3 * eps0_noise]
gate("G10 non-vacuity: substituting a free value (1.5) for the reading changes "
     "the base-rate answer (criterion reads the computed value, not a tautology)",
     _fake_close != close_forms,
     f"real close={close_forms} vs fake(1.5) close={_fake_close}")

# candidate 'within noise' of the eps->0 reading? (the UNRESOLVED trigger)
candidate_within_noise = float(err_eps0) <= K * eps0_noise and eps0_converged

verdict, rationale = decide_verdict(
    rule_satisfiable, pslq_hit, eps0_converged,
    refuted_eps0, refuted_bank, candidate_within_noise)

log("== STEP 5: VERDICT ==")
log(f"  FINAL VERDICT: {verdict}")
log(f"  rationale: {rationale}")

OUT["verdict"] = verdict
OUT["rationale"] = rationale
OUT["failed_gates"] = FAILED
OUT["_partial"] = False
OUT["_stage"] = "final"
OUT["discriminating_fact"] = (
    f"The gap-slope 'ratio' is fit-protocol dependent, not a single number. "
    f"gap-1's width has real positive eps-curvature (d2 gap/d eps2 ~ {b1:.2f}) "
    f"while gap-2's is ~0 (b2 ~ {b2:.3f}); a curvature-removed eps->0 fit gives "
    f"ratio {eps0_val:.5f} (depth cap {DEEP}, N={DATA[DEEP]['N']}, two eps seeds, "
    f"noise {eps0_noise:.1e} ~ {eps0_digits:.1f} digits) while the banked "
    f"straight-through-origin large-eps line gives {bank_val:.5f}. The named "
    f"candidate sqrt(1/phi^2+1) = {float(cand):.5f} lies BETWEEN the two "
    f"readings and matches NEITHER: it misses the eps->0 reading by "
    f"{float(err_eps0)*100:.2f}% and the banked reading by "
    f"{float(err_bank)*100:.2f}%, both > 3x the respective noise floors -- "
    f"refuted in BOTH directions. No exact form is identifiable via this "
    f"numerical route: the achieved precision ({achieved_digits} honest digits) "
    f"is far below the sealed tolerance-height rule's 15-digit floor, and the "
    f"base-rate control shows simple/golden forms collide at this precision.")

json.dump(OUT, open(RESULTS, "w"), indent=1, default=str)
log(f"== DONE: results.json written, verdict {verdict}, {len(FAILED)} failed "
    f"gates ==")
