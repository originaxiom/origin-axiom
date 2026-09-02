#!/usr/bin/env python3
"""R48(d): B511/D3 dynamics done on TRACE coordinates, which is the only well-posed way to run it in double precision.
State per history: (x,y,z) = (tr A, tr B, tr AB) of an SU(2) pair; kappa = x^2+y^2+z^2-xyz-2.
Moves (verified against matrices below): F: (x,y,z)->(z, x, xz-y); M: (A,B)->(A,BA): (x,y,z)->(x, z, xz-y);
D: (A,B)->(A^2,B^2): (x,y,z)->(x^2-2, y^2-2, xyz-x^2-y^2+2).  F and M preserve kappa exactly; D does not.
Optionally re-project z after each F/M step onto the exact kappa level set (the map is chaotic, so this keeps the
conserved quantity exact while the orbit shadows the invariant measure).  Also: the matrix recursion is ill-conditioned
like phi^t (perturbations multiply by Fibonacci numbers), which is why every matrix-level run of the committed script
is numerically meaningless after ~70 steps -- the banked 2.0000000000 percentiles are the collapse signature."""
import numpy as np, warnings, importlib.util, sys
warnings.filterwarnings('ignore')
SRC = sys.argv[1] if len(sys.argv) > 1 else '/tmp/claude-0/-home-user-origin-axiom/def55705-87fb-5c25-8c65-d57916765de8/scratchpad/wt_main/frontier/B511_physics_verdict/d3_wild_access.py'
spec = importlib.util.spec_from_file_location('d3', SRC); d3 = importlib.util.module_from_spec(spec); spec.loader.exec_module(d3)
tr = lambda M: np.real(np.trace(M, axis1=1, axis2=2))
K = lambda x, y, z: x*x + y*y + z*z - x*y*z - 2
print('== identity checks against matrices (n=3000 Haar pairs)')
rng = np.random.default_rng(3); A, B = d3.haar(3000, rng), d3.haar(3000, rng); x, y, z = tr(A), tr(B), tr(A @ B)
print('  F: tr(ABA) = xz - y       max err %.1e' % np.abs(tr(A @ B @ A) - (x*z - y)).max())
print('  M: tr(A.BA) = xz - y      max err %.1e' % np.abs(tr(A @ B @ A) - (x*z - y)).max())
print('  D: tr(A^2)=x^2-2, tr(B^2)=y^2-2, tr(A^2B^2)=xyz-x^2-y^2+2   max err %.1e %.1e %.1e' % (np.abs(tr(A@A)-(x*x-2)).max(), np.abs(tr(B@B)-(y*y-2)).max(), np.abs(tr(A@A@B@B)-(x*y*z-x*x-y*y+2)).max()))
print('  short-time agreement, matrices vs trace map, mix M10/D10/F80, t<=40:')
def step(x, y, z, r, mix):
    ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
    xF, yF, zF = z, x, x*z - y
    xM, yM, zM = x, z, x*z - y
    xD, yD, zD = x*x - 2, y*y - 2, x*y*z - x*x - y*y + 2
    return np.where(ev_m, xM, np.where(ev_d, xD, xF)), np.where(ev_m, yM, np.where(ev_d, yD, yF)), np.where(ev_m, zM, np.where(ev_d, zD, zF))
rng = np.random.default_rng(11); n = 1000; A, B = d3.haar(n, rng), d3.haar(n, rng); x, y, z = tr(A), tr(B), tr(A @ B); mix = (0.10, 0.10)
for t in range(40):
    r = rng.random(n); ev_m = r < mix[0]; ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
    AB = A @ B; Bn = np.where(ev_m[:, None, None], B @ A, np.where(ev_d[:, None, None], B @ B, A)); An = np.where(ev_d[:, None, None], A @ A, AB); A, B = An, Bn
    x, y, z = step(x, y, z, r, mix)
    if t in (9, 19, 29, 39): print('    t=%d max|kappa_matrix - kappa_trace| = %.1e   P(|k-2|<0.05): matrices %.3f trace %.3f' % (t, np.abs(K(tr(A), tr(B), tr(A@B)) - K(x, y, z)).max(), np.mean(np.abs(K(tr(A), tr(B), tr(A@B)) - 2) < 0.05), np.mean(np.abs(K(x, y, z) - 2) < 0.05)))
def project(x, y, z, kappa):   # move z onto the level set: z^2 - xy z + (x^2+y^2-2-kappa) = 0, root nearest to z
    c = x*x + y*y - 2 - kappa; disc = x*x*y*y - 4*c; ok = disc >= 0
    s = np.sqrt(np.maximum(disc, 0)); z1 = (x*y + s)/2; z2 = (x*y - s)/2
    zn = np.where(np.abs(z1 - z) < np.abs(z2 - z), z1, z2); return np.where(ok, zn, z)
print('== long runs on the trace map (n=20000 histories, 3000 steps)')
for mix, name in [((0.10, 0.10), 'M10/D10/F80'), ((0.20, 0.0), 'M20/F80'), ((0.0, 0.20), 'D20/F80')]:
    for proj in (False, True):
        rng = np.random.default_rng(11); n = 20000; A, B = d3.haar(n, rng), d3.haar(n, rng); x, y, z = tr(A), tr(B), tr(A @ B); kappa = K(x, y, z); samples = []
        for t in range(3000):
            r = rng.random(n); ev_d = (r >= mix[0]) & (r < mix[0] + mix[1])
            x, y, z = step(x, y, z, r, mix)
            if proj:
                kappa = np.where(ev_d, K(x, y, z), kappa); z = project(x, y, z, kappa)
            else: kappa = K(x, y, z)
            x = np.clip(x, -2, 2); y = np.clip(y, -2, 2); z = np.clip(z, -2, 2)   # SU(2) traces are bounded; clip guards against roundoff escape
            if t > 1500 and t % 10 == 9: samples.append(K(x, y, z) if not proj else kappa)
        s = np.concatenate(samples); k = s
        print('  %-12s proj=%-5s P(|k-2|<0.05)=%.3f P(wild)=%.3f percentiles[5,25,50,75,95]=%s' % (name, proj, np.mean(np.abs(k-2) < 0.05), np.mean((np.abs(k-2) > 0.5) & (k >= -2) & (k <= 2)), np.round(np.percentile(k, [5, 25, 50, 75, 95]), 4).tolist()))
print('banked D3.1/D3.3: percentiles ~[1.8, 1.99999, 2.0, 2.0, 2.0]; P(classical) >= 0.84; P(wild) <= 0.10')
