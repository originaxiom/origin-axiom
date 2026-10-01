# Exact local Green witnesses on the changing logarithmic cone

October 1, 2026. R72 authored proof, frozen before finite controls.
We quantify over the supplied R66 canonical collar, all allowed fixed
q>0,q!=1,alpha>0, and the ZERO Fourier, charge-zero adjoint coefficient.
No complete architecture, full domain classification or particle count.

## 1. Actual equation and a small tail

Reuse R68's exact Q=Gamma(partial_r+A(r)/r) and R71's explicit
nine-coefficient neutral basis and Gram matrix G. The form pairing is
mathG=I8 tensor G; Gamma=[[0,-I36],[I36,0]], and J=-mathG Gamma.
For this block A is mathG-Hermitian, anticommutes with Gamma, and

  A(r)=A0+R(s), s=-log r,
  A0=diag(M tensor I9,-M tensor I9), M=diag(-1,0,0,1).

Its eigenvalue multiplicities are (-1:18,0:36,+1:18).
Q u=0 is EXACTLY u_s=A(s)u. It is not the frozen-limit equation.
Since C_y's kZ acts trivially in this block, the actual perturbation is
bounded in the trace-Hilbert operator norm by

  ||R(s)|| <= 2|v(s)|+4 sqrt(alpha)t(s)
                 +4|beta|t(s)^2/sqrt(alpha),              (1)

with v=h_s,t=exp(-h). Indeed ||ad H||<=2, ||ad N||<=2,
||ad P||<=2 in the Frobenius matrix norm; each link wedge/contraction
has norm1. A sum of the operator bounds gives (1). Restriction to the
neutral Hilbert subspace cannot enlarge these norms. This is a
conservative bound, not a sharp angular spectrum.

R66's exact branch has v->0,t->0. Thus a sufficiently late tail
s>=S has ||R||<=epsilon0=1/64 for every fixed allowed pair.
S may depend on the supplied parameters/background. No measured
radius, uniform q->1 limit or selected physical scale is asserted.
The elementary exact comparator alpha=1,beta=+/-1 admits
S=2^20 because the bound is 4/sqrt(s)+5/s. This is a control,
not a prediction or replacement of the general exact branch.

## 2. Exact solution spaces by an explicit contraction

This is a special-case proof of the standard roughness mechanism;
no unread roughness theorem is invoked.

For theta=1/4 or -3/4 set u=exp(theta(s-S))w and
B0=A0-theta I. Let Ps,Pu be its negative/positive spectral projections.
The stable spectrum is <=-a=-1/4, unstable >=b=3/4.
The stable ranks are54 and18 respectively. In the Banach space
of continuous w with norm sup exp(gamma(s-S))||w(s)||, gamma=1/8,
for each z in ran(Ps) define

  (Tz w)(s)=exp(B0(s-S))z
     +integral_S^s exp(B0(s-t))Ps R(t)w(t)dt
     -integral_s^infinity exp(B0(s-t))Pu R(t)w(t)dt.      (2)

The stable convolution bound is epsilon0/(a-gamma).
The unstable convolution bound is epsilon0/(b+gamma).
Their sum is q0=1/7<1. The inhomogeneous seed term has norm<=||z||.
Hence (2) has a unique exact fixed point, linear in z, with norm
<=7||z||/6. Differentiating its convergent integrals proves
w_s=(B0+R)w; no finite asymptotic residual is discarded.
At S, Ps w(S)=z. The unstable graph has norm<=1/48,
so the initial-value map is injective with dimension rank(Ps).

Conversely every solution in this weighted space satisfies (2):
variation of constants gives the stable integral; weighted decay
eliminates the growing unstable homogeneous term at infinity.
Thus uniqueness applies to ANY exact solution satisfying the bound.

The theta=1/4 construction gives a space Sl of dimension54,
whose solutions satisfy ||u(s)||<=C exp((s-S)/8).
The theta=-3/4 construction gives Sf of dimension18, satisfying
||u(s)||<=C exp(-7(s-S)/8). Sf is a subspace of Sl by the converse.
Every Sl solution is L2(dr), because dr=exp(-s)ds and
exp(-s) exp(s/4) is integrable. These are exact LOCAL Q-harmonic
solutions, not global zero modes or solutions of d and delta separately.

## 3. Conserved current gives actual nonminimal graph classes

From A dagger mathG=mathG A and A Gamma=-Gamma A,

  A dagger J+J A=0,
  d_s(u dagger J w)=0                                  (3)

for any two exact solutions. Sf paired with Sl tends to zero by
exp(-7s/8)exp(s/8)=exp(-3s/4); its conserved pairing is therefore zero.
At S, the ambient solution space is C72 with nondegenerate J.
The annihilator of Sl has dimension72-54=18. Sf already lies there
and has that dimension. Therefore

  Sl annihilator = Sf subset Sl,
  radical(J restricted to Sl)=Sf,
  rank(J restricted to Sl)=36.                         (4)

These statements do not require solving a polynomial log expansion,
identifying its individual powers or setting them equal to H1 traces.

Cut each solution off smoothly to zero before the outer collar edge,
while keeping it unchanged near r=0. It belongs to Dmax(Q): it is L2,
Q vanishes on the tail, and the cutoff residual lives on a regular
compact annulus. Integration by parts pairs two such cutoffs by their
nonzero conserved apex current, with the sign fixed by outward normal.
Every element of the compact-support graph closure Dmin pairs to zero
with Dmax, by graph-norm continuity. Hence every nonradical Sl class
is NOT in Dmin. The construction yields a36-complex-dimensional
nondegenerate subspace of Dmax/Dmin for the full coefficient operator.

The fast subspace actually gives minimal classes: u=O(r^(7/8)).
A cutoff changing at r~epsilon with derivative O(1/epsilon) has
squared Q error <=const epsilon^(-2) integral_0^(2epsilon) r^(7/4)dr
=O(epsilon^(3/4)), tending to zero; the L2 tail also vanishes.
After outer cutoff, fast solutions are graph limits of compact-support
smooth fields. Thus the kernel of the Sl-to-boundary map is exactly Sf.
This justifies the quoted36 witnessed classes, not a complete
classification of Dmax/Dmin including charged/nonzero Fourier sectors.

The Hermitian form iJ has ambient signature(36,36).
An isotropic Sf of dimension18 gives on its coisotropic quotient
signature(18,18). Accordingly the witnessed current space needs a
maximal isotropic half of dimension18 for a separated symmetric end
choice restricted to this quotient. This is a necessary local linear
boundary duty, NOT selection of that half, a full self-adjoint
realization or independent physical parameters/particles.

## 4. Preserve the physical distinctions

R68 already proved four exact Z traces. R72 now proves a larger
nondegenerate witnessed quotient without promoting R71's formal
eigenvectors to solutions. It is conditional authored analysis;
finite coefficient/rate/current checks do not independently review
the Banach-space proof or derive the supplied action and metric.

Q-harmonicity alone does NOT imply separately d-closed and delta-closed
on a maximal domain. A frozen scalar control with eta=1/4 supplies
a slow critical Q solution with nonzero separate derivatives.
It is a comparator, not this exact matrix solution or a new particle.
Nonlinear products may still diverge; compact gauge, reality and full
superfield domains must be tested in one common admitted class.
The cutoff argument constructs local graph witnesses, not source-free
global modes. Core and outer matching remain mandatory. No physical
chirality, physical generation count or complete Standard Model follows.

Next: determine which witnessed traces can join the action's bosonic
profiles and parent products, then an exact full end law and core match.
Threshold and other Fourier/coefficient blocks remain separate duties.
The parameter-free SM, quantum probabilities/consistency and gravity
requirements retain their original scope.
