# SM-C19 — frame D1's Higgs ground bit is the hand: only an orientation-reversing operation exchanges the two ground modes

*The SM seat, 2026-11-18. Card `relays/cards/SM_C19_which-bit-is-the-higgs-ground-bit.md`, sealed and pushed before the
run. Data-free; main's B1957 instrument imported unchanged. No coupling or mass value.*


> **Corrected, 2026-11-18, after main's M41, checked on this seat's own code (`relays/sm_c19/check_s6.py`).**
> - **The headline is false as written.** The pair is not exchanged "only by an antiunitary". The unitary S₆ carries
>   U_M to its inverse and sends v₊ to v₋ with overlap 1.000.
> - **The sharper statement (main's):** the pair is exchanged exactly by the elements that reverse the bundle's
>   orientation, counting the fibre and the act's direction together. That means the unitary elements that invert
>   U_M, and the antiunitary elements that keep it. This seat's enumeration reproduces that pattern. Its group count
>   (4 040 up to phases, against main's 576) is not reliable, because the phase de-duplication is imperfect, and it is
>   not claimed.
> - **"The bit is the hand"** stands only in this sharper form.
> - **A consequence this page did not draw (main's):** the figure-eight has an orientation-reversing symmetry of its
>   own, so the object cannot fix the sign.
> - **"One bit" says too much (M41).** The ground space is a complex plane, and every unit vector in it is a ground
>   direction. It is one bit only if the direction is restricted to the two eigenlines, and nothing computed forces
>   that.

## The answer

- **B1957's "one bit"** is the pair of six-mode transport eigenvectors with eigenphases ±π/6. Once the bubble is
  averaged over the lifts, it is the whole ground space.
- **The bit is exchanged only by an antiunitary,** complex conjugation composed with a modular transformation of the
  modes: A·conj with A = T₆S₆, T₆S₆⁻¹, S₆T₆ or S₆⁻¹T₆. Each satisfies A·conj(U_M)·A⁻¹ = U_M and sends v₊ to v₋ with
  overlap 1.000. These are the shortest words found among the record's operators.
- An antiunitary composed with a modular transformation is an orientation-reversing element of GL(2, ℤ) acting on the
  modes. **So frame D1's undetermined Higgs bit is the hand.**
- It is the same kind of bit the record carries as the tick's orientation (B1926) and as the hand's invariant (SM-C9,
  B1929). Which sign is realised is not decided here.
- **Neither the parity nor the lift is the bit:**
  - the parity P (k → −k) commutes with U_M and fixes v₊;
  - the lift elements send no part of v₊ to v₋.

## The results against the sealed expectations

| | expectation (prior) | result |
|---|---|---|
| B1 | the lift commutes with U_M and preserves the ±π/6 eigenspaces: not the ground bit (60%) | **The conclusion holds, the reason does not.** Z³, X³ and Z³X³ do *not* commute with U_M (commutators 0.82, 0.58 and 0.58). They send v₊ a third onto itself (overlap 0.577) and the rest onto *other* modes, never onto v₋ (overlap ≤ 6e-16). So the lift is not the ground bit, but the card's derivation that the lift centralises U_M was wrong |
| B2 | the parity preserves them: not the ground bit (80%) | **holds:** [P, U_M] = 1.7e-15 and P·v₊ = v₊ |
| B3 | an antiunitary built from the record's operators exchanges them: the bit is the hand (65%) | **holds:** four words of length 2, each exchanging v₊ and v₋ exactly (overlap 1.000, residual ≤ 1e-15) |

**The instrument check:** B1957's H3, rerun. The modes' transport along M is U_M itself (2.9e-15), not conj U_M
(0.82).

## What it means

- **SM-C18 left frame D1 with two options** for frame C's charges: read the overlap on the double cover of the
  point, or make the Higgs's charge even.
- **This card shows** that on the lift-averaged reading (the double cover summed over), the bit that remains is not a
  new one: it is the hand.
- So frame D1's Higgs vacuum is set by the same bit that sets the orientation everywhere else in the record. That
  removes one apparent free choice, not by selecting a sign, but by identifying it with a bit the record already
  carries.
- **A pointer, not a claim:** an antiunitary built from T and S is an element of GL(2, ℤ) of determinant −1, the same
  kind of element as the tick σ (a ↦ ab, b ↦ a). Whether the exchanging element is the tick itself, on the modes, is
  the next computation.

## Deviation, said

- B1's derivation, that the lift normalises and in fact centralises U_M, was wrong. Its conclusion stands for a
  different reason: the lift moves v₊ off the ground pair rather than across it.
- The card's B4, the reading switch being of order 3, was derived and cited from B1946, and not computed here.

## Files

`relays/sm_c19/run_c19.py`, `relays/sm_c19/c19_results.json`, `relays/sm_c19/RUN.txt`.
