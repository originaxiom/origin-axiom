# R18: complete weighted cohomology in a declared strong-source complex

2026-09-07. Pre-execution design. Path-local R18, no global B number.

BANKED IDENTITY: reuse the immutable R14 cusp field, R15 global scalar
parametrix and relative-pair calculation, R16 exterior engine and
amplitude convention, and R17 actual radial producer/sufficient height.

PRIOR ART: weighted radial homotopies are standard, not a new physical
law: Bullock, https://nyjm.albany.edu/j/2001/7-2.pdf, sections 4 and 6.
Compact mixed-boundary de Rham theory: Pauly--Schomburg,
https://arxiv.org/pdf/2106.03448, Lemma 4.6, Theorems 4.8--4.9 and
Remark 4.10; Licht, https://arxiv.org/pdf/1710.06868, section 7.1,
especially (7.7)--(7.10). Hilbert complexes and closed-range Hodge
theory: Arnold--Falk--Winther, https://www-users.cse.umn.edu/~arnold/papers/bulletin.pdf,
sections 3.1--3.2. These sections were read, accessed 2026-09-07.
None of their nonsingular compact theorems by itself covers our ends.
Dai--Yan 2005.04607 is NOT applied: its complete bounded-geometry
Morse hypotheses cannot simply be transferred to removed lines/cusps.

## Grounding and two outcomes

P0: the maximal de Rham Hilbert complex on the complement of finitely
many disjoint proper geodesic source lines in the R15 hyperbolic class,
with the declared positive densities, all effective strengths
abs(q)*beta_a >= 1, and positive total endpoint density on every cusp.
The conclusion quantifies over this class, not every defect realization,
parent, real form, gauge bundle or amplitude. W=0 and a global real F
are assumptions. This is a mathematical conditional model, not a TOE.

P1/P4: continue PB-BOUNDARY / X33. R17 explicitly leaves the global
closed-range and complete-kernel comparison open. A bounded chain
parametrix would settle those duties in this class without claiming
compact resolvent or importing a scalar spectral gap for charged forms.
The scoped closed-double/annular kills do not kill a sourced complex.

P2/P3: already_banked("weighted cohomology") flags B870; its full body
is about a central-extension group-cohomology obstruction, not this
weighted L2 comparison. "Hardy homotopy" returns no hits; "singular
Fredholm" has ten hits, zero settled two-term matches. Read the actual
R14--R17 producers and reports. The atlas card is epoch-blind, 1161 arcs.
The all-head regex sweep is PRESENT (mostly unrelated Hardy uses), not
an absence certificate. Its deleted-history check is matching PATHS,
not exhaustive deleted CONTENT. No novelty or universal absence claim.
Receipt: WEIGHTED_COHOMOLOGY_PRIOR.txt. Fetched pins: main c78003cd,
physics 659487bb, SM d1a91c7a, outside-bench 1fa9641b at the recorded
sweep; the immediately pre-seal refetch advances outside-bench to
6c7aaba6. No new incoming claim is assumed and no branch is merged.

P6: expect the strong maximal complex to compare to (C,T) for q>0
and (C,E) for q<0. Expect the weak positive-source constant-trace
control to refute an amplitude-independent version. If bounded maps
fail, bank only the proved local lemmas and retain the precise global
gap; do not declare the entire route dead. Polynomial and quadrature
tests check the proof's components, not an infinite-dimensional theorem
by sampling. Analytic domain/gluing arguments must be written separately.

CC numbering reservations and the full banking checklist were read.
Full-suite green and independent receiving-seat verification are not
waived. No global arc or physical identification is promoted here.

## Norms and operator convention

H=qF; d_H=d+dH wedge has its maximal distributional graph domain
in canonical L2. The Hodge operator meant here is
D=d_H,max+(d_H,max)*, with its Hilbert adjoint, NOT an unspecified
maximal first-order D and NOT two independently chosen domains.

U(alpha)=exp(H) alpha is unitary INTO L2(exp(-2H) dvol; forms with
the actual metric). Then U d_H U^-1=d_max. It is not asserted to be
a bounded invertible map of the original unweighted L2 space.
R15's bounded smooth corrector changes the weighted norms by globally
bounded positive factors; d and maximal graph domains do not change.

At finite height use the flat cylindrical comparison dr^2+r^2 dtheta^2
+dt^2. For a=q beta the coordinate component containing epsilon copies
of dtheta has radial density r^p, p=1-2a-2epsilon. Including dr does
not change p. The exact hyperbolic density has bounded positive ratio
(tanh(r)/r)^(-2a) (sinh(r)/r)^(1-2epsilon)
 (cosh(r))^(1-2*epsilon_t), tending to one.

On a high cusp use s=log z, H=V(w)+h(s),
h=q exp(2s)(b*s+c), b=pi*Q/A>0. The radial density for tangential
degree j, WITH OR WITHOUT ds wedge, is
w_j(s)=exp((2j-2)*s-2*h(s)), times exp(-2V) on the punctured torus.

## Proposed bounded homotopies and domain argument

Finite line collar 0<r<R:

 K0 f(r)=integral_0^r f(t)dt,
 ||K0||^2 <= R^2/[2(1-p)] for p<1;
 KR f(r)=-integral_r^R f(t)dt,
 ||KR||^2 <= R^2/[2(p+1)] for p>-1.

These follow from the squared integral kernels after conjugation by
r^(p/2). The second formula includes the logarithmic p=1 case.
For a>=1 all tangential p<=-1: constant traces are not L2 and the
endpoint homotopy has no residual projection (relative source face).
For a<=-1 all tangential p>=1: constants are L2 and backward integration
retracts to the full annulus (absolute source face, not a filled disk).
Weak a=1/2 has a scalar constant in L2 and a nonzero trace residual;
bounded K0 alone does not prove acyclicity.

On cusps let phi_j=(j-1)*s-h(s). R17's S0 gives abs(h')>=8 and
monotone growth. Set alpha0=abs(h'(S0))-1>=7. For q>0,
phi_j'<=-alpha0 and the forward kernel is bounded by
exp(-alpha0*(s-t)), t<=s. For q<0, phi_j'>=alpha0 and backward
integration from infinity obeys the reversed estimate. Both operators
have norm <=1/alpha0. Constants are L2 only on the positive-charge
cusp; the negative-charge cusp is relative.

The radial operators act on the ENTIRE punctured torus. Do not use
uncontrolled angular cutoffs at infinity: norm(d chi(w)) grows as exp(s).
Near a joint corner use Euclidean cusp radius rho=abs(w-p), not a fixed
physical-radius tube. Truncate cusps first, then finite-height source
collars; no uniform disjoint physical tube at infinity is assumed.

For maximal weak forms write u=alpha(r)+dr wedge beta(r). The equation
du=d_B alpha+dr wedge (partial_r alpha-d_B beta), tested against smooth
compact base forms, gives a distributional endpoint trace wherever
beta and the radial part of du are L1 in r. The reciprocal-weight
integrals in the above estimates ensure that property at the relative
ends. Nonintegrability of constant traces forces this trace to vanish.
Thus dK+Kd=I on the maximal domain at a relative end. This must be
justified weakly; separate L2 control of partial_r alpha is NOT assumed.

At absolute ends the identity is dK+Kd=I-P. Point evaluation at a
regular slice is NOT L2-bounded. Average both K and P against the SAME
normalized density eta on a fixed regular slab. All degrees use the
same eta; its integral is one. The resulting Kbar and Pbar are bounded.

Choose chi=1 near the end, zero before the regular transition. The map
A=I-d(chi K)-chi Kd equals
(1-chi)I+chi P-dchi wedge K. For relative ends P=0; A vanishes at
the end, and restriction/zero extension gives the finite relative pair.
For absolute ends A depends only on finite-core data and has a constant
tail; restriction/this extension gives the absolute pair. All derivative
cutoffs lie at finite height, where they are bounded multipliers.
The maps commute with d and are inverse up to bounded homotopy.
Finite source-collar maps retain the longitudinal cap coordinate, hence
preserve an already imposed relative cusp condition at the corners.

On the compact smooth-cornered C, the mixed de Rham result gives a
bounded K_C and finite harmonic projection Pi_C. Its usual local
regularization proof applies in finitely many boundary-adapted charts;
smooth metrics are uniformly equivalent there. Our interface is a
smooth collection of circles, not a fractal boundary partition.
For bounded chain equivalences i,p and ip=I-dJ-Jd, set
Q=J+i*K_C*p and Pi=i*Pi_C*p. Then dQ+Qd=I-Pi. Pi annihilates
exact forms and has finite rank; consequently ran(d)=ker(d) intersect
ker(Pi), a closed subspace. The cohomology is the finite relative
cohomology. This is the closed-range argument, not an inference from
finite Betti numbers alone.

## Sealed controls and interpretation

1. Exact conjugacy on all eight coordinate forms; independently computed
   line and cusp norm weights. Reversing the exponent must fail.
2. Derive both Hardy kernel bounds with a positive symbolic exponent.
   Complex polynomial/power profiles, both charge signs, strengths
   1, 3/2, 2 and R=1, 3/10. Numerical ratios must respect the analytic
   squared bounds within 1e-10. Keep the logarithmic primitive case.
3. Reuse the actual R14/R17 radial checks; all three tangential degrees
   obey the sign margin. Conjugated Volterra matrices at 64 and 128
   midpoint nodes, interval length 6/alpha0, must have norm <=
   (1+3/N)/alpha0 and change <0.05/alpha0. Removing the weight must
   violate this bound. Matrix controls are not a PDE spectral certificate.
4. Exact all-degree polynomial homotopy and cutoff identities, including
   the projection residual and the dchi term. Omission mutants fail.
   A shrinking bump proves point trace unbounded; averaged trace stays
   bounded. A relative cap is preserved by a transverse homotopy.
5. Explicit finite cochain model checks the composed parametrix algebra
   after nonorthogonal changes of basis. This is an algebra control,
   not a replacement for the preceding infinite-dimensional argument.
6. Recompute R15's cellular full pairs for 0,1,2,3 arcs and a second
   three-arc resolution. Retain H0/H2 and the zero-arc/missing-tube
   controls. Test the source-strength classifier on weak/mixed/neutral
   inputs; no count is awarded outside the declared class.

If the comparison is established, R15's two-cusp/three-proper-arc
homological hypotheses give degree vectors (0,4,1,0) and (0,1,4,0),
hence complete H1 multiplicities four and one in THIS realization.
No new interval-certified source-isometry or physical parent selection
is claimed. A four-dimensional interpretation, consistent interactions,
anomalies and source/domain selection remain separate obligations.

Seal design, source and tests before execution. Preserve failures and
repair only in separately sealed new files. No edits during live runs.
