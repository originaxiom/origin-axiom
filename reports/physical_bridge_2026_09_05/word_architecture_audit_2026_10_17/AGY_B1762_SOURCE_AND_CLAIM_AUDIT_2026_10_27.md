# Agy B1762: preserve the numerical lead; repair the claims

October 27, 2026. Fetched source: 046acf2d4dfa095d7f9c2102a2e62894596c94b1,
agy/frontier-2026-10-26. One new commit since audited 3e519e627.
This is an author source audit and exact hand-algebra countercheck,
not a rerun of the scientific producer or independent certification
of its quadrature, optimization or phenomenology. No scientific module
was imported, collected or executed. Saved JSON was read as evidence
of what the producer reports. The original artifacts are unchanged.

## 1. Verdict and positive to preserve

B1762 contains a useful compact phenomenological ansatz: prescribed
functions of the existing forms and Yukawa Gram matrices give much
better saved nine-target scores and CP magnitude than the stated
single-Higgs baseline. This warrants preservation and a properly
controlled follow-up. It does not yet establish physical derivation,
a globally selected parameter-free model or a universal parity theorem.
The published PROVED/VERIFIED headline exceeds the verified scope.

The saved JSON and run text agree on the highlighted rows:

| Fixed point and recipe | Nine-target score at MZ | abs J | Saved J pull |
|---|---:|---:|---:|
| 0.3145+3.0345i, baseline | 821.161809 | 6.39137e-8 | -20.4907 |
| Same point, L2p | 26.309946 | 2.77509e-5 | -2.0327 |
| Same point, L3p | 25.812479 | 2.69973e-5 | -2.5351 |
| Rounded arithmetic apex, baseline | 898.212339 | 5.77034e-8 | -20.4949 |
| Same apex, L3p | 25.887253 | 2.67422e-5 | -2.7052 |

These are consistency-checked reported numbers, not independently
reproduced predictions. They remain worth investigating after the
following corrections. A flaw in the proof does not make the saved
numerical improvement disappear.

## 2. Exact counterexample to the asserted generation-block identity

Read the actual imported B1723 b1656_funcs.py and the B1742 Smat map:

    I=QI, J=QJ, K=QI QJ, EPS=J,
    BLOCKS=[J,I,K], Smat(h)=h0 I+h1 J+h2 K,
    Y_ab=sum_entries((Ca^T EPS Smat(h) Cb) M).

Here I,J,K are quaternion matrices, not identity matrices. Their squares
are -Id. Write u_s=sum_entries((EPS C_s)M), the exact dual-basis
coordinates used by weighted_M. In particular EPS C_j=J J=-Id,
so u_j=-tr(M).

Take the supposed block-diagonal slice h=(1,0,0). The producer uses
Ca=J for generation 0 and Cb=I for generation 1. Then

    Ca^T EPS=(-J)J=Id,
    Ca^T EPS Smat(h) Cb=I I=-Id,
    (M_0)_(0,1)=-tr(M)=u_j.                       (A)

The C1 selection in B1761 explicitly requires abs(R_up_j)>1e-8.
Where its norm weight is positive, u_j=sqrt(2pi L+c_j) R_up_j is
nonzero. If that weight is clipped to zero by the code, it is a
separate clipping condition, not the asserted symmetry theorem.
More fundamentally (A) alone disproves an identity for all allowed
coefficient matrices based solely on the cited parity argument.
The hypothesized 0-versus-{1,2} off-block entry is not identically zero.

For completeness, multiplication of the same declared matrices gives

    M_0 = [ -u_i   u_j  -u_1 ]
          [  u_j   u_i   u_k ]
          [  u_1   u_k  -u_i ].                  (B)

In particular u_i=0 does not make this matrix block diagonal. If u_1
is nonzero, M_0 is not even symmetric in its two generation indices.
There is a stronger check independent of channel-weight positivity:
the same multiplication gives (M_2)_(0,0)=-u_k and
(M_2)_(1,2)=u_i. The alleged M_0 block support forces u_j=u_1=0;
the alleged M_2 off-block support forces u_k=u_i=0. Together these
supports force ALL four coordinates to vanish, hence M=0. They cannot
describe the nonzero pencils reported in the same experiment, even
if some individual channels are clipped.
The Higgs-coordinate basis [I,J,K] and generation blocks [J,I,K] are
also different. A common totally symmetric tensor with a common parity
basis must be exhibited, not assumed. A further explicit basis change
might reveal a different structural statement; it is not supplied by
the printed theorem and would have to transport every sector/operator.

There is also an internal sign inconsistency in FINDINGS section 2.1:
it writes P(0)=-1 and the product rule P(j)P(k)=-1, then infers the
same-parity diagonal blocks. That inference is the opposite one.
A parity selection rule is a necessary vanishing condition, not an
iff that every symmetry-allowed entry is nonzero.

## 3. The verification code measures different objects

B1762 producer lines 132-136 compute:

- the off-block entries of the UP GRAM MATRIX Sigma_up;
- norm(Sigma_lep-P Sigma_down P).

They do not compute forbidden entries of M_0, M_1 or M_2, although
variables, verdict summary and FINDINGS present them as those tests.
The saved second number is 6.18e-16, not a test of the slices' diagonal
blocks. A block-diagonal Gram means Frobenius orthogonality among
slices; it does not mean the slices have complementary entry supports.
The Gram observation is retained with its correct type.

All five B1762 tests read committed JSON/file presence/verdict strings.
None recomputes Yukawa slices, Gram matrices, running or minimizers.
Passing these locks cannot independently verify the theorem or the
producer. The identity tests need the actual matrices, rejecting
controls and both a known-positive recovery and a complement check.

## 4. Prescribed formulas do not yet remove physical inputs

The producer defines delta=Sigma_up[0,0]/2, p=1+delta, boosts -DR[0],
and tries phase exp(i delta), imaginary abs(Schur coefficient), and
another phase exp(2i abs(Schur coefficient)). Ten recipes including
baselines/control are evaluated. There is no action, stationary
condition or anomalous-dimension calculation in this producer deriving
these prescriptions. The source audit identifies this exact supplied
step; it does not assert no derivation exists anywhere in the corpus.
The prior same-action Hessian/source relays still specify what would
earn the identification. Agy should cite an actual derivation if one
exists beyond this producer.

The code's boost numerator is v012^dagger Sigma_up v012 (line 150).
It is not divided by v012^dagger v012 and no eigenvector residual is
checked. Since v012 is the normalized DR vector with its first component
deleted, its norm generally differs from one. Calling this quantity a
proved eigenvalue is unsupported even if the approximate value is close.

Trace normalization cancels from a projectively normalized inverse
power at fixed p. However delta=Sigma00/2 now uses the normalized
Gram to define both p and a phase: changing this convention changes
the recipe unless the actual law derives that convention. One cannot
reuse the earlier normalization-cancellation argument for this new role.
Likewise Re and abs are explicit frame/phase prescriptions; a registered
frame may support them, but their physical covariance/selection must
be established, not inferred from their having no adjustable numeral.

The arithmetic apex is read as (0.333333,3.055050) from B1757, not
computed exactly. This rounding is small; it is not evidence of failure,
but the run is not an exact-arithmetic evaluation. The line, horocycle,
field assignments, c=3 lepton correction, response model and the
prescriptions remain supplied dependencies. Four laws chosen after
seeing fits do not acquire a zero model-selection cost because each
later evaluation uses no continuous optimizer.

A further dimension correction: CP2 times CP2 has EIGHT real direction
DOFs. B1757's actual free fit uses two arbitrary complex three-vectors,
with normalization and phase redundancies, as its own source and
B1761's `chi2_8dof_b1757` label indicate. Four real DOFs describes a
restricted subfamily, not that unconstrained fit.

## 5. The GUT-labelled score is a partial target deformation

Producer lines 90-94 copy MZ targets and modify just four entries by
half-log shifts from two double ratios. It leaves up ratios, CKM,
J and all uncertainties unchanged, and does not evolve the model.
This can be a declared sensitivity experiment. It is not a complete
RGE calculation or a consistent readout of all ten observables at a
new scale.

I personally checked Huang-Zhou 2021's numerical section and tables
2-3, plus its scale/covariance discussion:
https://arxiv.org/html/2009.04851v2
The paper tabulates the full-SM masses at MZ and 10^12 GeV. The up
ratios change too (e.g. mc/mt from 0.620/168.26 to 0.283/85.07).
Its separate lepton/down ratios are not specified by arbitrarily
splitting a double-ratio shift half to each. The paper identifies a
typical GUT scale near 2e16 GeV, not 10^12 GeV; the latter is one of
its benchmark scales. An OA-specific matching scale could differ,
but would need its own derivation rather than that citation.

The modern Antusch-Hinze-Saad primary running paper also explicitly
separates SM benchmarks, MSSM, GUT scale, threshold assumptions and
running quark mixing/J:
https://journals.aps.org/prd/abstract/10.1103/fdcc-ycph
Its existence and framework were checked, not its entire paper read.
Agy's other three named arXiv citations resolve to the stated relevant
authors/topics; no fabricated citation is alleged. None of those abstract
checks establishes agy's phase/exponent laws. No substitute fit has
been made using the newer data in this audit.

## 6. Reported ranges and the numerical-floor claim need correction

The claim of J agreement within about 2.5 sigma across the ENTIRE strip
is contradicted by the saved records. At tau=0.3145+3.10i:

| Fixed recipe | abs J | Saved J pull |
|---|---:|---:|
| L1p | 1.94136e-5 | -7.5910 |
| L2p | 2.24848e-5 | -5.5434 |
| L3p | 2.30826e-5 | -5.1449 |

At 2.95i L2p gives 3.64287e-5, +3.7524 sigma. The quoted
[2.13,3.09]e-5 interval mixes selected rows/recipes rather than bounding
the displayed complete family. The good central/apex rows remain.
Abs(J) is the tested quantity; a successful magnitude does not by itself
select the physical sign of CP violation.

The numerical `floor` is a single Nelder-Mead run started at
(0.08,0.055), without stored success/termination/gradient/global-bound
certificates. Even a converged local minimum is not a theoretical
floor. At the central point L4p's saved score 25.433696 is GREATER
than that same fixed-Hd family's saved local result 25.0699, as expected;
this only checks consistency, not global optimality. Proximity to an
optimizer incumbent does not prove exhaustion of the pencil. Preserve
the 0.26 apex difference as a reported comparison, not a proof of
99 percent theoretical performance or no fine-tuning.

The Schur block-inverse identity is valid with the usual invertibility
hypotheses, but its comparison control uses a hybrid: it attaches an
old DR-based first coefficient to the decoupled block response. It
changes more than merely deleting one feedback term in a consistently
stationary model. Its poorer score is a scoped comparison, not proof
that every decoupled mechanism fails or that physical Schur response
has been derived.

The nine-target score also includes a fixed 10 percent allowance in
quadrature with experimental relative errors (B1740 compare.sigmas).
It is a declared discrepancy score under that tolerance, not a pure
experimental chi-square. The ten-target extension adds J with a
different error prescription and no joint covariance. No discovery
significance or parameter-free predictive acceptance follows from
dividing this score by nine or ten.

## 7. Constructive repair order and banking scope

1. Correct/retract only the false slice-parity proof; retain the actual
   Gram identities at their computed scope and prove any desired
   transformed slice statement with the full basis map.
2. Freeze explicit candidate laws and a meaningful failure criterion;
   derive their Hessian, source/partner and exponent/phase from one
   admitted action or mark them phenomenological prescriptions.
3. Independently recompute the frozen producer with precision/quadrature
   controls and actual rejecting matrix tests under the required gates.
   This source audit is not permission to execute a newly invented test.
4. Use one selected law on held-out points/targets, full family accounting
   and a consistent scale/threshold/covariance prescription. Do not mix
   the best J from one law with the best mass score from another.
5. Separate conditional phenomenology from foundational reductions and
   a physical SM3 claim. None of these defects excludes the full
   architecture or erases the observed numerical lead.

This report changes no incoming scientific output, banked result,
review/admission rule or pending P210 acceptance. Its own newly authored
algebra is open to independent checking; equation (A) is supplied in
full so the receiving seat can verify it directly without an optimizer.
