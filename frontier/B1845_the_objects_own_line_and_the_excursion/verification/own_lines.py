"""Data-free: B1733's rule applied to P-717's closed approximants A_k = L^5 R (LR)^k (and to LR): the larger Smith invariant of
A - I and A + I, and the order-5 lines A fixes up to sign (row vectors v with v(A -/+ I) = 0 mod 5), by their T-class."""
from sympy import Matrix
from sympy.matrices.normalforms import smith_normal_form
from sympy import ZZ
L = Matrix([[1,0],[1,1]]); R = Matrix([[1,1],[0,1]])
def word(s):
    M = Matrix.eye(2)
    for ch in s: M = M * (L if ch == 'L' else R)
    return M
def tclass(v):
    a, b = v
    if a % 5 == 0: return "a=0 (width 1)"
    return "slope %d/5 (width 5)" % min(a % 5, (-a) % 5)
def fixed5(A):
    out = []
    for sgn, B in (("+1", A - Matrix.eye(2)), ("-1", A + Matrix.eye(2))):
        for x in range(5):
            for y in range(5):
                if (x, y) == (0, 0): continue
                w = Matrix([[x, y]]) * B
                if all(int(e) % 5 == 0 for e in w): out.append(((x, y), sgn))
    seen = {}
    for v, s in out:
        key = min(v, ((-v[0]) % 5, (-v[1]) % 5)); seen[key] = s
    return seen
for name, A in [("LR", word("LR")), ("RL", word("RL"))] + [("L^5R(LR)^%d" % k, word("L"*5 + "R" + "LR"*k)) for k in range(0, 13)]:
    s1 = smith_normal_form(A - Matrix.eye(2), domain=ZZ); s2 = smith_normal_form(A + Matrix.eye(2), domain=ZZ)
    inv = (abs(s1[1,1]), abs(s2[1,1])); f = fixed5(A)
    print("%-14s tr %4d  Smith(A-I) %6d  Smith(A+I) %6d  order-5 lines fixed (up to sign): %s" % (
        name, A.trace(), inv[0], inv[1], {("(%d/5, %d/5)" % v): (s, tclass(v)) for v, s in f.items()} or "none"))
