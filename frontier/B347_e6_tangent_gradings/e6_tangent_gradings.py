"""B347 -- the E6 character-variety tangent of the figure-eight, and its two Z/2 gradings.

Standalone low-dimensional topology / SL(n,C)-character-variety computation. NO physics claim; nothing
promotes to CLAIMS.md. This is the *correct* replacement for a cross-session handoff's "E6 dictionary":
the tangent to the E6 character variety of the figure-eight (4_1) at the principal-SL2 x geometric rep.

Object.  rho0 : pi_1(4_1) -> SL(2,C) is the geometric (discrete faithful) holonomy. Compose with the
PRINCIPAL homomorphism SL(2) -> E6, whose exponents are the E6 exponents {1,4,5,7,8,11}; the E6 adjoint
decomposes under it as  e6 = (+)_i Sym^{2 m_i}  (dims 3+9+11+15+17+23 = 78). So the Zariski tangent
    H^1(pi_1(4_1), e6_rho)  =  (+)_i  H^1(4_1, Sym^{2 m_i}) ,
computed here by Fox calculus on the presentation <a,b | a b^3 a B A^2 B> (SnapPy census, verified).

Results (all reproduced by run_all()):
  1. dim H^1(4_1, Sym^{2m}) = 1 for every E6 exponent m  =>  total = 6 = rank E6.
     (the honest "6-dim moduli"; refutes the handoff's degenerate-cascade reading -- exponents contribute
      EQUALLY, one direction each.)
  2. AMPHICHIRAL (orientation-reversing) involution sigma_-: acts as a REAL structure J^2 = +1 on every
     line -- uniform, no split (amphichirality does not select among exponents).
  3. HYPERELLIPTIC (orientation-preserving) involution a->a^-1, b->b^-1: grades by (-1)^{m+1}. Its
     (-1)-eigenspace is exactly {4,8} = the e6/f4 = 26 coset ("escape", E6-Zariski-dense, B265); its
     (+1)-eigenspace is {1,5,7,11} = the F4 exponents. So the manifold's Z/2 realizes the E6 -> F4 split.

Pure mpmath (pyenv); the geometric rep is hard-coded over Q(sqrt3, i) and self-verified against the relator.
"""
import mpmath as mp

mp.mp.dps = 70
_s3 = mp.sqrt(3)
_I = mp.mpc(0, 1)
EXPONENTS = [1, 4, 5, 7, 8, 11]
REL = "abbbaBAAB"                       # SnapPy 4_1 relator (uppercase = inverse)

# --- the geometric SL(2,C) rep (discrete faithful holonomy of 4_1), entries in Q(sqrt3, i) -------------
_BASE = {
    "a": mp.matrix([[-2 - _s3 * _I, _s3 / 2 + 3 * _I / 2], [-_s3 + _I, mp.mpf(1)]]),
    "b": mp.matrix([[mp.mpf(0), _s3 / 2 + _I / 2], [-_s3 / 2 + _I / 2, mp.mpf(3) / 2 + _s3 * _I / 2]]),
}
_BASE["A"] = _BASE["a"] ** -1
_BASE["B"] = _BASE["b"] ** -1


def _ev(word, rep=_BASE):
    R = mp.eye(next(iter(rep.values())).rows)
    for c in word:
        R = R * rep[c]
    return R


def geometric_rep_residual():
    """||rho(relator) - I|| for the hard-coded rep (should be ~1e-60)."""
    return mp.norm(_ev(REL) - mp.eye(2))


# --- Sym^d of a 2x2 matrix (a genuine homomorphism SL2 -> SL(d+1)) ------------------------------------
def symrep(g, d):
    a, b, c, e = g[0, 0], g[0, 1], g[1, 0], g[1, 1]

    def cpow(p, k):
        r = [mp.mpf(1)]
        for _ in range(k):
            nr = [mp.mpf(0)] * (len(r) + 1)
            for j in range(len(r)):
                nr[j] += r[j] * p[0]
                nr[j + 1] += r[j] * p[1]
            r = nr
        return r

    Ms = mp.zeros(d + 1, d + 1)
    for i in range(d + 1):
        X = cpow([a, c], i)
        Y = cpow([b, e], d - i)
        conv = [mp.mpf(0)] * (d + 1)
        for u in range(len(X)):
            for v in range(len(Y)):
                conv[u + v] += X[u] * Y[v]
        for k in range(d + 1):
            Ms[k, i] = conv[d - k]                 # basis x^k y^{d-k}
    return Ms


def symrep_homomorphism_residual(d=6):
    return mp.norm(symrep(_BASE["a"] * _BASE["b"], d) - symrep(_BASE["a"], d) * symrep(_BASE["b"], d))


def _R(d):
    R = {c: symrep(_BASE[c], d) for c in "ab"}
    R["A"] = R["a"] ** -1
    R["B"] = R["b"] ** -1
    return R


def _foxmat(gen, d, R):
    dim = d + 1
    Dm = mp.zeros(dim, dim)
    pre = mp.eye(dim)
    for ch in REL:
        low = ch.lower()
        if ch.islower():
            if low == gen:
                Dm = Dm + pre
            pre = pre * R[low]
        else:
            pre = pre * R[low.upper()]
            if low == gen:
                Dm = Dm - pre
    return Dm


def _rank(M, tol=mp.mpf(10) ** -40):
    S = mp.svd_c(M, compute_uv=False)
    s = [abs(S[i]) for i in range(len(S))]
    return sum(1 for x in s if x > max(s) * tol)


def H1_dim(m):
    """dim H^1(4_1, Sym^{2m}) at the geometric rep, via ranks of the Fox cochain complex."""
    d = 2 * m
    dim = d + 1
    R = _R(d)
    Da, Db = _foxmat("a", d, R), _foxmat("b", d, R)
    d1 = mp.zeros(dim, 2 * dim)
    for i in range(dim):
        for j in range(dim):
            d1[i, j] = Da[i, j]
            d1[i, j + dim] = Db[i, j]
    d0 = mp.zeros(2 * dim, dim)
    Aa, Bb = R["a"] - mp.eye(dim), R["b"] - mp.eye(dim)
    for i in range(dim):
        for j in range(dim):
            d0[i, j] = Aa[i, j]
            d0[i + dim, j] = Bb[i, j]
    return (2 * dim - _rank(d1)) - _rank(d0)


def e6_tangent_total():
    return sum(H1_dim(m) for m in EXPONENTS)


# --- involution actions on the (1-dim) cohomology lines -----------------------------------------------
def _conjv(v):
    return mp.matrix([mp.conj(v[i]) for i in range(v.rows)])


def _zeval(word, za, zb, R):                       # value of a 1-cocycle on a word
    dim = za.rows
    z = mp.zeros(dim, 1)
    P = mp.eye(dim)
    zv = {"a": za, "b": zb}
    for c in word:
        zc = zv[c] if c in "ab" else -R[c] * zv[c.lower()]
        z = z + P * zc
        P = P * R[c]
    return z


def _nullspace(M, tol=mp.mpf(10) ** -35):
    U, S, V = mp.svd_c(M, full_matrices=True)
    sv = [abs(S[i]) for i in range(len(S))]
    sm = max(sv)
    return [mp.matrix([mp.conj(V[i, j]) for j in range(M.cols)])
            for i in range(M.cols) if (sv[i] if i < len(sv) else mp.mpf(0)) <= sm * tol]


def _solveD(target):
    """least-norm D (det=1) with rho(target[g]) = D * conj_flag(rho(g)) * D^-1 for g in a,b.
    target[g] is (word, conjugate_bool)."""
    rows = []
    for g in "ab":
        word, conj = target[g]
        L = _ev(word)
        Rr = mp.matrix([[mp.conj(_BASE[g][i, j]) for j in range(2)] for i in range(2)]) if conj else _BASE[g]
        blk = mp.zeros(4, 4)
        for i in range(2):
            for j in range(2):
                for k in range(2):
                    blk[i * 2 + j, k * 2 + j] += L[i, k]
                    blk[i * 2 + j, i * 2 + k] -= Rr[k, j]
        rows.append(blk)
    M = mp.zeros(8, 4)
    for r in range(8):
        for c in range(4):
            M[r, c] = rows[r // 4][r % 4, c]
    U, S, V = mp.svd_c(M, full_matrices=True)
    D = mp.matrix([[mp.conj(V[3, 0]), mp.conj(V[3, 1])], [mp.conj(V[3, 2]), mp.conj(V[3, 3])]])
    return D / mp.sqrt(mp.det(D))


# amphichiral involution sigma_-: a->ababAB, b->baBA  (rho.sigma = D conj(rho) D^-1); sigma^-1=(abABab,BAba)
_AMPHI = dict(sinv={"a": "abABab", "b": "BAba"},
              D=_solveD({"a": ("ababAB", True), "b": ("baBA", True)}), conjugate=True)
# hyperelliptic involution: a->a^-1, b->b^-1 (rho.sigma = D rho D^-1); sigma^-1 = itself
_HYPER = dict(sinv={"a": "A", "b": "B"},
              D=_solveD({"a": ("A", False), "b": ("B", False)}), conjugate=False)


def _line_eigenvalue(m, inv, square):
    """eigenvalue of the involution J (or J^2 if square) on the 1-dim H^1(Sym^{2m})."""
    d = 2 * m
    dim = d + 1
    R = _R(d)
    RD = symrep(inv["D"], d)
    conj = inv["conjugate"]
    sinv = inv["sinv"]
    Da, Db = _foxmat("a", d, R), _foxmat("b", d, R)
    d1 = mp.zeros(dim, 2 * dim)
    for i in range(dim):
        for j in range(dim):
            d1[i, j] = Da[i, j]
            d1[i, j + dim] = Db[i, j]
    d0 = mp.zeros(2 * dim, dim)
    Aa, Bb = R["a"] - mp.eye(dim), R["b"] - mp.eye(dim)
    for i in range(dim):
        for j in range(dim):
            d0[i, j] = Aa[i, j]
            d0[i + dim, j] = Bb[i, j]
    Z = _nullspace(d1)

    def dot(x, y):
        return sum(mp.conj(x[i]) * y[i] for i in range(x.rows))

    def gs(vs):
        o = []
        for v in vs:
            w = v.copy()
            for u in o:
                w = w - dot(u, w) * u
            n = mp.sqrt(dot(w, w).real)
            if n > mp.mpf(10) ** -25:
                o.append(w / n)
        return o

    Bon = gs([mp.matrix([d0[r, c] for r in range(2 * dim)]) for c in range(dim)])
    z0 = None
    for v in Z:
        w = v.copy()
        for u in Bon:
            w = w - dot(u, w) * u
        if mp.sqrt(dot(w, w).real) > mp.mpf(10) ** -18:
            z0 = w
            break

    def J(vec):
        za, zb = vec[0:dim, 0], vec[dim:2 * dim, 0]
        ea = RD * (_conjv(_zeval(sinv["a"], za, zb, R)) if conj else _zeval(sinv["a"], za, zb, R))
        eb = RD * (_conjv(_zeval(sinv["b"], za, zb, R)) if conj else _zeval(sinv["b"], za, zb, R))
        return mp.matrix([ea[i] for i in range(dim)] + [eb[i] for i in range(dim)])

    w = J(J(z0)) if square else J(z0)
    A = mp.zeros(2 * dim, 1 + dim)
    for r in range(2 * dim):
        A[r, 0] = z0[r]
        for c in range(dim):
            A[r, 1 + c] = d0[r, c]
    AH = mp.matrix(A.cols, A.rows)
    for r in range(A.rows):
        for c in range(A.cols):
            AH[c, r] = mp.conj(A[r, c])
    return mp.lu_solve(AH * A, AH * w)[0]


def amphichiral_indicator(m):
    """J^2 eigenvalue of the amphichiral (orientation-reversing) involution on H^1(Sym^{2m}); +1 = real."""
    mu = _line_eigenvalue(m, _AMPHI, square=True)
    assert abs(mu.imag) < mp.mpf(10) ** -6, mu
    return 1 if mu.real > 0 else -1


def hyperelliptic_sign(m):
    """+/-1 eigenvalue of the hyperelliptic involution (a->a^-1,b->b^-1) on H^1(Sym^{2m}); = (-1)^{m+1}."""
    lm = _line_eigenvalue(m, _HYPER, square=False)
    assert abs(lm.imag) < mp.mpf(10) ** -6, lm
    return 1 if lm.real > 0 else -1


def run_all():
    dims = {m: H1_dim(m) for m in EXPONENTS}
    amph = {m: amphichiral_indicator(m) for m in EXPONENTS}
    hyp = {m: hyperelliptic_sign(m) for m in EXPONENTS}
    return dict(dims=dims, total=sum(dims.values()), amphichiral=amph, hyperelliptic=hyp,
                minus_eigenspace=[m for m in EXPONENTS if hyp[m] < 0])


if __name__ == "__main__":
    print("geometric rep residual   :", mp.nstr(geometric_rep_residual(), 3))
    print("symrep homomorphism resid:", mp.nstr(symrep_homomorphism_residual(), 3))
    r = run_all()
    print("dim H^1(Sym^2m) per exponent:", r["dims"], " total =", r["total"], "(rank E6 = 6)")
    print("amphichiral J^2 (o-reversing):", r["amphichiral"], " -> uniform real structure")
    print("hyperelliptic sign (o-presv) :", r["hyperelliptic"])
    print("  (-1)-eigenspace =", r["minus_eigenspace"], "= e6/f4 coset {4,8} (B265 escape sector)")
