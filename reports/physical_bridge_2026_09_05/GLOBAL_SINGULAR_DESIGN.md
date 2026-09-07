# Path-local R15 — extend the singular field, and count the full boundary pair

2026-09-07, before first scientific execution. Local research seal; no B
allocation, main banking acceptance, remote write or empirical claim.

P0: the commuting, topologically trivial gauge-bundle ansatz on complete
finite-volume hyperbolic three-manifolds with prescribed disjoint proper
geodesic line sources; specialize its finite-cutoff topology to m202 and
the three proper components of its order-three fixed locus. This is not
a statement about every branch, gauge bundle, physical metric or TOE.

P6 prior: the R14 end fields should extend globally after repairing the
constant-mode obstruction. The corrected finite pair should retain net
three but need not contain only three modes. The anticipated Betti numbers
are (0,4,1,0) and (0,1,4,0), NOT an assumed pure three-family spectrum.

## Prior work, searched rather than discarded

Continue R12's proper-arc excision and R14's explicit torus Green field.
Their sealed sources stay unchanged. R13's smooth meridional harmonic
form is a different field. R72's source choice remains a live candidate,
not refuted by the smooth local-system count. The compact-E6 parent used
below is an explicit modeling assumption, not the geometric Riley bundle.

Fresh fetch: main 506c591f, physics 659487bb, SM c3c3a8ed. The only new
physics diff is a table-format repair. Main B1294 and SM's chirality map
were read; their newly received theorems are NOT independently certified
by this round. The smooth principal-deformation problem does not specify
the logarithmic sources or mixed boundary domain studied here. B1294's
coefficient caveat predates our R13 numerical coefficient. No overwrite
or cross-seat priority claim follows from the receive time.

The existing already_banked query 'singular cusp global Poisson Higgs
relative cohomology' gives 179 hits; its only four-term settled hit is
B975, whose complete body was read (rendering/provenance, not this PDE).
The fetched ten-head absence sweep for
`parametrix|reduced resolvent|global (Higgs|Poisson)|three.arc.*cohomolog|cohomolog.*three.arc|four.*one.*mirror`
returns PRESENT. It is not an absence certificate or proof that this
construction is new. Local law/lead/ladder/kill-graph searches retain the
cut/boundary hatch, the parent-representation warning and PB-BOUNDARY.
R12's entire Cubes implementation is read and reused, not rediscovered.
WORKING_RULES and CC numbering/banking relay remain binding; R15 is only
a label inside this report directory. Full/independent banking not earned.

Primary sources checked 2026-09-07:

- Golénia--Moroianu, https://arxiv.org/pdf/0705.3559, Proposition 5.2
  and (5.14)--(5.15): SCALAR positive Laplacian on finite-volume
  hyperbolic 3-manifolds has essential spectrum [1,infinity). Do NOT
  transfer its scalar spectral gap to the one-form or charged operator.
- Pantev--Wijnholt, https://arxiv.org/pdf/0905.1968, (3.20)--(3.25)
  for line density; (3.36)--(3.40) for the deformed differential and
  relative cohomology. Its physical domain is a separate assumption.
- Braun et al., https://arxiv.org/pdf/1812.06072, (2.18), (B.15)--(B.16),
  (B.23): charged modes come from the parent ADJOINT and conjugate sectors
  must not be double-counted as both H1 and H2 fields.

## Proposed global construction, to be audited with the controls below

Metric curvature length one; Delta=div grad is nonpositive in L2 and
L=-Delta. Each source has constant density beta per proper length.
J=2*pi*sum beta delta_line is a locally finite distribution, not an
integrable total charge on an infinite line. All densities positive is
the chosen case, not a symmetry-forced sign or normalization.

1. Near each complete cusp use R14's F_end with its actual torus and
   source endpoints, initially c=0. Near the compact parts of each
   geodesic use beta*log(tanh r), r=distance from that geodesic. Its
   cylindrical metric is dr^2+sinh(r)^2 dtheta^2+cosh(r)^2 dt^2;
   radial flux per unit t is exactly 2*pi*beta. Local parametrices
   differ smoothly near their common source. Patch their regular parts
   using cutoffs so F0 has Delta F0=J+r0 with r0 smooth and compactly
   supported on the UNEXCISED complete manifold. This is an existence
   construction; no triangulated numerical F0 on m202 is being claimed.
2. Let psi_i=chi_i(z)*z^2 on cusp i, cut off to zero in the core, with
   chi=0 below one height and 1 above another. For A_i=Im(tau_i),

       integral_M Delta psi_i dvol = 2*A_i.

   The compact support belongs to Delta psi_i, not to psi_i. Therefore
   choose finite c_i such that 2*sum A_i*c_i=-integral r0. A nonzero
   mean residual is NOT fed to an inverse that excludes constants.
3. r=r0+sum c_i Delta psi_i is orthogonal to constants. On this complete
   connected finite-volume manifold ker L consists of constants and
   zero is isolated below the scalar essential threshold 1. Thus the
   reduced inverse exists and v=(L|1-perp)^(-1) r is real and L2.
   F=F0+sum c_i psi_i+v satisfies Delta F=J distributionally, hence
   phi=u dF, W=0 solves the commuting BPS equations off the sources.
   With scalar spectral gap lambda_*>0, ||v||2<=||r||2/lambda_* and
   ||dv||2<=||r||2/sqrt(lambda_*). No numerical lambda_* is supplied.
4. In a source-free residual tail, v is harmonic on the whole cusp
   (including the line after its logarithm is subtracted). Its L2
   expansion has a constant and decaying z K1 Fourier modes, but no
   growing z^2 term. Hence for positive total density the outward
   z^2 log(z) normal component survives. Small source tubes are inward.
   At finite large caps/small tubes this gives the actual sign pattern
   E=outward external surfaces and T=inward annuli, with corners.
5. The c_i are NOT all selected. With s cusps their allowed differences
   obey sum A_i delta_c_i=0, leaving s-1 homogeneous through-flux
   parameters, plus an irrelevant additive constant in F. On m202 this
   is one real matching freedom. No unique physical vacuum is derived.

The scalar reduced inverse is on the smooth complete M, not on a manifold
punctured by the sources; the explicit parametrix has already removed
the singular distribution before inversion. This distinction is essential.
No finite-action defect completion, ADE fibre construction or normalized
charged wavefunction is inferred from solvability of this scalar problem.

## Finite-cutoff cohomology and parent, without an index-only shortcut

Q is the compact core of m202, H1(Q;Z)=Z^2 and H2(Q;Z)=Z. For k disjoint
proper arcs let C=Q minus open tubes, T=their k annular sides and E=the
remaining original boundary. Excision gives H2(Q,C)=Z^k, all other
positive relative groups zero. The map H2(Q)->Z^k is intersection with
the arcs. For two boundary tori, any cross-cusp arc gives a primitive
nonzero entry. Three endpoints on each torus force at least one such
arc: detailed endpoint pairing is NOT required. For k=3 this implies

    H_*(C)       = (Z,Z^4,0,0),
    H_*(C,T)     = (0,Z^4,Z,0),
    H_*(C,E)     = (0,Z,Z^4,0).

In general with a primitive nonzero intersection vector and k>0 the
4 becomes k+1. The relative groups follow from both exact sequences
and Poincare--Lefschetz duality for the complementary boundary triad.
Neither the knotting of the arcs nor a product structure is assumed
in that proof. The product T2 x I with vertical arcs is an INDEPENDENT
cellular control sharing this homology, not a triangulation of m202.

For finite cutoffs F is smooth and bounded, d_q=e^(-qF) d e^(qF) is
conjugate to d and preserves a chosen relative boundary subcomplex.
Thus the two mixed-boundary de Rham problems have these Betti numbers.
Their H1 multiplicities are 4 and 1, net magnitude 3. This is conditional
regulated charged cohomology, not a proof that the singular complete-end
physical operator has these normalizable modes. The exponential maps
are unbounded as cutoffs are removed; that limit is the next task.
The labels R versus Rbar depend on the charge/orientation convention.

Choose the compact E6 parent and u=omega_1^vee (B351/R13 Cartan).
The adjoint root grading is expected to be
78 = (45+1)_0 + 16_(+1) + conjugate16_(-1).
Verify it from the 72 roots and their D5 Weyl orbits, not by substituting
one 27 as parent matter. If this parent/domain is realized, the finite
cutoff result is four spinors and one conjugate (up to sign), not three
27s. A zero-Higgs control must recover the full 78, not this split.
No E8 family multiplicity, principal geometric holonomy, interacting
mass lifting or physical SO(10)->SM breaking is silently inserted.

## Two-sided verification criteria, sealed before running

1. Derive Delta(chi(log z) z^2) from the metric; two distinct polynomial
   transition profiles with zero endpoint derivatives must integrate to
   2A. A cut-off constant must integrate to zero; treating psi as compact
   must fail for nonzero A. Derive the radial Hardy threshold identity
   under s=log z, f=e^s w; this check is SCALAR only.
2. Exact local log(tanh r) equation and source flux. Omission of the
   mean-repair coefficient leaves a nonzero residual mean. Unequal cusp
   areas test the weighted matching condition and its one free direction.
3. Exact cellular C,T,E complexes for k=0,1,2,3 on a 6x6 torus and k=3
   on an 8x8 torus, heights 1 and 2. Boundary-square zero is verified by
   the existing Cubes method. Check ALL Betti groups, PL duality, Euler
   and k=0's nonzero H0. Dropping T must fail the full H0/H2 comparison even
   when the Euler agrees. Invalid primitive/nonzero hypotheses must not
   be accepted by the exact-sequence summary.
4. Recompute m202's abelianized presentation and actual order-three
   self-cusp matrices using SnapPy, not cusp-swap determinants. m004's
   group has no order-three witness and is the negative control. This
   is a software geometric witness, not interval-certified geometry.
5. Reconstruct E6 roots from the Cartan; verify root count/lengths,
   D5 rank five and 40 roots, and two 16-element reflection orbits with
   projected squared length 5/4. Zero u gives 78 neutral generators.
   The 27-parent shortcut is rejected by dimensions and actual grading.

An algebraic identity or symbolic model is not a numerical mesh solution.
Preserve any first failure, no silent tolerances/expectations edits. Tests
and design/source are hashed and locally committed before execution.
