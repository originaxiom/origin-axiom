#!/usr/bin/env python3
"""B1352 stage E' -- ARE THE SMALL CUSP-FIXED SINGULAR VALUES REAL?  B1350's genuine V10 point (class 1, step 0.02/|Y|) is a
600-bit Newton point with relator residual 6e-68; the three smallest relative singular values of T = [mu - I; lambda - I]
there are 6.8e-39, 3.5e-36, 3.3e-30 (pivot_scaling.py).  They decide h^0(dM; 27) = 0.  Test: polish the point by Newton at
2000 bits (target 1e-150, damping 1e-50, as report_hp.py --polish), measure how far it moves, and recompute the three
singular values; if the point's own accuracy were worse than 1e-39 relative the small values would change.
Usage: python3 polish_and_svals.py [class name]"""
import os, sys, json, time
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
import report_hp as R          # sets 2000 bits, 200-digit mpmath, the lifted acb2mp cap
H = R.H
from flint import acb_mat, acb, arb
n = 27
name = sys.argv[1] if len(sys.argv) > 1 else "class 1"
t0 = time.time()
pts = R.load_points(os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification', 'v10_direction_points.json'))
mats, invs, res = pts[name]
def svals(mats, invs):
    lam = H.ev(mats, invs, H.LONG, n)
    T = H.mat2mp(H.vstack(mats[1] - H.eye(n), lam - H.eye(n)))
    s = sorted(mp.svd_c(T, compute_uv=False))
    return [x / s[-1] for x in s[:3]]
r0 = float(H.frob(H.ev(mats, invs, H.REL, n) - H.eye(n)).mid())
s0 = svals(mats, invs)
print(f"  {name}: loaded (banked at 200 digits; 600-bit Newton residual {res}); relator residual at 2000 bits {r0:.1e}")
print(f"     three smallest relative singular values of T before polishing: {[mp.nstr(x, 12) for x in s0]}")
mats2, invs2, _, nr = H.newton(mats, invs, iters=8, mu="1e-50", verbose=True, target=mp.mpf('1e-150'))
move = float(H.frob(mats2[1] - mats[1]).mid()) / float(H.frob(mats[1]).mid())
s1 = svals(mats2, invs2)
print(f"     polished residual {nr:.1e}; relative move of rho(a): {move:.1e}   ({time.time() - t0:.0f} s)")
print(f"     three smallest relative singular values of T after polishing:  {[mp.nstr(x, 12) for x in s1]}")
print(f"     relative changes: {[mp.nstr(abs(a - b) / a, 3) for a, b in zip(s0, s1)]}")
print(f"[{time.time() - t0:.0f} s]")
