# The forcing chain and the residue: a substitution, and the sign that survives everything it builds

**Complete draft v1 — 2026-07-08. Full prose with the narrative voice drafted (CC's rendering
of the owner's register, for the owner's final revision). NOT yet through its own literature
gate or adversarial panel — the remaining steps to the pilot's standard. Claims traceable to the
banked record (T-NORM, T-HIER, T-PQB, T-2REG, B479). Novelty language provisional pending the gate.**

---

## Abstract

The substitution σ: a → ab, b → a generates the entire program: its eigenvalue is the golden
ratio, its companion matrix is the golden monodromy, its mapping torus is the figure-eight, its
trace field is ℚ(√−3), and iterating it walks the Markov spine. We follow σ up the tower it
builds and ask what survives every level. The answer is a single sign. The orientation character
— the norm N(λ_m) = −1 = det X_m of the metallic half-matrix, the determinant det(Par·W(w)) =
−ω^{#L−#R} of the quantized word, the ℤ/2 that separates the two-register breath det(Par@N) =
(−1)^{(N−1)/2} — is one and the same residue, appearing in the arithmetic, the geometry, and the
quantization as the one quantity that does not cancel. We prove the residue's laws: it is frozen
through the φ-power degeneracy, it beats with the Pisano period π(3) = 8 along the letter tower,
and it is the fixed point of the object under its own half-turn — the *held breath*, which we
show is exactly the torsion: member m holds the breath of every divisor d ≥ 3 of m. The program's
method mirrors its subject. Cancel everything; what remains is real, and what remains is the sign.

---

## 1. Introduction

A generating rule is a small thing that will not stop. σ: a → ab, b → a is two arrows, and from
them the whole object unfolds: the golden ratio as the growth rate, the matrix [[1,1],[1,0]] as
the linearization, the figure-eight as the mapping torus, ℚ(√−3) as the field, the Markov numbers
as the traces. This paper is about what such a rule *keeps*. Most of what a substitution produces
cancels as you climb — traces grow, fields escalate, volumes accumulate, and the specific values
wash out into class data. But underneath the growth one quantity is conserved at every level, and
it is not a magnitude. It is a sign.

We call it the residue, and its recurring appearance is the paper's thesis: the norm of the scale
(−1), the determinant of the quantized word (−ω to a power), the parity of the classical map
(±1) are the same ℤ/2, seen through three different instruments. Section 2 lays out the forcing
chain — how σ forces each next object with no freedom. Section 3 proves the norm identity and its
freezing through the golden degeneracy. Section 4 gives the residue's determinant law and its
Pisano rhythm. Section 5 is the two-register breath — the residue read simultaneously in the
quantum and classical registers. Section 6 is the deepest: the *held breath*, the fixed locus of
the object under its own half-turn, which turns out to be exactly the torsion of the family.

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

**Theorem F3 (freezing through the golden degeneracy).** The members m = 1, 4, 11, 29, … — the
odd powers of φ (λ_m = φ^{1,3,5,7,…}) — all live in the same field ℚ(√5), and the norm −1 is
carried unbroken through the degeneracy. No imaginary quadratic field admits a unit of norm −1;
the residue is therefore a real-field phenomenon, and it cannot be quantized away.

The norm identity is the residue in its arithmetic dress. It says the object's handedness is not
an added structure but the *norm of its own growth rate*, forced by the shape x² − mx − 1 of the
recurrence. You cannot have the golden growth without the negative norm; the sign is in the seed.

---

## 4. The residue and the Pisano rhythm

**Theorem F4 (the determinant law).** Define the residue of a word w ∈ {R,L}* as
det(Par·W(w)) at level 15. Then residue(w) = −ω^{#L−#R}, ω = e^{2πi/3}: it depends only on the
letter imbalance mod 3, via the elementary determinants det W_R = ω̄, det W_L = ω, det Par = −1.
Balanced words (#R = #L) have residue −1 — *frozen*.

**Theorem F5 (the Pisano rhythm).** Along the Fibonacci letter tower (a → R, b → L), the imbalance
at rung k is ±F_{k−2}, so the residue cycles with the Fibonacci sequence mod 3 — with period
π(3) = 8, the Pisano period. The residue does not merely survive the tower; it *beats* along it,
in the object's own arithmetic rhythm.

This is the residue in its quantum dress. The same ℤ/2 that is the norm of the scale is the
determinant of the quantized word, and along the tower it acquires a heartbeat: a period-8 pulse
set by the golden recurrence reduced mod the Markov prime 3.

---

## 5. The two-register breath

**Theorem F6 (the two registers agree).** The quantum orientation det(Par@N) and the classical
orientation sign(σ acting on (ℤ/N)²) are equal, and both equal (−1)^{(N−1)/2} (Jacobi). At the
seam levels 15, 45, 75, 225 they breathe together: the residue read through the quantized operator
and the residue read through the classical map are the same sign, at every level.

The breath is the residue seen in two mirrors at once — the quantum and the classical — and the
theorem is that the mirrors agree. There is one orientation, and the two quantizations of the
object are two ways of reading it, never two values.

---

## 6. The held breath is torsion

The residue is what survives the object's motion. The final theorem asks what survives the object
*holding still* — the fixed locus under its own half-turn σ_m.

**Theorem F7 (held breath = torsion).** On the cusp locus κ = −2, the characters fixed by σ_m are
exactly the order-d torsion characters for divisors d ≥ 3 of m. The geometric (hyperbolic)
character is never fixed — it always breathes, exchanged by σ_m. What can hold still is precisely
the torsion: a generator of finite order d, with d | m, whose finite order makes σ_m act as the
swap a ↔ b, whose fixed locus is the symmetric characters. **Member m holds the breath of every
divisor d ≥ 3 of m.** The field of the held breath is Δ_d = τ_d²(τ_d² − 8), τ_d = 2cos(2π/d):
3 | m gives ℚ(√−7) (order 3), 5 | m gives ℚ(√41) (order 5); m ∈ {1,2,4} hold no breath at all.

The held breath is the object's orbifold skeleton — the elliptic points where a generator becomes
a rotation. The geometry breathes; the torsion holds. And the divisibility is exact: what a member
can hold still is the torsion of its divisors, no more and no less.

---

## 7. Method, mirrored

The program's method is its subject. To find the residue we did what σ does: we generated
everything the object touches and let the magnitudes cancel — the traces, the fields, the volumes,
the values — and watched for what would not go. What would not go was the sign. The residue is not
a result we added at the end; it is the fixed point of the whole procedure, the ℤ/2 that survived
the arithmetic (the norm), the quantization (the determinant), the two registers (the breath), and
the object's own stillness (the held breath). Cancel everything; what remains is real.

---

## 8. What is classical, and what remains open

Classical: units of norm −1 in real quadratic orders (Dirichlet); the Pisano period (Lagrange);
the Jacobi-symbol parity of the metaplectic determinant; the fixed-point theory of mapping-class
actions on character varieties. Ours (scoped, pending the gate): the three-register identification
of the residue (norm = determinant = parity as one ℤ/2); the Pisano-8 beat of the quantized word;
the held-breath-is-torsion theorem with its closed-form fields and the m ∈ {1,2,4} exception. Open:
(i) the standard-word lemma (chain words word-mirror for all k); (ii) the heredity of the chain's
torsion primes; (iii) whether the held-breath fields ℚ(√−7), ℚ(√41), … carry any further structure
beyond the order-d mechanism (each appearance requires its own reason — none is banked as
cumulative).

---

## Appendix: reproducibility

Norm identity `br_n_norm.py` (B469); the determinant law and Pisano rhythm `rf3_quantum.py`
(B470); the two-register breath `br1_br2.py` (B469); the held-breath theorem
`B479_held_breath_torsion/held_breath_capstone.py` (verified to order-13). Each lock re-run at
draft. The banked λ_chain value was independently re-verified as a genuine limit (not a
finite-rung artifact) during this paper's assembly; recorded in the corrections ledger.

---
*MSC 37B10, 11R11, 57K32, 11B39, 81Q50. Companion to Papers 1, 2, 4. Repository URL at packaging.*
