# CELL H — THE FOURTH WALL, TWICE OVER: the triple-Massey layer on the
# golden double carries NO information (undefined on distinct solo
# indices; FULL indeterminacy everywhere else)
# (cell agent, 2026-07-17; campaign prereg = CAMPAIGN_PREREGISTRATION.md,
# CELL H clause; exact over K = Q(sqrt-3) throughout; zero floats)

## VERDICT (the sealed negative branch, sharpened)

The triple Massey products <u_i, u_j, u_k> on H^1(D;27) of the golden
(unbent weld) double, with the Jordan-cross coefficient system
27 x 27 -> 27bar (the E6 cubic's polarization; strictly associative by
N's total symmetry), valued in H^2(D;C) = C, distinguish NOTHING — for
two independent exact reasons, each sufficient alone:

1. **Definedness fails on the generation triple.** The cup classes
   [u_i cup u_j] in H^2(D;27bar) are NONZERO for EVERY off-diagonal
   pair meeting the solo triple {2,3,4} — in particular on all three
   solo pairs, both orders. Every <u_i,u_j,u_k> with two distinct solo
   indices (all 24 of them) is therefore UNDEFINED: the obstruction
   sits one level below the Massey product. (The full 5x5 zero/nonzero
   table: the boundary-born block {0,1} cups to zero within itself;
   the diagonal is zero (Koszul 2-torsion over K); everything else is
   nonzero. cellH_output.txt STEP 6.)

2. **The indeterminacy is everything, for every triple.** The dual cup
   pairing H^1(D;27bar) x H^1(D;27) -> H^2(D;C) is NONZERO (exact
   5x5 matrices PL, PR in STEP 8; rank(PL) = 4; Koszul PL = -PR^T
   verified). Since the target is 1-dimensional, the indeterminacy
   subgroup u_i cup H^1(27bar) + H^1(27bar) cup u_k equals ALL of
   H^2(D;C) for ALL 25 pairs (i,k) (post-analysis: 25/25 FULL). The
   only defined solo products — the three Massey cubes <u_i,u_i,u_i>,
   i in {2,3,4} — have representative scalar exactly 0 and full
   indeterminacy: <u_i,u_i,u_i> = the whole coset space, no invariant.

So at the first cochain level above the class-level walls (Koszul, D1,
B660/S4), the H^2(D;C)-valued triple-Massey layer is structurally
EMPTY on this object with these coefficients. The hierarchy question,
if it lives anywhere cochain-side, must live in (a) the VALUES of the
nonzero cup classes [u_i cup u_j] in the 5-dimensional H^2(D;27bar)
(a genuinely new nonzero invariant on the solo triple — see
by-product 1), or (b) matric/higher Massey systems in quotient
coefficient systems where the cups die, or (c) the quantum route.

## The method (all exact; degree-2 presentation route)

- Banked basis: the 5 classes rebuilt VERBATIM from b637_threeform.py's
  double_Y construction (bend None; Z^1 dim 31 = banked). DECISIVE
  BASIS CONTROL G0: Y[(0,3,4)] = 2/3·sqrt(-3) and
  Y[(1,3,4)] = 1/24 + 1/72·sqrt(-3) recomputed through the FULL banked
  T.H evaluator (stage-3 certify-peeling patch) — both EXACTLY equal
  the banked unbent table. The cellH basis IS the banked basis.
- Coefficients: 27bar = contragredient action rho(g)^{-T}; cross
  (x,y)_r = sum C_pqr x_p y_q from the rebuilt cubic (270 entries, all
  rational); gates: cross equivariance for all 8 letters, dual dot
  invariance, strict associativity dot(x cross y, z) = dot(x, y cross z)
  (this is what makes the Massey representative a cocycle: delta m =
  (u_i u_j)u_k - u_i(u_j u_k) = 0, verified numerically as well).
- Class test (both directions exact): a bar 2-cocycle c is a group
  coboundary iff its evaluation E(c) on the corrected relator bar
  2-chains (the b637 rel_chain convention, generalized to the
  4-generator amalgam presentation) lies in im(Fox map). Injectivity
  H^2(pi;M) -> H^2(presentation 2-complex;M) gives "in-image => class
  zero"; the normalized-cochain recursion a(w.l) = a(w) +
  rhobar(w)a(l) - c(w,l) (with a(X) = c(X,x) - rhobar(X)a(x)) rebuilds
  a genuine group-level primitive from any Fox solution, so "class
  zero => in-image" and the primitive is constructive. GATED by:
  E(delta f) = PHI.f_gen for synthetic normalized element-functions
  (27bar and trivial coefficients), relator-insertion invariance of
  every primitive, delta a = c on word pairs, delta m = 0 on word
  triples.
- Scalars: H^2(D;C) = C via the left-null functional phi of the
  abelianized relator matrix (rank 3, coker 1-dim; phi = the 4th
  relator's evaluation — the weld relator LONG(a,b)LONG(c,d), the only
  abelianization-zero relator).
- h^0(D;27) = h^0(D;27bar) = 1; h^1(D;27bar) = 5 (theta-duality,
  computed); Z^1(D;27bar) dim 31.

## Exact by-products (new, banked basis, all in cellH_output.txt)

1. **The 27bar cup class table** (STEP 6): the generation triple is
   CUP-COUPLED at 27bar level — [u_i cup u_j] != 0 for all i != j
   except within the boundary-born pair {0,1}. This refines Y[234] != 0
   (Y is the full contraction of these classes) and shows S4's
   v0-contracted zero cannot grant Massey definedness.
2. **The v0-mediated class matrix MV0 in the banked basis** (STEP 6 +
   post-analysis): M_ij = phi(E(dot(u_i cup u_j, v0))); exactly
   antisymmetric, rank 4, kernel 1-dimensional =
   (7560 + 10920r)u_0 + (12640320 - 8648640r)u_1 + u_4, r = sqrt(-3).
   Its SOLO BLOCK IS NOT ZERO in the banked basis (e.g. M_23 =
   2524411008000 + 2502057600000r). B660/S4's "solo block zero" is a
   statement in S4's OWN presentation basis (their honest flag "no
   basis-matched cross-check" was exactly right); the basis-invariant
   content — antisymmetric, rank 4, one kernel class — is what
   transports, and it matches cc2's banked stage-2 form.
3. **The dual cup pairing** PL[t][s] = phi([zbar_t cup u_s]) (STEP 8):
   rank 4; LEFT radical = exactly the basis class zbar_2 (it cups to
   zero with all five u's); RIGHT radical = EXACTLY THE SAME CLASS as
   ker(MV0) (the identity checked exactly in the post-analysis). One
   distinguished H^1(D;27) class is simultaneously the radical of the
   v0-mediated 2-form and of the dual cup pairing — registered as an
   exact structural identity (hint-row material).
4. **kappa (the invariant-dual contraction)**: kappa(u_i) =
   dot(v0bar, u_i(.)) is the ZERO 1-cocycle for i = 0,1,2,3 and
   (1,1,1,1) on the generators for i = 4 — only class 4 sees the
   invariant line (consistent with H130's W-support {034,124,134}, all
   containing slot 4).

## Controls and honesty

- G0 basis match (two banked Y components, exact); all coefficient-
  system gates; CONTROL A/A' (relator-chain vs Fox, 27bar + trivial);
  cup cocycle identity (3 pairs x 3 mixed-side word triples);
  primitive gates on all 5 gated pairs (relator-insertion
  well-definedness + delta a = c); delta m = 0; Koszul PL = -PR^T;
  MV0 antisymmetry. Zero floats anywhere.
- Run 1 (cellH_output_run1_controlfail.txt) aborted at CONTROL A
  because the SYNTHETIC control cochain f(w) = rhobar(w)xi was not
  normalized (f(1) != 0) while the machinery lives in the normalized
  bar complex. Fix: normalize the control functions themselves
  (f(w) = rhobar(w)xi - xi). No pipeline object was affected — every
  pipeline cochain (cups, primitives, Massey representatives) is
  normalized by construction (u(1) = 0). Both logs preserved.
- The representative-shift control found no informative defined triple
  to run on (all defined triples have full indeterminacy — the control
  is moot: the verdict facts are class-level and basis-free).
- Scope: this closes the H^2(D;C)-valued TRIPLE Massey layer with the
  Jordan-cross coefficient system on the golden double. It does NOT
  close: cup-VALUE invariants in H^2(D;27bar) (by-product 1 makes them
  the live object), matric/restricted Massey systems, higher (4-fold+)
  products in quotient systems, other bends/doubles, or the quantum
  route. Stated exactly as the prereg's negative branch requires.

## Artifacts (sha256)

- massey_first.py
  fa65bd641b1d2304895dd6ac6c86cfd10da2e97e0b175c43f6fdf5a1ab91a5b4
- cellH_output.txt (the banked run, EXIT 0)
  893831d677b4784014d5c9110360e3f99c0009bfa7ec1b33b99f3062fa0f44b8
- massey_post.py
  13b3d1108940894c3dc933e1d580d50179a621520d52a494f7abbf103be2ba2d
- cellH_post_output.txt
  f08a56f2dc56e06b8bde6ddfa9091942c57e0360164c8a6538e86428e5c4265e
- cellH_output_run1_controlfail.txt (honest record; control working)
  e04f30ed23c53e346dcf4b00017946cc7eface6bf01a6360de082c2151368483
- upstream inputs: b637_threeform.py
  713f32d8435c5581585158ab06e4096cda88019223f864da50588f8a041c9c1c;
  unbent_table.txt
  2ee6fbaecbd1645763a927949a05c524444ca20afad58ec3cd38014489f7b4fa

Repo untouched (new files only, all under cellH/). No model names.
No SM numbers (Gate 5 standing).
