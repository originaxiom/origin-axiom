# R21: anomaly completion on the actual subgroup, and its holonomy cost

2026-09-08. Pre-execution design. Path-local R21; no B allocation.

BANKED IDENTITY: reuse R19's E6 Cartan matrix, root/fundamental Weyl
orbits and charge direction u=omega_1^vee, and R20's nontrivial
C3-compatible characters (zeta,zeta^-1). Reproduce the positive
adjoint spinor and its anomaly, not a replacement spinor with the
opposite D5 chirality. B864's 16+10+1 cancellation and the earlier
audit branch's B796/gap2_gs are prior work, not discoveries here.
The new question is their realization on the ACTUAL quotient-parent
subgroup and their compatibility with this sourced background.

PRIOR ART: Garcia-Etxebarria--Montero, https://arxiv.org/pdf/1808.00009,
sections 3.6.3, 3.7 and 4.1, read in full: ordinary spin bordism
Omega_5(BSpin(10))=0 and Omega_5(BE6_sc)=0, and the Z3 lens-space
eta formula/charge constraint. Choi--Forslund--Lam--Shao,
https://arxiv.org/pdf/2309.03937, section 2.2 pp.9--11 and Appendix B:
periodicity tests depend on global gauge form; extra topological
fields can change the effective fractional-coupling description.
Pantev--Wijnholt, https://arxiv.org/pdf/0905.1968, section 3.4 pp.29--31:
actual inflow couplings, their geometry and the possible KK-scale
mass of an anomalous U1 must be supplied. These are source premises,
not results reproduced by a finite symbolic test. Access 2026-09-08.

## Scope, prior and routing

P0: the compact subgroup H=C_{E6/Z3}(u) of the R19/R20 prescribed
source model, with three left-handed adjoint-origin 16_(+1) modes,
on ordinary spin four-manifolds. No combined spin-gauge quotient is
assumed. Test one added-field anomaly completion and whether a
covariantly constant Higgs could implement it on the unchanged
nontrivial order-three internal holonomy. Conclusions about that
ansatz are not closures of nonparallel fields, defects or inflow.

P1/P4: PB-BOUNDARY/X33, continuing the load-bearing consistency
obligation explicitly named in R20. The closed-double, cusp-trivial
twist and fundamental-27 restrictions retain their narrower scopes.
No empirical mass/scale comparison is planned. This is not main
banking; independent proof/receiving-seat review remains unpaid.

P2/P3: atlas and already-banked queries completed; the eleven-head
all-branch lexical sweep is PRESENT. Read the older B796 gap2 body
through its literature addendum, B864/B1096/B1119 and relevant
B951/B971 source discussion. B1119's 'anomaly' is a different
invariant-form error. No absence or novelty claim. Current main
31dd52b9's B1302 was read with its cusp-index producer: its no-twist
theorem requires triviality on BOTH cusps, unlike R19/R20. Its bounded
48-specialization 'golden face' test is not adopted as a universal
specialization theorem. See ANOMALY_COMPLETION_PRIOR.md.

P6: positive prior for the exact H-representation completion and
factorization below; negative prior for a nonzero parallel charge-4
Higgs at the pair-free holonomies. Expect a nontrivial residual Z3
anomaly if only a holonomy-trivial charge-12 scalar condenses and
the three spinors are the entire remaining charged matter. Preserve
failures; do not alter an original instrument after its first run.

## Lattices and a real representation map

Use simple-coroot coordinates and the R19 C with edges 0--2--3--4--5
and 1--3. Long roots have squared length two. The maximal torus of H
has cocharacters C^-1 Z^6. For lambda=v+c*u, v perpendicular to u,
c=3*lambda_0/4. Write z for the coweight coordinates, lambda=C^-1 z.

1. Derive the primitive D5-singlet character t=4c=3*lambda_0,
   expected integer row (4,3,5,6,4,2) on z. Its primitivity and the
   saturation of the D5-coroot columns C[:,1:] prove ker(t)=Spin(10),
   not an extra independent Z4 remnant. Scalar u-charge q is allowed
   for a D5 singlet precisely when q is a multiple of four.
2. Let O swap the two short D5 arms (indices 1 and 2) on v. Test
   F(v+c*u)=O(v)+3*c*u. F must carry C^-1 Z^6 isomorphically onto
   Z^6, preserve the D5 root/coroot datum up to that arm swap, and
   send u to 3u. This then integrates to H -> H_sc -> E6_sc.
   The first arrow is a compact-group isomorphism onto the standard
   centralizer H_sc, NOT an extension to E6/Z3 -> E6_sc.
3. Pull back the actual 27 weight functionals by F. Require integral
   root coefficients and the decomposition 16_(+1)+10_(-2)+1_(+4),
   with the 16 weight set EXACTLY R19's positive adjoint spinor.
   Omitting the arm swap is a live wrong-chirality/lattice control.
   The H representation exists; no 27 of E6/Z3 is being asserted.

## Anomaly and ordinary periodic counterterm

For a left Weyl representation with weights ell, use the convention
I6=sum(ell^3)/6 - p1(T)*sum(ell)/24, with curvature divided by 2*pi
and Hermitian Cartan eigenvalues. Put Q=lambda^t C lambda/2 and
lambda_T=p1(T)/2. Compute from actual root weights the candidate

   I6(3*16_(+1)) = t * X4,       X4=3*Q-lambda_T.

An independent orthonormal D5 spinor sign enumeration checks the
trace identity: I6(n*16)=n*(8*c^3/3+2*c*sum(v_i^2)-2*c*p1/3).
Check the full polynomial, not only the scalar-U1 specialization.
For general n the coefficient is n/3 times t*X4; neither n=3 nor
chirality is inferred from the anomaly equation alone.

Prove global integrality on H by a map, not by checking a finite flux
grid: if Q'=F^*Q_sc, test 3*Q=3*Q'-t^2. Q_sc is the normalized
integral degree-four class of simply connected E6 and t a genuine
character. Thus X4 is an integral class on BH times BSpin. A second
check derives the integer quadratic form 3*C^-1/2 on all z. Its
diagonal/off-diagonal coefficient denominators determine all levels;
levels one and two fail, level three passes. Do not turn this torus
check alone into a classification of all quotient-parent torsion.

In a scheme preserving D5 and local Lorentz invariance, descent can
put the anomaly on U1: I5=(4*A_u/(2*pi))*X4. For theta of period
2*pi and delta theta=4*epsilon, the local term -i*integral(theta X4)
cancels that variation. The positive kinetic term
f^2/2*(d theta-4*A_u)^2 gives m_A=4*g*f with kinetic F_u^2/(4*g^2).
This is a mass relation with input f,g, not a predicted mass.

A CHARGED circle-valued field is a section, not a free scalar on
every H bundle: nonzero modulus reduces the structure group to
ker(t). Fractional one-/two-copy formal counterterms on arbitrary H
bundles do NOT prove those spectra inconsistent. Test this explicitly
with the anomaly-free completed matter for arbitrary multiplicity.
Defects and extra topological sectors are separate possibilities.

## Added fields, mass terms and the unchanged internal background

Add n vectors V in 10_(-2), n singlets N in 1_(+4), and a complex
scalar Phi in 1_(+4). For n=3 these are 33 additional Weyl components,
not claimed to be supplied by R19's adjoint spectrum. The whole
fermion representation is the F-pullback of n ordinary E6_sc 27s,
so its full local anomaly vanishes and its global anomaly vanishes
by naturality of the anomaly and the cited E6_sc bordism result.

With Phi=(f+rho)*exp(i theta)/sqrt(2), the gauge-invariant terms are
  (y_V/2)*Phi*V.V + (y_N/(2*M))*Phi.conjugate()^2*N.N + h.c.
Nonzero diagonal y's make every added V,N massive, leaving the
original chiral Spin(10) spinors. The second term is dimension five;
this is an effective action below an INPUT cutoff M, not a UV-complete
theory. A positive quartic lambda*(|Phi|^2-f^2/2)^2 supplies a stable
radial mode. Couplings, potential, extra fields and scales are inputs.
The full heavy determinant, not just a covariant ABJ trace, supplies
the consistent low-energy anomaly-matching functional. Do not confuse
the consistent and covariant pure-U1 coefficients (factor three).

On the existing order-three holonomy, charge q has character chi^q.
Compute H0 of that rank-one flat system exactly. Charge four is not
parallel; allowed parallel D5-singlet charges are 12*Z, by gcd(4,3)=1.
This rules out only a nonzero covariantly constant bulk Phi while
keeping that background. A nonparallel/localized Higgs, changed
holonomy, or a defect axion is not tested by this obstruction.

For charge 12, ker(t^3) has component group Z3, split explicitly by
exp(2*pi*i*u/3), with trivial intersection with Spin(10). It acts as
zeta on the 16. With no other low-energy charged/topological sector,
compute the Z3 anomaly using the EXACT lens sum (1808.00009 (4.4),
n=3,k=3) and independently the net charge mod nine (4.10). Three
spinors give 48 charge-one Weyl components: expect eta=1/3 mod one
in that convention, not zero. The inverse orbit changes the sign.
Controls: neutral, charge-conjugate pair, nine spinors, and complete
27-shaped H matter. Charge-12-only mass monomials for V.V or N.N
must fail the same exact charge test. This is a restricted residual
anomaly, NOT a kill of the sourced theory or all discrete completions.

## Execution and checks

Seal this design, prior receipt, source and direct mathematical tests
with generated sha256 digests before first execution. Run native exact
JSON and pytest with R19/R18; rerun R20's successful word control as a
separate dependency check. Include coefficient/charge/chirality mutants
and vectorlike controls. All failures get immutable receipts and a
separately sealed correction if needed. No tree edits during scientific
or certifying runs. Update reader surfaces after terminal outputs;
retain all earlier full-suite/governance debts without waivers.
