# Silver cusp boundary rule and the physical completion

October 4, 2026. The uniform pure holomorphic boundary rule does not
preserve the silver candidates' matching interior differences. The exact
run returns (-1,0) on W and exterior-square W, for all four candidates and
both conjugate cusp structures. The interior result (-1,-1) is reproduced,
not withdrawn. This is a result about a specified cohomological boundary
subspace, not a physical fermion spectrum or a universal chirality obstruction.

The consequence for the programme is a compatibility obligation: the law
that holds a candidate background must also determine an acceptable charged
domain. Admission and a favorable count from different domains cannot be
combined into a physical result.

## Exact result

The supplied PGL cusp matrices give tau=(1-i)/2 on the marked m135 inputs
and tau=-i/2 on the marked m136 inputs. These ratios follow from
Q-I=tau(P-I) after trace-two normalization. This does not independently
certify the geometric labels or complete hyperbolic structures.

Each row applies to both recorded characters and to tau and its conjugate.
Counts are allowed H1 dimensions for the bundle and its actual
inverse-transpose dual, in that order.

| Carrier | W allowed H1 | Exterior-square allowed H1 | Paired differences | Interior differences retained |
|---|---|---|---|---|
| m135 | (0,1) | (1,1) | (-1,0) | (-1,-1) |
| m136 | (0,1) | (1,1) | (-1,0) | (-1,-1) |

All split controls have differences (0,0). The original ordinary, relative
and interior profiles are reproduced by direct exact arithmetic over
Q(sqrt(2),i), separately from the earlier rational restriction-of-scalars
implementation. Relations, cusp commutativity, Fox identities and both
dual orders are checked before these counts are accepted.

The [proof](PROOF.md) explains the result for the chosen rule. On the joint
unipotent cusp sector put X=log P, Y=log Q. The image of closed pure forms
(u,tau u), modulo exact forms, has dimension

    dim L_tau = dim(ker X intersect ker Y) = h0(T;E).

The SAME-tau space on the linear dual is the full cup annihilator. This
does not assert a physical Hermitian adjoint-domain relation. B1509
Proposition E, explicitly credited, gives

    N_L = dim L - h0(T;E) + h0(M;E) - h0(M;E*),
    N_L_tau = h0(M;E) - h0(M;E*).

The last difference is -1 for W and 0 for its exterior square. Replacing
tau by its conjugate, or by any finite value in this pure-form definition,
cannot change that formula. This is not a scan over all physical domains.

## Controls that protect the conclusion

Removing one independent exterior-square boundary class and taking the
ENLARGED full dual annihilator gives difference -1 again. On m135 the
allowed pair becomes (1,2); on m136 it becomes (0,1). This is the sealed
arbitrary opposite control, not a derived boundary law. It demonstrates
domain sensitivity but cannot justify choosing a domain for its count.

The run checks marking covariance under (p,q)->(p,pq), global gauge
conjugation on one candidate and its exterior square, all split companions,
trivial and acyclic torus systems, and a unipotent comparator with unequal
dual invariant dimensions (1 and 2). The latter prevents a false universal
half-dimension assertion. A size-three Jordan control checks the nontrivial
correction between logarithmic and group cocycles. Noncommuting cusp inputs
are rejected. Closed representatives are quotiented by exacts before counting.

## Consequence for what an end law must see

This is a post-run authored consequence of the already banked Proposition E,
not a new preregistered population test or a novelty claim.

Suppose two global coefficient systems have isomorphic peripheral systems
and equal delta=h0(M;E)-h0(M;E*). Any prescription L that uses only those
peripheral systems and the same supplied cusp geometry, and pairs L with
its full dual annihilator, gives the same N_L on both. Both dim L and
h0(T;E) agree, so Proposition E proves the assertion directly.

This applies to the exterior squares of each silver nonsplit W and its
split companion. The preceding silver verifier checks that the chosen
extension cocycle vanishes literally on both cusp generators; exterior
powers therefore have identical peripheral matrices. The current run
reproduces delta=0 for both companions. Yet their interior differences
are -1 and 0. A rule based ONLY on the peripheral coefficient and cusp
shape cannot reproduce that distinction through this paired N_L.

The fundamental W is different: delta changes from 0 in the split case
to -1 in the nonsplit case. This explains why the pure-form rule retains
one asymmetry but loses its exterior-square partner.

This is a discriminator for proposed completions, not a theorem against
local physical actions. A local action can have a boundary metric, fields
or response determined by the global solution. Additional end states and
analytic operator domains are outside this finite prescription. A boundary
rule could also provide an asymmetry already in the split model. The
consequence states what must be distinguished if the aim is to preserve
the extension-dependent pair of interior counts.

## Next physical test

The [branch review](BRANCH_REVIEW.md) separates live work, old corrections
and remaining source-level defects. The target remains one bulk-plus-end
construction on an actual candidate:

1. State the action and which inputs OA actually derives.
2. Derive background equations AND boundary/source variations. A fixed
   Dirichlet metric supplies conditional admission, not its physical origin.
3. Obtain the charged operator and domain from that same completion, with
   full degrees, conjugates, normalizability and continuum contributions.
4. Test split, both ordered extensions and mixed directions under the same
   law. Use the peripheral-indistinguishability criterion before a large
   calculation that cannot answer the intended question.
5. Then interpret simultaneous sectors, interactions and anomaly balance.

If the end is another geometric piece, derive its response and the full
interface variations; matching values alone does not prove stationarity.
Do not substitute a kinetic response operator for a relaxed potential.
A smooth closed double may solve admission while retaining paired matter.
A singular or interacting completion is a distinct possibility, not an
automatic solution or something this test excludes.

## Execution and limitations

Initial design and code were sealed in ec523543a. Its native run passed
the comparator cell but was interrupted during costly generic number-field
conversion, before any full member receipt. Output and traceback remain
in NATIVE_FIRST.jsonl. The exact conversion repair was sealed in b6daa183b;
84 values agree exactly with the original converter before the candidate
run. No mathematical criterion changed.

NATIVE_SECOND.jsonl ends PASS, four members, exit 0. Six new tests plus
seven silver regression tests pass: 13 in 44.92 seconds. OUTPUT_HASHES.txt
pins both successful captures. Original and repair manifests remain separate.
No full repository suite, independent specialist review, physical domain,
empirical prediction or shared bank certification is claimed. The write-page
discipline kept results, post-run inference and proposed work separate.

The full physical goal remains active and unachieved. This removes one
ambiguity about how the pieces fit; it does not establish that a parameter-free
Standard Model or a theory of everything follows from the framework.
