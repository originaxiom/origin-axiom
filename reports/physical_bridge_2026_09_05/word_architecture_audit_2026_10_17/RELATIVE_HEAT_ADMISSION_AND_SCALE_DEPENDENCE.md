# Relative heat admission and the scale dependence carried by light modes

October 27, 2026. UNREVIEWED author conditional analytic lemma and source
recovery. No scientific execution, new numerical solver or determinant
value. This closes a logical part of the relative-threshold construction,
not all analytic hypotheses for the actual physical operators.

## 1. Reuse the existing continuum result at its actual scope

Personally read weave_cusp_heat_2026_10_08/PROOF completely. It already
retains the continuum heat density, the spatial-cutoff commutator,
short-range Duhamel argument and distinction between a finite supertrace
and a divergent positive determinant modulus. The paired phase proof's
polar/finite-exhaustion construction was also reread through its phase
prescription: strong resolvent convergence is not trace-norm or
modulus convergence. Those results are not rediscovered or extended
from a graded chiral diagnostic to the parity-even gauge threshold.

The current Wilson problem instead compares SAME-species operators
P_q and P_0, with the flat character q versus0, on the same chosen
background. They agree on the end in the source's compact-core gauge.
Locally their flat gauge connections are gauge equivalent. Equal local
heat coefficients and equal end models are necessary evidence, but
neither ALONE is a trace-class theorem or a value of a determinant.

## 2. Exact sufficient hypotheses for a relative determinant

Require for each charge q:
A. P_q,P_0 are nonnegative selfadjoint Laplace-type operators with their
   actual admitted smooth complete domains, and the flat-character change
   introduces no defect or independently changed boundary condition.
B. exp(-s P_q)-exp(-s P_0) is trace class for each s>0. Its trace r_q(s)
   has r_q(s)=O(s^N) for every positive N as s->0, with the corresponding
   finite-order remainder control. This is global relative locality,
   stronger than just equality of formal pointwise coefficients.
C. r_q(s)=h_q+O(exp(-delta_q s)) at large s, with delta_q>0 and
   h_q=dim ker P_q-dim ker P_0. A positive essential threshold and a
   justified relative spectral estimate can supply this; an end gap
   alone does not specify the relative estimate or discrete modes.

These are sufficient conditions, not assertions that every physical
bosonic/ghost operator has passed them. For a finite charge roster the
bounds can be combined. A global gauge-insertion coefficient may involve
more operators/insertions than a bare scalar relative determinant; its
own trace estimates must be proved. The same warning applies to a
proper-time integral with an additional power of s from spacetime loops.

Personally read Muller, Relative determinants of elliptic operators and
scattering theory (1996), definitions2.1,2.2,2.4 and proposition2.3 with
the positive-essential-gap remark, through the basic properties2.5:
https://www.numdam.org/item/JEDP_1996____A13_0.pdf (October27).
His framework explicitly requires trace-class and small/large-time
control. The scalar Euclidean and product-cylinder examples are not
silently substituted for this coupled curved cusp/source domain.
Aldana1001.2033's abstract was located: it concerns conformal metric
changes under specific decay hypotheses, not automatically our charged
flat-bundle problem; no full-paper reading/application is claimed.

A possible route to B is to prove heat off-diagonal bounds for the
actual lifted operator and sum Wilson-sensitive nonperipheral loops.
The character is trivial on the peripheral commutator and its powers,
so those shrinking cusp loops cancel. Nonperipheral character-sensitive
loops have a positive length lower bound for a FIXED finite-area
hyperbolic surface, while a path based deep in the cusp must return
toward the core. Gaussian decay may then dominate the cusp density
and give a flat small-time remainder. This describes a route to the
estimates, not a completed proof of them for the source matrix operators.
No scalar Selberg trace formula is imported by a group-name match.

## 3. A finite charge combination removes the arbitrary reference

Let c_q be one of the explicit relative gauge coefficients from the
preceding Wilson table, so sum_q c_q=0. Set

  R(s)=sum_q c_q r_q(s).

Under A–C it is a legitimate finite sum of traces of trace-class
DIFFERENCES, even when the individual exp(-sP_q) traces diverge.
Changing the common reference replaces every r_q by r_q-r_ref;
its contribution cancels EXACTLY because sum c_q=0. No cyclicity of
an infinite unrenormalized trace is used. This is a derived reference
independence within the fixed compatible family, not freedom to change
the physical counterterm or species weights independently.

Its large-time constant is

  h=sum_q c_q h_q=sum_q c_q dim ker P_q.                  (1)

The reference kernel also cancels. A fixed end does not force h=0:
compact-core eigenvalues may cross zero, changing which fields should
be retained in the low-energy theory. The weighted kernel count is
not a topological charged-generation index and need not be an integer,
because c_q contains normalized charge indices.

## 4. What a common mass scale can and cannot change

Define, under A–C, the light-subtracted relative zeta combination

  Z(z)=1/Gamma(z) integral_0^infty s^(z-1) [R(s)-h] ds,    (2)

initially for Re(z)>0, with continuation to a neighborhood of0.
If h=0 the same integral is entire after multiplication by1/Gamma(z).
At small s, R(s)=O(s^N) for all N, so R(s)-h=-h+O(s^N).
The constant gives -h/z in its Mellin integral, while 1/Gamma(z)=z+O(z^2).
At large s the integrand is exponentially decaying. Therefore

  Z(0)=-h.                                              (3)

This is an explicit check of the zero-mode contribution; setting it
zero from a matched tail would erase low-energy running data.
For a common positive rescaling P_q -> c P_q, all eigenvalues and
thresholds rescale and R_c(s)=R(c s), with the same kernels. Hence

  Z_c(z)=c^(-z) Z(z),
  L_rel(cP)=L_rel(P)+Z(0) log c
           =L_rel(P)-h log c, L_rel=-Z'(0).               (4)

If h=0, the relative log determinant is independent of a COMMON
multiplicative scale. If h!=0, its scale dependence is fixed by the
actual charge-weighted light kernel (1), rather than a separately
fitted threshold constant. For c=ell^-2, the change is2h log ell.
This is a relative INTERNAL determinant identity, not a prediction
of the physical matching scale or a replacement for the 4D EFT beta
factors. Those factors must multiply the actual source determinant
combination and the retained light fields consistently.

At theta0, where full SU5 is restored, all H within each R coincide
and the preceding relative combination vanishes, including h. At a
noncentral angle a new light mode can produce a logarithmic singularity
in a heavy determinant. Comparing across that crossing requires a
new EFT/light split, not analytic continuation that hides log zero.
These are mandatory controls for a prospective numerical implementation.

## 4a. An explicitly convergent matching integral

The same hypotheses give a useful construction without taking the
trace of any individual infinite heat operator. For mu>0 define

  I(mu)=-integral_0^infty [R(s)-h(1-exp(-mu^2 s))] ds/s.   (5)

Near0 the numerator is -h mu^2 s+O(s^2)+O(s^N), so the
integral is locally absolutely convergent. At infinity it is
R(s)-h+h exp(-mu^2 s), which decays exponentially by C.
Its derivative is consequently justified on compact positive mu ranges:

  d I / d log(mu^2) = h.                                  (6)

To check the finite constant rather than guess a scheme, write
integral_epsilon^infty [R(s)-h] ds/s = h log(epsilon)+a0+o(1).
Using integral_epsilon^infty exp(-mu^2 s) ds/s
=-gamma-log(mu^2)-log(epsilon)+o(1) gives

  I(mu)=-a0+gamma h+h log(mu^2)
       =L_rel(P)+h log(mu^2).                             (7)

All logarithms use the same spectral units. Equivalently under a change
of numerical units P->cP and mu^2->c mu^2, (7) is invariant.
Changing P at fixed mu is a physical scale comparison and need not
cancel when h is nonzero. With h=0, (5) reduces to the absolutely
convergent -integral R(s) ds/s and mu disappears altogether.

The exponential switch in (5) is an explicit matching prescription,
not a derived physical subtraction law. Another admissible switch
changes the finite part by a constant times h. Thus the zero-weighted-
kernel case has no such switch ambiguity; a nonzero h needs the same
EFT matching convention and spin/ghost weights as the retained light
sector. Equation (6) alone supplies neither that physical coefficient
nor the measured gauge couplings. It prevents an adjustable finite
threshold from being passed off as a parameter-free calculation.

## 5. Preserve the distinction between a lemma and admission of the model

Derived under the stated estimates: reference independence of relative
charge combinations; the exact zero-mode constant in Z(0); and the
common-scale law (4). These remove a common reference and, in a
zero-weighted-kernel sector, a common internal scale from this relative
observable. They do not remove metric/shape/Wilson/state freedom, prove
B/C for the actual physical measure, or predict a coupling.

Next recover/prove the requisite relative heat estimates for the actual
source matrix operators and external gauge insertions, using the prior
continuum/graph results at their correct scope. That packet must be
source complete, independently reviewed and accepted before scientific
execution. The new conditional lemma is not an execution admission.
The original full SM/three/gravity mission is neither completed nor
redefined by this smaller analytic step.
