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
