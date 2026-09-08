# B1306 — THE OLDER DEBT, SLICE A: the SM-derivation seat's tower (sm:B1302, sm:B1303, sm:B1304, sm:B1350) and the third numbering collision: DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1306 (rule 5: newest first; the older debt's inventories run in
parallel and land as slices B–D) · **Seat pinned:** `standard-model-derivation` branch @ `0dffacd4` (worktree `oa-audit-seat/sm-seat-0dffacd4`),
its relay `SM_TO_CC_2026-09-08_THE_TOWER.md` read in full · **Read in full before this seal:** sm:B1303 FINDINGS §1–§6 (the 2×2 criterion, the
tower through Y₂₁, the law's three clauses, the SM lines of Y₁₅/Y₁₈/Y₂₁), sm:B1304 §1–§2 (Y₂₄ = Y₁₂ pulled back; the unipotent structure),
sm:B1302 §1–§2 and the heads of its four addenda (the 768 one-triplet vacua), sm:B1350 §1–§3 (the V₁₀ direction: stages 0–3 exact, stage 4
pending), `docs/THE_TOWER_2026-09-08.md` §1–§3, the seat's alias-table collision rows and its "harvest from main" commit (13d965a9).
**The seat's scripts are re-run in the pinned worktree before the seal (receipts in `verification/sm_new/`).** Nothing below was computed with
main's own code before the seal.

## 0. The rules' lines and the view from above

- The seat's numbers B1302, B1303, B1304 were banked on its branch (2026-09-08, 16:00–17:00 UTC) BEFORE main's B1302 (16:27 UTC), B1303
  (17:59) and B1304 (19:25); the seat saw main's B1302 land, recorded the collision (cite sB1302, sB1303; "main's numbers are canonical"),
  and moved its next arcs to B1350, asking main to reserve B1350–B1399. Main's numbering relay of the same day (B1308–B1315 granted) had
  not reached the seat. **The third collision in a month, and the mechanism is the one the alias table names: a request that lives on a
  branch reaches main only at a harvest.** Repair on main: the alias table gains rows B1300–B1304 (seat's) / B1302–B1304 (main's,
  canonical) / B1305–B1307 (main's) / B1308–B1319 and B1350–B1399 (reserved for the seat); `tests/test_b1277_alias_table.py` RESERVED gains
  (1308, 1319) and (1350, 1399); main's next free number becomes **B1320**; the seat's relay gets its RELAY_LEDGER row (BANKED at this landing);
  main's held reply acknowledges B1300–B1319 and B1350–B1399. **The harvest-debt gate (B1307) would have caught the seat's request the hour it
  was pushed; it is the next arc.**
- `already_banked.py "2x2 criterion" "fixed quotient" "monodromy" "half-deck" "one-triplet" "unipotent" "Fibonacci manifold"`: run at the seal
  (receipt); main's own tower work is B1273–B1274 (seat harvests) and B1305's Q4(a) (the law's arithmetic to 24, which sm:B1303 now
  CORRECTS at even levels: no new odd support at 20 and 22 — B1305 A reproduced B1301's list, which B1303 withdraws; an E53-shaped item
  on main's side, fixed here).
- **The view from above.** The SM seat has made the tower COMPUTABLE: one 2×2 matrix product per character decides h¹, in place of a
  40-digit SVD per deck orbit; with it the supports to Y₂₁ are known, the law has three exact clauses, the 2-adic new supports stop at
  Y₁₂ (Y₂₄ is Y₁₂ pulled back), and the SM closings of the tower are Y₉ (706 464 lines), Y₁₂ (34 752, the one-triplet ones), Y₁₅
  (5.016 · 10⁹ lines), Y₁₈ (= Y₉'s), Y₂₁ (48 945 letters). For L203 (selection among the closings) this is the object-native menu, made
  finite and arithmetic: which closings carry the SM is decided by which primes carry roots of Δ of exact order n with the half-deck's
  global sign. **The 768 one-triplet vacua of Y₁₂ are "the closest approach to the SM's field content the object has produced"** (the seat's
  words) and their limits are the seat's too: vector-like, one light generation, massless at tree level, SM × U(1)². And sm:B1350 is
  main's L204 being computed by the seat first, again. Nothing here moves the chirality bit; everything here sharpens L203 and prices
  L204's computation.

## 1. Pre-registered questions

**Q1 — the 2×2 criterion, re-derived with main's own code** (`b1306_tower_criterion.py`). Independent route: the words φⁿ(a), φⁿ(b) for
φ: a ↦ a²b, b ↦ ab are built explicitly; the FULL Fox Jacobian of the two relators φⁿ(a)a⁻¹, φⁿ(b)b⁻¹ is evaluated at every non-trivial
character of H₁(Y_n) = coker(Φⁿ − I) exactly modulo a prime q ≡ 1 (mod m), m the exponent (own Smith parametrisation); h¹(Y_n; ψ) = 1 − rank J(ψ).
Predictions for n = 3 … 9: (a) the support counts are B1301's/B1303's **3, 0, 20, 27, 56, 0, 147**; (b) rank J(ψ) ≤ 1 for every non-trivial
character (no h¹ ≥ 2); (c) J + I has determinant 1 for every non-trivial character (sm:B1304's unipotent lemma, checked on the full
Jacobian, not on the factorised product); (d) the seat's factorised product A(x_{n−1}) ⋯ A(x₀) — coded separately from the criterion's
statement — equals J + I at every character (the chain rule), so the two routes agree everywhere, not only on the support. PASS = (a)–(d);
FAIL = any count or any identity differs (then the finding is a presentation or chain-rule discrepancy, to be located).

**Q2 — the law's correction at even levels, on main's own record:** B1305 A's `b1305_tower.py` (Q4(a)) reproduced B1301's forward list
including "new odd support at 20 (41)", which sm:B1303 withdraws (Y₂₀: nothing at 41; clause (iii): ε = +1 at even levels). Prediction: with
the criterion of Q1 run on Y₂₀'s 1 680 order-41 characters (own code, exact mod q), **h¹ = 0 on every one** and the 20 order-11 characters
(Y₅'s) have h¹ = 1 — B1305 A's forward-list sentence gets a dated correction (E53 at source: the list was the seat's superseded reading,
reproduced faithfully). PASS/FAIL as stated. (Y₂₀ has 2.3·10⁸ characters; only the 1 680 + 20 are run.)

**Q3 — sm:B1304's Y₂₄ = Y₁₂ (the 2-primary subgroup):** the seat's `two_adic_lines.py` re-run (receipt) and, with Q1's code on the (ℤ/32)²
2-primary subgroup of Y₂₄ (1 024 characters), predicted support **123 = 3 + 24 + 96 with no order-32 character**. PASS/FAIL.

**Q4 — sm:B1302's 768 one-triplet vacua:** the seat's `one_triplet_vacua.py`, `selection_768.py`, `structure_of_the_768.py` re-run (receipts;
the census machinery is the seat's, built on its B1283 which B1303-main verified); REGISTERED with the seat's limits verbatim (vector-like; one
light generation; massless at tree level; SM × U(1)²); L203 gains the row. Not re-derived here (the mass-matrix census is a day's work; the
lines' count 34 752 and the one-triplet thinning on 31 488 were re-derived in B1305 A).

**Q5 — sm:B1350 (main's L204, done by the seat first):** stages 0–3 (the subregular point's h¹ = 3 for 27 and 27̄ at ρ₀, N = 0; the two V₁₀
classes with h¹ = 1 each; neither cusp-trivial, restriction rank 2; first-order trace-flat) VERIFIED by re-running the seat's
`v10_direction.py` stages 0–3 (receipt) and REGISTERED on L204 with the pin; stage 4 (the 400-bit Newton deformations and N(27)) is pending on
the seat — L204's main arc becomes a verification of sm:B1350 when it lands, not a re-computation from scratch (credit by pin).

**Q6 — registrations:** L203 (the tower's SM closings through Y₂₁; the 768; the law's clauses as the object-native selector); L204 (sm:B1350);
L210's items as the seat's; the E53 fix on B1305 A's forward list; HARVEST_LEDGER rows for sm:B1302–B1304, sm:B1350, the tower relay, the seat's
"harvest from main" addenda (it verified main's B1298/B1299/B1302 against its own — recorded as the seat's confirmation of main's harvest); the
alias table and RESERVED repair; the held reply.

## 2. Priors

Q1 (a)–(d): 85 % (the presentation identity is the seat's theorem, checked by hom counts; a chain-rule order slip is the one risk, and (d) is
its detector). Q2: 90 %. Q3: 90 %. Expected verdict: **VERIFIED (the criterion by an independent Fox route; the even-level correction; Y₂₄)
+ REGISTERED (the 768; sm:B1350; the law) + the numbering repaired + one E53 fix on main.**

## 3. Method, controls, discipline

Own code for Q1–Q3 (exact modular arithmetic; own Smith parametrisation; the chain-rule product coded separately as the control); seat
scripts re-run in the pinned worktree with receipts; PASS and FAIL branches; pytest's own rc; credit by arc and pin; no grade lowered
without computation; loose relay files never at root; the seat's E70 label is its own ledger's (main's E70 is the quantifier class) —
noted, no renumbering. Out of scope: re-deriving the 768's mass census; sm:B1350's stage 4; Y₂₁'s lines.
