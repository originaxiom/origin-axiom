# R5 — full one-loop orientation potential, sealed before calculation

2026-09-05. Continuation of R4 after upstream a8fd2460 was merged and its
59 focused tests and independent action checks completed. No measured input.

BANKED IDENTITY: R4's explicit compact-E6 action, two scalar 27s, one real
adjoint, cubic Yukawa interaction, and classical zero of every potential
square at distinct S,N and Y. Reproduce its rank-109 scalar Hessian and
66 broken generators inside this pipeline before interpreting loop numbers.
B1250's D2 grading is now explicitly Weyl-conjugate to this construction;
this does not derive the action or select its vacuum.

PRIOR ART: `already_banked.py radiative vacuum potential Coleman Weinberg`
(33 hits; no >=3/5 settled match), atlas context card `radiative vacuum
selection`, and `absence_sweep.py 'Coleman|radiative.*vacuum|effective.potential'
--regex` returned PRESENT across nine fetched heads. Relevant hits read:
B962 PRIOR_ART_VEV Q2; B796's dimensional-transmutation mechanism catalog;
the separate heterotic/Kähler-scale question map and its explicit quantum
stabilization opening. These are not a claim that quantum work is absent.
The current task is the particular newly constructed R4 action.

Formula source: Stephen P. Martin, [hep-ph/0111209v2, equations 1.1 and
3.2–3.5](https://arxiv.org/pdf/hep-ph/0111209), accessed 2026-09-05.
Use MS-bar and Landau gauge, summing real scalars, Weyl fermions and vectors;
the respective constants in the logarithmic potential are 3/2,3/2,5/6.
This is a theoretical convention, not an empirical premise.

## Scope and additional choices

P0: the leading perturbative angular lifting in the **chosen** four-dimensional
non-supersymmetric R4 theory, along its exact tree-level vacuum family
`phi1=S, phi2=N, A in su5, Tr27(A^2)=5`. This is not a result about every
potential, field content, spacetime, member, relational mechanism or loop order.

Set all R4 quartic coefficients equal to a common positive lambda. This
one-parameter ray includes its original lambda=1 representative but does not
exhaust the independent positive coefficients. Choose one Weyl 27 with equal
Yukawa coefficients y=1/4 for the numerical absolute potential. Any family
number and fixed symmetric Yukawa matrices give A-independent fermion masses
on this family, so the angular cancellation will also be stated algebraically.
No generation count or Yukawa parameter is thereby predicted.

The scalar kinetic terms are those already declared in R4:
`sum |D phi|^2 + (1/2) Tr27(DA DA)`. Explicitly choose gauge generators with
`Tr27(t_a t_b)=3 delta_ab`; test the simple SU2 generator normalization from
the representation itself. This fixes a definition of the free coupling g,
not its value. For the original nonorthonormal Hermitian basis T, put
`Gamma_ab=Tr27(T_a T_b)`, `K_s=diag(2 I108,Gamma)`, `K_g=Gamma/3`.

For each background compute the **full** real constraint Jacobian J(A) and
real gauge-orbit matrix G(A), and form

```text
M_s^2 = K_s^(-1/2) [2 lambda J^T J] K_s^(-1/2)
M_v^2 = g^2 K_g^(-1/2) [G^T K_s G] K_g^(-1/2)
M_f^2 = M_f^dagger M_f,  M_f = y [C(S,.)+C(N,.)].
V_1 = {sum_s m_s^4[log(m_s^2/mu^2)-3/2]
       -2 sum_Weyl m_f^4[log(m_f^2/mu^2)-3/2]
       +3 sum_v m_v^4[log(m_v^2/mu^2)-5/6]}/(64 pi^2).
```

Goldstone scalar eigenvalues are retained (zero contribution in this gauge
at tree-level minima); Landau-gauge ghosts are massless. The continuous
`x^2 log x -> 0` limit handles zero squared masses. A significantly negative
eigenvalue or non-positive kinetic metric is an instrument/domain failure,
not something to repair by taking absolute values.

## Computations, controls and two possible outcomes

1. Reproduce the R4 ranks and compact metric. Compare generalized eigenvalues
   against explicit whitening. Compare vector masses against an independent
   direct kinetic-term formula. Check a simple abelian Higgs factor-of-two
   control and scalar radial normalizations. Verify directional derivatives
   of the full constraints at a non-Y background. Negative kinetic and
   negative mass controls must be rejected.
2. Evaluate Y, the old generic competitor, and an SU4xU1 orientation with
   fundamental eigenvalue multiplicities 4+1. All obey the same exact norm
   and annihilate S,N. Include 96 random Cartan-sphere points, seed 20260905.
   Compact SU5 Hermitian diagonalization exhausts this SU5-adjoint family's
   gauge orbits by its Cartan sphere; sampling it does NOT exhaust the sphere.
3. Check sector-by-sector `sum m^4` orientation independence and compare
   angular differences at mu=1/2,1,2. If either fails beyond scaled numerical
   tolerance, stop before interpreting a scale-independent lifting: missing
   operator/counterterm or normalization dependence needs diagnosis. Constancy
   is a hypothesis to verify, not presumed protection of the entire action.
4. At Y use norm-preserving paths with canonical tangent norm `Tr X^2=1` in
   color and weak adjoints. Finite central curvatures at epsilon .02,.01,.005,
   .0025 check convergence; an off-diagonal direction in each multiplet
   independently checks degeneracy. These are leading effective-potential
   curvatures, not complete pole masses. Radial shifts enter orientation
   energy at the next order when the normal tree Hessian is invertible.
5. Record scalar and vector contributions separately. At fixed norms their
   orientation-dependent contributions can scale as lambda^2 and g^4 if the
   previous trace check passes. Evaluate lambda in {.05,.2,1} and g in
   {0,.25,.5,.75}; the zero-g control is a decoupled limit. A sign change is
   evidence for parameter dependence, not a reason to discard either sign.
6. For the preselected illustrative point lambda=.2,g=.5, compare all sampled
   candidates and run BFGS from the eight lowest sampled/named starts, on
   normalized four-dimensional Cartan coordinates (maxiter=150, gtol=1e-7).
   Retain every success/failure and every final point. This is a local search,
   NOT a global-minimum proof. A lower explicit competitor rules out Y as the
   lowest energy on this family at that point; a search finding none does not
   prove uniqueness. Positive curvatures are local, not global, evidence.

Prior: quantum lifting may favor or disfavor the SM and may depend on free
couplings. Tree-level zero modes alone do not decide it. The chosen potential
has no symmetry that we have proved protects all omitted operators. Even an
SM-favoring result would leave light-Higgs construction, threshold matching,
parameter selection, gravity and empirical tests to be paid separately.

All computed spectra and scan points are retained, not only winners. Seal
the code, tests and design before their first execution. Failed files remain
byte-faithful; corrected runs get a new name and a new pre-run code seal.
