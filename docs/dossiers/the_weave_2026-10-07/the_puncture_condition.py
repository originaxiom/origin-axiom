#!/usr/bin/env python3
"""W22 of the weave: THE END CONDITION THE WEAVE FIXES. The fibre's Dirac problem at the common point, up to the hand.

The fibre's Dirac operator twisted by W = sum_p chi_p (x) rho_Q needs a boundary condition at the puncture, where the
holonomy is -1 (GENESIS GAP2's end condition). With the puncture's holonomy central, each parity block has a
two-dimensional space C^2 of local solutions, and a self-adjoint condition that keeps the 2d chirality is a subspace
Lambda_+ of C^2: the directions allowed to be singular (|z|^(-1/2)) in chirality +, the rest singular in chirality -.
The block's index is dim Lambda_+ - 1: -1, 0 or +1 (Riemann-Roch: the extension's degree; Lambda_+ = C^2 is the one
whose holomorphic sections are W21's forms theta_3(z | 2 tau) / sqrt(theta_1(z | tau))).

The weave fixes it. The moves act on the local solutions at the puncture through their lifts. If those lifts act
irreducibly on C^2, the only conditions every move keeps are Lambda_+ = 0 or C^2 in every block, so the index is -3 or
+3, never 0. A vector-like condition (index 0) needs a line in each block. The spin structure is fixed too: the odd one
is the only spin structure every move fixes, and with it the three blocks see the three even ones.

What this computes:
  (1) the group the lifts of L and R generate, and its commutant on C^2;
  (2) for each parity block, the lifts of the moves (words in L, R to length 6) that fix the block, and their commutant
      on C^2;
  (3) for the threads to length 6, the eigenlines of each lift (one thread's lift leaves a line);
  (4) the moves' action on the four spin structures (quadratic forms on the records mod 2): which ones every move fixes.

    python3 the_puncture_condition.py   ->  the_puncture_condition.json beside it
"""
import itertools
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_chiral_triplet as CT  # noqa: E402
import the_common_point as CP  # noqa: E402
import the_spin_room as SR  # noqa: E402


def word_aut(w):
    phi = {1: [1], 2: [2]}
    for c in w:
        phi = CP.compose(phi, CP.AUT[c])
    return phi


def commutant_dim(mats):
    rows = [np.kron(g.T, np.eye(2)) - np.kron(np.eye(2), g) for g in mats]
    s = np.linalg.svd(np.vstack(rows), compute_uv=False)
    return int(sum(s < 1e-9))


def closure(gens):
    key = lambda M: tuple(np.round(M.flatten(), 6))  # noqa: E731
    G = {key(np.eye(2)): np.eye(2, dtype=complex)}
    fr = list(G.values())
    while fr:
        nx = []
        for A in fr:
            for g in gens:
                B = A @ g
                if key(B) not in G:
                    G[key(B)] = B
                    nx.append(B)
        fr = nx
    return G


def spin_structures():
    """quadratic forms q on (Z/2)^2 with q(x + y) = q(x) + q(y) + x.y, as (q(1,0), q(0,1)); Arf = majority value"""
    out = {}
    for q10, q01 in itertools.product((0, 1), repeat=2):
        q11 = (q10 + q01 + 1) % 2
        out[(q10, q01)] = {"values on (1,0), (0,1), (1,1)": [q10, q01, q11],
                           "Arf invariant": int(q10 + q01 + q11 >= 2)}
    return out


def act_on_q(M, q):
    """(q o M^-1) as (q(1,0), q(0,1)); M an integer matrix acting on column vectors of the records mod 2"""
    Mi = np.round(np.linalg.inv(M)).astype(int) % 2
    def qv(v):
        v = tuple(int(x) % 2 for x in v)
        if v == (0, 0):
            return 0
        q10, q01 = q
        return {(1, 0): q10, (0, 1): q01, (1, 1): (q10 + q01 + 1) % 2}[v]
    return (qv(Mi @ np.array([1, 0])), qv(Mi @ np.array([0, 1])))


def run():
    res = {}
    lifts = [SR.qmat(g) for m in ("L", "R") for g in CP.extend(CP.AUT[m])]
    G = closure(lifts)
    res["(1) the group of the lifts of L and R: order"] = len(G)
    res["(1) its commutant on the local solutions C^2 (1 = irreducible)"] = commutant_dim(lifts)
    blocks = {}
    for u in CT.PAR:
        stab = []
        for n in range(1, 7):
            for t in itertools.product("LR", repeat=n):
                phi = word_aut(t)
                if CT.u_after(u, phi) == u:
                    stab += [SR.qmat(g) for g in CP.extend(phi)]
        blocks[str(u)] = {"lifts of the moves fixing the block (words to length 6)": len(stab),
                          "commutant on C^2": commutant_dim(stab),
                          "order of the group they generate": len(closure(stab))}
    res["(2) each parity block's stabilizer"] = blocks
    threads = {}
    for n in range(2, 7):
        for t in itertools.product("LR", repeat=n):
            w = "".join(t)
            if "L" not in w or "R" not in w or w != min(w[i:] + w[:i] for i in range(n)):
                continue
            for sign in (1, -1):
                phi = CP.word_aut(w, sign)
                evs = [np.linalg.eigvals(SR.qmat(g)) for g in CP.extend(phi)]
                threads[("+" if sign > 0 else "-") + w] = bool(all(abs(e[0] - e[1]) > 1e-9 for e in evs))
    res["(3) threads to length 6 whose every lift has two distinct eigenlines (a line a vector-like condition can use)"] = {
        "threads": len(threads), "with distinct eigenlines": sum(threads.values()),
        "without (lift +-1 or a scalar)": sorted(k for k, v in threads.items() if not v)}
    qs = spin_structures()
    fixed = []
    for q in qs:
        if all(act_on_q(np.array(CP.MAT[m]), q) == q for m in ("L", "R", "-I")):
            fixed.append(q)
    res["(4) the spin structures"] = {str(k): v for k, v in qs.items()}
    res["(4) fixed by every move"] = [str(q) for q in fixed]
    res["(4) the fixed one is odd (Arf 1)"] = bool(len(fixed) == 1 and qs[fixed[0]]["Arf invariant"] == 1)
    ok = (len(G) == 48 and res["(1) its commutant on the local solutions C^2 (1 = irreducible)"] == 1
          and all(b["commutant on C^2"] == 1 for b in blocks.values()) and res["(4) the fixed one is odd (Arf 1)"])
    res["the weave fixes the condition up to the hand (Lambda_+ = 0 or C^2 in every block; index -3 or +3)"] = bool(ok)
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_puncture_condition.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False)
    print(json.dumps(out, indent=1, ensure_ascii=False))
