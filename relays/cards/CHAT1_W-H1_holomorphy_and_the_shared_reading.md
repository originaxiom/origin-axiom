# Card W-H1: holomorphy and the shared reading. Does requiring frame C's couplings to be holomorphic in τ, as its matter couplings already are, force every sector to read S (W-D2's D-1), rather than leave it a choice? Data-free

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `card:` data-free. It was written at the author's word of
2026-11-20: proceed with the seat's recommendation after W-D2. The card is committed before its script, and the script
before its run. Nothing is compared, and no target is opened.

## 1. The question and the record

- **The question.** W-D2 found that on the act's line frame C's cusp mixing is aligned when every sector reads S, the
  world (S, S, S). The record rules that choosing (S, S) after the look is post hoc (B1946; P-861). This card asks
  whether a principle forces that world.
- **The candidate is on record from before the look.** P-847, 2026-11-14: "S is built from modular forms evaluated at
  τ (holomorphic), S̃ is its twisted conjugate; holomorphy of the Higgs reading would select S". P-847 adds that the
  rest of the frame is real-analytic, so the criterion is weaker than B1927's. B1946's alignment of (S, S) is dated
  2026-11-15.
- **What stands against it on record.**
  - With one doublet, the charge rule makes the up sector take the conjugate of the reading the down quarks and leptons
    take (P-847, main's reading by charge). So holomorphy cannot hold in every sector with one doublet.
  - P-847 did not accept agy-exp's claim that holomorphy picks one world, and agy-exp withdrew it. The reason:
    theta functions of either sign of characteristic are jointly holomorphic in (z, τ), and the U(1)_Y flip stands.
  - B1946, and P-847's note of 2026-11-15: one reading for one object is not adopted, because it would be chosen after
    the look.

## 2. The argument to be typed (in the relay, not by the run)

1. Frame C's coupling is a sum over channels. Each channel is a real normalisation times a residue R_s(τ) times a
   contraction with the Higgs matrix (B1940's frame_mp).
2. The residues are holomorphic in τ, since they are theta constants and η. That covers the characteristics of both
   signs, which is agy-exp's point. The normalisations are real-analytic. This is the split of a holomorphic coupling
   and a real normalisation.
3. The Higgs matrix S is built from q-series in τ. S̃ = ε S* εᵀ conjugates its coefficients, so S̃ is antiholomorphic
   in τ.
4. Requiring every channel's unnormalised coupling to be holomorphic in τ, as the matter already makes it, therefore
   excludes S̃ in every sector.
5. With one doublet the charge rule then has no solution. A gauge-invariant holomorphic coupling for the up quarks
   needs a second doublet of opposite hypercharge. This is the standard reason for two doublets.
6. In frame C the Higgs carries no line: its hypercharge is defined in the code and never used (P-847). So its fibre
   triplet does not depend on its charge, and both doublets carry the same S.
7. So holomorphy, the charge rule and frame C's line-free Higgs give (S, S, S), W-D2's D-1. Its alignment on the act's
   line follows.

## 3. What is computed (exact checks of steps 2, 3 and 4)

- **Points and τ:** the mark and the twin on the act's line, at the columns x = 0.13 and 0.31 and the heights 1.5, 3
  and 6. That is 12 values of τ.
- **The holomorphy test:** the Cauchy–Riemann residual ρ = max|∂_τ̄ f| / max|∂_τ f|. The derivatives are central
  differences in x and y, with step 10^(−dps/3) at 60 digits.
- **H0, the Higgs coefficients.** ρ for the three components c_i(τ) of the frame's own triplet.
- **H1, the residues.** ρ for R_s(τ), for every channel that is not zero, in the up, down and lepton sectors.
- **H2, the unnormalised channel couplings.** ρ for R_s(τ)·(C_aᵀ ε H C_b ∘ E_s), every channel, with H = S and with
  H = S̃.
- **H3, the mirror.** Whether S̃(τ) = S(−τ̄): the conjugate reading at τ equals the holomorphic reading at the mirror
  point. That holds if the q-series have real coefficients. The check reports the relative difference.
- **H4, the normalised coupling.** ρ for the physical coupling Y(τ), with the norms, with H = S.

## 4. Expectations (committed now)

| cell | prediction | prior |
|---|---|---|
| H0 | ρ ≤ 1e-15 for every c_i at every τ | 95 % |
| H1 | ρ ≤ 1e-15 for every channel's residue that is not zero, in every sector, at every τ | 90 % |
| H2 | ρ ≤ 1e-15 for every channel with H = S, and ρ ≥ 0.1 for some channel with H = S̃, at every τ | 85 % |
| H3 | \|S̃(τ) − S(−τ̄)\| ≤ 1e-20·\|S(τ)\| at every τ | 70 % |
| H4 | ρ ≥ 1e-3 for the normalised coupling with H = S, at every τ | 85 % |

## 5. What the outcomes mean (fixed now)

- **H0 to H2 hold.**
  - The only ingredient of frame C's couplings that is not holomorphic, apart from the real normalisations, is the
    conjugate reading.
  - Steps 2 to 4 are then established, and the relay types steps 5 to 7.
  - The principle's standing: as a criterion for the reading it predates the look (P-847, 2026-11-14). Its
    two-doublet form, and what it implies, are stated here after the look (W-D2). Main rules on whether that lifts
    B1946's post hoc ruling.
- **H2 fails for S.** Some ingredient other than the reading breaks holomorphy. Step 4 does not hold, and the argument
  stops there.
- **H3 holds.** S̃ is S read in the mirror's complex structure. So requiring holomorphy in τ, not in −τ̄, ties the
  global bit to the orientation, which SE2 counts. The relay types that tie.
- **H4.** Whether "the rest of the frame is real-analytic" bites: the norms break holomorphy only as a real
  normalisation would.

## 6. What this card does not do

- It compares nothing.
- It does not compute frame D1's two-doublet world, in which the Higgs's twist depends on its charge.
- It does not touch the leptons, which stay tied to the down quarks (W-D2).
- It does not decide whether holomorphy is the programme's own principle. It checks what the principle needs and what
  it implies in frame C.

0 of 19.
