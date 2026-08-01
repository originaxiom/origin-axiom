#!/usr/bin/env python3
"""P5 §2.2 — does the abelianization see the Hopf coordinate? COMPUTED, not asserted.

REWRITTEN 2026-08-01 after the Phase 3 adversarial pass (B847). The previous version computed
NOTHING: it built both matrices from the SAME literal argument, never parsed the image words, and
its "witnesses" were hardcoded tuples compared for inequality and a print of the string "-> True".
Every assertion was true by construction. That is MB12 vacuity in the artifact certifying the
sentence the draft called load-bearing.

This version parses the image WORDS, derives the matrices from them, and carries negative controls
so the checks can fail.

NOTE ON SCOPE (Phase 3): the separation this exhibits is confined to det 0, because
det != 0 => injective (Hopf dichotomy: non-injective => rank <= 1 image => rank <= 1 matrix).
It therefore licenses exactly one statement -- the stratum-3 vs stratum-4 cut is not toral -- and
NOT any claim about the classification as a whole.
"""
import sympy as sp


def reduce_word(w):
    """Free reduction of a word given as a string: lowercase = generator, uppercase = inverse."""
    out = []
    for c in w:
        if out and out[-1].swapcase() == c:
            out.pop()
        else:
            out.append(c)
    return "".join(out)


def exponent_sums(w):
    """(a-exponent, b-exponent) of a freely reduced word."""
    w = reduce_word(w)
    return (sum((1 if c == "a" else -1) for c in w if c in "aA"),
            sum((1 if c == "b" else -1) for c in w if c in "bB"))


def abelianization_of(image_a, image_b):
    """Derive the matrix FROM the image words -- not from a literal."""
    ea, eb = exponent_sums(image_a), exponent_sums(image_b)
    return sp.Matrix([[ea[0], eb[0]], [ea[1], eb[1]]])


def substitute(word, image_a, image_b):
    """Apply the endomorphism a->image_a, b->image_b to a word, then freely reduce."""
    out = []
    for c in word:
        if c == "a":
            out.append(image_a)
        elif c == "A":
            out.append(image_a.swapcase()[::-1])
        elif c == "b":
            out.append(image_b)
        elif c == "B":
            out.append(image_b.swapcase()[::-1])
    return reduce_word("".join(out))


# ---- the pair -------------------------------------------------------------------------------
TM_A, TM_B = "ab", "ba"        # Thue-Morse, stratum 3 -- injective
S4_A, S4_B = "ab", "ab"        # stratum 4 -- NOT injective
TM = abelianization_of(TM_A, TM_B)
S4 = abelianization_of(S4_A, S4_B)

# second pair, at a DIFFERENT det-0 matrix, against the cherry-picking objection
P1_A, P1_B = "aa", "aa"             # non-injective
P2_A, P2_B = "aa", "aaabAB"         # a^2[a,b]; injective
PSI1 = abelianization_of(P1_A, P1_B)
PSI2 = abelianization_of(P2_A, P2_B)

# NEGATIVE CONTROL: a pair that must NOT share an abelianization, so `same` can come back False
CTRL_A, CTRL_B = "ab", "a"          # metallic m=1
CTRL = abelianization_of(CTRL_A, CTRL_B)


def main():
    print("matrices DERIVED from the image words (not from literals):")
    for name, (ia, ib, M) in {
        "TM   a->ab, b->ba": (TM_A, TM_B, TM),
        "s4   a->ab, b->ab": (S4_A, S4_B, S4),
        "psi1 a->aa, b->aa": (P1_A, P1_B, PSI1),
        "psi2 a->aa, b->a^2[a,b]": (P2_A, P2_B, PSI2),
        "ctrl a->ab, b->a": (CTRL_A, CTRL_B, CTRL),
    }.items():
        print(f"  {name:26} exps {exponent_sums(ia)},{exponent_sums(ib)}"
              f"  -> {[list(M.row(0)), list(M.row(1))]}  det {M.det()}")

    same = (TM == S4)
    print(f"\nTM and s4 share an abelianization: {same}")
    print(f"NEGATIVE CONTROL -- TM vs metallic share one: {TM == CTRL}  (must be False)")

    # stratum 4's kernel, by actual substitution
    src = "aB"                                   # a b^-1
    img = substitute(src, S4_A, S4_B)
    print(f"\nkernel, computed: phi_s4('{src}') = '{img}'  (empty = identity);"
          f"  source nontrivial: {reduce_word(src) != ''}")
    # TM must NOT kill it -- otherwise the 'kernel' says nothing about stratum 4 specifically
    img_tm = substitute(src, TM_A, TM_B)
    print(f"CONTROL -- phi_TM('{src}') = '{img_tm}'  (must be non-empty)")

    # TM injectivity: the images do not commute, so <ab,ba> is free of rank 2 (Nielsen-Schreier),
    # hence phi_TM surjects onto a rank-2 free group and Hopficity forces injectivity.
    lhs, rhs = reduce_word(TM_A + TM_B), reduce_word(TM_B + TM_A)
    print(f"\nTM non-commutation, computed: (ab)(ba) = '{lhs}' vs (ba)(ab) = '{rhs}' -> {lhs != rhs}")
    print("  => <ab,ba> free of rank 2 (Nielsen-Schreier) => phi_TM injective (Hopficity).")
    print("  NOTE: this half is a two-step INFERENCE from cited theorems, not an exhibition.")

    assert same, "TM and s4 must share an abelianization"
    assert TM != CTRL, "the negative control must NOT share it -- else the test cannot fail"
    assert img == "", "phi_s4 must kill a b^-1"
    assert reduce_word(src) != "", "the kernel element must be nontrivial in the source"
    assert img_tm != "", "phi_TM must NOT kill it, or the witness is not stratum-specific"
    assert lhs != rhs, "the TM non-commutation witness must separate"
    assert PSI1 == PSI2 and PSI1 != TM, "the second pair must sit at a different abelianization"
    assert all(M.det() == 0 for M in (TM, S4, PSI1, PSI2)), "the separation lives on det 0"

    print("\n=> Same abelianization, opposite Hopf coordinates. The Hopf coordinate is not a")
    print("   function of the abelianization -- ON det 0. Off det 0 it IS (det != 0 => injective),")
    print("   so this licenses exactly one claim: the stratum-3 vs stratum-4 cut is not toral.")
    return same


if __name__ == "__main__":
    main()
