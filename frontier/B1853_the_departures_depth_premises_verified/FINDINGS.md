# B1853 — THE DEPARTURE'S DEPTH: THE ACTION SELECTS WITHIN A PREMISE, THE PREMISE IS A CHARGE (the explore seat's two relays, verified; P-735, P-736)

**Verdict: PROVED (data-free; a verification of seat relays).** cc (main), 2026-11-07, S306l. The explore seat is a peer
session working at the owner's word. Its question, as it reports it: "Is the departure's length forced, with no data and
no choice?" It sent two pre-registered tests, harvest rows 1612–1613. Main re-derived every claim with its own code.
The seat's modules were read for their definitions only. 0 of 19.

## 1. What main re-derived (`verification/explore_facts.py`, `explore_facts_run.txt`)

**The definitions, as the relays state them.**
- A defect replaces m golden runs by runs S, first and last ≥ 2. Its matrix is E = D_S D_g⁻¹.
- **The premises:**
  - "rung-invisible", or charge at N: E ≡ ±I mod N;
  - "line-invisible", or symmetry at 5: E commutes with LR mod 5.
- **The actions:**
  - excess length: the k → ∞ difference of 2 arccosh(tr/2), evaluated at k = 20;
  - excess volume: vol(b++word) − (k + syllables)·vol(m004), evaluated at k = 10.
- **The ranges:**
  - R1: m ≤ 6 with runs ≤ 6; m = 7, 8 with runs ≤ 3.
  - R2 adds m ≤ 3 with runs ≤ 64, m = 4 with runs ≤ 24, and m = 5 with runs ≤ 10.

**The least-volume departure (row 1612):**
- R1 has 42 768 defects, 643 of them rung-invisible.
- **HV1:** the least excess volume is (6), uniquely, at 1.5714462325. Next come (5,1,1,1,1,2) and its mirror at
  2.1955011599, a gap of 0.6241.
- **HV2:** among the 3 494 line-invisible defects the least is (2,1,1,1,2), the same one least length selects.
- **HV3:** (ΔV(11) − ΔV(6))/ΔV(6) = 0.117.
- **The tie:** ΔV(2,2,2) = 2.3592.

**The level premise as a conservation law (row 1613):**
- **HL1:** the centraliser of LR in SL(2, 𝔽₅) is ⟨LR⟩, of order 10 and containing −I. So the line premise is exactly
  the symmetry reading.
- **HL2:** at N = 2, 3, 4 and 5, only ±I conserve the (±) conjugacy class of every golden background. So the rung
  premise at N is exactly the charge (superselection) reading.
  *[Dated note, 2026-11-11 (B1862's correction of B1856, the audit's finding E3; carried here by Review 78): "charge" covers two cases. E ≡ +I is invisible to every state. E ≡ −I acts as the parity operator, so it is invisible only on states of definite parity; that is a further condition, a parity superselection rule. Of the 643 rung-invisible defects of R1, 338 are the first and 305 the second.]*
- **HL3, the least-length departure under each premise, over R1 ∪ R2:**
  - none: (2), 0.7393;
  - symmetry at 5: (2,1,1,1,2);
  - charge at 5: (6), next by 0.4450;
  - charge at 4 and 5: (21);
  - charge at 2, 3, 4 and 5: (61).
  Each is unique within the range, the next between 0.45 and 0.69 higher.
  **[Corrected by B1855, and marked here at Review 77: the last two rows are minima within R1 ∪ R2 only. Outside
  the range, gapped defects satisfy the same premises with less excess, so (21) and (61) are not the selected
  departures. See the dated note at the end.]**
- **The apex law, exact:** the single run (n) in the golden background has apex (n − 1)/2 + √5/2. It is the maximum over
  shifts of (x₊ − x₋)/2 for the cyclic quotients (n, 1, 1, …).
- **LR's fixed points on P¹(ℤ/N):** none at N = 2, 3 or 4. At N = 5 there is one, (1 : 2), from the double root of
  x² − 3x + 1 at the ramified prime.

## 2. What it means

- **The action selects within a premise; it does not remove the premise.**
  - Under the rung premise the least excess volume and the least excess length both select (6).
  - Without a premise, length selects (2).
  - The depth of the departure therefore rests on the premise, and on minimisation as the use of the action. A
    volume-weighted sum diverges, since ΔV is bounded (P-476's Whitehead limit).
- **The premise is now named exactly.** The rung premise at level N is a superselection charge, the level-N class
  conserved for every golden background. The line premise is the symmetry at 5.
- **The charge law.** Under charge at S the selected departure is the single run lcm(S) + 1, with depth
  lcm(S)/2 + √5/2. This is a candidate scoped to R1 ∪ R2, to be proved in general (P-737).
  **[Settled by B1855, and marked here at Review 77: the law holds where lcm(S) ≤ 10 and is refuted where
  lcm(S) ≥ 12.]**
- **The speculation** that a charge lives only where the dynamics has a canonical invariant, S = {5}, is a LEAD (P-738).
- **What it does not do:** no frame value, no datum and no held-out quantity was touched, and the six were not a
  criterion.

## Seen first

- **Swept:** `VERDICT topic-sweep /least.volume|rung.invisible|superselection|charge premise/: 3 of 1599 arcs on main match (PROVED 3); 5 register rows match (DONE 2, QUEUED 3)`. The departures, the rung and line premises, and the least-action test are the web seat's
  (P-717, P-718; RELAY_LEDGER, THE_LEAST_ACTION_TEST, banked 2026-11-06). B1845 holds the excursion's apexes, consistent
  with the apex law (3.118… at n = 5). P-476 holds the Whitehead limit.
- **The literature:** the continued-fraction height of a modular geodesic and the centralisers in SL(2, 𝔽_p) are
  standard; both are checked here, not cited.

## 3. Disclosed

- **The seat's relays report the owner's question.** Nothing here is irreversible.
- **The seat's first conservation run crashed before any result** (an integer inverse used on mod-5 matrices). It kept
  the logs and committed the fix before its rerun. Main's re-derivation shares no code with it.
- **The explore lane was unregistered until this landing.** It is now watched by `harvest_debt.py`, pinned at
  `3c510bbe`, and listed in `docs/SEAT_REGISTER.md`.

## Dated note (2026-11-07, S306m; B1855, P-737 settled)

- **HL3's rows for charge at 4, 5 ((21)) and charge at 2, 3, 4, 5 ((61)) were minima within R1 ∪ R2 only.** Outside
  those ranges, gapped defects satisfy the same premises with less excess: {4, 5} 3.9224 against 4.5940; {2, 3, 4, 5}
  3.8672 against 6.6524 (B1855, checked exactly on main).
- **So the charge law's depth lcm(S)/2 + √5/2 holds only where lcm(S) ≤ 10.** That part is the seat's proof, cited in
  B1855 and not re-run on main (P-741). Conserving more levels does not deepen the departure without bound.
- **Unchanged:** HL1, HL2, and the selections under no premise, the line premise, and charge at 5. The run of 6 under
  charge at 5 is the seat's proved case, corroborated on main.
