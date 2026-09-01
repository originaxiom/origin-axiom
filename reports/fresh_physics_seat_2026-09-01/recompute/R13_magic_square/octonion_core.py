"""R13 blind recomputation — my own split octonions, split binarions, triality algebras.

Everything exact over Q (fractions.Fraction). Written BEFORE opening any B904 stage
script. Conventions are my own; B904's conventions were not consulted.

Zorn vector-matrix split octonions:
  element = (a, v1,v2,v3, w1,w2,w3, b)  <->  [[a, v],[w, b]]
  product  [[a1,v1],[w1,b1]] * [[a2,v2],[w2,b2]] =
     [[a1*a2 + v1.w2,          a1*v2 + b2*v1 + CR*(w1 x w2)],
      [a2*w1 + b1*w2 + CR2*(v1 x v2),   b1*b2 + w1.v2]]
  with CR/CR2 sign choices fixed by demanding norm multiplicativity + alternativity,
  N(x) = a*b - v.w, conj(x) = (b, -v, -w, a).
"""
from fractions import Fraction as F
import itertools

DIM_O = 8

def _dot(p, q):
    return sum(x * y for x, y in zip(p, q))

def _cross(p, q):
    return (p[1] * q[2] - p[2] * q[1],
            p[2] * q[0] - p[0] * q[2],
            p[0] * q[1] - p[1] * q[0])

# sign choices for the two cross terms; validated in selftest below
CR = -1   # sign on w1 x w2 term (upper right)
CR2 = 1   # sign on v1 x v2 term (lower left)

def omul(x, y):
    a1, b1 = x[0], x[7]
    v1, w1 = x[1:4], x[4:7]
    a2, b2 = y[0], y[7]
    v2, w2 = y[1:4], y[4:7]
    cw = _cross(w1, w2)
    cv = _cross(v1, v2)
    a = a1 * a2 + _dot(v1, w2)
    v = tuple(a1 * v2[i] + b2 * v1[i] + CR * cw[i] for i in range(3))
    w = tuple(a2 * w1[i] + b1 * w2[i] + CR2 * cv[i] for i in range(3))
    b = b1 * b2 + _dot(w1, v2)
    return (a,) + v + w + (b,)

def oconj(x):
    return (x[7],) + tuple(-c for c in x[1:7]) + (x[0],)

def onorm(x):
    return x[0] * x[7] - _dot(x[1:4], x[4:7])

def opolar(x, y):
    # <x,y> with <x,x> = 2 N(x)
    return onorm(tuple(a + b for a, b in zip(x, y))) - onorm(x) - onorm(y)

OBASIS = [tuple(F(1) if i == k else F(0) for i in range(8)) for k in range(8)]
O_ONE = tuple(F(1) if i in (0, 7) else F(0) for i in range(8))

# mult table: OMT[i][j] = vector of omul(e_i, e_j)
OMT = [[omul(OBASIS[i], OBASIS[j]) for j in range(8)] for i in range(8)]
# polar form matrix
OPOL = [[opolar(OBASIS[i], OBASIS[j]) for j in range(8)] for i in range(8)]

# ---------------- split binarions C' = Q[j], j^2 = +1 ----------------
def cmul(z, w):
    return (z[0] * w[0] + z[1] * w[1], z[0] * w[1] + z[1] * w[0])

def cconj(z):
    return (z[0], -z[1])

def cnorm(z):
    return z[0] * z[0] - z[1] * z[1]

def cpolar(z, w):
    return cnorm((z[0] + w[0], z[1] + w[1])) - cnorm(z) - cnorm(w)

CBASIS = [(F(1), F(0)), (F(0), F(1))]
CMT = [[cmul(CBASIS[i], CBASIS[j]) for j in range(2)] for i in range(2)]
CPOL = [[cpolar(CBASIS[i], CBASIS[j]) for j in range(2)] for i in range(2)]


def selftest():
    import random
    random.seed(1)
    def rnd():
        return tuple(F(random.randint(-4, 4)) for _ in range(8))
    ok = True
    for _ in range(200):
        x, y = rnd(), rnd()
        # norm multiplicativity
        if onorm(omul(x, y)) != onorm(x) * onorm(y):
            ok = False; print("NORM MULT FAIL"); break
        # alternativity: x(xy) = (xx)y ; (yx)x = y(xx)
        if omul(x, omul(x, y)) != omul(omul(x, x), y):
            ok = False; print("LEFT ALT FAIL"); break
        if omul(omul(y, x), x) != omul(y, omul(x, x)):
            ok = False; print("RIGHT ALT FAIL"); break
        # conj: x*conj(x) = N(x) 1
        xn = omul(x, oconj(x))
        if xn != tuple(onorm(x) * c for c in O_ONE):
            ok = False; print("CONJ FAIL"); break
    # non-associativity witness (must NOT be associative)
    assoc = True
    for _ in range(50):
        x, y, z = rnd(), rnd(), rnd()
        if omul(omul(x, y), z) != omul(x, omul(y, z)):
            assoc = False
            break
    if assoc:
        ok = False; print("ASSOCIATIVE?! not octonions")
    # split: norm form must be isotropic (obvious: e0 has N=0)
    if onorm(OBASIS[0]) != 0:
        ok = False; print("NOT SPLIT")
    # binarions
    for _ in range(50):
        z = (F(random.randint(-4, 4)), F(random.randint(-4, 4)))
        w = (F(random.randint(-4, 4)), F(random.randint(-4, 4)))
        if cnorm(cmul(z, w)) != cnorm(z) * cnorm(w):
            ok = False; print("C NORM FAIL"); break
    print("octonion/binarion selftest:", "PASS" if ok else "FAIL")
    return ok

if __name__ == "__main__":
    selftest()
