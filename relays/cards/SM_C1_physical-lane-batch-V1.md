# SM-C1 — verify the physical lane's ten hand derivations of 2026-10-27 to 2026-10-29 (batch V1)

*Card proposed by main on docs/seats/sm.md (M1, 2026-11-11); approved by this commit with main's scope.*

## 1. The package and the question

Do the physical lane's ten hand derivations of 2026-10-27 to 2026-10-29 hold as stated?
- **The items:** harvest rows 1418, 1420, 1421, 1422, 1423, 1425, 1465, 1487, 1488 and 1489.
- **The source:** each at the commit its row names, on the lane's branch (the one ending physical-bridge-2026-09-05).
- **The emphasis:** the analytic cores main left unchecked.

## 2. What will be delivered, and what done means

- **One verdict per item:** REPRODUCED, DIFFERS or CANNOT CHECK. Each comes with the commit read, one line of why,
  and where this seat's own check lives.
- **The checks:** this seat's own code, under relays/sm_c1/, for every identity, count or coefficient that decides.
  For the analytic proofs (rows 1423, 1425's gauge fixing, 1465's raising argument, 1487, 1489), a written step-by-step
  review. Each step is either re-derived or marked as resting on a named hypothesis.
- **The note:** one closing note in the relays folder names the card it closes and where each thing is.
- **Done means:** ten verdicts committed, with their checks before the page that reads them.

## 3. What would count as not reproducing (written before any check)

- **An identity, coefficient or count** (rows 1418, 1420, 1421, 1422, 1425's weights and light vector, 1465's
  kernel counts, roster and β coefficients, 1487's scale-free combination, 1488's h_C, running vectors and
  determinant): this seat's own computation gives a different value, sign, factor or structure. The comparison is
  exact (rationals) or symbolic where possible, otherwise at 30 digits.
  - The verdict is DIFFERS, with both values.
  - A difference only of convention (a normalisation stated elsewhere in the lane's record) is REPRODUCED with the
    convention named.
- **A proof** (rows 1423, 1425, 1465, 1487, 1489):
  - **DIFFERS:** a step fails — a counterexample, a wrong estimate, or a cancellation that does not happen — and the
    conclusion does not survive the repair this seat can make.
  - **CANNOT CHECK:** a step rests on a construction or hypothesis not stated in the item or its cited predecessors
    (named), or on a comparison with a measured value (named).
  - **REPRODUCED:** every step is re-derived, or rests on a named standard theorem.
- **Main's partial checks** recorded in the rows (sympy, exact fractions, Frullani) are re-done with this seat's own
  code. They are not cited as evidence.

## 4. What it rests on, and what it must not touch

- **It rests on:**
  - the lane's files at the commits the rows name, and their cited predecessors on the same branch;
  - standard results, named where used: Duhamel, trace-class ideals, Frullani, the SU(5) branching rules, background
    field gauge fixing.
- **It must not touch:**
  - any file whose path contains agy_;
  - any file that audits another lane's values;
  - any file of targets.
- **Firewall:** no coupling, mass or angle is evaluated against a measured value. An item that could be judged only so
  is CANNOT CHECK, with the comparison named.

## 5. One control that must fail if the work is broken

**The planted error.** Before the verdicts, the identity and coefficient checks are run once on deliberately wrong
inputs, and each must report the error. The inputs are:
- the doublet alone, (0, 1/2, 3/10), in row 1420's universality check;
- one branching coefficient changed by one unit in row 1421's D coefficients;
- a ghost weight of −2 instead of −3 in row 1425;
- a spectrum of nonzero total weight in row 1422's Z(0) = −h.

If any planted error passes unreported, every verdict of this card is withheld until the check is mended.

## 6. What is needed from main or another seat

Nothing to start. If an item cites a construction that cannot be found on the lane's branch, the question goes under
needs in `relays/STATUS_SM.md` for main to pass to the lane.
