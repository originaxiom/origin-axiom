#!/usr/bin/env python3
"""R48 -- B511/D3.3 'wild-register accessibility' (frontier/B511_physics_verdict/d3_wild_access.py).
Banked: P(kappa ~ 2 classical) >= 0.84, P(wild-accessible kappa) <= 0.10 across all mixes; D3.1: median kappa 2.0.
(a) rerun the committed script's dynamics verbatim; (b) check which moves preserve the Fricke invariant kappa;
(c) rerun with the matrices kept on SU(2) by polar re-projection instead of det-scaling."""
import numpy as np, warnings, importlib.util, sys
warnings.filterwarnings('ignore')
SRC = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-user-origin-axiom/def55705-87fb-5c25-8c65-d57916765de8/scratchpad/wt_main/frontier/B511_physics_verdict/d3_wild_access.py'
spec = importlib.util.spec_from_file_location('d3', SRC); d3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(d3)
def kappa(A, B):
    x = np.real(np.trace(A, axis1=1, axis2=2)); y = np.real(np.trace(B, axis1=1, axis2=2)); z = np.real(np.trace(A @ B, axis1=1, axis2=2))
    return x*x + y*y + z*z - x*y*z - 2
def run(seed, n, steps, mix, mode):
    rng = np.random.default_rng(seed); A, B = d3.haar(n, rng), d3.haar(n, rng); k0 = kappa(A, B)
    for t in range(steps):
        r = rng.random(n); ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
        AB = A @ B
        Bn = np.where(ev_m[:, None, None], B @ A, np.where(ev_d[:, None, None], B @ B, A))
        An = np.where(ev_d[:, None, None], A @ A, AB); A, B = An, Bn
        if t % 20 == 19:
            for Mt in (A, B):
                if mode == 'committed': d = np.sqrt(np.abs(np.linalg.det(Mt))); Mt /= d[:, None, None]
                elif mode == 'su2': u, s, vh = np.linalg.svd(Mt); Mt[:] = u @ vh
    k = kappa(A, B)
    return dict(classical=float(np.mean(np.abs(k - 2) < 0.05)), wild=float(np.mean((np.abs(k - 2) > 0.5) & (k >= -2) & (k <= 2))), median=float(np.nanmedian(k)), nan=int(np.isnan(k).sum()), n=n)
print('== (b) which moves preserve kappa (n=2000 Haar pairs, exact SU(2) arithmetic in double precision)')
rng = np.random.default_rng(1); A, B = d3.haar(2000, rng), d3.haar(2000, rng); k0 = kappa(A, B)
for name, (An, Bn) in [('F: (A,B)->(AB,A)', (A @ B, A)), ('M: (A,B)->(A,BA)', (A, B @ A)), ('D: (A,B)->(A^2,B^2)', (A @ A, B @ B))]:
    print('  %-22s max|kappa_after - kappa_before| = %.2e' % (name, np.abs(kappa(An, Bn) - k0).max()))
print('  initial kappa of Haar pairs: median %.3f, P(|k-2|<0.05) = %.3f, P(wild) = %.3f' % (np.median(k0), np.mean(np.abs(k0-2) < 0.05), np.mean((np.abs(k0-2) > 0.5) & (k0 >= -2) & (k0 <= 2))))
for mode in ('committed', 'su2'):
    print('== (%s) renormalisation = %s' % ('a' if mode == 'committed' else 'c', 'det-scaling as committed' if mode == 'committed' else 'polar re-projection onto SU(2)'))
    for mix, name in [((0.10, 0.10), 'M10/D10/F80'), ((0.20, 0.0), 'M20/F80'), ((0.0, 0.20), 'D20/F80')]:
        for seed in (11, 12, 13):
            r = run(seed, 1000, 3000, mix, mode); print('  %-12s seed=%d classical=%.3f wild=%.3f median=%.3f nan=%d' % (name, seed, r['classical'], r['wild'], r['median'], r['nan']))
print('banked (D3_FINDINGS.md): P(classical) >= 0.84, P(wild) <= 0.10 across all mixes; D3.1 median kappa 2.0')
