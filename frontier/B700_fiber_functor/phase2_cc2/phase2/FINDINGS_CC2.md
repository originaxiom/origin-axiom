# FINDINGS — B700 phase 2 (cc2 half): the canonical torsor-iso, MTC leg

*Seat cc2 (read-only, advisory). Compute cell, exact symbolic computation only
(Sage 10.9, exact number-field / GAP-character-table arithmetic — no
float-only claims; every algebraic identity below was verified as an exact
equality in `QuadraticField(5)` / cyclotomic fields, not a numerical
approximation). Cites and answers **PREREG_PHASE2_CC2.md**,
sha256 = `7a9b113a475c7f2dd2f59adb91e1ffffc940a2a856d3c1c2191609a2b5309726`
(recomputed on the file as read; matches the seal in `SEALS.txt` byte-for-byte).*

---

## VERDICT

**MTC side: CANONICAL.**

φ₃ : {Fib, Yang–Lee} → U and φ₃ₐ : {weld order-10 orbits} → U are both
choice-free, both Galois-equivariant, and mutually compatible. The Yang–Lee
non-unitary sign does **not** inject an arbitrary (pivotal/braiding) choice:
it is *forced* — read directly off the modular S-matrix, which is itself an
invariant of the fixed braided/ribbon structure, and the only logically
possible source of extra freedom (a choice of spherical/pivotal structure)
provably does not exist beyond a single point for the golden fusion ring
(trivial invertible-object group ⇒ trivial pivotal-ambiguity torsor). All
three hard gates below are ✓.

**Scope flag (read before citing this as closing anything):** this cell
certifies only U (Part A) + φ₃ (Part B) + φ₃ₐ (Part C) + their mutual
compatibility. The **joint** 4-torsor verdict needs cc's half — φ₁ on
{the two golden 2-dim irreps of 2I} and φ₂ on the V₄ golden bit — plus a
cross-leg compatibility check (φ₁ vs φ₃ₐ in particular, since both live on
the same group 2I). That joint closure is **not done here** and is not
mine to close.

---

## PART A — the universal torsor U = Hom(ℚ(√5), ℂ)

Constructed `K = QuadraticField(5)`, `r5` a formal root of `x²−5` (abstract
generator, no sign privileged a priori). Sage computes `K.automorphisms()`
directly as `Hom(K, ℂ)` (since `K/ℚ` is Galois and totally real, every
embedding into ℂ lands in ℝ ⊂ ℂ and equals a field automorphism of K):

- Exactly **2** automorphisms: `id : r5 ↦ r5` and `σ : r5 ↦ −r5`. Call these
  `σ₊ := id`, `σ₋ := σ`.
- `σ² = id` exactly, `σ ≠ id` — Gal(K/ℚ) = ℤ/2 acting on U = {σ₊, σ₋} by
  left translation is **free and transitive**: a genuine torsor.
- No basepoint: the action has no fixed point in U (if it did, freeness
  would fail for the nontrivial element), so neither σ₊ nor σ₋ is
  distinguishable from the abstract field data alone. σ₊/σ₋ are just
  names for the two elements once ℝ's ambient order is used to read off
  which root of `x²−5` an embedding hits — that labeling convention is
  shared infrastructure, not a per-torsor arbitrary choice.

**Gate: U is a genuine 2-element free-transitive Gal-torsor — ✓.**

---

## PART B — the crux: Yang–Lee quantum-dimension sign

Golden fusion ring: `τ⊗τ = 1⊕τ`, fusion matrix `N_τ = [[0,1],[1,1]]`
(identical for Fibonacci and Yang–Lee — they share one fusion **ring**,
differing only in braiding/ribbon data S,T).

### B1. Frobenius–Perron dimension — canonical but blind

`charpoly(N_τ) = x² − x − 1`, exact roots in K: `φ = (1+√5)/2` and
`(1−√5)/2 = −1/φ`. Perron–Frobenius theorem picks out the **largest**
(automatically real, automatically positive) eigenvalue as FPdim, a
selection rule requiring no choice: `FPdim(τ) = φ` for **both** Fib and YL,
verified exactly — `FPdim(τ) == φ` is `True` in Sage, and this holds for
either category since `N_τ` is the same ℚ-rational matrix both times.
⇒ **FPdim is canonical (no ambiguity) but blind**: it is a constant function
on {Fib, YL}, hence cannot be the map to U (a constant map to one point of a
2-element free set is not equivariant unless trivial, and is certainly not
a bijection).

### B2. Categorical/quantum dimension from the S-matrix — canonical and distinguishing

Fibonacci's unitary modular S-matrix: `S = (1/√(2+φ)) · [[1, φ],[φ, −1]]`.
Verified exactly:

- `1 + φ² = 2 + φ` (exact identity in K, from `φ² = φ+1`) ⇒ row-0 of S has
  norm 1 exactly: `S` is a genuine unit-normalized (orthogonal) matrix.
- Numerator matrix squares to `(2+φ)·I` exactly (`Snum_fib² = (2+φ)I`,
  checked entrywise in K), confirming `S² = I`.
- `d_τ(Fib) = S_{0τ}/S_{00} = φ/1 = φ > 0`.

Yang–Lee's S-matrix is the Galois conjugate: apply `σ` (`√5 ↦ −√5`)
entrywise to the Fibonacci numerator matrix, giving
`Snum_YL = [[1, −1/φ],[−1/φ, −1]]`, normalization `2 + σ(φ) = 2 − 1/φ =
(5−√5)/2 > 0` (so the real square root exists — YL's S-matrix is real
orthogonal, `Snum_YL² = (2−1/φ)·I` exactly, same polynomial identity
Galois-transported). Then:

- `d_τ(YL) = σ(φ) = −1/φ = (1−√5)/2 < 0`, verified exactly, and
  **`d_τ(YL) = σ(d_τ(Fib))` holds as an exact equality in K** — this is the
  load-bearing equivariance fact (restated in Part C).

The categorical dimension is read **directly off the modular S-matrix** —
no pivotal/spherical choice enters its *definition* (S_{0i}/S_{00} is a
braided-categorical invariant, invariant under braided-equivalence, fixed
once the MTC's braiding+ribbon data is fixed). It **distinguishes** Fib
(`d_τ=φ>0`) from YL (`d_τ=−1/φ<0`), unlike FPdim.

### B3. Unitarity / pseudounitarity — intrinsic, no choice

Sharper-than-folklore check, self-contained from the data above (no
appeal to an external CFT realization needed): a fusion category is
**pseudounitary** iff `dim(X) = FPdim(X)` for every simple X under its
canonical positive spherical structure (Etingof–Nikshych–Ostrik). Every
unitary fusion category is pseudounitary (ENO 2005; EGNO *Tensor
Categories* ch. 9), so ¬pseudounitary ⇒ ¬unitary.

- Fib: `d_τ = φ = FPdim(τ)` — equal exactly ⇒ **pseudounitary** (consistent
  with the well-known fact that Fibonacci is realized as a genuine unitary
  MTC, e.g. as the even part of `(G₂)₁` / `SU(2)₃`).
- YL: `d_τ = −1/φ ≠ φ = FPdim(τ)` — **not** pseudounitary ⇒ **not unitary**.
  This is intrinsic to the category's own (S,T) data, requiring no further
  choice to detect.

### Why the sign is forced, not chosen (the actual resolution of the "load-bearing subtlety")

The one remaining worry is whether **within** a fixed braiding there could
still be *two* inequivalent spherical/pivotal structures, one giving
`d_τ=+FPdim` and another giving `d_τ=−FPdim`, making the reported sign an
artifact of which pivotal structure someone happened to pick. This is
ruled out exactly:

- Invertible objects of the golden fusion ring = objects with `FPdim = 1`.
  `FPdim(1)=1`, `FPdim(τ)=φ≠1` ⇒ `Inv(C) = {1}` (trivial group) — verified
  directly from the fusion matrix above.
- Distinct spherical/pivotal structures compatible with one fixed braiding
  differ by a monoidal natural automorphism of the identity functor, i.e.
  by an element of `Hom(Inv(C), {±1})`. With `Inv(C)` trivial, this group is
  trivial ⇒ **at most one** pivotal structure exists per fixed braiding for
  golden fusion rules.
- Hence, once "Fibonacci" vs "Yang–Lee" is fixed as a *specific* braided
  structure (which is exactly what distinguishes them as two different
  categories, not two presentations of one category), `d_τ` is **forced**,
  with zero remaining degrees of freedom. The apparent "choice" people worry
  about (categorical dim vs FP-dim) is not a choice available *within*
  either category — it is precisely the (Galois-conjugate) difference
  *between* the two categories, i.e. it **is** the torsor structure itself,
  not an obstruction to mapping it to U.

**Decision: φ₃(Fib) = σ₊, φ₃(YL) = σ₋ is CHOICE-FREE.** Gate (`d_τ(Fib)=φ`,
`d_τ(YL)=(1−√5)/2`, `FPdim=φ` both) — **✓ exactly**, all checked above.

---

## PART C — the weld map φ₃ₐ, equivariance, compatibility

### Independent verification of the weld's trace values (not just taking the prompt's word for it)

Computed the exact character table of **2I = SL(2,5)** via GAP (through
Sage): order 120, 9 conjugacy classes with representative orders
`[1,10,10,2,5,5,3,6,4]`, irrep degrees `[1,2,2,3,3,4,4,5,6]`
(`1+4+4+9+9+16+16+25+36 = 120` ✓, matches |2I|). The two 2-dimensional
("golden") irreps sit at GAP indices 2,3, and are mutually Galois-conjugate.
Their values on the two order-10 classes:

- irrep #2: `(−E(5)−E(5)⁴, −E(5)²−E(5)³)`
- irrep #3: `(−E(5)²−E(5)³, −E(5)−E(5)⁴)` (swapped — the Galois-conjugate irrep)

Both cyclotomic values satisfy `x²−x−1=0` exactly (checked in Sage), and
match `φ`, `(1−√5)/2` to full numeric precision, hence **equal them exactly**
(the two real roots of an irreducible-over-ℚ quadratic are distinguished by
sign, and the numeric match is unambiguous): `−E(5)−E(5)⁴ = (1−√5)/2 = −1/φ`,
`−E(5)²−E(5)³ = φ`. This **independently confirms**, from the finite-group
character table alone, exactly the claim in the prereg/prompt: fixing the
golden irrep #2, its two order-10 conjugacy classes carry traces `−1/φ` and
`φ`. (Sanity cross-check via `SU(2)` half-angle trace formula: order-10
elements lift order-5 icosahedral rotations, trace `= 2cos(π/5) = φ` or
`2cos(3π/5) = −1/φ`, both verified as exact symbolic identities in Sage —
`2cos(π/5)`, `2cos(2π/5)`, `2cos(3π/5)`, `2cos(4π/5)` simplify exactly to
`φ, 1/φ, −1/φ, −φ` respectively.)

### φ₃ₐ definition and choice-freeness

`φ₃ₐ(orbit) = σ₊` iff the orbit's trace `= φ`; `φ₃ₐ(orbit)=σ₋` iff trace
`= −1/φ`. Trace of a group element in a fixed representation is a
basis-independent, conjugation-invariant scalar — no choice enters.
**Choice-free — ✓ confirmed** (and independently re-derived above, not
merely asserted).

### Galois-equivariance (hard gate, both maps)

- **φ₃**: `d_τ(YL) = σ(d_τ(Fib))` exactly (`−1/φ = σ(φ)`, verified in K
  above). Applying Galois to the modular data of the golden MTC (entrywise
  conjugation of S) is exactly the standard "Galois symmetry of modular
  data" (de Boer–Goeree; Coste–Gannon; Bantay) restricted to this rank-2
  case, and it **swaps Fib ↔ YL while swapping σ₊ ↔ σ₋** — `σ∘φ₃ = φ₃∘swap`
  holds as an exact algebraic identity, not merely a numerical coincidence.
- **φ₃ₐ**: `σ(φ) = −1/φ` and `σ(−1/φ) = φ` exactly ⇒ applying σ to the
  trace-label swaps which of the two order-10 classes is assigned to σ₊ vs
  σ₋. Since φ₃ₐ's Galois-module structure on {weld orbits} is *defined*
  through this trace-labeling in the first place, equivariance here is
  immediate by construction (the prompt correctly flags this leg as the
  easy one) — but it is not vacuous: it fixes the labeling scheme
  concretely and lets it be compared, value-for-value, against φ₃.

**Gate: both maps Galois-equivariant, `σ∘φ = φ∘swap` — ✓ exactly, for both.**

### Compatibility (MTC side)

`φ₃(Fib) = σ₊` because `d_τ(Fib) = φ` **exactly** (the literal algebraic
number `(1+√5)/2`). `φ₃ₐ(class trace-φ) = σ₊` because that class's trace is
the same literal number `φ = (1+√5)/2` — not merely "both happen to be
positive," but the identical element of K. So the composite
`φ₃ₐ⁻¹∘φ₃` sends Fibonacci ↦ the φ-trace weld orbit, **not the swap**.

This is more than bookkeeping: both `φ` values trace back to the same
underlying trigonometric arithmetic at the 5th root of unity (Fibonacci's
`S_{0τ}/S_{00}` and the icosahedral spin-rep trace both reduce to
`2cos(π/5)`-type data over `ℚ(√5)`), which is why the check is non-circular
— a sign error in either definition (e.g. mixing up `φ` with `1/φ` or `−φ`)
would have been caught by the exact-value comparison, not papered over by
"both are positive."

**Gate: φ₃, φ₃ₐ compatible (same bijection to U, not off by the swap) — ✓
exactly.**

---

## Hard-gate checklist (from PREREG_PHASE2_CC2.md falsifiers)

| Gate | Status |
|---|---|
| U is the genuine 2-element Gal-torsor (2 embeddings, freely permuted) | ✓ |
| `d_τ(Fib) = φ`, `d_τ(YL) = (1−√5)/2` exactly; `FPdim` of both `= φ` (positive) | ✓ |
| `φ₃`, `φ₃ₐ` Galois-equivariant: `σ∘φ = φ∘(torsor-swap)`, verified exactly | ✓ |
| Compatibility: `φ₃`, `φ₃ₐ` induce the same U-identification (not swap-off) | ✓ |
| Pivotal/braiding-choice obstruction named and ruled out (`Inv(C)` trivial) | ✓ (ruled out) |

---

## Base-rate / triviality gate

"All ℤ/2-torsors are abstractly isomorphic" is **rejected as content** —
that fact is automatic and carries zero information. The actual content
established here:

1. **FPdim** is the canonical-but-blind invariant: well-defined with no
   ambiguity (Perron–Frobenius selection), constant across {Fib,YL}, hence
   *useless* for building a map to U — this is exactly the trap the
   base-rate gate warns about (an invariant can be "canonical" in the weak
   sense of unambiguous and still carry no distinguishing content).
2. **Categorical dimension** (from the S-matrix) is the invariant that
   actually distinguishes the two torsor elements, and it is canonical in
   the strong sense: it requires no pivotal/spherical/braiding choice
   beyond the braiding that already defines "Fibonacci" vs "Yang–Lee" as
   distinct objects, because the group of possible extra pivotal choices
   (`Hom(Inv(C),{±1})`) is *proved* trivial for this fusion ring (not merely
   assumed).
3. **Unitarity/pseudounitarity** is an intrinsic, self-standing property
   (`dim = FPdim` object-by-object) that independently confirms which side
   is which, with no reference to U at all — Fib passes, YL fails, exactly
   and unconditionally.

All three cohere exactly (φ for Fib matches FPdim and is positive/
pseudounitary; `−1/φ` for YL is the Galois conjugate, differs from FPdim,
and is non-pseudounitary/non-unitary), and the weld's independently
GAP-verified trace data matches the same `φ`/`−1/φ` split with the same
sign convention. **Choice-freeness holds** on the MTC leg: stated plainly,
yes, φ₃ and φ₃ₐ are canonical.

---

## What is NOT closed here

The **joint** verdict across all four torsors — {irreps of 2I} (cell 1),
{Fib,YL} (cell 3, this cell), {weld orbits} (cell 3a, this cell), and the
golden bit of V₄ = Gal(ℚ(√−3,√5)/ℚ) (cell 2) — requires cc's half (φ₁, φ₂)
and a full cross-leg compatibility matrix (in particular φ₁ vs φ₃ₐ, since
both concern the same group 2I, and φ₂ vs the rest). **That closure is
explicitly out of scope for this cell** and is flagged here rather than
assumed. This cell certifies: U (Part A), φ₃ canonical (Part B), φ₃ₐ
canonical (Part C), and φ₃/φ₃ₐ mutually compatible (Part C) — the MTC leg
only.
