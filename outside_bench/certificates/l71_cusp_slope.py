"""OUTSIDE BENCH -- L71: what the theta-odd deformations do to the cusp.

Seal: outside_bench/seals/L71_CUSP_SLOPE_PREREG.md
      sha256 788faf6fd92a0674109f38307cdf1725bb9f28c298e533956e181d47fc19ad31
      committed before this file was written, WITH the m=1,2 prototype disclosed.

Exact arithmetic in K = Q(zeta_6), u^2 = u - 1, over Fraction coefficients.
No sympy, no floats anywhere in the cells.

CELL 1  slope_m for m = 1..12
CELL 2  is the value forced by the cusp, or global?
CELL 3  MB12 -- does the statistic read the representation?

Run: python3 outside_bench/certificates/l71_cusp_slope.py
"""
from fractions import Fraction as F

EXPONENTS = {1, 4, 5, 7, 8, 11}


class K:
    """a + b*u  with u^2 = u - 1   (u = zeta_6; conj(u) = 1 - u)."""
    __slots__ = ('a', 'b')

    def __init__(self, a=0, b=0):
        self.a, self.b = F(a), F(b)

    def __add__(s, o): return K(s.a + o.a, s.b + o.b)
    def __sub__(s, o): return K(s.a - o.a, s.b - o.b)
    def __neg__(s): return K(-s.a, -s.b)

    def __mul__(s, o):
        # (a+bu)(c+du) = ac + (ad+bc)u + bd(u-1)
        return K(s.a * o.a - s.b * o.b, s.a * o.b + s.b * o.a + s.b * o.b)

    def inv(s):
        # norm = a^2 + ab + b^2 ; (a+bu)^-1 = (a + b - b u)/norm
        n = s.a * s.a + s.a * s.b + s.b * s.b
        assert n != 0, "inverting zero"
        return K((s.a + s.b) / n, -s.b / n)

    def __truediv__(s, o): return s * o.inv()
    def is_zero(s): return s.a == 0 and s.b == 0
    def __eq__(s, o): return s.a == o.a and s.b == o.b
    def conj(s): return K(s.a + s.b, -s.b)          # u -> 1-u

    def __repr__(s):
        # in the basis 1, sqrt(-3):  u = 1/2 + sqrt(-3)/2
        re, im = s.a + s.b / 2, s.b / 2
        if im == 0: return str(re)
        p = '+' if im > 0 else '-'
        av = abs(im)
        t = 'sqrt(-3)' if av == 1 else f'{av}*sqrt(-3)'
        return (f'{re} {p} {t}' if re != 0 else (t if im > 0 else '-' + t))


ZERO, ONE = K(0), K(1)


def mmul(X, Y):
    n, p, q = len(X), len(Y), len(Y[0])
    return [[sum((X[i][k] * Y[k][j] for k in range(p)), ZERO) for j in range(q)] for i in range(n)]


def eye(n): return [[ONE if i == j else ZERO for j in range(n)] for i in range(n)]


def sym_power(M, n):
    """Sym^n of a 2x2 matrix M = ((a,b),(c,d)) in the monomial basis x^(n-i) y^i."""
    a, b, c, d = M
    R = [[ZERO] * (n + 1) for _ in range(n + 1)]
    for i in range(n + 1):                       # image of basis vector i
        coeffs = {}
        # (a x + c y)^(n-i) (b x + d y)^i  -- x -> a x + c y, y -> b x + d y
        for s in range(n - i + 1):
            for t in range(i + 1):
                cf = ONE
                for _ in range(n - i - s): cf = cf * a
                for _ in range(s): cf = cf * c
                for _ in range(i - t): cf = cf * b
                for _ in range(t): cf = cf * d
                cf = cf * K(_binom(n - i, s) * _binom(i, t))
                k = s + t
                coeffs[k] = coeffs.get(k, ZERO) + cf
        for k, v in coeffs.items():
            R[k][i] = v
    return R


def _binom(n, k):
    r = 1
    for j in range(k):
        r = r * (n - j) // (j + 1)
    return r


def rref(rows, ncols):
    """Row-reduce; returns (reduced rows, pivot columns)."""
    M = [r[:] for r in rows]
    piv, r = [], 0
    for c in range(ncols):
        p = next((i for i in range(r, len(M)) if not M[i][c].is_zero()), None)
        if p is None: continue
        M[r], M[p] = M[p], M[r]
        iv = M[r][c].inv()
        M[r] = [x * iv for x in M[r]]
        for i in range(len(M)):
            if i != r and not M[i][c].is_zero():
                f = M[i][c]
                M[i] = [M[i][j] - f * M[r][j] for j in range(ncols)]
        piv.append(c); r += 1
        if r == len(M): break
    return M[:r], piv


def nullspace(rows, ncols):
    R, piv = rref(rows, ncols)
    free = [c for c in range(ncols) if c not in piv]
    basis = []
    for fc in free:
        v = [ZERO] * ncols
        v[fc] = ONE
        for i, pc in enumerate(piv):
            v[pc] = -R[i][fc]
        basis.append(v)
    return basis


def rank(rows, ncols):
    return len(rref(rows, ncols)[0])


W = 'bABa'
RWORD = 'a' + W + 'B' + W[::-1].swapcase()
LAM = W + W[::-1]


def stage(n, u):
    A = (ONE, ONE, ZERO, ONE)
    B = (ONE, ZERO, u, ONE)
    Ai = (ONE, -ONE, ZERO, ONE)
    Bi = (ONE, ZERO, -u, ONE)
    return {'a': sym_power(A, n), 'A': sym_power(Ai, n),
            'b': sym_power(B, n), 'B': sym_power(Bi, n)}


def slope(m, u, verbose=False):
    n, d = 2 * m, 2 * m + 1
    tab = stage(n, u)
    I = eye(d)

    def word(w):
        M = I
        for ch in w: M = mmul(M, tab[ch])
        return M

    rel = word(RWORD)
    rel_ok = all((rel[i][j] - I[i][j]).is_zero() for i in range(d) for j in range(d))
    Lm = word(LAM)
    Am = tab['a']
    comm_ok = all((mmul(Lm, Am)[i][j] - mmul(Am, Lm)[i][j]).is_zero()
                  for i in range(d) for j in range(d))

    def fox(w, gen):
        T = [[ZERO] * d for _ in range(d)]
        pref = I
        for ch in w:
            if ch.lower() == gen:
                add = pref if ch.islower() else [[-x for x in row] for row in mmul(pref, tab[ch])]
                T = [[T[i][j] + add[i][j] for j in range(d)] for i in range(d)]
            pref = mmul(pref, tab[ch])
        return T

    Fa, Fb = fox(RWORD, 'a'), fox(RWORD, 'b')
    Z = nullspace([Fa[i] + Fb[i] for i in range(d)], 2 * d)
    cob = []
    for j in range(d):
        e = [ONE if i == j else ZERO for i in range(d)]
        cob.append([sum(((Am[i][k] - I[i][k]) * e[k] for k in range(d)), ZERO) for i in range(d)]
                   + [sum(((tab['b'][i][k] - I[i][k]) * e[k] for k in range(d)), ZERO) for i in range(d)])
    Rcob, pivcob = rref(cob, 2 * d)
    rb = len(Rcob)
    h1 = len(Z) - rb

    def outside_span(v):
        w = v[:]
        for i, pc in enumerate(pivcob):
            if not w[pc].is_zero():
                f0 = w[pc]
                w = [w[j] - f0 * Rcob[i][j] for j in range(2 * d)]
        return any(not x.is_zero() for x in w)
    h0 = d - rank([[Am[i][j] - I[i][j] for j in range(d)] for i in range(d)]
                  + [[tab['b'][i][j] - I[i][j] for j in range(d)] for i in range(d)], d)
    per = d - rank([[Am[i][j] - I[i][j] for j in range(d)] for i in range(d)], d)

    xi = next((z for z in Z if outside_span(z)), None)
    assert xi is not None, f"m={m}: no cocycle outside the coboundaries"
    xa, xb = xi[:d], xi[d:]

    def cocycle(w):
        v = [ZERO] * d
        pref = I
        for ch in w:
            if ch == 'a': g = xa
            elif ch == 'b': g = xb
            else:
                src = xa if ch == 'A' else xb
                g = [-sum((tab[ch][i][k] * src[k] for k in range(d)), ZERO) for i in range(d)]
            v = [v[i] + sum((pref[i][k] * g[k] for k in range(d)), ZERO) for i in range(d)]
            pref = mmul(pref, tab[ch])
        return v

    xl = cocycle(LAM)
    # coker(N), N = rho(a) - I : a functional vanishing on im N
    N = [[Am[i][j] - I[i][j] for j in range(d)] for i in range(d)]
    NT = [[N[i][j] for i in range(d)] for j in range(d)]      # transpose
    fs = nullspace(NT, d)
    assert len(fs) == 1, f"m={m}: coker has dim {len(fs)}"
    f = fs[0]
    ca = sum((f[i] * xa[i] for i in range(d)), ZERO)
    cl = sum((f[i] * xl[i] for i in range(d)), ZERO)
    s = None if ca.is_zero() else cl / ca
    return dict(rel_ok=rel_ok, comm_ok=comm_ok, h0=h0, h1=h1, per=per,
                ca=ca, cl=cl, slope=s, N=N, Am=Am, Lm=Lm, d=d, f=f)


U = K(0, 1)                       # u = zeta_6
TAU = K(0, -2) - K(0, 2) * K(-1)  # placeholder, set properly below
TAU = K(F(0), F(0))
# tau = -2*sqrt(-3) = -2*(2u - 1) = 2 - 4u
TAU = K(2, -4)

print("=" * 78)
print("L71 -- WHAT THE THETA-ODD DEFORMATIONS DO TO THE CUSP")
print("seal sha256 788faf6fd92a0674109f38307cdf1725bb9f28c298e533956e181d47fc19ad31")
print("=" * 78)
print(f"\n  presentation <a,b | {RWORD}>   longitude {LAM}")
print(f"  rho(a)=[[1,1],[0,1]]  rho(b)=[[1,0],[u,1]]  u = zeta_6, u^2 = u-1")
print(f"  the target value tau = -2*sqrt(-3) = {TAU}")

print("\n" + "=" * 78)
print("CELL 1 -- the slopes, m = 1 .. 12   (E6 exponents starred)")
print("=" * 78)
res = {}
allA = True
for m in range(1, 13):
    r = slope(m, U)
    res[m] = r
    star = '*' if m in EXPONENTS else ' '
    ok = (r['slope'] is not None and r['slope'] == TAU)
    allA &= ok
    print(f" {star} m={m:2d}  dim={r['d']:2d}  rel_ok={r['rel_ok']}  [a],[lam] commute={r['comm_ok']}"
          f"  h0={r['h0']} h1={r['h1']} periph_inv={r['per']}")
    print(f"        [xi(a)] = {r['ca']}     [xi(lambda)] = {r['cl']}")
    print(f"        slope   = {r['slope']}   == tau : {ok}")
print(f"\n  CELL 1 OUTCOME: {'A' if allA else 'B'}   (all twelve equal -2*sqrt(-3): {allA})")

print("\n  C1/C2/C3 -- controls read off the same run:")
print(f"    relator = I in every block                 : {all(res[m]['rel_ok'] for m in res)}")
print(f"    rho(lambda) commutes with rho(a) every m   : {all(res[m]['comm_ok'] for m in res)}")
six = {m: res[m] for m in sorted(EXPONENTS)}
print(f"    at the six E6 exponents: h0 = {[six[m]['h0'] for m in six]},"
      f" h1 = {[six[m]['h1'] for m in six]},"
      f" periph_inv = {[six[m]['per'] for m in six]}")
print("      (P2W5-L72's exact Q(zeta_6) table: h0 = 0, h1 = 1, periph_inv = 1 for all six)")
assert all(six[m]['h0'] == 0 and six[m]['h1'] == 1 and six[m]['per'] == 1 for m in six)

print("\n" + "=" * 78)
print("CELL 2 -- is the value forced by the cusp alone?")
print("=" * 78)
print("  The cusp condition is  (rho(a)-I) xi(lam) = (rho(lam)-I) xi(a).")
print("  Solve it for the PAIR (xi(a), xi(lam)) freely and look at the ratio of classes.")
free_ok = True
for m in range(1, 13):
    r = res[m]
    d = r['d']
    Na = [[r['Am'][i][j] - (ONE if i == j else ZERO) for j in range(d)] for i in range(d)]
    Nl = [[r['Lm'][i][j] - (ONE if i == j else ZERO) for j in range(d)] for i in range(d)]
    # rows of [ -Nl | Na ] acting on (xi(a), xi(lam)) = 0
    rows = [[-Nl[i][j] for j in range(d)] + [Na[i][j] for j in range(d)] for i in range(d)]
    basis = nullspace(rows, 2 * d)
    f = r['f']
    ratios = []
    for v in basis:
        ca = sum((f[i] * v[i] for i in range(d)), ZERO)
        cl = sum((f[i] * v[d + i] for i in range(d)), ZERO)
        ratios.append((ca, cl))
    # is there a solution with [xi(lam)] != tau [xi(a)] ?
    witness = any(not (cl - TAU * ca).is_zero() for ca, cl in ratios)
    free_ok &= witness
    print(f"   m={m:2d}  cusp-only solution space dim {len(basis):2d};"
          f"  a solution with ratio != tau exists: {witness}")
print(f"\n  CELL 2 OUTCOME: {'A' if free_ok else 'B'}"
      f"   (the cusp does NOT force the ratio: {free_ok})")

print("\n" + "=" * 78)
print("CELL 3 -- MB12: does the statistic read the representation?")
print("=" * 78)
UBAR = U.conj()
print(f"  conjugate rep: u -> 1 - u = {UBAR}")
c3 = True
for m in (1, 4, 8):
    r = slope(m, UBAR)
    exp = TAU.conj()
    ok = r['slope'] == exp
    c3 &= ok
    print(f"   m={m:2d}  slope(conjugate rep) = {r['slope']}   expected conj(tau) = {exp}   {ok}")
print(f"\n  CELL 3 OUTCOME: {'A' if c3 else 'B'}   (the statistic MOVES with the rep: {c3})")

print("\n" + "=" * 78)
print("C4 -- SnapPy's cusp shape of 4_1 (magnitude is the test; sign is convention)")
print("=" * 78)
try:
    import warnings
    warnings.filterwarnings('ignore')
    import snappy
    sh = snappy.Manifold('4_1').cusp_info('shape')[0]
    print(f"  SnapPy cusp shape      : {sh}")
    print(f"  this bench's tau       : {TAU}   = -2*sqrt(3)*i ~ -3.4641016151i")
    print(f"  |SnapPy| = {abs(complex(sh)):.10f}   |tau| = {2*3**0.5:.10f}")
    print(f"  magnitudes agree to    : {abs(abs(complex(sh)) - 2*3**0.5):.3e}")
    print("  SIGN DIFFERS -- SnapPy's meridian/longitude orientation is its own;")
    print("  this was fenced in the seal as a convention difference, not a discrepancy.")
    assert abs(abs(complex(sh)) - 2 * 3 ** 0.5) < 1e-9
except ImportError:
    print("  SnapPy not available -- control skipped, and the skip is reported.")

print("\n" + "=" * 78)
print("POST-HOC MECHANISM -- NOT PREREGISTERED: WHY the cusp forces it")
print("=" * 78)
print("""  rho(a) = exp(N), rho(lambda) = exp(tau N) with the SAME nilpotent N (single block).
  Write exp(N) - I = N.phi(N) with phi(N) = I + N/2 + N^2/6 + ... , which is UNIPOTENT.
  The cusp condition (exp(N)-I) xi(lam) = (exp(tau N)-I) xi(a) becomes
       N ( phi(N) xi(lam) - tau phi(tau N) xi(a) ) = 0,
  so the bracket lies in ker N.  Now apply f, the functional with f o N = 0:
    - f(phi(N) v) = f(v) for every v, since phi(N) - I is a polynomial in N with no
      constant term and f o N = 0;
    - f vanishes on ker N whenever dim > 1.
  Hence f(xi(lam)) = tau f(xi(a)) IDENTICALLY.  The three ingredients, checked exactly:""")
for m in range(1, 7):
    n, d = 2 * m, 2 * m + 1
    tab = stage(n, U)
    I = eye(d)
    Am = tab['a']
    N = [[Am[i][j] - I[i][j] for j in range(d)] for i in range(d)]
    NT = [[N[i][j] for i in range(d)] for j in range(d)]
    f = nullspace(NT, d)[0]
    fN = [sum((f[i] * N[i][j] for i in range(d)), ZERO) for j in range(d)]
    kerN = nullspace(N, d)
    fker = [sum((f[i] * v[i] for i in range(d)), ZERO) for v in kerN]
    print(f"   m={m:2d}  dim={d:2d}   f o N = 0 : {all(x.is_zero() for x in fN)}"
          f"   dim ker N = {len(kerN)}   f(ker N) = 0 : {all(x.is_zero() for x in fker)}")
    assert all(x.is_zero() for x in fN) and all(x.is_zero() for x in fker)
print("""
  So the statistic reads the CUSP SHAPE and nothing else.  It cannot distinguish the
  theta-odd deformations from the geometric one, at any m, by construction.""")

print("\n" + "=" * 78)
print("DONE -- outcomes above; interpretation lives in the memo, not here.")
print("=" * 78)
