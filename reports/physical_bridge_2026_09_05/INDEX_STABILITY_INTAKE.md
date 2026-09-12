# R26 final all-head intake, September 12, 2026

Read-only intake after the completed R26 scientific runs and before
their reporting checkpoint. No branch merged, upstream source edited,
new census executed or received result independently certified.

## Pinned fetch

The all-head/tag origin fetch completed with exit zero. Two remote
heads advanced by fast-forward; the earlier paper-review forced update
and its retained old tip remain recorded in
[the preceding intake](RELAY_TRIAGE_2026_09_12.md).

    outside: a445e6575eba2c03921d0eabd957ec7764a7b231
          -> 24d73610c21848e83fb98e50df30e587a37999db
    paper:   8bf2c4439b0c4b5e575e749b507bb1b79918f9ef
          -> c83b6b802ee0e610a50ee07426ed610c2c6bd674

Other remote tips at this fetch (role aliases where a branch prefix
contains an attribution label; immutable object IDs are the identifiers):

    audit/b775-braver-questions 53da05f6c545edf62ba7ff6d7d001aa1c2642320
    audit/physical-bridge-2026-09-05 46b34c092a2eefa42ada025c66a18febfa12e630
    new-session-qor5up 3851df2aa683b67ba3f5c4976f4371c3bd22716e
    physics-seat-evaluation-8dkbrl 659487bbd93c7990c4686a8b86985b6b66efedc4
    standard-model-derivation-0qt6ao 1703c0d80b6ad4281de61feb882667515500e8e7
    seat-r001 f7a49536bc45bebc1557d3d081b6b3664a7c2199
    main b94ed03aecba8aae3afc62504e22ec664c26e94f
    paper/structure-genesis-first a31456d2d5e4f08723aa9cfabb7a8573cc2c13d4

The symbolic origin/HEAD points at the same main tip and is not an
eleventh branch. The R26 pre-execution retrieval remains pinned to its
original earlier heads; this intake does not rewrite that population.

## Paper-review changes: useful correction, not a universal zero theorem

The four new commits are b2e83f1d, 53ad98d0, 5a3be058 and c83b6b80.
The B1335 findings, B1332's two new addenda, and the paper-impact note
were read in full. The complete B1335 `verify_m010.py`, `index_lib.py`
and `char0.py` were also read. B1332's finding/verdict changes were
compared. This is not a read or rerun of every new scan and log.

[B1335](https://github.com/originaxiom/origin-axiom/blob/c83b6b802ee0e610a50ee07426ed610c2c6bd674/frontier/B1335_the_vanishing_is_not_formal_exhibited/FINDINGS.md)
reports an m010 Sym^3 character sector with nonzero index over finite
fields, within its stated algebraic domain, and zero for the examined
geometric characteristic-zero sectors. This is a positive candidate
counterexample to vanishing from the four identities alone, not a
physical chiral spectrum or a counterexample on a geometric cover of
m004. The chosen geometric SL2 lift's peripheral trace -2 explains
its odd-germ zero under the specified cusp-trivial twists; that does
not classify all representations, lifts or twists. Numerical singular-
value separation is evidence about the reported ranks, not an interval
or exact characteristic-zero certificate.

The [isotropy correction](https://github.com/originaxiom/origin-axiom/blob/c83b6b802ee0e610a50ee07426ed610c2c6bd674/frontier/B1332_the_cup_product_vanishes/ADDENDUM_reduction_needs_both.md)
is important independently of the census. Isotropy of one restriction
image gives an inequality, not half-dimension equality. Its dual image
must be isotropic too for the two bounds plus duality to force equality.
The received finite-field sector is offered as an explicit pointwise
counterexample. The class-wide two-sided route remains live.

The [broadened addendum](https://github.com/originaxiom/origin-axiom/blob/c83b6b802ee0e610a50ee07426ed610c2c6bd674/frontier/B1332_the_cup_product_vanishes/ADDENDUM_one_cusp_isotropy_broadened.md)
reports 106 sectors on six additional manifolds, 84 nonvacuous sectors
and 128 scalar conditions, and retains three earlier exact examples.
It records an initially vacuous scan and false counterexamples from
using the wrong class of invariant forms. Those repairs and positives
must be preserved; this intake neither reruns the numbers nor turns
the surviving isotropy question into a theorem. Its claim that isotropy
is the only possible route is not a completeness theorem established
by these samples.

Two code-level custody details matter before reproduction. The
self-contained finite-field script prints one selected sector after
enumerating to four representations; it is not itself the full census.
Its displayed `V == dual(V)` compares literal matrices, not module
isomorphism, so that display alone cannot exclude self-duality. If
the unequal cohomological counts are independently verified, they can
provide a different obstruction; the literal comparison is not it.
The characteristic-zero script imports `recog12` after inserting
`/tmp/sweep`. That helper exists in earlier arcs on the received
branch, but not beside B1335's new script. A rerun must pin and resolve
it explicitly rather than inherit an ambient temporary copy.
The referenced `verification/logs/` files are not tracked under B1335
at this tip; no missing log is represented as read.

The [paper-impact note](https://github.com/originaxiom/origin-axiom/blob/c83b6b802ee0e610a50ee07426ed610c2c6bd674/papers/P3_THE_PAPER/PAPER_IMPACT_2026-09-12.md)
still calls B1334 a proof on the identity component. The checked tree
diff contains NO B1334 change. The earlier intake's parameter-dependent
kernel/rank obligation is therefore not repaired by this update, nor
by adding numerical zero sectors. The extra scope duties concerning
global self-duality and nonparabolic even-weight invariants also remain.
That is an outstanding proof obligation, not a constructed manifold
counterexample to B1334. Its parabolic index is still not automatically
the R18/R19/R26 sourced singular Dirac index.

## Outside-bench changes: outputs, maps and an unproved universal inference

The two new commits are 137e3a66 and 24d73610. Memo 205 and both new
owner-register addenda were read in full; the certificate changes and
the new complete terminal-output portion were compared. The certificate
was not run here and its unchanged whole body was not reread in this
intake.

[Memo 205](https://github.com/originaxiom/origin-axiom/blob/24d73610c21848e83fb98e50df30e587a37999db/outside_bench/memos/L142_THREE_FACTS.md)
reports six named cubic readouts giving the same field, a negative
different-field control, inequivalent 27/78 modules, and unequal
simultaneous-conjugacy invariants for two ordered matrix pairs. Its
permutation conjugator controls genuine conjugation without the earlier
dense rational growth. The smaller cubic field model is compared with
the original rather than silently substituted. These are useful exact
control choices, received here rather than reproduced.

Keep the map types explicit: Schur excludes an E6-equivariant linear
map between those irreducibles; ordered-pair invariants address the
specified simultaneous conjugacy. Neither licenses a slogan excluding
every possible relation. Conversely, six equal field outputs and the
received trialitarian interpretation do not alone prove that every
construction on the charge space must return that field. That universal
sentence needs a map from each admissible readout to the claimed
structural invariant, not just agreement of the examples. This is a
scope duty, not a refutation of the six field computations or of a
possible common origin. The earlier commutant/center and quaternion
ramification duties remain as recorded in the preceding intake.

The new owner register distinguishes old rows from already executed
work and lists remaining mathematical computations. Its structural
chirality-without-inserted-closing target is narrower than a universal
absence of conditional chiral kernels. The R19/R26 prescribed-source
positive is not withdrawn by that register's wording. No outside
empirical prediction or completed physical TOE is imported.

## Disposition

R26's proof/source/test population is unchanged and its completed
scientific receipts stand at their declared scope. The new finite-field
and isotropy repairs strengthen the reason to type every vanishing
statement by operator, representation, field and domain. Next is still
one stationary source/end action and quantum completion; received
other-seat results are not independent certification of that work.
