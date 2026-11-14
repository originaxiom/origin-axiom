# SM-C12 — the principle note tested: one leg confirmed, one refuted and corrected, one closed

*The SM seat, 2026-11-14, at the owner's request. Card `relays/cards/SM_C12_the-principle-note-tested.md`, sealed and
pushed at e90147a67 before any run. Data-free; nothing compared with a measured number.*

## The results

| test | the note's leg | result |
|---|---|---|
| T1 = W5 | the hand is the act's own orientation-odd invariant, read through the record's odd L-value | **confirmed on fresh data.** η_A(T²_M) = −L_odd(1, χ_c)/π² exactly on all 911 characters of 13 levels never seen |
| T2 | "the remainder appears exactly where the act and its mirror fail to cancel" (the note's in-passing reading) | **refuted, and corrected.** The remainder is the act's letter imbalance: η = (#L − #R)/3 on all 74 states. Two chiral states (±LLLRRLRR) have η = 0 |
| T3 = W3 | a closing that reverses the arrow can carry a remainder | **refuted (W3 happens).** h¹(V*) = h¹(V) on every module of every closed torus bundle of the tick, n = 1 to 6 |
| W4 | the hand and the order as two bits at an odd tick | **withdrawn before any run:** a non-orientable object has no hand of its own (card, § 0) |

## T1: the odd L-value is the twisted η invariant, now on characters it had not seen

- **The run:** 13 fresh levels, none in SM-C7's population (checked against B1737's list), and 911 characters.
- **The identity holds on every character.** η_A = ρ_A(4.67) + η(T²_M), against SM-C7's period of G_c along the
  geodesic, read as a rational with denominator up to 24N². The largest rational residual is 1.5 × 10⁻¹⁵.
- **The second computation agrees on every level checked.** It is SM-C7's cone sum on 12 levels, and the period at 96
  nodes on −LR 5.
- **The plants fire:**
  - P1 (M⁻¹) on 905;
  - P2 (the untwisted η dropped) on 437, which is every character of the levels with η ≠ 0;
  - P3 (Jc in place of c) on 903.
- **A deviation, said.** The card asked for the cone sum on five characters of every level. For −LR 5 (trace −123)
  the cone sum runs over M², whose trace is about 15 000, and would take hours per character.
  - The first launch was stopped after 22 minutes on that level (`relays/sm_c12/RUN_t1_stopped.txt`). Its one finished
    level, +LR 6, is identical in the rerun.
  - The rerun used the 96-node period for that one level.
- **What it means.** SM-C9's post hoc identity is now confirmed under seal. Up to −π², the record's odd L-value at s = 1
  is the η invariant of the closed torus bundle twisted by the character's flat line bundle: a twisted form of Atiyah's
  identity. It is ready for main to recompute and bank.

## T2: what survives is the act's letter imbalance, not its chirality

- **The run:** all 74 signed word states of length 2 to 8 (main's states()), at level 1.
- **What held:**
  - E-T2a: η = 0 exactly where #L = #R, and in fact η = (#L − #R)/3 on every state. That is Rademacher's symbol over 3,
    as the card's § 0 derived before the run.
  - E-T2b: every one of the 16 amphichiral states has η = 0.
  - E-T2c: two chiral states have η = 0. The note's in-passing reading is refuted.
- **E-T2d failed as sealed.** The sum of η_A over the non-trivial characters is not always 0.
  - Post hoc, labelled (`relays/sm_c12/posthoc_t2_sum.py`): it is (sgn(2 − tr) − 1)·η on all 74 states. That is 0
    for negative trace and −2η for positive trace.
  - The card's cover argument missed a sign. The characters' cover is T²_M again, identified through M − I, whose
    determinant 2 − tr is negative for tr > 2. So that cover carries the opposite orientation.
- **The correction to the note.** The orientation-odd remainder survives where the act's two moves fail to cancel each
  other (#L ≠ #R), not where the act fails to cancel its mirror. That is still the principle at work, one level down,
  inside the act.

## T3: no remainder on a closed object, even when the closing reverses the arrow

- **The run:** the closed torus bundles T_{Jⁿ}, n = 1 to 6, with every character, every doublet, and, for odd n, the
  irreducibles induced from the orientation cover (144 at n = 3, 1 320 at n = 5).
- **g₀ = h¹(V*) − h¹(V) = 0 on every module of every n.** W3 happens.
- **The control holds on every module:** closed duality, g_w = h⁰(V* ⊗ w) − h⁰(V).
- **Two slips in the card, said.**
  - Its control was written with the h⁰ terms the other way round. That form fails on the two modules per odd n that
    carry invariants (the trivial character and w), as it must.
  - Its expectation, "g₀ = 0 on every module", leaves out the known escape through invariants. The census is reported
    in full and without the invariant modules; g₀ is 0 either way.
- **What it means.** On the tick's family, an end is the only place a remainder survives. The fusion of order with
  orientation (SM-C10) is a statement about ends, not about closed objects. The note's claim 1 is strengthened, and its
  fusion clause is narrowed.

## The principle note, after the tests

- **Stands:**
  - claim 1, the open end, now without exception on the tick's closed family;
  - the realised sign, with W1 balanced;
  - the hand as the act's own odd invariant (T1, confirmed).
- **Corrected:** the remainder's location. It is the act's letter imbalance (Rademacher), not its chirality.
- **Narrowed:** the fusion at one tick holds at the end only.
- **Withdrawn:** W4.

## Files

- **`relays/sm_c12/t1_w5.py`, `relays/sm_c12/t1_results.json`, `relays/sm_c12/RUN_t1.txt`:** T1, and the stopped
  first launch.
- **`relays/sm_c12/t2_remainder.py`, `relays/sm_c12/t2_results.json`, `relays/sm_c12/RUN_t2.txt`:** T2, and its post
  hoc sum (`relays/sm_c12/t2_posthoc_sum.json`).
- **`relays/sm_c12/t3_closed.py`, `relays/sm_c12/t3_results.json`, `relays/sm_c12/RUN_t3.txt`:** T3.
