# W3 ENUMERATION — cc seat, WORKING NOTES
# (independent cell; no cc2 W3 enumeration artifact existed in the arc
# directory at the time of writing and none was read; inputs = the two
# sealed prereg documents + the banked pre-W3 record only)

Governing: PREREG_W3_DECISION.md (563a2858) + PREREG_W3_DECISION_ADDENDUM_1.md.
Gate artifact: ENUM_CC.md (this file is scratch reasoning behind it).
Computation: v5_discriminating_facts.py -> v5_discriminating_facts_out.txt
(all assertions passed; anchors and checkpoints reproduce the banked
STEP3/W33 numbers from scratch — no banked JSON was loaded).

## 1. The sealed universe, grounded in the banked record

Hearing-end inventory (PREREG_W3 body):
- S,T / modular data at the relevant stages: the golden S-matrix with
  S-normalization 5^{-1/2} per application, D^2 = 3*phi*sqrt(5)
  (W2_CLOSEOUT_CC2; the trace law / LAW-O rows of docs/LAW_MAP.md).
- Holonomy / Fox calculus: the monodromy A_1, the congruence shadow
  (B644), the canonical order-10 elliptic lift sigma(A_1) with
  tr = phi (THE GOLDEN-ROTATION LAW, LAW_MAP row; B674 route 1).
- Graded module + skein machinery: the vector-valued weight-1/5 system
  (F1,F2) over M(Gamma(5)) (PREREG_W2's V), the plain weight tower,
  the flat skein module of the once-punctured torus with multicurve
  bases (CROSSCHECK_W2_CC2 (c)).
- The level tower: the ladder Z(kappa) (melody theorem, B651/B662-G),
  the stage tower and its per-level modular data.
- Sym/Fock lifts: THE EXPONENTIATION LAW (LAW_MAP row): the design
  space of flat objects is dead and the exponentiated candidate at the
  fixed-operator level is the ONE POINT that W2 then killed.

Being-end inventory (ADDENDUM_1, named):
- The FULL level-15 congruence representation with BOTH CRT factors:
  SL(2,Z/15) = SL(2,Z/3) x SL(2,Z/5) (B640 hearing-group theorem at
  level 15; B644; ADJUDICATION_BIFOCAL_OBJECTION's computed witness in
  Q(zeta_15)).
- The cubic and its Q(sqrt-3) data: the alternating cubic, 24*zeta_6
  core law, Z[omega]-integral structure constants (B662/B647 arcs;
  CAMPAIGN_STATUS 2026-07-16 entry).
- The boundary/cusp contribution: the cusp lattice Z[2*sqrt(-3)],
  Gram [[1,0],[0,12]], conductor 4 (B672 branch-tiebreak lemma).
- The sum-rule coefficients: [c23] = -(7983360/13)*omega*[c34]
  (B671/B673, two-seat verified) — note the 13-denominator, v5 = 0.

Key structural banked fact used for completeness (operator axis):
"measurement is passage through the finite" (LAW_MAP row 83, two exact
instances B640/B644): every banked operator on the modular/being side
acts THROUGH A FINITE GROUP (congruence quotient at level 5/15,
2I x Z/3, Tube(Fib) finite-dim, sigma(A_1) order 10). The only
non-finite banked actions are the geometric/Anosov ones — the weld on
skein slopes (hyperbolic Mobius, CROSSCHECK_W2_CC2 (b)) — plus
grade-growing WORD FAMILIES (operator count grows with grade), which
is an operation-count choice, not a new operand (the ADJUDICATION's
closing paragraph).

## 2. The four exclusions — exact hypotheses (details in ENUM_CC.md)

E1 = the seven wave-1 kills, each candidate-specific and computed:
 1-4 B672 (B205 q-tower; word-length filtration; ladder certificate
 0/130 + 2-part bound; pure eta-menu mod-5 exponent obstruction);
 5-6 B677/G1 (Tube(Fib) semisimple => HH^{>=1} = 0, trace collapse;
 weld-weighted character combos: value-irrationality at n=0 + support
 classes 11/60 etc.); 7 B674 route 1 (ES twisted trace tower
 identically 0; mechanism = the golden-rotation law). E1 is a LIST of
 exact kills, not a general theorem: it covers exactly these
 candidates. (New trace candidates fall to E3's ring-level clause
 instead — finite-order => integral trace; see completeness.)

E2 = the melody theorem (B651; minimal period P = 175560 via B662/G):
 the ladder Z(kappa) is PERIODIC; its complete information content is
 one period of finite data. Hypothesis: the construction's stream is
 drawn from the ladder / is eventually periodic. Kill mechanism vs the
 targets: an eventually-periodic stream takes finitely many values =>
 bounded v5 and bounded size; the targets' v5(denom) grows 1 -> 146
 in-window (FACT 1, computed) and the dressed integer targets grow
 partition-like (3402 by n = 40, banked).

E3 = the 5-adic exclusion (LAW_MAP row 27; instance 1 = W33 ladder,
 instance 2 = W2 Molien kill, decided at n <= 1). Exact hypotheses:
 (a) the output is a twisted character / Molien series of a FIXED
 finite-order operator on a graded object with integer multiplicities
 => every coefficient is a Z-combination of roots of unity = an
 algebraic INTEGER (the two-line theorem, ADJUDICATION); more
 generally (ring-level statement as banked) any construction whose
 coefficient ring is algebraic-integral; (b) point 3 of the kill: a
 FIXED constant has fixed v5 and cannot bridge a v5 gap that grows
 with n. Targets: v5(denom) = 1, 12, 49, 99, 146 at n = 1, 10, 40,
 80, 119 (FACT 1 reproduces this from scratch; F2 identical profile).
 REACH per ADDENDUM_1: ANY finite-order operator, ANY end(s) — both
 CRT factors included (computed witness: combined-factor Molien in
 Z[zeta_15] through q^8, denominators identically 1). E3 does NOT
 cover: non-fixed (grade-growing) operator families, non-character
 outputs, or coefficient rings that are non-integral BY CONSTRUCTION.

E4 = the W2 design theorems, exactly three, no more:
 (a) the flat-level growth kill (D1, W2_DESIGN_NOTE_GAMMA5): every
 W-stable grading on the flat Gamma(5) objects has bounded
 (total-pole-order: dim gr_n -> ~#cusps = 12) or linear (weight:
 dim M_k) graded growth — bounded/linear graded dimensions cannot
 carry partition-like coefficients; verbatim on the flat skein module
 (polynomial multicurve growth, CROSSCHECK (c)) — together THE
 EXPONENTIATION LAW.
 (b) the hyperbolic-slope obstruction (CROSSCHECK (b)): the weld acts
 on skein slopes by the hyperbolic Mobius action of A_1 — infinite
 order, irrational fixed points, does NOT preserve the complexity
 grading; Sym inherits both defects; no skein-side finite-order graded
 W exists.
 (c) the elliptic-vs-parabolic cusp obstruction (D1 first bullet): the
 order-10 elliptic lift centralizes no parabolic, hence preserves no
 single cusp's q-filtration.
 Per W2_CLOSEOUT_ADJUDICATION_CC item 3: E4 covers THESE hyperbolic
 weld actions and flat objects computed — not every conceivable
 infinite-order operator. Applied only so.

## 3. The axes decomposition (the completeness spine)

O — operator source: O0 none/identity; O2 fixed, factors through a
 finite group (ALL banked modular/being-side operators — see the
 passage-through-the-finite fact above); O3 the geometric infinite-
 order action (the hyperbolic weld on slopes; the only banked
 non-finite action); O4 grade-growing word family (operator count
 grows with grade; letters from the banked inventory).
M — module source: M1 finite-data objects (Tube(Fib), certificates,
 cohomology towers); M2 flat graded (modular / vvmf-module / skein);
 M3 Sym/Fock lifts of M2; M4 being-end integral modules (cubic
 Z[omega], cusp lattice, sum-rule-normalized).
R — output reduction: R1 trace / graded character (coefficient n =
 full trace on grade n); R2 non-character (matrix element / partial
 contraction / vector-valued readout).
G — grading: G1 periodic/ladder; G2 flat integer (weight, complexity,
 pole order, cusp-q); G3 partition-like (Sym-induced); G4 depth
 (grade n counts n operations).

THE ARITHMETIC DICHOTOMY that closes the case sweep: for any
in-universe construction, the output's per-grade accumulated
S-normalization count either (i) is bounded in the grade — then the
coefficients live in a fixed ring with v5 bounded (O0/O2 characters
are outright algebraic-integral by the two-line theorem; non-S depth
letters contribute v5 = 0 each, FACT 2; fixed constants/dressings
shift v5 by a constant, FACT 3 + the kill's point 3 + the dressed-view
computation inside kill #8) — killed by E3 against FACT 1's growing
v5; or (ii) GROWS with the grade — and the ONLY banked producers of
5-half-power arithmetic are the S-matrix normalization 5^{-1/2}
(W2_CLOSEOUT_CC2) and its certificate face, the quadratic Gauss sums
of LAW-O (t = Gamma(3k)/(3*sqrt(det B_w)), the mechanized trace law)
— any construction accumulating them grade-linearly is BY DEFINITION
the depth-graded S-conjugation family (C7), in any presentation
(iterated conjugation; matrix elements of Sym^n of an S-built
operator, whose entries are degree-n monomials in 1/D-weighted
entries; level-tower/profinite accumulation). Constructions that die
structurally BEFORE arithmetic: flat gradings (E4a/E4c), the skein
weld (E4b), periodic gradings (E2), the seven named trace candidates
(E1).

Why characters can never carry the S-normalization: the character of
a finite-order operator is a sum of roots of unity REGARDLESS of how
non-integral the matrix entries are (eigenvalues of a finite-order
operator are roots of unity). So growing v5 forces a NON-character
output (R2) — this is why C7 is necessarily R2, and why C5's boundary
is exact.

## 4. The second-survivor hunt (candidates the close-out did not name)

Tested and dispatched (each with its exact reason):
(a) T-depth / congruence-word depth (grade n = n applications of T or
    of any SL(2,Z/15) word, both CRT factors free): every letter
    contributes a root of unity; v5 = 0 at every grade (FACT 2);
    first mismatch n = 1. KILLED (E3 ring-level mechanism,
    re-instantiated in-cell — computed, not asserted). -> C8.
(b) Sum-rule-coefficient depth (grade n = n applications of
    -(7983360/13)*omega): v13 grows, v5 = 0 (gcd(13,5) = 1, FACT 2);
    targets have PURE 5-power denominators (FACT 1). KILLED. -> C8.
(c) Cubic-constant depth (Z[omega] structure constants): 5 inert in
    Q(omega) (FACT 2) => v5 >= 0 at every grade. KILLED. -> C8.
(d) Fixed-operator matrix elements on Sym (R2 with O2): entries of
    Sym^n(W) are degree-n monomials in W's entries; if the entries
    are integral (congruence rep over Z[zeta_15]) the stream is
    integral -> E3; if the entries carry 1/D (any sigma(S)-built W)
    the accumulated S-count grows linearly with the grade -> this IS
    a PRESENTATION of C7, not a second class.
(e) Grade-growing fractional-eta towers (eta^{a_n}, a_n growing):
    the only banked fractional-eta object is the FIXED dressing
    eta^{48/5} (B672) — a fixed series, inside C6/kill #8's computed
    dressed view. No banked level-indexed fractional multiplier
    family exists. OUT-OF-UNIVERSE-BY-STATEMENT — flagged as fence
    F2 in ENUM_CC.md (a genuine universe boundary, stated loudly).
(f) Module-coefficient readout (the vvmf function realization: F1,
    F2's own q-coefficients ARE the target arithmetic; any
    construction reaching growing v5 through the function-space
    realization reads the targets' own coefficients): excluded by
    the sealed circularity rule ("RR is not an input anywhere",
    PREREG_W2) and vacuous as generation (cannot fail — MB12).
    OUT-OF-UNIVERSE-BY-STATEMENT — fence F1.
(g) Untwisted character of Sym(V) (partition-like growth, right
    size!): identity = finite-order; integer coefficients; E3
    verbatim. -> inside C5.
(h) Gauss-sum streams indexed by ladder rungs: periodic in kappa
    (melody theorem) -> E2; indexed by growing level with bounded
    S-count per term: bounded v5 -> E3; accumulated across the tower:
    C7's profinite presentation.

MULTIPLE-SURVIVORS was genuinely reachable: (a)-(c) would have
survived if any of their letters had carried a 5-half-power — the
in-cell computation (FACT 2) is what killed them, not fatigue.

## 5. Honesty flags

- E1 applied ONLY to its seven computed candidates; residual trace
  territory is closed by E3's ring-level clause (within its proven
  two-line mechanism), never by "E1 by analogy."
- E3 extended in exactly one computed step beyond its banked ring-
  level wording for C8: from "algebraic-integer ring" to "ring with
  v5 bounded below" (5-inert/5-coprime letters). The extension's
  discriminating fact is COMPUTED in-cell (FACT 2), per the
  compute-the-discriminating-fact rule; flagged as an extension.
- E4 applied strictly to its three proven theorems; the S-depth
  family's grading question is stated as OPEN, not obstructed.
- The universe fence did real work twice (F1, F2 above) — flagged in
  the gate artifact rather than silently absorbed.
- C7's named design-failure modes (so the sole-survivor verdict is
  falsifiable downstream, MB12): (i) if its design collapses to a
  per-grade finite-order character, E3 fires; (ii) if its output is
  secretly the F-coefficient readout, fence F1 fires (circularity);
  (iii) if no grade-compatible depth tower exists, it dies as a
  structural design kill in its one sealed cycle.
