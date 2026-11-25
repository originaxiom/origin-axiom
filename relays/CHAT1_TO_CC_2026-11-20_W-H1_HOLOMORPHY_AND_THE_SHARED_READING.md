# W-H1: in frame C every residue and the Higgs's coefficients are holomorphic in τ. Apart from the real norms, the conjugate reading is the only ingredient that is not. Requiring the unnormalised couplings to be holomorphic in every sector therefore excludes S̃ everywhere; with the charge rule that needs a second doublet. Frame C's rule for the Higgs gives the second doublet the same triplet, a counted choice (W-D2), and the world is (S, S, S), W-D2's aligned D-1, which changes no number. The criterion predates the look, and so does this seat's statement of both its forms (W-F14); choosing its every-sector form and the shared triplet came after it. S̃ is S at the mirror point turned by the unit k, an identity of the Higgs matrix alone that does not tie the global bit to SE2

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. Nothing is compared and no target
is opened. It was written at the author's word of 2026-11-20: proceed with the seat's recommendation after W-D2.
Not W-H1 of 2026-11-17 (the harvest checked from outside), which shares the label; main's later notes cite this page as
W-H1, so it is not renamed.

**The record of the run:**
- the card: `relays/cards/CHAT1_W-H1_holomorphy_and_the_shared_reading.md`, 534014f5c (07:43:59);
- the script: `relays/chat1_2026-11-20_wh1/wh1_run.py`, 8ee4140ca (07:46:09), SHA-256 beginning 83aa26df;
- the outputs: `wh1_run_out.txt` and `wh1_output.json`, committed as produced at a3e3955d8;
- the post hoc check: `wh1_posthoc.py`, labelled.
  - Its first check was committed at 522c77f63 before its run.
  - The second was added after the first's output was read, and committed at 9e3da6fd3 before its run, together with
    the first check's output.
  - Both outputs are at 6dc7f5380.

**Disclosed.**
- **A smoke test.** After the card's commit and before the script's, the script's functions were run once at
  τ = 0.2 + 2i, which is not on the card's grid. The script was not changed afterwards.
- **H4 holds the canonical end fixed.** It holds L at its value at the base τ, because B1927's table is read in double
  precision and cannot be differenced at the script's step. The card did not say this. The script's docstring does.
- **The referee read.** The first read was cut off on 2026-11-20. Its full redo (2026-11-25, applied here) reproduced
  the run byte for byte and every number. It found:
  - the joint-holomorphy point attributed to the wrong party;
  - the global bit wrongly tied to SE2;
  - this seat's own pre-look statement of the criterion's two forms (W-F14) left undisclosed;
  - the shared triplet presented as forced, against W-D2's typing;
  - H4's height-6 failure coming mostly from the fixed end;
  - the supersymmetry analogy overstated.
  Its own checks (independent evaluations of H0 to H3, the chain-rule H4, the triplets of B1691's module) are cited as
  the referee's and are not committed.

**Typing.** [E] means established on record, by the run, or by the referee where it says so. [J] means this seat's
judgement.

## 0. In short

1. **[E] The holomorphic ingredients.** Over two points, two columns and three heights:
   - the frame's three Higgs coefficients are holomorphic in τ (Cauchy–Riemann residual ρ ≤ 5e-41);
   - so are all 11 non-zero channel residues of the up, down and lepton sectors (ρ ≤ 1.5e-38), and the characteristics
     of both signs are among them.
2. **[E] The two readings.** With the reading S, every channel's unnormalised coupling is holomorphic (ρ ≤ 2.3e-39).
   With S̃, every channel's is not: ρ is 1.19 to 25.
3. **[J] The argument, in steps 5 to 7.**
   - Requiring the unnormalised couplings to be holomorphic in every sector, as the matter's residues already are,
     excludes S̃ in every sector.
   - With one doublet the charge rule then has no holomorphic solution. The up quarks need a second doublet of opposite
     hypercharge: one of the two standard reasons for two doublets (the other, the higgsino anomaly, has no counterpart
     here).
   - Frame C's Higgs never uses its hypercharge (P-847), so frame C's rule gives both doublets the same triplet, a
     counted choice (W-D2). That gives (S, S, S).
4. **[E] The real norms, with the canonical end held fixed.** The normalised couplings are not holomorphic, but the
   breaking falls with height:
   - ρ is 3e-2 to 1e-1 at height 1.5;
   - 2e-3 to 4e-2 at height 3;
   - 6e-6 to 6e-3 at height 6.
   With the end's τ-dependence folded in by the chain rule (B1927's table gradient, one-sided at the table's top,
   height 6), the referee finds 5.5e-4 to 1.3e-3 at the mark at height 6. The low values come from the fixed end.
5. **[E] The mirror, post hoc and exact.** S̃(τ) = −Q_K S(−τ̄) Q_K⁻¹: the conjugate reading is the holomorphic reading
   at the mirror point, turned by the unit k. The card's simpler form (H3) fails. The identity concerns the Higgs matrix
   alone.
6. **[J] What it means.**
   - Holomorphy, required in every sector, turns the reading from a choice into a consequence. The price is a second
     doublet, its shared triplet (a counted choice), and the principle itself.
   - As a criterion for the reading it is on record from before the look (P-847, 2026-11-14), and so is this seat's
     statement of its two forms (W-F14, 2026-11-14). Choosing its every-sector form, and the shared triplet, came after
     the look. Main rules on the standing.

## 1. The expectations, as sealed

| cell | prediction | outcome |
|---|---|---|
| H0 | ρ ≤ 1e-15 for every c_i at every τ | holds; at most 4.8e-41 |
| H1 | ρ ≤ 1e-15 for every non-zero channel's residue, every sector, every τ | holds; at most 1.5e-38, 11 channels at each τ |
| H2 | ρ ≤ 1e-15 for every channel with S, and ρ ≥ 0.1 for some channel with S̃, at every τ | holds. With S, at most 2.24e-39. With S̃, every channel has 1.19 ≤ ρ ≤ 25 |
| H3 | \|S̃(τ) − S(−τ̄)\| ≤ 1e-20 \|S(τ)\| at every τ | **failed.** The relative difference is 0.61 to 1.0; per the referee it is exactly 2\|c₃(−τ̄)\|/\|S(τ)\|₁. Post hoc: conj(c_i(τ)) = σ_i·c_i(−τ̄) with σ = (+1, +1, −1), exactly. So S̃(τ) = −Q_K S(−τ̄) Q_K⁻¹, with a residual of 0 at 40 digits |
| H4 | ρ ≥ 1e-3 for the normalised coupling with S at every τ | **failed**, at the mark at height 6 only, and with L held fixed. It holds at heights 1.5 and 3. At height 6, ρ is 5.9e-6 (up) and 2.2e-4 (down) at the mark, and 6.2e-3 and 1.35e-3 at the twin. With L's τ-dependence folded in (the referee's), 5.5e-4 to 1.3e-3 at the mark |

## 2. The argument, step by step

1. **[E] The channel structure.** Frame C's coupling is a sum over the units s of n_s·R_s(τ)·K_s(H), where:
   - n_s is the channel's real norm (B1919's, with Theorem 90's weight and the canonical end);
   - R_s is the closed-form residue (B1906);
   - K_s(H) is the contraction C_aᵀ ε H C_b ∘ E_s.
   This is main's B1940 frame_mp. The script imports it and repeats its per-sector steps through W-D2's script.
2. **[E] The residues are holomorphic, and the norms are real-analytic** (H1, H4).
   - The residues are theta constants over η³, for the characteristics of both signs. That agrees with P-847's reason
     for not accepting agy-exp's claim that holomorphy picks one world: theta functions of either sign of characteristic
     are jointly holomorphic in (z, τ).
   - The norms break holomorphy, with a residual that falls with height.
   - [J] This resembles the split of a holomorphic superpotential coupling and its real Kähler normalisation, but is not
     the same split. There the real factors rescale whole fields. Here each channel carries its own norm (n_s is 3.4 to
     5.8 across channels at one τ, per the referee), so the normalised coupling is a sum of holomorphic terms with
     different real weights.
3. **[E] S is holomorphic in τ and S̃ is not** (H0, H2). S̃ conjugates the triplet's coefficients. Post hoc it equals
   −Q_K S(−τ̄) Q_K⁻¹, so the Higgs matrix S̃ is holomorphic in the mirror's complex structure, not in τ's.
4. **[E] With S, every channel's unnormalised coupling is holomorphic. With S̃, none is** (H2). So the conjugate reading
   is the only ingredient of frame C's couplings, apart from the real norms, that is not holomorphic.
5. **[J] One doublet has no holomorphic solution in every sector.** The charge rule makes the up quarks take the
   conjugate of the reading the down quarks and leptons take (P-847, main's reading by charge; an argument, not banked,
   and frame C's code does not enforce it). So with one doublet, holomorphy cannot hold in every sector. A
   gauge-invariant holomorphic coupling for the up quarks needs a second doublet of opposite hypercharge.
   - This is the remark of W-F14 (2026-11-14, § 3, before the look). It set out both forms: required of a named sector,
     holomorphy fixes the global bit with one doublet (W₋ or W₊, both deranged on the act's line, W-D2 C1); required of
     every sector, it excludes both one-doublet assignments. Choosing the every-sector form and adding a second doublet
     is the step taken after the look.
6. **[J] The second doublet's triplet is frame C's rule, a counted choice.** Frame C's Higgs carries no line: its
   hypercharge is defined in the code and never used (P-847). So frame C's rule gives a second doublet the same triplet.
   - Holomorphy alone does not: B1691's module has other holomorphic triplets (R, D²R and their combinations, per the
     referee).
   - B1946 drew from the same line-free premise that nothing forces either reading. P-847's note of 2026-11-15 declined
     one reading for one object after the look. W-D2 typed the shared mode as a counted choice. This page does not lift
     that typing.
   - Main's later note (B1974, 2026-11-24) forces the shared triplet only under further hypotheses, and still records it
     as this seat's counted choice.
   - In frame D1 the Higgs's twist scales with its charge (W-B2; B1962), so two doublets of opposite charge would carry
     different modes. That case is open and not computed here.
7. **[J] So holomorphy in every sector, the charge rule and frame C's rule for the triplet give (S, S, S).** That is
   W-D2's D-1, aligned on the act's line, with rates identified numerically on a grid of tenths.
   - In frame C the second doublet changes no number: D-1 is, number for number, the one-doublet (S, S) the charge rule
     excludes (W-D2 § 2). It changes the typing.
   - The record's other same-reading world, (S̃, S̃, S̃), is excluded by holomorphy in τ. W-D2's referee found it aligned
     at the act's line's two points too, so there the alignment does not tell the two same-reading worlds apart;
     holomorphy does.

## 3. What it means, and its standing

- [J] **It changes the type of the reading.** The relative reading, (S, S, S) against the mixed worlds, becomes a
  consequence of holomorphy in every sector, given two doublets and the shared triplet.
- [E] **The global bit is fixed as well, and not by SE2.** The post hoc identity concerns the Higgs matrix alone: with S̃
  each channel's coupling is holomorphic in neither τ nor −τ̄ (ρ is 1.19 to 25 in τ, so 0.04 to 0.84 in −τ̄, per the
  referee). The identity does not tie the bit to SE2, and P-847 records the fibre mirror's exchange of S and S̃ as tested
  and refuted. Main's later note (P-847, 2026-11-20, with B1970) records the global bit as fixed by holomorphy.
- [J] **What it costs.**
  - It removes the Higgs reading as a free input: C04 in W-P1A, the Higgs world.
  - It adds a second doublet. FK15 is OPEN, and the record's Higgs is "forced to exist, not forced which".
  - It keeps the shared triplet as a counted choice (W-D2).
  - It adds holomorphy as a principle, imposed on the unnormalised couplings. The norms are not holomorphic, which is
    P-847's caveat that the criterion is weaker than B1927's.
  - Whether that is a net saving is main's to count.
- [E] **Its standing on record.**
  - P-847 listed holomorphy of the Higgs reading as an untested criterion that would select S on 2026-11-14, and W-F14
    set out its two forms the same day. Both are before B1946 found (S, S) aligned on 2026-11-15.
  - B1946 and P-847's note of 2026-11-15 rule that one reading for one object is not adopted after the look, and that
    both same-reading options must be declared and sealed.
  - Since this page, main has recorded the result as derived given hypotheses, found after the look (P-847's note of
    2026-11-20, with B1970).
- [J] **This page's contribution.** It shows that the criterion's every-sector form, with the charge rule, needs a
  second doublet, and with frame C's rule for the triplet gives (S, S, S) rather than (S̃, S̃, S̃). That consequence,
  and the two choices it rests on, came after the look. Whether it lifts B1946's ruling is main's to say.
- [E] **It does nothing for the leptons.** They stay tied to the down quarks in (S, S, S) (W-D2).

## 4. Limits

- The holomorphy checks are numerical: finite differences at 60 digits, at the act's line's two points and six values
  of τ (12 cells; H0 and H3 depend on τ alone). They are not a proof. Steps 2 to 4 also follow from the construction:
  thetas and η are holomorphic, and S̃ conjugates its coefficients.
- H4 holds the canonical end fixed.
- The post hoc identity for S̃ is checked at three values of τ at 40 digits. Per the referee it follows from the
  q-series: c₁ and c₂ have real coefficients and c₃ imaginary ones (B1691's R carries iθ₃², which the Serre derivative
  keeps), so conj c_i(τ) = σ_i c_i(−τ̄) term by term. H3 fails for that reason. The card's premise for H3 was false on
  the record, since B1691's R already carries the i.
- Steps 5 to 7 are an argument on the record's charge rule. They are not a computation of a two-doublet frame.
- It compares nothing.

0 of 19.
