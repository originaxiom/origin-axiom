# F02 analytic argument: the action, the background and the domain

This argument is recorded before executing the accompanying algebraic
controls. It applies standard complete-manifold operator theory and reuses
existing R15/R28 constructions. It is not independently specialist-reviewed.

## 1. What the adopted action does and does not require

Braun--Cizel--Huebner--Schaefer-Nameki's twisted seven-dimensional gauge
theory supplies a positive Hermitian form norm and a twisted differential.
The BPS conditions are complex flatness and a moment-map equation. Their
fermion zero modes use the twisted differential and its Hermitian adjoint;
the parity of the form complex organizes four-dimensional chirality.
These are imported modeling inputs, not deductions from the knot.
[Primary source, equations (2.9), (2.13), (2.18), (2.36)--(2.44)](https://arxiv.org/html/1812.06072v2).

R28 already gives the commuting bulk potential in form-norm conventions:

    V = (2/g7^2) integral (|d phi|^2 + |delta phi|^2 + |d W|^2).

At zero residual its first variation vanishes for compactly supported
regular variations. This is not a demand that integral |phi|^2 be finite.
The kinetic coefficient of a parameter t is instead proportional to
integral |partial_t phi|^2. Boundary counterterms, gravity, backreaction,
supersymmetric end completions and UV validity are not settled by the bulk
formula. Here only this adopted fixed-metric bulk theory is being tested.

After fixing a smooth positive bundle metric, a smooth complex connection
decomposes into unitary A and a self-adjoint one-form Psi. On all bundle-valued
forms set D=d_A+Psi wedge, and Q=D+D^*, where the star here denotes formal
adjoint in ordinary L2. Thus

    Q = d_A+d_A^* + sum_i (epsilon_i+iota_i) Psi_i,
    c(v) = epsilon(v)-iota(v),   hat-c(v)=epsilon(v)+iota(v).

The last term is Hermitian even if the different Psi_i do not commute or
grow without bound at infinity. Q is formally symmetric and elliptic, with

    [Q,chi]=c(dchi),   c(v)^*c(v)=|v|^2 identity.

These properties do not require D^2=0. Flatness is needed for the cohomology
interpretation, not for the domain theorem. The standard 4D kinetic norm
is the L2 norm of the mode, not the L2 norm of the background Psi.
No counting of real/conjugate parent representations is changed here.

## 2. Complete-space domain theorem

Let M be smooth, connected, geodesically complete and without boundary;
let E have finite rank and a smooth positive Hermitian metric. A and Psi
are smooth as above. There is no finite-volume assumption and no global
bound or integrability assumption on Psi. Then Q on C_c^infinity is
essentially self-adjoint in L2(Omega^* M tensor E).

Proof. Use the maximal distributional domain

    Dom(Q_max) = {u in L2 : Q u, as a distribution, is in L2}.

Formal symmetry identifies Q_max with the Hilbert adjoint of Q_min on
C_c^infinity. Elliptic local regularity gives u in H1_loc for u in Dom(Q_max).
On a compact set, all coefficients are bounded and smooth. Mollification
in finitely many trivializations, with a partition of unity, approximates
compactly supported H1 sections by C_c^infinity in the Q graph norm.

Completeness supplies compactly supported Lipschitz cutoffs chi_R, between
zero and one, equal to one on the radius-R ball, zero beyond radius 2R,
with |dchi_R| <= C/R. Closed metric balls are compact. Lipschitz cutoffs
suffice since chi_R u is compactly supported H1 and can be smoothed by
the preceding local argument. The product rule gives

    Q(chi_R u)=chi_R Q_max u+c(dchi_R)u.

Consequently chi_R u -> u in L2 and

    ||Q_max u - Q(chi_R u)||2
      <= ||(1-chi_R)Q_max u||2 + (C/R)||u||2 -> 0.

Hence Dom(Q_max) is contained in the graph closure of the minimal domain.
The reverse containment is automatic. The closed minimal operator equals
its adjoint, proving essential self-adjointness. No term ||Psi u||2 was
separated from ||Q u||2, so no unjustified global potential bound entered.
For compact M one needs only the local graph approximation. QED.

This is the standard cutoff mechanism: compare Wolf, Theorem 5.1 and proof,
printed pp. 622--624, and Chernoff's general first-order result. Wolf's
displayed theorem is not being quoted as an arbitrary-potential statement;
the extension needed here follows from the unchanged scalar commutator
in the proof above. Wolf pp. 621--625 were visually read. Only Chernoff's
publisher abstract was read, so it is background attribution, not an
uninspected load-bearing theorem application.
[Wolf PDF](https://math.berkeley.edu/~jawolf/publications.pdf/paper_050.pdf),
[Chernoff, JFA 12 (1973), 401--414](https://doi.org/10.1016/0022-1236(73)90003-7).

The resulting domain can be stated exactly as Dom(Q_max) above. It is not
asserted to equal global H1 when the potential is unbounded. The self-adjoint
square has domain {u in Dom(Q_bar): Q_bar u in Dom(Q_bar)} and defines a
nonnegative mass-squared operator. This proof does not separately certify
essential self-adjointness of Q^2 restricted to C_c^infinity.

## 3. A global zero-potential, non-L2-background control already available

Specialize R15 to no source lines on a connected complete finite-volume
hyperbolic three-manifold with s>=2 cusps. At end i let the reference torus
area be A_i and use metric dr^2+exp(-2r)h_i. Choose real constants c_i,
not all zero, with sum_i A_i c_i=0. With cutoffs chi_i equal to one high
in their cusps set F0=sum_i c_i chi_i exp(2r). Its Laplacian r0 is smooth,
compactly supported and has integral 2 sum_i A_i c_i=0. On constants-perp
the nonnegative scalar Laplacian L=-Delta has a bounded inverse because
zero is an isolated scalar eigenvalue on this finite-volume hyperbolic
manifold. Let v=L_perp^-1 r0. Then

    F=F0+v,   Delta F=0,   phi=u dF,   W=0

is a smooth global commuting zero-residual bulk background for fixed Cartan
u. This repeats R15's homogeneous through-flux freedom, not a new global
nonsplit existence theorem. The scalar spectral input is inherited from
R15; no numerical gap or mesh solution is claimed.

The L2 harmonic corrector v has constant torus average high in each cusp:
its average solves v''-2v'=0 and its exp(2r) solution is not L2. Jensen's
inequality therefore gives, on any end with c_i nonzero,

    integral_[S,R] |dF|^2 >= 2 A_i c_i^2 (exp(2R)-exp(2S)).

The background is not L2 although its adopted static residual potential
is zero. Varying c_i has the same divergence with c_i replaced by delta c_i;
these are fixed asymptotic data, not ordinary finite-kinetic-norm moduli.
For one cusp the balance condition forces this homogeneous c to zero.
More general asymptotic classes are not classified by that observation.

On the smooth complete space the corresponding charged Q has the unique
closure of section 2. Thus an infinite background norm does not itself
invalidate the Hilbert-space operator. This does not show the background
survives backreaction or has normalizable charged zero modes. Since F is
single-valued, its flat complex connection is complex-gauge trivial; it is
NOT the nonsplit m010 representation and cannot validate that representation
by substitution. Nor is multiplication by exp(qF) a bounded unitary L2
equivalence: its growth can change reduced cohomology and spectra.

## 4. Countercontrols against false conclusions

**Unique closure does not force a zero graded index.** On the complete real
line, Q = [[0,-partial_x+x],[partial_x+x,0]] is of the same operator type.
Its even kernel is spanned by exp(-x^2/2); the odd formal solution exp(x^2/2)
is not L2. Squaring gives the two harmonic oscillators -partial_x^2+x^2-1
and -partial_x^2+x^2+1. Their paired positive eigenvalues are separated
from zero. The even-to-odd index is +1. This standard toy model has infinite
volume and F=x^2/2 is not harmonic; it is not a framework BPS solution or
physical generation. Its purpose is to refute the purported logical
implication from self-adjointness alone to vector-like zero modes.

**Unique closure does not imply Fredholmness.** The free Q=c*partial_x on
the real line has no L2 kernel, but the normalized even Gaussians
f_R=pi^(-1/4)R^(-1/2)exp(-x^2/(2R^2)) satisfy ||Q f_R||2^2=1/(2R^2).
Thus Q is not bounded below and cannot have closed range with zero kernel;
it is not Fredholm. The example supplies no assertion about the essential
spectrum of the actual charged hyperbolic operator.

**Completeness is load-bearing.** On the open half-line the free Q has
deficiency vectors u_plus=exp(-x)(1,i), u_minus=exp(-x)(1,-i), each of
norm one, satisfying Q u_plus=i u_plus and Q u_minus=-i u_minus. Therefore
the minimal operator is not essentially self-adjoint. Removing a finite-
distance source locus can invalidate the complete-space argument. R16's
singular-domain choices and R30's compact regulator are not refuted.

## 5. Physical conclusion and remaining experiment

For a fixed smooth complete background and the adopted L2 action, there is
no freely adjustable self-adjoint cusp extension. One must compute the
operator in that domain. For a singular/incomplete background, the source
completion must justify its domain instead. Neither case permits choosing
a domain solely to obtain a desired generation count.

This removes one ambiguity, not the physical goal. The nonsplit witness
still needs a global harmonic/background solution in a defensible end class,
the correct parent representation and normalizable spectrum. F01 excludes
one precisely defined class. F02 does not construct a solution outside it.
Fredholmness, zero-mode multiplicities, anomaly cancellation, interactions,
vacuum selection and gravitational completion remain separate duties.
