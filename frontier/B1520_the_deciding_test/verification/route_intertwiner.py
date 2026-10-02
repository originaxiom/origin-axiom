#!/usr/bin/env python3
"""B1520 route 1 (R1) -- conjugacy by the intertwiner equations, exactly over Q(q).

For each of the sixteen maps Phi = (sigma, d) -- sigma one of the eight representatives of Out(pi_1 m004) (symmetries.py) and
d in {0, 1} (d = 1: dualise, V -> V* = V^-T) -- and each target T in {rho_q, rho_{1/q}}, solve the linear equations
    X . Phi(rho_q)(g) = T(g) . X,      g = m, n,
for X in M_4(Q(q)) (16 unknowns, 32 equations), with Phi(rho_q)(g) = rho_q(sigma(g)) (inverse-transposed when d = 1). Ballas'
family rho_q (Ballas, arXiv:1403.3314, p. 17, t = q/2) is typed here from the paper. Reported: the dimension of the solution
space over Q(q); for a one-dimensional space, the generator X(q) (scaled to polynomial entries with no common factor), det X(q)
factored, and its positive real zeros, where the equations are re-solved exactly at that q (over Q, or over the number field
Q(q0) for an irrational zero) and the solution space is tested for an invertible element exactly (the determinant of a generic
combination, as a polynomial in the coefficients). A generator with det X = 0 identically is a singular map and never counts as
an isomorphism. X is verified by substitution. Shares no code with route 2 (route_traceform.py) or with B1512.
Usage: python3 route_intertwiner.py [--controls-only]   (writes route_intertwiner.json, or route_intertwiner_controls.json)"""
import json
import sys
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

HERE = Path(__file__).resolve().parent
q = sp.symbols("q", positive=True)
FIELD = sp.QQ.frac_field(q)


def ballas(qq):
    t = qq / 2
    m = sp.Matrix([[1, 0, 1, t - 1], [0, 1, 1, t], [0, 0, 1, t + sp.Rational(1, 2)], [0, 0, 0, 1]])
    n = sp.Matrix([[1, 0, 0, 0], [2 + 1 / t, 1, 0, 0], [2, 1, 1, 0], [1, 1, 0, 1]])
    return {"m": m, "n": n}


def word_matrix(gens, w):
    X = sp.eye(4)
    for c in w:
        X = X * (gens[c] if c.islower() else gens[c.lower()].inv())
    return X.applyfunc(sp.cancel)


def pulled_back(gens, sigma, dual):
    out = {}
    for g in ("m", "n"):
        X = word_matrix(gens, sigma[g])
        out[g] = (X.inv().T if dual else X).applyfunc(sp.cancel)
    return out


def equations(S, T):
    """the 32 x 16 coefficient matrix of X S(g) - T(g) X = 0 (g = m, n) in the entries of X (row-major)"""
    unknowns = sp.symbols("x0:16")
    X = sp.Matrix(4, 4, unknowns)
    eqs = []
    for g in ("m", "n"):
        eqs.extend(list(X * S[g] - T[g] * X))
    return sp.Matrix([[sp.cancel(sp.diff(e, u)) for u in unknowns] for e in eqs])


def intertwiner_space(S, T):
    """basis of {X : X S(g) = T(g) X, g = m, n} over Q(q), each generator scaled to polynomial entries with no common factor"""
    D = DomainMatrix.from_Matrix(equations(S, T)).convert_to(FIELD)
    ns = D.nullspace()            # rows are basis vectors (DomainMatrix convention)
    out = []
    for i in range(ns.shape[0]):
        Xb = sp.Matrix(4, 4, [sp.cancel(x) for x in ns.to_Matrix().row(i)])
        den = sp.lcm([sp.denom(sp.together(x)) for x in Xb])
        Xb = (Xb * den).applyfunc(lambda x: sp.expand(sp.cancel(x)))
        nonzero = [x for x in Xb if x != 0]
        content = sp.gcd_list(nonzero) if nonzero else 1
        out.append(Xb.applyfunc(lambda x: sp.factor(sp.cancel(x / content))))
    return out


def point_domain(at):
    """Q for a rational point, else the number field Q(at) (exact arithmetic with an algebraic number)"""
    return sp.QQ if at.is_Rational else sp.QQ.algebraic_field(at)


def intertwiner_space_at(S, T, at):
    """basis (rows of length 16 over K) of the intertwiners at the exact point q = at, and K"""
    K = point_domain(at)
    D = DomainMatrix.from_Matrix(equations(S, T).subs(q, at)).convert_to(K)
    ns = D.nullspace()
    return [ns[i:i + 1, :].to_list()[0] for i in range(ns.shape[0])], K


def some_invertible(rows, K):
    """does the span of the given intertwiners (rows over K) contain an invertible matrix? Exact: det(sum c_k X_k) as a polynomial
    in the c_k over K is not the zero polynomial"""
    if not rows:
        return False
    R = K[sp.symbols(f"c0:{len(rows)}")]
    entries = [[R.zero] * 4 for _ in range(4)]
    for k, row in enumerate(rows):
        for idx, v in enumerate(row):
            i, j = divmod(idx, 4)
            entries[i][j] = entries[i][j] + R.convert_from(v, K) * R.gens[k]
    return DomainMatrix(entries, (4, 4), R).det() != R.zero


def verify(X, S, T):
    return all((X * S[g] - T[g] * X).applyfunc(sp.cancel) == sp.zeros(4, 4) for g in ("m", "n"))


def decide(S, T, label):
    basis = intertwiner_space(S, T)
    rec = {"pair": label, "dim over Q(q)": len(basis)}
    if len(basis) == 1:
        X = basis[0]
        detX = sp.factor(sp.cancel(X.det()))
        rec["X verified"] = verify(X, S, T)
        rec["det X"] = str(detX)
        if detX == 0:
            rec["isomorphic for every q > 0"] = False
            rec["note"] = "the only intertwiner over Q(q) is singular: not isomorphic for generic q"
            return rec
        num = sp.numer(sp.together(detX))
        zeros = [r for r in sp.Poly(num, q).all_roots() if r.is_real and r > 0] if num.free_symbols else []
        rec["positive zeros of det X"] = [str(r) for r in zeros]
        rec["at the zeros: dim, some invertible"] = []
        for r in zeros:
            rows, K = intertwiner_space_at(S, T, r)
            rec["at the zeros: dim, some invertible"].append([str(r), len(rows), some_invertible(rows, K)])
        rec["isomorphic for every q > 0"] = rec["X verified"] and all(z[2] for z in rec["at the zeros: dim, some invertible"])
    elif len(basis) == 0:
        rec["isomorphic for every q > 0"] = False
        rec["note"] = "no intertwiner over Q(q): isomorphic at most at finitely many q (route 2 locates them)"
    else:
        rec["isomorphic for every q > 0"] = "dimension > 1: reducible case, not expected"
    return rec


def representatives():
    sym = json.loads((HERE / "symmetries.json").read_text(encoding="utf-8"))
    return {k: {"m": v["m"], "n": v["n"], "orientation": v["orientation"]} for k, v in sym["representatives"].items()}


def controls():
    rho = ballas(q)
    rho_inv = {g: M.subs(q, 1 / q).applyfunc(sp.cancel) for g, M in rho.items()}
    P = sp.Matrix([[1, 2, 0, -1], [0, 1, 3, 0], [1, 0, 1, 2], [2, -1, 0, 1]])
    conj = {g: (P * M * P.inv()).applyfunc(sp.cancel) for g, M in rho.items()}
    rho2q = {g: M.subs(q, 2 * q).applyfunc(sp.cancel) for g, M in rho.items()}
    # C7: diagonal characters of H1 = Z (m, n -> the same diagonal matrix satisfies the relator, exponent sum 0); exactly one
    # character shared, so the only intertwiner is the singular E_11: must be reported NOT isomorphic
    diag_s, diag_t = sp.diag(1, 2, 3, 5), sp.diag(1, 7, 11, 13)
    chi_s, chi_t = {"m": diag_s, "n": diag_s}, {"m": diag_t, "n": diag_t}
    x = sp.symbols("x")
    r3 = sp.CRootOf(x ** 3 - x - 1, 0)              # an irrational positive point, ~1.3247, exact in Q(r3)
    rows_pos, K_pos = intertwiner_space_at(rho, rho, r3)
    rows_neg, K_neg = intertwiner_space_at(rho, rho2q, r3)
    rows_one, K_one = intertwiner_space_at(rho, rho_inv, sp.Integer(1))
    out = {
        "C1 rho_q vs rho_q (positive)": decide(rho, rho, "id"),
        "C2 rho_q vs P rho_q P^-1 (positive)": decide(rho, conj, "conj"),
        "C3 rho_q vs rho_2q (negative)": decide(rho, rho2q, "2q"),
        "C4 rho_q vs rho_{1/q}, no map (negative off q = 1)": decide(rho, rho_inv, "1/q"),
        "C5 at q = the real root of x^3 - x - 1: rho vs rho, dim and invertible (positive)": [len(rows_pos), some_invertible(rows_pos, K_pos)],
        "C6 at the same point: rho_q vs rho_2q, dim and invertible (negative)": [len(rows_neg), some_invertible(rows_neg, K_neg)],
        "C7 a unique singular intertwiner (negative)": decide(chi_s, chi_t, "singular"),
        "C8 at q = 1: rho_q vs rho_{1/q}, dim and invertible (positive: they coincide)": [len(rows_one), some_invertible(rows_one, K_one)],
        "C9 BANKED IDENTITY: the relator mnMNmNMnmN holds": word_matrix(rho, "mnMNmNMnmN") == sp.eye(4),
        "C10 BANKED IDENTITY: tr rho_q(nMNmmNMn) = 3q + q^-3 (B1510 Lemma R)":
            sp.simplify(word_matrix(rho, "nMNmmNMn").trace() - (3 * q + q ** -3)) == 0,
    }
    ok = (out["C1 rho_q vs rho_q (positive)"]["isomorphic for every q > 0"] is True
          and out["C2 rho_q vs P rho_q P^-1 (positive)"]["isomorphic for every q > 0"] is True
          and out["C3 rho_q vs rho_2q (negative)"]["isomorphic for every q > 0"] is False
          and out["C4 rho_q vs rho_{1/q}, no map (negative off q = 1)"]["isomorphic for every q > 0"] is False
          and out["C5 at q = the real root of x^3 - x - 1: rho vs rho, dim and invertible (positive)"] == [1, True]
          and out["C6 at the same point: rho_q vs rho_2q, dim and invertible (negative)"] == [0, False]
          and out["C7 a unique singular intertwiner (negative)"]["dim over Q(q)"] == 1
          and out["C7 a unique singular intertwiner (negative)"]["isomorphic for every q > 0"] is False
          and out["C8 at q = 1: rho_q vs rho_{1/q}, dim and invertible (positive: they coincide)"] == [1, True]
          and out["C9 BANKED IDENTITY: the relator mnMNmNMnmN holds"]
          and out["C10 BANKED IDENTITY: tr rho_q(nMNmmNMn) = 3q + q^-3 (B1510 Lemma R)"])
    out["controls passed"] = ok
    return out


def run():
    rho = ballas(q)
    rho_inv = {g: M.subs(q, 1 / q).applyfunc(sp.cancel) for g, M in rho.items()}
    reps = representatives()
    table = {}
    for name, sig in reps.items():
        for dual in (False, True):
            S = pulled_back(rho, sig, dual)
            key = ("D." if dual else "") + name
            table[key] = {"orientation": sig["orientation"], "dualised": dual,
                          "to rho_q": decide(S, rho, key + " -> rho_q"),
                          "to rho_{1/q}": decide(S, rho_inv, key + " -> rho_{1/q}")}
    return table


def main():
    if "--controls-only" in sys.argv:
        out = controls()
        (HERE / "route_intertwiner_controls.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
        print(json.dumps(out, indent=1))
        return
    out = {"controls": controls(), "table": run()}
    (HERE / "route_intertwiner.json").write_text(json.dumps(out, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    main()
