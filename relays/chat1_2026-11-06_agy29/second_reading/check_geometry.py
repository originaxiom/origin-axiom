#!/usr/bin/env python3
"""
verify_agy29/check_geometry.py -- independent SnapPy check of agy Stage 29's geometric claims (1, 3, 5a-5c, 5e) and of 9(a)'s CS premise.

PRE-REGISTERED: this header (predictions + pass rules) was written before any run; its sha256 is recorded in
prereg_sha256.txt before the first run. Smoke runs only on a reduced copy (smoke_check_geometry.py: K_LIST=[1], no N_LIST).

DATA-FREE. Only hyperbolic geometry is computed: tetrahedron shapes, complex lengths of closed geodesics, volumes,
cusp translations, Chern-Simons invariants, the axis height of a monodromy matrix. No measured quantity, no held-out
target, no scale ratio, coupling, CKM or CP value is computed. Nothing here evaluates exp(+-k*Vol/2pi), alpha or
Lambda/mu*. agy's code is not imported or run; its typed constants (complex lengths and shapes, read through the geo
mask, lines 28069 and 28100-28106, and its polynomial, lines 28044-28055 / 28528) are copied here by hand.

DISCLOSURE (not blind): before writing this header I saw, by accident, main's one-line S306d commit subject saying it
verified Theorem 154's coth^2 identity to 2.6e-13. Prediction G2 is therefore not blind.

Manifolds: snappy 3.3.2, ManifoldHP('b++LLLLLLR' + 'LR'*k) for k in K_LIST = 1..12; exploratory 'b++' + 'L'*n + 'RLR'
for n in N_LIST = (4, 8, 10); m004 (and m003, m015 for the CS premise).

PREDICTIONS AND PASS RULES
G1 (claim 1, the tube's size). L(k) := complex length of the shortest closed geodesic (Re > 0, Im in (-pi, pi]).
   Pass rule: "size never changes with k" is TRUE iff max_k |L(k) - L(1)| < 1e-8.
   Prediction: FALSE as an exact statement; L(k) converges (|L(k) - L(12)| decreasing in k), and Re L(k) stays in
   [0.18, 0.19] for every k (the tube does not dilute).
G2 (claim 5c, the identity z3 = coth^2(L_tube/2)). w(k) := coth^2(L(k)/2).
   Pass rule: HOLDS at k iff an edge parameter zeta in {z, 1/(1-z), 1-1/z} of the middle fan tetrahedron (index 3) has
   |w - zeta| < 1e-30 (HP; if an HP step fails and double precision is used instead, the tolerance is 1e-10 and the
   row is flagged). The best match over all tetrahedra (and of conj(w)) is also reported.
   Prediction: HOLDS for k = 1..12 (not blind: see disclosure).
   Exploratory, no pass rule: the same test for L^n R L R, n in (4, 8, 10), middle fan tetrahedron index n // 2.
G3 (agy's fan formulas, claimed 'for every k >= 0'). z2, z3 := the edge parameters of tets 2 and 3 minimising
   |z3 - (z2 - 1)|. Pass rule: the formulas HOLD at k iff each of |z3 - (z2 - 1)|, dist(z2, params(tet 4)),
   dist((z2-1)(z2+2)/(z2-2), params(tet 1)), dist(z2(z2^2+4z2-4)/(z2-2)^2, params(tet 0)) is < 1e-30; at k = 1 also
   dist(1 - (z0-1)(1-z1)/z0^2, params(tet 7)) and params(tet 8) < 1e-30.  Prediction: HOLD for k = 1..12.
G4 (agy's degree-8 polynomial, k = 1). P(z) = 4z^8+35z^7+94z^6-108z^5-584z^4+336z^3+1440z^2-1856z+640.
   Pass rule: P(z2(1)) = 0 iff |P(z2)| / sum_j |c_j||z2|^j < 1e-40; irreducible iff PARI polisirreducible(P) = 1.
   Prediction: both hold.
G5 (claims 5, 5a, 5b; an equality holds iff |difference| < 1e-10):
   (a) -Re z2(1) == sqrt(40/3), the record's Teichmuller apex at k = 1 (B1846 sec. 6)?  Prediction: NOT equal (~3e-4).
   (b) -Re z2(1) / sqrt(2) == Im z2(1)?  Prediction: NOT equal (~3e-3).
   (c) Im L(1) == -pi/4 (a 45-degree twist)?  Prediction: NOT equal (~2e-2 rad).
   (d) the angle of z2(1) from the negative real axis == 45 degrees?  Prediction: NOT equal (~35 degrees).
   (e) k = 1..12: -Re z2(k) against the axis apex height h_k = sqrt(tr^2 - 4) / (2|c|) of A_k = L^6 R (LR)^k in
       GENESIS's convention L = [[1,1],[0,1]], R = [[1,0],[1,1]] (h_1 = sqrt(40/3)).
       Prediction: the k = 1 near-equality does not persist: |difference| > 1e-2 for every k >= 4.
   (f) h_k == sqrt(5 F_{2k+4} / F_{2k+2}) (agy's Stage-28 apex law)?  Prediction: equal for every k; its limit
       sqrt(5)*phi differs from agy's Theorem-154 'k_inf apex' sqrt((25 + 11 sqrt 5)/4) by more than 1e-2.
G6 (claim 3, the volume near the tube). Per-tetrahedron Bloch-Wigner volumes; the shares of tet 3 and of tets 2-4.
   Pass rule: "99.7% of the local space at the waist" is supported only if some volume share at the tube is >= 0.99.
   Prediction: tet 3 ~ 0.04 and tets 2-4 ~ 0.14 at k = 1, both falling roughly like 1/k; the claim is NOT supported.
G7 (provenance of agy's typed 'SnapPy benchmark' rows, k in {1, 2, 3, 5, 8}).
   Pass rule: consistent with SnapPy iff |z3_agy - z3(k)| < 1e-12 and min(|L_agy - L(k)|, |L_agy - conj L(k)|) < 1e-12.
   Prediction: consistent.
G8 (claim 5e, the cusp). The maximal cusp (stopping displacement) of m004 and of b++LLLLLLRLR: the lengths of both
   peripheral translations and which peripheral curve has chi = 0 (chi from the relators' exponent sums, PARI matker).
   Prediction: m004: meridian 1, chi = 0 curve the longitude, length 2*sqrt(3); b++LLLLLLRLR: chi = 0 curve SnapPy's
   meridian (B1846 step1), length ~3.50267806.
G9 (claim 9a's premise: k drops from S_total iff CS = 0). Chern-Simons and amphicheirality (symmetry group) of m004,
   m003, m015 and b++LLLLLLRLR.  Prediction: m004 amphicheiral with CS = 0 (|CS| < 1e-12); at least one of the others
   chiral with |CS| > 1e-3 (so S_total = -k*CS - sigma*Vol depends on k there).
"""
import cmath
import json
import math
import os
import sys
import time

import mpmath as mp
import snappy
from cypari import pari

mp.mp.dps = 60
K_LIST = list(range(1, 13))
N_LIST = [4, 8, 10]
OUT = {}
HERE = os.path.dirname(os.path.abspath(__file__))


def mpc(x):
    """snappy Number (or python number) -> mpmath mpc at full precision."""
    if isinstance(x, (int, float, complex)):
        return mp.mpc(x)
    re = x.real()
    im = x.imag()
    return mp.mpc(mp.mpf(str(re).replace(' ', '')), mp.mpf(str(im).replace(' ', '')))


def params(z):
    return [z, 1 / (1 - z), 1 - 1 / z]


def dist_to(z, plist):
    return min(abs(z - p) for p in plist)


def bloch_wigner(z):
    return mp.im(mp.polylog(2, z)) + mp.arg(1 - z) * mp.log(abs(z))


def _spectrum(M):
    for cut in (0.6, 1.2, 2.0):
        spec = M.length_spectrum(cut)
        if len(spec) > 0:
            return spec
    raise RuntimeError('empty length spectrum up to 2.0')


def shortest_geodesic(name):
    """Return (L as mpc, flag) for the shortest closed geodesic, HP first, then double precision (flagged)."""
    try:
        spec = _spectrum(snappy.ManifoldHP(name))
        return mpc(spec[0].length), 'HP-spectrum'
    except Exception as e:  # noqa: BLE001
        err = repr(e)
    spec = _spectrum(snappy.Manifold(name))
    return mp.mpc(complex(spec[0].length)), 'double-spectrum (' + err[:60] + ')'


def norm_len(L):
    if mp.re(L) < 0:
        L = -L
    im = mp.im(L)
    while im > mp.pi:
        im -= 2 * mp.pi
    while im <= -mp.pi:
        im += 2 * mp.pi
    return mp.mpc(mp.re(L), im)


def coth2_half(L):
    return (mp.cosh(L / 2) / mp.sinh(L / 2)) ** 2


def apex_height(k):
    Lm = [[1, 1], [0, 1]]
    Rm = [[1, 0], [1, 1]]

    def mul(A, B):
        return [[A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]],
                [A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]]]
    A = [[1, 0], [0, 1]]
    for _ in range(6):
        A = mul(A, Lm)
    A = mul(A, Rm)
    for _ in range(k):
        A = mul(mul(A, Lm), Rm)
    tr = A[0][0] + A[1][1]
    c = A[1][0]
    return mp.sqrt(mp.mpf(tr * tr - 4)) / (2 * abs(c)), A


def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def tol_for(flag):
    return mp.mpf('1e-30') if flag.startswith('HP') else mp.mpf('1e-10')


def fmt(x, n=12):
    return mp.nstr(x, n)


t0 = time.time()
# ---------------- G1, G2, G3, G5(e), G6 over k ----------------
rows = []
for k in K_LIST:
    name = 'b++LLLLLLR' + 'LR' * k
    M = snappy.ManifoldHP(name)
    shapes = [mpc(z) for z in M.tetrahedra_shapes('rect')]
    vols = [bloch_wigner(z) for z in shapes]
    vol_total = mp.fsum(vols)
    vol_snappy = mp.mpf(str(M.volume()).replace(' ', ''))
    L, flag = shortest_geodesic(name)
    L = norm_len(L)
    w = coth2_half(L)
    tol = tol_for(flag)
    p3 = params(shapes[3])
    best = None
    for i, z in enumerate(shapes):
        for j, p in enumerate(params(z)):
            for which, ww in (('w', w), ('conj w', mp.conj(w))):
                d = abs(ww - p)
                if best is None or d < best[0]:
                    best = (d, i, j, which)
    d_mid = dist_to(w, p3)
    # fan formulas
    cand = []
    for z2c in params(shapes[2]):
        for z3c in params(shapes[3]):
            cand.append((abs(z3c - (z2c - 1)), z2c, z3c))
    cand.sort(key=lambda t: t[0])
    d23, z2, z3 = cand[0]
    z1f = (z2 - 1) * (z2 + 2) / (z2 - 2)
    z0f = z2 * (z2 ** 2 + 4 * z2 - 4) / (z2 - 2) ** 2
    d_tet4 = dist_to(z2, params(shapes[4]))
    d_tet1 = dist_to(z1f, params(shapes[1]))
    d_tet0 = dist_to(z0f, params(shapes[0]))
    extra = {}
    if k == 1:
        z7f = 1 - (z0f - 1) * (1 - z1f) / z0f ** 2
        extra = {'d_tet7': fmt(dist_to(z7f, params(shapes[7])), 3), 'd_tet8': fmt(dist_to(z7f, params(shapes[8])), 3)}
    fan_ok = max(d23, d_tet4, d_tet1, d_tet0) < tol
    h_k, A = apex_height(k)
    fibo = mp.sqrt(mp.mpf(5 * fib(2 * k + 4)) / fib(2 * k + 2))
    row = dict(k=k, ntet=len(shapes), flag=flag, L=fmt(L, 15), w_minus_mid=fmt(d_mid, 3),
               identity_holds=bool(d_mid < tol), best_match=(fmt(best[0], 3), best[1], best[2], best[3]),
               mid_is_min_vol_of_fan=bool(min(range(7), key=lambda i: vols[i]) == 3),
               z2=fmt(z2, 15), z3=fmt(z3, 15), d_z3_z2m1=fmt(d23, 3), d_tet4=fmt(d_tet4, 3), d_tet1=fmt(d_tet1, 3),
               d_tet0=fmt(d_tet0, 3), fan_formulas_hold=bool(fan_ok), **extra,
               vol_bw_sum=fmt(vol_total, 15), vol_snappy=fmt(vol_snappy, 15),
               share_tet3=fmt(vols[3] / vol_total, 6), share_tets234=fmt((vols[2] + vols[3] + vols[4]) / vol_total, 6),
               vol_tet3=fmt(vols[3], 6),
               neg_re_z2=fmt(-mp.re(z2), 12), apex_h_k=fmt(h_k, 12), diff_negrez2_apex=fmt(-mp.re(z2) - h_k, 6),
               A_k=A, apex_vs_fib_law=fmt(h_k - fibo, 3))
    rows.append(row)
    print(json.dumps(row), flush=True)
OUT['rows_k'] = rows

# G1 summary
L_by_k = {r['k']: mp.mpmathify(r['L']) for r in rows}
L1 = L_by_k[K_LIST[0]]
Llast = L_by_k[K_LIST[-1]]
g1 = dict(max_change_from_k1=fmt(max(abs(L_by_k[k] - L1) for k in K_LIST), 6),
          never_changes=bool(max(abs(L_by_k[k] - L1) for k in K_LIST) < mp.mpf('1e-8')),
          dist_to_last=[fmt(abs(L_by_k[k] - Llast), 3) for k in K_LIST],
          re_L_range=[fmt(min(mp.re(L_by_k[k]) for k in K_LIST), 8), fmt(max(mp.re(L_by_k[k]) for k in K_LIST), 8)],
          im_L_range_deg=[fmt(min(mp.im(L_by_k[k]) for k in K_LIST) * 180 / mp.pi, 8),
                          fmt(max(mp.im(L_by_k[k]) for k in K_LIST) * 180 / mp.pi, 8)])
OUT['G1'] = g1
print('G1', json.dumps(g1), flush=True)

# ---------------- G4, G5 (a-d, f) at k = 1 ----------------
r1 = rows[0]
z2 = mp.mpmathify(r1['z2'])
M1 = snappy.ManifoldHP('b++LLLLLLRLR')
sh1 = [mpc(z) for z in M1.tetrahedra_shapes('rect')]
cand = sorted(((abs(z3c - (z2c - 1)), z2c, z3c) for z2c in params(sh1[2]) for z3c in params(sh1[3])), key=lambda t: t[0])
z2 = cand[0][1]
coef = [640, -1856, 1440, 336, -584, -108, 94, 35, 4]  # c_0 .. c_8
Pz = mp.fsum(c * z2 ** j for j, c in enumerate(coef))
scale = mp.fsum(abs(c) * abs(z2) ** j for j, c in enumerate(coef))
irr = int(pari('polisirreducible(4*x^8+35*x^7+94*x^6-108*x^5-584*x^4+336*x^3+1440*x^2-1856*x+640)'))
L1 = mp.mpmathify(r1['L'])
g4 = dict(P_rel_resid=fmt(abs(Pz) / scale, 3), P_vanishes=bool(abs(Pz) / scale < mp.mpf('1e-40')), irreducible=bool(irr == 1))
negre = -mp.re(z2)
imz = mp.im(z2)
g5 = dict(neg_re_z2=fmt(negre, 15), sqrt_40_3=fmt(mp.sqrt(mp.mpf(40) / 3), 15),
          a_diff=fmt(negre - mp.sqrt(mp.mpf(40) / 3), 6), a_equal=bool(abs(negre - mp.sqrt(mp.mpf(40) / 3)) < 1e-10),
          b_neg_re_over_sqrt2=fmt(negre / mp.sqrt(2), 12), b_im_z2=fmt(imz, 12), b_diff=fmt(negre / mp.sqrt(2) - imz, 6),
          b_equal=bool(abs(negre / mp.sqrt(2) - imz) < 1e-10),
          c_im_L1_deg=fmt(mp.im(L1) * 180 / mp.pi, 10), c_diff_rad=fmt(mp.im(L1) + mp.pi / 4, 6),
          c_equal=bool(abs(mp.im(L1) + mp.pi / 4) < 1e-10),
          d_angle_from_neg_real_deg=fmt(mp.atan2(imz, negre) * 180 / mp.pi, 10),
          d_equal=bool(abs(mp.atan2(imz, negre) - mp.pi / 4) < 1e-10),
          f_lim_fib=fmt(mp.sqrt(5) * (1 + mp.sqrt(5)) / 2, 12), f_agy_kinf=fmt(mp.sqrt((25 + 11 * mp.sqrt(5)) / 4), 12),
          f_diff=fmt(mp.sqrt(5) * (1 + mp.sqrt(5)) / 2 - mp.sqrt((25 + 11 * mp.sqrt(5)) / 4), 6))
OUT['G4'] = g4
OUT['G5'] = g5
print('G4', json.dumps(g4), flush=True)
print('G5', json.dumps(g5), flush=True)

# ---------------- G7: agy's typed benchmark rows ----------------
agy = [(1, mp.mpc('-4.6517533689778370', '2.5789108962944680'), mp.mpc('0.1848698045116111', '-0.8021024422395611')),
       (2, mp.mpc('-4.5260956462821786', '2.4838038257403112'), mp.mpc('0.1851996322338285', '-0.8133186699528422')),
       (3, mp.mpc('-4.5008495452744164', '2.4640167035128124'), mp.mpc('0.1852176593606331', '-0.8156582629234140')),
       (5, mp.mpc('-4.4945297426528716', '2.4590068205115765'), mp.mpc('0.1852182837070880', '-0.8162495391914790')),
       (8, mp.mpc('-4.4942449545126015', '2.4587803080528716'), mp.mpc('0.1852182621335392', '-0.8162762470182559'))]
g7 = []
for k, z3a, La in agy:
    if k not in L_by_k:
        continue
    r = rows[K_LIST.index(k)]
    z3 = mp.mpmathify(r['z3'])
    Lk = L_by_k[k]
    dz = abs(z3a - z3)
    dL = min(abs(La - Lk), abs(La - mp.conj(Lk)))
    g7.append(dict(k=k, d_z3=fmt(dz, 3), d_L=fmt(dL, 3), consistent=bool(dz < 1e-12 and dL < 1e-12),
                   agy_coth2_minus_agy_z3=fmt(abs(coth2_half(La) - z3a), 3)))
OUT['G7'] = g7
print('G7', json.dumps(g7), flush=True)

# ---------------- G8: maximal cusp ----------------
g8 = []
for name in ('m004', 'b++LLLLLLRLR'):
    M = snappy.Manifold(name)
    C = M.cusp_neighborhood()
    C.set_displacement(C.stopping_displacement())
    tm, tl = C.translations()
    G = M.fundamental_group()
    gens = G.generators()
    rels = G.relators()
    E = [[r.count(g) - r.count(g.upper()) for g in gens] for r in rels]
    ker = pari('matker(Mat([' + ';'.join(','.join(str(x) for x in row) for row in E) + ']))')
    chi = [int(x) for x in ker[0]]
    per = G.peripheral_curves()[0]
    chis = [sum(chi[gens.index(c.lower())] * (1 if c.islower() else -1) for c in w) for w in per]
    g8.append(dict(name=name, meridian_len=fmt(abs(mp.mpc(complex(tm))), 12), longitude_len=fmt(abs(mp.mpc(complex(tl))), 12),
                   peripheral_words=per, chi_on_generators=chi, chi_meridian=chis[0], chi_longitude=chis[1],
                   cusp_volume=fmt(mp.mpf(float(C.volume())), 10), two_sqrt3=fmt(2 * mp.sqrt(3), 12)))
OUT['G8'] = g8
print('G8', json.dumps(g8), flush=True)

# ---------------- G9: CS and amphicheirality ----------------
g9 = []
for name in ('m004', 'm003', 'm015', 'b++LLLLLLRLR'):
    M = snappy.Manifold(name)
    cs = float(M.chern_simons())
    try:
        amph = bool(M.symmetry_group().is_amphicheiral())
    except Exception as e:  # noqa: BLE001
        amph = 'n/a ' + repr(e)[:40]
    g9.append(dict(name=name, CS=cs, amphicheiral=amph))
OUT['G9'] = g9
print('G9', json.dumps(g9), flush=True)

# ---------------- exploratory: other run lengths ----------------
expl = []
for n in N_LIST:
    name = 'b++' + 'L' * n + 'RLR'
    M = snappy.ManifoldHP(name)
    shapes = [mpc(z) for z in M.tetrahedra_shapes('rect')]
    L, flag = shortest_geodesic(name)
    L = norm_len(L)
    w = coth2_half(L)
    mid = n // 2
    best = min(((abs(w - p), i) for i, z in enumerate(shapes) for p in params(z)), key=lambda t: t[0])
    expl.append(dict(n=n, flag=flag, L=fmt(L, 12), d_mid=fmt(dist_to(w, params(shapes[mid])), 3),
                     best=(fmt(best[0], 3), best[1]), holds_at_mid=bool(dist_to(w, params(shapes[mid])) < tol_for(flag))))
OUT['explore_n'] = expl
print('EXPLORE', json.dumps(expl), flush=True)

OUT['seconds'] = round(time.time() - t0, 1)
with open(os.path.join(HERE, 'check_geometry_out.json'), 'w') as f:
    json.dump(OUT, f, indent=1, default=str)
print('done', OUT['seconds'], 's')
