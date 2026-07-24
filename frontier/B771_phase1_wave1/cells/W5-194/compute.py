#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B771 Phase-1 Wave-5 cell W5-194 -- remove W4-194's vacuous B3, re-confirm
H121-dissolves on the NON-vacuous legs (B1 algebraic + a 2-grid/2-seed
hardening sweep of B1/B2), per Wave-5 addendum 6141775b.

WHY B3 WAS VACUOUS (algebra, not a re-run of the numerics):
  string_logabs(C, r, n, endpoint_half) forms
      M_closed = I + (w-1) C_A                         (w = e^{2 pi i / n})
      M_open   = M_closed @ diag(D),  D_0 = D_{r-1} = e^{i pi / n},  D_else = 1
  Right-multiplying by a diagonal scales det by det(diag(D)) = D_0 * D_{r-1}
  = e^{i 2 pi / n}, a UNIT-MODULUS scalar, for every r and every n. Hence
      log|G_open(r)| = log|det M_open| = log|det M_closed| + log|e^{i2pi/n}|
                      = log|G_closed(r)| + 0   identically.
  a_O - a_C is therefore 0 by construction (W4-194 measured it at 1e-18,
  i.e. floating-point noise around an exact algebraic identity) -- it can
  never fail, so it certified nothing about confinement. Removed below;
  the algebraic identity is checked once, printed for the record, and is
  NOT a verdict input (no comment-only diagnostics, no tautological
  self-test masquerading as a hypothesis check).

REMAINING (non-vacuous) H121-T5 legs, both retained/hardened:
  B1 -- decay is ALGEBRAIC not exponential (log-log beats log-lin fit;
        effective local rate -> 0 with range).
  B2 -- E20 comparator: eta(n) lies on a smooth k/n^2 law; Z/11 is not an
        outlier.
These are re-run over a 2-grid (lattice size L) x 2-seed (Fermi momentum
k_F, i.e. filling fraction) hardening sweep = 4 independent legs, each
producing its own B1/B2 pass/fail. House method: UNSTABLE (legs disagree)
beats a forced verdict.

B772 lesson check: G_n(r) is a twisted-determinant "character-like"
quantity graded by n; the N_SET below already mixes even (n=2) and odd
(n=3,5,7,11,13,17) n, per-n (not summed/traced over n), so an even/odd
cancellation could not hide inside any single n's result.

GATE 5-Q (binding): structural lattice-operator language only (quasiperiodic
Schrodinger cocycle, free-fermion twisted determinant). No QCD claim.
Nothing to CLAIMS. Verdict logic is in code, can emit UNRESOLVED.
"""
import json, math, os
import numpy as np

np.random.seed(0)
OUT = {}
CHECKS = []

def check(name, passed, detail, direction, kind="hypothesis"):
    CHECKS.append((name, bool(passed), detail, direction, kind))
    tag = "PASS" if passed else "FAIL"
    print(f"  [{tag}] {name}  ::  {detail}")
    return bool(passed)

# =====================================================================================
# PART A -- SCREENING (T4), unchanged from W4-194 (not implicated by the B3 removal;
# re-run in-cell so the verdict is self-contained, not cited from the prior cell).
# =====================================================================================
print("="*86)
print("PART A -- SCREENING (T4): transfer-matrix Lyapunov gamma(g) on the letter floor")
print("="*86)

def sturmian(n_len, m):
    alpha = (math.sqrt(m*m + 4.0) - m) / 2.0
    idx = np.arange(1, n_len + 1)
    s = np.floor((idx + 1) * alpha) - np.floor(idx * alpha)
    return (2.0 * s - 1.0), alpha

def lyapunov(E, lam, letters):
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

letters_g, _ = sturmian(3000, 1)
g_cal = lyapunov(2.5, 0.0, letters_g)
check("A0 LE-code calibration: free lambda=0, E=2.5 -> arccosh(1.25)=0.6931 (asserts code correct)",
      abs(g_cal - math.acosh(1.25)) < 1e-2, f"computed {g_cal:.5f} vs {math.acosh(1.25):.5f}", "|diff|<1e-2", kind="validity")
g_free0 = lyapunov(0.0, 0.0, letters_g)
check("A0b free-critical control: lambda=0, E=0 (|E|<2) -> LE ~ 0",
      abs(g_free0) < 5e-3, f"computed {g_free0:.6f}", "|LE|<5e-3", kind="validity")

GRIDS = [np.logspace(-1.8, -0.5, 12),
         np.logspace(-1.5, -0.3, 12),
         np.logspace(-2.0, -0.7, 12),
         np.logspace(-1.3, -0.35, 12)]
ENERGIES = [0.0, 0.4, 0.8, 1.2]
WORDS = [1, 2]
N_A = 4000
letters_by_m = {m: sturmian(N_A, m)[0] for m in WORDS}

pos_frac_all, mono_frac_all, p_fits = [], [], []
for m in WORDS:
    letters = letters_by_m[m]
    for gi, grid in enumerate(GRIDS):
        for E in ENERGIES:
            gam = np.array([lyapunov(E, lam, letters) for lam in grid])
            pos_frac_all.append(np.mean(gam > 1e-4))
            dif = np.diff(gam)
            mono_frac_all.append(np.mean(dif > 0))
            good = gam > 1e-6
            if good.sum() >= 5:
                lx = np.log(grid[good]); ly = np.log(gam[good])
                p = np.polyfit(lx, ly, 1)[0]
                p_fits.append((m, gi, E, p))

pos_frac = float(np.mean(pos_frac_all))
mono_frac = float(np.mean(mono_frac_all))
p_vals = np.array([r[3] for r in p_fits])
p_mean = float(np.mean(p_vals)); p_std = float(np.std(p_vals))
p_cv = p_std / abs(p_mean) if p_mean != 0 else float('inf')
print(f"  n(LE curves)={len(pos_frac_all)}  n(power-law fits)={len(p_fits)}")
print(f"  positivity fraction = {pos_frac:.4f}  monotone fraction = {mono_frac:.4f}")
print(f"  power-law exponent p: mean={p_mean:.3f} CV={p_cv:.3f} range=[{p_vals.min():.3f},{p_vals.max():.3f}]")

A1 = check("A1 SCREENING positivity: LE>0 for all coupling lam>0 (never a free/AF direction)",
           pos_frac > 0.90, f"positive-fraction={pos_frac:.3f} over {len(pos_frac_all)} curves", "frac>0.90")
A2 = check("A2 SCREENING monotonicity: dgamma/dlam>0",
           mono_frac > 0.85, f"monotone-step-fraction={mono_frac:.3f}", "frac>0.85")
A3_universal = check("A3 SCREENING specific law: p is a STABLE universal exponent ~0.9",
           (p_cv < 0.15) and (abs(p_mean - 0.9) < 0.15),
           f"p_mean={p_mean:.3f} CV={p_cv:.3f}", "CV<0.15 & |p-0.9|<0.15")

screening_qual = A1 and A2
screening_law = A3_universal

OUT["partA_screening"] = dict(
    n_curves=len(pos_frac_all), n_pfits=len(p_fits),
    positivity_fraction=pos_frac, monotone_fraction=mono_frac,
    p_mean=p_mean, p_std=p_std, p_cv=p_cv,
    p_min=float(p_vals.min()), p_max=float(p_vals.max()),
    A1_positivity=A1, A2_monotone=A2, A3_universal_law=A3_universal,
    screening_qualitative=screening_qual, screening_specific_law=screening_law)

# =====================================================================================
# PART B -- CONFINING-like string tension (T5). B3 REMOVED. B1 + B2 re-run over a
# 2-grid (lattice size L) x 2-seed (Fermi momentum k_F / filling) hardening sweep.
# =====================================================================================
print("="*86)
print("PART B -- CONFINING string tension (T5): B1+B2 ONLY (B3 removed, vacuous by construction)")
print("="*86)

def corr_matrix(L, kF):
    # free-fermion ground state at filling kF/pi (kF=pi/2 -> half filling, the W4-194 case)
    j = np.arange(L)
    d = j[:, None] - j[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        C = np.where(d == 0, kF / np.pi, np.sin(kF * d) / (np.pi * d))
    return C

def string_logabs(C, r, n):
    w = np.exp(2j * np.pi / n)
    Ca = C[:r, :r].astype(complex)
    M = np.eye(r, dtype=complex) + (w - 1.0) * Ca
    sign, ld = np.linalg.slogdet(M)
    return ld

# --- documentation-only algebraic check of WHY B3 was vacuous (not a verdict input) ---
def string_logabs_open(C, r, n, endpoint_half=1.0):
    w = np.exp(2j * np.pi / n)
    Ca = C[:r, :r].astype(complex)
    M = np.eye(r, dtype=complex) + (w - 1.0) * Ca
    ph = np.exp(1j * np.pi / n * endpoint_half)
    D = np.ones(r, dtype=complex); D[0] = ph; D[-1] = ph
    M = M * D[None, :]
    sign, ld = np.linalg.slogdet(M)
    return ld

_Cdoc = corr_matrix(220, math.pi / 2.0)
_closed_doc = string_logabs(_Cdoc, 90, 11)
_open_doc = string_logabs_open(_Cdoc, 90, 11)
print(f"  [DOC, not a check] B3-vacuity algebra: log|G_closed(90)|={_closed_doc:.10f}  "
      f"log|G_open(90)|={_open_doc:.10f}  diff={_open_doc-_closed_doc:.3e}  "
      f"(predicted exactly 0 since diag(D) has unit-modulus determinant e^(i2pi/11); "
      f"B3 measured this identity, not a physical differential -- REMOVED from the verdict)")

# --- 2-grid x 2-seed hardening sweep ---
GRID_LS = [220, 320]                 # 2 grids: lattice size
SEED_KFS = [math.pi / 2.0, math.pi / 3.0]   # 2 seeds: half-filling (as W4-194) and 1/3-filling
N_SET = [2, 3, 5, 7, 11, 13, 17]     # mixes even (2) and odd n -- B772 parity check satisfied

legs = []
for L in GRID_LS:
    for kF in SEED_KFS:
        C = corr_matrix(L, kF)

        # validity control: n -> large (w->1) => |G|->1 => log|G|->0, for THIS leg's C
        lc_big = string_logabs(C, min(120, L - 40), 10**6)
        v_ok = bool(abs(lc_big) < 1e-3)
        check(f"B0 [L={L},kF={kF:.4f}] string-op control: n->1e6 => log|G|~0",
              v_ok, f"log|G_1e6|={lc_big:.2e}", "|log|G||<1e-3", kind="validity")

        r_max = L - 60
        r_vals = np.arange(6, r_max, 2)
        win = (r_vals >= 20) & (r_vals <= r_max)
        x = r_vals[win].astype(float)

        eta_by_n, R2ll_by_n, R2le_by_n, adrift = {}, {}, {}, {}
        for n in N_SET:
            lg = np.array([string_logabs(C, int(r), n) for r in r_vals])
            y = lg[win]
            lx = np.log(x)
            cll = np.polyfit(lx, y, 1); eta = -cll[0]
            yll = np.polyval(cll, lx)
            R2ll = 1 - np.sum((y - yll)**2) / np.sum((y - y.mean())**2)
            cle = np.polyfit(x, y, 1)
            yle = np.polyval(cle, x)
            R2le = 1 - np.sum((y - yle)**2) / np.sum((y - y.mean())**2)
            a_small = (y[1] - y[0]) / (x[1] - x[0])
            a_large = (y[-1] - y[-2]) / (x[-1] - x[-2])
            eta_by_n[n] = float(eta); R2ll_by_n[n] = float(R2ll); R2le_by_n[n] = float(R2le)
            adrift[n] = (float(a_small), float(a_large))

        n11 = 11
        alg_beats_exp = R2ll_by_n[n11] > R2le_by_n[n11]
        a_s11, a_l11 = adrift[n11]
        rate_drifts_to_zero = abs(a_l11) < 0.5 * abs(a_s11)
        fam_alg = float(np.mean([R2ll_by_n[n] > R2le_by_n[n] for n in N_SET]))
        B1_pass = bool(alg_beats_exp and rate_drifts_to_zero and fam_alg >= 0.8)
        check(f"B1 [L={L},kF={kF:.4f}] decay ALGEBRAIC not exponential (n=11)",
              B1_pass,
              f"R2_loglog={R2ll_by_n[n11]:.4f}>R2_exp={R2le_by_n[n11]:.4f}; "
              f"a_eff {a_s11:+.5f}->{a_l11:+.5f}; family_alg_frac={fam_alg:.2f}",
              "loglog>exp & rate->0 & family>=0.8")

        ns = np.array(N_SET, float); etas = np.array([eta_by_n[n] for n in N_SET])
        basis = 1.0 / ns**2
        k = float(np.dot(basis, etas) / np.dot(basis, basis))
        pred = k * basis
        R2_smooth = 1 - np.sum((etas - pred)**2) / np.sum((etas - etas.mean())**2)
        resid = etas - pred
        z11 = abs(resid[N_SET.index(11)]) / (np.std(resid) + 1e-15)
        B2_pass = bool((R2_smooth > 0.95) and (z11 < 3.0))
        check(f"B2 [L={L},kF={kF:.4f}] E20 comparator: eta(n)=k/n^2 smooth, Z/11 not special",
              B2_pass, f"R2={R2_smooth:.4f} k={k:.4f}; n11 residual z={z11:.2f} sigma",
              "R2>0.95 & z(11)<3")

        legs.append(dict(L=L, kF=kF, eta_by_n=eta_by_n, R2ll_by_n=R2ll_by_n, R2le_by_n=R2le_by_n,
                          adrift_n11=list(adrift[11]), B1_pass=B1_pass, B2_pass=B2_pass,
                          smooth_law_k=k, smooth_law_R2=R2_smooth, n11_residual_sigma=z11,
                          validity_ok=v_ok))

B1_per_leg = [l["B1_pass"] for l in legs]
B2_per_leg = [l["B2_pass"] for l in legs]
B1_stable = len(set(B1_per_leg)) == 1
B2_stable = len(set(B2_per_leg)) == 1
B1_algebraic_agg = B1_per_leg[0] if B1_stable else None   # None = UNSTABLE
B2_notspecial_agg = B2_per_leg[0] if B2_stable else None

print(f"  B1 across {len(legs)} legs (2 grids x 2 seeds): {B1_per_leg}  stable={B1_stable}")
print(f"  B2 across {len(legs)} legs (2 grids x 2 seeds): {B2_per_leg}  stable={B2_stable}")

# genuine confinement holds only if BOTH legs are stable AND both dissolution-evidence
# checks FAIL everywhere (i.e. decay is exponential & Z/11 IS special, robustly).
# If either leg is unstable across the grid/seed sweep, house method: UNSTABLE, not forced.
if (not B1_stable) or (not B2_stable):
    confinement_status = "UNSTABLE"
    confinement_holds = False   # cannot claim genuine confinement on unstable evidence either
else:
    confinement_status = "STABLE"
    confinement_holds = (not B1_algebraic_agg) and (not B2_notspecial_agg)

OUT["partB_confinement"] = dict(
    legs=legs,
    B1_per_leg=B1_per_leg, B2_per_leg=B2_per_leg,
    B1_stable=B1_stable, B2_stable=B2_stable,
    B1_algebraic_agg=B1_algebraic_agg, B2_notspecial_agg=B2_notspecial_agg,
    confinement_status=confinement_status, confinement_holds=confinement_holds,
    B3_removed=True,
    B3_removal_reason=("open-closed differential multiplies det() by a column-diagonal whose "
                        "determinant is a fixed unit-modulus phase e^(i2pi/n); log|G_open|="
                        "log|G_closed| identically for all r,n -- vacuous by construction, verified "
                        f"in-cell to {abs(_open_doc-_closed_doc):.2e} (float noise around an exact "
                        "algebraic identity), never entered the verdict below."))

# =====================================================================================
# VERDICT (in-code). Same class-A/class-B structure as W4-194, with class B now built
# ONLY from the non-vacuous B1+B2 legs (B3 removed).
#   class A held := screening_law (p->0.9 universal) hardens
#   class B held := confinement_holds (genuine, stable exp/area-law + Z/11-special) hardens
# SEALED CRITERION: dissolves-negative holds (RESOLVED-B) iff it survives on the
# non-vacuous evidence; if B1/B2 do not reproduce stably across the hardening sweep,
# re-open (UNRESOLVED) rather than force the prior verdict.
# =====================================================================================
print("="*86)
print("VERDICT")
print("="*86)

classA = screening_law
classB = confinement_holds

if not (B1_stable and B2_stable):
    verdict = "UNRESOLVED"
elif classA and classB:
    verdict = "RESOLVED-A"
elif (not classA) and (not classB):
    verdict = "RESOLVED-B"
else:
    verdict = "UNRESOLVED"

validity_checks_pass = all(c[1] for c in CHECKS if c[4] == "validity")
all_checks_pass = all(c[1] for c in CHECKS)

print(f"  validity/calibration checks pass: {validity_checks_pass}")
print(f"  screening qualitative (generic, not object-specific): {screening_qual}")
print(f"  screening SPECIFIC law [class A]: {classA}")
print(f"  confinement genuine, non-vacuous legs only [class B]: {classB}  (status={confinement_status})")
print(f"  => VERDICT: {verdict}")

if verdict == "RESOLVED-B":
    headline = ("W4-194's H121-dissolves negative SURVIVES B3 removal: with the vacuous "
                "open-closed differential (identically zero by unit-modulus-determinant "
                "construction) stripped out, the confining signature still dissolves on B1 "
                "(n=11 string decay is ALGEBRAIC not exponential, effective rate -> 0) and B2 "
                "(eta(n)=k/n^2 smooth, Z/11 not special), reproduced STABLY across a 2-grid "
                "(L=220,320) x 2-seed (k_F=pi/2,pi/3) hardening sweep (4/4 legs agree on both). "
                "The screening law (p->0.9 universal) independently dissolves as in W4-194. "
                "H121 remains dissolved: gauge-signatures do not survive as object-specific "
                "structural facts.")
elif verdict == "RESOLVED-A":
    headline = "H121 hardens after B3 removal: screening law AND genuine stable confinement both survive."
else:
    headline = (f"After B3 removal, the negative does NOT reproduce cleanly: "
                f"B1_stable={B1_stable} B2_stable={B2_stable} classA={classA} classB={classB} "
                f"(status={confinement_status}) -- re-opened per sealed criterion.")

disc = (f"p_CV={p_cv:.3f} (need <0.15) with p in [{p_vals.min():.2f},{p_vals.max():.2f}] => class A dissolves; "
        f"B1 algebraic-decay verdict across 4 legs (L in {GRID_LS}, kF in "
        f"[{SEED_KFS[0]:.4f},{SEED_KFS[1]:.4f}]) = {B1_per_leg} (stable={B1_stable}); "
        f"B2 not-special verdict across same 4 legs = {B2_per_leg} (stable={B2_stable}); "
        f"B3 (open-closed differential) proven identically 0 by unit-modulus-determinant "
        f"algebra ({abs(_open_doc-_closed_doc):.2e} residual) and REMOVED from the verdict.")

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

here = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(here, "results.json"), "w") as f:
    json.dump(OUT, f, indent=2)
print("\nwrote results.json")
