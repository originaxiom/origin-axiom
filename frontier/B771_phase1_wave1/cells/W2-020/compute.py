"""
W2-020 (L64) -- INDEPENDENT Fox-calculus recomputation of H^1(pi_1(4_1), Ad_E6 rho_geo) = 6
and its theta-grading (E6-only exponents {4,8} vs F4-shared exponents {1,5,7,11}).

INDEPENDENCE from the two banked pipelines:
  (1) B445 (e6_h1_hp.py): numeric (mpmath dps=60), generators = SnapPy's own
      simplified-presentation matrices M.fundamental_group().SL2C(g), relator
      "abbbaBAAB" (SnapPy's internal Tietze-reduced word, whose generators a,b
      are NOT literal meridians).
  (2) B575 G4 (l51_obstruction.py): exact over Q(sqrt(-3)), generators built by
      exponentiating the e6 root vectors e_pr,f_pr inside the 27-dim minuscule
      rep, relator word "abABaBAbaB" (a 10-letter word tied to the E6 embedding
      construction), Fox calculus done on 78-dim adjoint blocks via the
      SL(2)-isotypic decomposition of e6 itself.

THIS CELL: a third, independent construction --
  - presentation: the classical RILEY parabolic presentation of the figure-eight
    knot group, <a,b | a W = W b>, W = b^-1 a b a^-1 (Riley 1975), whose
    generators a,b ARE literal meridians (parabolic, trace 2) by construction.
  - representation: solved from scratch here (not asserted) by requiring the
    relator matrix identity to hold for A=[[1,1],[0,1]], B=[[1,0],[-w,1]];
    this reduces the relator to the single polynomial w^2+w+1=0 (an exact,
    in-cell derivation, not a citation).
  - field: Q(sqrt(-3)) via an exact Fraction-based K class (independent
    implementation, Eisenstein-integer arithmetic on w = (-1+sqrt(-3))/2,
    the OTHER primitive cube root of unity than B575's OMEGA=(1+sqrt(-3))/2).
  - the SL(2) rep is lifted to Sym^{2m}(rho) for m in the six E6 exponents
    {1,4,5,7,8,11} (NOT via any E6 bracket -- pure SL(2) symmetric powers,
    exactly as MFP's theorem organizes the E6 adjoint), and H^1/H^2/H^0 are
    computed by exact Fox calculus (Fox Jacobian nullspace / coboundary rank)
    on THIS word, entirely independent linear algebra from both banked runs.
  - a second seed (the conjugate root of w^2+w+1=0, i.e. complex conjugation
    of the field) is run as the required >=2-seed check.

SEALED CRITERION (W2-020): independent method agrees with H^1=6 (and the
4+2 theta-split) => RESOLVED-A; disagrees (discrepancy shown) => RESOLVED-B.
"""
import sys
import time
from fractions import Fraction as Fr

T0 = time.time()
def log(msg):
    print(f"[{time.time()-T0:7.2f}s] {msg}", flush=True)

# ============================================================ exact field Q(sqrt(-3))
class K:
    """a + b*sqrt(-3), a,b in Q (Fraction)."""
    __slots__ = ('a', 'b')
    def __init__(self, a=0, b=0):
        self.a = a if isinstance(a, Fr) else Fr(a)
        self.b = b if isinstance(b, Fr) else Fr(b)
    def __add__(s, o): o = s._c(o); return K(s.a + o.a, s.b + o.b)
    def __radd__(s, o): return s.__add__(o)
    def __sub__(s, o): o = s._c(o); return K(s.a - o.a, s.b - o.b)
    def __rsub__(s, o): return s._c(o).__sub__(s)
    def __neg__(s):    return K(-s.a, -s.b)
    def __mul__(s, o):
        o = s._c(o)
        return K(s.a * o.a - 3 * s.b * o.b, s.a * o.b + s.b * o.a)
    def __rmul__(s, o): return s.__mul__(o)
    @staticmethod
    def _c(o):
        return o if isinstance(o, K) else K(o)
    def conj(s): return K(s.a, -s.b)          # sqrt(-3) -> -sqrt(-3)
    def norm(s): return s.a * s.a + 3 * s.b * s.b
    def inv(s):
        n = s.norm()
        assert n != 0, "division by zero in K"
        c = s.conj()
        return K(c.a / n, c.b / n)
    def __truediv__(s, o): return s * s._c(o).inv()
    def __eq__(s, o):
        o = s._c(o)
        return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def is_zero(s): return s.a == 0 and s.b == 0
    def __repr__(s):
        return f"({s.a}+{s.b}*sqrt(-3))" if s.b else f"({s.a})"

K0, K1 = K(0), K(1)

def Kint(n): return K(Fr(n), Fr(0))

def Kpow(x, e):
    r = K1
    for _ in range(e):
        r = r * x
    return r

# ============================================================ generic exact linear algebra
def mzero(n, m): return [[K0] * m for _ in range(n)]
def meye(n):
    M = mzero(n, n)
    for i in range(n):
        M[i][i] = K1
    return M

def mmul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    Bt = list(zip(*B))
    out = []
    for i in range(n):
        Ai = A[i]
        row = []
        for j in range(m):
            Bj = Bt[j]
            ssum = K0
            for t in range(k):
                if not Ai[t].is_zero() and not Bj[t].is_zero():
                    ssum = ssum + Ai[t] * Bj[t]
            row.append(ssum)
        out.append(row)
    return out

def madd(A, B): return [[A[i][j] + B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def msub(A, B): return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def mscale(c, A): return [[c * x for x in row] for row in A]
def mzero_p(A): return all(x.is_zero() for row in A for x in row)
def minv2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    det = a * d - b * c
    assert not det.is_zero(), "singular 2x2"
    di = det.inv()
    return [[d * di, K(0) - b * di], [K(0) - c * di, a * di]]

def rref(M):
    """Row-reduce M (list of rows of K). Returns (rref_rows, pivot_cols)."""
    A = [row[:] for row in M]
    rows = len(A)
    cols = len(A[0]) if A else 0
    piv = []
    r = 0
    for c in range(cols):
        pr = None
        for i in range(r, rows):
            if not A[i][c].is_zero():
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        iv = A[r][c].inv()
        A[r] = [x * iv for x in A[r]]
        for i in range(rows):
            if i != r and not A[i][c].is_zero():
                f = A[i][c]
                A[i] = [A[i][j] - f * A[r][j] for j in range(cols)]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return A[:r], piv

def nullspace(M):
    """Basis of {v : M v = 0}, M = rows x cols."""
    if not M:
        return []
    R, piv = rref(M)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for fc in free:
        v = [K0] * cols
        v[fc] = K1
        for r_i, pc in enumerate(piv):
            v[pc] = K(0) - R[r_i][fc]
        basis.append(v)
    return basis

def rank(M):
    R, piv = rref(M)
    return len(piv)

# ============================================================ stage 0: the Riley presentation
# Word bookkeeping: lowercase = generator, uppercase = its inverse.
def word_matrix(word, LET):
    Mx = meye(2)
    for ch in word:
        Mx = mmul(Mx, LET[ch])
    return Mx

def invert_word(word):
    """Inverse of a word: reverse it and swap case of every letter."""
    swap = str.maketrans('abAB', 'ABab')
    return word[::-1].translate(swap)

log("stage 0: deriving the Riley relation a W = W b, W = b^-1 a b a^-1 (from scratch, symbolic in w)")

# Solve for w symbolically first with a tiny exact polynomial solver (sympy is
# allowed for the ONE polynomial-solve step; all downstream linear algebra is
# the hand-rolled exact field above, independent of sympy's matrix code).
import sympy as sp
wsym = sp.symbols('w')
Asym = sp.Matrix([[1, 1], [0, 1]])
Aisym = sp.Matrix([[1, -1], [0, 1]])
Bsym = sp.Matrix([[1, 0], [-wsym, 1]])
Bisym = sp.Matrix([[1, 0], [wsym, 1]])
Wsym = Bisym * Asym * Bsym * Aisym
lhs = sp.expand(Asym * Wsym)
rhs = sp.expand(Wsym * Bsym)
diff = sp.expand(lhs - rhs)
p01 = sp.Poly(diff[0, 1], wsym)
p10 = sp.factor(diff[1, 0])
log(f"  relator condition (0,1) entry: {p01.as_expr()} = 0")
log(f"  relator condition (1,0) entry (must share the same nontrivial factor): {p10}")
assert p01.as_expr() == wsym**2 + wsym + 1, f"unexpected Riley polynomial: {p01.as_expr()}"
roots = sp.solve(wsym**2 + wsym + 1, wsym)
log(f"  Riley polynomial w^2+w+1=0 roots: {roots}  (primitive cube roots of unity, in Q(sqrt(-3)))")
assert len(roots) == 2

# Exact K-field roots: w = (-1 +/- sqrt(-3))/2
W_SEEDS = [K(Fr(-1, 2), Fr(1, 2)), K(Fr(-1, 2), Fr(-1, 2))]
for wchk in W_SEEDS:
    val = wchk * wchk + wchk + K1
    assert val.is_zero(), f"seed root check failed: {wchk}"
log(f"  both seeds verified exactly in the hand-rolled K field: w1={W_SEEDS[0]}, w2={W_SEEDS[1]}")

# The full relator as an explicit word (independent of B445's and B575's words):
#   R = a * W * b^-1 * W^-1,   W = "BabA"  (= b^-1 a b a^-1)
W_WORD = "BabA"
WINV_WORD = invert_word(W_WORD)
assert WINV_WORD == "aBAb", WINV_WORD
REL_WORD = "a" + W_WORD + "B" + WINV_WORD
log(f"  W word = {W_WORD!r}, W^-1 word = {WINV_WORD!r}, full relator word R = {REL_WORD!r} (len {len(REL_WORD)})")

# ============================================================ MAIN routine, run once per seed
def run_seed(w, seed_name):
    log(f"===== SEED {seed_name}: w = {w} =====")
    A = [[K1, K1], [K0, K1]]
    Ai = [[K1, K(0) - K1], [K0, K1]]
    B = [[K1, K0], [K(0) - w, K1]]
    Bi = [[K1, K0], [w, K1]]
    assert mzero_p(msub(mmul(A, Ai), meye(2)))
    assert mzero_p(msub(mmul(B, Bi), meye(2)))
    LET = {'a': A, 'A': Ai, 'b': B, 'B': Bi}

    Rm = word_matrix(REL_WORD, LET)
    assert mzero_p(msub(Rm, meye(2))), f"RELATOR FAILS for seed {seed_name}: {Rm}"
    log(f"  relator '{REL_WORD}' -> identity, EXACT, confirmed in 2x2 (end-to-end presentation check)")

    # trace field sanity: tr(A B) should generate Q(sqrt(-3)) (not a bigger/smaller field)
    AB = mmul(A, B)
    trAB = AB[0][0] + AB[1][1]
    log(f"  tr(AB) = {trAB}  (in Q(sqrt(-3)), consistent with the figure-eight's known invariant trace field)")

    # -------------------------------------------------- Sym^{2m} construction over K
    def sym_power(M, n):
        """Sym^n of a 2x2 matrix M, as an (n+1)x(n+1) exact K matrix.
        Column k (0-indexed) = coefficients of (a x + c y)^{n-k} (b x + d y)^k
        in the monomial basis x^n, x^{n-1}y, ..., y^n."""
        a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]

        def poly_pow(p, q, e):
            out = [K0] * (e + 1)
            for i in range(e + 1):
                out[i] = Kint(_binom(e, i)) * Kpow(p, e - i) * Kpow(q, i)
            return out

        def conv(u, v):
            r = [K0] * (len(u) + len(v) - 1)
            for i, ui in enumerate(u):
                if ui.is_zero():
                    continue
                for j, vj in enumerate(v):
                    if vj.is_zero():
                        continue
                    r[i + j] = r[i + j] + ui * vj
            return r

        dim = n + 1
        out = mzero(dim, dim)
        for k in range(dim):
            col = conv(poly_pow(a, c, n - k), poly_pow(b, d, k))
            for i in range(dim):
                out[i][k] = col[i]
        return out

    from math import comb as _binom

    # -------------------------------------------------- Fox calculus per block
    EXPONENTS = [1, 4, 5, 7, 8, 11]
    THETA_ODD = {4, 8}       # E6-only, NOT F4 exponents
    THETA_EVEN = {1, 5, 7, 11}  # F4 exponents {1,5,7,11} -- Bourbaki degrees {2,6,8,12} minus 1
    assert set(EXPONENTS) == THETA_ODD | THETA_EVEN

    results = {}
    for m in EXPONENTS:
        n = 2 * m
        d = n + 1
        Asp = sym_power(A, n)
        Bsp = sym_power(B, n)
        Aisp = sym_power(Ai, n)
        Bisp = sym_power(Bi, n)
        assert mzero_p(msub(mmul(Asp, Aisp), meye(d)))
        assert mzero_p(msub(mmul(Bsp, Bisp), meye(d)))
        REP = {'a': Asp, 'A': Aisp, 'b': Bsp, 'B': Bisp}

        # Fox Jacobian: walk REL_WORD, accumulate prefix action; d x 2d matrix [Ca|Cb]
        Ca = mzero(d, d)
        Cb = mzero(d, d)
        Pi_act = meye(d)
        for ch in REL_WORD:
            if ch == 'a':
                contrib, tgt = meye(d), 'a'
            elif ch == 'A':
                contrib, tgt = mscale(K(-1), Aisp), 'a'
            elif ch == 'b':
                contrib, tgt = meye(d), 'b'
            else:  # 'B'
                contrib, tgt = mscale(K(-1), Bisp), 'b'
            term = mmul(Pi_act, contrib)
            if tgt == 'a':
                Ca = madd(Ca, term)
            else:
                Cb = madd(Cb, term)
            Pi_act = mmul(Pi_act, REP[ch])
        assert mzero_p(msub(Pi_act, meye(d))), "prefix product did not close up to the identity"

        L = [[Ca[i][j] for j in range(d)] + [Cb[i][j] for j in range(d)] for i in range(d)]
        Z1 = nullspace(L)
        dimZ1 = len(Z1)

        # B1 = image of the coboundary map v -> ((a-1)v, (b-1)v)
        stack_rows = []  # we build the map as a (2d) x d matrix and rank it
        coM = [[Asp[i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)] + \
              [[Bsp[i][j] - (K1 if i == j else K0) for j in range(d)] for i in range(d)]
        dimB1 = rank(coM)     # rank of the (2d x d) coboundary matrix = dim of its image
        dimH0 = d - dimB1

        dimH1 = dimZ1 - dimB1

        # H^2 = left-nullspace of L (functionals phi with phi.L = 0)
        Lt = [[L[i][j] for i in range(d)] for j in range(2 * d)]
        phis = nullspace(Lt)
        dimH2 = len(phis)

        grade = 'theta-odd (E6-only)' if m in THETA_ODD else 'theta-even (F4-shared)'
        results[m] = dict(d=d, Z1=dimZ1, B1=dimB1, H0=dimH0, H1=dimH1, H2=dimH2, grade=grade)
        log(f"  m={m:2d} (Sym^{n:<2d}, dim {d:2d}, {grade:24s}): "
            f"H0={dimH0} Z1={dimZ1} B1={dimB1} -> H1={dimH1}, H2={dimH2}")

    total_H1 = sum(r['H1'] for r in results.values())
    total_H2 = sum(r['H2'] for r in results.values())
    theta_even_H1 = sum(results[m]['H1'] for m in THETA_EVEN)
    theta_odd_H1 = sum(results[m]['H1'] for m in THETA_ODD)
    log(f"  TOTAL: dim H^1(pi_1, Ad_E6 rho_geo) = {total_H1}   (banked value: 6)")
    log(f"  TOTAL: dim H^2 = {total_H2}")
    log(f"  theta-split: theta-even (F4-shared, m in {sorted(THETA_EVEN)}) H1 sum = {theta_even_H1}  "
        f"(banked: 4)")
    log(f"  theta-split: theta-odd  (E6-only,   m in {sorted(THETA_ODD)}) H1 sum = {theta_odd_H1}  "
        f"(banked: 2)")
    return dict(results=results, total_H1=total_H1, total_H2=total_H2,
                theta_even_H1=theta_even_H1, theta_odd_H1=theta_odd_H1)


SEED_RESULTS = {}
for w, name in zip(W_SEEDS, ["S1 (w=(-1+sqrt(-3))/2)", "S2 (w=(-1-sqrt(-3))/2, conjugate)"]):
    SEED_RESULTS[name] = run_seed(w, name)

# ============================================================ verdict
log("=" * 70)
log("VERDICT ASSEMBLY")
all_agree = True
for name, R in SEED_RESULTS.items():
    ok = (R['total_H1'] == 6 and R['theta_even_H1'] == 4 and R['theta_odd_H1'] == 2)
    log(f"  seed {name}: total H1={R['total_H1']}, theta-even={R['theta_even_H1']}, "
        f"theta-odd={R['theta_odd_H1']}  -> {'MATCH' if ok else 'MISMATCH'}")
    all_agree = all_agree and ok

# cross-seed consistency (both roots of the Riley polynomial must give the same dims,
# block by block -- complex conjugation of the field permutes nothing structural)
s1, s2 = list(SEED_RESULTS.values())
per_block_agree = all(s1['results'][m]['H1'] == s2['results'][m]['H1'] for m in s1['results'])
log(f"  cross-seed per-block H1 agreement: {per_block_agree}")

VERDICT = "RESOLVED-A" if (all_agree and per_block_agree) else "RESOLVED-B"
log(f"FINAL VERDICT: {VERDICT}")
log("Independent inputs used: Riley 1975 presentation shape (a,b meridians, W=b^-1aba^-1) "
    "as an ansatz; the polynomial w^2+w+1=0 pinning the representation was DERIVED in-cell, "
    "not asserted. E6/F4 exponent sets {1,4,5,7,8,11}/{1,5,7,11} are standard Bourbaki-table "
    "Lie data (Coxeter degrees - 1), used as bedrock, not computed here.")
