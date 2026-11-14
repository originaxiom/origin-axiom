# SM-C11 — P-333: the sealed F-CI read on m003's five-ended companion o10_150729, and the companions' census

*Card of the SM seat, 2026-11-14. Main's M24 orders P-333 after SM-C10 and SM-C8, and its register row names the next
action ("the sealed F-CI read on o10_150729"). Committed and pushed, with its expectations, before anything of it is
computed. Data-free: SnapPy's census and integer cusp maps. This seat has not read the audit-room draft the row cites,
and does not.*

## 1. The question

P-333's row records a claim about o10_150729 (= S³ − L10n113, m003's fixed-point companion, five ends; B1491):
- F-CI's three on all five ends;
- A₅ acting on the ends;
- it is the only one of 16 thread companions computed.

It asks for a sealed F-CI read, and for the companions' census to word length 10. B1492 read o10_150729 in the
harmonic frame only. Its F-CI cell (D5) was run on L8a15 and not on o10_150729.

## 2. What will be computed

**Part 1: the F-CI cell on o10_150729.**
- The instrument is main's own, B1492's fci_L8a15.py (B1418's definition, B1490's loop), imported unchanged from a
  checkout of main and called with the name o10_150729. For every isometry it records:
  - the orientation, and the permutation of the ends with its order;
  - for each orientation-preserving isometry, the cusps it fixes and the value |det(X − I)| of its cusp map X there;
  - F-CI's three is the value 3.
- **Read from its output:**
  - the group's order and its action on the five ends (the permutation group generated: its order, whether it is
    A₅, S₅, D₅ or ℤ/5);
  - for each end, whether some cusp-fixing isometry there has value 3;
  - the cusp shapes, and whether they are hexagonal.

**Part 2: the companions' census, to word length 10.**
- The states are main's: every signed word state of length 2 to 10 (genesis_own.states, B1454; both signs).
- **A state's companion** is the regular abelian cover whose group is the torsion of H₁, the cusp-trivial characters
  (B1491). It is built with SnapPy's cover() from the projection of each generator onto that torsion. The checks:
  - its degree is |2 − tr φ|, and so is its number of ends;
  - for m003 it is isometric to o10_150729, and for +LLLR to L8a15.
- **The F-CI cell is run on each companion**, with a cap of 300 seconds per companion. A companion that exceeds the
  cap is listed, not dropped silently.
- **Reported:** per companion, the ends, the isometry group's order, whether the group is transitive on the ends, the
  cusp-fixing values, and whether a three occurs; the count of companions with a three; the census by trace.

## 3. Expectations, written before any run

| | expectation | prior |
|---|---|---|
| E1 | the row's claim: the isometry group of o10_150729 acts on its five ends as A₅ | 30% |
| E2 | the row's claim: every one of the five ends is fixed by an orientation-preserving isometry with value 3 | 25% |
| E3 | the cusps of o10_150729 are hexagonal (B1490's second condition) | 40% |
| E4 | some companion to word length 10 other than o10_150729 carries a three | 35% |
| E5 | the controls: m003's companion is o10_150729; +LLLR's is L8a15, with 12 isometries, acting as S₃ on the ends, and no three (B1492 D5) | 95% |

## 4. The outcomes

- **T:** E1 and E2 hold. F-CI's three sits on all five ends of m003's companion, as the row says.
- **P:** a three occurs on o10_150729 but not on every end, or not with A₅.
- **N:** no three on o10_150729. The row's claim fails in F-CI. A negative is reported with its second computation:
  the values recomputed from SnapPy's symmetry group by a second path (cusp maps from symmetry_group().isometries()),
  as main's gate on negatives asks (S306p).
- **The census** is reported whatever Part 1 gives.

## 5. Controls that must fail if the work is broken

- **P1:** the value computed as |det X| in place of |det(X − I)| (always 1). The three must vanish everywhere.
- **P2:** the companion built from a wrong character group (the trivial cover). Its degree must fail the
  |2 − tr φ| check.

## 6. Files

relays/sm_c11/, with its script, output and run. The page is relays/SM_C11_THE_FIVE_ENDED_COMPANION.md.
