# B644 — PREREGISTRATION: is the ear the mod-5 congruence shadow? (L94)

*Sealed before the run. The comparison cell for L94: B210/B206's
congruence-McKay 2I (monodromy arithmetic, SL(2,𝔽₅) at the ramified
prime 5) vs B640's hearing 2I (the SU(3)₂ θ-odd image, ker(det) of
2I×ℤ/3). Both realize a golden 2-dim character. The QUESTION: does the
hearing representation literally FACTOR through reduction mod 5 —
ρ_hear = χ₂ ∘ (mod-5), with χ₂ one of the two golden 2-dim irreps of
SL(2,𝔽₅) ≅ 2I?*

## The standing reconciliation obligation (checked against the bank)

B210 banked a RESOLVED-NEGATIVE: "the WRT modular-rep image at the
golden level is not 2I" — that operator is the SU(2)₃ FULL modular
image (order 2880, congruence level 20). B640's operator is the SU(3)₂
θ-ODD-PLANE image (level 15). Different stage, different plane, no
contradiction — but this cell must state the reconciliation in its
FINDINGS whatever the outcome.

## The construction (all exact conventions banked)

- The hearing side: B629's `exact_hearing.su3_data(2)` at 60 dps,
  B601's letters R = T, L = S⁻¹T⁻¹S, restricted to the θ-odd 2-plane
  (B640's U, verified). ker(det) = the 120 canonical BFS words.
- The arithmetic side: R₅ = [[1,1],[0,1]], L₅ = [[1,0],[1,1]] over
  𝔽₅; the same words evaluated mod 5.
- SL(2,𝔽₅) class data: the class of g is (order(g); for orders 5 and
  10 additionally the unipotent parameter's QR-type mod 5). The golden
  2-dim irrep table (2I ⊂ SU(2), χ = 2cos of the rotation angle):
  ord 1 → 2, ord 2 → −2, ord 4 → 0, ord 3 → −1, ord 6 → 1,
  ord 5 → {1/φ, −φ}, ord 10 → {φ, −1/φ} (the two Galois-conjugate
  irreps swap the QR-convention).

## Gates (two-outcome, sealed)

- **M1** ⟨R₅,L₅⟩ closes to order 120 in SL(2,𝔽₅).
- **M2 (kernel)** for every canonical BFS word (all 360) and 200
  seeded random words of length ≤ 40: ρ_hear(w) is scalar ⟺
  mod5(w) = ±I. Failure count 0.
- **M3 (character factorization)** on all 120 ker(det) canonical
  words: the map class(mod5(w)) ↦ tr ρ_hear(w) is WELL-DEFINED
  (constant per class) and equals ONE consistent golden irrep table
  (one QR-convention fits all 120; the other must fail somewhere —
  the discriminating control).
- **M4 (the pentagon)** the cat-map word RL: its mod-5 class and the
  table value at that class = −1/φ = tr ρ_hear(RL) (B640's banked
  headline recovered THROUGH the arithmetic side).

## Verdicts

- M1–M4 all pass ⇒ **THEOREM (verification strength): the ear at the
  minimal bearing stage κ = 5 hears the monodromy through its mod-5
  congruence shadow** — ρ_hear = χ₂ ∘ mod-5 on ker(det); L94 CLOSES;
  the dual-McKay D-row upgrades (the ear's 2I derived, not placed).
- M2 or M3 fail ⇒ the two 2I's are abstractly isomorphic but NOT the
  same homomorphism — bank the obstruction witness; L94 stays open
  with the witness named.
- No SM numbers; no physics reading; Gate 5 untouched.
