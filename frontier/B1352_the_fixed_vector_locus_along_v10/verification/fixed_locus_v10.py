#!/usr/bin/env python3
"""B1352 -- THE FIXED-VECTOR LOCUS ALONG THE V10 DIRECTION (L204's remaining half, on B1350's genuine points).

Pantev-Wijnholt's chiral count on the cusped object is -chi(d+M) per charged sector, and a disc-type d+ can arise only on a
weight whose cusp holonomy is trivial (a cusp-fixed vector: the torus cohomology of every other weight vanishes, so no
boundary condition is left to choose -- B1268's bound -h0(dM; V) <= N <= h0(dM; V*) restated).  Along the V10 direction
the generic deformed point has no cusp-fixed vector (B1350: h0(dM; 27) = h0(dM; 27bar) = 0, N = 0).  The one place left is
the FIXED-VECTOR LOCUS: the deformations along V10 on which the cusp holonomy keeps a fixed vector, mu v = v, lambda v = v.
B1268 (b) searched that locus along V8 with an augmented Newton and found N = 0; this script does the same along V10.

Start: a banked converged V10 point (600 bits, B1350's v10_direction_points.json).  Unknowns: the E6 representation and a
vector v in the 27 normalised by v0^H v = 1, v0 one of the three cusp-fixed vectors of rho_0 (one per block 13, 9, 5 of the
27 = V12 + V8 + V4 at the subregular point).  Equations: the relator, mu v = v, lambda v = v, v0^H v = 1.  Damping 1e-50
(B1350's finding).  At the converged locus point: the self-duality test, and the cohomology of 27 and 27bar re-read at 2000
bits with the torus checks (report_hp).  Usage: python3 fixed_locus_v10.py "<direction>" <block 0|1|2> [iters]"""
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
direction = sys.argv[1] if len(sys.argv) > 1 else "class 1"
block = int(sys.argv[2]) if len(sys.argv) > 2 else 0
ITERS = int(sys.argv[3]) if len(sys.argv) > 3 else 60

# rho_0 (subregular) and its three cusp-fixed vectors, one per block of the 27
e2, h2, f2, g2 = E.subregular_sl2()
rho0 = S.build_rep(e2, f2)
A0, B0 = H.to_acb(H.rescale(rho0.M[1])), H.to_acb(H.rescale(rho0.M[2]))
A0i, B0i = H.to_acb(H.rescale(rho0.I[1])), H.to_acb(H.rescale(rho0.I[2]))
M0, M0i = {1: A0, 2: B0}, {1: A0i, 2: B0i}
lam0 = H.ev(M0, M0i, H.LONG, n)
Kl = H.mp_nullspace(H.mat2mp(H.vstack(A0 - H.eye(n), lam0 - H.eye(n))))
print(f"=== rho_0: cusp-fixed space of dimension {len(Kl)} (one vector per block of 27 = 13 + 9 + 5) ===")
# order the fixed vectors by the block they live in: the highest-weight vector of each sl2-block; identify by the
# position of the largest component (the rescaled basis is weight-ordered per block)
def support(v):
    return max(range(n), key=lambda i: abs(v[i]))
Kl = sorted(Kl, key=support)
for i, v in enumerate(Kl):
    print(f"    fixed vector {i}: dominant coordinate {support(v)}")
v0mp = Kl[block]
v0 = acb_mat([[acb(arb(str(v0mp[i].real)), arb(str(v0mp[i].imag)))] for i in range(n)])
v0h = H.hermitian(v0)

# the banked V10 point
pts = json.load(open(os.environ.get('FIXED_LOCUS_POINTS', os.path.join(HERE, '..', '..', 'B1350_the_v10_direction', 'verification', 'v10_direction_points.json'))))   # env FIXED_LOCUS_POINTS: another banked V10 point (the step-0.04 scaling point)
d = pts[direction]
mats = {g: acb_mat([[acb(arb(re), arb(im)) for (re, im) in row] for row in d[str(g)]]) for g in (1, 2)}
invs = {g: mats[g].inv() for g in (1, 2)}
r0 = float(H.frob(H.ev(mats, invs, H.REL, n) - H.eye(n)).mid())
print(f"=== start: the converged V10 point along {direction!r} (relator residual {r0:.1e}); fixed-vector target block {block} ===")

def resid(mats, invs, v):
    lam = H.ev(mats, invs, H.LONG, n)
    r1 = (mats[1] - H.eye(n)) * v
    r2 = (lam - H.eye(n)) * v
    r3 = v0h * v - acb_mat([[acb(1)]])
    return H.flat(r1) + H.flat(r2) + H.flat(r3)

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
start_extra = float(sum((abs(x) * abs(x) for x in resid(mats, invs, v0)), arb(0)).sqrt().mid())
print(f"    start residual of the fixed-vector equations at the V10 point: {start_extra:.3e}")
mats2, invs2, v, nr = H.newton(mats, invs, extra=extra, iters=ITERS, mu="1e-50", verbose=True)
print(f"    converged: residual {nr:.1e}   ({time.time() - t0:.0f} s)")
rel = float(H.frob(H.ev(mats2, invs2, H.REL, n) - H.eye(n)).mid())
fx = float(sum((abs(x) * abs(x) for x in resid(mats2, invs2, v)), arb(0)).sqrt().mid())
print(f"    relator residual {rel:.1e}; fixed-vector residual {fx:.1e}")
# how far did the point move, and is it still a V10-type (non-self-dual) point?
tt = H.selfduality_trace_test(mats2, invs2, n)
print("    self-duality defects:", [x.str(3) for x in tt], "->", "NOT self-dual" if max(float(x.mid()) for x in tt) > 1e-20 else "SELF-DUAL")
dist = float(H.frob(mats2[1] - mats[1]).mid()) / float(H.frob(mats[1]).mid())
dist0 = float(H.frob(mats2[1] - A0).mid()) / float(H.frob(A0).mid())
print(f"    relative distance moved from the V10 point: {dist:.3e}; distance from rho_0: {dist0:.3e}  (0 would mean the locus point is rho_0 itself)")
# dump the locus point for the high-precision re-read
out = os.environ.get("FIXED_LOCUS_OUT", os.path.join(HERE, "fixed_locus_points.json"))   # env FIXED_LOCUS_OUT: where to bank the locus point
import fcntl
with open(out + ".lock", "w") as lockf:          # concurrent runs share fixed_locus_points.json: read-modify-write under a lock
    fcntl.flock(lockf, fcntl.LOCK_EX)
    try:
        allpts = json.load(open(out))
    except (FileNotFoundError, ValueError):
        allpts = {}
    key = f"{direction} | fixed vector of block {block}"
    allpts[key] = {str(g): [[[arb(mats2[g][i, j].real.mid()).str(120, radius=False), arb(mats2[g][i, j].imag.mid()).str(120, radius=False)] for j in range(n)] for i in range(n)] for g in (1, 2)}
    allpts[key]["residual"] = f"{nr:.1e}"; allpts[key]["distance_from_rho0"] = f"{dist0:.3e}"; allpts[key]["self_dual"] = bool(max(float(x.mid()) for x in tt) <= 1e-20)
    json.dump(allpts, open(out, "w"))

# the 60-digit report as a first read (the 2000-bit re-read is report_hp.py on fixed_locus_points.json)
rep = H.cohomology_report(mats2, invs2, n, f"27 on the locus ({key})")
dm, di = H.dual_of(mats2, invs2)
repd = H.cohomology_report(dm, di, n, f"27bar on the locus ({key})")
print(f"    ==> (60-digit read) N(27) = {rep['h1'] - repd['h1']};  bound -{rep['h0t']} <= N <= {repd['h0t']}")
print(f"[{time.time() - t0:.0f} s]")
