#!/usr/bin/env python3
"""R48(b): why the committed dynamics 'classicalizes' -- track the matrices' shape under the committed det-scaling.
Prints, every 40 steps, the median ratio sigma_min/sigma_max of A (1 = unitary, 0 = rank-1 collapse), the median kappa,
and how many histories have gone non-finite."""
import numpy as np, warnings, importlib.util, sys
warnings.filterwarnings('ignore')
SRC = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-user-origin-axiom/def55705-87fb-5c25-8c65-d57916765de8/scratchpad/wt_main/frontier/B511_physics_verdict/d3_wild_access.py'
spec = importlib.util.spec_from_file_location('d3', SRC); d3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(d3)
rng = np.random.default_rng(11); n = 1000; A, B = d3.haar(n, rng), d3.haar(n, rng); mix = (0.10, 0.10)
def kap(A, B):
    x = np.real(np.trace(A, axis1=1, axis2=2)); y = np.real(np.trace(B, axis1=1, axis2=2)); z = np.real(np.trace(A @ B, axis1=1, axis2=2)); return x*x+y*y+z*z-x*y*z-2
for t in range(400):
    r = rng.random(n); ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
    AB = A @ B
    Bn = np.where(ev_m[:, None, None], B @ A, np.where(ev_d[:, None, None], B @ B, A))
    An = np.where(ev_d[:, None, None], A @ A, AB); A, B = An, Bn
    if t % 20 == 19:
        for Mt in (A, B): d = np.sqrt(np.abs(np.linalg.det(Mt))); Mt /= d[:, None, None]
    if t % 40 == 39:
        fin = np.isfinite(A).all(axis=(1, 2)) & np.isfinite(B).all(axis=(1, 2))
        s = np.linalg.svd(A[fin], compute_uv=False) if fin.any() else np.zeros((0, 2))
        k = kap(A[fin], B[fin]) if fin.any() else np.array([np.nan])
        print('t=%3d finite=%4d/%d  median sigma_min/sigma_max(A)=%.3e  median|A|max=%.2e  median kappa=%.6f  P(|kappa-2|<0.05)=%.3f' % (
            t, fin.sum(), n, np.median(s[:, 1] / s[:, 0]) if len(s) else float('nan'), np.median(np.abs(A[fin]).max(axis=(1, 2))) if fin.any() else float('nan'), np.nanmedian(k), np.mean(np.abs(k - 2) < 0.05)))
