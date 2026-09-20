# Working continuation: the source scalar and the whole mode space

2026-09-20. UNEXECUTED ANALYTICAL PREPARATION after the R36 report
at f514417257369da3209761d22527c917a8c3448a. The formulas below were
derived by hand during preparation. They are disclosed analytic
priors, not blind predictions, independently accepted proofs or
executed R37 results. No new scientific producer has been run.
No shared B, physical identification, source selector or quantum gap
is earned. R36 remains the latest executed scientific checkpoint.

## 1. The question has changed type, not just acquired another profile

R36 distinguishes charged bilinear Yukawas from Hermitian currents
and retains the Green boundary term. Its prescribed smooth bulk
scalar was not derived from a source equation. The next question is
the scalar sector of the SAME added R29 source EFT.

R29's Q in 1_4 lives on a prescribed contractible tube U with measure
sigma dvol and its own natural boundary condition. It is not a
whole-manifold smooth scalar. S in 10_2 is permitted by R33's actual
H subgroup, but its presence is an additional field assumption.
Choosing a scalar action and deriving its modes is not deriving that
action from the object, the full E6 parent or a torsion-free G2 model.

The quantifier here is a proposed added, finite-width, compact
H-source theory, followed by an explicitly separate flat comparator.
No class-wide no-go, actual sourced hyperbolic eigenfunction or
physical number is claimed. Retain R19's different singular domain.

## 2. Candidate minimal extension and all fields that must be varied

On one tube, retain Q=Phi and add S with the SAME positive kinetic
weight sigma for its internal and four-dimensional derivatives:

    V_S = integral_U sigma [
        |D_i S|^2 + r |S|^2 + lambda_S |S|^4
        - eta (Q* S dot S + Q S* dot S*)
    ],
    K_S = integral_U sigma |D_mu S|^2.

Here eta, lambda_S>0 and r are INPUT parameters in the existing
curvature-length convention. The covariant derivative is in the
actual 10_2 representation, not a stand-alone charge-two character
of H. Use R36's line-connection convention D=d+i charge A; its A is
minus the connection coordinate in R29's D=d-i charge A notation.
This changes notation, not the physical charges or connection.
Extend the central residual by the scalar's charge density:

    D_res = div h - kappa sigma (4 |Q|^2 + 2 |S|^2) 1_U,

with a sum for multiple tubes. Retain R29's C integral D_res^2,
curl, gauge and Q terms. This is a specified bosonic H EFT, not a
supersymmetric/full-parent completion. Missing parent couplings,
including a possible h-dependent scalar potential, cannot be
assumed absent in a future parent theory.

Using independent complex variations, the proposed S equation is

    -sigma^-1 D_i(sigma D^i S)
      + r S + 2 lambda_S |S|^2 S - 2 eta Q S*
      - 4 C kappa D_res S = 0.

Its natural condition is sigma D_n S=0 on the tube boundary.
The Q equation gains -eta S dot S; its existing moment-map term
uses the NEW D_res, rather than a fixed external density. The h
equation likewise uses that residual. S also contributes its central
and D5 gauge currents. At S=0 those new variations/currents vanish,
so the old Q=f>0 parallel, flat-A, h=dF stationary background remains
a candidate stationary point of the extended classical action.

This last statement is stationarity, not a claim that the point is
the unique or global minimum. Coupled finite-amplitude Q,S changes,
quantum expectation values and backreaction still need analysis.
The scalar mass split below only addresses the quadratic S block.

## 3. Canonical modes follow from this action, conditionally

At that point D_res=0. In a parallel tube frame Q=f and
S=(x+i y)/sqrt(2). The real quadratic operators are

    K_x = -sigma^-1 div(sigma grad) + r - 2 eta f,
    K_y = -sigma^-1 div(sigma grad) + r + 2 eta f,

each on ten components, with covariant Neumann data before choosing
the parallel frame. The connection is flat and the tube contractible.
The weighted gradient form is nonnegative and its kernel on a
connected tube consists of parallel constants. Therefore the candidate
lowest scalar profile is s_0=1/sqrt(W), W=integral_U sigma dvol,
with squared masses r-2 eta f and r+2 eta f. For the uniform R29
hyperbolic tube, W=L, not its vanishing unweighted volume.

The two branches are positive when r>2 eta f; equality requires
retaining a massless scalar. Below it there is a classical instability,
not evidence of symmetry-preserving mirror removal. Flat directions
and spectra in the other field sectors are not decided here.

For normalized four-dimensional coefficients S_4 and Q_4,
S=S_4/sqrt(W), Q=Q_4/sqrt(W). Projection predicts quartic coefficient
lambda_S/W and phase-locking coefficient eta/sqrt(W). In particular
Q_4=sqrt(W) f at the reference point; this recovers the same mass split.
Canonical normalization does not choose W, r, eta or f.

## 4. The interaction measure is another explicit input

A minimal source-local candidate keeps BOTH R33 intertwiners:

    integral_U sigma [
        y_m S_a chi^t epsilon Y_a chi
        + y_p S_a* psi^t epsilon Y_a psi + h.c.
    ].

The use of sigma in this Yukawa, the two microscopic coefficients
and the internal bilinear form contraction are ADDITIONAL choices.
Gauge symmetry and the scalar kinetic term alone do not force them.
A different interaction density is a different source theory. This
distinction must be tested, not hidden by normalizing a wavefunction.

Using R30/R36's exact positive pairs, v_i=d_q u_i/sqrt(lambda_i),

    M_ij = integral_U sigma s_0 conjugate(u_i) conjugate(u_j),
    P_ij = integral_U sigma conjugate(s_0) g(v_i,v_j).

For finite width these use whole-manifold fermions transmitting
through the tube interface. They do not satisfy a new Robin condition
there. A zero extension of s_0 is not a smooth whole-manifold mode.

Put b=sigma conjugate(s_0), w=u_i u_j and E_ij=(lambda_i+lambda_j)/2.
The full candidate Green identity on U is

    sqrt(lambda_i lambda_j) P_ij
      = E_ij conjugate(M_ij)
        + integral_U w [(1/2) Delta_(-2A)b
                       - q <dF,D_(-2A)b>]
        + integral_boundary_U {
            b [(1/2)D_n^(2A)w + q F_n w]
            - (1/2) w D_n^(-2A)b
          }.

The weight is inside b: its derivatives cannot be silently dropped.
For constant sigma and the parallel s_0 the interior correction and
D_n b vanish. The FIRST interface flux generally survives.
R36's outer-boundary simplification does not apply to that artificial
cut. This is where the actual global modes or uniform estimates enter.

## 5. Opposite controls must include a complete equal-energy space

A transparent flat comparator uses Q_flat=T2_(2pi) times [0,1],
trivial flat line, F=0, absolute outer data. This is NOT R29's
nonzero sourced hyperbolic solution. It can be viewed with the
source-shift coefficient switched off for the comparator alone.

Let U_e=(-e,e)^2 times [0,1], 0<e<pi/2, with
sigma_e=1/(4e^2). It is a contractible rectangular tube with Lipschitz
boundary, W=1 and s_0=1. Corner geometry is not asserted smooth.
The full scalar eigenvalue-two space on this comparator has the
orthonormal REAL basis, in this order,

    u=(cos x cos y, cos x sin y, sin x cos y, sin x sin y)/pi,
    v_i=du_i/sqrt(2).

There are no other modes at eigenvalue two: positive axial Neumann
eigenvalues start at pi^2, and n_x^2+n_y^2=2 gives exactly the four
listed real modes. There ARE lower modes, including a zero mode,
which this control does not discard or reinterpret as the desired
three-generation spectrum. Zero modes are not divided by sqrt(lambda).

Define a=1/2+sin(2e)/(4e), b=1-a and c=1/pi^2.
Direct integrals are predicted to give diagonal matrices

    M = c diag(a^2, a b, a b, b^2),
    P = c diag(a b, (a^2+b^2)/2, (a^2+b^2)/2, a b).

Off-diagonal entries vanish by the actual reflection integrals,
not by a stated diagonal ansatz. For the first mode alone,

    M_11 -> c,     P_11 ~ c e^2/3,     M_11/P_11 ~ 3/e^2.

That is a finite absolute mirror coupling in this chosen measure,
unlike the R36 smooth-bulk localized-profile control. But the FULL
mode space simultaneously gives

    M -> c diag(1,0,0,0),
    P -> c diag(0,1/2,1/2,0),
    norm(M)_op/norm(P)_op
       = 2 a^2/(a^2+b^2) -> 2, NOT infinity.

Thus inspecting only the first pair would overstate sector selectivity.
The unsuppressed ordinary couplings sit on its equal-energy neighbours.
These are proposed invariant singular-spectrum checks, not a physical
mass matrix: the two independent microscopic coefficients and scalar
dynamics still multiply them, and no S expectation value is assumed.
A complex unitary basis change must leave those singular spectra fixed.

For the first mode, explicit interface flux is predicted to be

    flux_11 = -c a sin(2e)/e = 2(P_11-M_11).

The full matrix must obey 2P=2M+flux. Omitting the internal interface
would wrongly give P=M. All faces, including the zero axial-cap
contribution, must be integrated in the test.

As a measure discriminator, keep the SAME weighted scalar kinetic
normalization but remove sigma from the Yukawa density. Then both
matrices are multiplied by 4e^2 and ALL their entries vanish. This
tests the interaction action, not a harmless coordinate convention.
The finite-width comparison does not construct a zero-width QFT:
local coefficients grow with shrinking support, codimension-two
trace/domain issues return, and counterterms or extra defect dynamics
may be needed. R29's warning about literal line forms remains relevant.

## 6. Prior and remaining verification duties

The full R29 source proof/design, R33 interaction proof/prior and R36
overlap proof/report were reread. The ladder was read through its
rungs and end rules; long-line truncation was recovered by smaller
reads. The atlas card remains generic/epoch-limited. The B960/B1086
kill rows and hatches are not a negative theorem for this added EFT.

The retrieval query "weighted tube scalar Yukawa" has 59 hits and
three settled-threshold bodies: B1220, B1232 and B677, all read to
their ends. B677's categorical Tube(Fib) is not this geometric tube.
B1232 requires normalized invariant observables rather than a basis
choice. B1220 warns that each premise needs its own prior search.
No numerical claim from these arcs is imported as a new computation.
The captured query oa_r37_banked_first exits 1 because settled hits
exist, not an execution failure: 3,496 bytes, SHA256
5e82072f4d1a0094e7df4d6bab22c9fd979cdc984d26b83aec930aa085e8088c.
The full settled list was read separately from the first-twelve display.
ASCII/Unicode tube, scalar, interface, weighted and Yukawa searches
were scoped to the checked-out bodies; no all-history absence is claimed.
A guessed query filename and an initial kill-JSON shape assumption
failed before their actual path/array shape was read. No absence
conclusion followed. No new paper or fresh all-seat fetch is claimed.

Before any important execution, complete the relevant producer and
prior-art reads, freeze those inputs, write and seal the actual
proof/producer/tests, and push the seal. Check, independently:

- the coupled S, Q, h and gauge variations, including the S density;
- the weighted Green form, scalar operator and natural domain;
- the scalar normalization, real-branch masses and marginal control;
- the induced four-dimensional coefficients without choosing a scale;
- every matrix entry, exact eigen-equation and mode normalization;
- the explicit full interface matrix and a dropped-flux discriminator;
- singular spectra before and after a complex unitary basis change;
- the selected-mode versus whole-eigenspace and measure discriminators.

Do not alter R36's sealed files or failed tests to make this pass.
The actual next physical duty remains the sourced global modes and
their complete low-energy overlaps, followed by interacting-phase,
source/end/anomaly and controlled-limit tests. Supplying an allowed
source action is not selecting it from the object. Neither this
working note nor its successful future controls would complete a TOE.

## Preparation custody, not validation of the proposed calculation

Read-only R36 custody passes unchanged: six sealed files, 44 frozen
inputs, six raw captures and the same four focused failed IDs.
Cumulative custody verifies 558 artifact paths, 140 latest distinct
seals and unchanged R30/R31 evidence. Its 117 relative links belong to
this smaller staged/prior population, not R36's 233-link population.

Preparation governance reports 26 PASS / the same four FAIL details
as R36's September 20 check. The review counter is 182. No old failure
is waived, foreign relay closed or new science/whole-suite run claimed.
Strict staged whitespace passes. Final hashes and custody are checked
again after recording these receipts. The captures are exclusive:

- oa_r37_preparation_gates_first: exit 1, 2095 output bytes;
  output SHA256 18b367f7027e026732e1584d4a1b7b04cb376fdb5fb52a6fed01443486261ddc;
  receipt SHA256 a23e174f2dfdd6ac9e37cfe13f764743e9c765a2c3898cdd71bc9c9cd1ebd0da.
- oa_r37_preparation_custody_first: exit 0, 616 output bytes;
  output SHA256 d1d6d7760e3fd082318131cce631724fd36d3f8fd21d59d508be34fb54958e26;
  receipt SHA256 397114e8c20614038868d337ed62e2a5bbbbca21d957a12b4ab13681ae8eac26.
- oa_r37_r36_custody_first: exit 0, 289 output bytes;
  output SHA256 291c3ba2b72bef166d2197b01d1f08036a9b464c1e3c9191849126601b255dc2;
  receipt SHA256 22741151a7c93531b9f2c50f5497a21c69dd661fd51cafb85f2e2c1268fa42b4.
