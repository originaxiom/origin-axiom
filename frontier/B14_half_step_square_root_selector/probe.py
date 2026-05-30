"""Frontier probe B14 -- half-step square-root selector.

This probe checks whether the Fibonacci half-step F is forced once the selected
core A is fixed. It is exact algebra only; no claim is promoted.
"""

from __future__ import annotations

import sympy as sp


def L_shear(k: int | sp.Symbol) -> sp.Matrix:
    return sp.Matrix([[1, k], [0, 1]])


def R_shear(k: int | sp.Symbol) -> sp.Matrix:
    return sp.Matrix([[1, 0], [k, 1]])


def main() -> None:
    print("=" * 72)
    print("B14 -- Half-step square-root selector")
    print("SPECULATIVE: observations only, not claims (GOVERNANCE.md section 5)")
    print("=" * 72)

    L = L_shear(1)
    R = R_shear(1)
    A = L * R
    P = sp.Matrix([[0, 1], [1, 0]])
    F = L * P

    print("\n[1] Record swap and Fibonacci half-step")
    assert P**2 == sp.eye(2)
    assert P * L * P == R
    assert F == sp.Matrix([[1, 1], [1, 0]])
    assert F.det() == -1
    assert F.trace() == 1
    assert F**2 == A
    assert (-F) ** 2 == A
    print(f"    P = {P.tolist()}, P^2 = I")
    print("    P L P = R")
    print(f"    F = L P = {F.tolist()}, det(F)={F.det()}, tr(F)={F.trace()}")
    print("    F^2 = A")

    print("\n[2] Uniqueness of GL(2,Z) square roots of A")
    # If X^2=A, the eigenvalues of X must square to phi^2 and phi^-2.
    # Integer trace excludes det=+1 roots, which would have trace +/-sqrt(5).
    # With det=-1 and trace s=+/-1, Cayley-Hamilton gives:
    # X^2 - s X - I = 0, so A = s X + I, hence X = s(A-I).
    roots = []
    for trace in (1, -1):
        candidate = trace * (A - sp.eye(2))
        assert candidate**2 == A
        assert candidate.det() == -1
        assert candidate.trace() == trace
        roots.append(candidate)
    assert roots == [F, -F]
    print(f"    roots from Cayley-Hamilton = {[root.tolist() for root in roots]}")
    print("    no det=+1 integer-trace square root exists")

    print("\n[3] Bounded brute-force control")
    brute_roots = []
    for x11 in range(-5, 6):
        for x12 in range(-5, 6):
            for x21 in range(-5, 6):
                for x22 in range(-5, 6):
                    X = sp.Matrix([[x11, x12], [x21, x22]])
                    if X.det() in (-1, 1) and X**2 == A:
                        brute_roots.append(X)
    assert brute_roots == [-F, F]
    print(f"    bounded roots in [-5,5]^4 = {[root.tolist() for root in brute_roots]}")

    print("\n[4] General mixed closures B(a,b)")
    a, b, s = sp.symbols("a b s", positive=True, integer=True)
    B = L_shear(a) * R_shear(b)
    assert B == sp.Matrix([[1 + a * b, a], [b, 1]])
    # If X^2=B and det(X)=-1, then tr(B)=tr(X)^2+2. Since tr(B)=2+ab,
    # the square-root trace satisfies s^2=ab, and CH gives X=(B-I)/s.
    root_from_B = (B - sp.eye(2)) / s
    root_candidate = sp.Matrix([[s, a / s], [b / s, 0]])
    assert root_from_B == sp.Matrix([[a * b / s, a / s], [b / s, 0]])
    # The top-left entry becomes s after imposing the square-root trace
    # condition s^2=ab.
    assert sp.simplify(root_from_B[0, 0].subs(a * b, s**2) - root_candidate[0, 0]) == 0
    print("    if X^2=B(a,b), det(X)=-1, and tr(X)=s, then s^2=ab")
    print("    candidate X=(B-I)/s = [[s,a/s],[b/s,0]]")
    print("    over positive integers, integrality forces a=b=s")

    for k in range(1, 6):
        Fk = L_shear(k) * P
        Bkk = L_shear(k) * R_shear(k)
        assert Fk**2 == Bkk
        assert Fk == sp.Matrix([[k, 1], [1, 0]])
        print(f"    k={k}: (L_k P)^2 = B(k,k) = {Bkk.tolist()}")

    print("\n[5] Combined selector status")
    print("    half-step existence selects balanced closures a=b")
    print("    torsion-free/minimality selects ab=1")
    print("    together: a=b=1, F=L P, F^2=A")

    print("\nVerdict: STALLED")
    print("The half-step is unique if record-swap P is admitted; P itself is not derived.")


if __name__ == "__main__":
    main()
