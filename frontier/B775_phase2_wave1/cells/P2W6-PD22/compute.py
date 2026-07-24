"""P2W6-PD22 (OI-133) -- PD2.2: the phase-map riddle.

QUESTION. After the pentagon-pair phase prediction was killed at rung 75 (B374) and the
existence law itself died at N = 225, what does the existence law ACTUALLY determine about
the phase map -- or is the phase genuinely free?

SEALED CRITERION. phase map characterized (what the law determines, shown) => RESOLVED-A /
the phase is genuinely free (tombstone) => RESOLVED-B.

CONVENTIONS (declared; identical to B372 frontier/B372_level45_sweeper/fp_engine.Level,
re-implemented over F_p in exact float64 BLAS arithmetic for speed -- every product is
< 2^53 so the arithmetic is EXACT, not floating):
    N odd; p prime, p = 1 mod M with M = lcm(4N, ord W1); zeta_M = g^((p-1)/M) for g a
    primitive root; zeta_{4N} = zeta_M^{M/4N}; zeta_N = zeta_{4N}^4; zeta_o = zeta_M^{M/o}
    (equals B372's zo = z^{4N/o} whenever o | 4N, which holds at every banked rung).
    D  = diag(zeta_N^{j(j-1)/2}),  F = [zeta_N^{ij}],  Fi = F^{-1},
    WR = F D^{-1} F^{-1},  W1 = WR . D.  Tested group G = <D, WR> (B374 rung135.py).
    SECTOR (B374 convention) = the span of the W1-eigenvectors of a multiplicity-1 OPPOSITE
    exponent pair {a, o-a}, invariant under both generators.
    LINE = a 1-dimensional G-invariant subspace (a 1-dim subrepresentation).
    PHASE = 360*a/o degrees for the sector exponent a (trace on the sector = 2 cos phase).

HOUSE-METHOD LESSONS, explicit:
 L1 no MB12 vacuity  -- verdict() is a pure function; it is exercised on FOUR logically
                        possible fact-vectors, and both RESOLVED branches fire.
 L2 no unearned negative -- every negative here is an exact finite census, not an estimate.
 L3 no forced reason -- the two load-bearing facts are logically independent and are
                        labelled; the closed-form angle rule is declared a COROLLARY of the
                        twist map, not counted as a separate reason.
 L4 no undeclared selection -- the banked arc sampled only N in 15*3^k / 15*5^k; that
                        selection is DECLARED and its effect is shown (it manufactures both
                        the "pentagon pair" and the "ord = 4N/3" law).
"""
import json
import os
import sys
import time
from math import gcd

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
T0 = time.time()
R = {}          # results.json payload
LOG = []


def say(*a):
    s = " ".join(str(x) for x in a)
    LOG.append(s)
    print(s, flush=True)


def lcm(a, b):
    return a * b // gcd(a, b)


# ----------------------------------------------------------------- number theory
def is_prime(n):
    if n < 2:
        return False
    for q in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        if n % q == 0:
            return n == q
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37):
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def primes_1_mod(m, count, start=10 ** 5):
    out, k = [], start // m + 1
    while len(out) < count:
        p = m * k + 1
        if is_prime(p):
            out.append(p)
        k += 1
    return out


def primitive_root(p):
    fac, n = [], p - 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            fac.append(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        fac.append(n)
    g = 2
    while True:
        if all(pow(g, (p - 1) // q, p) != 1 for q in fac):
            return g
        g += 1


# ----------------------------------------------------------------- the level engine
class Lvl:
    """Level-N Weil data over F_p.  zN_val = the value of zeta_N used (a twist
    zeta_N -> zeta_N^u is realised by passing zeta_N^u here)."""

    def __init__(self, N, p, zN_val):
        assert N % 2 == 1
        self.N, self.p, self.zN = N, p, zN_val
        pw = np.array([pow(zN_val, e, p) for e in range(N)], dtype=np.float64)
        j = np.arange(N)
        self.D = np.diag(pw[(j * (j - 1) // 2) % N])
        Di = np.diag(pw[(-(j * (j - 1) // 2)) % N])
        F = pw[np.outer(j, j) % N]
        Fi = np.mod(pw[(-np.outer(j, j)) % N] * pow(N, p - 2, p), p)
        self.WR = self.mm(self.mm(F, Di), Fi)
        self.W1 = self.mm(self.WR, self.D)
        # exactness guard: max row-sum of a product must stay below 2^53
        assert N * (p - 1) ** 2 < 2 ** 53, "F_p float64 exactness guard"

    def mm(self, A, B):
        return np.mod(A @ B, self.p)

    def mv(self, A, v):
        return np.mod(A @ v, self.p)


def order_of(L, M, cap=4000):
    I = np.eye(L.N)
    P = M.copy()
    for k in range(1, cap + 1):
        if np.array_equal(P, I):
            return k
        P = L.mm(P, M)
    raise RuntimeError("order cap")


def rank_mod(rows, p):
    """rank over F_p of a short list of long vectors (Gauss-Jordan, vectorised).
    Exact integer arithmetic: entries stay < p < 2^31 so all products fit in int64."""
    M = [np.mod(np.asarray(r, dtype=np.int64), p) for r in rows]
    rank = 0
    for i in range(len(M)):
        nz = np.nonzero(M[i])[0]
        if nz.size == 0:
            continue
        c = int(nz[0])
        v = (M[i] * pow(int(M[i][c]), p - 2, p)) % p
        M[i] = v
        for k in range(len(M)):
            if k != i:
                f = int(M[k][c])
                if f:
                    M[k] = (M[k] - f * v) % p
        rank += 1
    return rank


def nullspace(A, p):
    m, n = A.shape
    M = np.mod(A, p).astype(np.int64).tolist()
    piv, r = [], 0
    for c in range(n):
        pr = None
        for i in range(r, m):
            if M[i][c] % p:
                pr = i
                break
        if pr is None:
            continue
        M[r], M[pr] = M[pr], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [x * inv % p for x in M[r]]
        for i in range(m):
            if i != r and M[i][c] % p:
                f = M[i][c]
                M[i] = [(M[i][j] - f * M[r][j]) % p for j in range(n)]
        piv.append(c)
        r += 1
        if r == m:
            break
    out = []
    for fc in [c for c in range(n) if c not in piv]:
        v = [0] * n
        v[fc] = 1
        for i, c in enumerate(piv):
            v[c] = (-M[i][fc]) % p
        out.append(np.array(v, dtype=np.float64))
    return out


def _order_stage(N, u=1, start=10 ** 5):
    p0 = primes_1_mod(4 * N, 1, start=start)[0]
    g0 = primitive_root(p0)
    z = pow(pow(g0, (p0 - 1) // N, p0), u, p0)
    return order_of(Lvl(N, p0, z), Lvl(N, p0, z).W1)


def level_census(N, u=1, nprimes=2, start=10 ** 5, want_eig=False):
    """Full sector census at level N (twist u).  Returns order, #mult-1 opposite pairs,
    the invariant sectors (exponent pairs) and, optionally, their W1 eigenvalues in F_p."""
    o = _order_stage(N, u, start)
    M = lcm(4 * N, o)
    out = None
    for p in primes_1_mod(M, nprimes, start=start):
        g = primitive_root(p)
        zM = pow(g, (p - 1) // M, p)
        L = Lvl(N, p, pow(pow(zM, M // N, p), u, p))
        assert order_of(L, L.W1) == o
        zo = pow(zM, M // o, p)
        zop = [pow(zo, k, p) for k in range(o)]
        tr, P = [], np.eye(N)
        for _ in range(o):
            tr.append(int(np.trace(P)) % p)
            P = L.mm(P, L.W1)
        oinv = pow(o, p - 2, p)
        dims = [sum(zop[(-j * a) % o] * tr[j] for j in range(o)) % p * oinv % p
                for a in range(o)]
        assert sum(dims) % p == N % p and all(d <= N for d in dims)
        m1 = [a for a in range(1, o) if dims[a] == 1 and dims[(o - a) % o] == 1
              and a < (o - a) % o]
        need = sorted(set([a for a in m1] + [(o - a) % o for a in m1]))
        vec, sectors, eigs = {}, [], []
        for e in range(N):
            miss = [a for a in need if a not in vec]
            if not miss:
                break
            acc = {a: np.zeros(N) for a in miss}
            w = np.zeros(N)
            w[e] = 1.0
            for j in range(o):
                for a in miss:
                    acc[a] = np.mod(acc[a] + zop[(-j * a) % o] * w, p)
                w = L.mv(L.W1, w)
            for a in miss:
                if acc[a].any():
                    vec[a] = acc[a]
        assert len(vec) == len(need)
        for a in m1:
            b = (o - a) % o
            va, vb = vec[a], vec[b]
            if rank_mod([va, vb], p) != 2:
                continue
            ok = True
            for G in (L.D, L.WR):
                for v in (va, vb):
                    if rank_mod([va, vb, L.mv(G, v)], p) != 2:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                sectors.append((a, b))
                if want_eig:
                    i = int(np.nonzero(va)[0][0])
                    lam = int(L.mv(L.W1, va)[i]) * pow(int(va[i]), p - 2, p) % p
                    eigs.append((lam, p))
        rec = dict(N=N, u=u, order=o, n_mult1_pairs=len(m1), sectors=sectors,
                   n_mult_ge2=sum(1 for d in dims if d >= 2))
        if want_eig:
            rec["eigs"] = eigs
        if out is None:
            out = rec
        else:
            assert (out["order"], out["sectors"]) == (rec["order"], rec["sectors"]), (out, rec)
    out["phases_deg"] = [round(360 * min(a, b) / out["order"], 6) for a, b in out["sectors"]]
    out["cross_prime"] = nprimes
    return out


def line_census(q, u=1, start=10 ** 5):
    """ALL G-invariant LINES of the level-q object (twist u) -- exhaustive.
    A line is a common eigenvector of D and WR.  D is diagonal, so the line is supported
    inside one D-value coordinate class S; then WR v = beta v forces v in ker(WR[out,S]),
    and beta is a root of unity of order dividing ord(WR), so the finitely many candidate
    beta are enumerated exactly.  No approximation anywhere."""
    o = _order_stage(q, u, start)
    oW = None
    M0 = lcm(4 * q, o)
    p = primes_1_mod(M0, 1, start=start)[0]
    g = primitive_root(p)
    zM = pow(g, (p - 1) // M0, p)
    L = Lvl(q, p, pow(pow(zM, M0 // q, p), u, p))
    oW = order_of(L, L.WR)
    # a root of unity of order oW inside F_p (enlarge the prime if needed)
    if (p - 1) % oW:
        M1 = lcm(M0, oW)
        p = primes_1_mod(M1, 1, start=start)[0]
        g = primitive_root(p)
        zM = pow(g, (p - 1) // M1, p)
        L = Lvl(q, p, pow(pow(zM, M1 // q, p), u, p))
        oW = order_of(L, L.WR)
    zW = pow(g, (p - 1) // oW, p)
    betas = [pow(zW, k, p) for k in range(oW)]
    cls = {}
    for i in range(q):
        cls.setdefault(int(L.D[i, i]), []).append(i)
    lines, wide = [], 0
    for alpha, S in cls.items():
        out_idx = [i for i in range(q) if i not in S]
        Bin = L.WR[np.ix_(S, S)]
        if out_idx:
            K = nullspace(L.WR[np.ix_(out_idx, S)], p)
        else:
            K = [np.eye(len(S))[k] for k in range(len(S))]
        if not K:
            continue
        wide = max(wide, len(K))
        KB = np.array(K).T                       # |S| x k
        for beta in betas:
            Mb = np.mod(np.mod(Bin @ KB, p) - beta * KB, p)
            for c in nullspace(Mb, p):
                v = np.zeros(q)
                w = np.mod(KB @ c, p)
                if not w.any():
                    continue
                v[S] = w
                assert rank_mod([v, L.mv(L.WR, v)], p) == 1
                assert rank_mod([v, L.mv(L.D, v)], p) == 1
                i = int(np.nonzero(v)[0][0])
                lam = int(L.mv(L.W1, v)[i]) * pow(int(v[i]), p - 2, p) % p
                lines.append(dict(lam=lam, p=p, trivial=(lam == 1),
                                  beta=beta, alpha=alpha))
    return dict(q=q, u=u, order=o, ord_WR=oW, lines=lines, p=p, max_class_dim=wide)


def crt_perm(q1, q2):
    N = q1 * q2
    P = np.zeros((N, N))
    for j in range(N):
        P[(j % q1) * q2 + (j % q2), j] = 1.0
    return P


def tensor_check(q1, q2, start=10 ** 5):
    """exact CRT tensor identity  P (X_N) P^T = X'_{q1} (x) X'_{q2}  for X = D, WR, W1."""
    N = q1 * q2
    p = primes_1_mod(4 * N, 1, start=start)[0]
    g = primitive_root(p)
    zN = pow(g, (p - 1) // N, p)
    L = Lvl(N, p, zN)
    u1, u2 = pow(q2, -1, q1), pow(q1, -1, q2)
    A = Lvl(q1, p, pow(pow(zN, q2, p), u1, p))
    B = Lvl(q2, p, pow(pow(zN, q1, p), u2, p))
    P = crt_perm(q1, q2)
    ok = {}
    for nm in ("D", "WR", "W1"):
        X = getattr(L, nm)
        ok[nm] = bool(np.array_equal(np.mod(np.mod(P @ X, p) @ P.T, p),
                                     np.mod(np.kron(getattr(A, nm), getattr(B, nm)), p)))
    return ok, (u1, u2)


# ============================================================ STAGE 1 -- reproduction
say("=" * 78)
say("STAGE 1  reproduce the banked PD2.2 rungs (B372/B373/B374 + rung75/rung225)")
BANKED = {15: (20, 3, [(6, 14)]), 45: (60, 6, [(6, 54)]), 75: (100, 13, [(25, 75)]),
          135: (180, 15, [(54, 126)]), 225: (300, 16, [])}
rep_ok, rep_rows = True, []
for N, (o, npr, sec) in BANKED.items():
    r = level_census(N)
    hit = (r["order"] == o and r["n_mult1_pairs"] == npr and r["sectors"] == sec)
    rep_ok &= hit
    rep_rows.append(dict(N=N, order=r["order"], pairs=r["n_mult1_pairs"],
                         sectors=r["sectors"], phase=r["phases_deg"], banked_match=hit))
    say(f"  N={N:4d} ord={r['order']:4d} pairs={r['n_mult1_pairs']:3d} "
        f"sectors={r['sectors']} phase={r['phases_deg']} banked_match={hit}")
R["stage1_reproduction"] = dict(rows=rep_rows, all_match=bool(rep_ok))
say(f"  ALL BANKED RUNGS REPRODUCED: {rep_ok}")

# ============================================================ STAGE 2 -- the selection
say("")
say("=" * 78)
say("STAGE 2  DECLARED SELECTION (L4): the banked arc sampled ONLY N in 15*3^k / 15*5^k.")
say("         Widening to all odd N in [3,49] + {63,75,105,135,147,225,243,245}:")
SCAN = [3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43,
        45, 47, 49, 63, 75, 105, 135, 147, 225, 243, 245]
scan = {}
for N in SCAN:
    r = level_census(N)
    scan[N] = r
    say(f"  N={N:4d} ord={r['order']:4d} 4N/3={4*N/3:8.2f} pairs={r['n_mult1_pairs']:3d} "
        f"sectors={r['sectors']} phase={r['phases_deg']}")
R["stage2_scan"] = {str(N): dict(order=r["order"], pairs=r["n_mult1_pairs"],
                                 sectors=r["sectors"], phase=r["phases_deg"])
                    for N, r in scan.items()}
sel_phases = sorted({p for N in (15, 45, 135) for p in scan[N]["phases_deg"]})
wide_phases = sorted({p for N in SCAN for p in scan[N]["phases_deg"]})
ord_law = {N: (scan[N]["order"] == 4 * N // 3 if N % 3 == 0 else None) for N in SCAN}
ord_law_fails = [N for N, v in ord_law.items() if v is False]
say(f"  SELECTION EFFECT phases inside the banked 3-tower {{15,45,135}}: {sel_phases}"
    f"  (the 'pentagon pair')")
say(f"  SELECTION EFFECT phases over the widened frame:              {wide_phases}")
say(f"  SELECTION EFFECT 'ord = 4N/3' FAILS at N = {ord_law_fails} (3|N but ord != 4N/3)")
R["stage2_selection_effect"] = dict(banked_tower_phases=sel_phases,
                                    widened_phases=wide_phases,
                                    ord_4N_over_3_fails_at=ord_law_fails)

# ============================================================ STAGE 3 -- the mechanism
say("")
say("=" * 78)
say("STAGE 3  MECHANISM: the exact CRT tensor identity (independent fact #1)")
SPLITS = [(3, 5), (9, 5), (27, 5), (3, 25), (9, 25), (3, 7), (5, 7), (5, 9), (3, 11),
          (3, 13), (7, 9), (49, 3), (49, 5), (3, 35), (15, 7), (5, 27), (25, 27), (81, 5)]
tens_rows, tens_ok = [], True
for q1, q2 in SPLITS:
    ok, u = tensor_check(q1, q2)
    good = all(ok.values())
    tens_ok &= good
    tens_rows.append(dict(q1=q1, q2=q2, N=q1 * q2, exact=good, twists=list(u)))
    say(f"  {q1:3d} x {q2:3d} = {q1*q2:5d}: D,WR,W1 tensor-exact = {good}  twists={u}")
say(f"  TENSOR IDENTITY EXACT EVERYWHERE TESTED: {tens_ok}")
R["stage3_tensor"] = dict(rows=tens_rows, all_exact=bool(tens_ok))

# ============================================================ STAGE 4 -- the atoms
say("")
say("=" * 78)
say("STAGE 4  THE ATOMS: lines and sectors of each prime power (independent fact #2)")
ATOMS = [3, 9, 27, 81, 243, 5, 25, 125, 7, 49, 343, 11, 13, 121, 169]
atom = {}
for q in ATOMS:
    lc = line_census(q)
    sc = level_census(q, want_eig=True)
    typ = ("SECTOR+LINE" if lc["lines"] and sc["sectors"] else
           "SECTOR" if sc["sectors"] else "LINE" if lc["lines"] else "NEITHER")
    atom[q] = dict(order=sc["order"], n_lines=len(lc["lines"]),
                   line_all_trivial=all(l["trivial"] for l in lc["lines"]),
                   sectors=sc["sectors"], phase=sc["phases_deg"],
                   n_mult_ge2=sc["n_mult_ge2"], type=typ,
                   max_class_dim=lc["max_class_dim"])
    say(f"  q={q:4d} ord={sc['order']:4d}  #lines={len(lc['lines'])} "
        f"(all W1-eigenvalue 1: {all(l['trivial'] for l in lc['lines']) if lc['lines'] else 'n/a'})  "
        f"#sectors={len(sc['sectors'])} phase={sc['phases_deg']}  TYPE={typ}"
        + (f"   [W1 mult>=2 at {sc['n_mult_ge2']} exponents; the sector census keeps the"
           " B374 mult-1 opposite-pair convention -- DECLARED]" if sc["n_mult_ge2"] else ""))
R["stage4_atoms"] = {str(q): a for q, a in atom.items()}
say("  ATOM LAW (read off): 3^odd = SECTOR+LINE, 3^even = LINE, 5^odd = SECTOR,")
say("                       5^even = LINE, p^even (p>=7) = LINE, p^odd (p>=7) = NEITHER")


def atom_type(p_, e):
    """(has_line, has_sector) for the prime power p^e, from the STAGE-4 atom law."""
    if e == 0:
        return (True, False)
    if p_ == 3:
        return (True, e % 2 == 1)
    if p_ == 5:
        return (e % 2 == 0, e % 2 == 1)
    return (e % 2 == 0, False)


def factor(n):
    f, d = {}, 2
    while d * d <= n:
        while n % d == 0:
            f[d] = f.get(d, 0) + 1
            n //= d
        d += 1
    if n > 1:
        f[n] = f.get(n, 0) + 1
    return f


def predict_count(N):
    """#(2-dim invariant sectors) = #ways to pick ONE sector-factor, lines elsewhere."""
    fs = factor(N)
    tot = 0
    for p_ in fs:
        if not atom_type(p_, fs[p_])[1]:
            continue
        if all(atom_type(q_, e_)[0] for q_, e_ in fs.items() if q_ != p_):
            tot += 1
    return tot


def predict_phase(N):
    """the closed form (COROLLARY of the STAGE-6 twist map, not an independent reason)."""
    fs = factor(N)
    if predict_count(N) != 1:
        return None
    if fs.get(5, 0) % 2 == 1:                      # the 5-part supplies the sector
        m = N // 5 ** fs[5]
        return 36.0 if pow(m, 2, 5) == 1 else 108.0    # Legendre symbol (m|5)
    return 90.0                                    # the 3-part supplies the sector


# ============================================================ STAGE 5 -- existence law
say("")
say("=" * 78)
say("STAGE 5  EXISTENCE LAW vs the direct census (the CONVERSE direction is fact #2b:")
say("         the direct census is an INDEPENDENT check that no further sector exists)")
ex_hit = ex_tot = 0
ex_rows = []
for N in SCAN:
    pred, obs = predict_count(N), len(scan[N]["sectors"])
    ex_tot += 1
    ex_hit += (pred == obs)
    ex_rows.append(dict(N=N, predicted=pred, observed=obs, hit=pred == obs))
    if pred != obs:
        say(f"  MISMATCH N={N}: predicted {pred}, observed {obs}")
say(f"  existence law: {ex_hit}/{ex_tot} levels predicted correctly (incl. the N=225 death)")
R["stage5_existence"] = dict(hits=ex_hit, total=ex_tot, rows=ex_rows)

# ============================================================ STAGE 6 -- the phase law
say("")
say("=" * 78)
say("STAGE 6  THE PHASE MAP: the twist -> phase map on the atoms")
tw_rows = []
for q in (3, 27, 5, 125):
    for u in range(1, min(q, 8)):
        if gcd(u, q) != 1:
            continue
        rr = level_census(q, u=u, nprimes=1)
        tw_rows.append(dict(q=q, u=u, phase=rr["phases_deg"]))
        say(f"  atom q={q:4d} twist u={u}: sector phase = {rr['phases_deg']} deg"
            + (f"   [(u|5) = {1 if pow(u,2,5)==1 else -1}]" if q % 5 == 0 else ""))
say("  TWIST MAP: a 3-power atom's phase is twist-RIGID at 90 deg (eigenvalue +-i);")
say("             a 5-power atom's phase is 36 deg iff (u|5) = +1, else 108 deg.")
R["stage6_twistmap"] = tw_rows

say("")
say("  CLOSED FORM (corollary): sector exists  <=>  v_p(N) even for every p >= 7 AND")
say("     (v_3(N) odd or v_5(N) odd).  Phase = 90 deg if v_5(N) is even (the 3-part")
say("     supplies it); else 36 deg if (N/5^v5 | 5) = +1 and 108 deg if = -1.")
ph_hit = ph_tot = 0
ph_rows = []
for N in SCAN:
    if not scan[N]["sectors"]:
        continue
    pred, obs = predict_phase(N), scan[N]["phases_deg"][0]
    ph_tot += 1
    ph_hit += (pred == obs)
    ph_rows.append(dict(N=N, predicted=pred, observed=obs, hit=pred == obs))
    say(f"  N={N:4d}: predicted {pred} deg, observed {obs} deg  hit={pred == obs}")
say(f"  phase law: {ph_hit}/{ph_tot}")
R["stage6_phase_insample"] = dict(hits=ph_hit, total=ph_tot, rows=ph_rows)

# ============================================================ STAGE 7 -- held out
say("")
say("=" * 78)
say("STAGE 7  HELD-OUT PREDICTIONS (registered in-code BEFORE the heavy census;")
say("         375/405/675 are exactly the three levels B374 pre-registered)")
HELDOUT = {375: (1, 108.0), 405: (1, 36.0), 675: (1, 90.0)}
say("  B374's registered pre-registration:  405 EXISTS/36deg,  375 EXISTS,  675 NO SECTOR")
say("  THIS CELL predicts:                  405 EXISTS/36deg,  375 EXISTS/108deg,"
    "  675 EXISTS/90deg")
say("  => 675 is a DECISIVE disagreement with the banked pre-registration.")
ho_hit = ho_tot = 0
ho_rows = []
for N, (pc, pp) in HELDOUT.items():
    assert predict_count(N) == pc and predict_phase(N) == pp, "prediction drift"
    t = time.time()
    r = level_census(N, nprimes=2)          # cross-prime confirmed, as the banked rungs are
    obs_c = len(r["sectors"])
    obs_p = r["phases_deg"][0] if r["sectors"] else None
    hit = (obs_c == pc and obs_p == pp)
    ho_tot += 1
    ho_hit += hit
    ho_rows.append(dict(N=N, pred_count=pc, obs_count=obs_c, pred_phase=pp,
                        obs_phase=obs_p, hit=hit, order=r["order"],
                        pairs=r["n_mult1_pairs"]))
    say(f"  N={N:4d} ord={r['order']:4d} pairs={r['n_mult1_pairs']:3d} "
        f"sectors={r['sectors']} phase={obs_p}  PREDICTED ({pc}, {pp})  hit={hit} "
        f"[{time.time()-t:.0f}s]")
say(f"  held-out: {ho_hit}/{ho_tot}")
b675 = next(r for r in ho_rows if r["N"] == 675)
R["stage7_heldout"] = dict(hits=ho_hit, total=ho_tot, rows=ho_rows,
                           b374_prereg_675_no_sector_refuted=bool(b675["obs_count"] == 1))
say(f"  B374's registered 'N=675: NO sector' is REFUTED by direct computation: "
    f"675 carries {b675['obs_count']} sector at phase {b675['obs_phase']} deg "
    f"(cross-prime confirmed).")

# ============================================================ STAGE 8 -- verdict
say("")
say("=" * 78)
say("STAGE 8  VERDICT LOGIC (pure function; exercised on counterfactual fact-vectors)")


def verdict(F):
    """F = fact-vector.  Returns (verdict, reason).  All three outcomes reachable."""
    if not F["banked_reproduced"]:
        return "UNRESOLVED", "engine fails to reproduce the banked rungs"
    if F["sector_levels"] < 3:
        return "UNRESOLVED", "fewer than 3 levels carry a sector: underpowered"
    if not F["tensor_exact"]:
        return "UNRESOLVED", "no factorisation mechanism established"
    # is the phase a FUNCTION of the structural invariants at all?
    if not F["phase_is_function_of_invariants"]:
        return "RESOLVED-B", ("two levels share every structural invariant yet carry "
                              "different phases: the phase is genuinely free")
    ex = F["existence_hits"] == F["existence_total"]
    ph = F["phase_hits"] == F["phase_total"]
    ho = F["heldout_hits"] == F["heldout_total"]
    if ex and ph and ho and F["heldout_total"] >= 3:
        return "RESOLVED-A", ("the phase map is characterised: existence + phase are "
                              "fixed functions of the prime factorisation of N")
    if ph and ex and not ho:
        return "UNRESOLVED", "law fits in-sample but fails held-out levels"
    if F["phase_hits"] == 0:
        return "RESOLVED-B", "no structural rule reproduces any observed phase: free"
    return "UNRESOLVED", "the law is only partial"


# is the phase a function of the invariants?  (invariant = (which part supplies the
# sector, the Legendre symbol of the co-factor));  collision test over all levels
inv_map = {}
phase_functional = True
for N in list(SCAN) + list(HELDOUT):
    ph = (scan[N]["phases_deg"][0] if N in scan and scan[N]["sectors"]
          else next((r["obs_phase"] for r in ho_rows if r["N"] == N), None))
    if ph is None:
        continue
    fs = factor(N)
    key = ("five" if fs.get(5, 0) % 2 == 1 else "three",
           1 if fs.get(5, 0) % 2 == 1 and pow(N // 5 ** fs[5], 2, 5) == 1 else
           (-1 if fs.get(5, 0) % 2 == 1 else 0))
    if key in inv_map and inv_map[key] != ph:
        phase_functional = False
    inv_map[key] = ph
say(f"  invariant -> phase table (collision-free = {phase_functional}): "
    + str({str(k): v for k, v in inv_map.items()}))

FACTS = dict(banked_reproduced=bool(rep_ok), tensor_exact=bool(tens_ok),
             sector_levels=ph_tot + ho_tot,
             existence_hits=ex_hit, existence_total=ex_tot,
             phase_hits=ph_hit, phase_total=ph_tot,
             heldout_hits=ho_hit, heldout_total=ho_tot,
             phase_is_function_of_invariants=bool(phase_functional))
V, WHY = verdict(FACTS)
R["facts"] = FACTS
R["verdict"] = V
R["verdict_reason"] = WHY
R["phase_map"] = dict(
    mechanism="level-N Weil data = tensor product over prime powers (exact CRT identity)",
    order="ord W1(N) = lcm_p ord(p^e); ord(3^a)=4*3^(a-1), ord(5^b)=2*5^b, "
          "ord(p^c)=ord(p)*p^(c-1); 'ord = 4N/3' holds exactly on N = 3^a*5^b, a>=1",
    existence="a 2-dim invariant sector exists iff v_p(N) is even for every p >= 7 AND "
              "(v_3(N) odd or v_5(N) odd)",
    uniqueness="forced: 5^odd carries no invariant line, so at most one factor can supply "
               "the sector",
    phase="v_5(N) odd -> 36 deg if Legendre (N/5^v5 | 5) = +1 else 108 deg;  "
          "v_5(N) even -> 90 deg (twist-rigid, eigenvalue +-i)",
    trace="2cos(phase): phi at 36 deg, 1-phi at 108 deg, 0 at 90 deg",
    scope="atom table computed for 3^1..3^5, 5^1..5^3, 7^1..7^3, 11^1..11^2, 13^1..13^2; "
          "the exponent-parity rule beyond those exponents is conjectural, and no held-out "
          "prediction here relies on it")
R["invariant_to_phase"] = {str(k): v for k, v in inv_map.items()}

# ---- L1 non-vacuity: the gate must be able to FIRE and to FAIL on possible worlds ----
CF = []


def cf(name, **over):
    f = dict(FACTS)
    f.update(over)
    v, w = verdict(f)
    CF.append(dict(case=name, verdict=v, reason=w))
    say(f"  counterfactual [{name}] -> {v}  ({w})")


say("  L1 non-vacuity -- the verdict function on logically possible fact-vectors:")
cf("as computed")
cf("675 had come back with phase 36 (a value the object does realise elsewhere)",
   heldout_hits=ho_hit - 1)
cf("phases collide: two levels, same invariants, different phase",
   phase_is_function_of_invariants=False)
cf("no structural rule reproduces any phase", phase_hits=0, heldout_hits=0,
   existence_hits=ex_hit)
cf("only 2 levels carry a sector", sector_levels=2)
cf("the tensor identity had failed", tensor_exact=False)
R["stage8_counterfactuals"] = CF
fires = sorted({c["verdict"] for c in CF})
say(f"  branches reachable on possible worlds: {fires}")
R["branches_reachable"] = fires

say("")
say("=" * 78)
say(f"VERDICT: {V}")
say(f"REASON : {WHY}")
say("PHASE MAP (the answer to OI-133):")
say("  ord(W1) at level N = lcm over prime powers of  ord(3^a)=4*3^(a-1),")
say("    ord(5^b)=2*5^b, ord(p^c)=ord(p)*p^(c-1)  -- 'ord = 4N/3' is the 3-5 corner only.")
say("  A 2-dim invariant sector EXISTS  <=>  v_p(N) is EVEN for every prime p >= 7,")
say("    AND (v_3(N) is odd OR v_5(N) is odd).  It is then UNIQUE, because 5^odd carries")
say("    no invariant line -- uniqueness is forced, not observed luck.")
say("  Its PHASE is then completely determined:")
say("    v_5(N) odd  -> the 5-part supplies the sector: 36 deg (trace phi) if the")
say("                   Legendre symbol (N/5^v5 | 5) = +1, else 108 deg (trace 1-phi);")
say("    v_5(N) even -> the 3-part supplies it: 90 deg (trace 0), twist-rigid.")
say("  The 'pentagon pair' was the 5-atom's Galois orbit seen through a fixed 5-part;")
say("  rung 75 broke it because at 75 = 3*5^2 the SUPPLIER changes from the 5-part to")
say("  the 3-part.  The phase is NOT free.")
say(f"[{time.time()-T0:.0f}s total]")

with open(os.path.join(HERE, "results.json"), "w") as fh:
    json.dump(R, fh, separators=(",", ":"), sort_keys=False)
with open(os.path.join(HERE, "output.txt"), "w") as fh:
    fh.write("\n".join(LOG) + "\n")
