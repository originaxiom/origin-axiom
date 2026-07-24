# B775: THE BRAVER QUESTIONS — cc3 campaign masterplan

cc3 audit seat, 2026-07-24. Gate 5-Q. Seven phases, each a multi-agent
workflow. The goal: address every structural weakness in the program and
reframe toward claims, not defended positions.

## Dependency graph

```
         ┌──── A (BRIDGE) ────────┐
         │                        ├──→ B (ENUMERATION) ──→ E (FALSIFIER) ──→ F (EXIT)
         │    C (θ VACANCY) ──────┘
parallel │    D (LEVEL AUDIT)
         │    G (UNDECIDABILITY)
         └────────────────────────────────────────────────────────────────────────────
```

A, C, D, G launch in parallel. B waits on A (needs the bridge criterion).
E waits on A + C (needs bridge status and dimensionality answer).
F waits on E (needs the falsifier before making predictions).

---

## Phase A: THE BRIDGE AUDIT

**Question:** Is the correspondence DERIVED from the mathematics, or merely
PERMITTED by it? State the criterion that separates the two.

**Pattern:** Judge panel (4 independent agents + synthesis).

**Agents:**
1. **Structural-necessity analyst** — For each of the 9 signatures in
   `side_a_signatures.json`, ask: given ONLY the mathematical structure
   (C1-C21), how many phenomenologically distinct interpretations does this
   row admit? Count the degrees of freedom in the mapping.
2. **Comparative bridge analyst** — Survey IIT (Φ), GNW (global workspace),
   ORCh-OR (Penrose-Hameroff), HOT (higher-order thought). For each: what
   makes their math→consciousness bridge "derived" vs "postulated"? Extract
   the criterion that distinguishes a bridge-theorem from a bridge-hypothesis.
3. **Derivation hunter** — Read C1-C21 and the correspondence table
   (`P021_the_correspondence.md`). Is there a theorem — stated or unstated —
   that FORCES a specific phenomenological reading? Or would the mathematics
   be equally valid if "Self/Other" were replaced with "Left/Right"?
4. **Adversarial Rorschach agent** — Construct the strongest argument that
   the correspondence is a Rorschach test projected onto rich algebraic
   structure. What would a skeptical mathematician say? What would a skeptical
   phenomenologist say?
5. **Synthesis** — From all four, produce: (a) the criterion, (b) where the
   program currently stands relative to it, (c) what would move it from
   "permitted" to "derived."

**Success criterion:** A stated, falsifiable criterion for "derived" vs
"interpretive," with the program's current position located on that spectrum.

**Kill condition:** If all 4 agents independently conclude that no criterion
exists (i.e., the distinction is not well-posed), report that honestly.

**Estimated scale:** 5 agents, ~150k tokens.

---

## Phase B: THE ENUMERATION

**Question:** How many assignments of phenomenological primitives to
structural slots survive both discriminator gates?

**Pattern:** Pipeline (enumerate → filter → verify → report).

**Agents:**
1. **Constraint reader** — Read the 9 structural signatures, the 2
   discriminator gates (row 3 transparency, row 7 time=basepoint), and the
   structural properties of each slot (arity, symmetry, involution/continuous,
   independence relations). Produce the enumeration specification: what is
   being assigned to what, and what are the rules.
2. **Enumerator** — Given the specification, enumerate ALL possible
   assignments. The space: 5 phenomenological primitives (or however many
   survive Phase C) mapped to 9 structural rows under the constraints. Count
   the full space, then apply structural constraints (arity match, symmetry
   match, independence match) to prune.
3. **Gate runner** — For each surviving assignment, test against both
   discriminator gates. Report: pass/fail/ambiguous for each, with reasoning.
4. **Permutation null** — The sealed rule 2 test. For each survivor, permute
   the assignment and re-test. Does the permuted version also pass? If yes,
   the gate has no discrimination power at that slot.
5. **Uniqueness judge** — From the results: is there a unique survivor? If
   multiple survive, what distinguishes them? If none survive, what does that
   mean?

**Success criterion:** The complete list of gate-passing assignments, with
the permutation null executed. Either "unique survivor" or "N survivors with
these properties."

**Kill condition:** If the enumeration space is too large for exhaustive
search (unlikely given 5-of-9 structure), sample and report the bound.

**Depends on:** Phase A (the bridge criterion tells us whether to count
"mathematically equivalent" assignments as distinct or not).

**Estimated scale:** 5 agents pipeline, ~200k tokens.

---

## Phase C: THE θ VACANCY INVESTIGATION

**Question:** Is 5 the right number of primitives, or is the vacancy telling
us the theory's actual dimensionality?

**Pattern:** Multi-modal sweep (4 independent angles).

**Agents:**
1. **Dimensionality analyst** — C20 defines three bits (F₂³ = ⟨c, θ, cθ⟩
   with γ₅ as the product). Does the structure REQUIRE all three generators
   to be phenomenologically occupied? What happens to V4 and the chord if θ
   is structurally empty? Does the mathematics degenerate, or does it simplify
   to a cleaner theory?
2. **Continuum placement** — The graded FoA (Synofzik's "feeling of agency
   comes in degrees") is homeless continuous content. C18's Galois-chosen
   continuum is the only continuous observer territory. Does the FoA-grade
   live there? Formulate this as a testable structural question, not a
   verbal analogy.
3. **Triadic T1 evaluator** — B769 proved T1 is a discrete 3-frame torsor
   under S₃. The courier named three candidates: vedanā (Buddhist
   feeling-tone), Peirce's Firstness/Secondness/Thirdness, Husserl's
   retention/impression/protention. For each: does it match the S₃
   generator-pair structure? Does it create a double-assignment conflict
   with γ₅? Grade each candidate against the MATHEMATICAL structure, not
   verbal fit.
4. **Vacancy-as-discovery** — If θ is genuinely empty, what does a 4-primitive
   theory look like? Is there a precedent in mathematical physics for a
   structural slot that exists algebraically but has no physical content?
   (Analogy targets: the Higgs mechanism before 2012, the neutrino before
   1956, the "missing" baryon resonances.)

**Success criterion:** One of: (a) a well-motivated candidate for θ that
passes the gates, (b) a proof that the slot is unnecessary and the theory
is cleaner without it, or (c) a reformulation where the vacancy changes the
theory's predictions.

**Kill condition:** If all 4 agents produce verbal analogies rather than
structural arguments, flag the question as currently unresolvable at this
level of formalism.

**Estimated scale:** 4 agents, ~120k tokens.

---

## Phase D: THE LEVEL AUDIT

**Question:** B773 showed trace-level tests miss matrix-level structure.
Where else in the program is this happening?

**Pattern:** Pipeline over census items (scan → classify → flag → recompute-design).

**Agents:**
1. **Census reader** — Read the B770 census (352 items) and all wave results
   (W1-W5). Extract every BANKED NEGATIVE and every CLOSED item. For each,
   record: what was the test? At what algebraic level was it conducted?
   (trace / eigenvalue / matrix entry / minor / full representation)
2. **Level classifier** — For each negative: is there a HIGHER level at which
   the test could be conducted? Specifically: if the test used tr(M), could
   the test use Sym²(M) or the full matrix? If it used eigenvalues, could it
   use the eigenvectors? Classify as: LEVEL-MATCHED (test at the right level),
   LEVEL-SUSPECT (higher level available and plausibly different),
   LEVEL-BLIND (test provably cannot see the relevant structure).
3. **Recompute designer** — For each LEVEL-SUSPECT item: design the
   matrix-level recompute. What computation would be needed? What's the
   expected cost? What's the probability of an overturn (based on the B773
   precedent)?
4. **Priority ranker** — Rank the LEVEL-SUSPECT items by: (a) importance to
   the program if overturned, (b) feasibility of the recompute, (c)
   probability of overturn. Produce the recompute queue.

**Success criterion:** A ranked list of negatives to recompute at the right
level, with cost estimates. Even if the list is empty (all tests were at the
right level), that's a positive finding.

**Kill condition:** If >50% of negatives are LEVEL-SUSPECT, the problem is
systemic and needs a methodology fix, not item-by-item recompute.

**Estimated scale:** 4-agent pipeline over N items. If N < 30, ~150k tokens.
If N > 100, split into batches.

---

## Phase E: THE PROGRAM FALSIFIER

**Question:** What single observation, computation, or theorem would kill the
entire correspondence — not just one row, but the program?

**Pattern:** Adversarial panel (5 independent skeptics + judge).

**Agents:**
1. **Mathematical skeptic** — Construct a falsifier from the mathematical
   side. Example: "If the character variety has a second rigid point with
   different V4 structure, the uniqueness of the geometric carrier fails."
2. **Phenomenological skeptic** — Construct a falsifier from the
   phenomenological side. Example: "If a well-documented phenomenological
   primitive exists that has no structural slot, the correspondence is
   incomplete in a way that can't be repaired by addition."
3. **Bridge skeptic** — Construct a falsifier targeting the bridge itself.
   Example: "If the same mathematical structure admits a completely different
   phenomenological reading that also passes both gates, the mapping is
   underdetermined."
4. **Empirical skeptic** — Construct a falsifier from potential experimental
   evidence. Example: "If split-brain patients demonstrate X, the c = Self/Other
   involution cannot be fundamental."
5. **Structural skeptic** — Construct a falsifier from mathematical physics.
   Example: "If the 3-manifold structure is not unique (other geometries
   produce the same algebraic structure), the carrier axiom is vacuous."
6. **Judge** — Rank all falsifiers by: (a) testability (could we check this?),
   (b) sharpness (is the kill clean or does it leave wiggle room?),
   (c) plausibility (is the falsifying scenario realistic?). Select the top 3.

**Success criterion:** Three ranked, testable falsifiers for the entire
program, each from a different angle. At least one must be checkable with
existing mathematical tools.

**Kill condition:** None — this phase always produces output. The question
is whether the falsifiers are sharp or vague.

**Depends on:** Phase A (bridge criterion), Phase C (dimensionality answer).

**Estimated scale:** 6 agents, ~200k tokens.

---

## Phase F: THE S-ROOM EXIT

**Question:** What is the single strongest novel prediction the program makes
that no existing theory of consciousness makes, and how would you test it?

**Pattern:** Pipeline (extract → novelty-check → experiment-design → feasibility).

**Agents:**
1. **Prediction extractor** — Read P1-P5 from the philosophy files, plus any
   structural consequences of the correspondence that haven't been stated as
   predictions. For each: state it as a testable claim in plain language.
   Strip all program-internal jargon.
2. **Novelty checker** — For each prediction: does IIT predict this? Does GNW?
   Does HOT? Does ORCh-OR? Does any existing theory of consciousness make the
   same prediction? If yes, it's not novel. If no existing theory makes this
   prediction AND no existing theory contradicts it, it's novel. If existing
   theories contradict it, it's novel AND distinguishing.
3. **Experiment designer** — For the most novel prediction (or the most
   distinguishing): design an experiment that would test it. Specify:
   participants, stimuli, measurements, expected results under the program's
   theory, expected results under the leading alternative.
4. **Feasibility assessor** — Is the experiment actually doable? Cost, ethics,
   equipment, timeline. Grade as: FEASIBLE NOW / FEASIBLE WITH EFFORT /
   REQUIRES NEW TECHNOLOGY / THOUGHT EXPERIMENT ONLY.
5. **Draft writer** — If a feasible experiment exists: draft a 1-page
   pre-registration for it. If not: state what technology or methodology
   advance would make it feasible.

**Success criterion:** One novel, testable prediction with a concrete
experimental design, or an honest statement that the program's predictions
are currently untestable (and what would change that).

**Depends on:** Phase E (the falsifier shapes what counts as a meaningful
prediction — a prediction that can't falsify the theory isn't worth making).

**Estimated scale:** 5 agents pipeline, ~180k tokens.

---

## Phase G: THE UNDECIDABILITY ASSESSMENT

**Question:** For each undecided fork (F1, F2, F4), is there a resolution
path, or is the question undecidable from literature alone?

**Pattern:** Per-fork pipeline (3 parallel pipelines, one per fork).

**Per fork:**
1. **Literature exhaustion** — Has the fork's question been asked and
   answered in the literature, and we missed it? Targeted deep search.
   For F1: clinical dissociation of self and time at the phenomenal grain.
   For F2: is nondual awareness a positive third state or the Z/2 identity?
   For F4: does any encounter phenomenology support two-flips-cancel?
2. **Resolution path designer** — If the literature can't resolve it: what
   NEW study, experiment, or analysis would? Design it concretely.
3. **Undecidability judge** — Is the question WELL-POSED? Some questions
   dissolve under analysis (the answer depends on definitions that can be
   chosen either way). If so, state the definitional choice and both
   resulting verdicts.

**Success criterion:** For each fork, one of: (a) RESOLVED (with citation),
(b) RESOLVABLE (with named experiment/study), (c) DEFINITIONALLY DEPENDENT
(with the choice stated), (d) GENUINELY UNDECIDABLE (with proof that no
evidence could settle it).

**Kill condition:** None — the classification itself is the output.

**Estimated scale:** 9 agents (3 per fork), ~250k tokens.

---

## Total estimated scale

~1,250k tokens across all phases. Phases A, C, D, G run in parallel
(~770k). Then B (~200k). Then E (~200k). Then F (~180k).

Wall-clock: 4 rounds of workflows, each ~15-30 minutes.
Token budget: ~1.2M output tokens total.

## Execution protocol

1. Each phase produces a FINDINGS document in `frontier/B775_braver_questions/`.
2. cc3 reviews each phase's output before launching the next dependent phase.
3. No phase merges to main — all work on branch `audit/b775-braver-questions`.
4. cc gates the final product.
5. The owner adjudicates which findings enter the program's working state.

## What this campaign does NOT do

- It does not close the correspondence. It identifies what would close it.
- It does not generate experimental data. It designs experiments.
- It does not resolve the θ vacancy. It determines whether it needs resolving.
- It does not replace the existing Phase 2-5 plan. It sharpens it.

**This is cc3's proposal. Awaiting the owner's go/no-go.**
