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

The first candidate auxiliary lemma is a self-contained proof of B1634's already-stated inner-automorphism intersection for its exact lifts. It could strengthen a load-bearing certificate without invoking the braid-kernel theorem, but it would not derive the lifts, faithful F₂, Λ or the cusp unit. It has not been executed or banked in this review and is not the headline objective.

Every claimed removal of a condition must state the old premise, the earlier premises that now imply it, the proof, and the surviving alternatives. If the earlier premises do not determine it, retain the condition rather than rename it as a derivation. Mathematical necessity within a defined model and empirical adequacy remain separate questions.

## Work disposition

- The all-branch refresh and focused genesis catch-up are complete at the pins below. A full re-verification of all branches is not claimed.
- The pure-spinor boundary bridge draft is paused and preserved. It is unsealed and unexecuted.
- The previous charged-boundary result files are preserved. Their earlier verification does not establish a derivation from genesis.
- No canonical genesis status is changed by this report. No new B-number is allocated.
- No new mathematical or physical derivation is claimed from this review alone. Main still states zero of nineteen Standard-Model parameters derived.

The intended outcome is not a promise that a complete theory must emerge. It is a smaller, better-justified set of premises with more of the established mathematics following from them, and a precise account of the remaining bridge to physics.
