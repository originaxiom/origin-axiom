#!/usr/bin/env python3
"""GAUDIN CLOSURE (named follow-up of C4b/superposition, B1151 arc): replace
the Wigner-SURMISE approximation with the EXACT GUE nearest-neighbor spacing
law (the Gaudin/Mehta distribution) and re-run the per-factor and merged KS
tests on the same banked data (2469 zeta + 2991 L(chi_-3) zeros to T=3000,
same unfolding conventions as c4b_superposition.py) to see whether the
per-factor residual (D=0.0401/0.0487 vs the Wigner surmise) was surmise
error, as C4b hypothesized, or a real deviation.

THE EXACT LAW (Bornemann's Nystrom/Gauss-Legendre method for Fredholm
determinants, CITED: F. Bornemann, "On the numerical evaluation of
distributions in random matrix theory: a review", Markov Processes Relat.
Fields 16 (2010) 803-866; the sine-kernel bulk-scaling limit of GUE local
eigenvalue statistics is CITED, Mehta "Random Matrices" ch.6/Dyson):
  gap probability   E(s) = det(I - K_s),  K(x,y) = sin(pi(x-y))/(pi(x-y))
  on L^2(0,s), unit mean density (K(x,x) = 1 by the removable-singularity
  limit).  Nystrom discretization: m-point Gauss-Legendre nodes/weights on
  (0,s), matrix M_ij = sqrt(w_i) K(x_i,x_j) sqrt(w_j), E(s) = det(I - M),
  computed via slogdet for numerical stability at small E(s).
  IDENTITY (CITED, Mehta ch.6): for a stationary unit-density determinantal
  process, the nearest-neighbor spacing density is p(s) = E''(s), so the
  spacing CDF is F(s) = 1 + E'(s) - E'(0) = 1 + E'(s)  (since E'(0) = -1,
  verified below as a preregistered fact, not assumed).
  2-fold superposition of independent unit-density processes with density
  fractions f1+f2=1 (same closed-form combination law as the Wigner-surmise
  cert it replaces): E_super(s) = E(f1 s) E(f2 s),
     F_super(s) = 1 + f1 E'(f1 s) E(f2 s) + f2 E(f1 s) E'(f2 s).

PREREGISTERED (two-outcome; every fact below is asserted in code):
  M1 (Nystrom convergence): E(s) at m=40 agrees with m=80 to < 1e-10 (abs)
     at s in {0.5, 1.5, 3.0} (spans the per-factor and merged spacing range).
  M2 (endpoint / normalization sanity): E(0) = 1 exactly (0-point matrix);
     spline-derivative slope at s=0 gives E'(0) = -1 to < 1e-6 (this fixes
     the additive constant in F(s) = 1 + E'(s), not assumed a priori);
     mean spacing integral( 1 - F(s) ds, 0..Smax ) = 1 to < 2e-3.
  A0 (anchors, like-for-like with the banked Wigner cert, to 1e-3):
     D_zeta = 0.0401, D_L = 0.0487 (per-factor vs Wigner surmise),
     D_merged_single = 0.13365 (merged vs single Wigner),
     D_merged_Wigner_super = 0.02400 (merged vs 2-fold WIGNER superposition).
  G1 (the claim under test): per-factor KS against the EXACT Gaudin CDF.
     EXPECTED branch: D drops below the Wigner-surmise values (0.0401/0.0487)
     AND p > 0.01 for both factors -- confirming the C4b hypothesis that the
     per-factor residual was surmise error, not a real deviation.  Otherwise
     (D does not drop / p stays small) bank the negative: a real per-factor
     deviation from GUE survives the exact law.
  G2 (merged, exact law): merged spacings vs the exact 2-fold GAUDIN
     superposition (f1=2469/5460=0.4522, f2=2991/5460=0.5478, matching C4b's
     global-count fractions exactly, not the task-prompt rounded values).
     Report D, p; compare against the banked Wigner-surmise superposition
     D=0.02400.
  C1 (control, discriminating direction, exact law): each single factor
     fits the exact single-Gaudin CDF at least as well as (not worse than)
     the exact 2-fold superposition CDF -- the superposition is not a
     universally better fitter.
Gate 5: no measured physical constants enter anywhere (pure number theory /
random-matrix statistics on committed zero data + closed-form kernel).
"""
import os
from math import log, pi
import numpy as np
from scipy.stats import kstest
from scipy.interpolate import CubicSpline

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.join(HERE, 'c4data')

# ---------------------------------------------------------------- data / unfolding
# identical logic to the banked c4b_superposition.py (same unfolding => like-for-like)
def read_zeros(fn):
    return sorted(float(x) for x in open(os.path.join(DATA, fn)) if x.strip())

zz = read_zeros('c4_zeros_zeta.txt')
zl = read_zeros('c4_zeros_L.txt')
print(f"data: {len(zz)} zeta zeros (to {zz[-1]:.2f}), {len(zl)} L(chi_-3) zeros (to {zl[-1]:.2f})")

def unfold_factor(ts, cond):
    us = []
    for a, b in zip(ts, ts[1:]):
        tm = 0.5 * (a + b)
        rho = (1 / (2 * pi)) * log(cond * tm / (2 * pi))
        if rho > 0:
            us.append((b - a) * rho)
    return np.array(us)

uz = unfold_factor(zz, 1)
ul = unfold_factor(zl, 3)
merged = sorted(zz + zl)

def rhoK(t):
    return (1 / (2 * pi)) * (log(t / (2 * pi)) + log(3 * t / (2 * pi)))

um = []
for a, b in zip(merged, merged[1:]):
    tm = 0.5 * (a + b)
    r = rhoK(tm)
    if r > 0:
        um.append((b - a) * r)
um = np.array(um)
print(f"unfolded counts: zeta={len(uz)} L={len(ul)} merged={len(um)}   "
      f"max spacings: {uz.max():.3f}/{ul.max():.3f}/{um.max():.3f}")

# ---------------------------------------------------------------- Wigner-surmise anchors (A0, like-for-like)
from math import erfc, sqrt, exp
def E_W(s): return exp(-4 * s * s / pi) - s * erfc(2 * s / sqrt(pi))
def gue_cdf_wigner(s):
    from scipy.special import erf as verf
    s = np.asarray(s, dtype=float)
    return verf(2 * s / np.sqrt(pi)) - (4 * s / pi) * np.exp(-4 * s * s / pi)

Dz_w, pz_w = kstest(uz, gue_cdf_wigner)
Dl_w, pl_w = kstest(ul, gue_cdf_wigner)
Dm_w, pm_w = kstest(um, gue_cdf_wigner)
print(f"A0: zeta vs Wigner   D={Dz_w:.4f} (bank 0.0401) p={pz_w:.3g}")
print(f"A0: L    vs Wigner   D={Dl_w:.4f} (bank 0.0487) p={pl_w:.3g}")
print(f"A0: merged vs single-Wigner D={Dm_w:.5f} (bank 0.13365) p={pm_w:.3g}")
assert abs(Dz_w - 0.0401) < 1e-3
assert abs(Dl_w - 0.0487) < 1e-3
assert abs(Dm_w - 0.13365) < 1e-3

f1 = len(zz) / (len(zz) + len(zl))
f2 = 1 - f1
print(f"density fractions (global counts): f_zeta={f1:.4f} f_L={f2:.4f}")

def E_Wp(s): return -erfc(2 * s / sqrt(pi)) - (4 * s / pi) * exp(-4 * s * s / pi)
def sup_cdf_wigner_scalar(s):
    if s <= 0: return 0.0
    return 1.0 + f1 * E_Wp(f1 * s) * E_W(f2 * s) + f2 * E_W(f1 * s) * E_Wp(f2 * s)
def sup_cdf_wigner(s):
    s = np.asarray(s, dtype=float)
    return np.array([sup_cdf_wigner_scalar(v) for v in np.atleast_1d(s)])

Dms_w, pms_w = kstest(um, sup_cdf_wigner)
print(f"A0: merged vs 2-fold WIGNER superposition  D={Dms_w:.5f} (bank 0.02400) p={pms_w:.3g}")
assert abs(Dms_w - 0.02400) < 1e-3
print("A0 anchors reproduced -- like-for-like with the banked Wigner-surmise cert.\n")

# ---------------------------------------------------------------- EXACT sine-kernel Fredholm determinant
def E_gauss(s, m):
    """E(s) = det(I - K_s) via m-point Gauss-Legendre Nystrom discretization
    of the sine kernel on (0,s).  s<=0 => E=1 (empty interval)."""
    if s <= 0:
        return 1.0
    x, w = np.polynomial.legendre.leggauss(m)
    nodes = 0.5 * s * (x + 1.0)
    weights = 0.5 * s * w
    diff = nodes[:, None] - nodes[None, :]
    with np.errstate(divide='ignore', invalid='ignore'):
        K = np.sin(np.pi * diff) / (np.pi * diff)
    np.fill_diagonal(K, 1.0)  # removable singularity: sinc(0) = 1
    sw = np.sqrt(weights)
    M = sw[:, None] * K * sw[None, :]
    sign, logdet = np.linalg.slogdet(np.eye(m) - M)
    return float(sign * np.exp(logdet))

# --- M1: Nystrom convergence, m=40 vs m=80, at sample points spanning the data range
M_MAIN = 40
sample_pts = [0.5, 1.5, 3.0]
conv = []
for s in sample_pts:
    e40 = E_gauss(s, 40)
    e80 = E_gauss(s, 80)
    conv.append(abs(e40 - e80))
print("M1: Nystrom convergence m=40 vs m=80 at s in {0.5,1.5,3.0}:",
      [f"{c:.2e}" for c in conv])
assert all(c < 1e-10 for c in conv), "Nystrom m=40 not converged to 1e-10"

# --- build E(s) on a dense grid, spline it and its derivative (Smax covers all
#     spacing values used below: raw per-factor spacings (max ~2.5) AND the
#     superposition arguments f_i * s for merged spacings (max ~3.15), so
#     f_i*s <= 0.548*3.15 ~= 1.73 < Smax comfortably)
Smax = 6.0
STEP = 0.005
grid = np.arange(0.0, Smax + 1e-9, STEP)
Evals = np.array([E_gauss(s, M_MAIN) for s in grid])
assert Evals[0] == 1.0  # M2 part a: E(0) = 1 exactly (empty 0x0 determinant)
spl = CubicSpline(grid, Evals)
dspl = spl.derivative()

Eprime0 = float(dspl(0.0))
print(f"M2: E(0)={Evals[0]:.10f} (exact 1)   E'(0)={Eprime0:.8f} (expect -1)")
assert abs(Eprime0 - (-1.0)) < 1e-6

def F_exact(s):
    """Exact Gaudin/Mehta spacing CDF F(s) = 1 + E'(s), unit mean spacing."""
    s = np.asarray(s, dtype=float)
    sc = np.clip(s, 0.0, Smax)
    out = 1.0 + dspl(sc)
    out = np.where(s >= Smax, 1.0, out)
    out = np.where(s <= 0.0, 0.0, out)
    return np.clip(out, 0.0, 1.0)

fine = np.linspace(0.0, Smax, 400001)
mean_exact = float(np.trapezoid(1.0 - F_exact(fine), fine))
print(f"M2: mean spacing (exact law) = {mean_exact:.6f} (gate: |.-1|<2e-3)")
assert abs(mean_exact - 1.0) < 2e-3
print("M1/M2 passed: Nystrom E(s) converged, normalization/mean confirmed.\n")

# ---------------------------------------------------------------- G1: per-factor, exact law
Dz, pz = kstest(uz, F_exact)
Dl, pl = kstest(ul, F_exact)
print(f"G1: zeta alone vs EXACT Gaudin  D={Dz:.4f} (Wigner was {Dz_w:.4f})  p={pz:.3g}")
print(f"G1: L    alone vs EXACT Gaudin  D={Dl:.4f} (Wigner was {Dl_w:.4f})  p={pl:.3g}")
g1_pass = (Dz < Dz_w) and (Dl < Dl_w) and (pz > 0.01) and (pl > 0.01)
print("G1 branch:", "EXPECTED (surmise error confirmed)" if g1_pass
      else "NEGATIVE (real per-factor deviation survives exact law)")

# ---------------------------------------------------------------- G2: merged, exact 2-fold Gaudin superposition
def E_exact(s):
    s = np.asarray(s, dtype=float)
    sc = np.clip(s, 0.0, Smax)
    out = spl(sc)
    out = np.where(s >= Smax, 0.0, out)
    out = np.where(s <= 0.0, 1.0, out)
    return out

def sup_cdf_exact_scalar(s):
    if s <= 0: return 0.0
    a1, a2 = f1 * s, f2 * s
    Ea1, Ea2 = float(E_exact(a1)), float(E_exact(a2))
    dEa1, dEa2 = float(dspl(np.clip(a1, 0, Smax))), float(dspl(np.clip(a2, 0, Smax)))
    dEsup = f1 * dEa1 * Ea2 + f2 * Ea1 * dEa2
    return 1.0 + dEsup

def sup_cdf_exact(s):
    s = np.asarray(s, dtype=float)
    return np.array([sup_cdf_exact_scalar(v) for v in np.atleast_1d(s)])

# sanity on the superposition model itself: CDF(0)=0, CDF(Smax)~1, unit mean
sgrid = np.linspace(0.0, Smax, 6001)
scdf = sup_cdf_exact(sgrid)
mean_sup = float(np.trapezoid(1.0 - scdf, sgrid))
print(f"G2 model sanity: sup_cdf(0)={sup_cdf_exact_scalar(0.0):.1e}, "
      f"sup_cdf({Smax})={sup_cdf_exact_scalar(Smax):.8f}, mean={mean_sup:.6f}")
assert abs(sup_cdf_exact_scalar(Smax) - 1.0) < 1e-6
assert abs(mean_sup - 1.0) < 2e-3

Dms, pms = kstest(um, sup_cdf_exact)
print(f"G2: merged vs EXACT 2-fold GAUDIN superposition  D={Dms:.5f}  p={pms:.3g}")
print(f"    (Wigner-surmise superposition was D={Dms_w:.5f}; single-Gaudin/Wigner merged D~{Dm_w:.5f})")

# ---------------------------------------------------------------- C1: control, exact law
Dz_vs_sup, _ = kstest(uz, sup_cdf_exact)
Dl_vs_sup, _ = kstest(ul, sup_cdf_exact)
print(f"C1: zeta alone vs exact-superposition D={Dz_vs_sup:.4f} (vs exact-single {Dz:.4f})")
print(f"C1: L    alone vs exact-superposition D={Dl_vs_sup:.4f} (vs exact-single {Dl:.4f})")
c1_pass = (Dz_vs_sup >= Dz) and (Dl_vs_sup >= Dl)
assert c1_pass, "control failed: a single factor fits the superposition at least as well as single-Gaudin"

# ---------------------------------------------------------------- final bank (two-outcome, honest either way)
print()
print("=" * 78)
if g1_pass:
    print("G1 RESULT: EXPECTED branch. Replacing the Wigner surmise with the exact")
    print(f"Gaudin/Mehta sine-kernel law drops per-factor D from {Dz_w:.4f}/{Dl_w:.4f}")
    print(f"(Wigner) to {Dz:.4f}/{Dl:.4f} (exact), both with p>0.01 -- the C4b")
    print("hypothesis is confirmed BY EXACT COMPUTATION: the per-factor residual")
    print("was surmise error, not a real deviation from GUE bulk statistics.")
else:
    print("G1 RESULT: NEGATIVE branch. The exact Gaudin law does NOT clear the")
    print(f"per-factor residual (D={Dz:.4f}/{Dl:.4f}, p={pz:.3g}/{pl:.3g}) below the")
    print("p>0.01/D-improvement gate -- banked as a real, surmise-independent")
    print("per-factor deviation from GUE bulk statistics.")
print(f"G2: merged vs exact 2-fold superposition D={Dms:.5f} p={pms:.3g}")
print(f"    vs banked Wigner-surmise superposition D={Dms_w:.5f} p={pms_w:.3g}")
print("C1 control: single factors fit exact-single at least as well as exact-superposition -- PASS")
print("Gate 5: no measured physical constants used (pure zero-data + closed-form kernel).")
print("=" * 78)
