# Current source findings and limits

2026-11-17. Evidence: source inspection and hand arguments, not independently
checked by scientific execution in this reading. Exact excerpts and source
lines are in QUOTATIONS.json. No assertion below is a universal exclusion.
The X-FOUNDATION target is 017266d878ea366b3fb064f14ea7c17e8274a222.
The final loop head 48a4054aa adds disclosures and answers, not producer
repairs. Both new notes were read in full. Its acknowledgement of all
fifteen prior X-APEX findings is retained as a builder response, not an
independent mathematical check. The new XF-01--XF-06 items are separate.

## MAIN-01 — the partial-trace sentence misses a factor two

Source: main f2f019621, unchanged at e9ed81182,
frontier/B1953_frame_cs_down_coupling_is_the_symbol_of_one_covariant_operator_on_families_times_the_weil_space/FINDINGS.md,
lines 30--31 and 76--77; verification/exact_facts.py, lines 18--24.

The page correctly states tr D(v)=0 and tr(D(v)P)=1 and uses
6Y=(I-5P)/2. But it then identifies the phased sum F with the trace
of O3, and minus the trace of O2. From P3=(I+P)/2 and P2=(I-P)/2,
linearity gives tr O3=F/2 and tr O2=-F/2. The other identity on the
same line, tr_W(O 6Y)=-(5/2)F, is correct.

This can also be checked without numerical arithmetic on each actual
displacement: D(a,b)=zeta^(3ab) X^a Z^b, and the trace of D(a,b)P has
its only contribution at 2x=a mod 5. Its phase is then one. The trace
of each nonidentity D(a,b) is zero. Thus each partial trace is exactly
one half, not one. This is a hand source check, not a new executed test.

Required correction: replace the prose by twice the partial trace (or
half the phased sum), and carry the factor into any physical normalization.
It does not change modular covariance or the displayed traced-Gramian
computations. This plan's first uncommitted projection section repeated
the erroneous sentence; it is preserved in preserved_draft_01/ and
corrected to -(F/12) tensor 6Y before delivery. No own proof is being
independently certified by this correction.

## XF-01 — the two finite chirality matrices are not an adjoint pair

Source: relays/x_foundation_1_verify/verify_x_foundation_1.py,
lines 334--343, 399--402 and 452--455.

The lowest channel uses an n_y by (n_y-1) matrix, imposing zero values at
both artificial endpoints. The other chirality is rebuilt with the
opposite derivative sign and the same shape and endpoint restriction.
It is not the transpose/conjugate transpose, whose shape is reversed.
The kernel helper counts small values in the returned singular-value list;
it does not compute the omitted cokernel of a tall matrix.

For the continuum scalar operator d/dy+M with domain H1_0 on a finite
interval, integration by parts gives the adjoint differential expression
-d/dy+M with maximal H1 domain, not H1_0 again. Using the latter for both
signs is not a compatible finite-boundary index problem. An infinite-line
limit may have the intended index, but that requires a domain/convergence
argument; counting two separately restricted matrices does not establish it.

Required correction: distinguish the finite localization diagnostic from
an index, derive the actual adjoint/domain pair, and certify its relation
to the complete operator. This does not refute domain-wall localization.

## XF-02 — three copies and a model neck are supplied

Source: the same script, lines 285--306, 321--343, 413--424 and 449--459.

The code creates k copies of the lowest monopole or Landau channel and
calls the cusp routine with k_flux=3. Its radial model starts on a
spherical-monopole half-line; its cusp model is a truncated R times torus
neck with a tanh mass and a cylindrical negative-y side. Neither code
constructs the figure-eight's compact core, transition functions or
actual global Dirac operator.

The root/period computation is separate. Divisibility of a pure-Q loop
by three is not a derivation of flux three, nor of its identification
with the SM family index. Zero, higher multiples, the other sign and
compensating U3 lifts remain alternatives. Lines 154--168 themselves
demonstrate a primitive compensating loop. Main B1956 already records
the input-selection issue; this reading identifies the matrix source.

Required correction: keep the model's localization evidence conditional
on its inserted channels and field. Obtain the global representation-valued
index only after constructing the carrier, bundle, source/action and domains.

## XF-03 — zero total trace is not a core bundle construction

Source: the same script, lines 170--189, especially 188--189; the stage-one
result note, executive item 1.

The program checks the presentation's cohomology and the scalar equality
3+3*(-1)=0. The equality is a necessary trace-flux compatibility check,
not the construction of L_(+3) plus E_(-3) over the complete m004 core.
In particular, the claimed nonzero-degree boundary eigenline cannot extend
as an everywhere-defined line subbundle on a carrier with H2=0. A full
non-Abelian bundle and Higgs field can have nontrivial asymptotic eigenbundles
while that splitting fails in the core; their extension and dynamics must
actually be supplied or derived. The trace check proves neither.

Required correction: exhibit that extension and the Higgs degeneracy/core
data, or state that only the boundary trace test was performed. No
non-Abelian extension is excluded here.

## XF-04 — the order-four cover match follows an assigned coupling

Source: relays/x_foundation_3_verify/verify_x_foundation_3.py,
lines 491--509; stage-three result note, executive item 3.

The code pairs the hyperbolic matrix M=LR with the independently imposed
order-four shear and then finds the least k for which i^k=1. It computes
the torsion of M^4-I correctly as a separate arithmetic check. It does
not derive why one physical monodromy step must transport the register
by that shear, nor a full compatible action of the two native moves.
The preceding lines explicitly retain the second-move exit obstruction.

Required correction: call this a conditional product/transport construction.
The fourfold cover exists; its emergence as the required physical joining
is unpaid. The underlying C7 proof is this lane's own work and is not
independently certified by this reading.

## XF-05 — the scale-rank witness omits its free prefactor

Source: relays/x_foundation_4_verify/verify_x_foundation_4.py,
lines 283--298 and 4700--4709; stage-four result note, Part 4A item 1(iii).

The 20-column matrix adds a row fixing a difference of two log scales.
The stated physical relation is instead

    log(v/M) = -a Vol + log(c_NP),

with c_NP explicitly left open. When log(c_NP) is an independent variable,
the extra equation introduces that variable too. For any chosen v/M,
c_NP=(v/M) exp(a Vol) satisfies it. Thus this equation alone removes no
independent hierarchy input. The rank result for a fixed right-hand side
does not count the full declared model's freedom.

Required correction: retain c_NP as a column/independent input, and derive
both the instanton action and its prefactor before claiming a reduction.
The source already discloses the prefactor; its numerical rank witness
must carry the same condition. The fixed-constant rank identity is not
being disputed.

## XF-06 — positive endpoint quartics do not certify a complete no-go

Source: the same script, lines 3437--3450 and 3548--3549; stage-four
result note, Part 4A item 1(i).

The collected lambda values are returned final-scale values. A positive
minimum over these endpoints does not prove that lambda never crossed
zero at an intermediate scale. Nor is a zero crossing by itself the
general stationary-point condition for an effective potential. For the
explicit simplified ansatz V(phi)=lambda(log phi) phi^4/4, differentiation
already requires 4 lambda+beta_lambda=0; anomalous dimensions and thresholds
need their own treatment in the actual model.

Required correction: limit the result to the computed endpoints and
trajectories actually checked, or supply a complete monotonicity/flow
certificate and the relevant effective-potential stability analysis.
This neither establishes nor excludes a radiative hierarchy here.

## SM-01 — retain the finite scope of the action-weight negatives

Source: SM head 6ea836f560846d9e6aadb3bb715f1b862410c5c0,
relays/sm_c16/run_c16.py, lines 33--44 and 99--105;
relays/sm_c17/run_c17.py, lines 38--48; the two corresponding result notes.

The population is 3000 random mixed positive words of length 40 from one
declared seed. The real-weight test uses six sigma values. The phase
test uses k in {0,1,2} and seven sigma values. These calculations can
constrain those tests. They do not prove a statement about every
coefficient, every allowed word, alternative legal moves, or the measure
of an interacting physical history sum.

Required scope in any reuse: no cusp-favouring outcome was found under
the specified populations, grids and diagnostics. Preserve the measured
test failures and useful finite evidence. A universal closure needs an
additional argument; reversing a sign merely to improve an outcome would
also require a new, explicitly derived physical prescription.

## END-01 — the table's lower-domain fallback is unflagged

Source: main f2f019621b0014ed4d0b595077c5a1ac64fa0025,
frontier/B1927_the_canonical_end_is_covariant_the_read_out_needs_no_chosen_end_and_analyticity_picks_the_length_two_horocycle/verification/canon_readout.py,
canon(), lines 35--46. Already registered as P-864.

If linear interpolation is nonfinite, the function returns the nearest
value. Its only extrapolation flag tests y>YMAX. A point below or outside
the convex hull can therefore use nearest interpolation without a flag.
The code source confirms that cause; the reported numerical discrepancy
in P-864 was not recomputed here.

Required correction: enforce the certified domain, or reduce and carry
the end, marking and other data together with a valid error bound.
Record affected calls first. A global cancellation of all existing
results does not follow from this defect.

## Earlier findings still relevant to the current master script

The exact difference from the fully read X-APEX-4 source to X-FOUNDATION-4
is in FOUNDATION4_SOURCE_REUSE.json. The Dirichlet-tail gap promotion
(current line 4545; earlier XA-04) and the selected-point sector scales
in the alleged zero-bit averaged IR trajectory (4162--4170; earlier XA-11)
remain. A new row or a stage-wide green flag does not discharge them.
The prior X-APEX report and its first-failure evidence remain versioned.

## Primary literature used for the operator requirement

Personally read: Cecchini, sections 2.11--2.18 and 3.3 of
[Callias-type operators in C*-algebras and positive scalar curvature](https://arxiv.org/html/1611.01800v3).
The theorem requires admissible complete-manifold data and computes an
index through the positive asymptotic eigenbundle. It does not turn an
arbitrary finite neck into the original global operator. This is a
hypothesis checklist, not an application already earned by the programme.
The whole paper and its generalized C*-module proof were not audited here.
