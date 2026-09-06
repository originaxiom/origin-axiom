# B1272 — THE OBJECT'S MIRROR ON THE TWO-FACE E₆: it is an outer involution of SPLIT type — the Cartan involution of E₆(6), not of E₆(−26) — and it selects one zero-sum triple of the 27

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact on B1270's icosian E₈; the real-form bound is a two-line lemma) + NEGATIVE for the fork's crossing (θ does not reach E₆(−26)) · **Price: unchanged at 14 rows / 11 sources** (no identification earned; I-10/I-11 re-read)

## The question (THE_STATE §7 item 2; B1265-main)

*"Does the object's θ act as an outer involution here, and with which fixed subalgebra?"* B1265-main derived
E₆(−14) from D₂ (inner) and showed E₆(−26) — Lorentz, compact colour, the graviton — needs an **outer**
involution, *"which is precisely θ"*, then fenced: the object's θ is trivial on the character variety, a reason
to doubt it carries E₆(−26). Here θ is **built from the object** and read exactly on the E₆ the two faces derive.

## 1. The mirror, derived (`verification/theta_two_faces.py` (a))

The amphichirality of A = LR is conjugation by P = diag(1, −1): P R P⁻¹ = R⁻¹, P L P⁻¹ = L⁻¹. On the golden face
⟨R, L⟩ mod 5 = SL(2,𝔽₅) = 2I, **det P = −1 = 2² is a square, so the mirror is INNER on 2I**: conjugation by
diag(3, 2), of order 4, whose image h under B1270's isomorphism is a unit icosian of order 4 with
Ad(h) R_q = R_q⁻¹, Ad(h) L_q = L_q⁻¹ (checked). Ad(h) sends the founding ratio g to a *conjugate* of g⁻¹; the
representative **h′ = L_q h** of the same mirror class (h′² = −1) sends **g ↦ g⁻¹ exactly**, so it preserves the
Eisenstein plane ℤ[g] and E₆ = ℤ[g]^⊥, and it inverts L. Ad(h′) is an involution of the lattice.

**Correction of B1270 (E69).** B1270 called *quaternion conjugation* x ↦ x̄ "θ, the Eisenstein conjugation,
B576's mirror axis made exact". Quaternion conjugation is the **inversion** x ↦ x⁻¹ on the unit group — an
anti-automorphism, not the mirror. Both maps restrict to g ↦ g⁻¹ on ℤ[g] and both swap (27,3) ↔ (27̄,3̄), so
every use B1270 and B1271 made of "θ" (the triplet swap, the chirality bit as ω ↔ ω̄) stands; the *identification
with the mirror* is withdrawn and replaced by Ad(h′). They differ by the inner involution x ↦ h′ x̄ h̄′.

## 2. Three involutions on E₆ and their Cartan signatures ((a), exact)

| involution of the icosian E₈ | on g | on E₆ | E₆ roots fixed | 2-orbits | Cartan on the E₆ span: fixed / odd |
|---|---|---|---|---|---|
| **the mirror Ad(h′)** | g⁻¹ | **outer** (27 ↔ 27̄) | 6 = 3A₁ | 33 | **3 / 3** |
| quaternion conjugation (the inversion) | g⁻¹ | outer | 2 = A₁ | 35 | 1 / 5 |
| their ratio x ↦ h′ x̄ h̄′ | g | inner (27 classes kept) | 12 = A₃ | 30 | 4 / 2 |

(The mirror fixes 8 = 4A₁ roots of E₈.) All three are exact lattice automorphisms; "outer" is read off the
P(E₆)/Q(E₆) coset (the six classes of 27 swapped with the 27̄ classes, or kept).

## 3. The real-rank bound, and the verdict

**Lemma.** If an involution T of the E₆ root datum is the restriction to a T-stable Cartan of the Cartan
involution θ of a real form 𝔤₀, then dim(𝔥^{−T}) ≤ real rank(𝔤₀): the θ-odd part 𝔞 = 𝔥 ∩ 𝔭 of a θ-stable
Cartan is an abelian subspace of 𝔭, and the real rank is the maximal dimension of such. (On the root-real span
i𝔱 ⊕ 𝔞 the odd part is 𝔞.) Real ranks: E₆(−78) 0, **E₆(−26) 2**, E₆(−14) 2, E₆(2) 4, **E₆(6) 6**; outer forms:
E₆(−26), E₆(6). Every involution of e₆(ℂ) is the complexified Cartan involution of exactly one real form.

- **The mirror (odd 3, outer) → E₆(6) only**: 𝔨 = sp(8), the **split** form. **It is not E₆(−26)'s involution**
  (real rank 2 < 3). The inversion (odd 5) also points to E₆(6). Their ratio (inner, odd 2) is compatible with
  E₆(−14) or E₆(2) — the D₂ side.
- So the object supplies **both** kinds: an inner involution of E₆(−14) type (D₂, B1265-main; the ratio here)
  and an outer one — but the outer one is **split**, not the graviton branch. **θ does not cross the fork.**
  B1265-main's doubt is confirmed, for a computed reason.
- **What B576's f₄ is, then.** B576's θ-grading of e₆ into f₄ ⊕ 26 is the grading of the unique non-trivial
  automorphism commuting with the **principal sl₂** (its verification script assigns θ-parity by exponent:
  blocks 4 and 8 odd). That automorphism is E₆(−26)'s involution — in the **representation frame**, where E₆
  contains the principal sl₂ of the geometric holonomy. The **lattice frame** (E₆ from the two faces) carries
  the object's mirror as a split-type involution. The two frames give different involutions for "θ on E₆";
  their identification is exactly I-25's unearned embedding. **The corpus's own earlier reading agrees:**
  B1119 found *"variant B (mirror swap, duality on colour) → E₆(6) split, character +6"* from the
  Lorentz-double side; B1114 places the Lorentz pair's host in E₆(2) or E₆(6). And `EXTERNAL_VERIFICATION
  §3.2`: only E₆(6) and E₆(−26) carry a *real* 27 and escape the Hermitian N = 0 argument — the mirror's form
  is one of the two chirality-capable ones, the split one.

## 4. The mirror selects one zero-sum triple of the 27 ((c), exact)

An SO(10) × U(1) grading of a 27 is fixed by one of its weights w₀ (pairings 1/16/10 with the others, checked
for all 27); its involution D₂(w₀) commutes with the mirror iff θ(w₀) = −w₀ on the E₆ part. **Exactly 3 of the
27 weights qualify, and they are mutually orthogonal in E₈ with E₆ parts summing to zero — one of the cubic's
45 zero-sum triples.** (Against the inversion: 15 of 27; against the ratio: 7 fixed weights.) Three commuting
SO(10) × U(1) gradings from a zero-sum triple meet in **SO(8) × U(1)²** — the triality frame of E₆, under which
27 = 8_v ⊕ 8_s ⊕ 8_c ⊕ 1 ⊕ 1 ⊕ 1 with the three singlets the triple itself. The mirror thus picks, inside the
27, a rank-3 element of the cubic (a "cubic triple") and the D₄ ⊂ E₆ whose triality permutes the three 8's.
Recorded as structure; no identification is made with a generation index (E63).

## 5. The mirror on the object's own sl₂ ((d), exact over ℚ(ω); a fence)

Among words of length ≤ 6, 104 endomorphisms α of π₁(m004) satisfy ρ ∘ α ≅ ρ̄ (relator kept, traces conjugated;
ρ the Riley representation). **None is an involution on the nose** (J J̄ scalar for none); 44 have α² inner and
60 have α² = Ad(D) with D outside ρ(π₁) at this length. The real type of the mirror's antilinear structure on
sl(2,ℂ) — sl(2,ℝ) (reflection) or su(2) (inversion) — is therefore **not decided here**; it is the datum that
would say whether the principal sl₂ is real-split (E₆(6), E₆(2)) or compact (the other three) in the mirror's
real structure. Left open, bounded: an involutive representative needs a longer word or a basepoint on the
mirror's fixed set.

## 6. Ledger

- **THE_STATE §7 item 2 answered on the lattice:** the object's θ is outer, of split type (Cartan signature
  3/3), the Cartan involution of **E₆(6)**; not E₆(−26)'s. JOIN 3's crossing candidate fails on the object's own
  E₆; the E₆(−26) involution lives in the principal-sl₂ frame (B576), whose identification with the lattice E₆
  is I-25's open row.
- **I-10 / I-11 re-read, unchanged:** the fork is now two computed involutions of the same lattice E₆ — D₂-type
  (inner, E₆(−14)/E₆(2)) and the mirror (outer, E₆(6)) — not one bridge; the rows' physical identifications
  (spin, polarization) are untouched.
- **New structure:** the mirror's zero-sum triple / SO(8) × U(1)² frame in the 27.
- **E69** typed (identification by restriction).

## Controls (MB12)

- The mirror is *derived* (P reduced mod 5, the isomorphism of B1270 rebuilt, R and L inverted — asserted), not
  chosen; the alternative representatives (h, h′) are exhibited and the one preserving ℤ[g] used.
- The bound's inputs are computed, not read off: outer/inner from the P/Q coset, the Cartan signature from ranks
  of (T ∓ 1) on the 72 E₆ roots; the fixed root systems are typed from their Cartan matrices.
- The zero-sum-triple statement can fail (15 of 27 for the inversion, 7 for the ratio; 3 with sum 0 only for the
  mirror).

## Verification

`verification/theta_two_faces.py` (exact; ~4 min, (d) dominant), run record `verification/theta_two_faces_run.txt`.
Lock: `tests/test_b1272_theta_on_the_two_face_e6.py` (lattice parts fast; (d) slow).
Feeds on: B1270 (the icosian E₈, the isomorphism, g), B1265-main (the fork table), B576 (the f₄ grading),
B1119/B1114 (the split host), B713 (P and the Galois torsor), B1263 (the 2T surjections). Registers no
identification change.
