"""B1510 library: formal deformations of a block-diagonal representation rho0 = A (+) 1 of a one-relator group, and main's
index over the field of formal Laurent series F((eps)).  Field-generic: FP (GF(p)) or FK (a sympy algebraic number field).

Conventions (the same as index_lib and B1509): a deformation is rho_eps(g) = (I + sum_k eps^k U_k(g)) rho0(g) for the generators;
U_1 is then a 1-cocycle in the left convention u(gh) = u(g) + Ad(rho0(g)) u(h).  The relator R(eps) = rho_eps(r) has R_0 = I, and at
order k, R_k = J(U_k) + P_k, with J the Fox coboundary in Ad rho0 and P_k a polynomial in U_1 .. U_{k-1}.  H^2 = coker J."""


# ------------------------------------------------------------------ fields
class FP:
    def __init__(self, p):
        self.p, self.zero, self.one = p, 0, 1

    def add(self, a, b): return (a + b) % self.p
    def sub(self, a, b): return (a - b) % self.p
    def mul(self, a, b): return (a * b) % self.p
    def neg(self, a): return (-a) % self.p
    def inv(self, a):
        assert a % self.p, "inverse of zero"
        return pow(a % self.p, self.p - 2, self.p)
    def iszero(self, a): return a % self.p == 0
    def of(self, n): return n % self.p
    def show(self, a): return int(a % self.p)


class FK:
    def __init__(self, K):
        self.K, self.zero, self.one = K, K.zero, K.one

    def add(self, a, b): return a + b
    def sub(self, a, b): return a - b
    def mul(self, a, b): return a * b
    def neg(self, a): return -a
    def inv(self, a):
        assert a != self.K.zero, "inverse of zero"
        return self.K.quo(self.K.one, a)
    def iszero(self, a): return a == self.K.zero
    def of(self, n): return self.K.convert(n)
    def show(self, a): return str(self.K.to_sympy(a))


# ------------------------------------------------------------------ matrices (lists of lists)
def zeros(F, n, m): return [[F.zero] * m for _ in range(n)]
def eye(F, n): return [[F.one if i == j else F.zero for j in range(n)] for i in range(n)]


def mmul(F, A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = []
    for i in range(n):
        Ai = A[i]
        row = []
        for j in range(m):
            s = F.zero
            for l in range(k):
                a = Ai[l]
                if not F.iszero(a):
                    b = B[l][j]
                    if not F.iszero(b):
                        s = F.add(s, F.mul(a, b))
            row.append(s)
        out.append(row)
    return out


def madd(F, A, B): return [[F.add(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
def msub(F, A, B): return [[F.sub(x, y) for x, y in zip(r, s)] for r, s in zip(A, B)]
def mscale(F, c, A): return [[F.mul(c, x) for x in r] for r in A]
def mT(A): return [list(r) for r in zip(*A)]
def iszeromat(F, A): return all(F.iszero(x) for r in A for x in r)


def rref(F, A):
    R = [list(r) for r in A]
    piv, r = [], 0
    ncol = len(R[0]) if R else 0
    for c in range(ncol):
        if r >= len(R):
            break
        k = next((i for i in range(r, len(R)) if not F.iszero(R[i][c])), None)
        if k is None:
            continue
        R[r], R[k] = R[k], R[r]
        iv = F.inv(R[r][c])
        R[r] = [F.mul(x, iv) for x in R[r]]
        for i in range(len(R)):
            if i != r and not F.iszero(R[i][c]):
                f = R[i][c]
                R[i] = [F.sub(x, F.mul(f, y)) for x, y in zip(R[i], R[r])]
        piv.append(c)
        r += 1
    return R, piv


def rank(F, A):
    if not A or not A[0]:
        return 0
    return len(rref(F, A)[1])


def nullspace(F, A, ncols):
    """basis of {x : A x = 0}, as lists of length ncols"""
    if not A:
        return [[F.one if i == j else F.zero for j in range(ncols)] for i in range(ncols)]
    R, piv = rref(F, A)
    out = []
    for fc in [c for c in range(ncols) if c not in piv]:
        v = [F.zero] * ncols
        v[fc] = F.one
        for i, pc in enumerate(piv):
            v[pc] = F.neg(R[i][fc])
        out.append(v)
    return out


def solve(F, A, b):
    """one solution x of A x = b (free variables 0), or None if inconsistent"""
    n = len(A[0])
    R, piv = rref(F, [list(r) + [bb] for r, bb in zip(A, b)])
    if n in piv:
        return None
    x = [F.zero] * n
    for i, pc in enumerate(piv):
        x[pc] = R[i][n]
    return x


def inverse(F, A):
    n = len(A)
    R, piv = rref(F, [list(r) + e for r, e in zip(A, eye(F, n))])
    assert piv[:n] == list(range(n)), "singular"
    return [r[n:] for r in R]


# ------------------------------------------------------------------ series of matrices: lists S[0..N]
def smul(F, S, T, N):
    out = [zeros(F, len(S[0]), len(T[0][0])) for _ in range(N + 1)]
    for i in range(N + 1):
        if iszeromat(F, S[i]):
            continue
        for j in range(N + 1 - i):
            if iszeromat(F, T[j]):
                continue
            out[i + j] = madd(F, out[i + j], mmul(F, S[i], T[j]))
    return out


def sinv(F, S, N):
    """inverse of a series of square matrices with invertible constant term"""
    X0 = inverse(F, S[0])
    X = [X0]
    for k in range(1, N + 1):
        acc = zeros(F, len(S[0]), len(S[0]))
        for j in range(1, k + 1):
            if not iszeromat(F, S[j]):
                acc = madd(F, acc, mmul(F, S[j], X[k - j]))
        X.append(mscale(F, F.neg(F.one), mmul(F, X0, acc)))
    return X


class Family:
    """rho_eps on the generators from rho0 and corrections U[k][g] (k = 1..N); words evaluated as truncated series"""

    def __init__(self, F, rho0, U, N, gens=("m", "n")):
        self.F, self.N, self.gens = F, N, gens
        d = len(rho0[gens[0]])
        self.d = d
        self.X, self.Xi = {}, {}
        for g in gens:
            ser = [rho0[g]] + [mmul(F, U[k][g], rho0[g]) if k in U else zeros(F, d, d) for k in range(1, N + 1)]
            self.X[g] = ser
            self.Xi[g] = sinv(F, ser, N)

    def word(self, w):
        F, N, d = self.F, self.N, self.d
        S = [eye(F, d)] + [zeros(F, d, d) for _ in range(N)]
        for ch in w:
            S = smul(F, S, self.X[ch] if ch.islower() else self.Xi[ch.lower()], N)
        return S

    def fox(self, w):
        """Fox derivatives of w as series of d x d matrices (left convention)"""
        F, N, d = self.F, self.N, self.d
        D = {g: [zeros(F, d, d) for _ in range(N + 1)] for g in self.gens}
        pre = [eye(F, d)] + [zeros(F, d, d) for _ in range(N)]
        for ch in w:
            g = ch.lower()
            if ch.islower():
                D[g] = [madd(F, a, b) for a, b in zip(D[g], pre)]
                pre = smul(F, pre, self.X[g], N)
            else:
                pre = smul(F, pre, self.Xi[g], N)
                D[g] = [msub(F, a, b) for a, b in zip(D[g], pre)]
        return D


def line_eigenvalue(F, L, N, a):
    """the eigenvalue near 1 of a series of (a+1) x (a+1) matrices with L[0] = diag(L_AA, 1) and L_AA - 1 invertible;
    Schur complement fixed point lambda = L_55 + L_5A (lambda - L_AA)^-1 L_A5, as a list of N+1 scalars"""
    LAA = [[r[:a] for r in M[:a]] for M in L]
    LA5 = [[[r[a]] for r in M[:a]] for M in L]
    L5A = [[M[a][:a]] for M in L]
    L55 = [M[a][a] for M in L]
    lam = [F.one] + [F.zero] * N
    for _ in range(N + 1):
        Mser = [msub(F, mscale(F, lam[k], eye(F, a)), LAA[k]) for k in range(N + 1)]
        Minv = sinv(F, Mser, N)
        corr = smul(F, smul(F, L5A, Minv, N), LA5, N)
        lam = [F.add(L55[k], corr[k][0][0]) for k in range(N + 1)]
    return lam


def log_det(F, V, N, d):
    """tr log(I + V) for a series V with V[0] = 0, up to order N (needs 1..N invertible in F)"""
    out = [F.zero] * (N + 1)
    P = [zeros(F, d, d) for _ in range(N + 1)]
    P[0] = eye(F, d)
    for j in range(1, N + 1):
        P = smul(F, P, V, N)
        coef = F.inv(F.of(j))
        if j % 2 == 0:
            coef = F.neg(coef)
        for k in range(N + 1):
            tr = F.zero
            for i in range(d):
                tr = F.add(tr, P[k][i][i])
            out[k] = F.add(out[k], F.mul(coef, tr))
    return out


# ------------------------------------------------------------------ ranks over F((eps)) by valuation
def val(F, s, prec):
    for i in range(min(prec, len(s))):
        if not F.iszero(s[i]):
            return i
    return None


def laurent_rank(F, M, prec):
    """rank over F((eps)) of a matrix of truncated power series (lists of coefficients known to `prec` terms), by full pivoting on
    minimal valuation.  Returns (rank, pivot valuations, remaining precision).  Each pivot of valuation v costs v terms."""
    rows = [[(list(e) + [F.zero] * prec)[:prec] for e in r] for r in M]       # every entry as exactly `prec` coefficients
    rk, vals = 0, []
    while rows and rows[0]:
        best = None
        for i, r in enumerate(rows):
            for j, e in enumerate(r):
                v = val(F, e, prec)
                if v is not None and (best is None or v < best[0]):
                    best = (v, i, j)
        if best is None:
            break
        v, i, j = best
        piv = rows[i][j]
        unit = piv[v:prec] + [F.zero] * v
        newprec = prec - v
        # inverse of the unit series to newprec terms
        uinv = [F.inv(unit[0])]
        for k in range(1, newprec):
            acc = F.zero
            for t in range(1, k + 1):
                acc = F.add(acc, F.mul(unit[t], uinv[k - t]))
            uinv.append(F.neg(F.mul(uinv[0], acc)))
        prow = rows[i]
        newrows = []
        for r_i, r in enumerate(rows):
            if r_i == i:
                continue
            e = r[j]
            q = None
            if val(F, e, prec) is not None:
                sh = e[v:prec] + [F.zero] * v                       # e / eps^v, known to newprec terms
                q = [F.zero] * newprec
                for a in range(newprec):
                    if F.iszero(sh[a]):
                        continue
                    for b in range(newprec - a):
                        q[a + b] = F.add(q[a + b], F.mul(sh[a], uinv[b]))
            nr = []
            for c_i, x in enumerate(r):
                if c_i == j:
                    continue
                if q is None:
                    nr.append(x[:newprec])
                    continue
                y = prow[c_i]
                z = list(x[:newprec])
                for a in range(newprec):
                    if F.iszero(q[a]):
                        continue
                    for b in range(newprec - a):
                        z[a + b] = F.sub(z[a + b], F.mul(q[a], y[b]))
                nr.append(z)
            newrows.append(nr)
        rows = newrows
        prec = newprec
        rk += 1
        vals.append(v)
        if prec <= 0:
            return rk, vals, prec
    return rk, vals, prec


def series_matrix(F, S):
    """a series of matrices S[0..N] -> a matrix of coefficient lists"""
    n, m = len(S[0]), len(S[0][0])
    return [[[S[k][i][j] for k in range(len(S))] for j in range(m)] for i in range(n)]


def blocks(F, Ms, layout):
    """assemble a block matrix of coefficient-list entries; layout: list of rows of matrix names or ('zero', n, m)"""
    out = []
    for brow in layout:
        nrows = None
        parts = []
        for b in brow:
            if isinstance(b, tuple):
                parts.append(("z", b[1], b[2]))
                nrows = b[1] if nrows is None else nrows
            else:
                parts.append(("m", Ms[b]))
                nrows = len(Ms[b]) if nrows is None else nrows
        for i in range(nrows):
            row = []
            for kind, *rest in parts:
                if kind == "z":
                    row += [[F.zero] for _ in range(rest[1])]
                else:
                    row += rest[0][i]
            out.append(row)
    return out


def index_laurent(F, fam, word_r, word_mu, word_l, prec):
    """main's index of the family's representation W over F((eps)), from ranks only.  With d = dim V, two generators and one
    relator: n(V) = dim ker(H^1(M;V) -> H^1(T;V)) = 2d - rank(Big) - t0 + a0, Big = [[J, 0], [Res, -BT]], where J is the Fox
    coboundary, Res the restriction of 1-cochains to the peripheral words, BT the coboundary of 0-cochains on T."""
    out = {}
    for side in ("V", "V*"):
        fx = fam if side == "V" else _DualFamily(F, fam)
        d, N = fx.d, fx.N
        Id = [eye(F, d)] + [zeros(F, d, d) for _ in range(N)]
        D0 = series_matrix(F, [msub(F, fx.X["m"][k], Id[k]) + msub(F, fx.X["n"][k], Id[k]) for k in range(N + 1)])
        Dr = fx.fox(word_r)
        J = series_matrix(F, [[ra + rb for ra, rb in zip(Dr["m"][k], Dr["n"][k])] for k in range(N + 1)])
        Wmu, Wl = fx.word(word_mu), fx.word(word_l)
        BT = series_matrix(F, [msub(F, Wmu[k], Id[k]) + msub(F, Wl[k], Id[k]) for k in range(N + 1)])
        Res = _res_matrix(F, fx.fox(word_mu), fx.fox(word_l), d, N)
        negBT = [[[F.neg(x) for x in e] for e in r] for r in BT]
        Big = blocks(F, {"J": J, "Res": Res, "nBT": negBT}, [["J", ("zero", d, d)], ["Res", "nBT"]])
        rB, vB, pB = laurent_rank(F, Big, prec)
        rBT, vBT, pBT = laurent_rank(F, BT, prec)
        rD0, vD0, pD0 = laurent_rank(F, D0, prec)
        rJ, vJ, pJ = laurent_rank(F, J, prec)
        t0, a0 = d - rBT, d - rD0
        n = 2 * d - rB - t0 + a0
        a1 = (2 * d - rJ) - (d - a0)                                    # dim Z^1 - dim B^1
        out[side] = {"n": n, "a0": a0, "a1": a1, "t0": t0, "r1": a1 - n, "rank_Big": rB, "pivot_vals_Big": vB,
                     "prec_left": min(pB, pBT, pD0, pJ)}
    out["I"] = out["V"]["n"] - out["V*"]["n"]
    return out


def _res_matrix(F, Dmu, Dl, d, N):
    rows_k = []
    for k in range(N + 1):
        top = [Dmu["m"][k][i] + Dmu["n"][k][i] for i in range(d)]
        bot = [Dl["m"][k][i] + Dl["n"][k][i] for i in range(d)]
        rows_k.append(top + bot)
    return series_matrix(F, rows_k)


class _DualFamily:
    def __init__(self, F, fam):
        self.F, self.N, self.gens, self.d = F, fam.N, fam.gens, fam.d
        self.X = {g: [mT(M) for M in fam.Xi[g]] for g in fam.gens}       # rho(g)^-T
        self.Xi = {g: [mT(M) for M in fam.X[g]] for g in fam.gens}

    word = Family.word
    fox = Family.fox
