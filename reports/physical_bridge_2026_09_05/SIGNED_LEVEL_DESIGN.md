# Signed powers and cyclic levels: pre-execution audit

October 2, 2026. Path-local R78, not a shared B-number or a physics claim.
This implements the membership/completeness stage of the committed genesis
reconciliation plan. R77's source-core drafts remain unsealed and unrun.

## Question, category and prior

Within the conditional signed once-punctured-torus bundle grammar, does
reducing an unsigned positive word to its primitive root and then attaching
the original sign to the root correctly reconstruct every signed monodromy
as an ordinary cyclic cover? In particular test U = -(LR)^2, already in the
entries [-5,5] window of B1516 C9. Inverse/sign legality and the surface
carrier remain premises, not conclusions of this audit.

Prior 95%: C9 will still report success while its implied signed-root/level
reconstruction fails for U. Prior 90%: U has exact fibre cokernel C3 + C3
and admits an interval-certified one-cusp hyperbolic realization. The
producer's count of failures in its declared window is an outcome, not
an expected universal count. A different named census identification is
not a failure; failed interval certification is not proof of nonexistence.

Two outcomes are retained: RECONSTRUCTION DEFECT VERIFIED or NOT VERIFIED;
geometry CERTIFIED or NOT CERTIFIED at the specified precisions. A failure
of our producer or test is preserved before any separately sealed repair.

## Received work and reused content

Read B1516 GENESIS.md, FINDINGS.md, its entire foundations producer, run
record and test file; read main B1434/B1439 findings and both population
producers fully. Their primitive positive-word census is a well-defined
restricted family. Their levels are explicitly (eps A(w))^k. B1516 C9
verifies conjugacy to eps A(w), but then assigns the unsigned primitive
root with sign eps and level k without testing that second equality.

The proof below addresses that interface, not the numerical index/slopes
of a previously computed background. No coefficient producer from main
is executed. No novelty or whole-repository absence claim is made: the
geometric witness may already be a familiar census manifold or appear
elsewhere under a different name. Exact-name prior-art navigation follows
identification before any such interpretation. R57's mixed trace bound
and distinction between legal inverse and invertibility are reused.

The foreign source is preserved byte-for-byte as a .txt snapshot, pinned
to its original commit, and imported under a non-main name. Only its
pure-integer check_census, check_generation, to_positive_word and matrix
helpers are called. Neither its main nor its record-writing mode is run.
Pins in SIGNED_LEVEL_INPUTS.json describe read sources, not independent
verification of all their results. No merge or write to another seat.

## Frozen computations and opposite controls

1. Exact integer A, A^2, U, positive control (−A)^2, negative odd power;
   trace/determinant, Smith invariant factors of B−I independently via
   entry gcd and determinant; enumerate all fixed mod-3 row characters.
2. Enumerate every mixed word of length 2..6. The authored trace bound
   tr A(w) >= length+1 makes this exhaustive for trace 7. Compare signed
   primitive candidates by homology, not just trace. This is a necessary
   invariant exclusion, not a general conjugacy algorithm.
3. Re-run the foreign C9 on its full box 5 and inspect all its reductions
   for sign-even reconstruction failures. Preserve its reported success
   separately from our additional predicate. Re-run the 758 census.
4. Check corrected triples (unsigned primitive word, length multiplier,
   sign) under ordinary covers, on all mixed words to length 6, both
   signs, multipliers 1..4 and cover degrees 1..4. A deliberately wrong
   sign-before-power reconstruction must be detected. This finite check
   safeguards the general central-sign power identity; it is not a full
   mapping-class classification.
5. Named geometry b+-LRLR, positive control b++LRLR and common cover
   b++LRLRLRLR: inside Sage, verify_hyperbolicity at 100 and 160 bits,
   exact homology, complete cusp counts, verified isometry signatures.
   identify() supplies names only; certify each selected census name by
   equality of verified complete-cusped isometry signatures. No Chern–
   Simons value, physical chirality or empirical observable is computed.

Commands after seal: signed_level.py, the one new test file, then
sage -python signed_level_geometry.py. stdout and terminal status are
captured outside the repository with capture_checked_run.rb. Byte hashes
and HEAD must remain unchanged during scientific runs; no bytecode/cache
writes in the tree. Seal this design, proof, inputs, both producers, tests
and snapshot, commit/push/server-confirm BEFORE scientific import/run.

## Allowed interpretation and outstanding duties

A defect would correct the architecture's signed-power bookkeeping and
the claimed scope of a finite completeness check. It would NOT withdraw
the 758-state results on their declared family, conditional LR minimum,
root selector, frame-specific no-go, or establish three physical
generations. Fixed characters are candidate coefficient data, not matter.

The repaired coordinates retain signs AFTER unsigned powers, with cover
map (w,k,eps) -> (w,kn,eps^n). Alternatively use signed-power-primitive
seeds; negative even unsigned powers cannot simply be discarded. No
unique normal form up to all conjugacies is claimed. The signed frame
itself is conditional on admitted sign moves. Analytic proof review,
recipient reconciliation, actual coefficient/action/domain admission and
the original full Standard Model/TOE goal remain open.
