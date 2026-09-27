# Deck descent: distinguish holonomy from the geometric action

2026-09-27. Local audit follow-through, input a1bea799; no shared B/I number.
F20 remains unexecuted. This cell is a scope check prompted by B1384 at
9f9a0751, not a new M6 cohomology census or a physical generation claim.

## Question and prior

B1384's actual producer sets T = (Ind V)(a^2) and verifies
T^3 = (Ind V)(a^6), sometimes nontrivial unipotent. This is a holonomy
matrix on one fibre. Does it exclude an honest order-three deck action
on the full pulled-back bundle without semisimplifying V?

Prior: NO. A bundle pulled back from the quotient has a canonical deck
action. The total-space action includes movement of the base and the
bundle's transition identification; its cube is identity even when
the chosen same-fibre holonomy matrix has nontrivial cube. The proof
must retain the nonsplit monodromy and distinguish both operations.

This qualifies a possible broad reading of “strict C3 after
semisimplification.” It does not refute B1384's displayed matrix identity,
its Shapiro/Mackey calculation, or its explicit physical-generation fence.

## Prespecified exact checks

Use a circle with degree-three cover solely as an instrument control.
Start with rank-two monodromy M=[[1,c],[0,1]], c=1,-2, and the rank-six
induced companion T with blocks (1,0)=I, (2,1)=I, (0,2)=M. Thus
T^3 = diag(M,M,M). Also use the split c=0 control.

1. Check the cube and inverse exactly; for c nonzero its nilpotent
   remainder is nonzero and square-zero. Preserve it throughout.
2. On three fibres around the covering circle represent the true action
   by blocks T,T,T^-2. The seam factor T^-3 supplies the last block.
   Check the 18-by-18 action cubes to identity.
3. The seam-omitted mutant has T in all three blocks and must NOT cube
   to identity for the nonsplit controls. Split control must distinguish
   this phenomenon: both cubes are identity when c=0.
4. The true averaging projector must be idempotent of rank six.
   Naively averaging the same-fibre T must fail idempotence for c nonzero.
5. Circle cohomology: ker(T-I) has dimension one and ker(T^3-I) dimension
   three for c nonzero (two and six in the split control). On the latter
   kernel T induces a strict order-three action; its invariant subspace
   has the downstairs dimension. H1 has the same dimensions on the circle.
   These are NOT M6's numbers and this toy's Euler characteristic is zero.
6. Verify determinant-one and exact invertibility. No floating tolerance,
   semisimplification of the nonsplit controls or fitted coefficients.

## Execution and stopping

Seal this design, proof, producer, tests and branch-intake assessment
with hashes and exact Git source pins. Commit locally before any import
or execution. Do not push. Keep science read-only until native and
focused tests have terminal exits. Preserve first failures and seal
corrections separately. No full-repository regression is needed: the
instrument imports only SymPy, not repository science; do not claim one.

If any expected identity fails, stop promotion and record the failure.
Finite matrices are controls for the general written construction, not
a substitute for its proof or for M6's physical operator/domain analysis.

## Source and novelty scope

Personally read B1384 FINDINGS and induction code (including T assignment),
B1378 FINDINGS and the local F01 scope correction. Relevant phrases were
searched in the SM branch's frontier/docs/philosophy/papers surfaces;
this is not a semantic absence or whole-history novelty certificate.
P022 is motivation, not a mathematical premise.

The Stacks Project, definition 35.2.3, was read in HTML for the standard
term “canonical descent datum” (https://stacks.math.columbia.edu/tag/023D).
It concerns quasi-coherent sheaves on schemes; it is NOT imported as a
theorem about the present smooth flat bundles. PROOF.md gives the needed
topological construction directly. No paper or PDF is claimed fully read.
