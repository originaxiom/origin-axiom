# Recovered steps, not reset gaps — 2026-09-06

Source-and-rerun receipt for the owner's four-force table and old/new-result
sweep. No old producer is changed. The answer's unqualified 14-versus-12
warning lost the distinction between an intermediate algebra and its known
rank-reducing completion.

## The 14 to 12 reduction exists

B992 establishes that the Levi's three abelian directions span Y, chi, psi.
B970 WORK §1 derives the charges from the Cartan matrix: S has (Y,chi,psi)
=(0,0,4), N has (0,-5,1). Nonzero separate S/N VEVs leave aY+b chi+c psi
unbroken only if 4c=0 and -5b+c=0. Thus only Y remains. Color and weak
generators annihilate both singlets. B1025 §I5 further narrows the directions
to multiplicity-one lines **given the embedding chain**; the act and
magnitudes are not thereby derived.

R4's later, explicitly chosen scalar potential realizes this completion at
an actual global classical minimum: the full compact stabilizer of S, N and
adjoint Y is the span of the actual 12 SM generators. Its competing minimum
and radiative successors remain in VACUUM_MODEL.md, QUANTUM_VACUUM.md,
QUANTUM_SHIFT.md and HIGGS_SECTOR.md. Existence, selection, order of
approximation and physical identification are separate questions.

The alternative A1 route also has a rank-reducing singlet: codex R038,
independently banked in B1238. Its producer was rerun: stabilizer in su6 alone
24/rank4, in su6+su2 25/rank5; X acts with norm 1, Y with norm 0; the surviving
diagonal combination has norm 0; moment-map norms 5/6 and 1/2. The extra
gauged-su2 reading is not interchangeable with the holonomy-centralizer
reading. No SUSY D-flat vacuum follows from this single VEV.

## Other positive/superseding results

- B1102 completes B1100's exact hypercharge match with 18 rational directions.
  None commutes with a full color su3 at that A2 landing. The rank-four
  existence theorem survives; the histogram is not a full SM product.
- B1134 constructs Lorentz plus compact color with one real structure; its
  stated family has 24 successful pairs. B1127's earlier compact-color
  computation was independently rerun during the four-force check (4/48).
  The B1134 sweep was read here, not freshly rerun in this receipt.
- B1141 selects the SL2 lift by beat consistency. B1145 closes that beat on
  the A1 27 exactly. Both complete producers were freshly rerun. This is
  internal algebraic closure, not an earned 4d spinor/Dirac/index map.
- B980 already withdraws the claimed 122-order cosmological-constant miss:
  the anyon level was identified with a gravitational level without a
  derivation. This withdraws a false negative; it does not predict Lambda.
- B864's one-dimensional anomaly cone is for the 15 without nuR. Adding
  the derived nuR restores the anomaly-free Y/chi plane. Keep the full
  matter content when invoking uniqueness. The standard embedded trace
  ratio is not arbitrary; physical electromagnetic identification is distinct.
- The 64's lack of invariant **vectors** is not a lack of invariant
  **functions**: B1140's own complement contains a vector with Killing
  norm 36. Its spin-two representation slots are not a derived graviton
  action. These were checked directly during the four-force audit.

## Search population and run receipts

Fetched main through 8bccf659 for the rank sweep; nine local/remote heads
enumerated by absence_sweep.py with regex
`(14.{0,8}12|rank.reduction|two.seeds|rank.reduc)`: PRESENT on all nine.
Deleted matching **paths**: zero; not an exhaustive deleted-content search.
Additional git-log subject/content searches found the older R038 relay and
ab96bd3b's existing reconciliation. Already-banked hits were read as pointers,
not proofs. No repository-wide absence claim follows.

At local 390e9cad (only the prior generated REVIEWER view dirty):

```text
python3.12 -m pytest tests/test_b1025_audit.py tests/test_b1092_purity_selector.py tests/test_b1098_nonabelian_hatch.py tests/test_b1102_exact_solve.py tests/test_b1236_a1_landing_exact.py tests/test_physical_bridge_vacuum.py tests/test_physical_bridge_vacuum_orientation.py -q -p no:randomly
23 passed in 48.86s

OA_SLOW=1 python3.12 -m pytest tests/test_b1141_spin_payment.py tests/test_b1145_sp2_fermion_seat.py -q -p no:randomly -k reproduces
2 passed, 13 deselected in 26.21s
```

Both used OPENBLAS_NUM_THREADS=1 and OMP_NUM_THREADS=1. These are transcribed
terminal receipts, not manufactured raw logs or a full-suite certificate.
B1025's lock uses supplied branching counts; R4's separate live matrix
checks supply the stronger action/stabilizer evidence.

The next fetch reached 9a79adfd. Its new chirality addenda withdraw the
SL2-cohomology-as-chiral-generations reading and register I-26. Mathematical
candidates must not be relabelled physical generations here. The new upstream
windows were read, not merged/certified by this receipt; the physical action
remains pinned to its own producers.
