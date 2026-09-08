# R20 basis-transfer control: exact automorphisms saturate the certified group

2026-09-08. Post-failure design, sealed before this control executes.

BANKED IDENTITY: R20 seal 72e40d9c stopped because Q and its canonical
retriangulation K have no direct combinatorial isomorphism. Original
source/tests/failure remain immutable. Physics R72b (659487bb) already
records r:(a,b)->(b,bA) and s:(a,b)->(a,aB), as well as the order-three
map. Use these actual maps, not newly guessed ones.

PRIOR ART: Prasad, Strong Rigidity of Q-Rank 1 Lattices, Theorems A/B,
https://doi.org/10.1007/BF01418789; original pp.255--257 read at
https://www.maths.gla.ac.uk/~mpowell/Prasad-on-Mostow-rigidity.pdf
on 2026-09-08. Applied to PSL(2,C), this realizes outer automorphisms
of a complete finite-volume hyperbolic 3-manifold group by isometries.
SnapPy's verified canonical/combinatorial APIs are already read and
cited in the original design.

P0/P1/P4: SAME scalar-holonomy source model and global forms, PB-BOUNDARY.
No changed physical ansatz, expected character spectrum, tolerance or
original mathematical test. Only the geometry-to-H1 certification route
changes. P6: expect the two explicit word automorphisms to generate
twelve distinct H1 actions and saturate the verified isometry group.
If a word map or saturation fails, preserve that result; do not guess
a replacement from the desired character answer.

New lower/upper proof, with no basis transfer assumption:
- Verify r and s are FREE-GROUP automorphisms using explicit inverses
  r^-1:(a,b)->(Ba,a) and s^-1:(a,b)->(a,Ba), both directions.
- Verify each sends the actual relator to a freely conjugate copy
  of R or R^-1. The induced maps are actual automorphisms of pi1(Q).
- Generate r^k s^e, 0<=k<6, e=0,1. Verify the same relator property;
  their twelve distinct integral H1 matrices prove twelve distinct
  OUTER classes, since inner automorphisms are identity on H1.
- Canonical retriangulation with verified=True at both requested
  precisions independently counts exactly twelve self-isomorphisms.
  Rigidity plus equality of the lower and upper counts certifies the
  ENTIRE H1 action, already in the original a,b basis.
- Independently inspect the canonical cusp actions for orientation,
  the normal order-three subgroup and its fixed endpoints. Require
  distinct cusp-action descriptors before using their orders.
- As a separate control, numerical symmetry enumeration in the
  original triangulation and exact two-cusp homology equations must
  return the SAME twelve H1 matrices. Do not call this secondary
  peripheral table itself interval-certified or use it to certify
  the word actions. Record that distinction in the output.
- Keep verified m004 count eight as the comparator.
- Apply the UNCHANGED original character/cohomology/parent-lift
  functions to the exact word-action set. Direct new assertions
  cover their mathematical values and the new lower/upper proof.
  The six failing original geometry-dependent tests are retained.

This recovers the original complete-action target; it is not a
smaller passing subset. No full-source dynamics or global vacuum
selection is inferred. No tree edits during any live run.
