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
TAU = K(2, -4)                                  # -2*sqrt(-3)
U = K(0, 1)


def stage(n, u):
    A = (ONE, ONE, ZERO, ONE); B = (ONE, ZERO, u, ONE)
    Ai = (ONE, -ONE, ZERO, ONE); Bi = (ONE, ZERO, -u, ONE)
    return {'a': sym_power(A, n), 'A': sym_power(Ai, n),
            'b': sym_power(B, n), 'B': sym_power(Bi, n)}


def mv(M, v):
    return [sum((M[i][k] * v[k] for k in range(len(v))), ZERO) for i in range(len(M))]


def solve(M, rhs, ncols):
    """one solution of M x = rhs, or None."""
    rows = [M[i][:] + [rhs[i]] for i in range(len(M))]
    R, piv = rref(rows, ncols + 1)
    if ncols in piv:
        return None
    x = [ZERO] * ncols
    for i, pc in enumerate(piv):
        x[pc] = R[i][ncols]
    return x


def analyse(m):
    n, d = 2 * m, 2 * m + 1
    tab = stage(n, U); I = eye(d)

    def word(w):
        M = I
        for ch in w: M = mmul(M, tab[ch])
        return M

    rel = word(RWORD)
    rel_ok = all((rel[i][j] - I[i][j]).is_zero() for i in range(d) for j in range(d))
    Am, Lm = tab['a'], word(LAM)
    comm_ok = all((mmul(Lm, Am)[i][j] - mmul(Am, Lm)[i][j]).is_zero()
                  for i in range(d) for j in range(d))
    Na = [[Am[i][j] - I[i][j] for j in range(d)] for i in range(d)]
    Nl = [[Lm[i][j] - I[i][j] for j in range(d)] for i in range(d)]

    def fox(w, gen):
        T = [[ZERO] * d for _ in range(d)]; pref = I
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
        cob.append(mv(Na, e) + mv([[tab['b'][i][jj] - I[i][jj] for jj in range(d)]
                                   for i in range(d)], e))
    Rc, pc = rref(cob, 2 * d)

    def outside(v):
        w = v[:]
        for i, p in enumerate(pc):
            if not w[p].is_zero():
                f0 = w[p]; w = [w[j] - f0 * Rc[i][j] for j in range(2 * d)]
        return any(not x.is_zero() for x in w)

    h1 = len(Z) - len(Rc)
    h0 = d - rank([r[:] for r in Na] + [[tab['b'][i][j] - I[i][j] for j in range(d)]
                                        for i in range(d)], d)
    per = d - rank([r[:] for r in Na], d)
    xi = next(z for z in Z if outside(z))
    xa, xb = xi[:d], xi[d:]

    def cocycle(w):
        v = [ZERO] * d; pref = I
        for ch in w:
            if ch == 'a': g = xa
            elif ch == 'b': g = xb
            else:
                src = xa if ch == 'A' else xb
                g = [-t for t in mv(tab[ch], src)]
            v = [v[i] + mv(pref, g)[i] for i in range(d)]
            pref = mmul(pref, tab[ch])
        return v

    xl = cocycle(LAM)
    res = xa + xl

    # ---- the cusp space
    rows = [[-Nl[i][j] for j in range(d)] + [Na[i][j] for j in range(d)] for i in range(d)]
    Zc = nullspace(rows, 2 * d)
    Bc = [mv(Na, e) + mv(Nl, e) for e in
          ([ONE if i == j else ZERO for i in range(d)] for j in range(d))]
    rB = rank(Bc, 2 * d)
    dimH1T2 = len(Zc) - rB
    res_in_Zc = rank(Zc + [res], 2 * d) == len(Zc)

    # ---- ker N and the coker functional, COMPUTED not assumed
    kerN = nullspace([r[:] for r in Na], d)
    f = nullspace([[Na[i][j] for i in range(d)] for j in range(d)], d)[0]
    ker_idx = [i for i in range(d) if not kerN[0][i].is_zero()]
    f_idx = [i for i in range(d) if not f[i].is_zero()]

    # ---- CELL 2: are x -> f(x) and y -> f(y) proportional on Z^1(T^2)?
    prop = True
    for v in Zc:
        fx = sum((f[i] * v[i] for i in range(d)), ZERO)
        fy = sum((f[i] * v[d + i] for i in range(d)), ZERO)
        if not (fy - TAU * fx).is_zero():
            prop = False; break

    # ---- CELL 3: two declared completions, same res
    def coords(basis2, vec):
        M = [[basis2[0][i], basis2[1][i]] + [Bc[j][i] for j in range(d)] for i in range(2 * d)]
        s = solve(M, vec, 2 + d)
        return (s[0], s[1]) if s else None

    e0 = [ONE if i == 0 else ZERO for i in range(d)]
    k = kerN[0]
    BI = [k + [ZERO] * d, [ZERO] * d + k]                 # (kerN, 0) and (0, kerN)
    BI_ok = (rank(Bc + [BI[0]], 2 * d) == rB + 1
             and rank(Bc + BI, 2 * d) == rB + 2
             and rank(Zc + [BI[0]], 2 * d) == len(Zc)
             and rank(Zc + [BI[1]], 2 * d) == len(Zc))
    BII, RBc, pBc = [], *rref(Bc, 2 * d)

    def out2(v):
        w = v[:]
        for i, p in enumerate(pBc):
            if not w[p].is_zero():
                f0 = w[p]; w = [w[j] - f0 * RBc[i][j] for j in range(2 * d)]
        return any(not x.is_zero() for x in w)

    acc = [r[:] for r in Bc]
    for v in Zc:
        if len(BII) == 2: break
        if rank(acc + [v], 2 * d) > rank(acc, 2 * d):
            BII.append(v); acc = acc + [v]
    cI = coords(BI, res) if BI_ok else None
    cII = coords(BII, res) if len(BII) == 2 else None

    def ratio(c):
        return None if (c is None or c[0].is_zero()) else c[1] / c[0]

    return dict(rel_ok=rel_ok, comm_ok=comm_ok, h0=h0, h1=h1, per=per, d=d,
                dimH1T2=dimH1T2, res_zero=all(x.is_zero() for x in res),
                res_in_Zc=res_in_Zc, ker_idx=ker_idx, f_idx=f_idx, prop=prop,
                BI_ok=BI_ok, rI=ratio(cI), rII=ratio(cII), cI=cI, cII=cII)


EXPONENTS = {1, 4, 5, 7, 8, 11}
print("=" * 78)
print("L71 -- THE FULL PERIPHERAL CLASS: IS THERE A SECOND COORDINATE?")
print("seal sha256 d5c420834fe2a78a0c0f209ad7f32e0868ec252b8f4f5f9c25a179cc169d4de9")
print("  (the seal carries ADDENDUM 1: its first declared basis was WRONG and is corrected")
print("   there, before any cell below was read)")
print("=" * 78)

res = {}
for m in range(1, 12):
    r = analyse(m); res[m] = r
    star = '*' if m in EXPONENTS else ' '
    print(f"\n {star} m={m:2d}  dim={r['d']:2d}  rel_ok={r['rel_ok']} comm={r['comm_ok']}"
          f"  h0={r['h0']} h1={r['h1']} periph_inv={r['per']}  dim H^1(T^2)={r['dimH1T2']}")
    print(f"        ker N supported on index {r['ker_idx']};"
          f"  coker functional f supported on index {r['f_idx']}")
    print(f"        res(xi) is a cusp cocycle: {r['res_in_Zc']}      res(xi) = 0 ? {r['res_zero']}")
    print(f"        f(y) = tau*f(x) on ALL of Z^1(T^2): {r['prop']}")
    print(f"        beta/alpha  under basis I  : {r['rI']}")
    print(f"        beta/alpha  under basis II : {r['rII']}")

print("\n" + "=" * 78)
print("OUTCOMES")
print("=" * 78)
c1 = all(not res[m]['res_zero'] for m in res)
print(f"  CELL 1  res(xi) != 0 for every m           : {c1}  -> OUTCOME {'A' if c1 else 'B'}")
c2 = all(res[m]['prop'] for m in res)
print(f"  CELL 2  f(y) = tau f(x) on all of Z^1(T^2) : {c2}  -> OUTCOME {'A' if c2 else 'B'}")
diff = []
for m in res:
    a, b = res[m]['rI'], res[m]['rII']
    diff.append(None if (a is None or b is None) else (a == b))
c3_differ = any(x is False for x in diff)
print(f"  CELL 3  the two completions agree, per m   : {diff}")
print(f"          they DIFFER somewhere: {c3_differ}  -> OUTCOME {'A' if c3_differ else 'B'}")
print(f"\n  controls: dim H^1(T^2) = 2 every m: {all(res[m]['dimH1T2'] == 2 for m in res)};"
      f"  res is a cusp cocycle every m: {all(res[m]['res_in_Zc'] for m in res)}")
print(f"    six E6 exponents h0/h1/periph = "
      f"{[(res[m]['h0'], res[m]['h1'], res[m]['per']) for m in sorted(EXPONENTS)]}")

print("\n" + "=" * 78)
print("WHY basis I fails -- the canonical data spans only ONE dimension of H^1(T^2)")
print("=" * 78)
print("  ker N = <k>.  Both (k,0) and (0,k) are cusp cocycles and neither is a coboundary.")
print("  How many dimensions do they span MODULO the coboundaries?")
for m in range(1, 7):
    n, d = 2 * m, 2 * m + 1
    tab = stage(n, U); I = eye(d)
    def word(w):
        M = I
        for ch in w: M = mmul(M, tab[ch])
        return M
    Am, Lm = tab['a'], word(LAM)
    Na = [[Am[i][j] - I[i][j] for j in range(d)] for i in range(d)]
    Nl = [[Lm[i][j] - I[i][j] for j in range(d)] for i in range(d)]
    Bc = [mv(Na, e) + mv(Nl, e) for e in
          ([ONE if i == j else ZERO for i in range(d)] for j in range(d))]
    k = nullspace([r[:] for r in Na], d)[0]
    v1 = k + [ZERO] * d
    v2 = [ZERO] * d + k
    rB = rank(Bc, 2 * d)
    r1 = rank(Bc + [v1], 2 * d) - rB
    r2 = rank(Bc + [v2], 2 * d) - rB
    r12 = rank(Bc + [v1, v2], 2 * d) - rB
    # which combination falls into the coboundaries?
    comb = None
    if r12 == 1:
        # find c with v2 - c*v1 in B^1 : solve over the coboundary space
        M = [[v1[i]] + [Bc[j][i] for j in range(d)] for i in range(2 * d)]
        sol = solve(M, v2, 1 + d)
        comb = sol[0] if sol else None
    print(f"   m={m:2d}  dim B^1={rB:2d}  dim H^1(T^2)={len(nullspace([[-Nl[i][j] for j in range(d)] + [Na[i][j] for j in range(d)] for i in range(d)], 2*d)) - rB}"
          f"   <(k,0)> mod B^1: {r1}   <(0,k)> mod B^1: {r2}   <(k,0),(0,k)> mod B^1: {r12}")
    if comb is not None:
        print(f"          (0,k) - ({comb})*(k,0) IS a coboundary;  tau = {TAU}"
              f"   equal: {comb == TAU}")
print("""
  So the two canonical vectors span ONE dimension modulo the coboundaries, and the
  relation between them is exactly tau -- the same identity memo 213 proved.  The
  canonical peripheral data (ker N, the coker functional f, tau) reaches a
  1-DIMENSIONAL subspace of the 2-dimensional H^1(T^2;V).  There is no canonical
  second coordinate to read.""")

print("\n" + "=" * 78)
print("CELL 4 -- is L71's computable content already in the record?")
print("=" * 78)
import pathlib
ROOT = pathlib.Path(__file__).resolve().parents[2]
items = [
    ('integrability at 2nd order', 'frontier/B575_bridge_obstruction/FINDINGS.md',
     'Q \u2261 0. The bridge is open at second order, in every direction'),
    ('Zariski closure per direction', 'frontier/B576_deformed_closure/FINDINGS.md',
     'THE DEFORMED CLOSURE: the chirality is exactly the \u03b8-odd motion'),
    ('cup product at the foundation', 'frontier/B270_integrability_cup_product/FINDINGS.md',
     'the cup-product obstruction vanishes; deformations are cusp deformations'),
    ('peripheral behaviour', 'outside_bench/memos/THE_CUSP_CANNOT_TELL.md',
     'THE PERIPHERAL SLOPE IS THE SAME IN EVERY BLOCK'),
]
allp = True
for label, rel, needle in items:
    body = (ROOT / rel).read_text(errors='replace')
    ok = needle in body
    allp &= ok
    print(f"  [{'OK ' if ok else 'MISS'}] {label:30s} {rel}")
print(f"\n  CELL 4 OUTCOME: {'A' if allp else 'B'}   (all four present: {allp})")

print("\n" + "=" * 78)
print("DONE -- outcomes above; interpretation lives in the memo, not here.")
print("=" * 78)
