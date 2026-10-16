# B1662 — THE PULL-BACK ACTS ON THE RECORDS: the owner's ruling on P-179, made by the math (GENESIS v1.48)

**Verdict: PROVED** (a ruling arc: the facts the ruling rests on are verified and locked; GENESIS amended through the
adoption step). cc (main), 2026-10-16. **0 of 19;** the price unchanged, 4 + 9 = 13.

## 0. Seen first

`VERDICT topic-sweep /pull.back|inverse move|GM5b|negating the records|sign of the word|positivity/: 10 of 1433 arcs on main match (NEGATIVE 2, PROVED 8)`
— the precedents are B1482 (the sign is the cancelling move), B1479 (the bit is the sign of the word state), B1083
(positivity as the arrow's home), B1640 (positivity's reach), B1454 and B1422. The rest use "positivity" in other
senses. Read: `speculations/S_THE_PUSH_BACK.md` §§8–9 (firewalled; the owner's passages, main's analysis, the sweep).
**Literature:** Kesten (1959), Furstenberg (1963) for random walks on non-amenable groups; Milnor for SL(2, ℝ)/SL(2, ℤ)
as the trefoil's complement; Series (1985) for the cutting sequences.

## 0b. Disclosed

- **No preregistration.** This is a ruling arc. Its four exact facts are elementary. Its three walks are seeded
  illustrations of the cited theorems, smaller versions of main's explorations of the same day (`pullback_readings.py`,
  4000 walks; `arrow_escape.py`, 2000 walks), whose results they reproduce.
- **The ruling.** The owner, 2026-10-16: "lest elaborate, see the options and recomendations then we decide. its not a
  matter of my preferences but math", and then "i accept your recomendations all". Main's recommendation is
  `S_THE_PUSH_BACK.md` §9.1.
- **The sweep** of the 24 arcs whose findings cite positivity was made before the ruling by a reading agent, and its
  substantive items were checked by main (§9.3).

## 1. The facts (`verification/the_pull_back_acts.py`; `.json`)

| fact | what | result |
|---|---|---|
| **F1** | PF1's form at the root: [LR, RL] has trace −2 and equals −U with U unipotent; unchanged when either letter's sign flips | **HOLDS:** [[−7, 6], [−6, 5]]; the failed cancellation lands on the sign times the cusp |
| **F2** | the balance points: S = L R⁻¹ L fixes i, S² = −I, S⁴ = I; L⁻¹R fixes ω, (L⁻¹R)³ = −I | **HOLDS** |
| **F3** | no forward word reaches them: every determinant-1 matrix with non-negative entries (entries ≤ 40) has trace 2 or ≥ 3 | **HOLDS:** never −I, never trace 0 or ±1 |
| **F4** | the mirror: diag(1, −1) sends L to L⁻¹ and R to R⁻¹, and τ to −τ̄ | **HOLDS** |
| **W1** | reading A (the inverse move acts), equal strength: returns to the identity saturate | **HOLDS:** a mean of 0.477 at T = 500 and at T = 4000 (600 walks, seed 101) |
| **W2** | reading B′ (the pull-back only undoes the last step): returns grow | **HOLDS:** 33.5 → 97.0 (seed 202), like √T |
| **W3** | the escape under A: (1/n) E log‖Xₙ‖ > 0 | **HOLDS:** 0.0992 (n = 1500, 600 walks, seed 303) |

## 2. The ruling and what it does

- **The pull-back acts on the records: GM5b adopted.** The inverse moves are legal, as a reading of PF1's cancelling
  chosen by the math, not a derivation. PF1's own form is two steps and their pull-backs (F1). Only this reading never
  settles at equal strength (W1 against W2). A pull-back that does not act could be seen by no computation.
- **FK4 answered: the sign is generated.** A full turn round a balance point negates the records (F2), and no forward
  word reaches them (F3). So the place where a hand can be registered on a fermion (B1479, B1481) is generated, not
  added.
- **GM5d and FK6 re-read.** Positivity is no longer a rule on states. Step and pull-back are mirror images (F4), so it
  becomes the choice of side, still CHOSEN, a selection.
- **The arrow is the escape.** It is a positive rate with no preference (W3, Furstenberg), not non-invertibility.
  B1083's "never a choice" survives, re-homed.
- **The arena recorded (P-178 N1).** SE1's trace-1 solution, the trefoil's order-6 move L⁻¹R, is reached by the moves
  only under GM5b (F2, F3). GM3 keeps it from being a thread. The root is the motion, the arena the space it moves in. A
  reading recorded, with the classical facts cited.
- **Nothing banked about the threads changes.** Every hyperbolic class keeps a forward representative (Series).

## 3. Re-graded (dated addenda, the computations kept)

- **B1482:** "positivity excludes" holds of the forward semigroup only; S1–S4 stand.
- **B1479:** "not yet generated" superseded; P1–P3 stand.
- **B1083:** the arrow re-homed to escape; the C and P bits stand.
- **Scope sentences:** B1640 (anticipated the ruling), B1454 (the root's uniqueness holds with and without
  positivity), B1422 (the a = b = −1 branch reachable).
- **The other 18** use "positivity" in other senses.

## 4. What it does not show

- Any value: 0 of 19. The price is unchanged, because GM5b is not among the root's four inputs and no identification
  row moves.
- Which side our reality is on. CP violation would read it (S_THE_PUSH_BACK §8.3c, an argument not yet computed).
- The pull-back's strength p: transience and escape hold for every p, and anything that depends on p is open.
- That the push-back picture is right. It stays firewalled (P-177, P-179). Only the move's legality is adopted.

Files: `verification/the_pull_back_acts.py` (with `.json` and `_run.txt`); `adoption/amend.py` with
`received/GENESIS_v1_47_main.md`; `verification/regrade.py`; the lock `tests/test_b1662_the_pull_back_acts.py`.
