#!/usr/bin/env python3
"""B1352 control -- THE FIXED-VECTOR LOCUS ALONG V8 (B1268's stage (b), never completed: its record stops at Newton iteration 3
with |res| = 5.6e2 under the 1e-24 damping).  Same instrument as fixed_locus_v10.py, on the V8 direction: the exact V8 block
cocycle (obstruction.py), the first-order point exp(0.02 Y/|Y|) rho_0, Newton (damping 1e-50) to the genuine theta-odd point
(B1268 (a)'s point, recomputed), then the augmented search for the locus mu v = v, lambda v = v with v0 the cusp-fixed
vector of block <block>.  Usage: python3 fixed_locus_v8.py <block 0|1|2> [iters]"""
from __future__ import annotations
import os, sys, json, time
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification'))
import cusped_theta_odd_hp as H
from flint import acb_mat, acb, arb, ctx
E, S = H.E, H.S
n = 27
t0 = time.time()
block = int(sys.argv[1]) if len(sys.argv) > 1 else 0
ITERS = int(sys.argv[2]) if len(sys.argv) > 2 else 60

import obstruction as O            # the eight exact block cocycles at the subregular point (40 s)
w8, Za, Zb = next(c for c in O.COC if c[0] == 8)
Ya, Yb = H.e6_matrix([H.q2acb(z) for z in Za]), H.e6_matrix([H.q2acb(z) for z in Zb])
rho0 = O.rho0
A0, B0 = H.to_acb(H.rescale(rho0.M[1])), H.to_acb(H.rescale(rho0.M[2]))
A0i, B0i = H.to_acb(H.rescale(rho0.I[1])), H.to_acb(H.rescale(rho0.I[2]))
M0, M0i = {1: A0, 2: B0}, {1: A0i, 2: B0i}
znorm = max(float(H.frob(Ya).mid()), float(H.frob(Yb).mid()))
ce = acb(0.02) / acb(arb(str(znorm)))
mats = {1: (Ya * ce).exp() * A0, 2: (Yb * ce).exp() * B0}
invs = {1: A0i * (-(Ya * ce)).exp(), 2: B0i * (-(Yb * ce)).exp()}
print(f"=== (a) the V8 direction: |Y| = {znorm:.3e}, step 0.02/|Y|, start residual {H.frob(H.ev(mats, invs, S.REL, n) - H.eye(n)).str(3)} ===")
mats, invs, _, nr = H.newton(mats, invs, iters=40, mu="1e-50", verbose=True)
tt = H.selfduality_trace_test(mats, invs, n)
print(f"    converged residual {nr:.1e}; self-duality defects {[x.str(3) for x in tt]} -> {'NOT self-dual' if max(float(x.mid()) for x in tt) > 1e-20 else 'self-dual'}   ({time.time() - t0:.0f} s)")
pts_path = os.path.join(HERE, "v8_point.json")
v8pt = {str(g): [[[arb(mats[g][i, j].real.mid()).str(120, radius=False), arb(mats[g][i, j].imag.mid()).str(120, radius=False)] for j in range(n)] for i in range(n)] for g in (1, 2)}
v8pt["residual"] = f"{nr:.1e}"
json.dump({"V8": v8pt}, open(pts_path, "w"))

lam0 = H.ev(M0, M0i, H.LONG, n)
Kl = H.mp_nullspace(H.mat2mp(H.vstack(A0 - H.eye(n), lam0 - H.eye(n))))
def support(v): return max(range(n), key=lambda i: abs(v[i]))
Kl = sorted(Kl, key=support)
v0mp = Kl[block]
v0 = acb_mat([[acb(arb(str(v0mp[i].real)), arb(str(v0mp[i].imag)))] for i in range(n)]); v0h = H.hermitian(v0)
print(f"=== (b) the fixed-vector locus along V8, target block {block} (dominant coordinate {support(v0mp)}) ===")
def resid(mats, invs, v):
    lam = H.ev(mats, invs, H.LONG, n)
    return H.flat((mats[1] - H.eye(n)) * v) + H.flat((lam - H.eye(n)) * v) + H.flat(v0h * v - acb_mat([[acb(1)]]))
def jac_Y(mats, invs, v, g, Y):
    lam = H.ev(mats, invs, H.LONG, n)
    dmu = (Y * mats[1]) * v if g == 1 else acb_mat(n, 1)
    dlam = (H.adfox_apply(mats, invs, H.LONG, g, Y, n) * lam) * v
    return H.flat(dmu) + H.flat(dlam) + [acb(0)]
def jac_v(mats, invs, v, k):
    lam = H.ev(mats, invs, H.LONG, n)
    ek = acb_mat(n, 1); ek[k, 0] = acb(1)
    return H.flat((mats[1] - H.eye(n)) * ek) + H.flat((lam - H.eye(n)) * ek) + H.flat(v0h * ek)
extra = dict(v0=v0, resid=resid, jac_Y=jac_Y, jac_v=jac_v)
print(f"    start residual of the fixed-vector equations: {float(sum((abs(x) * abs(x) for x in resid(mats, invs, v0)), arb(0)).sqrt().mid()):.3e}")
mats2, invs2, v, nr = H.newton(mats, invs, extra=extra, iters=ITERS, mu="1e-50", verbose=True)
rel = float(H.frob(H.ev(mats2, invs2, H.REL, n) - H.eye(n)).mid()); fx = float(sum((abs(x) * abs(x) for x in resid(mats2, invs2, v)), arb(0)).sqrt().mid())
tt = H.selfduality_trace_test(mats2, invs2, n)
dist0 = float(H.frob(mats2[1] - A0).mid()) / float(H.frob(A0).mid()); dist = float(H.frob(mats2[1] - mats[1]).mid()) / float(H.frob(mats[1]).mid())
print(f"    converged: residual {nr:.1e} (relator {rel:.1e}, fixed-vector {fx:.1e}); self-duality defects {[x.str(3) for x in tt]} -> {'NOT self-dual' if max(float(x.mid()) for x in tt) > 1e-20 else 'SELF-DUAL'}")
print(f"    relative distance moved from the V8 point: {dist:.3e}; distance from rho_0: {dist0:.3e}   ({time.time() - t0:.0f} s)")
out = os.path.join(HERE, "fixed_locus_points.json")
try: allpts = json.load(open(out))
except (FileNotFoundError, ValueError): allpts = {}
key = f"V8 | fixed vector of block {block}"
allpts[key] = {str(g): [[[arb(mats2[g][i, j].real.mid()).str(120, radius=False), arb(mats2[g][i, j].imag.mid()).str(120, radius=False)] for j in range(n)] for i in range(n)] for g in (1, 2)}
allpts[key]["residual"] = f"{nr:.1e}"; allpts[key]["distance_from_rho0"] = f"{dist0:.3e}"; allpts[key]["self_dual"] = bool(max(float(x.mid()) for x in tt) <= 1e-20)
json.dump(allpts, open(out, "w"))
rep = H.cohomology_report(mats2, invs2, n, f"27 on the locus ({key})"); dm, di = H.dual_of(mats2, invs2); repd = H.cohomology_report(dm, di, n, f"27bar on the locus ({key})")
print(f"    ==> (60-digit read) N(27) = {rep['h1'] - repd['h1']};  bound -{rep['h0t']} <= N <= {repd['h0t']}")
print(f"[{time.time() - t0:.0f} s]")
