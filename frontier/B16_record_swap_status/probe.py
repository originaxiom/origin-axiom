"""Frontier probe B16 -- status of the record-swap symmetry.

This checks whether P is forced by existing structure or by adding an exchange
symmetry requirement. It does not promote a claim.
"""

from __future__ import annotations

import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B16 -- Record-swap symmetry status")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md section 5)")
    print("=" * 72)

    L = sp.Matrix([[1, 1], [0, 1]])
    R = sp.Matrix([[1, 0], [1, 1]])
    A = L * R
    P = sp.Matrix([[0, 1], [1, 0]])
    I = sp.eye(2)

    print("\n[1] P exchanges the primitive shears")
    assert P.det() == -1
    assert P**2 == I
    assert P * L * P.inv() == R
    assert P * R * P.inv() == L
    print("    P^2=I, det(P)=-1")
    print("    P L P^-1 = R and P R P^-1 = L")

    print("\n[2] Bounded exact search: involutions exchanging L and R")
    swap_involutions = []
    for a in range(-6, 7):
        for b in range(-6, 7):
            for c in range(-6, 7):
                for d in range(-6, 7):
                    X = sp.Matrix([[a, b], [c, d]])
                    if X.det() in (-1, 1) and X**2 == I and X * L * X.inv() == R:
                        swap_involutions.append(X)
    assert swap_involutions == [-P, P]
    print(f"    solutions = {[x.tolist() for x in swap_involutions]}")
    print("    P is unique up to sign once exchange symmetry is required")

    print("\n[3] Automorphisms of the primitive pair {L,R}")
    pair_automorphisms = []
    for a in range(-6, 7):
        for b in range(-6, 7):
            for c in range(-6, 7):
                for d in range(-6, 7):
                    X = sp.Matrix([[a, b], [c, d]])
                    if X.det() not in (-1, 1):
                        continue
                    XL = X * L * X.inv()
                    XR = X * R * X.inv()
                    if XL == L and XR == R:
                        pair_automorphisms.append((X, "fix"))
                    elif XL == R and XR == L:
                        pair_automorphisms.append((X, "swap"))
    expected = [(-I, "fix"), (-P, "swap"), (P, "swap"), (I, "fix")]
    assert pair_automorphisms == expected
    print(f"    automorphisms = {[(x.tolist(), kind) for x, kind in pair_automorphisms]}")

    print("\n[4] Relation to order choice")
    RL = R * L
    assert P * A * P == RL
    assert A != RL
    assert sp.trace(A) == sp.trace(RL) == 3
    print("    P A P = RL")
    print("    A and RL are conjugate but based-distinct")

    print("\n[5] Relation to half-step")
    F = L * P
    assert F**2 == A
    assert (-F) ** 2 == A
    print("    F=L P and F^2=A")
    print("    sign ambiguity in P only gives +/-F")

    print("\n[6] Minimality controls for weaker conditions")
    candidates = []
    for a in range(-8, 9):
        for b in range(-8, 9):
            for c in range(-8, 9):
                for d in range(-8, 9):
                    X = sp.Matrix([[a, b], [c, d]])
                    if X.det() in (-1, 1):
                        candidates.append(X)

    det_minus_involutions = [
        X for X in candidates if X.det() == -1 and X**2 == I
    ]
    assert len(det_minus_involutions) > 2
    print(f"    det=-1 involution alone leaves {len(det_minus_involutions)} candidates")

    maps_L_to_R_up_to_orientation = [
        X
        for X in det_minus_involutions
        if X * L * X.inv() in (R, R.inv())
    ]
    assert maps_L_to_R_up_to_orientation == [-P, P]
    print("    det=-1 involution mapping L to R^(+/-1) gives +/-P")

    conjugates_A_to_RL = [
        X for X in det_minus_involutions if X * A * X.inv() == R * L
    ]
    assert conjugates_A_to_RL == [-P, P]
    print("    det=-1 involution conjugating A to RL gives +/-P")

    half_step_factors = [X for X in candidates if (L * X) ** 2 == A]
    assert half_step_factors == [-P, P]
    print("    requiring (L X)^2=A gives +/-P even without separately asking X^2=I")

    time_reversals = [
        X
        for X in det_minus_involutions
        if X * A * X.inv() == A.inv()
    ]
    assert len(time_reversals) > 2
    print(f"    det=-1 involutive time reversal of A leaves {len(time_reversals)} candidates")

    print("\nVerdict: STALLED")
    print("P is unique if exchange symmetry is required; exchange symmetry is not derived.")


if __name__ == "__main__":
    main()
