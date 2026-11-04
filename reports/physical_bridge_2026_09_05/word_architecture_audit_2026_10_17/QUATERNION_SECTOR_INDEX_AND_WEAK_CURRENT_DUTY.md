# The discrete sector's index and the separate weak-current duty

November 4, 2026. **UNREVIEWED author proof successor.** No scientific import, collection, CAS or tests. The new compact-resolvent proof and its underlying full-lift construction still await independent scrutiny.

Quantifier is the actual 128 physical coefficient sector of the coupled quaternion bundle on the specified complete one-cusp curve, restricted to any representation of its surviving gauge group. The result determines its Fredholm index. It does not count its finite kernels or the massive low-energy states, and it does not give a verdict about every architecture or weak chirality.

## 1. Reuse the full operator and the actual end

The [discrete-sector proof](CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md) reconstructs the complete four-slot mass map and proves compact resolvent on the reducing 128 block. Its angular coefficient is antiperiodic on every slot. Bounded zeroth-order homotopies of that operator keep the same domain and retain this end estimate.

The two spin fields have bundle B=S tensor F, det B=K. Here S is extending and F has quaternion peripheral -I2. Their combined coefficient in a cusp spin frame is periodic. The gauge coefficient bundle V in the 128 block has peripheral -I. Thus V, V tensor K and V tensor B are all antiperiodic in the relevant cusp frames. This is the actual new bundle, rather than the old model's spin-parity roster.

Fix an irreducible representation R of the surviving U3 gauge group and let V_R be its internal multiplicity bundle in the 128 block. The gauge connection and all background fields commute with that group, so this restriction is well-defined. The same argument also applies to the full block without representation restriction.

## 2. A bounded-end bundle comparison

There is a determinant-preserving smooth unitary bundle isomorphism

    J:B -> O direct-sum K                               (1)

which can be fixed in the periodic cusp frame. This is an analytical comparison. It is not a holomorphic splitting of B and not an identification of the supplied flat flavour transport with a newly selected physical gauge field.

Here is the extension argument. On a compact core with boundary prescribe the first unit vector of (1) in the end frame. A unit vector in a rank-two Hermitian bundle has fibre S3. Since S3 is connected and simply connected, the prescribed section extends over the one- and two-cells of that core. Smooth it while preserving the boundary data and its unit norm. Its orthogonal line is identified with det B=K by the fixed determinant map. This constructs (1) with its prescribed determinant and end behaviour. The choice of section is comparison data, not a selected vacuum.

The boundedness at the end is essential. In the holomorphic cusp frames B has metric Omega^-1 I2 and O plus K has metric diag(1,Omega^-2). An explicit local unitary determinant-preserving coefficient map is

    (u,v) -> (Omega^-1/2 u, Omega^1/2 v).                 (2)

Both sides have the same pointwise norm and determinant pairing. Since Omega=exp(-t), derivatives of the logarithms of the factors in (2) are constant in the canonical radial variable. Their induced connection difference is bounded in an orthonormal frame. The spin/flavour transition is periodic, so no additional angular winding is required in (2). The remaining connection difference on the compact core is bounded by smoothness.

Transport the original B connection by J. It and the direct connection on O plus K have the same determinant connection on K. Their difference is a smooth skew-Hermitian traceless one-form, bounded in the physical operator. Linear interpolation is therefore a unitary determinant-preserving bounded zeroth-order homotopy. Connections during this comparison need not stay flat or define stationary backgrounds.

## 3. Derive the four-slot index before counting modes

First scale both background Higgs fields to zero in the mass expression. They are bounded in orthonormal frames, so this is a bounded homotopy with the same 128 domain and coercive end. It is an index comparison, not a path of stationary vacua. The earlier source explicitly retains no extra fermion mass proportional to a nonzero auxiliary D moment.

Let chi(V) mean the L2 Dolbeault Fredholm index on the declared complete domain. At zero Higgs the scalar/form block of the actual mass map contributes

    -chi(V_R)-chi(V_R tensor K).                        (3)

The first term is the index of Dbar_(V_R) dagger on the connection/form slot. The second is the adjoint Dolbeault block on V_R tensor K, transported by the source volume-form map sigma=i Omega^2 lambda/sqrt(2). That actual map is what produces the Dz lambda row. It cannot be replaced by a second copy of the first term. The source's full physical proof derives this decomposition and its metric isometries. [Actual source operator](../weave_physical_mass_2026_10_08/PROOF.md)

The spin/flavour pair contributes chi(V_R tensor B). Its antisymmetric determinant pairing and the positive metric identify its target with the required trace-dual conjugate target. These are the same source maps with the two spin lines packaged in B. All four physical Weyl slots and both conjugate gauge sectors remain.

After (1)--(2) and the bounded connection homotopy, its index is

    chi(V_R tensor B)
      =chi(V_R)+chi(V_R tensor K).                      (4)

All three Dolbeault operators here are Fredholm. Their zero-angular obstruction is absent because the combined gauge coefficients are antiperiodic. Their canonically rescaled radial blocks have the same diverging angular bound as in the discrete-sector proof, with bounded connection and metric shifts. Their complete graph/adjoint domains are the source ones.

Adding (3) and (4) and restoring the bounded Higgs terms gives

    ind M_R = 0.                                       (5)

This is an all-lift, all-marking conditional index result for the stated sector and parent. It requires neither an explicit kernel basis nor a sampled coefficient matrix. It does not infer that either kernel is empty. It does not transfer an index from the old uncoupled cusp.

## 4. A discriminating old-parent control

If F is trivial at the cusp instead, B has the extending spin's antiperiodic transition, whereas O plus K is periodic. Matching those frames requires an angular half-winding. Its orthonormal derivative grows like exp(t), so the bounded-end comparison above is unavailable. This is where the argument changes, even though both bundles still have determinant K.

The old parent's actual formula 2J(1-beta)-J(-beta)-J(2-beta) can then be nonzero. At beta=1 its value is +1. That already-derived control is preserved. It prevents promoting det B=K alone, or a smooth splitting alone, into a universal zero-index theorem. The cusp connection and completed domains are load-bearing.

This proof also does not automatically extend to even-degree cusp pullbacks, where the 128 gauge antiperiodicity can disappear. Recompute Fredholmness and the full boundary comparison there.

## 5. A zero colour/electromagnetic index does not decide weak chirality

The actual surviving gauge group of this balanced branch is U3, with colour and electromagnetism. It does not include an unbroken weak SU2. Equation (5) is therefore a statement about those surviving representations. The physical mass proof interprets its index as the difference of left R and left conjugate-R zero-mode multiplicities.

For the observed Standard Model after electroweak symmetry breaking, the photon couples through the vector current Q psi-bar gamma_mu psi, while the W current contains the left projector 1-gamma5. Right-handed quarks and leptons are weak singlets before breaking. Those distinctions are explicit in the PDG's equations 10.2 and 10.6 and their surrounding text. I personally read the introduction and those equations on printed pages 1--3 of this edition. [PDG electroweak review](https://pdg.lbl.gov/2025/reviews/rpp2025-rev-standard-model.pdf)

Consequently (5) alone cannot distinguish a weak-chiral Standard Model phase from another theory with the same vector-like colour/electromagnetic charges. It also does not prove either. A zero index for a specified unbroken-SM representation would be a different and stronger constraint. This construction's actual group and operator must be used.

The next discriminant is the full charged kernel/low-mode spectrum together with the projected weak-current vertices and Higgs mass map of this same action. A weak generator that fails to preserve the background has an internal massive vector profile, whose equation and norm must be derived. Its action cannot be read from the unbroken gauge centralizer alone. The discrete 128 modes and the surviving continuum must both remain in that interaction calculation.

## 6. Input account

An independent guess of this sector's net unbroken-gauge index is removed conditionally by (5). No spin/flavour input or physical state has been identified away. J and its connection interpolation are auxiliary index tools and do not preserve every physical observable or the register along the comparison path.

The finite kernel multiplicities, their massive partners, chiral weak interactions, three generations, normalized parameters, continuum dynamics, parent selection and gravity remain open. No foundational row or measured parameter is certified paid. The result requires non-authoring review of the complete bounded-end and domain argument before acceptance.
