"""B1527 -- route W: the class index through the fibration, sharing no linear algebra with cusp_lib's Fox route.

For a word state Gamma = F x|_phi Z (F = <a, b> free, t x t^-1 = phi(x)), the Lyndon-Hochschild-Serre (Wang) sequence gives
    0 -> H^1(Z; V^F) -> H^1(Gamma; V) -> H^1(F; V)^t -> 0,
so h^1(Gamma; V) = dim ker((rho(t) - 1) on V^F) + dim ker(t* - 1 on H^1(F; V)), with t acting on cocycles of F by
(t^-1 . z)(g) = rho(t)^-1 z(phi(g)).  On Z^1(F; V) = V^2 (the values on a and b), ker(t* - 1 on H^1(F; V)) has dimension
dim ker K - d, where K(z, v) = t^-1.z - z - dv on V^2 + V and dv = ((rho(a) - 1)v, (rho(b) - 1)v).

The index then follows from LEMMA E (B1527 PREREGISTRATION section 3): for V flat on a one-cusped M with chi(M) = 0,
    I(V) = h^1(V*) - h^1(V) + 2 (a0 - b0) + s0 - t0,
with a0 = h^0(Gamma; V), b0 = h^0(Gamma; V*), t0 = h^0(Delta; V), s0 = h^0(Delta; V*), all computed here.
Ranks by singular values at the ambient mp.dps, with this module's own threshold and margins."""
import mpmath as mp

REL_TOL = mp.mpf(10) ** -30


class Rank:
    def __init__(self):
        self.kept, self.dropped = mp.mpf(1), mp.mpf(0)

    def __call__(self, A):
        if A.rows == 0 or A.cols == 0:
            return 0
        S = mp.svd_c(A, compute_uv=False)
        s = sorted([abs(S[i]) for i in range(min(A.rows, A.cols))], reverse=True)
        if s[0] == 0:
            return 0
        r = sum(1 for x in s if x > REL_TOL * s[0])
        if r > 0:
            self.kept = min(self.kept, s[r - 1] / s[0])
        if r < len(s):
            self.dropped = max(self.dropped, s[r] / s[0])
        return r


def _stack_rows(blocks):
    rows = sum(B.rows for B in blocks)
    cols = blocks[0].cols
    out = mp.matrix(rows, cols)
    r = 0
    for B in blocks:
        for i in range(B.rows):
            for j in range(cols):
                out[r + i, j] = B[i, j]
        r += B.rows
    return out


def _word(w, M, Mi):
    X = mp.eye(M["a"].rows)
    for c in w:
        X = X * (M[c] if c.islower() else Mi[c.lower()])
    return X


def _fox_F(w, M, Mi):
    """left Fox derivatives of a word in a, b (cocycle rule z(gh) = z(g) + g z(h)): dict x -> d x d matrix"""
    d = M["a"].rows
    D = {"a": mp.matrix(d, d), "b": mp.matrix(d, d)}
    P = mp.eye(d)
    for c in w:
        if c.islower():
            D[c] += P
            P = P * M[c]
        else:
            P = P * Mi[c.lower()]
            D[c.lower()] -= P
    return D


def _null_dim(A, rk):
    return A.cols - rk(A)


def h1_wang(img, M, rk):
    """h^1(Gamma; V) for the module with matrices M['a'], M['b'], M['t'] (generators of the bundle group)"""
    d = M["a"].rows
    Mi = {g: mp.inverse(M[g]) for g in "abt"}
    I = mp.eye(d)
    # V^F and rho(t) on it
    VF = _stack_rows([M["a"] - I, M["b"] - I])
    f = _null_dim(VF, rk)
    first = 0
    if f > 0:
        U, S, V = mp.svd_c(VF, full_matrices=True)
        r = d - f
        basis = mp.matrix(d, f)
        for k in range(f):
            for i in range(d):
                basis[i, k] = mp.conj(V[r + k, i])
        # (rho(t) - 1) restricted to V^F (t preserves V^F): its kernel dimension
        first = _null_dim((M["t"] - I) * basis, rk)
    # K(z, v) = t^-1.z - z - dv on V^2 + V
    Fa = _fox_F(img["a"], M, Mi)
    Fb = _fox_F(img["b"], M, Mi)
    Ti = Mi["t"]
    K = mp.matrix(2 * d, 3 * d)
    blocks = {(0, 0): Ti * Fa["a"] - I, (0, 1): Ti * Fa["b"], (1, 0): Ti * Fb["a"], (1, 1): Ti * Fb["b"] - I}
    for (bi, bj), Bk in blocks.items():
        for i in range(d):
            for j in range(d):
                K[bi * d + i, bj * d + j] = Bk[i, j]
    for i in range(d):
        for j in range(d):
            K[i, 2 * d + j] = -(M["a"] - I)[i, j]
            K[d + i, 2 * d + j] = -(M["b"] - I)[i, j]
    second = _null_dim(K, rk) - d
    return first + second


def invariants(mats, words, rk):
    """dim of the vectors fixed by every word's matrix"""
    d = mats["a"].rows
    Mi = {g: mp.inverse(mats[g]) for g in "abt"}
    I = mp.eye(d)
    return _null_dim(_stack_rows([_word(w, mats, Mi) - I for w in words]), rk)


def dual(mats):
    return {g: mp.inverse(mats[g]).T for g in mats}


def index_wang(img, cusp, mats):
    """route W's index and its data; mats: the module's matrices on a, b, t"""
    rk = Rank()
    Md = dual(mats)
    h1V, h1Vd = h1_wang(img, mats, rk), h1_wang(img, Md, rk)
    a0, b0 = invariants(mats, ["a", "b", "t"], rk), invariants(Md, ["a", "b", "t"], rk)
    t0, s0 = invariants(mats, list(cusp), rk), invariants(Md, list(cusp), rk)
    I = h1Vd - h1V + 2 * (a0 - b0) + s0 - t0
    return {"I": I, "h1(V)": h1V, "h1(V*)": h1Vd, "a0": a0, "b0": b0, "t0": t0, "s0": s0,
            "margins": {"smallest kept": mp.nstr(rk.kept, 3), "largest dropped": mp.nstr(rk.dropped, 3)}}
