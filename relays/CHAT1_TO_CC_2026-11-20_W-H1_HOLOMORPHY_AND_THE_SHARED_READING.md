# W-H1: in frame C every residue and the Higgs's coefficients are holomorphic in τ. Apart from the real norms, the conjugate reading is the only ingredient that is not. Requiring the unnormalised couplings to be holomorphic therefore excludes S̃ in every sector. With the charge rule that needs a second doublet, and frame C's line-free Higgs gives it the same triplet: the world (S, S, S), W-D2's aligned D-1. The criterion predates the look; its two-doublet form does not. S̃ turns out to be S at the mirror point, turned by the unit k

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. Nothing is compared and no target
is opened. It was written at the author's word of 2026-11-20: proceed with the seat's recommendation after W-D2.

**The record of the run:**
- the card: `relays/cards/CHAT1_W-H1_holomorphy_and_the_shared_reading.md`, 534014f5c (07:43:59);
- the script: `relays/chat1_2026-11-20_wh1/wh1_run.py`, 8ee4140ca (07:46:09), SHA-256 beginning 83aa26df;
- the outputs: `wh1_run_out.txt` and `wh1_output.json`, committed as produced at a3e3955d8;
- the post hoc check: `wh1_posthoc.py`, labelled. Its first check was committed at 522c77f63 before its run. The second
  was added after the first's output was read, and committed at 9e3da6fd3 before its run. Its output is at 6dc7f5380.

**Disclosed.**
- **A smoke test.** Before the script's commit, its functions were run once at τ = 0.2 + 2i, which is not on the card's
  grid. The script was not changed afterwards.
- **H4 holds the canonical end fixed.** It holds L at its value at the base τ, because B1927's table is read in double
  precision and cannot be differenced at the script's step. The card did not say this. The script's docstring does.

**Typing.** [E] means established on record or by the run. [J] means this seat's judgement.

## 0. In short

1. **[E] The holomorphic ingredients.** Over two points, two columns and three heights:
   - the frame's three Higgs coefficients are holomorphic in τ (Cauchy–Riemann residual ρ ≤ 5e-41);
   - so are all 11 non-zero channel residues of the up, down and lepton sectors (ρ ≤ 1.5e-38), and the characteristics
     of both signs are among them.
2. **[E] The two readings.** With the reading S, every channel's unnormalised coupling is holomorphic (ρ ≤ 2.2e-39).
   With S̃, every channel's is not: ρ is 1.19 to 25.
3. **[J] The argument, in steps 5 to 7.**
   - Requiring the unnormalised couplings to be holomorphic, as the matter already makes them, excludes S̃ in every
     sector.
   - With one doublet the charge rule then has no solution. The up quarks need a second doublet of opposite
     hypercharge, the standard reason for two doublets.
   - Frame C's Higgs never uses its hypercharge (P-847), so both doublets carry the same triplet. That gives (S, S, S).
4. **[E] The real norms.** The normalised couplings are not holomorphic, but the breaking falls with height:
   - ρ is 3e-2 to 1e-1 at height 1.5;
   - 2e-3 to 4e-2 at height 3;
   - 6e-6 to 6e-3 at height 6.
5. **[E] The mirror, post hoc and exact.** S̃(τ) = −Q_K S(−τ̄) Q_K⁻¹: the conjugate reading is the holomorphic reading
   at the mirror point, turned by the unit k. The card's simpler form (H3) fails.
6. **[J] What it means.**
   - Holomorphy turns the reading from a choice into a consequence, at the price of a second doublet and of the
     principle itself.
   - As a criterion for the reading it is on record from before the look (P-847, 2026-11-14). Its two-doublet form,
     and the aligned world it gives, are stated after the look. Main rules on the standing.

## 1. The expectations, as sealed

| cell | prediction | outcome |
|---|---|---|
| H0 | ρ ≤ 1e-15 for every c_i at every τ | holds; at most 4.8e-41 |
| H1 | ρ ≤ 1e-15 for every non-zero channel's residue, every sector, every τ | holds; at most 1.5e-38, 11 channels at each τ |
| H2 | ρ ≤ 1e-15 for every channel with S, and ρ ≥ 0.1 for some channel with S̃, at every τ | holds. With S, at most 2.2e-39. With S̃, every channel has 1.19 ≤ ρ ≤ 25 |
| H3 | \|S̃(τ) − S(−τ̄)\| ≤ 1e-20 \|S(τ)\| at every τ | **failed.** The relative difference is 0.61 to 1.0. Post hoc: conj(c_i(τ)) = σ_i·c_i(−τ̄) with σ = (+1, +1, −1), exactly. So S̃(τ) = −Q_K S(−τ̄) Q_K⁻¹, with a residual of 0 at 40 digits |
| H4 | ρ ≥ 1e-3 for the normalised coupling with S at every τ | **failed.** It holds at heights 1.5 and 3. At height 6, ρ is 5.9e-6 (up) and 2.2e-4 (down) at the mark, and 6.2e-3 and 1.35e-3 at the twin |

## 2. The argument, step by step

1. **[E] The channel structure.** Frame C's coupling is a sum over the units s of n_s·R_s(τ)·K_s(H), where:
   - n_s is the channel's real norm (B1919's, with Theorem 90's weight and the canonical end);
   - R_s is the closed-form residue (B1906);
   - K_s(H) is the contraction C_aᵀ ε H C_b ∘ E_s.
   This is main's B1940 frame_mp, which the script imports.
2. **[E] The residues are holomorphic, and the norms are real-analytic** (H1, H4).
   - The residues are theta constants over η³, for the characteristics of both signs. That agrees with P-847's record
     of agy-exp's point that such thetas are jointly holomorphic.
   - The norms break holomorphy, with a residual that falls with height.
   - [J] This is the split of a holomorphic coupling and a real normalisation that supersymmetric couplings have. Here
     it is found in frame C's construction, not imposed.
3. **[E] S is holomorphic in τ and S̃ is not** (H0, H2). S̃ conjugates the triplet's coefficients. Post hoc it equals
   −Q_K S(−τ̄) Q_K⁻¹, so it is holomorphic in the mirror's complex structure, not in τ's.
4. **[E] With S, every channel's unnormalised coupling is holomorphic. With S̃, none is** (H2). So the conjugate reading
   is the only ingredient of frame C's couplings, apart from the real norms, that is not holomorphic.
5. **[J] One doublet has no holomorphic solution.** The charge rule makes the up quarks take the conjugate of the
   reading the down quarks and leptons take (P-847, main's reading by charge). So with one doublet, holomorphy cannot
   hold in every sector. A gauge-invariant holomorphic coupling for the up quarks needs a second doublet of opposite
   hypercharge.
6. **[J] Both doublets carry the same triplet.** Frame C's Higgs carries no line: its hypercharge is defined in the code
   and never used (P-847). So its triplet does not depend on its charge, and in frame C the shared mode is not a second
   choice.
   - In frame D1 the Higgs's twist scales with its charge (W-B2; B1962), so two doublets of opposite charge would carry
     different modes. That case is open and not computed here.
7. **[J] So holomorphy, the charge rule and frame C's line-free Higgs give (S, S, S).** That is W-D2's D-1, aligned on
   the act's line, with rates identified numerically on a grid of tenths.
   - The record's other same-reading world, (S̃, S̃, S̃), is excluded by holomorphy in τ. W-D2's referee found it
     aligned on the act's line too, so the alignment there does not depend on which of the two holomorphy picks.

## 3. What it means, and its standing

- [J] **It changes the type of the reading.** The relative reading, (S, S, S) against the mixed worlds, becomes a
  consequence of holomorphy, given two doublets. The global bit is tied to the orientation: holomorphy in τ against
  holomorphy in −τ̄, which by the post hoc identity exchanges S and S̃ up to the unit k. The orientation is SE2's
  counted choice.
- [J] **What it costs.**
  - It removes the Higgs reading as a free input: C04 in W-P1A, the Higgs world.
  - It adds a second doublet. FK15 is OPEN, and the record's Higgs is "forced to exist, not forced which".
  - It adds holomorphy as a principle, imposed on the unnormalised couplings. The norms are not holomorphic, which is
    P-847's caveat that the criterion is weaker than B1927's.
  - Whether that is a net saving is main's to count.
- [E] **Its standing on record.**
  - P-847 listed holomorphy of the Higgs reading as an untested criterion that would select S on 2026-11-14. That is
    before B1946 found (S, S) aligned on 2026-11-15.
  - B1946 and P-847's note of 2026-11-15 rule that one reading for one object is not adopted after the look, and that
    both same-reading options must be declared and sealed.
- [J] **This page's contribution.** It shows that the earlier criterion, applied with the charge rule, forces the
  two-doublet world and singles out (S, S, S) from (S̃, S̃, S̃). That consequence was found after the look. Whether it
  lifts B1946's ruling is main's to say.
- [E] **It does nothing for the leptons.** They stay tied to the down quarks in (S, S, S) (W-D2).

## 4. Limits

- The holomorphy checks are numerical: finite differences at 60 digits, at 12 points on the act's line. They are not a
  proof. Steps 2 to 4 also follow from the construction: thetas and η are holomorphic, and S̃ conjugates its
  coefficients.
- H4 holds the canonical end fixed.
- The post hoc identity for S̃ is checked at three values of τ at 40 digits, not derived.
- Steps 5 to 7 are an argument on the record's charge rule. They are not a computation of a two-doublet frame.
- It compares nothing.

0 of 19.
