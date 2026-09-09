# R24: total mass-eigenline flux on the actual regulated source complement

2026-09-09. Pre-execution design. Path-local; no B allocation.

BANKED IDENTITY: R15's global commuting sourced field; R18's strong
maximal charged complex; R19's relative spectrum; R23's faithful
Clifford map and covariant positive-mass eigenline. These inputs are
not inferred from numerical Chern--Simons values or selected here.

PRIOR ART: Nie, arXiv:0909.4754v2, equations (1.4), (1.5), (2.2)--(2.12)
and Remark 1.12; the complete paper was read. R15 and R23's actual
producers were read. GLOBAL_MASS_FLUX_PRIOR.md and the saved all-head
presence sweep route the other hits. No universal absence assertion.

## Quantifier and expected outcomes

P0: orientable finite-volume hyperbolic three-manifolds with a finite
specified family of disjoint proper geodesic source arcs, positive
constant densities and at least one endpoint on every cusp, in R15's
commuting ansatz. Truncate all cusps, excise all charged arcs, retain
every resulting boundary face and round every circular seam. The
calculation ranges over this source/cut class, not just one member.
The source-free case is a topology/control case, not a claim that its
unperturbed gradient is nonzero. Closed fixed curves are not silently
charged. Mixed-sign sources and empty-end cusps are outside the
positive-boundary-sign statement.

P1--P4: the current PB-BOUNDARY/X33 source/anomaly join. R23's local
charge is not yet an evaluated total for the actual R15 field. The
relative-domain and full-eigenbundle qualifications stay in force.
No lower-priority phenomenological fitting or new parent is proposed.

P6: expect a positive identification K=-Phi with the secondary Euler
form, and total flux sign(q)*k for k prescribed arcs. A failure of
the spin map, curvature/sign identity, corner flow or boundary-sign
argument prevents that conclusion. Expect no physical selection of
k=3 and no automatic cancellation of the resulting gauge anomaly.

Every asserted finite identity must have discriminating controls.
Preserve first runs, failures and original code/tests. Any correction
requires a separately sealed follow-on, not a changed original receipt.

## A. The global bundle map and normalization

Use an oriented orthonormal tangent frame with column connection
A_ij, so nabla e_j=sum_i e_i A_ij. Set A v=a cross v, i.e.
A_ij=-epsilon_ijk a_k. The spin connection is Gamma=-i a.sigma/2.
Recompute the natural connection on even differential forms through
R23's actual U: it must be Gamma tensor 1 + 1 tensor Gamma, and the
mass must act on the second factor. This checks the bundle being
used, rather than choosing an unrelated flat auxiliary doublet.

For n=grad(qF)/|grad(qF)| and P=(1+n.sigma)/2, calculate directly

    K = i/(2 pi) Tr(P F_Gamma + P(DP)^2)
      = n.f/(4 pi) - n.(Dn cross Dn)/(8 pi),
    f = da + (a cross a)/2.

The cross product of one-forms includes both antisymmetric terms.
Use a rational stereographic chart and arbitrary connection/derivative
jets; a polynomial identity there extends to the other chart by
smoothness. Nie uses ROW connection omega=-A and curvature
Omega=domega-omega wedge omega=-F_A. Compute his n=3 expression
Phi=(epsilon n Dn Dn - epsilon n Omega)/(8 pi) with those conventions,
not a recalled sign. It must give K=-Phi.

Controls: outward unit sphere flux -1; reversed mass +1; constant
mass in a flat frame zero; the actual hyperbolic Levi-Civita connection
on a horosphere has nonzero curvature and covariant-projector terms
which CANCEL for its vertical unit vector. Omission of either term
must fail. Recheck the torsion-free coframe equation. No numerical
quadrature substitutes for the symbolic identification.

Any spin structure on the oriented three-manifold permits this local
factorization; changing the lift tensors both factors by the same flat
sign line. Its curvature does not change K or the real/integral surface
flux. Global torsion phases/Pfaffian signs are NOT thereby settled.

## B. Round the corners before applying the boundary theorem

At a finite cusp/tube meeting use coordinates u=rho-epsilon >=0 and
v=Z-z >=0, with constant Euclidean-radius tube in the cusp. The metric
is conformally Euclidean; the signs of V=grad(qF), q>0, are (+a,-b)
in this normal two-plane, with a,b>0. The component along the seam
is immaterial. Round by (u,v)=delta*(1-cos t,1-sin t), 0<=t<=pi/2.
The outward normal is (-cos t,-sin t), and the tangent from tube
to cap is (sin t,-cos t). Compute their pairings with V.

For the frozen positive field there is exactly one normal crossing,
and its tangent points OUT of the incoming tube region. For the
actual variable field use a nonzero positive-cone homotopy in a small
collar to the frozen field; do not assume a variable ratio a/b is
monotone. The homotopy preserves the eigenline class. Incoming surface
is therefore homotopic to T for q>0 and E for q<0. The tangential
field points outward at the incoming region's boundary in BOTH cases:
reversing V also exchanges which side is incoming. Verify that double
sign reversal explicitly. No circular seams are discarded.

Write the full argument that the relative boundary index is chi(T)
or chi(E), not merely a plug-in of Euler numbers. Nie then gives
Ind(V)=chi(C)-chi(incoming), and closedness of Phi in dimension three
gives integral_boundary K=-Ind(V). If V has nonisolated zeros, define
its total index by an interior generic perturbation fixed near the
nonvanishing boundary. This does NOT assert three actual Morse zeros.

## C. Topology and the complete exhaustion

Q has only torus boundaries, hence chi(Q)=0. For k proper arcs,
Q=C union N, with N a disjoint union of k balls, C intersection N=T
a union of k annuli. Thus chi(C)=-k, chi(T)=0, chi(E)=-2k.
The expected total K flux is +k for q>0 and -k for q<0. Recompute
R15's cubical relative complexes for k=0,1,2,3 and a second resolution
and height. These are independent product-model controls, NOT an
identification of the actual manifold with that product. Compare both
relative cochain Euler numbers and Betti numbers; include a ball with
constant, outward and inward mass controls to distinguish disc from
annular incoming pieces. Do not mistake chi(Q)=0 for chi(C)=0.

Recheck the boundary-sign exhaustion from the actual asymptotics:
F=U(w)+exp(2s)*(b*s+c)+v, b=pi*Q_cusp/A>0, with bounded high-cusp
s-derivative of the smooth L2 corrector. The derivative of U(w)
in s is zero even at puncture approach. Choose a high cap first;
at each finite cap height choose smaller tubes so beta/rho dominates
the bounded regular radial derivative, then small rounding collars.
The cutoffs need not be a fixed-rate simultaneous limit. Include
zero-b and fixed-radius counter-controls, which must fail the uniform
sign inference. Free finite c_i change a safe height, not this class.

All admissible sufficiently deep regulated cores have the same total
integer flux. This is a topological exhaustion statement, not a proof
that separate noncompact face integrals converge or carry individually
quantized fractions. Source magnitudes do not affect this class while
positive; matching it to R18's Hilbert kernel additionally requires
the declared strong maximal domain and |q beta|>=1.

## D. Physical join and remaining duty

Compare the actual total flux to R19's net relative index and R23's
descent with its outer term. For k=3 the resulting boundary anomaly
coefficient must be three actual H spinors, retaining the nonzero U1
and mixed traces. An internally constant gauge parameter still gives
zero bulk variation, not anomaly cancellation. Check that arithmetic
on the root-derived weights, not inserted representation dimensions.

This does not build a boundary eta invariant, admissible eight-dimensional
filling, finite-action defect, source selector, interacting vacuum,
compact 4D limit or gravity. R23's full degree-eight response and its
higher eigenline powers remain necessary in general external families.
Next: an actual end sector or compatible massive-gauge-field mechanism
with the opposite response. No hand-added opposite chirality is a
derivation. No TOE or main-bank completion is asserted.

## Execution and custody

Seal this design, producer and tests before import/execution, with
command-derived digests in the append-only manifest and SEAL_LEDGER.
Save the first native JSON, focused dependency tests and explicitly
enumerated expanded regression with original failures intact. Keep
the tree read-only while certifying. Append results/current readers,
laws and open duties; commit/push the own branch. No external relay,
main merge, new B ID or independent-review certificate is implied.
