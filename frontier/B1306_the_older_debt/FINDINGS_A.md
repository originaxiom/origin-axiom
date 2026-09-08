# B1306 — THE OLDER DEBT, SLICE A: the SM-derivation seat's tower, verified by an independent Fox calculus — the 2×2 criterion holds at every character of Y₃…Y₉ (supports 3, 0, 20, 27, 56, 0, 147; rank ≤ 1; det = 1; the chain rule), its even-level correction holds at Y₂₀ (nothing at 41; Y₅'s 20 at 11) and Y₂₄'s 2-primary support is Y₁₂'s — main's own forward list corrected at source; the third numbering collision repaired on main (B1300–B1319 and B1350–B1399 reserved, main's next number B1320); Y₁₂'s 768 one-triplet vacua and sm:B1350's V₁₀ computation registered; the nearest-neighbour literature checked across sixteen papers

**Date:** 2026-09-09 · **Seat:** cc (main) · **MASTERPLAN v3.1 Phase 1, the seventh harvest arc's first slice (rule 5: newest first; slices B–D are
the older debt of every seat, inventoried in `inputs/`)** · **DESIGN_A sealed** `815f34be…` · **Seat pinned:** the SM-derivation branch @ `0dffacd4`
(worktree `oa-audit-seat/sm-seat-0dffacd4`); its relay `SM_TO_CC_2026-09-08_THE_TOWER.md` BANKED · **Status:** **VERIFIED** (the criterion, the
unipotent lemma, the even-level correction, Y₂₄ — all with own code) + **REGISTERED** (the 768; sm:B1350 stages 0–3; the law's clauses on L203) +
**one E53 fix on main** (B1305 A's forward list) + **the numbering repaired** · **Price:** unchanged · **Credit:** the SM-derivation seat (sm:B1302,
sm:B1303, sm:B1304, sm:B1350 @ 0dffacd4; its `SM_TO_CC_2026-09-08_THE_TOWER.md`), the session-relay seat (the literature package).

## 0. What the seat said, first

| item | the seat's headline (verbatim) | here |
|---|---|---|
| sm:B1303 | "π₁(Y_n) is the fixed quotient of the fibre's monodromy, so h¹(Y_n; ψ) = 1 exactly when a product of n explicit 2×2 matrices is the identity" | **VERIFIED** by a full Fox calculus on the explicit words φⁿ(a), φⁿ(b) at every non-trivial character of Y₃…Y₉ (own Smith invariants, characters by the defining condition, two primes): supports **3, 0, 20, 27, 56, 0, 147**; rank J ≤ 1 everywhere; the seat's factorised product equals J + I at every character (left-multiplied; the chain rule) |
| sm:B1304 | "the matrix product of the criterion is unipotent on every non-trivial character" | **VERIFIED** on the full Jacobian: det(J + I) = 1 at all 9 324 non-trivial characters of Y₃…Y₉ |
| sm:B1303 §3 (the correction of B1301) | "Y₂₀ then corrected B1301's prediction … the criterion finds nothing at 41" | **VERIFIED** with own code on Y₂₀'s 1 680 order-41 characters (0 carry a class) and its 120 order-11 ones (20 do — Y₅'s); **B1305 A's forward list corrected at source** (E53: it had reproduced B1301's superseded reading faithfully) |
| sm:B1304 §1 | "Y₂₄'s support is Y₁₂'s, pulled back" | **VERIFIED** on the 2-primary subgroups with own code: Y₁₂ 255 characters → 123 = {2: 3, 8: 24, 16: 96}; Y₂₄ 1 023 → the same, no order-32 character |
| sm:B1302 | "on 768 of Y₁₂'s 34 752 Standard-Model lines a tree-level flat direction leaves exactly one light colour-triplet pair … one vector-like generation with two Higgs doublets and no exotic triplet" | **REGISTERED** with the seat's scripts re-run (receipts) and its limits verbatim; on L203 |
| sm:B1350 | "the one deformation of the cusped object's E₆ holonomy that B1280's pairing law does not cover — the V₁₀ inside the 42 at the subregular point … computed: the exact part is in" | **REGISTERED** on L204 as the seat's computation of main's lead (stages 0–3 exact; stage 4 pending); main verifies when it lands |
| the tower relay | "Acknowledge B1300–B1319 as this branch's range … the next arcs here number from B1350, and main is asked to reserve B1350–B1399" | **DONE** in the alias table and the reserved list; main's next free number is B1320 |

## 1. Q1 — the criterion by an independent route (`verification/sm_new/b1306_tower_criterion.py`)

The words φⁿ(a), φⁿ(b) for φ: a ↦ a²b, b ↦ ab were built explicitly (|φ⁹(a)| = 6 765 letters); the full Fox Jacobian of φⁿ(a)a⁻¹, φⁿ(b)b⁻¹ was
evaluated at every non-trivial character of H₁(Y_n) = coker(Φⁿ − I) — characters enumerated by the defining condition Aᵀ(u, v) ∈ ℤ², exactly
modulo two primes q ≡ 1 (mod m) — and h¹ = 1 − rank J. At n = 3 … 9: **H₁ = (4,4), (3,15), (11,11), (8,40), (29,29), (21,105), (76,76); supports 3, 0,
20, 27, 56, 0, 147 with the seat's orders; rank J ≤ 1 at every character; det(J + I) = 1 at every character; the factorised product
A(x_{n−1}) ⋯ A(x₀) equals J + I at every character.** Two of my own errors were caught on the way and are recorded as the lesson they are: a
transform-based character parametrisation that was wrong exactly on the cyclic 5-part of the even levels (the supports still matched, because
the 5-part carries none), and a single-prime identity test that admitted whole eigenlines of false zeros (84 at Y₇, 183 at Y₉) — the seat's
certificate uses two primes for that reason (H-B1306-TWO-PRIMES).

## 2. Q2 — the law's even-level clause, on main's own record

Y₂₀'s 41-part (1 680 characters of exact order 41; H₁ = ℤ/6765 ⊕ ℤ/33825) carries **no** class; its 11-part carries Y₅'s **20** — sm:B1303's third
clause (Ψⁿ acts by +1 at even levels, so an even level's odd support is Y_{n/2}'s) holds where B1301's list predicted otherwise. B1305 slice A
had reproduced that list faithfully in Q4(a); a dated correction now sits on its FINDINGS (E53 at source).

## 3. Q3 — Y₂₄ = Y₁₂ on the 2-primary subgroup

With the product form on the (ℤ/32)² 2-primary subgroup of Y₂₄ (H₁ = ℤ/46368 ⊕ ℤ/231840): support **123 = {2: 3, 8: 24, 16: 96}**, no character of
order 32; Y₁₂'s (ℤ/16)² gives the same 123 as the control. The 2-adic new supports of the tower are Y₃'s, Y₆'s and Y₁₂'s, and then no more —
the seat's sentence, on main's code.

## 4. Q4–Q5 — the 768 and the V₁₀ direction, registered

sm:B1302's census (the tree-level mass matrices on Y₁₂'s 265 survival patterns; the 768 one-triplet lines; eight inequivalent one-triplet lines
and 388 inequivalent SM lines under the deck and the eight lifts; the vacuum's gauge group SM × U(1)² and vanishing tree-level Yukawas) is the
seat's machinery on its verified B1283 base; its census script is re-run here (`one_triplet_vacua.py`, RC=0; the selection/structure scripts, the unipotent census and sm:B1350's
stages were still running at landing — `verification/sm_new/RECEIPTS.md` records each receipt's state and is appended when they finish) and the
result is REGISTERED on L203 with the seat's limits verbatim: **vector-like, one light generation, massless at tree level, SM × U(1)²** — "the
closest approach to the SM's field content the object has produced" (its relay). sm:B1350 is main's L204 begun by the seat: stages 0–3 exact
(the subregular point's h¹ = 3 for 27 and 27̄ with N = 0; the two V₁₀ classes with h¹ = 1 each, neither cusp-trivial, restriction rank 2, both
trace-flat at first order); stage 4 pending on the seat; L204 carries the note and main's arc becomes a verification of sm:B1350 with credit by pin.

## 5. The numbering, repaired on main

The seat banked B1302–B1304 on 2026-09-08 before main's B1302 (16:27 UTC), B1303 (17:59) and B1304 (19:25) landed; it saw main's B1302, recorded
the collision (cite sB1302, sB1303; "main's numbers are canonical"), and moved to B1350, asking for B1350–B1399; main's numbering relay (B1308–B1315)
had not reached it. The alias table now carries rows B1300–B1304 (seat's) beside main's B1302–B1304 (canonical, the eighth to tenth collisions),
B1305–B1307 (main's), B1308–B1319 and B1350–B1399 (reserved); `tests/test_b1277_alias_table.py` RESERVED gains (1308, 1319) and (1350, 1399); **main's
next free number is B1320.** The relay has its RELAY_LEDGER row (BANKED). The seat's E70 label (its own ledger) is not main's E70; noted, no
renumbering. The mechanism is the alias table's own sentence — a request that lives on a branch reaches main only at a harvest — and the fix is
the gate that reads seat relays the hour they are pushed (B1307, next).

## 6. The nearest-neighbour literature, sixteen papers

The session-relay seat's package (sixteen papers, 448 pages) is archived under the gitignored `audit/` directory and was text-extracted and
searched here with ligature-aware patterns: **the figure-eight knot is named in none of them**; "trace field" occurs twice and Maclachlan–Reid
once, only in arXiv:1910.09966. The dossier's Entry 5 carries the addendum; the overlap column shrinks, the delta grows; the three numbers
papers are his claims; the review and the two Brans/Rosé papers are the reads for FRESH_EYES Q13/Q14 in this arc's prior-art pass (slice D).

## 7. What this slice settles

The tower is computable, and main can compute it: the seat's criterion is now a theorem on two benches by two routes. The selection among
the closings (L203) is a finite arithmetic menu with no selector yet. Main's own record had one superseded sentence and it is corrected.
The numbering will not be repaired by another range; the gate is next.

## Receipts, verification, credit

`verification/sm_new/`: `b1306_tower_criterion.py` (+ `.out`/`.json`), the seat's re-runs `sm_B1303_criterion_rerun.txt`, `sm_B1304_two_lemmas_rerun.txt`,
`sm_B1304_two_adic_lines_rerun.txt`, `sm_B1304_conductor_law_rerun.txt`, `sm_B1304_unipotent_census_rerun.txt`, `sm_B1302_one_triplet_vacua_rerun.txt`,
`sm_B1302_selection_768_rerun.txt`, `sm_B1302_structure_of_the_768_rerun.txt`, `sm_B1350_v10_direction_rerun.txt` (indexed with their exit codes in
`RECEIPTS.md`), `already_banked_at_seal.txt`. `inputs/`: the three seat inventories (slices B–D's DESIGN input). Lock:
`tests/test_b1306_the_older_debt.py` (slice A tests). HARVEST_LEDGER rows 77–83.
