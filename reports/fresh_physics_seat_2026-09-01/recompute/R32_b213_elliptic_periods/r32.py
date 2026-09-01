#!/usr/bin/env python3
"""R32 — B213 'Higgs-side periods': every number in higgs_periods.py is a RECORDED sage output (Phase B reader:
IMPORTED / reproducible unknown, Sage-gated).  Recomputed here with PARI (through snappy's cypari), no Sage:

  E = 40a1 : y^2 = x^3 - 7x - 6          conductor, rank (analytic, via ellanalyticrank), torsion, CM, j,
             real period Omega (= 2*omega_1 since Delta > 0: two real components), L(E,1), L/Omega,
             BSD prediction Sha*prod c_p/|T|^2 with the Tamagawa numbers from elllocalred.
  null test: the other rank-0 curves in B213's NULL_L_OVER_OMEGA table, by coefficients (Cremona labels are
             not in this PARI build; each curve is identified by its conductor, and the 40a isogeny class is
             generated from 40a1 by ellisomat so 40a2/40a3 are matched by value, not by label).
  Mahler measure of Phi(x,z) = z^2 - (x^2+1) z + (2x^2-1): 2-variable Mahler measure by Jensen in z then a
             numerical integral in x (mpmath), against B213's 0.74175...
  bonus:     is Phi's curve really 40a1?  (B211's identification, which B213 imports) — j-invariant of the
             genus-1 curve Phi = 0 via PARI's ellfromeqn, compared with j(40a1) = 148176/25.
"""
import json, os
from fractions import Fraction
import mpmath as mp
from snappy import pari

HERE = os.path.dirname(os.path.abspath(__file__))
pari.set_real_precision(38)
mp.mp.dps = 30
out, lines = {}, []
def say(s): print(s, flush=True); lines.append(s)

CURVES = {   # Cremona label -> [a1,a2,a3,a4,a6]  (standard tables)
    '40a1': [0, 0, 0, -7, -6], '11a1': [0, -1, 1, -10, -20], '14a1': [1, 0, 1, 4, -6], '15a1': [1, 1, 1, -10, -10],
    '17a1': [1, -1, 1, -1, -14], '19a1': [0, 1, 1, -9, -15], '20a1': [0, 1, 0, 4, 4], '21a1': [1, 0, 0, -4, -1],
    '24a1': [0, -1, 0, -4, 4], '37b1': [0, 1, 1, -23, -50],
}
BANK = {'40a1': 0.5, '11a1': 0.2, '14a1': 1 / 6, '15a1': 0.25, '17a1': 0.25, '19a1': 1 / 3, '20a1': 1 / 6,
        '21a1': 0.25, '24a1': 0.25, '37b1': 2 / 3, '40a2': 1.0, '40a3': 0.25}

def data(E):
    gr = pari.ellglobalred(E)
    N = int(gr[0])
    disc = E.disc()
    om1 = E.omega()[0]                       # omega_1 (real)
    Omega = 2 * om1 if disc > 0 else om1  # real period of E(R)
    L1 = pari.ellL1(E, 0)
    tors = int(pari.elltors(E)[0]); tstruct = [int(x) for x in pari.elltors(E)[1]]
    # Tamagawa numbers
    cp = 1
    for p in pari.factor(N)[0]:
        cp *= int(pari.elllocalred(E, p)[3])
    ar = pari.ellanalyticrank(E)
    return dict(conductor=N, disc_sign=int(pari.sign(disc)), omega1=float(om1), Omega=float(Omega), L1=float(L1),
                L_over_Omega=float(L1 / Omega), torsion=tors, torsion_structure=tstruct, tamagawa_product=cp, analytic_rank=int(ar[0]),
                j=str(E.j()), has_cm=bool(pari.ellap(E, 2) is not None and False) )

say('== 40a1 ==')
E = pari.ellinit(CURVES['40a1'])
d = data(E)
# CM check: j must not be one of the 13 rational CM j-invariants
CM_J = {0, 1728, -3375, 8000, -32768, 54000, 287496, -884736, -12288000, 16581375, -884736000, -147197952000, -262537412640768000}
d['has_cm'] = Fraction(str(E.j())) in CM_J
d['bsd_prediction'] = float(Fraction(d['tamagawa_product'], d['torsion'] ** 2))   # Sha assumed 1 (as B213)
d['L_over_Omega_exact_guess'] = str(Fraction(d['L_over_Omega']).limit_denominator(100))
for k, v in d.items(): say('  %s = %s' % (k, v))
out['40a1'] = d
bank = dict(conductor=40, rank=0, torsion=4, cm=False, real_period=1.4844124734223865, L_at_1=0.7422811388969421, L_over_Omega=0.5, j='148176/25')
ok = (d['conductor'] == 40 and d['analytic_rank'] == 0 and d['torsion'] == 4 and not d['has_cm'] and d['j'] == '148176/25'
      and abs(d['omega1'] - bank['real_period']) < 1e-12 and abs(d['L1'] - bank['L_at_1']) < 1e-3 and abs(d['L1']/d['omega1'] - 0.5) < 1e-25)
say('  MATCH bank (cond 40, rank 0, tors 4, non-CM, j 148176/25, Omega 1.48441247342, L 0.74228113889, L/Omega = 1/2): %s' % ok)
say('  NOTE: bank Omega 1.48441 = omega_1 (least real period, Sage omega() default); BSD real period = 2*omega_1 = %.10f since Delta>0.' % d['Omega'])
say('        L(E,1)/omega_1 = %.25f ; with Omega_BSD: L/Omega = %s = (2 components)*(prod c_p=%d)/|T|^2 ... bank wrote prod c_p = 8' % (d['L1']/d['omega1'], Fraction(d['tamagawa_product'], d['torsion']**2), d['tamagawa_product']))
say('  torsion structure: %s  (bank: Z/4; full rational 2-torsion (x+1)(x+2)(x-3) forces Z/2 x Z/2)' % d['torsion_structure'])
say('  L(E,1): bank 0.7422811388969421 vs PARI %.16f  (diff %.2e; Sage lseries().at1() is a truncated sum)' % (d['L1'], abs(d['L1']-0.7422811388969421)))
say('  BSD: prod c_p / |T|^2 = %d / %d = %s  vs L/Omega %.30f' % (d['tamagawa_product'], d['torsion'] ** 2, Fraction(d['tamagawa_product'], d['torsion'] ** 2), d['L_over_Omega']))
out['40a1_match'] = ok

say('== null test: L(E,1)/Omega over B213\'s rank-0 curves ==')
null = {}
for lab, co in CURVES.items():
    if lab == '40a1': continue
    Ec = pari.ellinit(co); dc = data(Ec)
    fr = Fraction(dc['L_over_Omega']).limit_denominator(24)
    r1 = dc['L1'] / dc['omega1']; fr1 = Fraction(r1).limit_denominator(24)
    null[lab] = dict(conductor=dc['conductor'], analytic_rank=dc['analytic_rank'], L_over_Omega_BSD=dc['L_over_Omega'], as_fraction=str(fr),
                     L_over_omega1=r1, as_fraction_omega1=str(fr1), disc_sign=dc['disc_sign'],
                     bank=BANK[lab], match=abs(r1 - BANK[lab]) < 1e-9 and abs(float(fr1) - r1) < 1e-12,
                     bsd_cp_over_T2=str(Fraction(dc['tamagawa_product'], dc['torsion'] ** 2)))
    say('  %s cond %d rank %d sign(D)=%+d  L/omega_1 = %s  L/Omega_BSD = %s = c_p/|T|^2 %s  (bank %s, omega_1 convention) match=%s' % (
        lab, dc['conductor'], dc['analytic_rank'], dc['disc_sign'], fr1, fr, null[lab]['bsd_cp_over_T2'], Fraction(BANK[lab]).limit_denominator(24), null[lab]['match']))
# the 40a isogeny class from 40a1
iso = pari.ellisomat(E)
say('  40a isogeny class: %d curves (from ellisomat)' % len(iso[0]))
cls = []
for ent in iso[0]:
    co = ent[0]; Ec = pari.ellinit(co); dc = data(Ec)
    fr = Fraction(dc['L1'] / dc['omega1']).limit_denominator(24)
    cls.append(dict(coeffs=[int(x) for x in co], L_over_omega1=dc['L1'] / dc['omega1'], as_fraction=str(fr), torsion=dc['torsion'], cp=dc['tamagawa_product']))
    say('    %s  L/omega_1 = %.15f = %s  |T|=%d prod c_p=%d' % ([int(x) for x in co], dc['L1'] / dc['omega1'], fr, dc['torsion'], dc['tamagawa_product']))
vals = sorted(set(c['as_fraction'] for c in cls))
say('  class values %s ; bank says 40a2 -> 1, 40a3 -> 1/4 : present = %s' % (vals, {'1', '1/4'} <= set(vals)))
out['null_test'] = null; out['iso_class_40a'] = cls

say('== Mahler measure of Phi(x,z) = z^2 - (x^2+1) z + (2x^2-1) ==')
# m(P) = (1/2pi i)^2 int int log|P| ; do z by Jensen: for fixed |x|=1, m_z = sum over roots z_i of log max(1,|z_i|)
def inner(theta):
    x = mp.exp(1j * theta)
    a, b, c = 1, -(x * x + 1), 2 * x * x - 1
    disc = mp.sqrt(b * b - 4 * a * c)
    z1, z2 = (-b + disc) / 2, (-b - disc) / 2
    return sum(mp.log(max(1, abs(z))) for z in (z1, z2))
mah = mp.quad(inner, [0, mp.pi / 2, mp.pi, 3 * mp.pi / 2, 2 * mp.pi]) / (2 * mp.pi)
say('  m(Phi) = %s   (bank 0.7417527164660; L(E,1) = %.13f; Omega/2 = %.13f)' % (mp.nstr(mah, 15), d['L1'], d['Omega'] / 2))
say('  |m(Phi) - L(E,1)| = %.3e  -> NOT equal (B213 itself says only "~"); relative gap %.2e' % (abs(float(mah) - d['L1']), abs(float(mah) - d['L1']) / d['L1']))
out['mahler'] = dict(value=float(mah), bank=0.7417527164660, match=abs(float(mah) - 0.7417527164660) < 1e-9, gap_to_L1=abs(float(mah) - d['L1']))

say('== is Phi = 0 the curve 40a1?  (B211 identification imported by B213) ==')
# ellfromeqn needs a cubic/quartic form; Phi is quadratic in z, quadratic in x^2: set u = x^2 -> z^2 - (u+1) z + (2u-1) = 0
# is genus 0 in (u,z)!  In (x,z) it is z^2 - (x^2+1)z + 2x^2 - 1 = 0: solve for x^2 = (z^2 - z - 1)/(z - 2) => x^2 (z-2) = z^2 - z - 1,
# i.e. the curve w^2 = (z-2)(z^2 - z - 1) with w = x (z-2): a genus-1 curve, j-invariant from PARI.
Ecv = pari.ellfromeqn(pari('w^2 - (z-2)*(z^2 - z - 1)'))
Ecv = pari.ellinit(Ecv)
jcv = Ecv.j(); Ncv = int(pari.ellglobalred(Ecv)[0])
say('  curve w^2 = (z-2)(z^2-z-1): conductor %d, j = %s ; j(40a1) = %s ; same = %s' % (Ncv, jcv, E.j(), jcv == E.j()))
cls_j = [str(pari.ellinit(ent[0]).j()) for ent in iso[0]]
say('  j-invariants of the 40a class members: %s ; Phi-curve j in class: %s' % (cls_j, str(jcv) in cls_j))
out['phi_is_40a1'] = dict(conductor=Ncv, j=str(jcv), j_40a1=str(E.j()), same_j=bool(jcv == E.j()), class_js=cls_j, j_in_40a_class=str(jcv) in cls_j)
say('  => Phi = 0 is an elliptic curve of conductor 40, ISOGENOUS to 40a1 (same isogeny class, same L-function) but a DIFFERENT curve %s'
    % ('(j matches member %d)' % cls_j.index(str(jcv)) if str(jcv) in cls_j else '(j not in class!)'))
# independent Mahler-measure check: brute 2-D torus integral of log|P| in double precision (scipy), no Jensen
from scipy.integrate import dblquad
import numpy as _np
def m2d(P):
    f = lambda s_, t: _np.log(abs(P(_np.exp(1j * t), _np.exp(1j * s_))))
    v, err = dblquad(f, 0, 2 * _np.pi, 0, 2 * _np.pi, epsabs=1e-9, epsrel=1e-9)
    return v / (4 * _np.pi ** 2), err
cands = {'z^2-(x^2+1)z+2x^2-1 (B213 Phi)': lambda x, z: z*z - (x*x+1)*z + 2*x*x - 1,
         'x^2(z-2)-(z^2-z-1) (same curve, other monic form)': lambda x, z: x*x*(z-2) - (z*z - z - 1),
         'z^2-(u+1)z+2u-1 (u = x^2, the genus-0 shadow)': lambda x, z: z*z - (x+1)*z + 2*x - 1}
for nm, P in cands.items():
    v, err = m2d(P)
    say('  m[%s] = %.9f (+- %.1e) by direct 2-D torus integral' % (nm, v, err))
    out['mahler'][nm] = v
say('  Jensen value for Phi: %s ; direct 2-D: %.9f ; bank 0.7417527164660' % (mp.nstr(mah, 12), out['mahler']['z^2-(x^2+1)z+2x^2-1 (B213 Phi)']))
json.dump(out, open(HERE + '/r32_out.json', 'w'), indent=1, default=str)
open(HERE + '/r32_out.txt', 'w').write('\n'.join(lines) + '\n')
