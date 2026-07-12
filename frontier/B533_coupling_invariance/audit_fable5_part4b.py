#!/usr/bin/env python3
"""B533 audit part 4b: DECIDE the GL(4,Z) conjugacy question.

For each pair (A,B) of type matrices with the same irreducible charpoly:
  1. integer basis of the solution lattice {U : U A = B U}
  2. saturation check via invariant factors (gcd of k-minors)
  3. mod-2 obstruction: det(sum c_i B_i) mod 2 depends only on c mod 2.
     If no c in F_2^4 gives odd det -> det never +-1 -> NOT conjugate (PROVEN).
  4. if no obstruction: extended box search (radius 20, chunked numpy)
     for an explicit unimodular conjugator.
"""

import sys
import os
import numpy as np
import sympy as sp
from itertools import product as iprod, combinations

sys.path.insert(0, os.path.join(os.path.dirname(__file__),
                                '..', 'B530_natural_history'))
from listen_39_induction_engine import (
    grow, factor_position_map, standard_return_words_from_positions,
    canonical_induced_system,
)

X = sp.Symbol('x')
CHARPOLY = X**4 - 2*X**3 - 5*X**2 - 4*X - 1


def analyze(factor, host, trim=2):
    fpm = factor_position_map(host, len(factor))
    positions = fpm[factor]
    rws = standard_return_words_from_positions(host, positions, trim=trim)
    ind = canonical_induced_system(rws, max_power=2)
    return sp.Matrix(ind['matrix'])


def integer_solution_basis(A, B):
    """Integer basis of {U in M4(Z) : U A = B U} (as 4x4 sympy matrices)."""
    K = sp.Matrix(sp.kronecker_product(A.T, sp.eye(4))
                  - sp.kronecker_product(sp.eye(4), B))
    ns = K.nullspace()
    vecs = []
    for vv in ns:
        den = sp.lcm([sp.fraction(sp.nsimplify(e))[1] for e in vv])
        vv2 = vv * den
        g = sp.gcd([e for e in vv2 if e != 0])
        vecs.append([sp.Integer(e / g) for e in vv2])
    return vecs


def invariant_factors(vecs):
    """Invariant factors of the 4x16 integer matrix with rows vecs,
    via gcds of k-minors."""
    W = sp.Matrix(vecs)  # 4 x 16
    m, n = W.shape
    d = [sp.Integer(1)]
    for k in range(1, m + 1):
        gk = sp.Integer(0)
        for rows in combinations(range(m), k):
            for cols in combinations(range(n), k):
                minor = W[list(rows), list(cols)].det()
                gk = sp.gcd(gk, minor)
                if gk == 1:
                    break
            if gk == 1:
                break
        d.append(gk)
        if gk == 0:
            break
    factors = []
    for k in range(1, len(d)):
        if d[k] == 0:
            break
        factors.append(sp.Integer(d[k] / d[k-1]))
    return factors


def main():
    host = grow(10)
    mats = {}
    for label, factor in [('T1', 'a'), ('T2', 'B'), ('T3', 'A'), ('T5', 'Bab')]:
        mats[label] = analyze(factor, host)
        cp = sp.factor(mats[label].charpoly(X).as_expr())
        assert cp == sp.factor(CHARPOLY), f"{label} charpoly mismatch"

    print("=" * 78)
    print("B533 audit 4b — GL(4,Z) conjugacy: decisive test")
    print("=" * 78)

    A = mats['T1']
    verdicts = {}
    for label in ('T2', 'T3', 'T5'):
        B = mats[label]
        print(f"\n─── T1 ~ {label} ───")
        vecs = integer_solution_basis(A, B)
        print(f"  solution space dim: {len(vecs)}")

        inv = invariant_factors(vecs)
        print(f"  invariant factors of the basis lattice: {inv}")
        saturated = all(f == 1 for f in inv)
        print(f"  basis lattice saturated: {saturated}")
        if not saturated:
            print("  WARNING: basis not saturated — obstruction test would be"
                  " unreliable; skipping to box search only")

        basis_mats = [sp.Matrix(4, 4, lambda i, j, v=v: v[4*i + j]) for v in vecs]

        # mod-2 obstruction (valid only if saturated)
        odd_possible = False
        for c in iprod((0, 1), repeat=4):
            if all(ci == 0 for ci in c):
                continue
            U = sum((ci * bm for ci, bm in zip(c, basis_mats)), sp.zeros(4, 4))
            if U.det() % 2 == 1:
                odd_possible = True
                break
        print(f"  mod-2: odd det achievable: {odd_possible}")

        if saturated and not odd_possible:
            print(f"  ==> det(U) is ALWAYS EVEN on the full integer solution"
                  f" lattice.")
            print(f"  ==> NO unimodular conjugator exists.")
            print(f"  ==> T1 and {label} are NOT GL(4,Z)-conjugate  [PROVEN]")
            verdicts[label] = 'NOT_CONJUGATE_PROVEN'
            continue

        # mod-3 check too (det = +-1 needs det != 0 mod 3)
        nonzero_mod3 = False
        for c in iprod((0, 1, 2), repeat=4):
            if all(ci == 0 for ci in c):
                continue
            U = sum((ci * bm for ci, bm in zip(c, basis_mats)), sp.zeros(4, 4))
            if U.det() % 3 in (1, 2):
                nonzero_mod3 = True
                break
        print(f"  mod-3: det != 0 mod 3 achievable: {nonzero_mod3}")
        if saturated and not nonzero_mod3:
            print(f"  ==> NOT GL(4,Z)-conjugate  [PROVEN via mod 3]")
            verdicts[label] = 'NOT_CONJUGATE_PROVEN'
            continue

        # extended box search, chunked numpy batched dets
        Bs = np.array([np.array(bm.tolist(), dtype=np.float64)
                       for bm in basis_mats])
        R = 20
        rng = np.arange(-R, R + 1)
        found = None
        grid = np.array(np.meshgrid(rng, rng, rng, rng,
                                    indexing='ij')).reshape(4, -1).T
        CH = 200000
        for start in range(0, len(grid), CH):
            cs = grid[start:start + CH].astype(np.float64)
            Us = np.einsum('ck,kij->cij', cs, Bs)
            dets = np.abs(np.linalg.det(Us))
            hits = np.where(np.abs(dets - 1.0) < 1e-5)[0]
            for h in hits:
                c = grid[start + h]
                Uex = sum((int(ci) * bm for ci, bm in zip(c, basis_mats)),
                          sp.zeros(4, 4))
                if abs(Uex.det()) == 1 and (Uex*A - B*Uex).is_zero_matrix:
                    found = (list(map(int, c)), Uex)
                    break
            if found:
                break
        if found:
            c, Uex = found
            print(f"  UNIMODULAR CONJUGATOR: c={c}, det={Uex.det()}")
            print(f"  U = {Uex.tolist()}")
            print(f"  ==> T1 and {label} ARE GL(4,Z)-conjugate  [banked claim"
                  f" REFUTED]")
            verdicts[label] = 'CONJUGATE'
        else:
            print(f"  no unimodular combo found for |c| <= {R}")
            verdicts[label] = 'INCONCLUSIVE'

    print("\n" + "=" * 78)
    print("VERDICTS")
    print("=" * 78)
    for label, v in verdicts.items():
        print(f"  T1 ~ {label}: {v}")


if __name__ == '__main__':
    main()
