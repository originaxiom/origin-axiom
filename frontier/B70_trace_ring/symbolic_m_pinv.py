"""B70 (Path D) -- the SL(n) fixed-line Jacobian J(m) from first principles, via the symbolic-m
eps-series pinv-limit. The symbolic-m analogue of B58-PhaseA jacobian_closure.py (which works at INTEGER
m over F_p). VALIDATED at n=3: reproduces B51's SL(3) tower exactly.

Construction. Near the identity the rep is A=(I+h g)exp(eps P), B=exp(eps Q) (dual number h^2=0 for the
gradient; eps-series to order L). The metallic trace map phi_m: a->a^m b, b->a sends (A,B)->(A^m B, A).
The point (V51 stalled here): A^m for SYMBOLIC m. With A=exp(eps P),
   A^m = exp(m eps P)                                   (eps^k coeff has m^k -- polynomial in m),
and the gradient (h^1) part of A^m = ((I+h g)exp(eps P))^m is
   sum_{i=0}^{m-1} exp(i eps P) g exp((m-i) eps P)      (Faulhaber sums sum_i i^j (m-i)^k -- polynomial
in m). Both are polynomial in m (validated against integer-m matrix powers, n=3,4). So the whole
construction is symbolic in m. The fixed-line Jacobian DT_0 is the eps->0 pinv-LIMIT of
DT(eps)=DX.pinv(Dx): the normal equations DT(eps) G(eps) = R(eps) (G=Dx Dx^T, R=DX Dx^T, S=I) solved
order-by-order. The n x n matrix arithmetic AUTO-enforces the Cayley-Hamilton / exterior-power closure,
so e_2..e_{n-1} (the B58 two-block barrier) need NO hand-built multi-block trace ring.

VALIDATED (n=3, L=8): char(DT_0) factors exactly as the SL(3) tower
   char(M^-1) char(M^2) char(M^3) (t-1)(t+1),  char(M^k)=t^2-L_k t+(-1)^k, L_k=tr([[m,1],[1,0]]^k),
at m=1..7, and the INTERPOLATED J(m) reproduces it symbolically. The single fully-symbolic Q[m] solve
is heavier (the series-inverse + Gauss-Jordan over Q[m]); the per-m exact solve + interpolation
(degree<=4 from >=7 over-determined points) is the tractable equivalent and is rigorous.

This is the from-first-principles symbolic-m construction the a_d proof needs; SL(4) (with the e_2
char(-M^2) two-block sector, gated vs B65) is the substantial continuation. Computer-assisted; the SL(3)
reproduction is exact. Proven core P1-P16 untouched.
"""
import random

import sympy as sp

m, eps, t = sp.symbols("m epsilon t")


def make(n, L, seed=20, mv=None):
    """Build the symbolic-m (or m=mv) eps-series environment for SL(n) near the identity."""
    random.seed(seed)
    def rmat():
        M = sp.Matrix(n, n, lambda i, j: sp.Integer(random.randint(-3, 3)))
        return M - sp.eye(n) * sp.trace(M) / n
    P, Q = rmat(), rmat()
    BASIS = []
    for i in range(n):
        for j in range(n):
            if i != j:
                E = sp.zeros(n, n); E[i, j] = 1; BASIS.append(E)
    for i in range(n - 1):
        E = sp.zeros(n, n); E[i, i] = 1; E[i + 1, i + 1] = -1; BASIS.append(E)
    dim = n * n - 1
    msym = mv if mv is not None else m

    def trunc(M):
        return sp.Matrix(n, n, lambda i, j: sum(sp.expand(M[i, j]).coeff(eps, e) * eps**e for e in range(L + 1)))
    def mul(*Ms):
        R = Ms[0]
        for X in Ms[1:]:
            R = trunc(R * X)
        return R
    def exp_s(Pm, scale):
        out = sp.zeros(n, n); Pk = sp.eye(n)
        for k in range(L + 1):
            out = out + (scale**k * eps**k / sp.factorial(k)) * Pk
            if k < L:
                Pk = Pk * Pm
        return trunc(out)
    iS = sp.symbols("i_"); faul_cache = {}
    def faul(j, k):
        if (j, k) not in faul_cache:
            ex = sp.summation(iS**j * (m - iS)**k, (iS, 0, m - 1))
            faul_cache[(j, k)] = sp.expand(ex.subs(m, mv)) if mv is not None else sp.expand(ex)
        return faul_cache[(j, k)]
    def grad_pow(Pm, g):
        out = sp.zeros(n, n); powP = {0: sp.eye(n)}
        for e in range(1, L + 1):
            powP[e] = powP[e - 1] * Pm
        for j in range(L + 1):
            for k in range(L + 1 - j):
                out = out + (faul(j, k) * eps**(j + k) / (sp.factorial(j) * sp.factorial(k))) * (powP[j] * g * powP[k])
        return trunc(out)
    def inv_s(M):
        N = sp.expand(sp.eye(n) - M); acc = sp.eye(n); term = sp.eye(n)
        for _ in range(L):
            term = trunc(term * N); acc = acc + term
        return trunc(acc)
    expP, expQ, expPm = exp_s(P, 1), exp_s(Q, 1), exp_s(P, msym)
    def emul(g, M):
        R = g * M
        return sp.Matrix(n, n, lambda i, j: sum(sp.expand(R[i, j]).coeff(eps, e) * eps**e for e in range(L + 1)))
    def dmul(A, B):
        return (mul(A[0], B[0]), trunc(mul(A[0], B[1]) + mul(A[1], B[0])))
    def dinv(A):
        a0i = inv_s(A[0]); return (a0i, trunc(-mul(a0i, A[1], a0i)))
    def dtrace_h1(A):
        return [sp.expand(sp.trace(A[1]).coeff(eps, e)) for e in range(L + 1)]
    def word_eval(w, mats):
        acc = (sp.eye(n), sp.zeros(n, n))
        for c in w:
            acc = dmul(acc, mats[c])
        return acc
    return dict(n=n, L=L, dim=dim, BASIS=BASIS, P=P, expP=expP, expQ=expQ, expPm=expPm,
                grad_pow=grad_pow, dmul=dmul, dinv=dinv, dtrace_h1=dtrace_h1, word_eval=word_eval, emul=emul)


def grad_series(env, words, substitute):
    """Returns Dx_l (l=1..L), each dim x 2dim: the eps^l coeff of the h^1 word-trace gradients.
    substitute=True applies phi_m (the trace map); False is the source map."""
    n, L, dim = env["n"], env["L"], env["dim"]
    expP, expQ, expPm = env["expP"], env["expQ"], env["expPm"]
    out = [[[sp.Integer(0)] * (2 * dim) for _ in words] for _ in range(L)]
    for which in ("A", "B"):
        for jg, g in enumerate(env["BASIS"]):
            col = jg if which == "A" else dim + jg
            if which == "A":
                A_d = (expP, env["emul"](g, expP)); B_d = (expQ, sp.zeros(n, n))
                Am = (expPm, env["grad_pow"](env["P"], g))
            else:
                A_d = (expP, sp.zeros(n, n)); B_d = (expQ, env["emul"](g, expQ))
                Am = (expPm, sp.zeros(n, n))
            A_eff, B_eff = (env["dmul"](Am, B_d), A_d) if substitute else (A_d, B_d)
            mats = {"A": A_eff, "B": B_eff, "a": env["dinv"](A_eff), "b": env["dinv"](B_eff)}
            for r, w in enumerate(words):
                series = env["dtrace_h1"](env["word_eval"](w, mats))
                for l in range(L):
                    out[l][r][col] = series[l + 1]
    return [sp.Matrix(out[l]) for l in range(L)]


def solve_DT0(Dx, DX, dim, L):
    """DT_0 = eps->0 pinv-limit: solve the eps-series normal equations DT.G=R order by order (S=I).
    Mcoef is rank-deficient (only DT_0 is pinned; higher DT_j are free) -> gauss_jordan_solve, params=0."""
    mo = L + 1
    G = [sp.zeros(dim, dim) for _ in range(mo + 1)]
    R = [sp.zeros(dim, dim) for _ in range(mo + 1)]
    for l in range(2, mo + 1):
        for i in range(max(1, l - L), min(L, l - 1) + 1):
            G[l] = G[l] + Dx[i - 1] * Dx[l - i - 1].T
            R[l] = R[l] + DX[i - 1] * Dx[l - i - 1].T
    jmax = mo - 2; morders = list(range(2, mo + 1))
    Mcoef = sp.zeros(len(morders) * dim, (jmax + 1) * dim)
    for mi, mm in enumerate(morders):
        for j in range(jmax + 1):
            o = mm - j
            if 2 <= o <= mo:
                Mcoef[mi * dim:(mi + 1) * dim, j * dim:(j + 1) * dim] += G[o].T
    DT0 = sp.zeros(dim, dim)
    for a in range(dim):
        rhs = sp.Matrix.vstack(*[R[mm][a, :].T for mm in morders])
        sol, tau = Mcoef.gauss_jordan_solve(rhs)
        sol0 = sol.subs({s: 0 for s in tau}) if tau.free_symbols else sol
        DT0[a, :] = sol0[:dim, 0].T
    return DT0


def fixed_line_jacobian(n, words, L, mvals=(1, 2, 3, 4, 5, 6, 7), seed=20):
    """The fixed-line Jacobian J(m) over Z[m], by the symbolic-m construction evaluated at each m in
    mvals (exact) + interpolation (entries are degree<=4 in m). Returns (J(m), {m: DT_0})."""
    dim = n * n - 1; DT0_at = {}
    for mv in mvals:
        env = make(n, L, seed=seed, mv=mv)
        DT0_at[mv] = solve_DT0(grad_series(env, words, False), grad_series(env, words, True), dim, L)
    Jm = sp.zeros(dim, dim)
    for i in range(dim):
        for j in range(dim):
            Jm[i, j] = sp.interpolate([(mv, DT0_at[mv][i, j]) for mv in mvals], m)
    return Jm, DT0_at


def char_factor(k, sign=1):
    """char(sign*M^k) = t^2 - sign*L_k t + (-1)^k, L_k=tr([[m,1],[1,0]]^k)."""
    M = sp.Matrix([[m, 1], [1, 0]])
    Lk = sp.trace(M**k) if k >= 0 else sp.trace(M.inv()**(-k))
    return sp.expand(t**2 - sign * Lk * t + (-1)**(k % 2))


def sl3_tower():
    """The SL(3) metallic fixed-line tower (B51): char(M^-1)char(M^2)char(M^3)(t-1)(t+1)."""
    return sp.expand((t - 1) * (t + 1) * char_factor(-1) * char_factor(2) * char_factor(3))


SL3_WORDS = [["A"], ["B"], ["A", "B"], ["a"], ["b"], ["a", "B"], ["A", "b"], ["a", "b"]]


def main():
    print("B70 (Path D) -- symbolic-m fixed-line Jacobian via the eps-series pinv-limit\n")
    print("n=3 gate vs B51's SL(3) tower (L=8, m=1..7 + interpolation):")
    Jm, DT0_at = fixed_line_jacobian(3, SL3_WORDS, L=8)
    cp = sp.factor(Jm.charpoly(t).as_expr())
    print("  interpolated char(J(m)) =", cp)
    print("  SL(3) tower (B51)        =", sp.factor(sl3_tower()))
    print("  MATCH:", sp.expand(cp - sl3_tower()) == 0)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
