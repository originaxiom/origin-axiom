#!/usr/bin/env python3
"""B1354 stage 2 -- THE TOWER CONTINUED: a formal branch tangent to V10 that keeps the three cusp-fixed vectors of rho_0 through order 4
exists (persistence_tower.py: the order-4 conditions have an affine solution family in the second-order class lam2 -- V4, V8, V16 absent,
V6 tied to V14).  Here the tower is climbed order by order.  At order k the unknowns are the free parameters s of lam^(k-2)'s family
(symbolic), lam^(k-1) and lam^(k) (affine); the equations are the relator defects coker R_{k-1}, coker R_k and the obstruction classes
o_{k-1}, o_k of the three fixed vectors; the model is exact quadratic in s (verified at random points), the affine unknowns are
eliminated, and the remaining system in s is decided by a Groebner basis over GF(p).  When solutions exist a point is chosen
(random on an affine family), lam^(k-2) is fixed there, and the climb continues; the branch found is checked at the end by the
Toeplitz kernel dimensions kd(m) = 3m (all three vectors persist through order K).  Two primes.
Usage: python3 continuation.py [KMAX] [prime ...]"""
from __future__ import annotations
import os, sys, time, random
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import persistence_tower as PT
from persistence_tower import Solver, zero, I27, n, OH, S
t0 = time.time()
KMAX = int(sys.argv[1]) if len(sys.argv) > 1 else 8
PR = [int(x) for x in sys.argv[2:]] or [67108819, 67108837]

def equations(st, Y, lams, K):
    """(coker R_3, ..., coker R_K, o_2(e0..e2), ..., o_K(e0..e2)) for the branch with class additions lams[k] (k = 2..K), all parts
    computed by the pivot formulas (polynomial in the lams)."""
    p = st.p
    X = {g: [zero, Y[g]] for g in (1, 2)}
    rel = []
    for k in range(2, K + 1):
        Xk = {g: X[g] + [zero] for g in (1, 2)}
        R = OH.rel_series(st.M, st.Mi, Xk, p, k)
        b = (-R[k].reshape(-1)) % p
        if k >= 3: rel.append(st.d1.coker(b))
        x = st.d1.part_any(b)
        corr = st.unflat(x); add = st.direction(lams.get(k, [0] * 8))
        for g in (1, 2): Xk[g][k] = (corr[g] + add[g]) % p
        X = Xk
    T = st.T_series(X, K)
    obs = []
    for a in range(3):
        o = st.obstructions(T, st.K[a], K)
        obs.append(np.concatenate(o[1:]))                      # o_2..o_K for e_a
    return np.concatenate(rel + obs) % p, X, T

def quad_model(f, nvar, p, rng, checks=2):
    f0 = f(np.zeros(nvar, dtype=np.int64)); N = f0.shape[0]
    lin = np.zeros((N, nvar), dtype=np.int64); quad = {}; inv2 = pow(2, -1, p); fe = []
    for i in range(nvar):
        e = np.zeros(nvar, dtype=np.int64); e[i] = 1; f1 = f(e); e[i] = 2; f2 = f(e)
        q = ((f2 - 2 * f1 + f0) % p * inv2) % p; l = (f1 - f0 - q) % p
        lin[:, i] = l
        if q.any(): quad[(i, i)] = q
        fe.append(f1)
    for i in range(nvar):
        for j in range(i + 1, nvar):
            e = np.zeros(nvar, dtype=np.int64); e[i] = 1; e[j] = 1
            q = (f(e) - fe[i] - fe[j] + f0) % p
            if q.any(): quad[(i, j)] = q
    def model(u):
        u = np.asarray(u, dtype=np.int64) % p; val = (f0 + lin @ u) % p
        for (i, j), q in quad.items():
            c = int(u[i]) * int(u[j]) % p
            if c: val = (val + c * q) % p
        return val
    ok = all(not np.any((model(u) - f(u)) % p) for u in (np.array([rng.randrange(p) for _ in range(nvar)], dtype=np.int64) for _ in range(checks)))
    return f0, lin, quad, ok

def solve_step(st, Y, lams_fixed, k, fam, rng, label):
    """lams_fixed: dict of fixed lam^(j) for j <= k-3; fam: (a, B) affine parametrisation of lam^(k-2) = a + B s (s in F^d);
    unknowns u = (s [d], lam^(k-1) [8], lam^(k) [8]).  Returns (ok, lam_{k-2} chosen, family of lam^(k-1) as (a', B'))."""
    p = st.p; a, B = fam; d = B.shape[1]
    nvar = d + 16
    def lams_of(u):
        L = dict(lams_fixed); L[k - 2] = (a + B @ u[:d]) % p; L[k - 1] = u[d:d + 8]; L[k] = u[d + 8:d + 16]
        return L
    def f(u):
        Ev, _, _ = equations(st, Y, lams_of(u), k)
        return Ev
    t1 = time.time()
    f0, lin, quad, ok = quad_model(f, nvar, p, rng)
    qvars = sorted(set(i for (i, j) in quad for i in (i, j)))
    lvars = [i for i in range(nvar) if i not in qvars]
    print(f"    order {k} [{label}]: unknowns s ({d}) + lam{k-1} (8) + lam{k} (8); {f0.shape[0]} equations; quadratic model exact: {ok}; quadratic unknowns: {len(qvars)} (all among s: {all(i < d for i in qvars)})   ({time.time() - t1:.0f} s)")
    sol = Solver(lin[:, lvars], p); Qp = sol.Q
    Rl = (Qp @ lin[:, qvars]) % p; R0 = (Qp @ f0) % p
    eqs = []
    for r in range(Qp.shape[0]):
        cf = {}
        if R0[r]: cf[()] = int(R0[r])
        for c_, i in enumerate(qvars):
            if Rl[r, c_]: cf[(c_,)] = int(Rl[r, c_])
        for (i, j), q in quad.items():
            c = int((Qp[r] @ q) % p)
            if c: cf[(qvars.index(i), qvars.index(j))] = c
        if cf: eqs.append(cf)
    if eqs:
        monos = sorted(set(m for cf in eqs for m in cf))
        Mat = np.array([[cf.get(m, 0) for m in monos] for cf in eqs], dtype=np.int64) % p
        eqs = [eqs[i] for i in Solver(Mat.T, p).piv]
    names = [f"s{i}" if i < d else f"l{k-1}_{i-d}" if i < d + 8 else f"l{k}_{i-d-8}" for i in qvars]
    if any(set(cf) == {()} for cf in eqs):
        print(f"        ==> inconsistent at the linear level: no continuation at order {k}"); return False, None, None
    import sympy as sp
    if eqs:
        one, G = PT.groebner_decide(eqs, len(qvars), p, names)
        if one:
            print(f"        ==> Groebner basis {{1}}: NO branch keeps the three vectors through order {k} (given the lower choices)"); return False, None, None, None
        exprs = G.exprs
        linear = all(sp.Poly(g, *sp.symbols(names)).total_degree() <= 1 for g in exprs)
        print(f"        ==> {len(eqs)} independent equations in {len(qvars)} quadratic unknowns; Groebner basis: {len(exprs)} elements, all linear: {linear}; e.g. {[str(g)[:60] for g in exprs[:3]]}")
        if not linear:
            print(f"        (non-linear solution set: taking a point by solving the basis is not implemented; stopping)"); return False, None, None, None
        # solve the linear basis for the quadratic unknowns: express as affine family
        xs = sp.symbols(names)
        A = []; bvec = []
        for g in exprs:
            P = sp.Poly(g, *xs); row = [0] * len(qvars); const = 0
            for mono, c in P.terms():
                c = int(c) % p
                if sum(mono) == 0: const = c
                else: row[mono.index(1)] = c
            A.append(row); bvec.append((-const) % p)
        A = np.array(A, dtype=np.int64) % p; bvec = np.array(bvec, dtype=np.int64) % p
        sq = Solver(A, p); part_q = sq.part(bvec); assert part_q is not None
        Kq = sq.kernel                                          # free directions among the quadratic unknowns
    else:
        part_q = np.zeros(len(qvars), dtype=np.int64); Kq = np.eye(len(qvars), dtype=np.int64)
    # choose a random point for the quadratic unknowns, then solve the linear unknowns
    sq_pt = (part_q + (np.array([rng.randrange(p) for _ in range(Kq.shape[0])], dtype=np.int64) @ Kq if Kq.shape[0] else 0)) % p
    u = np.zeros(nvar, dtype=np.int64)
    for c_, i in enumerate(qvars): u[i] = sq_pt[c_]
    # linear unknowns: lin[:, lvars] x = -(f0 + lin[:, qvars] sq + quad(sq))
    rhs = (f0 + lin[:, qvars] @ sq_pt) % p
    for (i, j), q in quad.items():
        c = int(u[i]) * int(u[j]) % p
        if c: rhs = (rhs + c * q) % p
    xl = sol.part((-rhs) % p); assert xl is not None, "linear part inconsistent after Groebner (should not happen)"
    for c_, i in enumerate(lvars): u[i] = xl[c_]
    # the family of the linear unknowns: xl + kernel of lin[:, lvars]; among them lam^(k-1)'s components
    Ev = f(u); assert not np.any(Ev), "chosen point does not satisfy the equations"
    L = lams_of(u)
    # the next family: lam^(k-1) = its chosen value + free directions restricted to lam^(k-1)'s coordinates that keep all equations
    # (directions in ker of the linear part that involve only lam^(k-1) and lam^(k) coordinates -- we carry only those touching lam^(k-1))
    kerL = sol.kernel                                         # directions in the linear unknowns
    dirs = []
    for v in kerL:
        full = np.zeros(nvar, dtype=np.int64)
        for c_, i in enumerate(lvars): full[i] = v[c_]
        if np.any(full[:d]) or np.any(full[d + 8:]): continue    # only pure lam^(k-1) directions (lam^(k) will be re-solved next order)
        dirs.append(full[d:d + 8])
    # add directions among the quadratic unknowns that lie in lam^(k-1)'s block (rare)
    a_next = L[k - 1] % p; B_next = np.array(dirs, dtype=np.int64).T.reshape(8, len(dirs)) % p
    print(f"        chosen lam{k-2} fixed; lam{k-1} family has {len(dirs)} free pure directions carried to the next order")
    return True, L[k - 2], (a_next, B_next), L

def run(p, seed):
    st = PT.Setting(p); rng = random.Random(seed)
    print(f"=== prime p = {p} ===")
    Yc = [0, 0, 0, 0, 1, 0, 0, 0]; Y = st.direction(Yc)
    fam = (np.zeros(8, dtype=np.int64), np.eye(8, dtype=np.int64))
    lams_fixed = {}
    ok, lam_fixed, fam_next, L = solve_step(st, Y, lams_fixed, 4, fam, rng, "lam2 symbolic")
    if not ok: return 4
    lams_fixed[2] = lam_fixed; fam = fam_next
    for k in range(5, KMAX + 1):
        ok, lam_fixed, fam_next, L = solve_step(st, Y, lams_fixed, k, fam, rng, f"lam{k-2} symbolic")
        if not ok: return k
        lams_fixed[k - 2] = lam_fixed; fam = fam_next
    # the branch with every order fixed at the last solved values: the Toeplitz check of stage D (kd(m) = 3m iff all three persist)
    full = dict(lams_fixed); full[KMAX - 1] = L[KMAX - 1]; full[KMAX] = L[KMAX]
    Ev, X, T = equations(st, Y, full, KMAX)
    assert not np.any(Ev)
    kd = st.toeplitz_kd(T, KMAX)
    print(f"    the branch found (class additions at orders 2..{KMAX}; second order: {[int(x) for x in full[2]]}): Toeplitz kernel dimensions kd(1..{KMAX + 1}) = {kd}  (3m = all three cusp-fixed vectors persist through order m)")
    print(f"    second-order class in the block basis {st.labels}: V4 = {int(full[2][1])}, V8 = {int(full[2][3])}, V16 = {int(full[2][7])} (must vanish); V6 = {int(full[2][2])}, V14 = {int(full[2][6])}")
    return None

if __name__ == "__main__":
    res = {}
    for i, p in enumerate(PR):
        res[p] = run(p, 77 + i)
        print(f"    prime {p}: {'the climb continued through order ' + str(KMAX) if res[p] is None else 'stopped at order ' + str(res[p])}   ({time.time() - t0:.0f} s)")
    print(f"[{time.time() - t0:.0f} s]")
