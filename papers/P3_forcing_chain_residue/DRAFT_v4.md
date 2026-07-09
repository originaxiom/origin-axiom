# The forcing chain and the residue — [FROZEN INTERNAL NOTE, NOT PUBLICATION-READY]

**⚠ FROZEN (2026-07-09) as an internal note.** After three adversarial re-panel rounds, this write-up
still carries framing/labelling defects (documented in `SCRUTINY_P1P3_round3.md`) — e.g. "degenerate
d = 4, 6" (d=6 is non-degenerate) and residual ⊆-direction prose. Retained as an internal record only.
**The verified computations live in the cited B-nodes** (T-NORM, T-2REG, T-PQB, B479, with B479's d=5
field corrected to a degree-4 field over ℚ(√5)). Do not circulate as a paper.

**Complete draft v4 — 2026-07-09. v4 corrects three MAJOR defects the re-panel (round 2) confirmed in
v3, all CC-verified in Sage: (1) the determinant register is THREE-valued (the coset −μ₃ = {−1,−ω,−ω²}),
not ℤ/6 — v3's "six values" over-corrected v1's "ℤ/2"; (2) the norm, the parity, and the word-determinant
are THREE distinct orientation invariants that agree only in special cases — not "one residue" (the norm
is constant −1, the parity ALTERNATES with the level, the determinant is three-valued); (3) the d=5
held-breath field is NOT ℚ(√41) — the order-5 character generates a degree-4 field with quadratic subfield
ℚ(√5) (the "41" was a discriminant factor); and Theorem F7's "exactly" is downgraded to the proven ⊇
direction. v3 folded in the prior-art assessment (B491, Goldman/Cantat/BGMW; APPEARS-NOVEL/NEEDS-SPECIALIST).
v2 (2026-07-08) revised after the first panel: v1 had over-stated the determinant register as a single ℤ/2,
mis-stated the order-5 field, and gave a quantifier ("every divisor d ≥ 3") that clashed with the m∈{1,2,4}
exception (the missing hypothesis is non-degeneracy, τ_d ≠ 0, which fails at d = 4). All three are
corrected here. Full prose in the owner's register. NOT yet through its own literature gate or a
re-panel. Claims traceable to the banked record (T-NORM, T-HIER, T-PQB, T-2REG, B479).**

---

## Abstract

The substitution σ: a → ab, b → a generates the entire program: its eigenvalue is the golden
ratio, its companion matrix is the golden monodromy, its mapping torus is the figure-eight, its
trace field is ℚ(√−3), and iterating it walks the Markov spine. We follow σ up the tower it builds
and ask what survives every level. What survives is orientation — but read carefully, because it is
not one number: it is a small family of orientation invariants that agree exactly where they meet.
The **norm** N(λ_m) = −1 = det X_m of the metallic half-matrix is a genuine ℤ/2, and it is *constant*
across the family (indexed by the member m). The two-register **parity** det(Par@N) = sign(σ on
(ℤ/N)²) = (−1)^{(N−1)/2} is a genuine ℤ/2 in which the quantum and classical quantizations agree at
*every* level — but its value *alternates* with the level N (−1 at N = 15, 75; +1 at N = 45, 225).
The word **determinant** det(Par·W(w)) = −ω^{#L−#R} is *three-valued*, the coset −μ₃ = {−1, −ω, −ω²}:
a fixed orientation sign times a ℤ/3 character of the letter imbalance mod 3, collapsing to −1 exactly
on the balanced words #R = #L. These are three faces of orientation, not one residue; they coincide
only where they can — the determinant is −1 at balance, the parity equals the norm when N ≡ 3 (mod 4).
We prove their laws: the norm is frozen through the φ-power degeneracy; the determinant beats with the
Pisano period π(3) = 8 along the letter tower; and the object's fixed locus under its own half-turn —
the *held breath* — contains the torsion: member m holds the order-d torsion characters for divisors
d ≥ 3 of m whose cusp point is non-degenerate, with field ℚ(√−7) at d = 3 and a degree-4 field over
ℚ(√5) at d = 5. Cancel everything; what remains, in each register, is a sign.

---

## 1. Introduction

A generating rule is a small thing that will not stop. σ: a → ab, b → a is two arrows, and from
them the whole object unfolds: the golden ratio as the growth rate, the matrix [[1,1],[1,0]] as
the linearization, the figure-eight as the mapping torus, ℚ(√−3) as the field, the Markov numbers
as the traces. This paper is about what such a rule *keeps*. Most of what a substitution produces
cancels as you climb — traces grow, fields escalate, volumes accumulate, and the specific values
wash out into class data. But underneath the growth, orientation is conserved — and the honest
statement, which an earlier draft of this paper got wrong by forcing into one number, is that
orientation appears as *three* related invariants, in three different registers, agreeing exactly
where they meet.

The **norm** of the scale, N(λ_m) = −1, is a ℤ/2 that is constant across the family. The **parity**
of the map, (−1)^{(N−1)/2}, is a ℤ/2 whose two quantizations (quantum det(Par) and classical sign(σ))
agree at every level but whose *value alternates* with the level N. The **determinant** of the
quantized word, −ω^{#L−#R}, is three-valued — a fixed sign times a ℤ/3 character of the letter
imbalance. They are not the same number: the norm is frozen, the parity oscillates, the determinant
carries a third root; they coincide only in the balanced / N ≡ 3 (mod 4) cases. This paper's earlier
claim of "one residue seen through three instruments" was a true observation stated one categorical
level too strong; the corrected picture — three faces of orientation with explicit coincidence
conditions — is what we prove. Section 2 lays out the forcing chain. Section 3 proves the norm
identity and its freezing. Section 4 gives the determinant law (three-valued) and its Pisano rhythm.
Section 5 is the two-register parity law — the quantum and classical orientations agree at each level,
value and all. Section 6 is the deepest: the *held breath*, the fixed locus under the object's own
half-turn, which contains the torsion of the family.

---

## 2. The forcing chain

**Theorem F1 (the chain forces itself).** The following is a chain of forced determinations, each
step canonical: σ (the substitution) forces φ (its Perron eigenvalue); φ forces A₁ = [[2,1],[1,1]]
(the companion of x² − 3x + 1, up to conjugacy) and its half X₁ = [[1,1],[1,0]]; A₁ forces 4₁ (its
mapping torus); 4₁ forces the geometric representation ρ_geo; ρ_geo forces the invariant trace
field ℚ(√−3). No step carries a choice. The object is not assembled; it is deduced from two arrows.

The metallic family is σ's one-parameter deformation: σ_m: a → aᵐb, b → a, with eigenvalue the
metallic mean λ_m = (m + √(m²+4))/2, monodromy A_m = R^m L^m, and half X_m = [[m,1],[1,0]].

---

## 3. The norm identity, and its freezing

**Theorem F2 (the norm identity).** For every m, det X_m = N(λ_m) = −1: the orientation character
of the metallic half and the field norm of the metallic scale coincide, because X_m is the
companion matrix of x² − mx − 1, whose constant term is −1. The half is orientation-reversing at
every member; the scale is a unit of norm −1 at every member.

**Theorem F3 (freezing through the golden degeneracy).** The members m = 1, 4, 11, 29, … — the odd
powers of φ (λ_m = φ^{1,3,5,7,…}) — all live in the same field ℚ(√5), and the norm −1 is carried
unbroken through the degeneracy. No imaginary quadratic field admits a unit of norm −1; the residue
is therefore a real-field phenomenon in this register, and it cannot be quantized away.

The norm identity is the residue in its arithmetic dress. It says the object's handedness is not an
added structure but the *norm of its own growth rate*, forced by the shape x² − mx − 1 of the
recurrence. You cannot have the golden growth without the negative norm; the sign is in the seed.

---

## 4. The determinant law and the Pisano rhythm (a three-valued register)

**Theorem F4 (the determinant law).** Define the residue of a word w ∈ {R,L}* as det(Par·W(w)) at
level 15. Then residue(w) = −ω^{#L−#R}, ω = e^{2πi/3}: it depends only on the letter imbalance
mod 3, via the elementary determinants det W_R = ω̄, det W_L = ω, det Par = −1. Because det Par = −1
for *every* word, the sign is frozen and the image is exactly the **three-element coset −μ₃ =
{−1, −ω, −ω²}** — a fixed orientation sign times a ℤ/3 character of the imbalance. It is *three-valued*,
not six: the "positive" roots 1, ω, ω² are never attained (there is no word with det(Par·W) = +1).
The register lies inside μ₆ (indeed −ω has multiplicative order 6, which is the source of an earlier
draft's mislabelling it "ℤ/6"), but it is not surjective onto μ₆. It collapses to the single value −1
exactly on the **balanced words** #R = #L, where it meets the norm and parity registers. So this is a
ℤ/3 *refinement* of the balance sign, not a ℤ/6 group of values.

**Theorem F5 (the Pisano rhythm).** Along the Fibonacci letter tower (a → R, b → L), the imbalance
at rung k is ±F_{k−2}, so the residue cycles through {−1, −ω, −ω²} with the Fibonacci sequence mod 3
— period π(3) = 8, the Pisano period. The residue does not merely survive the tower; it *beats* along
it, a three-valued pulse in the object's own arithmetic rhythm, collapsing to −1 at the balanced rungs.

This is orientation in its quantum dress: the balance sign refined by the quantization to a three-valued
character of the imbalance, acquiring a period-8 heartbeat set by the golden recurrence reduced mod the
Markov prime 3. Two earlier drafts mis-counted it — v1 as "ℤ/2" (undercount: it distinguishes three
values), v2/v3 as "ℤ/6" (overcount: only three are attained). The honest count is three, the coset −μ₃.

---

## 5. The two-register parity law

**Theorem F6 (the quantum and classical orientations agree at each level).** The quantum orientation
det(Par@N) and the classical orientation sign(σ acting on (ℤ/N)²) are equal, and both equal
(−1)^{(N−1)/2} (Jacobi). At the seam levels this reads: N = 15 → −1, N = 45 → +1, N = 75 → −1,
N = 225 → +1 (verified by the reproducer). So at *each* level the two quantizations give the *same*
sign — that is the theorem — but the shared value **alternates** with the level, tracking N mod 4.

This is a genuine ℤ/2 — the *parity register* — seen in two mirrors at once (the quantum parity
operator and the classical map), and the content is that the mirrors agree. It is a distinct invariant
from the norm register of §3: the parity's value *depends on the level N* and alternates, whereas the
norm N(λ_m) = −1 is *constant across the family*. The two agree exactly when N ≡ 3 (mod 4) (levels 15,
75) and disagree when N ≡ 1 (levels 45, 225). Identifying the parity with the norm — as an earlier
draft did, calling them "the same orientation bit" — conflates a level-indexed alternating sign with a
family-indexed constant one; they are two of the three faces of orientation this paper distinguishes,
not one.

---

## 6. The held breath is torsion

The residue is what survives the object's motion. The final theorem asks what survives the object
*holding still* — the fixed locus under its own half-turn σ_m.

**Theorem F7 (held breath ⊇ torsion).** On the cusp locus κ = −2, the characters fixed by σ_m
**include** the order-d torsion characters for every divisor d ≥ 3 of m *whose order-d cusp point is
non-degenerate*. The geometric (hyperbolic) character is never fixed — it always breathes, exchanged
by σ_m. The mechanism proves this ⊇ direction: a generator of finite order d, with d | m, has aᵐ = I,
so σ_m acts as the swap a ↔ b and fixes the symmetric characters. (We prove torsion ⊆ Fix; the reverse
inclusion — that σ_m fixes *no* non-torsion character on κ = −2 — is not established here, so we state
the theorem as ⊇ and flag the "exactly" as open. An earlier draft asserted "exactly.")

*The field of the held breath.* Write τ_d = 2cos(2π/d) for the trace of the order-d rotation. The field
generated by the order-d held-breath character depends on the degree of τ_d over ℚ:
- **d = 3:** τ_3 = −1 is *rational*, and the held-breath character has minimal polynomial z² − z + 2,
  roots (1 ± √−7)/2 — genuinely the quadratic field **ℚ(√−7)** (CC-verified).
- **d = 5:** τ_5 is *irrational* (degree 2), so the held-breath character is degree **4**: its minimal
  polynomial is z⁴ − 3z³ + 7z² − 4z + 4, an irreducible quartic with **no real roots**, field
  discriminant 5²·41, and **quadratic subfield ℚ(√5)** (the golden field) — *not* ℚ(√41). The "41" is
  a factor of the discriminant, not the field; an earlier draft read the squarefree part of the
  polynomial discriminant (16400 = 2⁴·5²·41) and mislabelled the field as ℚ(√41). The honest statement
  is: the order-5 held breath lives in a degree-4 field over ℚ(√5).

The closed form Δ_d = τ_d²(τ_d² − 8) is a genuine per-rotation invariant, but it names the *field*
only when τ_d ∈ ℚ (the d = 3 case, and the degenerate d = 4, 6); when τ_d is irrational the character
field is a proper extension of the real subfield ℚ(τ_d) (degree 4 at d = 5, over ℚ(√5)) and Δ's norm
enters only through the discriminant. So the clean "the held-breath field is a quadratic ℚ(√D_d)" is a
d = 3 statement; the general order-d field over ℚ(τ_d) is left as the specialist question the
prior-art assessment (companion note) poses.

**The divisibility, and its exception.** Member m holds the breath of every divisor d ≥ 3 of m
whose cusp point is non-degenerate. Non-degeneracy fails exactly at d = 4, where τ_4 = 2cos(π/2) =
0 and Δ(0) = 0 — the order-4 rotation is central/reducible and holds no breath. This is why
m ∈ {1, 2, 4} hold no breath at all: m = 1 and m = 2 have no divisor ≥ 3, and m = 4's only
divisor ≥ 3 is the degenerate d = 4. The first member that breathes-and-holds is m = 3 (order 3,
ℚ(√−7)); the first order-5 holder is m = 5 (a degree-4 field over ℚ(√5)).

The held breath is the object's orbifold skeleton — the elliptic points where a generator becomes
a rotation. The geometry breathes; the torsion holds. And the divisibility is exact, once the
degenerate d = 4 is excluded: what a member can hold still is the torsion of its non-degenerate
divisors, no more and no less.

---

## 7. Method, mirrored

The program's method is its subject. To find the residue we did what σ does: we generated
everything the object touches and let the magnitudes cancel — the traces, the fields, the volumes,
the values — and watched for what would not go. What would not go was orientation. It is not one
result added at the end; it is the fixed point of the whole procedure, appearing as the constant
norm in the arithmetic, the level-alternating parity in the two quantizations, the three-valued
determinant of the word, and the torsion of the object's own stillness — three faces of one thing,
agreeing where they meet. Cancel everything; what remains, in each register, is a sign.

---

## 8. What is classical, and what remains open

Classical: units of norm −1 in real quadratic orders (Dirichlet); the Pisano period (Lagrange);
the Jacobi-symbol parity of the metaplectic determinant; the Markoff-cubic modular action on the
one-holed-torus character variety (Goldman) and the fixed-point/finite-orbit theory of mapping-class
actions on it (Biswas–Gupta–Mj–Whang; Cantat). Ours (scoped; an adversarial prior-art assessment run
after this paper's panel returns **APPEARS-NOVEL / NEEDS-SPECIALIST**): the three-register reading of
orientation (the constant norm; the level-alternating parity; the three-valued word-determinant, with
the explicit coincidence conditions); the Pisano-8 beat of the quantized word; the held-breath ⊇ torsion
theorem with the d = 3 field ℚ(√−7), the d = 5 degree-4 field over ℚ(√5), and the degenerate-d = 4
exception behind the m ∈ {1,2,4} gap. The closest prior art is Cantat (2009), who computes the fixed
points of the figure-eight monodromy [[2,1],[1,1]] on the same character surface by the fixed-curve
(x, x/(x−1), x) method, landing in ℚ(√17) — the same mechanism, but for the pseudo-Anosov at
commutator-order-4, not the finite-order σ_m at the cusp κ = −2 with the divisor-indexed order-d fields;
whether our field law is a corollary of that method or genuinely new is the one specialist question (see
the companion specialist note). Open: (i) the ⊆ direction of Theorem F7 (that no non-torsion character
is σ_m-fixed); (ii) the standard-word lemma (chain words word-mirror for all k); (iii) the general
order-d held-breath field over ℚ(τ_d) (degree 4 at d = 5), and whether these fields carry structure
beyond the per-order mechanism (each appearance requires its own reason — none is banked as cumulative).

---

## Appendix: reproducibility

Norm identity `br_n_norm.py` (B469); the determinant law and Pisano rhythm `rf3_quantum.py`
(B470, which decodes exactly the three symbols {−1, −ω, −ω²}); the two-register parity `br1_br2.py`
(B469, printing det(Par@N) = ±1 alternating: −1 at 15/75, +1 at 45/225); the held-breath theorem
`B479_held_breath_torsion/held_breath_mechanism.py` (the d = 3 minpoly z²−z+2 → ℚ(√−7), the d = 5
minpoly z⁴−3z³+7z²−4z+4 → degree-4 field with quadratic subfield ℚ(√5)). Each lock re-run at draft.
The v1→v4 corrections are recorded in SCRUTINY_P1P3_round2.md: v1 called the determinant register ℤ/2
(undercount) and the "residue" one bit; v2/v3 over-corrected to ℤ/6 (overcount) and mis-stated the
order-5 field as ℚ(√41) (a discriminant factor); v4 states the register as the three-valued coset −μ₃,
the three orientation invariants as distinct, and the order-5 field as degree-4 over ℚ(√5). The
held-breath quantifier carries the non-degeneracy
hypothesis that excludes d = 4).

---
*MSC 37B10, 11R11, 57K32, 11B39, 81Q50. Companion to Papers 1, 2, 4. Repository URL at packaging.*
