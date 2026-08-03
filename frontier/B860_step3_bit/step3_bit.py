#!/usr/bin/env python3
"""B860 -- the step-3 trit is a BIT, the bit maps into the theta-even sector, and it has a
computed asymmetry that selects the SM under one named principle.

Three computations, each independent:
  (1) Borel-de Siebenthal on the extended A4 diagram: two-node removals give exactly
      {SU(4)xU(1), SM}; SU(3)xU(1)^2 needs three nodes -- one level deeper. TRIT -> BIT.
  (2) theta = the fold restricted to SU(5) (X -> -X^T). All four subalgebras theta-stable;
      cores so(5)=B2 <- {so(4), so(3)xso(2)} = EXACTLY the two maximal-rank subalgebras of B2.
      The bit maps to the B2 Borel-de Siebenthal bit in the forced (even) sector.
  (3) The abelian factors are theta-ODD (observer-dial, per the ledger's catalog). Stripping
      them, the generation (10+5bar in the 27) COLLAPSES to vector-like on the SU(4) side
      (6 self-dual, 4 pairs 4bar) and STAYS CHIRAL on the SM side ((3,2) unpaired).

THE IMPORT, named: "matter chirality must survive the dial". Under it the SM is unique.
Mathematics scope. Nothing reaches CLAIMS.md; Gate 5 untouched.
"""
import json
import os
from collections import Counter
from itertools import combinations

import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
N = 5


# ---------------------------------------------------------------- (1) the cycle enumeration
def bds_two_node_patterns():
    segs = set()
    for pair in combinations(range(5), 2):
        keep = [i for i in range(5) if i not in pair]
        used, parts = set(), []
        for start in keep:
            if start in used:
                continue
            seg = [start]
            used.add(start)
            nxt = (start + 1) % 5
            while nxt in keep and nxt not in used:
                seg.append(nxt); used.add(nxt); nxt = (nxt + 1) % 5
            prv = (start - 1) % 5
            while prv in keep and prv not in used:
                seg = [prv] + seg; used.add(prv); prv = (prv - 1) % 5
            parts.append(len(seg))
        segs.add(tuple(sorted(parts, reverse=True)))
    return sorted(segs, reverse=True)


# ---------------------------------------------------------------- (2) theta-cores, explicit
def block_su(idx):
    B = []
    for a in idx:
        for b in idx:
            if a != b:
                E = np.zeros((N, N)); E[a, b] = 1; B.append(E)
    for k in range(len(idx) - 1):
        H = np.zeros((N, N)); H[idx[k], idx[k]] = 1; H[idx[k + 1], idx[k + 1]] = -1
        B.append(H)
    return B


def u1(diag):
    return [np.diag(np.array(diag, dtype=float))]


def sl5_basis():
    B = []
    for i in range(N):
        for j in range(N):
            if i != j:
                E = np.zeros((N, N)); E[i, j] = 1; B.append(E)
    for i in range(N - 1):
        H = np.zeros((N, N)); H[i, i] = 1; H[i + 1, i + 1] = -1; B.append(H)
    return B


def theta(X):
    return -X.T


def theta_split(basis):
    A = np.array([M.flatten() for M in basis]).T
    Q, _ = np.linalg.qr(A)
    P = Q @ Q.conj().T
    stable = all(np.allclose(P @ theta(M).flatten(), theta(M).flatten(), atol=1e-10)
                 for M in basis)
    k = len(basis)
    T = np.zeros((k, k))
    for j, M in enumerate(basis):
        coeff, *_ = np.linalg.lstsq(A, theta(M).flatten(), rcond=None)
        T[:, j] = coeff
    ev = np.linalg.eigvals(T)
    plus = int(sum(1 for e in ev if abs(e - 1) < 1e-8))
    minus = int(sum(1 for e in ev if abs(e + 1) < 1e-8))
    return stable, plus, minus


# ---------------------------------------------------------------- (3) the dial-stripped generation
CONJ = {"6": "6", "4": "4bar", "4bar": "4", "1": "1",
        "(3,2)": "(3bar,2)", "(3bar,2)": "(3,2)", "(3,1)": "(3bar,1)",
        "(3bar,1)": "(3,1)", "(1,2)": "(1,2)", "(1,1)": "(1,1)"}


def chiral_residue(gen):
    c = Counter(gen)
    residue = {}
    for r, n in c.items():
        cb = CONJ[r]
        if cb == r:
            continue
        if n > c[cb]:
            residue[r] = n - c[cb]
    return residue


def main():
    res = {}

    res["bds_patterns"] = [list(p) for p in bds_two_node_patterns()]
    res["trit_is_a_bit"] = (res["bds_patterns"] == [[3], [2, 1]])

    cases = {
        "SU(5)": sl5_basis(),
        "SU(4)xU(1)": block_su([0, 1, 2, 3]) + u1([1, 1, 1, 1, -4]),
        "SM": block_su([0, 1, 2]) + block_su([3, 4]) + u1([2, 2, 2, -3, -3]),
        "SU(3)xU(1)^2": block_su([0, 1, 2]) + u1([2, 2, 2, -3, -3]) + u1([0, 0, 0, 1, -1]),
    }
    res["theta"] = {}
    for lab, B in cases.items():
        stable, even, odd = theta_split(B)
        res["theta"][lab] = dict(dim=len(B), stable=stable, even=even, odd=odd)
    res["cores_are_B2_bds_pair"] = (res["theta"]["SU(4)xU(1)"]["even"] == 6
                                    and res["theta"]["SM"]["even"] == 4
                                    and res["theta"]["SU(5)"]["even"] == 10)

    gen_su4 = ["6", "4", "4bar", "1"]
    gen_sm = ["(3,2)", "(3bar,1)", "(1,1)", "(3bar,1)", "(1,2)"]
    res["generation_su4_residue"] = chiral_residue(gen_su4)
    res["generation_sm_residue"] = chiral_residue(gen_sm)
    res["su4_collapses"] = (res["generation_su4_residue"] == {})
    res["sm_stays_chiral"] = (res["generation_sm_residue"] != {})
    res["import_named"] = "matter chirality must survive the dial (theta-odd abelian factors)"

    res["addendum"] = addendum()

    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1, sort_keys=True)

    print("=" * 74)
    print("B860 -- the step-3 bit")
    print("=" * 74)
    print(f"\n  (1) two-node removals on the A4 cycle: {res['bds_patterns']}"
          f"   -> TRIT IS A BIT: {res['trit_is_a_bit']}")
    print(f"\n  (2) theta-splits (dim / stable / even / odd):")
    for lab, t in res["theta"].items():
        print(f"      {lab:14} {t['dim']:>3} / {t['stable']} / {t['even']} / {t['odd']}")
    print(f"      cores = the B2 Borel-de Siebenthal pair: {res['cores_are_B2_bds_pair']}")
    print(f"\n  (3) dial-stripped generation:")
    print(f"      SU(4) side residue: {res['generation_su4_residue'] or 'NONE (vector-like)'}")
    print(f"      SM side residue   : {res['generation_sm_residue']}")
    print(f"\n  under the named import, the SM is the unique survivor: "
          f"{res['su4_collapses'] and res['sm_stays_chiral']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


# ================================================================ ADDENDUM (same day)
# The dichotomy upgraded from a multiset argument to an exhibited intertwiner + a Schur proof.
def intertwiner_J6():
    """epsilon: Lambda^2(4) -> Lambda^2(4)* -- the load-bearing piece of J: G -> Gbar."""
    from itertools import combinations as _comb
    pairs = list(_comb(range(4), 2))

    def eps4(i, j, k, l):
        perm = [i, j, k, l]
        if len(set(perm)) < 4:
            return 0
        s, p = 1, perm[:]
        for a in range(4):
            for b in range(a + 1, 4):
                if p[a] > p[b]:
                    p[a], p[b] = p[b], p[a]
                    s = -s
        return s

    J = np.zeros((6, 6))
    for a, (i, j) in enumerate(pairs):
        for b, (k, l) in enumerate(pairs):
            J[b, a] = eps4(i, j, k, l)
    return J, pairs


def rho_lambda2(X, pairs):
    M = np.zeros((6, 6), dtype=complex)
    for a, (i, j) in enumerate(pairs):
        for k in range(4):
            if k != j:
                key = tuple(sorted((k, j)))
                M[pairs.index(key), a] += (1 if k < j else -1) * X[k, i]
            if k != i:
                key = tuple(sorted((i, k)))
                M[pairs.index(key), a] += (1 if i < k else -1) * X[k, j]
    return M


def addendum():
    rng = np.random.default_rng(3)
    J, pairs = intertwiner_J6()
    worst = 0.0
    for _ in range(20):
        X = rng.normal(size=(4, 4)) + 1j * rng.normal(size=(4, 4))
        X -= np.trace(X) / 4 * np.eye(4)
        worst = max(worst, float(np.abs(J @ rho_lambda2(X, pairs)
                                        - (-rho_lambda2(X, pairs).T) @ J).max()))
    det = abs(float(np.linalg.det(J)))
    # SM side: Schur -- multiset mismatch, no J can exist
    mult_G = {"(3,2)": 1, "(3bar,1)": 2, "(1,2)": 1, "(1,1)": 1}
    mult_Gbar = {"(3bar,2)": 1, "(3,1)": 2, "(1,2)": 1, "(1,1)": 1}
    mismatches = sorted(set(mult_G) ^ set(mult_Gbar))
    return dict(J6_equivariance_dev=worst, J6_det=det,
                sm_mismatched_irreps=mismatches,
                dichotomy=(worst < 1e-12 and det == 1.0 and len(mismatches) > 0))
