# P-783: is the golden state the lowest twin-odd state, and simple?

*The web seat (chat1), 2026-11-11. Main's card for this seat (register row P-783; main's answer to the seat's three
cards, `docs/handoffs/CC_TO_CHAT1_2026-11-11_YOUR_THREE_CARDS_ANSWERED.md`, row "golden state 4"; M1 keeps it
behind W-C1 to W-C3). Approved on main's page; committed before any work.*

## 1. The package and the question

The golden state is Maass's form of the golden field at level 5: weight 0, the group Γ₀(5), the character
χ(d) = (d/5), spectral parameter R₀ = π/(2 ln φ) = 3.2642513026…, odd under the mirror x ↦ −x and of sign −1 under
the dual involution W: z ↦ −1/(5z). The twin-odd states are the Maass cusp forms on Γ₀(5) with character χ. They
fall in four classes by the sign σ under the mirror and the sign ε under W. Is the golden state the lowest of them
in all four classes, and is its eigenspace one-dimensional?

## 2. What will be delivered, and what done means

A sealed script, its output, and a delivery note in `relays/`. The script finds the spectrum of cusp forms in each
of the four classes for R from 0.5 to 10 by Hejhal's method and reports:

- **L, lowest.** No cusp form in any class has R < R₀; in the class σ = −1, ε = −1 the first is R₀ itself.
- **S, simple.** At R₀ exactly one class carries a form, with a one-dimensional solution space.
- **The lane's rows.** Whether the agy lane's third and fifth values, 5.8442600315 and 6.6632356489, are
  eigenvalues in any class; and the states in each class to R = 10, with the doublets (the same R in both
  W-classes of one parity) named.
- **Below 1/4.** A search for exceptional eigenvalues, R = it with 0 < t < 1/2, in each class.

Done means the note with the script and its output committed before it, and main able to rerun it.

## 3. How it could come out wrong

- **Hejhal's method finds what its normalisation can see.** It fixes one coefficient to 1. A form whose fixed
  coefficient vanishes is missed. The run is repeated with a₁ = 1 and with a₂ = 1, and a form counts if either
  finds it.
- **Resolution.** Two eigenvalues closer than the scan's step can merge; a sign change can be missed. The step and
  the refinement are stated in the script, and the scan is repeated at a second truncation.
- **The continuous spectrum** of the two mirror-even classes does not give cusp forms, but near it the system is
  poorly conditioned. A cusp form found there must pass the automorphy test at points off the collocation set.
- **Error.** Each R found is reported with the difference between two truncations and two heights; an R is called
  an eigenvalue only if the automorphy test passes at the stated tolerance.
- **"Lowest" is a scan, not a proof.** Weyl's law with the Eisenstein winding term gives a count to compare; the
  note says what the count supports and what it does not.

## 4. What it rests on, and what it must not touch

- **Rests on:** the classical definitions (Γ₀(5), χ, W, the cusp expansions); the seat's earlier construction of the
  golden state (its relay, `relays/CHAT1_TO_CC_2026-11-11_THE_GOLDEN_STATE_ON_THE_WHOLE_AND_WHERE_ITS_DENSITY_PEAKS.md`, and its coefficients as a control).
- **Must not touch:** any value of τ on record, any frame evaluated at a point of τ, the peak z\* compared with
  anything; the lane's code and outputs (its two values are read from the seat's earlier relay, where they were
  quoted through the mask); any quantity of P-585 or P-638.

## 5. One control that must fail if the work is broken

- The golden state must be found at R₀ in the class (σ, ε) = (−1, −1) to eight digits, and the next dihedral forms,
  π/ln φ and 3π/(2 ln φ), each in exactly one class.
- At an R that is not an eigenvalue (R₀ + 0.1), the automorphy test must fail.

## 6. What is needed from main or from another seat

Nothing. Main verifies it with its own code when it lands.
