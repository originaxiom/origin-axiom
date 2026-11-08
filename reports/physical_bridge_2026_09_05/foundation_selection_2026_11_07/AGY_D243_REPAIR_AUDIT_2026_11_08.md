# AGY d243e093f: source-level repairs and remaining proof failures

2026-11-08. Target `d243e093fc10b36cb0bb6df5fc979af64fffe2b4`.
Source read and author exact hand counterexamples, **UNREVIEWED**.
No target module import, collection, scientific execution or runtime
failure claim. Main remains `217e37c4f`; the latest all-branch fetch
made no further change. This is not a blanket audit of the AGY branch.

## Scope actually read and improvements preserved

Read the complete diff from `82d9d14af` to `d243e093f`, its changed relay,
the surrounding selector predicates/model data, T141 homology block,
T156 classifier and changed WP4 construction. The corresponding prior
audit is preserved at `e5a45fcfe`, and its finite-context F6 qualification
is preserved at `2896d441a`. That qualified issue is not reinstated here.

Useful repairs:

- The matrix now has distinct `carrier_gens` and `reg_gens`. P1/P2 are
  actually evaluated on the carrier matrices, rather than borrowing a
  Sanov output under an untyped finite-image name. This substantially
  addresses that particular type ambiguity for the rank-two rows.
- T156 inspects the actual producer source rather than hand-authored
  snippets, and its mutation changes an actual update. That is a real
  improvement in source provenance, with the limits below.
- T141 computes the stated homology-presentation ranks and a three-by-
  three Smith form. These are useful algebra checks under the stated
  topological presentation.
- WP4 removes arbitrary literal Higgs components in favor of the existing
  Serre-derived vector. This reduces arbitrary component choices in that
  declared model. It does not establish a unique physical construction.

No old conditional quaternion, tensor, theta or physical-bridge result
is erased by the following findings. The declared scoreboard stays 0/19.

## A. The F3 carrier is an F2 image with a redundant third generator

`p000_pure_logic_bridge.py:1051--1054` sets

    carrier_gens = [X,Y,X Y],
    reg_gens = [QI,QJ,QK].

The third carrier generator is a product of the first two. Thus the
nontrivial abstract F3 word x1 x2 x3^-1 is killed, and the matrix-generated
carrier is the same Sanov F2 as <X,Y>. The register assignments also obey
QK=QI QJ, so both matrix lists factor through that same relation.

If an abstract F3 remains the intended carrier, this is a nonfaithful
probe of it, not a realization verifying its free rank or all distinctions.
If the carrier means the matrix group, calling it F3 is false.

**Repair:** retain explicit abstract free-word equality for this control,
or use a genuinely free rank-three subgroup. For example an index-two
subgroup of the Sanov F2 has the Schreier basis X^2,Y,X Y X^-1 (kernel
of the x-parity map); its rank-three basis has no product relation of
the kind used here. Then assign the coefficient matrices independently
on that actual free basis and state which properties each test checks.
The earlier hand proof that rank is not forced does not depend on this
bad matrix realization and remains supported.

## B. P3's two-generator test is a universal trace identity, not its label

At lines 1002--1011, the rank-two branch only compares traces of
[A,B], [A,AB] and [AB,B]. But for **any** invertible A,B,

    [A,AB] = A [A,B] A^-1,
    [AB,B] = [A,B].

Their traces therefore agree identically. That numerical comparison cannot
test freeness, a universal automorphism-fixed primitive class, or the
all-rank theorem named by `universal_aut_primitive_class_n2`. It also
holds in abelian, nilpotent and other quotients.

The rank-three branch checks one triple trace against its product with
the first generator. One mismatch is a useful control on that particular
coefficient example; it is not an all-word/all-character classification.

**Repair:** use the actual source theorem with its complete hypotheses,
and label the finite trace identities as controls. Do not let a function
name upgrade one identity to a universal quantified premise.

## C. P4 does not test swap covariance or compute irreducibility

At lines 1013--1023 the routine checks a supplied list `irrep_dims` and

    tr[A,B] = tr[B,A].

For SL2, [B,A]=[A,B]^-1 and tr(M^-1)=tr(M). Hence this trace equality
holds for every SL2 pair, including ones with no generator-swap intertwiner.
An exact irreducible counterexample is

    A=diag(2,1/2), B=[[1,1],[1,2]].

Both determinants are one. The only A-invariant lines are its coordinate
axes and B preserves neither, so the pair is irreducible. Their generator
traces are 5/2 and 3. A swap intertwiner would conjugate A to B and force
those traces equal, which is impossible. P4 nevertheless accepts the
commutator-trace equality when `irrep_dims=[2]` is supplied.

**Repair:** actually solve the simultaneous intertwiner equations and
test invertibility, or use a complete representation-theoretic criterion
with its hypotheses. A declared block-size list is not a computed
irreducibility certificate. This does not invalidate the separately
exhibited odd-prime conjugate-pair swap intertwiner.

## D. The table still does not establish logical independence or selection

P5 at lines 1025--1037 explicitly tests dimension two, unitarity,
determinant one, and both generator squares equal to -I. These are
strong coefficient restrictions, not consequences earned by evaluating
them. The last two square tests go beyond merely lying in SU2, whose
unique order-two element is already -I.

The ladder still discards rows that fail multiple premises; it is not
the all-other-premises countermodel required for independence of each
one. Replacing assigned booleans by expressions does not repair that
logical quantifier. Nor does one survivor in six examples establish
uniqueness in the full category. The all-rank alternatives in our earlier
hand proof remain outside that comparison.

There is also a naming mismatch in M1: A_ab=[[1,1],[0,1]] and B_ab=A_ab^2
generate one infinite cyclic group, not a faithful rank-two free abelian
group Z^2. If `Z2` means Z/2, that finite group is not their image either.
This is an adequate commutative comparator for P1, but its scope needs
an accurate name rather than an incorrect carrier identification.

**Repair:** retain the table as a typed finite example filter; give any
logical-independence proof separate explicit models satisfying every
other premise. Keep fixed-sector and chosen-family predicates distinct.

## E. A homology matrix does not compute cusps or determine a filling

`toe_closure.py:25176--25207` obtains a Betti number from a declared
three-by-three relation matrix. The assigned presentation can support
that homology calculation. But the code then sets the cusp count to
one minus the indicator that the third column is nonzero, and infers
closedness from that value. This is not a topological cusp computation.

In particular Dehn filling along the homological longitude, which is
zero in H1, can close a one-cusped knot complement without changing
its H1 presentation. More generally a closed 3-manifold and a cusped
one can have the same H1. A zero column records a free homology class,
not a cusp. Filling along a nonzero class can explain a new relation
when the actual peripheral/filling map is supplied; the relation does
not derive that map backwards.

The three-by-three matrix alone also cannot identify a closed manifold
with the particular branched cover Sigma2(4_1). Preserve that as separately
supplied or verified topological provenance. The m004/m003/closed-cover
distinction remains useful; making its assumptions executable arithmetic
does not eliminate those assumptions.

**Repair:** explicitly name cusp/filling provenance and its actual map.
Use the matrix as a homology consistency check, not as a derivation of
the geometric carrier or its boundary topology.

## F. The provenance classifier still promotes unknown expressions

`toe_closure.py:29475--29501` labels any remaining Call or BinOp as
`FIRST_PRINCIPLES_RECOMPUTATION`, optionally if a supplied scalar residual
is small. It does not trace dependencies, bind the residual to that
assignment's equation or recognize the called producer. A static exact
counterexample to that classification rule is

    x = imported_pin + 0

or `x = load_saved_result()`: both fit those AST forms, although neither
recomputes the geometric/scientific quantity. Giving either the same
unrelated residual=0 also passes the classifier branch. These examples
describe the source's rule; no target AST function was executed here.

An unsuccessful recomputation with a bad residual is also not necessarily
an imported pin. It may be a failed solver; collapsing the two hides a
different evidence status. Actual-source inspection is an improvement,
but a syntactic expression shape cannot certify scientific provenance.

**Repair:** fail closed to UNKNOWN for unrecognized expressions, trace
their source dependencies, distinguish imported data, recomputation and
failed/uncertified computation, and bind any residual certificate to
the actual equation, producer, inputs and output under review.

## G. WP4 still supplies a joining law and a cutoff

`weave_unification_bridge.py:666--720` now uses explicit Teichmuller
palindrome points and Serre-derived h. However it also sets

    two_pi_L=4 pi log(phi),
    h0=sqrt(h_anti dot h_anti),
    S_down=adj(S_up),

and combines the anti-apex Higgs coordinates with a tube residue matrix.
No transporting bundle/frame, physical overlap integral or end/norm law
is derived in that block to identify their fibre coordinates and these
choices. Its call to h_tube is not used in that combination. A computable
constant or algebraic scalar extension is not automatically a forced one.
This is a conditional two-locus coupling ansatz, not yet parameter-free
physical realization. An actual cross-locus transport can change that
status if it is exhibited and justified in the same model.

The harmonic-time versus Teichmuller read-out distinction and P-744
duty in the preceding audit also remain. Haar basis invariance checks
the supplied matrices' basis covariance; it cannot derive their source,
identify two independently chosen fibre frames, or select a physical
boundary law. The positive mechanism and Serre construction should be
preserved with those assumptions visible.

## Interpretation and next action

This commit improves source hygiene and some conditional algebra. It
does not yet repair the selector proof, make the whole construction
parameter-free, or establish physical SM parameters. No claim of a
runtime failure or universal impossibility is made.

The corrective pattern is to test the proposition actually claimed,
including its quantifiers and carrier, instead of optimizing away literal
booleans. The immediate work is the typed model/predicate repair above;
the physical work is the actual transport/action/domain join. Our own new
affine D4 proof remains unreviewed and is not a substitute for that work.
