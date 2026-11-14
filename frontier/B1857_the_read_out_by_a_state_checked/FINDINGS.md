# B1857 — THE READ-OUT BY A STATE: THE LIGHTEST STATE SITS AT THE DEEPEST CLASS, BUT IN THE FLAT-FIBRE (SOL) MODEL (the explore seat's test, checked; P-726, P-717)

**Verdict: PROVED for the checked claims (data-free); the principle is recorded with its scope.** cc (main), 2026-11-07,
S306m. The explore seat tried a principle new to the record: the read-out is made by a state, the history's lightest
massive state, not by a weight (relays/explore_2026-11-07_read_out_by_a_state/; pre-registered 28c83c7df, output
56fd9f7e5 committed unread, post-run verification written after the read; harvest row 1617). 0 of 19.

## 1. The seat's setting and verdicts

- **The setting.** The flat-fibre bundle dt² + A·g_τ(t), where t is Sol time and the fibre's modulus runs along the
  history's Teichmüller geodesic. Its Laplacian separates over the fibre classes into wells q_c cosh 2(t − t_c), with
  q_c = 4π²/(A H_c), where H_c is the class's height.
- **HS1–HS5 TRUE.** The lightest state sits at the deepest class (the apex), with an exact real part. It is unique if and
  only if the deepest run is unique. It is exact only as A → 0: ⟨Im⟩/H* runs 0.998, 0.980, 0.861 and 0.758 at A = 10⁻⁴,
  10⁻², 1 and 2π. Its premise is a neutral tower probe.
- **HS6 FALSE as pre-registered.** By length, the cheapest line-invisible departure with a unique lightest state is
  (2,1,2,1,2), not (6).
- **POST HOC, range-scoped.** By volume, uniqueness removes exactly the two cheaper, mirror-degenerate departures. That
  leaves (6) under both level-5 readings.
  *[Dated note, 2026-11-11 (B1862's correction of B1856, the audit's finding E3; carried here by Review 78): the charge reading is itself two cases — E ≡ +I, invisible to every state, and E ≡ −I, invisible only under a parity superselection rule. The run of 6 has E ≡ +I, so it stands under either.]*
- **HS7:** the systole's multiplicity follows the class structure.

## 2. What main checked (`verification/state_readout_check.py`, `state_readout_check_run.txt`; main's own code)

- **The cosh law.** Along LR's axis, the flat-torus energy of a class, |m + nτ|²/Im τ, equals f_min cosh(t − t_c) in
  hyperbolic arclength t. That is f_min cosh 2(s − s_c) in Sol time s = t/2. It holds to 4.7 × 10⁻³⁸ on seven classes.
- **The state's place (analytic).** By Hellmann–Feynman, dE₀/dq = ⟨cosh⟩ > 0. So the lightest state sits at the least
  q_c, which is the greatest height: the apex.
- **Uniqueness, as the apex's multiplicity per period:**
  - (6): apex 3.618034, unique;
  - (2,1,2,1,2): apex 1.723607, unique;
  - (2,1,1,1,2): apex 1.625437, attained twice (a mirror pair);
  - (2,1⁸,2): apex 1.617974, attained twice.
- **HS6, by length.**
  - The line-invisible departures, cheapest first: (2,1,1,1,2) at 1.4745 (degenerate), (2,1⁸,2) at 1.4786 (degenerate),
    (2,1,2,1,2) at 2.1597 (unique), (6) at 2.3487.
  - So the unique-state selection by length is (2,1,2,1,2), as the seat found. Within R1 ∪ R2 nothing line-invisible
    lies between (B1853).
- **The post hoc, by volume.** (2,1,1,1,2) at 1.3972 and (2,1⁸,2) at 1.4103 are both degenerate. (6) at 1.5714 is unique.
  So volume plus uniqueness selects (6) under the line reading too. The seat's gap of 0.414 to the next is not re-run.
- **Not re-run:** HS1–HS5's spectra (the heights by two methods, E₀ by finite differences and DVR, the A-dependence) and
  HS7.

## 3. Its scope, against the τ read-out rule

- **The state lives in the flat-fibre model, whose clock is Sol (Teichmüller) time.** That is a moduli-space clock, which
  the record counts as CHOSEN (B1815). So it sits at the Teichmüller apex: 3.618 for (6), the (N2) reading.
- **The τ read-out rule (`docs/THE_TAU_READOUT_RULE.md`) reads τ on the hyperbolic metric's own clock,** whose tube
  value is 6.06i (B1854). The state principle answers P-726's "point or weight" in the Sol model.
- **Owed:**
  - the analogue on the hyperbolic metric: where the lowest state of the hyperbolic structure localises (P-744);
  - what fixes the fibre area A, which sets how sharp the state is (P-743);
  - a pre-registered rerun of the volume-and-uniqueness selection, with a completeness bound (P-742).

## Seen first

- **Swept:** `VERDICT topic-sweep /lightest state|read-out by a state|fibre area|Sol time/: 1 of 1603 arcs on main match (PROVED 1); 1 register rows match (DONE 1)`. P-726 and B1846 hold the point-or-weight question. B1853 and B1855 hold the departures. No arc reads
  out by a state.
- **The literature:** the hyperbolic distance formula along a geodesic (the cosh law), and Hellmann–Feynman, are
  standard and checked or stated here.

## 4. Disclosed

- **Main's first check script used cosh 2t in hyperbolic arclength.** Hyperbolic arclength is twice Sol time, so the
  factor was wrong. Its first multiplicity tolerance was also tighter than its continued fractions' truncation. Both
  were fixed before this record. Neither touches the seat's results.
- **The volume selection is post hoc, as the seat says.**

## Dated note, 2026-11-11 (B1875; the web seat's sealed card, verified on main)

- **Uniqueness of the apex is not kept when histories are composed.** Two histories that each have a unique apex and
  the same departure compose to one whose apex sits in two places: 18 of the 36 composites tested. So the property is
  one history's own, and it cannot be a rule on which histories are allowed.
- **The two "mirror-degenerate" departures above, described exactly.**
  - (2,1,1,1,2) closed by one golden period is LLRLR twice over and is −1 modulo 5. The move that carries one copy
    to the other moves the line. The reversal that exchanges its two runs of 2 keeps it.
  - (2,1⁸,2) has its two runs of 2 as L² and R². They are exchanged by a reversal that swaps the letters and carries
    the line to its twin.
- **The four apexes of § 2 are reproduced** by an integer form of the height, in which a tie is an equality of two
  integers.

**[NOTED 2026-11-13 (the building session, at main's word in M29; the rule of 2026-11-12 before a selection or a hand is claimed, WORKING_RULES and B1905): this arc's verdict line claims a selection, in the words “is selected under both level-5 readings”. On the builder's reading (B1905's classification of the older verdict lines, class "neither") this page names neither the family the selection is made from, as a finite classification with a test of membership, nor a consistency condition; the rule asks that a claimed selection name its family. This reading WAITS ON MAIN'S CHECK of that classification's rows; the verdict, its numbers and the words above are unchanged.]**

**[CHECKED BY MAIN 2026-11-14 (M37; register row P-849): family named on the page — the line-invisible departures, listed in full. So it is not a selection without its family. The note above stays as written.]**
