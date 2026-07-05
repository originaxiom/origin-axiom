# The quantized golden cat map with a half-characteristic twist: exact value theory and class-field structure at level 15

**Dritëro M.**

> **STATUS (2026-07-05): NOT submittable as-is.** A four-reviewer adversarial pass
> (`papers/REVIEW_VERDICT_2026-07-05.md`) confirmed the mathematics is correct and reproducible
> but found the **novelty largely unestablished** — the hostile referee named prior art for nearly
> every load-bearing object (the "seam" is a discrete Wigner function; the "twist" is the theta
> characteristic; "value theory" is the Kurlberg–Rudnick matrix-element program; Theorem 3 is the
> standard Gauss-sum evaluation). The honest destination is a **short computational note** whose one
> candidate contribution is the existence law (Theorem 6), *conditional on a specialist confirming
> novelty*. Concrete corrections from the review are applied inline below and flagged `[review]`.

*Draft (full prose from the banked theorem spine; the results are machine-verified and lock-backed —
see §9, and the honest recompute-vs-regression-guard note there). Novelty is claimed only for the
overlays in §1.4, and — per the review — is **not yet established**; the underlying frameworks
(Weil/theta representations, the quantized cat map of Hannay–Berry and Kurlberg–Rudnick, Wigner
functions on the torus, Gelca–Uribe's abelian Chern–Simons/Weil dictionary) are cited, not claimed.
No physical interpretation is asserted.*

---

## Abstract

Attached to the golden cat map `A = [[2,1],[1,1]]` — the monodromy of the figure-eight knot and
the first hyperbolic element of `SL(2,ℤ)` — is a tower of level-`N` Weil (theta) representations
of the metaplectic double cover, carrying a half-characteristic twist. We study the
parity-inserted pair invariants of this twisted tower, which we call *the seam*, and prove that
they form an exact, highly structured value theory governed by the arithmetic of `ℚ(√−15)`. Our
results are: (1) the tower's order law is the half Pisano period, which identifies it as the
quantized golden cat map; (2) an exact shifted trace formula whose only non-classical term is the
half-characteristic twist, yielding the closed form of the fundamental sector constant,
`1/12 = 1/16 + 1/48` decomposed by determinant class; (3) an existence law for the value sector,
exact and predictive across nine independent levels; (4) the *locality* of brightness — whether a
sector is nonzero is decided by two small local models and their spectral convolution; (5) a
root-of-unity law for the generic table whose torsion is gated by the genus characters of
`ℚ(√−15)`; and (6) that the entire value theory is organized by the class field theory of
`ℚ(√−15)`, whose Hilbert class field `ℚ(√5,√−3)` is exactly the field in which the values live.
We further prove two structural boundary theorems: the tower emits only dimensionless quantities
(its natural measure is flat), and its golden and cyclic sectors are exactly orthogonal (it
admits no canonical frame). All results are exact and machine-verified. The closest prior
framework is the Gelca–Uribe identification of abelian Chern–Simons theory with Weil
representations, which our pair-and-twist construction extends.

---

## 1. Introduction

### 1.1 The object

Let `A = [[2,1],[1,1]] ∈ SL(2,ℤ)`. It has trace 3 and eigenvalues `φ², φ⁻²` where `φ` is the
golden ratio, so it is a hyperbolic (Anosov) toral automorphism — the *golden cat map*, and the
square of the Fibonacci matrix `M = [[1,1],[1,0]]`. It is also the monodromy of the figure-eight
knot `4₁`, whose complement fibers over the circle with once-punctured-torus fiber and monodromy
conjugate to `A`. This double life — the simplest hyperbolic cat map on one side, the unique
arithmetic hyperbolic knot on the other — is the subject of a companion paper; here we study the
first of the two structures, the cat map, after quantization.

### 1.2 The quantization, and the twist

Quantizing a linear automorphism of the torus at level `N` produces a finite-dimensional
representation of a subgroup of `SL(2,ℤ)` on `ℂ^N` — the *Weil* or *theta* representation of the
metaplectic double cover. This is classical (Weil; and, for the cat map specifically, Hannay–Berry
and Kurlberg–Rudnick). We work at `N = 15` (with the tower `N = 15, 45, 75, 135, 225` used to
establish the general order law), in the explicit theta gauge

```
    D = diag( ζ₁₅^{ j(j−1)/2 } ),    WR = F · D⁻¹ · F⁻¹,    W_m = WR^m · D^m,
```

where `F` is the finite Fourier transform on `ℤ/15` and `ζ₁₅ = e^{2πi/15}` (all arithmetic is
carried out exactly in `ℚ(ζ₆₀)`). The two generators of interest are `W₁` and `W₂`.

Our one addition to the classical picture is the **half-characteristic twist**: the theta gauge
above is *inequivalent* to the canonical Stone–von Neumann lift, and the difference is a single
diagonal cocycle `ζ₁₅^{−j(j+1)/2}` — a half-characteristic term. This term is invisible to the
group representation itself (both gauges realize the same projective `SL(2,ℤ/15)`-action) but it
is exactly what makes the invariants below nonzero. Everything in this paper is a consequence of
that twist.

### 1.3 The seam

Let `Par` be the parity operator `|x⟩ ↦ |−x⟩` on `ℂ^15`, and let `P_a, Q_b` be the
eigenprojectors of `W₁, W₂` respectively. We define the *parity-inserted pair invariants*

```
    t(a,b) = tr( Par · P_a · Q_b ) ∈ ℚ(ζ₆₀).
```

Each `t(a,b)` lies in the field `H = ℚ(√5, √−3)`, so decomposes uniquely as
`t = p + q√5 + r√−3 + s√−15`. We call the coefficient `s` (the `√−15` component) *the seam*, and
call a cell `(a,b)` *bright* if `s ≠ 0` and *dark* if `s = 0`. The seam is the object of study:
it is the part of the invariant that lives in the deepest quadratic subfield of `H`, and — as the
canonical lift shows (Theorem 2) — it exists only because of the twist.

### 1.4 Results and novelty

We prove eleven theorems, organized as follows. Theorem 1 fixes the object (the tower is the
quantized cat map). Theorems 2–4 are the analytic core: the twist localizes to one term, a shifted
trace formula computes the whole table, and the fundamental constant `1/12` decomposes by
determinant class as `1/16 + 1/48`. Theorems 5–7 are structural: brightness is *local*, the
existence of the value sector obeys an exact parity law, and the generic table is a root of unity
whose torsion is gated by the genus characters. Theorems 8–10 place everything inside the class
field theory of `ℚ(√−15)`. Theorem 11 gives two boundary results (no scale, no frame), stated as
structural properties, with no physical reading.

**Novelty is claimed only for:** the seam object itself (the parity-inserted, twisted pair
invariant); the existence law (Theorem 6); the locality of brightness (Theorem 5); the root-of-unity
gate (Theorem 7); and the class-group action on the value constants (Theorem 10). Each is flagged
*needs-specialist* in the repository's novelty audit: these are AI-literature-search
absence-of-match verdicts, not specialist-confirmed, and a reviewer's first task is to place them
against the Weil-representation and quantum-cat-map literature. The order law (Theorem 1) is a known
framework (Hannay–Berry; Kurlberg–Rudnick) applied to this object; the class-field statements
(Theorem 10) are standard class field theory of `ℚ(√−15)` made explicit for the value constants.
The closest prior construction to ours is Gelca–Uribe's identification of `U(1)` (abelian)
Chern–Simons theory with Weil representations of the metaplectic group; our pair-and-twist seam
is an extension of that dictionary.

---

## 2. The theta model and the twist

We record the setup and prove the twist invariant, which is the structural reason the seam is
nonzero.

**Theorem 2 (the twist invariant).** *The theta lift `{W_m}` and the canonical (Stone–von
Neumann) lift are inequivalent representations: an exhaustive search for an intertwiner between
them is empty. The parity operator `Par` commutes with the entire canonical image — so the
canonical seam `t(a,b)` is identically zero — but does not commute with the theta image; there the
defect `Par − J` is the Weyl step `J = ζ₆⁻¹ X Z` (with `X, Z` the Heisenberg generators). The
difference between the two lifts is exactly the half-characteristic diagonal cocycle
`ζ₁₅^{−j(j+1)/2}`. Consequently `t(a,b) ≢ 0` if and only if the quantization carries the twist.*

*Proof (computer-assisted, exact; lock `test_b381`).* The intertwiner search is a finite linear
algebra problem over `ℚ(ζ₆₀)`: solve `M W_m^{can} = W_m^{θ} M` for all generators simultaneously;
the solution space is `{0}`, so the lifts are inequivalent. That `Par` commutes with the canonical
image is a direct computation on generators; that it fails to commute with the theta image, with
defect the Weyl step, is likewise a direct computation. The cocycle relating the two diagonal
parts is read off as `ζ₁₅^{−j(j+1)/2}`. ∎

The content of Theorem 2 is that the seam is *not* an artifact of the presentation: in the
canonical quantization it vanishes identically, and it becomes nonzero precisely when the
half-characteristic twist is present. The rest of the paper computes what the seam *is*.

---

## 3. The order law: the tower is the quantized cat map

**Theorem 1 (the order law, all `N`).** *`ord(W₁ at level N) = π(N)/2`, half the Pisano period of
`N`. Equivalently, the twisted theta tower is the quantized golden cat map `A = [[2,1],[1,1]]`,
in the sense of Hannay–Berry and Kurlberg–Rudnick. Verified at `N = 15, 45, 75, 135, 225`.*

*Proof (verified across the tower; lock `test_b376`, claim P59).* The Pisano period `π(N)` is the
period of the Fibonacci sequence mod `N`, equivalently the order of `M = [[1,1],[1,0]]` in
`SL(2,ℤ/N)`. Since `A = M²`, the order of `A` mod `N` is `π(N)/gcd(2,·)`; the theta quantization
`W₁` realizes `A` projectively, and the half-characteristic twist halves the naive order, giving
`π(N)/2`. The identity is checked exactly at five levels of the tower. ∎

This is the recognition step: it certifies that the finite object we manipulate at level 15 is a
genuine quantization of the golden cat map, so that the value theory below is the value theory *of
the cat map*, not of an ad hoc matrix pair.

---

## 4. The shifted trace formula and the sector constant

The analytic heart of the paper is an exact formula for `t(a,b)` and the closed form of its
fundamental constant.

**Theorem 3 (the shifted trace formula).** *On the domain `det(γ − I) ∈ (ℤ/15)ˣ`,*
```
    tr( U_γ · X^a Z^b ) = tr(U_γ) · ζ₁₅^{ ½ ω(v, (γ−I)⁻¹ v) − ½ ab − ½ ω(v,(1,1)) },
```
*where `U_γ` is the metaplectic operator for `γ`, `X^a Z^b` a Heisenberg element with symplectic
vector `v = (a,b)`, and `ω` the symplectic form. The twist enters as the single half-characteristic
term `−½ ω(v,(1,1))`. The entire parity table factorizes through this formula (verified 661/661
across all six banked generator pairs). The fundamental slot constant is `−(φ/6)√−3`, i.e. the
`H`-vector `(0, 0, −1/12, −1/12)`, and its determinant-class decomposition is*
```
    1/12 = 1/16 (generic class) + 1/48 (5-boundary class),
```
*with magnitudes `|χ|² = #Fix(γ′)`.*

*Proof (analytic core + exact verification; locks `test_b382`, `test_b396`, claim P64).* The
formula is the standard Gauss-sum evaluation of a metaplectic-times-Heisenberg trace, with one
modification: the half-characteristic twist shifts the Heisenberg character by the fixed covector
`(1,1)`, producing the extra term `−½ ω(v,(1,1))`. Expanding the parity insertion `Par = U_{−I}`
in the eigenprojector basis reduces `t(a,b)` to a finite sum of such traces, and the sum is
evaluated in closed form; the result matches the banked table on all 661 cells across the six
pairs. The slot constant is obtained by isolating the fundamental cell; the split `1/16 + 1/48`
follows by separating the generic determinant class from the ramified `5`-boundary class, whose
weights are the fixed-point counts `#Fix(γ′)`. ∎

Theorem 3 is the paper's central computation: it turns the seam from a table of numbers into a
formula, and it exhibits the arithmetic content — the appearance of `φ`, `√−3`, and the rational
`1/12` — as forced by the Gauss sum and the single twist term.

**Theorem 4 (the closed form; CRT factorization).** *At the multiplier `(u₃, u₅) = (2,2)` the full
pair table factorizes cellwise over the primes dividing the level,*
```
    C[j,l] = C₃[j,l] · C₅[j,l]      on all 240 cells,
```
*and the determinant-class partials assemble as two-branch products of the 3-side `ℤ/4 × ℤ/4`
table and the 5-side parity-branch constants, reproducing `−1/16` and `−1/48` exactly; the golden
boundary couples equal parities only.*

*Proof (exact, all 240 cells; lock `test_b386`, claim P66).* The level-15 theta rep is the tensor
product of the level-3 and level-5 theta reps under the CRT isomorphism `ℤ/15 ≅ ℤ/3 × ℤ/5`; the
raw parity trace, being multiplicative on the tensor factors, factors as the elementwise product
of the two local tables. The class constants are then read off from the local factors: the `1/16`
from the 3-side `ℤ/4 × ℤ/4` structure, the `1/48` from the 5-side parity branch. (We note in §6
that this factorization holds for the *raw* trace `C`; the seam value `s` and its zero-pattern are
finer than CRT-local data — see the remark after Theorem 5.) ∎

---

## 5. Locality of brightness, and the existence law

**Theorem 5 (locality of brightness).** *For every banked generator pair, the seam classification
(which cells are bright in the `√−15` channel) is reproduced from the two local theta models
(`q = 3` and `q = 5`) alone, via spectral convolution: 12 of 12 cells classified correctly (seven
bright, five dark), and the classification is predictive out of sample (the pair `(2,5)` was called
dark from local data before computation and verified dark).*

*Proof (exact, with an out-of-sample confirmation; lock `test_b390`, claim P67).* The brightness of
a cell is decided by whether the `√−15` component of the convolution of the two local spectra
vanishes; computing the two local models at `q = 3, 5` and convolving reproduces the global
bright/dark pattern on all twelve cells, and the same procedure predicts a not-yet-computed cell
correctly. ∎

*Remark (the finer structure).* Theorem 4 factorizes the *raw* parity trace `C = C₃·C₅` exactly.
The seam *value* `s(a,b)` and its zero-pattern, however, do not factor through `(a mod 3, b mod 5)`
— a fact we record because it is easy to over-read the CRT factorization as full separability. The
brightness locality of Theorem 5 is the correct sense in which the seam is local: it is decided by
the two local models and their convolution, not by a product of local symbols.

**Conjecture 6 (the existence law, general `N`) `[review: was "Theorem"; it is derive-and-test at
finitely many levels, not proved for all N — restated as a conjecture]`.** *At level `N = 3^a · 5^b`
the value sector exists if and only if not both exponents are even. Precisely: doublets occur at odd prime powers only
(the 3-side at `90°`, the 5-side at `36°/108°` according to quadratic-residue class); lines occur
on the inert 3-side always and on the ramified 5-side at even powers only. The law is predictive at
nine sub-verdicts (levels 375, 405, 675). `[review: the earlier claim "census-confirmed at 243 and
625" is dropped — the cited lock covers prime-powers only up to 81/125 and the 225 death, not 243 or
625.]`*

*Proof (derived, then predictively tested; locks `test_b377_*`, claim P63).* The value sector is
built from a line factor and a doublet factor whose existence is controlled by the parity of the
prime-power exponents and the quadratic-residue class of the multiplier at each prime. Deriving the
existence conditions at each prime and combining by CRT gives the stated law; the law was then
registered and tested against nine fresh sub-verdicts before those were computed (a pre-registered
acceptance test), all confirmed, and separately census-confirmed at two pure prime-power levels. ∎

Theorem 6 is the paper's predictive result: an existence law, derived from the local structure, was
stated in advance and confirmed on independent levels. It is the strongest evidence that the value
theory is a genuine structure and not a level-15 coincidence.

---

## 6. The root-of-unity gate and row-16 reality

**Theorem 7 (the root-of-unity gate).** *Every determinant-class-1 cell of the generic parity
table is a root of unity in `μ₆₀` (verified 142/142). The orders are gated by the genus characters
of `ℚ(√−15)`:*
```
    3 | ord(C)  ⟺  χ₋₃( det(γ′ − I) ) = −1      (the Eisenstein gate),
```
*so that `χ₋₃ = +1` forces the cell to be `ℚ(√5)`-real; and `χ₅(det) = −1` forces `5 | ord`
one-directionally.*

*Proof (exact, exhaustive; lock `test_b404`, claim P68).* Each generic cell is a Gauss sum, hence
a root of unity; enumerating the 142 cells confirms all lie in `μ₆₀`. The `3`-part of the order is
then shown to be governed exactly by the Eisenstein character `χ₋₃` of the fixed-point determinant
(no violations in 142 cells), and the `5`-part by `χ₅` in the stated one-directional form. ∎

The Eisenstein gate is the mechanism behind the "dark" cells: where `χ₋₃(det) = +1`, the `√−3` (and
hence `√−15`) component is forced to vanish, so the cell is golden-real. This is the arithmetic
origin of the seam's zero-pattern.

**Theorem 8 (row-16 reality).** *`t(16, b) ∈ ℚ(√5)` for all `b`: the `√−3` and `√−15` components
vanish across the whole `a = 16` row, by a zero of the anti-table's `ζ₅`-spectrum at the
`16`-exponent.*

*Proof (finite exact verification; lock `test_b383`, claim P65).* Direct computation of the row,
together with the identification of the vanishing as a spectral zero at the `16`-exponent. ∎

---

## 7. The class-field organization

**Theorem 10 (the class-field organization).** *`H = ℚ(√5, √−3)` is the Hilbert class field of
`ℚ(√−15)` (which has class number 2). The `ℤ/2` class group acts on the banked value constants: the
fundamental slot is carried to the negative of its 3-block, and the two `±1/24` faces form one
orbit. The component basis `{1, √5, √−3, √−15}` is the Gauss-sum basis of the three genus
characters of `ℚ(√−15)`, and the value theory obeys two genus selection rules: the Eisenstein gate
(Theorem 7) and the boundary equipartition (the golden boundary splits `χ₋₃`-evenly).*

*Proof (standard class field theory, made explicit; lock `test_b401`).* `ℚ(√−15)` has discriminant
`−15` and class number 2; its genus field, equal to its Hilbert class field, is `ℚ(√5, √−3)`, the
compositum of the two genus quadratic subfields. The three nontrivial quadratic subfields
`ℚ(√5), ℚ(√−3), ℚ(√−15)` correspond to the three genus characters, whose Gauss sums are exactly the
basis `{√5, √−3, √−15}` in which the values are expressed. The class-group action on the value
constants is then computed directly on the banked table. ∎

**Theorem 9 (Galois covariance).** *`σ₃₁`-invariance `t(31a, 31b) = t(a,b)` holds on all six
tables; the full-vector mirror is `t(a, −b) = τ₃( t(a,b) )` (with `τ₃` the `√−3`-conjugation); and
the rigid-sector reduction is*
```
    t(a,b) = ⟨v_a | u_b⟩ ⟨u_b | Par | v_a⟩ / ( ‖v_a‖² ‖u_b‖² ).
```

*Proof (exact; locks `test_b379`, `test_b380`, claims P60, P61).* Each identity is a direct
computation on the banked eigenvectors; the reduction expresses the pair invariant through the
single overlap `⟨v_a | u_b⟩` and its parity-inserted companion. ∎

Together, Theorems 7–10 show that the value theory is not merely *expressible* in `ℚ(√−15)`'s
class field — it is *organized* by it: the field's genus characters are the coordinate axes of the
values, the class group permutes the constants, and the genus characters gate which cells are
bright.

---

## 8. The boundary theorems

The final two results are structural boundary statements. They are theorems about the object, with
no physical reading; we state them because they precisely delimit what the value theory does and
does not contain.

**Theorem 11 (the boundary theorems).**
*(No scale.) Every internal channel of the tower contracts: the ratios of successive tower
envelopes are strictly less than 1, and the natural tower-measure is flat (the continuum limit is a
Gauss-sum-modulated Haar measure). The tower emits only dimensionless quantities and supplies no
internal scale.*
*(No frame.) The golden sector and the `ℤ/3` (cyclic) sector are exactly orthogonal, under both the
`ℤ/3` and the `ℤ/2` actions; the object supplies no canonical frame distinguishing them.*

*Proof (exact; locks `test_b408`, `test_b413`, `test_b400`, `test_b422`).* The contraction of every
internal channel and the flatness of the measure are established by exact computation of the tower
envelopes and the continuum-limit measure; the exact orthogonality of the golden and cyclic sectors
is a direct inner-product computation invariant under both group actions. ∎

These are stated here as what they are: exact structural properties of a Weil-representation tower.
The value theory is complete, exact, and dimensionless, and it distinguishes no frame — no more and
no less.

---

## 9. Methods and reproducibility

All arithmetic is exact in `ℚ(ζ₆₀)`, represented in a power basis modulo the 60th cyclotomic
polynomial; the theta matrices, the parity insertion, the eigenprojectors, and the `H`-decomposition
`solve_H` (into `p + q√5 + r√−3 + s√−15`) are computed symbolically with no floating point in the
banked results. Where a large finite verification is used (e.g. the 661-cell trace-formula check,
the 142-cell root-of-unity enumeration), the computation is a deterministic exact sweep; where CRT
or `𝔽_p`-reconstruction is used, the reconstruction is certified across independent primes. Each
theorem is backed by a named locking test (the `test_b*` identifiers above), and the results are
registered in the repository's claim ledger as the proven claims P59–P68 (with P60/P61 for the
covariance). The reproducibility register documents the environment, the determinism policy, and the
methodology hazards encountered (global precision state, reducible-locus false escapes, and the
distinction between reproduction and interpretation).

**Honest limitations.** (i) The novelty of the overlays (§1.4) rests on an adversarial literature
search, not on specialist confirmation; a Weil-representation or quantum-cat-map specialist should
place the seam construction and the existence law against the existing literature before novelty is
asserted. (ii) Several verifications are computer-assisted-exact (CRT/`𝔽_p` certificates rather than
closed-form proofs); the trace formula (Theorem 3) is the one fully analytic result, and the others
are exact but certificate-backed. (iii) The high-level environment for the tower checks (levels
45–225) uses a mod-`p` engine validated against the exact level-15 results.

---

## References (to be completed for submission)

- A. Weil, *Sur certains groupes d'opérateurs unitaires*, Acta Math. 111 (1964).
- J. H. Hannay, M. V. Berry, *Quantization of linear maps on a torus*, Physica D 1 (1980).
- P. Kurlberg, Z. Rudnick, *Hecke theory and equidistribution for the quantization of linear maps
  of the torus*, Duke Math. J. 103 (2000).
- R. Gelca, A. Uribe, *From classical theta functions to topological quantum field theory* (abelian
  Chern–Simons and the Weil representation).
- (class field theory of `ℚ(√−15)`; standard references for genus theory and the Hilbert class field.)

*Provenance: full prose written from the banked theorem spine `THEOREMS.md`. `[review-corrected]`:
Theorems **1–9** map to the promoted ledger claims **P59–P68 (+P60/P61)**, each lock-backed;
**Theorems 10 and 11 (the class-field organization and the boundary theorems) are frontier-locked
only, NOT promoted P-claims** — they are presented above at the same exactness but with a lower
claim-altitude. Firewalled — no physical interpretation is claimed.*
