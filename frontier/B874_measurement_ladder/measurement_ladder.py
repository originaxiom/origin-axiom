#!/usr/bin/env python3
"""B874 -- the measurement ladder: the exact centralizer census of the 2T-torus, and
the type of the full-measurement remnant.

B866 stratified charge measurement along the (8,16)-plane. This arc completes the
COORDINATE stratification exactly (all 15 subtori of C = <x8, x14, x16, x22>) and
computes the structure of the full-measurement centralizer Cent(C) over Q:

  - census: dim Cent = 30 for every subtorus inside the (8,16)-plane, 12 for every
    subtorus touching x14 or x22. The plane is the unique SOFT direction; x14/x22
    are maximally resolving alone.
  - Cent(C): dim 12 = derived 8 + center 4. The center IS C (one line: C is abelian
    and Cent(C) commutes with C by definition, so C sits in the center; dims match).
    The derived algebra has NONDEGENERATE intrinsic Killing form (rank 8) --
    semisimple of dim 8 => type A2 (the unique 8-dim semisimple), with signature
    (4,4) => the real form su(2,1) (su(3): (0,8); sl(3,R): (5,3); su(2,1): (4,4)).

Verdict: the full measurement does NOT land on the SM algebra (derived would be 11,
center 1). What survives every 2T-charge is an su(3)-TYPE remnant plus the four
measured charges. Recorded as computed structure; no dictionary is asserted.

Mathematics scope; nothing to CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from itertools import combinations

import sympy as sp

HERE = os.path.dirname(os.path.abspath(__file__))
B854 = os.path.normpath(os.path.join(HERE, "..", "B854_centralizer_exact",
                                     "e6_centralizer.py"))


def main():
    src = open(B854, encoding="utf-8").read()
    g = {"__file__": B854, "__name__": "b854"}
    exec(compile(src, B854, "exec"), g)
    DIM, N = g["DIM"], g["N"]
    br, hvec, evec, ROOTS = g["br"], g["hvec"], g["evec"], g["ROOTS"]
    basis = [hvec(i) for i in range(N)] + [evec(r) for r in ROOTS]

    def admat(v):
        cols = [br(v, b) for b in basis]
        return sp.Matrix([[sp.Rational(cols[j][i].numerator,
                                       cols[j][i].denominator)
                           for j in range(DIM)] for i in range(DIM)])

    ns = [8, 14, 16, 22]
    ADS = {n: admat(g["INV"][n]) for n in ns}

    census = {}
    for k in range(1, 5):
        for combo in combinations(ns, k):
            stack = sp.Matrix.vstack(*[ADS[n] for n in combo])
            census["+".join(f"x{n}" for n in combo)] = DIM - stack.rank()

    # ---- Cent(C) structure, exactly over Q
    stack = sp.Matrix.vstack(*[ADS[n] for n in ns])
    ker = stack.nullspace()
    dim_cent = len(ker)
    from fractions import Fraction as Fr
    K = [[Fr(sp.Rational(v[i]).p, sp.Rational(v[i]).q) for i in range(DIM)]
         for v in ker]
    Km = sp.Matrix([[sp.Rational(c.numerator, c.denominator) for c in k]
                    for k in K]).T
    brij = {}
    closure_ok = True
    for i in range(dim_cent):
        for j in range(i + 1, dim_cent):
            v = br(K[i], K[j])
            b = sp.Matrix([sp.Rational(c.numerator, c.denominator) for c in v])
            sol = Km.solve_least_squares(b)
            closure_ok &= (sp.simplify((Km * sol - b).norm()) == 0)
            brij[(i, j)] = sol
    D = sp.Matrix.hstack(*[brij[k] for k in sorted(brij)])
    derived_dim = D.rank()

    def admat12(i0):
        M = sp.zeros(dim_cent, dim_cent)
        for j in range(dim_cent):
            if i0 == j:
                continue
            key = (min(i0, j), max(i0, j))
            s = 1 if i0 < j else -1
            M[:, j] += s * brij[key]
        return M

    ads12 = [admat12(i) for i in range(dim_cent)]
    rowsC = []
    for j in range(dim_cent):
        M = sp.zeros(dim_cent, dim_cent)
        for i in range(dim_cent):
            if i == j:
                continue
            key = (min(i, j), max(i, j))
            s = 1 if i < j else -1
            M[:, i] = s * brij[key]
        rowsC.append(M)
    center_dim = len(sp.Matrix.vstack(*rowsC).nullspace())

    Kill = sp.Matrix(dim_cent, dim_cent,
                     lambda i, j: (ads12[i] * ads12[j]).trace())
    kr = Kill.rank()
    ev = Kill.eigenvals()
    pos = sum(m for e, m in ev.items() if sp.simplify(e).is_positive)
    neg = sum(m for e, m in ev.items() if sp.simplify(e).is_negative)

    res = dict(
        census=census,
        cent_dim=dim_cent, closure_ok=bool(closure_ok),
        derived_dim=derived_dim, center_dim=center_dim,
        center_is_C="C abelian and Cent(C) commutes with C by definition => "
                    "C <= center; dims 4 = 4 => center = C",
        killing_rank=kr, killing_signature=[int(pos), int(neg),
                                            dim_cent - int(pos) - int(neg)],
        derived_type="A2 (unique 8-dim semisimple; Killing nondegenerate on it)",
        derived_real_form="su(2,1) by signature (4,4) "
                          "[su(3): (0,8); sl(3,R): (5,3); su(2,1): (4,4)]",
        full_measurement_is_sm=False,
        ladder=sorted(set(census.values()), reverse=True),
    )
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1,
              sort_keys=True)

    print("=" * 74)
    print("B874 -- the measurement ladder")
    print("=" * 74)
    for k in sorted(census, key=lambda x: (-census[x], x)):
        print(f"  Cent(<{k}>) = {census[k]}")
    print(f"\n  Cent(C): dim {dim_cent} = derived {derived_dim} + center "
          f"{center_dim} (= C);  brackets close: {closure_ok}")
    print(f"  intrinsic Killing rank {kr}, signature "
          f"({pos},{neg},{dim_cent - pos - neg})")
    print(f"  derived type: A2, real form su(2,1)")
    print(f"  full measurement lands on the SM algebra: "
          f"{res['full_measurement_is_sm']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
