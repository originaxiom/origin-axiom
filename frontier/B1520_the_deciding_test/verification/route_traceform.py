#!/usr/bin/env python3
"""B1520 route 2 (R2) -- conjugacy decided by traces alone, with own Laurent-polynomial arithmetic in q (no sympy, no linear solve).

The criterion (Theorem T, PREREGISTRATION section 2). Let A, B be representations of <m, n> in GL_4 over a field K, and
w_1 = (empty), w_2, ..., w_16 words with Gram matrix G_ij = tr A(w_i w_j) invertible. If
    tr B(w_i w_j) = tr A(w_i w_j)   and   tr B(w_i g w_j) = tr A(w_i g w_j)    (all i, j; g = m, n),
then A and B are conjugate over K. (The A(w_i) are a basis of M_4(K); the trace equalities make the B(w_i) a basis with the same
structure constants for right multiplication by A(g), B(g); the linear map A(w_i) -> B(w_i) is then an algebra automorphism of
M_4(K), inner by Skolem-Noether.) Here K = Q(q) and every entry is a Laurent polynomial in q, so each trace equality is an
identity of Laurent polynomials, checked exactly; det G is a Laurent polynomial with no positive real root (all coefficients
positive), so Theorem T applies over R at every single q0 > 0 as well. A single unequal trace (as Laurent polynomials) proves
non-conjugacy over Q(q). The exact conjugacy locus: at q0 > 0 the two are conjugate iff all 768 Theorem-T traces agree at q0 (if:
Theorem T at q0, G(q0) invertible; only if: traces are class functions), so the locus is the set of positive roots of the gcd of
all the nonzero differences (own polynomial gcd over Q; sympy only isolates the roots of that one exact polynomial).
Ballas' family is typed here from the paper (arXiv:1403.3314, p. 17, t = q/2). Shares no code with route 1 or B1512.
Usage: python3 route_traceform.py [--controls-only]"""
import json
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

HERE = Path(__file__).resolve().parent


class L:
    """a Laurent polynomial in q with rational coefficients: {exponent: coefficient}"""
    __slots__ = ("c",)

    def __init__(self, c=None):
        self.c = {e: F(v) for e, v in (c or {}).items() if v != 0}

    @staticmethod
    def const(v):
        return L({0: v})

    def __add__(self, o):
        d = dict(self.c)
        for e, v in o.c.items():
            d[e] = d.get(e, 0) + v
        return L(d)

    def __neg__(self):
        return L({e: -v for e, v in self.c.items()})

    def __sub__(self, o):
        return self + (-o)

    def __mul__(self, o):
        d = {}
        for e1, v1 in self.c.items():
            for e2, v2 in o.c.items():
                d[e1 + e2] = d.get(e1 + e2, 0) + v1 * v2
        return L(d)

    def scale(self, s):
        return L({e: v * s for e, v in self.c.items()})

    def recip(self):
        """q -> 1/q"""
        return L({-e: v for e, v in self.c.items()})

    def __eq__(self, o):
        return self.c == o.c

    def is_zero(self):
        return not self.c

    def at(self, x):
        return sum((v * F(x) ** e for e, v in self.c.items()), F(0))

    def __repr__(self):
        if not self.c:
            return "0"
        return " + ".join(f"({v})q^{e}" for e, v in sorted(self.c.items()))


ZERO, ONE = L(), L.const(1)
Q = L({1: 1})


def mat(rows):
    return [[x if isinstance(x, L) else L.const(x) for x in r] for r in rows]


def mmul(X, Y):
    return [[sum_l(X[i][k] * Y[k][j] for k in range(4)) for j in range(4)] for i in range(4)]


def sum_l(it):
    out = L()
    for x in it:
        out = out + x
    return out


def det3(M):
    return (M[0][0] * (M[1][1] * M[2][2] - M[1][2] * M[2][1]) - M[0][1] * (M[1][0] * M[2][2] - M[1][2] * M[2][0])
            + M[0][2] * (M[1][0] * M[2][1] - M[1][1] * M[2][0]))


def minor(M, i, j):
    return [[M[a][b] for b in range(4) if b != j] for a in range(4) if a != i]


def det4(M):
    return sum_l((M[0][j] * det3(minor(M, 0, j))).scale(-1 if j % 2 else 1) for j in range(4))


def inverse_det_one(M):
    """the adjugate; valid because det M = 1 (asserted)"""
    assert det4(M) == ONE, "determinant is not one"
    return [[det3(minor(M, j, i)).scale(-1 if (i + j) % 2 else 1) for j in range(4)] for i in range(4)]


def transpose(M):
    return [[M[j][i] for j in range(4)] for i in range(4)]


def trace_of_product(X, Y):
    return sum_l(X[i][k] * Y[k][i] for i in range(4) for k in range(4))


def ballas():
    half = F(1, 2)
    t = Q.scale(half)                                    # t = q/2
    inv_t = L({-1: 2})                                   # 1/t = 2/q
    m = mat([[1, 0, 1, t - ONE], [0, 1, 1, t], [0, 0, 1, t + L.const(half)], [0, 0, 0, 1]])
    n = mat([[1, 0, 0, 0], [L.const(2) + inv_t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return {"m": m, "n": n}


def recip_rep(rep):
    return {g: [[x.recip() for x in r] for r in M] for g, M in rep.items()}


class Rep:
    def __init__(self, gens):
        self.G = dict(gens)
        for g in ("m", "n"):
            self.G[g.upper()] = inverse_det_one(gens[g])
        self.cache = {"": mat([[1 if i == j else 0 for j in range(4)] for i in range(4)])}

    def word(self, w):
        if w in self.cache:
            return self.cache[w]
        X = mmul(self.word(w[:-1]), self.G[w[-1]])
        self.cache[w] = X
        return X

    def trace(self, w):
        X = self.word(w)
        return sum_l(X[i][i] for i in range(4))


def pulled_back(rep, sigma, dual):
    R = Rep(rep)
    out = {}
    for g in ("m", "n"):
        X = R.word(sigma[g])
        out[g] = transpose(inverse_det_one(X)) if dual else X
    return out


WORDS = ["", "m", "n", "M", "N", "mn", "nm", "mN", "Nm", "Mn", "nM", "mm", "nn", "MN", "NM", "mnm", "nmn", "mnM", "nmN",
         "MNm", "mmn", "nnm", "mnMN", "MNmn"]


def choose_basis(R, x0):
    """16 words whose matrices are independent at q = x0 (exact rationals), greedy from WORDS"""
    chosen, rows = [], []
    for w in WORDS:
        v = [e.at(x0) for row in R.word(w) for e in row]
        if rank_q(rows + [v]) > len(rows):
            chosen.append(w)
            rows.append(v)
        if len(chosen) == 16:
            break
    return chosen


def rank_q(rows):
    A = [list(r) for r in rows]
    rk, col = 0, 0
    ncol = len(A[0]) if A else 0
    while rk < len(A) and col < ncol:
        piv = next((i for i in range(rk, len(A)) if A[i][col] != 0), None)
        if piv is None:
            col += 1
            continue
        A[rk], A[piv] = A[piv], A[rk]
        for i in range(len(A)):
            if i != rk and A[i][col] != 0:
                f = A[i][col] / A[rk][col]
                A[i] = [a - f * b for a, b in zip(A[i], A[rk])]
        rk += 1
        col += 1
    return rk


def det_laurent(M):
    """determinant of a square matrix of Laurent polynomials, by fraction-free (Bareiss) elimination on q^k-shifted polynomials"""
    n = len(M)
    shift = max((max((-e for e in x.c), default=0) for row in M for x in row), default=0)
    P = [[{e + shift: v for e, v in x.c.items()} for x in row] for row in M]     # polynomials as dicts
    def pmul(a, b):
        d = {}
        for e1, v1 in a.items():
            for e2, v2 in b.items():
                d[e1 + e2] = d.get(e1 + e2, 0) + v1 * v2
        return {e: v for e, v in d.items() if v != 0}
    def psub(a, b):
        d = dict(a)
        for e, v in b.items():
            d[e] = d.get(e, 0) - v
        return {e: v for e, v in d.items() if v != 0}
    def pdiv(a, b):  # exact division of polynomials
        a = dict(a)
        qd = {}
        db = max(b)
        while a:
            da = max(a)
            if da < db:
                raise ArithmeticError("inexact division")
            c = a[da] / b[db]
            qd[da - db] = c
            a = psub(a, {e + da - db: c * v for e, v in b.items()})
        return qd
    sign, prev = 1, {0: F(1)}
    for k in range(n - 1):
        piv = next((i for i in range(k, n) if P[i][k]), None)
        if piv is None:
            return L()
        if piv != k:
            P[k], P[piv] = P[piv], P[k]
            sign = -sign
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                P[i][j] = pdiv(psub(pmul(P[i][j], P[k][k]), pmul(P[i][k], P[k][j])), prev)
            P[i][k] = {}
        prev = P[k][k]
    d = P[n - 1][n - 1]
    return L({e - n * shift: v * sign for e, v in d.items()})


def positive_roots_count_and_values(poly):
    """positive real roots of a Laurent polynomial (sympy used ONLY here, to isolate roots of a known exact polynomial)"""
    import sympy as sp
    x = sp.symbols("x", positive=True)
    if poly.is_zero():
        return "identically zero"
    lo = min(poly.c)
    expr = sum(sp.Rational(v.numerator, v.denominator) * x ** (e - lo) for e, v in poly.c.items())
    roots = [r for r in sp.Poly(expr, x).all_roots() if r.is_real and r > 0]
    return [str(r) for r in roots]


def poly_of(lp):
    """a nonzero Laurent polynomial times the power of q that makes it a polynomial with nonzero constant term (same positive
    roots): {exponent: coefficient}"""
    lo = min(lp.c)
    return {e - lo: v for e, v in lp.c.items()}


def poly_rem(a, b):
    """remainder of a by b (polynomials over Q as {exponent: coefficient}, b nonzero)"""
    a = dict(a)
    db = max(b)
    while a and max(a) >= db:
        da = max(a)
        c = a[da] / b[db]
        for e, v in b.items():
            k = e + da - db
            a[k] = a.get(k, 0) - c * v
            if a[k] == 0:
                del a[k]
    return a


def poly_gcd(a, b):
    """monic gcd over Q (Euclid, exact)"""
    while b:
        a, b = b, poly_rem(a, b)
    lead = a[max(a)]
    return {e: v / lead for e, v in a.items()}


def compare(A_gens, B_gens, basis):
    """Theorem T's checks for A against B on the given basis: (all traces equal, the first difference or None, the exact set of
    q > 0 where all 768 traces agree -- the conjugacy locus -- as 'every q > 0' or a list of roots)"""
    A, B = Rep(A_gens), Rep(B_gens)
    first, g = None, None
    for wi in basis:
        for wj in basis:
            for mid in ("", "m", "n"):
                w = wi + mid + wj
                d = A.trace(w) - B.trace(w)
                if d.is_zero():
                    continue
                if first is None:
                    first = {"word": w, "difference": repr(d), "positive q where it vanishes": positive_roots_count_and_values(d)}
                g = poly_of(d) if g is None else poly_gcd(g, poly_of(d))
    if first is None:
        return True, None, "every q > 0"
    gl = L(g)
    return False, first, ([] if max(g) == 0 else positive_roots_count_and_values(gl))


def gram(gens, basis):
    R = Rep(gens)
    return [[R.trace(wi + wj) for wj in basis] for wi in basis]


def decide(A_gens, B_gens, basis):
    equal, diff, locus = compare(A_gens, B_gens, basis)
    return {"all Theorem-T traces equal": equal, "first differing trace": diff, "conjugate exactly at q > 0": locus}


def representatives():
    sym = json.loads((HERE / "symmetries.json").read_text(encoding="utf-8"))
    return {k: {"m": v["m"], "n": v["n"], "orientation": v["orientation"]} for k, v in sym["representatives"].items()}


def setup():
    rho = ballas()
    R = Rep(rho)
    basis = choose_basis(R, F(3))
    G = gram(rho, basis)
    dG = det_laurent(G)
    return rho, basis, dG


def controls(rho, basis):
    # positive: conjugation by a fixed rational matrix; negative: rho_{2q} (q -> 2q) and rho_{1/q}
    P = mat([[1, 2, 0, -1], [0, 1, 3, 0], [1, 0, 1, 2], [2, -1, 0, 1]])
    Pd = det4(P)
    adj = [[det3(minor(P, j, i)).scale(-1 if (i + j) % 2 else 1) for j in range(4)] for i in range(4)]
    s = F(1) / Pd.at(1)
    Pinv = [[x.scale(s) for x in r] for r in adj]
    conj = {g: mmul(mmul(P, M), Pinv) for g, M in rho.items()}
    two = {g: [[L({e: v * F(2) ** e for e, v in x.c.items()}) for x in r] for r in M] for g, M in rho.items()}
    out = {
        "C1 rho vs rho": decide(rho, rho, basis),
        "C2 rho vs P rho P^-1": decide(rho, conj, basis),
        "C3 rho_q vs rho_2q": decide(rho, two, basis),
        "C4 rho_q vs rho_{1/q}": decide(rho, recip_rep(rho), basis),
        "C5 the relator holds": Rep(rho).word("mnMNmNMnmN") == Rep(rho).word(""),
    }
    out["C7 BANKED IDENTITY: tr rho_q(nMNmmNMn) = 3q + q^-3 (B1510 Lemma R)"] = Rep(rho).trace("nMNmmNMn") == L({1: 3, -3: 1})
    out["C6 poly_gcd on known polynomials: gcd((q-1)^2 (q+2), (q-1)(q-3)) = q - 1"] = poly_gcd(
        {3: F(1), 1: F(-3), 0: F(2)}, {2: F(1), 1: F(-4), 0: F(3)}) == {1: F(1), 0: F(-1)}
    out["controls passed"] = (out["C1 rho vs rho"]["all Theorem-T traces equal"] and out["C2 rho vs P rho P^-1"]["all Theorem-T traces equal"]
                              and out["C1 rho vs rho"]["conjugate exactly at q > 0"] == "every q > 0"
                              and not out["C3 rho_q vs rho_2q"]["all Theorem-T traces equal"]
                              and out["C3 rho_q vs rho_2q"]["conjugate exactly at q > 0"] == []
                              and not out["C4 rho_q vs rho_{1/q}"]["all Theorem-T traces equal"]
                              and out["C4 rho_q vs rho_{1/q}"]["conjugate exactly at q > 0"] == ["1"]
                              and out["C5 the relator holds"]
                              and out["C7 BANKED IDENTITY: tr rho_q(nMNmmNMn) = 3q + q^-3 (B1510 Lemma R)"]
                              and out["C6 poly_gcd on known polynomials: gcd((q-1)^2 (q+2), (q-1)(q-3)) = q - 1"])
    return out


def run(rho, basis):
    rho_inv = recip_rep(rho)
    table = {}
    for name, sig in representatives().items():
        for dual in (False, True):
            S = pulled_back(rho, sig, dual)
            key = ("D." if dual else "") + name
            table[key] = {"orientation": sig["orientation"], "dualised": dual,
                          "to rho_q": decide(S, rho, basis), "to rho_{1/q}": decide(S, rho_inv, basis)}
    return table


def main():
    rho, basis, dG = setup()
    head = {"basis words": basis, "det Gram (Laurent polynomial in q)": repr(dG),
            "positive roots of det Gram": positive_roots_count_and_values(dG)}
    if "--controls-only" in sys.argv:
        out = dict(head, controls=controls(rho, basis))
        (HERE / "route_traceform_controls.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
        print(json.dumps(out, indent=1))
        return
    out = dict(head, controls=controls(rho, basis), table=run(rho, basis))
    (HERE / "route_traceform.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
