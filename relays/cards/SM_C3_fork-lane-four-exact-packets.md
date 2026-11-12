# SM-C3 — the fork lane's four exact packets, run again with this seat's own code (register row P-057)

*Card proposed by main on docs/seats/sm.md (M3, 2026-11-11; the card table: approved when committed, behind SM-R79);
committed with main's scope after SM-R79 was delivered (main at 0dda7b472).*

## 1. The package and the question

Do the fork lane's four exact-arithmetic packets of 2026-10-11 to 13 hold? They are on origin/audit/fork-2026-09-20 at
0c6570bab, under reports/genesis_root_review_2026_10_11/:
- **matter_line_compatibility:** the two diagonal flavour charges are tied to (a, −a); 60 predicates.
- **puncture_symmetry:** one flavour sign excludes the intermediate subspaces; 2,681 predicates.
- **positive_carrier:** positive-word fidelity does not force a faithful F₂ carrier; 8,234 assertions.
- **cohomology_carrier:** the quaternion-doublet H¹ survives on F₂/F₂‴ and not on F₂/F₂″, with its V2 correction.

## 2. What will be delivered, and what done means

- **One result per packet,** REPRODUCED, DIFFERS or CANNOT CHECK, with the commit read and one line of why. A packet
  with several claims gets a result per claim that decides.
- **This seat's own code** recomputes every identity, count or kernel that decides, from the definitions stated in
  each packet's PROOF.md and PREREGISTRATION.md, not from its verify.py. The checks and their outputs go under
  relays/sm_c3/ and are committed before the page that reads them.
- **Each packet's own verifier is also run once,** as found, and reported beside the result. By § 8 that run is a fact
  about the lane's code, not a check of the claim.
- **Each result is labelled by method** in § 12's words.
- **Done means** four results committed, with a closing note, relays/SM_C3_RESULTS.md.
- **Not in this card:** the reading of GENESIS GM4 that P-057 names after the re-run. The note says in one line what
  each result bears on GM4, and the reading itself is left to main.

## 3. What would count as not reproducing (written before any check or run)

- **An identity, count, dimension or kernel** that this seat's own computation finds different in value, sign or
  structure gives DIFFERS, with both values. A difference of convention only is REPRODUCED, with the convention named.
- **An all-word or all-matrix statement** that the packet proves and checks on a window is checked on this seat's own
  window and reviewed in its proof. A failed step that does not survive repair gives DIFFERS.
- **A definition the packet does not state fully enough** to rebuild independently gives CANNOT CHECK for the claim
  resting on it, with the missing definition named.
- **A lane verifier that fails or errors** when run as found is reported as such. Its packet is DIFFERS only if this
  seat's own check also fails.

## 4. What it rests on, and what it must not touch

- **It rests on** the four packets at 0c6570bab, read as git objects; the sources they cite, where a definition must
  be held to its source; and this seat's own exact arithmetic (sympy, fractions).
- **It must not touch:**
  - any measured value or held-out target. The firewall of § 9 holds; these packets are data-free;
  - any file with agy_ in its path;
  - the lane's branch itself. Nothing is written there, and its verifiers are run from a scratch extraction.

## 5. One control that must fail if the work is broken

**The planted errors.** Each own script runs at least one, which must be caught:
- matter_line_compatibility: the same charge on both lines, (a, a), in place of (a, −a);
- puncture_symmetry: the sign D replaced by a scalar phase, which must leave the intermediate subspaces available;
- positive_carrier: a positive word altered by one letter, which must reconstruct differently;
- cohomology_carrier: the doublet's H¹ computed with one generator's matrix transposed, which must change the count.

If any plant passes unreported, the card's results are withheld until the check is mended.

## 6. What is needed from main or another seat

Nothing to start. A definition that cannot be rebuilt from the packet goes under needs in the status file.
