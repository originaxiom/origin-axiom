# R14 — an explicit singular Higgs field on the three-source cusp end

**Positive construction:** the prescribed three-line cusp-end background
is now an explicit solution of the commuting sourced Higgs equations.
Its actual flux supports the outward-cusp/inward-tube boundary pattern.
This preserves R72's conditional three-line route. It does not establish
a global m202 field, source selection or three physical chiral families.

Read alongside [R13](HARMONIC_CUSP.md): that earlier smooth meridional
background is a different field, not an obstruction to this one.
The user's complete physical-theory goal remains unchanged.

## 1. Exact solution, with all input data visible

Take the hyperbolic cusp metric ds^2=(|dw|^2+dz^2)/z^2 on
C/(Z+tau Z) x [z0,infinity), with A=Im(tau)>0. Set the curvature
length to one. Specify vertical lines at p_i, constant charge DENSITIES
beta_i per hyperbolic proper length, and Q=sum beta_i. For m202's
hexagonal cusp use tau=exp(i pi/3), and the order-three rotation's
three fixed points 0,(1+tau)/3,2(1+tau)/3 after translating its fixed
center to zero. R12 already verified the actual m202 cusp witness;
R72's global axis-connection census is not independently recertified here.

Define

    U(w) = log|theta_1(pi w | tau)| - pi (Im w)^2/A,
    F(w,z) = sum_i beta_i U(w-p_i)
             + (pi Q/A) z^2 log(z/z0) + c z^2,
    phi = u dF,    W = 0.

The Lie direction u is commuting and fixed on this cusp; its physical
parent, normalization and global transport are not identified by this
formula. W=0 is the declared abelian cusp ansatz, NOT a covert identification
with the principal geometric Riley connection. The beta_i, c and matching
data are prescribed inputs until the originating construction fixes them.

The theta quasiperiods make U doubly periodic, and its simple logarithmic
zeros give the distributional identity

    Delta_T U = 2 pi (delta_0 - 1/A).

These are standard theta properties, used as an explicit Green-function
construction, not claimed as new special-function mathematics.
[NIST DLMF 20.2.1, 20.2.6 and zeros](https://dlmf.nist.gov/20.2).
Away from a zero, log|theta_1| is harmonic and the quadratic term gives
-2 pi/A; the local log radius singularity supplies the delta function.

For Delta_H=z^2(Delta_T+partial_z^2-z^-1 partial_z), the radial term
has F0''-F0'/z=2 pi Q/A. Hence

    Delta_H F = 2 pi z^2 sum_i beta_i delta_(p_i),

so phi is closed and coclosed away from its prescribed sources. In this
commuting flat-gauge ansatz the bracket terms vanish. This is the sourced
abelian Higgs problem specified by the cited framework, not proof of its
physical realization or a full G2/TOE geometry.
[Pantev--Wijnholt, section 3.2](https://arxiv.org/pdf/0905.1968),
[Braun et al., eq. 2.18](https://arxiv.org/pdf/1812.06072).

The radial z^2 log(z) term is ESSENTIAL when Q is nonzero. Omitting it
leaves off-source residual -2 pi Q z^2/A. For balanced densities Q=0,
the torus Green sum alone is harmonic off the lines: the positive control.
The local single-geodesic potential log(tanh distance) also satisfies its
cylindrical-coordinate equation, but is not substituted for the global
periodic cusp Green function.

## 2. What the cusp and charge tubes actually do

The outward top-cusp normal is z partial_z. Its field component is

    phi_z = u z^2 [(pi Q/A)(2 log(z/z0)+1)+2c].

For positive total density Q, it is eventually positive along u for
every fixed finite c in this family. At a fixed finite height c DOES
change the flux: with beta=(1,1,1), at z=1 the scalar component is
-29.1172, +10.8828, +50.8828 for c=-20,0,+20. The Poisson source is
unchanged. The matching datum has not been selected by the cusp alone.

Near a line phi is beta_i u d log R plus smooth terms. The outward
normal of the EXCISED domain points TOWARD the removed line. For a
positive charged sector and beta_i>0, the tube is therefore an INWARD
boundary, not an empty boundary. This corrects R72 section 2's statement
that the same-sign inward boundary is empty. The annular tubes have
chi=0, so the conditional Euler number can stay unchanged despite this
important operator-domain correction.

The finite-radius computation makes the balance explicit. With three
radius-.01 tubes and a cusp slab 1<=z<=3, beta=(1,1,1), c=0:

| boundary | scalar flux |
|---|---|
| top, with endpoint disks removed | +30.1003384590 |
| bottom, with endpoint disks removed | -9.4145211670 |
| three charge tubes together | -20.6858172920 |
| total | -3.55e-15 |

Dropping the tubes leaves +20.6858, not zero. The bottom is a core-matching
interface with its own negative flux, NOT an extra outward physical cusp.
Changing all charge signs reverses every flux. The balanced (-2,1,1)
control has zero top/bottom flux and tube fluxes which cancel.

Analytically the finite-radius tube flux for line i is

    -[2 pi beta_i - (2 pi Q/A) pi epsilon^2] log(Z/z0).

This includes the torus Green function's uniform term. Using the punctured
torus area A-3 pi epsilon^2 gives exact cancellation with the end caps.
It is not enough to balance an unpunctured torus against finite tubes.

On a whole compact truncated m202 with three proper arcs, R12's gluing
identity gives chi(C)=-3. If global matching supplies outward flux on
BOTH exterior cusps and positive-density inward tubes, the inward subset
is T (the three annuli), not empty. The complementary sign uses E, the
two three-punctured tori. Their Euler values are 0 and -6, yielding
relative Euler -3 and +3. This is the retained CONDITIONAL topological
index, not a spectrum computation. A nonempty T also removes the H0
mistake that an empty relative subset would introduce.

Constant line density is not a finite total charge. On a complete cusp
the line length is infinite and the running flux changes as 2 pi Q log Z.
On filled closed curves Gauss's law weights constant densities by curve
length (or integrates a variable density); an unweighted sum of labels
needs its own convention. Equal signs are still impossible without a
compensating source or boundary on a closed compact base. The cusp is
precisely what permits the escaping flux in this end construction.

## 3. Symmetry does not force equal densities

The exact order-three matrix [[-1,-1],[1,0]] has fixed torus points
(0,0),(1/3,1/3),(2/3,2/3). The order-six rotation acts by [0,2,1]:
one distinguished line endpoint and one exchanged pair.

Both densities (1,1,1) AND (2,1,1) give an invariant potential, with
rotation residual <=8.89e-16. (1,2,1) breaks the rotation by .5174.
This independently preserves R72's two-orbit distinction; symmetry
does not set beta_0=beta_1. Choosing the three charged lines rather than
other available loci is also not settled by this local field solution.

## 4. Verification and limits toward the goal

Sealed **a6d7c534**, before first execution:
[design](SINGULAR_CUSP_DESIGN.md), [source](singular_cusp.py),
tests/test_physical_bridge_singular_cusp.py. First run succeeds;
[full output](singular_cusp_first_run.json) is retained without truncation.

Two theta-series cutoffs agree; independent 50-digit mpmath evaluation
differs by 2.49e-16. Periodic potential/gradient errors are below 4e-15.
Analytic off-source PDE errors are below 1.03e-14. Independent second
finite differences at two steps stay below 7e-5 at all nine tested
sign/point cases. The symbolic equation and Green-function proof support
the exact statement; a finite numerical spot-check alone would not.

Nine new mathematical locks pass. The R12--R14 group is **34 passed,
one GUI warning, 14.44 seconds**. [Raw checks](SINGULAR_CUSP_CHECKS.txt).
The previous R13 broad regression was 159 passed, three preserved old
failures and eight original R11 fixture errors; it predates R14 and is
NOT described as a certificate of R14 or full-suite green.

The next required work is global CORE MATCHING and the charged operator:
extend compatible end fields through the actual m202 complement, specify
source densities and fibre/gauge transport, select the parent adjoint
representation and physical domain, then compute normalizable charged
modes with their conjugates and interactions. A counted 27 is not by
itself the adjoint field content of an E6 gauge theory. No such parent
identification or global matching has been earned by this end calculation.

This is a usable solution of a necessary differential piece of the live
candidate, not an unrelated easier theory substituted for the goal.
The other route is kept alive; none of its remaining duties is silently
declared solved. CC numbering remains respected, with no new B number,
PR, merge, push or completed-main-bank claim.

[Reporting gates](SINGULAR_CUSP_GATES.txt): 27 pass, 3 fail, with the
same inventory attribution, two static-vacuity classifications and four
older seal-marker omissions as R13. Review-due is 103. No new R14 gate
defect; these outstanding checks are not represented as discharged.
