# Independent P210 source and proof review

Reviewer: `p210-independent-nonauthoring-reviewer` (a separate reviewing
agent, not an author of the reviewed scientific sources).

Requested by the owner and assigned by the physical-bridge seat. The earlier
interrupted review attempt stopped at a usage limit and produced **no verdict**.
This document records the subsequent completed, bounded source review.

## 1. Decision and its boundary

**Frozen packet decision: APPROVE_EXECUTION.**

This approves the proposed ten bounded exact reconstruction/control methods
in the specification sealed at
`39ce620a82e5373d5f07eee91a6a7cbfd4cdd4f7`, subject to the existing genuine
main-acceptance, prospective-admission and clean-custody requirements. It
does not approve a physical realization, an index theorem for the complete
cusp, or the later notes as additional executable tests. There are no
unresolved changes required **for execution of this bounded packet**.

Specification:
`reports/physical_bridge_2026_09_05/word_architecture_audit_2026_10_17/verification_p210/SPECIFICATION.json`.

SHA256:
`f33348144c91711b0bcc3a05cf62974aac28a468eb57181f1ea6dfc93077f948`.

**Main acceptance is absent from this review.** No admission document was
constructed, no scientific module was imported or collected, and no
mathematical test, producer or repository aggregate gate was run. This
Markdown review is not, by itself, the separately committed structured
review/acceptance/admission chain expected by the executable gate.

## 2. Custody, independence and coverage

The review read the entire narrative design, execution-review duties, ten
method implementation, production wrapper, frozen v3 runner, strict gate,
tracked-state inspector, base prospective gate and provenance policy. It
also read the full gate registry/implementation, its six local check-module
dependencies and the view generator. None was executed.

All six analytical inputs directly listed in the specification, all five
listed older proof bodies, and the listed puncture producer were read. The
environment, historical source inventory, engineering design, six synthetic
fixtures, all four recorded fixture outcomes and their two repair notes
and environment-discovery note were inspected. This covers every one of
the specification's **39 artifact records**, in addition to its design.
The environment pin is repeated in its separate environment field; it is
not an additional independent artifact.

Read-only metadata checks independently established:

- the committed specification at the sealed commit has the SHA above;
- all 41 design/artifact/environment pin occurrences match the files read;
- neither reserved `results/attempt_01` output exists;
- the frozen `verification_p210` files have no diff from the sealed commit;
- both later custody manifests' local-file hashes match;
- all three historical Git-source hashes in the realization custody file
  match the named blobs at
  `3bf82d0ca08284a631016b217e0b9297a756f8ff`.

The metadata operations used file reads, JSON parsing and cryptographic
hashing, not mathematical-module imports. The inherited staged-only diff
still had SHA256
`1b1174453bc7f3159582386919a082dc803c0e9d63323a375872d4d346ba3786`
at the custody check. No existing source or staged file was edited.

Important executable pins independently inspected include:

| Source | SHA256 |
|---|---|
| P210 `checks.py` | `70d441f672228f6bbf9bb22e869a3575e6082d3002c7be044ad1c15c642b5a58` |
| P210 `run_checks.py` | `04682dc98cb80d9c123a942e0ace77105b281daa436c0e2b3ca9a713c0f484e9` |
| frozen v3 `run_checks.py` | `1cc1c9e299be3f85df41d066b2673c2c62b33e83ad978603f769cf04fd8adbf0` |
| `scripts/gates/prospective.py` | `f1f446846d07cbdb649eb04cc0971ad6f5fc1bc89a85493203b3f2ede0c52065` |
| `scripts/gates/prospective_strict.py` | `82985893d0db217514f7acfa5e676089e14eed30c6d98b0e6f22770fc4533f26` |
| `scripts/gates/tracked_state.py` | `22ac6ab65ed48fa5e1aeb92f74a9c7215ae4bf61825749a1ce66ce81854cc7f1` |
| P210 engineering fixtures | `4002fc024eabcd762ba7144e82299a1dd44aaa7ebe7f88b239a0abd646af13e6` |

The complete artifact pin population is the exact specification above,
not a newly transcribed replacement inventory. Its live governance reads
also use the repository corpus, policy ledgers and Git history. Those are
execution context, not a claim that 39 individual artifact records freeze
every file of the repository. A clean future execution tree and changes
after sealing still require inspection by main.

This review does not independently re-prove every theorem or numerical
claim cited by the older input proofs. Their global PDE, parent-theory and
physical identification statements are explicitly conditional inputs to
this packet, not conclusions tested or newly certified by its ten methods.

## 3. Mathematical review of the frozen packet

### 3.1 All null planes, the state stabilizer and grading

For the declared positive Hermitian coefficient space, the change
`a=(u+v)/sqrt(2), b=(u-v)/sqrt(2)` takes the two-slot Green form to
`a†a'-b†b'`. Projection of a six-dimensional null plane to `a` has
zero kernel, because a vector with `a=0` has `b†b=0`. It is consequently
an isomorphism, and nullness is precisely unitarity of its graph map
`b=Ua`. This establishes the full classification, not just the finite
Cayley chart tested in code.

The two quaternion generators on the second tensor factor generate
`M2(C)`. Their full complex commutant on `C3 tensor C2` is
`M3(C) tensor I2`; the implementation independently sets up all 36
unknown matrix entries and checks nullity nine, then exhibits nine
independent matrix units. It correctly preserves nonscalar family
freedom. Unitarity reduces the graph maps to `C tensor I2`, `C in U3`.

Gamma exchanges `a` and `b`. Its graph is invariant exactly if
`U^2=I`; with U unitary this is equivalent to U Hermitian. The plus
coefficient space then has rank `2r`. The displayed values
`2r-3` are **conditional sheaf/finite-distance index bookkeeping**,
not physical cusp indices. The proof and implementation keep that
qualification. The four sign-count multiplicities are correct.

The Cayley matrices have no denominator zero for Hermitian H, since
`1+i h` cannot vanish for real h. Substitution gives zero Green pairing
for `v=iHu`; the wrong real graph gives `2I`. The H=I null graph is
not Gamma-invariant: its Gamma image is the opposite graph and their
combined span has full dimension twelve. Thus the separate grading
control is genuinely discriminating.

The stabilizer is correctly scoped to the **declared** `(tau,S,M)`
action and the same action on both slots. At `S=I, M=epsilon^-1`,
the stated inner lifts fix these matrix coordinates. This is not a
proof that they fix every realized physical background. The proof
explicitly retains that distinction and the possible additional
register, geometric, spin and coefficient data.

### 3.2 Actual coupling rather than an invented mass matrix

The contraction in `checks.py` matches the ordered `(j,i,k)` basis,
epsilon and entrywise bilinear contraction in B1659's actual `Ysym`
and B1656's actual `coupling`, read at the historical Git pin above.
The paper's relevant fibre-frame, point-rank, norm and joint-law
sections were also inspected.

At the formal input `(I,epsilon^-1)`, use
`C_a^T epsilon=-epsilon C_a` and `(epsilon^-1)^T=epsilon` to reduce
the contraction to `tr(C_a C_b)=-2 delta_ab`. Hermitian conjugation
would not give the same ordered row identities; the actual implementation
uses transpose and preserves the bilinear law. Its altered-M controls
give different matrices. This is a valid exact algebraic recovery.

Neither this bilinear triplet coupling nor `Y†Y` is an exhibited map
between the two six-component normal Green slots. The packet does not
claim that identification. Also, a formal input of the universal matrix
law need not be a realizable single-point residue; see section 5 below.

### 3.3 Covariance and paths

For unitary g and unit-modulus alpha,
`H2(alpha g S g^-1)=g H2(S) g^-1` follows directly by multiplying
the transported Gram matrix. The four stated lifts are unitary, so the
use of `.H` for their inverse is valid. The three states, four lifts,
two phases and two family permutations do give 48 cases. The deliberately
frozen line at `diag(2,1)` is exchanged by j and fails as intended.

For any unit Pauli direction n, the complementary projectors onto its
eigenvalues are orthogonal. The positive root
`sqrt(1+t) P+ + sqrt(1-t) P-` squares to `I+t n.sigma` and tends to I.
Its normalized positive spectral line is independent of t and switches
to the orthogonal line for -n. The discontinuity assertion therefore
has an analytical proof beyond the six signed axis controls. The 18
finite checks are accurately scoped; they do not assert continuity of
infinite-dimensional operator domains.

The actual normal-frame note also retains the ramification derivative,
metaplectic/spin and root multipliers. Its three maps satisfy the
principal-parts diagrams by direct cancellation of their scalar factors.
For the Green pairing the positive and negative slot factors are
`jr` and `conjugate(jr)`, while `d'=(jr)^2 d`; substituting into
the displayed off-diagonal pairing cancels them. The raw covariance
checks do not pretend to test these complete geometric maps.

### 3.4 Both-slot operator and threshold

For the specified constant-tail comparator,
`D=-i sigma1 partial_t-sigma2 tensor K` with K Hermitian, the derivative
coefficient is skew-Hermitian and the zeroth-order coefficient is
Hermitian. Its Hermitian normal current is sigma1, up to the common
orientation/normal factor, and Gamma anticommutes with both terms.
The cross terms in the squared Fourier symbol cancel by the Clifford
anticommutator. The deliberately commuting wrong symbol has an extra
term linear in momentum and fails the square identity.

The zero equations are `u'=-Ku`, `v'=Kv`. Hence positive K directions
decay in u and negative ones in v, not both in the same slot. Both are
retained in the tests. Their common exponential squared norm is
`1/(2s)` for s positive. The scalar-sign and mixed-family controls
are consistent with those orientations. At K=0 constants are not L2
on the infinite half-line; the code correctly retains the six-dimensional
coefficient kernel and the diverging norm instead of constructing an
invertible limiting response or assigning a physical index zero.

The true cusp input has volume weight `rho=e^-t`; conjugation by
`sqrt(rho)` cancels the `rho'/2rho` term. The wrong exponent leaves
a nonzero residual. Direct polynomial differentiation/integration gives
`integral b^2=1/630`, `integral (b')^2=2/105`, ratio twelve, for
`b=x^2(1-x)^2`. The endpoint conditions support its use as an H1
Weyl control. This is prior science recovered, not a new particle result.

The zero threshold and the finite-distance critical quotient remain
different operator problems. Neither the finite ranks nor a gapped
finite matrix certify the full angular cusp, a Fredholm domain or a
four-dimensional spectrum. The analytical texts preserve those limits.

## 4. Execution and instrument review

The P210 wrapper checks the frozen v3 runner's bytes before loading it
and then changes only HERE, ENTRY and EXPECTED. The rebound root and
relative entry calculation are consistent with the repository layout.
The six synthetic fixtures cover that binding and failure propagation;
they are not controls of genuine prospective admission.

The first fixture failure is preserved before repair. Resolving the
temporary root matches production path semantics rather than weakening
the binding assertion. The later append/counter repair closes a real
coverage gap in the original overwritten sentinel record. The recorded
fourth run uses the intended interpreter; this review did not rerun it.

The frozen runner checks runtime/version metadata and the declared
environment, takes a strict HEAD/index/worktree snapshot, and requests
the strict prospective gate before loading `checks.py`. It then checks
the exact command/output population and current pins again, opens fresh
outputs exclusively, records the expected test population and finally
records custody. It rejects skips, expected failures, incomplete
population, failed tests and changed custody. This is more than the six
software fixtures alone establish; the source itself was inspected.

The prospective layer binds the specification/design/source hashes to
the seal commit; requires a separately committed nonauthoring,
source-complete approving review of that exact specification; and
requires main's separately committed acceptance of that exact review,
reachable from the fetched origin/main reference. These document checks
do not authenticate a reviewer's independence or mathematical honesty
by themselves. Main's substantive receiving duty remains essential.

The gate closure contains only the inspected local dependencies and
standard-library imports; no scientific producer is delegated. The
view gate can write generated navigation, so this dirty checkout must
not be used to execute it. A changed tracked view will be detected by
strict custody, not forgiven. The historical seal report is retained;
prospective admissibility is not global historical compliance.

Runtime metadata is **not a content-addressed dependency build**.
Package versions alone do not prove identical wheels or detect changes
made and reverted between snapshots. The packet explicitly disclaims
those stronger guarantees; it relies on its quiescent-window requirement.
Execution approval here does not upgrade those limits to security or
reproducible-build certification.

Nonblocking documentation observation: `EXECUTION_REVIEW_DUTIES.md`
contains the phrase “38 individual pins”; the actual specification has
39 artifacts. The complete population inspected in this review is the
specification, not that incidental prose count. Do not silently edit a
frozen file to repair this cosmetic count; preserve its seal.

## 5. Separate review: analytical successors

These two notes are outside the frozen execution packet. The conclusions
below are analytical source-review judgments, not claims that new tests
have run or that a new experiment has been admitted.

### 5.1 Existing graded cusp response, successor `65dd3c112`

Note SHA256:
`ac3dd9f39d34610594e2e77552857533b08932bbeeb3b61a41ee714e2ee9968e`.

The graded-condensate producer was read directly, including
`radial_blocks`, normalization coefficients and the run body. Its source
SHA256 is
`6e7254ff85f2465d077bd90b1f4182e6eb916fc43e244c5b6554fdc9fe136d80`.
The curved-action, graded-condensate, SM-parallel and two-field proof
bodies were also read. Their older global analytic claims remain
conditional rather than independently numerically reproduced here.

**No blocking algebraic error found in the new response derivation.**

The producer uses precisely the stated matrix
`B=[[partial+a,k],[-k,-partial+a]]`, and retains unpaired extreme
blocks with the appropriate derivative sign. With `E=diag(1,-1)`,
`K=EZ`, one has `B=E(partial+K)` and
`B†=(-partial+K)E`. Conjugating the doubled operator by
`diag(I,iE)` gives the displayed constant-tail Dirac operator,
including its factors of i. This is an exhibited isometry of the
specified blocks, not a new freely chosen mass.

Paired K has eigenvalues `+/-sqrt(a^2+k^2)`, so its positive/negative
spectral ranges give both decaying slots and the stated norm. For even
m, a is a nonzero half-integer. The upper extreme for even j has
positive K=(j+1)/2; the lower extreme for odd j has positive K=j/2.
There are j paired blocks and one retained scalar extreme. Thus
the count j+1 positive, j negative is correct **boundary-slot counting**,
not physical net charged chirality.

For real lambda, multiplying the eigen-equation gives
`L_lambda=-sigma3 tensor K+i lambda sigma1`; its square is
`(mu^2-lambda^2)I`. Inside the open gap the negative-real-exponent
spectral idempotent is exactly `(I-L_lambda/kappa)/2`. It need not
be orthogonal for nonzero lambda. Its range is null because
`L_lambda† G+G L_lambda=0` and a decaying current is zero. At the
threshold L is nilpotent and solutions are affine, with no nonzero
L2 solution. The note does not convert that threshold into an admitted
zero-dimensional boundary domain.

The actual coefficient/parent map, full nonzero-angular response and
selection of this stationary background are not obtained. The note
explicitly does not identify the tensor factor of this B block with
the paper's quaternion factor. Its preservation of the earlier
vector-like/zero-index results on the specified phases is appropriate.

### 5.2 Symmetric-state realization, successor `dff9478a9`

Note SHA256:
`97c7dd23a46ff519e614bb762b023b057bb5eb8ef5962e517f9791777ea3048b`.

The additional retained-embedding, actual puncture connecting-map,
surface-parent, surface-global-spin and field-map proof bodies were
read. The actual historical producers, not just the receiving report,
were inspected at `3bf82d0ca08284a631016b217e0b9297a756f8ff`:

- B1656 `the_electrons_zero.py`, through the complete head defining
  `dual_basis`, `weighted_M` and `coupling`, hash
  `8abe8b53f2012abda10aeca93b2f9c2808cbf46ee4368f8e0b1272ccffa10b2e`;
- B1659 `the_joint_law.py`, complete producer, hash
  `84756480041eed2b5b37aee72400060b04cd74646e3892c2066ef56e1646b786`;
- the paper's relevant fibre/point/norm/joint-law sections, blob hash
  `51c28227048e4038fa32dbed7d2aea415b6d329b4b52b988082b0069c1b72047`.

**No blocking algebraic error found in this scoped realization audit.**

Writing N=M epsilon really changes congruence transport into conjugation.
Commuting with both i and j forces both S and N to be scalar, so a
nonzero fully fixed matter matrix has rank two. A single rank-one
residue cannot equal it.

For `M=[[a,b],[c,d]]`, the four unit functionals are explicitly
`(b-c, -i(b+c), -a-d, i(a-d))`. Their squared sum is `4(ad-bc)`.
Consequently rank-one input has null-quaternion residues, whereas
`n epsilon^-1` has only its first unit channel nonzero. Finite nonzero
diagonal channel weights cannot turn the former into the latter:
zero imaginary weighted channels force zero imaginary raw channels,
then the null identity forces the first channel to vanish too. This
does not exclude other non-diagonal, multi-residue or singular inputs.
The actual B1656 `weighted_M` reconstructs precisely this dual basis.

The four dual basis matrices have squared Hilbert-Schmidt norm 1/2
and are orthogonal. If T is the imaginary weighted squared norm and
S0=|u1|^2, nullness gives `T >= eta^2 S0`; hence
`sqrt(T/(S0+T)) >= eta/sqrt(1+eta^2)`. This proves the relative
distance bound. The stated `(1,i,0,0)` residue with weights
`(1,delta,1,1)` attains it. Letting delta approach zero changes
nondegeneracy, unlike the fixed-tau large-cutoff canonical prescription.
The distinction between these limits is mathematically material and
correctly retained.

For nonzero rank-one M, `MM†/tr(MM†)` is indeed its image projector.
Under unitary congruence, `g^T conjugate(g)=I`, so this projector
transforms by unitary conjugation. The matter-dependent trace plane
therefore remains covariant at S=I while the complete matrix state is
not fully Q8-fixed. When its left residue is the earlier actual trace
vector, this recovers U, whose conditional finite-distance kernels are
(3,3), not (3,0). It is not a new dynamical boundary selection.

Finally the retained embedding maps sl2 into sl6, but not the scalar
part of End(C2) into a multiple of the traceless identity. That scalar
requires another specified field assignment. The existing equality of
the puncture gauge element and the chosen weak centre makes End(C2)
under conjugation even and the weak doublet odd. A bare equivariant
linear map is then zero by its central intertwining equation. This is
a correctly scoped representation test for that embedding, not a
general Higgs or physical-parent exclusion.

## 6. What remains scientifically open

The review supports execution of the frozen algebraic checks and the
scoped analytical consistency of the two successors. It does **not**
discharge the actual map from the registered profile/norm/state data to
one full parent action, its physical fields and its boundary domain.
It also does not select the stationary background, establish a chiral
three-generation spectrum, cancel anomalies, derive normalized physical
parameters or gravity, or remove a foundational input merely by deriving
a response after a supplied parent has been fixed.

The new note `ACTUAL_CUSP_WEYL_RESPONSE_AND_INDUCED_NORM.md` authored
while this review was in progress was **not reviewed** and is not covered
by any verdict here. No later relay or new source silently inherits
approval from this document.

Next authorized step for this packet is main's independent examination
and exact acceptance of the separately committed review record. Only
after that may genuine strict admission and execution in a clean,
quiescent checkout proceed. The physical derivation mission remains
open independently of whether all ten bounded controls later pass.
