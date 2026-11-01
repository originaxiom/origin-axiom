# Physical-family exact-control design

November 1, 2026. AFTER the author's analytical derivations, BEFORE
implementing, importing, collecting or executing these new controls.
This is verification design, not a prospective discovery claim, banked
identity or permission to run. The earlier proofs are UNREVIEWED.

## Quantifier, decision and prior

Finite exact controls for the source spin-parent parallel family,
physical metric factors, complete light roster, quantum coefficient
arithmetic and restricted/full-register distinction. The scripts cannot
certify global cusp PDE/domain hypotheses, the E8 component classification,
nonlinear matching, quantum compactification or a genesis-to-physics map.

Prior: the author expects the derived formulas to hold. All sixteen
named methods below must run exactly once and pass with no skips,
expected failures or incomplete population. A failed identity/control,
source mismatch or interrupted run is preserved and halts its claim;
no output is overwritten or silently repaired after viewing it.
Known positives and rejecting controls are included. Many arithmetic
identities are by-construction checks; a pass tests implementation,
not physical selection, novelty or independent input removal.

## Frozen conventions and existing sources to reuse

The actual action, Q0=E/2, H, real gauge tangent d=sqrt(2)k, full
E8 branching, SU5 hypercharge indices, complete kernel formulas and
modular period conventions are those of the four November 1 authored
notes and their cited original sources. The new module will not import
or rerun older scientific producers. Standard SymPy exact rational/
symbolic arithmetic is used, with the proposed research runtime declared
in ENVIRONMENT.json. No measured SM targets are read.

Use a rational spin-two frame E_(i+1,i)=4-i, F_(i,i+1)=i+1,
H=diag(-4,-2,0,2,4), positive Gram G_ii=1/binomial(4,i).
Adjoints use G; a literal transpose is not silently substituted.
J is the anti-diagonal alternating-sign principal-five Weyl matrix.
The compact quaternion units are i=diag(i,-i), j=[[0,1],[-1,0]], k=ij.
Marked Wilson pairs are (p,q) modulo one, modulo simultaneous sign only
where the full disconnected gauge action and its source frame apply.

## Sixteen intended methods, no additional hidden population

1. `test_principal_module_gram_and_chevalley_J`: reconstruct E,F,H,G,J;
   check brackets, weighted adjoints, trace relation, J^2=1 and the
   compatible Chevalley action. Identity Gram must fail the adjoint
   control. This does not compute all 248 E8 brackets or pi0(K).
2. `test_real_gauss_eigenline_and_scalar_vector_ratio`: reconstruct
   q=E/2,t=H/2; the real double commutator gives k†k t=t/2 and P_v t=t.
   Trace norms give 2N0/Z_t=1. Omitting sqrt(2) in d must fail.
3. `test_projective_orbit_metric_and_second_chart`: differentiate the
   normalized representative (1,c)/sqrt(1+|c|^2) in real coordinates,
   eliminate its actual phase connection, recover the Fubini--Study
   norm and its inverse chart. Omitting the response must fail at an
   explicit nonradial tangent. No closed CP1-only truncation is tested.
4. `test_shear_identity_and_heavy_exchange_controls`: check both actual
   antisymmetric superpotential terms under R->R+cQ. Check the positive
   massive-dressing polynomial and the rejecting zero-cubic model with
   nonzero quartic. This is finite algebra, not the nonlinear cusp IFT.
5. `test_complete_E8_principal_weight_population`: reconstruct all 240
   standard E8 roots and eight Cartans, derive principal H weights and
   subtract sl2 weight strings to obtain (24,11,21,11,1). This checks
   the full population; it is not the full group centralizer proof.
6. `test_complete_light_kernel_and_R_spin_control`: use the actual cusp
   pole bound and degree-zero spin/character test to assemble the full
   roster for order seven across four spins. Recover total chiral
   92+12kappa, vector12 and total R1 or R13 as appropriate. Dropping
   the principal R singlet must change the count.
7. `test_full_two_loop_matrix_and_weighted_row`: build T_a,C_a and copy
   populations from individual gauge blocks, recover b,B,wB and all
   three dimension-weighted off-diagonal checks. Omitting conjugates
   must change the matrix. Actual Yukawa overlap/nonrenormalization
   claims remain separate reviewed analytic duties.
8. `test_weighted_determinants_and_copy_frame_change`: derive c_r from
   the same index table; show cancellation for identical full ten/five
   metrics and the actual determinant transformation under a nonunitary
   copy-frame change. Wrong determinant multiplicity is rejected.
9. `test_harmonic_metric_period_covariance_and_scale`: derive the real
   period norm from the inverse flat conformal metric; check determinant
   one, L/R covariance with tau transported and the source g4/ell/g6
   coefficient relation. Wrong fixed periods under a move must fail.
10. `test_joint_SM_stratum_and_25_central_points`: enumerate the twenty
   gauge roots, checking BOTH holonomies. Recover gauge dimensions12 at
   the source,4 at an explicit generic pair,24 at all25 central pairs.
   A cycle-A-only test must fail on an explicit split cycle-B example.
11. `test_disconnected_torus_action_and_rank_four_control`: check the
   root-set inversion and all120 A4 Weyl permutations, whose restriction
   has trace>=-1 and never equals -I4. Check Chevalley reverses Y, so
   it is not in the old SM centralizer. Not a finite computation of the
   published E8 component count or its compact lift.
12. `test_uniform_roster_exceptions_and_order_four`: construct J[3],
   J[10] exactly, count108 in their union, cross-check full kernels on
   orders1..12 across all spins, and recover least allowed order4. This
   finite set supports the all-order proof; it is not an exhaustive
   computational search over every character.
13. `test_level_four_and_seven_orbits_and_axis_map`: exact finite
   L/R orbit of order4 and7, twelve/48 primitive pairs and six/24 after
   inversion. Derive both six-point permutations and intertwine them
   with the actual quaternion Ad(g_l),Ad(g_r) on signed axes.
14. `test_inner_register_rejects_quotient_map_extension`: derive
   abelian-character invariance under conjugation and Ad(i)j=-j.
   The generator-level full-register equivariance test must return
   false, while the Omega generator test of13 remains true.
15. `test_fixed_state_and_covariant_family_are_different`: exact
   marked-pair checks through denominators1..12 show only the trivial
   character is fixed by L and R, even modulo common inversion. Keep
   the nontrivial transported order-four packet as the positive control.
   The all-angle statement relies on its separate linear proof.
16. `test_order_ten_jump_and_order_seven_alias_scope`: reconstruct the
   extra mixed adjoint modes for eta=chi^5 at order10 and their beta
   insertion (10,6,4), still w-annihilated. Check the order-seven charge
   aliases and their explicit failure at order4. Zero h_C alone must
   not be reported as completeness of the same light roster.

## Implementation and execution boundary

Commit this design and runtime declaration before creating checks.py.
The implementation may be inspected with AST, source hashing and
metadata-only checks; do not import it, collect it or execute any test.
Seal its complete source/review inventory after implementation.

No direct-run command, runnable admission wrapper or main acceptance is
supplied by this design. Reusing an existing wrapper with a changed
binding creates engineering verification duties; an old fixture pass
is not that verification. Complete source/test/input/environment closure,
genuine independent review, main's separate acceptance and strict
prospective admission on a clean quiescent checkout remain necessary
before any scientific execution. Until then every method remains UNRUN.
Historical failures, prior seals and inherited staged work stay intact.
