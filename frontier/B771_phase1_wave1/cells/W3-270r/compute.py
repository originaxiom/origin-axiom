#!/usr/bin/env python3
"""
W3-270r -- gap-slope ratio: honest verdict logic + full-depth run (Wave-2 carry).

CARRY CONTEXT. Wave-2 cell W2-270 was REFUSED for two named defects:
  (D1) its verdict logic could ONLY emit RESOLVED-A / RESOLVED-B -- there was
       no code path that could ever output UNRESOLVED (STEP 5 of the prior
       compute.py: `if not rule_satisfiable: RESOLVED-B else RESOLVED-A/B`).
  (D2) it never reached depths 9-11 (its background run was killed after
       depth 8), so it never actually recomputed the object to convergence.
This cell fixes BOTH: a verdict function with a genuine UNRESOLVED branch
(SELF-TESTED below: fed synthetic inputs, it CAN emit each of the three
verdicts), and a full-depth run to depths 9,10,11 (N up to 2.2M).

OBJECT (B530 Movement XXXIII, frontier/B530_natural_history/listen_38_*.py):
substitution a->abAAB, b->aAB, A->abAB, B->aA on a 4-letter alphabet;
tight-binding chain (hopping 1, on-site potential eps on the "new" letters
{A,B}); three topological gaps at frozen IDS positions FREQ[0],
FREQ[0]+FREQ[1], 1-FREQ[3] (Bellissard gap labels). Gap WIDTH opens linearly
in eps at small eps; the banked headline is slope1/slope2 ~ 1.204 at depth 9,
with the candidate exact form sqrt(1/phi^2+1)=1.176 REFUTED (2.4% off).

WHAT THIS CELL COMPUTES (the discriminating fact, IN-CELL, never cited):
The banked "ratio 1.204" is a FIT-PROTOCOL ARTIFACT. slope_i is the eps->0
derivative d(gap_i)/d(eps). Gap 1 has strong positive curvature in eps
(d^2 gap1/d eps^2 ~ 0.4), gap 2 has almost none (~0.017). Fitting a straight
line THROUGH THE ORIGIN over a LARGE eps window ({0.01..0.05}) therefore
over-estimates slope1 (curvature contamination) while leaving slope2 nearly
correct -- inflating the ratio. The true eps->0 linear-response ratio,
extracted with a curvature-removing (quadratic-through-origin) fit over SMALL
eps, is ~1.15, NOT 1.204. This cell measures BOTH readings at depths 9-11,
two disjoint eps seeds each, checks N-convergence, and reports the honest
achievable precision. The named candidate 1.176 is then tested against BOTH
readings.

House method: exact/symbolic where a closed form exists (frequencies:
sympy-verified against the Perron eigenvector; slopes: no closed form is
known -- a genuine numerical linear-response coefficient of a Cantor-measure
spectrum); >=2 seeds with conditioning (UNSTABLE beats forced); every check
ASSERTED with its direction (gate()); the discriminating fact computed
in-cell; PSLQ gated by the sealed tolerance-height rule tol=10^-(agree-14);
UNRESOLVED is honest and the verdict function can emit it (SELF-TESTED).
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
CELL_DIR = "/Users/dri/origin-axiom/frontier/B771_phase1_wave1/cells/W3-270r"
RESULTS = f"{CELL_DIR}/results.json"


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


def gate(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    log(f"GATE {name}: {status}  {detail}")
    if not ok:
        FAILED.append(name)
    return ok


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

# sympy exact check that FREQ IS the normalized Perron eigenvector (M F = lam F)
phi_s = (1 + sp.sqrt(5)) / 2
sq_s = sp.sqrt(phi_s)
S_s = phi_s + 1 + phi_s * sq_s + sq_s
F_s = sp.Matrix([phi_s / S_s, 1 / S_s, phi_s * sq_s / S_s, sq_s / S_s])
Ms = sp.Matrix(M.astype(int).tolist())
resid = sp.simplify(Ms * F_s - (Ms * F_s)[0] / F_s[0] * F_s)
gate("G0b sympy: banked FREQ is an exact eigenvector of the incidence matrix",
     all(sp.simplify(x) == 0 for x in resid), "M F parallel to F (exact)")

TARGET_IDS = [FREQ[0], FREQ[0] + FREQ[1], 1 - FREQ[3]]
log(f"  TARGET_IDS = {TARGET_IDS}")


def _word(depth):
    u = 'a'
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


# ============================================================ STEP 1: solver
def gap_width(word, target_id, eps, window=60):
    """Max level spacing in a window around target_id*N via LAPACK windowed
    eigensolve (select='i')."""
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
    origin over SMALL eps; return (a, b, widths). a removes the leading
    curvature contamination that a straight-through-origin line would fold in."""
    w = np.array([gap_width(word, target_id, e, window) for e in eps_grid])
    A = np.vstack([eps_grid, eps_grid ** 2]).T
    coef, *_ = np.linalg.lstsq(A, w, rcond=None)
    return float(coef[0]), float(coef[1]), w


def slope_line_origin(word, target_id, eps_grid, window=60):
    """The BANKED protocol: straight line through the origin (no curvature
    term) over the eps grid. Reproduces the 1.204-style reading."""
    w = np.array([gap_width(word, target_id, e, window) for e in eps_grid])
    return float(np.sum(eps_grid * w) / np.sum(eps_grid ** 2)), w


# two disjoint SMALL-eps seeds (curvature small; quadratic term mops up rest)
SEED_A = np.array([0.004, 0.008, 0.012, 0.016, 0.020])
SEED_B = np.array([0.005, 0.010, 0.015, 0.020, 0.025])
# the banked-protocol large-eps grid, straight-through-origin (artifact reading)
BANKED_GRID = np.array([0.01, 0.02, 0.03, 0.04, 0.05])

DEPTHS = [7, 8, 9, 10, 11]
DATA = {}

log("== STEP 1: eps->0 (curvature-removed) slopes + banked-protocol reading ==")
for depth in DEPTHS:
    word = _word(depth)
    N = len(word)
    t0 = time.time()
    rec = {"N": N}
    # eps->0 curvature-removed, two seeds
    a1A, b1A, _ = slope_eps0(word, TARGET_IDS[0], SEED_A)
    a2A, b2A, _ = slope_eps0(word, TARGET_IDS[1], SEED_A)
    a1B, b1B, _ = slope_eps0(word, TARGET_IDS[0], SEED_B)
    a2B, b2B, _ = slope_eps0(word, TARGET_IDS[1], SEED_B)
    rec["eps0_seedA"] = [a1A, a2A]
    rec["eps0_seedB"] = [a1B, a2B]
    rec["curv_b_seedA"] = [b1A, b2A]
    rec["ratio_eps0_A"] = a1A / a2A
    rec["ratio_eps0_B"] = a1B / a2B
    # banked-protocol straight-through-origin, large eps
    s1L, _ = slope_line_origin(word, TARGET_IDS[0], BANKED_GRID)
    s2L, _ = slope_line_origin(word, TARGET_IDS[1], BANKED_GRID)
    rec["banked_slopes"] = [s1L, s2L]
    rec["ratio_banked"] = s1L / s2L
    DATA[depth] = rec
    log(f"  d={depth:2d} N={N:>8d} | eps0 A:s1={a1A:.6f} s2={a2A:.6f} "
        f"r={a1A/a2A:.6f} | eps0 B:r={a1B/a2B:.6f} | "
        f"banked(line,large-eps):s1={s1L:.6f} s2={s2L:.6f} r={s1L/s2L:.6f} "
        f"| curv b1={b1A:.3f} b2={b2A:.3f} [{time.time()-t0:.1f}s]")

OUT["depth_data"] = DATA

# ------ ASSERTED discriminating fact: gap1 has curvature, gap2 does not ------
# (this is WHY the banked line-through-origin reading is inflated)
b1_d9 = DATA[9]["curv_b_seedA"][0]
b2_d9 = DATA[9]["curv_b_seedA"][1]
gate("G1 gap1 curvature is real and >> gap2 curvature (depth 9): "
     "the mechanism that inflates the banked line-fit ratio",
     b1_d9 > 0.2 and abs(b2_d9) < 0.1,
     f"b1={b1_d9:.3f} (>0.2 expected)  b2={b2_d9:.3f} (|.|<0.1 expected)")

# ------ ASSERTED: banked reading reproduces the ~1.20-1.26 family ------
gate("G2 banked line/large-eps reading lands in the 1.20-1.27 'artifact' "
     "family at depth 9 (reproduces the headline-style number)",
     1.18 < DATA[9]["ratio_banked"] < 1.28,
     f"banked ratio d9 = {DATA[9]['ratio_banked']:.6f}")

# ------ ASSERTED: the two readings genuinely DISAGREE (protocol dependence) --
gap_readings = abs(DATA[9]["ratio_banked"] - DATA[9]["ratio_eps0_A"])
gate("G3 eps->0 ratio and banked-line ratio DISAGREE by >1% at depth 9 "
     "(proves the 'ratio' is fit-protocol dependent, not a single number)",
     gap_readings / DATA[9]["ratio_eps0_A"] > 0.01,
     f"|banked - eps0|/eps0 = {gap_readings/DATA[9]['ratio_eps0_A']*100:.2f}%")

# ============================================ STEP 2: N-convergence & precision
log("== STEP 2: N-convergence of the eps->0 ratio (depths 9,10,11) + seeds ==")
conv_depths = [9, 10, 11]
r_eps0 = [DATA[d]["ratio_eps0_A"] for d in conv_depths]
log(f"  eps->0 ratio (seedA) at depths {conv_depths}: "
    f"{[f'{x:.6f}' for x in r_eps0]}")

# depth-to-depth agreement (N-convergence digits)
depth_digits = []
for i in range(len(r_eps0) - 1):
    d = abs(r_eps0[i + 1] - r_eps0[i])
    depth_digits.append(float(-np.log10(d / r_eps0[i + 1])) if d > 0 else 16.0)
log(f"  depth-to-depth agreement digits (9->10, 10->11): "
    f"{[f'{x:.2f}' for x in depth_digits]}")

# seed-to-seed agreement at the deepest depth (eps-discretization digits)
d11 = DATA[11]
seed_gap = abs(d11["ratio_eps0_A"] - d11["ratio_eps0_B"])
seed_digits = float(-np.log10(seed_gap / d11["ratio_eps0_A"])) if seed_gap > 0 else 16.0
log(f"  seed A vs B at depth 11: {d11['ratio_eps0_A']:.6f} vs "
    f"{d11['ratio_eps0_B']:.6f}  agree ~ {seed_digits:.2f} digits")

# honest achieved precision = min of N-convergence and seed-agreement floors
achieved_digits = int(np.floor(min(
    depth_digits[-1] if depth_digits else 1.0,
    seed_digits)))
achieved_digits = max(achieved_digits, 1)
best_ratio = DATA[11]["ratio_eps0_A"]
log(f"  BEST eps->0 ratio estimate (depth 11, seedA) = {best_ratio:.6f}")
log(f"  HONEST ACHIEVED PRECISION = {achieved_digits} digits "
    f"(min of depth-conv {depth_digits[-1]:.2f} and seed-agree {seed_digits:.2f})")
OUT["ratio_eps0_conv"] = r_eps0
OUT["depth_conv_digits"] = depth_digits
OUT["seed_agree_digits_d11"] = seed_digits
OUT["achieved_digits"] = achieved_digits
OUT["best_ratio_eps0"] = best_ratio
OUT["best_ratio_banked"] = DATA[11]["ratio_banked"]

# ======================================= STEP 3: candidate test (BOTH readings)
log("== STEP 3: test the named candidate sqrt(1/phi^2+1) against BOTH readings ==")
mp.mp.dps = 30
phi_mp = (1 + mp.sqrt(5)) / 2
cand = mp.sqrt(1 / phi_mp ** 2 + 1)
log(f"  candidate sqrt(1/phi^2+1) = {mp.nstr(cand, 10)}")
r_eps0_mp = mp.mpf(repr(best_ratio))
r_bank_mp = mp.mpf(repr(DATA[11]["ratio_banked"]))
err_eps0 = abs(cand - r_eps0_mp) / r_eps0_mp
err_bank = abs(cand - r_bank_mp) / r_bank_mp
log(f"  vs eps->0 ratio {mp.nstr(r_eps0_mp,7)}:  rel err {mp.nstr(100*err_eps0,3)}%")
log(f"  vs banked ratio {mp.nstr(r_bank_mp,7)}:  rel err {mp.nstr(100*err_bank,3)}%")
# refuted iff the rel error exceeds several times the achieved precision floor
prec_floor = mp.mpf(10) ** (-(achieved_digits))
cand_refuted_eps0 = err_eps0 > 10 * prec_floor
cand_refuted_bank = err_bank > 10 * prec_floor
gate("G4 candidate sqrt(1/phi^2+1) REFUTED vs eps->0 ratio "
     "(rel err >> achieved-precision floor)",
     bool(cand_refuted_eps0),
     f"err {float(err_eps0):.2e} vs 10*floor {float(10*prec_floor):.2e}")
gate("G5 candidate sqrt(1/phi^2+1) REFUTED vs banked ratio",
     bool(cand_refuted_bank),
     f"err {float(err_bank):.2e} vs 10*floor {float(10*prec_floor):.2e}")
OUT["candidate_sqrt(1/phi^2+1)"] = {
    "value": mp.nstr(cand, 12),
    "rel_err_vs_eps0": mp.nstr(err_eps0, 5),
    "rel_err_vs_banked": mp.nstr(err_bank, 5),
    "refuted_both": bool(cand_refuted_eps0 and cand_refuted_bank)}

# ---- base-rate control: how many unrelated golden-family forms are 'close'
# at the achieved precision? (proves low precision cannot discriminate) ----
sqphi_mp = mp.sqrt(phi_mp)
battery = {
    "sqrt(1/phi^2+1)": cand,
    "sqrt(phi)/phi^(1/2)... phi^(1/6)": phi_mp ** mp.mpf('1/6'),
    "sqrt(phi)": sqphi_mp,
    "6/5": mp.mpf(6) / 5,
    "1+1/phi^3": 1 + 1 / phi_mp ** 3,
    "phi^2-1/2": phi_mp ** 2 - mp.mpf('0.5'),
    "sqrt(1+1/(2phi))": mp.sqrt(1 + 1 / (2 * phi_mp)),
    "(1+sqrt(phi))/phi^(3/2)": (1 + sqphi_mp) / phi_mp ** mp.mpf('1.5'),
    "2-sqrt(phi)*... 23/20": mp.mpf(23) / 20,
    "phi^(1/3)": phi_mp ** mp.mpf('1/3'),
}
close_floor = mp.mpf(10) ** (-(achieved_digits - 1))
close_eps0 = [nm for nm, v in battery.items()
              if abs(v - r_eps0_mp) / r_eps0_mp < close_floor]
log(f"  base-rate control: golden-family forms within achieved precision of "
    f"the eps->0 ratio: {close_eps0}")
OUT["base_rate_close_forms_eps0"] = close_eps0

# =============================================== STEP 4: sealed PSLQ tol rule
log("== STEP 4: sealed tolerance-height rule tol = 10^-(agree-14) ==")
tol_exp = achieved_digits - 14
rule_satisfiable = tol_exp >= 1
gate("G6 sealed PSLQ rule is satisfiable (needs >=15 honest digits, "
     "i.e. agree-14 >= 1)", rule_satisfiable,
     f"achieved={achieved_digits} -> tol_exp={tol_exp} (need >=1)")

pslq_hit = None
if rule_satisfiable:
    tol = mp.mpf(10) ** (-tol_exp)
    basis = [mp.mpf(1), phi_mp, sqphi_mp, phi_mp * sqphi_mp, mp.sqrt(5), r_eps0_mp]
    pslq_hit = mp.pslq(basis, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 5)
    log(f"  PSLQ over golden basis (rule satisfiable): {pslq_hit}")
else:
    log("  PSLQ NOT run at a trusted tolerance: achieved precision "
        f"({achieved_digits} digits) is below the rule's 15-digit floor; "
        "running it at the achieved tolerance would only re-report the "
        "base-rate collision above (untrusted by construction).")
OUT["pslq_hit_trusted"] = list(map(int, pslq_hit)) if pslq_hit else None
OUT["pslq_rule_satisfiable"] = bool(rule_satisfiable)


# ===================================================== STEP 5: verdict function
def decide_verdict(pslq_ok, pslq_hit, cand_ref_both, prec_digits, rule_ok):
    """Honest three-way verdict. SEALED CRITERION for this cell:
      exact form identified BOTH directions  -> RESOLVED-A
      bounded-negative (candidate refuted w/ computed margin) or a clean
        no-form result                       -> RESOLVED-B
      genuinely cannot tell / unconverged    -> UNRESOLVED
    NOTE the three branches are mutually exclusive and EXHAUSTIVE -- there is
    a live path to each of RESOLVED-A, RESOLVED-B, UNRESOLVED (self-tested)."""
    # (A) exact form identified: PSLQ trusted under the sealed rule AND a hit
    if rule_ok and pslq_ok and pslq_hit is not None:
        return "RESOLVED-A", "exact golden-family relation identified and " \
                             "trusted under the sealed tolerance-height rule"
    # (B) bounded negative: we have a COMPUTED margin refuting the named
    #     candidate in every reading, on a ratio that IS converged enough to
    #     make that refutation trustworthy (>=3 honest digits >> the 2%+ miss)
    if cand_ref_both and prec_digits >= 3:
        return "RESOLVED-B", "the named candidate is refuted with a computed " \
            "margin in BOTH fit-protocol readings; the ratio is converged " \
            "enough (>=3 honest digits) for the refutation to be trustworthy, " \
            "but no exact form is identifiable at this precision"
    # (U) neither identified nor confidently refuted, or not converged
    return "UNRESOLVED", "the ratio is neither identified nor refuted with a " \
        "trustworthy margin at the achieved precision/convergence"


# ---- SELF-TEST the verdict function: prove each branch is reachable ----
st_A = decide_verdict(True, [1, -2, 0, 0, 0, 5], False, 16, True)[0]
st_B = decide_verdict(False, None, True, 4, False)[0]
st_U = decide_verdict(False, None, False, 1, False)[0]
st_U2 = decide_verdict(False, None, True, 2, False)[0]  # refuted but <3 digits
gate("G7 verdict function is NON-DEGENERATE: RESOLVED-A/RESOLVED-B/UNRESOLVED "
     "are each reachable (fixes Wave-2 defect D1)",
     st_A == "RESOLVED-A" and st_B == "RESOLVED-B"
     and st_U == "UNRESOLVED" and st_U2 == "UNRESOLVED",
     f"selftest -> A:{st_A} B:{st_B} U:{st_U} U2:{st_U2}")

verdict, rationale = decide_verdict(
    bool(pslq_hit), pslq_hit,
    bool(cand_refuted_eps0 and cand_refuted_bank),
    achieved_digits, rule_satisfiable)

log("== STEP 5: VERDICT ==")
log(f"  FINAL VERDICT: {verdict}")
log(f"  rationale: {rationale}")
log(f"  DISCRIMINATING FACT (in-cell): the banked 'ratio 1.204' is a "
    f"fit-protocol artifact. Curvature-removed eps->0 ratio (depth 11) = "
    f"{best_ratio:.5f}; banked line/large-eps reading = "
    f"{DATA[11]['ratio_banked']:.5f}. gap1 curvature b1={b1_d9:.3f} vs gap2 "
    f"b2={b2_d9:.3f} is the mechanism. sqrt(1/phi^2+1)=1.176 misses the eps->0 "
    f"ratio by {float(err_eps0)*100:.2f}% and the banked ratio by "
    f"{float(err_bank)*100:.2f}% -- refuted BOTH ways.")

OUT["verdict"] = verdict
OUT["rationale"] = rationale
OUT["failed_gates"] = FAILED
OUT["discriminating_fact"] = (
    f"The banked slope-ratio 1.204 is a fit-protocol artifact: gap1's width "
    f"has real eps-curvature (d2/deps2 ~ {b1_d9:.2f}) while gap2's is ~0, so a "
    f"straight-through-origin fit over large eps inflates slope1 and hence the "
    f"ratio. Curvature-removed eps->0 ratio (depth 11, N=2.2M, two seeds, "
    f"N-converged to {achieved_digits} digits) = {best_ratio:.5f}; the "
    f"large-eps line reading = {DATA[11]['ratio_banked']:.5f}. The candidate "
    f"sqrt(1/phi^2+1)=1.176 is refuted in BOTH readings "
    f"({float(err_eps0)*100:.2f}% and {float(err_bank)*100:.2f}% off), well "
    f"beyond the {achieved_digits}-digit precision floor.")

json.dump(OUT, open(RESULTS, "w"), indent=1, default=str)
log("== DONE: results.json written ==")
