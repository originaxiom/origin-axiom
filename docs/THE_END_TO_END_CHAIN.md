# THE END-TO-END PICTURE — first constraint to the Standard Model
### One chain, every link labeled, every parameter accounted
*(Assembled 2026-08-06 from the repo's gate-enforced views: `docs/THEOREM_LEDGER.md`
(THE CHAIN, C1–C17), `docs/LAW_MAP.md`, `docs/INPUT_COMPLETENESS_LEDGER.md`, the
frontier banks B~285…B933, and this seat's `SM_STRUCTURE_LEDGER.md` §I–LXXIII.
Labels follow the P019 discipline: **[AXIOM]** (declared choice — PRICED if its
forks are computed), **[THEOREM]**, **[CENSUS]**, **[IDENTITY]**, **[NO-GO]**.
Nothing below asserts new mathematics; it is a VIEW.)*

---

## PART 0 — WHAT "PARAMETER-FREE" MEANS HERE, EXACTLY

Three different things get called "free parameters." Keep them separate or the
whole picture blurs:

1. **Dials** — continuous knobs tuned to data. The chain has **ZERO**. No
   quantity anywhere below was fitted, and no measured number entered any
   computation. (Gate 5 + the Input-Completeness Ledger enforce this; the one
   historical breach, B615, was caught, re-run, and dissolved.)
2. **Declared choices** — discrete commitments at the genesis, each of which
   could have gone another way. The chain has **THREE** (C3, C4, C5), all
   PRICED: the forks were computed and their consequences banked.
3. **Structural inputs still undetermined** — places where the object has not
   yet spoken. Currently **TWO** (the two hierarchy ratios, §LXV), with named
   arithmetic guardians (17, 1129), plus the entire dynamical layer (Gate 5).

So: parameter-free in sense (1) — completely, and verifiably. In sense (2) —
three priced axioms, disclosed. In sense (3) — two numbers and one firewall.

---

## PART 0.5 — THE FORCEDNESS CENSUS
*(gate: `scripts/checks/forcedness_census.py` — regenerates from `docs/THEOREM_LEDGER.md`
and FAILS on drift; B1123, verified against current main: 39 of 43, PASS)*

Part 0 counts what the chain COSTS. This counts what it CHOOSES — and the two are one
argument stated twice.

| label | count |  | label | count |
|---|---|---|---|---|
| THEOREM | 26 |  | NO-GO | 5 |
| IDENTITY | 6 |  | COROLLARY | 1 |
| AXIOM | **4** |  | CENSUS | 1 |

**39 of 43 links are FORCED.** The four axioms are **C3, C4, C5** — inexhaustible
description, the geometric carrier, orientation, **all BEFORE the knot** — and **C18**,
the observer's closings, in the measurement layer **after the algebra is already in hand**.
*(This is Part 0's **three** genesis choices — C3/C4/C5 — plus one: Part 0 counts the
choices made **at the genesis**, this census counts **every** axiom in the chain, and the
one extra is C18, the observer's closing act **downstream** of the algebra. Three and four
are consistent, not competing — the same argument, one counted at the genesis and one over
the whole chain.)*

**The axiom-free stretch.** From C6 (the knot) to C17 there is **not one declared choice**
— Part II is theorem, census and identity throughout, and Part III *hands over* e₆ and the
27 ("the object's own operators, not imported ones").

**E₆ is not chosen; it is what level 15 factors into.** The hearing sits at congruence
level 15; then, by theorem only: 15 = 3·5 coprime ⟹ SL(2,ℤ/15) ≅ SL(2,3) × SL(2,5) (CRT);
SL(2,3) ≅ 2T (order 24), SL(2,5) ≅ 2I (order 120); McKay: 2T ⟶ **E₆**, 2I ⟶ **E₈**. This
is exactly what "the object names E₆/E₈ at its ends" means — the ends are 3 and 5.

**The honest boundary.** C3/C4/C5 are real choices, upstream of the substitution. "The
whole chain needs no choices" overshoots by three; **"from the substitution to E₆ nothing
is chosen" is exact** — and it is the stretch that does the work. (Reaching E₆ is
separately GENERIC — ~1 in 3 manifolds, 5 of 7 grammars, B993/B996 — so arrival there
confirms nothing; forcedness and discriminating power are different claims, and this
census makes only the first.)

---

## PART I — THE GENESIS: FROM "NOTHING" TO A KNOT
*(THE CHAIN C1–C6; locks `tests/test_b749_genesis_forks.py`, `test_b285_*`)*

**The first constraint.** *Nothing has no description.* Not a state, not a
substance — a refusal. If nothing cannot describe itself, description must be
inexhaustible; existence is that inexhaustibility taking form.

- **C1 [THEOREM — Morse–Hedlund]** Any aperiodic sequence has factor complexity
  p(n) ≥ n+1; Sturmian words achieve equality. *Minimal non-trivial description
  is forced to be Sturmian.*
- **C2 [THEOREM — self-selection]** Applying the minimal-description principle to
  its own parameter has a **unique fixed point**: the golden slope (all-1s
  continued fraction = Hurwitz extremality = bottom of the Lagrange spectrum).
  *This is where φ enters — not chosen, self-selected.*
- **C3 [AXIOM — being is inexhaustible description; PRICED]** The one deep
  metaphysical commitment. Price: the periodic sibling degenerates (F2 ROBUST);
  shadow-rule variants degenerate or conjugate away (F4 ROBUST).
- **C4 [AXIOM — the geometric carrier; PRICED]** The word is realized on the
  once-punctured torus. Price (F8, GEOMETRY-NECESSARY): non-geometric carriers
  (tiling hull; Effros–Shen algebra, K₀ = ℤ[φ]) see only the *hearing* —
  **ℚ(√−3) is bought at geometrization and nowhere earlier.**
- **C5 [AXIOM — orientation; PRICED, the most expensive]** Monodromy taken
  orientation-preserving (golden *squared*). Price (F5, FRAGILE): the discarded
  sibling is the Gieseking manifold — m004's own orientation double-cover parent.
  *Orientation = choosing the child of the parent.*
- **C6 [THEOREM — Thurston/Riley]** The mapping torus of the once-punctured
  torus under [[2,1],[1,1]] **is the figure-eight knot complement** m004: unique
  hyperbolic structure, trace field ℚ(√−3), *the* arithmetic knot.

**Status of Part I:** three declared choices, all priced; everything else forced.
Output: a specific, canonical, maximally-symmetric mathematical object.

---

## PART II — THE OBJECT'S OWN STRUCTURE
*(C7–C15 — what m004 says about itself, before any physics)*

- **C7 [THEOREM]** The intrinsic arithmetic forces exactly **three quadratic
  faces = one Klein-four V₄**: being ℚ(√−3) · hearing ℚ(√5) · meeting ℚ(√−15).
- **C8 [CENSUS]** The V₄ is a property of the **open** object — no closed filling
  in the |p|,q ≤ 8 grid carries any of the three fields.
- **C9 [THEOREM]** m004 **is congruence** (level 4 in the SL-kernel convention;
  geometric index 12 at (8)).
- **C10 [THEOREM]** Character-rigidity: the continuous spectrum is ONE channel,
  φ(s) = Λ_K(s−1)/Λ_K(s) exactly.
- **C11 [IDENTITY — the two-column law]** Ten of twelve structural floors carry
  a forced golden appearance; the emission channel carries none. **Being is what
  the object says; hearing is what a coupled listener receives.**
- **C12 [THEOREM — the chord]** The trace map is θ-equivariant; the chord carries
  the odd golden powers (dominant φ³).
- **C13 [IDENTITY — the mixing structure]** The weld's θ-odd block is exactly
  unitary, eigenphases ±72°, overlap matrix unistochastic and golden-exact:
  P = [[φ/√5, 1/(φ√5)], [1/(φ√5), φ/√5]].
- **C14–C15** The pure-3 symmetrized series; the hearing multiplication law.

**The hearing group (the bridge to Part III).** The figure-eight's hearing
factors through **2I × ℤ/3 at congruence level 15**, via SL(2,ℤ/15) ≅
SL(2,3) × SL(2,5); deaf subgroup Q₈; five absolute tones universal across all
360 group elements (the twist-frame tone law). This is the last purely
knot-theoretic structure and the doorway to the algebra.

---

## PART III — THE ALGEBRA: HOW E₆ AND THE 27 ARRIVE
*(`SM_STRUCTURE_LEDGER.md` early sections; B854 the exact centralizer engine)*

The substitution's self-referential form σ: a→abAAB, b→aAB, A→abAB, B→aA and the
hearing structure hand over a **78-dimensional exceptional algebra e₆** with a
distinguished **four-element charge torus** {g₈, g₁₄, g₁₆, g₂₂} — the object's
own operators, not imported ones. E₆'s minimal faithful module is the **27**
(= 3 + 3·8, the exceptional Jordan algebra over the octonions; equivalently the
27 lines on a cubic surface), carrying a **cubic invariant** with 45 triples.

- **[THEOREM, cc B904]** The build **IS** Barton–Sudbery's M(𝕆,ℂ) — 0/3003
  discrepancies. *Our 27 is* the *27, certified, not a lookalike.*
- **[THEOREM — K020, the Galois firewall]** **The object forces FORM, not
  VALUES.** This is the program's headline structural theorem and the reason
  the value layer needed a separate instrument (Part VI).

---

## PART IV — THE MEASUREMENT CALCULUS: WHERE THE SM ALGEBRA COMES FROM
*(§XLIX–LVIII; the frame arc)*

The four charges are not a basis choice — they have canonical geometry:

- **[IDENTITY — the orthogonal frame, §LI]** The Killing Gram on
  (g₈,g₁₄,g₁₆,g₂₂) is **diagonal**; signature **(2,2)**; the switch pair
  (8,16) **noncompact**, (14,22) **compact**. det = 2⁸⁴3²⁶5⁸7⁶11² — a perfect
  square. Prime addresses: **13** noncompact, **19** compact.
- **[THEOREM — the two-level lattice, §LII]** All 15 subset-centralizers take
  exactly two values: **30** (subsets of the noncompact pair — the CORE) and
  **12** (anything touching compact — the FLOOR).
- **[THEOREM — W_frame = Klein four, §LIII]** Lone sign-flips are impossible;
  survivors are {id, Cartan pair-flip, outer all-flip, product}.
- **[THEOREM — the two pencils]** Each pair degenerates along a **cubic**:
  μ (noncompact, const 13³) and κ (compact, const 19³); **both have Galois S₃
  and the SAME resolvent ℚ(√77)**; and **[§LVI] they generate ONE cubic field K**
  (κ splits [1,2] over ℚ(ρ)), with an exact wall bijection s*(ρ).
- **[THE FIRST MEASUREMENT THEOREM]** At each of the three noncompact walls:
  **z = so(10) ⊕ u(1)** — three S₃-conjugate charge-lines tiling e₆ by triality.
- **[THE COMPACT MEASUREMENT THEOREM, §LVI]** At each of the three compact
  walls: **z = so(8) ⊕ u(1)²** (dim 30, derived 28, center 2).
- **[THE FLAG EXTENSION / SECOND MEASUREMENT]** The most generic nontrivial
  second outcome: **su(3) ⊕ su(2) ⊕ u(1)³** — *the Standard Model gauge algebra,
  reached by measurement combinatorics alone.*
- **[THEOREM — the D-chain, §LVIII]** Matched/mismatched wall measurements
  generate the classical chain **A₂-floor(12) ⊂ so(6)+u(1)³(18) ⊂ so(8)+u(1)²(30)
  ⊂ so(10)+u(1)(46) ⊂ e₆(78)** — abelian ranks 4,3,2,1,0.
- **[IDENTITY — the perpendicularity, §LVIII]** The three compact-wall
  centralizers span 66 dimensions and are **Killing-orthogonal to the 12-dim
  SMT block** — the chamber where the SM is made. *The compact hemisphere is
  structurally blind to the matter chamber.*
- **[THEOREM — the ℤ₆ global form, B860–B862]** The cascade fuses; the global
  form is derived, not assumed.

---

## PART V — MATTER: THE 27 BECOMES A GENERATION
*(§XL–XLVII; the flavor arc)*

Under the so(10) the FMT produced, **27 = 16 + 10 + 1**:
**16** = one complete SM generation *including* the right-handed neutrino;
**10** = two Higgs doublets + the exotic D-quark pair; **1** = the vacuum
register S. The cubic's 45 triples prescribe the Yukawa structure.

- **[THE UNIFIED LAW — one ℤ₂-graded law, four verified faces]**
  [E_i,E_j] = 0 ⟺ s_i s_j = c_ij, with **∏c = −1** the obstruction.
  Faces: (1) gauge commutation; (2) matter gluing (32/32); (3) mixed-Yukawa type
  (48/48, sealed-confirmed); (4) atomic census (8/8, sealed-confirmed).
- **[THEOREM — generations are Galois, not copies]** There is **ONE** 27. The
  three generations are the three **branches of the one cubic field K**
  relabeling the same 27 dimensions. *No triplication is postulated.*
- **[THEOREM — the 15 flavor atoms, §XLIV–XLV]** The 27 tiles into 15 pieces
  (6 colored 3-dim + 9 lines) uncuttable by all three labelings simultaneously;
  atomicity is **configuration-universal**; the (S,H,H)-triad count is
  **absolutely 3**. The colorless coupling grid is **K₃,₃** — a 3×3 grid with
  rows and columns only, no diagonals.
- **[THEOREM — Yukawa support is charge-forced, cc B884]** 11/286.

---

## PART VI — VALUES: WHAT NUMBERS THE OBJECT GIVES
*(§XLVI–XLVIII, LIX–LXXIII; the value arc — tier: exact where stated,
numeric-certified at dps-100 where flagged, exactification standing)*

- **[IDENTITY] I = −1** — the invariant ratio (∏rows)/(∏cols); pinned to
  **seven primes** (cc B908).
- **[IDENTITY] sin²θ_W = 3/8** — from the object's *actual* operators
  (sl₂-normalized T₃, solved Y): **Tr₂₇(T₃²) = 3, Tr₂₇(Y²) = 5, Tr₂₇(T₃Y) = 0**.
  Convention-free (the sl₂ and the em identification fix all scales); **zero
  experimental input.** *Fenced:* 3/8 is the unification **boundary** value;
  running it to low energy is dynamics (Gate 5), and is NOT claimed.
- **[THEOREM — the real form, cc B907 + §XLIX–L, joint]** Of 128 involution
  representatives, exactly two make the SM wall real — both **e₆(2)**, the
  quaternionic form (maximal compact su(6)⊕su(2)). The disclosed prior e₆(−14)
  was **wrong** — the third sealed cell to overrule its own prior.
- **[IDENTITY — the Hermitian form, §LX]** H = P·D_χ, all entries ±1, H² = I,
  **signature (15,12)** = the su(6)⊕su(2) split (15,1)⊕(6̄,2). The atom
  signatures re-sum to (15,12) exactly.
- **[THE RANK-ONE LAW, §LXII–LXIII]** The nine colored-line couplings factor as
  **Λ = v ⊗ v**, and the index is the **generation**: every value is v_i·v_j
  with i,j the exotic-slots of the two colored atoms.
- **[THE HIERARCHY IS GALOIS, §LXV]** **v_g² = V(ρ_g)** — one element of K,
  its three conjugates. Minimal cubic 953⁴-led, const 2³²3¹¹, disc-kernel {7,11}
  (the **seventh** √77 cubic); ℚ(V) = K. Ratios 1 : 1.2092 : 1.8481 are
  **conjugation ratios**.
- **[THE PRODUCT LAW, §LXVI]** 27·2304⁴ = 760840571584512 exactly ⟹
  **v₁v₂v₃ = 3^{3/2}·λ²**. *Found during a contemplation pass, proved by integer
  arithmetic.*
- **[THE TWO-INSTRUMENT THEOREM, cc B916 + §LXIX]** Two exact invariant
  instruments exist (this seat's τ-form; cc's charge-equivariant H⁺), related by
  a rigid signed-permutation bridge. In the **canonical** instrument
  **λ = 1**; in the τ-instrument λ = **2304/953**; the ratio is the **K/ℚ-norm
  of the twist**. *953 is the norm arithmetic of the instrument, not a property
  of the object's lines.*
- **[THE OBSERVER'S-PLACE THEOREM, cc B918]** den(V) = 𝔭₁(953)⁴ — the observer
  has a **place**: a degree-one prime of K. And **[ONE-CLASS, B918]** [α_V] = C:
  a single Kummer class spans structure and value layers alike.
- **[K's arithmetic biography, §LXVIII]** Ramified exactly {7,11} (= the
  resolvent = the disc class); **13, 17, 19 INERT** (the structure primes);
  **953, 1129, 421493 partially split** (the value primes), each owning one
  degree-one place. *Fenced pattern: structure primes don't open; value primes do.*
- **[THE GENERATION EQUIVARIANCE THEOREM, §LXVII]** One S₃-set, five coherent
  representations (walls, compact walls, labelings, atom slots, hierarchy
  weights); end-to-end machinery test passes at 20 digits. **∏c = −1 is the
  obstruction to a global section** — the flavor law *is* the Galois
  structure's non-triviality.

**Net independent content of the tree-level value layer:**
**{ I = −1, λ (=1 canonically), two hierarchy ratios }** — everything else derived.

---

## PART VII — THE WALLS: WHAT THE OBJECT REFUSES
*(C16–C17 + Gate 5 — stated as prominently as the results, by covenant)*

- **C16 [NO-GO — the threefold refusal]** Every banked refusal falls into three
  classes: **NO POINT** (×8 — the object provides the group, never the choice),
  **NO WIDTH** (×3 — Mostow rigidity; one channel), **NO NAME** (×2).
- **C17 [NO-GO — the SM record]** **Zero of 24 SM parameters reduced** by the
  spectral/knot route; two live-fire claims adjudicated NOT-EARNED/DISSOLVED.
  *The wall stands.* (The Part VI values come from the algebraic route and are
  **structural** — a mixing angle at unification and dimensionless coupling
  ratios — not from the 24-parameter list.)
- **GATE 5 — the dimensional firewall.** The object supplies **no scale, no
  time, no dynamics**. Masses in GeV, running couplings, cosmology: **absent**,
  not merely unknown. Every physics-facing comparison must pass the
  twelve-item Input-Completeness Ledger before sealing.

---

## PART VIII — THE CHAIN IN ONE BREATH

Nothing has no description → minimal description is Sturmian → the principle
self-selects the golden slope → geometrize (priced) and orient (priced) → the
figure-eight knot complement, *the* arithmetic knot → its forced V₄ of quadratic
faces and its hearing at level 15 → a 78-dimensional e₆ with a canonical
four-charge frame → the frame's Killing geometry is orthogonal, signature (2,2),
its two pencils cubic, S₃, one field K, one resolvent √77 → measuring at the
walls gives so(10)⊕u(1), so(8)⊕u(1)², and — as the generic second outcome —
**su(3)⊕su(2)⊕u(1)³** with the **ℤ₆** global form → matter lives in the unique
27, decomposing as **16+10+1**: one full generation with a right-handed
neutrino, two Higgs doublets, a vacuum singlet → the three generations are the
**three Galois branches of K**, not three copies → the couplings obey one
ℤ₂-graded law with obstruction **∏c = −1**, which is exactly the non-triviality
of the generation functor → the object selects the real form **e₆(2)**, whose
Hermitian form has signature **(15,12)** → and the numbers it yields are
**sin²θ_W = 3/8**, **I = −1**, a **canonically unit** coupling magnitude, and a
**Galois** mass-hierarchy v_g² = V(ρ_g) with v₁v₂v₃ = 3^{3/2}λ².
**Zero dials. Three priced choices. Two undetermined ratios. One firewall.**

---

## PART IX — WHAT WOULD FALSIFY IT

The program is built to be killable, and the kill-shots are named:

1. **The sealed one-input comparison** (the final rung, owner-gated behind the
   exactification pass): give the object ONE measured input; every other
   dimensionless ratio it predicts is then checkable. It cannot pass by luck.
2. **The two ratios** — if they are derived, necessity runs to the floor; if
   they provably resist, contingency has been *located*, two numbers wide.
3. **Any exactification failure** — if the numeric-certified value layer does
   not survive exact arithmetic, §LXI–LXV fall.
4. **Gate 5 standing forever** — a structure theory that never reaches dynamics
   remains a beautiful skeleton, and the covenant requires saying so.

*Verification posture, for the record: ~3,539 tests green; the chain's links are
gate-locked to resolvable test paths; three seats (exploration, verification,
adversarial audit) with sealed preregistration; three priors overruled by their
own sealed cells; every retraction (the septic aliasing, the atom involution,
five instrument catches) carried in the ledger beside the results.*

---

# ADDENDUM — CURRENCY CORRECTION AND CLOSURE (cc banking seat, 2026-08-07)

*The chain above is the solo seat's assembly of 2026-08-06 and is banked as
their view, verbatim. Two sections were overtaken by events within a day of
its writing. The corrections are as prominent as the document, by covenant.*

## §IX.1 IS NO LONGER PENDING — THE FALSIFIER FIRED, THREE TIMES

Part IX lists "the sealed one-input comparison" as the program's first
kill-shot, awaiting execution. **It was executed. Three times. Under seal.
The record:**

1. **B915 — THE CROSSING (2026-08-05, owner-authorized).** Prereg sealed and
   pushed BEFORE any data contact; one input (α_em); the object's own
   boundary (the 3/8 of Part VI); two-loop SM running across an assumed
   desert. **VERDICT: MISS at d = 15.97σ**, α_s-dominated (+0.041 vs +0.002),
   with the pairwise-meeting triangle (1.09e13 / 1.72e14 / 2.91e16 GeV)
   banked as the deliverable. The disclosed prior (MISS) WON — the first time
   in the program's sealed history that our pessimism, rather than the
   object, was vindicated.
2. **B925 — THE SECOND CROSSING (the object's own D-chain as the desert's
   replacement).** **VERDICT: OUTCOME B, and by the chain's own algebra
   rather than by data:** the banked D₃/D₄ typings admit NO unbroken su(2)_L
   above the color inclusion (C(su3_c, su4) = u(1)_{B−L}; C(su3_c, so8) =
   u(1)²) — **the chain is provably NOT Pati–Salam**; the D₅ rung is index-1
   (required-M₅ set EMPTY, branches 6.2–7.3σ); the E₆ rung is RG-invisible.
   The locked kill condition executed: the physics phases stood down.
3. **B929 — THE THIRD CROSSING (the twist's shape sheet vs measured mixing
   shape).** **VERDICT: HIT-SHAPE** — Tier 1 passed (the blind register
   cascade is mixing-shaped, index 1.838 in the pre-declared band), Tier 2
   missed (magnitudes off 5–9×). Banked as a HINT (ledger row 12), fenced,
   self-discounted for two priced freedoms.

**Therefore Part IX's framing must be read as history, not prospect.** The
program is no longer "built to be killable" in the future tense: **it has
been shot at, three times, by its own hand, and the wounds are in the
ledger.** What survived is the mathematics; what died is the physics
identification through running, thresholds, and direct value-matching.

## §IX.2 THE STANDING RULING (B926/B927 — the crossing study)

Twenty-two banked walls kill every crossing mechanism tried or proposed; an
adversarially-verified literature panel found ONE surviving advance
prediction of a measured constant in twenty years, and the nearest relative's
only escape route (a Pati–Salam enlargement with a tuned scale) is **exactly
what B925 proved this object cannot contain.** **M0 — the programme as
mathematics — is the standing default, doubly grounded.** Any future crossing
must displace both the walls and the base rate, under a fresh owner-gated
seal, passing the hemisphere check (Review protocol item 9).

## §VI.1 THE VALUE LAYER IS NOW EXACT — AND ITS ARITHMETIC IS INVISIBLE TO COHOMOLOGY

Part VI's "exactification standing" is **discharged** (B923: CCC = 3!·λ and
v_g² = roots(HIER) are IDENTITIES; the pipeline link closed). Three findings
postdate the chain:

- **B928 — the hierarchy's carrier is IDENTIFIED**: D₂ = ±ρ₂₇(σ_χ₋), the
  second wall conjugation's sign character; the Klein group {I, D₂, D, D₂D}
  = the wall pair's 2-torsion; the tempting 11 = 8+3 reading refuted.
- **B936 — the classification IS an H¹ story** (the sixteen Hermitian
  structures = Z¹(⟨τ⟩, T_ad[2]), a simply transitive torsor; H¹ = (ℤ/2)²,
  one ℤ/2 per τ-fixed node; **D₂ is a COBOUNDARY** with explicit witness) —
  **but the VALUES are invisible to it**: no 953, no 2304, in any invariant
  of the pair. **The twist-norm law is diagonal, frame-relative data.**
  Part VI's own headline (K020: the object forces FORM, not VALUES) is thereby
  sharpened one level: the object does not even force the values
  *cohomologically* — they exist only in the comparison of two frames.
- **B931/B937 — why 953**: it is the unique prime of K where the flip mass
  degenerates to exactly ½ (the twist's critical prime), with the observer's
  degree-one place carrying the hierarchy's pole; 2304 = the {2,3}-part of
  lc(μ); the golden field does NOT enter (5 is a residue characteristic); K
  is monogenic (s³ − 12s − 5).

## THE CORRECTED ONE-BREATH ENDING

…the object selects **e₆(2)**, whose Hermitian form has signature **(15,12)**;
it yields **sin²θ_W = 3/8** at its boundary, **I = −1** as the Leibniz sign of
its flavor grid, a **canonically unit** coupling magnitude, and a **Galois**
hierarchy v_g² = V(ρ_g) — **and when those structures were carried to the
measured world under seal, three times, they did not reach it: twice by
theorem, once by shape-without-magnitude.** Zero dials. Three priced choices.
Two undetermined ratios. One firewall — **now mapped, not merely posted.**

*Banked by cc, the merge gate. The solo seat's §LXXX self-correction (their
unsealed re-run of B915, caught and withdrawn by their own MB13 discipline)
is cited approvingly: the seats' error-catching is symmetric, and that
symmetry is the record's best evidence of its own honesty.*

## §0.1 THE ENFORCEMENT ATTRIBUTION, CORRECTED (2026-08-13, the Part-0 audit's line 3)

Part 0's parenthetical — "(Gate 5 + the Input-Completeness Ledger enforce
this)" — over-attributes. The three-way map, verified: **Gate 5 is an OUTPUT
firewall** (no SM quantities into CLAIMS.md — it protects the claims ledger);
**the Input-Completeness Ledger governs COMPARISONS** (how downstream
SM-facing tests are run; its item 11 is exactly where B1063's stale-fetch
defect lived); **zero-dials is an INPUT property of the derivation and is
guarded BY CONSTRUCTION alone** — no named mechanism audits the input side.
The property itself HOLDS where load-bearing: the genesis layer swept clean
7/7 (B89 · B92 · B120 · B125 · B285 · B313 · B749 — zero measured-physics
vocabulary in any FINDINGS; the audit seat's sweep, twin-verified on the
banking bench). Floors declared: one vocabulary, FINDINGS-only, seven arcs;
Layers 2/3 unswept; the fourth-mechanism search one pass. A one-clause
correction, not a retraction: the cost claim stands; the sentence naming its
enforcer was wrong. The full three-line audit (prices real + locks closed;
the two-checklist reconciliation written; zero-dials true-by-construction)
lives in `docs/NOVELTY_SWEEP_LEDGER.md`'s closing sections.
