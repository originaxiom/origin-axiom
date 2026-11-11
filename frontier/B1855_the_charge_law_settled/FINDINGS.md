# B1855 — THE CHARGE LAW SETTLED: THE RUN OF 6 IS PROVED LEAST UNDER THE LEVEL-5 CHARGE; THE LAW FAILS FROM lcm(S) = 12 (the explore seat's proof and counterexamples, checked; P-737)

**Verdict: PROVED for main's own claim, the refutation for lcm(S) ≥ 12** (its counterexamples checked in full). The
seat's proof for lcm(S) ≤ 10 is cited, with its checkable lemmas verified and S = {5} corroborated. It is not built on
until main re-runs its exhaustive search (P-741). Data-free. cc
(main), 2026-11-07, S306m. The explore seat settled P-737 both ways (relays/explore_2026-11-07_charge_law/, plan
c262308cc, output 9ca836350, read 91119a381; harvest row 1615). 0 of 19.

## 1. The seat's result

- **PROVED for every S ⊆ {2, 3, 4, 5} with lcm(S) ≤ 10:** S = {2}, {3}, {4}, {5}, {2, 3}, {2, 4} and {2, 5}.
  - Over all defects, of any number of runs, any run lengths and any gaps, the single run lcm(S) + 1 is the unique
    least-excess departure, at depth lcm(S)/2 + √5/2.
  - At S = {5} that is the run of 6, at depth 3.618 = √5·φ.
- **How it is proved:**
  - Lemma A: the excess is 2 log Q(E).
  - Lemma B: Q expands over the runs with Fibonacci factors.
  - Lemma C: F_d/φ^d ≥ φ⁻², which gives a bound B.
  - Lemma D: L^s ≡ ±I mod N exactly when N ∣ s.
  - Lemma E: the least bound over multi-run defects is a shortest path on SL(2, ℤ/L), searched exhaustively. Its margins
    over θ_L = log(1 + L/φ²) run from +0.0017 ({2, 5}) to +0.183 ({5}).
- **REFUTED for every S with lcm(S) ≥ 12, by explicit counterexamples:** gapped defects that satisfy the premise with
  less excess than the single run. All but S = {3, 4}'s lie outside B1853's ranges.
- **The shortest-word clause is false for every lcm(S) ≥ 6.**

## 2. What main checked (`verification/charge_law_check.py`, `charge_law_check_run.txt`; main's own code)

- **Every counterexample, in exact integers and 80 digits.** Each satisfies its premise exactly, and has excess below
  the single run lcm(S) + 1:

| S | excess | single run |
|---|---|---|
| {3, 4} | 2.7886 | 3.7021 |
| {3, 5} | 3.2997 | 4.0846 |
| {4, 5} | 3.9224 | 4.5940 |
| {2, 3, 5} | 3.5298 | 5.3367 |
| {3, 4, 5} and {2, 3, 4, 5} | 3.8672 | 6.6524 |

- **The S = {5} control** (runs 2 at 1 and 5 at 21) sits above the run of 6: 2.7905 against 2.3487.
- **Lemma A** agrees with the k = 20 excess to 7.1 × 10⁻¹⁸ on 3 000 R1 defects. In GENESIS's letters the leading
  eigenvector of LR is (φ, 1); the web seat's modules take the transposed letters, hence its (1, φ).
- **An independent corroboration of S = {5}, not the proof.** Main searched 296 two-run and 3 220 three-run gapped
  defects (positions to 40 and 30, lengths to 12 and 8) under the charge premise at 5. None lies below the run of 6; the
  least is 2.7905.
- **Not re-run on main:** Lemma B, and Lemma E's exhaustive shortest-path search, on which the proved cases rest. The
  LAW_MAP row waits on main's own run of that step (P-741).

## 3. What it corrects

- **B1853's HL3 ladder** (charge at 4, 5 gives (21); charge at 2, 3, 4, 5 gives (61)) was true only within R1 ∪ R2.
  Outside the ranges, gapped defects are cheaper. So the depth law lcm(S)/2 + √5/2 holds exactly where lcm(S) ≤ 10, and
  conserving more levels does not deepen the departure without bound.
- **Still standing:** B1853's HL1 and HL2, and the selections under no premise, under the line premise, and under charge
  at 5. Charge at 5's run of 6 is now proved for all defects.
  *[Dated note, 2026-11-11 (B1862's correction of B1856, the audit's finding E3; carried here by Review 78): "charge" covers two cases. E ≡ +I is invisible to every state. E ≡ −I acts as the parity operator, so it is invisible only on states of definite parity; that is a further condition, a parity superselection rule. Of the 643 rung-invisible defects of R1, 338 are the first and 305 the second. The run of 6 itself has E ≡ +I.]*
- **The reading.** Among the charge premises, S = {5}, the ramified prime and the one level where LR fixes a line, is
  exactly where the deep single run is provably least action.

## Seen first

- **Swept:** `VERDICT topic-sweep /charge law|P-737|lcm\(S\)/: 1 of 1601 arcs on main match (PROVED 1); 2 register rows match (QUEUED 2)`. P-737 is B1853's row. No arc proves or refutes the law beyond the ranges.
- **The literature:** Binet's formula, and Perron's formula for the height of a continued fraction's geodesic, both
  standard and checked here numerically. The bounds and the search are the seat's.

## 4. Disclosed

- **The proved scope rests on the seat's exhaustive search.** Main checked the lemmas that can be checked cheaply and
  corroborated S = {5} by brute force. It did not re-run the search.
- **Main's first Lemma A check used the seat's eigenvector in GENESIS's letters** and disagreed by about 11. Taking the
  convention into account fixed it. The miss was main's, not the seat's.
