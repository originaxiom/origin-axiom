"""B1957: the web seat's foundations card W-F8 (three distinctions against n), on main's own code.  Data-free.
W_n = the free product of n involutions s_1 .. s_n; the puncture p = s_1 ... s_n; the records E_n = the even part, free on
x_i = s_i s_(i+1).  A Hurwitz move h_i: s_i -> s_i s_(i+1) s_i, s_(i+1) -> s_i (it keeps p).  H_n = h_1 h_2^-1 h_3 ...
 T1  every h_i and its inverse keeps p as a reduced word, and acts on H_1(E_n) by an integer matrix of determinant +-1.
 T2  the class in H_1(E_n) of the puncture's lift: p^2 for odd n, p for even n.
 T3  the matrix of H_n on H_1(E_n), its characteristic polynomial (exact) and its spectral radius, n = 2 to 8; the matrix
     of h_1 h_2^-1 for every n >= 3 on span(x_1, x_2) and on the quotient.
 T4  the Euler characteristics: chi(W_n) = 1 - n/2, so E_n has rank n - 1; genus and cusps of the cover."""
import functools
from fractions import Fraction as Fr
import sympy as sp
print = functools.partial(print, flush=True)
red = lambda w: functools.reduce(lambda s, c: s[:-1] if s and s[-1] == c else s + (c,), w, ())


def hurwitz(i, n, inverse=False):
    """the substitution on letters 1..n (i from 1): s_i -> s_i s_(i+1) s_i, s_(i+1) -> s_i; the inverse: s_i -> s_(i+1), s_(i+1) -> s_(i+1) s_i s_(i+1)"""
    f = {k: (k,) for k in range(1, n + 1)}
    if not inverse: f[i] = (i, i + 1, i); f[i + 1] = (i,)
    else: f[i] = (i + 1,); f[i + 1] = (i + 1, i, i + 1)
    return f
img = lambda f, w: red(sum((f[c] for c in w), ()))
comp = lambda f, g: {k: img(f, g[k]) for k in g}                         # g first, then f
def cls(w, n):                                                           # the class of an even word in H_1(E_n), basis x_1 .. x_(n-1): letter s_j carries v_j = e_j + ... + e_(n-1), signs alternate
    v = [0] * (n - 1); s = 1
    for c in w:
        for k in range(c - 1, n - 1): v[k] += s
        s = -s
    return v
def matrix(f, n): return sp.Matrix([cls(img(f, (i, i + 1)), n) for i in range(1, n)]).T

if __name__ == "__main__":
    lam = sp.symbols("lam"); rows = []
    for n in range(2, 9):
        p = tuple(range(1, n + 1)); keep = True; unim = True
        for i in range(1, n):
            for invs in (False, True):
                h = hurwitz(i, n, invs); keep &= img(h, p) == p; unim &= abs(matrix(h, n).det()) == 1
            keep &= comp(hurwitz(i, n), hurwitz(i, n, True)) == {k: (k,) for k in range(1, n + 1)}
        H = functools.reduce(comp, [hurwitz(i, n, inverse=(i % 2 == 0)) for i in range(1, n)]); M = matrix(H, n)
        cp = sp.factor(M.charpoly(lam).as_expr()); rad = max(abs(complex(r)) for r in sp.Poly(M.charpoly(lam).as_expr(), lam).nroots(n=20))
        lift = p + p if n % 2 else p; rows.append((n, keep, unim, cls(lift, n), M.tolist() if n == 3 else None, cp, rad))
        print("n = %d: every move and its inverse keeps p: %s, acts by a matrix of determinant +-1: %s; records: rank %d; the puncture's lift (%s) has class %s; H_n's characteristic polynomial %s; spectral radius %.6f%s" % (
            n, keep, unim, n - 1, "p^2, one cusp" if n % 2 else "p, two cusps", cls(lift, n), cp, rad, "; its matrix %s" % M.tolist() if n == 3 else ""))
    print("the seat's radii: 1, 2.618034, 3.732051, 4.390257, 4.791288, 5.048917 for n = 2 to 7; main's: %s" % ", ".join("%.6f" % r[6] for r in rows[:6]))
    for n in (4, 5, 6):
        f = comp(hurwitz(1, n), hurwitz(2, n, True)); M = matrix(f, n)
        print("h_1 h_2^-1 at n = %d: on span(x_1, x_2) %s; x_3 -> %s; x_k fixed for k >= 4: %s" % (n, M[:2, :2].tolist(), list(M[:, 2]), all(list(M[:, k]) == [int(j == k) for j in range(n - 1)] for k in range(3, n - 1))))
    print("T4: chi(W_n) = n/2 - (n - 1) = 1 - n/2: %s for n = 2 to 7; the index-2 cover has chi = 2 - n, free of rank n - 1; with one cusp (odd n) its genus is (n - 1)/2, with two (even n) it is (n - 2)/2: %s" % (
        [str(Fr(n, 2) - (n - 1)) for n in range(2, 8)], [(n, (n - 1) // 2 if n % 2 else (n - 2) // 2, all((2 - 2 * g - c == 2 - n) for g, c in [(((n - 1) // 2), 1) if n % 2 else (((n - 2) // 2), 2)])) for n in range(2, 8)]))
