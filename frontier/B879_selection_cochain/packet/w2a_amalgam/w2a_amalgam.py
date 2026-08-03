#!/usr/bin/env python3
"""
W2a -- THE AMALGAM / MAYER-VIETORIS QUANTUM COCHAIN (seat cc3, 2026-07-17)

Sealed wave-2 cell per DESIGN_DA.md + PREREG_DC.md section W2a. Builds the
Mayer-Vietoris/amalgam quantum cochain for the "double" D of the figure-eight
mapping torus, on the SU(3)_k stage, at k = 2 (kappa=5, the golden stage) and
the secondary levels k = 1,3,4 (kappa = 4,6,7).

READ-ONLY inputs (never modified):
  - /Users/dri/oa-seat-cc3/origin-axiom/frontier/B238_su32_levelrank/su32_wrt.py
    (banked, test-locked Kac-Peterson SU(3)_k / SU(2)_k modular data, float64)
  - /Users/dri/oa-seat-cc3/seat-work/derivation_campaign/w0d_quantum_scout/quantum_probe.py
    (scout's float64 probe of the bare weld operator; its output is REPRODUCED
    here, at kappa=5, in exact arithmetic, as CONTROL 1)
  - DESIGN_DA.md, PREREG_DC.md (section W2a), SCOUT.md (design + task text)

EXACT ARITHMETIC STATEMENT (per task's hard rule): all verdict-path numbers
(ranks, nullities, the h^0/h^1 counts, the sealed-falsifier comparison) are
computed via a from-scratch, self-contained EXACT CYCLOTOMIC FIELD
implementation over Q(zeta_N), using ONLY Python's `fractions.Fraction` for
coefficients in the power basis {1, zeta, ..., zeta^{deg-1}} (deg = phi(N)),
with reduction via the exact integer/rational cyclotomic polynomial Phi_N(x)
(computed here by exact polynomial division, not imported). NO sympy, NO
floats, anywhere in a verdict-path computation. (sympy 1.14.0 and numpy 2.4.0
ARE present in this venv but are used ONLY for the float64 cross-checks
explicitly marked "CONTROL (float64 cross-check, not verdict-path)" below --
i.e. to independently reproduce the banked su32_wrt.py's own numbers via its
own numpy machinery as an external sanity check on the exact construction,
never to compute a verdict number itself.)

Run: python3 -u w2a_amalgam.py   (writes w2a_results.json + prints this log,
which is captured verbatim to w2a_run.log by the caller).
"""
import itertools
import json
import math
import sys
import time
import importlib.util
from fractions import Fraction as Fr

T0 = time.time()


def log(*a):
    print(*a)
    sys.stdout.flush()


# ============================================================================
# PART 0: exact cyclotomic field Q(zeta_N), pure Python Fractions
# ============================================================================

def euler_phi(n):
    result = n
    nn = n
    p = 2
    while p * p <= nn:
        if nn % p == 0:
            while nn % p == 0:
                nn //= p
            result -= result // p
        p += 1
    if nn > 1:
        result -= result // nn
    return result


def divisors(n):
    divs = []
    i = 1
    while i * i <= n:
        if n % i == 0:
            divs.append(i)
            if i != n // i:
                divs.append(n // i)
        i += 1
    return sorted(divs)


def poly_strip(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def poly_add(a, b):
    n = max(len(a), len(b))
    a = a + [Fr(0)] * (n - len(a))
    b = b + [Fr(0)] * (n - len(b))
    return poly_strip([x + y for x, y in zip(a, b)])


def poly_sub(a, b):
    n = max(len(a), len(b))
    a = a + [Fr(0)] * (n - len(a))
    b = b + [Fr(0)] * (n - len(b))
    return poly_strip([x - y for x, y in zip(a, b)])


def poly_mul(a, b):
    if a == [Fr(0)] or b == [Fr(0)] or not a or not b:
        return [Fr(0)]
    res = [Fr(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        if ai == 0:
            continue
        for j, bj in enumerate(b):
            if bj == 0:
                continue
            res[i + j] += ai * bj
    return poly_strip(res)


def poly_divmod(a, b):
    a = poly_strip(a)
    b = poly_strip(b)
    if b == [Fr(0)]:
        raise ZeroDivisionError
    db = len(b) - 1
    lead_b = b[-1]
    q = [Fr(0)] * max(1, len(a) - db)
    r = a[:]
    while True:
        r = poly_strip(r)
        dr = len(r) - 1
        if r == [Fr(0)] or dr < db:
            break
        coef = r[-1] / lead_b
        shift = dr - db
        if shift >= len(q):
            q += [Fr(0)] * (shift + 1 - len(q))
        q[shift] += coef
        sub = [Fr(0)] * shift + [coef * bi for bi in b]
        r = poly_sub(r, sub)
    return poly_strip(q), poly_strip(r)


def poly_egcd(a, b):
    old_r, r = poly_strip(a), poly_strip(b)
    old_s, s = [Fr(1)], [Fr(0)]
    old_t, t = [Fr(0)], [Fr(1)]
    while poly_strip(r) != [Fr(0)]:
        q, rem = poly_divmod(old_r, r)
        old_r, r = r, rem
        old_s, s = s, poly_sub(old_s, poly_mul(q, s))
        old_t, t = t, poly_sub(old_t, poly_mul(q, t))
    return poly_strip(old_r), poly_strip(old_s), poly_strip(old_t)


_CYCLOTOMIC_CACHE = {}


def cyclotomic_poly(n):
    """Phi_n(x), monic, exact rational coefficients (computed by exact
    polynomial division of x^n-1 by the Phi_d, d|n, d<n -- NOT looked up from
    a table, NOT from sympy)."""
    if n in _CYCLOTOMIC_CACHE:
        return _CYCLOTOMIC_CACHE[n]
    numer = [Fr(-1)] + [Fr(0)] * (n - 1) + [Fr(1)]
    for d in divisors(n):
        if d < n:
            dp = cyclotomic_poly(d)
            numer, rem = poly_divmod(numer, dp)
            assert poly_strip(rem) == [Fr(0)], (n, d, rem)
    _CYCLOTOMIC_CACHE[n] = numer
    return numer


class CycField:
    """Q(zeta_N) represented in the power basis {1,...,zeta^{deg-1}},
    deg = phi(N). Elements are length-deg tuples of Fraction."""

    def __init__(self, N):
        self.N = N
        self.deg = euler_phi(N)
        phi = cyclotomic_poly(N)
        assert len(phi) == self.deg + 1 and phi[-1] == 1
        self.phi = phi
        self.v0 = [-phi[i] for i in range(self.deg)]
        self._pow_cache = {}

    def reduce(self, coeffs):
        coeffs = list(coeffs)
        deg = self.deg
        v0 = self.v0
        for k in range(len(coeffs) - 1, deg - 1, -1):
            c = coeffs[k]
            if c == 0:
                continue
            coeffs[k] = Fr(0)
            shift = k - deg
            for i in range(deg):
                coeffs[shift + i] += c * v0[i]
        out = coeffs[:deg]
        if len(out) < deg:
            out += [Fr(0)] * (deg - len(out))
        return tuple(out)

    def zero(self):
        return tuple(Fr(0) for _ in range(self.deg))

    def one(self):
        v = [Fr(0)] * self.deg
        v[0] = Fr(1)
        return tuple(v)

    def from_rational(self, r):
        v = [Fr(0)] * self.deg
        v[0] = Fr(r)
        return tuple(v)

    def zeta_power(self, k):
        k = k % self.N
        c = self._pow_cache.get(k)
        if c is not None:
            return c
        coeffs = [Fr(0)] * (k + 1)
        coeffs[k] = Fr(1)
        res = self.reduce(coeffs)
        self._pow_cache[k] = res
        return res

    def add(self, a, b):
        return tuple(x + y for x, y in zip(a, b))

    def sub(self, a, b):
        return tuple(x - y for x, y in zip(a, b))

    def neg(self, a):
        return tuple(-x for x in a)

    def scal(self, s, a):
        s = Fr(s)
        return tuple(s * x for x in a)

    def mul(self, a, b):
        raw = poly_mul(list(a), list(b))
        return self.reduce(raw)

    def is_zero(self, a):
        return all(x == 0 for x in a)

    def eq(self, a, b):
        return all(x == y for x, y in zip(a, b))

    def conj(self, a):
        res = [Fr(0)] * self.deg
        for i, ai in enumerate(a):
            if ai == 0:
                continue
            zp = self.zeta_power(-i)
            for t in range(self.deg):
                res[t] += ai * zp[t]
        return tuple(res)

    def inv(self, a):
        g, s, t = poly_egcd(list(a), self.phi)
        assert len(g) == 1 and g[0] != 0, ("element not invertible", g)
        c = g[0]
        s = [x / c for x in s]
        return self.reduce(s)

    def is_rational(self, a):
        return all(x == 0 for x in a[1:])

    def as_rational(self, a):
        assert self.is_rational(a)
        return a[0]

    def to_complex(self, a):
        import cmath
        z = cmath.exp(2j * cmath.pi / self.N)
        val = 0j
        for i, ai in enumerate(a):
            if ai != 0:
                val += float(ai) * (z ** i)
        return val

    def embed_from(self, other, a):
        assert self.N % other.N == 0
        ratio = self.N // other.N
        res = [Fr(0)] * self.deg
        for i, ai in enumerate(a):
            if ai == 0:
                continue
            zp = self.zeta_power(i * ratio)
            for t in range(self.deg):
                res[t] += ai * zp[t]
        return tuple(res)


# ---------- matrix helpers over a CycField ----------

def mat_mul(F, A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[F.zero() for _ in range(m)] for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for t in range(k):
            a = Ai[t]
            if F.is_zero(a):
                continue
            Bt = B[t]
            for j in range(m):
                if not F.is_zero(Bt[j]):
                    out[i][j] = F.add(out[i][j], F.mul(a, Bt[j]))
    return out


def mat_dagger(F, A):
    n, m = len(A), len(A[0])
    return [[F.conj(A[j][i]) for j in range(n)] for i in range(m)]


def mat_id(F, n):
    return [[F.one() if i == j else F.zero() for j in range(n)] for i in range(n)]


def mat_scal(F, s, A):
    return [[F.scal(s, x) for x in row] for row in A]


def mat_sub(F, A, B):
    return [[F.sub(A[i][j], B[i][j]) for j in range(len(A[0]))] for i in range(len(A))]


def diag_mat(F, d):
    n = len(d)
    return [[d[i] if i == j else F.zero() for j in range(n)] for i in range(n)]


def diag_inv(F, d):
    return [F.inv(x) for x in d]


def mat_eq(F, A, B):
    n, m = len(A), len(A[0])
    return all(F.eq(A[i][j], B[i][j]) for i in range(n) for j in range(m))


def copy_mat(M):
    return [row[:] for row in M]


def rank(F, M):
    """Exact rank via Gauss-Jordan elimination with exact field division."""
    A = copy_mat(M)
    nrows = len(A)
    ncols = len(A[0]) if nrows else 0
    r = 0
    for col in range(ncols):
        piv = None
        for row in range(r, nrows):
            if not F.is_zero(A[row][col]):
                piv = row
                break
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pivinv = F.inv(A[r][col])
        A[r] = [F.mul(pivinv, x) for x in A[r]]
        for row in range(nrows):
            if row != r and not F.is_zero(A[row][col]):
                factor = A[row][col]
                A[row] = [F.sub(A[row][c2], F.mul(factor, A[r][c2])) for c2 in range(ncols)]
        r += 1
        if r == nrows:
            break
    return r


def nullity(F, M):
    m = len(M[0])
    return m - rank(F, M)


def find_order(F, M, max_order=500):
    n = len(M)
    I = mat_id(F, n)
    cur = copy_mat(M)
    if mat_eq(F, cur, I):
        return 1
    for m in range(2, max_order + 1):
        cur = mat_mul(F, cur, M)
        if mat_eq(F, cur, I):
            return m
    return None


# ============================================================================
# PART 1: SU(3)_k exact modular data (Kac-Peterson, same convention as the
# banked frontier/B238_su32_levelrank/su32_wrt.py::su3_data, verbatim formula,
# translated from numpy float64 to exact Fraction/cyclotomic arithmetic)
# ============================================================================

def su3_weights(k):
    return [(a, b) for a in range(k + 1) for b in range(k + 1 - a)]


def su3_data_exact(k):
    """Returns (weights, F, S_raw, T):
      F      = CycField(6*(k+3)) -- the natural field (see FINDINGS_RAW.md
               denominator derivation: S_raw needs Q(zeta_{3*kappa}), T needs
               Q(zeta_{6*kappa}), so N=6*kappa covers both).
      S_raw  = the RAW (unnormalized) Kac-Peterson alternating sum; exact.
      T      = diagonal list of exact CycField elements.
    The true unitary S = S_raw / sqrt(K), K = (S_raw^dagger S_raw)[0,0] (a
    rational number, verified below) -- but W = T S^-1 T^-1 S never actually
    needs sqrt(K): S^-1 T^-1 S = S_raw^dagger T^-1 S_raw / K exactly (see
    derivation in FINDINGS_RAW.md), a purely rational rescaling. So sqrt is
    never invoked anywhere in this script.
    """
    kap = k + 3
    weights = su3_weights(k)
    n = len(weights)
    Nmod = 6 * kap
    F = CycField(Nmod)

    def Lvec(w):
        a, b = w
        return (a + b + 2, b + 1, 0)

    perms = list(itertools.permutations(range(3)))

    def sgn(p):
        s = 1
        for i in range(3):
            for j in range(i + 1, 3):
                if p[i] > p[j]:
                    s = -s
        return s

    S_raw = [[F.zero() for _ in range(n)] for _ in range(n)]
    for i, wl in enumerate(weights):
        Li = Lvec(wl)
        sumLi = sum(Li)
        for j, wm in enumerate(weights):
            Lj = Lvec(wm)
            sumLj = sum(Lj)
            acc = F.zero()
            for p in perms:
                Lip = (Li[p[0]], Li[p[1]], Li[p[2]])
                dot = Lip[0] * Lj[0] + Lip[1] * Lj[1] + Lip[2] * Lj[2]
                e = -(3 * dot - sumLi * sumLj)  # zeta_{3kap}^e ; embed as zeta_{6kap}^{2e}
                zp = F.zeta_power(2 * e)
                term = zp if sgn(p) > 0 else F.neg(zp)
                acc = F.add(acc, term)
            S_raw[i][j] = acc

    T = []
    for (a, b) in weights:
        num = 2 * (a * a + a * b + b * b) + 6 * (a + b) - 2 * k  # over denom 6*kap
        T.append(F.zeta_power(num))

    return weights, F, S_raw, T


def build_weld(F, S_raw, T):
    """W = R L, R = T, L = S^{-1} T^{-1} S, using the raw-S shortcut
    W = T . S_raw^dagger . T^{-1} . S_raw / K  (K = (S_raw^dagger S_raw)[0,0],
    rational -- verified by caller). Returns (W, K, gate_facts dict)."""
    n = len(T)
    Td = diag_mat(F, T)
    Tinv = diag_mat(F, diag_inv(F, T))
    Sd = mat_dagger(F, S_raw)
    prod = mat_mul(F, Sd, S_raw)
    # gate: prod must be K*I exactly, K rational
    offdiag_zero = all(F.is_zero(prod[i][j]) for i in range(n) for j in range(n) if i != j)
    diagvals = [prod[i][i] for i in range(n)]
    alldiag_equal = all(F.eq(diagvals[0], diagvals[i]) for i in range(n))
    K_is_rational = F.is_rational(diagvals[0])
    K = F.as_rational(diagvals[0]) if K_is_rational else None
    gate = dict(S_dagger_S_offdiag_zero=offdiag_zero,
                S_dagger_S_diag_equal=alldiag_equal,
                K_is_rational=K_is_rational, K=str(K) if K is not None else None)
    assert offdiag_zero and alldiag_equal and K_is_rational and K > 0, gate
    tmp = mat_mul(F, Sd, Tinv)
    tmp = mat_mul(F, tmp, S_raw)
    tmp = mat_mul(F, Td, tmp)
    W = [[F.scal(Fr(1, 1) / K, x) for x in row] for row in tmp]
    return W, K, gate


# ============================================================================
# PART 2: run per level
# ============================================================================

def eigen_breakdown(F, W, order, kappa_label):
    """Exact eigenvalue-order multiplicities of W: embed into Q(zeta_lcm(order,F.N))
    and compute nullity(W - zeta_order^j) for j=0..order-1."""
    n = len(W)
    Nbig = order * F.N // math.gcd(order, F.N)
    Fbig = CycField(Nbig)
    Wbig = [[Fbig.embed_from(F, W[i][j]) for j in range(n)] for i in range(n)]
    out = []
    total = 0
    for j in range(order):
        lam = Fbig.zeta_power(j * (Nbig // order))
        lamI = [[lam if i == kk else Fbig.zero() for kk in range(n)] for i in range(n)]
        nul = nullity(Fbig, mat_sub(Fbig, Wbig, lamI))
        if nul > 0:
            ordj = order // math.gcd(order, j)
            out.append(dict(j=j, order_of_root=ordj, multiplicity=nul))
            total += nul
    return out, total, Nbig


def float_crosscheck(k):
    """CONTROL (float64 cross-check, not verdict-path): reproduce trace(W) and
    nullity(W-I), nullity(T-I) via the banked su32_wrt.py's own numpy Kac-
    Peterson code, independently of our exact implementation."""
    PATH = "/Users/dri/oa-seat-cc3/origin-axiom/frontier/B238_su32_levelrank/su32_wrt.py"
    spec = importlib.util.spec_from_file_location("b238_su32", PATH)
    b238 = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(b238)
    import numpy as np
    w, S, T, c = b238.su3_data(k)
    n = S.shape[0]
    Si, Ti = np.linalg.inv(S), np.linalg.inv(T)
    Rr, Lr = T, Si @ Ti @ S
    Wf = Rr @ Lr
    trf = complex(np.trace(Wf))
    tol = 1e-8
    sN = np.linalg.svd(Wf - np.eye(n), compute_uv=False)
    nulf = int(np.sum(sN < tol))
    sT = np.linalg.svd(T - np.eye(n), compute_uv=False)
    nulTf = int(np.sum(sT < tol))
    uni_f = bool(np.allclose(Wf @ Wf.conj().T, np.eye(n), atol=1e-8))
    return dict(trace=trf, nullity_W_minus_I=nulf, nullity_T_minus_I=nulTf, W_unitary=uni_f)


def run_level(k):
    kappa = k + 3
    log(f"\n{'='*78}\nLEVEL k={k}  (kappa={kappa}, SU(3)_{k})\n{'='*78}")
    weights, F, S_raw, T = su3_data_exact(k)
    n = len(weights)
    log(f"  weights ({n}): {weights}   field N=Q(zeta_{F.N}), deg={F.deg}")

    W, K, gate = build_weld(F, S_raw, T)
    log(f"  S_raw-dagger.S_raw gate: {gate}")

    # trace cross-check
    trW = F.zero()
    for i in range(n):
        trW = F.add(trW, W[i][i])
    trW_c = F.to_complex(trW)
    log(f"  trace(W) exact (as complex eval) = {trW_c:.10f}")

    # CONTROL: W unitary exactly
    Wd = mat_dagger(F, W)
    WWd = mat_mul(F, W, Wd)
    I = mat_id(F, n)
    W_unitary_exact = mat_eq(F, WWd, I)
    log(f"  CONTROL W.Wdagger == I exactly: {W_unitary_exact}")

    # CONTROL: bare-stage nullity(W - I)  [h0(M) = h1(M)]
    WmI = mat_sub(F, W, I)
    nul_W = nullity(F, WmI)
    log(f"  CONTROL nullity(W-I) [bare h0=h1] = {nul_W}")

    # W' = W^{-1} = W^dagger (unitary); verify directly (not just invoked as a lemma)
    Wp = Wd  # = W^{-1} since W unitary and W W^dagger = I exactly (verified above)
    WpmI = mat_sub(F, Wp, I)
    nul_Wp = nullity(F, WpmI)
    log(f"  M' weld W' = W^-1 = W^dagger (unitary shortcut); nullity(W'-I) = {nul_Wp}"
        f"  (lemma: always == nullity(W-I) since ker(A-I)=ker(A^-1-I) always -> {nul_Wp == nul_W})")

    # boundary: T-based (c=1) and trivial-differential alternatives
    Td = diag_mat(F, T)
    TmI = mat_sub(F, Td, I)
    nul_T = nullity(F, TmI)
    log(f"  boundary (T^1 - I) nullity [h0(bd), primary choice] = {nul_T}")
    log(f"  boundary (trivial diff=0) [h0(bd) alt] = n = {n}")

    # order + eigenvalue breakdown. The fine per-eigenvalue multiplicity
    # breakdown (needed to reproduce the scout's specific "orders 20/10"
    # cross-check) is only REQUIRED at kappa=5; at other levels it requires
    # embedding into a much bigger cyclotomic field (lcm(order, 6*kappa)) and
    # is expensive (large deg => slow exact Gaussian elimination) without
    # being asked for by the task, so it is computed only at k=2 (kappa=5).
    order = find_order(F, W, max_order=400)
    log(f"  order(W) exact = {order}")
    eig_info = None
    if order is not None and k == 2:
        eb, total, Nbig = eigen_breakdown(F, W, order, kappa)
        log(f"  eigenvalue-order breakdown (exact, field Q(zeta_{Nbig})): {eb}  total_mult={total} (n={n})")
        eig_info = dict(breakdown=eb, total_mult=total, Nbig=Nbig)
    elif order is not None:
        log(f"  (fine per-eigenvalue breakdown skipped at this level -- not required by the task;"
            f" only order(W)={order} reported, which is enough for the h1(D) computation)")

    # float64 cross-check (control only, not verdict-path)
    fc = float_crosscheck(k)
    log(f"  CONTROL (float64, banked su32_wrt.py, cross-check only): {fc}")
    trace_match = abs(fc['trace'] - trW_c) < 1e-6
    nul_match = (fc['nullity_W_minus_I'] == nul_W) and (fc['nullity_T_minus_I'] == nul_T)
    log(f"  cross-check exact-vs-float MATCH: trace {trace_match}, nullities {nul_match}, "
        f"unitary {fc['W_unitary'] == W_unitary_exact}")

    # ---- amalgam assembly (documented modeling choice: connecting/restriction
    # maps of the Mayer-Vietoris sequence assumed ZERO -- see FINDINGS_RAW.md) ----
    h0_M, h1_M = nul_W, nul_W
    h0_Mp, h1_Mp = nul_Wp, nul_Wp
    h0_bd_T, h1_bd_T = nul_T, nul_T
    h0_bd_triv, h1_bd_triv = n, n

    h0_D = h0_M + h0_Mp
    h1_D_primary = h0_bd_T + h1_M + h1_Mp          # T-boundary (c=1), zero connecting maps
    h1_D_trivial = h0_bd_triv + h1_M + h1_Mp        # trivial-differential boundary
    h2_D_primary = h1_bd_T                          # (informational; not part of falsifier)
    h2_D_trivial = h1_bd_triv

    log(f"  ASSEMBLED (zero-connecting-map assumption): h0(D)={h0_D}")
    log(f"    primary (T-bd):   h1(D) = h0(bd)[{h0_bd_T}] + h1(M)[{h1_M}] + h1(M')[{h1_Mp}] = {h1_D_primary}"
        f"   (h2(D)={h2_D_primary})")
    log(f"    alt (trivial-bd): h1(D) = h0(bd)[{h0_bd_triv}] + h1(M)[{h1_M}] + h1(M')[{h1_Mp}] = {h1_D_trivial}"
        f"   (h2(D)={h2_D_trivial})")

    return dict(
        k=k, kappa=kappa, n=n, field_N=F.N, field_deg=F.deg,
        K_normalization=str(K),
        S_dagger_S_gate=gate,
        trace_W=str(trW_c),
        W_unitary_exact=W_unitary_exact,
        nullity_W_minus_I=nul_W,
        nullity_Winv_minus_I=nul_Wp,
        M_prime_lemma_holds=(nul_Wp == nul_W),
        nullity_T_minus_I=nul_T,
        order_W=order,
        eigen_breakdown=eig_info,
        float_crosscheck=dict(trace=str(fc['trace']), nullity_W_minus_I=fc['nullity_W_minus_I'],
                               nullity_T_minus_I=fc['nullity_T_minus_I'], W_unitary=fc['W_unitary']),
        crosscheck_match=dict(trace=trace_match, nullities=nul_match, unitary=(fc['W_unitary'] == W_unitary_exact)),
        h0_M=h0_M, h1_M=h1_M, h0_Mp=h0_Mp, h1_Mp=h1_Mp,
        h0_bd_T=h0_bd_T, h1_bd_T=h1_bd_T, h0_bd_triv=h0_bd_triv, h1_bd_triv=h1_bd_triv,
        h0_D=h0_D,
        h1_D_primary=h1_D_primary, h2_D_primary=h2_D_primary,
        h1_D_trivial=h1_D_trivial, h2_D_trivial=h2_D_trivial,
    )


def main():
    log("W2a AMALGAM/MAYER-VIETORIS QUANTUM COCHAIN -- seat cc3 -- " + time.strftime("%Y-%m-%d %H:%M:%S"))
    log("Exact arithmetic: pure Python `fractions.Fraction` over a zeta-power")
    log("basis of Q(zeta_N) (self-contained CycField class in this script,")
    log("Phi_N(x) computed by exact polynomial division). sympy/numpy used only")
    log("for explicitly-marked float64 cross-checks, never on the verdict path.")
    log("")
    log("CONTROLS block (kappa=5 first, as required, before the amalgam work):")

    results = {}
    order_levels = [2, 1, 3, 4]  # kappa=5 first (controls), then 4,6,7
    for k in order_levels:
        results[k] = run_level(k)

    # ---- sealed falsifier check ----
    log(f"\n{'='*78}\nSEALED FALSIFIER (kappa=5, i.e. k=2)\n{'='*78}")
    r5 = results[2]
    verdicts = {}
    for variant, h1val, split in [
        ("primary_T_boundary", r5['h1_D_primary'], (r5['h0_bd_T'], r5['h1_M'] + r5['h1_Mp'])),
        ("alt_trivial_boundary", r5['h1_D_trivial'], (r5['h0_bd_triv'], r5['h1_M'] + r5['h1_Mp'])),
    ]:
        bd_born, solo = split
        if h1val == 5 and bd_born == 2 and solo == 3:
            verdict = "STRUCTURAL MATCH"
        elif h1val == 5:
            verdict = "PARTIAL (h1=5, no clean 2+3 split)"
        else:
            verdict = "MISMATCH"
        verdicts[variant] = dict(h1_D=h1val, boundary_born=bd_born, solo=solo, verdict=verdict)
        log(f"  [{variant}] h1(D)={h1val}  split=({bd_born} boundary-born + {solo} solo)  => {verdict}")

    # structural parity fact: solo = h1(M)+h1(Mp) = 2*nul_W is ALWAYS EVEN
    log(f"\n  STRUCTURAL NOTE (all levels): h1(M')=h1(M) always exactly (ker(A-I)=ker(A^-1-I)"
        f" identically for any invertible A -- proven, not assumed), so the 'solo' component"
        f" 2*h1(M) is ALWAYS EVEN under this construction, for ANY choice of boundary")
    log(f"  differential or level. An odd solo count (e.g. the classical '3') is therefore"
        f" STRUCTURALLY UNREACHABLE by this specific amalgam model, independent of which"
        f" boundary convention or level is used -- a clean parity obstruction, reported honestly.")

    log(f"\n{'='*78}\nSECONDARY: h1(D) across levels (stage-selection probe)\n{'='*78}")
    for k in [1, 2, 3, 4]:
        r = results[k]
        log(f"  k={k} kappa={r['kappa']} n={r['n']}: h1(D)_primary(T-bd)={r['h1_D_primary']}"
            f"   h1(D)_alt(trivial-bd)={r['h1_D_trivial']}")
    primary_vals = [results[k]['h1_D_primary'] for k in [1, 2, 3, 4]]
    alt_vals = [results[k]['h1_D_trivial'] for k in [1, 2, 3, 4]]
    kappa5_singular_primary = (primary_vals[1] not in (primary_vals[0], primary_vals[2], primary_vals[3])) and \
        len(set(primary_vals)) > 1
    kappa5_singular_alt = (alt_vals[1] not in (alt_vals[0], alt_vals[2], alt_vals[3]))
    log(f"  primary(T-bd) values [k=1,2,3,4] = {primary_vals}  kappa=5 uniquely singular? {kappa5_singular_primary}")
    log(f"  alt(trivial-bd) values [k=1,2,3,4] = {alt_vals}  kappa=5 uniquely singular? {kappa5_singular_alt}")

    out = dict(
        meta=dict(cell="W2a", seat="cc3", date=time.strftime("%Y-%m-%d"),
                   arithmetic="exact cyclotomic (Python fractions.Fraction over Q(zeta_N) power basis)",
                   runtime_seconds=time.time() - T0),
        levels={str(k): results[k] for k in [1, 2, 3, 4]},
        sealed_falsifier_kappa5=verdicts,
        stage_selection_probe=dict(
            primary_T_boundary_by_level=dict(zip(["k=1", "k=2", "k=3", "k=4"], primary_vals)),
            alt_trivial_boundary_by_level=dict(zip(["k=1", "k=2", "k=3", "k=4"], alt_vals)),
            kappa5_singular_primary=kappa5_singular_primary,
            kappa5_singular_alt=kappa5_singular_alt,
        ),
        structural_parity_note=(
            "h1(M')=h1(M) exactly (ker(A-I)=ker(A^-1-I) identically), so the 'solo' "
            "component 2*h1(M) is always even; the classical odd solo count (3) is "
            "structurally unreachable by this amalgam model at any level or boundary choice."
        ),
    )

    outpath = "/Users/dri/oa-seat-cc3/seat-work/derivation_campaign/w2a_amalgam/w2a_results.json"
    with open(outpath, "w") as f:
        json.dump(out, f, indent=2, default=str)
    log(f"\nWrote {outpath}")
    log(f"\nTOTAL RUNTIME: {time.time()-T0:.2f}s")
    log("DONE.")


if __name__ == "__main__":
    main()
