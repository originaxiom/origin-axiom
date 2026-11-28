# EXPECT_Q0008 — sm2 (fam1-v1-unset-05), committed before any run

Card: Q0008, `relays/claims/CLAIM_2026-11-27_C8_two_registers.md` on audit/physical-bridge-2026-09-05 at
2de93d2e65125601804e66dbc1f8631e9d9ec55c (the queue record's commit). Written from the card and the queue record alone,
before reading or running the producer's script and before running any code of mine. Not read: the peer's note, the other
banking seat's branch, anything on the producer's branch besides the card.

## What I will recompute (my own code, numpy and the standard library)
1. The geometric map: a representation of the figure-eight knot group into SL(2, F25), F25 = F5[d]/(d^2-2), with meridian
   U(1), and its longitude, computed from a word I derive (expected: Z·U(±2d), since the cusp field of the figure-eight
   is Q(sqrt(-3)) and -3 = 2 mod 5). This replaces the card's imported map by a check (K4).
2. The sheet lift: a dihedral colouring of the figure-eight (determinant 5) lifted to the binary dihedral group of order
   20 by r^a j^n, checked to be a homomorphism, with its meridian and longitude images (expected: j and 1).
3. The spin sign: whether the 13-dimensional even Weil module of PSL(2,25) lifts to Spin(13) through the nonsplit cover,
   so that Z goes to -1 (I expect yes: an involution's -1 eigenspace should have dimension 6, half of it odd).
4. The count: the joint eigenvalues of meridian and longitude on 248 = Λ²(13+3) + 64⊗2, for geometric holonomy alone and
   for its product with the sheet lift, counting longitude -1 with meridian +1 (periodic) or -1 (antiperiodic).

## Expectation
- Geometric alone: 8 periodic, 0 antiperiodic. By my reading, Λ² gives nothing (the longitude has fifth-root eigenvalues
  there), and the spinor part 64⊗2 gives 2 × (the number of the 64 spin weights at joint weight (0, 0) mod 5), so 8 needs
  exactly 4 such weights. With the sheet: 0 and 0, because j puts ±i on the 2 and no meridian eigenvalue there is ±1.
- So I expect the counts 8 → 0 to hold.
- The verdict I expect: ACCEPT conditional on named hypotheses: the HSpin(16) ⊂ E8 branching and the real structure, which I
  will use and not rebuild. The card's further statements (connectedness of a centralizer, Cohen–Griess, the hand proofs
  of the joint image) are citations; I will not bank on them (K4), and the verdict will say the E8 reading rests on them.
- I will also vary the declared choices (K7): the orientation of the longitude (U(2d) or U(-2d)), the conjugate Weil module
  (d → -d), and the colouring. If the count moves with them, the result is about the declaration, and I RETURN.
- What makes me REFUSE: a count other than 8 → 0 for the card's maps, the maps not being homomorphisms, or the spin sign
  coming out split (then the longitude has no -1 eigenvalue and the 8 is not reached the card's way).
