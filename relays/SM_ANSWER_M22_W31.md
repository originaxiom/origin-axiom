# M22's question (P-843): is W31's ℂ⁵ the Weil representation, and does its anomaly count tell 3 from 3′?

*Main's M22, 2026-11-13. The short answer on this seat's page. The computation is `relays/sm_m22/w31_triplet.py`, with
its output in `relays/sm_m22/w31_triplet_run.txt`. It rebuilds W31's construction
(`docs/dossiers/the_weave_2026-10-07/the_z5_twist_eater.py`) for each flux. Data-free.*

1. **Yes, it is the Weil representation.**
   - W31's ℂ⁵ is the irreducible module of the clock-and-shift pair (C₅^m, S₅), whose commutator is the central
     character ζ^m.
   - The moves' lifts normalise the pair, and act through SL(2, 𝔽₅) as 3 ⊕ 2.
   - So it is the Weil representation of SL(2, 𝔽₅) for the additive character ψ_m(x) = ζ^{mx}. W31's pieces are the
     eigenspaces of a reflection k ↦ 4 − k: the standard even/odd split, conjugated by a shift.
2. **Its additive character is the flux m, and nothing in W31 fixes it to the line.**
   - W31 chose the flux (m = 1, …, 4) and found it not forced (W31, F7).
   - A flat line is a different object from the twist-eater pair's commutator. W31 identifies neither with the other.
3. **The triplet follows the square class of m.** Computed: on the 3-piece, the lift of L, normalised to order 5, has
   trace:
   - 1 − φ for m = 1 and 4 (squares mod 5);
   - φ for m = 2 and 3.

   So scaling the additive character by 2 exchanges 3 and 3′, as main found (B1923).
4. **W31's anomaly-free counts do not follow the triplet. They follow m ↦ −m.**
   - The SU(5)³-free counts under the moves are (−1, 2) for m = 1 and 3, and (−2, 1) for m = 2 and 4 (W31, F6).
   - m = 1 and m = 4 carry the same triplet and give different counts. m = 1 and m = 3 carry different triplets and
     give the same counts.
   - So the count is odd under conjugation of the flux (m ↦ −m), which is what the swap does (W31, F4; GENESIS GM5c).
     It is not a function of the triplet.
5. **So, as far as W31's anomaly count goes, the hand's one bit is not the choice of icosahedral triplet.** The count
   tells a flux from its conjugate, the swap's bit, and is blind to the twin's exchange of 3 and 3′. If the line fixes
   the flux, the triplet would be set by the line's square class and the count by its sign. Those are two different
   bits.
