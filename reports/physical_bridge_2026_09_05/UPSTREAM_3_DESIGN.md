# Third upstream audit — fixed elements are not fixed subgroups

P0 / BANKED IDENTITY: this audits B1259's inference, on its fetched source at
9a79adfdee23e6dfde8b9f2b12515a314c896b13, against explicit finite linear
groups. It does NOT compute a chiral spectrum or claim that a flat orbifold
realizes the Acharya--Witten mechanism. B1084's order-96 group and census
are prior positive results, not to be killed by correcting their reading.

P1--P4: the ladder X33, B1084's full findings and both producers, B1105's
full scope audit, B952's full earlier rank warning, LAW_MAP/OPEN_LEADS and
B1084's routed kill/hatch have been read. Already-banked query `flat
orbifold isolation`: 74 hits, three settled matches (B1084/B1105/B952).
The all-head intersection/isotropy search is a presence lookup, not proof
that no earlier correction exists. R8's EXTENSION_6 remains a DRAFT,
UNSEALED and UNEXECUTED while this potentially over-wide kill is checked.

## Exact control, before execution

On R7 use the seven nonzero F2^3 characters. For a in F2^3, set
g_a = diag((-1)^(a dot v)) over v=1,...,7 in binary order. Verify:

- all 64 products, eight distinct elements, orthogonality and determinant +1;
- preservation of phi=e123+e145+e167+e246-e257-e347-e356;
- the induced metric via (i_i phi wedge i_j phi wedge phi)/6 is exactly I7,
  so this is the compact G2 stabilizer of a POSITIVE form, not just SO7;
- enumerate all subgroups, and compute EACH common fixed space by stacked
  exact rank AND the Reynolds projector, independently of the character count;
- each nonidentity element fixes a 3-plane, while the whole group's fixed
  space is zero. Predicted subgroup orders/fixed dimensions: 1/7,2/3,4/1,8/0;
- generic points in planes/axes and the origin have the corresponding
  pointwise isotropy. The maximal-isotropy stratum is just the origin, but
  this is NOT an isolated point of the entire singular set.

Bad controls: an SO7 diagonal sign change that does not preserve phi must
fail the G2 check; retaining only one generator must leave a positive fixed
space. A verifier that only asks whether each element has eigenvalue one
must accept the counterexample, demonstrating its logical blind spot.

## The actual B1084 group, not just a generic example

Rebuild three stated generators independently in SymPy: left -1 on H,
g_tau and g_sigma. Check their common fixed space exactly by stacked rank.
Replay the pinned float producer without edits, capturing its full stdout.
Check the new exact generators against its actual group, all 96 actions,
the old {3:53,1:42} element census, 30 A1 planes, and each plane's intersection
with the E6 R3. Preserve the line intersections even if the full-group fixed
space is zero. Do not import the slow exact producer just to reprint its
verdict: its source is read, not a fresh execution receipt.

Replay the fetched B1259 selftest verbatim in a child process; preserve the
stdout and exit code, but do not equate a passing element test with proof
about subgroup strata. Sources are pinned and output refuses overwrite.

P5/P6: seal design/code/tests by hash and local commit BEFORE execution.
Honest prior: the element lemma is correct, but the inference to all
enhancement strata is not licensed. An exact G2 counterexample is expected.
The independent original-group calculation may show the same distinction
already inside the banked model. All failures will remain visible.

## Physics fence and adjudication

Keep three meanings separate: Fix(g), common Fix(H), and an isolated
non-orbifold enhancement with an actual localized chiral index. The elementary
SO(odd) lemma rules out an isolated point of the total singular set of a
nontrivial linear quotient. It does not alone exclude a zero-dimensional
isotropy stratum inside positive-dimensional singular loci.

Primary literature read 2026-09-06: Witten hep-th/0108165 introduction and
section 3; Acharya--Witten hep-th/0109152 section 2 (the actual Dirac/local
unfolding mechanism); Acharya--Gukov hep-th/0409191 sections 3.1 and 5 opening.
The standard mechanism has further geometric, gauge and index hypotheses.
Finding a zero-dimensional isotropy stratum does NOT satisfy them. A flawed
proof must not be repaired by asserting the opposite physical theorem.
