"""B17 -- alternation/persistence selector."""

from __future__ import annotations

import itertools
import sympy as sp


def main() -> None:
    print("=" * 72)
    print("B17 -- Alternation/persistence selector")
    print("SPECULATIVE: observations only, not claims")
    print("=" * 72)

    L = sp.Matrix([[1, 1], [0, 1]])
    R = sp.Matrix([[1, 0], [1, 1]])
    P = sp.Matrix([[0, 1], [1, 0]])
    I = sp.eye(2)
    A = L * R
    RL = R * L
    alphabet = {"L": L, "R": R, "P": P}

    print("\n[1] Same-record repetition remains parabolic")
    for n in range(1, 8):
        assert sp.trace(L**n) == 2
        assert sp.trace(R**n) == 2
    print("    L^n and R^n have trace 2 for n=1..7")

    print("\n[2] Original filters select LR/RL first")
    length2_hits = []
    for word in ("".join(w) for w in itertools.product("LR", repeat=2)):
        M = I
        for ch in word:
            M *= alphabet[ch]
        if M.det() == 1 and abs(sp.trace(M)) > 2 and abs((M - I).det()) == 1:
            length2_hits.append((word, M))
    assert [(w, M.tolist()) for w, M in length2_hits] == [("LR", A.tolist()), ("RL", RL.tolist())]
    print("    length-2 carried filters select LR and RL")

    print("\n[3] Adding P creates spellings, not new sectors")
    words_for_A = []
    words_for_RL = []
    for n in range(1, 5):
        for chars in itertools.product("LRP", repeat=n):
            word = "".join(chars)
            M = I
            for ch in word:
                M *= alphabet[ch]
            if M == A:
                words_for_A.append(word)
            if M == RL:
                words_for_RL.append(word)
    assert "LPLP" in words_for_A
    assert "RPRP" in words_for_RL
    assert "LR" in words_for_A
    assert "RL" in words_for_RL
    print(f"    words for A up to length 4 include {words_for_A}")
    print(f"    words for RL up to length 4 include {words_for_RL}")

    print("\n[4] Operational half-step selector")
    half_step_solutions = []
    for a in range(-6, 7):
        for b in range(-6, 7):
            for c in range(-6, 7):
                for d in range(-6, 7):
                    X = sp.Matrix([[a, b], [c, d]])
                    if X.det() in (-1, 1) and (L * X) ** 2 == A:
                        half_step_solutions.append(X)
    assert half_step_solutions == [-P, P]
    print("    (L X)^2=A selects X=+/-P")

    print("\nVerdict: STALLED")
    print("Alternation refactors A through a half-step; it does not remove the half-step assumption.")


if __name__ == "__main__":
    main()
