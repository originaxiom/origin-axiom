# The forcing chain and the residue: a substitution, and the sign that survives everything it builds

**Complete draft v2 — 2026-07-08. Revised after the adversarial panel (SCRUTINY_P1P3.md): v1
over-stated the determinant register as a single ℤ/2 (it is genuinely ℤ/6-valued, −ω^{#L−#R}, and
only *restricts* to the ℤ/2 on balanced words), mis-stated the closed form for the order-5 held-
breath field (the per-τ discriminant is imaginary; the real field ℚ(√41) is its *norm* over the
Galois conjugates), and gave a quantifier ("every divisor d ≥ 3") that clashed with the m∈{1,2,4}
exception (the missing hypothesis is non-degeneracy, τ_d ≠ 0, which fails at d = 4). All three are
corrected here. Full prose in the owner's register. NOT yet through its own literature gate or a
re-panel. Claims traceable to the banked record (T-NORM, T-HIER, T-PQB, T-2REG, B479).**

---

## Abstract

The substitution σ: a → ab, b → a generates the entire program: its eigenvalue is the golden
ratio, its companion matrix is the golden monodromy, its mapping torus is the figure-eight, its
trace field is ℚ(√−3), and iterating it walks the Markov spine. We follow σ up the tower it builds
and ask what survives every level. The answer is a single sign — read carefully, because it wears
two coats. In the *arithmetic* and *classical* registers the survivor is a genuine ℤ/2: the norm
N(λ_m) = −1 = det X_m of the metallic half-matrix, and the parity det(Par@N) = (−1)^{(N−1)/2} of
the quantized map, are the same orientation bit. In the *quantum* register the same object refines:
the determinant det(Par·W(w)) = −ω^{#L−#R} of the quantized word is ℤ/6-valued (a cube-root times a
sign), and it *restricts* to the ℤ/2 exactly on the balanced words #R = #L, where it equals −1. We
prove the residue's laws: the ℤ/2 is frozen through the φ-power degeneracy; the ℤ/6 determinant
beats with the Pisano period π(3) = 8 along the letter tower; and the object's fixed locus under
its own half-turn — the *held breath* — is exactly its torsion: member m holds the order-d torsion
for every divisor d ≥ 3 of m whose cusp point is non-degenerate. The program's method mirrors its
subject. Cancel everything; what remains is real, and what remains is (at balance) the sign.

---

## 1. Introduction

A generating rule is a small thing that will not stop. σ: a → ab, b → a is two arrows, and from
them the whole object unfolds: the golden ratio as the growth rate, the matrix [[1,1],[1,0]] as
the linearization, the figure-eight as the mapping torus, ℚ(√−3) as the field, the Markov numbers
as the traces. This paper is about what such a rule *keeps*. Most of what a substitution produces
cancels as you climb — traces grow, fields escalate, volumes accumulate, and the specific values
wash out into class data. But underneath the growth one quantity is conserved at every level, and
it is not a magnitude. It is a sign — or, more honestly, a sign in two of the three registers and
a sixth root of unity in the third, agreeing where the three meet.

We call it the residue, and its recurring appearance is the paper's thesis. The norm of the scale
(−1) and the parity of the classical map (±1) are literally the same ℤ/2, seen through the
arithmetic and the classical instruments. The determinant of the quantized word (−ω to a power) is
the same object refined by the quantization: a ℤ/6-valued character of the letter imbalance that
collapses to the ℤ/2 on balanced words. Section 2 lays out the forcing chain — how σ forces each
next object with no freedom. Section 3 proves the norm identity and its freezing through the golden
degeneracy. Section 4 gives the determinant law and its Pisano rhythm — and states plainly that
this register is ℤ/6, not ℤ/2. Section 5 is the two-register agreement — the quantum and classical
orientations read as one sign. Section 6 is the deepest: the *held breath*, the fixed locus of the
object under its own half-turn, which turns out to be exactly the torsion of the family.

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

## 4. The determinant law and the Pisano rhythm (a ℤ/6 register)

**Theorem F4 (the determinant law).** Define the residue of a word w ∈ {R,L}* as det(Par·W(w)) at
level 15. Then residue(w) = −ω^{#L−#R}, ω = e^{2πi/3}: it depends only on the letter imbalance
mod 3, via the elementary determinants det W_R = ω̄, det W_L = ω, det Par = −1. This register is
**ℤ/6-valued** — a cube-root of unity times a sign, the six values {−1, −ω, −ω², 1, ω, ω²} — not a
pure ℤ/2. It *restricts* to the ℤ/2 exactly on the **balanced words** #R = #L, where the imbalance
is 0 and the residue is −1. There, and only there, does the quantum determinant agree on the nose
with the norm and parity registers.

**Theorem F5 (the Pisano rhythm).** Along the Fibonacci letter tower (a → R, b → L), the imbalance
at rung k is ±F_{k−2}, so the residue cycles with the Fibonacci sequence mod 3 — with period
π(3) = 8, the Pisano period. The residue does not merely survive the tower; it *beats* along it, in
the object's own arithmetic rhythm, and the beat is genuinely six-valued, collapsing to the sign
only at the balanced rungs.

This is the residue in its quantum dress. The determinant of the quantized word is the norm/parity
ℤ/2 *refined* by the quantization to a ℤ/6 character of the imbalance; along the tower it acquires
a heartbeat, a period-8 pulse set by the golden recurrence reduced mod the Markov prime 3. Calling
this register "one ℤ/2" (as an earlier draft did) undercounts it: the ℤ/2 is what remains at
balance, and the full register is the cube-root refinement that carries the beat.

---

## 5. The two-register agreement

**Theorem F6 (the quantum and classical orientations agree).** The quantum orientation det(Par@N)
and the classical orientation sign(σ acting on (ℤ/N)²) are equal, and both equal (−1)^{(N−1)/2}
(Jacobi). At the seam levels 15, 45, 75, 225 they agree: the orientation read through the quantized
parity operator and the orientation read through the classical map are the same sign, at every
level.

This is the genuine ℤ/2 of the paper, seen in two mirrors at once — the quantum parity and the
classical map — and the theorem is that the mirrors agree. There is one orientation, and the two
quantizations of the object are two ways of reading it, never two values. (This is a different and
stronger statement than the determinant law of §4: here both registers are honestly ℤ/2-valued and
they coincide; there the determinant is ℤ/6 and coincides with the ℤ/2 only at balance.)

---

## 6. The held breath is torsion

The residue is what survives the object's motion. The final theorem asks what survives the object
*holding still* — the fixed locus under its own half-turn σ_m.

**Theorem F7 (held breath = torsion).** On the cusp locus κ = −2, the characters fixed by σ_m are
exactly the order-d torsion characters for divisors d ≥ 3 of m *whose order-d cusp point is
non-degenerate*. The geometric (hyperbolic) character is never fixed — it always breathes, exchanged
by σ_m. What can hold still is precisely the torsion: a generator of finite order d, with d | m,
whose finite order makes σ_m act as the swap a ↔ b, whose fixed locus is the symmetric characters.

*The field of the held breath.* Write τ_d = 2cos(2π/d) for the trace of the order-d rotation, and
Δ(τ) = τ²(τ² − 8) for the per-rotation discriminant. The held-breath field is ℚ(√D_d), where D_d
is the **norm of Δ(τ_d) over the Galois conjugates of τ_d** — not Δ(τ_d) itself:
- **d = 3:** τ_3 = 2cos(2π/3) = −1 is rational, so D_3 = Δ(−1) = 1·(1 − 8) = −7, giving **ℚ(√−7)**.
- **d = 5:** τ_5 = 2cos(2π/5) and its conjugate 2cos(4π/5) are the roots of x² + x − 1 (so their
  sum is −1 and product −1); the per-rotation Δ(τ_5) is *imaginary*, but its norm over the two
  conjugates is D_5 = ∏ Δ = (τ τ′)²·(τ² − 8)(τ′² − 8) = 1·(1 − 8·3 + 64) = 41, giving the *real*
  field **ℚ(√41)**. (The single-rotation formula τ²(τ²−8) is the right per-rotation object; the
  field is its norm, which is why d = 3 lands imaginary and d = 5 lands real.)

**The divisibility, and its exception.** Member m holds the breath of every divisor d ≥ 3 of m
whose cusp point is non-degenerate. Non-degeneracy fails exactly at d = 4, where τ_4 = 2cos(π/2) =
0 and Δ(0) = 0 — the order-4 rotation is central/reducible and holds no breath. This is why
m ∈ {1, 2, 4} hold no breath at all: m = 1 and m = 2 have no divisor ≥ 3, and m = 4's only
divisor ≥ 3 is the degenerate d = 4. The first member that breathes-and-holds is m = 3 (order 3,
ℚ(√−7)); the first order-5 holder is m = 5 (ℚ(√41)).

The held breath is the object's orbifold skeleton — the elliptic points where a generator becomes
a rotation. The geometry breathes; the torsion holds. And the divisibility is exact, once the
degenerate d = 4 is excluded: what a member can hold still is the torsion of its non-degenerate
divisors, no more and no less.

---

## 7. Method, mirrored

The program's method is its subject. To find the residue we did what σ does: we generated
everything the object touches and let the magnitudes cancel — the traces, the fields, the volumes,
the values — and watched for what would not go. What would not go was the sign. The residue is not
a result we added at the end; it is the fixed point of the whole procedure, the ℤ/2 that survived
the arithmetic (the norm), the classical map (the parity), the two registers agreeing (the
breath), and the object's own stillness (the held breath) — refined, in the quantum determinant, to
the ℤ/6 beat that collapses to the sign at balance. Cancel everything; what remains is real.

---

## 8. What is classical, and what remains open

Classical: units of norm −1 in real quadratic orders (Dirichlet); the Pisano period (Lagrange);
the Jacobi-symbol parity of the metaplectic determinant; the fixed-point theory of mapping-class
actions on character varieties. Ours (scoped, pending the gate): the register-by-register reading of
the residue (the norm and parity as one ℤ/2; the quantum determinant as its ℤ/6 refinement,
agreeing at balance); the Pisano-8 beat of the quantized word; the held-breath-is-torsion theorem
with its norm-field closed form (ℚ(√−7), ℚ(√41)) and the degenerate-d = 4 exception behind the
m ∈ {1,2,4} gap. Open: (i) the standard-word lemma (chain words word-mirror for all k); (ii) the
heredity of the chain's torsion primes; (iii) whether the held-breath fields ℚ(√−7), ℚ(√41), …
carry any further structure beyond the order-d norm mechanism (each appearance requires its own
reason — none is banked as cumulative).

---

## Appendix: reproducibility

Norm identity `br_n_norm.py` (B469); the determinant law and Pisano rhythm `rf3_quantum.py`
(B470); the two-register agreement `br1_br2.py` (B469); the held-breath theorem
`B479_held_breath_torsion/held_breath_capstone.py` (verified to order-13, with the norm-field
computation D_3 = −7, D_5 = 41 reproduced at revision). Each lock re-run at draft. The banked
λ_chain value was independently re-verified as a genuine limit (not a finite-rung artifact) during
this paper's assembly; recorded in the corrections ledger, along with the v1→v2 corrections (the
determinant register is ℤ/6 not ℤ/2, agreeing at balance; the order-5 field is the norm ℚ(√41), not
the imaginary per-rotation discriminant; the held-breath quantifier carries the non-degeneracy
hypothesis that excludes d = 4).

---
*MSC 37B10, 11R11, 57K32, 11B39, 81Q50. Companion to Papers 1, 2, 4. Repository URL at packaging.*
