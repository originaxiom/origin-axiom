# R27: verify the smooth geometric vanishing and the finite-field positive

2026-09-12. Pre-execution design; path-local R27, no B allocation.

BANKED IDENTITY: B264/B445's nontrivial geometric symmetric-power
cohomology is boundary-supported, with the primary theorem explicitly
available; B1297 defines n(V) as the image of relative H1 in ordinary
H1, not the Euler index of every possible singular Hilbert complex.
R18/R19 and R26 are conditional, different-domain results retained here.

PRIOR ART: FINITE_TWIST_PRIOR.md. Menal-Ferrer--Porti Theorem 0.1 is
standard published mathematics, already used in the corpus. The task
is to verify its finite-cover application and the received B1335
positive independently, not to claim a new vanishing theorem or an
absence from all history. FINITE_TWIST_PROOF.md is the pre-run argument.

## P0--P6 and the two outcomes

P0: over every connected orientable complete finite-volume hyperbolic
three-manifold, a genuine SL2(C) geometric holonomy lift, every
nontrivial symmetric power, and every finite-image coefficient twist,
does restriction of ordinary H1 to the full boundary remain injective?
The finite-cover/transfer proof is the all-family argument; a finite
matrix sample cannot establish that quantifier. The arithmetic positive
has a separate, single-presentation/single-prime quantifier below.

P1--P4: this is an owner-requested load-bearing audit of the chirality
route, alongside PB-BOUNDARY/X33. It does not jump to a numerical value
rung. Both rows, all covers, chirally asymmetric members and hyperbolic
partial fillings are within the smooth theorem when its hypotheses
hold. Singular source ends, non-geometric representations and different
boundary/domain choices are not silently included. No empirical value,
physical identification, numerical gap or selected source is an input.

P6: either the displayed transfer proof and its controls hold, together
with an independently validated arithmetic positive, or preserve the
first failure and narrow the claim. A failure in one module does not
withdraw another module's theorem or valid positive. Never replace the
smooth restriction map by R19's sourced index by naming both chirality.

All design, proof, source and test bytes are hashed and committed before
their first import or scientific execution. Later repairs require a new
seal and preserve first output. Native output is durably captured with
exit status. No edits occur during any scientific/certifying run.

## A. The theorem and exact algebraic mechanism

Use Theorem 0.1 with n=m+1 >= 2, not an unqualified statement that all
irreducible representations include the trivial one. Kill the finite
twist on its kernel cover, apply restriction injectivity there, and
derive the local-coefficient trace identity tr p*=degree(p). Check
commutation with the boundary map, including every lifted cusp.
Apply the argument separately to V and V*. Trivial geometric summands
have zero index by unitary conjugation, not necessarily zero interior H1.

In the monomial basis e0^(m-j)e1^j, implement E, F, H and the SU2
Hermitian metric G_jj=1/binomial(m,j). Set
X=(iH,E-F,i(E+F)), Y=iX and T=sum wedge(ej) tensor Yj.
Compute H_p=T_(p-1) T_(p-1)*+T_p* T_p in degrees 1,2 for m=1..6.
Verify Lie relations, the metric adjoints and positivity by exact
Sylvester minors of G_p H_p. m=0 must give the zero matrix, not a
positive bound. This verifies the mechanism, not all-m positivity by
sampling; the proof has the all-m kernel argument and primary source.

## B. Transfer and the rank pitfall: discriminating controls

For circle covers of degree r=1,2,3,4,6 and the declared primitive rth
root z, construct the actual cellular incidence matrix, pullback
v -> (z^j v), and trace (v_j) -> sum z^(-j) v_j. Check both chain maps,
tr p*=r, and the averaging projector. In characteristic dividing r the
scalar r vanishes: the inverse-degree inference must be rejected.
This is a transfer control, not a three-manifold index computation.

For t in C*, J(t)=[t-1,0], F=[1,0], compute F on ker J at t=1,2.
This tests the inference that Laurent-polynomial Fox entries alone
make restriction on a changing kernel lower semicontinuous. Do not
call this toy a manifold counterexample or a refutation of every
possible deformation proof. Global self-duality and the domain
conditions in the original index identity are separate obligations.

## C. Independent B1335 positive, not a census

Pin the received target at c83b6b802ee0e610a50ee07426ed610c2c6bd674:
m010, p=13, the second of the first four honest SL2(F13)
representations in lexicographic generator-matrix order, Sym^3,
generator character (4,12). Use SnapPy only to expose the presentation,
peripheral words and triangulation identifier; record those and its
version. Do not certify hyperbolicity, geometric holonomy or CS here.
Enumerate at most 300,000 candidate generator pairs; if the specified
four are not reached, report this bound as incomplete, not no witness.

Write the arithmetic/cochain producer independently, importing no
other-seat library. Recover the symmetric power from polynomial
substitution. Construct cocycle equations both by Fox derivatives
and by affine block-matrix multiplication, with explicit inverse-word
cocycles. Cross-check every modular rank with SymPy's finite-field
DomainMatrix implementation. Check the relators, the full chain maps,
boundary cocycle and coboundary membership before reading an index.

Compute restriction rank two ways: on an actual kernel basis modulo
boundary coboundaries, and, for this one-cusp presentation, by
rank([J;F])-rank(J)-rank(B_boundary). Verify the latter's coboundary
containment hypothesis through F d0=B_boundary. Save exact matrices.
Check n, its dual, all four reported identities and both domain
equalities. Test absolute irreducibility by the generated matrix
algebra, not just equality of invariant dimensions. Check the two
peripheral matrices are in a single unipotent subgroup and that the
character is trivial on both peripheral words.

Expected received result, NOT adopted before computation: I(V)=+1,
I(V*)=-1, with r1=0 and 2, t0=t0*=1. Validate non-self-duality by
intertwiners or a trace obstruction, never literal matrix inequality.
Compute the boundary cup form on the actual restriction image using
the invariant Sym^3 bilinear form and both transport factors. Test
whether only one image is isotropic; non-isotropy of the other is a
positive control against the one-sided-isotropy inference.

Also compute the inverse-character and untwisted self-dual controls.
A deliberately invalid generator mutation must be rejected before any
cohomology result. A separate PSL-valid relator evaluating to -I tests
the odd-power lift trap. A non-literally-self-dual but isomorphic SL2
module tests the bad equality shortcut. Neither finite-field positive
nor these toys is promoted to a characteristic-zero physical vacuum.

## D. Reporting and carried-forward duties

Keep the standard theorem, its application, independent exact finite
controls, unverified received counts and physical hypotheses distinct.
Run focused and explicitly enumerated broad regression; compare failed
test IDs with R26 rather than claiming full green. Run reporting gates
without modifying old baselines. Commit and push this branch regularly.
Do not merge other seats, allocate reserved numbers, claim independent
banking, or mark the TOE goal achieved. Return to the common source/end
action, stationary solution, anomaly and gauge-spectrum problem.
