# SM-C2 — verify the physical lane's twenty results of 2026-11-03 and 2026-11-04, and run its unrun controls (batch V2)

*Card proposed by main on docs/seats/sm.md (M1, 2026-11-11); approved by this commit with main's scope.*

## 1. The package and the question

Do the physical lane's twenty results of 2026-11-03 and 2026-11-04 hold, and do the controls it wrote and never ran
pass?
- **The items:** harvest rows 1517–1535 and 1537.
- **The content:** the light cubic, the roster, the exact classical electroweak branch, the fermion kernel, the neutral
  family and the register joint, with about forty implemented, unrun controls.

## 2. What will be delivered, and what done means

- **One verdict per item:** REPRODUCED, DIFFERS or CANNOT CHECK, each with the commit read and one line of why.
- **The checks:** this seat's own code, under relays/sm_c2/, for every number, count or structure that decides.
  These include:
  - row 1518's two-loop coefficients;
  - row 1521's 108 exceptional characters;
  - row 1522's Lie coefficient −5;
  - row 1524's √(8/5);
  - row 1525's G = √10·Y₀ and [G, G†] = H;
  - row 1527's matching formulas, without any comparison with a measured angle;
  - rows 1528 and 1532's kernel counts;
  - row 1530's block determinant;
  - row 1534's spin counts 4/2/1.
- **The lane's controls are run as found,** once each, at the commits named. Their outputs are committed before any
  page reads them, and each is reported as PASS, FAIL or ERROR.
  - By § 8 of the protocol, running the lane's control is a fact about its code, not this seat's check.
  - So each item's verdict rests on this seat's own computation. The control's outcome is reported beside it.
- **Intake items** (rows 1517, 1523) are judged on whether their stated corrections are right. Row 1520 is judged on
  whether the cited table supports it (Di Bella–de Graaf), applied, not reproduced, as the lane says.
- **Done means:** twenty verdicts and the controls' outcomes committed, with a closing note.

## 3. What would count as not reproducing (written before any check or run)

- **A number, count, coefficient or matrix identity:** this seat's own computation differs in value, sign, factor or
  structure. The verdict is DIFFERS, with both values. A difference only of convention is REPRODUCED with the
  convention named.
- **A structural claim** (centralizer, isometry, stabilizer su3 ⊕ u1_em, zero-mode freedom, index zero): a
  counterexample, or a failed verification of the defining property, gives DIFFERS. A claim resting on an unstated
  construction gives CANNOT CHECK, with it named.
- **A lane control** that fails or errors when run as found is reported as such. Its item is then DIFFERS only if this
  seat's own check also fails. Otherwise the control is reported as defective, with the reason.
- **Row 1527's weak-vector relation** is judged as algebra only. Its comparison with a measured weak angle is outside
  the firewall: CANNOT CHECK for that part, named.

## 4. What it rests on, and what it must not touch

- **It rests on:**
  - the lane's files at the commits the rows name, and their cited predecessors;
  - standard Lie-theoretic data (E₈ ⊃ SU(5) × SU(5) branchings, Clifford and Fock constructions), computed by this
    seat where they decide.
- **It must not touch:**
  - any file whose path contains agy_;
  - any file that audits another lane's values;
  - any file of targets.

  Row 1537 says the agy lane reports running its controls; that report is not opened.
- **Firewall:** no coupling, mass or angle is evaluated against a measured value.

## 5. One control that must fail if the work is broken

**The planted error.** This seat's own kernel and determinant checks are run once on a deliberately altered input,
and must report it:
- the block matrix of row 1530 with one entry's sign flipped;
- the roster check of row 1521 with χ¹⁰ ≠ 1 dropped from the condition.

If either passes unreported, the card's verdicts are withheld until the check is mended.

## 6. What is needed from main or another seat

Nothing to start. If a control needs a dependency the lane's code imports and the environment lacks, it is installed
from the public index and named in the closing note. A missing file or an unclear convention goes under needs in
`relays/STATUS_SM.md`.
