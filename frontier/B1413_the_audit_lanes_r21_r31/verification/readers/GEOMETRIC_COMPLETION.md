# R22: the completion must change more than the four-dimensional field list

## VERDICT AS THE SEAT STATES IT
"R21's anomaly-free added-field theory remains valid, but its fermions are not supplied by the unchanged source operator. The proposed negative-charge vectors emerge with the opposite chirality. Finite-norm nonparallel charged profiles do exist as trial sections; normalizability is not the obstruction. A single minimally coupled scalar condensate with no compensating current cannot keep this order-three connection flat." It states these "direct the next calculation to an actual source/defect, inflow or coupled-field completion. They do not close that route, derive the Standard Model, or establish a full physical TOE."

## DECLARED INPUTS AND HYPOTHESES
- Prescribed: "R18's strong maximal complex, R19's exact relative cochains and E6 roots, R20's order-three character, and R21's actual H representation and charge-four singlet."
- Scope (P0): "the SAME commuting signed source field, same strong maximal domains, same scalar compact holonomy and same four-dimensional chirality convention as R19."
- Sourced literature inputs: Pantev–Wijnholt (arXiv:0905.1968) §3.1/3.4 for charged degrees and defect/inflow couplings; Braun et al. (arXiv:1812.06072) eqs. (2.41)–(2.52) for the chirality dictionary, cited as "standard prior input"; Golenia–Moroianu (arXiv:math/0701780) §3.2 for cusp transverse-mode removal, with an explicit caveat "Do not transfer its smooth scalar theorem to the singular Witten operator"; Aronszajn (1957) for unique continuation, "cited, not proven by a symbolic test."
- Assumed/expected (P6): "expect a failure of the naive mode transplant... Expect nonzero finite-norm trial profiles but NOT thereby stationary Higgs solutions... Expect the single-scalar Maxwell equation to obstruct keeping a flat connection with non-real holonomy. Any contrary result is preserved."
- Seals: pre-execution seal **b8485ab5**.

## CONTROLS
- "Choosing the opposite representative of any CPT pair leaves its anomaly contribution unchanged: both the index and the representation's anomaly change sign" — a control that should reproduce the same trace values regardless of representative choice.
- "A real antiperiodic circle eigenfunction has nontrivial -1 holonomy, zero current and nonzero gradient" and "Two separate same-charge fields can have opposite currents even at the order-three holonomy... This alone is not a two-field vacuum, but shows why the single-current proof must not be extended to it" — controls bounding the scope of the Maxwell/current no-go so it cannot be over-applied.
- k=1,2,4 source-component controls testing the general-k dependence of the H1 formula, "not extrapolation from the displayed controls."
- Reporting gate: originally "26 pass / 4 fail," which "caught public branch-label tokens and missing prior-arc context," corrected to "27 pass / 3 fail... Only the three older attribution/static-vacuity/literal-provenance gate debts remain."

## TESTS ON THIS BENCH
```
18 passed in 7.90s
```
(`tests/test_physical_bridge_geometric_completion*.py`, run from `<audit worktree @ 5e063851>`). No failures.

## CLAIMS FOR MAIN
1. Applying R19's same-source charged operator to R21's added H-representation (16_1+10_-2+1_4 and CPT partner) nets 3×(16_1+10_+2+1_4), not the intended anomaly-free spectrum — COMPUTED.
2. For any finite same-source enlargement by CPT pairs, Tr u and Tr u^3 are strictly positive sums over |q|, so this class cannot self-cancel R21's anomaly — PROVED-BY-SEAT.
3. Finite-norm, nonzero charged trial sections exist on the order-three charge-four cusp line despite nonintegral holonomy — COMPUTED.
4. A single minimally-coupled current-free scalar cannot hold a flat connection with non-real (order-three) holonomy, by an exact unique-continuation argument (input cited, not proved here) — CONDITIONAL (explicitly scoped to "one minimally coupled complex scalar... no other current").

## CONFLICTS WITH MAIN
Searched main's `docs` and `frontier` for distinctive phrases ("PB-BOUNDARY", "opposite chirality", "10_-2", "GEOMETRIC_COMPLETION"). No hits identify this round or its specific claims in main's record. This is a path-local audit-lane branch not yet harvested; main's own text states it "independently read this branch only through R20 at 6f862099... not R21 or R22." NONE.

## WHAT MAIN WOULD HAVE TO VERIFY
Recompute the H1(q)/H1(-q) table and the six-variable anomaly polynomial from R21's actual weight sets (not labels); independently check the finite-norm tail-integral bounds and the Maxwell/unique-continuation argument's scope (single scalar, no other current) before citing any of this as an obstruction beyond that stated class.
