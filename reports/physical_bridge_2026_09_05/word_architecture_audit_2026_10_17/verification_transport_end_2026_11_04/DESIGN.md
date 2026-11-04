# Full compensator and cusp controls

November 4, 2026. Prospective implementation design, written before its new source exists. The analytical proof was already inspected and drafted. This is neither a blinded experiment nor a complete scientific admission specification. No measured quantity, optimization, random seed or fitted physical target enters these controls.

The candidate comprises `FULL_E8_COMPENSATOR_LIFT_AND_REGISTER_TRANSPORT.md`, `COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md` and `PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md`. Tests support their algebra and local operator calculations. Their universal geometric/spin action, self-adjoint graph law and singular-sequence argument retain separate analytical-review duties.

## Declared conventions

- Source D5 vector basis and positive compact adjoint from the existing register/flavour checks. First-five Cartan weights are `(-4,-2,0,2,4)` in the source order.
- E8 roots from the existing complete neutral-family source. Retain all integer and half-integer roots and all eight Cartans.
- `A_vec=(-iN)exp(-i pi H/4)`, `D_vec=exp[-i pi(H_+-H_-)/4]`, `B=DA`, and rightmost-first group multiplication.
- Full Spin10 torus logarithm `x=(1/4,0,-1/4,-1/2,-3/4)`. A second lift is a separately recorded sign, not selected from numerical success.
- The existing A3 electromagnetic Cartan has four weights `1,-1/3,-1/3,-1/3`, and `h=exp(3 pi i Q_em/4)` is the candidate coherence correction.
- The source physical fermion slots and densities are `(lambda,a,u,v)` and `(Omega^2,1/2,Omega,Omega)`. Both flavour fields and every transpose coupling remain.
- The compactified spin extends through the puncture. The two compared flavour peripherals are -I2 for the quaternion construction and I2 for the commuting rotation control. The actual complete cusp and its unbroken gauge generators are hypotheses.

## Eight required controls

1. `test_full_root_central_phases_and_electromagnetic_lattice`
   Reuse the full E8 root generator, compute torus pairings exactly, and reconstruct the Zeta fixed/odd populations including Cartans. Check A^4 on every root and the equality h^2=C^-1 using independently constructed first-three versus last-five logarithms. Omitting the half roots must lose a nontrivial fourth power. Include a wrong electromagnetic phase that fails on actual mixed weights.

2. `test_actual_clifford_lift_of_d5_compensators`
   Reconstruct the existing ten-dimensional E,G,H and the two triples. Build creation/annihilation matrices on the 32-dimensional exterior algebra. Define the D5 spin map from the actual A/B/C Lie blocks, retaining both chiral halves. Check its Clifford covariance and compact adjoints before exponentiating. Obtain the D exponential by exact spectral-polynomial calculus, and A from its half-weight torus phases. Check A^4=Zeta, D^2=Zeta P, B^2=C^-1 P, (AB)^2=P and [A,B]=Zeta P on the spin representation as well as the vector representation. A comparison only on the D5 adjoint is insufficient.

3. `test_faithful_compensator_group_and_quotient_kernels`
   Enumerate the exact subgroup using the actual vector-plus-spin matrices. Compare its multiplication with an independently implemented C4-by-C8 inversion presentation. Check the full, vector and D5-adjoint quotient kernels. Determine the squares of order-four vector elements and explicitly reject the Q8-times-C2 label. Group order alone cannot assert group type. Preserve all four independent Spin10 core-lift sign combinations.

4. `test_full_pin2_correction_and_retained_gauge_sectors`
   Use the 45,15,10-by-6,16-by-4 and conjugate module actions to check the corrected reflection and rotation relations, including every central phase. Compute the quaternion subgroup's order and verify its joint action fixes the actual balanced D5 pair. Verify commutation with the old colour/electromagnetic algebra and Wilson holonomies. The scalar and spinor sectors must agree with their separate full-root phase check.

5. `test_continuous_stabilizer_and_phase_constraint`
   Reuse the source quartic polynomial and derive the symbolic Pin2 rotation/reflection invariance. A rotation taking the x axis to y must fail the fixed-state polynomial check. Express the phase condition using `t=exp(2i theta/3)` and verify the exact simultaneous equations, including a rejecting root. Check the two residual values in the faithful electromagnetic circle and their distinction on retained matter. No phenomenological phase or modulus is supplied.

6. `test_based_and_all_word_holonomy_covariance`
   Reuse the existing free-word conventions. For L,R, inverse moves and natural inner operations, compare precomposition by phi^-1 with the actual flavour action and full gauge representation. Include compositions and the word a^4, whose flavour image is trivial but whose bare full E8 lift is Zeta. A wrong composition order must fail. These finite controls support the all-word proof, not a chosen coherent geometric/spin lift over the universal family.

7. `test_stationary_gluing_and_full_peripheral_table`
   Reuse both source triples and reconstruct every F/moment residual and physical norm. Check both bare and corrected coupled transitions and the old order-three Wilson compatibility. Compute the combined peripheral transition independently on each physical slot and every E8 sector. Retain the quaternion and commuting-rotation controls. Incorrectly leaving Q unrescaled when adding R must fail its moment equation.

8. `test_actual_centralizer_mass_and_escaping_channel`
   Start from the full source mass formula and project only after proving that the chosen gauge direction commutes with q,r and their adjoints. Retain lambda,a,u,v in the source and trace-dual target. Compute the zero-angular radial spin block after the actual Omega rescaling. Check the canonical dt norm, derivative norm scaling for an explicit compact H1 bump and the effect of a vanishing tail perturbation. The antiperiodic comparison must reject the same zero-angular ansatz. These calculations support the analytical Weyl sequence and cannot certify the entire domain theorem or a physical zero-mode count by themselves.

## Reuse and execution requirements

Reuse the D5 reconstruction and full mass comparator from `verification_register_flavour_joint_2026_11_03/checks.py`, and the full E8 roots from `verification_neutral_full_kernel_2026_11_02/checks.py`. If an import would run unrelated science at module load, extract only a reviewed, source-pinned reusable definition in a separately declared successor. Preserve the sealed source bytes and historical outputs.

Before implementing, commit this design and the proof/source inventory. Before scientific import, collection or execution, complete the source closure, environment and wrapper validation, independent proof/code review, main's exact separate acceptance and the strict prospective gate. No earlier package or received external run substitutes for those duties. Any needed design correction receives a dated amendment before its implementation and run.
