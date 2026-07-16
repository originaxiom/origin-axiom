# B647 cell 2 — TRACK M WAVE 1: the chain-level swap (prereg; campaign seal a463c6aa)

**The question:** does the deck swap act on the Y-evaluation's
certificate chains EXACTLY (chain-level equivariance), rather than
only on cohomology? If yes, per-slot phase relations follow — the
candidate mechanism for the π/6 phase (B647 cell 1's reduction) and
the 24ζ₆ core ratio.

## Conventions block

- The weld-none double, B637's machinery as banked (b637_threeform.py
  unmodified); the swap map: letters a↔c, b↔d; coefficient companion
  J = U₂₇∘conj (B638's convention, J² = +1 banked).
- The four S_eval evaluations of Yval (the (a,LONG)/(LONG,a) pair on
  side 1; the (μ₂,λ₂)/(λ₂,μ₂) pair on side 2) — evaluated on the
  H¹-basis reps as banked.

## Gates (two-outcome)

- **M2-G1:** for each evaluation pair, is S₂(swapped arguments,
  J-transported cocycles) = J(S₁(arguments, cocycles)) EXACTLY at the
  chain level (before antisymmetrization)? Report per-pair TRUE/FALSE
  with the defect (the difference chain's value) when FALSE.
- **M2-G2 (only if G1 has TRUE pairs):** do the TRUE pairs imply a
  per-slot phase constraint on Y[134] (target: arg = π/6) by exact
  algebra? Derive or refute.

Outcomes: G1 all-FALSE ⇒ the mechanism is NOT chain-local; bank and
route the hunt to the homotopy-correction layer (H₂'s contribution).
G1 TRUE + G2 derives the phase ⇒ the spectator law's mechanism is
FOUND; the core ratio's remaining condition gets the same treatment.
