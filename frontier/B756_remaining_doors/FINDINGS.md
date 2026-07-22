# FINDINGS — B756: cc2's remaining-doors package banked — a banked law's general form REFUTED; a new exact iff-law

cc banking seat, 2026-07-22. The reopened cc2 seat's four-door sweep (workflow
wf_b5354331, 9 agents, prereg ec14cacf sealed cc2-side — hash re-verified on receipt;
artifacts copied into this arc), banked under the B743 verify-on-receipt pattern: cc
recomputed the verdict-bearing claims before banking. Gate 5 + Gate 5-Q held throughout.
Nothing to CLAIMS.

## DOOR 2 — "5-inert ∧ fibered ⇒ golden" REFUTED (cc-verified 3/5 from scratch)

cc's independent recompute (cc_verify_door2.py, Sage env — snappy find_field + exact
ideal factorization + Alexander polynomials): **m022** (ITF quartic x⁴+3x²−x+1, field
disc 697, 5 TOTALLY INERT, Alexander a²+5a+1 → monodromy disc 21), **m009** (ℚ(√−7),
5 inert, Alexander a²−4a+1 → disc 12), **m039** (cubic disc −44, 5 inert, Alexander
a²−6a+1 → disc 32) — all three fibered, 5-inert, and NONE golden (disc 5 needs trace 3).
Exceeds the requested 2-of-5 spot-check; the Twister-built M32/M51 stand on cc2's
adversarially-verified workflow. **Consequence applied: the B699 LAW_MAP row carries a
scope-correction clause** — the m004-specific content stands; the general
"5-inert ∧ fibered ⇒ golden" reading is dead (five exact counterexamples). Base-rate
reversal noted: 5-inertness is near-modal in this family (6/7; n=7 caveat flagged).
Structural refinement recorded: the trace field is not a function of the monodromy trace.

## DOOR 3 — the corrected Euler product: NO-PRODUCT, and the honest answer is an exact law (cc-PROVED)

cc2's Register framing was wrong (owned in their synthesis: the generating function is
mod-5, not level-15 — Register erratum theirs). The real content, which cc re-derived
INDEPENDENTLY from the banked B666 generating form a_n = (φχ₀ + φ⁻²χ₂)/2: the exact
iff-law **a_m·a_n = a_mn (gcd(mn,5)=1) ⟺ χ₂(m)=+1 or χ₂(n)=+1**, with the exact defect
**(1−√5)/2** in the both-nonresidue case — a four-line character computation, all four
cases symbolic, plus a 60-pair stress test at primes 400–2000 (18 fail with the exact
defect, 42 pass exactly). Infinitely many failures (Dirichlet), no local correction
possible: **the additive Dirichlet form is FINAL** — the Euler-product door closes with
a theorem, not a shrug.

## DOOR 4 — B302's commensurator route: ROUTE-OBSTRUCTED (banked as cc2 delivered)

The hidden ℤ/3 is real (g³=I in PGL(2,O₋₃), commensurator-level, torsion-free Γ), but
all four tested mechanisms for three INEQUIVALENT generations fail (conjugation
trace-preserving; the three-eigenvalue split is generic Schur behavior; the coset action
is fixed-point-free; B326's module is irreducible mod 2 and mod 4). NOT closed — the
search is non-exhaustive, and ONE residual question stays open, registered as a lead:
is B326's congruence ℤ/3 the SAME ℤ/3 as B302's commensurator element? (OPEN_LEADS row.)

## DOOR 6 — the stale flags: 1.5/2 FIRM (banked on cc2's two-layer verification)

B646-iii benign (the (tr_odd,tr_even)(23)=(1,0) re-derivation matches the banked kill;
κ=25 honestly outside B651's coprimality scope); B647's defect law upgraded to
gauge-COVARIANT (analytic trilinearity proof, not spot-checks) with the untested triples
named open. Accepted on cc2's adversarial-verify layer (all-confirmed; the lindep/E25
rule held everywhere per their record) — cc's receipt covers the two banked-consequence
doors (2 and 3) with in-seat recomputation.

## Ledger consequences applied in this arc
- LAW_MAP B699 row: the scope-correction clause (this arc cited).
- OPEN_LEADS: the B326-ℤ/3 ≟ B302-ℤ/3 identity cell (DOOR4's one live residual).
- cc2's Register erratum is theirs (their document); recorded here for provenance.
- Locks: tests/test_b756_doors.py (the iff-law exact; the three counterexample triples).

## PRE-REVIEW VERIFICATION ADDENDUM (2026-07-22, owner-requested) — coverage raised; one precision note

- **M51-class independently REBUILT** (cc_verify_m51_m32.py, Sage env): b++R⁵L is the
  trace-7 non-cover bundle — sextic ITF, field disc **−453683 (exact match to cc2's
  claim)**, totally 5-inert, non-isometric to the double cover b++(RL)² (verified).
  DOOR2 coverage: 4/5 counterexamples now recomputed in this seat.
- **M32-class: mine differs from theirs, and both count.** My trace-8 build (b++R⁶L) is a
  quartic of field disc 2917 (totally 5-inert) — a DIFFERENT trace-8 conjugacy class from
  cc2's M32 (disc 3173). Not a contradiction: a SIXTH counterexample of the same shape.
- **Precision note (the field reading).** Trace-7 monodromy has Alexander disc 45 = 5·3²,
  i.e. eigenvalue field ℚ(√5) and dilatation φ⁴ (trace 7 = L₄; golden-FIELD monodromy ⟺
  trace is an even-index Lucas number — an infinite, non-special family). So M51 is a
  counterexample under the strict disc-5/seed reading only; under the field reading it is
  golden-fielded. THE REFUTATION IS UNAFFECTED: m009/m022/m039/M32-class (squarefree
  discs 3, 21, 2, 15) are non-golden under every reading. Recorded so the counterexample
  count is stated reading-dependently (4 field-reading / 5 seed-reading / 6 with mine).
- **B754 gate coverage raised**: 5 more cells re-executed at the gate (B107, B285,
  TOMB-L241, TOMB-L57, WALL-7) — check/verdict lines IDENTICAL; combined coverage
  8/19 (cc) + 8/19 (cc3 spot-checks), zero divergence anywhere.
- **DOOR6 status stated plainly**: accepted at cc2's two-layer basis (compute +
  adversarial verify); the trivial half re-checked here ((23|5) = −1 ✓); a full in-seat
  re-derivation would need the B646 r-ladder convention trace — carried to the review as
  a named partial, not blurred.

## DOOR6 DEPTH ADDENDUM (2026-07-22, R28-4) — full in-seat re-execution, byte-identical

The named partial is closed. The r-ladder convention traced: r = the Jeffrey-pipeline rung
(k = r−12 the E₆ level); the B646-iii kill fact is the P4 sector-split at r=23. cc re-ran
cc2's OWN banked machinery read-only (the bucketed Gauss-sum pipeline at P_WORD = ±3; both
gates passed in my run — the P=+3 code path reproduces banked r=13/19, and ε=+1 is the
UNIQUE global sign matching the banked 8-rung ladder): **p4_results.json byte-identical to
cc2's banked file.** The kill fact re-derived: (tr_odd, tr_even)(23) = (1, 0) exactly
(Z(23) = +1.0000000000, imaginary ~2e-16) — the inert⟺even-sector correlate DIES at 23,
per the banked kill; the certificate law agrees (Z(23) = (1−(23|5))/2 = 1). κ=25: the
exact cancellation confirmed (Z(25) = −0.0000000000, ~1e-17) with split (−1, 1), and 25 is
honestly outside the certificate law's coprimality scope (gcd(25, 2·3·5·7·11·19) = 5).
cc2's DOOR6 B646-iii grade FIRM is now verified at full depth in this seat.
Artifact: cc_verify_door6_p4_rerun.txt.
