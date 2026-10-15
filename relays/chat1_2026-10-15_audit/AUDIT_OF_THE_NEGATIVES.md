# The negatives, audited: the arithmetic holds; the negatives were stated wider than they were computed

chat1, 2026-10-15, 01:36 to about 03:00. The owner asked: "are u sure about your math on all your negatives
especially? what are u doing wrong? we came so far.. wheres the problem?"

**How it was checked.**
- **Four independent read-only audits,** one per folder of the day's negatives. Each auditor re-derived every
  negative with its own code:
  - A, the condensate: an explicit E8 with a Frenkel–Kac cocycle;
  - B, the first row: its own theta series;
  - C, the scale, T-ROOT and T-SIGN: SnapPy 3.3.2 and its own T-ROOT recomputation;
  - D, the selection chain: reruns of the sealed constructions in scratch, and words to length 12.
- **The auditors' scripts are filed** under `auditors/` as they wrote them. chat1 scanned them for side effects only.
- **chat1's own labelled post hoc** on step 3a's completion: `../chat1_2026-10-14_step3/post_hoc_completions.*`. A
  fifth read-only referee checked it and its reading. Its scripts are in `auditors/post_hoc_referee/`.
- **Not covered:** the day's readings in `../chat1_2026-10-14_the_field/` and `../chat1_2026-10-14_mysteries/`.
- Nothing sealed is re-graded. **0 of 19.**

## 0. The answer

1. **The arithmetic holds.** No auditor found a computational or code error in any negative, and every figure they
   checked reproduced.
2. **The negatives were over-read.** Most were stated about "the frame", "the root", "the weave" or "the record". They
   were computed in one cell, one completion, one word weight or one placement, or under an undefined "select". Eight
   are wrong as worded, and three are features presented as failures.
3. **The error is systematic, and it is chat1's.**
   - Positives went through seals, base rates and referees, and came back scoped. Negatives went out as conclusions.
   - When step 3a produced counter-evidence (the root at 1 : 0.0215 : 0 in the (−½, 7/2) cell), chat1 filed it as a
     scope note that "changes no grade". It did not revise the headline the evidence undercut.
4. **What changes:**
   - the selection question is open again, at the level of cells;
   - step 3a's negative stands under every completion computed, but the completion decides the 7/2 cells' rank;
   - the CP "failure" is withdrawn as a failure;
   - the first row's "Reading B is closed" is reopened;
   - four cells and one ledger row on main need rewording.

## 1. Wrong as worded

| # | claim (where) | what is true |
|---|---|---|
| 1 | "At c = 6 the action selects nothing" / "lands on no vacuum" (the selection report §0, §6b; the relay §1; the meditation §6). B1652 banked it as "weighed, not selected, at c = 6" | The root is the heaviest single thread at every c under all three word weights. At c = 6 it holds 27%, 50% or 66%, and the unfixed word weight sets most of that: at c → 0 it already holds 40% (B) and 53% (C). Fair: "at c = 6 the classical action does not concentrate the weave; the root is its most probable thread" (C, D) |
| 2 | "The root has no hierarchy" (B1652's F5, built on chat1's "the least hierarchical thread", "not hierarchical enough") | W72's cell gives 1 : 0.37 : 0.0096, a mild hierarchy, not none. (3/2, 7/2) gives 1 : 0.81 : 0.62 or 1 : 0.485 : 0, and (−½, 7/2) gives 1 : 0.0215 : 0 or 1 : 0.0184 : 0 (H-ORTH or H-E4). "So the thread is the whole question for the hierarchy" is wrong too, since the same thread gives 0.37, 0.81 or 0.018 by cell (D, and §3) |
| 3 | "A completion other than H-ORTH, which would be a fit" (step 3a's fence) | E4·F and ϑ²F are both parameter-free and the same on every thread (§3) |
| 4 | "chat1's floated escape is closed" (the first row §2 and its relay). Main's RELAY_LEDGER: "Reading B's escape closed" | It is closed only for one condensate per leg. With both condensates on one leg the coupling has rank 3 in general. With 8 free real parameters it reproduces the whole first row and Δm²₂₁/Δm²₃₁ at τ = i, 1.5i and ω: a fit, not a prediction. On a cubic surface of Higgs directions it keeps a massless ν₁ off R, with \|U_e1\|² across [0, 1]. chat1 set it aside for having no Jacobi-forced massless neutrino, which nature does not require (B) |
| 5 | "RL as the charged leptons' residual and B1649's leading order cannot both hold" (the first row §4) | R(ω) is an isotropic eigenline of RL: eigenvalue ω, overlap 1 to 10⁻¹⁵. What is incompatible is TM1's ⅔ row assignment (B) |
| 6 | "The cusp condensate picks no direction in M: it has no M-part at all" (the condensate's title; its relay: "it picks none") | Its own cell A1c gives the backreaction an M-part on the real quaternion-Cartan axis: ±1/6 on 108 roots, ±1/2 on 4. Fair: "it picks no isotropic line in M" (A) |
| 7 | "Two orders of magnitude above L154's 6" (T-ROOT) | 105–138 against 6 is 18–23 times, about 1.3 orders (C) |
| 8 | A misquote: "0.61 → 1 (units i and j)" (the condensate's relay) | The unit j tends to ½ (0.610, 0.505, 0.500); only i tends to 1 (A) |

## 2. Features presented as failures

1. **"The weave cannot choose a sign of CP"** (the selection report §0, §4 and §6b item 4; the relay's title and D7;
   B1652's F5 D7; P-149's FK12 amendment).
   - The mathematics stands. A word and its reverse are one oriented manifold and carry conjugate couplings.
   - But they are CP images of each other. Between two CP-conjugate vacua, the sign of the CP phase is a labelling
     convention: observers in either vacuum see every CP-odd rate with the same sign, relative to the matter they are
     made of. This is spontaneous CP violation, and there is nothing to select.
   - **The real CP obstacles stand:**
     - one sector has no physical phase;
     - one coupling for every sector gives CKM = 1 and J = 0;
     - at c = 6, the reflection-symmetric threads, whose couplings are real, carry 91.5–98.9% of the weight (D).
2. **T-SIGN's "the positivity ruling chooses bit 0", read as "no CP"** (B1652's F2 D7 cites it).
   - The bit separates θ = 0 from θ = π, and both conserve CP. Amphichirality alone makes those threads CP-even. So
     F2's D7 failure rests on W74 alone.
   - **A missed credit:** B1479 ("the bit is the sign of the word state") and B1482 (GM5d) banked T-SIGN's headline to
     length 12 on 2026-10-07. T-SIGN extends it to length 18 (C).
3. **The massless first generation** (S1; the first row's F5; B1649).
   - It is a zero forced by Jacobi's identity: the record's own leading order, and the leptonic twin of B1649's
     V_us = 0.
   - Step 3a's S2 "failure" says the same thing from the other side. At rank 3, no cell computed gives m₁/m₂ ≪ 0.05.
     A rank-2 cell has m₁ = 0, and whether a lift then makes m₁/m₂ small is P-128's open question.

## 3. Step 3a's completion, checked (chat1's labelled post hoc)

- **The structure.** Every one-unit 7/2 section is E4·F_l + c f, where F_l is the unique −½ section.
  - F₊ is R, so E4·R is isotropic and its column of the coupling vanishes.
  - In this basis the + column under any completion is c₊ times f's column.
  - The referee confirmed the tower to 10⁻¹⁶:
    - ϑ of the −½ sections gives the 3/2 sections;
    - step 3a's particular sections are E4·F + α f, with α = (−221, −4, −112);
    - ϑ²F is E4·F + β f, with β = (−224, −4, −112).
- **The completions.**
  - **H-ORTH**, chat1's sealed choice, subtracts each thread's f-component.
  - **The ring completion H-E4** has c = 0.
  - **ϑ²** has c₊ = −4.
  - H-E4 and ϑ² have no free number and are the same on every thread.
- **Control:** H-ORTH recomputed from the E4 basis reproduces the sealed masses to 1.2·10⁻⁸ on every admitted thread.

| cell | completion | rank | the root | the root's place among the 59 admitted |
|---|---|---|---|---|
| (3/2, 7/2) | H-ORTH (sealed) | 3, light pair nearly degenerate (m₁/m₂ ≥ 0.769 in the band) | 1 : 0.809 : 0.618 | least hierarchical |
| (3/2, 7/2) | H-E4 | 2 on all 59 | 1 : 0.485 : 0 | least hierarchical |
| (−½, 7/2) | H-ORTH (sealed) | 2 | 1 : 0.0215 : 0 | 36th |
| (−½, 7/2) | H-E4 | 2 on all 59 | 1 : 0.0184 : 0 | smallest (0.18–0.63 on the other threads below y = 1.75) |

- **No completion computed splits the pair at rank 3.**
  - Every admixture computed with c₊ ≠ 0 gives the nearly degenerate pair: H-ORTH, and two voided runs read as arbitrary
    fixed admixtures.
  - The rank 2 under H-E4 is the knife-edge c₊ = 0. It meets S2's inequality only trivially.
  - ϑ² (c₊ = −4) is rank 3 and still to be computed with its right admixture.
- **The (−½, 7/2) root lies far below its low-lying neighbours under both completions.**
  - Among admitted threads, only the deepest come near it.
  - Five unadmitted deeper threads go lower (LLLLLR and LRRRRR: 0.0088 at y = 3.35).
- **One coincidence, recorded without weight.** The down quarks' m_s/m_b at M_Z is 0.0187 ± 0.0016. The (−½, 7/2)
  root under H-E4 sits 0.2σ from it.
  - Five root values across cells and completions give about 12–16% chance of landing within 1σ of some sector. That
    takes log-uniform priors, or the instrument's own values. The chance is 28–35% if every ratio of the rank-3 roots
    counts.
  - That cell's first generation is massless, while m_d/m_s = 0.050 is not small.
  - Nothing is assigned.
- **Void, by a defect in the script's fits:** its identity entries and the runs labelled "H-PART" and "H-THETA2". The
  fits were dominated by poorly determined high q-coefficients. The referee's one-coefficient read-out above repairs
  them.

## 4. Stands only as scoped

- **The first row, "1 or at most ½, and nature's 0.675 in the gap."**
  - It holds for one fibre, one τ, one point, one R, one condensate per leg, and the Hodge–Riemann metric.
  - Each of these reaches the gap:
    - couplings at different fixed points: B1651's U6, squared, gives 0.653, 0.620 and 0.591;
    - two moduli: R(i) against R(ω) gives 0.825;
    - the one-leg placement;
    - T-NORM (B).
- **"The weave does not fix the hierarchy" (the scale).**
  - It holds with k and σ as independent couplings in the classical action.
  - Frameworks where the levels lock (chiral gravity, c = 24k) are untested (C).
- **"The level matters at order one" (T-ROOT).** This holds only under word weight (A). Under (B) and (C) the footprint
  at k = 1 is 2–3% (C).
- **"The principles split" (the meditation).** Every principle tabled admits the root, except one of the two transfers
  of B517 (D).
  - **[2026-10-15, morning]** The SM seat's W86 removes the exception, and this item falls. Under B517's own condition
    (non-negative entries), its transfer admits every word, the root included.
  - No principle on record excludes the root.
- **"The one-number law fails beyond length 8."**
  - It fails for long words built of golden blocks.
  - At lengths 9–12 the sealed tolerance still holds: RMS 0.437 < 1.0 over 501 words (D).
- **The condensate's cells A1a, A1b and V (Reading B).**
  - A1a and A1b are true by construction: W70's hypercharge rule, and weak-SU(2) invariance.
  - Reading B's argument proves nothing, since the weights of a compact group are always real. It needs W70's
    block-to-unit identification.
  - The two-field edge is real. Two independent condensed fields give an exactly null M-part (W64's lines), which the
    audit lane's F-term sets to zero (A).
- **T-ROOT's seal.** The lower bounds of T2 and T3 could not fail: at c → 0 the root share already exceeds them (C).
- **THE_SCALE §4.3's class-S line is wrong.** The size of the Higgs field in class S is a free Coulomb-branch modulus.
  The line carries no weight in the argument (C).

## 5. Stands: the real obstacles

- **The sector structure.** One thread gives one coupling to every sector, hence CKM = 1 and J = 0.
- **The light pair at rank 3.**
  - W72's cell (C1) keeps m₁/m₂ ≥ 0.0515 in the band to length 8. That falls to 0.040 at lengths 9–12, and to 0.031
    on LLR(LR)¹² (D).
  - The up quarks and the leptons need 0.002 and 0.0047.
- **B1649's zero.** It survives integration whenever R is a matter mode (S1). At a point no flat line lifts it (main's
  firewalled pre-seal finding for P-128).
- **Free inputs.** c and the word weight are free, and so is the completion of the 7/2 cells.
- **CP.** One sector has no physical phase.

## 6. What chat1 was doing wrong

1. **Negatives lost their premises; positives kept theirs.**
   - The referees cut chat1's positives down to their premises: the one-number law, the forbidden band, the locus
     claim.
   - The load-bearing negatives went out about "the dynamics", "the root", "the weave" and "the record". Yet they were
     computed in one cell, at large c, with words to length 8 and one placement.
2. **A demand for a unique answer that nothing requires.** These were each reported as "selects nothing", "cannot" or
   "fails":
   - a peaked distribution;
   - a CP-conjugate pair;
   - a set of allowed loci;
   - a law with two variables.

   For the CP sign, uniqueness is not even physical.
3. **Cells that could not fail, presented as tests:** the condensate's A1a and A1b, and T-ROOT's lower bounds. A
   one-sided seal makes a negative look tested.
4. **A canonical choice that was not the only one.** H-ORTH was called "the minimal-norm completion" and the
   alternatives "a fit". The ring completion was missed.
5. **Counter-evidence booked as a footnote.** C3's root went into a scope note, not into the headline it undercut.
6. **A missed credit** (T-SIGN against B1479 and B1482).
7. **The same error, in the other direction, inside this audit.**
   - Its first draft read the completion check as "S2's failure belongs to H-ORTH, not to the cell" and called the
     root "most hierarchical overall".
   - Its referee caught both before commit: the rank 2 is a knife-edge, and the deeper threads go lower.
   - Scope has to bind positives and negatives alike.

## 7. What follows

- **The selection question is open again, at the level of cells.**
  - "Dynamics → the root" survives, as "the root is the most probable thread".
  - "The root → not hierarchical enough" holds in W72's cell only.
  - "→ not found" stands as a report, since no principle fixes the nineteen, but its stated reason does not.
- **The decisive computations are:**
  - the ϑ² completion (the other parameter-free one, c₊ = −4) with its right admixture;
  - what lifts the zero in a rank-2 cell (P-128, main's);
  - the sector structure (one thread gives one coupling to every sector);
  - the (7/2, 7/2) cell.
- **Corrections are filed** as dated notes in every file named above. The relay to main asks for the rewording of
  B1652's F5 cells D1, D5 and D7 and its verdict, of F2's D7 citation, and of RELAY_LEDGER's "Reading B's escape
  closed".
