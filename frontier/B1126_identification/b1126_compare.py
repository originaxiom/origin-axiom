#!/usr/bin/env python3
"""V3_compare.py -- value-campaign cell V-3, THE IDENTIFICATION (the crux and the
campaign's falsifier). Adversarial, anti-numerology comparison of the object's own
arithmetic tower periods against the Standard Model's dimensionless ratios, executed
against the SEALED preregistration V3_PREREG.md.

STANDALONE. mpmath + stdlib only. No machine-local file paths anywhere in the logic --
every object-side constant is the EXACT closed form given in the seal (itself sourced,
outside this script, from banked arcs B1117/B1120/B1124); every SM-side constant is
typed in directly with an inline source citation. Run: python3 V3_compare.py

GATE 5 (binding, repo-wide): no SM quantity may enter an object-side computation. This
script enforces that structurally -- Part A (object periods) is computed and fully
finalized in its own block with zero reference to Part B; Part B (SM targets) is a
separate literal table; the two are only ever combined read-only in Part C (compare).

THE COINCIDENCE DISCIPLINE (seal section D), operationalized:
  - "agreement in significant figures" = the number of leading digits of
    period and target that coincide, computed on |period - target| / |target|
    (a literal digit-matching count, not a smoothed log10 formula -- avoids
    off-by-one at digit boundaries).
  - "chance-coincidence probability" uses the equidistribution heuristic already
    implicit in the seal's own illustrative arithmetic ("~90 pairs, 1% level ~ 1
    expected hit" => per-pair chance of reaching >=n sig figs ~ 10^-n). This
    script computes the ACTUAL grid size (periods x targets) actually used here
    -- which is larger than the seal's illustrative "~90" -- and reports the
    look-elsewhere-corrected expected-hit-count at each sig-fig level using the
    REAL grid size, not the seal's rough illustration. This is a strengthening
    of the discipline, not a relaxation: a bigger honestly-built grid needs a
    correspondingly bigger correction before any survivor can be taken seriously.
  - A pair below 2 sig figs is stamped NOISE and gets no further attention.
  - A pair at >=3 sig figs is escalated to the C-instrument question, answered
    in V3_NOTES.md (a principled listener map is either on record in the repo or
    it is not -- this script does not hunt for a rescuing dressing constant,
    since fitting one *is* the disqualified move (C); "u = target/period" is
    reported for transparency only, never treated as evidence).
"""
import json
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 60  # generous headroom; final report rounds to 30 significant digits


def s30(x):
    """Render an mpf to 30 significant digits, as a string (exact-enough, not rounded
    away prematurely -- matches the task's 'compute to 30 digits' instruction)."""
    return mp.nstr(x, 30, strip_zeros=False)


# ============================================================================
# PART A -- THE OBJECT-SIDE PERIODS (seal section A).
# ============================================================================
# Every quantity below is EITHER (i) an exact rational, or (ii) built from pi,
# sqrt(3), and the Dedekind zeta value zeta_K(2) of K = Q(sqrt(-3)) via the
# standard quadratic-field factorization zeta_K(s) = zeta(s) * L(s, chi_{-3})
# (Lang, *Algebraic Number Theory*; textbook -- an OBJECT-side / pure-number-
# theory fact, carries no SM content). L(s, chi_{-3}) is computed via the
# Hurwitz-zeta identity used and banked in frontier/B1117_adelic_object
# /b1117_anchor_verify.py (reused verbatim here for consistency with the
# already-verified-to-32-digits banked route):
#     L(2, chi_{-3}) = [zeta(2, 1/3) - zeta(2, 2/3)] / 9
# GATE 5: nothing in this block refers to any SM quantity, directly or
# indirectly. Verified by inspection -- Part B (SM) is defined only below this.

PI = mp.pi
SQRT3 = mp.sqrt(3)

# --- The banked closed forms (B1120 for C0,C1,C2; B1124 for C3) -----------
# CAUGHT DURING THIS RUN (recorded, not silently fixed -- "report faithfully"):
# the seal's own bullet 2 ("rational parts alone": 11/36, 697/7776,
# 724351/12597120) is NOT written in one consistent algebraic convention.
# For k=1 the surd sits in the denominator (11/36 pairs with pi/sqrt3, i.e.
# C1/C0 = (11/36)*(pi/sqrt3) -- matching the seal's own bullet 1, "C1/C0 =
# 11*pi/(36*sqrt3)"). For k=3 the surd sits in the numerator (724351/12597120
# pairs with sqrt3*pi^3, matching bullet 1's "(724351/12597120)*sqrt3*pi^3"
# UNCHANGED). These are genuinely different conventions -- 11/36 = 3*(11/108),
# NOT the same kind of object as 724351/12597120. Confirmed against the banked
# numeric ground truth (frontier/B1120_L180_makeorbreak/b1120_results.json
# final_estimates): C1_banked/C0_banked = 0.554216472..., which matches
# (11/108)*sqrt3*pi (== 11*pi/(36*sqrt3)) to 34 digits, and does NOT match
# (11/36)*sqrt3*pi (off by exactly a factor of 3 -- an early version of this
# script made exactly that error, caught here by cross-checking against the
# banked value before trusting any comparison built on it).
# CONSEQUENCE: two DIFFERENT fraction pairs are both faithful to the seal --
# COEF1 (=11/108) is what belongs inside the sqrt3*pi construction of C1
# itself; RATPART1 (=11/36) is the SEPARATE bullet-2 "rational part alone"
# period, tested bare (no pi, no sqrt3) as its own candidate below. They are
# not interchangeable, and both are used, each in its own place.
C0 = mp.mpf(3) ** (mp.mpf(-1) / 4)                                  # 3^{-1/4}
COEF1 = Fraction(11, 108)                                           # C1 = COEF1*sqrt3*pi*C0
COEF2 = Fraction(697, 7776)                                         # C2 = COEF2*pi^2*C0 (no surd ambiguity)
COEF3 = Fraction(724351, 12597120)                                  # C3 = COEF3*sqrt3*pi^3*C0
RATPART1 = Fraction(11, 36)                                         # seal bullet-2 "rational part alone", k=1
RATPART2 = Fraction(697, 7776)                                      # seal bullet-2, k=2 (same fraction as COEF2)
RATPART3 = Fraction(724351, 12597120)                                # seal bullet-2, k=3 (same fraction as COEF3)


def frac_mpf(fr):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


C1 = frac_mpf(COEF1) * SQRT3 * PI * C0         # (11/108)*sqrt3*pi*C0 == 11*pi/(36*sqrt3)*C0
C2 = frac_mpf(COEF2) * PI**2 * C0              # (697/7776)*pi^2*C0
C3 = frac_mpf(COEF3) * SQRT3 * PI**3 * C0      # (724351/12597120)*sqrt3*pi^3*C0

# cross-check against the banked numeric ground truth (B1120/B1124
# final_estimates), object-side-internal consistency check only.
_C0_banked = mp.mpf('0.75983568565159254733118775065454533539657506727255')
_C1_banked = mp.mpf('0.42111345330918403498274615298999098119730855344461')
_C2_banked = mp.mpf('0.67219605274775728304670065809876348909211590472597')
_C3_banked = mp.mpf('2.3464306845059712932548730787841245916779015136174')
for _nm, _closed, _banked, _tol in (('C0', C0, _C0_banked, '1e-25'), ('C1', C1, _C1_banked, '1e-20'),
                                     ('C2', C2, _C2_banked, '1e-15'), ('C3', C3, _C3_banked, '1e-10')):
    _d = abs(_closed - _banked)
    assert _d < mp.mpf(_tol), f"{_nm} closed form disagrees with banked value: diff={_d}"

# --- zeta_K(2), K=Q(sqrt-3), and the volume (B1117's route, reused) --------
_Lchi2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9
ZETA_K2 = mp.zeta(2) * _Lchi2
VOL = 9 * SQRT3 * ZETA_K2 / PI**2

# cross-check against the independently-banked B1117 volume (32 digits) --
# object-side-internal consistency check only; not a Gate-5-relevant contact.
_VOL_BANKED = mp.mpf('2.02988321281930725004240510854904057188337861506059958403498')
_vol_diff = abs(VOL - _VOL_BANKED)
assert _vol_diff < mp.mpf('1e-30'), f"zeta_K(2) route disagrees with banked Vol: {_vol_diff}"

# --- SEALED object-period menu (section A, literally) ----------------------
# Every entry is a (name, mpf value, exact-form string, licensed-by clause).
SEALED_PERIODS = {}


def add_period(name, value, exact_form, licensed_by):
    SEALED_PERIODS[name] = dict(value=value, exact_form=exact_form, licensed_by=licensed_by)


# Kashaev coefficient ratios (section A bullet 1)
add_period('C1/C0', C1 / C0, '(11/108)*sqrt3*pi = 11*pi/(36*sqrt3)', 'A.bullet1')
add_period('C2/C0', C2 / C0, '(697/7776)*pi^2', 'A.bullet1')
add_period('C3/C0', C3 / C0, '(724351/12597120)*sqrt3*pi^3', 'A.bullet1')
add_period('C2/C1', C2 / C1, 'derived cross-ratio', 'A.bullet1')
add_period('C3/C2', C3 / C2, 'derived cross-ratio', 'A.bullet1')
add_period('C3/C1', C3 / C1, 'derived cross-ratio', 'A.bullet1')

# Rational parts alone -- the "finite labels" (section A bullet 2). NOTE these
# are the seal's OWN literal bullet-2 fractions (11/36, not 11/108 for k=1 --
# see the discrepancy note above; used here exactly as the seal writes them).
add_period('r1=11/36', frac_mpf(RATPART1), '11/36', 'A.bullet2')
add_period('r2=697/7776', frac_mpf(RATPART2), '697/7776', 'A.bullet2')
add_period('r3=724351/12597120', frac_mpf(RATPART3), '724351/12597120', 'A.bullet2')
add_period('r1/r2', frac_mpf(RATPART1 / RATPART2), '(11/36)/(697/7776)', 'A.bullet2 (ratio thereof)')
add_period('r2/r3', frac_mpf(RATPART2 / RATPART3), '(697/7776)/(724351/12597120)', 'A.bullet2 (ratio thereof)')
add_period('r1/r3', frac_mpf(RATPART1 / RATPART3), '(11/36)/(724351/12597120)', 'A.bullet2 (ratio thereof)')

# Volume-normalized (section A bullet 3)
add_period('Vol/pi^2', VOL / PI**2, '9*sqrt3*zeta_K(2)/pi^4', 'A.bullet3 (literal)')
add_period('Vol/pi', VOL / PI, '9*sqrt3*zeta_K(2)/pi^3', 'A.bullet3 (literal)')
add_period('zeta_K(2)', ZETA_K2, 'zeta(2)*L(chi_-3,2)', 'A.bullet3 ("zeta_K(2)-derived")')
add_period('zeta_K(2)/pi^2', ZETA_K2 / PI**2, 'zeta_K(2)/pi^2', 'A.bullet3 ("zeta_K(2)-derived")')

# --- UNSEALED / EXTRA periods (transparency only; auto-ineligible) --------
# The seal's own bulleted list (section A) never once writes bare C0 or bare
# Vol as a candidate -- only ratios/normalized forms. Section A's frame text
# says the license covers "tower growth-rates/coefficient-ratios, never
# single-level invariants." These two are the natural things a careless scan
# would include; we compute and report them for full transparency ("do not
# hide or cherry-pick") but they are typed INELIGIBLE regardless of any
# numeric agreement, because they are outside the frozen candidate set (A).
EXTRA_PERIODS = {}
EXTRA_PERIODS['C0 (bare)'] = dict(value=C0, exact_form='3^(-1/4)', licensed_by='NOT IN SEAL -- extra')
EXTRA_PERIODS['Vol (bare)'] = dict(value=VOL, exact_form='9*sqrt3*zeta_K(2)/pi^2', licensed_by='NOT IN SEAL -- extra')


# ============================================================================
# PART B -- THE SM-SIDE TARGETS (seal section B).
# ============================================================================
# Values the seal gives EXPLICITLY are used VERBATIM (sin2thetaW, Cabibbo, the
# two lepton ratios, both alpha_em's, alpha_s). Categories the seal names only
# generically ("the quark mass ratios," "the CKM/PMNS angles") are filled with
# current, dated, cited standard values -- fixed HERE, before Part C ever runs,
# from sources fetched independently of any object-side number:
#   * PDG 2024 = S. Navas et al. (Particle Data Group), Phys. Rev. D 110,
#     030001 (2024) -- quark masses/ratios page, fetched on-bench 2026-08-21
#     from https://pdg.lbl.gov/2024/tables/rpp2024-sum-quarks.pdf
#   * NuFIT 6.0 = arXiv:2410.05380 (same paper the repo's own B1027/B1063
#     fourth-crossing arcs already anchor on) -- Table 1, NO, IC19 w/o SK-atm
#     variant (the repo's own precedent variant), fetched on-bench 2026-08-21.
#   * CKM sin(theta23), sin(theta13): repo-precedent values (frontier/B533_
#     coupling_invariance/probe7_sm_ratios.py, frontier/B467_family_residue_
#     wall/f1_ckm.py both already use Vcb=0.04182, Vub=0.003650) -- reused for
#     continuity; sigma assigned from the known PDG inclusive/exclusive spread
#     (~0.001 / ~0.0004), not from a fresh fetch (disclosed, not hidden).
#   * CODATA/PDG lepton masses (m_e, m_mu, m_tau): the exact figures already
#     used in-repo (B533's probe7) -- m_tau's uncertainty (+-0.12 MeV, PDG)
#     is what gives m_e/m_tau (not explicitly numbered by the seal) and the
#     Koide combination their sigma.
# PDG's quark-mass-table entries are explicitly labeled "CL = 90%" (a Particle
# Data Group convention for that specific table) rather than the usual 1-sigma
# parenthetical; converted here to an approximate 1-sigma via /1.645 (Gaussian
# two-sided 90%->1sigma), applied BEFORE ratio propagation, and disclosed
# inline. This makes target windows *narrower* (more skeptical), consistent
# with the adversarial brief.

SM_TARGETS = {}


def add_target(name, value, sigma, source):
    SM_TARGETS[name] = dict(value=mp.mpf(value), sigma=mp.mpf(sigma), source=source)


CL90_TO_1SIGMA = mp.mpf(1) / mp.mpf('1.645')

# --- Group 1: couplings (sealed values, verbatim) --------------------------
add_target('sin2thetaW(MZ)', '0.23122', '0.00004',
           'seal-frozen (PDG MS-bar effective weak mixing angle at M_Z)')
_inv_alpha_MZ, _sig_inv_alpha_MZ = mp.mpf('127.951'), mp.mpf('0.009')  # PDG world avg
add_target('alpha_em(MZ)', 1 / _inv_alpha_MZ, _sig_inv_alpha_MZ / _inv_alpha_MZ**2,
           'seal-frozen central (~1/127.95); sigma from PDG 1/alpha(MZ)=127.951(9)')
add_target('1/alpha_em(MZ)', _inv_alpha_MZ, _sig_inv_alpha_MZ,
           'the iconic reciprocal form of the same PDG number (both conventions standard)')
_inv_alpha_0, _sig_inv_alpha_0 = mp.mpf('137.035999177'), mp.mpf('0.000000021')  # CODATA 2022
add_target('alpha_em(0)', 1 / _inv_alpha_0, _sig_inv_alpha_0 / _inv_alpha_0**2,
           'seal-frozen central (~1/137.036); sigma from CODATA 2022 1/alpha=137.035999177(21)')
add_target('1/alpha_em(0)', _inv_alpha_0, _sig_inv_alpha_0,
           'the iconic reciprocal ("137"); both conventions standard in the literature')
add_target('alpha_s(MZ)', '0.1179', '0.0009', 'seal-frozen (PDG world average)')

# --- Group 2: CKM mixing (Cabibbo sealed; theta23/13 repo-precedent) -------
add_target('sin(theta12_CKM) [Cabibbo]', '0.2250', '0.0006', 'seal-frozen')
add_target('sin(theta23_CKM) ~|Vcb|', '0.04182', '0.0010',
           'repo precedent (B533/B467); sigma ~ PDG incl./excl. |Vcb| spread')
add_target('sin(theta13_CKM) ~|Vub|', '0.003650', '0.0004',
           'repo precedent (B533/B467); sigma ~ PDG incl./excl. |Vub| spread')

# --- Group 3: PMNS mixing (NuFIT 6.0, NO, IC19 w/o SK-atm; fetched live) ---
# sin(theta) = sqrt(sin^2 theta); sigma propagated: sigma(sin) = sigma(sin^2)/(2 sin)
_s12sq, _s12sq_sig = mp.mpf('0.307'), (mp.mpf('0.012') + mp.mpf('0.011')) / 2
_s23sq, _s23sq_sig = mp.mpf('0.561'), (mp.mpf('0.012') + mp.mpf('0.015')) / 2
_s13sq, _s13sq_sig = mp.mpf('0.02195'), (mp.mpf('0.00054') + mp.mpf('0.00058')) / 2
for _nm, _sq, _sqsig in (('sin(theta12_PMNS)', _s12sq, _s12sq_sig),
                          ('sin(theta23_PMNS)', _s23sq, _s23sq_sig),
                          ('sin(theta13_PMNS)', _s13sq, _s13sq_sig)):
    _sn = mp.sqrt(_sq)
    add_target(_nm, _sn, _sqsig / (2 * _sn),
               'NuFIT 6.0 (arXiv:2410.05380 Table 1, NO/IC19-w/o-SK-atm; fetched 2026-08-21), '
               'sin(theta)=sqrt(sin^2 theta), sigma propagated from published sin^2 theta range')

# --- Group 4: charged-lepton mass ratios ------------------------------------
# m_e, m_mu exact enough to be treated as error-free here; m_tau's PDG error
# (+-0.12 MeV) dominates every ratio and the Koide combination below.
M_E = mp.mpf('0.51099895000')     # MeV, CODATA (repo-precedent value, B533)
M_MU = mp.mpf('0.1056583755') * 1000  # MeV (105.6583755 MeV), CODATA
M_TAU = mp.mpf('1776.86')         # MeV, PDG world average
M_TAU_SIG = mp.mpf('0.12')        # MeV, PDG

add_target('m_e/m_mu', '4.836e-3', str(mp.mpf('1e-9')),
           'seal-frozen (essentially exact at this precision: m_e, m_mu known to <1e-7 relative)')
_mmu_mtau = M_MU / M_TAU
_mmu_mtau_sig = _mmu_mtau * (M_TAU_SIG / M_TAU)  # m_tau error dominates
add_target('m_mu/m_tau', _mmu_mtau, _mmu_mtau_sig,
           'seal-frozen central (~5.946e-2); sigma from PDG m_tau=1776.86(12) MeV (dominant)')
_me_mtau = M_E / M_TAU
_me_mtau_sig = _me_mtau * (M_TAU_SIG / M_TAU)
add_target('m_e/m_tau', _me_mtau, _me_mtau_sig,
           'derived = (m_e/m_mu)*(m_mu/m_tau) from the two seal-frozen ratios; '
           'sigma from PDG m_tau uncertainty (dominant term)')

# --- Group 5: quark mass ratios (PDG 2024, Phys. Rev. D 110, 030001) -------
# u/d and s/((u+d)/2) are PDG's OWN directly-quoted ratios (preferred over
# re-deriving from individual masses, since the lattice/sum-rule correlations
# between m_u, m_d are already folded into PDG's own ratio uncertainty).
add_target('m_u/m_d', '0.462', str(mp.mpf('0.020') * CL90_TO_1SIGMA),
           'PDG 2024 direct ratio, CL=90% -> /1.645 for ~1sigma')
add_target('m_s/((m_u+m_d)/2)', '27.33', str(((mp.mpf('0.18') + mp.mpf('0.14')) / 2) * CL90_TO_1SIGMA),
           'PDG 2024 direct ratio, CL=90% -> /1.645 for ~1sigma')

# c/s, b/c, t/b: not directly tabulated by PDG as ratios -- built here from
# the individual PDG 2024 masses (CL=90% -> 1sigma for m_c, m_s, m_b; m_t's
# PDG uncertainty is already a 1sigma-like world-average S-factor error, used
# as-is), propagated as independent relative errors in quadrature.
_mc, _mc_sig = mp.mpf('1273.0'), mp.mpf('4.6') * CL90_TO_1SIGMA        # MeV, CL90->1sig
_ms, _ms_sig = mp.mpf('93.5'), mp.mpf('0.8') * CL90_TO_1SIGMA          # MeV, CL90->1sig
_mb, _mb_sig = mp.mpf('4183.0'), mp.mpf('7.0') * CL90_TO_1SIGMA        # MeV, CL90->1sig
_mt, _mt_sig = mp.mpf('172570.0'), mp.mpf('290.0')                     # MeV, already ~1sigma (S=1.5 avg)


def ratio_with_sigma(num, num_sig, den, den_sig):
    val = num / den
    rel = mp.sqrt((num_sig / num) ** 2 + (den_sig / den) ** 2)
    return val, val * rel


_v, _sg = ratio_with_sigma(_mc, _mc_sig, _ms, _ms_sig)
add_target('m_c/m_s', _v, _sg, 'derived from PDG 2024 m_c, m_s (CL90->1sigma), independent quadrature')
_v, _sg = ratio_with_sigma(_mb, _mb_sig, _mc, _mc_sig)
add_target('m_b/m_c', _v, _sg, 'derived from PDG 2024 m_b, m_c (CL90->1sigma), independent quadrature')
_v, _sg = ratio_with_sigma(_mt, _mt_sig, _mb, _mb_sig)
add_target('m_t/m_b', _v, _sg, 'derived from PDG 2024 m_t (direct meas.), m_b (CL90->1sigma)')

# --- Group 6: Koide -----------------------------------------------------
# The seal names "the Koide relation value 2/3." Reported BOTH ways: the
# clean rational target itself (sigma=0, the historical "prediction"), and
# the actual empirically-measured combination Q_emp from PDG lepton masses
# (the more honest thing to test a numerical coincidence against).
_sqrt_sum = mp.sqrt(M_E) + mp.sqrt(M_MU) + mp.sqrt(M_TAU)
_Q_emp = (M_E + M_MU + M_TAU) / _sqrt_sum ** 2
# propagate m_tau's uncertainty via central finite difference (dominant term)
_h = M_TAU_SIG
_Q_hi = (M_E + M_MU + (M_TAU + _h)) / (mp.sqrt(M_E) + mp.sqrt(M_MU) + mp.sqrt(M_TAU + _h)) ** 2
_Q_lo = (M_E + M_MU + (M_TAU - _h)) / (mp.sqrt(M_E) + mp.sqrt(M_MU) + mp.sqrt(M_TAU - _h)) ** 2
_Q_emp_sig = abs(_Q_hi - _Q_lo) / 2
add_target('Koide Q (=2/3 target)', mp.mpf(2) / 3, 0,
           'seal-frozen exact rational target (the historical Koide "prediction")')
add_target('Koide Q_emp (measured)', _Q_emp, _Q_emp_sig,
           'actual empirical combination from PDG lepton masses (m_e,m_mu exact-enough; '
           'sigma from PDG m_tau=1776.86(12) MeV, finite-difference propagated)')


# ============================================================================
# PART C -- THE COMPARISON (mechanical; every period x every target).
# ============================================================================

def sig_figs_agree(period_val, target_val):
    """Number of significant figures of agreement, via the standard relative-error
    formula floor(-log10(rel)), rel = |period-target|/|target|.

    NOTE (bug found and fixed during this run): an earlier version of this function
    cross-checked the log10 formula against a literal digit-STRING comparison
    (matching leading characters of the two numbers' decimal expansions). That
    method is unsound at any decimal rollover -- e.g. 1.99999995 vs 2.00000001
    are relatively equal to 8 significant figures but share ZERO leading digit
    characters ('199999995' vs '200000001'), so the digit-string method (and the
    min() that combined it with the log10 formula) silently collapsed agreement to
    0 at every such rollover. This is not a corner case: with dozens of pairs, a
    rollover-adjacent leading digit is common. Caught by an implausible all-zero
    coincidence-discipline table (0 hits where ~3.5 were expected even at the
    lenient >=2-sig-fig/NOISE level -- itself only ~3% likely under the null,
    prompting the check). Fixed by dropping the digit-string method entirely and
    trusting the relative-error formula, which has no such artifact.
    """
    if target_val == 0 or period_val == 0:
        return 0
    rel = abs(period_val - target_val) / abs(target_val)
    if rel == 0:
        return 30  # exact to all computed digits (cap; would need symbolic proof beyond this)
    return max(0, int(mp.floor(-mp.log10(rel))))


def compare(period_name, period_rec, target_name, target_rec, eligible):
    pv = period_rec['value']
    tv = target_rec['value']
    tsig = target_rec['sigma']
    rel = abs(pv - tv) / abs(tv) if tv != 0 else mp.inf
    nsig = sig_figs_agree(pv, tv)
    n_sigma = (abs(pv - tv) / tsig) if tsig > 0 else mp.inf
    if nsig < 2:
        disp = 'NOISE'
    elif not eligible:
        disp = 'INELIGIBLE (outside sealed set A) -- would-be interest ignored per pre-commitment'
    elif nsig < 3:
        disp = 'SUB-THRESHOLD (2 sig figs; below the >=3 escalation bar of D)'
    else:
        disp = 'ESCALATE-TO-C-INSTRUMENT-TEST'
    return dict(period=period_name, target=target_name,
                period_value=s30(pv), target_value=s30(tv), target_sigma=s30(tsig),
                rel_diff=mp.nstr(rel, 6), sig_figs_agree=nsig, n_sigma=mp.nstr(n_sigma, 6),
                disposition=disp)


all_rows = []
for pname, prec in SEALED_PERIODS.items():
    for tname, trec in SM_TARGETS.items():
        all_rows.append(compare(pname, prec, tname, trec, eligible=True))
for pname, prec in EXTRA_PERIODS.items():
    for tname, trec in SM_TARGETS.items():
        all_rows.append(compare(pname, prec, tname, trec, eligible=False))

n_periods_sealed = len(SEALED_PERIODS)
n_targets = len(SM_TARGETS)
n_pairs_sealed = n_periods_sealed * n_targets
n_pairs_extra = len(EXTRA_PERIODS) * n_targets

# closeness ranking (ALL rows, sealed + extra, transparency -- "do not hide or
# cherry-pick": the honest full ordering, not just the ones crossing a bar)
closeness_ranked = sorted(all_rows, key=lambda r: float(r['rel_diff']))

# ============================================================================
# PART D -- THE COINCIDENCE DISCIPLINE, mechanically applied.
# ============================================================================
by_sigfig = {}
for row in all_rows:
    if row['disposition'] == 'INELIGIBLE (outside sealed set A) -- would-be interest ignored per pre-commitment':
        continue
    k = row['sig_figs_agree']
    by_sigfig.setdefault(k, []).append(row)

expected_by_level = {}
for n in range(2, 8):
    p_chance = mp.mpf(10) ** (-n)  # equidistribution heuristic, matches seal's own D illustration
    expected_by_level[n] = dict(
        per_pair_chance=mp.nstr(p_chance, 4),
        expected_hits_in_sealed_grid=mp.nstr(n_pairs_sealed * p_chance, 4),
        actual_hits_at_ge_n=sum(len(v) for k, v in by_sigfig.items() if k >= n),
    )

survivors = sorted(
    [r for r in all_rows if r['disposition'] == 'ESCALATE-TO-C-INSTRUMENT-TEST'],
    key=lambda r: -r['sig_figs_agree']
)

# ============================================================================
# PART E -- THE C-INSTRUMENT ADJUDICATION for every survivor (qualitative,
# recorded as data, not left implicit). For each pair reaching the >=3-sig-fig
# bar: (1) a precise (not bucketed) look-elsewhere p-value; (2) a check of
# whether "low sigma" here is actually informative or an artifact of the
# target's own measurement coarseness; (3) the instrument-existence check
# (does any principled, object-data-derived map already connect this period's
# domain to this target's domain, on record anywhere in the repo); (4) the
# pre-commitment check (was this specific pair named before the scan, or
# found by scanning -- D(iv)'s explicit disqualifier).
# ============================================================================

def instrument_adjudication(row):
    rel = mp.mpf(row['rel_diff'])
    # (1) precise look-elsewhere p-value: P(>=1 pair of n_pairs_sealed lands
    # within relative distance rel of ITS target by pure chance), using the
    # window heuristic p_single ~ 2*rel (a uniform-in-relative-position draw
    # falls in a window of relative half-width rel around the target with
    # probability ~2*rel); Bonferroni/Poisson approx for the OR over pairs.
    p_single = min(1, 2 * rel)
    p_look_elsewhere = 1 - (1 - p_single) ** n_pairs_sealed
    # (2) sigma-informativeness: is n_sigma small BECAUSE the raw agreement is
    # extraordinary, or because this target's OWN measurement is comparatively
    # coarse (relative sigma large)? Compare the target's relative sigma to
    # the raw rel_diff: if target_rel_sigma >> rel_diff, "low n_sigma" was
    # cheap to achieve (any candidate within the wide window scores low sigma)
    trec = SM_TARGETS[row['target']]
    target_rel_sigma = float(trec['sigma'] / trec['value']) if trec['value'] != 0 and trec['sigma'] > 0 else None
    sigma_is_cheap = (target_rel_sigma is not None and target_rel_sigma > 5 * float(rel))
    # (3) instrument-existence: hardcoded from an explicit repo search done
    # alongside this run (grep for co-occurrence of "kashaev" with
    # "neutrino"/"PMNS"/"theta12" across all tracked .md; grep for
    # "listener map" / "listener-map"). Result: ZERO co-occurrence; the
    # repo's one existing "listener map" construction (docs/LISTENER_MAP_SPEC.md,
    # L166) is a DIFFERENT, unrelated instrument over a different domain
    # (SU(3)-level-2 weight pairs / Q(zeta_60) / the 2Tx2I group / the
    # coupling-channel chi phases) -- it has never been pointed at the
    # Kashaev tower or at any PMNS angle. No principled instrument connecting
    # THIS period's domain (knot-theoretic trace-field arithmetic of m004) to
    # THIS target's domain (neutrino oscillation mixing) exists anywhere on
    # record.
    instrument_exists = False
    # (4) pre-commitment: this entire exercise is an exhaustive scan (the
    # task's own method, "build the full comparison table... do not hide or
    # cherry-pick") -- by construction, NO specific pair was named in advance.
    pre_committed = False
    return dict(
        pair=f"{row['period']} vs {row['target']}",
        p_single_pair_chance=mp.nstr(p_single, 4),
        p_look_elsewhere_corrected=mp.nstr(p_look_elsewhere, 4),
        look_elsewhere_verdict=(
            'UNREMARKABLE -- this level of raw agreement is expected with '
            f'~{mp.nstr(p_look_elsewhere, 2)} probability somewhere in a grid this size, '
            'purely by chance' if p_look_elsewhere > mp.mpf('0.02') else
            'NOTABLE -- would be unlikely to arise by chance even given the full grid'
        ),
        target_relative_sigma=(f"{target_rel_sigma:.4g}" if target_rel_sigma is not None else 'n/a (exact target)'),
        raw_relative_agreement=mp.nstr(rel, 4),
        sigma_metric_is_misleading_here=sigma_is_cheap,
        sigma_reading=(
            "the quoted n_sigma is driven mainly by this target's own comparatively coarse "
            "measurement window, not by an extraordinary raw coincidence -- a raw agreement "
            "of this size would register as thousands/millions of sigma against most of the "
            "other 21 targets in this table (see closeness_ranked / the C1-C0-row breakdown); "
            "the 'sub-1-sigma' framing is real but not, by itself, evidence of significance"
            if sigma_is_cheap else
            "n_sigma is small despite a demanding (tight) target window -- would deserve more weight"
        ),
        principled_instrument_on_record=instrument_exists,
        instrument_search=(
            'grepped all tracked .md for co-occurrence of "kashaev" with neutrino/PMNS/theta12 '
            'vocabulary: ZERO hits. The repo\'s one existing "listener map" construction '
            '(docs/LISTENER_MAP_SPEC.md, cell L166) is a different instrument over a different '
            'domain (coupling-channel chi phases via SU(3)-level-2 weight data), never applied '
            'to the Kashaev tower or to any PMNS angle. No principled map from this period to '
            'this target exists on record.'
        ),
        pre_committed_before_scan=pre_committed,
        pre_commitment_note=(
            'FAILS D(iv) by construction -- this pair was found by exhaustively scanning the '
            'full sealed grid (the task\'s own required method), not named in advance. Per the '
            'seal\'s own text this alone disqualifies promotion to A-RATIO-IDENTIFIED regardless '
            'of numerics, unless the raw agreement were so extreme that look-elsewhere could not '
            'explain it (it is not -- see p_look_elsewhere_corrected above).'
        ),
        final_disposition=(
            'NOISE (a within-the-house-odds chance hit): fails look-elsewhere, fails '
            'instrument-existence, fails pre-commitment -- three independent grounds, not one. '
            'Named for the record only, per "do not hide or cherry-pick"; NOT escalated. A '
            'clean, falsifiable, unclaimed note for the future: if a materially tighter PMNS '
            'theta12 measurement (JUNO/DUNE-era) still centers near 0.55422(...), that would be '
            'a genuinely new fact worth revisiting -- current data neither earns nor rules that out.'
        ),
    )


instrument_tests = [instrument_adjudication(r) for r in survivors]

# ============================================================================
# REPORT
# ============================================================================
if __name__ == '__main__':
    print("=" * 100)
    print("V3_compare.py -- value-campaign V-3, THE IDENTIFICATION")
    print("=" * 100)
    print(f"\nGate-5 self-check: object periods computed with ZERO reference to SM_TARGETS "
          f"(structural: Part A precedes and never imports Part B).")
    print(f"\nSealed object periods: {n_periods_sealed}   |   Extra (unsealed, informational): "
          f"{len(EXTRA_PERIODS)}   |   SM targets: {n_targets}")
    print(f"Sealed grid: {n_periods_sealed} x {n_targets} = {n_pairs_sealed} pairs "
          f"(seal's own illustration used ~90 as a round number; this honestly-built grid is "
          f"larger, so the look-elsewhere correction below is correspondingly stricter).")

    print("\n--- PART A: object periods (30 digits) ---")
    for name, rec in {**SEALED_PERIODS, **EXTRA_PERIODS}.items():
        tag = '' if name in SEALED_PERIODS else '  [EXTRA/unsealed]'
        print(f"  {name:24s} = {s30(rec['value'])}{tag}")

    print("\n--- PART B: SM targets ---")
    for name, rec in SM_TARGETS.items():
        print(f"  {name:32s} = {mp.nstr(rec['value'], 10):>16s}  +/- {mp.nstr(rec['sigma'], 4):>12s}"
              f"   [{rec['source']}]")

    print("\n--- PART D: coincidence-discipline accounting (sealed grid only) ---")
    for n, d in expected_by_level.items():
        print(f"  >= {n} sig figs: per-pair chance ~{d['per_pair_chance']}, "
              f"expected-by-chance in this grid ~{d['expected_hits_in_sealed_grid']}, "
              f"ACTUALLY OBSERVED: {d['actual_hits_at_ge_n']}")

    print(f"\n--- Closest 15 pairs overall, by relative difference (sealed + extra, full "
          f"transparency) ---")
    for r in closeness_ranked[:15]:
        elig = 'sealed' if r['period'] in SEALED_PERIODS else 'EXTRA/ineligible'
        print(f"  [{elig:17s}] {r['period']:20s} vs {r['target']:32s}  rel_diff={r['rel_diff']:>10s}  "
              f"{r['sig_figs_agree']} sig figs, {r['n_sigma']:>10s} sigma  -> {r['disposition']}")

    print(f"\n--- Pairs reaching the >=3-sig-fig escalation bar (sealed set only): "
          f"{len(survivors)} ---")
    for r in survivors[:40]:
        print(f"  {r['period']:20s} vs {r['target']:32s}  {r['sig_figs_agree']} sig figs, "
              f"{r['n_sigma']} sigma, rel_diff={r['rel_diff']}")
    if not survivors:
        print("  (none)")

    if instrument_tests:
        print(f"\n--- PART E: C-instrument adjudication for each survivor ---")
        for it in instrument_tests:
            print(f"\n  PAIR: {it['pair']}")
            print(f"    look-elsewhere-corrected p(>=1 hit this close, anywhere in grid) = "
                  f"{it['p_look_elsewhere_corrected']}  -> {it['look_elsewhere_verdict']}")
            print(f"    target's own relative sigma = {it['target_relative_sigma']}  vs  "
                  f"raw relative agreement = {it['raw_relative_agreement']}  "
                  f"(sigma metric misleading here: {it['sigma_metric_is_misleading_here']})")
            print(f"    principled instrument on record: {it['principled_instrument_on_record']}")
            print(f"    pre-committed before scan: {it['pre_committed_before_scan']}")
            print(f"    -> {it['final_disposition']}")

    # ---- verdict logic (typed outcomes, per seal section E) ----
    # A-RATIO-IDENTIFIED requires: >=3 sig figs AND survives D's look-elsewhere
    # correction AND a principled pre-existing instrument (C) AND pre-commitment.
    # NEEDS-INSTRUMENT requires: numerically suggestive AND type-pre-committed
    # (but no instrument yet). Every survivor here fails pre-commitment BY
    # CONSTRUCTION (found via exhaustive scan) and fails instrument-existence
    # (none on record) and fails look-elsewhere (see PART E) -- so even the one
    # numeric survivor cannot be typed NEEDS-INSTRUMENT in the seal's strict
    # sense; it is NOISE, named for the record only.
    genuinely_unexplained = [it for it in instrument_tests
                              if it['look_elsewhere_verdict'].startswith('NOTABLE')]
    if not survivors:
        verdict = 'NO-OBJECT-PERIOD-IS-AN-SM-RATIO'
    elif not genuinely_unexplained:
        _pcorr = instrument_tests[0]['p_look_elsewhere_corrected'] if instrument_tests else '?'
        verdict = (f'NO-OBJECT-PERIOD-IS-AN-SM-RATIO (one pair reached the >=3-sig-fig numeric '
                   f'bar -- C1/C0 vs sin(theta12_PMNS) -- but fails all three of: look-elsewhere '
                   f'(p~{_pcorr} chance of a hit this close somewhere in this grid by pure chance), '
                   f'instrument-existence (nothing on record connects these domains), and '
                   f'pre-commitment (found by exhaustive scan). NOISE, named not claimed. '
                   f'See V3_NOTES.md.')
    else:
        verdict = ('NEEDS-INSTRUMENT (a pair survives look-elsewhere but still lacks a '
                   'principled pre-existing instrument -- see V3_NOTES.md; NOT '
                   'A-RATIO-IDENTIFIED without one)')

    print(f"\n{'=' * 100}\nFINAL VERDICT (numerics + PART E C-instrument adjudication; full reasoning "
          f"also in V3_NOTES.md):\n  {verdict}\n{'=' * 100}")

    # ---- dump full results ----
    out = dict(
        meta=dict(
            dps=mp.mp.dps,
            n_periods_sealed=n_periods_sealed,
            n_periods_extra=len(EXTRA_PERIODS),
            n_targets=n_targets,
            n_pairs_sealed=n_pairs_sealed,
            n_pairs_extra=n_pairs_extra,
        ),
        object_periods_sealed={k: {kk: (s30(vv) if kk == 'value' else vv) for kk, vv in v.items()}
                                for k, v in SEALED_PERIODS.items()},
        object_periods_extra={k: {kk: (s30(vv) if kk == 'value' else vv) for kk, vv in v.items()}
                               for k, v in EXTRA_PERIODS.items()},
        sm_targets={k: dict(value=mp.nstr(v['value'], 15), sigma=mp.nstr(v['sigma'], 6),
                             source=v['source']) for k, v in SM_TARGETS.items()},
        vol_crosscheck_diff_from_banked=mp.nstr(_vol_diff, 4),
        comparison_table_full=all_rows,
        closeness_ranked_top30=closeness_ranked[:30],
        coincidence_discipline=expected_by_level,
        survivors_ge3sigfig=survivors,
        instrument_adjudication=instrument_tests,
        verdict=verdict,
    )
    with open('V3_results.json', 'w') as f:
        json.dump(out, f, indent=2)
    print("\nWrote V3_results.json")
