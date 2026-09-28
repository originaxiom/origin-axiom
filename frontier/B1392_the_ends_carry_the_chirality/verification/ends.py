#!/usr/bin/env python3
"""B1392 -- THE ENDS CARRY THE CHIRALITY: in the seat's frame, a cusp where the Higgs class does not vanish is sealed (the deformed
problem is well-posed there and the end contributes nothing to the count); a cusp where it vanishes (B1369's free cusp) keeps the
cusp's continuum and carries the count.  So N != 0 forces an unsealed end, and on the complete manifold the problem is then not
Fredholm: chirality and a well-posed problem exclude each other.

(A) THE CUSP, symbolically (sympy).  Coordinates (x, y, h), g = (dx^2 + dy^2 + dh^2)/h^2.
    - the undeformed 1-form sector: Delta_H (h^s dx) = -s^2 h^s dx, and the L^2 borderline is Re s = 0, so the cusp's continuum is
      [0, oo) -- zero is its bottom (B1388's premise, derived here);
    - a dx + b dy (a, b constant) is closed and co-closed; its norm is h sqrt(a^2 + b^2);
    - the harmonic functions of h alone are h^0 and h^2; only h^0 is L^2 up the cusp; the co-closed dh-forms c(h) dh are c = C h,
      i.e. d(C h^2 / 2);
    - for omega = a dx + b dy, |nabla omega|_g / |omega|_g^2 = O(1/h), so the Witten potential T^2 |omega|^2 beats the Hessian
      term T |nabla omega| up the cusp.
(B) THE CANONICAL REPRESENTATIVE (the proof is in FINDINGS section 1): every class has exactly one harmonic representative with a
    bounded primitive in every cusp, omega = alpha_c + (exponentially small) at cusp c, alpha_c the flat form of v on the torus.
(C) THE MEMBERS.  For B1186's 99 arithmetic members (B1390) and cube~3.24: b_1, the cusps, and per cusp the rank of its peripheral
    image P_c in H_1(M; Q) -- a class leaves cusp c unsealed iff it lies in ann(P_c), of dimension b_1 - rank P_c (B1369's free
    cusps are those with rank P_c < b_1).  Every rank is >= 1, so a generic class seals every cusp.
Usage: python3 ends.py"""
import json
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
import sympy as sp

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]

NONARITHMETIC = ["v2875", "t06828", "t06829", "t11365", "o9_41000", "o9_41003", "o9_41004", "o9_41005", "o9_41006", "o9_41008",
                 "o10_143600", "o10_143601", "o10_143602"]            # B1390


def cusp_symbolics():
    x, y, h = sp.symbols("x y h", positive=True)
    a, b, C, s = sp.symbols("a b C s", real=True)
    X = (x, y, h)
    g = sp.diag(1 / h ** 2, 1 / h ** 2, 1 / h ** 2)
    ginv = g.inv()
    sqrtg = h ** -3

    def codiff(w):                                    # delta w = -(1/sqrt g) d_i (sqrt g g^{ij} w_j)
        return sp.simplify(-sum(sp.diff(sqrtg * sum(ginv[i, j] * w[j] for j in range(3)), X[i]) for i in range(3)) / sqrtg)

    def dform(w):                                     # (dw)_{ij} = d_i w_j - d_j w_i
        return sp.Matrix(3, 3, lambda i, j: sp.diff(w[j], X[i]) - sp.diff(w[i], X[j]))

    w = [a, b, 0]
    out = {}
    out["closed"] = dform(w) == sp.zeros(3, 3)
    out["coclosed"] = codiff(w) == 0
    out["norm^2"] = sp.simplify(sum(ginv[i, j] * w[i] * w[j] for i in range(3) for j in range(3)))
    c = sp.Function("c")
    sol = sp.dsolve(sp.Eq(codiff([0, 0, c(h)]), 0), c(h))
    out["coclosed dh-forms"] = sol.rhs
    f = h ** s
    lap = sp.simplify(codiff([sp.diff(f, xi) for xi in X]))
    out["Delta h^s / h^s"] = sp.factor(sp.simplify(lap / f))
    out["harmonic exponents"] = sp.solve(sp.Eq(out["Delta h^s / h^s"], 0), s)
    # L^2 up the cusp: int^oo h^(2s) h^(-3) dh < oo  iff  2 s - 3 < -1
    out["L2 exponents"] = [e for e in out["harmonic exponents"] if 2 * e - 3 < -1]
    # the Christoffel symbols of g = e^{2 phi} delta, phi = -log h, and |nabla omega|_g for omega = a dx + b dy
    phi = -sp.log(h)
    dphi = [sp.diff(phi, xi) for xi in X]
    Gam = [[[sp.simplify((1 if k == i else 0) * dphi[j] + (1 if k == j else 0) * dphi[i] - (1 if i == j else 0) * dphi[k])
             for j in range(3)] for i in range(3)] for k in range(3)]
    nab = sp.Matrix(3, 3, lambda i, j: sp.diff(w[j], X[i]) - sum(Gam[k][i][j] * w[k] for k in range(3)))
    nab2 = sp.simplify(sum(ginv[i, i2] * ginv[j, j2] * nab[i, j] * nab[i2, j2] for i in range(3) for i2 in range(3)
                           for j in range(3) for j2 in range(3)))
    out["|nabla omega|^2"] = sp.factor(nab2)
    out["|nabla omega| / |omega|^2"] = sp.simplify(sp.sqrt(nab2) / out["norm^2"])
    # the undeformed 1-form sector at a cusp: Delta_H (h^s dx) = (d delta + delta d)(h^s dx).  delta(h^s dx) = 0; d(h^s dx) =
    # s h^(s-1) dh ^ dx; for a 2-form, (delta beta)^j = -(1/sqrt g) d_i (sqrt g beta^{ij}), then lower the index.
    fs = h ** s
    assert codiff([fs, 0, 0]) == 0
    beta = sp.zeros(3, 3)
    beta[2, 0] = sp.diff(fs, h)                      # beta_{h x} = d_h(h^s), beta_{x h} = -beta_{h x}
    beta[0, 2] = -beta[2, 0]
    beta_up = ginv * beta * ginv
    dbeta_up = [sp.simplify(-sum(sp.diff(sqrtg * beta_up[i, j], X[i]) for i in range(3)) / sqrtg) for j in range(3)]
    dbeta = [sp.simplify(sum(g[j, k] * dbeta_up[k] for k in range(3))) for j in range(3)]
    out["Delta_H(h^s dx) / (h^s dx)"] = sp.simplify(dbeta[0] / fs)
    assert dbeta[1] == 0 and dbeta[2] == 0
    # L^2 of h^s dx up the cusp: |dx|_g^2 = h^2, dvol = h^-3: int^oo h^(2 Re s - 1) dh; the borderline is Re s = 0, where
    # s = i nu gives -s^2 = nu^2: the continuous spectrum [0, oo) -- zero is its bottom (B1388's premise, derived)
    nu = sp.Symbol("nu", real=True)
    out["continuum: -s^2 at s = i nu"] = sp.simplify(out["Delta_H(h^s dx) / (h^s dx)"].subs(s, sp.I * nu))
    return out


def abelianise(word, gens):
    v = [0] * len(gens)
    for ch in word:
        i = gens.index(ch.lower())
        v[i] += 1 if ch.islower() else -1
    return v


def peripheral_ranks(M):
    """b_1 and, per cusp, the rank of the image of its peripheral subgroup in H_1(M; Q) (B1369's snappy_ranks)"""
    G = M.fundamental_group()
    gens = list(G.generators())
    rels = G.relators()
    R = sp.Matrix([abelianise(r, gens) for r in rels]) if rels else sp.zeros(0, len(gens))
    rR = R.rank() if rels else 0
    out = []
    for (mu, lam) in G.peripheral_curves():
        P = sp.Matrix([abelianise(mu, gens), abelianise(lam, gens)])
        out.append((sp.Matrix.vstack(R, P) if rels else P).rank() - rR)
    return len(gens) - rR, out


def members_table():
    import snappy
    fam = json.load(open(ROOT / "frontier" / "B1186_family_is_112" / "verification" / "family_census.json"))
    rows = []
    for name in fam["members_B"]:
        if name in NONARITHMETIC:
            continue
        M = snappy.Manifold(name)
        b1, ranks = peripheral_ranks(M)
        rows.append((name, M.num_cusps(), b1, ranks))
    M = snappy.Manifold("o10_150725").covers(3)[4].covers(3)[24]
    b1, ranks = peripheral_ranks(M)
    rows.append(("cube~3.24", M.num_cusps(), b1, ranks))
    return rows


if __name__ == "__main__":
    print("=== (A) the cusp, symbolically: g = (dx^2 + dy^2 + dh^2)/h^2 ===")
    S = cusp_symbolics()
    for k, v in S.items():
        print("  %-28s %s" % (k, v))
    assert S["closed"] and S["coclosed"]
    assert sp.simplify(S["norm^2"] - sp.Symbol("h", positive=True) ** 2 * (sp.Symbol("a", real=True) ** 2 + sp.Symbol("b", real=True) ** 2)) == 0
    assert sorted(S["harmonic exponents"]) == [0, 2] and S["L2 exponents"] == [0]
    assert sp.simplify(S["Delta_H(h^s dx) / (h^s dx)"] + sp.Symbol("s", real=True) ** 2) == 0
    print("  -> an unsealed cusp keeps the undeformed 1-form continuum [0, oo): Delta_H(h^s dx) = -s^2 h^s dx on the L^2 borderline"
          " Re s = 0 -- the problem is not Fredholm there (B1388's premise, derived).")
    print("  -> a sealed cusp (alpha_c != 0): |omega| = h |alpha_c|, and the Hessian term is O(1/h) of the potential: T^2|omega|^2 -> oo.")
    print("\n=== (C) the members: per cusp, the rank of its peripheral image (unsealed classes: dimension b_1 - rank) ===")
    rows = members_table()
    free = sum(1 for (_, _, b1, rk) in rows for r in rk if r < b1)
    min_rank = min(r for (_, _, _, rk) in rows for r in rk)
    n_free_members = sum(1 for (_, _, b1, rk) in rows if any(r < b1 for r in rk))
    print("  %d members (99 arithmetic census members + cube~3.24): %d cusps; minimum peripheral rank %d, so a generic class seals every"
          " cusp; free cusps (a class can leave them unsealed) %d, on %d members" % (
              len(rows), sum(n for (_, n, _, _) in rows), min_rank, free, n_free_members))
    c324 = [r for r in rows if r[0] == "cube~3.24"][0]
    print("  cube~3.24: b_1 %d, ranks %s -> the classes unsealed at every cusp: dimension b_1 - (the joint rank) = the cuspidal line"
          " (v+, B1386)" % (c324[2], c324[3]))
    assert min_rank >= 1
    print("DONE")
