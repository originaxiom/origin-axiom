# R25: the reference wall supplies the opposite response, with mirror modes

2026-09-09. Path-local research. Design, producer and tests sealed and
pushed at **16ba8ce1**, before their first execution. No B allocation.

**Result.** Implementing R23's positive reference mass as a free
physical collar produces a six-dimensional Weyl channel on the
actual negative-mass eigenline. On R24's whole rounded source boundary
its effective four-dimensional index is **-k**, opposite the interior
+k. Its anomaly is the negative of the FULL R23 eigenbundle response.
This derives a specific compensating free spectrum from the mass wall,
not from an appended list of oppositely charged representations.

The cost is also computed: it is a mirror sector, and moving its
normalized modes toward the ends does not decouple them from the
unchanged normalizable constant gauge field. The wall also introduces
a scalar mass outside the original traceless Higgs ansatz. This is
therefore an explicit conditional free completion, NOT a source-selected
defect, a mirror-free physical theory, or a no-go for other completions.
R19's conditional three/zero kernel is not withdrawn.

## 1. The added ansatz, with the actual sign dictionary

Let Sigma be the ENTIRE compact rounded boundary of an admissible
R24 regulated core, with its boundary orientation. The nonzero actual
mass m=q grad F defines P+=(1+n.sigma)/2 and P-=1-P+. Their lines
have c1(L+)=K and c1(L-)=-K; R24 proves integral_Sigma K=k for the
positive-charge source class. Flattening |m| on this fixed boundary
does not change either line. Nothing selects k or the sources here.

In a product collar, normal coordinate r increases outward. Choose
M,ell>0 and put

    Mwall(r,x) = M P+(x) + M tanh(r/ell) P-(x).

The inside limit is M n.sigma; the outside limit is +M identity.
Its trace is M(1+tanh(r/ell)), so the scalar mass coefficient is
M(1+tanh(r/ell))/2. Both endpoints and the trace are computed from
the actual projector matrix. This is not another q dF one-form in
the original commuting Witten differential. No supersymmetric UV
origin of this extra mass, or action selecting this collar, is claimed.
A reference used to define a determinant does not by itself add
physical particles; R25 explicitly tests what happens IF it is
implemented by this physical mass interpolation.
[Choi--Ohmori, discussion after (2.57)](https://arxiv.org/pdf/2205.02188).

The chirality sign is not chosen to make cancellation work. Four
explicit gamma matrices give chi4=-gamma1 gamma2 gamma3 gamma4;
chi4=+ labels R23's odd/left sector. Set the internal seven-dimensional
matrices to chi4 tensor sigma_i. On right chirality they are -sigma_i,
the exact R23 even-form kinetic map. With the third internal direction
outward, direct multiplication gives

    chi6 = i product(gamma_tangential) = Gamma_r
         = chi4 tensor sigma3.

All Clifford anticommutators, the original kinetic map and the
reversed-sign rejecting control pass. The positive-normal projector
has complex rank four: one six-dimensional Weyl spinor per gauge
component. R23's charged-pair reality convention is retained; its
conjugate representative is not a second determinant.

## 2. Solve the normal channel before counting it

The equation is (Gamma_r partial_r+Mwall)psi=0. On the crossing
negative eigenline, with Gamma_r=+1, its solution is

    f(r) = cosh(r/ell)^(-a),   a=M ell>0,
    ||f||^2 = ell sqrt(pi) Gamma(a)/Gamma(a+1/2).

Direct differentiation gives zero residual. The opposite normal
chirality grows at an end. More generally exp(-c integral mass dr)
decays at both ends exactly when c*sign(m_inside)<0 and
c*sign(m_outside)>0. All four asymptotic sign pairs are tested: a
crossing gives one chirality, a non-crossing gives none. The constant
positive channel has no two-sided normalizable normal solution.

For the normalization, t=tanh(r/ell) gives
ell integral_-1^1 (1-t^2)^(a-1) dt. Substituting u=t^2 gives the
beta integral above. Exact integer-exponent polynomial integrations
give 2, 4/3, 16/15 and 32/35, rejecting a missing Jacobian or factor.
This agrees with the familiar sharp-wall exponential comparator;
the sign is derived here in our seven-dimensional representation.
[Fukaya et al., (2.1)--(2.12)](https://arxiv.org/pdf/2001.03318).

An infinite PRODUCT normal line is only this transverse localization
model. Its infinite volume cannot simultaneously be assumed to carry
the original finite-volume constant gauge mode. A finite collar gives
the localized approximation when its gap times its width is large.
No fixed-M approximation uniformly through the singular exhaustion,
or full finite-collar zero-eigenvalue census, has been proved.

## 3. The induced connection and the spin-surface index

Projection of the R-doublet connection gives P- nabla_R P-, including
both ambient curvature and the derivative of the projector. This is
the same bundle identified in R24, not an independently chosen flat
line. Smooth product-metric/connection deformations do not change its
Chern number. For a normalized local negative eigenvector v, direct
curvature of v* (d+Gamma_R) v agrees with the projector expression.
With a nonzero curved test connection the omitted-connection residual
is h sin(2 theta)/(4 pi), while K-+K+=0 exactly. The flat sphere
has negative-eigenline flux +1, the opposite of R23's positive line.

The off-diagonal P+ dP- P- is NONZERO in the same control. Thus
the projected tangential operator is the adiabatic low-energy operator,
not an exact finite-M decomposition for a varying mass direction.
At each fixed compact boundary the tangential scale can be separated
from M. This does not establish the actual open-end determinant or
discard bulk-edge cross-correlations in the complete effective action.

For a compact spin surface of genus g, let S^2 be its canonical
bundle. Then deg(S)=g-1 and the positive spin Dirac operator twisted
by L- and a flat scalar gauge character has the Dolbeault index

    ind_2 = chi(S tensor L- tensor flat)
          = (g-1-k) + 1-g = -k.

For a rank-r flat gauge factor the numerical index is -r k; as a
representation-valued index it is -k copies of R. The six-dimensional
chirality relation above makes the four-dimensional left-minus-right
index -k as well. This uses the ordinary compact spin-surface index
theorem, not a new noncompact index theorem.
[Freed, section 4](https://abel.math.harvard.edu/~dafr/detsur.pdf),
[Taylor, (10)--(16), (33)--(36)](https://mtaylor.web.unc.edu/wp-content/uploads/sites/16915/2018/04/rroch.pdf).

Omitting S would give -k+1-g: for g=4,k=3 it incorrectly gives -6.
An independent spherical Cech control enumerates the monomials of
O(d-1) and its first-cohomology Laurent powers. It gives
(h0,h1)=(max(d,0),max(-d,0)) and index d for every tested d=-4..4.
Genus and reference-sign controls agree; disconnected boundaries
are handled by summing component degrees, not guessing their genera.

In the connected g=4,k=3 positive-reference case the holomorphic
line S tensor L- tensor flat has degree zero. Its h0 is zero unless
it is holomorphically trivial, when h0=1. Riemann--Roch then gives
(h0,h1)=(0,3) or (1,4). R25 does NOT determine which line the actual
geometry supplies, or identify it with R19's Alexander character.
The net -3 does not require that identification. These are the edge's
two possible counts under those surface hypotheses, not a new count
of the completed finite system.

For the negative reference, P+ crosses from +M to -M and Gamma_r=-1.
The line degree is now +k but the six-dimensional chirality reverses:
the four-dimensional index is STILL -k. Changing the reference sign
does not remove these mirror degrees of freedom. Reversing the mass
flux reverses the result; zero flux gives zero net index, not a theorem
that the six-dimensional channel or all paired modes vanish.

## 4. Full anomaly matching, not just an index coincidence

Use R21's ACTUAL H spinor weights and I_(2j)=[Ahat ch(R)]_(2j).
For the positive-reference wall the six-dimensional Weyl polynomial is

    E8 = [Ahat ch(R) ch(L-)]8
       = I8 - K I6 + K^2 I4/2 - K^3 I2/6 + K^4 I0/24
       = -R23 B8.

Independent substitution of every weight ell->ell-K gives exactly
this answer. Dropping higher powers fails the full-class test. The
negative reference gives -[Ahat ch(R) ch(L+)]8 and has the same
coefficient -I6 of K. In a product gauge-zero-mode background, with
K internal, integration over Sigma therefore gives -k I6 for either
reference. General external families still require the full polynomial.

For k=3 this cancels R19's three-spinor polynomial; the original
linear and cubic U1 traces are both 48, not zero. R23's internally
constant-gauge control still has bulk variation zero and uncancelled
interior coefficient +3 BEFORE the wall is included. The wall supplies
the compensating -3; it cannot be omitted from that bookkeeping.

This is perturbative anomaly-polynomial matching for the stated free
interface. It is NOT a global eta/Pfaffian phase, existence of every
required extension, an interacting boundary action, or a complete
singular quantum determinant. Finite core/wall mixing can pair their
opposite modes and give them masses. That removes vector-like pairs;
it does not by itself leave only the original unpaired chiral spectrum.

## 5. Why moving the wall does not remove its gauge charge

For the same minimally coupled gauge field with normalized constant
profile u0=1/sqrt(V), canonical fermion normalization gives

    g_ij = g7 integral psi_i* u0 T psi_j
         = (g7/sqrt(V)) T delta_ij.

The fermion norm uses its actual kinetic measure. This identity holds
wherever the normalized mode is localized, assuming the stated
unbroken generator and finite positive gauge normalization V. Sending
a mode to small cusp area is not a charge-suppression mechanism.

The exact translating control f_R(x)=sqrt(M) exp(-M|x-R|) has unit
norm and overlap <f_0,f_R>=(1+M R)exp(-M R), tending to zero. Its
constant-gauge coupling stays g7/sqrt(V). With cusp measure exp(-2s)ds,
use the compensating exp(s) profile factor on s>=0. The raw half-line
norm is Z=1-exp(-2M R)/2. After normalization, probability below a
fixed A<R is

    (exp(2M A)-1)/(2 exp(2M R)-1) -> 0,

but total gauge charge is unchanged. This is an escape control, NOT
the actual sourced wall wavefunction or a strong Hilbert-space limit.
By contrast a localized gauge profile gives vanishing coupling in the
control, and V->infinity gives g4->0: both alter the retained gauge-mode
assumption. No bound on every warped, interacting or nonlocal completion
is inferred from this calculation.

## 6. Verdict, next executable question and custody

Closing sentence:

> In the declared free reference-wall ansatz, the derived boundary
> channel has the opposite eigenbundle anomaly and net index, but
> localization alone cannot decouple it from the unchanged constant
> gauge mode; the interpolation is an added mass, not a selected source.

Only that candidate is scoped. PB-BOUNDARY remains OPEN. The next
concrete question is whether compactly supported gauge curvature and
mass backreaction preserve the actual R18/R19 graded Dirac index even
though d_A^2 is no longer zero. Start from the proved closed-range gap
and an explicit operator perturbation, not by reusing flat cohomology
or assuming every kernel multiplicity survives. This tests a way to
retain the chiral asset while allowing R21-type massive-U1 dynamics.
Its gauge variation, quantum matching, scalar/defect origin and coupled
finite-action equations must still be derived together. An index
stability statement alone will not complete that physical construction.

Source/amplitude/domain/orbit selection, Spin(10)-to-SM breaking,
the neutral four-dimensional limit, a common gravity sector and
empirical predictions remain distinct duties. The corrected curved-cone
and certified partial-filling candidates are not excluded or replaced.

First native run: **7.677 s**, complete JSON retained. **15 new tests
pass**; focused dependencies give **71 passed, 1 failed** in 31.55 s,
the failure being the preserved R24 raw matrix comparison. The quiescent
46-file regression gives **341 passed, 14 failed, 8 errors**, one warning,
in **287.77 s**. Its 22 failed/error IDs are EXACTLY R24's, with none
added or missing. No original source, assertion or tolerance was edited.

Receipts: [native](boundary_wall_first_run.json), [focused](BOUNDARY_WALL_CHECKS.txt),
[regression](BOUNDARY_WALL_REGRESSION.txt), [pre-execution metadata](BOUNDARY_WALL_PREEXEC.txt).
Raw unredacted test outputs are retained outside the repository; only
environment path prefixes are redacted in the public receipts. The
all-head intake and primary-source limits are in [the prior](BOUNDARY_WALL_PRIOR.md).
No full-repository green, independent proof review, main banking or
completed physical TOE is claimed. Reporting gates are recorded
separately in BANKING_RECEIPT.md and BOUNDARY_WALL_GATES.txt.

The final refetch received five outside-seat commits through 7ce09cba.
Their independent matrix-residual agreement and numerical R20 bridge
capability are scoped in [the final intake](BOUNDARY_WALL_INTAKE.md),
not adopted as an independent proof or banking review of this result.
