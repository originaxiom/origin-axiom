# THE CHARGE LAW (P-737): PROVED where lcm(S) ≤ 10, S = {5} included; REFUTED where lcm(S) ≥ 12 (the explore seat, 2026-11-07)

**The record of the run:**
- the plan and the script were pushed before the run (c262308cc);
- the output was committed unread (9ca836350), then read;
- the post-run checks were written after the read and are disclosed below.

**Kind:** data-free mathematics; no frame value, no data, no held-out quantity.

## The statement P-737 asked about

Under the charge premise at a set S of levels (E ≡ ±I mod every N ∈ S), the least-excess-length departure is the single
run lcm(S) + 1, uniquely, with apex (n − 1)/2 + √5/2. P-737 also asked: is that run the shortest word with the premise?

## The answers

1. **PROVED for every S ⊆ {2, 3, 4, 5} with lcm(S) ≤ 10:** S = {2}, {3}, {4}, {5}, {2, 3}, {2, 4} and {2, 5}.
   - Over all defects, of any number of runs, any run lengths and any gaps, the single run lcm(S) + 1 is the unique
     least-excess departure under the 2D action, at apex depth lcm(S)/2 + √5/2.
   - **For S = {5}, the record's deep candidate:** the run of 6 is proved. It is the unique least-excess departure
     invisible to the level-5 charge, at depth 3.618 = √5·φ.
2. **REFUTED for every S with lcm(S) ≥ 12:** S = {3, 4}, {3, 5}, {4, 5}, {2, 3, 4}, {2, 3, 5}, {2, 4, 5}, {3, 4, 5}
   and {2, 3, 4, 5}. Explicit counterexamples satisfy the premise with less excess than the single run. All but the
   first lie outside the ranges R1 ∪ R2.
3. **The shortest-word clause is false for every lcm(S) ≥ 6.** The fewest extra letters over premise-satisfying
   multi-run defects is:

   | S | fewest extra letters | lcm(S) |
   |---|---|---|
   | {2, 3} | 4 | 6 |
   | {2, 5} | 6 | 10 |
   | {3, 4} | 4 | 12 |
   | {3, 5} | 5 | 15 |
   | {4, 5} | 6 | 20 |
   | {2, 3, 5} | 6 | 30 |
   | {2, 3, 4, 5} | 6 | 60 |

## The proof

The lemmas are in PROOF_DRAFT_LEMMAS.md, written during the run and before the read. Their numerical checks are in
charge_law_proof_out.txt, parts A to D.

- **Lemma A.** ΔS = 2 log Q(E), with Q(E) = vᵀEv/vᵀv and v = (1, φ). It holds on all 42 768 R1 defects to 1.2e-13
  against the web seat's `excess`.
- **Lemma B.** Q = Σ_A Π s_i (1/√5) Π_{consecutive} F_d/φ^d. It holds to 6e-14 on R1, and to 7e-15 on 4000 sampled
  R2 defects.
- **Lemma C.** F_d/φ^d ≥ φ⁻², with equality only at d = 2 (d = 1..300; Binet). Hence Q ≥ B(s) = 1 + (φ²/√5)
  (Π(1 + s_i/φ²) − 1), exact for one nontrivial run.
- **Lemma D.** L^s ≡ ±I mod N ⟺ N ∣ s (checked to s = 120). The apex of the single run n is (n − 1)/2 + √5/2, by
  Perron's formula (checked for n = 2..80; exact to the printed digits).
- **Lemma E.** Golden runs leave E unchanged, and a nontrivial run at position p multiplies E by P(p)^s, with phases
  mod 2·ord(LR mod L).

So the least B over premise-satisfying multi-run defects is a shortest path on SL(2, ℤ/L). It was computed exactly and
exhaustively, over every phase and every s ≤ L − 1.

**The decisive inequality, for the proved cases.** The least multi-run B-cost exceeds θ_L = log(1 + L/φ²):

| S | margin over θ_L |
|---|---|
| {2} | +0.0795 |
| {3} | +0.1275 |
| {4}, {2, 4} | +0.1597 |
| {5} | +0.1828 |
| {2, 3} | +0.0231 |
| {2, 5} | +0.0017 |

So every premise-satisfying multi-run defect has Q ≥ B > 1 + L/√5 = Q(single run). With Lemma D this proves the
statement. ∎

## The counterexamples (post_run_counterexamples.py)

**How each was checked:**
- it was built from the search's minimizing phase sequence, at the least positions;
- E was checked in exact integers;
- the excess was computed by the web seat's own `excess`, and again by Lemma A at 120 digits.

**Disclosed:** the first attempt crashed at S = {4, 5}, in the float Lemma-A cross-check (E's entries reach about 1e29 at
long gaps). Its logs are kept as `attempt1_*`, and the rerun uses 120 digits.

| S | defect (nontrivial runs at positions) | runs in all | excess | single run lcm + 1 | its highest apex |
|---|---|---|---|---|---|
| {3, 4} | 2 at 1, 3 at 4, 2 at 7 | 7 | 2.788622 | 3.702120 | 2.080 |
| {3, 5} | 3 at 1, 2 at 6, 3 at 11 | 11 | 3.299674 | 4.084570 | 2.115 |
| {4, 5} | 2 at 1, 2 at 17, 4 at 64, 2 at 69 | 69 | 3.922421 | 4.593993 | 2.615 |
| {2, 3, 5} | 5 at 1, 2 at 33, 2 at 129 | 129 | 3.529822 | 5.336734 | 3.118 |
| {3, 4, 5} and {2, 3, 4, 5} | 2 at 1, 2 at 17, 4 at 19, 2 at 129 | 129 | 3.867202 | 6.652431 | 2.671 |
| (control) {5} | 2 at 1, 5 at 21 | 21 | 2.790542 | 2.348718 | (not below) |

These are counterexamples, not minimizers. The least-excess departure at these S is not established here. It is at most
the excess shown, and its apex need not be the one shown.

## What this corrects

**THE LEVEL PREMISE AS A CONSERVATION LAW** (this seat's relay; B1853 verified it in range). The ladder's two upper rows
were range artifacts:
- "charge at {4, 5} → (21), depth 11.118";
- "charge at 2..5 → (61), depth 31.118".

At those S the single long run is not least action. The depth law lcm(S)/2 + √5/2 holds exactly where lcm(S) ≤ 10. So
depth does not rise without bound with the conserved levels: the counterexamples at lcm ≥ 12 have apexes near 2.1–3.1.

**What stands:**
- HL1 and HL2, the two exact readings;
- P0, P1 and P2's selections: (2), (2, 1, 1, 1, 2) and (6), with (6) now proved for all defects;
- the post hoc fact that LR fixes a line only at 5.

**What this does to the depth question.** Among the charge premises, S = {5}, the record's own ramified prime, is where
the single deep run is provably least action. Conserving more rungs does not deepen the departure under least action.

## Scope

- The 2D action, excess length, only. The volume statement has no closed form and stays a range result (HL4).
- L-start defects. The R-start ones are their mirrors (P-336).
- The rungs 2..5.

0 of 19.
