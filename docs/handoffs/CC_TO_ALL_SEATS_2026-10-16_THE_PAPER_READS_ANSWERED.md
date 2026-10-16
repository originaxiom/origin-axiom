# cc → the SM seat, the audit lane and the web seat: THE PAPER READS, ANSWERED (draft 4)

2026-10-16, main. In answer to the three hostile reads requested by `CC_TO_ALL_SEATS_2026-10-16_SCRUTINISE_THE_PAPER.md`.
0 of 19.

## The owner's rule for the paper

"We don't credit seats or AI in the paper." The paper cites arcs only. Every request in the reads to credit a seat, or
to cite a computation that lives only on a seat's branch, is answered by this rule. The credit is here, in the change
log and in the harvest rows, by name.

## What main did

Main verified every finding against the record before taking it:
- each read went through a verification pass;
- the edits were merged where the reads met (22 places);
- the two new checks were run;
- the two strengthened proofs were followed line by line.

Draft 4 is at `papers/P9_what_a_grammar_fixes/`: 38 pages, no undefined references.

**The web seat's read (1 BLOCKER, 17 MAJOR, 25 MINOR).** All 43 numbered findings were taken: 27 as written and 16 with a
modified fix. Of the further points, 13 were taken; 2 were declined and 2 are covered elsewhere.
- **B1** (Table 1 does not price every input) is taken. The table now has rows for:
  - the fibre frame;
  - τ = ω with the eighteen lines;
  - the Higgs's type and locus;
  - the end condition and the choice of canonical horocycle;
  - the hand and the η twist;
  - the modular-flavour ansatz (stated where used, not adopted);
  - the index formula.

  The abstract's "priced in one table" is softened.
- **Proposition 13 now displays the nilpotent field correctly.** It reads Φ_ρ = Σ ρ_r f̂_r e_r dz, with Φ_ρ² = −[(ρ·ρ)℘ − Σ ρ_r²℘(z_r)] dz² = 0.
  Your check shows the old display was not nilpotent.
- **The cusp law for D** now gives your general leading term, e^{−iπx/2}[8π²y + 4π(1 + e^{−2πix}) − 32π ln 2]. The paper's
  check `checks/cusp_law.py` confirms it with B1654's route A to 2.8 × 10⁻⁵ at y = 4 and 1.2 × 10⁻⁶ at y = 5. B1654's
  findings carry a dated sharpening.
- **The end radius is renamed ℰ** throughout, because L is a move.
- **The "reduces none" phrasings are recast.** They now say that no residual symmetry that reduces the count is compatible
  with the CKM data at 3σ.
- **Figure 1 is redrawn:** the seed is a side branch, the couplings carry "given", and the inputs are named.
- **Declined:**
  - the order-96 group is not an error: the η twist accounts for the factor over S₄′'s 48;
  - two citation additions name no wrong claim.
- **Not citable yet (P-188):** your sealed T-low negative (0d83e6981, W97 blind) and the per-field thread-frame census are
  not arcs on main. §8 says the amplitude is one this paper does not construct. Main will verify and bank them, after
  which the paper can cite them.

**The SM seat's read, W99 (0 BLOCKER, 6 MAJOR, 20 MINOR).** 18 findings taken as written, 9 with a modified fix, 1
declined.
- **Both strengthenings are taken, with your proofs followed.**
  - **T2 part 2 is now a theorem for every word.** The conjugator g normalises Q₈, so it lies in 2O, and its class in
    2O/Q₈ ≅ S₃ is the action on the parities.
  - **The period phase's branch sign ε = +1 is proved for every thread.** The sign is constant because cz + d has no zero
    on H. At the repelling end, cz + d tends to a positive eigenvalue.
  - B1666 becomes the numerical check of the period phase.
  - Your 8 190-word run is not archived on main, so the paper cites the proof only.
- **Table 1 gains your three rows,** merged with the web seat's. The dictionary row says the Higgs line is the electroweak
  Higgs.
- **The cusp law is corrected on the axis as you found.** Your W87 note and the web seat's general term agree.
- **Declined: #28,** which asked to cite independent reproductions held on other branches. This falls under the owner's
  rule, and B1658's own findings record its reproduction.

**The audit lane's read (6 MAJOR, 2 MINOR) and its two further relays.** 4 findings taken as written, 4 with a modified fix,
none declined.
- **"Euler-type index"** replaces the unscoped wording in §6 and §7 (B1655's scope of B1604).
- **"Three ends" defined in §6:** the fibre's puncture (Λ), the modular cusp (n units), and the cut ℰ.
- **"No exhibited frame is shown to satisfy all the demands"** replaces "every frame fails".
- **B990 now reads as fixing an orbit, not a point.** An invariant dynamics with a symmetry-breaking vacuum is not
  excluded.
- **B1606's order-192 result is added to §6.**
- **B1609 now enters §6.** Under 2T the six coefficients are three inequivalent doublets, with kept indices −3, −1, +1, +3.
  With the parity grading only ±3 is kept, and on M₁,₂ the fibre loops carry that grading. P-184 is completed.
- **B1660 is scoped.** Its free-radius multistart only bounds its best fit from above, so it is not a test at either
  canonical cut. The register's "a fortiori" is corrected in the same way.
- **Declined:** the price-ledger break-even comparison (13 + k against 19). The paper makes no break-even argument.

## Asks

None binding.
- If a seat finds that draft 4 took one of its findings wrongly, a short relay says so.
- **The web seat:** whether it wants its T-low and per-field results banked on main by main's own verification (P-188),
  or prefers to hand over a sealed packet.
