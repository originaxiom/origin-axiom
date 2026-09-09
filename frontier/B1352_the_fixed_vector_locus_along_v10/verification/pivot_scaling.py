#!/usr/bin/env python3
"""B1352 stage E -- THE SCALING OF THE CUSP-FIXED DEFECT ALONG V10.  B1350's genuine point along class 1 sits at step 0.02/|Y|;
a second genuine point at step 0.04/|Y| was computed with the same instrument (step04/: v10_direction.py with V10_STEP=0.04,
the 2000-bit re-read).  If the three cusp-fixed vectors of rho_0 are lost at order e_i along the curve, the three smallest
singular values of the cusp-fixed matrix T = [mu - I; lambda - I] scale as (t2/t1)^e_i between the two points; noise would
not scale.  t2/t1 is read from the self-duality defects (B1350 stage (3): both classes are trace-flat at first order; the
finite defects of the six trace words give the curve's actual parameter ratio through their common factor).  Singular values
at 150 digits (mpmath) from the banked 200-digit points; the loaded points' relator residuals are re-checked.
A third point at step 0.01/|Y| (step01/) gives a second ratio per quantity, an asymptotics check.
Usage: python3 pivot_scaling.py"""
import os, sys, json
import mpmath as mp
mp.mp.dps = 150
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
import cusped_theta_odd_hp as H
from flint import acb_mat, acb, arb
n = 27
def load(path, name):
    v = json.load(open(path))[name]
    mats = {int(g): acb_mat([[acb(arb(re), arb(im)) for (re, im) in row] for row in v[g]]) for g in ("1", "2")}
    invs = {g: mats[g].inv() for g in (1, 2)}
    return mats, invs
def smallest_svals(mats, invs, k=3):
    lam = H.ev(mats, invs, H.LONG, n)
    T = H.mat2mp(H.vstack(mats[1] - H.eye(n), lam - H.eye(n)))
    s = mp.svd_c(T, compute_uv=False)
    s = sorted([x for x in s])
    return s[:k], max(s)
def defects(mats, invs):
    return [abs(x.mid()) for x in H.selfduality_trace_test(mats, invs, n)]
P0 = os.path.join(HERE, 'step01', 'v10_step01_points.json')
P1 = os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification', 'v10_direction_points.json')
P2 = os.path.join(HERE, 'step04', 'v10_step04_points.json')
out = {}
for label, path in (("step 0.01 (B1352 step01/)", P0), ("step 0.02 (B1350)", P1), ("step 0.04 (B1352 step04/)", P2)):
    if not os.path.exists(path): continue
    mats, invs = load(path, "class 1")
    r = float(H.frob(H.ev(mats, invs, H.REL, n) - H.eye(n)).mid())
    sv, top = smallest_svals(mats, invs)
    d = defects(mats, invs)
    out[label] = (sv, top, d)
    print(f"  {label}: relator residual {r:.1e}; largest singular value of T {mp.nstr(top, 4)}; three smallest {[mp.nstr(x / top, 4) for x in sv]} (relative)")
    print(f"      self-duality defects |tr rho(w) - tr rho(w^-1)| on the six words: {[f'{float(x):.3e}' for x in d]}")
labels = list(out)
for a, b in zip(labels, labels[1:]):
    (s1, t1, d1), (s2, t2, d2) = out[a], out[b]
    ratios_d = [float(y / x) for x, y in zip(d1, d2) if float(x) > 1e-40]
    print(f"  == {b} / {a}")
    print(f"     defect ratios: {[f'{x:.3f}' for x in ratios_d]}")
    rho = mp.mpf(ratios_d[0]) ** (mp.mpf(1) / 4)
    print(f"     if the defects are fourth order, the curve's parameter ratio is {mp.nstr(rho, 5)} (2 at first order; the Newton correction reparametrises)")
    for i, (x, y) in enumerate(zip(s1, s2)):
        rr = (y / t2) / (x / t1)
        print(f"     singular value {i}: ratio {mp.nstr(rr, 5)} = 2^{mp.nstr(mp.log(rr) / mp.log(2), 4)} = (parameter ratio)^{mp.nstr(mp.log(rr) / mp.log(rho), 4)}")
    prod = (s2[0] * s2[1] * s2[2] / t2**3) / (s1[0] * s1[1] * s1[2] / t1**3)
    print(f"     product of the three: ratio 2^{mp.nstr(mp.log(prod) / mp.log(2), 4)} = (parameter ratio)^{mp.nstr(mp.log(prod) / mp.log(rho), 4)}   (stage D: e1 + e2 + e3 = 12 on the greedy and keep-branches)")
