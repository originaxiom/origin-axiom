# B1353 — THE ISOLATED ENHANCEMENT POINT ON AN E₆ LOCUS, MADE FINITE: in the flat G₂ orbifold class a point of the E₆ locus can be an isolated fixed point of its stabiliser (B1259's element lemma does not forbid it — main's E70), and all fourteen such local models are enumerated; in every one, every A-type stratum through the apex contains a line of the E₆ plane, so the transversal A₁/E₆ collision that Acharya–Witten's E₇ points need never occurs, while the literature's rule (chiral fermions at an ADE locus through a *non-orbifold* conical point; orbifold points modelled on Calabi–Yau ones) and the orbifold link's b₂ = 0 close the rest. The three E₇ points of the destination's item 1 are not orbifold points: the closing is the curved conical G₂ geometry, as B1259 said, now with the stratum theorem. 0 of 19.

**Verdict: PROVED** (the enumeration and the stratum statement: exact finite computation with a two-line proof; the physics: the literature's rule, cited). Depends on B1084 (the flat orbifold and its hatch), B1259 (the element lemma; main's E70 scope), B1352 (the cusp's last place closed, which made this the escape left). Verification: `verification/isolated_point_groups.py` (record `isolated_point_groups_run.txt`, 2 s). Lock: `tests/test_b1353_the_isolated_enhancement_point.py`.

## 0. The question

B1084 built the flat G₂ orbifold (ℂ² × ℝ³)/Ĝ, |Ĝ| = 96, with one E₆ locus (pointwise stabiliser exactly 2T) and three
A₁ families, and found the Acharya–Witten collision criterion met at the apex but "isolation failing" because no
element has a 0-dimensional fixed set. B1259 proved the element lemma (every element of SO(7) fixes a line) and
concluded that the flat class cannot isolate. Main's E70 scoped that: the element lemma stands, but a *group* can have
an isolated fixed point even when each of its elements fixes a line, so the stratum no-go does not follow. This arc
makes the question finite and answers it.

## 1. The setting, exactly

The E₆ locus of a flat G₂ orbifold is the fixed set of a binary tetrahedral 2T ⊂ G₂. Such a 2T lies in an SU(2) whose
fixed space in ℝ⁷ is an associative 3-plane P; the stabiliser of P in G₂ is SO(4) = (SU(2)_L × SU(2)_R)/Z₂ acting on
ℝ⁷ = Im ℍ ⊕ ℍ by (l, r)·(y, x) = (l y l⁻¹, l x r⁻¹), with 2T ⊂ SU(2)_R (right multiplication, trivial on Im ℍ = P).
A stabiliser Γ_p of a point p ∈ P that preserves P lies in SO(4); its kernel on P must be exactly 2T (the locus's
generic stabiliser), and p is an isolated fixed point of Γ_p iff the image H ⊂ SO(3) of Γ_p on P has no fixed vector,
i.e. iff H is non-cyclic: D_n (n ≥ 2), T, O, I. (An SO(3)-subgroup with a fixed vector is cyclic; the dihedral groups'
flips invert the axis.)

**Goursat.** Γ_p ⊂ SU(2)_L × SU(2)_R (mod the diagonal Z₂) with kernel {(±1, r) : r ∈ 2T} is a fibre product
L ×_Q R with R ⊇ 2T ◁ R and L/L_K ≅ R/2T. The finite subgroups of SU(2) containing 2T are 2T, 2O and 2I, and 2T is
normal in 2T and 2O but not in 2I (checked by quaternion arithmetic; A₅ ⊃ A₄ is not normal). So R ∈ {2T, 2O}:
- R = 2T: Γ_p = (L × 2T)/Z₂ with L ∈ {D*₂, D*₃, D*₄, D*₆, 2T, 2O, 2I} (any L with non-cyclic image; the dihedral
  series continues, four members shown);
- R = 2O: L ⊃ L_K of index 2 with the quotient matched to 2O/2T: (D*_n, C_{2n}), (D*_{2n}, D*_n), (2O, 2T) — the
  "half-diagonal" groups; seven shown.

## 2. Results (`isolated_point_groups.py`)

| L, L_K; R | \|Γ_p\| | fixed dims of the non-trivial elements {1: ·, 3: ·} | apex isolated | distinct A-planes through 0 | A ∩ P | A ∩ A′ meeting only at 0 / in a line |
|---|---|---|---|---|---|---|
| D*₂, D*₂; 2T | 96 | 54, 41 | yes | 18 | line, always | 36 / 117 |
| D*₃, D*₃; 2T | 144 | 86, 57 | yes | 26 | line | 252 / 73 |
| D*₄, D*₄; 2T | 192 | 138, 53 | yes | 30 | line | 216 / 219 |
| D*₆, D*₆; 2T | 288 | 206, 81 | yes | 50 | line | 828 / 397 |
| 2T, 2T; 2T | 288 | 182, 105 | yes | 50 | line | 564 / 661 |
| 2O, 2O; 2T | 576 | 434, 141 | yes | 86 | line | 2688 / 967 |
| 2I, 2I; 2T | 1440 | 1166, 273 | yes | 170 | line | 11340 / 3025 |
| **D*₂, C₄; 2O** (**B1084's Ĝ**) | **96** | **42, 53** | **yes** | **30** | **line** | **216 / 219** |
| D*₃, C₆; 2O | 144 | 68, 75 | yes | 44 | line | 432 / 514 |
| D*₄, C₈; 2O | 192 | 114, 77 | yes | 54 | line | 1008 / 423 |
| D*₆, C₁₂; 2O | 288 | 170, 117 | yes | 86 | line | 2376 / 1279 |
| D*₄, D*₂; 2O | 192 | 114, 77 | yes | 42 | line | 444 / 417 |
| D*₆, D*₃; 2O | 288 | 182, 105 | yes | 74 | line | 1764 / 937 |
| 2O, 2T; 2O | 576 | 362, 213 | yes | 122 | line | 4380 / 3001 |

Read: (i) **every one of the fourteen has an isolated fixed point at the apex** (joint fixed dimension 0) — B1084's Ĝ
included: its census {3d: 53, 1d: 42} is reproduced exactly (23 copies of P from 2T, 30 axis ⊕ 2-plane A-planes,
42 lines), and its apex *is* an isolated fixed point of the group. B1084's "isolation fails" read the elements; the
group isolates. (ii) **Every A-type plane through the apex meets the E₆ plane P in a line**, in all fourteen groups
(the count "each meets P in a subspace of dimension 1" holds for every A-element). (iii) Two A-planes can meet only
at the apex — 216 of B1084's 435 pairs do — so the flat class does contain A₁/A₁ collisions at a point; it never
contains an A₁/E₆ collision at a point.

**The two-line proof of (ii).** For g = (l, r) ∈ SO(4), Fix(g) = Fix_{Im ℍ}(Ad l) ⊕ Fix_ℍ(x ↦ l x r⁻¹). The first
summand is Im ℍ if l = ±1 and the axis line of l otherwise; the second is ℍ for g = 1, a 2-plane when l ≠ ±1 is
conjugate to r (x ↦ l x r⁻¹ has eigenvalue 1 with multiplicity 2 exactly when l and r have the same angle), and 0
otherwise. So the 3-dimensional fixed planes are P itself (l = ±1, r ∈ 2T ∖ {±1}) and the A-planes
axis(l) ⊕ {x : l x = x r} (l ~ r, l ≠ ±1) — and each A-plane contains the line axis(l) ⊕ 0 ⊂ P. The intersection is
exactly that line. (For D- and E-type strata through the apex — fixed planes of non-cyclic subgroups — the same
decomposition gives the same conclusion, the subgroup's fixed set being the intersection of its elements'.)

**Scope.** Γ_p ⊂ SO(4) covers every stabiliser that preserves the E₆ plane through p, i.e. every point at which the
E₆ locus is locally one 3-plane. A finite Γ_p ⊂ G₂ not in SO(4) would permute several E₆ planes through p (conjugates
of 2T) — a collision of E₆ loci, a different and more singular configuration than the destination's "E₆ locus with
E₇ points"; it is not enumerated here (Cohen–Wales' list of finite subgroups of G₂ would be the instrument) and is
registered (§5).

## 3. The literature's rule, and what the orbifold link cannot carry

- Witten, *Anomaly cancellation on manifolds of G₂ holonomy* (hep-th/0108165): "the generic singularities of X are
  codimension four A−D−E orbifold singularities, which give gauge symmetry. Chiral fermions arise when the locus of
  A−D−E singularities passes through isolated points at which X has an isolated conical singularity that is **not just
  an orbifold singularity**"; "Anomaly considerations imply that chiral fermions must arise, under certain conditions,
  if a singularity of type A passes through an isolated point at which X has a (non-orbifold) conical singularity";
  and the topological reason the locus Q passes through the point: "the two-sphere U wraps a non-trivial cycle in Y,
  and hence Q cannot be slipped away from the singularity."
- Acharya–Witten, *Chiral fermions from manifolds of G₂ holonomy* (hep-th/0109152) §2: "If Q is smooth and the normal
  space to Q is a smoothly varying family of G-singularities, the low energy theory will be G gauge theory on ℝ⁴ × Q
  without chiral multiplets. So chiral fermions will have to come from singularities of Q or points where Q passes
  through a **worse-than-orbifold** singularity of X." Their chiral models are cones on WCP³_{p,p,q,q} and on twistor
  spaces: three ℝ³'s of A-singularities meeting **only at the apex** of a *curved* cone (three intersecting D6-brane
  stacks in Type IIA), with chiral fermions (p, p, 1) + (1, p, q) + (p, 1, q) at the apex.
- Acharya–Gukov, *M theory and singularities of exceptional holonomy manifolds* (hep-th/0409191): "even though Joyce
  manifolds naturally admit orbifold singularities, none of them contains isolated G₂ or Spin(7) singularities close
  to the orbifold point in the space of metrics. … it is crucial that orbifold singularities are modelled on
  Calabi–Yau singularities … Therefore, at best, such singularities can give us the same physics as one finds in the
  corresponding Calabi–Yau manifolds."

Two structural facts complete the rule for the object's E₆ locus. (a) **The link of a flat apex is S⁶/Γ_p, with
b₂ = 0** (H²(S⁶/Γ; ℚ) = H²(S⁶; ℚ)^Γ = 0): there is no harmonic two-form on the link, hence no U(1) from the C-field at
the apex — the U(1) under which Witten's chiral SU(N) fields are charged and whose inflow forces them. (b) **E₆ is
anomaly-free** (no cubic Casimir), so no anomaly can force or detect a net number of 27s at any point; the only
detector is a U(1) mixed anomaly, and (a) removes the U(1). The orbifold apex therefore carries neither the geometry
of Witten's mechanism (an ADE locus passing through a non-orbifold conical point, with the A₁/E₆ collision isolated)
nor its detector.

## 4. What it means

**The three E₇ points are not orbifold points.** The destination's item 1 (`docs/THE_DESTINATION_LEDGER_2026-09-06.md`)
needs an E₆ locus with three points where an A₁ locus meets it transversally and the singularity enhances to E₇, each
carrying one chiral 27. In the flat class: the E₆ locus P is smooth (ℝ³ upstairs, ℝ³/H downstairs), the apex can be
an isolated fixed point of the group (fourteen models, B1084's among them), but every A-stratum through it contains a
line of P — the enhancement along an axis line is a codimension-6 line (a 5d locus, no 4d chirality), not a point.
B1259's conclusion stands with its mechanism corrected: not "no element isolates" but "no stratum collides". The
closing that could carry the bit is the curved conical G₂ geometry over the E₆ locus (cones with H₂(Y) ≠ 0 — the
Acharya–Witten and twistor-space cones), which is where the record already placed it (O4 of the chirality map).

**The three faces.** Geometric: the fixed-set algebra of SO(4) on Im ℍ ⊕ ℍ — the axis line is common to the A-plane
and P. Arithmetic: the Goursat list is finite and the dihedral series exhausts it; 2T is normal in 2O and not in 2I.
Quantum: the orbifold link's b₂ = 0 and E₆'s vanishing cubic anomaly — nothing at the apex can carry or detect the
count.

## 5. Caveats and registered

1. Stabilisers not preserving the E₆ plane (several E₆ branches through p) are not enumerated: registered, with the
   instrument named (finite subgroups of G₂ containing non-conjugate-by-SO(4) copies of 2T; Cohen–Wales 1983).
2. The physics statements are the literature's, cited verbatim; the arc adds the geometric obstruction (ii) and the
   two structural facts (a), (b). No claim is made about M-theory's spectrum at a codimension-7 orbifold point beyond
   them (Acharya–Witten: even codimension-6 orbifold points have "no known useful description").
3. The dihedral series D*_n is shown for n = 2, 3, 4, 6; the proof of (ii) is uniform in n.

## 6. Files

`verification/isolated_point_groups.py` (quaternion groups; Goursat enumeration; the census; the A-plane intersections;
B1084's group placed), `isolated_point_groups_run.txt`.
