# THE LISTENER-MAP SPEC — L166 (the crossing door, posed as a construction problem)

**Registered 2026-08-18** · produced by the field-masterplan's W5 cell (3 agents: spec /
license / adversarial check; the cell's outputs appear VERBATIM below; the one repair the
adversarial lens forced is made in the bench header, never silently inside the cell text).
Status: **REGISTERED 2026-08-18 → LARGELY ANSWERED WITHIN 48 HOURS — see the STATUS
ADDENDUM at the end** (B1070/B1071: Λ constructed, sealed, PROVED; the registration text
below is preserved verbatim as the record of the pose). Originally: this document poses
the problem; solving it is the crossing cell's job (the main-goal directive of 2026-08-18: the bridge to SM physics runs
through constructing u from field data, never fitting it). `doc-currency` living document.

**Verdicts at registration**: license 6/6 fences COMPLIANT (table below) · adversarial
check: firewalled TRUE, falsifiable TRUE, construction-shaped **FALSE on AC4 — repaired
here** (the finding, verified against B641/B856 on this bench: AC4's three checkpoints —
the five tones, h(5) = −1, period-5 — are listener-INDEPENDENT facts (B641's
ear-independence law; B856 C2), so the gate could not fail and MB12 kills it as an
acceptance criterion).

## THE BENCH REPAIR (binding on any execution)

- **AC4 is DEMOTED to a sanity check**, explicitly non-discriminating: reproducing the
  five tones / h(5) = −1 / period-5 confirms correct typing only; it accepts or rejects
  NO candidate (any correctly-typed unit vector passes, by B641's banked law).
- **AC4′ — DISCRIMINATION (replaces AC4's gate role).** The candidate's acceptance test
  must include at least one computed quantity that provably VARIES over the codomain —
  exhibited by two directions with different values (candidates: off-real-segment
  behavior on ℂP¹_odd, the θ-even mirror readouts, phase/Im-h data — exactly the
  territory G5/the uniqueness sub-question name as untested) — and the candidate Λ's
  value of that quantity must be pinned by the construction, not chosen. PASS: the
  discriminating quantity and its two-direction witness are exhibited, and Λ's output is
  forced. FAIL: every quantity in the acceptance test is ear-independent (AC4's own
  defect), or the value is selected post hoc.
- **B641 joins the inputs list** (the adversarial lens's catch: B856's FINDINGS says "the
  observer-invariance is B641's, and B641 is stronger", yet the cell's inputs omitted
  it): B641 — the five-tone LAW with ear-independence sampled at 6 real unit vectors,
  max deviation 2.14e-60; LAW_MAP's own caveat that this is exhaustive-but-floating-point
  on a sample, NOT a closed-form proof over all of ℂP¹_odd — which is precisely why
  AC4′'s discriminating territory may exist at all.

---

## 1. THE SPEC (the cell's output, verbatim)

**THE LISTENER-MAP PROBLEM SPECIFICATION — the admissible-u classification problem on the coupling instrument (B593/B856/B1011)**

### 1.1 Statement

SCOPE FIRST (COMPUTE_THE_PROGRAM.md's P0 discipline: state the quantifier before computing). This document computes nothing — it is a problem statement, scoped to one structure inside the object's COUPLING channel only: B593's welded instrument on SU(3) at level 2's six primaries (the corpus's "SU(3)_2"; B238's Kac-Peterson modular data), as factorized exactly by B1011. It does not touch the pair channel (B936, D2, frame-relative — L150 closed SEPARATE by B1016, sealed 59f51572), the object-level theta/character-variety layer, or any SM quantity. Gate 5 is absolute throughout (WORKING_RULES section 6): no measured physics number appears anywhere below, and none may enter any future execution of this spec without a fresh seal.

THE INSTRUMENT (fixed, not reopened). C^6, the SU(3)-level-2 weight space (weights (a,b), a,b>=0, a+b<=2; B238's su3_data), carries the representation of <R,L> where R=T and L=S^-1 T^-1 S (S,T the Kac-Peterson modular matrices). B1011 C1 proves exactly |<R,L>| = 2880 = |2T x 2I| (2T the binary tetrahedral group, order 24; 2I the binary icosahedral group, order 120; verified at two unramified primes, 61 and 241, plus Serre's injectivity lemma), with 63 = 7x9 conjugacy classes and no hidden central extension. The conjugation weld C — called theta throughout B593/B856/B1011 (B1011 PREREGISTRATION C2) — grades C^6 = C^2_odd (+) C^4_even exactly, and B1011's headline factorizes each isotypic summand as a McKay-tensor-McKay object: rho_6 = (chi (x) V2(2I)) (+) (V2(2T) (x) V2(2I)), chi the order-3 character of 2T with kernel Q8 (2T/Q8 = Z/3). Every field datum here lives in Q(zeta_60) which contains Q(sqrt5) (B1011 C4: 2T's trace set {-2,-1,0,1,2}; 2I's golden nine {-2,-phi,-1,-1/phi,0,1/phi,1,phi,2}).

THE LISTENER. B593/B856 evaluate h(g) = u-dagger M_odd(g) u for g = R^m L^m (the metallic-family weld) at a unit vector u — "the listener direction" — held throughout to exactly two vectors, u3 and u6: the antisymmetric (theta-odd) combinations of SU(3)-level-2's conjugate weight pairs {(1,0),(0,1)} and {(2,0),(0,2)} (B856's hearing_family.py, setup()). THIS CHOICE IS GIVEN, NOT DERIVED. B1011 C5 states the exclusion explicitly: "the pointwise map m -> h(m) for a specific listener u inherits B593/B856's listener convention and is NOT re-derived here" — B1011 derives the value sets, the period, and the forced criteria from group/field data, never which vector plays u. B1066 names the resulting gap in these words: "the listener map (which physical apparatus is which listener state u) remains unconstructed ... the kind table is its coarse form; the fine form is a separate, harder cell, registered not attempted."

THE OBJECT THIS SPEC POSES. A listener map is a classification rule

  Lambda : (field-side data of the instrument)  ->  (admissible unit directions u, a subset of CP^1_odd union CP^3_even)

— not a single guessed vector, not a fit. Its DOMAIN is data belonging to the instrument's own ambient structure only: the field Q(zeta_60)/Q(sqrt5) and Gal(Q(zeta_60)/Q); the exact group 2Tx2I, its 63 conjugacy classes and character table (B1011 C1/C3, class_reps.json / class_chars.json); the theta-grading (C2); and the object's own already-licensed discrete frame freedoms (CROSSING_REQUIREMENTS R11: B782's torsor bits; B1040 step S11's free (Z/2)^3 closings action). This is "field-side" in the operational sense B1040 established for a DIFFERENT observer battery (B700/B733/B735/B766/B782, via B723): a TEMPLATE is whatever transplants verbatim to a structurally analogous instance and stands when object-specific data is deleted; a SELECTION is whatever does neither — B1040's own worst case, step S3, found "the object provides the AMBIGUITY," no template at all. Its CODOMAIN is the space of unit directions in the eigenspace u3 and u6 already inhabit (C^2_odd) and, per B1011 C6, the theta-even mirror sector too — "open instrument territory" with its value set already exact, so the codomain is not confined to the odd plane. "FIELD-LICENSED" means Lambda is expressible using domain data alone — no measured value enters its definition, ever (the forbidden clause is absolute on this point). The listener map is the object this spec asks to be POSED, not solved: whether such a Lambda exists, and if so whether it is unique, are the two questions that follow. B1066's fuller sense of "listener map" — assigning a PHYSICAL apparatus to each admissible u — is a further, separate act this spec does not license (see FORBIDDEN F1/F7 and GAPS G9).

### 1.2 Existence

DOES A NONEMPTY, NON-VACUOUS Lambda EXIST AT ALL — some rule, stated purely in the domain data above, that excludes at least one candidate unit direction (MB12, TERMINOLOGY.md: "a preregistered test must be able to both pass and fail — applied to the target, the OPERATION, and the CRITERION"), without referencing u3/u6's numeric coordinates or any measured value?

WHAT WOULD DECIDE IT — two admissible, symmetric outcomes, in B1040's own two-outcome form:

- A POSITIVE CONSTRUCTION: exhibit Lambda explicitly — e.g. "u = the unit direction fixed, up to phase, by [a named stabilizer inside 2Tx2I or Gal(Q(zeta_60)/Q)]," or "u = the canonical direction attached to [a named Galois orbit on the 63 classes]" — then run it through the acceptance criteria.

- A STRUCTURAL NO: prove, in B1040 step S3's own form ("no Q-rational point ... simply transitively"), that the natural candidate symmetry group (Aut(2Tx2I) x Gal(Q(zeta_60)/Q), or whatever group the attempted Lambda claims invariance under) acts on the candidate direction-space with NO field-fixed point — i.e. the u-choice is intrinsically a SELECTION in B1040's sense, exactly as B1040 found for the geometric-characters torsor in its own, disjoint battery (B701/B713's y^2-3y+3, "Galois simply-transitive").

Either outcome closes the question. Neither has been attempted on THIS instrument: B1040's sealed battery (B700/B733/B735/B766/B782) and B593/B856/B1011/B1066's instrument share zero citations in either direction (checked by grep, both ways) — the discriminant exists here as a method, not yet as a result.

### 1.3 Uniqueness

ASKED ONLY IF EXISTENCE HOLDS. Is Lambda's admissible set a SINGLE ray per eigenspace — matching u3 and u6 exactly, or superseding them with a stated, exact correction — or a positive-dimensional family, or a finite orbit of size greater than one?

WHAT WOULD DECIDE IT: name the symmetry group G that Lambda is claimed invariant under, and compute G's action on Lambda's admissible set directly. Transitive with trivial stabilizer implies a unique ray (uniqueness holds). Transitive with a named nontrivial stabilizer implies a named finite or continuous orbit (uniqueness fails, in a characterized way). Non-transitive implies several inequivalent field-licensed directions, none preferred without a further, separately-licensed criterion.

A sharper, currently open sub-question the same computation would settle: B856's own code (Re_h_spread_over_listener_directions, hearing_family.py) verified Re h constant only along the tested REAL one-parameter segment between u3 and u6 (11 sample points, to 1e-15) — not over the full CP^1_odd, still less CP^3_even. Whether that invariance extends to the whole admissible set, or is a feature of the tested segment alone, is exactly what the uniqueness computation would resolve, and it has not been run.

### 1.4 Acceptance criteria (AC4 demoted — see THE BENCH REPAIR)

A candidate construction counts as HAVING BUILT a listener map only if it clears all of the following, each stated so it can independently PASS or FAIL (MB12, TERMINOLOGY.md; WORKING_RULES section 8: "vacuity-check before sealing ... every sealed criterion must be able to pass AND to fail"):

AC1 — NON-VACUITY (on the target). Lambda must exclude at least one unit direction in the ambient space. PASS: a proper, nonempty admissible subset, or a proved-empty subset carrying its own obstruction proof (the existence question's structural-NO form). FAIL: Lambda = the whole projective space (excludes nothing), or an unexplained empty set.

AC2 — FIELD-ONLY DEFINABILITY (on the operation; the anti-fitting check). Lambda's defining rule must be statable and checkable by a reader shown no measured SM number: redact every measured value from the construction's writeup and confirm the rule and its output are unchanged. PASS: the rule survives full redaction verbatim. FAIL: the rule cannot be stated, or changes, once measured numbers are hidden.

AC3 — SISTER TRANSPLANT (on generality; B1040/B737's battery form, run here for the first time). Apply Lambda's defining rule, unchanged, to at least one structurally analogous instance reachable from the corpus's own machinery — e.g. the silver family's own stage, SU(4) at level 2 (LAW_MAP's "own-channel law," B684/G2 — no listener instrument has been built there; this would be the first), or 2Tx2I replaced by another McKay pair. Report per instance VERBATIM-TRANSPLANT or NAMED-BREAK (B1040 V2's vocabulary). PASS: transplants, or breaks with a stated structural reason. FAIL: silently undefined elsewhere, no diagnosis offered.

AC4 — EXACT REPRODUCTION (a non-regression gate). Substituting Lambda's output into u-dagger M_odd(R^m L^m) u for m = 1..5 must reproduce the already-sealed exact values — the five tones, h(5) = -1, B1011 C5's period-5 — to the same exactness standard those arcs used (Q(zeta_60) exact arithmetic, no float in the verdict line; B1011's own exactification bar). PASS: exact symbolic match. FAIL: any mismatch, which falsifies the CANDIDATE construction, not the sealed priors — the non-weakening clause (named at B915, kept in CROSSING_REQUIREMENTS section 1) forbids treating a mismatch as license to reopen B593/B856/B1011.

AC5 — ORBIT-DECIDABILITY (turns the uniqueness question into a checkable one). The construction must name its invariance group G and exhibit G's action on the admissible set as one of: transitive-trivial-stabilizer / transitive-nontrivial-stabilizer / non-transitive. PASS: any of the three, computed. FAIL: uniqueness claimed without exhibiting the group action.

AC6 — TYPE CONFORMANCE (B1032's type law). Any menu-valued functional of Lambda's output (u-dagger M_odd u and its relatives) must remain inside the already-banked finite algebraic menus (the golden nine, the five tones, the mirror eight) or exactly and closedly extend them — never require an unconstrained continuous parameter. PASS: stays inside, or exactly extends, a finite algebraic menu. FAIL: produces or requires a generic real ("the object's forced outputs live in a finite algebraic menu ... a crossing may NOT target a generic real by value," B1032 FINDINGS).

Each AC is independently gateable. A construction failing any one is not a listener map under this spec, whatever its output otherwise suggests.

### 1.5 Forbidden

ABSOLUTE, per Gate 5 (WORKING_RULES section 6) and the house guard binding this workflow.

F1 — NO FITTING, EVER. No candidate Lambda, at any stage of its construction or its acceptance-criteria checks, may reference a measured SM value as a seed, a target, a sanity check, or a tie-breaker among otherwise-equal candidates. A rule that reduces to "choose u so u-dagger M_odd u lands near a measured angle" fails AC2 by construction — it is exactly the fitting exercise Gate 5 exists to exclude, not a judgment call.

F2 — THE VALUE-CONTACT SURFACE IS EXHAUSTED; this door does not reopen it. Every menu this instrument's outputs could plausibly be compared against has already been taken to measured data and closed NEGATIVE, decisively and at power (no measured numbers restated here — Gate 5 absolute; the discriminating figures live in the cited arcs' own files, not in this document): B1027/B1063 — the chi-phase menu {0, +-2*pi/3} against the CP-violating phases (the quark mixing phase, the leptonic delta_CP), MISS in both sectors, powered, the pre-committed refresh closing it "CONFIRMED-DECISIVE" (B1063's own verdict line); B1066 R-A — the listener pair {(1 -+ 1/sqrt5)/2} against the sin^2(theta) mixing angles, MISS at every trial, corroborated against a second, independent source (the collaboration's own JUNO companion paper); B1066 R-B — the phi-geometric tone row (1/(2phi), 1/2, phi/2) against every PMNS/CKM row and column, MISS, "unrescuable by the unknown phase" at the one delta-independent anchor. B1066's own words: "the licensed value-contact surface is EXHAUSTED ... the listener map named as the sole residual door." This construction may build the classification Lambda; it may not use Lambda to re-attempt R-A, R-B, or the phase menu, nor build any new pairing that does so, without a wholly new arc, a wholly new seal, and the full CROSSING_REQUIREMENTS checklist (R1-R11) — the one-shot rule (B1063's precedent, reaffirmed in B1066 Appendix B item 5) governs any such re-pose, and this document is not that arc.

F3 — NO NEW ANCHORS. CROSSING_REQUIREMENTS R11 permits at most one continuous calibration constant (T2, provisionally spoken for by sigma/L154) beyond the discrete T1 frame-selectors; this construction problem consumes ZERO anchors of either type — it is a classification over already-licensed discrete/algebraic data, not a fit with free parameters.

F4 — NO CHANNEL-MIXING. Nothing here may touch the pair channel (B936, D2, the Hermitian v-dagger-H-v layer) — L150 is CLOSED SEPARATE (B1016, sealed 59f51572): the coupling channel (this instrument) and the pair channel are proved-distinct value structures, and R10 requires a candidate to declare its channel. This spec declares: coupling channel only.

F5 — NO NUMERICS TOWARD VALUES, ANYWHERE. This is a problem statement; no construction attempt, no computation of a candidate Lambda, and no evaluation of u-dagger M_odd u at any candidate direction is performed here or licensed by this document.

F6 — TERMINOLOGY HYGIENE. "Conductor" names at least two distinct corpus quantities (the elliptic-curve conductor of 15A8, LAW_MAP/B509-510; and the word-indexed "unique prime conductor" of the hearing-landscape theorem, LAW_MAP/B664-665) and "level" at least two (SU(3)'s own affine level, used throughout this spec always spelled out — "SU(3) at level 2," never bare; and the gravitational Chern-Simons level of R4/B1012). Neither term is used unqualified anywhere above. qL-numbers belong to a separate branch of the corpus and are not invoked here.

F7 — KIND_TABLE'S ROWS ARE NOT A LISTENER MAP. Part 1's coarse admissibility rows (amplitude-part / probability / phase / mirror; KIND_TABLE.md, B1020) classify by KIND only; citing them is not constructing Lambda, and a candidate that stops at kind-matching has not met AC1-AC6.

### 1.6 Inputs (B641 added — see THE BENCH REPAIR)

THE BANKED CLOSED FORMS A CONSTRUCTION WOULD CONSUME (exact, sealed; cited here, not recomputed):

- B1011 C1 — <R,L> = 2Tx2I exactly, order 2880 (verified at two unramified primes, 61 and 241, plus Serre's injectivity lemma); 63 = 7x9 conjugacy classes with word representatives (class_reps.json); no hidden central extension.

- B1011 C2 — the theta-grading C^6 = C^2_odd (+) C^4_even exactly, verified in Q(zeta_60) arithmetic (Sigma-Sigma-dagger = 75*I exact).

- B1011 C3/C4 — the exact 63/63 class-by-class character match against an independently built quaternion model (2T = Hurwitz units, 2I = icosians over Q(sqrt5)); the trace sets 2T = {-2,-1,0,1,2}, 2I = the golden nine {-2,-phi,-1,-1/phi,0,1/phi,1,phi,2}, phi entering only via 2cos(pi/5), 2cos(2pi/5).

- B1011 C5/C6 — the forced-count inclusion-exclusion (theta-odd 992, theta-even 284); the five tones and B856's period-5 as DERIVED theorems, not merely observed; the theta-even mirror value set {0,+-1/4,+-1/(4phi),+-1/2,+-1/(2phi),+-phi/4,+-phi/2,+-1} delivered in closed form.

- B593/B856's instrument definition itself: M_odd(g), the weld-by-conjugation C (= theta), the quadratic form u-dagger M_odd u, the second-order hearing law (A_eps = A0 - eps^2 * u-dagger-W-u, no first-order term, verified to 1e-15 and re-verified in exact Q(zeta_20) symbolic arithmetic) — and, as the GIVEN convention this spec's problem is about, u3 and u6 themselves (hearing_family.py's setup()).

- B1040's field/object vocabulary (template = stands under object-deletion, transplants verbatim to sisters; selection = does neither) and its own worked precedent, step S3 (the geometric-characters torsor, pure-selection, "the object provides the AMBIGUITY") — imported here as METHOD, not as a result about this instrument (B1040's battery and this instrument share no citation, either direction, checked).

- KIND_TABLE.md (B1020) Part 1's coarse rows — the coupling channel's kind labels (amplitude-part / probability / phase / mirror, all over Q(sqrt5)) — the coarse classification any Lambda must refine, not contradict.

- CROSSING_REQUIREMENTS.md R10 (channel declaration) and R11 (the T1-discrete / T2-continuous anchor typology) — the downstream discipline a constructed Lambda would inherit if ever used in a future crossing (not invoked by this spec itself, per F3).

- B1032's type law — the coupling channel's forced outputs live in a finite algebraic menu; a crossing, and by AC6 this construction's output, may target a relation or a finite label, never a generic real.

- TERMINOLOGY.md's MB12 (the vacuity-check rule) as the acceptance criteria's own checking standard.

### 1.7 Gaps, named

WHAT IS NOT BANKED, NAMED RATHER THAN GUESSED:

G1 — No derivation of u3/u6 from field/group data exists anywhere in the corpus. B1011 C5 states this as an explicit scope exclusion, not an oversight: "the pointwise map m -> h(m) for a specific listener u inherits B593/B856's listener convention and is NOT re-derived here."

G2 — The listener map itself is named as unconstructed, in exactly these words, by B1066: "the listener map (which physical apparatus is which listener state u) remains unconstructed ... the kind table is its coarse form; the fine form is a separate, harder cell, registered not attempted."

G3 — B1040's field/object discriminant has never been run on THIS instrument. B1040's sealed battery (B700, B733, B735->B723, B766, B782) is a disjoint arc family from B593/B856/B1011/B1066 — grepped both directions, zero cross-citations. Its per-step verdicts (the Z/2-only reading; 0-of-11 omega-essential steps) are facts about a DIFFERENT observer construction, and transfer to this problem as method only, not as an answer already in hand.

G4 — No stabilizer/orbit computation exists for the natural candidate symmetry group (Aut(2Tx2I), or Gal(Q(zeta_60)/Q), or their product) acting on the unit sphere of C^2_odd or C^4_even — the computation the uniqueness question needs has not been attempted.

G5 — B856's own invariance result is narrower than it can be misread as. Its Re_h_spread_over_listener_directions (hearing_family.py) tests Re h only along the real one-parameter segment {t*u3 + (1-t)*u6, normalized : t in [0,1]}, 11 sample points, to 1e-15 — not over the full projective line CP^1_odd, still less CP^3_even. Whether the invariance extends to the whole admissible set is open, and is exactly what AC5's orbit computation would resolve.

G6 — A NAMING COLLISION IS UNCHECKED; flagged so it is not walked into unexamined. B1040's "never consumes mu_6's Z/3" is a statement about Q(sqrt-3)'s unit group (a FIELD's own arithmetic, inside the OTHER observer battery). B1011's chi is a Z/3-valued CHARACTER of 2T (2T/Q8 = Z/3, a GROUP's abelianization, inside THIS instrument). Both are "Z/3"s carrying cube roots of unity; whether they are related under any natural map is uncomputed. Conflating them would repeat the species of error B1032 found and fixed under "the two banked theta-even's" (the F4 exponent set versus B1011's mirror value set) — a corpus-level term collision, not a shared fact.

G7 — Whether 2T's representations other than chi (its other nontrivial irreps) bear on u-selection is unexplored; B1011's factorization uses only chi (1-dimensional) on the odd side.

G8 — No no-go exists either. It has not been shown that Lambda CANNOT exist (the S3-style obstruction form, per the existence question) — the question is open in both directions, not leaning negative by default.

G9 — B1066's fuller sense of "listener map" (assigning a PHYSICAL apparatus/observable to each admissible u) is a further layer this spec does not ask to be built: no licensed pairing beyond KIND_TABLE's coarse rows is banked ("no such pairing is banked, and the kind table's current rows were both consumed here" — B1066), and Gate 5 forbids constructing one by fitting (F1). That layer is named as a boundary of this problem, not a gap this construction should try to close. *(stamp 2026-08-19: still CURRENT as of B1082 — the stale-absence sweep verified this absence/openness against the full corpus.)*

---

## 2. THE LICENSE TABLE (the cell's output, verbatim)

**Verdict: COMPLIANT**

| fence | source | permits | forbids | spec complies |
|---|---|---|---|---|
| R5 kind-admissibility + per-kind SPENT status inside the coupling channel | docs/KIND_TABLE.md Part 1 (B1020), rows for tones/\|h\|²/mirror/phase (object side) and sin²θ/moduli/CP-phase (SM side); frontier/B1066_lane3_nomination/FINDINGS.md; docs/views/VERDICT_LEDGER.md B1066 row ('both remaining kind-rows consumed') | Building Lambda over kind-labelled domain data; citing KIND_TABLE's rows as the coarse admissibility floor a construction must refine, never contradict (F7 already states this limit). | Any fresh (object-kind, SM-target-kind) value-contact inside the coupling channel without a new arc+seal: amplitude-part (tones, B1066 R-B), probability (the listener family/\|h\|², B1066 R-A), and phase (χ, B1027/B1063) are all tested-MISS and SPENT; stopping at kind-matching alone never counts as building Lambda (F7). | True |
| L150/R10 — the coupling/pair channel separation and the declare-your-channel duty | frontier/B1016_l150_junction/FINDINGS.md (sealed 59f51572, prior SEPARATE, held); docs/CROSSING_REQUIREMENTS.md R10; docs/SEAL_LEDGER.md and docs/OPEN_LEADS.md L150 closure rows | Constructing Lambda wholly inside the coupling-channel instrument (B856/B1011: ρ₆ on SU(3)₂'s six primaries, C²_odd ⊕ C⁴_even); citing the coupling channel as forced, listener-invariant, anchor-free. | Any appearance of pair-channel data (B936, D₂, the Hermitian v†Hv layer, det-ratios, the K-norm, the octet) in Lambda's domain or codomain; asserting a channel bridge without the one door R10 names (a novel, arc-supplied 2T×2I action on the 27, which none currently supplies). | True |
| Gate 5 (no measured SM numbers; functor-gated physics readings) + the one-way firewall (form not contents; layer 3 never evidences layer 1/2) | WORKING_RULES.md rule 6 and 6a ('Gate 5 stands' / Gate 5-Q); GOVERNANCE.md §2 (the framing lock, 'form / contents'), §8 (anti-overclaim glossary), §11 (automated gates incl. the one-way firewall), §13 (the three layers) | Posing an unsolved existence/uniqueness question purely over layer-1/2 (THEOREM/LAW-graded) domain data; citing B1011/B1032/B1016/B1066 as scoping evidence for a new problem, not a new claim. | Any measured SM value anywhere in the document; wording that lets the object 'produce' physics contents rather than a compatible form; citing coupling-tier (hint/speculation/review) material as evidence for a layer-1/2 statement. | True |
| B1032's type law (menu-valued output only, never a generic real) + R11's anchor typology (T1 discrete frame-selectors; T2 ≤1 continuous calibration constant) | docs/LAW_MAP.md §F ('THE TYPE LAW', B1032 row); frontier/B1032_type_law/FINDINGS.md ('the object's forced outputs live in a finite algebraic menu ... it may NOT target a generic real by value'); docs/CROSSING_REQUIREMENTS.md R11 | Lambda's output, and any menu-valued functional of it, landing inside or exactly/closedly extending an already-banked finite menu (golden nine, five tones, mirror eight, listener family); referencing the T1 frame bits (B782 torsor, B1040 S11's (ℤ/2)³) and the single provisional T2 constant (σ, pending L154) as licensed background facts, not as fittable inputs. | Any construction whose output needs an unconstrained continuous parameter (Type Law FAIL clause); spending a second T2 anchor, or any anchor of an unnamed type; treating parameter-fitting as construction. | True |
| THE ASYMMETRY PRINCIPLE — one coordinate/projection suffices to exclude; certification needs the full tuple, never a projected slice | docs/LAW_MAP.md §G (THE ASYMMETRY PRINCIPLE row, provenance B1062's M5 addendum): 'one elliptic coordinate suffices to EXCLUDE a component; certifying a component geometric requires ALL coordinates typed at every root — exclusion is one-coordinate-valid, certification is full-tuple-only'; scope note: 'applies wherever a multi-coordinate object is typed through a projection' | A structural-NO (exclusion) resting on a single obstruction/no-fixed-point computation; AC5 requiring the FULL group action on the FULL admissible set (all of CP¹_odd and CP³_even) before any uniqueness claim is entered. | Certifying a unique ray, or asserting that B856's real-segment invariance extends to the whole odd/even eigenspaces, on the strength of the tested one-parameter projection alone. | True |
| The exhausted value-contact surface + the one-shot rule on any re-pose | frontier/B1066_lane3_nomination/FINDINGS.md (sealed ad21f28f…); PREREGISTRATION.md §2-PRE ('the LISTENER MAP ... is NAMED as the residual beyond this cell — the kind table is its coarse form; the fine form is a separate, harder cell, registered not attempted') and Appendix B item 5 ('the refresh is one-shot ... any future re-pose is a new arc under a new seal'); docs/views/VERDICT_LEDGER.md and REVIEWER.md B1066 rows ('the licensed value-contact surface is EXHAUSTED. The listener map named as the sole residual door.') | Posing/constructing the listener map Lambda itself — the one cell B1066 explicitly leaves unattempted. | Using a constructed Lambda to re-attempt R-A (the listener pair vs sin²θ), R-B (the tone row vs PMNS/CKM moduli), the χ-phase menu (B1027/B1063), or any new SM pairing, without a wholly new arc, a wholly new seal, and a fresh CROSSING_REQUIREMENTS R1–R11 pass. | True |

**The license agent's forward-looking notes:** No repairs required — all six fences hold against the spec as written; nothing in the spec text offends a binding rule. Two forward-looking notes for whoever executes this spec next (not defects in the spec itself): (1) Row "kind table" — the mirror set (B1011 C6, theta-even) was never itself numerically fitted to SM data, only the tone subset was (B1066 R-B); B1066's own verdict language books SPENT status at the KIND level ("both remaining kind-rows consumed"), not the row level, so a future arc using Lambda's output on the mirror sector should state explicitly which reading it relies on before treating that pairing as licensed — though the spec's own F2 ("nor build any new pairing that does so") and F5 (zero numerics performed here) already gate it shut either way, so this is hygiene, not a hole. (2) Row "type law / anchor rule" — F3's "consumes ZERO anchors" is true only because F5 keeps this document short of ever mounting a comparison; a future crossing that builds Lambda constitutively from the T1 frame bits (B782 torsor / B1040 S11's (Z/2)^3) will still need to declare those bits under R11's own anchor count at THAT seal. Verified by direct grep-then-open of every cited register (KIND_TABLE.md, LAW_MAP.md §F/§G, GOVERNANCE.md §2/§5/§6/§8/§11/§13, WORKING_RULES.md rule 6/6a, CROSSING_REQUIREMENTS.md R10/R11, TERMINOLOGY.md MB12, and the B1011/B1016/B1032/B1066 arc files themselves — PREREGISTRATION.md and FINDINGS.md, not just the LAW_MAP summary rows) rather than trusted from the spec's own paraphrase; every direct quote the spec attributes to a banked source (B1011 C5's listener-convention scope line, C6's "open instrument territory," B1032's "finite algebraic menu ... never a generic real by value," B1066's "EXHAUSTED ... sole residual door" and its Appendix B item 5 one-shot clause, B1063's "CONFIRMED-DECISIVE") was found verbatim or near-verbatim in the source file itself. No measured physics number appears anywhere in the spec text (full scan performed) — Gate 5 absolute holds throughout.

---

## 3. THE ADVERSARIAL CHECK (the cell's output, verbatim)

- construction_shaped: **False** (repaired above)
- firewalled: **True**
- falsifiable: **True**

**Weakest point:** AC4 ("exact reproduction"). Its three named checkpoints -- the five tones, h(5) = -1, and B1011 C5's period-5 -- are, by the corpus's own banked math, properties of the MATRIX M_odd(R^mL^m) itself, not of the listener u, so almost any correctly-typed unit vector clears them, not just u3/u6. Verified directly against source: B641 (a sealed LAW, absent from this spec's own "inputs" list even though B856's FINDINGS.md says outright "the observer-invariance is B641's, and B641 is stronger") proves Re(zeta^-1 . u-dagger M_odd u) "ear-independent on ALL 360 elements -- max deviation 2.14e-60" -- sampled at 6 real unit vectors, e.g. (3/5,4/5), (1,0) (LAW_MAP.md itself flags this row as "exhaustive-but-floating-point ... only a 'proof sketch'", not a closed-form proof over the full CP^1_odd). B856 FINDINGS.md C2 shows h(5) = -1 because R^5L^5 literally acts as the scalar matrix -I on the whole odd plane ("verified directly"), so h(5) = u-dagger(-I)u = -1 for EVERY unit u -- an algebraic triviality, not a test of direction at all. Period-5 is inherited by h(m) for any fixed u once the matrix itself has period 5. The one place a genuinely listener-dependent signal lives -- B856 says it outright, "the observer's freedom moves the phase and not the real part" -- is exactly the piece AC4 does not name. So a candidate Lambda can output essentially any unit vector in C^2_odd, clear all three of AC4's stated checkpoints, and be presented as validated without having recovered u3 or u6 in any meaningful sense. Nothing in AC1-AC6 requires Lambda's defining rule to be fixed/hashed BEFORE it is checked against this target (contrast the repo's own WORKING_RULES rule 3, "hash first ... before the first run"), so a search-until-something-clears-AC4 construction is not merely conceivable, it is the path of least resistance this battery leaves open. Secondary soft spot, different mechanism: AC3's PASS condition is "transplants, OR breaks with a stated structural reason" -- both branches pass, so it can fail only by silent omission.

**Verdict note:** Three attacks, three different outcomes -- not a uniform verdict.

(A) FAILS, concretely, not hypothetically. AC4 is sold as the empirical backbone ("a non-regression gate," "exact reproduction") but its three named targets are all listener-INDEPENDENT facts already proven or strongly evidenced elsewhere in the corpus (B641's ear-independence law; B856 C2's h(5)=-1-by-scalar-matrix, "verified directly"). A candidate clears most of AC4 by construction, before doing any real derivation -- exactly "a criterion a lookup could pass," found by tracing the spec's own citations one hop further than the spec itself goes. The license table credits a full grep-then-open pass but its "inputs" row list never reaches B641, the one arc that would have flagged AC4's vacuity to the spec's own author -- a real gap in the diligence, not just in the spec.

(B) HOLDS. Full-text scan: no measured SM number anywhere in the spec. I specifically hunted for an indirect smuggling route -- u3/u6's own historical genesis, since AC4 requires reproducing their output -- on the theory that "reproduce u3/u6" could be measurement-matching wearing a math costume if u3/u6 were themselves originally fished for via a physics comparison. Checked directly against B593's PREREGISTRATION/FINDINGS: u3/u6 were fixed for a structural reason (the second-order "chirally-displaced listener" law, R4-A) strictly before the sin^2(theta12)/JUNO reading was even proposed, downstream, at B856 -- and that reading was refuted on kind. The concern does not survive contact with the source. Separately, F2's explicit ban on replaying a validated Lambda into R-A/R-B is doing real, necessary work (AC4 ties Lambda's output directly back to u3/u6's numbers, which is exactly the seam that could otherwise launder a "new" construction into a re-pose of an already-spent one-shot test) -- correctly written, not decorative.

(C) HOLDS, at the level the lens asks. Existence has a genuine two-sided witness (a positive construction vs. a B1040-S3-style proof that Aut(2Tx2I) x Gal(Q(zeta60)/Q) fixes no point on CP^1_odd union CP^3_even); uniqueness has a clean AC5-operationalized trichotomy (transitive-trivial / transitive-nontrivial / non-transitive), each with a nameable failure witness (a second inequivalent admissible direction, or an exhibited nontrivial stabilizer element). One flag, not a reversal: AC4 speaks of "Lambda's output" as singular, while the existence section defines Lambda as SET-valued and the uniqueness section explicitly allows a positive-dimensional family or an orbit of size > 1 as a legitimate PASS outcome -- the spec never states what AC4 requires when the honest answer is multi-valued, which is precisely the case its own uniqueness trichotomy keeps open. That is a live gap in one operational gate, not in the two headline questions, which are well-posed and better-built than most documents of this kind.

Net: the license table's six-fence "COMPLIANT" is accurate as far as it goes -- spot-verified MB12, B1011 C1-C6, B1040 S3's template/selection vocabulary, the Asymmetry Principle row, KIND_TABLE Part 1, CROSSING_REQUIREMENTS R10/R11, and every attributed B1066 quote directly against source; all held, including the license table's own self-flagged G2 two-file splice. But fence-compliance and construction-quality are different questions. This pass answers the second one: the spec is honest and correctly firewalled, and poses a genuinely falsifiable pair of questions, but its flagship acceptance criterion does not test what it claims to test.

---

## 4. THE PREPARATION ORDER (bench, 2026-08-18 — merged with CROSSING_REQUIREMENTS §3's two unstruck items; owner's execute-when-ready standing)

**Track A — the door itself (all exact, in-sandbox, unblocked):**
- **A1 = G4, the named first computation**: the orbit/stabilizer run — Aut(2T×2I) ×
  Gal(ℚ(ζ₆₀)/ℚ) acting on the unit spheres of ℂ²_odd and ℂ⁴_even. Decides the existence
  question's SHAPE (fixed point / finite orbit / free — B1040-S3's trichotomy).
- **A2**: close B641 to closed form — is Re(ζ⁻¹·u†M_odd u) constant over ALL of ℂP¹_odd
  (theorem), or only on the tested real segment (counterexample exhibited)? Upgrades a
  LAW_MAP proof-sketch row either way, and decides WHERE AC4′'s discriminating quantity
  can live (odd sector vs mirror/phase territory only).
- **A3 = G5**: the θ-even mirror's u-dependence landscape over ℂP³_even — which
  functionals vary (AC4′'s candidate territory), exact in ℚ(ζ₆₀).
- **A4**: the kind-table mirror-row reading (the license agent's note: SPENT is booked at
  KIND level; the θ-even row was never itself fitted) — a bench adjudication the prereg
  must quote.

**Track B — the register's two unstruck items (CROSSING_REQUIREMENTS §3):**
- **B1 = L149 + AC3 fused**: build the silver/sister instrument (the own-channel law's
  analog stage) — ONE build serves both the register's "can any structure-level match
  confirm at all" and this spec's sister-transplant criterion. Without it AC3 cannot run.
- **B2**: S4-typing of B1000's five closings (𝔽₂ / ℝ₊ / Lie — which interface numbers
  exist).

**Track C — strengthening, parallel, NOT blocking:**
- **C1 = L154**: the σ-identification (B1012's σ vs B254's banked c-content; if one, A2
  converts from anchor to OUTPUT and the input list loses its only continuous member —
  the zero-anchor crossing).
- **C2 = B882's conjecture** (the 77-echo's true form per the W4 cell): its own lane;
  the crossing does not route through the trialitarian datum.
- **C3**: K's class group (the 953-place's principality, B1067's named blocker):
  biography completeness; not in the crossing's path.

**Explicitly NOT needed (so nobody precomputes it)**: the child family — B718's ledger is
decisive that the child inherits nothing structured (no field law, no charged skeleton,
golden slope generic); the SM structure does not migrate to the closing. The child is not
crossing-relevant. The twelve faces are the PREREG'S OWN ROWS to fill (the both-checklists
rule — an obligation on the seal, not a completed sweep; wording corrected 2026-08-18,
the W6 adversarial reader's catch); the object side's one open item is C2.

**The execution sequence**: W2/W3 land → their banks (+ this document's bank) → Track A
as the L166 opening arc → B1 → W6 synthesis (ranks everything by crossing-feed) → the
crossing cell's PREREGISTRATION (every R1–R11 row + the twelve as rows checkable, the
location clause, the channel declared: coupling) → seal → execute → the paper carries the
outcome either way.

**A4 — EXECUTED at registration (2026-08-18)**: the kind-table consumption ledger written
(`docs/KIND_TABLE.md`, THE CONSUMPTION LEDGER): tones/probability/phases CONSUMED
(B1066 R-B / B1066 R-A / B1027+B1063); **the mirror row UNCONSUMED — the last licensed
contact row in the coupling channel**; any future contact through it = a new arc under a
new seal, only after a constructed Λ pins u. Tracks A1–A3 run as a workflow at this
document's registration (wf_e25251a5-72a).


---

## STATUS ADDENDUM — 2026-08-19 (the stale-absence sweep; the registration text above is the POSE, this block is what happened)

The spec was answered faster than any registration in the programme's record. Row by row
against the gap list (each verdict banked, none re-derived here):

- **The construction itself (G1, G2, G8)** — CLOSED POSITIVE. B1070 (PROVED) and B1071
  (SEALED, PROVED; three independent re-implementations, zero errors) construct Λ: on
  ℂP¹_odd the exceptional orbits under Aut(2T×2I) × Gal(ℚ(ζ₆₀)/ℚ) are 12/20/30 (+ generic
  60); **u3/u6 are the unique pair fixed individually by all 16 Galois automorphisms in
  the minimal (order-5 vertex) orbit** — Λ = "the minimal exceptional orbit's Galois-fixed
  directions" outputs exactly {u3, u6}. Existence POSITIVE; uniqueness = THE PAIR, derived
  not conventional. G8's no-go was never needed: §1.2's own "A POSITIVE CONSTRUCTION"
  outcome is the one that happened.
- **G3 (the B1040-S3 trichotomy on THIS instrument)** — CLOSED. B1070 runs it and lands
  outcome (b): a distinguished finite orbit (size 12) — definitive, non-degenerate.
  B1071 independently reproduces it.
- **G4 (the stabilizer/orbit computation)** — CLOSED, as this spec's own Track A1. The
  orbit census above IS that computation; B1071 proves the fourth-orbit exclusion via a
  Möbius two-fixed-point bound.
- **G5 (B856's invariance beyond the tested segment)** — CLOSED. B1070 upgrades B641's
  ear-independence from an 11-point real segment to THEOREM-EXACT over the whole of
  ℂP¹_odd: M_odd(g) = χ(g)·W(g) with W ∈ SU(2) exactly for all 2880 elements, so
  Re h = half-trace for EVERY unit u. B1071 re-verifies at zero failures.
- **The silver instrument (:86) and AC3/AC6** — BUILT and FILLED. B1072 (PROVED)
  constructs SU(4) level 2 exactly (10 primaries, κ = 6, ΣΣ† = 864·I, group order
  18432 = 2¹¹·3², proper Goursat subdirect, no order-5) and runs Λ verbatim: the rule is
  FIELD-GENERIC, the selectivity OBJECT-SPECIFIC. B1073 (PROVED + same-day addendum)
  closes AC6 on both channels (every coupling value ℚ(ζ₅)-algebraic by construction; the
  composition gate h(w) = χ(w)·W(w)₁₁).
- **Still genuinely open**: G6 (the ℤ/3 naming collision — unexamined, still flagged),
  G7 (the non-χ irreps of 2T), G9 (the physical-apparatus layer — a boundary by design,
  and the fourth sealed crossing B1075 that used this listener MISSED at power, closing
  the coupling channel's value story). OPEN as of B1082.
