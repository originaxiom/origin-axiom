#!/usr/bin/env python3
"""A3 audit: exact Gieseking beat on the peripheral subgroup.

This is an independent, small exact check. All entries are in Q(q),
q^2-q+1=0, represented as pairs x+y*q. The peripheral longitude word is
the one found in twisted_double.py, stage 5. The matcher at the bottom is
exhaustive for the whole peripheral subgroup: it solves the normal-form
equations for arbitrary integers (r,s), rather than searching words up to
an unproved length cutoff.
"""
from fractions import Fraction as F

SOURCE_COMMIT = "15b3366937af19e643a54d564883253f013fc651"
SOURCE_SHA256 = {
    "gieseking_beat.py": "7b73758d9ce274bdc477ea7c877121bfdf01777dd2900a3e638602e7875c0a82",
    "twisted_double.py": "4a0fb415c7681e052681ab4c1a703d666751776d8fb883edf5ccda44a5cfeba6",
}

Z = (F(0), F(0)); O = (F(1), F(0)); Q = (F(0), F(1)); N = (F(-1), F(0))

def add(a, b): return (a[0] + b[0], a[1] + b[1])
def neg(a): return (-a[0], -a[1])
def sub(a, b): return add(a, neg(b))
def mul(a, b):
    # q^2=q-1
    return (a[0]*b[0] - a[1]*b[1],
            a[0]*b[1] + a[1]*b[0] + a[1]*b[1])
def inv(a):
    x, y = a
    # Norm(x+yq)=x^2+xy+y^2.
    n = x*x + x*y + y*y
    return ((x+y)/n, -y/n)
def bar(a):                         # q -> 1-q
    return (a[0] + a[1], -a[1])

def mm(A, B):
    return [[add(mul(A[i][0], B[0][j]), mul(A[i][1], B[1][j]))
             for j in range(2)] for i in range(2)]
def mi(A):
    d = sub(mul(A[0][0], A[1][1]), mul(A[0][1], A[1][0]))
    di = inv(d)
    return [[mul(di, A[1][1]), mul(di, neg(A[0][1]))],
            [mul(di, neg(A[1][0])), mul(di, A[0][0])]]
def mb(A): return [[bar(x) for x in row] for row in A]

I = [[O, Z], [Z, O]]
A = [[O, O], [Z, O]]
B = [[O, Z], [Q, O]]
Ai, Bi = mi(A), mi(B)
AB = {'a': A, 'A': Ai, 'b': B, 'B': Bi}

def wmat(word, gens=AB):
    out = I
    for c in word: out = mm(out, gens[c])
    return out

# Fiber generators and the stage-5 longitude from twisted_double.py.
x = mm(A, Bi); y = mm(Ai, B)
XF = {'x': x, 'X': mi(x), 'y': y, 'Y': mi(y)}
def fword(word): return wmat(word, XF)
lam_word = 'bABaaBAb'
mu = A
lam = wmat(lam_word)
assert mm(mu, lam) == mm(lam, mu)

# The first exact beat reported by gieseking_beat.py.
W = [[O, Q], [Z, O]]
assert sub(mul(W[0][0], W[1][1]), mul(W[0][1], W[1][0])) == O
def beat(g): return mm(mm(W, mb(g)), mi(W))

# The same exact W has the certificate's fiber action.  In the ordered
# basis ([x],[y]), columns are exponent sums of x,y in these words.
assert beat(x) == fword('xxy')
assert beat(y) == fword('YX')
fiber_beat = [[2, -1], [1, -1]]
fiber_tick = [[3, -1], [1, 0]]
assert [[fiber_beat[0][0]**2 + fiber_beat[0][1]*fiber_beat[1][0],
          fiber_beat[0][0]*fiber_beat[0][1] + fiber_beat[0][1]*fiber_beat[1][1]],
         [fiber_beat[1][0]*fiber_beat[0][0] + fiber_beat[1][1]*fiber_beat[1][0],
          fiber_beat[1][0]*fiber_beat[0][1] + fiber_beat[1][1]**2]] == fiber_tick

# Exact peripheral images, before any H_1 projection.
mu_image, lam_image = beat(mu), beat(lam)
assert mu_image == mu
assert lam_image == mi(lam)

# Normal form for every peripheral word mu^r lambda^s, r,s in Z. Since
# lambda = -I + c*N with N^2=0 and c=-2+4q, one has
#   mu^r lambda^s = ((-1)^s I) + ((-1)^s*(r-s*c))*N.
# Hence equality determines the parity of s, then q-coefficient forces s,
# and finally the rational coefficient forces r. This is an exhaustive
# matcher over Z^2, not a finite word-length search.
c = (-F(2), F(4))
def peripheral_normal_form(r, s):
    sign = O if s % 2 == 0 else N
    off = mul(sign, sub((F(r), F(0)), (F(s)*c[0], F(s)*c[1])))
    return [[sign, off], [Z, sign]]

def match_peripheral(T):
    """Return the unique (r,s) with T=mu^r lambda^s, or None.

    The diagonal must be +/-1, which fixes s parity. Writing the upper-right
    entry as u+v*q and comparing v gives s; comparing u then gives r.
    """
    d = T[0][0]
    if T[1][0] != Z or T[1][1] != d or d not in (O, N): return None
    parity = 0 if d == O else 1
    # off = sign*(r - s*c), c=(-2,4); q coefficient is sign*(-4*s).
    u, v = T[0][1]
    sign_int = 1 if parity == 0 else -1
    s_num = -v // (4 * sign_int)
    if v != F(-4 * sign_int * s_num) or s_num % 2 != parity: return None
    r_num = (u / sign_int) - 2*s_num
    if r_num.denominator != 1: return None
    r_int, s_int = int(r_num), int(s_num)
    return (r_int, s_int) if peripheral_normal_form(r_int, s_int) == T else None

assert match_peripheral(mu_image) == (1, 0)
assert match_peripheral(lam_image) == (0, -1)
assert peripheral_normal_form(1, 0) == mu
assert peripheral_normal_form(0, 1) == lam

# Induced H_1 action in ordered basis ([mu],[lambda]); columns are images.
H = [[1, 0], [0, -1]]
assert H[0][0]*H[1][1] - H[0][1]*H[1][0] == -1
assert H[0][0]**2 + H[0][1]*H[1][0] == 1
assert H[1][0]*H[0][1] + H[1][1]**2 == 1

print('mu = a')
print('source commit =', SOURCE_COMMIT)
print('source sha256 =', SOURCE_SHA256)
print('lambda =', lam_word)
print('lambda matrix =', lam)
print('W = [[1,q],[0,1]], det(W)=1')
print('W*bar(mu)*W^-1 = mu^1 lambda^0')
print('W*bar(lambda)*W^-1 = mu^0 lambda^-1')
print('peripheral H1 matrix (basis mu,lambda) = [[1,0],[0,-1]]')
print('det = -1; order = 2')
