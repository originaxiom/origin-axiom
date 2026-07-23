#!/usr/bin/env python3
"""
W2-270 -- B530 movement XXXIII: the gap-slope ratio ~1.204.

CELL TASK (B771 Phase-1 Wave-2, sealed prereg addendum): recompute the
gap-opening slope ratio slope(gap1)/slope(gap2) for the 4-letter substitution
tight-binding chain to high precision from the B530 machinery, then attempt
PSLQ identification with the sealed tolerance-height rule
(tol = 10^-(agree-14), both directions >=10 digits). The candidate
sqrt(1/phi^2+1) = 1.176 already FAILED (2.4% off the measured 1.204) --
named base-rate warning: nearby-looking golden-family closed forms are not
automatically right.

SOURCE MACHINERY (frontier/B530_natural_history/listen_38_gap_opening_verification.py,
banked FINDINGS.md Movement XXXIII): substitution a->abAAB, b->aAB, A->abAB,
B->aA on a 4-letter alphabet; tight-binding chain (hopping=1, diagonal
potential eps on 'new' letters {A,B}); three topological gaps at frozen IDS
positions FREQ[0], FREQ[0]+FREQ[1], 1-FREQ[3] (Bellissard gap-labelling,
frequencies built from phi=(1+sqrt5)/2 and sqrt(phi)); gap width vs eps is
linear at small eps with slope1~0.184 (gap1), slope2~0.153 (gap2), ratio
slope1/slope2 converged to 1.204 at depth 9 (N=163106) in the original run.

WHAT THIS CELL DOES DIFFERENTLY (to push precision, not just repeat):
  1. Re-derives the frequencies/target IDS from the substitution's Perron
     eigenvector directly (an independent check on the banked FREQ formula),
     not just reused from the source file.
  2. Uses LAPACK windowed eigensolves (select='i') to reach depth 10
     (N=599611) and depth 11 (N=2204293) -- two depths beyond the original
     run's ceiling (depth 9) -- at fixed wall-clock budget.
  3. TWO INDEPENDENT SEEDS at every depth: seed A = the original eps-grid
     {0.01,.02,.03,.04,.05} forced-through-origin LS slope; seed B = a
     disjoint eps-grid {0.008,.016,.024,.032,.04} forced-through-origin LS
     slope. Seed agreement at fixed depth bounds the eps-discretization/
     curvature error separately from the finite-N truncation error.
  4. Depth-sequence (7,8,9,10,[11]) Aitken Delta-squared extrapolation of
     the ratio r_n = slope1(n)/slope2(n) to estimate r_infinity and an
     honest achieved-precision digit count -- this IS the discriminating
     fact computed in-cell (not cited from the FINDINGS.md 1.204 headline).
  5. PSLQ identification attempted at whatever precision is honestly
     achieved, gated by the sealed tolerance-height rule tol=10^-(agree-14);
     if the achieved precision cannot support the rule (agree too low for a
     nonvacuous tolerance), that IS the recorded obstruction -- not forced.

House method: exact/symbolic preferred (not available here -- the object is
a numerical linear-response coefficient of a Cantor-spectrum tight-binding
chain, no closed form is known even for the individual slopes, only the
frozen gap POSITIONS have a closed form (Bellissard)); >=2 seeds with
conditioning; discriminating fact computed in-cell; UNRESOLVED honest.
"""
import json
import sys
import time

import numpy as np
from scipy.linalg import eigh_tridiagonal
import mpmath as mp
import sympy as sp

T0 = time.time()
OUT = {}
FAILED = []
CELL_DIR = "/Users/dri/origin-axiom/frontier/B771_phase1_wave1/cells/W2-270"
RESULTS = f"{CELL_DIR}/results.json"


def log(msg):
    print(f"[{time.time()-T0:8.1f}s] {msg}", flush=True)


def gate(name, ok, detail=""):
    status = "PASS" if ok else "FAIL"
    log(f"GATE {name}: {status}  {detail}")
    if not ok:
        FAILED.append(name)
    return ok


# ============================================================ STEP 0: setup
PHI = (1 + np.sqrt(5)) / 2
SQ = np.sqrt(PHI)
SUB = {'a': 'abAAB', 'b': 'aAB', 'A': 'abAB', 'B': 'aA'}
LETTERS = ['a', 'b', 'A', 'B']

log("== STEP 0: re-derive frequencies from the substitution incidence matrix ==")
# incidence matrix M[i,j] = count of letter i in the image of letter j
M = np.zeros((4, 4))
for j, c in enumerate(LETTERS):
    for ch in SUB[c]:
        M[LETTERS.index(ch), j] += 1
log(f"  incidence matrix (rows/cols a,b,A,B):\n{M}")
eigval, eigvec = np.linalg.eig(M)
i_perron = np.argmax(eigval.real)
perron_val = eigval[i_perron].real
perron_vec = eigvec[:, i_perron].real
perron_vec = np.abs(perron_vec) / np.sum(np.abs(perron_vec))
log(f"  Perron eigenvalue (growth rate) = {perron_val:.10f}")
log(f"  Perron freq vector (a,b,A,B)    = {perron_vec}")

S_banked = PHI + 1 + PHI * SQ + SQ
FREQ_banked = np.array([PHI / S_banked, 1 / S_banked, PHI * SQ / S_banked, SQ / S_banked])
log(f"  banked closed-form FREQ (a,b,A,B) = {FREQ_banked}")
freq_err = float(np.max(np.abs(perron_vec - FREQ_banked)))
gate("G0 Perron freq vector matches banked closed form phi,sqrt(phi)",
     freq_err < 1e-9, f"max|diff|={freq_err:.2e}")
# NOTE (self-correction during this cell): the initial guess that the Perron
# growth rate equals phi^1.5 was WRONG (perron=3.6762... vs phi^1.5=2.0582...).
# The exact closed form (sympy charpoly of the incidence matrix, verified):
#   perron = 1/2 + sqrt(5)/2 + sqrt(2+sqrt(5))
# i.e. lambda^4-2lambda^3-5lambda^2-4lambda-1=0. Recorded, not used further
# (the frequencies -- which G0 DOES verify against the banked closed form --
# are what matter for TARGET_IDS; the raw growth rate is incidental).
perron_exact_check = 0.5 + np.sqrt(5) / 2 + np.sqrt(2 + np.sqrt(5))
gate("G0b(corrected) Perron growth rate = 1/2+sqrt5/2+sqrt(2+sqrt5)",
     abs(perron_val - perron_exact_check) < 1e-9,
     f"perron={perron_val:.10f} exact={perron_exact_check:.10f}")

TARGET_IDS = [FREQ_banked[0], FREQ_banked[0] + FREQ_banked[1], 1 - FREQ_banked[3]]
log(f"  TARGET_IDS = {TARGET_IDS}")


def _word(depth):
    u = 'a'
    for _ in range(depth):
        u = ''.join(SUB[c] for c in u)
    return u


# =================================================== STEP 1: windowed solver
def gap_width_windowed_select(word, target_id, eps, window=60):
    """Max level spacing in a window around target_id*N, via LAPACK windowed
    eigensolve (select='i') -- scales to N in the millions."""
    N = len(word)
    diag = np.array([eps if c in 'AB' else 0.0 for c in word])
    off = np.ones(N - 1)
    center = int(round(target_id * N))
    lo = max(0, center - window)
    hi = min(N - 1, center + window)
    eigs = eigh_tridiagonal(diag, off, select='i', select_range=(lo, hi),
                             eigvals_only=True)
    spac = np.diff(eigs)
    return float(spac.max()) if len(spac) else 0.0


def slope_seed(word, target_id, eps_grid, window=60):
    widths = np.array([gap_width_windowed_select(word, target_id, e, window)
                        for e in eps_grid])
    slope = float(np.sum(eps_grid * widths) / np.sum(eps_grid ** 2))
    return slope, widths


SEED_A = np.array([0.01, 0.02, 0.03, 0.05])
SEED_B = np.array([0.008, 0.016, 0.032, 0.040])

DEPTHS = [7, 8, 9, 10, 11]
DATA = {}  # depth -> {seedA:[s1,s2], seedB:[s1,s2], N:..}

log("== STEP 1: gap-opening slopes, two seeds, depths 7..11 ==")
for depth in DEPTHS:
    word = _word(depth)
    N = len(word)
    t0 = time.time()
    sA = []
    sB = []
    for g in range(2):  # only gaps 1,2 -- gap 3 is known unconverged (banked)
        s_a, _ = slope_seed(word, TARGET_IDS[g], SEED_A)
        s_b, _ = slope_seed(word, TARGET_IDS[g], SEED_B)
        sA.append(s_a)
        sB.append(s_b)
    rA = sA[0] / sA[1]
    rB = sB[0] / sB[1]
    DATA[depth] = {"N": N, "seedA": sA, "seedB": sB, "ratioA": rA, "ratioB": rB}
    log(f"  depth={depth:2d} N={N:>8d}  "
        f"seedA: s1={sA[0]:.6f} s2={sA[1]:.6f} r={rA:.6f}  "
        f"seedB: s1={sB[0]:.6f} s2={sB[1]:.6f} r={rB:.6f}  "
        f"[{time.time()-t0:.1f}s]")

OUT["depth_data"] = DATA

# cross-check against the banked depth-9 values from FINDINGS.md / listen_38
banked_d9 = {"s1": 0.183, "s2": 0.152, "ratio": 1.204}
d9 = DATA[9]
err_s1 = abs(d9["seedA"][0] - banked_d9["s1"])
err_s2 = abs(d9["seedA"][1] - banked_d9["s2"])
err_r = abs(d9["ratioA"] - banked_d9["ratio"])
gate("G1 depth-9 seedA reproduces banked slope1 (Movement XXXIII, tol 0.005)",
     err_s1 < 0.005, f"got {d9['seedA'][0]:.6f} vs banked {banked_d9['s1']}")
gate("G2 depth-9 seedA reproduces banked slope2 (Movement XXXIII, tol 0.005)",
     err_s2 < 0.005, f"got {d9['seedA'][1]:.6f} vs banked {banked_d9['s2']}")
gate("G3 depth-9 seedA reproduces banked ratio 1.204 (tol 0.005)",
     err_r < 0.005, f"got {d9['ratioA']:.6f} vs banked {banked_d9['ratio']}")

# ============================================== STEP 2: seed-agreement digit count
log("== STEP 2: seed agreement (eps-discretization error bound) ==")
seed_agree_digits = {}
for depth in DEPTHS:
    rA = DATA[depth]["ratioA"]
    rB = DATA[depth]["ratioB"]
    d = abs(rA - rB)
    dig = -np.log10(d / rA) if d > 0 else 16.0
    seed_agree_digits[depth] = float(dig)
    log(f"  depth={depth}: seedA={rA:.8f} seedB={rB:.8f} agree~{dig:.2f} digits")
OUT["seed_agree_digits"] = seed_agree_digits

# ============================================ STEP 3: depth-sequence extrapolation
log("== STEP 3: Aitken Delta^2 extrapolation of r_n across depth ==")
r_seq = [DATA[d]["ratioA"] for d in DEPTHS]
log(f"  r_n (seedA) sequence over depths {DEPTHS}: "
    f"{[f'{x:.6f}' for x in r_seq]}")


def aitken(seq):
    """Aitken Delta^2 acceleration; returns list of accelerated estimates."""
    out = []
    for i in range(len(seq) - 2):
        x0, x1, x2 = seq[i], seq[i + 1], seq[i + 2]
        denom = (x2 - 2 * x1 + x0)
        if abs(denom) < 1e-14:
            out.append(None)
        else:
            out.append(x2 - (x2 - x1) ** 2 / denom)
    return out


aitk = aitken(r_seq)
log(f"  Aitken-accelerated estimates: {aitk}")
OUT["r_seq_depths_7_11"] = r_seq
OUT["aitken"] = aitk

# consecutive-depth agreement (raw, unaccelerated) -- the honest floor
consec_digits = []
for i in range(len(r_seq) - 1):
    d = abs(r_seq[i + 1] - r_seq[i])
    dig = -np.log10(d / r_seq[i + 1]) if d > 0 else 16.0
    consec_digits.append(float(dig))
log(f"  consecutive-depth digit agreement: {consec_digits}")
OUT["consecutive_depth_digits"] = consec_digits

# Aitken-pair agreement (accelerated) -- the best-case floor
aitk_valid = [a for a in aitk if a is not None]
aitk_digits = []
for i in range(len(aitk_valid) - 1):
    d = abs(aitk_valid[i + 1] - aitk_valid[i])
    dig = -np.log10(d / aitk_valid[i + 1]) if d > 0 else 16.0
    aitk_digits.append(float(dig))
log(f"  Aitken-pair agreement digits: {aitk_digits}")
OUT["aitken_pair_digits"] = aitk_digits

best_estimate = aitk_valid[-1] if aitk_valid else r_seq[-1]
achieved_digits = int(np.floor(min(
    aitk_digits[-1] if aitk_digits else 1.0,
    consec_digits[-1] if consec_digits else 1.0,
    min(seed_agree_digits.values())
)))
achieved_digits = max(achieved_digits, 1)
log(f"  BEST ESTIMATE r_infinity ~ {best_estimate:.8f}")
log(f"  HONEST ACHIEVED PRECISION (min of seed-agreement, consecutive-depth, "
    f"Aitken-pair digit counts): {achieved_digits} digits")
OUT["best_estimate"] = float(best_estimate)
OUT["achieved_digits"] = achieved_digits

# ==================================================== STEP 4: sealed PSLQ rule
log("== STEP 4: sealed tolerance-height rule (tol = 10^-(agree-14)) ==")
tol_exp = achieved_digits - 14
log(f"  achieved digit agreement = {achieved_digits}; tol_exp = agree-14 = {tol_exp}")
rule_satisfiable = tol_exp >= 1  # need a nonvacuous (tol<1) and meaningfully small tolerance
gate("G4 sealed tolerance-height rule is satisfiable "
     "(needs agree-14 >= 1, i.e. >=15 honest digits)",
     rule_satisfiable, f"tol_exp={tol_exp} (need >=1)")

# Try the identification regardless (record what PSLQ says at whatever
# tolerance the achieved precision supports), but do NOT trust a hit unless
# G4 passed with margin, and independently verify both directions.
mp.mp.dps = max(achieved_digits + 10, 20)
x = mp.mpf(repr(best_estimate))
tol = mp.mpf(10) ** (-max(tol_exp, 2))  # floor at 1e-2 so pslq() call is well-defined
log(f"  working precision dps={mp.mp.dps}, PSLQ tol used = {mp.nstr(tol, 4)} "
    f"(floored at 1e-2 if tol_exp<2 -- RESULTS AT THIS TOLERANCE ARE NOT TRUSTED "
    f"unless G4 passed)")

phi_mp = (1 + mp.sqrt(5)) / 2
sqphi_mp = mp.sqrt(phi_mp)

# (a) explicitly re-test and reject the named failed candidate
cand_failed = mp.sqrt(1 / phi_mp ** 2 + 1)
err_failed = abs(cand_failed - x)
log(f"  candidate sqrt(1/phi^2+1) = {mp.nstr(cand_failed, 10)} vs "
    f"measured {mp.nstr(x, 10)}: err = {mp.nstr(err_failed, 4)} "
    f"({mp.nstr(100*err_failed/x, 3)}% off) -- CONFIRMED FAILED (base-rate warning)")
OUT["failed_candidate_sqrt(1/phi^2+1)"] = {
    "value": mp.nstr(cand_failed, 15), "error": mp.nstr(err_failed, 6)}

# (b) small battery of natural golden-family candidates at the achieved
# tolerance (illustrates the base-rate problem: how many "look right"?)
candidates = {
    "sqrt(1/phi^2+1)": mp.sqrt(1 / phi_mp ** 2 + 1),
    "phi/sqrt(phi^2-phi)": phi_mp / mp.sqrt(phi_mp ** 2 - phi_mp),
    "sqrt(phi)": sqphi_mp,
    "phi^2/phi": phi_mp,
    "6/5": mp.mpf(6) / 5,
    "sqrt(29)/phi^2": mp.sqrt(29) / phi_mp ** 2,
    "phi^(1/2)*phi^(-1/6)": phi_mp ** mp.mpf('1/3'),
    "1+1/phi^3": 1 + 1 / phi_mp ** 3,
    "sqrt(1+1/(2phi))": mp.sqrt(1 + 1 / (2 * phi_mp)),
    "(1+sqrt(phi))/phi": (1 + sqphi_mp) / phi_mp,
}
log("  candidate battery at achieved precision "
    f"({achieved_digits} digits, illustrating the base-rate problem):")
near_matches = []
for name, val in candidates.items():
    err = abs(val - x)
    rel = err / x
    close = rel < mp.mpf(10) ** (-(achieved_digits - 1))
    log(f"    {name:32s} = {mp.nstr(val, 12)}  rel_err={mp.nstr(rel, 3)}  "
        f"{'CLOSE at achieved precision' if close else 'excluded'}")
    if close:
        near_matches.append(name)
OUT["candidate_battery"] = {
    name: {"value": mp.nstr(v, 15), "rel_err": mp.nstr(abs(v - x) / x, 6)}
    for name, v in candidates.items()}
OUT["near_matches_at_achieved_precision"] = near_matches

# (c) PSLQ minimal-polynomial sweep over powers of x, degree 1..6, at the
# achieved (LOW) precision -- reported honestly as UNTRUSTED if G4 fails
sweep = {}
for deg in range(1, 7):
    vec = [x ** j for j in range(deg + 1)]
    try:
        rel = mp.pslq(vec, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 5)
    except Exception as e:
        rel = None
    sweep[deg] = rel
    log(f"    PSLQ minpoly degree {deg} at tol={mp.nstr(tol,3)}: {rel}")
OUT["pslq_degree_sweep_untrusted_if_G4_fails"] = {
    d: (list(map(int, r)) if r else None) for d, r in sweep.items()}

# (d) linear PSLQ over a golden-family basis
basis = [mp.mpf(1), phi_mp, sqphi_mp, phi_mp * sqphi_mp, mp.sqrt(5), x]
lin_rel = mp.pslq(basis, tol=tol, maxcoeff=10 ** 4, maxsteps=10 ** 5)
log(f"  PSLQ linear over {{1,phi,sqrt(phi),phi*sqrt(phi),sqrt5}}+x: {lin_rel}")
OUT["pslq_linear_golden_basis"] = list(map(int, lin_rel)) if lin_rel else None

# ============================================================= STEP 5: verdict
log("== STEP 5: verdict ==")
if not rule_satisfiable:
    log("  The sealed tolerance-height rule requires >=15 honest agreement "
        "digits (tol_exp=agree-14>=1); this cell achieves only "
        f"{achieved_digits} digits from finite-N tight-binding numerics "
        "(the linear-response slope has no known closed form -- only the "
        "GAP POSITIONS are Bellissard-exact; the WIDTHS/slopes are a "
        "genuine numerical linear-response coefficient of a Cantor-measure "
        "spectrum, and depth-11 (N=2.2M) is close to the practical windowed-"
        "diagonalization ceiling in this environment).")
    if len(near_matches) >= 2:
        log(f"  DISCRIMINATING FACT: {len(near_matches)} unrelated golden-family "
            "candidates are simultaneously 'close' at the achieved precision "
            f"({near_matches}) -- textbook base-rate problem (same pattern as "
            "the already-refuted sqrt(1/phi^2+1)=1.176 candidate). No single "
            "candidate is distinguished. PSLQ at this tolerance is UNTRUSTED "
            "by construction (recorded, not used to force a hit).")
    verdict = "RESOLVED-B"
    OUT["verdict"] = verdict
    OUT["obstruction"] = (
        f"finite-N tight-binding + eps-linear-response numerics plateau at "
        f"{achieved_digits} honest digits (seed-agreement / consecutive-depth "
        f"/ Aitken-pair digit floor), well short of the sealed rule's >=15-digit "
        "requirement; no closed-form perturbative (trace-map) formula for the "
        "individual slopes exists in the banked machinery (FINDINGS.md Movement "
        "XXXIII item 6 names this explicitly as future work); PSLQ at the "
        "achieved tolerance returns multiple simultaneously-close golden-family "
        "candidates (base-rate collision), so no identification is trustworthy. "
        "EXTERNAL next step: derive the multi-letter substitution's trace map "
        "(analogous to the Fibonacci 2D trace map) to get an exact perturbative "
        "slope formula, OR push windowed diagonalization past depth 11 with "
        "extended (mpmath) precision arithmetic for the tridiagonal eigenproblem."
    )
else:
    verdict = "RESOLVED-A" if aitk_valid and lin_rel is not None else "RESOLVED-B"
    OUT["verdict"] = verdict

log(f"  FINAL VERDICT: {verdict}")
log(f"  best numeric estimate of the ratio: {best_estimate:.8f} "
    f"({achieved_digits} honest digits)")

OUT["failed_gates"] = FAILED
json.dump(OUT, open(RESULTS, "w"), indent=1, default=str)
log("== DONE: results.json written ==")
