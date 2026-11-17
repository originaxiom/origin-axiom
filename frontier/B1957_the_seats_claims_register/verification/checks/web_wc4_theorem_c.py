"""B1957: the web seat's W-C4 (the agy lane's Theorem C of 2026-11-07, which scopes B298's 'a multiplicity of 3 needs
a cubic structure'), recomputed by main in exact arithmetic over Q(omega).  Data-free.
 C1  V, the holonomy representation of m004 from Riley's generators x = [[1,1],[0,1]], y = [[1,0],[-omega,1]], is
     absolutely irreducible (I, x, y, xy span the 2 x 2 matrices), and the trace of xy is not real.
 C2  commutant dimensions: V^3 has 9, V^2 has 4, V + conj(V) has 2; (chi + conj chi)^3 has 18, chi(x) = chi(y) = omega.
 C3  the three non-zero classes of F_2^2 are one orbit of SL(2, F_2), a non-abelian group of order 6.
 C4  the prime above 3 in Q(sqrt -3) is ramified with residue field F_3; SL(2, F_3) has order 24 and 7 classes, and
     with three characters of degree 1 the only list of degrees is 1, 1, 1, 2, 2, 2, 3."""
import itertools
import sympy as sp
w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2
x = sp.Matrix([[1, 1], [0, 1]]); y = sp.Matrix([[1, 0], [-w, 1]]); cj = lambda M: M.applyfunc(sp.conjugate)


def commutant_dim(gens):
    """the dimension of the matrices commuting with every generator (each generator a square matrix)"""
    n = gens[0].shape[0]; X = sp.Matrix(n, n, sp.symbols("c0:%d" % (n * n))); eqs = []
    for g in gens: eqs += list((g * X - X * g).applyfunc(sp.expand))
    A = sp.Matrix([[sp.expand(e).coeff(s) for s in X] for e in eqs]); return n * n - A.applyfunc(sp.nsimplify).rank()


if __name__ == "__main__":
    span = sp.Matrix([list(M.applyfunc(sp.expand)) for M in (sp.eye(2), x, y, x * y)]).rank(); tr = sp.expand((x * y).trace())
    print("C1: I, x, y, xy span a space of dimension %d of the 2 x 2 matrices; tr(xy) = %s, imaginary part %s" % (span, tr, sp.im(tr)))
    d3 = commutant_dim([sp.diag(g, g, g) for g in (x, y)]); d2 = commutant_dim([sp.diag(g, g) for g in (x, y)]); dc = commutant_dim([sp.diag(g, cj(g)) for g in (x, y)])
    chi = sp.diag(w, sp.conjugate(w)); d18 = commutant_dim([sp.diag(chi, chi, chi)] * 2)
    print("C2: commutant dimensions: V + V + V: %d; V + V: %d; V + conj V: %d; (chi + conj chi) three times: %d" % (d3, d2, dc, d18))
    G2 = [sp.Matrix(2, 2, e) for e in itertools.product((0, 1), repeat=4) if (e[0] * e[3] - e[1] * e[2]) % 2 == 1]
    orbit = {tuple((g * sp.Matrix([1, 0])).applyfunc(lambda t: t % 2)) for g in G2}; ab = all((a * b - b * a).applyfunc(lambda t: t % 2) == sp.zeros(2, 2) for a in G2 for b in G2)
    print("C3: SL(2, F_2) has %d elements, abelian: %s; the orbit of (1, 0) has %d elements: all the non-zero classes" % (len(G2), ab, len(orbit)))
    G3 = [e for e in itertools.product(range(3), repeat=4) if (e[0] * e[3] - e[1] * e[2]) % 3 == 1]
    mul = lambda a, b: ((a[0] * b[0] + a[1] * b[2]) % 3, (a[0] * b[1] + a[1] * b[3]) % 3, (a[2] * b[0] + a[3] * b[2]) % 3, (a[2] * b[1] + a[3] * b[3]) % 3)
    inv = {a: next(b for b in G3 if mul(a, b) == (1, 0, 0, 1)) for a in G3}; classes = {frozenset(mul(mul(g, a), inv[g]) for g in G3) for a in G3}
    comm = {mul(mul(a, b), mul(inv[a], inv[b])) for a in G3 for b in G3}; sub = set(comm)
    while True:
        new = {mul(a, b) for a in sub for b in sub} | sub
        if new == sub: break
        sub = new
    lists = [c for c in itertools.combinations_with_replacement(range(1, 5), len(classes)) if sum(d * d for d in c) == len(G3) and c.count(1) == len(G3) // len(sub)]
    print("C4: x^2 + x + 1 = (x - 1)^2 mod 3, so 3 ramifies and the residue field is F_3; SL(2, F_3): order %d, %d classes, commutator subgroup of order %d (so %d characters of degree 1); lists of degrees with that many classes and squares summing to the order: %s" % (len(G3), len(classes), len(sub), len(G3) // len(sub), lists))
