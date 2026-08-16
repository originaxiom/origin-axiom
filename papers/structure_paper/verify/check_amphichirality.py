#!/usr/bin/env python3
"""
Appendix B -- verification of the amphichirality theorem (paper Thm. "the metallic family
is amphichiral" and Prop. "the block-sequence criterion").

Self-contained: needs only sympy.  Imports NOTHING project-internal.  Exact integer
matrix arithmetic throughout.

## WHY THIS SCRIPT EXISTS

This claim has been reversed three times in the paper's history, and every reversal but
the last was made without opening the cited source:

    asserted with no source
      -> withdrawn, because no source had been opened
      -> restored, because Goodman-Heard-Hodgson (GHH) was found to exist
      -> withdrawn AGAIN, because GHH was finally READ.

GHH classify symmetries of NON-ARITHMETIC once-punctured-torus bundles, removing the
arithmetic monodromy words before the argument starts.  The removed words include RL and
RRLL -- that is, m = 1 and m = 2, the golden and silver members.  The figure-eight knot
complement is THE arithmetic knot complement.  So the source's hypotheses exclude
precisely the members the paper cares about most, and the biconditional was never
available from it.

The repair is not a better citation.  It is that the family's amphichirality has a
two-line proof that cites nothing, and this script is that proof, executed.

## THE STATEMENT

Let R = [[1,1],[0,1]], L = [[1,0],[1,1]], and let the monodromy of M_m be phi_m = R^m L^m.
Let J = [[0,1],[1,0]], so det J = -1 and J R J^-1 = L.  Then

    J phi_m J^-1 = L^m R^m = R^-m phi_m R^m       (the second is a cyclic rotation)

so g = R^m J satisfies

    g phi_m g^-1 = phi_m        and        det g = -1.

An orientation-REVERSING self-map of the fibre torus that COMMUTES with the monodromy
descends to the mapping torus; it reverses the fibre orientation and preserves the base
direction, hence reverses the orientation of M_m.  So every M_m is amphichiral.

Verifies, in order:
  1. det J = -1 and J conjugates R to L (so J is the L<->R swap);
  2. for m = 1..40, g = R^m J has det -1 and centralizes phi_m -- the theorem;
  3. phi_m is symmetric, and phi_m = [[m^2+1, m],[m, 1]] as the paper states;
  4. the transpose identity W^T = swap(reverse(W)) on all L,R words to length 10, and
     that STRICT anti-palindromicity forces symmetry while the CYCLIC version does not
     -- RLLR is cyclically anti-palindromic with matrix [[3,4],[2,3]], not symmetric.
     The metallic words satisfy the strict condition, which is why phi_m is symmetric;
  5. the block-sequence criterion: cyclic palindrome <=> anti-palindromic, exhaustively
     over all block sequences of length <= 6 with entries <= 4;
  6. a NEGATIVE control: a non-anti-palindromic word is NOT symmetric, so the criterion
     is not vacuous.

Run:  python3 check_amphichirality.py        (exit 0 = all PASS)
"""

import itertools
import sys

import sympy as sp

FAILURES = []

R = sp.Matrix([[1, 1], [0, 1]])
L = sp.Matrix([[1, 0], [1, 1]])
J = sp.Matrix([[0, 1], [1, 0]])


def check(label, got, want):
    ok = got == want
    print(f"  [{'PASS' if ok else 'FAIL'}] {label}")
    if not ok:
        print(f"          expected: {want}")
        print(f"          got:      {got}")
        FAILURES.append(label)
    return ok


def word_matrix(w):
    """The matrix of an L,R word, read left to right."""
    M = sp.eye(2)
    for c in w:
        M = M * (R if c == "R" else L)
    return M


def swap(w):
    return "".join("L" if c == "R" else "R" for c in w)


def rotations(w):
    return {w[i:] + w[:i] for i in range(len(w))}


def anti_palindromic(w):
    """reverse(w) equals the L<->R swap of w, up to cyclic rotation."""
    return w[::-1] in rotations(swap(w))


def blocks_to_word(ms):
    return "".join("R" * m + "L" * m for m in ms)


def is_cyclic_palindrome(ms):
    rev = tuple(reversed(ms))
    return any(rev == tuple(ms[i:] + ms[:i]) for i in range(len(ms)))


def main():
    print("=" * 74)
    print("Appendix B -- the metallic family is amphichiral, proved rather than cited")
    print("=" * 74)

    print("\n1. J is the L<->R swap, and it reverses orientation")
    check("det J = -1", J.det(), sp.Integer(-1))
    check("J R J^-1 = L", J * R * J.inv(), L)
    check("J L J^-1 = R", J * L * J.inv(), R)

    print("\n2. THE THEOREM: g = R^m J reverses orientation and centralizes phi_m")
    bad_det, bad_comm = [], []
    for m in range(1, 41):
        phi = R**m * L**m
        g = R**m * J
        if g.det() != -1:
            bad_det.append(m)
        if g * phi * g.inv() != phi:
            bad_comm.append(m)
    check("det(R^m J) = -1 for every m = 1..40", bad_det, [])
    check("R^m J centralizes phi_m for every m = 1..40", bad_comm, [])
    print("          so every M_m admits an orientation-reversing self-homeomorphism.")

    print("\n3. the monodromy is the matrix the paper prints, and is symmetric")
    bad_form, bad_sym = [], []
    for m in range(1, 41):
        phi = R**m * L**m
        if phi != sp.Matrix([[m * m + 1, m], [m, 1]]):
            bad_form.append(m)
        if phi != phi.T:
            bad_sym.append(m)
    check("phi_m = [[m^2+1, m], [m, 1]] for m = 1..40", bad_form, [])
    check("phi_m is symmetric for m = 1..40", bad_sym, [])

    print("\n4. the transpose identity, and the distinction it turns on")
    # W^T = swap(reverse(W)) as WORDS, since R^T = L.  So STRICT anti-palindromicity --
    # reverse(W) equal to swap(W) on the nose -- forces W = W^T.  CYCLIC
    # anti-palindromicity does NOT: it only makes W^T a rotation of W.
    #
    # An earlier draft of the paper asserted the cyclic version implies symmetry.  This
    # check is what caught it, and RLLR below is the counterexample it produced.
    bad_word_identity, bad_strict = [], []
    for n in range(1, 11):
        for tup in itertools.product("RL", repeat=n):
            w = "".join(tup)
            if word_matrix(w).T != word_matrix(swap(w[::-1])):
                bad_word_identity.append(w)
            if w[::-1] == swap(w):                       # STRICT
                M = word_matrix(w)
                if M != M.T:
                    bad_strict.append(w)
    check("W^T = swap(reverse(W)) for every word to length 10", bad_word_identity, [])
    check("strict anti-palindromic => symmetric, all words to length 10", bad_strict, [])

    print("\n   the counterexample that forces the word 'strict':")
    w = "RLLR"
    check("RLLR is CYCLICALLY anti-palindromic", anti_palindromic(w), True)
    check("RLLR is NOT strictly anti-palindromic", w[::-1] == swap(w), False)
    Mc = word_matrix(w)
    check("and its matrix is NOT symmetric", Mc == Mc.T, False)
    check("RLLR's matrix is [[3,4],[2,3]]", Mc, sp.Matrix([[3, 4], [2, 3]]))

    print("\n   the metallic words satisfy the STRICT condition:")
    bad_metallic = [m for m in range(1, 21)
                    if ("R" * m + "L" * m)[::-1] != swap("R" * m + "L" * m)]
    check("reverse(R^mL^m) = swap(R^mL^m) exactly, m = 1..20", bad_metallic, [])

    print("\n5. the block-sequence criterion, exhaustively")
    disagree = []
    for k in range(1, 7):
        for ms in itertools.product(range(1, 5), repeat=k):
            if is_cyclic_palindrome(list(ms)) != anti_palindromic(blocks_to_word(ms)):
                disagree.append(ms)
    total = sum(4**k for k in range(1, 7))
    check(f"cyclic palindrome <=> anti-palindromic on all {total} block sequences",
          disagree, [])

    print("\n6. negative control: the criterion is not vacuous")
    w = "RRL"                      # block sequence (2,1) padded -- not anti-palindromic
    check("RRL is not anti-palindromic", anti_palindromic(w), False)
    M = word_matrix(w)
    check("and its matrix is not symmetric", M == M.T, False)
    check("RLL is not anti-palindromic either", anti_palindromic("RLL"), False)
    # but the metallic words ARE
    check("R^3L^3 is anti-palindromic", anti_palindromic("RRRLLL"), True)

    print("-" * 74)
    if FAILURES:
        print(f"FAIL: {len(FAILURES)} check(s) did not reproduce.")
        for f in FAILURES:
            print(f"   - {f}")
        return 1
    print("PASS: every metallic bundle is amphichiral, by a proof that cites nothing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
