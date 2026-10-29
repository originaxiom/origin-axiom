# P-406 census (second draft) — hostile referee report (read-only, 2026-10-29)

Saved by main from the referee's hand-back (the referee could not write report files). Its checks are c1–c7 beside this
file. They reuse the record's code read-only: B1691's q-series, b1656_funcs, B1667's canonical radii. As a control, c2
reproduces S248's 0.27323 (L = 0.65) and 0.021109 (L = 2.5).

**Verdict:** BLOCK as drafted. It passes with corrections once B1–B3 are reworded and the value table goes in. Several
errors came from the first referee's report, which main accepted without recomputing: "V ≡ 1 at zero line", "the
isotropic sections give m₂ ≡ m₁ ≡ 0", and "order one … never a hierarchy".

## BLOCKING

**B1. (S1) fails at the canonical end radius, and "hierarchy" is undefined.**
- B1667 fixes L = L_h(τ), leaving only h ∈ {max, 2}. The L-free coupling is a limit outside the frame.
- The values at (i, zero line) at L_max(i) = 0.68839 and L₂(i) = 2.71926 (c1, c6) are the census's Table T.
  - R gives m₂/m₃ = 0.019 at L₂(i), with no free parameter.
  - The non-degenerate parameter-free directions give m₁/m₃ = 0.023–0.077.
- The horocycle moves R's value by a factor of 11.
- At L_max(i) the k-channel weight is 0.446, vanishing at L ≈ 0.617 (c4).

**B2. (S2) is false as worded for two frames.**
- The holomorphic flux frame trades the modulus for discrete integers.
- B1704's added fermions hold τ on the unit arc (y ≈ 0.89–1.00): C_d is a point there.
- FR-DYN below Im τ = 1.2 was not checked.
- Outputs constant without being (S1) values: m₁ ≡ 0 for isotropic sections; V ≡ 1 with one shared section and reading.
- "The object does not fix" needs sweep wording.

**B3. "V ≡ 1 (B1620)" is misattributed.**
- B1620 is the weave's group frame.
- With the record's reading (S̃, S, S) and one DR, V ≠ 1 (off-diagonal 0.02–0.16; J ≈ 7 × 10⁻⁷; c7).
- With per-sector sections, ∣V₁₂∣ reaches 0.69 (c3), and J = 2.9 × 10⁻⁵ (c5).
- "J = 0 on mirror geodesics" needs real-coefficient sections; complex ones give 4.4 × 10⁻⁶ (c5).

## CORRECTIONS

- **C1. The definition's slots.** L in 𝒦, h in D; list D per frame; a slot H for tagged hypotheses and identifications.
- **C2. (S1)'s exponents.**
  - Use the canonical-end exponents: near i, p = 1 for m₁ in the 3/2 class and 2 on the f₂(i) = 0 rows; near ω,
    (∣ε∣, ∣ε∣³).
  - The cusp is a boundary point.
  - The laws are local and section- and L-dependent.
- **C3. The lemma's scope.**
  - The record's lines have every order 1–12 and 15–30.
  - The configuration-fixed points are (i, 0), (ω, 0), (i, (½, ½)) and (ω, (⅓, ⅔)).
  - The first referee's r3 values on other lines are not configuration-fixed.
  - Reflection geodesics can be fixed on high-order lines.
- **C4.** "The six are four" is an α = 2/5 line result. B1691's law is L-free.
- **C5.** J's sign is a convention (B1750 § 2). What is fixed is J = 0 on mirror-fixed configurations.
- **C6. F3 row.**
  - z₂ is not one of the 19.
  - B1805 is NEGATIVE.
  - p/q belongs in D.
  - Add θ̄ and the Higgs's two parameters to "not reached".
- **C7. F4 row.**
  - Add B1704, B1684 and B1686.
  - W176's least is at Im τ = 4 on (0, 1/N), not on slope 2/5.
  - The pitchfork is post hoc.
  - W175 and W176 are READ, not VERIFIED.
  - Define the partial minimisation.
- **C8. The count.** FR-FIB has m = 10 and leaves 9 of the 19 unreached; the three gauge couplings were omitted.
- **C9. Labels.**
  - ℚ(√−3) is a thread fact.
  - The arrow: forced in B1750 § 2, its side a convention or CHOSEN.
  - "Shared by m003" is an inference.
  - I-18's row is internally inconsistent: its P-274 bracket says θ̄ ∈ {0, π}; its B1246 sharpening says θ, not θ̄.
  - B1162's open items are the MSSM witness's.
- **C10. Seen first.** Its sweep found 33 arcs and 17 rows. Uncited antecedents: B1652, P-139/B990, B1667, B1704,
  B1671/P-194, B213, B1670 with THE_PRICE_OF_THE_NINETEEN, B1750 § 2, THE_DERIVED_STRUCTURE_FOR_REVIEW,
  PARAMETER_CLOSURE_MASTERPLAN.
- **C11. Names.** F1–F4 collide with B1652's F1–F5, B1662's cells and GENESIS's F-FC, F-CI, F-HE, F-AP. Rename them.
- **C12. Inline the open-doors list** (PLAN.md is gitignored).
- **C13. (S3) overclaims.** f(d) is an output rank; P-418 counts inputs. P-406 as registered is not answered: re-scope it.

## NOTES

- **N1.** S248's "canonical end radius" values were at L = 0.65 and 2.5. At the exact radii at i they are 0.2080 and
  0.01907.
- **N2.** The lemma is correct; ±Γ₁(N) is torsion-free for N ≥ 4.
- **N3.** Write C(d). Use "constant per component, values reported". Take the rank on the open dense analytic set.
- **N4.** B1697's claim line still reads "m2/m3 → 1/2".

## Main's verification

- **c1, c3, c5, c6 and c7 regenerate byte-identically on main.**
- **c1's values reproduced by a separate code path** (main's `values_at_i_main.py`, its own driver of b1656_funcs) to
  every printed digit:
  - R: 0.20804 and 0.019069;
  - t = −5/288: 0.83217 and 0.076275;
  - a₀: (0.58547, 0.73081) and (0.075318, 0.6583);
  - DR: (0, 1).
- **B1704, B1684 and B1686's characterisations** checked against their verdict lines; B1652's frame names confirmed.
- **GENESIS's F-AP is the SM seat's G₂ apex frame**, not FR-G2Q.
- **All findings applied** in B1809 (CENSUS_v3).
- **Main's error.** It carried three of the first referee's claims as "accepted as stated", without recomputing them (E37
  instance).
