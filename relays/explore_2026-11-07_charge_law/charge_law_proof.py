"""The explore seat, 2026-11-07: THE CHARGE LAW (P-737) -- PROOF_PLAN.md in this folder. Data-free.
  A  Lemma A: excess = 2 log Q(E), Q(E) = v^T E v / v^T v, v = (1, phi) -- against the web seat's excess on all of R1
  B  Lemma B: the multilinear Fibonacci expansion of Q -- against Lemma A on all of R1 and a sample of R2
  C  Lemma C: w(d) = F_d / phi^d >= phi^-2, equality only at d = 2 (d = 1..300)
  D  Lemma D: single runs -- the congruence (L^s = +-I mod N iff N | s) and the apex law (n - 1)/2 + sqrt5/2, n = 2..80
  E  the exhaustive search over SL(2, Z/L) for every nonempty S of {2,3,4,5}: least multi-run B-cost against theta_L;
     fewest extra letters; if HP fails, the sequences under the threshold and their exact Q over gap realizations
    python3 charge_law_proof.py
"""
import importlib.util
import itertools
import math
import pathlib
import random
import sys
import time
from functools import reduce

import mpmath as mp
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))


def load(name):
    sp = importlib.util.spec_from_file_location(name, HERE / (name + ".py"))
    mod = importlib.util.module_from_spec(sp)
    sys.modules[name] = mod
    sp.loader.exec_module(mod)
    return mod


LA = load("least_action_check")
D0 = LA.D0
PHI = (1 + 5 ** 0.5) / 2
SQ5 = 5 ** 0.5
FIB = [0, 1]
while len(FIB) < 420:
    FIB.append(FIB[-1] + FIB[-2])
LM, RM, I2 = ((1, 0), (1, 1)), ((1, 1), (0, 1)), ((1, 0), (0, 1))


def E_int(runs):
    return D0.mul(LA.mat(runs), D0.inv(LA.mat([1] * len(runs))))


def Q_E(E):
    return (E[0][0] + (E[0][1] + E[1][0]) * PHI + E[1][1] * PHI * PHI) / (2 + PHI)


def Q_exp(runs):
    pos = [(i + 1, r - 1) for i, r in enumerate(runs) if r > 1]
    t, tot = len(pos), 1.0
    for mask in range(1, 1 << t):
        A = [pos[i] for i in range(t) if (mask >> i) & 1]
        term = 1.0 / SQ5
        for _, s in A:
            term *= s
        for (p1, _), (p2, _) in zip(A, A[1:]):
            term *= FIB[p2 - p1] / PHI ** (p2 - p1)
        tot += term
    return tot


def mm(X, Y, n):
    return (((X[0][0] * Y[0][0] + X[0][1] * Y[1][0]) % n, (X[0][0] * Y[0][1] + X[0][1] * Y[1][1]) % n),
            ((X[1][0] * Y[0][0] + X[1][1] * Y[1][0]) % n, (X[1][0] * Y[0][1] + X[1][1] * Y[1][1]) % n))


def minv(X, n):
    return ((X[1][1] % n, -X[0][1] % n), (-X[1][0] % n, X[0][0] % n))


def red(X, n):
    return ((X[0][0] % n, X[0][1] % n), (X[1][0] % n, X[1][1] % n))


def pmI(X, N):
    a, b, c, d = X[0][0] % N, X[0][1] % N, X[1][0] % N, X[1][1] % N
    return b == 0 and c == 0 and a == d and a in (1 % N, (N - 1) % N)


def lcm(xs):
    return reduce(lambda a, b: a * b // math.gcd(a, b), xs, 1)


def search(S, budget_extra=1.0, sigma=False):
    Lm = lcm(S)
    r = np.arange(Lm, dtype=np.int64)
    a, b, c, d = np.meshgrid(r, r, r, r, indexing="ij")
    a, b, c, d = a.ravel(), b.ravel(), c.ravel(), d.ravel()
    keep = ((a * d - b * c) % Lm) == (1 % Lm)
    st = np.stack([a[keep], b[keep], c[keep], d[keep]], axis=1).astype(np.int64)
    del a, b, c, d, keep
    n = len(st)
    lookup = np.full(Lm ** 4, -1, dtype=np.int64)
    code = ((st[:, 0] * Lm + st[:, 1]) * Lm + st[:, 2]) * Lm + st[:, 3]
    lookup[code] = np.arange(n)
    # the golden period mod L and the parabolic generators P(p)
    LRm, P, k = red(D0.mul(LM, RM), Lm), red(I2, Lm), 0
    while True:
        P, k = mm(P, LRm, Lm), k + 1
        if P == red(I2, Lm):
            break
    period = 2 * k
    gens, prefix = {}, red(I2, Lm)
    for p in range(1, period + 1):
        T = red(LM if p % 2 == 1 else RM, Lm)
        G = mm(mm(prefix, T, Lm), minv(prefix, Lm), Lm)
        gens.setdefault(G, p)
        prefix = mm(prefix, T, Lm)
    moves = {}
    for G, p in gens.items():
        M = red(I2, Lm)
        for s in range(1, Lm):
            M = mm(M, G, Lm)
            cost = float(s) if sigma else math.log(1 + s / PHI ** 2)
            if M not in moves or cost < moves[M][0]:
                moves[M] = (cost, p, s)
    mlist = list(moves.items())
    mat = np.array([[M[0][0], M[0][1], M[1][0], M[1][1]] for M, _ in mlist], dtype=np.int64)
    mcost = np.array([v[0] for _, v in mlist])
    theta = float(Lm) if sigma else math.log(1 + Lm / PHI ** 2)
    budget = theta + budget_extra
    dist = np.full(n, np.inf)
    pred_state = np.full(n, -1, dtype=np.int64)
    pred_move = np.full(n, -1, dtype=np.int64)
    first = {}  # t = 1: E = L^{s1} at phase 1
    for s1 in range(1, Lm):
        E1 = red(D0.pw(LM, s1), Lm)
        c1 = float(s1) if sigma else math.log(1 + s1 / PHI ** 2)
        first[s1] = (E1, c1)
        na = (E1[0][0] * mat[:, 0] + E1[0][1] * mat[:, 2]) % Lm
        nb = (E1[0][0] * mat[:, 1] + E1[0][1] * mat[:, 3]) % Lm
        nc = (E1[1][0] * mat[:, 0] + E1[1][1] * mat[:, 2]) % Lm
        nd = (E1[1][0] * mat[:, 1] + E1[1][1] * mat[:, 3]) % Lm
        tgt = lookup[((na * Lm + nb) * Lm + nc) * Lm + nd]
        cand = c1 + mcost
        better = cand < dist[tgt]
        dist[tgt[better]] = cand[better]
        pred_state[tgt[better]] = -s1
        pred_move[tgt[better]] = np.flatnonzero(better)
    cmin = mcost.min()
    it, changed = 0, True
    while changed:
        changed, it = False, it + 1
        act = np.flatnonzero(dist + cmin <= budget)
        if len(act) == 0:
            break
        Ea, da = st[act], dist[act].copy()
        for j in range(len(mlist)):
            m0, m1, m2, m3 = mat[j]
            cand = da + mcost[j]
            sel = cand <= budget
            if not sel.any():
                continue
            E_ = Ea[sel]
            na = (E_[:, 0] * m0 + E_[:, 1] * m2) % Lm
            nb = (E_[:, 0] * m1 + E_[:, 1] * m3) % Lm
            nc = (E_[:, 2] * m0 + E_[:, 3] * m2) % Lm
            nd = (E_[:, 2] * m1 + E_[:, 3] * m3) % Lm
            tgt = lookup[((na * Lm + nb) * Lm + nc) * Lm + nd]
            cs = cand[sel]
            better = cs < dist[tgt] - 1e-12
            if better.any():
                dist[tgt[better]] = cs[better]
                pred_state[tgt[better]] = act[sel][better]
                pred_move[tgt[better]] = j
                changed = True
    cong = np.ones(n, dtype=bool)
    for N in S:
        A_, B_, C_, D_ = st[:, 0] % N, st[:, 1] % N, st[:, 2] % N, st[:, 3] % N
        cong &= (B_ == 0) & (C_ == 0) & (A_ == D_) & ((A_ == 1 % N) | (A_ == (N - 1) % N))
    idx = np.flatnonzero(cong & np.isfinite(dist))
    if len(idx) == 0:
        return dict(L=Lm, period=period, gens=len(gens), moves=len(mlist), states=n, iters=it, theta=theta,
                    best=None, path=None)
    best = idx[np.argmin(dist[idx])]
    path, x = [], best
    while True:
        j = pred_move[x]
        _, (cst, p, s) = mlist[j]
        path.append((p, s))
        if pred_state[x] < 0:
            path.append((1, -pred_state[x]))
            break
        x = pred_state[x]
    path.reverse()
    under = int(np.sum(dist[cong] <= theta)) if not sigma else int(np.sum(dist[cong] < theta))
    return dict(L=Lm, period=period, gens=len(gens), moves=len(mlist), states=n, iters=it, theta=theta,
                best=float(dist[best]), path=path, under=under)


if __name__ == "__main__":
    t0 = time.time()
    print("THE CHARGE LAW (P-737) -- the proof's computations (the explore seat, 2026-11-07)")

    print("\nA. Lemma A on all of R1: |2 log Q(E) - excess| (excess = the web seat's, k = 20)")
    R1 = list(LA.space())
    worst = 0.0
    for runs in R1:
        q = Q_E(E_int(runs))
        worst = max(worst, abs(2 * math.log(q) - float(LA.excess(runs))))
    print("  %d defects; max |difference| %.3e; Lemma A holds: %s" % (len(R1), worst, worst < 1e-9))

    print("\nB. Lemma B (the Fibonacci expansion) against Lemma A")
    worstB = max(abs(Q_exp(r) - Q_E(E_int(r))) / Q_E(E_int(r)) for r in R1)
    random.seed(737)
    sample = []
    for _ in range(4000):
        m = random.choice([2, 3, 4, 5])
        top = {2: 64, 3: 64, 4: 24, 5: 10}[m]
        runs = tuple([random.randint(2, top)] + [random.randint(1, top) for _ in range(m - 2)] + [random.randint(2, top)])
        sample.append(runs)
    worstB2 = max(abs(Q_exp(r) - Q_E(E_int(r))) / Q_E(E_int(r)) for r in sample)
    print("  R1: max relative difference %.3e; R2 sample of %d: %.3e; Lemma B holds: %s" % (
        worstB, len(sample), worstB2, max(worstB, worstB2) < 1e-9))

    print("\nC. Lemma C: w(d) = F_d / phi^d against phi^-2, d = 1..300")
    mp.mp.dps = 50
    ws = [mp.mpf(FIB[dd]) / mp.phi ** dd for dd in range(1, 301)]
    floor = mp.phi ** -2
    print("  min over d: %s at d = %d; phi^-2 = %s; w(d) > phi^-2 for every d != 2: %s" % (
        mp.nstr(min(ws), 15), 1 + ws.index(min(ws)), mp.nstr(floor, 15),
        all(w > floor for i, w in enumerate(ws) if i != 1) and abs(ws[1] - floor) < mp.mpf(10) ** -40))

    print("\nD. Lemma D: single runs")
    ok_cong = all(pmI(red(D0.pw(LM, s), N), N) == (s % N == 0) for N in (2, 3, 4, 5) for s in range(1, 121))
    print("  L^s = +-I mod N iff N | s (N = 2..5, s = 1..120): %s" % ok_cong)
    worstD = 0
    for nn in range(2, 81):
        im, _ = D0.highest_cf(LA.closed_runs((nn,), 20), reps=20)
        worstD = max(worstD, abs(float(im) - ((nn - 1) / 2 + SQ5 / 2)))
    print("  apex law (n - 1)/2 + sqrt5/2 for n = 2..80: max |difference| %.3e; holds: %s" % (worstD, worstD < 1e-9))

    print("\nE. the exhaustive search, every nonempty S of {2,3,4,5}")
    subsets = [S for k in range(1, 5) for S in itertools.combinations((2, 3, 4, 5), k)]
    all_hold = True
    for S in subsets:
        t1 = time.time()
        rb = search(S)
        rs = search(S, budget_extra=0.0, sigma=True)
        if rb["best"] is None:
            verdict = "no premise-satisfying multi-run state within theta + 1 (HP holds)"
            hold = True
        else:
            hold = rb["best"] > rb["theta"]
            verdict = "least multi-run B-cost %.6f vs theta %.6f, margin %+.6f, path %s; states at or under theta: %d" % (
                rb["best"], rb["theta"], rb["best"] - rb["theta"], rb["path"], rb["under"])
        all_hold &= hold
        sig = ("fewest extra letters (multi-run) %d vs L = %d, path %s" % (rs["best"], rs["L"], rs["path"])
               if rs["best"] is not None else "no multi-run state with fewer than L extra letters")
        print("  S = %-14s L = %2d  period %3d  generators %3d  moves %5d  |SL(2,Z/L)| %6d  iters %2d  (%.0f s)" % (
            S, rb["L"], rb["period"], rb["gens"], rb["moves"], rb["states"], rb["iters"], time.time() - t1))
        print("      HP: %s -- %s" % (hold, verdict))
        print("      sigma: %s" % sig)
    print("\n  HP for every S: %s" % all_hold)
    print("\nruntime %.1f s" % (time.time() - t0))
    print("charge_law_proof exit 0")
