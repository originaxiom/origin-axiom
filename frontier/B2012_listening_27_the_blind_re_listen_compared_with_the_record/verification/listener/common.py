# common.py -- shared helpers
from fractions import Fraction as Fr

class QD:
    """element a + b*sqrt(d) of Q(sqrt d), exact"""
    __slots__ = ('a', 'b', 'd')
    def __init__(self, a, b=0, d=2):
        self.a = Fr(a); self.b = Fr(b); self.d = d
    def __add__(s, o):
        o = s._c(o); return QD(s.a+o.a, s.b+o.b, s.d)
    __radd__ = __add__
    def __sub__(s, o):
        o = s._c(o); return QD(s.a-o.a, s.b-o.b, s.d)
    def __rsub__(s, o):
        o = s._c(o); return QD(o.a-s.a, o.b-s.b, s.d)
    def __neg__(s): return QD(-s.a, -s.b, s.d)
    def __mul__(s, o):
        o = s._c(o); return QD(s.a*o.a + s.d*s.b*o.b, s.a*o.b + s.b*o.a, s.d)
    __rmul__ = __mul__
    def _c(s, o): return o if isinstance(o, QD) else QD(o, 0, s.d)
    def __eq__(s, o): o = s._c(o); return s.a == o.a and s.b == o.b
    def __hash__(s): return hash((s.a, s.b))
    def __repr__(s):
        if s.b == 0: return str(s.a)
        return "(%s%+s*r%d)" % (s.a, s.b, s.d)
    def conj(s): return QD(s.a, -s.b, s.d)
    def __float__(s): return float(s.a) + float(s.b)*s.d**0.5

def mL(p):  x, y, z = p; return (x, z, x*z - y)
def mR(p):  x, y, z = p; return (z, y, y*z - x)
def mLi(p): x, y, z = p; return (x, x*y - z, y)
def mRi(p): x, y, z = p; return (x*y - z, y, x)
MOVES = (mL, mR, mLi, mRi)

def orbit(p0, moves=MOVES, cap=10**6):
    idx = {p0: 0}; pts = [p0]; i = 0
    while i < len(pts):
        p = pts[i]; i += 1
        for f in moves:
            q = f(p)
            if q not in idx:
                idx[q] = len(pts); pts.append(q)
                if len(pts) > cap: return None, None
    return pts, idx

def perms(pts, idx, moves=(mL, mR)):
    return [[idx[f(p)] for p in pts] for f in moves]

def gap_group_info(permlist, n):
    """returns (order, structure description, is transitive) using GAP via sage's libgap"""
    from sage.all import libgap
    gens = [libgap.PermList([i+1 for i in pm]) for pm in permlist]
    G = libgap.Group(gens)
    o = G.Size()
    try:
        sd = G.StructureDescription() if int(o) < 10**7 else "large"
    except Exception as e:
        sd = "?"
    return int(o), str(sd)

def T_matrix(permlist, n):
    """T = sum over generators g of push-forward g_* + (g^-1)_*. As a matrix acting on functions f:
       (g_* f)(q) = sum_{p: g(p)=q} f(p); for a permutation, (g_* f)(q) = f(g^{-1} q). T is symmetric."""
    import numpy as np
    M = np.zeros((n, n), dtype=np.int64)
    for pm in permlist:
        for p, q in enumerate(pm):
            M[q, p] += 1   # g_*
            M[p, q] += 1   # (g^-1)_*
    return M

def charpoly_factor(M):
    n = M.shape[0]
    try:
        import flint
        A = flint.fmpz_mat(n, n, [int(v) for v in M.ravel()])
        cp = A.charpoly()
        c, facs = cp.factor()
        return cp, facs
    except ImportError:
        from sage.all import matrix, ZZ
        A = matrix(ZZ, n, n, [int(v) for v in M.ravel()])
        cp = A.charpoly()
        return cp, list(cp.factor())
