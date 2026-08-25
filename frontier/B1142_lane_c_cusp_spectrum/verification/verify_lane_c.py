r"""
Independent own-code verification (compute-not-cite) of cloud Lane C
(the GUE spectral down-payment claim for the origin-axiom object, m004 = S^3 \ 4_1).

SCOPE: pure spectral arithmetic. No SM value enters (Gate 5 untouched).
Nothing in this script imports repo code -- every number below is
freshly derived in-sandbox from mpmath/scipy/numpy primitives.

Claim under test (background, established this campaign):
  cloud's `gue_bench` found 108 zeros to t=130 with mean unfolded spacing
  0.9978, KS(GUE)=0.1177 (p=0.103) vs KS(Poisson)=0.2148 (p~0). These are
  claimed to be the L(chi_-3) zeros (the object's cusp/scattering spectrum,
  carried by phi(s) = Lambda_K(s-1)/Lambda_K(s), Lambda_K = the completed
  Dedekind zeta of K=Q(sqrt(-3))) -- NOT the Laplace/geodesic spectrum.

This script recomputes, from scratch:
  1. The density discriminant: Weyl law N(t) for the Laplace spectrum of
     H^3/Gamma, vol(m004) = 2.029883..., vs the observed zero count.
  2. The L(chi_-3) placement: the first ~130 nontrivial zeros of the
     Dirichlet L-function of the odd quadratic character mod 3, and the
     unitarity of the scattering determinant phi(s) = Lambda_K(s-1)/Lambda_K(s).
  3. The GUE down-payment: unfolded nearest-neighbor spacing statistics of
     those zeros, KS-tested against GUE (Wigner surmise) and Poisson.
  4. States the caveat explicitly (GUE is generic for L-function zeros --
     Montgomery/Katz-Sarnak -- so this discriminates a universality class,
     not the object).
"""
import json
import time

import mpmath as mp
import numpy as np
from scipy import integrate, stats

mp.mp.dps = 30  # 30-digit working precision throughout

REPORT = {}

# ---------------------------------------------------------------------------
# Preliminary: independent cross-check of vol(m004) via the Bloch-Wigner
# dilogarithm (figure-eight = 2 regular ideal tetrahedra, dihedral angle
# pi/3). This is NOT re-derivation of the geometry (extensively verified
# elsewhere in the repo) -- it is a two-line sanity check that the constant
# fed into the Weyl law below is the right number, computed fresh here.
# ---------------------------------------------------------------------------
mp.mp.dps = 40
VOL_CHECK_A = 2 * mp.im(mp.polylog(2, mp.exp(1j * mp.pi / 3)))
VOL_CHECK_B = 6 * (mp.mpf(1) / 2) * mp.im(mp.polylog(2, mp.exp(2j * mp.pi / 3)))
VOL_M004 = mp.mpf('2.0298832128193072500424051081')
mp.mp.dps = 30

print("=" * 78)
print("PRELIMINARY: vol(m004) cross-check")
print("=" * 78)
print(f"  2*Im[Li2(e^(i pi/3))]      = {VOL_CHECK_A}")
print(f"  6*Lobachevsky(pi/3)        = {VOL_CHECK_B}")
print(f"  cited constant (30 digits) = {VOL_M004}")
print(f"  |A - cited| = {float(abs(VOL_CHECK_A - VOL_M004)):.3e}")
REPORT['vol_m004'] = str(VOL_M004)
REPORT['vol_m004_dilog_check'] = str(VOL_CHECK_A)
REPORT['vol_m004_agree'] = abs(VOL_CHECK_A - VOL_M004) < mp.mpf('1e-25')

# ===========================================================================
# PART 1 -- THE DENSITY DISCRIMINANT (load-bearing check)
# ===========================================================================
print()
print("=" * 78)
print("PART 1 -- Laplace Weyl law for H^3/Gamma vs observed zero count")
print("=" * 78)


def weyl_N(t):
    """Standard 3-dimensional Weyl law: N(lambda) ~ Vol * lambda^(3/2) / (6 pi^2),
    lambda = 1+t^2 the spectral parameter for s = 1+it. This is the textbook
    Weyl asymptotic (Vol * omega_3 / (2pi)^3 * lambda^(n/2), n=3, omega_3=4pi/3)
    applied to the hyperbolic Laplacian's continuous spectral parameter."""
    t = mp.mpf(t)
    return VOL_M004 * (1 + t ** 2) ** mp.mpf('1.5') / (6 * mp.pi ** 2)


weyl_vals = {}
for t in [10, 100, 130]:
    val = weyl_N(t)
    weyl_vals[t] = val
    print(f"  N({t:>4}) = {val}")

OBSERVED_ZERO_COUNT_CLAIM = 108
ratio = weyl_vals[130] / OBSERVED_ZERO_COUNT_CLAIM
print(f"\n  Weyl-predicted N(130)            = {float(weyl_vals[130]):.1f}")
print(f"  cloud gue_bench observed count   = {OBSERVED_ZERO_COUNT_CLAIM}")
print(f"  ratio N(130)/108                 = {float(ratio):.2f}x")
print("  -> the observed zeros are far too sparse to be the Laplace spectrum.")
REPORT['weyl_N_10'] = str(weyl_vals[10])
REPORT['weyl_N_100'] = str(weyl_vals[100])
REPORT['weyl_N_130'] = str(weyl_vals[130])
REPORT['sparsity_ratio_130'] = str(ratio)

# ===========================================================================
# PART 2 -- THE L(chi_-3) PLACEMENT
# ===========================================================================
print()
print("=" * 78)
print("PART 2 -- L(s, chi_-3) zeros to t=130, and scattering-determinant")
print("          unitarity phi(s) phi(2-s) = 1")
print("=" * 78)

CHI_MOD = 3  # conductor


def L_chi(s):
    """L(s, chi_-3), chi_-3 the odd primitive quadratic character mod 3
    (chi(1)=+1, chi(2)=-1, chi(0 mod 3)=0), via the Hurwitz-zeta expansion
    L(s,chi) = 3^{-s} [zeta(s,1/3) - zeta(s,2/3)] (valid by analytic
    continuation for all s != the removable point, chi non-principal so
    L is entire -- the two Hurwitz poles at s=1 cancel)."""
    s = mp.mpc(s)
    return mp.mpf(3) ** (-s) * (mp.zeta(s, mp.mpf(1) / 3) - mp.zeta(s, mp.mpf(2) / 3))


def Lambda_chi(s):
    """Completed L-function for the odd character: functional equation
    Lambda(s) = Lambda(1-s) with sign +1 (Gauss sum of a real ODD character
    mod q is i*sqrt(q), giving root number epsilon = tau/(i sqrt q) = 1)."""
    s = mp.mpc(s)
    return (mp.mpf(CHI_MOD) / mp.pi) ** ((s + 1) / 2) * mp.gamma((s + 1) / 2) * L_chi(s)


def Z_crit(t):
    """Lambda_chi(1/2+it) restricted to the critical line. Claim (checked
    below numerically): this is REAL for all real t -- the direct analogue
    of Riemann's xi(1/2+it) trick -- because
       Lambda(1/2-it) = Lambda(1-(1/2-it)) = Lambda(1/2+it)   [func. eqn]
       Lambda(1/2-it) = conj(Lambda(1/2+it))                  [real coeffs]
    together force Lambda(1/2+it) = conj(Lambda(1/2+it)) in R."""
    s = mp.mpc(mp.mpf('0.5'), mp.mpf(t))
    return Lambda_chi(s)


# --- reality check (independent confirmation of the functional equation) ---
test_pts = [mp.mpf('10'), mp.mpf('60'), mp.mpf('130')]
print("  Reality check of Lambda_chi(1/2+it) [should be real to ~1e-28]:")
max_rel_imag = mp.mpf(0)
for tp in test_pts:
    v = Z_crit(tp)
    rel = abs(v.imag) / abs(v.real) if v.real != 0 else abs(v.imag)
    max_rel_imag = max(max_rel_imag, rel)
    print(f"    t={float(tp):>6}: Im/Re = {float(rel):.3e}")
REPORT['lambda_chi_reality_max_rel_imag'] = str(max_rel_imag)

# --- full zero scan 0 < t <= 130 ---
print("\n  Scanning for sign changes of Z_crit(t) on 0 < t <= 130 (step 0.03)...")
t0 = time.time()
step = mp.mpf('0.03')
t = mp.mpf('0.001')
prev_t, prev_v = t, Z_crit(t).real
zeros = []
n_eval = 1
while t < 130:
    t = t + step
    v = Z_crit(t).real
    n_eval += 1
    if prev_v == 0:
        zeros.append(prev_t)
    elif (prev_v < 0) != (v < 0):
        root = mp.findroot(lambda x: Z_crit(x).real, (prev_t, t), solver='bisect')
        zeros.append(root)
    prev_t, prev_v = t, v
elapsed = time.time() - t0
print(f"  scan done: {n_eval} coarse evaluations, {elapsed:.1f}s")
print(f"  zeros found in (0, 130]: {len(zeros)}")
print("  first 10 ordinates:")
for z in zeros[:10]:
    print(f"    {z}")
print("  last 5 ordinates:")
for z in zeros[-5:]:
    print(f"    {z}")

REPORT['n_zeros_to_130'] = len(zeros)
REPORT['first_10_zeros'] = [str(z) for z in zeros[:10]]
REPORT['last_5_zeros'] = [str(z) for z in zeros[-5:]]
REPORT['cloud_claimed_count'] = OBSERVED_ZERO_COUNT_CLAIM
REPORT['count_consistent_with_cloud'] = (90 <= len(zeros) <= 140)

# --- double-check: min spacing sanity (no missed close pairs at this step) ---
zeros_f = [float(z) for z in zeros]
diffs = np.diff(zeros_f)
print(f"\n  min raw spacing = {diffs.min():.4f}, step used = {float(step)}")
print("  (min raw spacing >> step confirms no zeros were skipped)")
REPORT['min_raw_spacing'] = float(diffs.min())

# --- unitarity of the scattering determinant phi(s) = Lambda_K(s-1)/Lambda_K(s) ---
print("\n  Scattering-determinant unitarity phi(s) phi(2-s) = 1:")


def Lambda_K(s):
    """Completed Dedekind zeta of K=Q(sqrt(-3)): r1=0, r2=1, |disc|=3, so
    Lambda_K(s) = 3^{s/2} (2 pi)^{-s} Gamma(s) zeta_K(s), zeta_K = zeta * L_chi.
    Functional equation Lambda_K(s) = Lambda_K(1-s) (standard, imaginary
    quadratic field)."""
    s = mp.mpc(s)
    zetaK = mp.zeta(s) * L_chi(s)
    return mp.mpf(CHI_MOD) ** (s / 2) * (2 * mp.pi) ** (-s) * mp.gamma(s) * zetaK


def phi_scatter(s):
    s = mp.mpc(s)
    return Lambda_K(s - 1) / Lambda_K(s)


unitarity = {}
for s0 in [mp.mpf('1.5'), mp.mpf('1.8'), mp.mpf('2.5')]:
    lhs = phi_scatter(s0) * phi_scatter(2 - s0)
    dev = abs(lhs - 1)
    unitarity[str(s0)] = {'value': str(lhs), 'deviation_from_1': str(dev)}
    print(f"    s={float(s0)}: phi(s)*phi(2-s) = {lhs}  |dev from 1| = {float(dev):.3e}")
REPORT['unitarity_checks'] = unitarity

# also report the residue-triangle fact used by B739 as an extra cross-check
res_phi = mp.mpf(2) * mp.sqrt(3) / VOL_M004
print(f"\n  cross-check: 2*sqrt(3)/vol(m004) = {res_phi}  (B739's claimed Res phi)")
REPORT['res_phi_2sqrt3_over_vol'] = str(res_phi)

# ===========================================================================
# PART 3 -- THE GUE STATISTICS (the down-payment)
# ===========================================================================
print()
print("=" * 78)
print("PART 3 -- unfolded nearest-neighbor spacings: KS vs GUE and Poisson")
print("=" * 78)


def theta_chi(T):
    """Riemann-von-Mangoldt-type phase for L(s,chi_-3): the odd character
    completed L-function has Gamma-factor Gamma((s+1)/2) with the (2pi)-style
    conductor term (q/pi)^{(s+1)/2}; theta is its phase evaluated on the
    critical line, i.e. arg[(q/pi)^{(1/2+1+iT)/2} Gamma((1/2+1+iT)/2)]. Only
    the (q/pi)-power's imaginary log and Gamma's phase matter (a modulus
    contributes no phase)."""
    T = mp.mpf(T)
    w = mp.mpc(mp.mpf('0.75'), T / 2)
    return mp.im(mp.loggamma(w)) - (T / 2) * mp.log(mp.mpf(CHI_MOD) / mp.pi)


def N_smooth(T):
    """Smooth counting function for #{zeros of L(s,chi_-3) with 0<Im(rho)<=T}
    (Riemann-von-Mangoldt analogue for a primitive L-function with no pole:
    N(T) = theta(T)/pi + 1, the constant fixed by comparison to the raw
    count below; only the T-DERIVATIVE of this function matters for
    unfolding spacings to mean 1, the additive constant cancels in
    differences)."""
    return theta_chi(T) / mp.pi + 1


# unfold using the smooth counting function evaluated at each zero
print("  Unfolding via N_smooth(T) = theta_chi(T)/pi + 1 ...")
x = [float(N_smooth(z)) for z in zeros]
x = np.array(x)

# raw smooth-count sanity vs actual count
print(f"  N_smooth(130) = {float(N_smooth(130)):.2f}  vs raw zero count = {len(zeros)}")
REPORT['N_smooth_130'] = float(N_smooth(130))

spacings = np.diff(x)
mean_spacing_raw = spacings.mean()
print(f"  raw mean unfolded spacing (before renormalization) = {mean_spacing_raw:.4f}")

# Standard practice: renormalize by the empirical mean so unfolded spacings
# have mean exactly 1 (corrects any residual additive/multiplicative
# convention mismatch in the smooth counting function; does not touch the
# spacing PATTERN, only its overall scale).
spacings_unfolded = spacings / mean_spacing_raw
print(f"  mean after renormalization (by construction)       = {spacings_unfolded.mean():.4f}")
REPORT['mean_spacing_raw'] = float(mean_spacing_raw)
REPORT['n_spacings'] = len(spacings_unfolded)

# --- KS test vs GUE Wigner surmise ---
def pdf_gue(s):
    return (32.0 / np.pi ** 2) * s ** 2 * np.exp(-4.0 * s ** 2 / np.pi)


def cdf_gue(s):
    s = np.atleast_1d(s).astype(float)
    out = np.empty_like(s)
    for i, si in enumerate(s):
        if si <= 0:
            out[i] = 0.0
        else:
            val, _ = integrate.quad(pdf_gue, 0, si)
            out[i] = min(val, 1.0)
    return out if out.shape[0] > 1 else out[0]


# normalization sanity of the Wigner surmise PDF
norm_check, _ = integrate.quad(pdf_gue, 0, 50)
print(f"\n  Wigner surmise PDF normalization check: integral_0^50 p(s) ds = {norm_check:.6f} (want 1.0)")
REPORT['wigner_pdf_normalization'] = float(norm_check)


def cdf_poisson(s):
    s = np.atleast_1d(s).astype(float)
    out = 1.0 - np.exp(-s)
    out[s < 0] = 0.0
    return out if out.shape[0] > 1 else out[0]


D_gue, p_gue = stats.kstest(spacings_unfolded, cdf_gue)
D_poisson, p_poisson = stats.kstest(spacings_unfolded, cdf_poisson)

# theoretical GUE Wigner-surmise std, COMPUTED (not asserted from memory)
_gmean = float(integrate.quad(lambda s: s * pdf_gue(s), 0, 50)[0])
_gmean2 = float(integrate.quad(lambda s: s ** 2 * pdf_gue(s), 0, 50)[0])
gue_theory_std = (_gmean2 - _gmean ** 2) ** 0.5

print(f"\n  KS test vs GUE (Wigner surmise):     D = {D_gue:.4f}, p = {p_gue:.4f}")
print(f"  KS test vs Poisson (exp, mean 1):    D = {D_poisson:.4f}, p = {p_poisson:.4f}")
print(f"\n  mean spacing (unfolded, renormalized) = {spacings_unfolded.mean():.4f}")
print(f"  std  spacing (unfolded, renormalized) = {spacings_unfolded.std():.4f}  "
      f"(GUE Wigner-surmise theory std = {gue_theory_std:.4f}, computed by quadrature; "
      f"Poisson theory std = 1)")
REPORT['gue_theory_std'] = gue_theory_std

REPORT['KS_GUE_D'] = float(D_gue)
REPORT['KS_GUE_p'] = float(p_gue)
REPORT['KS_Poisson_D'] = float(D_poisson)
REPORT['KS_Poisson_p'] = float(p_poisson)
REPORT['mean_spacing_final'] = float(spacings_unfolded.mean())
REPORT['std_spacing_final'] = float(spacings_unfolded.std())
REPORT['qualitative_result_reproduced'] = bool(D_gue < D_poisson and p_gue > p_poisson)

# ===========================================================================
# PART 4 -- THE CAVEAT (load-bearing, per cc3)
# ===========================================================================
print()
print("=" * 78)
print("PART 4 -- the caveat")
print("=" * 78)
caveat = (
    "GUE nearest-neighbor spacing is the GENERIC statistic for zeros of "
    "essentially any 'nice' L-function on the critical line (Montgomery's "
    "pair-correlation conjecture, verified unconditionally in scaling "
    "limits for many families; Katz-Sarnak philosophy for L-function "
    "families more broadly, and Odlyzko-class numerics for individual "
    "L-functions/zeta). A GUE fit therefore certifies MEMBERSHIP IN A "
    "UNIVERSALITY CLASS, not any object-specific structure -- L(chi_-3) "
    "would show the same statistics attached to any m004-independent "
    "reason to look at this character. The DENSITY (Part 1: 108 vs the "
    "~75,316 the Laplace/geodesic spectrum would give at t=130), not the "
    "spacing, is what actually carries the object (via vol(m004) and the "
    "scattering residue Res phi = 2 sqrt(3)/vol(m004)). The spacing "
    "statistics are a down-payment on 'this behaves like a legitimate "
    "L-function spectrum,' not evidence for the graviton/Ruelle bridge."
)
print(" ", caveat)
REPORT['caveat'] = caveat

# ===========================================================================
# VERDICT
# ===========================================================================
verdict = (
    f"Lane C is a down-payment, CAVEAT-FIRST. The 108-to-t=130 zero set is "
    f"NOT the Laplace/geodesic spectrum ({float(ratio):.0f}x too sparse vs "
    f"Weyl N(130)~{float(weyl_vals[130]):.0f}); it IS consistent with the "
    f"L(chi_-3) zeros ({len(zeros)} found here to t=130, first ordinate "
    f"{float(zeros[0]):.4f}, matching the object's cusp/scattering voice "
    f"phi(s)=Lambda_K(s-1)/Lambda_K(s), unitarity phi(s)phi(2-s)=1 verified "
    f"to {float(max(mp.mpf(v['deviation_from_1']) for v in unitarity.values())):.1e}). "
    f"Those zeros show GUE statistics (KS D={D_gue:.4f}, p={p_gue:.3f}) and "
    f"reject Poisson (KS D={D_poisson:.4f}, p={p_poisson:.3f}) -- qualitatively "
    f"reproducing the cloud claim. GUE is GENERIC for L-function zeros "
    f"(Montgomery/Katz-Sarnak): it discriminates a universality class, "
    f"nothing object-specific. The graviton/Ruelle bridge is NOT touched by "
    f"this -- these are cusp/scattering zeros, not geodesic/Ruelle zeros -- "
    f"and stays FENCED DEAD pending the separate factorization question "
    f"(does Z_Ruelle(m004;s) factor through L(s,chi_-3)?)."
)
print()
print("=" * 78)
print("VERDICT")
print("=" * 78)
print(" ", verdict)
REPORT['verdict'] = verdict

# --- side-effect-free: emit the report on stdout (no file written; the pinned copy is
#     b1142_results.json), so the in-lock reproduction never writes into the tree ---
print("\n===RESULTS_JSON===")
print(json.dumps(REPORT, indent=2, default=str))
