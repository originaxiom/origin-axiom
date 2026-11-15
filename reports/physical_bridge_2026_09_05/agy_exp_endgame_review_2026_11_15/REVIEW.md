# Independent X-ENDGAME review

2026-11-15. The reviewed head is
`b05424e99c85791ba3d37614b9b80a8b69af364b`, on
`agy/self-consistent-loop-2026-11-11`. There are twenty new campaign
commits after the previous review at `d6f77f7ff`.

The source card was sealed at `b192a3a01`, the independent checker at
`95829e787`, and its first output at `5a6f5b85e`. The six check groups
completed in isolated CPython 3.12.1 with mpmath 1.3.0, using exact
integers and 80-digit arithmetic. The checker imports none of the
reviewed branch's source. The original result is in `run01/result.json`.

This is preliminary verification under the renewed session request.
Main's independent review and banking remain owed. The earlier physical
packets retain their existing execution decisions. Parameter comparisons
performed here number zero.

## What changed and what held

The new campaign correctly uses monodromy order four modulo three.
The independently reconstructed results are

| Calculation | Result of this check |
|---|---|
| Orders of M and J modulo three | 4 and 8 |
| Nonzero three-torsion orbits under M | Two orbits of length four |
| Fourth-cover fixed characters | 45, split as 1+4+8+32 by exact order |
| O32 orbit counts under the five stated groups | (8,4,4,2,16) |
| Supplied level-three Weil commutator | Order-four identities, determinant and traces recomputed at 80 digits |
| Supplied Majorana jet matrix | Same covariance and cusp rank under independent sums |
| Regular tetrahedron shape, complete cusp derivative and volume | Same values |
| Hessian of negative volume on the stated gluing curve | Diagonal entries sqrt(3) |
| Classical area and normalized flat-interval collar identity | Same formulas under their supplied premises |

The new noncommuting running benchmark addresses the earlier coverage
question. Its reference expression inherits an ordered-product error.
The numerical checks below isolate it directly.

## 1. The global flux argument uses a closed fibre in the punctured model

The first result note, line 15, claims

> $H^2(M_3; \mathbb{Z}) \xrightarrow{\sim} H^2(E; \mathbb{Z}) \cong \mathbb{Z}$

Its card explicitly defines `M3` as the mapping torus of `E^times`.
That is the punctured-torus model. The fibre retracts onto two circles,
so its cellular chain groups have `C1=Z^2` and `C2=0`. The mapping
torus has

\[
 C_2=\mathbb Z^2,\quad C_1=\mathbb Z^3,\quad
 \partial_2=\begin{pmatrix}1&1\\1&0\\0&0\end{pmatrix},
 \qquad\det(M-I)=-1.
\]

Consequently `H2(M3;Z)=0` and `H1(M3;Z)=Z`. Universal coefficients
then give `H^2(M3;Z)=0`. The independent checker constructs the boundary
matrix and computes its rational rank. Its closed-fibre recovery control
adds the invariant two-cell and gives `H^2=Z`.

The statement in the result note applies to a closed-torus mapping
torus. Passing to that object changes the carrier. On the actual
punctured fibre, the integral compact-fibre Chern number requires a
specified extension across the puncture or relative boundary data.

There is also a direct obstruction if the magnetic torus is interpreted
as the single boundary horotorus. For a smooth source-free global
curvature `F`, Stokes' theorem gives

\[
 \int_{\partial\overline M}F=\int_{\overline M}dF=0.
\]

A nonzero boundary Chern number therefore needs an additional source
or changed extension problem. Both possibilities can be investigated
with their actual fields and boundary laws.

The four-fold cover retains an exact positive result. Its matrix is

\[
 M^4-I=\begin{pmatrix}33&21\\21&12\end{pmatrix}.
\]

Its entries have gcd three and its determinant has magnitude 45.
Thus its Smith invariants are `(3,15)`. For the punctured mapping torus
of `M^4`, `H1=Z direct-sum Z/3 direct-sum Z/15` and
`H^2=Z/3 direct-sum Z/15`. These torsion bundle classes are compatible
with the finite character calculation. They supply neither a free
integer Chern class nor the asserted compact-fibre degree-three
extension.

The computation in `verify_x_endgame_1.py`, lines 99–122, tests the
two-by-two determinant and labels `det(M)` as the action on the closed
fibre's area class. It never distinguishes the two cellular complexes.
Its green flag therefore misses this carrier change.

The punctured-torus description is also stated explicitly in the
primary mathematical account used for this review.
[Bridson–Reid, section 1](https://web.ma.utexas.edu/users/areid/BRf8_may19.pdf)

## 2. Mixed Yukawa products are reversed in the running code

The fifth result note, line 16, claims a published noncommuting
two-loop check with

> coefficients 13/2, 7, 5/4, -16, 9/16, -79/80, -43/80

The left-acting source defines `Hu=Yu Yu^dagger` and
`Hd=Yd Yd^dagger`. Its up-sector mixed term is

\[
 (-H_uH_d-\tfrac14H_dH_u)Y_u,
\]

and its down-sector term exchanges `u` and `d`. This appears in the
float implementation at lines 178–205 and in the high-precision
implementation at lines 1265–1280.

Luo–Xiao use `beta_H=H A` in their right-acting convention. Their
equations 1, 6 and 7 fix the conversion to the campaign's convention
as `Yu=H^dagger`. Taking the adjoint gives `beta_Yu=A^dagger Yu`.
The mixed term must therefore be

\[
 (-\tfrac14H_uH_d-H_dH_u)Y_u.
\]

This conversion follows the Yukawa interaction and the paper's explicit
instruction about multiplication order. The same adjoint reversal
applies in the down sector. The scalar-potential convention changes
coefficients involving the quartic coupling and leaves this reversal
of mixed products intact.
[Luo–Xiao, equations 1, 6 and 7](https://arxiv.org/html/hep-ph/0207271)

A second primary calculation provides the direct left-acting check.
Bednyakov–Pikelner–Velizhanin define the same `Y Y^dagger` products
and write mixed coefficients `-1/2` for `Ydu` and `-1/8` for `Yud`
in their equation 27. Their derivative is with respect to `ln(mu^2)`.
Multiplying by two gives the coefficients above. Their footnote 7
explicitly identifies their Yukawas with Luo–Xiao's adjoints.
[Second primary calculation, equation 27 and footnote 7](https://arxiv.org/html/1406.7171v3)

The corrections in the campaign's notation are exactly

\[
 \delta\beta_{Y_u}^{(2)}=\tfrac34[H_u,H_d]Y_u,\qquad
 \delta\beta_{Y_d}^{(2)}=-\tfrac34[H_u,H_d]Y_d.
\]

The independent checker constructs a noncommuting complex rational
example and compares the published right-action with its adjoint.
Both identities have residual below `10^-70`. The resulting change
of a mixed invariant is

\[
 \delta\frac d{dt}\operatorname{Tr}(H_uH_d)
       =\tfrac32\operatorname{Tr}([H_u,H_d]^2).
\]

For the example, the value before the common two-loop factor is
exactly `-0.01769472`. Thus a common constant unitary change of basis
cannot account for the difference. Diagonal inputs hide it, as the
checker also verifies. A different renormalization scheme would need
its own explicit transformation and observable matching.

A second independent calculation uses the two-generation rank-one
mixing problem underlying the campaign's benchmark. Direct
eigenvector differentiation of the correctly converted equations
gives the coefficient `11/2` on `yt^2 yb^2`. The campaign's ordering
gives `7`. The other listed terms agree in this restricted comparison.
At its test inputs, the pure two-loop logarithmic mixing derivatives
differ by approximately `1.1435255641e-5`, including the loop factor.
Both closed-form identities are satisfied below `10^-65`.

The planted up-sector commutator with coefficient `3/4` is the
up-sector part of this required correction. Its failure against the
campaign's own expression cannot establish that the expression is
the published result.

The source citation also needs repair. Physical Review D 47, 1093 is
the grand-unification paper, whose equation 24 defines an integral.
The CKM paper is Physical Review D 47, 2038. Its equations 10 and
17–26 state the matrix and mixing conventions. The later Luo–Xiao
correction is relevant when constructing the modern SM equations.
[Grand-unification paper, equation 24](https://arxiv.org/html/hep-ph/9209232v1),
[CKM paper](https://arxiv.org/html/hep-ph/9210260v2)

The full running trajectories require recomputation after fixing both
matrix products and the independent reference check. This finding
establishes the local differential error. Its effect on every final
observable has not been computed in this review.

## 3. Covariance admits continuous relative Majorana coefficients

The third stage constructs

\[
 M_R=A_v+A_w+A_u,
\]

with `Av=y^3 conjugate(E6) v v^T`,
`Aw=y^2 conjugate(E4) w w^T` and `Au=u u^T`.
The source is `verify_x_endgame_3.py`, lines 203–244.
Each summand has the same modular tensor law, including the unit
scalar phase under `S`. Therefore

\[
 M_R(c_v,c_w,c_u)=c_vA_v+c_wA_w+c_uA_u
\]

retains that covariance for constant coefficients. Symmetry is also
preserved. Relative coefficients require a selection law.

The independent implementation uses divisor-sum Eisenstein series
and direct theta sums. It reconstructs the supplied cusp ratio
`sigma1/sigma3=0.000000247842874...` and the rank-two failure when
the last jet is dropped. Those positive results survive.

At the campaign's generic bulk modulus, the supplied coefficients
`(1,1,1)` give normalized singular values approximately
`(0.00122553,0.27442507)`. Changing only the second coefficient to
two gives `(0.00122837,0.54758013)`. All four tested coefficient
choices preserve the same `T` and `S` covariance below `10^-60`.
The largest ratio shift exceeds one quarter.

This is a continuous family with changed unitary invariants while
retaining the tested symmetry. An action or canonical jet pairing
could select a member. That derivation is owed before the unit
coefficients count as forced inputs. The existence and full rank
of the supplied member remain established within this check.

## 4. The classical area and collar remain consequences of a supplied action

The second source explicitly uses

\[
 S(A,z)=-\operatorname{Vol}(z)+cA+
       \frac{2\pi^2 I^2}{A}+\frac{V_{\rm flat}(\tau(z),w)}{16\pi^2A^2},
       \qquad c=\tfrac12.
\]

The independent calculation confirms the regular geometric root,
the complete cusp derivative and the reported volume Hessian.
For the classical area terms, differentiation gives

\[
 A_* =\sqrt{\frac{2\pi^2 I^2}{c}}.
\]

At `I=3,c=1/2` this is `6 pi`. Changing `c` to `1/4` or one gives
`6 sqrt(2) pi` or `3 sqrt(2) pi`, respectively. These values were
computed independently and satisfy the stationary equation. The
physical common action must fix the relative gravitational, Maxwell
and source coefficients before its stationary area is a foundational
input reduction.

The flat Epstein fermion determinant from X-FUNNEL remains in the
new potential. The new report also deletes it as a robustness control.
That control preserves a conditional classical minimum. The vacuum
action of the magnetic fermions still requires their magnetic operator
and domains.

The collar source takes `psi(t)=exp(kappa t)` on a flat interval with
`L=Im(tau_cusp)`. Its normalization identity is correct,

\[
 \frac{\psi_+(L)/\|\psi_+\|}{\psi_-(L)/\|\psi_-\|}=e^L.
\]

The checker confirms it by independent quadrature. A torus aspect
ratio and a radial collar depth require a geometric identification.
In a hyperbolic cusp, `ds^2=dt^2+exp(-2t)g_T`, the proper radial
coordinate, the cross-section area and its conformal shape are distinct
data. The source has yet to derive its choice of interval, measure,
radial equation and evaluation point from that geometry and action.

## 5. The closing condition and zero-knob builder select additional data

The first result note, line 19, begins

> Requiring all three chiral Landau generations to close periodically around the base

The computed order four establishes the least cover that trivializes
the supplied monodromy. Ordinary bundle gluing already permits a
nontrivial monodromy. On a base circle, sections obey a twisted
periodicity condition. Requiring every generation to be parallel and
periodic imposes an additional condition on that spectrum. Deriving
that condition is part of the family-selection task.

There is also a free base character in the flat connection problem.
For the mapping-torus presentation, assigning `t -> exp(i theta)`
leaves every fibre relation unchanged. It is the free `Z` summand
of `H1`. A connection or matter action could select that holonomy.
The two-by-two determinant calculation supplies its topological
classification, without fixing the connection.

The fifth source's `build_zero_knob_uv_state_mp`, lines 1105–1148,
sets the gauge normalization to `alpha^-1=Vol*A`, the quartic to
`g^2/5`, the running interval to `-45 Vol/pi`, the collar length to
`Im(tau)`, the singlet mass to the unit-coefficient jet matrix and
the representation to magnetic degree three. These choices define
a numerical recipe. Source inspections for floating-point literals
and repository imports cannot establish the uniqueness of that
recipe from the foundational principles.

The record's phrase zero continuous fitted parameters can describe
a recipe whose constants were fixed without a fit. Verified removal
of independent physical inputs additionally requires their selection
derivations. The coefficient family in section 3 demonstrates an
explicit remaining freedom under the advertised covariance premises.

## 6. A raw determinant phase does not prove the claimed necessity

The third result note, line 25, concludes that cancellation

> requires vector-like parity completion

For the displayed direct sum, conjugate determinants do multiply to
a nonnegative real number. That algebraic cancellation is sufficient
within the supplied construction.

Under the same chiral basis transformations admitted by the Haar
checks, with common left basis held fixed,

\[
 Y_u\mapsto Y_uU_u^\dagger,\quad
 Y_d\mapsto Y_dU_d^\dagger,
\]

the raw phase shifts by
`-arg(det Uu)-arg(det Ud)`. Thus `arg det(Yu Yd)` alone is not a
basis-invariant physical obstruction. A physical strong-CP conclusion
requires transporting the gauge theta term and its anomalous chiral
transformation. This calculation supplies a parity-doubled example,
without establishing necessity over the other admitted theories.

## 7. The gravity identities retain their supplied four-dimensional fields

The fourth source explicitly supplies random nondegenerate tetrads,
four-dimensional Lorentz connections, a simplicity construction and
a rational Immirzi coupling. It then compares the self-dual and
Palatini–Holst densities. Those algebraic identities are compatible
with the standard construction. This review did not independently
rerun that source's gravity or torsion calculations.

The spin-group identification and algebraic density identity require
a further map from the registering architecture to the tetrad,
connection, action normalization, source equations and physical
operator domains. The reported calculation provides a conditional
gravitational framework. Derivation of those fields and dynamics
remains a duty before SM3 plus gravity is complete.

## Coverage, first failures and next corrections

The upstream stage-one strict gap criterion remains false and is
disclosed in its report. Stages two through five have true aggregate
flags in their saved outputs. All ten upstream script/output pins
match the source bytes. The independent checker finished all six
groups with exit status zero and empty output/error streams. Its
counterexamples are recorded as mathematical findings.

The first runtime metadata query selected system Python 3.9 and could
not find mpmath under isolated startup. No scientific code ran there.
The declared 3.12.1 runtime completed the first scientific run. During
card preparation, the general classical-area formula had an incorrect
factor in an uncommitted draft. It was corrected by differentiation
before the card and checker seals, as the card records.

Before using the campaign's final vector, the consequential repairs
are the carrier/flux extension and both ordered Yukawa products.
The reference benchmark must be corrected at the same time. Then
the remaining relative Majorana coefficients, action coefficients,
collar law, base holonomy, selected cover and ultraviolet matching
laws need derivation or explicit input accounting.

This review independently checks the listed arithmetic and selected
local formulas. Complete overlap quadratures, the full two-loop and
threshold evolution, quantum torsion normalization, instanton matching,
the full kernel and a stationary interacting gravitational model remain
outside this completed verification scope.
