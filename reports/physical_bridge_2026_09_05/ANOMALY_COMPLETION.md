# R21: an anomaly-free subgroup completion, with its geometric cost computed

2026-09-08. Path-local research, not a main B arc or a complete TOE.
Original design/source/test seal **6a08d343**; action-control seal
**d21189d6**. [Design](ANOMALY_COMPLETION_DESIGN.md),
[prior receipt](ANOMALY_COMPLETION_PRIOR.md),
[exact first output](anomaly_completion_first_run.json).

**Result.** The actual subgroup of R20's quotient parent admits a
27-dimensional representation whose spinor is precisely R19's positive
adjoint spinor. Adding its vector and singlet pieces cancels the
three-spinor anomaly. A charge-four scalar gives those added fermions
gauge-invariant masses, leaving the original chiral Spin(10) content.
This is an explicit added-field four-dimensional effective theory,
not yet a reduction of the sourced geometry.

The geometric test matters: that scalar has no nonzero parallel
section in the existing pair-free holonomy. The smallest allowed
parallel singlet has charge twelve and retains a gauge Z3. With only
the original three spinors left light, this Z3 has eta=1/3 modulo one.
Thus the parallel-Higgs shortcut needs additional anomaly-carrying
content; nonparallel fields, defects and inflow remain live routes.

## 1. The actual global subgroup, not an imported parent 27

Let H=C_{E6/Z3}(u), u=omega_1^vee, in R19's simple-coroot coordinates,
with long-root squared length two. Write lambda=v+c*u, v perpendicular
to u. Since u^2=4/3, c=3*lambda_0/4. The H cocharacter lattice is
C^-1 Z^6. Its primitive D5-singlet character is

    t=4c=3*lambda_0=(4,3,5,6,4,2) z,  lambda=C^-1 z.

The row has gcd one. The five D5-coroot columns C[:,1:] have maximal
minors (-2,4,-6,5,-3,4), also gcd one. They are the full kernel
lattice, not a finite-index sublattice. Thus ker(t)=Spin(10) is
connected and simply connected. A D5-singlet charge must lie in
4 Z. The apparent scalar Z4 after a charge-four VEV is already the
Spin(10) center, not an extra independent discrete gauge factor.

There is an explicit root-datum map to the simply connected parent's
standard centralizer H_sc. Swap the two short D5 arms on v and send
c*u to 3*c*u. In the simple-coroot basis it is

    F = [[3,0,0,0,0,0],
         [1,0,1,0,0,0],
         [3,1,0,0,0,0],
         [3,0,0,1,0,0],
         [2,0,0,0,1,0],
         [1,0,0,0,0,1]].

F*C^-1 is integral with determinant -1 and integral inverse. F
preserves the D5 root/coroot system and its metric, and F*u=3*u.
It integrates to an isomorphism H -> H_sc, followed by H_sc -> E6_sc.
This does NOT extend the entire quotient parent to E6_sc. The two
abstractly isomorphic centralizers have different parent embeddings.

Pulling back the actual fundamental-27 weight functionals yields

    16_(+1) + 10_(-2) + 1_(+4).

All pulled-back weights have integral E6 root coordinates. The
charge-one set equals R19's positive adjoint root set, weight by
weight. The arm swap is essential: omitting it fails both the lattice
and spinor-set tests. Merely tripling the old charge labels would
have silently changed D5 chirality.

This is a genuine representation of H, NOT a fundamental 27 of
E6/Z3. R20/B960's parent restriction stands. The scalar 1_(+4) has
integral weight 3*u; for example it occurs as the cube of the old
highest 27 weight in center-trivial Sym^3(27). This is an allowed
parent-representation possibility, not a derived field or a claim
that no other components of that parent representation are present.

## 2. Explicit anomaly-free field content and masses

Under the conditional four-dimensional fermion interpretation of
R19's kernel, add three vectors V in 10_(-2) and three singlets N
in 1_(+4). These are **33 new left-Weyl components**, not zero modes
already counted in the original adjoint complex.

| Three copies of | Tr u | Tr u^3 | Spin(10)^2-u, T(10)=1 |
|---|---:|---:|---:|
| Original 16_(+1) | 48 | 48 | 6 |
| Added 10_(-2) | -60 | -240 | -6 |
| Added 1_(+4) | 12 | 192 | 0 |
| Total | 0 | 0 | 0 |

The full six-variable linear/cubic anomaly polynomial vanishes,
not just these specializations. The full representation is the
pullback of three E6_sc 27s. Its global anomaly also vanishes: the
simply connected result Omega_5^Spin(BE6_sc)=0 applies before
pullback; naturality supplies an anomaly trivialization on induced
H bundles. This uses the primary bordism result, not the shortcut
that pi4 alone settles all anomalies. Ordinary spin spacetime is
assumed; combined spin-gauge quotients are not classified here.
[Garcia-Etxebarria--Montero, sections 3.6.3 and 3.7](https://arxiv.org/pdf/1808.00009).

Introduce a complex Phi in 1_(+4), with Phi=(f+rho)e^(i theta)/sqrt(2),
positive covariant kinetic term and potential
lambda*(|Phi|^2-f^2/2)^2. Allowed interactions include

    -1/2 sum_a [ yV_a Phi V_a.V_a
                 + (yN_a/M) Phi.conjugate()^2 N_a.N_a ] + h.c.

Each paired vector weight sum is canceled by Phi; the singlet mass
likewise cancels the full character. Nonzero diagonal input couplings
give the added fermions masses

    mV_a=|yV_a| f/sqrt(2),  mN_a=|yN_a| f^2/(2M).

They can be heavy while the original complex 16s stay chiral under
Spin(10). Directly, no two original D5 spinor weights are opposites,
so these singlet VEVs do not allow a same-chirality spinor mass.
The radial mass squared is 2*lambda*f^2. With gauge kinetic
F_u^2/(4g^2), the extra vector has m_A=4*g*f. The surviving
continuous group is **Spin(10), rank five**, not already the SM.

The separate action control derives these masses from Cartesian
|D Phi|^2 and the potential/monomials, verifies finite local gauge
covariance including d epsilon, and rejects missing-connection and
wrong-conjugation mutants. See [its output](anomaly_action_control_first_run.json).

The N operator has dimension five. This is an EFT with input cutoff
M, not a UV completion. f, couplings, potential, additional fields,
four-dimensional spacetime and a matching/scale regime are inputs.
H multiplets do not automatically define full-parent bulk fields on
the internal geometry; a defect realization or a full-parent lift
with its extra components still has to be supplied. The earlier
R4--R10 two-fundamental-27 action is not silently transplanted here.

## 3. Quantized local anomaly matching, not a family selector

For Hermitian curvature eigenvalues divided by 2*pi, use
I6=sum(ell^3)/6-p1(T)*sum(ell)/24. Actual spinor weights give

    I6(3*16_(+1)) = t X4,
    X4 = 3 Q - lambda_T,
    Q = (lambda^t C lambda)/2,  lambda_T=p1(T)/2.

An independent orthonormal D5 spinor-sign enumeration verifies the
same trace identity. For n copies, I6=(n/3)t X4.

The coefficient is an integral characteristic class on H bundles over
ordinary spin spacetime. This is proved by F, not merely by a flux
grid. Write Q'=F^*Q_sc, where Q_sc is the normalized integral basic
class of simply connected E6. The exact identity is

    3 Q = 3 Q' - t^2.

Thus X4=3 Q'-t^2-lambda_T is integral. Independently the coefficient
denominators of z^t C^-1*z/2 give minimum integral level three. On
spin S2 x S2, equal fundamental-coweight fluxes on both factors give
integral(Q)=4/3; levels one and two fail. This torus control is not
a classification of quotient-parent torsion classes.

In a descent scheme preserving D5 and local Lorentz invariance,
I5=(4*A_u/(2*pi))*X4. The local term -i integral(theta X4), with
delta theta=4*epsilon, cancels the light-fermion variation and passes
the 2*pi-period test. The action control checks the full variation
against the independently generated light anomaly polynomial and
rejects a charge-three shift. The full heavy-fermion determinant
supplies the low-energy matching functional; a covariant ABJ trace
is not interchangeable with the consistent pure-U1 gauge anomaly.

Global-form-dependent periodicity is standard prior art.
[Choi--Forslund--Lam--Shao, section 2.2 and Appendix B](https://arxiv.org/pdf/2309.03937).
The simple counterterm criterion does **not** force three generations:
a charged field of nonzero modulus is a section and restricts the
bundles to a Spin(10) reduction. A fractional-flux H bundle may not
admit that section. Indeed the explicitly completed H matter is
anomaly-free for one, two, three and nine copies, and the linear
identity proves this for every integer multiplicity. Extra topological
fields can also modify the fractional-coupling description. The three
in this construction still enters through three prescribed sources.

## 4. The cost of keeping the internal holonomy unchanged

At either R20 nontrivial character, charge q sees chi^q. Since an
H singlet requires q in 4 Z and chi has order three,

    allowed parallel singlet charges = 4 Z intersect 3 Z = 12 Z.

For Phi of charge four, H0(Q;L_chi^4)=0. This is checked by the
actual two-generator flat differential: a parallel section must be
fixed by both holonomies. It does NOT exclude nonparallel or
localized Higgs profiles, including profiles supported away from cusps.

A charge-twelve VEV retains ker(t^3). Its component group is Z3,
split by exp(2*pi*i*u/3); t on this element is 4/3 modulo integers,
so the subgroup intersects Spin(10) trivially. It commutes with
Spin(10), giving Spin(10) x Z3. The action control verifies its
order and phase on every spinor weight. This is a **gauge subgroup**,
not the order-three source **isometry**; they are not identified.

The original three spinors carry 48 charge-one Weyl components
under this Z3. The exact spin lens-space sum gives

    eta(L^3(3), charge 1)=1/9,
    eta(three spinors)=48/9=1/3 modulo one.

The inverse holonomy gives 2/3. Independently, net Z3 charge is
48=3 mod 9, failing the discrete consistency condition. Neutral
and conjugate-pair controls pass; nine spinors and each completed
27-shaped H copy pass. These are computed eta and charge tests,
not an anomaly inferred from matching dimensions.
[Garcia-Etxebarria--Montero, equations (4.4) and (4.10)](https://arxiv.org/pdf/1808.00009).

The charge-twelve scalar cannot give the proposed spectator mass
monomials: the required signed powers are 1/3 and -2/3, not integers.
Every parallel-singlet VEV preserves this holonomy Z3. Leaving only
the three spinors therefore needs an additional anomaly-carrying,
topological or inflow sector. This closes that restricted
parallel-Higgs-only shortcut, not the sourced theory.

## 5. What must now come from the source

The completed sub-duty is:

> The actual quotient-parent subgroup admits an anomaly-free
> added-field completion of the three-spinor sector, while an
> unchanged-holonomy parallel-singlet Higgs alone cannot leave
> just those spinors with a consistent residual gauge theory.

The positive result prevents a blanket anomaly kill. The holonomy
test prevents treating a written Higgs/axion term as a completed
geometric construction. PB-BOUNDARY stays OPEN.

Next construct a finite-energy, normalizable nonparallel charged
Higgs or a defect/inflow sector in the SAME sourced model. Compute
its internal profile, kinetic norm, gauge transformations, period,
coefficients and matching, and then recheck the charged operator
with its backreaction. Also determine how the added matter arises;
an H representation by itself is not a supply of internal modes.

Noncentral simply connected transport remains an alternative not
excluded by R20. Retain source/global-form/orbit selection,
Spin(10)-to-SM breaking and interactions, the neutral low-energy
cusp channel and common dynamical gravity. Mixed gauge-gravity
anomaly cancellation is not a graviton construction. Actual internal
forms and the possibly KK-scale mass must still be paid for, as in
[Pantev--Wijnholt section 3.4](https://arxiv.org/pdf/0905.1968).

## 6. Evidence, preserved failures and banking boundary

Original native run: exit zero, SymPy 1.14.0, 1.092 s after startup.
Its complete first JSON and the original focused receipt survived:
12 new tests plus unchanged R18/R19/R20 controls, 46 passed and
one optional-GUI warning in 19.19 s. The action-control first native
run also succeeds; 17 original/control tests pass in 3.84 s.
Both sources and test files remain unchanged from their seals.

First broad run: 39 files, 262 pass / 13 fail / 8 error, 230.58 s.
Its full stdout was observed but not saved before a continuation
reset discarded the in-memory capture. Its missing process handle
was verified, not treated as still running. The preserved
[first summary](ANOMALY_COMPLETION_REGRESSION_FIRST_SUMMARY.txt)
is explicitly reconstructed, not labeled byte-faithful stdout.

The separately expanded **40-file run** has a complete saved
[receipt](ANOMALY_COMPLETION_REGRESSION.txt): **267 pass / 13 fail /
8 error**, one warning, **248.60 s**, exit one. The failed/error
set exactly equals R20's 21 entries: zero added, zero missing.
Original assertions and failures are not deleted to make it green.
Only environment prefixes are redacted in public captures; the
expanded raw capture is retained in an explicitly excluded local file.
This is not complete-repository pytest or an independent proof review.

No source branch is merged; no B ID, PR, main banking or external
relay is claimed. CC's new numbering relay and main B1302 were read
at main 31dd52b9. The old GS discussion was recovered from older
audit B796 before describing this mechanism. Whole-repository
governance and independent-review debts remain; the full physical
theory goal is not achieved. Reporting gates return **27 pass / 3 fail**,
review due at 122 merges. The attribution, static-vacuity and older
literal-provenance debts are unchanged; no baseline is waived.
Receipt: [ANOMALY_COMPLETION_GATES.txt](ANOMALY_COMPLETION_GATES.txt).
