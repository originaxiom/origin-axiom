r"""
Follow-up check: is cloud's "108 zeros to t=130" the zero set of L(s,chi_-3)
ALONE (my verify_lane_c.py found only 65), or of the FULL Dedekind zeta
zeta_K(s) = zeta(s) * L(s,chi_-3) -- i.e. the zeros of Lambda_K itself, the
object's B739 "voice"? mpmath.nzeros(130) = 43 Riemann-zeta zeros, and
43 + 65 = 108 EXACTLY. This script builds the combined 108-element set
(interleaved zeta zeros + L(chi_-3) zeros), unfolds it by the COMBINED
smooth counting function, and runs the same GUE/Poisson KS tests -- both
as the more precise reproduction of "Lambda_K's zeros" and as a check of
whether interleaving two a-priori-independent GUE-class spectra still
passes a single-GUE test (a genuine random-matrix-theory subtlety: merged
independent point processes generically move spacing statistics AWAY from
single-channel GUE and toward Poisson).
"""
import json
import time

import mpmath as mp
import numpy as np
from scipy import integrate, stats

mp.mp.dps = 30

CHI_MOD = 3


def L_chi(s):
    s = mp.mpc(s)
    return mp.mpf(3) ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def Lambda_chi(s):
    s = mp.mpc(s)
    return (mp.mpf(CHI_MOD) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * L_chi(s)


def Z_crit(t):
    s = mp.mpc(mp.mpf('0.5'), mp.mpf(t))
    return Lambda_chi(s)


print("Re-scanning L(s,chi_-3) zeros on (0,130] (step 0.03) ...")
t0 = time.time()
step = mp.mpf('0.03')
t = mp.mpf('0.001')
prev_t, prev_v = t, Z_crit(t).real
chi_zeros = []
while t < 130:
    t = t + step
    v = Z_crit(t).real
    if (prev_v < 0) != (v < 0):
        root = mp.findroot(lambda x: Z_crit(x).real, (prev_t, t), solver='bisect')
        chi_zeros.append(float(root))
    prev_t, prev_v = t, v
print(f"  {len(chi_zeros)} zeros, {time.time()-t0:.1f}s")

import os as _os
_cache = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), 'zeta_zeros_130.json')
with open(_cache) as f:
    zeta_zeros = json.load(f)
print(f"Riemann zeta zeros (0,130]: {len(zeta_zeros)}")

combined = sorted(chi_zeros + zeta_zeros)
print(f"\nCOMBINED zero set (zeta_K = zeta * L(chi_-3)) on (0,130]: {len(combined)}")
print(f"  cloud claimed: 108")
print(f"  43 (zeta) + {len(chi_zeros)} (L_chi) = {43+len(chi_zeros)}")

# --- smooth counting functions for unfolding ---
def theta_zeta(T):
    """Riemann-Siegel theta function (standard, for the Riemann zeta
    counting formula N(T) = theta(T)/pi + 1 + S(T))."""
    T = mp.mpf(T)
    return mp.im(mp.loggamma(mp.mpc(mp.mpf('0.25'), T / 2))) - (T / 2) * mp.log(mp.pi)


def theta_chi(T):
    T = mp.mpf(T)
    w = mp.mpc(mp.mpf('0.75'), T / 2)
    return mp.im(mp.loggamma(w)) - (T / 2) * mp.log(mp.mpf(CHI_MOD) / mp.pi)


def N_zeta_smooth(T):
    return theta_zeta(T) / mp.pi + 1


def N_chi_smooth(T):
    return theta_chi(T) / mp.pi + 1


def N_K_smooth(T):
    """Smooth count for zeta_K = zeta * L(chi_-3): the phase of a product is
    the sum of phases, so the combined counting function is exactly the sum
    of the two component counting functions (up to the additive constant,
    irrelevant for spacings)."""
    return N_zeta_smooth(T) + N_chi_smooth(T)


print(f"\nN_K_smooth(130) = {float(N_K_smooth(130)):.2f}  (raw combined count = {len(combined)})")

# ---------------------------------------------------------------------
# TEST A: the combined 108-element interleaved set, unfolded by N_K_smooth
# ---------------------------------------------------------------------
x_comb = np.array([float(N_K_smooth(z)) for z in combined])
sp_comb_raw = np.diff(x_comb)
mean_raw = sp_comb_raw.mean()
sp_comb = sp_comb_raw / mean_raw
print(f"\n[TEST A: combined interleaved 108-set]")
print(f"  raw mean unfolded spacing (before renorm) = {mean_raw:.4f}")
print(f"  mean spacing (renormalized to 1)          = {sp_comb.mean():.4f}")
print(f"  std  spacing                               = {sp_comb.std():.4f}")


def pdf_gue(s):
    return (32.0 / np.pi ** 2) * s ** 2 * np.exp(-4.0 * s ** 2 / np.pi)


def cdf_gue(s):
    s = np.atleast_1d(s).astype(float)
    out = np.empty_like(s)
    for i, si in enumerate(s):
        out[i] = 0.0 if si <= 0 else min(integrate.quad(pdf_gue, 0, si)[0], 1.0)
    return out if out.shape[0] > 1 else out[0]


def cdf_poisson(s):
    s = np.atleast_1d(s).astype(float)
    out = 1.0 - np.exp(-s)
    out[s < 0] = 0.0
    return out if out.shape[0] > 1 else out[0]


D_gue_c, p_gue_c = stats.kstest(sp_comb, cdf_gue)
D_poi_c, p_poi_c = stats.kstest(sp_comb, cdf_poisson)
print(f"  KS vs GUE:     D={D_gue_c:.4f}  p={p_gue_c:.4f}")
print(f"  KS vs Poisson: D={D_poi_c:.4f}  p={p_poi_c:.4f}")

# ---------------------------------------------------------------------
# TEST B (for reference): L(chi_-3) ALONE, 65-element set (already run in
# verify_lane_c.py -- repeated here so both tests sit in one place/table)
# ---------------------------------------------------------------------
x_chi = np.array([float(N_chi_smooth(z)) for z in chi_zeros])
sp_chi_raw = np.diff(x_chi)
sp_chi = sp_chi_raw / sp_chi_raw.mean()
D_gue_x, p_gue_x = stats.kstest(sp_chi, cdf_gue)
D_poi_x, p_poi_x = stats.kstest(sp_chi, cdf_poisson)
print(f"\n[TEST B: L(chi_-3) alone, {len(chi_zeros)}-set, for reference]")
print(f"  mean spacing = {sp_chi.mean():.4f}  std = {sp_chi.std():.4f}")
print(f"  KS vs GUE:     D={D_gue_x:.4f}  p={p_gue_x:.4f}")
print(f"  KS vs Poisson: D={D_poi_x:.4f}  p={p_poi_x:.4f}")

print(f"\n[reference: cloud's cited numbers]")
print(f"  n=108, mean unfolded spacing 0.9978, KS(GUE)=0.1177 (p=0.103), KS(Poisson)=0.2148 (p~0)")

out = {
    'n_chi_zeros': len(chi_zeros),
    'n_zeta_zeros': len(zeta_zeros),
    'n_combined': len(combined),
    'N_K_smooth_130': float(N_K_smooth(130)),
    'combined_mean_spacing_raw': float(mean_raw),
    'combined_mean_spacing': float(sp_comb.mean()),
    'combined_std_spacing': float(sp_comb.std()),
    'combined_KS_GUE_D': float(D_gue_c), 'combined_KS_GUE_p': float(p_gue_c),
    'combined_KS_Poisson_D': float(D_poi_c), 'combined_KS_Poisson_p': float(p_poi_c),
    'chi_only_mean_spacing': float(sp_chi.mean()),
    'chi_only_std_spacing': float(sp_chi.std()),
    'chi_only_KS_GUE_D': float(D_gue_x), 'chi_only_KS_GUE_p': float(p_gue_x),
    'chi_only_KS_Poisson_D': float(D_poi_x), 'chi_only_KS_Poisson_p': float(p_poi_x),
}
# side-effect-free: emit on stdout (no file written; pinned copy is b1142_results.json)
print("\n===COMBINED_RESULTS_JSON===")
print(json.dumps(out, indent=2, default=str))
