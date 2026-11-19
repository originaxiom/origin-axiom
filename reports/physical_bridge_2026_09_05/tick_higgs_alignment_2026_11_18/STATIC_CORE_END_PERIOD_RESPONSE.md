# Static energy of a puncture period from the parent curvature term

19 November 2026. Author hand calculation for review, following 09f0c2617. The comparison is on the two-dimensional internal surface of the supplied supersymmetric parent. Four-dimensional momentum is zero. Coupling, trace metric, background metric and flat holonomies are inherited inputs. No measured value enters.

## Core with prescribed trace

Cut the complete finite-area surface on a horocycle. Write K for the connected compact genus-one core with one boundary circle, A_K for its area, and use the positively oriented coordinate x of period one on its boundary. Take either previous flat background A0 with q=r=0. In a parallel frame around the puncture prescribe the linear connection trace p dx. The peripheral fibre holonomy equals I for both backgrounds. The trace frame is carried in the comparison. Let P project orthogonally onto the adjoint vectors fixed by the entire fibre holonomy, evaluated in this frame. The answer for the minimized coefficient of epsilon² at fixed first variation p is

    E_K(p) = ||Pp||² / (2 g6² A_K).

The parent potential in weave_curved_action_2026_10_08/PROOF.md gives ||d_A0 a||²/(2g6²) for the gauge quadratic term. At q=r=0 the linearized spin residuals have their own nonnegative squares. Setting their variations to zero attains their minimum. The following minimization ranges over all smooth connection variations with the prescribed tangential trace, allowing gauge and harmonic directions.

For each parallel adjoint section v, Stokes gives the integral of <v,d_A0 a> as <v,p>. The minimum-norm curvature compatible with these pairings is the parallel top form (Pp/A_K) dvol. Its norm gives the displayed bound. To see attainment, extend the prescribed trace smoothly to a0 on K and subtract d_A0 a0 from the target curvature. The difference pairs to zero with every parallel v. Pull back to the connected finite cover killing the fibre holonomy (degree one or four). The integral of this vector-valued top form there is invariant under the deck action in the parallel trivialization, and its pairings with every invariant v vanish. Its integral is therefore zero. Integration identifies top relative de Rham cohomology of a connected compact oriented surface with R, component by component. There is a primitive with zero tangential trace. Average that primitive equivariantly over the finite deck group and descend. Adding the descended form to a0 attains the bound. The minimizing curvature obeys the linear bulk field equation d_A0† d_A0 a=0. Harmonic zero modes need no inverse. In particular, this formula fixes the energy after allowing the whole linear response inside the core.

## End with square-integrable fields

Use the actual adjoining circle cusp with metric dr²+l² exp(-2r) dx² for r>=0 in curvature-radius-one units. Its area A_E=l. On the constant angular component in radial gauge write a=f(r) dx. The static energy numerator is the integral of exp(r)||f'(r)||²/l. Angular averaging gives the same lower bound with arbitrary angular/radial components because a periodic angular derivative averages to zero. Finite derivative energy implies existence of the limit of the mean f by weighted Cauchy–Schwarz. Square integrability in the kinetic norm forces that limit to be zero. With f(0)=p,

    E_E(p) = ||p||² / (2 g6² A_E),       f(r)=exp(-r) p.

Indeed Cauchy–Schwarz with the weight l exp(-r) gives the bound and the displayed field saturates it. This profile has finite kinetic norm and finite curvature energy, and smooth cutoffs approximate it in the form norm. A flat constant profile with the same nonzero period would have infinite kinetic norm. The profile derives a response to a trace imposed at the finite cut by allowing nonzero curvature in the end.

For matching tangential data the minimized quadratic energy is consequently

    E(p) = <p, [P/A_K + I/A_E] p> / (2 g6²).

Piecewise smooth minimizers with equal tangential trace are admissible in the curvature form domain: the distributional exterior derivative has no seam delta term. In collar gauge the normal component can be matched by a gauge change vanishing at the seam. The variational derivative with respect to the common trace is [P/A_K+I/A_E]p/g6². The two outward flux variations add with this sign because both positive quadratic forms are written in the same trace variable.

On a freely varying seam the sourceless equation forces p=0 for both backgrounds. Conditional on prescribed p, the identity core has P=I, and the parity core projects to 80 fibre-invariant E8 directions. Restrict the trace test to the matched base-invariant 134-dimensional space of 09f0c2617. P has ranks 134 and 78 respectively there. Thus the costs differ on exactly 56 directions by ||p||²/(2g6² A_K) for a vector wholly in that complement. This restriction selects allowed trace vectors for comparison on a fibre. The calculation does not solve the three-dimensional mapping-torus field equations or prove that every minimizing field is compatible with a base evolution. Both areas depend on the cut. The free solution has no cut dependence. A source fixed at a chosen cut would require a physical reason for its location and coupling.

## Why minimizing before linearization needs a separate check

At the identity-fibre history every differentiable small pair of handle holonomies starting at I has commutator I to first order. Nevertheless the nonlinear flat problem admits a branch with a prescribed small boundary holonomy and an interior variation of square-root order. Here is an exact example in a distinguishing direction of the base-invariant space. Take the canonical cyclic permutation B on the defining three. The Hermitian traceless Y=i(B-B†)/sqrt(3) commutes with B, has zero diagonal in the fibre sign basis and has eigenvalues +1,0,-1. Hence it is orthogonal to the fibre-invariant subspace and belongs to the 56-dimensional complement. Use an SU(2) subgroup acting on its +1,-1 eigenlines and leaving its zero line fixed.

Choose handle holonomies U=exp(i s sigma_x), V=exp(i s sigma_y) on that two-space. Conjugating sigma_y by U rotates it by angle 2s. Multiplying UVU^{-1} by V^{-1} gives half-trace cos²(s)+sin²(s)cos(2s)=1-2sin⁴(s). The commutator therefore has eigenangles ±2 arcsin(sin² s) for sufficiently small positive s. Simultaneous conjugation makes its axis exactly that of Y. For any sufficiently small theta>0 choose sin² s=sin(theta/2). The punctured fibre group is free on the two handles, so this gives a flat core with peripheral holonomy exp(i theta Y) and handle holonomies at distance O(sqrt(theta)) from I. Reversing the boundary orientation inverts the holonomy and changes no cost. In a chosen collar trivialization the tangential connection can be represented by theta Y dx (up to the common holonomy sign convention). The matching gauge loop extends into the core because SU(3) is simply connected.

Thus along this source direction the unrestricted nonlinear core can already attain zero curvature energy on the identity side. The positive Hessian cost on that side is the cost within differentiable first-order response. Treating it as a positive lower bound on the full constrained vacuum energy would give a false selection argument. This explicit escape applies to the fibre core. It leaves open whether the prescribed base return, a stationary source, matter backreaction or the physical end domain would allow the same handle path.

## Review scope

Check the adjoint projector and relative top-form argument, end weights and surface measures, the distinction between prescribing the seam and varying it, and the nonanalytic holonomy control. The earlier genus-one residue comparison and complete-cusp divergence are at 09f0c2617. The general relative boundary-form framework is discussed by [Al-Zamil and Montaldi](https://arxiv.org/abs/1004.2687). The specific projection and cusp profile above follow by Stokes and direct minimization. No independent scientific execution or review. No physical parameter earned.
