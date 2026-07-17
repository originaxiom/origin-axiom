# CELL D — THE σ*-EQUIVARIANCE THEOREM: the chord data is defined over k(Γ)

**B662 successor campaign, wave 1, cell D.** Outcome per prereg:
**PROVEN** — the subfield law upgrades from LAW (two witnessed
instances) to **THEOREM (for the two banked objects, with the general
mechanism identified)**. Every decisive ingredient verified EXACTLY
(Fraction arithmetic) on the banked data; run log
`cellD_output.txt` (342 s), decisive script `verify_equivariance.py`.

---

## 1. Statement

**Theorem (chord-data descent).** For both banked weld doubles, the
chord data — the σ*-matrix C and the full Y-tensor of H¹(D; 27) — has
all its coordinates in the object's **invariant trace field k(Γ)**:

- **fig-8:** trace field K = ℚ(√−3) = k(Γ) (degree 2). The chord
  pipeline's arithmetic is closed in K (the B637 field class), so the
  data lies in K; K = k(Γ) is Neumann–Reid (B659 resolved the
  coincidence half). Gal(K/k(Γ)) = 1: the descent statement is
  degenerate — nothing further to prove.
- **silver (the content):** trace field L = ℚ(s, i), s⁴ = 8s² + 16,
  degree 8; k(Γ) = ℚ(i) (B659, SnapPy-verified m136 shapes
  {1/2+i/2, 1+i}). The Y-tensor's ten values and the σ*-matrix's 25
  entries are **fixed by the full Galois group Gal(L/ℚ(i))**, hence lie
  in ℚ(i) = k(Γ). This is a genuine degree-8 → degree-2 collapse and
  is FORCED by the construction, not a numerical coincidence of the
  banked table.

Moreover the containment is exact generation: the banked Y[023] =
−1/802575000 − (523/269665200000)i has nonzero imaginary part, so the
chord data generates exactly ℚ(i) (and the fig-8 data generates
exactly ℚ(√−3), banked) — the "= k(Γ)", not just "⊆ k(Γ)", half.

---

## 2. The Galois frame (P0 — verified exactly)

L has ℚ-basis 1, s, s², s³, i, is, is², is³. The roots of x⁴−8x²−16
are ±s and ±4i/s (s·(4i/s) = 4i, since 1/s = (s³−8s)/16), so L/ℚ is
Galois of degree 8 and

  **Gal(L/ℚ(i)) = {1, σ, τ, στ}**, σ: s ↦ −s, τ: s ↦ 4i/s (both fix i),

a Klein four-group (σ² = τ² = 1, στ = τσ — all verified as exact 8×8
rational maps, ring-homomorphism property checked on all 64 basis
products). Complex conjugation c (i ↦ −i, s ↦ s; the banked `.conj()`)
satisfies **c σ = σ c and c τ = (στ) c** (verified): conjugation does
NOT commute with τ — the partner involution g′ := c g c is

  σ′ = σ,  τ′ = στ,  (στ)′ = τ.

**Fix(σ, τ) = span(1, i) = ℚ(i)** — verified by exact nullspace
computation, so an element of L fixed by σ and τ lies in ℚ(i). This is
the only Galois theory the proof needs.

The τ-direction is where Neumann–Reid Thm 2.2 lives: L is the
(ℤ/2)²-extension of k(Γ) = ℚ(i) predicted for a trace field over its
invariant trace field.

---

## 3. The proof, lemma by lemma

Notation: ρ = the banked 2×2 silver letters (entries_L.json,
a, b, c ∈ SL2(L)); S1 = lift_sl2(ρ) (the 27-letters); u = the banked
weld intertwiner (u·conj(M) = T·u on the peripheral pair); U27 =
lift_sl2(u); S2 = U27·conj(S1)·U27⁻¹; LETS = the 12 letters of the
double; Y = the banked evaluator (Fox/certificate/cup machinery of
B649 3b-ii). All chord numbers are outputs of the deterministic
pipeline F: LETS ↦ (H¹ basis reps, Y-table).

**Lemma 1 (transport).** Every step of F downstream of LETS is
arithmetic in L (+, −, ×, ÷) with rational constants (the cubic, the
principal sl₂, the word combinatorics of relators/certificates —
data-independent), with branching only on zero-tests. A field
automorphism g of L preserves rational constants, commutes with the
arithmetic, and preserves zero-ness, hence commutes with every pivot
choice and every branch: **F(g(LETS)) = g(F(LETS))** for any
automorphism g. (Pure mathematics; no computation needed. Note the
pipeline from LETS onward contains NO complex conjugation — conj is
absorbed into the definition of S2 — which is exactly why the lemma
applies to τ even though τ does not commute with conj.)

**Lemma 2 (the letters are a Galois descent datum) — P1, exact.**
For each g ∈ Gal(L/ℚ(i)) there is M_g ∈ GL2(L) and a sign character
ε_g: Γ → {±1} with g(ρ(x)) = ε_g(x)·M_g ρ(x) M_g⁻¹ for x = a, b, c:

| g | M_g | ε_g(a,b,c) |
|---|---|---|
| σ | diag(1, −1) | (−, +, −) |
| τ | diag(−1, 1) ≡ diag(1, −1) in PGL₂ | (+, +, −) |
| στ | **identity** | (−, +, +) |

σ is the checkerboard identity read directly off the banked entries
(diagonal entries of a and c odd in s, off-diagonal even; b the
reverse pattern — `inspect_galois_output.txt`). For τ and στ the
intertwiner space was solved exactly over L: **dimension 1, unique
sign pattern, invertible solution** (all three verified entrywise on
a, b, c). The striking shape: M_στ = I — the letters are
στ-invariant up to the sign character alone (στ(a) = −a, στ(b) = b,
στ(c) = c entrywise), and τ-conjugation coincides with σ-conjugation
in PGL₂, so at the 27-level W_σ = W_τ and W_στ = I₂₇ (consistent with
the cocycle rule W_στ ~ W_σ·σ(W_τ)). The sign characters are trivial
on both relators and on the peripheral words (all exponent sums
even), consistent with ρ ⊗ ε ≅ ρ^g — the classical trace-field
sign-twist, here explicit.

**Lemma 3 (the weld is compatible with the descent datum) — P2, exact.**
The σ*-real structure enters here. With g′ the conj-partner of g
(§2), the banked weld u satisfies

  **g(u)·conj(M_{g′})·u⁻¹ = λ_g·M_g**, λ_σ = −1, λ_τ = +1, λ_στ = −1

(verified exactly, 2×2). This is the descent-datum cocycle condition
tying the antilinear weld J = U27∘conj to the linear Galois action:
it is what makes ONE intertwiner work for both sides of the double.

**Lemma 4 (single 27-level intertwiner for the whole double) — P3,
exact.** With W_g := lift_sl2(M_g) (the lift kills the signs ε_g —
the 27 is a PSL₂/even-symmetric-power module Sym¹⁶⊕Sym⁸⊕Sym⁰):

  **g(LETS[x]) = W_g · LETS[x] · W_g⁻¹ for ALL 12 letters, g = σ, τ, στ**

(36 exact 27×27 identities). Also the weld's 27-level descent
identity, needed for the σ*-corollary:

  **g(U27) = W_g · U27 · conj(W_{g′})⁻¹** (exact, all three g).

**Lemma 5 (cubic invariance under every lift) — P4, exact.** The
rational cubic C on the 27 satisfies the derivation identity
C(Xu,v,w) + C(u,Xv,w) + C(u,v,Xw) = 0 for X = e_pr, f_pr, h_pr
(verified as an exact tensor identity on the 270-term support), and
its support has weight-sum zero (verified), so C is invariant under
exp(nilpotents), under the torus D(t2) for ANY t2, and under the Weyl
factor — i.e. under **every** lift_sl2 image, in particular under W_g.
(Spot-checked exactly on test vectors as well.)

**Lemma 6 (gauge covariance of the evaluator).** For any W that
conjugates all 12 letters and preserves the cubic, the evaluator
satisfies E_{W·LETS·W⁻¹}(z₁,z₂,z₃) = E_{LETS}(W⁻¹z₁, W⁻¹z₂, W⁻¹z₃)
(blockwise W⁻¹ on the six 27-blocks). Proof: in SideL, mat(w) ↦
W·mat(w)·W⁻¹ and zval ↦ W·zval, so every ω-value is unchanged by
Lemma 5; S_eval is a fixed signed sum of ω-values over
data-independent words (certificates, Fox positions); the peripheral
words are fixed strings. (Symbolic; rides on Lemmas 4–5.)

Define the g-semilinear transport on cocycles:
**Φ_g(z) := (I₆ ⊗ W_g⁻¹)·g(z).** By Lemma 4, Φ_g maps Z¹ to Z¹; it
maps B¹ to B¹ exactly (Φ_g(δv) = δ(W_g⁻¹ g(v)), one line from
Lemma 4).

**Lemma 7 (the banked H¹ basis is a ℚ(i)-form basis) — P5, THE
DECISIVE COMPUTATION, exact.** For all three nontrivial
g ∈ Gal(L/ℚ(i)) and all five banked H¹ representatives:

  **Φ_g(rep_m) = rep_m EXACTLY — at cocycle level, not merely mod B¹**

(15 identities of 162-vectors over L, all exact; each image was also
re-verified to be a cocycle). So the deterministic elimination basis
is itself Galois-fixed: it IS a ℚ(i)-form of H¹(D; 27). This is the
Hilbert-90/effective-descent step of the prereg, realized concretely:
abstract descent (H¹(Gal, GL₅(L)) = 1) guarantees a fixed basis
exists; the computation shows the banked basis already is one, so no
gauge is needed and the banked coordinates ARE the ℚ(i)-form
coordinates.

**Assembly (the theorem).** For g ∈ {σ, τ} and any banked triple
(i,j,k):

  g(Y_ijk) = E_{g(LETS)}(g·rep_i, g·rep_j, g·rep_k)   [Lemma 1]
           = E_{LETS}(Φ_g rep_i, Φ_g rep_j, Φ_g rep_k) [Lemmas 4–6]
           = E_{LETS}(rep_i, rep_j, rep_k) = Y_ijk      [Lemma 7, exact]

so Y_ijk ∈ Fix(σ, τ) = ℚ(i) = k(Γ). ∎

Because Lemma 7 holds with EXACT cocycle equality, the proof needs no
coboundary-insensitivity (class-descent) input at all — the one place
a further lemma could have been required is bypassed.

**Corollary (the σ*-matrix).** From the U27 identity (Lemma 4) one
gets the commutation **Φ_g ∘ σ* = σ* ∘ Φ_{g′}** on cocycles (direct
computation from σ*'s definition J = U27∘conj with side swap, using
g∘conj = conj∘g′). σ* preserves B¹ (uses the banked J² = +1,
re-verified in this run: σ*(δv) = δ(Jv) blockwise-swapped). Apply Φ_g
to the banked class identity σ*rep_i ≡ Σ_j C_ij·rep_j (mod B¹):
semilinearity gives Φ_g σ* rep_i ≡ Σ_j g(C_ij)·rep_j, while the left
side is σ* Φ_{g′} rep_i ≡ σ* rep_i ≡ Σ_j C_ij·rep_j (Lemma 7 for g′).
Coordinates in a basis are unique, so g(C_ij) = C_ij for g = σ, τ:
**C ∈ ℚ(i) = k(Γ)**, forced. ∎

Consistency: the banked tables are indeed s-free (independently
re-read in this cell: 10/10 Y entries, 25/25 C entries) — now a
theorem's instance rather than an observation. The proof nowhere
assumed it.

---

## 4. What the antilinear ingredients do (prereg precision)

The prereg listed the swap law Y∘σ* = conj(Y) and the real structure
(J² = +1, C·conj(C) = I) as proof ingredients. Their precise role:

- The **linear** part of the proof (Lemmas 1, 2, 5, 6, 7) is pure
  Gal(L/ℚ(i)) descent and would apply to any construction with
  Galois-descent-datum letters.
- The **antilinear** structure enters exactly twice: (i) the weld
  compatibility (Lemma 3 / the U27 identity), because S2 is defined
  THROUGH conj — the identity g(U27) = W_g·U27·conj(W_{g′})⁻¹ with the
  twisted partner g′ is the statement that the real structure and the
  Galois action form one coherent descent datum on the double; and
  (ii) the σ*-corollary (via Φ_g σ* = σ* Φ_{g′} and J² = +1).
- The Hilbert-90 sharpening banked in B649 3b-i (diagonal units are
  gauge-variant; the invariant is the real structure + the field of
  definition) is honored: the theorem's content is exactly the field
  of definition, and Lemma 7 exhibits the ℚ(i)-form concretely instead
  of gauging.
- The swap law itself is NOT consumed by this theorem — it remains the
  input for the conj-direction (field-of-moduli/CP question), which is
  cell F's territory: ℚ(i) is imaginary quadratic; descent below ℚ(i)
  is neither claimed nor needed here.

## 5. Scope and honesty

- **Proven:** the theorem for the two banked objects (fig-8
  degenerate; silver by the seven exact gate families P0–P5 above).
  All decisive computations exact (Fraction); no floats anywhere.
- **The general mechanism (route, not theorem):** for an arbitrary
  member, Lemma 2 is trace-field theory (ρ^g ≅ ρ⊗ε for g fixing
  k(Γ) — the NR Thm 2.2 circle; B659 already flagged the containment
  as "near-routine descent"), and abstract Hilbert 90 always provides
  SOME ℚ(i)-form of H¹. Two steps are NOT automatic in general and
  were computed here: the weld's descent-datum compatibility
  (Lemma 3), and either an exactly-fixed basis (Lemma 7's strong form)
  or, failing that, class-descent of the evaluator (banked as verified
  gates on the fig-8, B637, but not proven over general fields). A
  general-member theorem would need those two supplied per member —
  stated as the residual gap for the campaign's general-law ambitions.
- The B659 delta stands as predicted: the field-coincidence half is
  Neumann–Reid; what this cell adds is the proof that the
  **cocycle-level chord data** (not just traces/shapes) descends to
  k(Γ), plus the exact-generation observation.

## 6. Files and provenance

Cell deliverables (this directory,
`frontier/B662_successor_campaign/cellD/`):

- `verify_equivariance.py` — the decisive script
  (sha256 11d0331a…ef93e85)
- `cellD_output.txt` — full verbatim run log, all gates
  (sha256 f970e8e6…494609)
- `inspect_galois.py` / `inspect_galois_output.txt` — the data
  inspection that exposed the checkerboard s-parity and the sign
  characters (sha256 3fbe8761…73c2199 / 1257793e…955405)
- `cellD_descent_data.json` — M_τ, M_στ, sign characters, G-matrix
  verdicts (sha256 c0fd0ac9…8d204)

Banked inputs consumed (read-only, B649_silver_holonomy):
`entries_L.json` (54aa472e…de80f9), `letters27_L.json`
(dc04611b…ce9b84), `cubic_rational.json` (4f92b5ac…b926b),
`e6_principal_rational.json` (30629613…725fd6), `silver_Y_L.json`
(6ef6113c…ffd61b), `sigma_matrix_L.json` (4724a2b3…b554ba); the
pipeline head of `b649_stage3b_swap.py`/`b649_stage3a.py` re-executed
verbatim (reproduced dim Z¹ = 31, 26 coboundaries, 5 reps, J² = +1).
