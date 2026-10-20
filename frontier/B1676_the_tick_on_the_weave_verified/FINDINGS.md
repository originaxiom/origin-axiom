# B1676 — THE TICK ON THE WEAVE, VERIFIED ON MAIN: N3's democratic matrix belongs to one class of threads (#L ≡ #R mod 8), not to the principle; on the weave the ticks' joint mean is a scalar, their commutant the scalars, and they generate all of End(T)

**Verdict: PROVED (a verification arc).** cc (main), 2026-10-20. POINT_REGISTER P-200 (the owner's question whether the
golden rule a → ab, b → a is the m004 mistake in word form). 0 of 19.
- **What this arc re-banks.** The SM seat's W107, N3 on the weave, run blind at main's ask. Its rule (2daabdde4) came
  before its script (7beaa530d), which came before its one run (191c367a7). The seat read no output of main's.
- **Main's own predictions came first, independently.** Main's design (`docs/foundations/N3_ON_THE_WEAVE_DESIGN.md`,
  committed at S146) was written before main read W107. Its Q2–Q4 match W107's results: the mean is rank one exactly
  when the determinant is 1, the lines are trimaximal with more than one, and the weave's mean keeps the grading.
- **How it was verified.** Main's own route reproduces every count (`verification/main_check/`). It uses the record's
  letter lifts (B1621's `T_of` on single letters) multiplied along each word, B1621's parity basis, and its own Lyndon
  enumeration. It does not import the seat's code.

## 0. Seen first

`VERDICT topic-sweep /clock|tick|democratic|Sturmian|substitution|fixed.point word/: 81 of 1447 arcs on main match (NEGATIVE 13, OPEN 4, PROVED 64)`
— chiefly B1621 (the golden rule's clock and tick: LR's mean rank one and democratic), B1633 (the averaged word coupling
a scalar), B1607 (the principle's tick at the common point), and B1323 (the Sturmian morphisms abelianise onto exactly
the non-negative GL(2, ℤ) matrices). **Literature:** flavour democracy (Harari, Haut and Weyers 1978); Sturmian morphisms
as the positive automorphisms of F₂ (Mignosi and Séébold 1993; Wen and Wen 1994).

## 0b. Disclosed

- **Seen before W107 ran.** Main's smoke test (rank one on LR, zero on LLLR) and main's structural argument: an
  odd-trace thread acts as a phase times a signed 3-cycle, so its eigenvalues are the cube roots of its determinant.
- **One of W107's cells failed as worded.** Its "generate End(T)" was measured as the linear span, which is 6. Post hoc
  and labelled: every odd-trace tick has zero diagonal, and the algebra the ticks generate is all of End(T).
- **Which threads carry the mean depends on the lift's sign convention.** Flipping the sign of one letter's lift moves
  the class: 916 threads become 906. The structure does not change: about a quarter of the threads have a rank-one mean,
  and the joint mean is a scalar. This is B1640's point that the multiplier's hand is a convention.

## 1. What holds (W107, reproduced on main)

| | result |
|---|---|
| the threads | 8 798 primitive positive words of length 2–16 up to rotation; 3 822 of odd trace, all of even length, each acting on the parity lines as a 3-cycle |
| the tick's mean (Q2) | **rank one exactly when #L ≡ #R (mod 8), zero otherwise**: 916 and 2 906. The eigenvalues are the cube roots of det T(w) = ζ₈^{3(#R−#L)}, up to the lift's convention |
| its lines (Q3) | every rank-one mean is a body diagonal (±1, ±1, ±1)/√3 of the parity basis, the democratic matrix conjugated by a clock element; all four occur (215, 229, 235, 237); the axis is a function of the word's matrix mod 4 |
| the weave's joint mean (Q4) | **a scalar**, 0.0799 · I, with off-diagonal 3.1% of the diagonal; the commutant of the ticks is the scalars and no vector is fixed by all; the ticks generate End(T) |
| even-trace threads | 139 act on T as the identity; their rank-one means lie on parity lines |

## 2. What it says

- **N3's democratic matrix is a seed-class property, not the principle's.**
  - It belongs to the threads with #L ≡ #R (mod 8): those whose linking number with the trefoil, in the seat's words,
    is divisible by 8.
  - LR is the simplest of them, with #L − #R = 0. Its trivial class under the weave's characters is why the golden
    rule's tick looked like "the principle's".
  - The same characters sort the period phase i^{#L−#R} (mod 4).
- **On the weave the ticks fix no direction.** Their joint mean is a scalar and their commutant the scalars. N3's
  conclusion, "fix no number", stands on the weave, now for the right reason: the weave averages the four democratic
  directions away.
- **What it does not show:** any number (0 of 19); the clock's weave-wide statement (Q1), which holds by construction
  for every wording and is not re-tested here; anything about longer words than 16.
- **For the paper:** draft 9's N3 already says the weave version "is not computed here". This arc computes it, so it is
  queued for a later draft (P-203: no new content enters the frozen paper).

## 3. Files

- `verification/received/`: W107's rule, script and run, copied from the SM seat's branch at `3307563fd`. The
  208 648-line output is identified by its sha256 in `SHA256_RECEIVED.txt`, not copied.
- `verification/main_check/`: main's independent script and its run.
- The lock: `tests/test_b1676_the_tick_on_the_weave_verified.py`.
