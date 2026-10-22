# W121 — the record's triplet on the closed 4d solutions: do the units 4d gravity forces give a chiral three? (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's main task** (2026-10-22): carry the record's 3d gravity to 4d. W120 found two carriers.
  - In the second, the records' torus is the fibre of a 4d vacuum solution. Each pinched record is a cosmic string,
    and on a closed base the strings come in twelves.
- **W120 named the next question.** Do the units that 4d gravity forces give the record's triplet a chiral three?
  - On the weave's own surface, three is exactly one unit of end data at the cusp (W45, W46). Nothing inside the weave
    supplies it (W47; GENESIS FK10).
  - A closed torus-fibred solution supplies units of its own: 12χ(O_S) strings. This arc counts the triplet there.
- **Weave or thread.** WEAVE-type.
  - The quantities are defined by the moves' joint action: the monodromy group they generate, its metaplectic cover's
    abelianization, and T's representation of the whole modular group.
  - The claims are about every closed torus-fibred solution with only pinched (I₁) fibres. No thread is chosen.

## The object (by hand, to be checked)

- **The solution.** A closed elliptic surface S → C with a section σ, χ(O_S) ≥ 1 and N = 12χ(O_S) fibres of type I₁.
  - Off σ, its fibres are once-punctured tori: the pullback of the weave's surface M₁,₂ by the classifying map
    C → M̄₁,₁.
  - The records' fibre is the punctured fibre, the puncture is σ, and the cusp's preimages are the strings.
  - The compact Ricci-flat one is K3 (χ = 2, 24 strings, K_S = O).
- **The operator** is W45's, carried over: the four-dimensional Dirac operator twisted by 𝕎 (ρ_Q on each punctured
  fibre), with the fibre's odd spin structure and the puncture's natural condition along σ.
  - By Leray its index is a Riemann–Roch number on the base of (K_C ⊗ L)^{1/2} ⊗ 𝒯, with L the fundamental line bundle
    (deg L = χ(O_S)) and 𝒯 the flat bundle of the fibre's zero modes (monodromy ρ_T).
  - On the weave's surface K_C ⊗ L was λ³, hence weight 3/2. On K3 it is trivial, so the spinors there carry weight 0.
- **The count.** With Deligne's canonical extension at each string:
  index = deg((K_C ⊗ L)^{1/2}) · 3 − N · Σμ + 3(1 − g) = (3/2)χ(O_S) − 12χ(O_S)·Σμ, where Σμ is the sum of the exponents
  of ρ(T).
  - The genus cancels.
  - For ρ_T, Σμ = ⅛ + ⅜ + ⅞ = 11/8, so the index is −15χ(O_S). For ρ̄_T, Σμ = ⅛ + ⅝ + ⅞ = 13/8, so it is −18χ(O_S).
  - On K3 these are −30 and −36.
- **When the triplet lives on S at all.** 𝒯 is a representation of the metaplectic cover (W45 E1), and Mp₂(ℤ)^ab =
  ℤ/24 with a positive twist's lift mapping to 1 (W47).
  - So the lifted monodromies of N positive twists multiply to 1 only if N ≡ 0 mod 24, that is χ(O_S) even. For
    χ(O_S) odd their product is the central −1, on which ρ_T is −I.
  - The spinor's square root needs deg(K_C ⊗ L) = 2g − 2 + χ(O_S) even: the same condition.
  - So the rational elliptic surface (χ = 1) carries no spinor ⊗ triplet, and K3 is the least closed solution that
    does.
- **The record's flat bundle at a pinched record.** The vanishing cycle of every I₁ fibre is a primitive class (p, q).
  ρ_Q sends any curve in that class to ±i, ±j or ±k, since (p, q) is not even. A loop that shrinks to the node would
  need holonomy 1. So 𝕎 cannot extend across any string: every string is a defect of the record's flat bundle, and the
  count needs a condition there.
  - The natural conditions coincide, since no exponent of ρ_T or ρ̄_T at a string is an integer (as W47 K2 found at
    the weave's cusp). So the canonical extension is the condition, with no freedom.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| P1 | for every primitive (p, q) with \|p\|, \|q\| ≤ 30, the Christoffel word's image under ρ_Q (a ↦ i, b ↦ j) has order 4 (it is ±i, ±j or ±k); none is ±1 | 99% |
| P2 | with W45's kept identification (ρ(S) = S̃'s matrix, ρ(T) = L⁻¹'s), the product of the 2k positive twists (ρ(T)ρ(S)ρ(T)ρ(S)⁻¹)^k, k = 1 … 12, is scalar exactly at k = 3, 6, 9 and 12 (the lifts of ±I, central in Mp₂(ℤ)), and it is −I₃ at k = 6 and I₃ at k = 12, to 10⁻¹² | 95% |
| P3 | every one of the 24 factors has ρ_T-exponents {⅛, ⅜, ⅞} (sum 11/8), and under ρ̄_T (the other kept identification) {⅛, ⅝, ⅞} (sum 13/8); no exponent is 0 | 97% |
| P4 | the count on K3: the canonical extension's degree is −33 (ρ_T) and −39 (ρ̄_T), by the sum over the 24 factors and again as 48 × the stack degree −(1/2)Σμ; the index is −30 and −36 | 95% |
| P5 | the general law over χ(O_S) = 2, 4, 6: index −15χ(O_S) and −18χ(O_S), never ±3; ±3 would need 9 or 11 added units at the strings (ρ_T) and 11 or 13 (ρ̄_T), each a choice | 95% |

## What the outcomes mean (fixed now)

- **P1 to P5 hold.**
  - The units 4d gravity forces do not give three. On K3, the least closed solution where the record's triplet lives,
    the count with the natural conditions is −30 for one hand and −36 for the other. On every closed solution of this
    kind it is −15χ(O_S) or −18χ(O_S).
  - The forced strings overshoot: each lowers the count by 11/8 or 13/8, and no closed solution reaches ±3 without
    added units at the strings, which are a choice.
  - Three stays exactly one unit at the weave's own cusp (W46), GENESIS FK10's open datum. The record's flat bundle is
    singular at every string, so a closed 4d solution is not a smooth home for it.
- **P2 fails** (the lifted product is I₃ at k = 6). Then the rational elliptic surface would carry the triplet, P5
  would gain χ(O_S) = 1, and the count there is read in the same way, post hoc.
- **P4 or P5 gives ±3 somewhere.** That is a candidate, given the stated operator. It goes to main with its solution
  named, and the count stays 0 of 19.
- **Any cell failing** is recorded as failed.

## What stays out

- Singular fibres other than I₁, which arise only at special moduli, where strings coalesce.
- The non-compact Ricci-flat solutions (the rational elliptic surface with a fibre removed). Their end needs a
  condition of its own.
- The physical status of the operator: whether 𝕎 is the right bundle on S, and whether the string defects carry
  their own modes. This arc counts in the stated reading only.

## Seen before the rule (disclosed)

- **By hand:** the formula above, its genus cancellation, the values −30 and −36, the parity argument for P1, and the
  ℤ/24 argument for P2.
- **Read:** W45's script and its record, for ρ_T's construction and exponents (⅛, ⅜, ⅞ and ⅛, ⅝, ⅞).
- **No computation** for this arc has been run.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
