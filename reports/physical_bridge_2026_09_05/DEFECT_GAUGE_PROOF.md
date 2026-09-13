# R29 pre-execution argument: a finite source and its gauge thin limit

This argument concerns the ADDED bosonic H theory specified in
[the design](DEFECT_GAUGE_DESIGN.md), not a derived full-parent
supersymmetric theory or an accepted chiral completion. H and its
charge-four character are the actual subgroup of [R21](ANOMALY_COMPLETION.md).
The metric, tube domains, kinetic coefficients and potentials are inputs.
Statements below are proof candidates until their controls are reported;
finite tests alone are not independent verification of the analytic proof.

## 1. Fields, action, variations and a regulated stationary solution

Let M_S be a smooth compact connected truncation with nonempty boundary,
with disjoint
contractible tubes U_a and a flat H connection whose holonomy is in the
central U1. Its charge-q_a line bundle restricted to U_a is trivial.
Take q_a=4 (or its opposite when explicitly changing the source sign).
A complex field Q_a is defined on U_a, NOT continued by zero as a
whole-manifold smooth field. Give it natural covariant Neumann boundary
conditions. sigma_a is a prescribed positive bounded weight on U_a;
it may be constant up to its boundary. Use its indicator in bulk integrals.

Let h be a real internal one-form in the central direction, with
algebra norm absorbed into C>0. Set

    D = div h - kappa sum_a q_a sigma_a |Q_a|^2 1_(U_a),

    V = C integral_M (|dh|^2 + D^2)
        + (1/(2 g7^2)) integral_M |F_A|^2
        + sum_a integral_Ua sigma_a
            (|D_i Q_a|^2 + lambda_a (|Q_a|^2-v_a^2/2)^2).

Here D_i Q=(partial_i-i q A_i)Q, d is the exterior derivative,
div h=+nabla^i h_i, and form norms include 1/p!. Four-dimensional
spacetime is assumed Minkowski. Add the usual positive-energy gauge
kinetic term -F_(mu nu)^2/(4g7^2), the mixed F_(mu i) term with the
same coefficient, positive h kinetic energy and sigma_a |D_mu Q_a|^2.
All parameters are in curvature-length units; no measured scale is fixed.

The action is H-gauge invariant: h and |Q|^2 are invariant, F has
invariant norm, and DQ transforms as Q. No supersymmetry or full E6
lift is asserted. In particular a possible full-parent |h Q|^2 term
is NOT present in this declared action. Adding it changes the equations
and can destroy the exhibited solution. The supplied localization of
Q is another physical input, not a derived soliton.

The complete weak first variations of the static potential are

    delta_h V = 2C integral [<dh,d xi> + D div xi],

    delta_Q V = 2 Re integral_U sigma [
         <DQ,D eta> + (2 lambda (|Q|^2-v^2/2)-2C kappa q D) Q* eta],

    delta_A V = (1/g7^2) integral <F,d_A alpha>
                 - sum integral_U 2 sigma q Im(Q* D_i Q) alpha^i.

D5 contributes its usual curvature variation and no Q current.
These expressions include the dependence of the source density on Q:
it is not held fixed during variation. Natural tube/end conditions
kill the integrated derivative boundary terms; at zero residual they
vanish before integration by parts. A prescribed scalar source alone
would miss the Q equation and current.

In a parallel trivialization on each contractible U_a choose
Q_a=v_a/sqrt(2), and keep A flat. Solve the Dirichlet Poisson problem

    Delta F = rho = kappa sum q_a sigma_a v_a^2/2 1_(U_a),
    F|_(boundary M_S) = any specified smooth function,  h=dF.

For bounded piecewise density the standard weak Dirichlet construction
gives h in L2 with dh=0 and div h=rho; on a smooth compact boundary
the usual H2 regularity of F also applies. This follows from the
coercive Dirichlet Laplacian, not a claim to have numerically computed
the actual global F on the originating manifold. The h boundary
values in the construction are selected inputs; the zero residuals
also satisfy the natural conditions of the displayed h functional.

Now dh=D=F_A=DQ=|Q|^2-v^2/2=0. Every coupled first variation vanishes.
V=0 is a global minimum of this nonnegative STATIC functional on its
declared admissible fields. Its Hessian is a sum of squares, with
possible flat directions; no unique vacuum or all-order quantum
stability follows. No constraint forces three tubes or their strengths.

This does not violate R22's whole-manifold parallel-section obstruction.
No Q field here is required to parallel-transport around a nontrivial
loop outside U_a. A nonzero zero-extension would instead be discontinuous
at its boundary and is not this model.

## 2. Exact hyperbolic core and its exterior residue

On an embedded geodesic segment of proper length L, use

    ds^2=dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dz^2,
    w=sinh(r) cosh(r), theta period 2*pi.

For the uniform cross-section weight sigma=1/(pi sinh(epsilon)^2)
one has integral_transverse sigma dvol per unit axis length = 1.
A constant Q=v/sqrt(2) supplies

    rho=kappa q v^2/(2*pi*sinh(epsilon)^2),
    beta=kappa q v^2/(4*pi),

    h_r = beta tanh(r)/sinh(epsilon)^2,       r<epsilon,
          beta/(sinh(r)cosh(r)),             r>epsilon.

The radial field is smooth at the axis, continuous at the join,
piecewise smooth, and has no divergence delta at the join.
Its divergence is rho inside and zero outside; total side flux is
2*pi*L*beta=kappa*q*v^2*L/2. Axial cap flux is zero in this example.
Removing the Q-induced shift restores R28's nonzero bare core cost.

Each finite core supplies the logarithmic exterior residue through
an actual varied field in the added model. The limiting source strength
is still an input through kappa and v, not selected. Promoting v also
changes beta; R28's kinetic logarithm then returns as epsilon->0.
The source action's zero static value does not make that modulus finite.

The source-field contribution itself has collective-amplitude kinetic
weight integral_U sigma = L on this uniform tube. If that normalization
is continued along an infinite proper axis, the weight diverges with
its length. Thus the compact construction is not a finite-norm end-sector
construction on the complete space. A fixed nonnormalizable background
is not thereby forbidden, but its amplitude is not an ordinary 4D field.
Tail profiles, overlap/injectivity at the cusp and the actual end action
must be solved before taking this regulated source theory to M itself.

## 3. The actual transverse vector operator

Consider A_mu(x,y)=a_mu(x) f(y) in the central direction, with transverse
four-momentum k^mu a_mu=0. The Q phase couples through
sigma*v^2/2 (partial_mu theta-q A_mu)^2. Its gradient mixes only
longitudinally; A_i's mixed kinetic cross term does too. Since h
commutes with this U1, h supplies no additional central vector mass.

The remaining quadratic form, after canonical gauge normalization, is

    H_epsilon = -Delta_M + V_epsilon,
    V_epsilon = g7^2 sum_a q_a^2 v_a^2 sigma_a 1_(U_a).

It acts on the ordinary bulk L2 scalar profile f with H1 form domain
(and Neumann exterior boundary on M_S), not on a line-trace state space.
On a complete space with an unbounded potential, use instead the closed
form domain H1 intersect L2(V dvol); the constant profile need not belong
to it. No finite complete-space potential average is assumed below.
Internal gradients MUST be retained. The constant normalized profile
has Rayleigh value

    m00^2 = average_M V_epsilon.

For uniform tubes this average can stay finite as radius tends to zero.
It is only an upper bound on inf spec(H_epsilon), not the lowest mass.

At a fixed finite radius on a compact connected M_S, bounded V>=0,
not zero almost everywhere, gives lambda0>0. A useful explicit bound
uses the Neumann Poincare gap delta>0, mu=average V and K=ess sup V.
Write f=a/sqrt(Vol)+g with g perpendicular to constants and b=||g||.
For E=<f,Hf>,

    b^2 <= E/delta,
    mu |a|^2 <= 2 integral V |f|^2 + 2 K b^2,
    lambda0 >= mu*delta/(2*delta+mu+2*K) > 0.

This is a conditional analytic bound, not a computed gap for a particular
cusp geometry. With V=0, the constant zero mode returns. Uncharged D5
constant vectors remain massless in this restricted central-flat model.
No SM breaking or full low-energy particle spectrum is inferred.

## 4. Why bare positive mass localized on shrinking lines loses its gap

For epsilon<r<R on the exact tube define f_epsilon=0 inside epsilon,
1 outside R, and between them

    f_epsilon(r)=log(tanh(r)/tanh(epsilon))
                      /log(tanh(R)/tanh(epsilon)).

Let ell=log(tanh(R)/tanh(epsilon)). Direct integration gives

    integral_tube |df_epsilon|^2 = 2*pi*L/ell.

For fixed R, f_epsilon tends pointwise to 1 away from the axis and
tends to 1 in L2 on the finite tube. Its energy tends to zero. These
continuous piecewise smooth H1 profiles can be smoothed, retaining
zero on the mass support, with the same vanishing-energy bound.

For finitely many compact smooth arcs, local tube charts and finite
products of such cutoffs supply the same conclusion. Bounded metric
comparison controls curved segments and endpoints; each endpoint is
covered by an extended segment chart (or half-chart at an exterior
boundary). Constants may depend on the fixed truncation and arc geometry,
not on epsilon. This is a codimension-two H1 capacity argument.

Consequently, for ANY nonnegative locally integrable V_epsilon
supported in shrinking tubes around those arcs, however large its
height or integrated strength, the cutoff pays zero potential energy.
Its normalized Rayleigh quotient tends to zero. Thus on the fixed
compact bulk Hilbert space,

    inf spec(-Delta+V_epsilon) -> 0.

For a complete finite-volume hyperbolic M with finitely many proper
smooth source arcs, first truncate a cusp with eta_S=1 below S and
0 above S+1. In ds^2+exp(-2s)g_T choose a Lipschitz linear transition:

    integral |d eta_S|^2 = (A/2)(1-exp(-2))*exp(-2S),
    integral |1-eta_S|^2 <= (A/2) exp(-2S).

Only finitely many compact arc segments meet its support. Multiply
eta_S by their avoiding cutoffs. For fixed S, their gradient cost
vanishes as epsilon->0 and their L2 limit is eta_S. Then S->infinity
removes the cusp cost and ||eta_S||^2 tends to Vol(M)>0. The product
gradient inequality (or Cauchy--Schwarz on the cross term) suffices.
This ordered limit proves the same spectral-bottom conclusion on the
complete space, without importing a numerical Poincare gap or assuming
a compact resolvent. More cusps are a finite sum.

This is NOT a claim of spectral/resolvent convergence of all operators,
an isolated massless particle, an observed new photon, or a theorem
about changed metrics, nonabelian backgrounds or other kinetic domains.
The U1 here is extra, not electromagnetism. A finite physical radius,
a bulk condensate, or a renormalized/enlarged defect kinetic theory is
not excluded by this bare shrinking-support result.

## 5. The literal positive line-mass form is not closable on bulk L2

On a compact interior source segment take a nonzero smooth a(z)
supported away from its endpoints. Let R_n=exp(-n), epsilon_n=exp(-n^2),
and let u_n=a(z)(1-f_(epsilon_n,R_n)(r)). Then u_n has the fixed line
trace a, while

    ||u_n||_L2^2 = O(R_n^2),
    ||du_n||_L2^2 = O(1/(n^2-n)) + O(R_n^2).

The axial derivative term is included. Smooth approximants equal to
a(z) in a neighborhood of the axis have the same limits. For gamma>0,
consider on smooth compact fields

    q_line[u] = integral_M |du|^2 + gamma integral_line |u|^2 dz.

Now u_n->0 in bulk L2 and q_line[u_n-u_m]->0, since the traces cancel,
but q_line[u_n]->gamma integral |a|^2>0. This violates the definition
of closability. There is no positive Friedrichs form on bulk L2
obtained by merely adding this literal line-evaluation term.

This is stronger and more precise than saying a delta function is
undefined, but it is NOT a no-go for renormalized point interactions:
their domains/subtractions can differ, or line fields can carry their
own kinetic norm. It is also not a result about R18's charged,
weighted maximal fermion complex, a different Hilbert operator.

## 6. Independent finite-spectrum and codimension-one controls

On a flat two-torus, in a Fourier cutoff n in [-N,N]^2, use

    H_N=diag(|n|^2)+eta 1 1^T, eta>0.

This is a TOY rank-one point potential, not a hyperbolic discretization.
The ground root lies in (0,1), and the determinant lemma gives

    lambda_N*(eta^-1 + sum_(n!=0) 1/(|n|^2-lambda_N))=1,
    lambda_N <= 1/(eta^-1+S_N), S_N=sum_(n!=0) 1/|n|^2.

There are 8k points on square shell k and |n|^2<=2k^2 there, so
S_N>=4 sum_(k=1)^N 1/k -> infinity. The constant-only matrix element
is eta at every cutoff, yet the lowest eigenvalue tends to zero.
Direct real-symmetric diagonalization is separate from the secular
root calculation. eta=0 and a UNIFORM positive mass are opposite
controls. No extrapolated grid replaces the shell proof.

On a one-dimensional circle the nonzero-mode sum is finite:
2 sum 1/n^2 <= 4. For 0<eta<1 the analogous ground root has
lambda_N<=eta and

    lambda_N >= 1/(eta^-1+4/(1-eta)) > 0

uniformly in N. The H1 trace is continuous in one transverse dimension,
so its positive delta form is closed. This comparator prevents turning
the codimension-two conclusion into a universal localized-Higgs no-go.

## 7. Renormalized defect theories are an explicit escape, not a footnote

de Rham 0707.0884v3, equation (25), gives in its scalar brane model

    lambda_R = lambda_B/(1+lambda_B*L/(2*pi*alpha)),
    L=log(Lambda/mu).

For lambda_B>=0 and L>0 this is bounded by 2*pi*alpha/L.
Conversely a fixed positive lambda_R would require
lambda_B=lambda_R/(1-lambda_R*L/(2*pi*alpha)), with a pole and
a sign change as the cutoff is taken arbitrarily large.

This elementary algebra is a control on this positive-bare route,
NOT a universal renormalization obstruction or an identification of
the paper's scalar propagator with our gauge operator. The same paper
constructs a consistent brane EFT with appropriately renormalized
couplings and additional brane fields; that positive result is retained.
Only selected pages were read; see [intake](DEFECT_GAUGE_INTAKE_2026_09_13.md).
The capacity literature likewise motivates, but does not replace,
the explicit hyperbolic-cusp argument above.

## 8. Relation to the physical goal

Finite-width source fields solve one coupled classical existence
question in a declared added model. Their bare zero-width gauge mass
cannot be read from the constant profile alone on the stated Hilbert
space. Neither result cancels the original chiral anomaly.

Smoothing h~beta dr/r changes the singular fermion-domain problem:
it is not a bounded perturbation vanishing at all ends as in R26.
No R18/R19 three/zero count is transferred to the resolved operator
without deriving that operator and its actual domain. The source
activation, signs, number, width, full-parent lift, anomaly response,
neutral continuum and gravitational/empirical identifications remain
duties of a common theory, not newly established absences in the corpus.
