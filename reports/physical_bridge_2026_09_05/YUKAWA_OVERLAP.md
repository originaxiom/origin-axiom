# R36: charged overlaps retain a source-profile and boundary duty

2026-09-19. Path-local PB-BOUNDARY / PB-ACTION continuation, not a
shared B arc, independent main bank or completed physical theory.
Scientific seal `a42b7118837ff8cdd3f5118e5cc523e971154d92` was pushed
and remote-confirmed before execution. The earlier working derivation
at febedec0 is disclosed analytical prior; this is not a blind forecast.

## Result

The charged product/Green identity and its two-sided controls pass:
**11 native check groups, 15 new tests**. The expanded ten-file run has
**158 passes and the same four failed IDs as R34**. No failed source or
test was changed, skipped from that population, or relabeled green.
The older halted R33 control remains outside this declared population.
[Producer](yukawa_overlap.py), [proof](YUKAWA_OVERLAP_PROOF.md),
[design](YUKAWA_OVERLAP_DESIGN.md), [receipts](YUKAWA_OVERLAP_RECEIPTS.json).

This earns an authored overlap relation with exact controls in the
specified ADDED interaction model. It does not compute the actual
global sourced eigenfunctions or derive the scalar profile. The
general compact-domain proof still needs independent review; finite
symbolic tests are not an interval or global PDE certificate.

## What is different from the constant-gauge argument

R30/R31's exact positive scalar eigenpair is u_i and
v_i=d_q u_i/sqrt(lambda_i). R33's left-Weyl mirror has profile
conjugate(u_i), and the ordinary partner has profile v_i. For a
canonically normalized charge-two scalar profile s and the declared
bilinear form contraction, the matrices are

    M_ij = integral s conjugate(u_i) conjugate(u_j),
    P_ij = integral conjugate(s) g(v_i,v_j).

The local microscopic couplings are additional factors and need not
be equal. These are not density overlaps. The exact type control
(1,i,0)/sqrt(2) has Hermitian norm one but bilinear square zero.
Accordingly the earlier constant-gauge-current normalization does
not establish a universal equal-Yukawa obstruction.

With b=conjugate(s), Delta=div grad and the induced dual connection,
the full relation is

    sqrt(lambda_i lambda_j) P_ij
      = (lambda_i+lambda_j)/2 conjugate(M_ij)
        + integral_Q u_i u_j [(1/2)Delta_(-2A)b-q<dF,D_(-2A)b>]
        - (1/2)integral_boundary_Q u_i u_j D_n^(-2A)b.

Fermion Robin data remove one flux term, not the last scalar-derivative
term. The controls test the covariant product rule and Green identity
for arbitrary functions, radial volume density and connection, with
both equal and dual charges. Variable-phase gauge covariance passes.
Omitting the drift, scalar conjugation or required end contribution
fails its stated discriminator.

At fixed finite source width, the authored proof applies with the
regularity supplied by R29/R31 and smooth b. The small-width uniform
estimates on its RIGHT-HAND SIDE are not supplied by this identity.
One must not discard an apparently small term before dividing by
small eigenvalues. Nor may an exact zero mode be divided by sqrt(lambda).

## Both tempting universal conclusions fail their controls

| Declared control | Verified result | Scope and lesson |
|---|---|---|
| Flat circle times unit-area T2, F=0, order-three flat line | P=-D conjugate(M)D for the paired circle modes; direct complex Fourier integrals and invariant singular-value polynomials agree | A varying scalar is not automatically selective. This is not the sourced hyperbolic manifold. |
| Absolute interval times unit-area T2, normalized scalar N_t exp(-tx) | M/P=(t^2+2)/2, but M~2sqrt(2)/(pi sqrt(t)) and P~4sqrt(2)/(pi t^(5/2)) | Relative selectivity can grow while BOTH couplings vanish at fixed microscopic coefficients. The profile is prescribed, not a stationary solution. |
| Same interval control's scalar kinetic norm | Integral norm(ds_t)^2=t^2 | The localization has a cost. This is not a mass eigenvalue without a specified scalar action and boundary problem. |
| F=2x, actual Robin data, test coefficient x^2 | Boundary contribution -2/5 and drift are needed for the exact identity | Undeformed Neumann data and the dropped drift fail; the coefficient is a test weight, not a physical scalar mode. |

The flat-line control also checks that its squared order-three
holonomy is nontrivial. A globally parallel charge-two profile cannot
be silently used on that selected central flat background. This does
not exclude a nonparallel bulk scalar, a different background, or a
scalar living only on a contractible source tube.

No control's numerical constant is a mass prediction, a generation
count or an object-selected parameter. The circle and interval have
different topology/domains, and the interval has extra zero modes.
The result is a discrimination between arguments, not a transfer of
either entire comparator to m202.

## The next physical join is the actual source scalar and its interface

R29's charged source fields live on contractible tubes with their own
weighted kinetic term and natural boundary conditions. They are not
globally smooth zero-extended scalar fields. To continue this SAME
route, an S sector must be specified there, including its variation,
kinetic normalization, mass, coupling to Phi and feedback on the
source. The representation is allowed by R33; its dynamics are not
thereby derived.

There is an additional interface issue, already visible in the
off-shell Green identity: fermions transmit through an artificial
tube boundary and do not satisfy a new Robin condition there.
The scalar lives on its own domain. Thus the full flux from the
proof, not just the simplified OUTER-boundary term, must be retained
when computing a tube-supported interaction. Treating a tube field
as a discontinuous global profile would hide that duty.

The immediate next calculation should therefore vary that scalar
sector in the existing source action and derive its canonical low
mode and interface couplings. Only actual global fermion profiles,
or uniform estimates sufficient for those couplings, can decide
whether the interaction is selective at a finite physical scale.
R31's cutoff trials remain trials. R34's allowed quartic and R19's
conditional singular kernel remain valid in their respective models.

After that, a symmetry-preserving interacting mirror gap still needs
fermion/boson/composite/current diagnostics, source/end anomaly
completion and a controlled limit. Gravity and empirical predictions
remain further parts of the full goal. This overlap calculation is
a necessary calculation within that route, not a replacement goal.

## Verification and custody

The three scientific captures are preserved as
[native output](YUKAWA_OVERLAP_NATIVE_FIRST.json),
[new tests](YUKAWA_OVERLAP_TESTS_FIRST.txt), and
[ten-file run](YUKAWA_OVERLAP_FOCUSED_FIRST.txt).
All six sealed scientific files and 44 frozen inputs are checked
against their pinned commits. The worktree was read-only throughout
the native, new-test and focused runs. Native/new-test output was
inspected before starting the focused run; no scientific repair
was needed. The raw capture directory remains exclusive/append-only.

The full [prior](YUKAWA_OVERLAP_PRIOR.md) distinguishes the 13 retrieved
settled bodies from actual inputs; no historical or literature absence
claim is made. No old corpus result is accepted merely because its
script prints a successful label. Reporting checks and retained
governance debts are in [the final check](YUKAWA_OVERLAP_FINAL_CHECKS.txt).
