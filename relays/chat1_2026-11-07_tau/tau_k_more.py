"""The metric's own fibre modulus at the tube along L^6 R (LR)^k, firmed up: three more members (k = 6, 7, 8) and a
fifth subdivision at k = 1 and k = 8 (P-727; the owner's "all three", its third item, "Firm up tau_infinity
directly"; data-free). Run once per member: `python3 -B tau_k_more.py m004`, then `k=1`, `k=6`, `k=7`, `k=8`; each run
prints its log and writes out_more_<member>.json beside this file. `python3 -B tau_k_more.py summary` reads those five
outputs and the sealed out_k3.json, out_k4.json and out_k5.json, and prints the checks, the predictions and the firmed
limit. run_chain_more.sh runs these and keeps each one's stdout, stderr and exit code.

PRE-REGISTRATION (written before any run of this script; the sha256 of this file, of tauinst_a3.py and of
run_chain_more.sh are recorded in prereg_more_sha256.txt and committed before the first run).

The record this card starts from (991d7e2ac; outputs f869c637d): the tube's Im tau, Richardson R4 at n <= 4, is
6.149155064, 6.081856711, 6.068679601, 6.065973881, 6.065411398 for k = 1..5, each with error about 4.2e-4 from the
n-extrapolation; the k-steps D_k = Im tau_(k+1) - Im tau_k are -0.067298353, -0.013177110, -0.002705720, -0.000562483,
with ratios 0.19580, 0.20533, 0.20789; Aitken on k = 3, 4, 5 gives 6.065263777, which the sealed card stated as
0 + 6.06526(57)i. The error is the n-extrapolation's, and it is common to the members: at k = 3, 4, 5 the tube's last
three n-steps agree to within 5e-6 (+0.07453, +0.02227, +0.00580), with step ratios about 2.46, 3.35, 3.84 approaching
the second-order 4. So this card (a) carries the k-series three members further at the same n, and (b) measures the
n-extrapolation's remainder directly with a fifth subdivision, at k = 1 (whose n <= 4 series is on record) and at
k = 8 (the member nearest the limit).

What is computed: tauinst_a3.py, which is tauinst_a2.py (amendments 1 and 2 of the sealed card) with four changes made
for this card before any of its runs (its header gives the measurements): Geo.floor is vectorised with the same
arithmetic and tie rule; the sphere closure drops products whose isometric radius exceeds the shortest cusp
translation (Shimizu's lemma); Mesh's agreement test for the horoball radii is 1e-6 relative instead of 1e-9; and
make_geo builds the polyhedron from 212-bit shapes wherever the double-precision generators differ from the 212-bit
ones by more than 1e-13 relative, which is k = 6, 7 and 8. At m004 and k = 1..5 the sealed double-precision Geo is
kept, and the floors, closed sphere sets and Ford volumes equal tauinst_a2.py's exactly, so C9 can hold to rounding.
C3 reads SnapPy's length_spectrum_alt: the sealed card's length_spectrum goes through a Dirichlet domain, whose
construction failed at k = 4 and 5 and which ran over 15 minutes at k = 6 without finishing. Everything else is the
sealed card's: R = 10.5, collocation height 0.92 x the Ford floor's minimum, cusp cross-section H = 6, r = 2 mesh
refinements, the tube level s0 = h(core) mod 1 from the systole, n 1-to-4 subdivisions with projection along grad h,
the covariant root tau = (-E12 + i sqrt(det E))/E22, and the extrapolation in n: R4 from the last two n, A3 (Aitken)
from the last three, the error |R4 - A3| + |R4 - R4'| with R4' from the two n before. k = 8's collocation matrix is
21660 x 10830 (1.9 GB, about 4.7 GB at the solve's peak), so the members run one at a time.

Members and levels: m004 at s = 1/4 and s = 0 (n <= 3), as sealed; k = 1 at s = 1/2 and s = 1/4 (n <= 3) and the tube
(n <= 5), the sealed levels in the sealed order with the tube carried one subdivision further; k = 6 and k = 7 at the
tube (n <= 4); k = 8 at the tube (n <= 5). Word: SnapPy 'b++' + 'L'*6 + 'R' + 'LR'*k. For k = 1 and k = 8, the n <= 4
part of the tube's series gives the members' values at the common depth (R4 from n = 3, 4); the whole series gives the
n <= 5 values (R4 from n = 4, 5).

Pass rules (a FAIL is reported; a member with any FAIL gives no tube value; if C1, C5 or C9 fails, no member does):
  C1  m004: some mode's |c_mu| equals B1295's 4.260982635 to < 1e-8.
  C2  every member: Ford grid volume within 2e-4 (relative) of SnapPy's; Hejhal rms residual < 1e-8; paired-face
      check < 1e-8.
  C3  k members: the systole has chi = 0 and its real length agrees with SnapPy's length_spectrum_alt (the shortest
      geodesics, without a Dirichlet domain) to 1e-6; h is constant along its axis to < 1e-8.
  C4  every surface: Euler characteristic -1, one boundary loop, no non-manifold or inconsistently oriented edge;
      |integral of alpha ^ beta| = 1 to 1e-6 at every n; |det E - 1| < 1e-3 at the finest n.
  C5  m004: tau(Sigma_1/4) within 2e-4 of i; tau(Sigma_0) with |Re| within 5e-4 of 1/2 and Im within 5e-4 of 1.12438.
  C7  k = 1: |d theta| on the core within 2e-4 of 0.04200.
  C8  m004 has 12 reversing involutions (entries in [-14, 14]), every one with both fibres != I mod 2; k = 1 has 4,
      every one with the two fibres in opposite classes.
  C9  the instrument is the sealed one: m004's two series (n = 0..3) and k = 1's three (n = 0..3, 0..3 and, for the
      tube, 0..4) equal out_m004.json's and out_k1.json's to 1e-9 in Re and Im at every n, and k = 1's core level
      equals out_k1.json's to 1e-12.

Predictions (stated now; not pass rules). v_k is the tube's Im tau (R4 at n <= 4); D_k = v_(k+1) - v_k, with v_5 the
sealed 6.065411398. Derivation: the ratio D_(k+1)/D_k rose 0.19580, 0.20533, 0.20789, its increments shrinking by
about 0.27; carried on, the ratios are about 0.2086, 0.2088, 0.2088, so D_5, D_6, D_7 are about -1.17e-4, -2.45e-5 and
-5.1e-6, and Aitken on k = 6, 7, 8 lands within 1e-6 of Aitken on k = 3, 4, 5. For the fifth subdivision: the step
ratios' distance from 4 went 1.54, 0.65, 0.16, shrinking by 2.4 and then 4, so the next step ratio is about 3.93-3.96.
  Q1  D_5 in [-1.24e-4, -1.12e-4]; D_6 in [-2.7e-5, -2.2e-5]; D_7 in [-6.5e-6, -4.0e-6].
  Q2  k = 6, 7, 8: the tube's reduced |Re tau| <= max(2 x its error, 1e-3); and every reversing involution with entries
      in [-14, 14] puts the two sigma-fixed fibres in opposite classes (B1852's even-run pattern).
  Q3  Aitken's Delta^2 on v_6, v_7, v_8 (defined when D_6 and D_7 have one sign and |D_7| < |D_6|) lies within 5e-6 of
      the sealed 6.065263777 (recomputed in the summary from out_k3.json, out_k4.json and out_k5.json).
  Q4  at k = 1 and at k = 8, the tube's fifth step: (a) rho_5 = (Im tau_4 - Im tau_3)/(Im tau_5 - Im tau_4) lies in
      [3.85, 4.05]; (b) delta = R4(n <= 5) - R4(n <= 4) lies in [-2.5e-5, +7.6e-5].
  Q5  |delta_8 - delta_1| < 1e-5 (the n-remainder does not depend on k).
  Q6  the firmed value below has error < 1e-4 and lies within the sealed 0.00057 of 6.065263777.
The firmed value (tube, Im tau): lim = Aitken on v_6, v_7, v_8 when Q3's condition holds; then
tau_inf = lim + delta_8, with error |lim - v_8| + err_8, where err_8 is k = 8's error from its whole series (n = 3, 4, 5
by the rule above); otherwise no firmed value is stated. The summary also prints lim + delta_1 as a cross-check. The
real part is not extrapolated: Q2's values are printed, with B1852's topological Re 0 at k = 1.

Disclosed before the seal:
  - every number in the record paragraph above, and the sealed card's outputs (991d7e2ac, f869c637d), including the
    tube's series at n = 0..4 for k = 1..5, were read before these predictions were written;
  - from tests outside the repository, for tauinst_a3.py and C3: on k = 6 under tauinst_a2.py's floor, the closure's
    rounds to round 2 (spheres, visible spheres, floor minimum, Ford volume) and the radii and |c| of round 3's
    products; then, for m004 and k = 1..8 under tauinst_a3.py, the polyhedron's precision (double against 212-bit
    generators; the peripheral words' errors), the closed sphere sets' sizes, the Ford volumes against SnapPy's, the
    floor minima, the systole (word, chi, complex length) against SnapPy's length_spectrum_alt, the mesh's agreement of
    horoball radii, and the run times and memory; that SnapPy's length_spectrum ran over 15 minutes at k = 6 without
    finishing; the mode counts and collocation sizes of k = 5..8; and numpy's lstsq on a random matrix of k = 6's
    collocation size, for its memory;
  - a first smoke copy on an unrelated word, L^7 R L R, which stopped at its mesh (horoball radii disagreeing by 0.35)
    after its systole search had returned a parabolic word (length 1.0e-6, just above the search's cut of 1e-6); the
    members' systoles are all 0.1849-0.1852;
  - a second smoke copy on k = 1 at an unrelated level, s = 0.3 (a surface 2.7 times the tube's at every n), to n = 5,
    printing only sizes, times and memory; and the summary's code run on copies of the sealed outputs.
No harmonic time, level or surface of k = 6, 7 or 8, and no fifth subdivision of any tube, was computed before the
seal.

Firewall: tau is a modulus of the object, not a held-out target; no measured value is read, no coupling, scale or
ratio of scales is computed, nothing is compared with data.
"""
import json, os, sys, time, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tauinst_a3 as T

R, YFRAC, HTR, RREF = 10.5, 0.92, 6.0, 2
LM, RM, I2 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))
SEALED_LIM_RULE = (3, 4, 5)


def imul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(2)) for j in range(2)) for i in range(2))


def iword(word):
    A = I2
    for ch in word:
        A = imul(A, LM if ch == 'L' else RM)
    return A


def fixed_fibre_classes(word, bound=14):
    """Every det -1 involution J (entries in [-bound, bound]) with J phi J = phi^-1; the mod-2 classes of J and phi J."""
    phi = iword(word)
    (a0, b0), (c0, d0) = phi
    phinv = ((d0, -b0), (-c0, a0))
    out = []
    for a, b, c in itertools.product(range(-bound, bound + 1), repeat=3):
        if a * a + b * c != 1:          # J = [[a, b], [c, -a]]: trace 0, det -1, so J^2 = I
            continue
        J = ((a, b), (c, -a))
        if imul(imul(J, phi), J) != phinv:
            continue
        PJ = imul(phi, J)
        is_I = lambda X: (X[0][0] % 2, X[0][1] % 2, X[1][0] % 2, X[1][1] % 2) == (1, 0, 0, 1)
        out.append(dict(J=J, J_is_I_mod2=is_I(J), phiJ_is_I_mod2=is_I(PJ)))
    return out


def series_summary(series):
    """R4 from the last two n, A3 from the last three, error |R4 - A3| + |R4 - R4'| (R4' from the two n before)."""
    t = [complex(*x['tau']) if isinstance(x['tau'], list) else complex(x['tau']) for x in series]
    im = np.array([x.imag for x in t]); re = np.array([abs(x.real) for x in t])
    def r4(v, i): return v[i] + (v[i] - v[i - 1]) / 3
    def a3(v):
        d1, d2 = v[-2] - v[-3], v[-1] - v[-2]
        return v[-1] - d2 * d2 / (d2 - d1) if abs(d2 - d1) > 1e-15 else v[-1]
    out = {}
    for lab, v in (('im', im), ('absre', re)):
        R4 = r4(v, len(v) - 1); R4p = r4(v, len(v) - 2); A3 = a3(v)
        out[lab] = float(R4); out[lab + '_A3'] = float(A3); out[lab + '_R4prev'] = float(R4p)
        out[lab + '_err'] = float(abs(R4 - A3) + abs(R4 - R4p))
        out[lab + '_finest'] = float(v[-1])
    return out


def snappy_shortest(M, cut):
    """SnapPy's shortest geodesics up to real length `cut`, by length_spectrum_alt. The sealed card's length_spectrum
    goes through a Dirichlet domain, whose construction failed at k = 4 and 5 and which took over 15 minutes at k = 6
    without finishing."""
    return M.length_spectrum_alt(max_len=cut)


def sealed(member):
    return json.load(open(os.path.join(HERE, f"out_{member}.json")))


def same_series(a, b, tol=1e-9):
    if len(a) < len(b): return False
    return all(abs(x['tau'][0] - y['tau'][0]) <= tol and abs(x['tau'][1] - y['tau'][1]) <= tol for x, y in zip(a, b))


def run(member):
    if member == 'm004':
        name, word, kk, levels = 'm004', 'LR', 0, [(0.25, 3), (0.0, 3)]
    else:
        kk = int(member.split('=')[1])
        assert kk in (1, 6, 7, 8), member
        word = 'L' * 6 + 'R' + 'LR' * kk
        name = 'b++' + word
        levels = {1: [(0.5, 3), (0.25, 3), ('core', 5)], 6: [('core', 4)], 7: [('core', 4)], 8: [('core', 5)]}[kk]
    log = lambda m: print(m, flush=True)
    t0 = time.time()
    import scipy, numba, snappy
    res = {'member': member, 'name': name, 'word': word, 'R': R, 'Yfrac': YFRAC, 'H': HTR, 'r': RREF, 'checks': {},
           'versions': dict(numpy=np.__version__, scipy=scipy.__version__, numba=numba.__version__, snappy=snappy.__version__,
                            python=sys.version.split()[0])}
    log(f"{member} ({name}); versions {res['versions']}")
    cls = fixed_fibre_classes(word)
    res['reversing_involutions'] = [dict(J=[list(r) for r in c['J']], J_is_I_mod2=c['J_is_I_mod2'],
                                         phiJ_is_I_mod2=c['phiJ_is_I_mod2']) for c in cls]
    opposite = bool(cls) and all(c['J_is_I_mod2'] != c['phiJ_is_I_mod2'] for c in cls)
    both_not_I = bool(cls) and all((not c['J_is_I_mod2']) and (not c['phiJ_is_I_mod2']) for c in cls)
    res['classes_opposite'] = opposite; res['classes_both_not_I'] = both_not_I
    log(f"  exact: {len(cls)} reversing involutions; the two fibres in opposite classes for every one: {opposite}; "
        f"both != I mod 2 for every one: {both_not_I}")
    if member == 'm004':
        res['checks']['C8'] = bool(len(cls) == 12 and both_not_I)
    if kk == 1:
        res['checks']['C8'] = bool(len(cls) == 4 and opposite)
    if kk >= 6:
        res['Q2_classes'] = opposite
    g = T.make_geo(name, wordlen=7, rmin=0.05, verbose=False)
    res['bits_prec'] = g.bits_prec; res['generator_disagreement'] = g.generator_disagreement
    log(f"  polyhedron from {'double-precision' if g.bits_prec is None else str(g.bits_prec) + '-bit'} shapes "
        f"(double against 212-bit generators: {g.generator_disagreement})")
    T.complete_spheres(g, verbose=False)
    vol, fmin = T.ford_volume(g)
    snapvol = float(g.M.volume())
    log(f"  {len(g.tets)} tetrahedra; cusp |p1| {abs(g.p1):.6f}, |p2| {abs(g.p2):.6f}; Ford volume {vol:.6f} against "
        f"SnapPy {snapvol:.6f}; floor minimum {fmin:.5f}; {len(g.sph_r)} spheres")
    H = T.Harmonic(g, R, YFRAC * fmin, verbose=False)
    fc = T.face_check(H)
    log(f"  harmonic time: {H.nm} Fourier-Bessel modes ({2 * H.nm} unknowns), rms residual {H.resid:.2e}, "
        f"paired-face check {fc:.2e} ({time.time() - t0:.0f}s)")
    res.update(tets=len(g.tets), ford_volume=float(vol), snappy_volume=snapvol, floor_min=float(fmin), modes=int(H.nm),
               hejhal_rms=float(H.resid), face_check=float(fc))
    res['checks']['C2'] = bool(abs(vol - snapvol) < 2e-4 * snapvol and H.resid < 1e-8 and fc < 1e-8)
    if member == 'm004':
        cm = np.sqrt(H.coef[:H.nm] ** 2 + H.coef[H.nm:] ** 2) / 2
        c0 = float(cm[np.argmin(np.abs(cm - 4.260982635))])
        res['B1295_coefficient'] = c0
        res['checks']['C1'] = bool(abs(c0 - 4.260982635) < 1e-8)
        log(f"  C1: B1295's coefficient reproduced as {c0:.10f}")
    s0 = None
    if kk >= 1:
        Lc, w, A = T.systole(g)
        spec = snappy_shortest(g.M, float(Lc.real) + 0.05)
        snapL = complex(spec[0].length) if len(spec) else complex('nan')
        wa, za = T.axis_points(A)
        hv = H(wa, za)
        gr = T.core_gradient(H, wa[::10], za[::10])
        chi_s = int(T.word_chi(g, w))
        res.update(systole_word=w, systole_chi=chi_s, systole_length=[float(Lc.real), float(Lc.imag)],
                   snappy_systole=[snapL.real, snapL.imag], core_h=float(hv.mean()), core_h_spread=float(np.ptp(hv)),
                   core_grad=float(gr.mean()), core_grad_spread=float(np.ptp(gr)))
        res['checks']['C3'] = bool(chi_s == 0 and abs(Lc.real - snapL.real) < 1e-6 and np.ptp(hv) < 1e-8)
        s0 = float(hv.mean() % 1.0)
        if abs(s0 - 1.0) < 1e-6: s0 = s0 - 1.0
        res['core_level'] = s0
        log(f"  systole {w} (chi {chi_s}): complex length {Lc.real:.8f} {Lc.imag:+.8f}i, SnapPy {snapL.real:.8f} "
            f"{snapL.imag:+.8f}i; h on its axis {hv.mean():.12f} (spread {np.ptp(hv):.1e}); "
            f"|d theta| there {gr.mean():.6f}")
        if kk == 1:
            res['checks']['C7'] = bool(abs(gr.mean() - 0.04200) < 2e-4)
    Ms = T.Mesh(g, HTR, RREF, verbose=False)
    vals = T.node_values(Ms, H)
    log(f"  mesh and node values ({time.time() - t0:.0f}s)")
    res['levels'] = []
    c4 = True
    for lab, nsub in levels:
        s = s0 if lab == 'core' else lab
        t1 = time.time()
        out = T.surface_series(Ms, H, s, vals, nsub, log=log)
        ck = out['check']
        ok = (ck['chi'] == -1 and ck['loops'] == 1 and ck['nonmanifold'] == 0 and ck['inconsistent'] == 0 and
              all(abs(abs(x['cup']) - 1) < 1e-6 for x in out['series']) and abs(out['series'][-1]['detE'] - 1) < 1e-3)
        c4 = c4 and ok
        ser = [{'n': int(x['n']), 'F': int(x['F']), 'detE': float(x['detE']), 'cup': float(x['cup']),
                'tau': [complex(x['tau']).real, complex(x['tau']).imag]} for x in out['series']]
        rec = {'level': lab if isinstance(lab, str) else float(lab), 's': float(s), 'check': ck,
               'snapped': int(out['snapped']), 'series': ser, 'extrapolated': series_summary(ser), 'C4': bool(ok),
               'seconds': time.time() - t1}
        if nsub == 5:
            rec['extrapolated_n4'] = series_summary(ser[:5])
        res['levels'].append(rec)
        summ = rec['extrapolated']
        log(f"  level {lab} (s = {s:.12f}): Im tau = {summ['im']:.7f} +- {summ['im_err']:.7f} (finest {summ['im_finest']:.7f}, "
            f"A3 {summ['im_A3']:.7f}); |Re tau| = {summ['absre']:.2e} +- {summ['absre_err']:.2e}; C4 {'PASS' if ok else 'FAIL'} "
            f"({time.time() - t1:.0f}s)")
    res['checks']['C4'] = bool(c4)
    def lv(x):
        return next(r for r in res['levels'] if r['level'] == x)
    if member == 'm004':
        q, z = lv(0.25)['extrapolated'], lv(0.0)['extrapolated']
        res['checks']['C5'] = bool(abs(q['im'] - 1) < 2e-4 and q['absre'] < 2e-4 and abs(z['absre'] - 0.5) < 5e-4 and
                                   abs(z['im'] - 1.12438) < 5e-4)
        old = sealed('m004')
        res['checks']['C9'] = bool(all(same_series(lv(x)['series'], next(r for r in old['levels'] if r['level'] == x)['series'])
                                       for x in (0.25, 0.0)))
    if kk == 1:
        old = sealed('k1')
        res['checks']['C9'] = bool(all(same_series(lv(x)['series'], next(r for r in old['levels'] if r['level'] == x)['series'])
                                       for x in (0.5, 0.25, 'core')) and abs(s0 - old['core_level']) <= 1e-12)
    if kk >= 6:
        tube = lv('core')['extrapolated']
        res['Q2_re'] = bool(tube['absre'] <= max(2 * tube['absre_err'], 1e-3))
    res['seconds'] = time.time() - t0
    log(f"  checks: {res['checks']}; total {res['seconds']:.0f}s")
    with open(os.path.join(HERE, f"out_more_{member.replace('=', '')}.json"), 'w') as f:
        json.dump(res, f, indent=1)


def aitken(v):
    d1, d2 = v[1] - v[0], v[2] - v[1]
    if d1 * d2 > 0 and abs(d2) < abs(d1):
        return v[2] - d2 * d2 / (d2 - d1)
    return None


def summary():
    out = {m: json.load(open(os.path.join(HERE, f'out_more_{m}.json'))) for m in ('m004', 'k1', 'k6', 'k7', 'k8')}
    m = out['m004']
    gate = all(m['checks'].get(c, False) for c in ('C1', 'C5', 'C9')) and out['k1']['checks'].get('C9', False)
    print(f"m004: checks {m['checks']}; k = 1: checks {out['k1']['checks']}; C1, C5 and C9 {'PASS' if gate else 'FAIL'}")
    tube = {}
    for k in (1, 6, 7, 8):
        r = out[f'k{k}']
        lev = next(x for x in r['levels'] if x['level'] == 'core')
        ok = gate and all(r['checks'].values())
        e4 = lev.get('extrapolated_n4', lev['extrapolated'])
        tube[k] = dict(ok=ok, n4=e4, full=lev['extrapolated'], series=lev['series'])
        extra = f"; Q2 classes {r['Q2_classes']}, Q2 real part {r['Q2_re']}" if k >= 6 else ''
        print(f"k = {k}: checks {r['checks']} -> {'used' if ok else 'NOT USED'}; core level {r['core_level']:+.3e}; "
              f"tube (n <= 4) Im {e4['im']:.9f} +- {e4['im_err']:.7f}, |Re| {e4['absre']:.2e} +- {e4['absre_err']:.2e}{extra}")
    old = {k: next(x for x in sealed(f'k{k}')['levels'] if x['level'] == 'core')['extrapolated']['im'] for k in SEALED_LIM_RULE}
    lim_sealed = aitken([old[k] for k in SEALED_LIM_RULE])
    print(f"sealed: Im tau at k = 3, 4, 5 {old[3]:.9f}, {old[4]:.9f}, {old[5]:.9f}; Aitken {lim_sealed:.9f}")
    if not all(tube[k]['ok'] for k in (6, 7, 8)):
        print("k = 6, 7, 8 not all usable; no k-series, no limit, no firmed value stated"); return
    v = {5: old[5], 6: tube[6]['n4']['im'], 7: tube[7]['n4']['im'], 8: tube[8]['n4']['im']}
    D = {k: v[k + 1] - v[k] for k in (5, 6, 7)}
    q1 = (-1.24e-4 <= D[5] <= -1.12e-4) and (-2.7e-5 <= D[6] <= -2.2e-5) and (-6.5e-6 <= D[7] <= -4.0e-6)
    print(f"k-steps (n <= 4): D5 {D[5]:+.4e}, D6 {D[6]:+.4e}, D7 {D[7]:+.4e}; ratios {D[6] / D[5]:.5f}, {D[7] / D[6]:.5f}; Q1 {q1}")
    q2 = all(out[f'k{k}']['Q2_classes'] and out[f'k{k}']['Q2_re'] for k in (6, 7, 8))
    print(f"Q2 (k = 6, 7, 8: |Re tau| at the tube and the exact classes) {q2}")
    lim = aitken([v[6], v[7], v[8]])
    if lim is None:
        print(f"Q3: D6 {D[6]:+.3e} and D7 {D[7]:+.3e} do not shrink with one sign; no limit, no firmed value stated"); return
    q3 = abs(lim - lim_sealed) < 5e-6
    print(f"Aitken on k = 6, 7, 8 (n <= 4): {lim:.9f}; minus the sealed {lim - lim_sealed:+.2e}; Q3 {q3}")
    dl = {}
    for k in (1, 8):
        ser = tube[k]['series']
        im = [x['tau'][1] for x in ser]
        rho5 = (im[4] - im[3]) / (im[5] - im[4])
        dl[k] = tube[k]['full']['im'] - tube[k]['n4']['im']
        q4 = (3.85 <= rho5 <= 4.05) and (-2.5e-5 <= dl[k] <= 7.6e-5)
        print(f"k = {k}, fifth subdivision: Im tau at n = 3, 4, 5 {im[3]:.7f}, {im[4]:.7f}, {im[5]:.7f}; rho5 {rho5:.4f}; "
              f"R4(n <= 5) {tube[k]['full']['im']:.9f} +- {tube[k]['full']['im_err']:.7f} (A3 {tube[k]['full']['im_A3']:.9f}); "
              f"delta {dl[k]:+.3e}; Q4 {q4}")
    q5 = abs(dl[8] - dl[1]) < 1e-5
    print(f"delta_8 - delta_1 {dl[8] - dl[1]:+.2e}; Q5 {q5}")
    firmed = lim + dl[8]
    err = abs(lim - v[8]) + tube[8]['full']['im_err']
    q6 = err < 1e-4 and abs(firmed - lim_sealed) < 0.00057
    print(f"firmed: Im tau_inf = {firmed:.7f} +- {err:.7f} (Aitken {lim:.9f} + delta_8 {dl[8]:+.3e}; k part {abs(lim - v[8]):.2e}, "
          f"n part {tube[8]['full']['im_err']:.2e}); cross-check with delta_1: {lim + dl[1]:.7f}; Q6 {q6}")
    print(f"real part: |Re tau| at the tube, k = 6, 7, 8: " +
          ", ".join(f"{tube[k]['n4']['absre']:.2e} +- {tube[k]['n4']['absre_err']:.2e}" for k in (6, 7, 8)))


if __name__ == '__main__':
    if sys.argv[1] == 'summary':
        summary()
    else:
        run(sys.argv[1])
