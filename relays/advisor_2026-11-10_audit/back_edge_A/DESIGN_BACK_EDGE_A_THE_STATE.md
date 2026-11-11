# DESIGN — back-edge A: the state (the closed loop on the hyperbolic metric)

**From:** the advisor seat. **To:** the owner and cc. **Kind:** `propose:` — a design written before any computing.
Data-free: no measured number appears, and nothing here is compared with one.
**The owner's ruling it follows:** 2026-11-10, to the question which back-edge to try first: "A" (R9).
**What it takes up from the register:** P-744 (the read-out by a state on the hyperbolic metric), with P-742, P-743
and P-726 beside it.
**Who checks it:** this seat wrote the design, so this seat does not review it. The pre-registration built from it is
reviewed by cc or another seat before any run; this seat's part afterwards is the acceptance check only.

## 1. What back-edge A is

In the closed loop of `THE_CLAIM_STATED_THE_CLOSED_LOOP.md`, the record's chain is a line because nothing downstream
constrains anything upstream. Back-edge A supplies two such constraints from the geometry's own spectrum:

> **(A-read)** The point of the fibration circle at which τ is read is where the history's lightest state sits.
> **(A-adm)** A history is allowed only if that state is single: one state, one place.

With (A-adm), what is allowed depends on what is read. That is the back-edge.

B1857 has this in the flat-fibre (Sol) model. The design below is for the hyperbolic metric, on the metric's own
clock, where the τ read-out rule lives.

## 2. Four things the design must settle before anyone computes

### 2.1 Which operator — the scalar Laplacian cannot be it

On a finite-volume hyperbolic manifold the lowest state of the Laplace–Beltrami operator on functions is the constant
function, with eigenvalue 0. Its "place" is the whole manifold, weighted by volume. Pushed to the circle that is
B1846's volume weight ρ, which B1846 T2 already shows has no atom. **So "the lightest state" of the scalar Laplacian
is the weight, not a point, and gives no back-edge.** B1857 avoids this by taking the lightest *massive* state of a
twisted mode in a model with a free area A.

The state therefore needs an operator with no zero mode. The candidates that use only the metric and discrete data:

| Operator | Uses | No zero mode because | Chosen ingredient |
|---|---|---|---|
| **(S1)** the scalar Laplacian's first excited state | the metric | orthogonal to constants | none — but see 2.2 |
| **(T)** the Laplacian on sections of the frame's flat bundle | the metric and the frame's line | a non-trivial flat unitary bundle has no parallel section | which line — this is Data, so the loop tightens |
| **(D)** the Dirac operator | the metric and a spin structure | generically | which spin structure (B1477–B1481 hold the record's work on them) |

**The rule proposed for choosing, written before computing:** the state's operator is the operator whose zero modes
are the frame's matter — the one B1656 uses at the fibre's puncture — extended from the fibre to the whole history.
That is (T) with the frame's line. It adds nothing: the frame already carries it. (S1) is run beside it as the
control that uses no Data at all.

### 2.2 Whether the state exists at all

A state is an L² eigenfunction below the continuous spectrum, which on a cusped hyperbolic 3-manifold begins at 1.
- For (S1): m004 is arithmetic and congruence (chain link C9), where small eigenvalues are excluded below a known
  bound; **on the golden background itself there may be no state.** On a long history a small eigenvalue must
  appear, because two fibres cut the manifold into pieces of volume proportional to its length. Where that sets in
  is a computation.
- For (T): the bottom of the twisted spectrum depends on the bundle's holonomy around the cusp. If the holonomy on
  the cusp torus is non-trivial, the twisted continuous spectrum starts higher or is absent on that cusp, and a
  lowest state exists more readily.

**This is a first, sharp, data-free question:** for which histories does a state exist? A history with no state has
no read-out under A. That is an admissibility condition nobody chose.

### 2.3 Where the frame's line can live — exact facts (`extension_facts.py`, this folder)

A flat line on the fibre extends over the history only if the monodromy W returns it to itself. Computed in integers:

- The golden background has |det(LR − I)| = 1 and |det(LR + I)| = 5. **No non-trivial fibre character is fixed by LR;
  exactly one cyclic group of order 5 is sent to its inverse** — the points ±(1,2), ±(2,4) of the 5-torsion. This is
  the line B1845 calls RL's own.
- On a character sent to its inverse, the object that extends is the pair χ ⊕ χ⁻¹ with the swap: a flat rank-2
  bundle, not a line.
- **The sign alternates with the number of golden periods.** For the run of 6 closed by (LR)^k: W v = +v at k = 1
  and 3, W v = −v at k = 2. The same alternation holds for (2,1,2,1,2), (2,1,1,1,2) and the golden word.

| history | k = 1 | k = 2 | k = 3 |
|---|---|---|---|
| (6) + (LR)^k | line (+) | pair (−) | line (+) |
| (2,1,2,1,2) + (LR)^k | pair (−) | line (+) | pair (−) |
| (2,1,1,1,2) + (LR)^k | W ≡ −I mod 5: every order-5 point, as pairs | line (+) | pair (−) |
| golden (LR)^(k+1) | line (+) | pair (−) | line (+) |

Three consequences:

1. **The record's "line premise" is a consistency condition, not a free premise.** "The departure fixes the line" is
   exactly "the frame's line extends over the history". If the frame is read on one line, this premise is forced by
   the loop. The "charge premise" (the departure is ±I at level 5) is the same condition for a frame that uses the
   whole level-5 space. Which of the two is forced therefore reduces to one question already on the register: does
   the frame live on one line or on the level-5 space (P-721)?
2. **Odd and even k are different bundles.** A limit k → ∞ taken through k = 3, 4, 5 mixes them. Any twisted
   computation treats the two parities separately, or uses the pair uniformly.
3. **SnapPy agrees on the count:** H₁ of L⁶RLR has torsion ℤ/20 = |det(W − I)|, which contains the 5-torsion the line
   needs at k = 1; H₁ of the golden background is torsion-free, so there the line exists only as the pair.

### 2.4 The place of a state, and when it is "one place"

By the symmetry σ of a palindromic history, every eigenfunction is σ-even or σ-odd. An even one has an extremum on
both fixed fibres (the tube and the anti-apex); an odd one vanishes on both. So a single eigenfunction does not by
symmetry pick one of the two points. The definition proposed, written first:

- **the profile** of a state ψ is p(s) = ∫ over the level surface Σ_s of |ψ|², per unit harmonic time, normalised to
  total 1;
- **the place** is the mode of p;
- **the state is single** if the lowest eigenvalue is simple (its gap to the next is resolved by the instrument's
  stated error) **and** p has one mode carrying more than a stated share of the total. The share is fixed in the
  pre-registration, with the instrument's error known, not after seeing a profile.

## 3. The fork inside A that the owner must rule on

(A-adm) leaves many histories allowed: B1857 already has two with a single state, (6) and (2,1,2,1,2), and there
will be more. To end with one, something further is needed, and there are two routes:

| | Route | What it adds | Against it |
|---|---|---|---|
| **A-one** | one history: among the allowed, the least action | a minimisation postulate. The record still lists minimisation as CHOSEN (B1853), and length and volume disagree on the answer (B1857). | under plenitude every allowed history happens; picking the cheapest is picking a thread |
| **A-all** | all allowed histories together are the configuration; the read-out is of their joint action | nothing — it is the weave rule applied to the loop | "the read-out of a set of histories" is not yet defined; B1813 says a sum over them needs a counting rule |

A-one is computable now and is what the record has been doing. A-all is what plenitude and the weave rule ask for,
and its first step is a definition, not a computation. **The seat's advice:** run A-one as the test bed — it is where
the instruments are — and label everything it returns a thread result; state A-all as the claim, and open its
definition as a fork in `GENESIS.md`. The claim "exactly one outcome" is then about A-all, and A-one's fixed points
are its candidates' threads.

**The owner accepted this advice on 2026-11-10 (`OWNER_RULINGS_2026-11-10.md`, R10).**

> **Dated note, 2026-11-10, night — two points of the web seat, passed on by main, and accepted** (main's B1872 and
> its note to this seat of the same day).
>
> 1. **(A-adm) is not yet a rule about what is allowed.** "Together" now has a definition on main: the joint action
>    of the allowed histories on the shared records. A condition belongs to what is allowed only if it is kept when
>    two allowed histories are composed. Nobody has shown that "the lightest state is single" is kept. Until someone
>    does, (A-adm) is a selection made on one history, a thread device, and under R10 it cannot define the weave's
>    allowed set. The design's fork already labels A-one a thread result; this note extends that label to (A-adm)
>    itself.
> 2. **"The frame's line" must be a mark on the shared records.** A history's own line moves with the point at which
>    the history is cut open, so § 2.3's table is a table about base points as much as about histories. If the tick
>    is an act the mark is the golden line and not one of its two twins (`principle_top_down/attacks_B_to_E/`, H13).
>
> **A test to put before any run of this design** (it needs main's instrument, not this seat's): take the two
> histories that B1857 found with a single state, compose them, and ask whether the composite has one. If not,
> back-edge A in this form closes nothing for the weave, and what is left of it is (A-read) as a read-out on one
> history.
>
> **Dated note, 2026-11-11: the test was run, and (A-adm) is withdrawn as a rule about what is allowed.** The web
> seat ran it as a sealed card the same night and main verified it with its own code (B1875). Two histories with a
> single state and the same departure compose to a history whose apex is in two places: 18 of the 36 composites
> tested, each by an exact symmetry of the composite's own word. Being single is a property of one history's own
> cycle of heights. So back-edge A, in the form designed here, closes nothing for the weave. What is left is
> (A-read) on one history, labelled a thread's. The tests A0 to A7 below are kept as written and none is to be
> run as a test of the weave.

### 3b. Other principles that could pick a history (the owner's question, 2026-11-10)

"Least action" is one rule of the form "take the least X". Others exist, and on the numbers the record already holds
they pick different histories. (Excess volume and excess length from B1853, B1857 and the audit's re-run; the single
state is B1857's, in the flat-fibre model; nothing here is new computation.)

| Departure | letters | runs | excess volume | excess length | single state | invisible to all of level 5 |
|---|---|---|---|---|---|---|
| (6) | 6 | 1 | 1.5714 | 2.3487 | yes | yes (the extra L⁵ is the identity mod 5) |
| (2,1,1,1,2) | 7 | 5 | **1.3972** | **1.4745** | no (a mirror pair) | no (it fixes the line only) |
| (2,1,2,1,2) | 8 | 5 | 1.9858 | 2.1597 | yes | no (it fixes the line only) |
| (2,1⁸,2) | 12 | 10 | 1.4103 | 1.4786 | no (a mirror pair) | no (it fixes the line only) |

| Principle | What it says | Picks | Needs |
|---|---|---|---|
| least action, by volume | the cheapest in the metric's volume | (2,1,1,1,2); with "single state", (6) | an action; "single state" beside it |
| least action, by length | the cheapest in geodesic length | (2,1,1,1,2); with "single state", (2,1,2,1,2) | a different action — it disagrees with volume |
| shortest description | fewest letters, or fewest runs | (6) | a description language |
| first reached | the first allowed word in the grammar's own order of generation | (6) under the level-5 premise; not computed under the line premise | an order of generation |
| no unresolved tie (sufficient reason) | a configuration with two equal alternatives is not one configuration | removes the mirror pairs; does not rank the rest | nothing — this is what "single state" already is |
| what cancellation cannot see (the foundation's own PF1) | the departure that persists is the least one no level can detect and undo | (6), if "no level" means all of level 5 | which levels count (the line or the whole level; P-721) |
| self-similarity | the history is generated by the same rule as its background | no departure at all, or an infinite self-similar pattern of them | — it rules out a single isolated departure |
| typicality | the history is the generic one under the grammar's own measure | none of these; and the measure is not unique (B1813) | a measure |
| consistency alone | the history is whatever the loop's conditions leave | whatever A1–A6 return; one only if the conditions are tight enough | nothing |

**Three readings of this table.**

1. **Rules of the form "least X" need an X, and two X on record already disagree.** So "least action" is an input,
   and so is any replacement for it.
2. **Only three entries need no X:** no unresolved tie, self-similarity, and consistency alone. They are the ones
   that deserve the name "pure logic". None of them, alone, is known to leave exactly one history.
3. **Agreement across principles is itself evidence.** (6) is the pick of shortest description, first reached, the
   foundation's own non-cancellation reading and volume-with-single-state, and it is not the pick of either bare
   action. A history selected by many unrelated rules is more robust than one selected by one; a pre-registered table
   of this kind over the full family of A6 would measure that. It does not make (6) forced, and P-717's disclosure
   applies: attention came to 5 and the run of 6 from the data.

**For the claim:** this is the case for A-all. If several defensible rules pick different single histories, then a
single history is a choice, and what is not a choice is the allowed set as a whole.

## 4. The tests, in the order of cost

Each is pre-registered and sealed in its own commit before it runs; each names its instrument's control first
(Review 76's practice: an instrument runs on a known answer before any reading).

| # | Test | Cost | What it decides | Refuted or stopped when |
|---|---|---|---|---|
| **A0** | the facts of 2.3, and the scalar ground state's triviality (2.1) | done here, exact | which bundles exist on which histories | — |
| **A1** | **existence:** does a state exist — (S1) and (T), by parity of k — on the golden background, on (6), (2,1,2,1,2), (2,1,1,1,2) at k = 1, 2, 3 | one eigen-solver setup per member (the Hejhal or collocation class of B1846/B1854) | whether A has anything to read | no state on the candidate histories: A is closed as a negative for that operator |
| **A2** | **the loop is a loop (T0):** the place of the (T) state against the place of the (S1) state, and (T) on the two parities | as A1 | whether the place depends on Data | the place is the same for every operator and bundle: Read does not depend on Data; A-read stands but adds no loop beyond (A-adm) |
| **A3** | **single or not:** eigenvalue gap and profile share on each history | as A1 | (A-adm)'s allowed set within the declared family | — |
| **A4** | **it can fail (T3):** a mirror-degenerate history named in advance, (2,1,1,1,2), must come out not single | as A1 | the criterion is not vacuous | the control is single: the criterion admits everything |
| **A5** | **the second thread (T4):** the same on the silver and bronze backgrounds with their own levels (|det(W + I)| = 2 + tr) | as A1 | whether the loop selects the golden background | it closes equally there: SE1 and SE2 stay chosen |
| **A6** | **the family (T2):** every history with at most two departures to a stated length — existence, single, place | large; only after A1–A5 | the number of fixed points of A-one | none, or more than one after the stated selection |
| **A7** | **a second reader (T5):** A1–A4 by a seat that has not seen the first outputs, with another method | as A1 | the instrument | the two disagree beyond their stated errors |

**The value of τ at the place is not read in any of these.** A1–A7 return existence, simplicity and a location on the
circle. τ there is a separate, later reading under the τ read-out rule, and its comparison with anything is a sealed
card (P-714).

## 5. Traps this design is written to avoid (each seen in the audit)

| Trap | Where it was seen | The guard here |
|---|---|---|
| a number called an error bar that is not one | B1854 (finding E9) | A1 states the solver's error from a control with a known spectrum before any reading |
| a control that cannot fail | B1847's lock (L5), B1853's HL2 (E12) | A4 names its failing case in advance |
| a limit through mixed objects | the k → ∞ extrapolation over both parities (2.3) | parities are separate families |
| a premise that is really a consistency condition, or the reverse | the line and charge premises (2.3); B1856 (E3) | each premise is stated as "extends over the history" for a named bundle |
| a thread result stated about the whole | finding class 3.9 | every output of A-one carries `domain: thread`; only A-all may be stated about the weave |
| the answer known before the question | P-717's disclosure; finding V4 | the share threshold, the family bounds and the selection rule are fixed before A1 runs, by a seat that has not seen where the fit landed |
| a model's free scale | the Sol model's area A (P-743) | no free scale: the hyperbolic metric has none |

## 6. What each outcome would mean

- **A state exists, its place depends on the bundle, single states are rare, and one history survives:** A-one has a
  fixed point; the loop is real on a thread; the work moves to A-all and to the forward links still chosen.
- **A state exists and is single on many histories:** the loop does not determine the outcome by itself; minimisation or
  A-all carries the weight, and the record says so.
- **No state on the candidate histories:** back-edge A is closed for that operator, with its scope, and the next
  candidate is taken up.
- **The loop closes equally on the other backgrounds:** the golden one is not selected by A.

Any of these is a result. None of them is a value.
