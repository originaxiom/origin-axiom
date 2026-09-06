# R13 — the meridional harmonic field is now computed numerically

The leading cusp coefficient is **8.52196526983**, for the declared
unit meridian period and curvature-coordinate convention. This is a
convergence-tested numerical result, not an exact nonvanishing theorem
or physical constant. It addresses the explicit uncomputed-coefficient
caveat in the SM seat's particular theta-odd abelian cusp argument.

The full truncated harmonic 1-form is computed and its transport under
the actual group generators checked. The physical operator must retain
its tangential part too. Nonzero period makes the background non-L2 on
the complete hyperbolic cusp; that does NOT exclude normalizable charged
fluctuations. **Net chirality is not established by this calculation.**
R4--R10's conditional physical model and R11--R12's positive results stand.

## 1. The owner's relay, distinguished from the new calculation

The complete [sB1277 cusp addendum](https://github.com/originaxiom/origin-axiom/blob/2a7f88553652b9b28efefaf89925c116e008b639/frontier/B1277_the_vacuum_manifold_of_the_closing/ADDENDUM_2026-09-06_the_arcs_and_the_corners.md)
and producer at 2a7f8855 were read, as was the
[sB1279 symmetry report](https://github.com/originaxiom/origin-axiom/blob/6f077ef2ba988a6a4d98b177758a0c2d67d6377c/frontier/B1279_the_symmetries_of_the_closing/FINDINGS.md).
The latter explicitly says N=0: three-family multiplicities plus their
mirrors are not three unpaired chiral families. Its 706,464 lines and
19,624 orbits are received claims, NOT independently recounted in R13.
Its CP-projection argument is not adopted as a no-go for other physical
boundary, localized or singular sectors.

Physics-seat R60/R70 and both R70 producers were read at
9a5d19285a1b01e26d20948df40afd281d827316. Main pin: 2901ae9f.
Local B351's Cartan, B739's cusp expansion and the READ primitives in
B1007_arb_maass/_reference_double.py supply prior art. The existing
solver is ADAPTED, not rediscovered. Sources are not merged or rewritten.
Search terms and scopes are in [the design](HARMONIC_CUSP_DESIGN.md);
no universal absence claim is made about the corpus.

CC's [banking receipt](BANKING_RECEIPT.md) is respected: R13 is path-local,
not a B allocation or physics-seat round. This is a local research result,
not independent-receipt/main-bank certification or publication.

## 2. An actual field, not just a cohomology dimension

Set w=y+i L x, L=2 sqrt(3), with x longitude, y meridian and height z.
The declared curvature-unit metric is

    ds^2 = (L^2 dx^2 + dy^2 + dz^2)/z^2.

For a commuting flat-connection Higgs ansatz, d phi=d*phi=0; the internal
1-form norm enters the 4d kinetic reduction. These specify a conditional
model, not physical identification or UV completion of the object.
[Braun et al., eq. 2.18 and Appendix B](https://arxiv.org/pdf/1812.06072).

On the universal cover phi=df, but f is NOT single-valued on m004:
f(gP)-f(P)=ab(g), with period +1 on both Riley generators. Its expansion is

    f = y + sum c_j z K_1(kappa_j z) T_j(x,y),
    kappa_j = 2 pi sqrt(k_j^2/L^2+l_j^2).

The scalar Laplacian is z^2(f_zz-f_z/z+f_xx/L^2+f_yy). Exact symbolic
checks verify the kernel equation F''-F'/z-kappa^2 F=0 and normal component

    g = phi(z partial_z)
      = -sum c_j kappa_j z^2 K_0(kappa_j z) T_j.

The naive cylinder kernel exp(-kappa z) leaves residual
kappa exp(-kappa z)/z and fails. The growing I_1 branch is excluded by
the declared growth class. Standard identities and asymptotics:
[NIST 10.25](https://dlmf.nist.gov/10.25), [10.40](https://dlmf.nist.gov/10.40).
Decay is exp(-kappa z) times a power, or exp(-kappa exp(r)) at r=log z.

The source's first allowed angular modes are sin(4 pi x) and then
cos(4 pi x)sin(2 pi y), with kappa ratio 2. Exact symmetry checks retain
that ordering. The slow coefficient is solved for, not assumed or fitted
to an empirical target. The meridional period is tracked through every
group word AND peripheral lattice reduction in the collocation equations.
The bounded height ascent uses genuine Gamma translates even if ascent
stalls; it is not claimed to certify the full fundamental domain.

## 3. Convergence and direct transport

| cutoff in dual norm | height | real modes / rank | held-out max residual | leading coefficient |
|---|---|---|---|---|
| 4 | .65 | 21 / 21 | 1.24e-6 | 8.521964948584 |
| 6 | .65 | 48 / 48 | 2.91e-10 | 8.521965269858 |
| 8 | .55 | 86 / 86 | 2.72e-11 | 8.521965269830 |
| 10 | .65 | 135 / 135 | 5.00e-15 | 8.521965269826 |
| 10, longer moves | .75 | 135 / 135 | 4.41e-15 | 8.521965269826 |
| 6, theta-only basis | .65 | 192 / 192 | 2.89e-10 | 8.521965269825 |

The last fit does NOT impose half-translation/glide restrictions. Its
agreement tests that restriction instead of simply assuming it. Relative
spread across the three high-cutoff fits is 4.71e-13; the theta-only
fit differs by 1.23e-13. Scaled condition estimates are 1.43--2.45.
The declared NUMERICAL_CANDIDATE criterion passes. These are finite
stability/residual checks, NOT rigorous infinite-tail bounds or error bars.

Zero period returns zero; a manufactured single mode is recovered to
4.44e-16 in its coefficient. Omitting the cocycle gives 1.33938 error
in the genuine held-out equation. Forgetting multivaluedness is detected.

Separately sealed POST-RESULT checks remove the height-ascent verifier:
direct primitive transport on all retained random points with both
heights >= .55 gives a/a^-1 errors <=4.45e-16 (3,000 points each),
b error 2.14e-13 (505 points), and b^-1 error 9.89e-14 (460 points).
The differential obeys the actual 1-form pullback with the group Jacobian
to 3.77e-10 on 16 points per generator, at both derivative steps. Its
analytic components match potential differences at three other points.

Changing the leading coefficient by one percent preserves LOCAL
harmonicity but breaks b/b^-1 transport by about .0079. This is a
discriminating control. It supports the particular annular ASYMPTOTIC
cusp pattern, without proving the exact global function or identifying
the coefficient as a physical mass or coupling.

## 4. The physical normalization distinction

Any closed real 1-form on this standard cusp has periods p along y and
q along x. Write phi=p dy+q dx+dF with periodic F. Torus averages of
periodic derivatives vanish. Positivity/Cauchy--Schwarz gives

    integral_(z0..Z) |phi|^2 dvol
      >= (L p^2+q^2/L) log(Z/z0).

Restoring curvature length ell multiplies this by ell. This is a bound
on ALL closed forms with these periods on the specified metric, not
just our truncated fit. Nonzero period therefore forbids finite kinetic
normalization for THIS profile as a dynamical 4d modulus on the complete
hyperbolic end. It does not calculate the full static action, which has
different derivative/curvature terms.

Positive controls: a constant scalar has finite norm L/(2 z0^2); the
differential of the decaying sine mode has finite norm
L kappa z0 K_0(kappa z0)K_1(kappa z0)/2, agreeing with direct integration.
Finite cusp volume alone neither proves nor disproves 1-form normalizability.

The computed field keeps period 1 to 1.12e-16. Tangential/normal
orthonormal RMS values are 1.08447/.37134 at z=1, and 2.00023/.02828
at z=2. The tangential period part grows in pointwise norm while the
radial part decays. Its radial sign plot is NOT the whole Higgs field.

An external non-L2 BACKGROUND can still affect normalizable CHARGED
FLUCTUATIONS. Those require representation, twisted operator, measure,
domain and source data; none is supplied by the norm alone. A finite
cutoff, closing, defect or different physical metric changes the problem
and is not ruled out here. The complete-end calculation is not an
already established mixed-boundary index domain.
[Pantev--Wijnholt's boundary problem](https://arxiv.org/pdf/0905.1968).

## 5. R70's coweight parity, corrected without discarding D5

In B351/R70's specified Bourbaki Cartan, diagram theta has fixed Cartan
dimension 4 and exchanges omega_1 and omega_6. Reconstructing all 72
roots by simple reflections gives:

| direction | diagram parity | centralizer dimension |
|---|---|---|
| omega_1 or omega_6 | neither even nor odd | 46 |
| omega_1+omega_6 | even | 30 |
| omega_1-omega_6 | odd | 46 |

A single omega_1 is not theta-odd in this frame. Its projections are
half the sum/difference; the odd difference still has a D5 centralizer.
A nonzero scalar charge at a pointwise fixed arc in a one-direction
equivariant ansatz still needs an even direction, so pure omega_1 does
not become admissible there automatically. Multi-component fields must
transform their forms and Lie directions together. This does not certify
the full E8 involution lift or establish vector-like/chiral matter.

## 6. Toward the full physical goal

An explicitly assumed coefficient is now a computed differential-field
input. The narrow regular theta-odd annular route does not gain net
chirality. R12 already explains that any regular theta-odd sign partition
on a torus has zero boundary Euler, independently of its leading mode.
A pure mixed-mode crossing is not a regular boundary; rectangular
interiors cannot silently replace a compact mixed-boundary operator domain.

The constructive next step is the CHARGED operator for a sourced allowed
Higgs/background representation, with normalizability and complete
boundary prescription. The scalar meridional class, Cartan direction and
E8 parent matter branching are distinct inputs. Mirror-paired vacuum
counts and R12's chosen three disks do not discharge these duties.
PB-BOUNDARY and PB-ACTION remain live, alongside the same theory's gravity
and empirical content. The user's complete-physical-TOE goal is unchanged.

### New source received during reporting — physics R71/R72

The fresh fetch reached **124c2466cb80f597f4447f1a6f0e8c259681ee58**.
R71, R72 and the accompanying FC-to-CC relay were then read in full.
R71 retracts R70's universal vector-like inference: some of its tested
outer-lift directions are chiral but anomalous. R72 explicitly changes
the lift hypothesis, distinguishes inner from outer, and proposes three
singular charge lines on the two-cusped m202, with a conditional
3 x (16+10+1) count. This candidate must NOT be discarded using R13's
different smooth, meridional m004 background.

R72 now retains the external cusp contribution to proper-arc excision,
as R12 required. Its own fences still say that the global harmonic
source field is not constructed and that the physical ADE-fibre lift
is additional data. Its signs, manifold selection and the D2/source
identification are separately discussed, not solved by counting lines.
R12 already verified m202's genuine three-fixed-point cusp witness;
the newer line-connection census and representation claims are located
next audit targets, NOT independently certified by R13.

The constructive continuation therefore includes this new singular
candidate: construct its Higgs field and check its actual BPS equation,
flux, charged representation and boundary domain. R13's non-L2 fact
does not kill an external singular background. Nor does an inner-lift
possibility alone prove the physical spectrum. Source:
[R72 at the fetched pin](https://github.com/originaxiom/origin-axiom/blob/124c2466cb80f597f4447f1a6f0e8c259681ee58/reports/fresh_physics_seat_2026-09-01/R72_THREE_FROM_THE_THIRD_ROOT.md).

## Evidence and certification

Original seal **9c646408**: [design](HARMONIC_CUSP_DESIGN.md),
[producer](harmonic_cusp.py), tests/test_physical_bridge_harmonic_cusp.py.
Transport seal **afe8f578**: [control design](HARMONIC_CUSP_TRANSPORT_DESIGN.md),
[producer](harmonic_cusp_transport.py), tests/test_physical_bridge_harmonic_transport.py.
[Machine output](harmonic_cusp_results.json), [complete raw repeat](HARMONIC_CUSP_RUN.txt),
[first received capture](HARMONIC_CUSP_FIRST_CAPTURE_TRUNCATED.txt).

The original run succeeded in 5.81378 seconds, but the terminal capture
truncated its output. The RECEIVED bytes are preserved. An unchanged-source
repeat with a larger capture limit succeeded in 4.78949 seconds and
supplies the complete output. This is disclosed capture loss, not a
silently overwritten first scientific failure.

The R12/R13 group has **25 passed, one GUI warning**, in 15.85 seconds;
fourteen are new R13 locks. All scientific seals remain unchanged.
Repository-wide gate and regression results are recorded separately,
without erasing earlier failures. These checks are not full-suite green,
an independent receiving-seat review, or a proof of the TOE.

The first broad regression's process handle 71784 and its in-memory
capture did not survive the turn transition; the last received partial
output was nineteen dots and eight fixture errors. On resumption the
handle was absent and no pytest process was live. No completion verdict
is inferred from that partial run. A new quiescent regression is labeled
as a repeat, not passed off as the original completion.

The completed repeat is **159 passed, 3 failed, 8 errors**, one GUI
warning, in 154.55 seconds. The three failures are the preserved G2
NumPy-key serialization case and two original R7 small-step second-
derivative controls; the eight errors are the original R11 QQ/ZZ HNF
fixture. Their separately sealed repairs remain passing. No new R13
failure or tolerance relaxation. See [the raw repeat](HARMONIC_CUSP_REGRESSION_REPEAT.txt).

[Reporting gates](HARMONIC_CUSP_GATES.txt): 27 pass, 3 fail, the same
inventory attribution, two static-vacuity classifications and four older
seal-marker omissions as R12. Review-due: 101. No new R13 gate failure.
The gate pass on current digests is not a completion certificate for the
research goal or the main banking protocol.
