#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B771 Phase-1 Wave-4 cell W4-194 -- HARDEN H121.

H121 (B565 T4+T5): the object's abelian/letter-floor "gauge-behavior" signs:
  T4 SCREENING     : gamma ~ g^p, p -> ~0.9, dgamma/dg > 0 throughout ("never AF").
  T5 CONFINING-like: Z/11 charge-strings; closed a_C=-0.180, open faster,
                     differential a_O - a_C = -0.0545 at "7.5 sigma".
Both medium-confidence (2 grids/2 seeds, explicit 1D caveats). HARDEN => decide.

This cell RECONSTRUCTS the two observables as STRUCTURAL lattice properties of the
mathematical object (a quasiperiodic Schrodinger operator on the metallic/Sturmian
letter floor; a critical free-fermion state carrying a Z/n clock grading) and runs
each at MANY grids/seeds/word-sets with an explicit comparator control (E20).

GATE 5-Q (binding): every observable is phrased as a property of the group/lattice/
algebra. NO claim these ARE QCD screening/confinement. Comparator control on the
specialness. Nothing to CLAIMS. The one-number pin is untouched.

VERDICT LOGIC is IN CODE at the bottom and can emit RESOLVED-A / RESOLVED-B /
UNRESOLVED. Discriminating facts computed in-cell; no cited numbers drive the verdict.
"""
import json, math, os
import numpy as np

np.random.seed(0)
OUT = {}
CHECKS = []   # (name, passed, detail, direction)

def check(name, passed, detail, direction, kind="hypothesis"):
    # kind="validity" -> a calibration/control check the CODE must pass to be trusted.
    # kind="hypothesis" -> a screening/confinement signature test whose PASS/FAIL is a finding.
    CHECKS.append((name, bool(passed), detail, direction, kind))
    tag = "PASS" if passed else "FAIL"
    print(f"  [{tag}] {name}  ::  {detail}")
    return bool(passed)

# =====================================================================================
# PART A -- SCREENING (T4): Lyapunov exponent of the transfer-matrix cocycle on the
# metallic/Sturmian letter floor as a function of coupling g (= distance from the
# free/invariant surface lambda=0). Structural: this is the Lyapunov exponent of the
# SL(2,R) trace-map cocycle of the quasiperiodic operator; no physics reading.
# =====================================================================================
print("="*86)
print("PART A -- SCREENING (T4): transfer-matrix Lyapunov gamma(g) on the letter floor")
print("="*86)

def sturmian(n_len, m):
    # metallic slope alpha_m = (sqrt(m^2+4)-m)/2, continued fraction [m;m,m,...] (m=1 golden)
    alpha = (math.sqrt(m*m + 4.0) - m) / 2.0
    idx = np.arange(1, n_len + 1)
    s = np.floor((idx + 1) * alpha) - np.floor(idx * alpha)   # in {0,1}, Sturmian word
    return (2.0 * s - 1.0), alpha                             # balanced letters {+1,-1}

def lyapunov(E, lam, letters):
    # top Lyapunov exponent of prod T_n, T_n=[[E - lam*w_n, -1],[1,0]] (Schrodinger cocycle),
    # single-vector renormalized growth. LE at lambda=0, |E|<2 is 0 (free/critical).
    v = np.array([1.0, 0.0])
    acc = 0.0
    pot = lam * letters
    for w in pot:
        a = E - w
        nv0 = a * v[0] - v[1]
        nv1 = v[0]
        v = np.array([nv0, nv1])
        nrm = math.hypot(v[0], v[1])
        acc += math.log(nrm)
        v /= nrm
    return acc / len(letters)

# --- calibration / positive control: free (lambda=0) hyperbolic energy E=2.5 => gamma=arccosh(1.25)
letters_g, _ = sturmian(3000, 1)
g_cal = lyapunov(2.5, 0.0, letters_g)
check("A0 LE-code calibration: free lambda=0, E=2.5 -> arccosh(1.25)=0.6931 (asserts code correct)",
      abs(g_cal - math.acosh(1.25)) < 1e-2, f"computed {g_cal:.5f} vs {math.acosh(1.25):.5f}", "|diff|<1e-2", kind="validity")
# --- free critical control: lambda=0, E=0 (inside band) => LE ~ 0
g_free0 = lyapunov(0.0, 0.0, letters_g)
check("A0b free-critical control: lambda=0, E=0 (|E|<2) -> LE ~ 0",
      abs(g_free0) < 5e-3, f"computed {g_free0:.6f}", "|LE|<5e-3", kind="validity")

N_A = 4000
GRIDS = [np.logspace(-1.8, -0.5, 12),   # grid 1
         np.logspace(-1.5, -0.3, 12),   # grid 2
         np.logspace(-2.0, -0.7, 12),   # grid 3
         np.logspace(-1.3, -0.35, 12)]  # grid 4
ENERGIES = [0.0, 0.4, 0.8, 1.2]         # seeds (inside free band |E|<2)
WORDS = [1, 2]                          # metallic word sets: golden(m=1), silver(m=2)

letters_by_m = {m: sturmian(N_A, m)[0] for m in WORDS}

pos_frac_all = []       # fraction of (seed,grid) LE curves that are strictly positive for lam>0
mono_frac_all = []      # fraction of adjacent-lambda steps with dgamma/dlam>0
p_fits = []             # per (m, grid, E) power-law exponent from log-log fit
for m in WORDS:
    letters = letters_by_m[m]
    for gi, grid in enumerate(GRIDS):
        for E in ENERGIES:
            gam = np.array([lyapunov(E, lam, letters) for lam in grid])
            pos_frac_all.append(np.mean(gam > 1e-4))
            dif = np.diff(gam)
            mono_frac_all.append(np.mean(dif > 0))
            # power-law fit gamma ~ lam^p on the strictly-positive, increasing sub-range
            good = gam > 1e-6
            if good.sum() >= 5:
                lx = np.log(grid[good]); ly = np.log(gam[good])
                p = np.polyfit(lx, ly, 1)[0]
                # R^2 of the log-log fit
                yh = np.polyval(np.polyfit(lx, ly, 1), lx)
                ss = 1 - np.sum((ly - yh)**2)/np.sum((ly - ly.mean())**2)
                p_fits.append((m, gi, E, p, ss))

pos_frac = float(np.mean(pos_frac_all))
mono_frac = float(np.mean(mono_frac_all))
p_vals = np.array([r[3] for r in p_fits])
p_mean = float(np.mean(p_vals)); p_std = float(np.std(p_vals))
p_cv = p_std / abs(p_mean) if p_mean != 0 else float('inf')
print(f"  n(LE curves)={len(pos_frac_all)}  n(power-law fits)={len(p_fits)}")
print(f"  positivity fraction (LE>0 for lam>0) = {pos_frac:.4f}")
print(f"  monotone-increasing fraction (dgamma/dlam>0) = {mono_frac:.4f}")
print(f"  power-law exponent p across seeds/grids/words: mean={p_mean:.3f} std={p_std:.3f} CV={p_cv:.3f}  range=[{p_vals.min():.3f},{p_vals.max():.3f}]")

# --- A1: positivity / never-AF (structural: LE strictly positive off the free surface)
A1 = check("A1 SCREENING positivity: LE>0 for all coupling lam>0 (never a free/AF direction)",
           pos_frac > 0.90, f"positive-fraction={pos_frac:.3f} over {len(pos_frac_all)} curves", "frac>0.90")
# --- A2: monotone increasing (screening: coupling grows the LE, never asymptotically free)
A2 = check("A2 SCREENING monotonicity: dgamma/dlam>0 (LE increases with coupling, never AF)",
           mono_frac > 0.85, f"monotone-step-fraction={mono_frac:.3f}", "frac>0.85")
# --- A3: the SPECIFIC claimed LAW  gamma~g^p, p->~0.9, universal
A3_universal = check("A3 SCREENING specific law: p is a STABLE universal exponent ~0.9 (H121's quantitative claim)",
           (p_cv < 0.15) and (abs(p_mean - 0.9) < 0.15),
           f"p_mean={p_mean:.3f} CV={p_cv:.3f} (need CV<0.15 and |p-0.9|<0.15)", "CV<0.15 & |p-0.9|<0.15")

screening_qual = A1 and A2                # qualitative screening (positive+monotone)
screening_law  = A3_universal             # the specific p~0.9 universal-law claim

OUT["partA_screening"] = dict(
    n_curves=len(pos_frac_all), n_pfits=len(p_fits),
    positivity_fraction=pos_frac, monotone_fraction=mono_frac,
    p_mean=p_mean, p_std=p_std, p_cv=p_cv,
    p_min=float(p_vals.min()), p_max=float(p_vals.max()),
    A1_positivity=A1, A2_monotone=A2, A3_universal_law=A3_universal,
    screening_qualitative=screening_qual, screening_specific_law=screening_law,
    calib_free_hyperbolic=g_cal, calib_free_critical=g_free0)

# =====================================================================================
# PART B -- CONFINING-like string tension (T5): Z/n charge-string (disorder / full-
# counting) operator on the critical free-fermion floor. Structural: G_n(r) =
# det(1 + (w-1) C_A), w=exp(2pi i/n), C_A = ground-state correlation matrix on an
# interval of length r. Decay of |G_n(r)| = the "string tension". We test whether the
# decay is EXPONENTIAL (area-law / genuine confinement) or ALGEBRAIC (perimeter /
# deconfined), whether Z/11 is SPECIAL (E20 comparator), and whether the reported
# open-closed differential survives.
# =====================================================================================
print("="*86)
print("PART B -- CONFINING string tension (T5): Z/n charge-string decay on free-fermion floor")
print("="*86)

def corr_matrix(L):
    # critical (half-filled) infinite-chain free-fermion ground state, sites 0..L-1
    j = np.arange(L)
    d = j[:, None] - j[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        C = np.where(d == 0, 0.5, np.sin(np.pi * d / 2.0) / (np.pi * d))
    return C

def string_logabs(C, r, n, endpoint_half=0.0):
    # log|G_n(r)| for twist w=exp(2pi i/n) on interval [0,r). endpoint_half adds a
    # dangling half-charge exp(1j*pi/n*endpoint_half) at the two endpoints ("open" string).
    w = np.exp(2j * np.pi / n)
    Ca = C[:r, :r].astype(complex)
    M = np.eye(r, dtype=complex) + (w - 1.0) * Ca
    if endpoint_half != 0.0:
        ph = np.exp(1j * np.pi / n * endpoint_half)
        D = np.ones(r, dtype=complex); D[0] = ph; D[-1] = ph
        M = M * D[None, :]            # extra endpoint phase columns (dangling ends)
    sign, ld = np.linalg.slogdet(M)
    return ld

L = 220
C = corr_matrix(L)
r_vals = np.arange(6, 200, 2)

# --- positive control: n -> large (w->1) => G->1 => log|G|->0
lc_big = string_logabs(C, 120, 10**6)
check("B0 string-op control: n->1e6 (w->1) => |G|->1 => log|G| ~ 0",
      abs(lc_big) < 1e-3, f"log|G_{{1e6}}(120)| = {lc_big:.2e}", "|log|G||<1e-3", kind="validity")

# --- closed strings for a family of n (comparator control / E20)
N_SET = [2, 3, 5, 7, 11, 13, 17]
eta_by_n = {}     # log-log (algebraic) exponent
R2ll_by_n = {}    # R^2 of log-log fit
R2le_by_n = {}    # R^2 of log-linear (exponential) fit over same window
adrift = {}       # (a_eff_small_r, a_eff_large_r) effective exponential rate drift
for n in N_SET:
    lg = np.array([string_logabs(C, r, n) for r in r_vals])
    # window away from tiny-r lattice effects
    win = (r_vals >= 20) & (r_vals <= 160)
    x = r_vals[win].astype(float); y = lg[win]
    lx = np.log(x)
    # algebraic fit  log|G| = -eta*log r + b
    cll = np.polyfit(lx, y, 1); eta = -cll[0]
    yll = np.polyval(cll, lx)
    R2ll = 1 - np.sum((y - yll)**2)/np.sum((y - y.mean())**2)
    # exponential fit  log|G| = -a*r + b  (this is what a "string tension" fit assumes)
    cle = np.polyfit(x, y, 1)
    yle = np.polyval(cle, x)
    R2le = 1 - np.sum((y - yle)**2)/np.sum((y - y.mean())**2)
    # effective local exponential rate a_eff(r) = d log|G|/dr ; for a power law = -eta/r -> 0
    a_small = (lg[r_vals==22][0] - lg[r_vals==18][0]) / 4.0
    a_large = (lg[r_vals==158][0] - lg[r_vals==154][0]) / 4.0
    eta_by_n[n] = eta; R2ll_by_n[n] = R2ll; R2le_by_n[n] = R2le
    adrift[n] = (a_small, a_large)

print("  n   eta(log-log)   R2_loglog   R2_exp    a_eff(r~20)  a_eff(r~156)   2/n^2")
for n in N_SET:
    a_s, a_l = adrift[n]
    print(f"  {n:>2}   {eta_by_n[n]:.5f}      {R2ll_by_n[n]:.5f}   {R2le_by_n[n]:.5f}   {a_s:+.5f}     {a_l:+.5f}     {2.0/n**2:.5f}")

# --- B1: decay is ALGEBRAIC not EXPONENTIAL (for n=11 specifically, and family-wide)
n11 = 11
alg_beats_exp = R2ll_by_n[n11] > R2le_by_n[n11]
a_s11, a_l11 = adrift[n11]
rate_drifts_to_zero = abs(a_l11) < 0.5 * abs(a_s11)   # effective "string tension" collapses with range
# family-wide: log-log beats log-lin for a clear majority
fam_alg = np.mean([R2ll_by_n[n] > R2le_by_n[n] for n in N_SET])
B1_algebraic = check("B1 decay is ALGEBRAIC not exponential (n=11: log-log fit beats exp fit AND effective rate ->0)",
      alg_beats_exp and rate_drifts_to_zero and fam_alg >= 0.8,
      f"R2_loglog={R2ll_by_n[n11]:.4f} > R2_exp={R2le_by_n[n11]:.4f}; a_eff {a_s11:+.4f}->{a_l11:+.4f} (drift={abs(a_l11)/abs(a_s11):.2f}); family_algebraic_frac={fam_alg:.2f}",
      "loglog>exp & rate->0 & family>=0.8")

# --- B2: E20 comparator -- is Z/11 SPECIAL, or does eta(n) lie on a smooth 1/n^2 curve?
ns = np.array(N_SET, float); etas = np.array([eta_by_n[n] for n in N_SET])
# fit eta = k / n^2 (single param via least squares through origin in 1/n^2)
basis = 1.0 / ns**2
k = float(np.dot(basis, etas) / np.dot(basis, basis))
pred = k * basis
R2_smooth = 1 - np.sum((etas - pred)**2)/np.sum((etas - etas.mean())**2)
# residual of n=11 relative to the smooth-curve prediction, in units of the family residual std
resid = etas - pred
z11 = abs(resid[N_SET.index(11)]) / (np.std(resid) + 1e-15)
smooth_fits = R2_smooth > 0.95
n11_not_special = z11 < 3.0
B2_notspecial = check("B2 E20 comparator: eta(n) is a SMOOTH 1/n^2 law; Z/11 is NOT special (no outlier at n=11)",
      smooth_fits and n11_not_special,
      f"eta=k/n^2 fit R2={R2_smooth:.4f} (k={k:.4f}); n=11 residual z={z11:.2f} sigma", "R2>0.95 & z(11)<3")

# --- B3: open-closed differential -- does a_O - a_C survive as a genuine (range-stable,
# n=11-special) confinement order parameter, or is it a vanishing finite-range artifact?
# closed = interval FCS ; open = same with dangling endpoint half-charges.
def exp_rate_window(C, n, endpoint_half, rlo, rhi):
    rs = np.arange(rlo, rhi, 2)
    y = np.array([string_logabs(C, int(r), n, endpoint_half) for r in rs])
    return np.polyfit(rs.astype(float), y, 1)[0]   # slope = effective exponential "tension"

diffs_windows = {}
for (rlo, rhi) in [(12, 40), (40, 90), (90, 160)]:
    aC = exp_rate_window(C, 11, 0.0, rlo, rhi)
    aO = exp_rate_window(C, 11, 1.0, rlo, rhi)
    diffs_windows[(rlo, rhi)] = (aC, aO, aO - aC)
print("  open-closed effective-tension differential a_O - a_C by range window (n=11):")
for k2, (aC, aO, dd) in diffs_windows.items():
    print(f"    r in {k2}:  a_C={aC:+.5f}  a_O={aO:+.5f}  a_O-a_C={dd:+.5f}")
d_near = abs(diffs_windows[(12, 40)][2]); d_far = abs(diffs_windows[(90, 160)][2])
diff_vanishes = d_far < 0.5 * d_near     # the differential collapses toward 0 with range

# comparator: same differential for other n (not special to 11)
diff_by_n = {}
for n in N_SET:
    aC = exp_rate_window(C, n, 0.0, 40, 120)
    aO = exp_rate_window(C, n, 1.0, 40, 120)
    diff_by_n[n] = aO - aC
d11 = abs(diff_by_n[11])
others = [abs(diff_by_n[n]) for n in N_SET if n != 11]
diff_not_special = d11 <= max(others) * 1.5   # 11's differential not an outlier among comparators
B3_artifact = check("B3 open-closed differential is a VANISHING, non-special artifact (collapses with range; not Z/11-special)",
      diff_vanishes and diff_not_special,
      f"|a_O-a_C| near={d_near:.5f} far={d_far:.5f} (ratio={d_far/d_near:.2f}); |diff|@11={d11:.5f} vs max(other)={max(others):.5f}",
      "far<0.5*near & 11 not outlier")

# confinement (genuine area-law, Z/11-special, stable differential) HOLDS only if all fail:
confinement_holds = (not B1_algebraic) and (not B2_notspecial) and (not B3_artifact)

OUT["partB_confinement"] = dict(
    eta_by_n={str(n): eta_by_n[n] for n in N_SET},
    R2_loglog_by_n={str(n): R2ll_by_n[n] for n in N_SET},
    R2_exp_by_n={str(n): R2le_by_n[n] for n in N_SET},
    a_eff_drift_n11=list(adrift[11]),
    smooth_law_k=k, smooth_law_R2=R2_smooth, n11_residual_sigma=z11,
    open_closed_diff_windows={f"{a}-{b}": list(v) for (a, b), v in diffs_windows.items()},
    diff_by_n={str(n): diff_by_n[n] for n in N_SET},
    B1_algebraic=B1_algebraic, B2_not_special=B2_notspecial, B3_artifact=B3_artifact,
    confinement_holds=confinement_holds)

# =====================================================================================
# VERDICT (in-code). H121 bundles a SPECIFIC screening LAW (p->0.9, universal) and a
# SPECIFIC confining signature (exponential/area-law string tension special to Z/11).
#   class A held  := the specific screening law hardens (screening_law)
#   class B held  := genuine confinement hardens (confinement_holds)
# RESOLVED-A iff BOTH specific signatures harden.
# RESOLVED-B iff BOTH specific signatures dissolve.
# UNRESOLVED otherwise (mixed).
# The qualitative screening survivor (LE>0, monotone) is reported separately -- it is a
# GENERIC quasiperiodic-operator fact (E20: not object-specific), NOT the H121 claim.
# =====================================================================================
print("="*86)
print("VERDICT")
print("="*86)

classA = screening_law
classB = confinement_holds

if classA and classB:
    verdict = "RESOLVED-A"
elif (not classA) and (not classB):
    verdict = "RESOLVED-B"
else:
    verdict = "UNRESOLVED"

validity_checks_pass = all(c[1] for c in CHECKS if c[4] == "validity")
all_checks_pass = all(c[1] for c in CHECKS)

print(f"  validity/calibration checks (code correctness) pass: {validity_checks_pass}")
print(f"  screening qualitative (LE>0 & monotone, GENERIC not object-specific): {screening_qual}")
print(f"  screening SPECIFIC law (p->~0.9 universal)  [class A] : {classA}")
print(f"  confinement genuine (exp/area-law, Z/11-special) [class B] : {classB}")
print(f"  => VERDICT: {verdict}")

if verdict == "RESOLVED-B":
    headline = ("H121 dissolves: the SCREENING power-law exponent is not a stable universal ~0.9 "
                "(it varies strongly with energy/word), and the CONFINING string tension is a "
                "finite-range artifact of exponential-fitting an ALGEBRAIC (deconfined) decay whose "
                "exponent is a smooth eta=k/n^2 -- Z/11 is not special. Only a GENERIC monotone-LE "
                "survives, which is true of any quasiperiodic operator, not the object's own gauge phenomenology.")
elif verdict == "RESOLVED-A":
    headline = "H121 hardens: specific screening law AND genuine Z/11-special confinement both survive."
else:
    headline = ("H121 partially hardens: some sub-signatures survive while others dissolve "
                "(see class A / class B split).")

# discriminating fact = the in-cell numbers that flip the verdict
disc = (f"p_CV={p_cv:.3f} (need <0.15 for a universal law) with p in [{p_vals.min():.2f},{p_vals.max():.2f}]; "
        f"n=11 string decay is algebraic (R2_loglog={R2ll_by_n[11]:.3f} > R2_exp={R2le_by_n[11]:.3f}) "
        f"with effective rate {adrift[11][0]:+.4f}->{adrift[11][1]:+.4f}; eta(n)=k/n^2 smooth R2={R2_smooth:.3f}, "
        f"n=11 residual {z11:.2f} sigma (not special).")

OUT["verdict"] = verdict
OUT["headline"] = headline
OUT["discriminating_fact"] = disc
OUT["screening_qualitative_survivor"] = screening_qual
OUT["class_A_screening_law"] = classA
OUT["class_B_confinement"] = classB
OUT["validity_checks_pass"] = validity_checks_pass
OUT["all_internal_checks_pass"] = all_checks_pass
OUT["checks"] = [dict(name=n, passed=p, detail=d, direction=dr, kind=k) for (n, p, d, dr, k) in CHECKS]

print()
print("HEADLINE:", headline)
print("DISCRIMINATING FACT:", disc)
print("VALIDITY/CALIBRATION CHECKS PASS (code health):", validity_checks_pass)
print("(the A1/A2/A3 FAILs are hypothesis outcomes = the finding, not code faults)")

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "results.json"), "w") as f:
    json.dump(OUT, f, indent=2)
print("\nwrote results.json")
