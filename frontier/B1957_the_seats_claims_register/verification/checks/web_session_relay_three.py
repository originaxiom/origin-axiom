"""B1957: the web seat's session relay of 2026-09-08, the lines main had only registered (its section 9.2 of
2026-11-18): 'the number 3 does two independent jobs', and the three steps of its route that are true.  On main's
own ground, exact.
 S1  det(A - 1) = 2 - tr A for every integer matrix of determinant 1 (an identity); over a box the matrices of finite
     order have orders 1, 2, 3, 4, 6 only; every one of order 3 has trace -1 and det(A - 1) = 3; the only one of order 2
     is -1, with det(A - 1) = 4; the fixed points on the torus counted directly are 3, 4, 2, 1 at orders 3, 2, 4, 6.
 S2  the automorphisms of E6's Cartan matrix are exactly two, so the outer group has order 2 and an automorphism of
     order 3 has trivial image in it (it is inner); at order 2 the same argument concludes nothing.  Control: D4 has six.
 S3  minus the longest element of the Weyl group acts on E6's simple roots as the non-trivial automorphism (so -1 is
     not in W(E6)) and on F4's as the identity (so -1 is in W(F4) and every representation of F4 is self-dual).
 S4  the characteristic of an sl2 is fixed by that automorphism: for the regular sl2 of each of the 64 standard Levi
     subalgebras, the dominant conjugate of its h is symmetric (the reason: h and -h are conjugate).
 S5  the 27 restricted to the fixed subalgebra F4: its weights projected on the symmetric part of the Cartan are 24
     distinct non-zero vectors of one length and the zero vector three times: 26 + 1.
 The route's third step is false (web_session_relay_f4.py); 'three generations' and 'the reason they are chiral' are
 the programme's readings and are not computed here."""
import functools, itertools, math
from fractions import Fraction as Fr
from collections import Counter
import pathlib as _pl, sys as _sys
_sys.path.insert(0, str(_pl.Path(__file__).resolve().parent))          # the sibling below is found in isolated mode too (the web seat's section 9, 2026-11-18)
import web_session_relay_f4 as F4R
print = functools.partial(print, flush=True)
C = F4R.C


def cartan(edges, n, double=()):
    M = [[2 if i == j else 0 for j in range(n)] for i in range(n)]
    for i, j in edges: M[i][j] = M[j][i] = -1
    for i, j in double: M[i][j] = -2; M[j][i] = -1          # <a_i, a_j^vee> = -2: a_i is the long root
    return M


def autos(M):
    n = len(M); return [p for p in itertools.permutations(range(n)) if all(M[p[i]][p[j]] == M[i][j] for i in range(n) for j in range(n))]


def longest(M):
    """the images of the simple roots under the longest element, found greedily"""
    n = len(M); img = [tuple(int(i == j) for j in range(n)) for i in range(n)]; word = []
    while True:
        k = next((i for i in range(n) if all(c >= 0 for c in img[i])), None)
        if k is None: return img, len(word)
        # w -> w s_k : the new images are w(s_k(a_j)) = w(a_j) - M[j][k] w(a_k)
        img = [tuple(img[j][t] - M[j][k] * img[k][t] for t in range(n)) for j in range(n)]; word.append(k)


def dominant(M, h):
    """the dominant conjugate of a coweight given by its values on the simple roots: reflect while a value is negative.
    s_i acts on the values by v_j -> v_j - M[i][j] v_i"""
    v = list(h)
    while True:
        k = next((i for i in range(len(v)) if v[i] < 0), None)
        if k is None: return tuple(v)
        v = [v[j] - M[k][j] * v[k] for j in range(len(v))]


if __name__ == "__main__":
    B = 6; orders = Counter(); tr3 = set(); d3 = set(); two = []; fix = {}
    def mul(X, Y): return ((X[0][0] * Y[0][0] + X[0][1] * Y[1][0], X[0][0] * Y[0][1] + X[0][1] * Y[1][1]), (X[1][0] * Y[0][0] + X[1][1] * Y[1][0], X[1][0] * Y[0][1] + X[1][1] * Y[1][1]))
    I2 = ((1, 0), (0, 1)); ident = True; n1 = 0
    for a, b, c, d in itertools.product(range(-B, B + 1), repeat=4):
        if a * d - b * c != 1: continue
        n1 += 1; A = ((a, b), (c, d)); dA = (a - 1) * (d - 1) - b * c; ident &= dA == 2 - (a + d)
        P = A; o = None
        for k in range(1, 13):
            if P == I2: o = k; break
            P = mul(P, A)
        if o is None: continue
        orders[o] += 1
        if o == 3: tr3.add(a + d); d3.add(dA)
        if o == 2: two.append((A, dA))
        if o in (2, 3, 4, 6):
            N = 12; cnt = sum(1 for x in range(N) for y in range(N) if ((a - 1) * x + b * y) % N == 0 and (c * x + (d - 1) * y) % N == 0); fix.setdefault(o, set()).add(cnt)
    print("S1: %d integer matrices of determinant 1 with entries to %d; det(A - 1) = 2 - tr A on all: %s; finite orders found: %s; at order 3 the traces are %s and det(A - 1) is %s; of order 2: %s; fixed points on the torus by order: %s" % (
        n1, B, ident, dict(sorted(orders.items())), sorted(tr3), sorted(d3), two, {k: sorted(v) for k, v in sorted(fix.items())}))
    D4 = cartan([(0, 1), (1, 2), (1, 3)], 4); F4 = cartan([(0, 1), (2, 3)], 4, double=[(1, 2)]); aE = autos(C)
    print("S2: automorphisms of the Cartan matrix: E6 %d %s, so the image of an element of order 3 in the outer group has order dividing gcd(3, %d) = %d; at order 2, gcd(2, %d) = %d; control D4: %d automorphisms, gcd(3, %d) = %d; F4: %d" % (
        len(aE), aE, len(aE), math.gcd(3, len(aE)), len(aE), math.gcd(2, len(aE)), len(autos(D4)), len(autos(D4)), math.gcd(3, len(autos(D4))), len(autos(F4))))
    out = {}
    for name, M in (("E6", C), ("F4", F4), ("D4", D4)):
        img, ln = longest(M); n = len(M); perm = []
        for i in range(n):
            neg = tuple(-x for x in img[i]); assert sorted(neg) == [0] * (n - 1) + [1]; perm.append(neg.index(1))
        out[name] = (ln, tuple(perm))
    print("S3: the longest element (its length, and the permutation of the simple roots given by its negative): %s; for E6 that permutation is the non-trivial automorphism: %s" % (out, out["E6"][1] == [p for p in aE if p != tuple(range(6))][0]))
    sigma = out["E6"][1]; diagrams = set(); sym = True
    for r in range(7):
        for S in itertools.combinations(range(6), r):
            if not S: continue
            sub = [[C[i][j] for j in S] for i in S]; inv = F4R.inverse(sub)
            coef = [2 * sum(inv[a][b] for b in range(len(S))) for a in range(len(S))]            # h = sum of coef_a a_a^vee, with a_i(h) = 2 on the subset
            h = [sum(coef[a] * C[S[a]][j] for a in range(len(S))) for j in range(6)]               # the values a_j(h) = sum coef_a <a_j, a_a^vee>
            assert all(h[i] == 2 for i in S); dom = dominant(C, h); diagrams.add(dom); sym &= tuple(dom[sigma[i]] for i in range(6)) == dom
    print("S4: the regular sl2 of the 63 non-empty standard Levi subalgebras of E6: %d distinct characteristics, every one fixed by the automorphism: %s; the largest is %s" % (len(diagrams), sym, tuple(int(x) for x in max(diagrams))))
    t = ((1j, 0), (0, -1j)); e = ((0, 1), (0, 0)); te = tuple(tuple(sum(t[i][k] * e[k][l] * (t[l][j].conjugate()) for k in range(2) for l in range(2)) for j in range(2)) for i in range(2))
    print("S4: in SL(2) the torus element diag(i, -i) carries e to %s e, so e and -e are conjugate, and the Weyl element carries h to -h" % int(te[0][1].real))
    Ci = F4R.inverse(C); w27 = F4R.weights((1, 0, 0, 0, 0, 0))
    # a weight with Dynkin labels w is sum_i (w C^-1)_i a_i; the automorphism permutes the labels; the symmetric part is (w + sigma w)/2
    proj = [tuple(Fr(w[i] + w[sigma[i]], 2) for i in range(6)) for w in w27]; norm = lambda v: sum(v[i] * Ci[i][j] * v[j] for i in range(6) for j in range(6))
    cnt = Counter(proj); zero = cnt.pop(tuple(Fr(0) for _ in range(6)), 0)
    print("S5: the 27's weights projected on the symmetric part: %d distinct non-zero vectors, each %s time(s), of squared lengths %s; the zero vector %d times: 24 + 2 for the 26, and 1" % (len(cnt), sorted(set(cnt.values())), sorted({str(norm(v)) for v in cnt}), zero))
