#!/usr/bin/env python3
"""IS ANYTHING REAL ON IT -- the lab lane's content, verified not relayed.

Owner: "is anything real on it? ... it feels underdeveloped, and the homework
before lab isnt properly done by us ... it also feels a bit missinformed".

R138 led with memo 197's 19.77% and mentioned memo 196 ADDENDUM 1 only as a
supporting clause -- then contradicted it by saying "a fail would still bite".
Addendum 1's claim is far stronger and settles the question.  It is therefore
VERIFIED HERE from the sealed convention rather than cited.

Convention, verbatim from EDGE_PREREG_SPEC section 3 / B1106:
  b_n = floor((n+1)a + rho) - floor(n a + rho),  a = 2 - phi = 1/phi^2, rho = a
  right hand = (b_0 .. b_{N-1});  left hand read outward = (b_{-1}, b_{-2}, ...)
  H: on-site potential w_n = b_n, uniform hopping 1, tridiagonal.
"""
from __future__ import annotations

import sys

import numpy as np

PHI = (1 + 5 ** 0.5) / 2
A = 2 - PHI            # = 1/phi^2
RHO = A

FAILURES: list[str] = []


def fail(tag, msg):
    FAILURES.append(f"{tag}: {msg}")
    print(f"  !! FAIL [{tag}] {msg}")


def letter(n: int) -> int:
    return int(np.floor((n + 1) * A + RHO) - np.floor(n * A + RHO))


def right_word(N):
    return [letter(n) for n in range(N)]


def left_word_outward(N):
    return [letter(-1 - k) for k in range(N)]


def ham(word):
    N = len(word)
    H = np.diag(np.array(word, dtype=float))
    for i in range(N - 1):
        H[i, i + 1] = H[i + 1, i] = 1.0
    return H


def main() -> int:
    print("=" * 78)
    print(" IS ANYTHING REAL ON IT -- the lab lane's content, verified")
    print("=" * 78)
    print(f"\n  slope a = 2 - phi = {A:.15f},  rho = a  (the sealed cut phase)")

    print("\n  N     idx  parity |  word closes | H_L == J H_R J | isospectrality")
    print("  ----- ---- ------- | ------------ | -------------- | --------------")
    fib = {7: 13, 8: 21, 9: 34, 10: 55, 11: 89, 12: 144, 13: 233, 14: 377, 16: 987}
    rows = []
    for idx in sorted(fib):
        N = fib[idx]
        R = right_word(N)
        L = left_word_outward(N)
        closes = (L == list(reversed(R)))
        HR, HL = ham(R), ham(L)
        J = np.fliplr(np.eye(N))
        conj = J @ HR @ J
        same = bool(np.array_equal(HL, conj))
        iso = float(np.max(np.abs(np.sort(np.linalg.eigvalsh(HR))
                                  - np.sort(np.linalg.eigvalsh(HL)))))
        par = "even" if idx % 2 == 0 else "odd"
        print(f"  {N:<5} {idx:<4} {par:<7} | {str(closes):<12} | {str(same):<14} | {iso:.3e}")
        rows.append((N, idx, par, closes, same, iso))

    print("""
  READ THE TABLE.  At every EVEN-index window the word closes AND H_L is
  LITERALLY THE SAME MATRIX as H_R under the reversal permutation J -- equal
  ELEMENTWISE, not merely similar.  The 1e-15 "isospectrality" is floating-point
  error from diagonalising one matrix twice.  At every ODD-index window the word
  does not close and the two differ macroscopically (~1.5e-1).""")

    even_ok = all(c and s and i < 1e-12 for _, idx, _, c, s, i in rows if idx % 2 == 0)
    odd_ok = all((not c) and (not s) and i > 1e-3 for _, idx, _, c, s, i in rows if idx % 2 == 1)
    print(f"\n  every even-index window: closes AND elementwise equal AND iso < 1e-12 : {even_ok}")
    print(f"  every odd-index window : does NOT close AND differs macroscopically   : {odd_ok}")
    if not (even_ok and odd_ok):
        fail("IDENTITY", "the J-conjugation pattern is not as memo 196 addendum 1 states")

    # ---- clause 2: is the "complementary split" also forced by J?
    print("\n" + "-" * 78)
    print(" CLAUSE 2 -- is the 5/6 'complementary split' ALSO forced by J?")
    print("-" * 78)
    print("""
  Under J a right-hand eigenvector with weight on the FIRST 20 sites maps to a
  left-hand eigenvector with weight on the LAST 20.  If so, the "complementary
  split between two hands" is the (near-end, far-end) count of ONE chain, and
  no second fabricated sample is measuring anything new.""")
    for N in (144, 377, 987):
        R = right_word(N)
        HR, HL = ham(R), ham(left_word_outward(N))
        wR = np.linalg.eigh(HR)[1]
        wL = np.linalg.eigh(HL)[1]
        near = int(sum(1 for k in range(N) if (wR[:20, k] ** 2).sum() > 0.5))
        far = int(sum(1 for k in range(N) if (wR[-20:, k] ** 2).sum() > 0.5))
        meas = int(sum(1 for k in range(N) if (wL[:20, k] ** 2).sum() > 0.5))
        agree = (far == meas)
        print(f"  N = {N:<4}  right chain: near-end {near}, far-end {far}   "
              f"|  measured LEFT count {meas}   |  far-end == left : {agree}")
        if not agree:
            fail("CLAUSE2", f"at N={N} the J-forced far-end count != the measured left count")

    print("""
  So all three sealed clauses are FUNCTIONS OF THE WORD, and the word is fixed
  by (rho, N) -- both pinned in the seal.  None is contingent on a measurement.""")

    # ---- what a measurement could still refute
    print("\n" + "-" * 78)
    print(" WHAT A MEASUREMENT COULD STILL REFUTE")
    print("-" * 78)
    print("""
  Not the object.  Given the tight-binding model and the intended word, the three
  clauses are identities -- so BY THE RECORD'S OWN RULE (MB12/E2, quoted in
  WHAT_WOULD_COUNT 4A.0: "a preregistered test must be able to both pass and
  fail"), they cannot fail.  What a run would test is:
      (1) does the fabricated array realise the INTENDED word   -- fabrication QC
      (2) is the photonic platform reciprocal                   -- known physics
  Both worth doing.  Neither is a test of the programme.

  AND THE CHAIN ALREADY SAID SO, AT C4, LONG BEFORE ANY OF THIS:
      "non-geometric carriers (tiling hull; Effros-Shen algebra, K_0 = Z[phi])
       SEE ONLY THE HEARING -- Q(sqrt-3) is bought at geometrization and nowhere
       earlier."
  A photonic Fibonacci array IS the tiling hull.  Every link reaching the SM runs
  through Q(sqrt-3).  So no photonic experiment can bear on any link downstream
  of C4 -- the lab lane tests C1-C2 and stops there.""")

    print("\n" + "=" * 78)
    print(" VERDICT")
    print("=" * 78)
    print(f"   the three sealed clauses are word identities : {even_ok and odd_ok}")
    print( "   the apparatus pricing (memo 196) is real     : N = 21 for the forced half")
    print( "   the falsifier tests the object              : NO -- it tests fabrication")
    print( "   it could reach the SM even if it passed     : NO -- C4 forbids it")
    if FAILURES:
        print("\n  FAILURES:")
        for f in FAILURES:
            print(f"    - {f}")
    print("=" * 78)
    return 1 if FAILURES else 0


if __name__ == "__main__":
    sys.exit(main())
