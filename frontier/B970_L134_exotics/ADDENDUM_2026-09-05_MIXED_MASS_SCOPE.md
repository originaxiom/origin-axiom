# Direct mass entries and physical heavy states are different questions

2026-09-05, physical-bridge audit R4. This is a new scope note; the original
B970 code, outputs, scout and WORK are unchanged.

B970 correctly derives that the **fixed** 5_10 times 5bar_10 mass entry in
the cubic needs the scalar direction S, with psi=4 and chi=0. B970 also
correctly records that the 27 contains two SM-indistinguishable 5bars.

Those two facts must be used together when naming a *physical* heavy state.
The banked 16·16·10 cubic also permits the N singlet in a scalar 16 to mix
5_10 with 5bar_16. R4 rebuilds the cubic directly from B883's representation
and contracts it with s S+n N. Both pure S and pure N give exact mass-matrix
rank 10; the general triplet/doublet blocks satisfy

```text
M_D M_D^dagger=(|s|^2+|n|^2) I3,
M_L M_L^dagger=(|s|^2+|n|^2) I2.
```

Thus a pure N can make one complete vectorlike multiplet heavy, while the
originally named exotic 5bar becomes the light chiral 5bar. It does not give
the original fixed 10·10 entry a mass, contradict charge conservation, or
produce triplet/doublet splitting. The statement "S is unique" must retain
its **direct-entry** scope, rather than excluding this already-allowed mixing.

R4 also supplies a particular bounded classical scalar potential and checks
its full Hessian. The minimum reaches the SM algebra but retains eleven
non-gauge scalar zero modes; it is not a completed physical model.

Proof, inputs, executable certificate and remaining work:
`reports/physical_bridge_2026_09_05/VACUUM_MODEL.md`, `vacuum.py`, and
`tests/test_physical_bridge_vacuum.py`. No observed mass was used or predicted.

**R5 follow-through (same date):** the complete, kinetically normalized one-loop
angular potential now gives positive leading mass-squared corrections to all
eleven octet/triplet modes on the common-quartic ray. Independent analytic
derivatives agree; exact polynomial identities make angular differences
scale-independent. The tree-level zero modes above remain true at tree level,
not a quantum failure. Global selection and the light Higgs are still open.
Source: `reports/physical_bridge_2026_09_05/QUANTUM_VACUUM.md`,
`tests/test_physical_bridge_quantum_vacuum.py`, and
`tests/test_physical_bridge_quantum_derivative.py`.

**R6 follow-through:** the full leading normal quantum shift is now solved,
with all 186 force components and the nine physical SM-singlet normal
directions accounted for. The reference scalar shifts are 14.9%, versus
3.72% and 0.930% in the predeclared weaker-coupling controls. All preserve
the SM action. The independently checked normal-shift identity confirms
that R5's positive angular curvatures already include this correction;
adding it twice would be a false kill. Scope and remaining obligations:
`reports/physical_bridge_2026_09_05/QUANTUM_SHIFT.md` and
`tests/test_physical_bridge_quantum_shift.py`.
