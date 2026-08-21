#!/usr/bin/env python3
"""naturalvalues.py -- value-probing wave, cell P-NATURALVALUES ("all around" the crux).

Adversarial, anti-numerology comparison of the object's OWN natural, single-level
dimensionless invariants (never tower periods/growth-rates -- that is V-3/B1126's
disjoint territory) against the Standard Model's dimensionless ratios, executed against
the sealed PRECOMMIT.md in this directory.

STANDALONE. mpmath + stdlib only. No machine-local file paths anywhere in the logic --
every object-side constant is either an EXACT closed form (computed here, arbitrary
precision) or, where no closed form is known, the highest-precision literal already
banked in the source arc (cited inline, never re-derived). Every SM-side constant is
typed in directly with an inline source citation, reproduced verbatim from the sealed
V-3/B1126 target table for cross-probe consistency. Run: python3 naturalvalues.py

GATE 5 (binding, repo-wide): no SM quantity may enter an object-side computation. Part A
(object invariants) is computed and fully finalized with zero reference to Part B; Part B
(SM targets) is a separate literal table; the two are combined read-only in Part C.
"""
import json
from fractions import Fraction

import mpmath as mp

mp.mp.dps = 60  # generous headroom; report rounds to 30 (or the source's native) digits


def s30(x):
    """Render an mpf to 30 significant digits (or fewer if that's all mpf holds)."""
    return mp.nstr(x, 30, strip_zeros=False)


def frac_mpf(fr):
    return mp.mpf(fr.numerator) / mp.mpf(fr.denominator)


# ============================================================================
# PART A -- THE OBJECT-SIDE NATURAL-INVARIANT MENU (PRECOMMIT.md section A).
# ============================================================================
# GATE 5: nothing in this block refers to any SM quantity, directly or indirectly.
# Verified by inspection -- Part B (SM) is defined only below this block.

PI = mp.pi
SQRT3 = mp.sqrt(3)
SQRT5 = mp.sqrt(5)
PHI = (1 + SQRT5) / 2

# --- zeta_K(2), K=Q(sqrt-3); L(chi_-3,2); Vol -- the B1117/B698 Hurwitz-zeta route ---
# (reused verbatim from the already-verified-to-32/40-digit banked routes in
#  frontier/B1117_adelic_object and frontier/B1126_identification/b1126_compare.py)
L_CHI3_2 = (mp.zeta(2, mp.mpf(1) / 3) - mp.zeta(2, mp.mpf(2) / 3)) / 9   # L(chi_-3, 2)
ZETA2 = mp.zeta(2)                                                       # zeta(2) = pi^2/6
ZETA_K2 = ZETA2 * L_CHI3_2                                                # zeta_K(2) = zeta(2)*L(chi_-3,2)
VOL = 9 * SQRT3 * ZETA_K2 / PI ** 2                                       # Vol(m004) = 9 sqrt3 zeta_K(2) / pi^2
M_A41 = VOL / PI                                                          # Mahler measure m(A_41), the K3 Borel regulator

# object-side-internal consistency checks (cross-check against independently-banked
# ground truth; not a Gate-5-relevant contact -- both sides are object-side).
_VOL_BANKED = mp.mpf('2.02988321281930725004240510854904057188337861506059958403498')
_vol_diff = abs(VOL - _VOL_BANKED)
assert _vol_diff < mp.mpf('1e-30'), f"Vol disagrees with banked B1117 value: {_vol_diff}"
_MA41_BANKED = mp.mpf('0.646131894438901028187273021447612788144483682')
_ma41_diff = abs(M_A41 - _MA41_BANKED)
assert _ma41_diff < mp.mpf('1e-30'), f"m(A_41) disagrees with banked B683 value: {_ma41_diff}"
# Vol = (3 sqrt3 / 2) * L(chi_-3,2) -- the identity stated in B1117's cc3 cross-check addendum
_vol_alt = (mp.mpf(3) * SQRT3 / 2) * L_CHI3_2
assert abs(VOL - _vol_alt) < mp.mpf('1e-55'), "Vol != (3 sqrt3/2) L(chi_-3,2) identity broken"
# m(A_41) = (3 sqrt3 / 2 pi) * L(chi_-3,2) -- B698's stated exact form
_ma41_alt = (mp.mpf(3) * SQRT3 / (2 * PI)) * L_CHI3_2
assert abs(M_A41 - _ma41_alt) < mp.mpf('1e-55'), "m(A_41) != (3 sqrt3/2pi) L(chi_-3,2) identity broken"
# and the reverse check that L(chi_-3,2) != m(A_41) as raw numbers (PRECOMMIT footnote)
assert abs(L_CHI3_2 - M_A41) > mp.mpf('0.1'), "L(chi_-3,2) and m(A_41) unexpectedly coincide"

# --- L'(15a,0), the K2 Beilinson regulator, level 15 (B698 Leg A / B683 threeway.py) ---
# No elementary closed form is banked; use the highest-precision literal on record
# (45 digits, sage/LMFDB 15.a7-derived, already cross-checked in-repo). Cited, not
# re-derived -- consistent with "read the arcs, do not re-derive."
LP_15A_0 = mp.mpf('0.251330433713252231374872566669336294636860391')
L_15A_2 = mp.mpf('0.661475187921069742727520633979626889791045796')
# object-side-internal consistency: the functional equation L'(15a,0) = (15/4pi^2) L(15a,2)
_fe_check = (mp.mpf(15) / (4 * PI ** 2)) * L_15A_2
assert abs(LP_15A_0 - _fe_check) < mp.mpf('1e-40'), "L'(15a,0) functional-equation check failed"

# --- h(Q(sqrt-15)), the genus residue (B698 Leg A, verified two ways) ---
H_Q_SQRT_M15 = mp.mpf(2)

# --- the five tones (LAW_MAP "the twist-frame tone law"; B641/B654/B1011) ---
TONE_0 = mp.mpf(0)
TONE_1 = 1 / (2 * PHI)
TONE_2 = mp.mpf(1) / 2
TONE_3 = PHI / 2
TONE_4 = mp.mpf(1)

# --- the Kashaev constant C0 (B1120/L180) ---
C0_KASHAEV = mp.mpf(3) ** (mp.mpf(-1) / 4)

# --- M(O,C) dims (B904/B882) ---
DIM_G = mp.mpf(78)
DIM_27 = mp.mpf(27)
DIM_SO8 = mp.mpf(28)
DIM_U1SQ = mp.mpf(2)
DIM_3X16 = mp.mpf(48)
assert DIM_SO8 + DIM_U1SQ + DIM_3X16 == DIM_G, "magic-square dim tiling does not sum to 78"

# --- M(O,C) structure constants (B904 Stage 2c/4, exact rationals over Q) ---
LAM = frac_mpf(Fraction(1, 1))
MU = frac_mpf(Fraction(-24, 1))
ABS_MU = abs(MU)
NU = frac_mpf(Fraction(-12, 1))
ABS_NU = abs(NU)
DET_PHI = frac_mpf(Fraction(-2, 3))
ABS_DET_PHI = abs(DET_PHI)

# --- SEALED object-invariant menu (PRECOMMIT.md section A, literally; 23 entries) ---
OBJECT_INVARIANTS = {}


def add_inv(name, value, exact_form, provenance, precision_note):
    OBJECT_INVARIANTS[name] = dict(value=value, exact_form=exact_form,
                                    provenance=provenance, precision_note=precision_note)


add_inv('Vol', VOL, '9*sqrt3*zeta_K(2)/pi^2 = (3*sqrt3/2)*L(chi_-3,2)',
        'B1117 (32-digit verified); B1116', 'exact closed form, arbitrary precision')
add_inv('m(A_41)', M_A41, 'Vol/pi', 'B698 Leg A / B1116/B1120 (K3 Borel regulator)',
        'exact closed form, arbitrary precision')
add_inv('L(chi_-3,2)', L_CHI3_2, '[zeta(2,1/3)-zeta(2,2/3)]/9 = zeta_K(2)/zeta(2)',
        'B1117/B698 (classical factorization, object-side)', 'exact closed form, arbitrary precision')
add_inv('Lp_15a_0', LP_15A_0, "L'(15a,0), K2 Beilinson regulator (func. eq. verified)",
        'B698 Leg A / B683 threeway.py (sage/LMFDB 15.a7)', 'banked literal, 45 digits, not independently re-derived')
add_inv('h_Q_sqrt_m15', H_Q_SQRT_M15, 'h(Q(sqrt(-15))) = |Cl(Q(sqrt(-15)))|',
        'B698 Leg A (two independent methods)', 'exact integer')
add_inv('tone_0', TONE_0, '0', 'LAW_MAP twist-frame tone law (B641/B654/B1011)', 'exact')
add_inv('tone_1', TONE_1, '1/(2*phi)', 'ditto', 'exact closed form, arbitrary precision')
add_inv('tone_2', TONE_2, '1/2', 'ditto', 'exact')
add_inv('tone_3', TONE_3, 'phi/2', 'ditto', 'exact closed form, arbitrary precision')
add_inv('tone_4', TONE_4, '1', 'ditto', 'exact')
add_inv('C0_kashaev', C0_KASHAEV, '3^(-1/4) = |disc Q(sqrt-3)|^(-1/4)', 'B1120/L180',
        'exact closed form, arbitrary precision')
add_inv('dim_g', DIM_G, 'dim M(O,C) (E6, Cartan-matrix-matched)', 'B904 Stage 4', 'exact integer')
add_inv('dim_27', DIM_27, 'dim of minimal rep of E6 / dim J3(O) (exceptional Jordan algebra)',
        'classical (Freudenthal/Jacobson); E6(-26)=EIV=M(O,C) real-form ID corroborated by this '
        "bench's own (26,52) signature split (B1125/B1127)", 'exact integer, cited not recomputed')
add_inv('dim_so8', DIM_SO8, 'dim so(8) (tri(O) block)', 'B904 Stage 1 (stage1_dims.json)', 'exact integer')
add_inv('dim_u1sq', DIM_U1SQ, 'dim tri(C_prime) = u(1)^2', 'B904 Stage 1', 'exact integer')
add_inv('dim_3x16', DIM_3X16, 'dim of the three 16-tiles', 'B904/B882 (28+2+48=78)', 'exact integer')
add_inv('lam', LAM, 'lambda (cross-product scale)', 'B904 Stage 2c (stage2c_results.json)', 'exact rational')
add_inv('mu', MU, 'mu (tri(O)-dual scale)', 'B904 Stage 2c (stage2c_results.json)', 'exact rational')
add_inv('abs_mu', ABS_MU, '|mu|', 'completion, signed-quantity rule (PRECOMMIT.md)', 'exact rational')
add_inv('nu', NU, 'nu (tri(C_prime)-dual scale)', 'B904 Stage 2c (stage2c_results.json)', 'exact rational')
add_inv('abs_nu', ABS_NU, '|nu|', 'completion, signed-quantity rule (PRECOMMIT.md)', 'exact rational')
add_inv('det_phi', DET_PHI, 'det phi, the E6-isomorphism determinant', 'B904 Stage 4 (FINDINGS.md, exact over Q)',
        'exact rational')
add_inv('abs_det_phi', ABS_DET_PHI, '|det phi|', 'completion, signed-quantity rule (PRECOMMIT.md)', 'exact rational')

assert len(OBJECT_INVARIANTS) == 23, f"expected 23 sealed invariants, got {len(OBJECT_INVARIANTS)}"

# value-identity notes -- verified here, not just asserted in prose
assert OBJECT_INVARIANTS['h_Q_sqrt_m15']['value'] == OBJECT_INVARIANTS['dim_u1sq']['value'] == 2
assert OBJECT_INVARIANTS['lam']['value'] == OBJECT_INVARIANTS['tone_4']['value'] == 1
assert abs(OBJECT_INVARIANTS['L(chi_-3,2)']['value'] - OBJECT_INVARIANTS['m(A_41)']['value']) > mp.mpf('0.1')

# ============================================================================
# PART B -- THE SM-SIDE TARGETS. Adopted VERBATIM from the sealed, same-day
# V-3/B1126 table (frontier/B1126_identification/b1126_compare.py), for
# cross-probe consistency within the value-probing wave. Re-verified by
# inspection (not blindly trusted) before reuse; every value keeps its
# original inline source citation.
# ============================================================================

SM_TARGETS = {}


def add_target(name, value, sigma, source):
    SM_TARGETS[name] = dict(value=mp.mpf(value), sigma=mp.mpf(sigma), source=source)


CL90_TO_1SIGMA = mp.mpf(1) / mp.mpf('1.645')

# --- Group 1: couplings ---
add_target('sin2thetaW(MZ)', '0.23122', '0.00004',
           'PDG MS-bar effective weak mixing angle at M_Z (reused from sealed V-3 table)')
_inv_alpha_MZ, _sig_inv_alpha_MZ = mp.mpf('127.951'), mp.mpf('0.009')
add_target('alpha_em(MZ)', 1 / _inv_alpha_MZ, _sig_inv_alpha_MZ / _inv_alpha_MZ ** 2,
           'PDG world avg 1/alpha(MZ)=127.951(9)')
add_target('1/alpha_em(MZ)', _inv_alpha_MZ, _sig_inv_alpha_MZ, 'same PDG number, reciprocal convention')
_inv_alpha_0, _sig_inv_alpha_0 = mp.mpf('137.035999177'), mp.mpf('0.000000021')
add_target('alpha_em(0)', 1 / _inv_alpha_0, _sig_inv_alpha_0 / _inv_alpha_0 ** 2,
           'CODATA 2022 1/alpha=137.035999177(21)')
add_target('1/alpha_em(0)', _inv_alpha_0, _sig_inv_alpha_0, 'same CODATA number ("137"), reciprocal convention')
add_target('alpha_s(MZ)', '0.1179', '0.0009', 'PDG world average')

# --- Group 2: CKM mixing ---
add_target('sin(theta12_CKM) [Cabibbo]', '0.2250', '0.0006', 'PDG (Cabibbo angle)')
add_target('sin(theta23_CKM) ~|Vcb|', '0.04182', '0.0010', 'repo precedent B533/B467; PDG incl./excl. spread')
add_target('sin(theta13_CKM) ~|Vub|', '0.003650', '0.0004', 'repo precedent B533/B467; PDG incl./excl. spread')

# --- Group 3: PMNS mixing (NuFIT 6.0) ---
_s12sq, _s12sq_sig = mp.mpf('0.307'), (mp.mpf('0.012') + mp.mpf('0.011')) / 2
_s23sq, _s23sq_sig = mp.mpf('0.561'), (mp.mpf('0.012') + mp.mpf('0.015')) / 2
_s13sq, _s13sq_sig = mp.mpf('0.02195'), (mp.mpf('0.00054') + mp.mpf('0.00058')) / 2
for _nm, _sq, _sqsig in (('sin(theta12_PMNS)', _s12sq, _s12sq_sig),
                          ('sin(theta23_PMNS)', _s23sq, _s23sq_sig),
                          ('sin(theta13_PMNS)', _s13sq, _s13sq_sig)):
    _sn = mp.sqrt(_sq)
    add_target(_nm, _sn, _sqsig / (2 * _sn),
               'NuFIT 6.0 (arXiv:2410.05380 Table 1, NO/IC19-w/o-SK-atm), sigma propagated')

# --- Group 4: charged-lepton mass ratios ---
M_E = mp.mpf('0.51099895000')
M_MU = mp.mpf('0.1056583755') * 1000
M_TAU = mp.mpf('1776.86')
M_TAU_SIG = mp.mpf('0.12')

add_target('m_e/m_mu', '4.836e-3', str(mp.mpf('1e-9')), 'CODATA (essentially exact at this precision)')
_mmu_mtau = M_MU / M_TAU
_mmu_mtau_sig = _mmu_mtau * (M_TAU_SIG / M_TAU)
add_target('m_mu/m_tau', _mmu_mtau, _mmu_mtau_sig, 'PDG m_tau=1776.86(12) MeV dominant')
_me_mtau = M_E / M_TAU
_me_mtau_sig = _me_mtau * (M_TAU_SIG / M_TAU)
add_target('m_e/m_tau', _me_mtau, _me_mtau_sig, 'derived = (m_e/m_mu)*(m_mu/m_tau)')

# --- Group 5: quark mass ratios (PDG 2024) ---
add_target('m_u/m_d', '0.462', str(mp.mpf('0.020') * CL90_TO_1SIGMA), 'PDG 2024 direct ratio, CL90->1sigma')
add_target('m_s/((m_u+m_d)/2)', '27.33', str(((mp.mpf('0.18') + mp.mpf('0.14')) / 2) * CL90_TO_1SIGMA),
           'PDG 2024 direct ratio, CL90->1sigma')

_mc, _mc_sig = mp.mpf('1273.0'), mp.mpf('4.6') * CL90_TO_1SIGMA
_ms, _ms_sig = mp.mpf('93.5'), mp.mpf('0.8') * CL90_TO_1SIGMA
_mb, _mb_sig = mp.mpf('4183.0'), mp.mpf('7.0') * CL90_TO_1SIGMA
_mt, _mt_sig = mp.mpf('172570.0'), mp.mpf('290.0')


def ratio_with_sigma(num, num_sig, den, den_sig):
    val = num / den
    rel = mp.sqrt((num_sig / num) ** 2 + (den_sig / den) ** 2)
    return val, val * rel


_v, _sg = ratio_with_sigma(_mc, _mc_sig, _ms, _ms_sig)
add_target('m_c/m_s', _v, _sg, 'PDG 2024 m_c, m_s (CL90->1sigma), independent quadrature')
_v, _sg = ratio_with_sigma(_mb, _mb_sig, _mc, _mc_sig)
add_target('m_b/m_c', _v, _sg, 'PDG 2024 m_b, m_c (CL90->1sigma), independent quadrature')
_v, _sg = ratio_with_sigma(_mt, _mt_sig, _mb, _mb_sig)
add_target('m_t/m_b', _v, _sg, 'PDG 2024 m_t (direct), m_b (CL90->1sigma)')

# --- Group 6: Koide ---
_sqrt_sum = mp.sqrt(M_E) + mp.sqrt(M_MU) + mp.sqrt(M_TAU)
_Q_emp = (M_E + M_MU + M_TAU) / _sqrt_sum ** 2
_h = M_TAU_SIG
_Q_hi = (M_E + M_MU + (M_TAU + _h)) / (mp.sqrt(M_E) + mp.sqrt(M_MU) + mp.sqrt(M_TAU + _h)) ** 2
_Q_lo = (M_E + M_MU + (M_TAU - _h)) / (mp.sqrt(M_E) + mp.sqrt(M_MU) + mp.sqrt(M_TAU - _h)) ** 2
_Q_emp_sig = abs(_Q_hi - _Q_lo) / 2
add_target('Koide Q (=2/3 target)', mp.mpf(2) / 3, 0, 'the historical Koide "prediction" (exact rational, sigma=0)')
add_target('Koide Q_emp (measured)', _Q_emp, _Q_emp_sig, 'actual empirical combination from PDG lepton masses')

assert len(SM_TARGETS) == 22, f"expected 22 SM targets, got {len(SM_TARGETS)}"
_target_mags = [abs(v['value']) for v in SM_TARGETS.values() if v['value'] != 0]
TARGET_MIN, TARGET_MAX = min(_target_mags), max(_target_mags)


# ============================================================================
# PART C -- THE COMPARISON (mechanical; every invariant x every target).
# ============================================================================

def sig_figs_agree(a, b):
    """Number of significant figures of agreement via floor(-log10(rel)),
    rel = |a-b|/|b|. An exact match (rel==0) is capped at 30 (report precision,
    not a symbolic-proof claim)."""
    if b == 0 or a == 0:
        return 0
    rel = abs(a - b) / abs(b)
    if rel == 0:
        return 30
    return max(0, int(mp.floor(-mp.log10(rel))))


def compare(inv_name, inv_rec, tgt_name, tgt_rec):
    iv = inv_rec['value']
    tv = tgt_rec['value']
    tsig = tgt_rec['sigma']
    rel = abs(iv - tv) / abs(tv) if tv != 0 else mp.inf
    nsig = sig_figs_agree(iv, tv)
    # n_sigma: well-defined only when the target carries a nonzero measurement
    # uncertainty. A tsig==0 target (the exact Koide 2/3 rational) is a MATH
    # constant, not a measurement -- report n_sigma as n/a rather than the
    # misleading 0-or-inf convention, and rely on rel_diff/sig_figs instead.
    if tsig > 0:
        n_sigma_str = mp.nstr(abs(iv - tv) / tsig, 6)
    else:
        n_sigma_str = 'n/a (exact target, no measurement sigma)'
    if nsig < 2:
        disp = 'NOISE'
    elif nsig < 3:
        disp = 'SUB-THRESHOLD (2 sig figs; below the >=3 escalation bar)'
    else:
        disp = 'ESCALATE-TO-C-INSTRUMENT-TEST'
    return dict(invariant=inv_name, target=tgt_name,
                invariant_value=s30(iv), target_value=s30(tv), target_sigma=s30(tsig),
                rel_diff=mp.nstr(rel, 6), sig_figs_agree=nsig, n_sigma=n_sigma_str,
                disposition=disp)


all_rows = []
for iname, irec in OBJECT_INVARIANTS.items():
    for tname, trec in SM_TARGETS.items():
        all_rows.append(compare(iname, irec, tname, trec))

n_inv = len(OBJECT_INVARIANTS)
n_targets = len(SM_TARGETS)
n_pairs = n_inv * n_targets

closeness_ranked = sorted(all_rows, key=lambda r: float(r['rel_diff']))

# range check (task step 2: "is it dimensionless and in the SM's range?")
range_check = {}
for iname, irec in OBJECT_INVARIANTS.items():
    v = abs(irec['value'])
    in_range = (TARGET_MIN <= v <= TARGET_MAX) if v != 0 else False
    range_check[iname] = dict(abs_value=mp.nstr(v, 8), in_sm_range=in_range,
                               sm_range=f"[{mp.nstr(TARGET_MIN, 6)}, {mp.nstr(TARGET_MAX, 6)}]")

# ============================================================================
# PART D -- THE COINCIDENCE DISCIPLINE, mechanically applied.
# ============================================================================
by_sigfig = {}
for row in all_rows:
    k = row['sig_figs_agree']
    by_sigfig.setdefault(k, []).append(row)

expected_by_level = {}
for n in range(2, 8):
    p_chance = mp.mpf(10) ** (-n)
    expected_by_level[n] = dict(
        per_pair_chance=mp.nstr(p_chance, 4),
        expected_hits_in_grid=mp.nstr(n_pairs * p_chance, 4),
        actual_hits_at_ge_n=sum(len(v) for k, v in by_sigfig.items() if k >= n),
    )

survivors = sorted(
    [r for r in all_rows if r['disposition'] == 'ESCALATE-TO-C-INSTRUMENT-TEST'],
    key=lambda r: -r['sig_figs_agree']
)

# ============================================================================
# PART E -- THE C-INSTRUMENT ADJUDICATION for every survivor.
# ============================================================================

# instrument-existence search, done alongside this run: grep all tracked .md for
# co-occurrence of M(O,C)/magic-square/Barton-Sudbery/E6-structure-constant
# vocabulary with electroweak/CKM/PMNS/quark-mass/Koide vocabulary, and separately
# for Kashaev/K2-K3-regulator/genus-residue vocabulary with the same SM side.
# Result: ZERO hits beyond the object's own internal cross-references (e.g. B904
# citing B882, B1117 citing B698) -- no principled map from any Part-A domain to
# any Part-B domain exists anywhere on record. docs/LISTENER_MAP_SPEC.md (L166) is
# a different, unrelated instrument (SU(3)-level-2 weight pairs), never pointed at
# any of these 23 invariants.
INSTRUMENT_SEARCH_NOTE = (
    'grepped all tracked .md for co-occurrence of this invariant\'s vocabulary '
    '(magic-square / Barton-Sudbery / E6 structure constants / Kashaev / Beilinson '
    'regulator / genus residue / tone law) with SM vocabulary (electroweak / CKM / '
    'PMNS / quark / lepton / Koide): zero hits beyond this probe\'s own construction. '
    'No principled instrument connecting this pair\'s two domains exists on record.'
)


def instrument_adjudication(row):
    rel = mp.mpf(row['rel_diff'])
    p_single = min(1, 2 * rel) if rel > 0 else mp.mpf('1')
    # An exact (rel==0) hit is the limiting case: the window heuristic saturates,
    # so report the RATIONAL-COINCIDENCE reading instead (see PRECOMMIT.md Part D
    # dedicated note) rather than a nonsensical p~0 look-elsewhere claim.
    is_exact = (rel == 0)
    if is_exact:
        p_look_elsewhere = None
        look_elsewhere_verdict = (
            'EXACT RATIONAL COINCIDENCE, not a continuous near-miss -- the window '
            'heuristic used for approximate hits does not apply. See the dedicated '
            'rational-coincidence reading in NOTES.md: both sides are drawn from '
            'small-denominator, {2,3}-smooth rationals for independent structural '
            'reasons (the object\'s disc=-3 arithmetic; Koide\'s target chosen '
            'historically for its simplicity), so an exact small-rational collision '
            'is the specific alternative explanation, not physical significance.'
        )
    else:
        p_look_elsewhere = 1 - (1 - p_single) ** n_pairs
        look_elsewhere_verdict = (
            'UNREMARKABLE -- this level of raw agreement is expected with '
            f'~{mp.nstr(p_look_elsewhere, 2)} probability somewhere in a grid this size, '
            'purely by chance' if p_look_elsewhere > mp.mpf('0.02') else
            'NOTABLE -- would be unlikely to arise by chance even given the full grid'
        )
    trec = SM_TARGETS[row['target']]
    target_rel_sigma = float(trec['sigma'] / trec['value']) if trec['value'] != 0 and trec['sigma'] > 0 else None
    sigma_is_cheap = (target_rel_sigma is not None and target_rel_sigma > 5 * float(rel)) if rel > 0 else None
    return dict(
        pair=f"{row['invariant']} vs {row['target']}",
        is_exact_rational_coincidence=is_exact,
        p_single_pair_chance=(mp.nstr(p_single, 4) if not is_exact else 'n/a (exact)'),
        p_look_elsewhere_corrected=(mp.nstr(p_look_elsewhere, 4) if p_look_elsewhere is not None else 'n/a (exact)'),
        look_elsewhere_verdict=look_elsewhere_verdict,
        target_relative_sigma=(f"{target_rel_sigma:.4g}" if target_rel_sigma is not None else 'n/a (exact target)'),
        raw_relative_agreement=mp.nstr(rel, 6),
        sigma_metric_is_misleading_here=sigma_is_cheap,
        principled_instrument_on_record=False,
        instrument_search=INSTRUMENT_SEARCH_NOTE,
        pre_committed_before_scan=False,
        pre_commitment_note=(
            "FAILS D(iv) by construction -- found by exhaustively scanning the full "
            "sealed 23x22 grid, not named in advance in PRECOMMIT.md. This alone caps "
            "the outcome at NAMED-CANDIDATE, never A-NATURAL-VALUE-IS-PHYSICAL, on this "
            "run alone -- regardless of numeric closeness."
        ),
        final_disposition=(
            'NAMED-CANDIDATE, relayed to cc3 (owner\'s 3rd-opinion rule for any '
            'positive-looking artefact) -- NOT claimed. Fails instrument-existence and '
            'strict pre-commitment; ' + ('an exact-rational-coincidence reading applies '
            'in place of a look-elsewhere p-value.' if is_exact else
            'look-elsewhere leaves it unremarkable.')
        ),
    )


instrument_tests = [instrument_adjudication(r) for r in survivors]

# ============================================================================
# REPORT
# ============================================================================
if __name__ == '__main__':
    print("=" * 100)
    print("naturalvalues.py -- value-probing wave, P-NATURALVALUES (\"all around\" the crux)")
    print("=" * 100)
    print(f"\nGate-5 self-check: object invariants computed with ZERO reference to SM_TARGETS "
          f"(structural: Part A precedes and never imports Part B).")
    print(f"\nObject invariants (sealed): {n_inv}   |   SM targets: {n_targets}   |   "
          f"Grid: {n_inv} x {n_targets} = {n_pairs} pairs")

    print("\n--- PART A: object invariants ---")
    for name, rec in OBJECT_INVARIANTS.items():
        print(f"  {name:16s} = {s30(rec['value']):>34s}   [{rec['exact_form']}]")

    print("\n--- Range check (task step 2: dimensionless and in the SM's range "
          f"[{mp.nstr(TARGET_MIN, 6)}, {mp.nstr(TARGET_MAX, 6)}]?) ---")
    n_in_range = sum(1 for v in range_check.values() if v['in_sm_range'])
    print(f"  {n_in_range}/{n_inv} invariants have |value| inside the SM target range "
          f"(a necessary, not sufficient, condition for a match)")

    print("\n--- PART B: SM targets ---")
    for name, rec in SM_TARGETS.items():
        print(f"  {name:32s} = {mp.nstr(rec['value'], 10):>16s}  +/- {mp.nstr(rec['sigma'], 4):>12s}"
              f"   [{rec['source']}]")

    print("\n--- PART D: coincidence-discipline accounting (full grid) ---")
    for n, d in expected_by_level.items():
        print(f"  >= {n} sig figs: per-pair chance ~{d['per_pair_chance']}, "
              f"expected-by-chance in this grid ~{d['expected_hits_in_grid']}, "
              f"ACTUALLY OBSERVED: {d['actual_hits_at_ge_n']}")

    print(f"\n--- Closest 20 pairs overall, by relative difference (full transparency) ---")
    for r in closeness_ranked[:20]:
        print(f"  {r['invariant']:16s} vs {r['target']:32s}  rel_diff={r['rel_diff']:>12s}  "
              f"{r['sig_figs_agree']:2d} sig figs, {r['n_sigma']:>10s}  -> {r['disposition']}")

    print(f"\n--- Pairs reaching the >=3-sig-fig escalation bar: {len(survivors)} ---")
    for r in survivors:
        print(f"  {r['invariant']:16s} vs {r['target']:32s}  {r['sig_figs_agree']} sig figs, "
              f"{r['n_sigma']}, rel_diff={r['rel_diff']}")
    if not survivors:
        print("  (none)")

    if instrument_tests:
        print(f"\n--- PART E: C-instrument adjudication for each survivor ---")
        for it in instrument_tests:
            print(f"\n  PAIR: {it['pair']}")
            print(f"    exact rational coincidence: {it['is_exact_rational_coincidence']}")
            print(f"    look-elsewhere: {it['p_look_elsewhere_corrected']}  -> {it['look_elsewhere_verdict']}")
            print(f"    principled instrument on record: {it['principled_instrument_on_record']}")
            print(f"    -> {it['final_disposition']}")

    # ---- verdict logic (typed outcomes, PRECOMMIT.md section E) ----
    # IMPORTANT (self-caught during this run, fixed here rather than silently patched):
    # an earlier version of this block minted a FOURTH outcome label
    # ("NEEDS-FURTHER-LOOK") whenever a survivor cleared the look-elsewhere bar --
    # that is not one of the charter's three typed outcomes. Per PRECOMMIT.md
    # section D/E: instrument_exists and pre_committed_before_scan are FALSE for
    # every row here BY CONSTRUCTION (no instrument is on record for ANY pair in
    # this probe, and every pair was found by exhaustively scanning a frozen grid,
    # never named in advance) -- so per the charter's rule 1 ("no scan-and-pick-
    # closest") every survivor is capped at NAMED-CANDIDATE, full stop, regardless
    # of how its look-elsewhere p-value reads. The look-elsewhere/NOTABLE-vs-
    # UNREMARKABLE distinction is still computed and reported (it says how
    # surprised to be), but it does not change the OUTCOME TYPE.
    genuinely_unexplained = [it for it in instrument_tests
                              if it['look_elsewhere_verdict'].startswith('NOTABLE')
                              or it['is_exact_rational_coincidence']]
    named_candidates = [it['pair'] for it in instrument_tests]
    if not survivors:
        verdict = 'NATURAL-VALUES-DISJOINT (no candidate reached the escalation bar; zero NAMED-CANDIDATEs)'
    else:
        notable_tag = (f" -- {len(genuinely_unexplained)} of these flagged NOTABLE/EXACT by the "
                        f"look-elsewhere metric (still capped at NAMED-CANDIDATE: instrument-existence "
                        f"and strict pre-commitment both fail structurally, see NOTES.md for the fuller "
                        f"true-reference-class argument)" if genuinely_unexplained else "")
        verdict = (f"NATURAL-VALUES-DISJOINT (headline) + {len(named_candidates)} NAMED-CANDIDATE(S) "
                   f"[{'; '.join(named_candidates)}]{notable_tag}; relayed to cc3, not claimed.")

    print(f"\n{'=' * 100}\nFINAL VERDICT:\n  {verdict}\n{'=' * 100}")

    out = dict(
        meta=dict(dps=mp.mp.dps, n_invariants=n_inv, n_targets=n_targets, n_pairs=n_pairs),
        object_invariants={k: {kk: (s30(vv) if kk == 'value' else vv) for kk, vv in v.items()}
                            for k, v in OBJECT_INVARIANTS.items()},
        range_check=range_check,
        sm_targets={k: dict(value=mp.nstr(v['value'], 15), sigma=mp.nstr(v['sigma'], 6), source=v['source'])
                    for k, v in SM_TARGETS.items()},
        object_side_crosschecks=dict(
            vol_diff_from_banked=mp.nstr(_vol_diff, 4),
            m_a41_diff_from_banked=mp.nstr(_ma41_diff, 4),
            l15a_functional_equation_diff=mp.nstr(abs(LP_15A_0 - _fe_check), 4),
        ),
        comparison_table_full=all_rows,
        closeness_ranked_top30=closeness_ranked[:30],
        coincidence_discipline=expected_by_level,
        survivors_ge3sigfig=survivors,
        instrument_adjudication=instrument_tests,
        verdict=verdict,
    )
    with open('results.json', 'w') as f:
        json.dump(out, f, indent=2)
    print("\nWrote results.json")
