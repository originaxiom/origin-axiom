# R21-9 — THE PAIR-EVENNESS LEMMA: ABSTRACT PROOF
# (B666 cell 4; closes the last asterisk of the sign-hears-the-discriminant
# theorem, B656/G1 / dossier C2)

**Status: PROVEN** (theorem grade; every step verified exhaustively on the
full W(D4) (192 elements) and the full W(E6) (51840 elements) by
`b666_cell4_verify.py`, output `cell4_output.txt`, all exact integer /
symbolic arithmetic). The proof is elementary — neither Stickelberger/Swan
transport nor any ramified-norm analysis is needed; the anticipated
ramification subtlety dissolves at the correct (orbit/total) level, and is
simultaneously shown to be REAL at the naive per-pair level (§5).

---

## 1. Setting and statement

Let w ∈ GL_n(ℤ) have finite order (all eigenvalues roots of unity) — e.g.
any element of a Weyl group acting on a rank-n lattice. Fix t ∈ ℤ and put

  f(x) = x² − t·x + 1,  B_w = t·I − w − w⁻¹.

Write the eigenvalue multiset of w as

  { 1 with multiplicity a₁, −1 with multiplicity a₂ } ∪ { pairs {ζ, ζ̄} },

where every eigenvalue ζ ∉ {±1} lies on the unit circle, so its complex
conjugate ζ̄ = ζ⁻¹ is also an eigenvalue and the non-real spectrum is a
disjoint union of conjugate (= inverse) pairs. Let a_m ≥ 0 be the
multiplicity of the m-th cyclotomic polynomial Φ_m in char_w
(char_w = ∏_m Φ_m^{a_m}, a₁ = a_{m=1}, a₂ = a_{m=2}), and let

  ψ_m(x) = the minimal polynomial of ζ_m + ζ_m⁻¹ over ℚ
           (monic, degree φ(m)/2, in ℤ[x], all roots in (−2, 2)), m ≥ 3.

**Theorem (pair-evenness, unconditional form).**
(i) For each conjugate pair, f(ζ)·f(ζ̄) = (t − ζ − ζ⁻¹)², the square of a
    totally real algebraic integer.
(ii) det B_w = (t−2)^{a₁} · (t+2)^{a₂} · Λ_w(t)², where
    Λ_w(t) = ∏_{m≥3} ψ_m(t)^{a_m} is a RATIONAL INTEGER; equivalently, as
    an identity of integer polynomials,
    char_{w+w⁻¹}(x) = (x−2)^{a₁} (x+2)^{a₂} ∏_{m≥3} ψ_m(x)^{2·a_m}.
(iii) For EVERY prime p — no hypothesis on t²−4, ramified or not — the
    total p-adic valuation of the product of f over all conjugate pairs
    is even: v_p(∏_{pairs} f(ζ)f(ζ̄)) = 2·v_p(Λ_w(t)) ∈ 2ℤ.

**Corollary (the sign-hears-the-discriminant theorem, both directions,
even rank).** Let n be even and det B_w ≠ 0 (automatic for |t| > 2).
(a) If v_p(t²−4) is odd, then det(w) = (−1)^{v_p(det B_w)} for every w.
(b) If v_p(t²−4) is even, then v_p(det B_w) is even for every w, so
    (−1)^{v_p(det B_w)} = det(w) holds exactly on ker(det) — the
    sign-balanced half of any Weyl group (det: W → {±1} is onto whenever
    W contains a reflection).

---

## 2. Proof of the theorem

**(i) The key identity.** f is self-reciprocal (coefficients 1, −t, 1):
x²·f(1/x) = f(x). Directly,

  f(ζ) = ζ² − tζ + 1 = −ζ·(t − ζ − ζ⁻¹).

Hence for a pair {ζ, ζ⁻¹}, with λ_ζ := t − ζ − ζ⁻¹ (note λ_{ζ⁻¹} = λ_ζ):

  f(ζ)·f(ζ⁻¹) = (−ζ)(−ζ⁻¹)·λ_ζ² = λ_ζ².

λ_ζ ∈ ℤ[ζ + ζ⁻¹] is an algebraic integer in the totally real field
ℚ(ζ + ζ⁻¹). (Equivalently: ζ and ζ⁻¹ contribute the SAME eigenvalue
ζ + ζ⁻¹ to w + w⁻¹, so each pair contributes the square of one
B_w-eigenvalue. The pair product being a literal square is forced by the
self-reciprocity of f; this is the step that makes all norm/ramification
machinery unnecessary.)

**(ii) Integrality of Λ.** char_w ∈ ℤ[x] and w is diagonalizable of
finite order, so char_w = ∏_m Φ_m^{a_m}. One copy of Φ_m (m ≥ 3)
contributes the φ(m)/2 unordered pairs {ζ, ζ⁻¹} of primitive m-th roots,
and

  ∏_{pairs in one Φ_m-orbit} λ_ζ = ∏_{y : ψ_m(y)=0} (t − y) = ψ_m(t) ∈ ℤ,

since ψ_m is monic with exactly those roots. Multiplying over all orbits:

  Λ_w(t) = ∏_{pairs} λ_ζ = ∏_{m≥3} ψ_m(t)^{a_m} ∈ ℤ.

Since det B_w = ∏_{eigenvalues ζ of w} (t − ζ − ζ⁻¹), the factor at ζ = 1
is t−2, at ζ = −1 is t+2, and each pair contributes λ_ζ², we get

  det B_w = (t−2)^{a₁} (t+2)^{a₂} Λ_w(t)²,

and the same computation with t replaced by the indeterminate x is the
stated factorization of char_{w+w⁻¹} (each ψ_m-root is hit twice per
Φ_m-copy because ζ and ζ⁻¹ merge in w + w⁻¹).

**(iii)** Immediate: the total pair product is Λ_w(t)², the square of a
rational integer, so its p-adic valuation is 2·v_p(Λ_w(t)), even — for
every prime p, unconditionally. ∎

## 3. Proof of the corollary

Two standing facts, both forced by n even:

- **Parity balance.** n = a₁ + a₂ + Σ_{m≥3} a_m·φ(m) and φ(m) is even for
  m ≥ 3, so a₁ + a₂ ≡ n ≡ 0 (mod 2): a₁ ≡ a₂ (mod 2).
- **Sign.** det(w) = 1^{a₁}·(−1)^{a₂}·∏_{m≥3}(∏ prim. m-th roots)^{a_m}
  = (−1)^{a₂}, since each pair multiplies to ζ·ζ⁻¹ = 1.

By the theorem, with A := v_p(t−2), B := v_p(t+2):

  v_p(det B_w) ≡ a₁·A + a₂·B  (mod 2).

**(a) v_p(t²−4) = A + B odd.** Then A, B have opposite parities. If
a₁ ≡ a₂ ≡ 0 (mod 2): v_p(det B_w) is even and det w = (−1)^{a₂} = +1 —
agreement. If a₁ ≡ a₂ ≡ 1 (mod 2): v_p(det B_w) ≡ A + B ≡ 1 (odd) and
det w = −1 — agreement. So agreement for every w.

**(b) v_p(t²−4) = A + B even.** For p odd, p divides at most one of t±2
(they differ by 4), so A, B are both even (one may be 0). For p = 2: if t
is odd, A = B = 0; if t ≡ 0 (mod 4), A = B = 1; if t ≡ 2 (mod 4), then
A, B ≥ 1 and A + B even forces both even or both odd. In every case A ≡ B
(mod 2), so a₁A + a₂B ≡ (a₁ + a₂)·A ≡ 0 (mod 2) using a₁ ≡ a₂ and, when
A, B are both odd, a₁ + a₂ even. Hence v_p(det B_w) is EVEN for every w,
(−1)^{v_p} = +1 always, and agreement holds exactly when det w = +1,
i.e. on ker(det) — index 2, the sign-balanced half. ∎

(This also proves the "for all w ⟺ v_p odd" biconditional: in the even
case the disagreement set is the nonempty coset of reflections.)

## 4. Degeneracy clause (exact boundary)

v_p(det B_w) requires det B_w ≠ 0. By (ii), det B_w = 0 iff t = 2 with
a₁ > 0, t = −2 with a₂ > 0, or ψ_m(t) = 0 for some contributing m ≥ 3.
All roots of every ψ_m lie in (−2, 2), so |t| > 2 ⟹ det B_w ≠ 0 for
every w. The hypothesis v_p(t²−4) odd excludes t = ±2 but NOT the
interior degeneracies: t = 1 (t²−4 = −3, v₃ odd) kills the Φ₆-block
(ψ₆(1) = 0) and t = −1 kills the Φ₃-block; t = 0 has v₂(−4) = 2 (even)
and kills Φ₄. On such w both sides are undefined; on all other w the
corollary holds verbatim (the proof never uses |t| > 2, only
non-vanishing of the contributing factors).

## 5. The per-pair obstruction (why the naive strengthening is false)

The banked phrasing "the valuation of the product of f over EACH
conjugate pair is even" is true at the level actually used (the total /
per-Galois-orbit product, a rational integer squared) but FALSE per pair
at ramified primes, and this is exactly where the anticipated subtlety
lives. Witness (verified in the run): t = 5, p = 3, an element with a
Φ₉-block (present in W(E6): 9 is a degree of W(E6), and the run exhibits
char_w = Φ₉ = x⁶ + x³ + 1). ψ₉(x) = x³ − 3x + 1; ψ₉(5) = 111 = 3·37,
v₃ = 1 (ODD), and ψ₉ ≡ (x+1)³ (mod 3): 3 is totally ramified in ℚ(ζ₉)⁺
(e = 3, standard cyclotomic ramification). The unique prime 𝔭 above 3 is
Galois-stable, so the three Galois-conjugate λ's carry equal valuation
v₃(λ) = 1/3; each per-pair product λ² has v₃ = 2/3 — neither even nor an
integer. The orbit total is ψ₉(5)² with v₃ = 2: even. So:

- per-pair evenness: TRUE whenever p is unramified in ℚ(ζ_m + ζ_m⁻¹)
  (each v_p(λ) ∈ ℤ), FALSE in general at ramified primes;
- orbit/total evenness (what the theorem needs): TRUE unconditionally,
  because the orbit product is a rational integer squared before any
  local analysis begins.

## 6. Verification manifest (all exhaustive, all exact)

`b666_cell4_verify.py` → `cell4_output.txt`:

- S0: the three symbolic identities of §2(i) (sympy, exact cancel).
- S1: the exact integer characteristic polynomial routine
  (Faddeev–LeVerrier over ℤ, divisions asserted exact) cross-checked
  against sympy on all 192 W(D4) elements + 25 sampled W(E6) elements.
- S2: complete cyclotomic factorization of char_w for every element of
  both groups (trial division over all m with φ(m) ≤ 6; residue
  asserted trivial).
- S3: the structure identity of (ii) as an exact integer POLYNOMIAL
  identity, for all 192 + 51840 elements; plus the integer-level
  recheck det B_w = (t−2)^{a₁}(t+2)^{a₂}Λ² at every (t, w) cell.
- S4: det w = (−1)^{a₂} and a₁ ≡ a₂ (mod 2) for every element.
- S5: the corollary counts — W(D4) on the full banked grid
  (t = 4, 5, 7, 8; p = 2, 3, 5, 7, 13 as applicable): every odd-v_p cell
  192/192, every even/control cell exactly 96/192, reproducing
  B656/G1's independent-verification numbers; W(E6) at t = 5:
  p = 3, 7 (odd v_p) 51840/51840, p = 13 (control) exactly 25920/51840.
- S6: the per-pair obstruction witness of §5 (exact: v₃(ψ₉(5)) = 1;
  ψ₉ ≡ (x−1)³ mod 3).

## 7. Relation to the C2 sweep pointers

The B659 sweep (SWEEP_RESULTS.md, C2) located Pellet–Stickelberger/Swan
as the nearest principle and sketched a route via
det B_w = det(w)·N(χ_w(α)) plus ramified-norm parity. The proof above is
strictly simpler and stronger: the self-reciprocity of f turns each pair
product into a literal square (no norms from ℚ(√(t²−4)) appear — the
field of α, β never enters), Galois-stability + integrality make the
total a rational integer squared (no ramification case split), and the
same factorization yields the even-case exactly-half law on ker(det) in
three lines. What survives of the anticipated subtlety is §5: at
ramified primes the per-pair statement genuinely fails (v = 2/3), and
the orbit level is the sharp one.

Consequence for the ledger: the sign-hears-the-discriminant theorem
(B656/G1, dossier C2) is now PROVEN in full on even-rank lattices —
both the odd-v_p all-w direction and the even-v_p exactly-half law —
with the exhaustive verifications (207,384 + 192·grid + this cell's
full W(D4)+W(E6) battery) demoted from evidence to illustration.
