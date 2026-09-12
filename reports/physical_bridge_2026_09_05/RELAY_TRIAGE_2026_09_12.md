# September 12 branch intake and proof obligations

Status: READ-ONLY TRIAGE, not an independent reproduction of the
other seats' experiments. No B numbers allocated, no merge performed,
and no change to the retained R26 prior. Reading-born objections below
are proof obligations, not preregistered experimental verdicts.

## Custody

Fetched all remote heads and tags at 08:52 UTC. Main remains
`b94ed03aecba8aae3afc62504e22ec664c26e94f`. Two tracked heads changed:

| branch | earlier observed head | current fetched head |
|---|---|---|
| claude/outside-bench | 4d481751b056030e695a68cb1ace4bfd8e5bdb8d | a445e6575eba2c03921d0eabd957ec7764a7b231 |
| claude/paper-verification-ufp0zn | 67f939cc8cc11b9018283e994a847268b05ab43b | 8bf2c4439b0c4b5e575e749b507bb1b79918f9ef |

The latter was reported as a forced update. Recording both IDs does
not certify that every prior artifact survives in the new history.
The log and changed-file lists were inspected. All newly changed
files have NOT been read or reproduced.

## Index branch: the claimed deformation proof

Read in full at the fetched head:

- `frontier/B1334_the_deformation_proof/FINDINGS.md`;
- `frontier/B1334_the_deformation_proof/ADDENDUM_what_is_left.md`;
- its `verification/index_lib.py` and `verification/mc_lib.py`.

The retained positive is the explicit distinction between one and
several boundary tori, the duality identity, the actual independent
coboundary block on each cusp, and the restrictions on a cusp-trivial
character family. The addendum corrects the body's claim that every
one-cusped manifold has zero-dimensional such a family: the relevant
condition is b1 minus the number of cusps. These are not to be lost.

Two steps need additional justification before the claimed general
vanishing proof is accepted here.

First, the Laurent-polynomial Fox Jacobian is not the matrix called
R in the code. `h_star` takes `Zs = nullspace(J, ...)`, and
`analyse_mc` constructs R by restricting those cocycles. A basis of
ker J can change size or develop poles as the parameter changes.
Thus the asserted global lower semicontinuity of
rank(R + Bt) - rank(Bt) does not follow merely from polynomial
entries of the original Fox matrix. On a constant-rank stratum one
can choose local frames; extending that argument through jumping
loci is a separate duty. The generic-open argument alone does not
establish the claimed conclusion at every special character.

Second, the theorem states only boundary self-duality of W, whereas
its use of inversion in the duality identity needs an identification
of W* with W on the whole manifold, or an equivalent justified
family symmetry. Symmetric powers of an SL2 representation do have
the needed global self-duality; the broader stated hypothesis does
not supply it. Domain D's H0 equality must also accompany use of
I = t0 - r1, rather than being silently dropped from the theorem.

The addendum's claim that deforming parabolic holonomy to loxodromic
holonomy always removes peripheral invariants also needs a parity
check for Sym^m: even symmetric powers have a zero-weight monomial.
In addition, a lift of a parabolic PSL2 holonomy to SL2 may have
eigenvalues -1, so the statement that every eigenvalue is 1 needs
its lift and parity conventions. None of these checks can be
replaced by a sample restricted to parabolic holonomy.

These observations do NOT show a nonzero manifold index, disprove
the sampled zero results, or prove the proposed theorem false on
its intended narrower domain. They prevent promotion of a proof
step whose hypotheses have not yet been demonstrated. The next
bounded check should distinguish a generic matrix-family control
from an actual three-manifold counterexample; the former can expose
a missing inference without settling the latter.

This I = n(V) - n(V*) for parabolic cohomology is not automatically
the same operator/domain index as this branch's singular-source
R18--R25 construction. Transferring a no-go between them requires
the chain/operator map, end conditions and representation data.

## Outside bench: arithmetic triality

Read `outside_bench/memos/THE_OBJECT_IS_6D4.md` in full, including all
four addenda. This records a claimed arithmetic D4 type and field
extension analysis, then explicitly reproduces B1077 and withdraws
the apparent conflict: the bare octonion norm and the dressed
centralizer are different objects. Its final quaternion-algebra
question remains a reduction, not a completed calculation.

The main claims, input matrices and primary-source hypotheses are
not independently reproduced here. In particular, a cubic field
inside a commutant must not be silently identified with that
commutant's center without the needed argument. This intake neither
promotes the triality claim nor kills it. The distinction between
bare and dressed objects, and the finite-field versus rational
splitting distinction, are retained for the later audit.

## Mission effect

The new branches do not authorize a global statement that chirality
is impossible. Nor has their intake supplied a physical action,
normalizable anomaly-free full spectrum or empirical prediction.
Finish the direct paper-transfer assessment, then keep the existing
source/end/index-stability path. Any additional calculation from
these relays needs its own seal, controls and exact scope.
