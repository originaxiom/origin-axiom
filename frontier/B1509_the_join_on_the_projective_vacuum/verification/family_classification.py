"""B1509, post-run (computed after extension_index_run.txt): the classification behind Corollary C, over the whole family.

Corollary C (FINDINGS section 2) says that, among rank-five determinant-one extensions of a line by mu rho_q or of mu rho_q by a line
(q > 0, q != 1, mu any nonzero twist), main's index is nonzero only at the two mu = -1 points.  Its proof uses three facts checked here:
  (i)   H^0(F; rho_q) = 0 for every q > 0, q != 1, where F = <u0, u1> is the fibre group (wang_monodromy.py).  Checked as: the 70
        maximal minors of [rho(u0) - 1; rho(u1) - 1] (8 x 4 over Q(q)) have numerators whose gcd has no positive root except q = 1.
        By the Wang sequence, h^1(M; mu rho_q) is then the dimension of the eigenvalue-1 kernel of S_A = mu^-1 S_rho on H^1(F; rho_q),
        whose characteristic polynomial is the monic Q(q, s) (checked in wang_monodromy_run.txt).
  (ii)  Q(q, 1) = (q - 1)^2, so there is no class at mu = 1 for q != 1.
  (iii) Q(q, -1) = q^2 - 34 q + 1 and Q(q, +-i) = -(q^2 - 14 q + 1): their positive roots are 17 +- 12 sqrt2 and 7 +- 4 sqrt3."""
import itertools
import json
import sys
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
U = {0: "nM", 1: "mnMM"}


def ballas(qq):
    t = qq / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return m, n


def word_matrix(mats, w):
    X = sp.eye(4)
    for ch in w:
        X = X * (mats[ch] if ch.islower() else mats[ch.lower()].inv())
    return X


def positive_roots_other_than_one(poly, q):
    out = []
    for r in sp.Poly(poly, q).all_roots():
        if r.is_real and r > 0 and r != 1:
            out.append(str(r))
    return out


def fibre_invariants(dual=False):
    q = sp.symbols("q", positive=True)
    m, n = ballas(q)
    mats = {"m": m, "n": n} if not dual else {"m": m.inv().T, "n": n.inv().T}
    B = (word_matrix(mats, U[0]) - sp.eye(4)).col_join(word_matrix(mats, U[1]) - sp.eye(4))
    B = B.applyfunc(sp.cancel)
    g = sp.Integer(0)
    nonzero = 0
    for rows in itertools.combinations(range(8), 4):
        num = sp.numer(sp.together(sp.cancel(B.extract(list(rows), list(range(4))).det())))
        num = sp.expand(num)
        if num != 0:
            nonzero += 1
            g = sp.gcd(g, num)
    g = sp.factor(g)
    return {"nonzero_maximal_minors": nonzero, "gcd_of_numerators": str(g),
            "positive_roots_other_than_1": positive_roots_other_than_one(g, q) if g.free_symbols else []}


def q_at_twists():
    q, s = sp.symbols("q s")
    Q = -q * s ** 4 + 8 * q * s ** 3 + (q ** 2 - 16 * q + 1) * s ** 2 + 8 * q * s - q
    out = {}
    for label, mu in (("1", 1), ("-1", -1), ("i", sp.I), ("-i", -sp.I)):
        f = sp.factor(sp.expand(Q.subs(s, mu)))
        roots = [r for r in sp.Poly(sp.expand(Q.subs(s, mu)), q).all_roots() if r.is_real and r > 0 and r != 1]
        out[label] = {"Q(q, mu)": str(f), "positive_roots_q_not_1": [str(sp.nsimplify(r)) for r in roots]}
    return out


def main():
    return {"H0(F; rho_q)": fibre_invariants(), "H0(F; rho_q*)": fibre_invariants(dual=True), "Q_at_central_twists": q_at_twists()}


if __name__ == "__main__":
    res = main()
    txt = json.dumps(res, indent=1, sort_keys=True, default=str)
    print(txt)
    if "--record" in sys.argv:
        (HERE / "family_classification_run.txt").write_text(txt + "\n", encoding="utf-8")
