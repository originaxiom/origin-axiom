# B584 — Round 3 of the chord program: THE LISTENER (preregistration)

**Date: 2026-07-14. Status: preregistered BEFORE the computation. Firewall: nothing
to CLAIMS.md; no SM quantities anywhere in the cells (the B580 binding rule).**

## The question

X3 (B583) proved the second unhearability theorem: the vacuum is C-fixed and
[C,S] = [C,T] = 0, so filling/vacuum probes never hear the θ-odd sector at any
level. Round 3 asks the forced constructive question: **what IS the minimal
nontrivial listener, and what does it hear from the figure-eight?**

The owner's proposal (2026-07-14): *the listener is the object's mirror.* The
sharpened candidate (to be tested): not the mirror alone — the **antiphase mirror
channel** u_λ = (e_λ − e_λ̄)/√2, the θ-odd difference state "object minus mirror."

## MB13 sweep (done before this prereg)

Prior art found and reused, not rediscovered:
- **B238** — SU(3)₂ modular data (S,T) gate-verified; Z(4₁-bundle; SU(3)₂) = −1/φ
  exactly (banked). The golden stage (κ = 5).
- **B570-C3** — E₆ level 2: ρ(A₁) on the θ-odd 3-space is non-scalar, order 4,
  char poly (λ−1)(λ²+1) (banked). So its θ-odd trace is 1 (a re-read, cell R3-4).
- **B242/B243/B245** — colored HOMFLY of 4₁ (IMMM formulas, validated); level-rank
  = conjugation∘transpose.
- **B580 Round 1** — filling covectors span exactly the θ-even plane (SU(2) stage).
- **B583-X3** — vacuum C-fixed; [C,S] = [C,T] = 0.

## The cells

- **R3-1 (core, BLIND):** SU(3)₂. Build C from weight conjugation (a,b) → (b,a);
  gates: C² = 1, [C,S] = [C,T] = 0, C = S². Monodromy ρ(RL) (R = T, L = S⁻¹T⁻¹S,
  the B238 convention). Decompose into θ-even/θ-odd blocks (must decouple exactly
  since C is central). Report the θ-odd 2×2 block: trace, eigenvalues,
  multiplicative order — computed blind, identified exactly after.
- **R3-2 (the operational identity):** P_odd = (1−C)/2 ⇒
  **tr_odd ρ = ½( Z − Z_C )** where Z_C = tr(Cρ) is the C-twisted bundle
  amplitude. Verified numerically on the stage. Reading: the θ-odd amplitude is
  half the difference between the plain play and the mirror-twisted play — the
  listener is the antiphase mirror channel, not the mirror alone.
- **R3-3 (bare knots are deaf sources):** the θ-odd component of a bare knot state
  is J_λ(K) − J_λ̄(K). For su(3): J_3̄ = H^antisym_{[1,1]}(A=q³, q) vs
  J_3 = H^sym_{[1]}(A=q³, q) (B245's validated IMMM formulas), compared at many
  generic q on the unit circle. Standard expectation (Turaev functoriality, dual
  color = reversed orientation): **equal**, i.e. bare knot states have zero θ-odd
  component — the third unhearability (bare knots, not just vacua, are θ-even).
- **R3-4 (E₆₂ re-read, cited):** from C3's banked char poly (λ−1)(λ²+1), the E₆₂
  θ-odd listener amplitude is tr = 1 with order-4 dynamics.

## Expectations vs blind

- Banked gates (must reproduce or the run is broken): Z = −1/φ (B238); modular
  gate green; block decoupling exact.
- BLIND: the SU(3)₂ θ-odd block (trace/order/eigenvalues). No expectation is
  registered for its value.
- Standard-expected: R3-3 equality (a failure would be investigated before any
  claim, per verify-don't-trust).

## Falsifiers

- If the SU(3)₂ θ-odd block is the identity (scalar +1): the golden-stage
  listener is DEAF — the antiphase-mirror listener thesis has no golden
  realization and rests on E₆₂ alone. Bank the null honestly.
- If R3-3 finds J_3 ≠ J_3̄: the "bare knots are θ-even" lemma is wrong and the
  listener does not need to be non-knot — stop and re-derive.

## No-SM binding

No step of this arc references any SM quantity. This is stage grammar only.
