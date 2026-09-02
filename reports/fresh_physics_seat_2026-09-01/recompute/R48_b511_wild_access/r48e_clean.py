#!/usr/bin/env python3
"""R48(e): B511/D3 dynamics done two clean ways, with the committed moves read correctly:
F: (A,B)->(AB, A);  M: (A,B)->(AB, BA);  D: (A,B)->(A^2, B^2)   [from d3_wild_access.py's np.where branches].
(1) matrices re-projected onto SU(2) EVERY step (polar factor), so they never leave the group;
(2) trace map on (x,y,z) with the correct M, no clipping; histories whose traces leave [-2,2] by roundoff are counted.
Also: which of F/M/D preserve kappa (one exact step on Haar pairs)."""
import numpy as np, warnings, importlib.util, sys
warnings.filterwarnings('ignore')
SRC = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-user-origin-axiom/def55705-87fb-5c25-8c65-d57916765de8/scratchpad/wt_main/frontier/B511_physics_verdict/d3_wild_access.py'
spec = importlib.util.spec_from_file_location('d3', SRC); d3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(d3)
tr = lambda M: np.real(np.trace(M, axis1=1, axis2=2)); K = lambda x, y, z: x*x + y*y + z*z - x*y*z - 2
rng = np.random.default_rng(1); A, B = d3.haar(3000, rng), d3.haar(3000, rng); k0 = K(tr(A), tr(B), tr(A@B))
print('== which moves preserve kappa (exact one step, 3000 Haar pairs)')
for name, (An, Bn) in [('F (AB, A)', (A@B, A)), ('M (AB, BA)', (A@B, B@A)), ('D (A^2, B^2)', (A@A, B@B))]:
    print('  %-14s max|dkappa| = %.2e' % (name, np.abs(K(tr(An), tr(Bn), tr(An@Bn)) - k0).max()))
def stats(k): return 'P(|k-2|<0.05)=%.3f P(wild)=%.3f pct[5,25,50,75,95]=%s' % (np.mean(np.abs(k-2) < 0.05), np.mean((np.abs(k-2) > 0.5) & (k >= -2) & (k <= 2)), np.round(np.percentile(k, [5, 25, 50, 75, 95]), 4).tolist())
MIXES = [((0.10, 0.10), 'M10/D10/F80'), ((0.20, 0.0), 'M20/F80'), ((0.0, 0.20), 'D20/F80'), ((0.0, 0.0), 'F100 (control: kappa conserved)')]
print('== (1) matrices, SU(2) re-projection every step, n=2000, 3000 steps, samples from t>1500')
for mix, name in MIXES:
    rng = np.random.default_rng(11); n = 2000; A, B = d3.haar(n, rng), d3.haar(n, rng); k0 = K(tr(A), tr(B), tr(A@B)); S = []
    for t in range(3000):
        r = rng.random(n); ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
        AB = A @ B; Bn = np.where(ev_m[:, None, None], B @ A, np.where(ev_d[:, None, None], B @ B, A)); An = np.where(ev_d[:, None, None], A @ A, AB); A, B = An, Bn
        for Mt in (A, B): u, s, vh = np.linalg.svd(Mt); Mt[:] = u @ vh
        if t > 1500 and t % 10 == 9: S.append(K(tr(A), tr(B), tr(A@B)))
    k = np.concatenate(S); print('  %-32s %s%s' % (name, stats(k), '  max|k-k0| at end = %.1e' % np.abs(S[-1]-k0).max() if mix == (0.0, 0.0) else ''))
print('== (2) trace map with correct M, no clipping, n=20000, 3000 steps')
def step(x, y, z, r, mix):
    ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
    w = x*y*z - x*x - y*y + 2                       # tr(A^2 B^2) = tr(AB.BA)
    xF, yF, zF = z, x, x*z - y
    xM, yM, zM = z, z, w
    xD, yD, zD = x*x - 2, y*y - 2, w
    return np.where(ev_m, xM, np.where(ev_d, xD, xF)), np.where(ev_m, yM, np.where(ev_d, yD, yF)), np.where(ev_m, zM, np.where(ev_d, zD, zF))
for mix, name in MIXES:
    rng = np.random.default_rng(11); n = 20000; A, B = d3.haar(n, rng), d3.haar(n, rng); x, y, z = tr(A), tr(B), tr(A@B); k0 = K(x, y, z); S = []
    for t in range(3000):
        x, y, z = step(x, y, z, rng.random(n), mix)
        if t > 1500 and t % 10 == 9: S.append(K(x, y, z))
    k = np.concatenate(S); esc = np.mean((np.abs(x) > 2 + 1e-9) | (np.abs(y) > 2 + 1e-9) | (np.abs(z) > 2 + 1e-9) | ~np.isfinite(x))
    kk = k[np.isfinite(k) & (k <= 2 + 1e-9)]
    print('  %-32s escaped/nonfinite histories at end = %.4f; over finite non-escaped samples: %s%s' % (name, esc, stats(kk), '  max|k-k0| at end = %.1e' % np.abs(K(x, y, z)-k0).max() if mix == (0.0, 0.0) else ''))
print('banked D3.3: P(classical) >= 0.84, P(wild) <= 0.10 across all mixes; D3.1 percentiles ~[1.8, 1.99999, 2.0, 2.0, 2.0]')
