# Hostile audit: outside-bench memos 41-53

**Audit date:** 2026-08-26

**Immutable outside source:** `0fcdb66cd57edeb13c8703b7f05717fcc2609893`

**Method:** archive extraction, isolated certificate reruns and independent counterexamples

## Outcome

The certificates genuinely establish a coherent finite-dimensional representation package.  They
do not establish a selected four-dimensional fermion carrier, three physical generations, a
heterotic cup product or Yukawa values.  Two advertised uniqueness statements and the antiunitary
reading fail outright.

## Exact algebra that survives

- **OA-C1080 (`PROVED`).**  For the stipulated Riley lift,
  `kappa=tr[a,b]=1+q`, the beat sends it to `2-q`, and trace/norm/minimal
  polynomial/discriminant are `3`, `3`, `X^2-3X+3`, `-3`.
- **OA-C1081 (`PROVED`).**  The displayed Galois pair lies on the level-zero Fricke surface, is
  fixed by the stipulated trace action and is exchanged by the beat.  The selected fiber action
  has characteristic polynomial `X^2-3X+1`.
- **OA-C1084 (`PROVED`).**  The supplied E6 involution preserves the 27 isomorphism class and has
  adjoint trace `-2`; all 24 locked hits have the same trace class.
- **OA-C1085 (`PROVED`).**  The selected two principal-A1 slots give only even weights on 27 and
  78 and remain even under tensor products.  The selected minimal internal A1 has the contrasting
  `6*2 + 15*1` restriction.
- **OA-C1086 (`PROVED`).**  The chosen `Psi=C^2 tensor 27` is an exact 54-dimensional semilinear
  module.  Its relator, beat intertwiners and square-meridian identity pass.  The central lock is
  `+1` on 24 doubly-odd slots and `-1` on 30 others; the stated Jordan-depth and longitude
  identities also reproduce.
- **OA-C1088 (`PROVED`).**  Conditional on the hard-coded modules and bridge, the
  symmetry-restricted invariant chain is `6615 -> 4 -> 1`, with generator
  `epsilon_C2 tensor C_E6`; the frozen depth-support table is exact.
- **OA-C1089 (`PROVED`).**  In the chosen A2^4-in-E8 possibility space, the selected Chevalley
  trilinear factorizes after the stated sign gauge as `epsilon_family tensor C_Jordan` and has no
  same-family support.

All seven memo-47-through-53 outputs reran byte-identically.  These are exact representation
theorems in their recorded conventions.

## Refutations and newly exposed question

### OA-C1082 — the fixed locus is not only the conjugate pair (`REFUTED`)

For the memo's polynomial trace map, `(0,0,0)` is also fixed on the cusped Fricke surface.  It is a
genuine character: take

```text
U = diag(i,-i),  V = [[0,1],[-1,0]].
```

Then `(tr U,tr V,tr UV)=(0,0,0)` and `tr[U,V]=-2`.  The displayed pair is contained in the fixed
locus; it is not the whole locus.

### OA-C1083 — component identity (`OPEN`)

The equality `tr(ab^-1)=gal(kappa)` is checked at the selected point, not in the coordinate ring or
function field of the entire character component.  A component-level reduction is still owed.

### OA-C1087 — unique-minimal carrier (`REFUTED`)

`C^2` alone is a smaller beat-compatible holonomy module.  If a nontrivial internal 27 is imposed,
all eleven accepted odd A1 strata already satisfy the selected-beat identities.  The source gives
neither an admissible carrier category nor a minimization order.  The 54-dimensional carrier is
constructed and useful, but it is not canonically selected by the stated algebra.

### OA-C1090 — antiunitary real structure (`REFUTED`)

The operation is Galois-semilinear after choosing a complex embedding.  No positive Hermitian
metric is supplied, and its square is the nontrivial unipotent meridian rather than the identity.
A nontrivial unipotent cannot be unitary for a positive-definite Hermitian form.  “Antiunitary” and
“involutive real structure” are therefore false as typed.

## Why this is not yet a heterotic or Standard-Model Yukawa

The carrier certificates contain no compactification `X`, bundle `V`, Wilson projection, Dirac
zero modes, `H^1` groups, cocycle representatives, wedge/contraction, Calabi-Yau trace or matter
metric.  Consequently they construct neither of the physical BCDD maps

```text
H1(V) x H1(Lambda2 V) x H1(Lambda2 V) -> H3(O_X)
Sym2 H1(V) x H1(Lambda2 V*) -> H3(O_X).
```

The carrier tensor is antisymmetric in its two `Psi` slots, whereas the one-Higgs BCDD up map is a
symmetric cohomological map.  OA-C1055 independently proves that the actual same-monad,
one-`H_u` up map has rank zero.  Any proposed identification with the nonzero carrier tensor must
therefore map it to zero or explicitly leave an OA-C1055 hypothesis.

Likewise, the “three” in memo 53 is the dimension of an imposed external A2 triplet.  It is not
`dim H1(X,V)=3`, a chiral index, a Wilson-surviving family count or a physical generation theorem.
The existing OA-C0007, OA-C0008, OA-C0009, OA-C0014, OA-C0015 and OA-C0016 gates retain these
physics obligations without duplicating them as new algebra rows.

Memo 42 is a synthesis ledger, not independent evidence.  Its claims that all discrete bits are
paid and physical spin is resolved exceed the exact certificates and conflict with the still-open
selection and physics-interface gates.
