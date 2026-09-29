"""
idx.py -- the 3D index of a 1-cusped ideal triangulation on an ARBITRARY boundary class,
computed from SnapPy's own edge AND cusp rows, in exact integer arithmetic on x = q^{1/2}.

THE GLUING RULE (derived here, not assumed; see probe2.py and step10_validate.py)
--------------------------------------------------------------------------------
Let E_1..E_N be the edge rows and Mr, Ln the meridian / longitude rows of
M.gluing_equations(form='log') (each of length 3N; slot (j,t), t indexing the three
pairs of opposite edges of tetrahedron j in snappy's (z,z',z'') order).

For a boundary class  gamma = x*mu + y*lambda  put the slot weights

        W_gamma(k)[j,t] = sum_i k_i E_i[3j+t]  -  ( x*Mr[3j+t] + y*Ln[3j+t] )

and

        I_T(gamma)(q) = sum_{k in Z^N, k_{i0}=0} q^{sum_i k_i}  prod_j J_D(W[j,0],W[j,1],W[j,2])
        J_D(a,b,c) = (-q^{1/2})^{-b} I^G(b-c, a-b),     I^G(m,e) = I_Delta(e,m)   [Garoufalidis conv.]

At gamma=0 this is exactly step7_fixed_gluing.index_zero.  Matching GHRS's hand-written
m004 formula  I_T(x mu + y lam) = sum_k q^k J(2k,k,x) J(2k-x+2y,k,-2y)  against snappy's rows
gives  v(mu) = -Mr  EXACTLY and  v(lam) = -Ln + (E_0 - E_1); adding an edge row to the
boundary vector multiplies the index by q^{-1} (proved + checked numerically in
step10_validate.py), so +E_0-E_1 is a no-op and the rule above is GHRS's rule.

x, y may be half-integers whenever x*Mr + y*Ln stays INTEGRAL (the saturation of the
row span) -- that is how GHRS's four half-integer classes of m004 arise (y = 1/2).

TRUNCATION: per-factor, using the exact minimal degree (Lemma 3.6 of arXiv:1208.1663).
Uniform truncation is WRONG here -- see step7_fixed_gluing.py's docstring.
"""
import itertools
from fractions import Fraction
import snappy
from tet_index import I_delta, s_str, s_mul, s_add, s_shift, s_trunc, s_eq, sgn


def delta_x(m, e):
    p = lambda t: max(0, t)
    return p(m) * p(m + e) + p(-m) * p(e) + p(-e) * p(-e - m) + max(0, m, -e)


def J_mindeg(a, b, c):
    return -b + delta_x(b - c, a - b)


def J_normalised(a, b, c, budget):
    """F = x^{-d} J_D(a,b,c) through x^{budget}; minimal degree 0."""
    d = J_mindeg(a, b, c)
    sh = -b - d
    s = I_delta(a - b, b - c, budget - sh)      # I^G(m,e) = I_delta(e,m)
    return {k + sh: sgn(b) * v for k, v in s.items() if k + sh <= budget}


_ROWS = {}
def rows(name, mfd=None):
    """(n, r, edge rows, meridian rows, longitude rows) from snappy."""
    key = name if mfd is None else id(mfd)
    if key in _ROWS:
        return _ROWS[key]
    M = snappy.Manifold(name) if mfd is None else mfd
    n, r = M.num_tetrahedra(), M.num_cusps()
    G = [list(map(int, row)) for row in M.gluing_equations(form='log')]
    assert len(G) == n + 2 * r
    E = G[:n]
    Mr = [G[n + 2 * c] for c in range(r)]
    Ln = [G[n + 2 * c + 1] for c in range(r)]
    cs = [sum(row[c] for row in E) for c in range(3 * n)]
    assert set(cs) == {2}, f"edge column sums {cs}"
    out = (M, n, r, E, Mr, Ln)
    _ROWS[key] = out
    return out


def bdry_vector(n, Mr, Ln, cls):
    """cls = list of (x,y) per cusp, Fractions allowed.  v = -sum_c (x_c Mr_c + y_c Ln_c).
       Raises unless v is integral."""
    v = [Fraction(0)] * (3 * n)
    for c, (x, y) in enumerate(cls):
        for s in range(3 * n):
            v[s] -= Fraction(x) * Mr[c][s] + Fraction(y) * Ln[c][s]
    out = []
    for t in v:
        assert t.denominator == 1, f"non-integral boundary vector {v}"
        out.append(int(t))
    return out


def triples(E, n, k, v, order=(0, 1, 2)):
    out = []
    for j in range(n):
        t = [sum(k[i] * E[i][3 * j + s] for i in range(n)) + v[3 * j + s] for s in range(3)]
        out.append((t[order[0]], t[order[1]], t[order[2]]))
    return out


def index_class(name, cls=((0, 0),), Xmax=30, zero_edges=None, order=(0, 1, 2),
                box=None, mfd=None, verbose=False):
    M, n, r, E, Mr, Ln = rows(name, mfd)
    if not isinstance(cls[0], (tuple, list)):
        cls = (cls,)
    assert len(cls) == r
    v = bdry_vector(n, Mr, Ln, cls)
    if zero_edges is None:
        zero_edges = list(range(r))              # gauge: r of the k_i set to 0
    free = [i for i in range(n) if i not in zero_edges]
    rank = len(free)
    if box is None:
        box = {0: 1, 1: 400, 2: 70, 3: 30, 4: 18, 5: 13, 6: 10}[rank]
    keep, maxabs = [], 0
    for kk in itertools.product(range(-box, box + 1), repeat=rank):
        k = [0] * n
        for idx, i in enumerate(free):
            k[i] = kk[idx]
        D = 2 * sum(k) + sum(J_mindeg(*t) for t in triples(E, n, k, v, order))
        if D <= Xmax:
            keep.append((tuple(k), D))
            maxabs = max(maxabs, max((abs(t) for t in kk), default=0))
    assert box - maxabs >= max(2, box // 4), f"widen box: outermost |k|={maxabs}, box={box}"
    tot = {}
    for k, D in keep:
        budget = Xmax - D
        prod = {0: 1}
        for t in triples(E, n, list(k), v, order):
            prod = s_mul(prod, J_normalised(*t, budget=budget), budget)
        tot = s_add(tot, s_shift(prod, D, Xmax))
    if verbose:
        print(f"      {len(keep)} pts, outermost |k|={maxabs}/{box}")
    return tot
