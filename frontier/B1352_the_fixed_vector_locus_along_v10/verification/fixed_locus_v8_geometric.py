#!/usr/bin/env python3
"""B1352 control -- THE FIXED-VECTOR LOCUS ALONG V8 AT THE GEOMETRIC POINT (B1268's stage (b), completed).

B1268 reached the genuine theta-odd point rho_s along the exact V8 class at the geometric point (stage (a), residual
2.6e-63) and then started the augmented search mu v = v, lambda v = v (stage (b)), which stalled at |res| = 5.6e2 under
the 1e-24 damping (its record stops at Newton iteration 3).  Same instrument, damping 1e-50 (B1350's lesson), and the
three cusp-fixed vectors of rho_0 tried one at a time (block 0, 1, 2 = sorted by dominant coordinate, as in
fixed_locus_v10.py).  Usage: python3 fixed_locus_v8_geometric.py <block 0|1|2> [iters]"""
from __future__ import annotations
import os, sys, json, time, fcntl
from fractions import Fraction as F
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
import cusped_theta_odd_hp as H
from flint import acb_mat, acb, arb, fmpq
n = 27
t0 = time.time()
block = int(sys.argv[1]) if len(sys.argv) > 1 else 0
ITERS = int(sys.argv[2]) if len(sys.argv) > 2 else 60
A0, B0, A0i, B0i, M0, M0i = H.A0, H.B0, H.A0i, H.B0i, H.M0, H.M0i

print("=== (a) the geometric point's exact V8 class and the Newton search (B1268 (a), damping 1e-50) ===")
Za, Zb = H.block_cocycle_exact(4)
Ya1, Yb1 = H.e6_matrix([H.q2acb(z) for z in Za]), H.e6_matrix([H.q2acb(z) for z in Zb])
znorm = max(float(H.frob(Ya1).mid()), float(H.frob(Yb1).mid()))
eps = F(0.02 / znorm).limit_denominator(10**6)
Ya, Yb = Ya1 * acb(fmpq(eps.numerator, eps.denominator)), Yb1 * acb(fmpq(eps.numerator, eps.denominator))
mats = {1: Ya.exp() * A0, 2: Yb.exp() * B0}
invs = {1: A0i * (-Ya).exp(), 2: B0i * (-Yb).exp()}
print(f"    start eps = {eps}: relator residual {H.frob(H.ev(mats, invs, H.REL, n) - H.eye(n)).str(3)}")
mats, invs, _, nr = H.newton(mats, invs, iters=40, mu="1e-50", verbose=True)
tt = H.selfduality_trace_test(mats, invs, n)
print(f"    converged: residual {nr:.1e}; self-duality defects {[x.str(3) for x in tt]} -> {'NOT self-dual (theta-odd)' if max(float(x.mid()) for x in tt) > 1e-20 else 'self-dual'}   ({time.time() - t0:.0f} s)")
out = os.path.join(HERE, "v8_geometric_points.json")
def dump(key, M, extra_fields):
    with open(out + ".lock", "w") as lockf:
        fcntl.flock(lockf, fcntl.LOCK_EX)
        try: allpts = json.load(open(out))
        except (FileNotFoundError, ValueError): allpts = {}
        allpts[key] = {str(g): [[[arb(M[g][i, j].real.mid()).str(120, radius=False), arb(M[g][i, j].imag.mid()).str(120, radius=False)] for j in range(n)] for i in range(n)] for g in (1, 2)}
        allpts[key].update(extra_fields)
        json.dump(allpts, open(out, "w"))
dump("V8 geometric | theta-odd point", mats, {"residual": f"{nr:.1e}"})

lam0 = H.ev(M0, M0i, H.LONG, n)
Kl = H.mp_nullspace(H.mat2mp(H.vstack(A0 - H.eye(n), lam0 - H.eye(n))))
def support(v): return max(range(n), key=lambda i: abs(v[i]))
Kl = sorted(Kl, key=support)
print(f"=== rho_0 (geometric): cusp-fixed space of dimension {len(Kl)}; dominant coordinates {[support(v) for v in Kl]} ===")
v0mp = Kl[block]
v0 = acb_mat([[acb(arb(str(v0mp[i].real)), arb(str(v0mp[i].imag)))] for i in range(n)]); v0h = H.hermitian(v0)
print(f"=== (b) the fixed-vector locus along V8 at the geometric point, target block {block} (dominant coordinate {support(v0mp)}), damping 1e-50 ===")
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
print(f"    start residual of the fixed-vector equations at the theta-odd point: {float(sum((abs(x) * abs(x) for x in resid(mats, invs, v0)), arb(0)).sqrt().mid()):.3e}")
mats2, invs2, v, nr = H.newton(mats, invs, extra=extra, iters=ITERS, mu="1e-50", verbose=True)
rel = float(H.frob(H.ev(mats2, invs2, H.REL, n) - H.eye(n)).mid()); fx = float(sum((abs(x) * abs(x) for x in resid(mats2, invs2, v)), arb(0)).sqrt().mid())
tt = H.selfduality_trace_test(mats2, invs2, n)
dist0 = float(H.frob(mats2[1] - A0).mid()) / float(H.frob(A0).mid()); dist = float(H.frob(mats2[1] - mats[1]).mid()) / float(H.frob(mats[1]).mid())
sd = bool(max(float(x.mid()) for x in tt) <= 1e-20)
print(f"    converged: residual {nr:.1e} (relator {rel:.1e}, fixed-vector {fx:.1e}); self-duality defects {[x.str(3) for x in tt]} -> {'NOT self-dual' if not sd else 'SELF-DUAL'}")
print(f"    relative distance moved from the theta-odd point: {dist:.3e}; distance from the geometric point: {dist0:.3e}   ({time.time() - t0:.0f} s)")
key = f"V8 geometric | fixed vector of block {block}"
dump(key, mats2, {"residual": f"{nr:.1e}", "distance_from_rho0": f"{dist0:.3e}", "self_dual": sd})
rep = H.cohomology_report(mats2, invs2, n, f"27 on the locus ({key})"); dm, di = H.dual_of(mats2, invs2); repd = H.cohomology_report(dm, di, n, f"27bar on the locus ({key})")
print(f"    ==> (60-digit read) N(27) = {rep['h1'] - repd['h1']};  bound -{rep['h0t']} <= N <= {repd['h0t']}")
print(f"[{time.time() - t0:.0f} s]")
