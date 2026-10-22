# W134 — the bridge: the weave's flavour triplet as the family SU(3) of E₈ ⊃ E₆ × SU(3). What E₈'s determinant condition asks of the weave's end, and how many chiral 27s it gives (the rule, committed before the script)

The SM-derivation seat, 2026-10-22. Committed and pushed before the script that reads it exists. Nothing here is a
result.

## Why

- **The owner's question (2026-10-22):** the seed's side gives the Standard Model's form from E₆ inside E₈; the weave
  gives the three. Why has no one shown how the two act together to fill the form with three generations?
- **The record's bridges so far,** each broken at a named place:
  - main's E₈ ⊃ E₆ × SU(3) on one thread (B1270–B1273): three copies of the 27, vector-like, with no Yukawa;
  - E₈ bundles on the weave's fibre (W23): at most two complete chiral generations;
  - fluxes on the fibre (W29, W31): hypercharge broken, or SU(5) left unbroken.
- **The bridge not yet taken.** The weave's three lives on the weave's surface (the τ-line), as the flat bundle of
  the moves' representation ρ. There W46 and W47 count it with the index I = n·f + t_r. This arc puts that ρ in E₈'s
  family slot. The owner asked for the rule (2026-10-22).

## The objects

- **E₈ ⊃ (E₆ × SU(3))/ℤ₃,** with 248 = (78, 1) ⊕ (1, 8) ⊕ (27, 3) ⊕ (27̄, 3̄). The chiral 27s are counted by the index
  of the 27 ⊗ V part, where V is the family bundle.
- **The weave's family bundle.** ρ is W123's monomial representation (ρ(S) = ζ₈P, ρ(T) = ζ₈L⁻¹), with the six
  allowed twists ε_r, r ∈ {0, 4, …, 20} (W47 K1). The index uses W46's pieces (T at weight 3/2; V2 and V4 at weight
  1) and conditions (0, V2, V4, L6).
- **The determinant condition.** Structure group in E₆ × SU(3) needs the family monodromy in SU(3). That is det = 1
  up to the order-3 scalars that E₈'s ℤ₃ identifies with E₆'s centre.
- **A fractional cusp datum.** A uniform dressing by η^m on every piece is m twenty-fourths of the cusp unit, since
  O(δ) = η^{−24}. It shifts the weight by m/2 and the character by χ_η^m together, so every χ stays defined. W47's
  whole units are m = 24n, and m = 0 is the empty end.
  - The generalized index is I(cond, r, m) = −χ_{3/2+m/2}(T ⊗ ε_r ⊗ χ_η^m) + Σ_{p ∈ cond} χ_{1+m/2}(p ⊗ ε_r ⊗ χ_η^m).
  - The dressed family part has det = χ_η^{9+3r+3m}.

## Weave or thread

**WEAVE-type.** The weave's own surface, the whole triplet in the family slot (no line chosen by hand), every allowed
twist, all four puncture conditions, and every datum |m| < 24. E₈'s frame is the record's.

## The cells, with predictions and priors

| cell | prediction | prior |
| --- | --- | --- |
| E0 | the instrument. **E₈ (exact roots):** with A₂ spanned by e₁ − e₂ and e₂ − e₃, the roots orthogonal to it number 72 (E₆). The other 162 project onto the six weights of 3 ⊕ 3̄, 27 each, so 248 = 78 + 8 + 81 + 81. **The index:** the generalized I(cond, r, m) reproduces W47's K5 table at m = 24n (n ∈ {−1, 0, 1}) | 97% |
| E1 | the obstruction (exact). **The determinant:** det(ρ ⊗ ε_r) = χ_η^{9+3r} on S and T, never trivial for an allowed r; the det-1 twists of ρ are χ_η^k with k ≡ 5 (mod 8). **The lemma:** each det-1 twist has ρ′(S)² = 1, so it allows only even integral weights. So no flat family bundle in SU(3) carries the weave's matter at the forced weight 3/2 (W45, W46) | 95% |
| E2 | the admissible data (exact). The dressed family part is in SU(3) iff m ≡ 5 − r (mod 8): m odd, so m ≡ 1 (mod 8) for r ≡ 4 and m ≡ 5 (mod 8) for r ≡ 0. **Neither the empty end (m = 0) nor the whole unit (m = ±24) is admissible.** The least admissible data are m = 1 (r ≡ 4 mod 8) and m = −3 (r ≡ 0 mod 8) | 95% |
| E3 | the count (two routes: the χ formula at the dressed weight, and the closed form through the exponents, I = t_r − Σ_T ⌊λ + m/24⌋ + Σ_{p ∈ cond} Σ ⌊λ + m/24⌋). **At the least admissible datum, \|I\| ≤ 1 at every condition and twist; for admissible \|m\| ≤ 16, \|I\| ≤ 2.** \|I\| = 3 occurs at exactly these twelve (r, m, condition): (4, 17, 0), (4, −23, L6), (12, 17, 0), (12, −23, 0), (12, −23, L6), (20, −23, L6), (0, 21, 0), (0, 21, L6), (8, 21, 0), (8, 21, L6), (8, −19, 0), (16, 21, L6) | 80% |
| E4 | the read-out. The table of chiral 27s by (r, m, condition); the least admissible datum giving three; a READING by hand on the Yukawas | — |

## What the outcomes mean (fixed now)

- **E0 to E3 hold.** Then:
  - **The seed's E₈ and the weave's three can be joined in E₆ × SU(3) only at a fractional end datum:** an odd number
    m of twenty-fourths of the cusp unit, with m ≡ 5 − r (mod 8).
    - E₈'s determinant condition excludes both the empty end and the whole unit, GENESIS FK10's unit included.
    - The dressing η^m is a coupling of the 27s to τ, the same kind of absorber W132 found for the moves' SU(2)
      leftover.
  - **The bridge does not force three.** At the least admissible datum it gives at most one chiral 27. Three chiral
    27s need at least 17/24 of a unit (the twelve data in E3).
  - **So the open question moves** from "is the unit forced?" (GENESIS FK10) to "what fixes m?". The dictionary
    (GENESIS FK11) gains one entry: the 27's family index is the weave's triplet, with an odd twenty-fourths datum.
- **E3 finds |I| = 3 at a datum the rule did not list, or at the least admissible datum.** Then E₈'s consistency would
  itself select a three-generation datum. That would be the positive this seat does not expect, and it is recorded
  as found.
- **E1 fails** (a flat SU(3) family bundle at the forced weight exists). The obstruction's arithmetic is wrong. It is
  recorded, and E2 and E3 are read only after that is resolved post hoc.

## What stays out

- **Holonomies that break E₆** (a non-central E₆ part); flat U(1) Wilson lines inside E₆.
- **The other blocks:** the (1, 8) and the singlets' counts. The (27̄, 3̄) is the 27's conjugate and adds no
  independent count.
- **Further conditions:** the Bianchi identity and second Chern class matching; per-line (non-uniform) data; the
  puncture's localized matter; the four-dimensional Higgs.
- **The Yukawa values.** Only a by-hand READING is given in E4.

## Seen before the rule (disclosed)

- **Read:** W23, W29, W31, W45, W46, W47 (its K2 exponent table and K5 index table), W127, W132; main's
  `THE_ASSEMBLY_2026-09-06.md` on B1270–B1273.
- **By hand:**
  - the determinant characters;
  - the lemma (a det-1 twist has ρ′(S)² = 1);
  - the admissibility m ≡ 5 − r (mod 8);
  - the m-independence of the χ formula's elliptic terms, and the closed form by floors;
  - E3's whole predicted table, by arithmetic on W47's recorded exponents;
  - E0's root count (72 and 162).
- **Not run:** nothing has been computed by a script.

## Discipline

- This rule is committed and pushed before the script exists.
- One run; its output is committed before it is read.
- A failed launch is disclosed, with its log kept. Any failed prediction is recorded as failed, and any later check is
  labelled post hoc.

0 of 19.
