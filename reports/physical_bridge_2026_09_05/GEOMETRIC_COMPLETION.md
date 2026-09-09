# R22: the completion must change more than the four-dimensional field list

2026-09-09. Path-local research. Pre-execution seal **b8485ab5**.
[Design](GEOMETRIC_COMPLETION_DESIGN.md),
[producer](geometric_completion.py),
[first output](geometric_completion_first_run.json).

**Result.** R21's anomaly-free added-field theory remains valid, but
its fermions are not supplied by the unchanged source operator.
The proposed negative-charge vectors emerge with the opposite
chirality. Finite-norm nonparallel charged profiles do exist as trial
sections; normalizability is not the obstruction. A single minimally
coupled scalar condensate with no compensating current cannot keep
this order-three connection flat. Curving it changes the differential
whose cohomology counted the three spinors.

These results direct the next calculation to an actual source/defect,
inflow or coupled-field completion. They do not close that route,
derive the Standard Model, or establish a full physical TOE.

## 1. The same-source mode supply has the wrong chirality for the shortcut

Keep R18--R20's prescribed positive source densities, strong maximal
domain, commuting field u*dF and scalar character (zeta,zeta^-1).
For integer gauge charge q != 0, with beta_a >= 1, the field sees
chi^q and the source qF. The latter sign is not independently free.

Recomputing R19's actual cochains, on k=3 source components:

| Charge | H1(q) | H1(-q) | Net in the chosen R_q |
|---|---:|---:|---:|
| q>0, q not divisible by 3 | 3 | 0 | +3 |
| q>0, q divisible by 3 | 4 | 1 | +3 |
| q<0, q not divisible by 3 | 0 | 3 | -3 |
| q<0, q divisible by 3 | 1 | 4 | -3 |

For k components replace 3 by k and 4 by k+1. The chain dimensions
are (1,k+2,1,0), d0 has rank one, and d1 has rank zero at the trivial
character and one at the two nontrivial characters. Thus the formula
holds for all integer charges by residue classes and charge sign,
not extrapolation from the displayed controls. H0=H3=0. Degree two
is the CPT description of the conjugate sector, not extra matter.
The degree/chirality dictionary is standard prior input.
[Braun et al., equations (2.41)--(2.48)](https://arxiv.org/pdf/1812.06072).

Apply this SAME operator to the R21 H representation and its CPT
partner, with one representative per pair:

    intended 4D fields:   3*(16_1 + 10_-2 + 1_4),
    net supplied fields: 3*(16_1 + 10_+2 + 1_4).

The vector's Spin(10) representation is self-dual; its U1 charge is
not. The supplied spectrum has

    (Tr u, Tr u^3, Spin(10)^2-u) = (120, 480, 12), T(10)=1,

instead of R21's (0,0,0). This uses the actual weight sets and full
six-variable anomaly polynomial. Choosing the opposite representative
of any CPT pair leaves its anomaly contribution unchanged: both
the index and the representation's anomaly change sign.

More generally, any finite enlargement by such same-source charged
CPT pairs has

    Tr u   = k*sum dim(R_q)*abs(q),
    Tr u^3 = k*sum dim(R_q)*abs(q)^3.

Each nonneutral contribution is positive in this convention; changing
the common source sign reverses all of them. Vector-like pairs do
not change either trace. This proves a restricted obstruction to
cancelling these anomalies by merely adding more fields governed by
the SAME source/domain rule. It is not an obstruction to mixed source
patterns, other Cartan profiles, defects, inflow or altered dynamics.

A positive escape control is explicit: reversing only the vector's
source response restores the R21 zero polynomial. That is additional
geometric/operator data, not a relabeling of its gauge charge. No such
independent response is derived from the existing u*dF ansatz here.

## 2. A finite-norm charged profile is possible

Main B1302's peripheral words have the SAME presentation basis as
R19. Recomputed exponent sums are (-2,3),(1,2) on the first cusp,
(-1,3),(-3,2) on the second. Charge four therefore has torus phases
(1/3,2/3) and (2/3,1/3), respectively. Neither flat line is trivial.

For ds^2=ds^2+exp(-2s)h_T the scalar norm has radial measure
exp(-2s)ds, but the transverse kinetic integral has measure ds.
Nonintegral torus holonomy gives a strictly positive transverse
Laplacian eigenvalue. Thus constant modulus on an entire cusp can
be L2 while having infinite kinetic energy. The square-torus gap
2/9 in units of 4*pi^2 is an instrument control, NOT the actual
hyperbolic cusp shape or a predicted physical mass.
[Golenia--Moroianu, section 3.2](https://arxiv.org/pdf/math/0701780).

Decay is a genuine alternative. In R18's exact end, write

    H=q*(V(w)+exp(2s)*(b*s+c)), b>0,
    Psi(s,w)=exp(-eta*exp(2s))*p(w), eta>0.

Here p is a smooth nonzero bundle section supported in a contractible
torus patch away from every source puncture. It exists for every
character. A finite-height cutoff and zero extension give a global
trial section, nonzero arbitrarily high in the cusp, on the same
source complement. Put X=exp(2S)>=1, d=q*(b+2c)-2eta and
K_p=||d_A p+q*dV*p||^2. Its three tail integrals are

    ||Psi||^2 = ||p||^2/2 * integral_X^infty e^(-2eta*x)/x^2 dx,
    radial form = ||p||^2/2 * integral e^(-2eta*x)
                                      *(q*b*log(x)+d)^2 dx,
    tangential form = K_p/2 * integral e^(-2eta*x)/x dx.

They are finite for both signs of q. In particular, with
J0=e^(-2eta*X)/(2eta) and
J1=e^(-2eta*X)*(X/(2eta)+1/(4eta^2)), the radial integral is bounded
by ||p||^2*(q^2*b^2*J1+d^2*J0). This follows from
(log x)^2<=x for x>=1 and (u+v)^2<=2u^2+2v^2. The norm and
tangential bounds are ||p||^2*J0/(2X^2) and K_p*J0/(2X).
The variable changes and elementary antiderivatives are exact;
floating quadrature is a separate numerical control, not an interval
PDE certificate. The bounded R15 corrector is restored by multiplying
the section by exp(-qv), using the same weighted graph-space map.

This pays existence of nonzero finite L2 and quadratic-form trial
profiles. It does NOT pay an internal derivation of the new scalar,
a stationary solution, a nonzero vacuum expectation value, its
Yukawa overlaps, or the finite total action of the singular background.
Nor does H0=0 exclude every SYM Higgs: those scalars can arise in
degree one. The full source action and its physical domain remain
separate from this trial-section construction.

## 3. The connection cannot be omitted from the Higgs equations

Consider precisely one minimally coupled complex scalar, a smooth
real potential depending on position and |Psi|^2, ordinary Maxwell
kinetic term, and no other current. This is a classical diagnostic of
the R21 shortcut, not a declaration that this is the full source action.

For one cusp Fourier mode f(s)*exp(i*k*x), variation of the actual
reduced kinetic action gives

    -A''/g^2 + 2*q*(q*A-k)*f^2 = 0.

A constant A with incompatible holonomy and nonzero f does not solve
this equation. In the charge-four order-three control, k=0 and
qA=1/3, the current is 8*f^2/3, not zero.

There is also a general argument, not restricted to one Fourier mode.
For a flat A, Maxwell's equation requires the scalar current to vanish
pointwise. On a simply connected patch trivialize A. Wherever Psi is
nonzero, Im(conjugate(Psi)*dPsi)=0 makes its phase locally constant.
Lift to the connected universal cover and fix this phase on one ball.
The imaginary part then vanishes on that ball and obeys a real linear
elliptic equation with locally bounded potential. Unique continuation
makes it vanish everywhere. Equivariance of a nonzero real-valued
section requires every holonomy to be +1 or -1. The order-three
charge-four line fails that requirement. The theorem applies on the
smooth source complement; no regularity across the deleted sources
is assumed. The analytic input is cited, not proven by a symbolic test.
[Aronszajn, pp.235--236](https://sites.math.washington.edu/~blwilson/Nodal/Aronszajn.pdf).

Both scope controls matter. A real antiperiodic circle eigenfunction
has nontrivial -1 holonomy, zero current and nonzero gradient. Two
separate same-charge fields can have opposite currents even at the
order-three holonomy: the k=0,1 modes with squared amplitudes 2f^2,f^2
cancel their currents exactly. This alone is not a two-field vacuum,
but shows why the single-current proof must not be extended to it.
Additional currents, nonminimal terms and nonabelian configurations
are not excluded.

Finally, for the original commuting charged differential, exact
exterior-algebra computation in every degree gives

    (d-iqA wedge+q*dF wedge)^2 = -iq*dA wedge.

Allowing curvature is an open route, but this expression then ceases
to be the flat complex used in R19. One must derive the full coupled
operator or nonabelian integrability equation before carrying the
three-spinor count into that new background.

## 4. Next physical construction, without discarding the positive results

The completed sub-duty is:

> In the declared common-sign strong-source class, R21's added-field
> anomaly completion is not obtained by its unchanged bulk mode rule;
> finite charged trial norms exist, but a single current-free scalar
> condensate cannot keep the non-real flat holonomy unchanged.

PB-BOUNDARY remains OPEN. Next derive a defect/inflow functional from
the existing fermion mass operator, including the source and cusp
boundary contributions, rather than append its four-dimensional
counterterm alone. Test its normalization, gauge variation and global
definition on the actual H bundles. In particular distinguish anomaly
cancellation from transporting the anomaly to an unaccounted boundary.
The mass/superconnection route is a concrete literature lead, not a
result of this round. An independently realized opposite-source channel
or a full multi-field/nonabelian solution is another live route.

Retain source/parent/domain selection, Spin(10)-to-SM interactions,
the neutral low-energy cusp channel, a common dynamical gravity
construction and empirical tests. None follows from the anomaly trace.

## 5. Verification and receiving-seat boundary

The first producer succeeds after seal b8485ab5, native runtime 6.429 s;
complete JSON saved before yielding. The unchanged R18--R21 dependencies
plus R22 have 69 passing tests, one optional-GUI warning, 31.57 seconds.
The 41-file expanded regression finishes with 285 passed / 13 failed /
8 errors, one warning, 291.22 seconds, exit one. Its failed/error ID
set is EXACTLY R21's: zero added, zero missing. All original source
and assertions remain unchanged. Complete stdout is saved, with only
environment prefixes redacted publicly; raw output is retained outside
the worktree. These are focused and expanded checks, not the full repo.
Receipts: [focused](GEOMETRIC_COMPLETION_CHECKS.txt),
[expanded](GEOMETRIC_COMPLETION_REGRESSION.txt).

Main B1304 independently read this branch only through R20 at
6f862099. It confirms the C3 locus and two upstream corrections, not
R21 or R22. No independent proof review, whole-repository green
certificate, main B allocation, main merge or full TOE is claimed.

The first reporting gate also remains in
[its original receipt](GEOMETRIC_COMPLETION_GATES.txt): 26 pass / 4 fail.
It caught public branch-label tokens and missing prior-arc context in
the new law rows. Both reporting issues were corrected without changing
scientific files or gate baselines; the originally sealed prior-sweep
JSON remains recoverable at b8485ab5. Older governance debts are not
waived. This reporting correction is not a scientific rerun.

The [corrected staged pass](GEOMETRIC_COMPLETION_GATES_CORRECTED.txt)
returns 27 pass / 3 fail, review due at 124 merges. Only the three
older attribution/static-vacuity/literal-provenance gate debts remain;
the new reporting issues are resolved. This is not full main banking.
