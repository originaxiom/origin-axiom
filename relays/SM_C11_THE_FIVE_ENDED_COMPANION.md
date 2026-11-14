# SM-C11 (P-333) — the F-CI read on m003's five-ended companion: a three on every end, under A₅; and the only one

*The SM seat, 2026-11-14. Card `relays/cards/SM_C11_the-five-ended-companion-in-F-CI.md`, sealed and pushed at
3436fff8e before the run. Main at 5b327b1e0 (M24). The instrument is main's own F-CI cell, B1492's fci_L8a15.py,
imported unchanged. Data-free: SnapPy's census and integer cusp maps. The audit-room draft that P-333's row cites was
not read.*

## The outcome: T on o10_150729, and the census says it is a selection

**Part 1: o10_150729 (= S³ − L10n113, m003's companion).** Every expectation of the row's claim holds.

| | expectation | prior | result |
|---|---|---|---|
| E1 | the isometries act on the five ends as A₅ | 30% | **holds.** 240 isometries, 120 of them orientation-reversing. The orientation-preserving ones act on the ends as a group of order 60 with every permutation even, that is A₅. With the reversing ones, the group on the ends is S₅ |
| E2 | every end is fixed by an orientation-preserving isometry with cusp value 3 | 25% | **holds,** on ends 0 to 4. The cusp-fixing values are 3 (40 times), 1 (40), 4 (20) and 0 (20) |
| E3 | the cusps are hexagonal | 40% | **holds,** on all five (shape ½ + (√3/2) i) |
| E5 | the controls: m003's companion is o10_150729; +LLLR's is L8a15, with 12 isometries, S₃ on the ends, no three | 95% | **holds** |

- **The second computation.** The cusp values were recomputed from SnapPy's symmetry_group().isometries(), a second path
  to the same cusp maps. It gives order 240 and the same values, three included.
- **The plants fire.**
  - P1: the value |det X| in place of |det(X − I)| is 1 on all 240 cusp maps, so the three disappears.
  - P2: the trivial cover fails the degree check, since |2 − tr| = 3 for +LLLR.
- **So, in F-CI, m003's companion carries a three on all five ends.** Its symmetry is A₅, the icosahedral rotation
  group, acting on the ends; it is S₅ with the mirror. Both of B1490's conditions hold: an order-3 isometry fixes a
  cusp, and the cusps are hexagonal. B1492 found both failing on L8a15.

**Part 2: the companions' census, to word length 10.**
- Every signed word state of length 2 to 10 (main's states(), B1454) was read: 232 states and 231 companions, one
  state (+LR) being its own companion. No companion was skipped and none raised an error.
- The companions have up to 104 ends. Every companion's degree and end count equal |2 − tr φ|, and every isometry
  group is transitive on the ends.
- **E4 fails** (prior 35%). **No companion other than m003's carries a three.**
  - The cusp-fixing values over the census are 0 and 4 everywhere.
  - Besides, 2 occurs once (on −LLRR's companion), and 1 and 3 only on m003's.
  - m003's companion is the one object to word length 10 with F-CI's three.

## What it means

- **The row's claim is right.** F-CI's three sits on all five ends of m003's companion, under A₅.
- **The row's other sentence is borne out too:** GENESIS's F-CI sentence records a selection, not a derivation. Among
  the 231 fixed-point companions to word length 10, the three occurs on exactly one: the companion of the state −LR,
  the trace −3 that gives five fixed points. Nothing in the census derives that state; the three is found on it,
  not produced by a rule.
- **One reading, offered and not ruled.** The five ends of m003's companion are the five fixed points of the act −LR
  on the torus, permuted by its symmetries as A₅. That is the icosahedral group, which W31 and B1923 meet through
  SL(2, 𝔽₅). Whether the two A₅'s are one is a question for main. It is not tested here.

## Files

- `relays/sm_c11/run_c11.py` and `relays/sm_c11/companion.py`: the run and the companion's construction.
- `relays/sm_c11/c11_results.json` and `relays/sm_c11/RUN.txt`: the output, 108 seconds for the census.
