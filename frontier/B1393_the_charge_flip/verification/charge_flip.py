#!/usr/bin/env python3
"""B1393 -- the charge flip: on cube~3.24's cuspidal Higgs twist, the charge-blind count against the charge-flip count, exactly.

The Higgs twist d + q*omega (omega harmonic in the cuspidal class v+) is gauge-equivalent to the flat real line bundle L_t with
monodromy g -> t^{v+(g)}, t = e^q; charge -q is L_{1/t} = L_t^*.  Everything below is Fox calculus on SnapPy's presentation of
pi_1(cube~3.24), exact over Q (python-flint) or over Z[t] (the determinantal divisor).

  A. the twisted numbers a_k = h^k(M; L_t), r_1 = rank(H^1(M; L_t) -> H^1(dM; L_t)), n = a_1 - r_1 (main's interior image, B1297),
     at rational t and 1/t; main's charge-blind index I = n(L_t) - n(L_{1/t}); the annihilator check r_1 + r_1* = t_1 = 8.
  B. where a_1 can jump: the generic rank of the Fox matrix over Q(t) and the gcd of its maximal-rank minors.  Its roots decide
     whether any real coupling is special.
  C. the lemma's two cases on one disc D in cusp 0: charge-flip nu = h^1(M, D; L_t) - h^1(M, dM - D; L_{1/t}) against
     -chi(M, D) = 1, and charge-blind nu = h^1(M, D; L_t) - h^1(M, D; L_{1/t}) = 0 (the relative groups by the pair sequences).
  D. second method: A on SnapPy's unsimplified presentation (49 generators), the same group through a different complex.
  E. the jump points themselves (primitive cube roots of unity, unitary order-3 twists along v+): a_1, r_1 there, over F_p for
     three primes p = 1 mod 3.
Usage: python3 charge_flip.py [A,B,C,D,E]   (default: all; about a minute)"""
import itertools
import sys
import time
import warnings
from fractions import Fraction as Fr
from pathlib import Path

warnings.filterwarnings("ignore")
import snappy
import sympy as sp
from flint import fmpq, fmpq_mat, fmpz_poly, nmod_mat

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
ISOSIG = (ROOT / "frontier" / "B1386_the_open_eisenstein_cusp" / "verification" / "cube3_24.isosig").read_text().strip()


class Pres:
    """a presentation as integer words (i > 0 a generator, -i its inverse), with the peripheral pairs"""

    def __init__(self, simplify=True):
        G = snappy.Manifold(ISOSIG).fundamental_group(simplify_presentation=simplify)
        self.n = len(G.generators())
        self.rels = [list(r) for r in G.relators(as_int_list=True)]
        self.per = [tuple(list(w) for w in pair) for pair in G.peripheral_curves(as_int_list=True)]
        self.m = len(self.rels)
        self.v = self._cuspidal_line()

    def expsum(self, word):
        e = [0] * self.n
        for x in word:
            e[abs(x) - 1] += 1 if x > 0 else -1
        return e

    def _cuspidal_line(self):
        H1 = sp.Matrix([self.expsum(r) for r in self.rels]).nullspace()
        B = sp.Matrix.hstack(*H1)
        P = sp.Matrix([self.expsum(w) for pair in self.per for w in pair])
        K = (P * B).nullspace()
        self.b1 = len(H1)
        assert len(K) == 1, "the cuspidal line is one-dimensional (B1386)"
        v = B * K[0]
        v = v * sp.ilcm(*[sp.fraction(x)[1] for x in v])
        g = sp.igcd(*[int(x) for x in v])
        v = [int(x) // g for x in v]
        return v if next(x for x in v if x) > 0 else [-x for x in v]

    # --- Fox calculus under g_i -> t^{v_i} ---
    def fox(self, word, t):
        """((d word / d g_i)(t))_i and the word's value, exact over Q (t a Fraction)"""
        T = fmpq(t.numerator, t.denominator)
        val = {i: (T ** self.v[i] if self.v[i] >= 0 else 1 / T ** (-self.v[i])) for i in range(self.n)}
        d = [fmpq(0)] * self.n
        pre = fmpq(1)
        for x in word:
            i = abs(x) - 1
            if x > 0:
                d[i] += pre
                pre = pre * val[i]
            else:
                pre = pre / val[i]
                d[i] -= pre
        return d, pre

    def fox_laurent(self, word):
        """(d word / d g_i) as Laurent polynomials {exponent: coefficient}"""
        d = [dict() for _ in range(self.n)]
        k = 0
        for x in word:
            i = abs(x) - 1
            if x > 0:
                d[i][k] = d[i].get(k, 0) + 1
                k += self.v[i]
            else:
                k -= self.v[i]
                d[i][k] = d[i].get(k, 0) - 1
        return d

    def numbers(self, t):
        """a0, a1, a2, r1, n = a1 - r1 for L_t, t a positive rational != 1"""
        J = fmpq_mat(self.m, self.n, [x for r in self.rels for x in self.fox(r, t)[0]])
        rJ = J.rank()
        a0, a1, a2 = 0, self.n - rJ - 1, self.m - rJ
        num, _ = J.numer_denom()
        X, nullity = num.nullspace()
        assert nullity == self.n - rJ
        Z = fmpq_mat(self.n, nullity, [X[i, j] for i in range(self.n) for j in range(nullity)])
        rows = []
        for pair in self.per:
            for w in pair:
                d, val = self.fox(w, t)
                assert val == 1, "L_t is trivial on every peripheral curve (v+ is cuspidal)"
                rows += d
        r1 = (fmpq_mat(len(rows) // self.n, self.n, rows) * Z).rank()
        return dict(a0=a0, a1=a1, a2=a2, euler=a0 - a1 + a2, r1=r1, n=a1 - r1, t1=2 * len(self.per))


def part_A(P, ts=(Fr(2), Fr(3), Fr(5), Fr(3, 2), Fr(7, 3), Fr(11, 4)), label="A."):
    print(f"{label} cube~3.24: presentation with {P.n} generators, {P.m} relators; b1 = {P.b1}; cuspidal line v+ = {P.v}")
    out = []
    for t in ts:
        x, y = P.numbers(t), P.numbers(1 / t)
        assert x["euler"] == 0 and y["euler"] == 0, "chi(M; L) = chi(M) = 0"
        assert x["r1"] + y["r1"] == x["t1"], "annihilator property r1 + r1* = t1 (B1297)"
        I = x["n"] - y["n"]
        out.append((t, x, y, I))
        print(f"   t = {str(t):>5}: a1 = {x['a1']}, a2 = {x['a2']}, r1 = {x['r1']}, n = {x['n']} | 1/t: a1 = {y['a1']}, r1 = {y['r1']}, "
              f"n = {y['n']} | r1 + r1* = {x['r1'] + y['r1']} = t1 | I = n - n* = {I}")
    assert all(I == 0 for *_, I in out)
    return out


def part_B(P):
    rows = [P.fox_laurent(r) for r in P.rels]
    lo = min(min(e) for row in rows for e in row if e)
    J = [[fmpz_poly([e.get(j + lo, 0) for j in range(max(e) - lo + 1)]) if e else fmpz_poly([]) for e in row] for row in rows]
    # generic rank: at a random rational point (a lower bound that the minors below confirm)
    tt = Fr(7919 * 104729 + 3, 7907 * 104723 + 1)
    def ev(p):
        x = Fr(0)
        for a in reversed(p.coeffs()):
            x = x * tt + int(a)
        return x
    r = fmpq_mat(P.m, P.n, [fmpq(ev(J[i][j]).numerator, ev(J[i][j]).denominator) for i in range(P.m) for j in range(P.n)]).rank()

    def det(Mx):
        if len(Mx) == 1:
            return Mx[0][0]
        return sum(((-1) ** j) * Mx[0][j] * det([row[:j] + row[j + 1:] for row in Mx[1:]]) for j in range(len(Mx)))
    g = fmpz_poly([])
    count = 0
    for R in itertools.combinations(range(P.m), r):
        for Cc in itertools.combinations(range(P.n), r):
            d = det([[J[i][j] for j in Cc] for i in R])
            count += 1
            if d != 0:
                g = d if g == 0 else g.gcd(d)
    # no (r+1)-minor is non-zero: the rank over Q(t) is exactly r
    assert all(det([[J[i][j] for j in Cc] for i in R]) == 0
               for R in itertools.combinations(range(P.m), r + 1) for Cc in itertools.combinations(range(P.n), r + 1))
    c = list(g.coeffs())
    while c and c[0] == 0:
        c = c[1:]
    g = fmpz_poly(c)
    fac = g.factor()
    print(f"B. the Fox matrix has rank {r} over Q(t) (every {r + 1}-minor vanishes identically), so a1 = {P.n - r - 1} generically;")
    print(f"   the gcd of its {count} maximal-rank minors, up to units t^k: {g} = {fac}")
    x = sp.Symbol("x")
    real_pos = [z for z in sp.Poly(sp.sympify(str(g).replace("^", "**")), x).real_roots() if z > 0]
    print(f"   its real roots, exactly: {sp.Poly(sp.sympify(str(g).replace('^', '**')), x).real_roots()}; positive ones: {real_pos} -- "
          f"so no real coupling q != 0 (t = e^q) is a jump point")
    return r, g, fac, real_pos


def rel_h1_disc(x):
    """h^1(M, D; L) for a disc D in one cusp torus, from the pair sequence: H^0(M;L) = 0 -> H^0(D) = Q -> H^1(M, D) -> H^1(M) -> H^1(D) = 0"""
    return 1 + x["a1"]


def rel_h1_complement(x):
    """h^1(M, dM - D; L): B = dM - D has 4 components (L trivial on each), H^1(B; L) = H^1(dM; L) (a torus minus a disc keeps H^1),
    so the pair sequence gives h^1(M, B) = h^0(B) + dim ker(H^1(M; L) -> H^1(dM; L)) = 4 + n"""
    return 4 + x["n"]


def part_C(P, t=Fr(2)):
    x, y = P.numbers(t), P.numbers(1 / t)
    flip = rel_h1_disc(x) - rel_h1_complement(y)
    blind = rel_h1_disc(x) - rel_h1_disc(y)
    chi_MD = 0 - 1
    print(f"C. one disc D in cusp 0, t = {t}: charge-flip nu = h^1(M, D; L_t) - h^1(M, dM - D; L_1/t) = {rel_h1_disc(x)} - "
          f"{rel_h1_complement(y)} = {flip} (lemma: -chi(M, D) = {-chi_MD}); charge-blind nu = h^1(M, D; L_t) - h^1(M, D; L_1/t) = "
          f"{rel_h1_disc(x)} - {rel_h1_disc(y)} = {blind}")
    assert flip == -chi_MD and blind == 0
    return flip, blind


def part_D():
    Q = Pres(simplify=False)
    print(f"D. second method, SnapPy's unsimplified presentation ({Q.n} generators, {Q.m} relators; b1 = {Q.b1}):")
    return part_A(Q, ts=(Fr(2), Fr(3, 2)), label="  ")


def part_E(P, primes=(7, 13, 19)):
    out = []
    for p in primes:
        w = next(a for a in range(2, p) if pow(a, 3, p) == 1)
        for tw in (w, pow(w, 2, p)):
            val = {i: pow(tw, P.v[i] % (p - 1), p) for i in range(P.n)}
            def fox_p(word):
                d = [0] * P.n
                pre = 1
                for x in word:
                    i = abs(x) - 1
                    if x > 0:
                        d[i] = (d[i] + pre) % p
                        pre = pre * val[i] % p
                    else:
                        pre = pre * pow(val[i], p - 2, p) % p
                        d[i] = (d[i] - pre) % p
                return d, pre
            J = nmod_mat(P.m, P.n, [x for r in P.rels for x in fox_p(r)[0]], p)
            rJ = J.rank()
            a1 = P.n - rJ - 1
            X, nullity = J.nullspace()
            Z = [[int(X[i, j]) for j in range(nullity)] for i in range(P.n)]
            rows = []
            for pair in P.per:
                for wd in pair:
                    d, val_w = fox_p(wd)
                    assert val_w == 1
                    rows.append(d)
            R = nmod_mat(len(rows), nullity, [sum(rows[k][i] * Z[i][j] for i in range(P.n)) % p for k in range(len(rows)) for j in range(nullity)], p)
            r1 = R.rank()
            out.append((p, tw, a1, r1))
    print("E. at the jump points, t a primitive cube root of unity (over F_p): " +
          "; ".join(f"p = {p}, t = {tw}: a1 = {a1}, r1 = {r1}, n = {a1 - r1}" for p, tw, a1, r1 in out))
    return out


if __name__ == "__main__":
    parts = sys.argv[1].split(",") if len(sys.argv) > 1 else ["A", "B", "C", "D", "E"]
    t0 = time.time()
    P = Pres()
    if "A" in parts:
        part_A(P)
    if "B" in parts:
        part_B(P)
    if "C" in parts:
        part_C(P)
    if "D" in parts:
        part_D()
    if "E" in parts:
        part_E(P)
    print(f"({time.time() - t0:.0f} s)")
