# The global chiral index on the product filling

19 November 2026. Follow-up to d36d50221. This calculation addresses the global domain on one filling. Let X be the compact figure-eight exterior truncated at a peripheral torus with a smooth metric made product near the boundary and flat on its cross-section. Let M=X×S¹ have the product metric, either spectator spin, and one boundary T³. Use flat coefficient bundles pulled back from X with unitary transport, the ordinary massless four-dimensional spin Dirac operator, and the APS spectral boundary sign of inward normal form ∂t+B. All these are physical/model hypotheses. The AGY-002 finite Fock checks do not specify them uniquely. M here supplies the *four-dimensional index problem*; an identification of its index with a multiplicity of particles in an external spacetime would require another map.

## Index including the harmonic trace

Allow strictly negative B eigenvalues for the positive-chirality operator D⁺. On each parallel coefficient summand the APS formula gives

    ind D⁺_< = ∫_M [Â(TM) ch(E)]_4 − (η(B)+h)/2,      h=dim ker B on positive-chirality boundary data.

This uses the actual dimensions of complex spinors, not the dimension of the full doubled boundary space. The local four-form here is zero pointwise: the twist is flat and the product metric has Levi-Civita curvature pulled back from X, where wedge products of degree four vanish. On the boundary the commuting holonomies are simultaneously diagonalizable. A spin-twisted Fourier mode has a real shifted momentum k and its two-component boundary Dirac matrix has eigenvalues ±|k| for k≠0. This holds even when the shifted lattice is not inversion invariant. Hence η(B)=0 by termwise cancellation in the convergent half-plane and continuation. If k=0 is allowed on n simultaneous internal lines, h=2n. The strict APS index is −n. Allowing an additional subspace of dimension j in ker B raises the index by j: quotienting the two domains gives exactly those j freely extendible boundary traces; the long exact sequence of kernels and cokernels gives this finite rank shift. This is also the elementary step between the two spectral-cut index conventions. [Atiyah, Patodi and Singer, Theorem 4.2 and its twisted form](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf).

For a parallel F-parity + sector the repair in d36d50221 allows the entire positive-chirality harmonic trace (j=2n); its index is +n. For a parallel F-parity − sector it allows none and the index is −n. Interchanging the assigned sign of χ reverses these two repaired indices. Nonzero spectral modes always use the same APS prescription.

| Flat coefficient choice and extending spin | n (internal parallel boundary coefficients) | strict APS chiral index | repaired chiral index |
|---|---:|---:|---:|
| Each parity of Λ*(five sheets), any extending spin | 0 | 0 | 0 |
| W25 tensor either sheet parity, any extending spin | 0 | 0 | 0 |
| Λ²W25 alone, periodic meridian and spectator | 12 | −12 | +12 with χ=Γ on the harmonic sector |
| Same exterior square, antiperiodic meridian or spectator | 0 | 0 | 0 |

The longitude is antiperiodic in all rows. The proof of each simultaneous character count is in the companion d36d50221. In the last control it is the *changing of boundary domain* that shifts the index by 24. Merely finding twelve odd internal vectors cannot decide the sign of a physical chirality. Even a nonzero index controls the difference of dimensions, not the full individual spectra, normalized currents or three copies of any specified charge representation.

## An independent pairing check for the sheet and single-companion rows

Write D=D_X+c_z ∂z in product frames, with c_z Clifford multiplication by the parallel unit vector along the spectator. The circle reflection lift on coefficient functions is Rψ(x,z)=ψ(x,−z) in the parallel spectator frame on its line cover. This is well-defined for either sign under z→z+period. All internal transitions, spin transitions along X, and the pullback connection commute with this coordinate substitution. The unitary map J=c_z R anticommutes with D and exchanges four-dimensional chirality: c_z anticommutes with D_X and Γ, and R anticommutes with ∂z. In an inward product collar, c_z also anticommutes with c(n). Therefore J commutes with B and preserves its spectral sign subspaces. This argument acts on sections; it needs no independent orientation-preserving spin lift of an orientation-reversing isometry on M.

In the first two rows h=0, so the full APS domain is self-adjoint, J-invariant, and has no harmonic trace choice. Every positive-chirality zero mode has a negative-chirality partner with the **same** internal state transformation under any parallel internal symmetry. J commutes with that symmetry. This gives equality as gauge modules, stronger than cancellation in the unweighted numerical index. It allows nonzero paired kernels. For h>0 with the χ harmonic choice, J interchanges K+ and K− at zero; using J to assert within-domain pairing in the third row would be an error. This sensitivity independently checks the exceptional row.

The scope is the smooth flat-twisted product action/domain. z-dependent masses, gauge fields with mixed curvature, changed spin or boundary actions, nonproduct fillings and distinct representations can change one or several steps; none follows just by reversing a finite grading. A future proposal should exhibit the term in the local density, boundary spectral asymmetry/harmonic domain, or breaking of J that changes the global index, and then compute it on the same charged domain. This result does not close chirality of the full programme. Independent review is owed for both the analytic formula and the grading conventions. No scientific code ran.
