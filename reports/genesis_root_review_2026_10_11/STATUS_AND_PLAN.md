# Genesis root review and work priorities

Date: 2026-10-11. Branch: `audit/fork-2026-09-20`.

The task is to strengthen the foundations, not extend the catalogue of candidate constructions. Read the existing results together, identify which are different presentations of one mechanism, and derive foundational conditions where the earlier premises actually entail them. A successful step removes a named independent assumption or establishes a previously unproved implication. More examples, a renamed assumption, or another occurrence of the same number do not meet that test.

This is an audit and work plan, not a new banked theorem or a replacement for canonical `GENESIS.md`. The reference is main at `6c148ddd495d133213140995976ff08849793d5d`, GENESIS v1.41. Its numbered premises and scope distinctions govern this review. The user's clarification puts conceptual consolidation ahead of the small auxiliary proof considered during the branch refresh.

## What the refreshed record changes

| Development | What the record supports | Limit relevant to the root review |
|---|---|---|
| Main B1634 and W50 | Main corrects the lift helper's sign error and identifies the weave's genuine metaplectic representation with the theta multiplier. The earlier “only projective” diagnosis must not be used as a standing obstruction. | The full representation calculation has not been independently rerun in this review. Its identification does not derive the physical link Λ or the end unit. |
| W45 and W46 as adopted in GENESIS v1.41 | Main records a chiral index of ±3 given Λ and one unit of cusp end data, with the multiplier issue repaired. | Λ and the unit remain tagged working inputs. An index conditional on them is not a parameter-free derivation of matter. |
| Physical branch through `8016cd2e3` | Its report connects the real bosonic quotient and harmonic Weyl modes within the same supplied parent action and boundary problem. This is more than an untyped cohomology count. | The report is read, not independently certified here. The parent, metric and boundary data remain supplied; no identification with the weave's holomorphic matter construction is assumed. Its successor at `9e434bfaa` is a preregistration, not another achieved result. |
| SM W52 and W53 | The seat counts remaining flavour freedom and reports poor fits in its tested geometry-weight ansatz. | A finite optimization campaign is not a certified global exclusion. Its outcome cannot kill other ansätze or the framework. The fit has not been rerun here. |
| Main B1635 and B1636 | Further coupling and golden-spectrum tests are registered. | The fetched commits are preregistrations, not results to build on. |

The live branch heads and the depth of reading are recorded in `REMOTE_HEADS.txt` and `SOURCE_SCOPE.md`. All ten advertised branch heads were fetched. Historical remote-tracking refs were retained. Fetching is not merging, and reading a report is not reproducing its claims.

## Patterns that deserve upstream attention

### A reference state need not be the physical state

GENESIS §4 already states that the root's torsion-free selector also leaves the root empty at its own level in main's named frame. It calls the root an origin of coordinates rather than a physical centre. This is not a new discovery in this review. It changes the question: how does the generated architecture acquire a physical realization, rather than how can every desired observable be extracted from m004 alone? It does not establish that another thread, the whole weave, or a sum over threads is physical.

### Repeated structures need a map before they become one mechanism

GENESIS §4 explicitly identifies the words and records routes as one construction in two presentations, not independent evidence. B1634 provides another, much more specific kind of connection: an asserted intertwining of representations, not merely a shared dimension or eigenvalue. Such connections are useful because they can transport constraints.

The working test for another claimed identity will be an explicit map of objects and allowed operations, together with its kernel, choices and domain. If two constructions merely share the labels “three”, “spin”, “chirality” or “E₆”, they are not yet the same physical construction. Repeated consequences of a shared input must not be counted as independent reasons for that input.

### Several physical conditions are currently packaged into one link

W27 states Λ as a field on spacetime times the shared fibre, in F-MC's 27, carrying a parity-twisted spin bundle, with sectors kept apart at the puncture and holomorphic zero modes identified as left-handed states. Those clauses can be recorded as one dictionary, but counting the dictionary as “one input” does not derive any clause. F-MC's typed inputs remain in addition.

The opportunity is to determine whether one construction already present in the record forces several clauses together. The burden is explicit: derive the field content, operator, domain and interpretation from the same earlier data. Importing these from different frames because they give compatible counts would not discharge Λ.

### A limited obstruction must remain limited

B1629's dated addendum corrects the inference from a uniform thread measure to “not dynamical”. The measured limiting cusp weight does not exclude other dynamics or measures. Conversely, an untested alternative is not evidence that the unit is derived. The cusp unit stays conditional until a specified upstream rule fixes it without choosing the desired index.

### A physical construction and its necessity are different achievements

The physical branch's same-action work is relevant and should be preserved. It tests whether a proposed completion actually supports the claimed fields. The genesis question is a further one: why that completion and those data? The current review must not erase the first achievement by calling everything “only mathematics”, nor answer the second question by pointing to the first.

## Dependency priorities

These are priorities for analysis, not claims that their answers are new or absent throughout history. Every detailed claim will receive its own prior-work sweep before an arc is opened.

| Priority | Dependency to examine | What would count as progress |
|---|---|---|
| 1 | GENESIS GM1–GM4 and the actual word-level lifts of L and R | Separate what follows from the count matrices, what needs faithful F₂ data, and what needs a surface realization. Recover an existing implication or prove a missing one from stated weaker premises; where alternatives survive, exhibit their exact differences. |
| 2 | GENESIS GAP1 and FK11, including the clauses of Λ | Trace each clause to its earliest mathematical inputs. Determine whether a single already-defined construction supplies more than one clause, with a typed map rather than matching labels. |
| 3 | End data, grading and hand in the weave's index | Reconstruct which parts are forced by the move action and which fix the domain or its integer datum. Test whether any recorded upstream rule determines the unit before the target “three” is supplied. Respect B1629's corrected scope. |
| 4 | The relation between the physical parent and the genesis | Check whether the parent action and boundary problem can be obtained from those same data. A comparison must specify fields, real structures, kinetic operators and domains before transporting a result between frames. |
| 5 | State and parameter selection | Only after the preceding choices are visible, assess whether the resulting structure fixes the modulus and couplings. Do not use a desired mass, family count or Standard-Model fit to choose an upstream premise. |

Priority is determined by how many downstream assumptions a derivation would remove, not by how attractive its numerical output looks. A counterexample to an implication can also clarify the root, but it closes only that implication under its stated premises.

## Concrete next deliverable

Build a dependency table for the proposed physical matter chain. For each arrow record its input type, output type, exact statement, earliest proof, current correction, and free choices. Begin with the passage from the integer-record grammar to faithful word data and its lifts; then follow the data into Λ and the end condition. Compare identities and assumptions across the routes before proposing any new construction.

The first auxiliary lemma has now been rederived in `word_lifts/PROOF.md`: B1634's already-stated inner-automorphism intersection for its exact lifts. The same packet classifies all four positive elementary pairs, proves they are simultaneously conjugate, and supplies the based bridge between the founding double tick and the later LR convention. Its sealed exact checks and nine control tests pass. This strengthens a load-bearing certificate and removes a redundant fixed-pair convention; it does not derive faithful F₂, positive word realization, Λ or the cusp unit. Normal independent review and banking remain pending.

The next dependency was tested in `bundle_transport/`: the existing parity cohomology and local puncture constructions do transport across that conjugacy, by different explicit maps, with 371 exact assertions passing. Their grading, algebraic triplets, extreme graded local subspaces and uniform pole order are preserved. This does not construct a physical operator domain or select Λ or the cusp unit. The fixed-pair action and the action generated by all alternative realizations still must not be conflated: their inner subgroups differ. See `word_lifts/FINDINGS.md` and `bundle_transport/FINDINGS.md` for their scopes.

The earlier carrier implication was then tested in `positive_carrier/`. A proper affine path quotient retains every positive description, its order, a nontrivial commutator and every substitution. Its elementary all-length proof and 8,234 passing exact safeguards show that these requirements do not alone force full signed-word fidelity. This strengthens the already-recorded R57 distinction without rejecting the conditional F2 surface theorem. The unrestricted universal group-completion property does select F2, but its necessity still needs an upstream justification.

The follow-up `cohomology_carrier/` tests the actual coefficient data. A metabelian quotient retains the Q8 point but kills its doublet H1; the proper quotient F2/F2''' retains that H1 and the full lifted six-dimensional move action. Thus a concrete signed-word distinction is needed, but full faithful F2 is not needed for this particular algebraic construction. The analytic descent and vanishing proofs have 3,626 exact safeguards passing on the second run, after a disclosed exact-expression comparison repair. The parity-character triplet and the quaternion doublet sum are kept distinct.

The passage from this retained algebraic module to physical field and end data was then traced through W27 and W45–W48 and compared with the physical branch's same-action reports. `cusp_connection/` gives a narrow positive realization: the existing Hodge line has smooth finite-action curvature with effective flux n on the modular base. The hand derivation and 136 exact checks distinguish this connection from an available flat trivialization. Identification with the discriminant frame retains an explicit modularity hypothesis. This strengthens the description of a supplied cusp extension but selects none: the specified energy favors zero if allowed, and unrestricted open metrics even permit real flux. It is not a four-dimensional matter-operator certificate.

The active next step is the physical coupling and end rule: does the already defined matter operator, or a determinant/anomaly line computed from it, require this tensor power and a nonzero integral extension? This is a question to audit, not a proposed anomaly mechanism assumed to exist. The dependency is itemized in `UPSTREAM_DEPENDENCIES.md`. Neither equivalent-pair enumeration, a larger quotient census nor a new list of flux candidates is an ongoing frontier. Publication certification of these local packets also remains owed.

The prepared puncture-symmetry check has now completed its first sealed run in `puncture_symmetry/`: 2,681 exact safeguards pass. Its proof rederives W28's existing commutant and scalar stabilizers and weakens a sufficient assumption: with joint move invariance retained, one specific order-two flat flavour sign excludes the intermediate subspaces; the full continuous flavour group is not needed. The sign also preserves the supplied interacting parent at its flat origin. The separate doubled Green-data model retains a continuous symmetry-invariant family unless its grading is imposed. These are conditional refinements, not a derivation of the actual physical end law, Lambda, or the cusp unit. The existing physical operator map and its distinct domain remain in scope.

Every claimed removal of a condition must state the old premise, the earlier premises that now imply it, the proof, and the surviving alternatives. If the earlier premises do not determine it, retain the condition rather than rename it as a derivation. Mathematical necessity within a defined model and empirical adequacy remain separate questions.

## The distinction guiding further consolidation

The October 13 [matter-line compatibility result](matter_line_compatibility/FINDINGS.md) passes 60 exact safeguards after its seal was pushed. In the supplied curved parent, fixed metric and superpotential tie the two diagonal flavour charges to (a,-a); their compatible line connections are dual. This removes independent charge choices within that specific coupling, not the supplied line or its sector. A common nonzero-curvature twist would require additional structure rather than silently preserving the same parallel pairing. The map from modular data to the physical operator and the selection of a nonzero sector remain the active duties.

The physical branch has now reproduced the five earlier packets at source `30fdb6a16`. A local replay of its separate-method reference passes all 30 predicates with byte-identical output; source and execution-log hashes also match. [CROSS_BRANCH_REPRODUCTION.md](CROSS_BRANCH_REPRODUCTION.md) records the checked scope, the later baseline reconciliation and the newer puncture packet that its earlier replay does not cover. This confirms the operator/end-law priority without creating a new physics result or a full-suite certificate.

The local packets separate different kinds of choice. A coherent insertion-order change is a convention when the full data are transported; the first two packets give the actual maps, so that convention should not be priced again as a physical freedom. Passing from positive descriptions to a group completion is instead a choice about which additional signed distinctions to retain; the carrier packets exhibit that difference and a weaker sufficient algebraic carrier. The cusp connection distinguishes a geometric realization from its selection: a smooth solution can exist without the action choosing its sector. Finally, identifying a resulting mathematical sector with a physical field requires an operator, domain and physical dictionary. An isomorphism or consistent realization does not settle those further questions.

This suggests a disciplined interpretation of recurring patterns: ask whether the recurrence is an identity transported by a known map, a property shared by inequivalent realizations, or a physical correspondence still requiring justification. These cases call for different work. The first consolidates results and removes duplicate choices; the second locates the missing discriminator; the third requires a common physical construction and tests. None is settled by counting how often an attractive number reappears.

The highest-leverage next derivation would make a presently independent downstream choice follow from an earlier, independently motivated rule. It is not established that one such rule will determine the carrier, Λ, the end unit and the action together. That is a research hypothesis to test, not a conclusion supplied by the ambition of the programme.

## Work disposition

### October 13 joining update

The [joining reconciliation](joining_review_2026_10_13/FINDINGS.md) incorporates the supplied handoff and the physical branch at `0b36fc3e0`. Gate 1's 17 reference checks and Gate 3's 43 exact plus 72 numerical checks reproduce here. More importantly, the branch already extended the scalar end calculation to the complete local eight-component zero-energy operator: both producers reproduce byte-identically here (26 and 14 exact predicates, with separately graded numerical controls). Recomputing that plane is not the next task. Nontrivial gauge transport changes the scalar response, and mixed channels prevent using transverse stiffness alone as a chirality verdict.

The physical branch also reports a four-real-dimensional finite-action lift of the supplied modular cusp connection for one metric. That report advances the base-only realization; it does not select the unit or certify the puncture/operator domain. Its newer neutral flat-line proposal is sealed, not a completed real-moment result at the fetched pin. The compact cover's conditional three-generation result must not be transferred to the noncompact exterior by matching labels.

The upstream priority is now sharper: preserve the information needed by the actual coefficient, justify the parent/end/state from earlier data, and use the existing full end plane in a same-field core join. Gate 1 proves a specific loss of information beyond the Q8 module; Gate 3 removes an independently assigned response only after choosing its exterior. Neither derives all those choices. The reconciliation lists the required background, framed trace, real-gauge and whole-field matching conditions before a global particle claim.

- The all-branch refresh and focused genesis catch-up are complete at the pins below. A full re-verification of all branches is not claimed.
- The pure-spinor boundary bridge draft is paused and preserved. It is unsealed and unexecuted.
- The previous charged-boundary result files are preserved. Their earlier verification does not establish a derivation from genesis.
- No canonical genesis status is changed by this report. No new B-number is allocated.
- The initial refresh was a reading-only audit. Its first follow-up now supplies the scoped word-lift derivations and exact controls above; it claims no physical derivation. Main still states zero of nineteen Standard-Model parameters derived.

The intended outcome is not a promise that a complete theory must emerge. It is a smaller, better-justified set of premises with more of the established mathematics following from them, and a precise account of the remaining bridge to physics.
