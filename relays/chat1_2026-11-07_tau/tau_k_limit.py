"""The metric's own fibre modulus at the tube along L^6 R (LR)^k, k = 1..5, toward k -> infinity (P-727; the owner's
"tau's k -> infinity limit"; data-free). Run once per member: `python3 -B tau_k_limit.py m004`, then
`python3 -B tau_k_limit.py k=1` ... `k=5`; each run prints its log and writes out_<member>.json beside this file.
`python3 -B tau_k_limit.py summary` reads the six outputs and prints the k-series, P1-P5 and the limit. run_chain.sh
runs these and keeps each one's stdout, stderr and exit code.

PRE-REGISTRATION (written before any run of this script; the sha256 of this file, of tauinst.py and of run_chain.sh are
recorded in prereg_sha256.txt and committed before the first run).

What is computed (the instrument is tauinst.py; nothing in it reads a measured value):
  - harmonic time h on the member M: the harmonic map M -> R/Z in the fibre class, by Hejhal collocation in the cusp's
    Fourier-Bessel expansion at pulled-back points (R = 10.5 for every member; collocation height 0.92 x the Ford floor's
    minimum; no constant term, so h's additive constant is the cusp gauge), the Ford sphere set closed under products of
    floor-visible elements;
  - the tube's core (k members): the systole (shortest closed geodesic over words of length <= 6 in SnapPy's simplified
    generators), its chi, h along its axis, |d theta| there; the tube level s0 = h(core) mod 1 and sigma's other fixed
    level, the anti-apex s0 + 1/2;
  - the level surface Sigma_s = {h = s mod 1}: marching tetrahedra on an intrinsic simplicial mesh of the truncated
    manifold (SnapPy's ideal tetrahedra, cusp cross-section at height H = 6 in the maximal-cusp normalisation, r = 2
    refinements), exact crossings, a node within max(1e-6, 1e-2 x the largest |delta h| on its mesh edges) of the level
    snapped and re-projected (no crossing within 1 % of an edge's end); then n = 0..N 1-to-4 subdivisions with each new
    vertex projected onto the exact level along grad h (N = 4 at the tube, N = 3 elsewhere);
  - its conformal modulus at each n: cone over the cusp hole, intrinsic Delaunay flips, cotangent Laplacian,
    tree-cotree cohomology basis, harmonic 1-forms, energy matrix E, tau the root in the upper half-plane of
    E22 t^2 + 2 E12 t + E11, that is (-E12 + i sqrt(det E))/E22 (covariant under a change of the cycle basis; it is
    (-E12 + i)/E22 when det E = 1), oriented by the integral of alpha ^ beta, reduced to the standard fundamental domain;
  - extrapolation in n, for Im tau and |Re tau| separately: Richardson with ratio 4 from the last two n (R4) and Aitken's
    three-point estimate from the last three n (A3); the reported value is R4, its error |R4 - A3| + |R4 - R4'|, where
    R4' is Richardson from the two n before;
  - exact, in integers (B1852's method; the record's L = [[1,1],[0,1]], R = [[1,0],[1,1]]): every det -1 involution J
    with entries in [-14, 14] and J phi J = phi^-1, and the classes mod 2 of J and phi J (the two sigma-fixed fibres;
    J = I mod 2 puts that fibre's tau on Re tau = 0, J != I mod 2 on Re tau = 1/2 or |tau| = 1).

Members: m004 (control, word LR); L^6 R (LR)^k for k = 1..5 (SnapPy 'b++' + 'L'*6 + 'R' + 'LR'*k). Levels: m004 at
s = 1/4 and s = 0; k = 1 at s = 1/2, s = 1/4 and the tube s0; k = 2..5 at the tube s0 and the anti-apex s0 + 1/2.

Pass rules (a FAIL is reported; a member with any FAIL gives no tube value; if C1 or C5 fails, no member does):
  C1  m004: some mode's |c_mu| (complex-exponential normalisation) equals B1295's 4.260982635 to < 1e-8.
  C2  every member: the Ford domain's grid volume within 2e-4 (relative) of SnapPy's; Hejhal's rms residual < 1e-8;
      the paired-face check (h at x and at g x on paired floor faces, both evaluated directly, less chi(g)) < 1e-8.
  C3  k members: the systole has chi = 0 and its real length agrees with SnapPy's length spectrum to 1e-6; h is
      constant along its axis to < 1e-8.
  C4  every surface: Euler characteristic -1, one boundary loop, no non-manifold or inconsistently oriented edge;
      |integral of alpha ^ beta| = 1 to 1e-6 at every n; |det E - 1| < 1e-3 at the finest n.
  C5  m004 (B1847 section 3): tau(Sigma_1/4) within 2e-4 of i; tau(Sigma_0) with |Re| within 5e-4 of 1/2 and Im within
      5e-4 of 1.12438.
  C6  k = 1 (B1847 section 4): at s = 1/2, |Re| within 1e-3 of 1/2 and Im within 2e-3 of 1.5904; at s = 1/4, |Re|
      within 2e-3 of 0.3722 and Im within 2e-3 of 1.0085 (|Re| is compared: the sign of Re depends on an orientation
      convention).
  C7  k = 1: |d theta| on the core within 2e-4 of B1847 section 8's 0.04200.
  C8  the exact classes reproduce B1852's table: m004 has 12 reversing involutions, every one with both fibres != I
      mod 2; k = 1 has 4, every one with the two fibres in opposite classes.

Predictions (stated now; not pass rules):
  P1  k = 1: Im tau(Sigma_s0) lies inside B1847 section 8's 6.15 +- 0.15.
  P2  every k member: the tube's reduced Re tau is 0 (B1852 for k = 1) and, for k = 2..5, the anti-apex's |Re tau| is
      1/2; each within max(2 x its error, 1e-3).
  P3  every k member: the core's level is an integer in the cusp gauge (s0 = 0).
  P4  |Im tau_(k+1) - Im tau_k| at the tube decreases with k, and |Im tau_5 - Im tau_4| < 1 % of Im tau_5.
  P5  k = 2..5: every reversing involution puts the two fibres in opposite classes (B1852's even-run pattern: these
      words have one even run, L^6).
The k -> infinity estimate (tube, Im tau): Aitken's Delta^2 on k = 3, 4, 5 if the two differences have the same sign and
shrink, with error |lim - Im tau_5| + max(error at k = 3, 4, 5); otherwise no limit is stated. The same estimate
(k = 3, 4, 5) is printed for the anti-apex as a secondary.

Disclosed before the seal: the instrument was developed on m004 (s = 1/4, 0) and on L^6 R L R at s = 1/4 and 1/2, and
the k = 1 core's chi, h and |d theta| were computed in development; no tube level of any member and no anti-apex of
k = 2..5 was extracted. B1847's numbers (including 6.15 +- 0.15) and B1852's result (Re tau = 0 at the k = 1 tube, its
table, its even-run pattern) were read before these predictions were written. This instrument's orientation is the
mirror of main's at s = 1/4, so |Re| is compared. Three faults found by a reduced smoke copy were fixed in tauinst.py
before the seal. (1) The subdivision shared one projected midpoint per (frame, vertex pair), which on a frame whose
faces are glued to each other gave one copy of an edge the other copy's midpoint (the n >= 1 moduli at sigma-fixed
levels blew up). (2) Needles from nodes just outside the old 1e-6 snapping band; the per-node band removes them.
(3) tau = (-E12 + i)/E22, the development formula (and B1847's), depends on the order of the two cycles at the size of
det E - 1: a 1e-13 shift of s reordered them and moved the n = 1 modulus at k = 1's s = 1/2 by 6e-3. The covariant root
above removes this; under 1e-12 perturbations of every length the reduced tau no longer changes. The control levels'
series under the final instrument were seen before the seal (m004 at s = 0 and 1/4 to n = 3, k = 1 at s = 1/4 to n = 3
and at s = 1/2 to n = 2), and the faults were fixed until they agreed with main, so C5 and C6 test agreement with
B1847, not a blind prediction.

Firewall: tau is a modulus of the object, not a held-out target; no measured value is read, no coupling, scale or
ratio of scales is computed, nothing is compared with data.
"""
import json, os, sys, time, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import tauinst as T

R, YFRAC, HTR, RREF = 10.5, 0.92, 6.0, 2
LM, RM, I2 = ((1, 1), (0, 1)), ((1, 0), (1, 1)), ((1, 0), (0, 1))


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


def run(member):
    if member == 'm004':
        name, word, kk, levels = 'm004', 'LR', 0, [(0.25, 3), (0.0, 3)]
    else:
        kk = int(member.split('=')[1])
        word = 'L' * 6 + 'R' + 'LR' * kk
        name = 'b++' + word
        levels = [(0.5, 3), (0.25, 3), ('core', 4)] if kk == 1 else [('core', 4), ('anti', 3)]
    log = lambda m: print(m, flush=True)
    t0 = time.time()
    import scipy, numba, snappy
    res = {'member': member, 'name': name, 'word': word, 'R': R, 'Yfrac': YFRAC, 'H': HTR, 'r': RREF, 'checks': {},
           'versions': dict(numpy=np.__version__, scipy=scipy.__version__, numba=numba.__version__, snappy=snappy.__version__,
                            python=sys.version.split()[0])}
    log(f"{member} ({name}); versions {res['versions']}")
    # exact: the sigma-fixed fibres' classes
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
    if kk >= 2:
        res['P5'] = opposite
    g = T.Geo(name, wordlen=7, rmin=0.05, verbose=False)
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
        spec = g.M.length_spectrum(float(Lc.real) + 0.25)
        snapL = complex(spec[0]['length']) if len(spec) else complex('nan')
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
        res['P3'] = bool(abs(hv.mean() - np.round(hv.mean())) < 1e-8)
        log(f"  systole {w} (chi {chi_s}): complex length {Lc.real:.8f} {Lc.imag:+.8f}i, SnapPy {snapL.real:.8f} "
            f"{snapL.imag:+.8f}i; h on its axis {hv.mean():.12f} (spread {np.ptp(hv):.1e}); |d theta| there {gr.mean():.6f}")
        if kk == 1:
            res['checks']['C7'] = bool(abs(gr.mean() - 0.04200) < 2e-4)
    Ms = T.Mesh(g, HTR, RREF, verbose=False)
    vals = T.node_values(Ms, H)
    log(f"  mesh and node values ({time.time() - t0:.0f}s)")
    res['levels'] = []
    c4 = True
    for lab, nsub in levels:
        s = s0 if lab == 'core' else ((s0 + 0.5) % 1.0 if lab == 'anti' else lab)
        t1 = time.time()
        out = T.surface_series(Ms, H, s, vals, nsub, log=log)
        ck = out['check']
        ok = (ck['chi'] == -1 and ck['loops'] == 1 and ck['nonmanifold'] == 0 and ck['inconsistent'] == 0 and
              all(abs(abs(x['cup']) - 1) < 1e-6 for x in out['series']) and abs(out['series'][-1]['detE'] - 1) < 1e-3)
        c4 = c4 and ok
        ser = [{'n': int(x['n']), 'F': int(x['F']), 'detE': float(x['detE']), 'cup': float(x['cup']),
                'tau': [complex(x['tau']).real, complex(x['tau']).imag]} for x in out['series']]
        summ = series_summary(ser)
        rec = {'level': lab if isinstance(lab, str) else float(lab), 's': float(s), 'check': ck,
               'snapped': int(out['snapped']), 'series': ser, 'extrapolated': summ, 'C4': bool(ok),
               'seconds': time.time() - t1}
        res['levels'].append(rec)
        log(f"  level {lab} (s = {s:.12f}): Im tau = {summ['im']:.6f} +- {summ['im_err']:.6f} (finest {summ['im_finest']:.6f}, "
            f"A3 {summ['im_A3']:.6f}); |Re tau| = {summ['absre']:.6f} +- {summ['absre_err']:.6f}; C4 {'PASS' if ok else 'FAIL'} "
            f"({time.time() - t1:.0f}s)")
    res['checks']['C4'] = bool(c4)
    def lv(x):
        return next(r for r in res['levels'] if r['level'] == x)['extrapolated']
    if member == 'm004':
        q, z = lv(0.25), lv(0.0)
        res['checks']['C5'] = bool(abs(q['im'] - 1) < 2e-4 and q['absre'] < 2e-4 and abs(z['absre'] - 0.5) < 5e-4 and
                                   abs(z['im'] - 1.12438) < 5e-4)
    if kk == 1:
        h_, q = lv(0.5), lv(0.25)
        res['checks']['C6'] = bool(abs(h_['absre'] - 0.5) < 1e-3 and abs(h_['im'] - 1.5904) < 2e-3 and
                                   abs(q['absre'] - 0.3722) < 2e-3 and abs(q['im'] - 1.0085) < 2e-3)
        res['P1'] = bool(abs(lv('core')['im'] - 6.15) <= 0.15)
    if kk >= 1:
        tube = lv('core')
        p2 = tube['absre'] <= max(2 * tube['absre_err'], 1e-3)
        if kk >= 2:
            an = lv('anti')
            p2 = p2 and abs(an['absre'] - 0.5) <= max(2 * an['absre_err'], 1e-3)
        res['P2'] = bool(p2)
    res['seconds'] = time.time() - t0
    log(f"  checks: {res['checks']}; total {res['seconds']:.0f}s")
    with open(os.path.join(HERE, f"out_{member.replace('=', '')}.json"), 'w') as f:
        json.dump(res, f, indent=1)


def summary():
    m = json.load(open(os.path.join(HERE, 'out_m004.json')))
    base_ok = m['checks'].get('C1', False) and m['checks'].get('C5', False)
    print(f"m004: checks {m['checks']}; C1 and C5 {'PASS' if base_ok else 'FAIL'}")
    rows = {}
    for k in range(1, 6):
        r = json.load(open(os.path.join(HERE, f'out_k{k}.json')))
        tube = next(x for x in r['levels'] if x['level'] == 'core')['extrapolated']
        anti = next((x for x in r['levels'] if x['level'] in ('anti', 0.5)), None)
        ok = base_ok and all(r['checks'].values())
        rows[k] = dict(ok=ok, tube=tube, anti=anti['extrapolated'] if anti else None, r=r)
        a = rows[k]['anti']
        print(f"k = {k}: checks {r['checks']} -> {'used' if ok else 'NOT USED'}; core level {r['core_level']:+.3e} "
              f"(P3 {r['P3']}); tube Im tau {tube['im']:.6f} +- {tube['im_err']:.6f}, |Re| {tube['absre']:.6f} +- "
              f"{tube['absre_err']:.6f}; anti-apex Im {a['im']:.6f} +- {a['im_err']:.6f}, |Re| {a['absre']:.6f} +- "
              f"{a['absre_err']:.6f}; P2 {r['P2']}" + (f"; P5 {r['P5']}" if 'P5' in r else '') + (f"; P1 {r['P1']}" if 'P1' in r else ''))
    use = [k for k in range(1, 6) if rows[k]['ok']]
    im = {k: rows[k]['tube']['im'] for k in use}
    diffs = [(k, abs(im[k + 1] - im[k])) for k in range(1, 5) if k in im and k + 1 in im]
    p4 = (len(diffs) == 4 and all(diffs[i][1] > diffs[i + 1][1] for i in range(3)) and diffs[-1][1] < 0.01 * im[5])
    print("tube |Im tau_(k+1) - Im tau_k|:", ", ".join(f"k={k}->{k + 1}: {d:.6f}" for k, d in diffs), f"; P4 {p4}")
    for lab, key, ks in (('tube', 'tube', (3, 4, 5)), ('anti-apex', 'anti', (3, 4, 5))):
        if not all(k in use for k in ks):
            print(f"{lab}: k = 3, 4, 5 not all usable; no limit stated"); continue
        v = [rows[k][key]['im'] for k in ks]; e = max(rows[k][key]['im_err'] for k in ks)
        d1, d2 = v[1] - v[0], v[2] - v[1]
        if d1 * d2 > 0 and abs(d2) < abs(d1):
            lim = v[2] - d2 * d2 / (d2 - d1)
            print(f"{lab}: Im tau at k = 3, 4, 5: {v[0]:.6f}, {v[1]:.6f}, {v[2]:.6f}; ratio {d2 / d1:.4f}; k -> infinity: "
                  f"{lim:.6f} +- {abs(lim - v[2]) + e:.6f}")
        else:
            print(f"{lab}: differences {d1:+.6f}, {d2:+.6f} do not shrink with one sign; no limit stated")


if __name__ == '__main__':
    if sys.argv[1] == 'summary':
        summary()
    else:
        run(sys.argv[1])
