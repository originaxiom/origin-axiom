"""B1102 shared engine: e6 basis load, the 27-dim rep (crystal construction, ported from
B1100's twisted_double.py stage 0/1 pattern, re-executed against the SAME underlying
module those scripts pulled from: check_charge_bracket.py -- "the paper's e6"), plus
small linear-algebra utilities (ad-matrices, modular rank cross-check) reused by both
b1102_adapted_basis.py and b1102_solve.py.

Provenance note (recorded honestly in the runlog too): the CERT file the prereg names
(cloud_handoff/certificates/twisted_double.py) itself imports its e6 -- the module
check_charge_bracket.py ("ccb"), which lives on the paper-lineage branch's verify
directory -- via importlib.util.spec_from_file_location. That IS the actual root of
the bracket/basis convention B1098's and B1100's stored numbers live in (confirmed:
the stored A2 triple X=e_a0+e_a2, H=2h0+2h2, Y=-2e_-a0-2e_-a2 checks out exactly under
ccb.br). At the B1102 bank the module was VENDORED into this arc dir as
e6_bracket_vendored.py (provenance header carries the original's sha256), so the arc
is self-contained in-tree. This module loads the vendored copy by default (env
B1102_CCB_PATH overrides, for cross-bench comparison), then re-derives the 27
(crystal of omega_1, shift-cocycle action) following the SAME algorithm as
twisted_double.py's stage 1 -- written fresh here, not imported, and independently
re-verified against the Chevalley bracket below (our own certification, not
inherited trust).
"""
import importlib.util
import os
from fractions import Fraction as F
import sympy as sp

CCB_PATH = os.environ.get(
    "B1102_CCB_PATH",
    os.path.join(os.path.dirname(os.path.abspath(__file__)), "e6_bracket_vendored.py"),
)


def load_ccb():
    spec = importlib.util.spec_from_file_location("ccb", CCB_PATH)
    ccb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(ccb)
    return ccb


# ---------------------------------------------------------------- ad-matrices
def ad_matrix_sp(br, DIM, Z):
    """ad(Z) as an exact sympy Matrix: column i = br(Z, e_i)."""
    cols = []
    for i in range(DIM):
        e = [F(0)] * DIM
        e[i] = F(1)
        img = br(Z, e)
        cols.append([sp.Rational(c.numerator, c.denominator) for c in img])
    return sp.Matrix(cols).T


def to_sp_vec(v):
    return sp.Matrix([sp.Rational(c.numerator, c.denominator) if isinstance(c, F) else sp.Rational(c) for c in v])


def frac_vec(sp_col, n=None):
    n = n if n is not None else sp_col.shape[0]
    return [F(sp.Rational(sp_col[i]).p, sp.Rational(sp_col[i]).q) for i in range(n)]


# ---------------------------------------------------------------- the 27 (crystal build)
def build_27(ccb):
    """Crystal-of-omega_1 construction of the 27, faithfully following twisted_double.py's
    stage 1 pattern (shift-cocycle module action e_r.v_lam = eps(r,q_lam) v_{lam+r}),
    against ccb's br/evec/hvec/eps/ip/ROOTS/IDX/N/DIM. Returns (weights, WIDX, rho27_Q)."""
    br, evec, hvec = ccb.br, ccb.evec, ccb.hvec
    eps, ip, ROOTS, IDX, N, DIM = ccb.eps, ccb.ip, ccb.ROOTS, ccb.IDX, ccb.N, ccb.DIM

    simple = [tuple(1 if k == i else 0 for k in range(N)) for i in range(N)]
    Msys = sp.Matrix(N, N, lambda i, j: ip(simple[i], simple[j]))
    rhs = sp.Matrix([1] + [0] * (N - 1))
    w1 = Msys.solve(rhs)
    omega1 = tuple(sp.Rational(w1[k]) for k in range(N))

    def tadd(a, b):
        return tuple(x + y for x, y in zip(a, b))

    def tsub(a, b):
        return tuple(x - y for x, y in zip(a, b))

    def ipr(a, b):
        return sum(a[i] * b[j] * Msys[i, j] for i in range(N) for j in range(N))

    weights = [omega1]
    seen = {omega1}
    queue = [omega1]
    while queue:
        lam = queue.pop()
        for al in simple:
            if ipr(lam, al) == 1:
                mu = tsub(lam, al)
                if mu not in seen:
                    seen.add(mu)
                    weights.append(mu)
                    queue.append(mu)
    assert len(weights) == 27, f"expected 27 weights, got {len(weights)}"
    WIDX = {w: i for i, w in enumerate(weights)}
    qlat = {w: tuple(int(x) for x in tsub(w, omega1)) for w in weights}
    for w in weights:
        assert all(sp.Rational(a) == int(a) for a in tsub(w, omega1)), "non-integral shift"

    def act_root(r):
        out = {}
        for w in weights:
            tgt = tadd(w, r)
            if tgt in WIDX:
                out[WIDX[w]] = (WIDX[tgt], F(eps(r, qlat[w])))
        return out

    ROOTACT = {r: act_root(r) for r in ROOTS}

    CJ = []
    for j in range(N):
        vals = sp.Matrix([[br(hvec(j), evec(al))[N + IDX[al]] for al in simple]])
        CJ.append([sp.Rational(vals[0, k]) for k in range(N)])

    def cartan_eig(j, lam):
        return sum(sp.Rational(CJ[j][k]) * sp.Rational(lam[k]) for k in range(N))

    def rho27_Q(vec):
        Mq = [[F(0)] * 27 for _ in range(27)]
        for j in range(N):
            if vec[j]:
                for w in weights:
                    ev = cartan_eig(j, w)
                    if ev:
                        i2 = WIDX[w]
                        Mq[i2][i2] += vec[j] * F(sp.Rational(ev).p, sp.Rational(ev).q)
        for r in ROOTS:
            c = vec[N + IDX[r]]
            if c:
                for col, (row, s) in ROOTACT[r].items():
                    Mq[row][col] += c * s
        return Mq

    return weights, WIDX, rho27_Q


def verify_27_is_a_rep(ccb, rho27_Q, sample_pairs=None, full=True):
    """rho27_Q([u,v]) == [rho27_Q(u), rho27_Q(v)] -- our OWN certification (not inherited).
    full=True checks all C(78,2) Chevalley-basis pairs exactly (matches twisted_double's
    own stage-1 verification scope)."""
    br, evec, hvec, N, DIM = ccb.br, ccb.evec, ccb.hvec, ccb.N, ccb.DIM
    basis_ad = [[F(1) if k == j else F(0) for k in range(DIM)] for j in range(N)]
    for r in ccb.ROOTS:
        basis_ad.append(evec(r))
    import itertools
    pairs = list(itertools.combinations(range(len(basis_ad)), 2)) if full else sample_pairs

    def matQ_mul(A, B):
        n = len(A)
        C = [[F(0)] * n for _ in range(n)]
        for i in range(n):
            for t in range(n):
                a = A[i][t]
                if a:
                    Bt = B[t]
                    Ci = C[i]
                    for j in range(n):
                        if Bt[j]:
                            Ci[j] += a * Bt[j]
        return C

    RHO = [rho27_Q(v) for v in basis_ad]
    fails = 0
    for (i2, j2) in pairs:
        lhs = rho27_Q(br(basis_ad[i2], basis_ad[j2]))
        L = matQ_mul(RHO[i2], RHO[j2])
        Rm = matQ_mul(RHO[j2], RHO[i2])
        rhs = [[L[i][j] - Rm[i][j] for j in range(27)] for i in range(27)]
        if lhs != rhs:
            fails += 1
    return fails == 0, len(pairs), fails


# ---------------------------------------------------------------- modular rank cross-check
def modular_rank(rows, ncols, p):
    """Exact-integer/Fraction matrix (list of rows of Fraction/int/sp.Rational), rank mod p
    via Gaussian elimination in GF(p). rows entries must be Fraction or int or sp.Rational."""
    def to_mod(x):
        if isinstance(x, F):
            num, den = x.numerator % p, x.denominator % p
        else:
            r = sp.Rational(x)
            num, den = int(r.p) % p, int(r.q) % p
        return (num * pow(den, p - 2, p)) % p

    M = [[to_mod(x) for x in row] for row in rows]
    nrows = len(M)
    r = 0
    for c in range(ncols):
        piv = None
        for i in range(r, nrows):
            if M[i][c] % p != 0:
                piv = i
                break
        if piv is None:
            continue
        M[r], M[piv] = M[piv], M[r]
        inv = pow(M[r][c], p - 2, p)
        M[r] = [(x * inv) % p for x in M[r]]
        for i in range(nrows):
            if i != r and M[i][c] % p != 0:
                f_ = M[i][c]
                M[i] = [(x - f_ * y) % p for x, y in zip(M[i], M[r])]
        r += 1
        if r == nrows:
            break
    return r


PRIMES = [1000003, 1000033]
