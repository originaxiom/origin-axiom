# W107 — N3 on the weave: every thread's tick on the triplet, blind (the rule, committed before the code)

**Why.** Main's relay of 2026-10-20, CC_TO_ALL_SEATS_2026-10-20_FOUNDATIONS_AND_THE_SEPARATE_WORK.md, opens the
foundations quest. Its §2 proposes "N3 on the weave": take every Sturmian wording, every positive word with its tick,
acting on the triplet T. Its §3 asks this seat to "Compute Q2–Q4 blind, by your own route, as W100 did for B1667". The
owner agreed on 2026-10-20 ("Both: read + blind compute").

**Weave or thread.** A WEAVE question.
- It takes every thread to a stated length (section "The objects"), with none hand-picked.
- Its quantities are each thread's tick on T and what the ticks do together.
- Its claims are about all threads at once. A row of the census is not a thread result.

**Blindness.** This rule is written before main's N3-on-the-weave output exists. This seat has read:
- main's relay (Q1–Q4 as worded there);
- B1621's FINDINGS (N3 on the golden thread, sealed 2026-10-09);
- its own W38, whose addendum gives the normal form used below.

It will not read any output of main's N3 on the weave before its own output is committed. The predictions below were
not sent to main before this commit.

## The objects

- **T.** The weave's matter triplet as this seat builds it: W21's construction, in W35's orthonormal basis of the
  Hodge–Riemann form (`the_mixing_patterns_verified.py`, `on_T`). The lifts are those chosen by W21's braid relation
  (`the_holomorphic_triplet.py`, `lift_choices()[0]`). The output records them as quaternions in 2O, with c(L) and
  c(R).
- **The parity basis.** The three parity lines: the eigenbasis of the clock and of the normal Klein group (W38's
  addendum). In it every element of the image is c(g) S(g), with S(g) a signed permutation matrix of determinant one
  and c a character.
- **The threads.** Every primitive cyclic word in L and R, containing both letters, of length 2 to 16, up to rotation.
  Words are not identified under the swap L ↔ R, which is not a move of the observed weave (the owner's ruling of
  2026-10-08). An odd-trace thread is one whose matrix has odd trace.
- **A thread's tick.** ρ(w) is the product of the lifts' actions on T along the word.
- **Its operator mean.** The limit of (1/N) Σ_{k<N} ρ(w)^k. Since ρ(w) has finite order n, this is exactly
  (1/n) Σ_{k<n} ρ(w)^k, the projector onto the eigenvalue-1 eigenspace.

## The cells, with predictions and priors

Several cells follow from W38's normal form once A0 holds, and are disclosed as decided at design time (the web seat's
E82 concern). The cells that can fail on the data are Q2c, Q3b, Q3c and Q4b.

- **A0, the controls.** Prior 97% for the whole cell.
  - ρ(L) and ρ(R) are unitary on T and satisfy LR⁻¹L = R⁻¹LR⁻¹.
  - They generate a group of order 96.
  - In the parity basis ρ(L) = c(L) S(L) and ρ(R) = c(R) S(R), with c(L) = e^{−iπ/4} and c(R) = e^{iπ/4}, and S(L),
    S(R) quarter-turns about two different coordinate axes.
- **Q2a, the normal form on every thread.** Prior 97%; decided at design time given A0.
  - For every thread, c(w) = e^{iπ(#R−#L)/4} and S(w) is a rotation of the cube.
  - 1 is an eigenvalue of ρ(w) exactly when c(w)⁻¹ is an eigenvalue of S(w).
- **Q2b, the odd-trace threads.** Prior 95%; decided at design time given A0.
  - Every odd-trace thread has even length.
  - Its S(w) has order 3: a rotation by a third of a turn about a body diagonal.
  - So its eigenvalues are c(w)·{1, ω, ω²}, and its operator mean is rank one exactly when #L ≡ #R (mod 8). Otherwise
    the mean is zero.
- **Q2c, how many.** Prior 75%. The fraction of odd-trace threads of length 2–16 whose mean is non-zero lies between
  0.18 and 0.32 (near ¼ if #L − #R is spread evenly over the even residues mod 8).
- **Q3a, the line.** Prior 95%; decided at design time given Q2b. Each rank-one mean projects onto a body diagonal
  (±1, ±1, ±1)/√3 in the parity basis: the democratic matrix conjugated by a clock element.
- **Q3b, the four axes.** Prior 85%. All four body diagonals occur among the threads of length 2–16.
- **Q3c, what decides the axis.** Prior 70%. Among the threads with a rank-one mean, the axis is a function of the
  word's matrix modulo 4.
- **Q4a, the algebra and the commutant.** Prior 97%. The ticks of the odd-trace threads of length 2–16 together
  generate all of End(T) (dimension 9). Their commutant is the scalars, and no non-zero vector is fixed by all of them.
- **Q4b, the mean over the weave.** Prior 65%.
  - Let M̄ be the average of the operator means over all odd-trace threads of length 2–16.
  - Its diagonal is equal by construction: every body-diagonal projector has diagonal (⅓, ⅓, ⅓).
  - The prediction: its largest off-diagonal entry is at most a tenth of its diagonal entry. So the weave's mean is a
    scalar to that precision, and the democratic structure of one thread does not survive the joint action.
- **Q4c, a control.** Prior 99%. The average of ρ(g) over the 96 elements of the image is zero.
- **R1, reported, not predicted.**
  - The even-trace threads' means, by S-class and c.
  - The counts of Q2b and Q2c under the other three sign choices of the lifts (±g_L, ±g_R), since c depends on them.

## What the outcomes mean

- **If Q2b holds,** N3's democratic matrix is not the weave's. Most threads' ticks have mean zero on T. The rest each
  give one of four axes, and which one depends on the thread.
- **If Q4b holds,** the democratic shape is a property of the golden thread's tick and some others, not of the weave.
  The weave's joint mean is a scalar, as B1633 found for the averaged word coupling, and it fixes no number.
- **If Q4b fails** (one axis or a pair dominates), the weave has a preferred line on T at this length. That would need a
  second length before any reading.
- **If Q2b fails,** W38's normal form or this seat's lifts are wrong, and the arc stops there.

## Instrument and discipline

- **The script.** One script, the_tick_on_the_weave.py, committed before its single run. Its output
  (the_tick_on_the_weave.json and the_tick_on_the_weave_run.txt) is committed before it is read.
- **Two routes.**
  - **Numerical.** The 3 × 3 complex products along each word, with eigenvalues and means at a tolerance of 10⁻⁹.
  - **Exact.** S(w) as integer products of S(L) and S(R), read at A0 and rounded with a check, and c(w) as an exponent
    modulo 8.
  - Every thread's numerical tick must equal c(w) S(w) to 10⁻⁹. A disagreement fails the run's control, and is
    reported as such.
- **Afterwards.** Any failed prediction is recorded as failed, and any later check is labelled post hoc.
- **The rule's own limits.** It does not compute Q1 (the clock). Main did not ask this seat for it.

0 of 19.
