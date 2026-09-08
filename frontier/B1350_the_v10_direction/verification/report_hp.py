#!/usr/bin/env python3
"""B1350 stage (4′): the cohomology at the converged deformed points re-read at HIGH precision (2000 bits, 200-digit ranks,
threshold 1e-90), with the full pivot spectrum printed and the torus consistency checks (Euler characteristic, duality)
applied.  B1268's report decides ranks at 60 digits with a 1e-30 relative threshold; at the deformed points of stage (4) the
pivots straddled it (accepted 5.6e-29 against rejected 1.3e-33 on d1; 1.5e-30 against 1.7e-31 on Z1(T2)) and the torus
numbers it printed violated h0 - h1 + h2 = 0 -- so the ranks, and with them N(27), must be read where the zeros are zeros.
Usage: python3 report_hp.py [points.json] [--polish]  (the control rho_0 is always reported first)."""
from __future__ import annotations
import os, sys, json, time
import numpy as np
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', 'B1268_cusped_net_chirality_bound', 'verification'))
import cusped_theta_odd_hp as H
from flint import acb_mat, acb, arb, ctx
E, S = H.E, H.S
PREC_BITS, DPS, TOL = 2000, 200, mp.mpf('1e-50')
ctx.prec = PREC_BITS; mp.mp.dps = DPS
# B1268's conversions cap the acb -> mpmath transfer at 70 digits and fix omega at the import-time precision (600 bits);
# both are lifted here so that exact zeros sit at the working precision and not at 1e-70
H.acb2mp = lambda z: mp.mpc(mp.mpf(z.real.mid().str(DPS + 20, radius=False)), mp.mpf(z.imag.mid().str(DPS + 20, radius=False)))
H.OMEGA_ACB = (acb(-1) + acb(0, 1) * acb(3).sqrt()) / 2
H.U_ACB = 1 + H.OMEGA_ACB
n = 27
t0 = time.time()

def pivots(M):
    """all pivots (relative to the largest entry) of an mp matrix under Gaussian elimination with full pivoting; returns sorted list."""
    A = M.copy(); rows, cols = A.rows, A.cols
    scale = max(abs(A[i, j]) for i in range(rows) for j in range(cols)) or mp.mpf(1)
    pivs = []
    r = 0
    for _ in range(min(rows, cols)):
        best, bi, bj = mp.mpf(0), None, None
        for i in range(r, rows):
            for j in range(cols):
                v = abs(A[i, j])
                if v > best: best, bi, bj = v, i, j
        if bi is None or best == 0: break
        pivs.append(best / scale)
        # swap rows r, bi
        for j in range(cols): A[r, j], A[bi, j] = A[bi, j], A[r, j]
        for i in range(rows):
            if i != r and A[i, bj] != 0:
                f = A[i, bj] / A[r, bj]
                for j in range(cols): A[i, j] -= f * A[r, j]
        r += 1
    return sorted(pivs, reverse=True)

def rank_of(M, name):
    pv = pivots(M)
    acc = [p for p in pv if p > TOL]; rej = [p for p in pv if p <= TOL]
    tail = [mp.nstr(p, 3) for p in pv[-6:]]
    print(f"      [{name}] rank {len(acc)} of ({M.rows}x{M.cols}); pivot tail {tail}; smallest accepted {mp.nstr(min(acc), 3) if acc else '-'}, largest rejected {mp.nstr(max(rej), 3) if rej else '-'}")
    return len(acc)

def report(mats, invs, label):
    I = H.eye(n)
    d0 = H.mat2mp(H.vstack(mats[1] - I, mats[2] - I))
    d1 = H.mat2mp(H.hstack(H.fox(mats, invs, H.REL, 1, n), H.fox(mats, invs, H.REL, 2, n)))
    r0 = rank_of(d0, f"{label} d0"); r1 = rank_of(d1, f"{label} d1")
    h0, h1 = n - r0, (2 * n - r1) - r0
    mu, lam = mats[1], H.ev(mats, invs, H.LONG, n)
    comm = float(H.frob(mu * lam - lam * mu).mid())
    fixed = H.mat2mp(H.vstack(mu - I, lam - I)); h0t = n - rank_of(fixed, f"{label} cusp fixed")
    Zt = H.mat2mp(H.hstack(lam - I, -(mu - I))); Bt = H.mat2mp(H.vstack(mu - I, lam - I))
    rZ = rank_of(Zt, f"{label} Z1(T2)"); rB = rank_of(Bt, f"{label} B1(T2)"); h1t = (2 * n - rZ) - rB
    # h2(T2; V) = dim of the coinvariants = n - rank[mu - I | lam - I] (27 x 54)
    coinv = H.mat2mp(H.hstack(mu - I, lam - I)); h2t = n - rank_of(coinv, f"{label} coinvariants(T2)")
    if h1 == 0:
        # no classes to restrict: rank(res) = 0 by definition (the kernel of d1 is the coboundaries, whose torus restrictions are torus coboundaries;
        # reading that rank numerically at 1e-50 is noise-limited by the 600-bit point, so it is not read)
        rank_res = 0
        euler_T = (h0t - h1t + h2t == 0)
        print(f"    {label}: h0(M) = {h0}, h1(M) = {h1}, h2(M) = h1 - h0 = {h1 - h0}; torus: h0 = {h0t}, h1 = {h1t}, h2 = {h2t} (Euler {'ok' if euler_T else 'VIOLATED'}); rank(res) = 0 (h1 = 0); [mu,lambda] = {comm:.1e}")
        return dict(h0=h0, h1=h1, h0t=h0t, h1t=h1t, h2t=h2t, rank_res=0, euler=euler_T)
    kern = H.mp_nullspace(d1, tol=TOL)
    cols = []
    for v in kern:
        fa = acb_mat([[acb(arb(str(v[i].real)), arb(str(v[i].imag)))] for i in range(n)])
        fb = acb_mat([[acb(arb(str(v[n + i].real)), arb(str(v[n + i].imag)))] for i in range(n)])
        val = H.vstack(H.cocycle_value(mats, invs, [1], fa, fb, n), H.cocycle_value(mats, invs, H.LONG, fa, fb, n))
        cols.append([H.acb2mp(val[i, 0]) for i in range(2 * n)])
    R = mp.matrix(cols).T if cols else mp.matrix(2 * n, 0)
    RB = mp.matrix(2 * n, R.cols + Bt.cols)
    for i in range(2 * n):
        for j in range(R.cols): RB[i, j] = R[i, j]
        for j in range(Bt.cols): RB[i, R.cols + j] = Bt[i, j]
    rank_res = rank_of(RB, f"{label} res+B") - rB
    euler_T = (h0t - h1t + h2t == 0)
    print(f"    {label}: h0(M) = {h0}, h1(M) = {h1}, h2(M) = h1 - h0 = {h1 - h0}; torus: h0 = {h0t}, h1 = {h1t}, h2 = {h2t} (Euler {'ok' if euler_T else 'VIOLATED'}); rank(res) = {rank_res}; [mu,lambda] = {comm:.1e}")
    return dict(h0=h0, h1=h1, h0t=h0t, h1t=h1t, h2t=h2t, rank_res=rank_res, euler=euler_T)

def both(mats, invs, label):
    rep = report(mats, invs, f"27 {label}")
    dm, di = H.dual_of(mats, invs)
    repd = report(dm, di, f"27bar {label}")
    dual_ok = (rep['h1t'] == repd['h1t']) and (rep['h2t'] == repd['h0t']) and (repd['h2t'] == rep['h0t'])
    # the long exact sequence of (M, dM): h1(M,dM;V) = h2(M;V*) = h1(V*) - h0(V*); exactness at H^1(M) -> H^1(dM) -> H^2(M,dM) -> H^2(M) -> H^2(dM) -> H^3(M,dM) = h0(V*)
    N = rep['h1'] - repd['h1']
    print(f"     ==> N(27) = h1(27) - h1(27bar) = {N};  bound -{rep['h0t']} <= N <= {repd['h0t']};  torus duality (h1 = h1*, h2 = h0*) {'ok' if dual_ok else 'VIOLATED'}   ({time.time() - t0:.0f} s)")
    return N, rep, repd

def load_points(path):
    pts = json.load(open(path))
    out = {}
    for name, d in pts.items():
        mats = {}
        for g in ("1", "2"):
            rows = d[g]
            mats[int(g)] = acb_mat([[acb(arb(re), arb(im)) for (re, im) in row] for row in rows])
        invs = {g: mats[g].inv() for g in (1, 2)}
        out[name] = (mats, invs, d.get("residual"))
    return out

if __name__ == "__main__":
    path = next((a for a in sys.argv[1:] if not a.startswith("--")), os.path.join(HERE, "v10_direction_points.json"))
    polish = "--polish" in sys.argv
    print(f"=== (4') high-precision cohomology: {PREC_BITS} bits, {DPS}-digit ranks, threshold {mp.nstr(TOL, 2)} ===")
    e2, h2, f2, g2 = E.subregular_sl2()
    rho0 = S.build_rep(e2, f2)
    A0, B0 = H.to_acb(H.rescale(rho0.M[1])), H.to_acb(H.rescale(rho0.M[2]))
    A0i, B0i = H.to_acb(H.rescale(rho0.I[1])), H.to_acb(H.rescale(rho0.I[2]))
    print("  -- control: the subregular point rho_0 (exact stages: h1(27) = h1(27bar) = 3, h0(dM) = 3, N = 0)")
    both({1: A0, 2: B0}, {1: A0i, 2: B0i}, "at rho_0")
    if os.path.exists(path):
        pts = load_points(path)
        results = {}
        for name, (mats, invs, res) in pts.items():
            print(f"  -- {name} (Newton residual at 600 bits: {res})")
            r = float(H.frob(H.ev(mats, invs, H.REL, n) - H.eye(n)).mid())
            print(f"     relator residual of the loaded point at {PREC_BITS} bits: {r:.1e}")
            if polish:
                mats, invs, _, nr = H.newton(mats, invs, iters=12, mu="1e-50", verbose=True, target=mp.mpf('1e-150'))
                print(f"     polished residual {nr:.1e}")
            results[name] = both(mats, invs, f"along {name}")
        print("\n=== summary ===")
        for name, (N, rep, repd) in results.items():
            print(f"    {name:20s}: N(27) = {N}; h1(27) = {rep['h1']}, h1(27bar) = {repd['h1']}; cusp h0(27) = {rep['h0t']}, h0(27bar) = {repd['h0t']}; torus Euler ok: {rep['euler'] and repd['euler']}")
    else:
        print(f"  (no points file at {path} yet)")
    print(f"[{time.time() - t0:.0f} s]")
