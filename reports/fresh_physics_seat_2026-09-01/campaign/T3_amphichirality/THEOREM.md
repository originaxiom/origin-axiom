# Amphichirality of orientation double covers — theorem, corollary, and the honest edge

Cell T3, outside evaluation seat, 2026-09-01.
Everything below is orientation-convention-explicit (E23 discipline); conventions are
collected in §4. Gate 5: no measured physical value appears anywhere in this document.

---

## 1. Definitions and the one subtle point, up front

Throughout, a **hyperbolic 3-manifold** means a complete finite-volume Riemannian
3-manifold of constant curvature −1 (cusps allowed).

**Amphichiral** (the sense used here and throughout this campaign): an *orientable*
hyperbolic 3-manifold `M` is amphichiral if it admits an **orientation-reversing
self-isometry** — equivalently, if `M` and its mirror `−M` (same manifold, opposite
orientation) are isometric by an orientation-preserving isometry. By Mostow–Prasad
rigidity this coincides with the topologist's notion (orientation-reversing
self-*homeomorphism*): any self-homeomorphism is properly homotopic to an isometry, and
the homotopy preserves the orientation behaviour. So no strength is lost or smuggled in
by working with isometries.

**Orientation double cover**: for a non-orientable manifold `N`, the connected 2-fold
cover `p : Ñ → N` corresponding to the index-2 subgroup
`ker(w₁) ≤ π₁(N)`, where `w₁ : π₁(N) → ℤ/2` is the first Stiefel–Whitney
homomorphism (a loop maps to `1` iff it reverses local orientation). Since `N` is
non-orientable, `w₁` is surjective, so `ker(w₁)` has index exactly 2 and `Ñ` is
connected. Concretely, `Ñ` is the space of pairs `(x, ω_x)` with `x ∈ N` and `ω_x` a
local orientation of `N` at `x`; the nontrivial deck transformation is

> `σ : (x, ω_x) ↦ (x, −ω_x)`,

a free involution with `Ñ/σ = N`. `Ñ` is orientable (its fundamental group is exactly
the orientation-preserving part), and it carries **two** orientations, exchanged by
nothing canonical — a fact this seat's A6 verdict leans on and which we do not need
below, but state for hygiene: *nothing in this cell chooses a sheet*.

**The subtle point, stated before it is used.** "The deck involution is
orientation-reversing" is not a definitional triviality — a deck transformation of an
orientable cover is a diffeomorphism and could a priori preserve orientation (the deck
involutions of ordinary 2-fold covers of *orientable* manifolds usually do). What forces
reversal here is precisely the non-orientability of the base, via the descent argument
in the proof: **an orientation invariant under the full deck group would descend to an
orientation of the quotient.** We give that argument in full.

---

## 2. Theorem A

> **Theorem A.** Let `N` be a non-orientable finite-volume hyperbolic 3-manifold and
> `p : Ñ → N` its orientation double cover, with nontrivial deck transformation `σ`.
> Then, with respect to the unique complete finite-volume hyperbolic metric on `Ñ`
> (namely `p*` of the metric of `N`), `σ` is an **orientation-reversing self-isometry**
> of `Ñ`. In particular `Ñ` is amphichiral, and the mirror self-isometry is realized by
> the deck involution itself.

**Proof.**

*Step 1 — `σ` is an isometry.* Give `Ñ` the pullback metric `p*g`, where `g` is the
hyperbolic metric of `N`. Deck transformations of a Riemannian covering are isometries
of the pullback metric by construction (`p ∘ σ = p`, and `p` is a local isometry, so
`σ` is a local isometry, and a bijective local isometry of connected complete manifolds
is an isometry). Note Mostow rigidity is **not needed for this step**; it is needed only
for the metric-independence remark in Step 3.

*Step 2 — `σ` reverses orientation.* `Ñ` is orientable and connected; fix an
orientation `ω` of `Ñ`. Since `σ` is a diffeomorphism of a connected orientable
manifold, `σ*ω = ε·ω` with a single global sign `ε ∈ {+1, −1}` (the local comparison
sign is locally constant, hence constant). Suppose toward contradiction `ε = +1`, i.e.
`σ` preserves `ω`. Then `ω` is invariant under the whole deck group `{id, σ}`, and an
orientation invariant under the deck group of a covering **descends to the base**: for
`y ∈ N` define the local orientation at `y` by pushing `ω` forward through `p` from
either point of `p⁻¹(y)` — invariance under `σ` is exactly the statement that the two
preimages give the *same* answer, and `p` being a local diffeomorphism makes the
resulting field of local orientations continuous. That is an orientation of `N`,
contradicting non-orientability. Hence `ε = −1`: `σ` is orientation-reversing. ∎
(Equivalently and more concretely, in the local-orientations model `σ(x, ω_x) =
(x, −ω_x)` visibly maps the sheet carrying a local orientation to the sheet carrying
its negation; the descent argument above is the same fact stated without a model.)

*Step 3 — metric-independence.* By Mostow–Prasad rigidity the complete finite-volume
hyperbolic metric on `Ñ` (and on `N`) is unique up to isometry, so "the" hyperbolic
metric of `Ñ` is isometric to `p*g` and the conclusion is a statement about `Ñ` as a
hyperbolic manifold, not about a preferred metric. This is where rigidity earns its
place in the statement. ∎

**Remarks.**
1. Freeness of `σ` is not used and not claimed as needed: amphichirality only asks for
   *some* orientation-reversing self-isometry. (That `σ` is additionally free is extra
   structure, and §3.3 records evidence that it buys something extra.)
2. The proof uses nothing about dimension 3 except through Mostow (Step 3); Steps 1–2
   hold for orientation covers of arbitrary non-orientable Riemannian manifolds.
3. This upgrades the seat's A6 verdict item (4) from **[argued]** to **[proved]**, and
   it is why the 40/40 census statistic in that verdict was a theorem wearing a
   statistic's clothes.

---

## 3. Corollary B (the 2-torsion law) and its edge

> **Corollary B.** Let `M` be an amphichiral (finite-volume, orientable) hyperbolic
> 3-manifold. Let `I` be any invariant of *oriented* hyperbolic 3-manifolds valued in
> an abelian group `A`, such that
> (i) `I` depends only on the orientation-preserving isometry class, and
> (ii) `I` is **mirror-odd**: `I(−M) = −I(M)`.
> Then `2·I(M) = 0` in `A`. Consequently:
> - if `A = ℝ/½ℤ` (the value group of SnapPy-normalized Chern–Simons), then
>   `I(M) ∈ {0, ¼}`;
> - if `A` is torsion-free (e.g. `A = ℝ`), then `I(M) = 0` exactly.
>
> By Theorem A this applies to `M = Ñ` for **every** orientation double cover of a
> non-orientable finite-volume hyperbolic 3-manifold.

**Proof.** Amphichirality gives an orientation-reversing self-isometry `φ : M → M`.
Read `φ` as a map `−M → M`; as such it is orientation-*preserving*, so by (i)
`I(−M) = I(M)`. By (ii) `I(−M) = −I(M)`. Hence `2·I(M) = 0`. The 2-torsion subgroup of
`ℝ/½ℤ` is `{0 + ½ℤ, ¼ + ½ℤ}` (solve `2x ∈ ½ℤ`), and a torsion-free group has trivial
2-torsion. ∎

This is B1227's one-theorem-two-regimes statement, here derived at publication care and
chained to Theorem A so that it holds *a priori* for every hyperbolic orientation
double cover — no census input.

### 3.1 What the corollary does and does not pin

For CS in `ℝ/½ℤ`, amphichirality pins the value only to the two-element set `{0, ¼}`.
That m004 sits at `0` rather than `¼` is a further fact about m004, **not** a
consequence of amphichirality (B1224/B1226 already recorded this; m003, m135, m207 are
amphichiral with CS = ¼, so the `¼` branch is genuinely inhabited among amphichiral
manifolds and the corollary is not vacuously sharp — MB12 for the statement itself).

### 3.2 The sweep's verdict on the corollary (see FINDINGS.md for data)

40/40 orientation double covers of the first non-orientable census manifolds are
amphichiral per SnapPy's proven-full symmetry groups, and 40/40 have CS on the
2-torsion set to ~1e−64 (quad-double), against a chiral control of 15 manifolds whose
minimum distance from the set is 1.3e−2. The corollary survives with the control
biting.

### 3.3 The honest edge: covers never used the ¼ branch (observed, NOT proved)

In the sweep — and in an extended CS-only scan of the first **120** orientation double
covers — the value distribution is `{0: all, ¼: none}`, with `|CS| ≤ 2.5e−64`. The
known ¼-manifolds are amphichiral but were *not produced as orientation covers here*
(checked: the Gieseking's cover is m004, not its CS = ¼ sister m003). So the data are
consistent with a **strictly sharper statement for covers**:

> **Conjecture C (not claimed as theorem).** The orientation double cover of a
> non-orientable finite-volume hyperbolic 3-manifold has CS = 0 exactly (not merely
> CS ∈ {0, ¼}).

Corollary B cannot prove this: mirror-oddness plus *some* reversing isometry gives only
2-torsion. If Conjecture C is true, the extra input must be the *additional* structure
Theorem A's isometry carries — it is a **free involution** (deck transformation), not
just any reversing symmetry. Typed as the missing datum: *a proof or counterexample
that a free orientation-reversing isometric involution forces the 2-torsion invariant
onto the identity component's torsion element `0` rather than `¼`* — plausibly via a
Chern–Simons/η-type invariant of the non-orientable quotient with values in `ℝ/¼ℤ`
whose transfer doubles it, but no such argument is banked here. A single orientation
double cover with CS = ¼ would kill Conjecture C while leaving Theorem A and
Corollary B untouched.

Consequence for the seat's refinement: the refinement ("amphichirality ⇒ CS ∈ {0,¼}")
is **confirmed and is not vacuous among amphichiral manifolds**, but for the covers
themselves the bound was never tight at ¼ in 120/120 trials — the record should not
cite the covers as evidence that both branch values occur *for covers*.

---

## 4. Conventions used (E23 discipline)

- **Amphichiral** = admits an orientation-reversing self-isometry (= self-homeo, by
  Mostow; §1).
- **CS normalization**: SnapPy `Manifold.chern_simons()`, real, defined modulo `½` for
  orientable cusped census manifolds, mirror-odd. Anchors verified in the sweep run:
  `CS(m004) ≡ 0`, `CS(m003) ≡ ¼ (mod ½)` (exact to quad-double).
- **Orientation of the cover**: never chosen. Every statement made is invariant under
  the sheet swap (CS flips sign under it, and both `0` and `¼` are fixed by negation in
  `ℝ/½ℤ` — consistency check: the corollary's value set had better be
  negation-invariant, and it is, being exactly the 2-torsion subgroup).
- **Basis conventions**: none needed (no homology bases, no cusp bases enter).
- **Symmetry-group certification**: a manifold is called amphichiral/chiral here only
  when SnapPy reports `is_full_group() = True` for the canonical-cell symmetry group,
  so both properties are certified, not heuristic.
