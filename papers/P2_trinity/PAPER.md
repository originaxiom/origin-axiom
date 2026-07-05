# The figure-eight knot as the golden cat map: a complete instance of the quantum-topology / arithmetic / dynamics trinity

**Dritëro M.**

> **STATUS (2026-07-05): NOT submittable as a research paper.** A four-reviewer adversarial pass
> (`papers/REVIEW_VERDICT_2026-07-05.md`) confirmed the arithmetic is correct but found **no new
> theorem**: the two anchor torsions are individually standard (Theorem 4a is the Lefschetz zeta of
> the cat map re-indexed; Theorem 4b reproduces Porti's known adjoint torsion, value −3), and the
> program's own novelty audit already rates the E₆ content KNOWN. The honest destination is an
> **expository survey** (no novelty claimed), or a short note "Two E₆ adjoint torsions of the
> figure-eight" *if the pairing survives a specialist*. **The anchoring "two computed discriminants
> 5 and −3" pairing is asymmetric** — see the corrected Corollary in §4. Review corrections applied
> inline and flagged `[review]`.

*Draft (full prose from the banked theorem spine; every dictionary entry is machine-verified and
lock-backed). This is a **synthesis paper**: its contribution is an organizing principle and an
explicit dictionary, **not new theorems** — the two E₆ torsions are, individually, standard
invariants (a periodic-orbit product = a Lefschetz zeta, and Porti's adjoint Reidemeister torsion).
What was offered as new is the E₆-graded packaging and the pairing; per the review that packaging is
not, on its own, a theorem, and the pairing is asymmetric (§4). No physical interpretation is
asserted.*

---

## Abstract

The figure-eight knot `4₁` is distinguished twice over: it is the mapping torus of the simplest
golden cat map `A = [[2,1],[1,1]]` (forcing the field `ℚ(√5)` through its dynamics) and the unique
arithmetic knot (Reid, 1991; forcing `ℚ(√−3)` through its hyperbolic geometry). These two
uniquenesses about a single knot compose — `√5·√−3 = √−15` — into `ℚ(√5,√−3)`, the Hilbert class
field of `ℚ(√−15)`. We show that this double uniqueness is the organizing principle behind a family
of invariants of `4₁`, exhibiting one object in several mathematical languages: its symbolic coding
(a Sturmian system), its dynamics (Anosov; the monodromy has topological entropy `2 log φ`, the
trace-map flow Lyapunov exponent `4 log φ` — two distinct systems, kept distinct `[review]`), its two Reidemeister-type torsions in
the exceptional adjoint representation `𝔢₆`, its quantum invariant (Kashaev, in the volume-conjecture
regime), its quantized value measure, and its L-function landscape. The central identity is that the
object carries **two `𝔢₆` torsions, one per uniqueness**: the E₆-graded dynamical zeta of the golden
*monodromy* equals the cat map's periodic-orbit product (golden, `ℚ(√5)`), while the E₆-graded
geometric Reidemeister torsion at the *hyperbolic holonomy* is Eisenstein (`ℚ(√−3)`, canonical
adjoint value `−3`, reproducing Porti's form). The two torsions realize the double uniqueness as two
computed discriminants meeting at `√−15`. We give the explicit dictionaries between these faces and
argue that the object's apparent "walls" — that it produces no dimensionful scale and no canonical
mixing frame — are not obstructions but the correct properties of golden × Eisenstein arithmetic: a
number is dimensionless, and the genus characters of a field of class number two are independent.
The figure-eight emerges as the unique minimal geometric realization of the arithmetic of the golden
× Eisenstein compositum — a self-contained instance of the trinity between quantum topology,
arithmetic, and dynamics.

---

## 1. Introduction

The figure-eight knot `4₁` sits at the intersection of three subjects that rarely meet on a single
object: the theory of the modular / cat map (dynamics), the arithmetic of small imaginary quadratic
fields (arithmetic), and the theory of quantum knot invariants (quantum topology). This paper
collects what `4₁` looks like in each language and argues that the three views are one, organized by
a single arithmetic fact.

That fact is a *double uniqueness* (§2). On the dynamical side, `4₁` is the mapping torus of the
golden cat map `A = [[2,1],[1,1]]`, the simplest Anosov automorphism of the once-punctured torus,
whose eigenvalues `φ^{±2}` live in `ℚ(√5)`. On the geometric side, `4₁` is — by a theorem of Reid
— the *unique* arithmetic knot, with invariant trace field `ℚ(√−3)` realized by its decomposition
into two regular ideal tetrahedra. These two fields multiply, `√5·√−3 = √−15`, into `ℚ(√5,√−3)`,
which is the Hilbert class field of `ℚ(√−15)`. The claim of the paper is that this compositum is the
organizing arithmetic of all of `4₁`'s invariants.

The contribution is a *synthesis*, and we are explicit about what is and is not new. The individual
invariants below — the Sturmian coding, the Anosov entropy, the periodic-orbit product, Porti's
adjoint torsion, the Kashaev invariant and the volume conjecture, the special L-values — are
standard, and are cited as such. What we offer as new is (i) the **E₆-graded packaging** of two of
them into two torsions of the exceptional adjoint `𝔢₆`, (ii) the observation that these two torsions
are respectively golden and Eisenstein, realizing the double uniqueness concretely, and (iii) the
reading of the object's "walls" as the correct arithmetic properties of `ℚ(√−15)` rather than as
failures. Each of these is flagged needs-specialist in §7; the E₆-grading in particular rests on a
first-order deformation computation (`dim H¹(4₁, 𝔢₆) = 6 = rank E₆`, one dimension per Kostant
exponent) that is an instance of the Menal-Ferrer–Porti framework, cited there.

---

## 2. The cornerstone: the double uniqueness

**Theorem 1 (double uniqueness → the seam field).** *The complement `S³ ∖ 4₁` is (a) the mapping
torus of `A = [[2,1],[1,1]] ∈ SL(2,ℤ)`, the golden Anosov automorphism of the once-punctured torus,
and (b) the unique arithmetic knot complement, with invariant trace field `ℚ(√−3)`. Consequently its
two canonical fields — the dynamical field `ℚ(√5) = ℚ(φ^{±2})` and the geometric field `ℚ(√−3)` —
generate `ℚ(√5, √−3)`, the Hilbert class field of `ℚ(√−15)`, with `√5·√−3 = √−15`.*

*Proof.* (a) is the standard fibering of the figure-eight complement (Cooper–Long; verified in this
work via the trace map, lock `B67`). (b) is Reid (1991): `4₁` is the unique arithmetic knot, and its
trace field is `ℚ(√−3)`, realized geometrically by the two regular ideal tetrahedra of shape
`ω = e^{iπ/3}`. The eigenvalues of `A` are `φ², φ^{−2} ∈ ℚ(√5)`. Finally `ℚ(√−15)` has discriminant
`−15 = (−3)(5)`, class number 2, and its genus field — equal to its Hilbert class field — is
`ℚ(√−3, √5)` by genus theory. ∎

**The strong form (two families).** The two facts above are the tips of two *families* of extremal
characterizations of `4₁`, which meet in this one knot:

- The **golden family** (`→ ℚ(√5)`): the mapping torus of `A`; `A` realizes the minimal dilatation
  `φ²` of any pseudo-Anosov on the once-punctured torus; the Alexander polynomial
  `t² − 3t + 1 = (t − φ²)(t − φ^{−2})` is `A`'s characteristic polynomial; the `2`-bridge knot
  `b(5,2)`; entropy `2 log φ`.
- The **Eisenstein family** (`→ ℚ(√−3)`): the unique arithmetic knot (Reid); two regular ideal
  tetrahedra of shape `ω`; the smallest-volume cusped hyperbolic 3-manifold; commensurable with the
  Bianchi orbifold `H³/PSL(2, ℤ[ω])`; hyperbolic volume in the Bloch group of `ℚ(√−3)`.

Their fields multiply to `ℚ(√−15)`'s class field, and the amphichiral `ℤ/2` symmetry of `4₁`
matches the class group of order two. `4₁` is the *minimal* meeting — the simplest hyperbolic knot.
Whether the two families genuinely reduce to a single fact ("minimal golden dynamics ∩ minimal
arithmetic geometry") or are logically independent is left open (it is the subject of a separate
uniqueness atlas); for the purposes of this paper the compositum `ℚ(√−15)` is the organizing field,
however it is forced.

---

## 3. The seven faces

Throughout, `A = [[2,1],[1,1]]`, `φ²` its Perron eigenvalue, and `F_n, L_n` the Fibonacci and Lucas
numbers.

**Dynamics.** The trace-map flow of `4₁` on its `SL(2,ℂ)` character variety is Anosov, with Lyapunov
spectrum `{0, ±4 log φ}` at the discrete-faithful point and conserved invariant `κ = tr[a,b]` (lock
`test_b416`). This is the golden cat map's own hyperbolicity, transported to the character variety.

**Symbolic coding.** The substitution `σ: a ↦ ab, b ↦ a`, whose incidence matrix is the Fibonacci
matrix (with `A = M²`), generates the Fibonacci Sturmian subshift: complexity `p(n) = n + 1`,
topological entropy `0`, gap-labelling group `ℤ + ℤφ` (lock `test_b417`). The same golden ratio that
sets the dynamical entropy sets the quasicrystal spacing of the coding.

**The two E₆ torsions.** These are the anchor of the paper and are developed in §4.

**Hessian / frequency spectrum.** The Chern–Simons Hessian spectrum on `H¹(4₁, 𝔢₆)` is the six
per-exponent torsions `{τ_{m_i}}` (with `∏ τ_{m_i} = τ(E₆)`); it is Fibonacci-golden, and no
the six per-exponent torsions are Fibonacci-golden (lock `test_b424`). `[review: the earlier clause
"no pairwise ratio matches a Standard-Model mass ratio" is cut — it imports a physics frame with no
antecedent in a pure-math paper.]`

**Quantum invariant.** The Kashaev invariant `⟨4₁⟩_N` satisfies the volume conjecture,
`2π log⟨4₁⟩_N / N → Vol(4₁)`, and lies in `ℚ(ζ_N)⁺` with a nonzero `ℚ(√5)`-part exactly when `5 | N`
(for example `⟨4₁⟩₅ = 46 + 2√5`) — locks `test_b384`, `test_b419`. This is the standard
volume-conjecture behaviour of `4₁` (the first and most-studied case); the arithmetic observation is
the `5 | N` golden content.

**Measure.** The level-`N` single-seed value distribution refines to a measure on
`lim(ℤ/3^k × ℤ/5)` whose continuum limit is a Gauss-sum-modulated Haar measure — flat in magnitude,
with phase an exact `ℤ[ζ₉]` Gauss sum of norm 9 (locks `test_b413`, `test_b415`).

**L-function landscape.** The dynamical entropy equals `4·Reg(ℚ(√5)) = 2√5·L(1, χ₅)`;
`L(1, χ_{−15}) = 2π/√15`; and the combined zeta assembles as
`ζ_H = ζ · L(χ_{−3}) · L(χ₅) · L(χ_{−15})` — one factor per quadratic subfield of the seam field
(locks `test_b420`, `test_b401`).

---

## 4. The two E₆ torsions

The exceptional Lie algebra `𝔢₆` decomposes under the principal `𝔰𝔩₂` as
`𝔢₆ = ⊕_{i} Sym^{2m_i}`, the sum over the Kostant exponents `m_i ∈ {1,4,5,7,8,11}`. This grading is
the natural home for a torsion of `4₁` twisted by an `𝔢₆`-valued representation, because
`dim H¹(4₁, 𝔢₆) = 6 = rank E₆`, with exactly one dimension per exponent (an instance of the
Menal-Ferrer–Porti computation of adjoint cohomology; lock `B347`). We compute the torsion twice —
once twisted by the *homological* monodromy of the fibration, once by the *geometric* holonomy — and
find that the two are respectively golden and Eisenstein.

**Theorem 4a (the dynamical zeta = the periodic-orbit product — golden).** *The E₆-graded dynamical
zeta of the golden monodromy `A = [[2,1],[1,1]]` is*
```
    ζ(E₆) = ∏_{i ∈ exp(E₆)} ζ_{m_i},     ζ_m = ∏_{j=1}^{m} (2 − L_{4j}) = ∏_{j=1}^{m} (−5 F_{2j}²),
```
*and `5 F_{2j}² = |det(A^{2j} − I)| = #Fix(A^{2j})`. Hence `ζ(E₆) = ∏ (−#Fix(A^{2j}))` over the E₆
exponents: this invariant is the golden cat map's periodic-orbit product, golden, with prime content
exactly the Fibonacci apparition primes `{2,3,5,7,11,13,17,19,29,41,47,89,199}`.*

*Proof.* Under the principal grading, `det(I − Sym^{2m} A)` has the invariant direction (the
`H¹ = 1` summand) removed, leaving `∏_{k≠m}(1 − φ^{4(m−k)}) = ∏_{j=1}^{m}(1 − φ^{4j})(1 − φ^{−4j})
= ∏_{j=1}^{m}(2 − L_{4j})`; the identity `2 − L_{4j} = −5 F_{2j}² = −|det(A^{2j} − I)|` is classical
(locks `test_b423`, `test_golden_cat_map_principle`). The prime content follows from the Fibonacci
apparition (the primes dividing some `F_n`). ∎

We emphasize what Theorem 4a is and is not. It is a clean identification of an E₆-graded zeta with
the cat map's periodic orbits; it is *golden by construction*, since the monodromy `A` has
golden eigenvalues. Individually this is elementary (a product of `det(A^{2j} − I)`); the content is
the E₆-graded packaging, which pairs it with Theorem 4b.

**Theorem 4b (the geometric torsion at the holonomy — Eisenstein).** *The E₆-adjoint Reidemeister
torsion of `4₁` at the discrete-faithful holonomy `ρ_geo` (with `a ↦ [[1,1],[0,1]]`,
`b ↦ [[1,0],[−ω,1]]`, `ρ(relator) = I` forcing `ω² + ω + 1 = 0`, trace field `ℚ(√−3)`) is
Eisenstein, not golden: its twisted Alexander coefficients are rational integers at every E₆
exponent (the `√−3` cancels — each determinant is `Gal(ℚ(√−3)/ℚ)`-invariant), and the canonical
adjoint value is `−3 = disc ℚ(√−3)`. This is Porti's adjoint Reidemeister-torsion form, and it
reproduces the value obtained independently by the normal torsion at the `κ = −2` root and by its
Fried–Milnor identification. `[review: only ONE method (Fox/Wada) is computed in this artifact; the
normal-torsion (V30) and Porti/Fried–Milnor (V31) values are banked cross-references, not
re-verified here — "three methods agree" is corrected to one computation plus two cross-references.]`*

*Verification.* Fox calculus (the Wada invariant) at `ρ_geo`, carried out exactly by CRT over primes
`p ≡ 1 mod 3`, and validated by the trivial representation reproducing the ordinary Alexander
polynomial `t² − 3t + 1`. The Eisenstein content is genuinely present in the Fox matrix — its trace
is complex at every exponent — but cancels in each determinant, leaving rational coefficients and the
adjoint value `−3` (lock `test_b425`). We note that Theorem 4b is an *honest correction* of an
earlier reading in this work that had mislabeled the dynamical zeta (Theorem 4a) as the geometric
torsion; separating the two — the golden zeta of the monodromy versus the Eisenstein torsion of the
holonomy — is the substance of the corollary below.

**Corollary (two torsions = two cornerstone sides).** *`4₁` carries two `𝔢₆` torsions: the dynamical
zeta (golden, `ℚ(√5)`, Theorem 4a) and the geometric torsion (Eisenstein, `ℚ(√−3)`, Theorem 4b).
They realize the double uniqueness of §2 as two computed torsion values, one on each genus side of
`ℚ(√−15)`. `[review — the pairing is asymmetric, stated honestly:]` the Eisenstein side is a genuine
coincidence — the geometric torsion value is `−3 = disc ℚ(√−3)`; the golden side is NOT — the
dynamical zeta value is `ζ₁ = 2−L₄ = −5`, which is a torsion value in `ℚ(√5)`, **not** `disc ℚ(√5)`
(that is `+5`). So the clean "`−3 = disc(√−3) ↔ 5 = disc(√5)`" reading does not hold; what holds is
that the two torsions live in the two genus subfields `ℚ(√−3)` and `ℚ(√5)` whose compositum is the
Hilbert class field of `ℚ(√−15)`. That weaker (and correct) statement is the pairing.*

This corollary is the paper's organizing statement. Each torsion is, on its own, a standard object
(a periodic-orbit product; Porti's adjoint torsion, reproducing a known value `−3`). The claim is
the *pairing*: that the two natural E₆ torsions of the same knot land in the two genus subfields of
`ℚ(√−15)`, one per uniqueness. That pairing is the novelty offered for scrutiny, and it is flagged
accordingly in §7.

---

## 5. The walls as correct properties

Two structural results (proved in the companion value-theory paper and cited here) delimit what the
object contains.

**Theorem 9 (no scale).** *Every internal value channel contracts up the tower, and the
tower-measure is flat; hence the object emits only dimensionless quantities* (locks `test_b408`,
`test_b413`).

**Theorem 10 (no frame).** *The golden and `ℤ/3` sectors are exactly orthogonal in the shared
`W₂`-label space, under both the `ℤ/3` and the `ℤ/2` (class-group) structures; no canonical frame
exists in the object* (locks `test_b400`, `test_b422`).

**Corollary (the honest boundary).** `4₁` is a geometric realization of the arithmetic of the golden
× Eisenstein compositum `ℚ(√−15)`, seen across the faces of §3. It provides neither a dimensionful
scale nor a canonical mixing frame — because a number is dimensionless, and the genus characters of a
class-number-two field are independent. The "walls" are the arithmetic's own properties, not
obstructions to be overcome.

We state this as the terminus, and we are careful about its reach: it is a statement about the
mathematics of a knot and a field. It carries no physical content, and nothing in this paper is
offered as a step toward one.

---

## 6. Discussion

The trinity between quantum topology, arithmetic, and dynamics is realized here on the simplest
hyperbolic knot, with the golden cat map and the Eisenstein arithmetic as its two poles. The
neighbourhood is well populated: Garoufalidis–Zagier's quantum modularity places the Kashaev
invariant's asymptotics in an arithmetic setting; Morishita's arithmetic topology supplies the
knots–primes analogy in which a torsion and a zeta are the same kind of object; and the
Menal-Ferrer–Porti adjoint-torsion framework is the setting for the E₆ computation. What we add is
the concrete `4₁`-instance: the two E₆ torsions, one golden and one Eisenstein, meeting at `√−15`.

The honest boundary of the work is that this is a *characterization of one mathematical object*. It
is special for mathematics — the unique minimal meeting of golden dynamics and Eisenstein geometry —
and it is exact and reproducible. It is not a physical theory, and its "walls" are the reason it is
not: the object is dimensionless and frameless by the arithmetic of its own field.

---

## 7. Novelty, limitations, and what a specialist would confirm

This is a synthesis paper, and its scrutiny profile is different from a single-theorem result.

- **Individually standard.** The Sturmian coding, the Anosov entropy, the periodic-orbit product,
  Porti's adjoint torsion (value `−3`), the Kashaev/volume-conjecture behaviour, and the special
  L-values are all standard and cited; none is claimed as new.
- **Offered as new (needs-specialist).** (i) The E₆-graded packaging of the two torsions and the
  observation that they are golden and Eisenstein respectively, realizing the double uniqueness; (ii)
  the reading of the two "walls" as the correct arithmetic properties of `ℚ(√−15)`. Both are
  AI-literature-search absence-of-match verdicts, not specialist-confirmed. The most load-bearing
  input, the E₆ deformation cohomology `dim H¹(4₁, 𝔢₆) = 6`, is an instance of a known framework
  (Menal-Ferrer–Porti), so a deformation-theory specialist should confirm that the E₆-grading of the
  torsion adds genuinely new content beyond that framework, or place it within it.
- **A specialist would confirm:** the novelty of the E₆ character variety of `4₁` and its adjoint
  torsion grading (a low-dimensional-topology / arithmetic specialist in the Falbel–Guilloux /
  Menal-Ferrer–Porti circle); and whether "the torsion is the dynamical zeta" is a new packaging or a
  known correspondence.
- **This paper has not been independently validated** as a paper; it is a first full draft from a
  lock-backed dictionary. Every dictionary entry is machine-verified (the `test_b*` locks), but the
  *synthesis* — the claim that these are one object organized by one field — is the interpretive
  layer, and it is the layer a reviewer will test.

---

## References (to be completed for submission)

- A. Reid, *Arithmeticity of knot complements*, J. London Math. Soc. 43 (1991) — `4₁` is the unique
  arithmetic knot.
- J. Porti, *Torsion de Reidemeister pour les variétés hyperboliques*, Mem. AMS 128 (1997) — the
  adjoint Reidemeister-torsion form.
- P. Menal-Ferrer, J. Porti, adjoint cohomology / higher-dimensional Reidemeister torsion of cusped
  hyperbolic manifolds.
- S. Garoufalidis, D. Zagier, quantum modularity and the asymptotics of the Kashaev invariant.
- M. Morishita, *Knots and Primes: An Introduction to Arithmetic Topology*, Springer (2012).
- D. Cooper, D. Long, character varieties and the A-polynomial of the figure-eight knot.
- (genus theory / Hilbert class field of `ℚ(√−15)`; Hannay–Berry and Kurlberg–Rudnick for the
  quantized cat map, cited in the companion value-theory paper.)

*Provenance: full prose written from the banked theorem spine `THEOREMS.md`; every dictionary entry
lock-backed. This is a synthesis; its individual invariants are standard and cited, its packaging is
the offered novelty (needs-specialist), and no physical interpretation is claimed.*
