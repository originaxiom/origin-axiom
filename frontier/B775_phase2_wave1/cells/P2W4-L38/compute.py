#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
B775 Phase-2 Wave-4   cell P2W4-L38   (OI-062 / S039 Act II)
============================================================
THE kappa = -2 DEFORMATION SCALE  --  the e^{-k*Vol} suppression, Vol = Vol(4_1).

READ IN-CELL (arcs):
  B67   the figure-eight A-polynomial FROM the trace-map fixed locus:
        fixed locus y = z = x/(x-1);  kappa(x) = tr[A,B] = L + 1/L;
        meridian trace T = tr(t), T^2 = (x^2+x-1)/(x-1);  identity kappa = T^4 - 5T^2 + 2.
        Complete hyperbolic structure = parabolic meridian T = 2  =>  kappa = -2  (L = -1).
  B213  Act I: the Higgs-side handle (char variety = 40a1) carries NO forced tiny number
        (all O(1)/BSD-generic; the 1/2 killed by a null test).  Firewall held a 4th time.
  S039  Act II row (open): "Lambda's tininess is a large-level/semiclassical suppression:
        e^{-k*Vol} in the WRT / complex-volume asymptotic".  Expected: the scale is external.

WHAT THIS CELL COMPUTES (the residual, with structure -- not an assertion):
  (1) Vol(4_1) three independent ways (Bloch-Wigner, Lobachevsky, snappy).
  (2) The kappa = -2 vacuum, EXACTLY, re-derived in-cell from the trace map (no citation):
      Fricke kappa(x) on the B67 fixed locus; the identity kappa = T^4 - 5T^2 + 2;
      kappa(T=2) = -2; the deformation coordinate kappa+2 = (T^2-1)(T^2-4).
  (3) The DEFORMATION LAW around kappa = -2, exactly, in both peripheral coordinates:
        meridian u (T = 2 cosh(u/2)):    kappa + 2 =  3u^2 + (5/4)u^4 + ...
        longitude v (L = -e^{v/2}):      kappa + 2 = -v^2/4 - v^4/192 - ...
      => v/u -> 2*sqrt(-3) : the deformation ratio (the cusp modulus) IS the atom Q(sqrt-3).
      Reproduced a 2nd way: snappy's cusp shape / log-holonomy ratio on real Dehn fillings.
  (4) The SCALE ITSELF: Vol(u) = Vol(0) - C*|u|^2 + O(u^4).  C is measured on TWO filling
      families at TWO precisions (double + HP) with Richardson conditioning, and identified.
      In the kappa coordinate: Vol = Vol_0 - (C/3)*|kappa+2| + ...
  (5) The BOUNDEDNESS test (the discriminating fact for "forced tiny number"): the exponent
      Vol over the WHOLE kappa != -2 deformation family (integer Dehn fillings, in-cell),
      with the exceptional (degenerate) slopes identified in-cell.
  (6) Level-quantization test: CS(complete) computed; a nonzero CS with a denominator would
      constrain the level k.  CS = 0 => the object supplies NO level datum.
  (7) Null test on the rate: PSLQ/identify search for an algebraic distinction of Vol/2pi.

VERDICT (sealed):
  RESOLVED-A : a FORCED (object-intrinsic) deformation scale -- i.e. the suppression exponent
               or its per-level base is itself small/forced-by-the-object, k-independently.
  RESOLVED-B : no forced scale -- rate and curvature are forced O(1) atom-valued invariants,
               the exponent is BOUNDED over the whole deformation family, the object supplies
               no level datum => the smallness is EXTERNAL (level k).      [EXTERNAL]
  UNRESOLVED : cross-checks disagree / the curvature fit is UNSTABLE.

Gate 5 STRICT: structural deformation scale only.  NO SM Higgs claim, no SM value, nothing to
CLAIMS.md, the one-number pin untouched.  Chord discipline (B774): the exponent is the honest
hyperbolic invariant Vol(4_1) and the honest peripheral (u,v) deformation -- no abelian proxy.
Env: pyenv python3 (mpmath, sympy, snappy).  Re-runnable: python3 compute.py
"""

import json, os, math, warnings
warnings.filterwarnings("ignore")
import mpmath as mp
import sympy as sp

mp.mp.dps = 60
OUT = os.path.dirname(os.path.abspath(__file__))
R = {}

# ==================================================================== #
# 1.  Vol(4_1) -- three independent ways                               #
# ==================================================================== #
z1 = mp.e ** (1j * mp.pi / 3)
Vol_A = 2 * mp.im(mp.polylog(2, z1))                      # 2 * Bloch-Wigner D(e^{i pi/3})
Vol_B = 6 * (mp.mpf('0.5') * mp.im(mp.polylog(2, mp.e ** (2j * mp.pi / 3))))   # 6*Lambda(pi/3)
try:
    import snappy
    HAVE_SNAPPY = True
except Exception:
    HAVE_SNAPPY = False

Vol_C = CS = cusp_shape = None
if HAVE_SNAPPY:
    Mhp = snappy.ManifoldHP('4_1')
    Vol_C = mp.mpf(repr(Mhp.volume()))
    cv = snappy.Manifold('4_1').complex_volume()
    CS = float(complex(cv).imag)
    cusp_shape = complex(snappy.Manifold('4_1').cusp_info('shape')[0])

VOL = Vol_A
agree_AB = abs(Vol_A - Vol_B) < mp.mpf('1e-50')
agree_AC = (Vol_C is None) or (abs(Vol_A - Vol_C) < mp.mpf('1e-30'))
CS_is_zero = (CS is not None) and abs(CS) < 1e-9

R['vol'] = {'bloch_wigner': mp.nstr(Vol_A, 20), 'lobachevsky': mp.nstr(Vol_B, 20),
            'snappy_HP': (mp.nstr(Vol_C, 20) if Vol_C else None),
            'agree_AB': bool(agree_AB), 'agree_AC': bool(agree_AC),
            'CS_complete': CS, 'CS_is_zero': bool(CS_is_zero)}

# ==================================================================== #
# 2.  The kappa = -2 vacuum, EXACT, re-derived in-cell from B67        #
# ==================================================================== #
x, T, u, v = sp.symbols('x T u v')
y = z = x / (x - 1)                                    # B67 trace-map fixed locus
kappa_x = sp.simplify(x**2 + y**2 + z**2 - x*y*z - 2)  # Fricke: tr[A,B]
kappa_x_ref = (x**4 - 3*x**3 + x**2 + 4*x - 2) / (x - 1)**2
fricke_ok = sp.simplify(kappa_x - kappa_x_ref) == 0

T2 = (x**2 + x - 1) / (x - 1)                          # B67: T^2 = tr(t)^2
identity_ok = sp.simplify(sp.expand(T2**2 - 5*T2 + 2 - kappa_x)) == 0   # kappa = T^4-5T^2+2

kappa_T = T**4 - 5*T**2 + 2
kappa_at_parabolic = sp.simplify(kappa_T.subs(T, 2))   # complete structure: T = 2
vacuum_ok = (kappa_at_parabolic == -2)
defo_coord = sp.factor(kappa_T + 2)                    # (T^2-1)(T^2-4)

R['kappa_vacuum'] = {
    'fricke_on_fixed_locus_matches_B67': bool(fricke_ok),
    'identity_kappa=T^4-5T^2+2_verified': bool(identity_ok),
    'kappa(T=2)': int(kappa_at_parabolic), 'vacuum_is_kappa_-2': bool(vacuum_ok),
    'deformation_coordinate': str(defo_coord),
}

# ==================================================================== #
# 3.  The exact deformation law in both peripheral coordinates         #
# ==================================================================== #
NORD = 8
# meridian side: T = 2 cosh(u/2)  (T = M + 1/M, u = 2 log M)
k_u = sp.series(((2*sp.cosh(u/2))**2 - 1) * ((2*sp.cosh(u/2))**2 - 4), u, 0, NORD).removeO()
k_u = sp.expand(sp.simplify(k_u))
c_u2 = sp.nsimplify(k_u.coeff(u, 2))                   # expect 3   (the hyperbolic prime)
c_u4 = sp.nsimplify(k_u.coeff(u, 4))                   # expect 5/4
# longitude side: L = -e^{v/2}  =>  kappa = L + 1/L = -2 cosh(v/2)  (EXACT, all orders)
k_v = sp.series(-2*sp.cosh(v/2) + 2, v, 0, NORD).removeO()
c_v2 = sp.nsimplify(k_v.coeff(v, 2))                   # expect -1/4
# lock: 3u^2 + ... = -v^2/4 - ...   =>  v = tau*u,  tau^2 = -12,  tau = 2*sqrt(-3)
tau_sym = sp.sqrt(sp.simplify(c_u2 / (-c_v2)))         # |tau| ; sign fixed below
tau_sq = sp.simplify(c_u2 / c_v2)                      # = -12
atom_lock = (sp.simplify(tau_sq + 12) == 0)            # tau^2 = -12 = 4*(-3): Q(sqrt-3)
# 2nd way: snappy cusp modulus
cusp_ok = (cusp_shape is not None) and abs(cusp_shape.imag - 2*math.sqrt(3)) < 1e-8 \
          and abs(cusp_shape.real) < 1e-8

R['deformation_law'] = {
    'kappa+2 (meridian u)': f"{c_u2}*u^2 + {c_u4}*u^4 + O(u^6)",
    'kappa+2 (longitude v)': f"{c_v2}*v^2 + O(v^4)   [kappa = -2cosh(v/2) exact]",
    'tau^2 = (dv/du)^2': str(tau_sq),
    'tau': f"2*sqrt(-3)  (|tau| = {sp.nsimplify(2*sp.sqrt(3))})",
    'atom_Q(sqrt-3)_lock': bool(atom_lock),
    'snappy_cusp_shape': (str(cusp_shape) if cusp_shape else None),
    'cusp_shape_matches_2sqrt3i': bool(cusp_ok),
}

# ==================================================================== #
# 4.  THE SCALE: Vol(u) = Vol(0) - C |u|^2 + O(u^4).  C measured.      #
#     TWO filling families (seeds) x TWO precisions, Richardson.        #
# ==================================================================== #
def curvature_series(slope_q, ps, hp):
    """(|u|, C_eff) along the family (p, slope_q) for p in ps."""
    Mf = (snappy.ManifoldHP if hp else snappy.Manifold)('4_1')
    V0 = mp.mpf(repr(Mf.volume()))
    out = []
    for p in ps:
        Mf.dehn_fill((p, slope_q))
        st = Mf.solution_type()
        if 'positively oriented' not in st:
            continue
        uu = complex(Mf.cusp_info(0)['holonomies'][0])
        dV = V0 - mp.mpf(repr(Mf.volume()))
        out.append((abs(uu), float(dV / mp.mpf(abs(uu))**2)))
    return out

fits = {}
stable = True
C_est = {}
if HAVE_SNAPPY:
    PS = [64, 128, 256, 512]
    for tag, (q, hp) in {'q1_double': (1, False), 'q1_HP': (1, True),
                         'q2_double': (2, False), 'q3_HP': (3, True)}.items():
        dat = curvature_series(q, PS, hp)
        fits[tag] = [(float(a), b) for a, b in dat]
        # Richardson on the last two (error ~ O(|u|^2) ~ O(1/p^2)): C = (4 f(2p) - f(p))/3
        if len(dat) >= 2:
            f1, f2 = dat[-2][1], dat[-1][1]
            C_est[tag] = (4*f2 - f1) / 3.0
    vals = list(C_est.values())
    spread = (max(vals) - min(vals)) if vals else 1.0
    C_mean = sum(vals)/len(vals) if vals else float('nan')
    stable = (len(vals) >= 3) and (spread < 1e-6)
else:
    C_mean, spread = float('nan'), 1.0
    stable = False

C_exact = float(mp.sqrt(3)/2)                          # sqrt(3)/2 = Im(tau)/4
C_identified = stable and abs(C_mean - C_exact) < 1e-7

R['scale_curvature'] = {
    'model': 'Vol(u) = Vol(0) - C*|u|^2 + O(|u|^4)',
    'C_richardson_per_family': {k: round(v, 12) for k, v in C_est.items()},
    'C_mean': (round(C_mean, 12) if C_mean == C_mean else None),
    'family_spread': (float(f'{spread:.3e}') if spread == spread else None),
    'stable_across_seeds_and_precisions': bool(stable),
    'C_exact_candidate': 'sqrt(3)/2 = Im(tau)/4 = 0.8660254038',
    'C_matches_sqrt3_over_2': bool(C_identified),
    'in_kappa_coordinate': ('Vol = Vol_0 - (C/3)*(kappa+2) + ...  on the REAL-u section '
                            '(kappa+2 = 3u^2), leading order only; C/3 = 1/(2*sqrt3) = 0.2886751'),
}

# ==================================================================== #
# 5.  The deformation SCALE and its boundedness (discriminating fact)  #
# ==================================================================== #
rate = VOL / (2*mp.pi)                     # forced, exact, O(1)
base = mp.e ** (-rate)                     # per-level suppression, O(1)
base_f = float(base)
base_is_O1 = 0.1 < base_f < 1.0
levels = [1, 2, 6, 12, 50]
scale_at_k = {int(k): float(mp.e ** (-mp.mpf(k)*rate)) for k in levels}
k_for_1e3 = float(-3*mp.log(10)/mp.log(base))

# The exponent over the WHOLE kappa != -2 family: integer Dehn fillings, in-cell.
vols, exceptional = [], []
if HAVE_SNAPPY:
    Mg = snappy.Manifold('4_1')
    for p in range(-8, 9):
        for q in range(0, 5):
            if (p, q) == (0, 0) or math.gcd(abs(p), abs(q)) != 1:
                continue
            ok = False
            for attempt in range(6):          # retriangulate before calling a slope non-geometric
                Mt = snappy.Manifold('4_1')
                if attempt:
                    Mt.randomize()
                Mt.dehn_fill((p, q))
                try:
                    st, vv = Mt.solution_type(), float(Mt.volume())
                except Exception:
                    continue
                if 'positively oriented' in st and vv > 1e-6:
                    vols.append(((p, q), vv)); ok = True; break
            if not ok:
                exceptional.append((p, q))
vols_sorted = sorted(vols, key=lambda t: t[1])
vmin = vols_sorted[0][1] if vols_sorted else None
vmax = float(VOL)
window = (vmax - vmin) if vmin else None
# per-level scale over the whole family: exp(-Vol/2pi) for Vol in [vmin, vmax]
base_range = (float(mp.e**(-mp.mpf(vmax)/(2*mp.pi))), float(mp.e**(-mp.mpf(vmin)/(2*mp.pi)))) \
             if vmin else None
bounded_O1 = (vmin is not None) and (vmin > 0.5) and (window < 1.5)

R['deformation_scale'] = {
    'form': 'S(k,u) = exp(-(k/2pi)*Vol(u)) = base(u)**k',
    'rate_Vol/2pi(vacuum)': mp.nstr(rate, 15),
    'base_exp(-Vol/2pi)': base_f, 'base_is_O1_not_tiny': bool(base_is_O1),
    'scale_at_level_k': scale_at_k,
    'k_needed_for_scale<1e-3': round(k_for_1e3, 3),
    'family_exponent_min(in-cell)': (round(vmin, 10) if vmin else None),
    'family_exponent_min_slope': (vols_sorted[0][0] if vols_sorted else None),
    'family_exponent_max(=vacuum, Thurston max)': round(vmax, 10),
    'family_exponent_window': (round(window, 10) if window else None),
    'per_level_base_range_over_family': (None if not base_range else
                                         [round(base_range[0], 6), round(base_range[1], 6)]),
    'n_geometric_slopes(in-cell)': len(vols),
    'n_slopes_without_geometric_solution(in-cell, <=6 retriangulations)': len(exceptional),
    'slopes_without_geometric_solution': sorted(set(tuple(e) for e in exceptional))[:16],
    'note_on_exceptional': ('a slope listed here failed to produce a positively-oriented '
                            'solution in-cell; that is an in-cell computational fact, not a '
                            'claim of non-hyperbolicity'),
    'exponent_bounded_O1': bool(bounded_O1),
}

# ==================================================================== #
# 6.  Level datum? + null test on the rate                             #
# ==================================================================== #
# CS(complete) = 0 (amphichiral): a nonzero CS with denominator d would constrain k mod d.
no_level_datum = bool(CS_is_zero)

# Null test: is Vol/2pi arithmetically distinguished (algebraic of low degree)?
# PSLQ protocol (anti-spurious): a candidate found at dps=60 must SURVIVE re-evaluation of the
# same integer relation at dps=250; a genuine relation evaluates to ~0 at any precision, a
# lattice artifact does not.  (deg*log10(maxcoeff) must stay well under the working precision.)
ident = mp.identify(rate, ['pi', 'log(2)', 'sqrt(3)'])
alg, alg_candidates = None, []
for deg in (2, 3, 4, 6, 8):
    rel = mp.pslq([rate**j for j in range(deg+1)], maxcoeff=10**10, maxsteps=20000)
    if rel:
        with mp.workdps(250):
            rate_hi = (2*mp.im(mp.polylog(2, mp.e**(1j*mp.pi/3)))) / (2*mp.pi)
            resid = abs(sum(mp.mpf(c)*rate_hi**j for j, c in enumerate(rel)))
        surv = resid < mp.mpf('1e-100')
        alg_candidates.append({'deg': deg, 'rel': [int(c) for c in rel],
                               'residual_at_dps250': mp.nstr(resid, 5),
                               'survives': bool(surv)})
        if surv:
            alg = (deg, [int(c) for c in rel]); break
rate_undistinguished = (ident is None) and (alg is None)
# contrast control: the CURVATURE is algebraic and IS identified (at the measured tolerance)
curv_ident = mp.identify(mp.mpf(C_mean) if C_mean == C_mean else mp.mpf(0), ['sqrt(3)'], tol=1e-8)
curv_delta = abs(C_mean - C_exact) if C_mean == C_mean else None

R['level_and_null'] = {
    'CS_complete': CS, 'object_supplies_no_level_quantization': no_level_datum,
    'null_test_rate_identify': (str(ident) if ident else 'none'),
    'null_test_rate_pslq_deg<=8_coeff<=1e10': (str(alg) if alg else
                                              'no algebraic relation survives dps=250'),
    'pslq_candidates_rejected_as_lattice_artifacts': alg_candidates,
    'rate_arithmetically_undistinguished': bool(rate_undistinguished),
    'control_curvature_identify': (str(curv_ident) if curv_ident else 'none'),
    'control_|C-sqrt3/2|': (float(f'{curv_delta:.3e}') if curv_delta is not None else None),
}

# ==================================================================== #
# 7.  VERDICT (in-code; can emit UNRESOLVED)                           #
# ==================================================================== #
def decide():
    if not (agree_AB and agree_AC):
        return 'UNRESOLVED', 'UNRESOLVED', 'the independent Vol computations disagree'
    if not (fricke_ok and identity_ok and vacuum_ok):
        return 'UNRESOLVED', 'UNRESOLVED', 'the kappa=-2 vacuum could not be re-derived exactly in-cell'
    if not atom_lock:
        return 'UNRESOLVED', 'UNRESOLVED', 'the (u,v) deformation lock did not close'
    if not stable:
        return 'UNRESOLVED', 'UNRESOLVED', 'the curvature C is UNSTABLE across seeds/precisions'
    if not C_identified:
        return 'UNRESOLVED', 'UNRESOLVED', 'C measured stably but does not match its exact candidate'
    # --- branch A: a forced, object-intrinsic small scale ---
    if (not base_is_O1) or (vmin is not None and vmin < 0.05):
        return ('RESOLVED-A', 'RESOLVED',
                'the deformation family itself produces an intrinsically tiny suppression '
                '(k-independent) -- a forced object scale')
    # --- branch B: everything forced is O(1); smallness is the external level ---
    if base_is_O1 and bounded_O1 and no_level_datum and rate_undistinguished:
        return ('RESOLVED-B', 'EXTERNAL',
                'the kappa=-2 deformation scale is computed WITH its structure and contains no '
                'forced small number: exponent Vol_0=2.02988 (rate Vol/2pi=0.32307, base=0.72393, '
                'O(1)); the deformation is exactly kappa+2 = 3u^2 = -v^2/4 with the ratio '
                'tau=2*sqrt(-3) (the atom) and volume curvature C=sqrt(3)/2 (= Im(tau)/4), so '
                'Vol = Vol_0 - (1/(2*sqrt3))(kappa+2) + ... on the real-u section; the exponent is BOUNDED over the whole '
                'deformation family (in-cell window [%.5f, %.5f], per-level base in [%.4f, %.4f]); '
                'and CS(complete)=0 supplies no level quantization -- so the smallness of e^{-k Vol} '
                'is set ENTIRELY by the EXTERNAL level k (5th firewall mode; B213 Act I extended to '
                'the kappa=-2 vacuum deformation)' % (vmin, vmax, base_range[0], base_range[1]))
    return 'UNRESOLVED', 'UNRESOLVED', 'the deformation-scale structure did not resolve into A or B'

verdict, terminal, why = decide()
R['cell'] = 'P2W4-L38'
R['lead'] = 'OI-062 / S039 Act II -- the kappa=-2 deformation scale (e^{-k*Vol})'
R['verdict'] = verdict
R['terminal_state'] = terminal
R['why'] = why
R['gate5'] = ('structural deformation scale only; NO SM Higgs claim; no SM value; nothing to '
              'CLAIMS.md; one-number pin untouched')
R['chord_discipline_B774'] = ('exponent = the genuine hyperbolic invariant Vol(4_1); deformation '
                              '= the genuine peripheral (u,v) holonomy pair and the trace-map '
                              'kappa = tr[A,B]; no abelianized/character proxy')
R['reproduced_2nd_way'] = ('Vol: Bloch-Wigner = Lobachevsky = snappy-HP;  tau = 2sqrt(-3): exact '
                           'symbolic (u,v) series from the B67 trace-map fixed locus AND snappy '
                           'cusp modulus/log-holonomy ratio;  C = sqrt(3)/2: two filling families '
                           'x two precisions, Richardson-conditioned')
R['numerics_conditioning'] = fits

with open(os.path.join(OUT, 'results.json'), 'w') as f:
    json.dump(R, f, indent=1)

L = []
P = L.append
P('B775 P2W4-L38 -- OI-062 / S039 Act II : the kappa = -2 deformation scale')
P('=' * 74)
P('1) Vol(4_1)  Bloch-Wigner = %s' % mp.nstr(Vol_A, 18))
P('             Lobachevsky  = %s   agree=%s' % (mp.nstr(Vol_B, 18), bool(agree_AB)))
P('             snappy(HP)   = %s   agree=%s' % (mp.nstr(Vol_C, 18) if Vol_C else 'n/a', bool(agree_AC)))
P('             CS(complete) = %.2e  (amphichiral)  zero=%s' % (CS, CS_is_zero))
P('2) kappa=-2 vacuum re-derived in-cell (B67 trace map, exact):')
P('     Fricke on fixed locus matches B67 : %s' % fricke_ok)
P('     identity kappa = T^4-5T^2+2       : %s' % identity_ok)
P('     kappa(T=2) = %s  => the complete structure IS the kappa=-2 fiber' % kappa_at_parabolic)
P('     deformation coordinate  kappa+2 = %s' % defo_coord)
P('3) deformation law (exact series):')
P('     kappa+2 = %s u^2 + %s u^4 + ...      (meridian, T=2cosh(u/2))' % (c_u2, c_u4))
P('     kappa+2 = %s v^2 + ...   [kappa=-2cosh(v/2) exact] (longitude, L=-e^{v/2})' % c_v2)
P('     => tau^2 = (dv/du)^2 = %s = 4*(-3)  -> tau = 2 sqrt(-3)  ATOM lock=%s' % (tau_sq, atom_lock))
P('     snappy cusp shape = %s  matches 2sqrt(3)i = %s' % (cusp_shape, cusp_ok))
P('4) volume curvature  Vol(u) = Vol0 - C|u|^2 + O(u^4):')
for k_, v_ in C_est.items():
    P('     C[%-10s] = %.12f' % (k_, v_))
P('     C_mean = %.12f   spread = %.2e   stable=%s   = sqrt(3)/2 ? %s'
  % (C_mean, spread, stable, C_identified))
P('     in kappa coordinate (real-u section, leading order): Vol = Vol0 - (1/(2 sqrt3))(kappa+2)')
P('5) the scale  S(k,u) = exp(-(k/2pi) Vol(u)) = base(u)^k :')
P('     rate Vol0/2pi = %s   base = %.10f  (O(1), NOT tiny)' % (mp.nstr(rate, 12), base_f))
P('     scale at k: ' + ', '.join('k%d:%.3e' % (a, b) for a, b in scale_at_k.items()))
P('     k needed for scale < 1e-3 : %.2f  (external)' % k_for_1e3)
P('     exponent over the WHOLE deformation family (in-cell integer fillings):')
P('       min Vol = %.10f at slope %s ; max = Vol0 = %.10f ; window = %.6f'
  % (vmin, vols_sorted[0][0], vmax, window))
P('       per-level base over family in [%.4f, %.4f]  -> bounded O(1) = %s'
  % (base_range[0], base_range[1], bounded_O1))
P('       geometric slopes %d ; no geometric solution in-cell %d : %s'
  % (len(vols), len(exceptional), sorted(set(tuple(e) for e in exceptional))[:10]))
P('6) level datum / null test:')
P('     CS = 0  => no level quantization from the object : %s' % no_level_datum)
P('     identify(Vol/2pi) = %s ; pslq alg deg<=8 = %s'
  % (ident if ident else 'none', alg if alg else 'none'))
P('     pslq candidates rejected as lattice artifacts: %s'
  % [(c['deg'], c['residual_at_dps250']) for c in alg_candidates])
P('     control: |C - sqrt(3)/2| = %.2e ; identify(C, tol 1e-8) = %s'
  % (curv_delta, curv_ident if curv_ident else 'none'))
P('-' * 74)
P('VERDICT: %s    terminal = %s' % (verdict, terminal))
P('WHY: %s' % why)
P('Gate 5: structural only; no SM Higgs claim; nothing to CLAIMS; one-number pin untouched.')
txt = '\n'.join(L)
with open(os.path.join(OUT, 'output.txt'), 'w') as f:
    f.write(txt + '\n')
print(txt)
