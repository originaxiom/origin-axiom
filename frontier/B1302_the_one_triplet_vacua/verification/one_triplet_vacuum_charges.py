#!/usr/bin/env python3
"""THE ONE-TRIPLET VACUUM'S GAUGE GROUP AND LIGHT SPECTRUM (B1302 addendum): on the solved configuration of B1302 --
<N_g2> with the flavon pair (S_g0g1, S_g1g0), generation g2 light -- the abelian factors surviving at tree level (the
four extra U(1)s of the SM closing: beta, gamma, the two family charges; B1283's charge table), their charges on the
light generation's fields, the same with the nu^c_g2 VEV added (B1283's maximal branch), and the light generation's
tree-level Yukawa couplings (the family tensor |eps_ijk| has no diagonal entry: zero).  Exact rational linear algebra;
the charge table is B1283's (beta = (psi + chi)/4, gamma = -(5/12) psi + (1/4) chi on every SM field)."""
from __future__ import annotations
import sys, itertools, collections
from fractions import Fraction as F
import sympy as sp

# (q_beta, q_gamma) of the multiplets of the 27 (B1283 section 1) and the family charges of the three generations
BG = {'Q': (0, F(-2, 3)), 'u^c': (0, F(-2, 3)), 'e^c': (0, F(-2, 3)), 'H_u': (0, F(4, 3)), 'D': (0, F(4, 3)),
      'd^c': (1, F(1, 3)), 'L': (1, F(1, 3)), 'H_d': (-1, F(1, 3)), 'Dbar': (-1, F(1, 3)),
      'nu^c': (-1, F(-5, 3)), 'N': (1, F(-5, 3))}
E = {0: (1, 0), 1: (0, 1), 2: (-1, -1)}
LIGHT = ('Q', 'u^c', 'd^c', 'L', 'e^c', 'nu^c', 'H_u', 'H_d')          # generation g2's light multiplets (D, Dbar absent)


def charge(lab, g):
    qb, qg = BG[lab]
    return sp.Matrix([[sp.Rational(qb), sp.Rational(qg), E[g][0], E[g][1]]])


def vev_matrix(g0, g1, g2, with_nu):
    rows = [charge('N', g2)]
    rows.append(sp.Matrix([[0, 0, E[g0][0] - E[g1][0], E[g0][1] - E[g1][1]]]))       # S_g0g1 (S_g1g0 is its negative)
    if with_nu:
        rows.append(charge('nu^c', g2))
    return sp.Matrix.vstack(*rows)


def analyse(g0, g1, g2, with_nu):
    M = vev_matrix(g0, g1, g2, with_nu)
    rk = M.rank(); surv = M.nullspace()
    out = dict(rank=rk, surviving=4 - rk, directions=[])
    for v in surv:
        v = v / sp.gcd(list(v)) if all(x.is_integer for x in v) else v * sp.lcm([x.q for x in v])
        v = v / sp.gcd([x for x in v if x != 0])
        charges = {}
        for lab in LIGHT:
            q = (charge(lab, g2) * v)[0]
            charges[lab] = q
        # the VEV'd fields must be neutral
        assert all((charge('N', g2) * v)[0] == 0 for _ in [0]) and (sp.Matrix([[0, 0, E[g0][0] - E[g1][0], E[g0][1] - E[g1][1]]]) * v)[0] == 0
        out['directions'].append((list(v), charges))
    return out


def main():
    print("=== the one-triplet vacuum (B1302): the surviving abelian factors and the light generation's charges ===")
    res = {}
    for (g0, g1, g2) in itertools.permutations((0, 1, 2)):
        for with_nu in (False, True):
            r = analyse(g0, g1, g2, with_nu)
            res[(g0, g1, g2, with_nu)] = r
    # the structure is generation-symmetric; report for (g0, g1, g2) = (1, 3, 2) i.e. indices (0, 2, 1)
    for with_nu in (False, True):
        r = res[(0, 2, 1, with_nu)]
        print(f"\n  configuration <N_2>, flavons S_13, S_31{', <nu^c_2>' if with_nu else ''}: charge-matrix rank {r['rank']}, surviving extra U(1)s: {r['surviving']}")
        for v, ch in r['directions']:
            print(f"    direction (beta, gamma, fam1, fam2) = {v}: charges on the light generation " + ", ".join(f"{lab} {ch[lab]}" for lab in LIGHT))
    same = all(res[k]['surviving'] == res[(0, 2, 1, k[3])]['surviving'] for k in res)
    print(f"\n  the same surviving rank for every generation assignment: {same}")
    # the light generation's tree-level Yukawas: the family tensor |eps_ijk| vanishes on the diagonal
    print("  the light generation's tree-level Yukawa couplings Q_g2 u^c_g2 H_u,g2, Q_g2 d^c_g2 H_d,g2, L_g2 e^c_g2 H_d,g2, L_g2 nu^c_g2 H_u,g2: the family tensor |eps_ijk| has |eps_{g2 g2 g2}| = 0, so all vanish at tree level (B1271's theorem on the light generation)")
    ok = res[(0, 2, 1, False)]['surviving'] == 2 and res[(0, 2, 1, True)]['surviving'] == 1 and same
    return dict(res={str(k): v['surviving'] for k, v in res.items()}, dirs=res[(0, 2, 1, False)]['directions'], dirs_nu=res[(0, 2, 1, True)]['directions'], ok=ok)


if __name__ == "__main__":
    out = main()
    print("\nSELFTEST:", "PASS" if out['ok'] else "FAIL")
    sys.exit(0 if out['ok'] else 1)
