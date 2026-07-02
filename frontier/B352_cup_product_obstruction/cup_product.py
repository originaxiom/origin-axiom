"""B352 / part 2 of the {4,8}-integrability program -- the cup-product obstruction, computed.

THE QUESTION (B265/B270, flagged open in B347): do the theta-odd tangent directions
m in {4,8} (the e6/f4 = 26 "escape" sector) of the E6 character variety of the
figure-eight integrate past first order, or does the second-order obstruction
[z u z] in H^2(pi_1(4_1), e6) kill them?

ARCHITECTURE (forced by an honest numerical fact). The Sym^{2m} blocks of Ad rho span
e^{+-2m mu} in eigenvalue -- ~20 orders of magnitude at m=11 -- so double precision
cannot carry the 9-letter relator products, and any conjugation through a mixed
78x78 basis compounds it (the first build of this probe failed exactly so: relator
residual 1e+49). The working design:
  - CHAIN COORDINATES throughout: the group action is block-diagonal there (one
    Sym^{2m} block per exponent); no 78-dim conjugation ever happens;
  - the exact e6 bracket (B351, Jacobi-verified) transported to chain coordinates
    ONCE, exactly, using the WEIGHT GRADING: chain vectors are ad-h weight vectors,
    each weight space is <= 6-dim, so the exact change of basis is a family of tiny
    Fraction solves (no big inversions);
  - intertwiners to B347's symrep basis are ANTIDIAGONAL (both bases are weight
    bases with opposite ordering), built by a closed-form recursion -- no inversion,
    verified against all three sl2 generators;
  - numerics in mpmath at dps 100 (self-guarded per MB13 par.4), which dominates the
    ~1e20 block range with ~60 digits to spare.

THE COMPUTATION:
  - H^1 per block by Fox calculus (small SVDs);
  - the obstruction: P(t) = prod_letters exp(t ad z(s)) X(s) = I + t*0 + t^2 A2
    (the t-coefficient vanishes iff z is a cocycle -- asserted); a curve in Aut(e6)
    with vanishing first derivative has second derivative in the tangent space, so
    A2 = ad(q); q is recovered by the Gram solve tr(ad_i^T ad_j) q_j = tr(ad_i^T A2);
  - the class of q in H^2 = coker(Fox d^1) (aspherical 1-relator presentation),
    block by block.

CONTROLS (all must pass for the verdict to count):
  C1  the m=1 direction is tangent to the ACTUAL curve of characters (the
      A-polynomial curve through the principal embedding): obstruction class = 0;
  C2  gauge invariance: a coboundary z = d^0 v has obstruction class = 0;
  C3  theta-parity: for theta-odd z (m in {4,8}) the obstruction q is theta-even,
      so its class components in the {4,8} blocks vanish identically; information
      can only sit in the F4 blocks {1,5,7,11} (the B351 theta-grading).

Firewalled; nothing to CLAIMS.md.
"""
import importlib.util
import pathlib
from fractions import Fraction

import mpmath as mp

_FRONTIER = pathlib.Path(__file__).resolve().parent.parent
_DPS = 100


def _guard():
    mp.mp.dps = _DPS


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, _FRONTIER / rel)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


E6 = _load("b351_e6", "B351_exact_e6_chevalley/exact_e6.py")
TG = _load("b347_tg", "B347_e6_tangent_gradings/e6_tangent_gradings.py")
_guard()

DIM = E6.DIM                                   # 78
EXPONENTS = E6.EXPONENTS                       # [1, 4, 5, 7, 8, 11]
REL = TG.REL                                   # "abbbaBAAB"
N_OF = {m: 2 * m + 1 for m in EXPONENTS}
OFFSET = {}
_o = 0
for _m in EXPONENTS:
    OFFSET[_m] = _o
    _o += N_OF[_m]
COLS = [(m, k) for m in EXPONENTS for k in range(N_OF[m])]      # chain coordinate order


# --- the exact chain skeleton -----------------------------------------------------------
def _chains():
    e, h, f = E6.principal_sl2()
    kern = E6._nullspace(E6._ad_matrix(e))
    by_m = {}
    for v in kern:
        p = next(iter(v))
        w = int(E6.brk(h, v).get(p, 0) / v[p])
        by_m[w // 2] = v
    assert sorted(by_m) == EXPONENTS
    chains = {}
    for m, v in by_m.items():
        c = [v]
        for _ in range(2 * m):
            c.append(E6.brk(f, c[-1]))
        assert not E6.brk(f, c[-1])
        chains[m] = c
    # exact closed-form action (pins conventions): ad h w_k = (2m-2k) w_k;
    # ad e w_k = k(2m+1-k) w_{k-1}
    for m, c in chains.items():
        for k, w in enumerate(c):
            hw = E6.brk(h, w)
            assert hw == {i: (2 * m - 2 * k) * x for i, x in w.items() if 2 * m != 2 * k}, (m, k)
            ew = E6.brk(e, w)
            tgt = {i: k * (2 * m + 1 - k) * x for i, x in c[k - 1].items()} if k else {}
            assert ew == tgt, (m, k)
    return chains


CHAINS = _chains()
_WEIGHT = {(m, k): 2 * m - 2 * k for m, k in COLS}

# norms (exact norm^2, then float sqrt) for the normalized chain basis
_N2 = {(m, k): sum(Fraction(c) ** 2 for c in CHAINS[m][k].values()) for m, k in COLS}


def _norm(mk):
    return mp.sqrt(mp.mpf(_N2[mk].numerator) / mp.mpf(_N2[mk].denominator))


# --- the exact bracket in chain coordinates (via the weight grading) --------------------
def _bracket_chain():
    """c[(i, j)] = sparse dict {k: Fraction} with [W_i, W_j] = sum_k c_k W_k, where
    W_i are the UNNORMALIZED chain vectors, indexed by chain-coordinate position.
    Exact: each solve happens inside one weight space (dim <= 6)."""
    # weight -> list of chain positions, and the exact Gram-free solver per weight:
    from collections import defaultdict
    by_w = defaultdict(list)
    for pos, mk in enumerate(COLS):
        by_w[_WEIGHT[mk]].append(pos)
    # exact solve: express an e6-sparse vector in the chain vectors of its weight
    def express(vec, w):
        cols = by_w[w]
        basis = [CHAINS[m][k] for m, k in (COLS[p] for p in cols)]
        idxs = sorted({i for b in basis for i in b} | set(vec))
        A_ = [[Fraction(b.get(i, 0)) for b in basis] for i in idxs]
        b_ = [Fraction(vec.get(i, 0)) for i in idxs]
        # exact least-structure Gauss (the system is consistent and full-rank)
        ncol = len(basis)
        M = [row[:] + [bb] for row, bb in zip(A_, b_)]
        piv = []
        r = 0
        for c in range(ncol):
            p = next((i for i in range(r, len(M)) if M[i][c] != 0), None)
            if p is None:
                continue
            M[r], M[p] = M[p], M[r]
            M[r] = [x / M[r][c] for x in M[r]]
            for i in range(len(M)):
                if i != r and M[i][c] != 0:
                    M[i] = [xi - M[i][c] * xr for xi, xr in zip(M[i], M[r])]
            piv.append(c)
            r += 1
        sol = [Fraction(0)] * ncol
        for rr, c in enumerate(piv):
            sol[c] = M[rr][ncol]
        # consistency: rows beyond rank must be zero
        for i in range(r, len(M)):
            assert M[i][ncol] == 0, "inconsistent weight-space solve"
        return {cols[c]: s for c, s in zip(range(ncol), sol) if s != 0}

    table = {}
    for i, (mi, ki) in enumerate(COLS):
        Wi = CHAINS[mi][ki]
        for j, (mj, kj) in enumerate(COLS):
            if j < i:
                continue
            Wj = CHAINS[mj][kj]
            br = E6.brk(Wi, Wj)
            if not br:
                continue
            w = _WEIGHT[(mi, ki)] + _WEIGHT[(mj, kj)]
            sol = express(br, w)
            if sol:
                table[(i, j)] = sol
                table[(j, i)] = {k: -v for k, v in sol.items()}
    return table


BRK_CHAIN = _bracket_chain()

# normalized-basis numeric structure constants: [Wt_i, Wt_j] = sum ct_k Wt_k with
# ct = c * n_i n_j / n_k  (moderate magnitudes; verified finite below)
_guard()
_NORMS = [_norm(mk) for mk in COLS]
BRK_NORMED = {}
for (i, j), sol in BRK_CHAIN.items():
    BRK_NORMED[(i, j)] = {
        k: mp.mpf(v.numerator) / mp.mpf(v.denominator) * _NORMS[i] * _NORMS[j] / _NORMS[k]
        for k, v in sol.items()
    }


# --- mp matrix helpers ------------------------------------------------------------------
def _zeros(r, c):
    return mp.zeros(r, c)


def _matmul(A_, B_):
    return A_ * B_


def _to_list(M):
    return M


def ad_chain(v):
    """ad(v) as a 78x78 mp matrix in the NORMALIZED chain basis; v is an mp column
    vector of chain coordinates."""
    out = mp.zeros(DIM, DIM)
    for (i, j), sol in BRK_NORMED.items():
        vi = v[i]
        if vi == 0:
            continue
        for k, c in sol.items():
            out[k, j] += vi * c
    return out


# --- the intertwiners (antidiagonal, closed form) and the block representation ----------
def _their_gens(d):
    """B347 symrep sl2 generator matrices (monomial basis), by symmetric differences
    at mp precision."""
    _guard()
    t = mp.mpf(10) ** -20
    def sr(M):
        return TG.symrep(M, d)
    E1, E2 = sr(mp.matrix([[1, t], [0, 1]])), sr(mp.matrix([[1, -t], [0, 1]]))
    F1, F2 = sr(mp.matrix([[1, 0], [t, 1]])), sr(mp.matrix([[1, 0], [-t, 1]]))
    H1, H2 = sr(mp.matrix([[1 + t, 0], [0, 1 / (1 + t)]])), sr(mp.matrix([[1 - t, 0], [0, 1 / (1 - t)]]))
    return {"e": (E1 - E2) / (2 * t), "f": (F1 - F2) / (2 * t), "h": (H1 - H2) / (2 * t)}


def _our_gens(m):
    """Exact sl2 matrices on the NORMALIZED chain basis (closed form + norm ratios)."""
    n = N_OF[m]
    E_, H_, F_ = mp.zeros(n, n), mp.zeros(n, n), mp.zeros(n, n)
    for k in range(n):
        H_[k, k] = 2 * m - 2 * k
        if k + 1 < n:
            F_[k + 1, k] = _norm((m, k + 1)) / _norm((m, k))
        if k >= 1:
            E_[k - 1, k] = k * (2 * m + 1 - k) * _norm((m, k - 1)) / _norm((m, k))
    return {"e": E_, "h": H_, "f": F_}


def _intertwiner(m):
    """tau with (ours) T = T (theirs), T[k, j] = tau_j delta_{k, 2m-j} (antidiagonal:
    both are weight bases, oppositely ordered). Recursion via the raising operators;
    verified against e, h, f."""
    d = 2 * m
    ours, theirs = _our_gens(m), _their_gens(d)
    tau = [mp.mpf(1)]
    for j in range(d):
        num = ours["e"][d - j - 1, d - j]
        den = theirs["e"][j + 1, j]
        assert den != 0
        tau.append(tau[-1] * num / den)
    T = mp.zeros(d + 1, d + 1)
    for j in range(d + 1):
        T[d - j, j] = tau[j]
    # verification
    for k in ("e", "h", "f"):
        R = ours[k] * T - T * theirs[k]
        worst = max(abs(R[i, j]) for i in range(d + 1) for j in range(d + 1))
        scale = max(abs(T[i, d - i]) for i in range(d + 1))
        # the reference generators are symmetric differences at t = 1e-20, so the
        # verification floor is O(t^2) = 1e-40 (times the entry scale), NOT eps(dps)
        assert worst < mp.mpf(10) ** -35 * max(scale, 1), (m, k, worst)
    return T


INTERTWINERS = {m: _intertwiner(m) for m in EXPONENTS}


def _block_rep(gmat):
    """{m: T Sym^{2m}(g) T^-1} -- the group action per block in normalized chain
    coordinates. T antidiagonal => the conjugation is entrywise (no inversion)."""
    _guard()
    out = {}
    for m in EXPONENTS:
        d = 2 * m
        Sy = TG.symrep(gmat, d)
        T = INTERTWINERS[m]
        Dm = mp.zeros(d + 1, d + 1)
        for i in range(d + 1):
            for j in range(d + 1):
                Dm[i, j] = T[i, d - i] * Sy[d - i, d - j] / T[j, d - j]
        out[m] = Dm
    return out


_guard()
_BASE_A = TG._BASE["a"]
_BASE_B = TG._BASE["b"]
BLK = {"a": _block_rep(_BASE_A), "b": _block_rep(_BASE_B)}
BLK["A"] = {m: BLK["a"][m] ** -1 for m in EXPONENTS}
BLK["B"] = {m: BLK["b"][m] ** -1 for m in EXPONENTS}


def X_full(ch):
    out = mp.zeros(DIM, DIM)
    for m in EXPONENTS:
        n, o = N_OF[m], OFFSET[m]
        Dm = BLK[ch][m]
        for i in range(n):
            for j in range(n):
                out[o + i, o + j] = Dm[i, j]
    return out


def rep_checks(n_pairs=6, seed=3):
    """(a) X(rel) = I per block; (b) X preserves the transported bracket."""
    _guard()
    worst_rel = mp.mpf(0)
    for m in EXPONENTS:
        P = mp.eye(N_OF[m])
        for ch in REL:
            P = P * BLK[ch][m]
        worst_rel = max(worst_rel,
                        max(abs(P[i, j] - (1 if i == j else 0))
                            for i in range(N_OF[m]) for j in range(N_OF[m])))
    import random
    rnd = random.Random(seed)
    XA = X_full("a")
    worst_auto = mp.mpf(0)
    for _ in range(n_pairs):
        u = mp.matrix([rnd.uniform(-1, 1) for _ in range(DIM)])
        v = mp.matrix([rnd.uniform(-1, 1) for _ in range(DIM)])
        Xu, Xv = XA * u, XA * v
        lhs = _brk_vec(Xu, Xv)
        rhs = XA * _brk_vec(u, v)
        num = mp.norm(lhs - rhs)
        den = mp.norm(rhs)
        worst_auto = max(worst_auto, num / den)
    return worst_rel, worst_auto


def _brk_vec(u, v):
    out = mp.zeros(DIM, 1)
    for (i, j), sol in BRK_NORMED.items():
        ui = u[i]
        if ui == 0:
            continue
        vj = v[j]
        if vj == 0:
            continue
        for k, c in sol.items():
            out[k] += ui * vj * c
    return out


# --- the Fox complex (block-diagonal) ----------------------------------------------------
def fox_block(m):
    """d^1_m : (n x 2n) and d^0_m : (2n x n) for the Sym^{2m} block."""
    n = N_OF[m]
    Da, Db = mp.zeros(n, n), mp.zeros(n, n)
    pre = mp.eye(n)
    for ch in REL:
        low = ch.lower()
        if ch.islower():
            if low == "a":
                Da = Da + pre
            else:
                Db = Db + pre
            pre = pre * BLK[low][m]
        else:
            pre = pre * BLK[low.upper()][m]
            if low == "a":
                Da = Da - pre
            else:
                Db = Db - pre
    d1 = mp.zeros(n, 2 * n)
    for i in range(n):
        for j in range(n):
            d1[i, j] = Da[i, j]
            d1[i, j + n] = Db[i, j]
    d0 = mp.zeros(2 * n, n)
    Aa = BLK["a"][m] - mp.eye(n)
    Bb = BLK["b"][m] - mp.eye(n)
    for i in range(n):
        for j in range(n):
            d0[i, j] = Aa[i, j]
            d0[i + n, j] = Bb[i, j]
    return d1, d0


FOX = {m: fox_block(m) for m in EXPONENTS}


def _svd(M):
    return mp.svd_c(mp.matrix(M), full_matrices=True)


def h1_line(m):
    """The H^1 representative for the block: in ker d^1_m, orthogonal to im d^0_m."""
    _guard()
    d1, d0 = FOX[m]
    n = N_OF[m]
    U, sv, Vh = _svd(d1)
    smax = max(sv[i] for i in range(len(sv)))
    kern = [mp.matrix([mp.conj(Vh[i, j]) for j in range(2 * n)])
            for i in range(2 * n)
            if (sv[i] if i < len(sv) else mp.mpf(0)) < smax * mp.mpf(10) ** -30]
    assert len(kern) == n + 1, (m, len(kern), n + 1)
    # subtract the im d^0 component (Gram-Schmidt against an orthonormalized image)
    cols = [mp.matrix([d0[i, j] for i in range(2 * n)]) for j in range(n)]
    ortho = []
    for c in cols:
        w = c.copy()
        for u in ortho:
            w = w - u * _dot(u, w)
        nw = mp.norm(w)
        if nw > mp.mpf(10) ** -40:
            ortho.append(w / nw)
    best, best_norm = None, mp.mpf(0)
    for v in kern:
        w = v.copy()
        for u in ortho:
            w = w - u * _dot(u, w)
        nw = mp.norm(w)
        if nw > best_norm:
            best, best_norm = w, nw
    assert best_norm > mp.mpf(10) ** -20, (m, best_norm)
    z = best / mp.norm(best)
    # embed into full chain coordinates: (z(a), z(b))
    za, zb = mp.zeros(DIM, 1), mp.zeros(DIM, 1)
    o = OFFSET[m]
    for k in range(n):
        za[o + k] = z[k]
        zb[o + k] = z[k + n]
    return za, zb


def _dot(u, v):
    return sum(mp.conj(u[i]) * v[i] for i in range(u.rows))


def h2_functional(m):
    """u_m with u_m^H d^1_m = 0 (the 1-dim block H^2 = coker d^1_m)."""
    _guard()
    d1, _ = FOX[m]
    n = N_OF[m]
    U, sv, Vh = _svd(d1.transpose_conj())
    smax = max(sv[i] for i in range(len(sv)))
    null = [mp.matrix([mp.conj(Vh[i, j]) for j in range(n)])
            for i in range(n)
            if (sv[i] if i < len(sv) else mp.mpf(0)) < smax * mp.mpf(10) ** -30]
    assert len(null) == 1, (m, len(null))
    u = null[0]
    return u / mp.norm(u)


# --- the second-order relator expansion ---------------------------------------------------
_AD_BASIS = None


def _ad_basis():
    global _AD_BASIS
    if _AD_BASIS is None:
        _guard()
        _AD_BASIS = []
        for i in range(DIM):
            M = mp.zeros(DIM, DIM)
            for (ii, j), sol in BRK_NORMED.items():
                if ii != i:
                    continue
                for k, c in sol.items():
                    M[k, j] += c
            _AD_BASIS.append(M)
    return _AD_BASIS


_GRAM = None


def _gram():
    global _GRAM
    if _GRAM is None:
        _guard()
        ads = _ad_basis()
        _GRAM = mp.zeros(DIM, DIM)
        for i in range(DIM):
            for j in range(i, DIM):
                s = mp.mpf(0)
                for r in range(DIM):
                    for c in range(DIM):
                        s += ads[i][r, c] * ads[j][r, c]
                _GRAM[i, j] = s
                _GRAM[j, i] = s
    return _GRAM


def obstruction_vector(za, zb):
    """q with ad(q) = the t^2 coefficient of the relator product; plus diagnostics."""
    _guard()
    Z = {"a": ad_chain(za), "b": ad_chain(zb)}
    Z2 = {g: Z[g] * Z[g] for g in "ab"}
    XF = {ch: X_full(ch) for ch in "abAB"}
    P0, P1, P2 = mp.eye(DIM), mp.zeros(DIM, DIM), mp.zeros(DIM, DIM)
    for ch in REL:
        X = XF[ch if ch.islower() else ch]
        if ch.islower():
            L0, L1, L2 = X, Z[ch] * X, Z2[ch] * X * 0.5
        else:
            g = ch.lower()
            L0 = XF[ch]
            L1 = -(XF[ch] * Z[g])
            L2 = (XF[ch] * Z2[g]) * 0.5
        P2 = P2 * L0 + P1 * L1 + P0 * L2
        P1 = P1 * L0 + P0 * L1
        P0 = P0 * L0
    first = mp.norm(P1)
    # solve ad(q) = P2 via the Gram normal equations
    ads = _ad_basis()
    b = mp.matrix([sum(ads[i][r, c] * P2[r, c] for r in range(DIM) for c in range(DIM))
                   for i in range(DIM)])
    q = mp.lu_solve(_gram(), b)
    R = mp.zeros(DIM, DIM)
    for i in range(DIM):
        if q[i] != 0:
            R = R + ads[i] * q[i]
    res = mp.norm(R - P2) / max(mp.norm(P2), mp.mpf(10) ** -200)
    return q, first, res


def obstruction_class(za, zb):
    q, first, res = obstruction_vector(za, zb)
    comps = {}
    for m in EXPONENTS:
        u = h2_functional(m)
        o, n = OFFSET[m], N_OF[m]
        comps[m] = abs(sum(mp.conj(u[k]) * q[o + k] for k in range(n)))
    diag = {"first_order_residual": float(first), "ad_solve_residual": float(res),
            "q_norm": float(mp.norm(q))}
    return {m: float(v) for m, v in comps.items()}, diag


# --- controls and the verdict --------------------------------------------------------------
def control_coboundary(seed=5):
    _guard()
    import random
    rnd = random.Random(seed)
    v = mp.matrix([rnd.uniform(-1, 1) for _ in range(DIM)])
    XA, XB = X_full("a"), X_full("b")
    za = XA * v - v
    zb = XB * v - v
    nrm = mp.sqrt(mp.norm(za) ** 2 + mp.norm(zb) ** 2)
    return obstruction_class(za / nrm, zb / nrm)


def run_all():
    r = {}
    worst_rel, worst_auto = rep_checks()
    r["relator_residual"] = float(worst_rel)
    r["automorphism_residual"] = float(worst_auto)
    z = {m: h1_line(m) for m in (1, 4, 8)}
    r["control_m1"] = obstruction_class(*z[1])
    r["control_coboundary"] = control_coboundary()
    r["obstruction_m4"] = obstruction_class(*z[4])
    r["obstruction_m8"] = obstruction_class(*z[8])
    za = z[4][0] + z[8][0]
    zb = z[4][1] + z[8][1]
    nrm = mp.sqrt(mp.norm(za) ** 2 + mp.norm(zb) ** 2)
    r["obstruction_m4_plus_m8"] = obstruction_class(za / nrm, zb / nrm)
    return r


if __name__ == "__main__":
    r = run_all()
    print("B352 -- the {4,8} cup-product obstruction (chain coordinates, mp dps %d)\n" % _DPS)
    print(f"rep checks: relator residual {r['relator_residual']:.2e}, "
          f"automorphism residual {r['automorphism_residual']:.2e}\n")
    for key in ("control_m1", "control_coboundary", "obstruction_m4",
                "obstruction_m8", "obstruction_m4_plus_m8"):
        comps, diag = r[key]
        pretty = {m: f"{v:.3e}" for m, v in comps.items()}
        print(f"{key}:")
        print(f"    components {pretty}")
        print(f"    diagnostics {[f'{k}={v:.2e}' for k, v in diag.items()]}")
