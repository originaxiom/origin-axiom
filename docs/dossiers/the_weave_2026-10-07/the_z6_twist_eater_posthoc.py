#!/usr/bin/env python3
"""W29, POST HOC (after the read-out of the_z6_twist_eater.py): what the 4 + 2 pieces of the 6 are.

The rule (W29_RULE.md) named the lift of -I as the parity |k> -> |-k> and the pieces as its eigenspaces. The read-out
found both false while the structure held (commutant 2, pieces of dimension 4 and 2). This reads, after the fact:
  P1 the lift of the automorphism -I (a -> a^-1, b -> b^-1): its support, its form (a phase times a reflection
     |k> -> |c - k>), its eigenspaces, and whether the lifts of L and R keep them;
  P2 the lift of (L R^-1 L)^2, which is -I composed with conjugation by a b^-1 (the qubit computation of W28): it equals
     a scalar times (A B^-1) U_{-I}; its support (a reflection); its eigenspaces, and whether they are the pieces.

    python3 the_z6_twist_eater_posthoc.py   ->  the_z6_twist_eater_posthoc.json beside it
"""
import json
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import the_z6_twist_eater as Z  # noqa: E402

inv = np.linalg.inv


def eigenspaces(U):
    ev, V = np.linalg.eig(U)
    groups = []
    for i, e in enumerate(ev):
        for gr in groups:
            if abs(gr[0] - e) < 1e-6:
                gr[1].append(i)
                break
        else:
            groups.append([e, [i]])
    out = []
    for _, idx in groups:
        Q, _ = np.linalg.qr(V[:, idx])
        out.append(Q @ Q.conj().T)
    return out


def reflection_centre(U):
    """c with U = D R_c, D diagonal and R_c |k> = |c - k>, or None"""
    for c in range(6):
        R = np.zeros((6, 6))
        for k in range(6):
            R[(c - k) % 6, k] = 1
        D = U @ R.T
        if np.allclose(D, np.diag(np.diag(D)), atol=1e-9):
            return c, D
    return None, None


def run():
    A, B = Z.A, Z.B
    UL = Z.intertwiners(A, A @ B)[0]
    UR = Z.intertwiners(A @ B, B)[0]
    UI = Z.intertwiners(inv(A), inv(B))[0]
    res = {"status": "POST HOC: after the read-out of the_z6_twist_eater.py (W29_RULE.md committed 37441028)"}
    c, D = reflection_centre(UI)
    d = np.diag(D) / np.diag(D)[0]
    is_clock = bool(np.allclose(d, np.diag(Z.C6), atol=1e-9))
    sp1 = eigenspaces(UI)
    res["P1 the lift of -I"] = {
        "a phase times the reflection |k> -> |c - k>, with c": c,
        "the phase is the clock C (U_{-I} = C R_c up to a scalar)": is_clock,
        "its eigenspace dimensions": sorted(int(round(np.trace(P).real)) for P in sp1),
        "the lifts of L and R keep them": bool(all(np.allclose(U @ P, P @ U, atol=1e-8) for U in (UL, UR) for P in sp1))}
    W2 = np.linalg.matrix_power(UL @ inv(UR) @ UL, 2)
    cand = A @ inv(B) @ UI
    i, j = np.unravel_index(np.argmax(abs(W2)), W2.shape)
    same = bool(np.allclose(W2, W2[i, j] / cand[i, j] * cand, atol=1e-8))
    c2, _ = reflection_centre(W2)
    sp2 = eigenspaces(W2)
    res["P2 the lift of (L R^-1 L)^2 = -I composed with conjugation by a b^-1"] = {
        "equals a scalar times (A B^-1) U_{-I}": same,
        "a phase times the reflection |k> -> |c - k>, with c": c2,
        "its eigenspace dimensions": sorted(int(round(np.trace(P).real)) for P in sp2),
        "the lifts of L and R keep them (they are the pieces)": bool(
            all(np.allclose(U @ P, P @ U, atol=1e-8) for U in (UL, UR) for P in sp2))}
    res["reading"] = ("the moves contain -I only composed with an inner automorphism; the lift of (L R^-1 L)^2, a "
                      "reflection with two fixed points, splits the 6 as 4 + 2, and those are the pieces. The bare "
                      "-I's lift is a reflection without fixed points, with two 3-dimensional eigenspaces that the moves "
                      "exchange. The rule's naming was wrong; the computed structure and every index set stand")
    return res


if __name__ == "__main__":
    out = run()
    with open(HERE / "the_z6_twist_eater_posthoc.json", "w") as f:
        json.dump(out, f, indent=1, ensure_ascii=False, default=str)
    print(json.dumps(out, indent=1, ensure_ascii=False, default=str))
