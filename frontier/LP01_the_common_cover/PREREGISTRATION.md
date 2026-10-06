# LP01 — PREREGISTRATION: THE COMMON COVER

**Sealed before `common_cover.py all` runs on anything but the two controls (m206 and m003 against m004).** Seat LP
(the listening thread, branch `claude/project-thread-hctlox`), 2026-10-06. Own numbering: LP01 is a seat id for main to
harvest. It is not a main arc number and claims no B-number.

**Why this cell.** On main three things are found together only on three two-cusped members of m004's class: chirality,
the 2T door and the count of three. Those members are m202, s959 and o10_150726 (B1418 Q1.2). B1291 excludes three
on any one-cusped manifold. The owner asked how to continue toward the full Standard Model with chiral matter. The
question this cell asks is whether those three members are reached from the root by a cover:

- **If they are**, the matter-carrying data sits on a manifold above m004.
- **If not**, "pass to the class" is an input, and it should be named as one.

## 0. Seen first

- `VERDICT topic-sweep /common cover/: 0 of 1354 arcs on main match (none)`.
- `VERDICT topic-sweep /commensurab/: 17 of 1354 arcs on main match (NEGATIVE 4, PROVED 13)`, read at the level of the
  verdict lines. None constructs a common cover of m004 and m202.
- **sep16 xB015 §(a), the line "Also reported per the seal's own rule":** explicit common covers with m004 were
  exhibited for m206 (degree 2) and m003 (degree 2 over each). They were **not found for m202 and m410 at degree ≤ 6
  over m004**. Commensurability rests on Fominykh–Garoufalidis–Goerner–Tarkaev–Vesnin 2016, Lemma 5.1: tetrahedral
  manifolds are commensurable with m004. m202 is otet04_00000 (checked here).
- **The audit lane's GENESIS reconciliation plan (physical-bridge branch, 2026-10-02):** "A trace field, a common cover or
  a matrix inverse is not itself a proof of native reachability or physical admissibility." This cell takes that as a
  rule. A common cover found here is **not** called reachable unless it is also a move GENESIS names.
- B1418: m202 and s959 are not covers of m004, nor of any smaller one-cusped class member (degrees 2–5). The seven covers
  of m004 inside B1186's 112 do not attain three.
- **Seen in data before this seal, all of it:**
  - the controls (`common_cover_control.out`): m206 is found at degrees (2, 1), cyclic, and factors through level
    m206. m003 is found at degrees (2, 2) with the common cover m206, which reproduces xB015.
  - the seat's exploratory check (outside the repo): no common cover at degrees
    (2, 1) or (3, 6) per (m202, m004). Drilling 57 geodesics of m004 gave no m202. No filling of m202 with |p|, q ≤ 6
    gave a word state.
  - Nothing else: no target has been run on this instrument.

## 1. The cell

`common_cover.py all`. For m202, s959 and o10_150726 in turn, it searches the degree pairs (a, b) with a·vol(m004) =
b·vol(target) and a ≤ 24. At the first a with a match, it reports every common cover found and measures each one with
B1418's own definitions, unchanged: chiral, three, door. It also reports the cover type over each side and whether the
cover factors through a level M2–M4 of m004.

## 2. A lemma, before the run

**L0. No common cover of m004 and a two-cusped target is a level of any word state.** A level of a word state is the
bundle of a power of its monodromy, a once-punctured-torus bundle, so it has one cusp. A finite cover of a two-cusped
manifold has at least two cusps. ∎ So the native moves of GENESIS §3 never reach the targets, whatever this cell finds.
The open question is whether a *general* finite cover of the root carries the data.

## 3. Predictions

| | prediction | prior |
|---|---|---|
| **P1** | a common cover of m004 and m202 exists with degree ≤ 24 over m004 | 75% |
| **P2** | every minimal common cover of m004 and m202 is chiral | 40% |
| **P3** | some minimal common cover of m004 and m202 has the three | 45% |
| **P4** | some minimal common cover of m004 and m202 has chirality, the three and the door together | 25% |
| **P5** | the minimal common cover is not a regular cover of m004 | 60% |
| **P6** | common covers with m004 are found for s959 (≤ 24 over m004) and o10_150726 (≤ 20) | 60% |

**Kills.**
- P1: no match to degree 24. That is then reported as "not found within the bound", never as non-existence; the class
  membership stands on FGGTV.
- P2 to P4: as stated. A minimal common cover that is amphichiral kills P2. One with no cusp-fixing |det(X − I)| = 3
  isometry on any cusp kills P3.
- P5: a regular cover of m004.
- P6: either target not found within its bound.

## 4. Reading rule (fixed now)

- **P4 holds:** a finite cover of the root carries chirality, the door and the three on one manifold. The gap between
  the principle's native moves and the matter content is then exactly one named move: **a general finite cover of the
  root**, since L0 excludes the levels. The page says this is a move GENESIS lists under "Commensurability", not one it
  derives.
- **P1 holds and P4 fails:** a common cover exists, but at least one of the three does not survive passing up to it. The
  data belong to m202, not to the tower above the root. "Pass to the class" is the input.
- **P1 fails:** nothing is said beyond the bound.

## 5. Disclosed

- Instrument (sha256, first 16): `common_cover.py` 6ec81e445d818e42, SnapPy 3.3.2.
- Isometry is decided by canonical isometry signature after a cusp-count and H₁ filter.
- SnapPy's `covers(d)` lists connected covers up to conjugacy. A common cover found on one side but listed under a
  different conjugate on the other still matches by signature.
- The door is computed only for π₁ with at most four generators, and is otherwise reported as None.
- Nothing cited is load-bearing (the owner's rule of 2026-10-06).

## 6. Scope

Frame F-CI. Objects: m004, m202, s959, o10_150726 and their finite covers to the stated degrees. Reach: the class.
No physical claim: chirality here is the absence of an orientation-reversing isometry, "three" is B1418's cusp-isometry
count, and neither is a fermion count. 0 of 19.
