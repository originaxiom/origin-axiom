# ENUM_CC — THE W3 TERMINAL ENUMERATION (cc seat; GATE ARTIFACT)
# Governing: PREREG_W3_DECISION.md (563a2858) + PREREG_W3_DECISION_ADDENDUM_1.md.
# Independent cell: no other seat's W3 enumeration was read (none existed
# in the arc directory at the time of writing). Supporting computation:
# v5_discriminating_facts.py / v5_discriminating_facts_out.txt (exact;
# all assertions passed; the banked W33/W2 target numbers reproduced from
# scratch). Working notes: enum_notes.md.

## I. THE FOUR EXCLUSIONS, WITH EXACT HYPOTHESES

E1 — FINITE-DATA TRACES (wave 1, kills 1-7; each candidate-specific,
each an exact computation; E1 is a list of proven kills, NOT a general
theorem):
  1. the B205 q-tower — exact first mismatch (B672);
  2. the word-length filtration — structurally excluded (B672);
  3. the ladder certificate — exact no-go: 0/130 support frequencies
     hit an RR theta class; the 2-part bound 8 < 40's requirement (B672);
  4. the pure eta-menu — the mod-5 exponent obstruction (B672);
  5. Tube(Fib) Hochschild — semisimple (dim 7) => HH^{>=1} = 0
     identically (B677/G1, T0);
  6. the weld-weighted character combinations — Q(zeta_5)-irrational
     leading coefficient at n = 0 vs integer targets + support classes
     {11/60, 59/60, 53/60, 17/60} never meeting {2/5, 3/5}; one
     rational rescaling excluded by sealed clause (B677/G1);
  7. the Eichler-Shimura twisted trace tower — tr(A_1*|H^1(Gamma(5),
     Sym^m)) = 0 identically for all m >= 1, two independent routes;
     mechanism = THE GOLDEN-ROTATION LAW (B674 route 1; LAW_MAP).
HYPOTHESIS COVERAGE: exactly these seven candidates. No reach beyond.

E2 — PERIODICITY / RATIONAL GENERATING FUNCTIONS (the melody theorem,
B651; minimal period P = 175560 certified B662/G): the ladder
Z(kappa) is periodic — its complete information content is one period
of finite data. HYPOTHESIS: the construction's output stream is drawn
from the ladder or is eventually periodic. KILL MECHANISM vs the
targets (computed, FACT 1): an eventually-periodic stream takes
finitely many values, hence has bounded v5 and bounded size; the
targets' v5(denom) grows 1 -> 146 across n = 1..119 and the dressed
integer targets grow partition-like (3402 by n = 40, banked). No reach
beyond eventually-periodic streams.

E3 — FINITE-ORDER INTEGRALITY vs GROWING v5 (the 5-adic exclusion;
instance 1 = W33's ladder exclusion; instance 2 = the W2 Molien kill,
decided at n <= 1; LAW_MAP row). EXACT HYPOTHESES:
  (a) the output is the twisted character / Molien series of a FIXED
      finite-order operator on a graded object with integer
      multiplicities => every coefficient is a Z-combination of roots
      of unity = an algebraic INTEGER (the two-line theorem,
      ADJUDICATION_BIFOCAL_OBJECTION) — more generally, ring-level as
      banked: any construction with an algebraic-integer coefficient
      ring;
  (b) point 3 of the kill: a FIXED constant (or fixed series dressing
      — the dressed view computed inside kill #8) has fixed v5 and
      cannot bridge a v5 gap growing with n.
TARGET FACT (reproduced from scratch, FACT 1): pure 5-power
denominators; v5(denom) = 1, 12, 49, 99, 146 at n = 1, 10, 40, 80,
119 on BOTH components; secant slopes in [1.205, 1.25].
REACH per ADDENDUM_1: ANY finite-order operator, ANY end(s) supplying
operator or module — both CRT factors of the level-15 congruence
representation included (computed witness: combined-factor Molien in
Z[zeta_15] through q^8, denominators identically 1). E3 does NOT
cover: grade-growing operator families, non-character outputs, or
coefficient rings non-integral BY CONSTRUCTION.

E4 — GRADING NON-PRESERVATION (the W2 design theorems — exactly
three, applied to nothing else, per W2_CLOSEOUT_ADJUDICATION_CC #3):
  (a) THE FLAT-LEVEL GROWTH KILL: every W-stable grading on the flat
      Gamma(5) objects has bounded (total-pole-order filtration,
      dim gr_n -> ~12 = #cusps) or linear (weight grading) growth;
      bounded/linear graded dimensions cannot carry partition-like
      coefficients; verbatim on the flat skein module (polynomial
      multicurve growth) — jointly THE EXPONENTIATION LAW;
  (b) THE HYPERBOLIC-SLOPE OBSTRUCTION: the weld acts on skein slopes
      by the hyperbolic Mobius action of A_1 — infinite order,
      irrational fixed points, does not preserve the complexity
      grading; Sym inherits both defects; no skein-side finite-order
      graded W exists;
  (c) THE ELLIPTIC-vs-PARABOLIC CUSP OBSTRUCTION: the order-10
      elliptic lift centralizes no parabolic, hence preserves no
      single cusp's q-filtration.
E4 says NOTHING about depth gradings or other infinite-order
operators — applied only within (a)-(c).

## II. THE CLASS LIST, DERIVED FROM THE SEALED UNIVERSE

Design axes (every construction in the sealed universe is a choice on
each): OPERATOR SOURCE O0 none | O2 fixed-through-a-finite-group (all
banked modular/being-side operators: S,T/modular data, sigma(A_1)
order 10, the full SL(2,Z/15) with both CRT factors, 2I x Z/3,
Tube(Fib) — the banked principle "measurement is passage through the
finite", LAW_MAP row 83, B640/B644) | O3 the geometric infinite-order
action (the hyperbolic weld on slopes — the ONLY banked non-finite
action) | O4 grade-growing word family (letters from the inventory);
MODULE SOURCE M1 finite-data | M2 flat graded (modular / vvmf-module /
skein) | M3 Sym/Fock lift | M4 being-end integral modules (cubic
Z[omega], cusp lattice Z[2*sqrt(-3)], sum-rule-normalized); OUTPUT
R1 trace/character | R2 non-character (matrix element / contraction);
GRADING G1 periodic/ladder | G2 flat integer | G3 partition-like
(Sym) | G4 depth (grade n = n operations).

C1 — THE SEVEN BANKED TRACE CANDIDATES (M1 x R1; the exact scope of
     E1's list).
C2 — PERIODIC/LADDER-GRADED CONSTRUCTIONS (G1; any stream drawn from
     Z(kappa)/certificate-periodic data, incl. Gauss-sum streams
     indexed by rungs).
C3 — FLAT GRADED CHARACTERS (M2 x R1, any in-universe operator; incl.
     cusp-q-graded variants).
C4 — SKEIN-SIDE EXPONENTIATED CONSTRUCTIONS (O3 x M2/M3: Sym/Fock of
     the skein module under the weld).
C5 — FIXED FINITE-ORDER TWISTED CHARACTERS ON EXPONENTIATED INTEGRAL
     OBJECTS (O2 x M3/M4 x R1: the Molien class — ANY finite-order
     operator from EITHER end, both CRT factors, cubic/boundary-
     derived finite operators, the identity (untwisted) included; any
     integral graded module, being-end modules included).
C6 — C5 WITH FIXED DRESSINGS/NORMALIZATIONS (the sum-rule constant,
     eta^{48/5} powers, any fixed constant or fixed banked series).
C7 — THE DEPTH-GRADED S-CONJUGATION FAMILY (O4 x M3 x R2 x G4; the
     named candidate): grade n carries n levels of S-conjugation,
     5^{-1/2} per S-application (the golden S-normalization);
     presentations: iterated S-conjugation; matrix elements of
     Sym^n of an S-built operator (entries = degree-n monomials in
     1/D-weighted entries); level-tower/profinite Gauss-sum
     accumulation (LAW-O's t = Gamma(3k)/(3*sqrt(det B_w)) as the
     S-normalization's certificate face). Explicitly NOT the periodic
     arithmetic ladder.
C8 — DEPTH-GRADED FAMILIES IN NON-S LETTERS (O4 with letters: T /
     congruence words at level 15 (both CRT factors), cubic Z[omega]
     constants, the 13-denominator sum-rule constant).

OUT-OF-UNIVERSE BY STATEMENT (fences, flagged loudly — not classes):
F1 — MODULE-COEFFICIENT READOUT: any construction reaching the target
     arithmetic through the vvmf function realization reads F1, F2's
     own q-coefficients — excluded by the sealed circularity rule
     ("RR is not an input anywhere", PREREG_W2) and vacuous as
     generation (cannot fail — MB12).
F2 — GRADE-GROWING FRACTIONAL-ETA TOWERS (eta^{a_n}, a_n growing):
     the only banked fractional-eta object is the FIXED dressing
     eta^{48/5} (inside C6); no banked level-indexed fractional
     multiplier family exists. FLAG: this is a genuine universe
     boundary — if the universe is ever extended by such a family,
     this class requires its own adjudication; it is NOT killed by
     any of the four exclusions.

COMPLETENESS ARGUMENT. (1) Operator axis: every banked operator is
O0/O2 (passage-through-the-finite, two banked instances), O3 (the
unique banked non-finite action), or O4 — exhaustive by the inventory.
(2) The arithmetic dichotomy closes the sweep: the output's
accumulated S-normalization count is either bounded in the grade —
then coefficients live in a fixed ring with v5 bounded (O0/O2
characters are outright algebraic integers — eigenvalues of
finite-order operators are roots of unity regardless of entry
arithmetic, so a character can NEVER carry the S-normalization; non-S
depth letters contribute v5 = 0 each, FACT 2; fixed constants shift
v5 by a constant, FACT 3) and the construction falls in C1/C2/C3/C5/
C6/C8, all v5-blocked against FACT 1 unless already structurally dead
(C3 by E4a/c, C4 by E4b, C2 by E2, C1 by E1) — or the count GROWS
with the grade, and the only banked producers of 5-half-power
arithmetic are the S-normalization and its Gauss-sum certificate
face: that construction IS C7 by definition, in any presentation.
Non-integral realizations that shortcut to growing v5 without
S-accumulation all read the targets' own coefficients (F1) or need an
unbanked multiplier family (F2) — fenced by statement, not silently.
So every O x M x R x G combination lands in C1-C8, F1, or F2.

## III. PER-CLASS ADJUDICATION (one line per verdict)

| # | class | verdict | exact reason |
|---|-------|---------|--------------|
| C1 | the seven banked trace candidates | KILLED-BY-E1 | each of the seven killed by its own banked exact computation (first mismatch / identical vanishing / support no-go); E1 applied to nothing else |
| C2 | periodic/ladder-graded constructions | KILLED-BY-E2 | melody theorem: eventually-periodic => finitely many values => bounded v5 and bounded size; targets: v5 -> 146 in-window (FACT 1) + partition-like dressed growth |
| C3 | flat graded characters | KILLED-BY-E4(a)+(c) | W-stable flat gradings bounded/linear — cannot carry partition-like coefficients; cusp-q variants not W-stable (elliptic lift centralizes no parabolic); [in-universe operators are finite-order on the modular side, so E3 also covers the arithmetic — double coverage noted, E4 is the primary structural kill] |
| C4 | skein-side exponentiated constructions | KILLED-BY-E4(b) | the weld is hyperbolic Mobius on slopes: infinite order, grading not preserved, Sym inherits both defects — no graded W exists to build with |
| C5 | fixed finite-order characters on exponentiated integral objects | KILLED-BY-E3 | the two-line theorem: coefficients are algebraic integers (any operator, any end, both CRT factors — ADDENDUM_1 reach, level-15 witness computed) vs the targets' growing v5 (FACT 1); instance 2 decided at n <= 1 |
| C6 | C5 with fixed dressings/normalizations | KILLED-BY-E3 | point 3: fixed constants/series have fixed v5 shift (FACT 3); cannot bridge a gap growing 1 -> 146; the eta^{48/5} dressed view was computed inside kill #8 |
| C7 | THE DEPTH-GRADED S-CONJUGATION FAMILY | SURVIVES | E1: not one of the seven (grade-growing operator family, non-trace output). E2: not the ladder and not eventually periodic (its v5 grows by design; periodic => bounded v5). E3: every hypothesis fails by construction — no FIXED operator (the word grows with grade), no character output (matrix element/contraction — a character of a finite-order operator could never carry 5^{-1/2}), coefficient ring non-integral BY DESIGN (5^{-1/2} per S; ADDENDUM_1: only non-finite-order structure such as grade-growing S-depth exits the killed class); arithmetic fingerprint matches: targets' v5 linear, secants in [1.205, 1.25] (FACT 1). E4: none of its three theorems addresses a depth grading — not flat (E4a), not the skein weld (E4b), not a cusp q-filtration (E4c); whether a grade-compatible depth tower EXISTS is the open design question, not a banked obstruction. Named failure modes for the design cycle (MB12): collapse to a per-grade finite-order character => E3 fires; collapse to F-coefficient readout => fence F1 (circularity); no well-defined tower => structural design kill |
| C8 | depth-graded families in non-S letters | KILLED-BY-E3 (mechanism re-instantiated, computed) | every non-S letter is 5-integral: roots of unity (units), Z[omega] with 5 inert (x^2+x+1 irreducible mod 5 — computed), the sum-rule constant's denominator 13 coprime to 5 (computed); v5 = 0 at EVERY grade regardless of depth vs targets' v5 = 1 at n = 1 growing to 146 (FACT 1+2); honesty flag: this is E3's ring-level clause extended one computed step (algebraic-integer -> v5-bounded-below), discriminating fact computed in-cell, not asserted |

Fences (adjudicated as out of scope, not as survivors):
F1 OUT-OF-UNIVERSE-BY-STATEMENT (the sealed RR-not-an-input rule; vacuous as generation).
F2 OUT-OF-UNIVERSE-BY-STATEMENT (no banked level-indexed fractional multiplier family; FLAGGED as a universe boundary that would need adjudication under any extension).

## IV. VERDICT (sealed vocabulary)

**SOLE-SURVIVOR(the depth-graded S-conjugation family, C7).**

Every other in-universe class is killed by a named exclusion applied
strictly within its proven hypotheses, with the discriminating
arithmetic computed in this cell where the banked record did not
already contain it. MULTIPLE-SURVIVORS was reachable: C8's three
letter-families (T/congruence, cubic, sum-rule) would each have
survived had any letter carried a 5-half-power — the in-cell
computation (FACT 2) is what closed them, not fatigue. NO-SURVIVOR
was reachable: C7 would have died had E3's hypotheses covered
grade-growing operator words or had the targets' v5 been bounded
(FACT 1 could have come out bounded). Per the sealed outcomes, C7
receives exactly one sealed design cycle (both seats, the W2 gate
discipline) — contingent on the two-seat gate: exact agreement of
this list and these verdicts with the other seat's independent
enumeration.
