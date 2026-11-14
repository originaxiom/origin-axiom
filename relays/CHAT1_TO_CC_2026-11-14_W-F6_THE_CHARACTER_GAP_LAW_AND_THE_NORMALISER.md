# W-F6: two proofs. A fibre-non-trivial character's h¹ on any once-punctured-torus bundle is [χ(μ) = det], so at the det −1 levels the ±1 gaps number exactly the fibre torsion; and the normaliser of ⟨J_m²⟩ is ±J_mⁿKᵉ for every m

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free), proofs by hand, each with a computed
check. This note closes card W-F6 (`relays/cards/CHAT1_W-F6_the_character_gap_law_and_the_normaliser.md`, 3e13f5554).

**How it was checked.** The proofs are by hand (not independently checked). The checks were computed once, on this
seat's own code, with expectations committed first; both plants fired.
- **The sealed run.** The script (sha256 `96dfe5cb…e960b1b3`, pushed at 3e13f5554) was run once; its output was
  committed (20bef07ec) before it was read. All four expectations were met.
- **The method.** Exact ranks over two prime fields (9646561 and 17685361); the two give the same census. The helpers
  are W-C8 part 2a's, taken by text.

## 1. The gap law

**Setting.**
- G = F ⋊ ⟨t⟩, F = ⟨a, b⟩, with t f t⁻¹ = φ(f) and φ a hyperbolic automorphism.
- φ(λ) = gλˢg⁻¹, where λ = [a, b] and s = ±1 is the determinant of φ's abelianisation A.
- μ = g⁻¹t, and χ is a character of G with fibre part θ.

**Theorem.** If θ ≠ 1, then h¹(G; χ) = [χ(μ) = s], and the class is non-zero on λ. If θ = 1, then h¹(G; χ) = [χ = 1]
whenever χ(t) is not an eigenvalue of A. That holds for every χ of finite order in characteristic 0. Over F_p it holds
whenever χ(t) is not an eigenvalue of A mod p: for χ(t) of a fixed order N, p outside a finite set depending on N.
The referee found the failure at this run's own prime: at golden level 1 with p = 9646561, χ(t) = 9471113 (a root of
x² − x − 1) gives θ = 1, χ ≠ 1 and h¹ = 1. The run's random t-values did not meet it.
The relation φ(λ) = gλˢg⁻¹ with s = det holds for every automorphism of F₂ (Nielsen); the θ ≠ 1 part needs no
hyperbolicity. The counts below also assume characteristic ≠ 2, the e-th roots of unity in the field, and
characteristic prime to |T|, all automatic over ℂ.

**Proof.**
1. **The line on the fibre (B1506 T1).** For θ ≠ 1:
   - Z¹(F; θ) is free on (c(a), c(b)), and B¹ is the line through (θ(a) − 1, θ(b) − 1).
   - The functional c(λ) = (1 − θ(b))c(a) + (θ(a) − 1)c(b) is non-zero and vanishes exactly on B¹.
   - So H¹(F; θ) is a line detected by c(λ).
2. **The action of t.** Let c be a cocycle of G and z its restriction to F.
   - From t f t⁻¹ = φ(f): z(φ(f)) = χ(t)z(f) + (1 − θ(φ f))c(t).
   - At f = λ, where θ(λ) = 1, this gives z(φ(λ)) = χ(t)z(λ).
   - Also z(gλˢg⁻¹) = s·θ(g)·z(λ).
   - So t acts on the line H¹(F; θ) by χ(t)⁻¹·s·θ(g) = s·χ(μ)⁻¹.
3. **The Wang sequence.** 0 → H¹(⟨t⟩; H⁰(F; χ)) → H¹(G; χ) → H¹(F; χ)^t → 0.
   - For θ ≠ 1, H⁰(F; χ) = 0. So H¹(G; χ) is the t-invariant part of the line: 1-dimensional exactly when
     χ(μ) = s, and then its class restricts to one non-zero on λ.
   - For θ = 1, H¹ = coker(χ(t) − 1) ⊕ {z ∈ Hom(F, K) : z∘φ = χ(t)z}. The second summand is non-zero only when χ(t) is
     an eigenvalue of A. A hyperbolic A has no eigenvalue that is a root of unity, so for χ of finite order, in
     characteristic 0, the sum is [χ(t) = 1]. ∎

**Corollary (part 5's regularity, now proved by hand; not independently checked).** Take w(t) = s, w = 1 on F. Then χ* ⊗ w = χ⁻¹w and
(χ⁻¹w)(μ) = s·χ(μ)⁻¹, so h¹(χ⁻¹w) = [χ(μ) = 1]. Hence:
- for θ ≠ 1, gap(χ) = h¹(χ) − h¹(χ* ⊗ w) = [χ(μ) = s] − [χ(μ) = 1];
- gap(1) = −gap(w) = [s = −1].

For each θ ≠ 1 there is exactly one χ with χ(μ) = −1 and one with χ(μ) = +1. So:
- **at s = −1**, the characters with gap +1, and those with gap −1, number exactly |T|, the fibre torsion. Those with
  +1 are the trivial character and the χ(μ) = −1 ones; those with −1 are w and the χ(μ) = +1 ones. This is part 2a's
  G4 identification;
- **at s = +1**, every character's gap is 0, and the record's data (θ ≠ 1, χ(μ) = 1, a class with c(λ) = 1) number
  |T| − 1;
- B1438's recipe at orientable levels, and part 2a's bar at the Klein-bottle levels (no class when χ(μ) = 1 and
  s = −1), are both special cases.

**The computed check (G1, G2).** The law held on every character computed, with t-values the 2e-th roots of unity and 3
further elements of F_p* per fibre part:
- the golden tick, levels 1 to 8 (5 to 1,769 characters per level);
- the silver tick (m = 2), levels 1 to 4;
- the bronze tick, levels 1 to 3;
- φ_A = R∘L∘L (trace 4, det +1, not metallic), levels 1 to 3;
- φ_B = P∘R∘L∘L, levels 1 to 3. φ_B was meant as a non-metallic case with det −1, but its abelianisation
  [[1, 3], [1, 2]] has the bronze tick's trace and determinant (3, −1) and is conjugate in GL(2, ℤ) to J₃ (so, Out(F₂)
  being GL(2, ℤ), its mapping tori are the bronze tick's), and its fibre torsion matches bronze's (3, 9, 36). **So it is not a non-metallic
  test.** The only non-metallic monodromy checked is φ_A, which is orientable.

The gap counts (G2) at s = −1:

| tick | levels | count each sign |
|---|---|---|
| golden | 1, 3, 5, 7 | 1, 4, 11, 29 |
| silver | 1, 3 | 2, 14 |
| bronze | 1, 3 | 3, 36 |
| φ_B | 1, 3 | 3, 36 |

At s = +1 every gap was 0, and the record's data numbered |T| − 1: golden 0, 4, 15, 44 at levels 2, 4, 6, 8; silver 3, 31;
bronze 8; φ_A 1, 11, 49; φ_B 8.

Plant GP (the law with −s in place of s) failed on levels of both signs.

## 2. The normaliser

**Theorem.** For every m ≥ 1, with J = J_m = [[m, 1], [1, 0]], A = J² and K = [[0, 1], [−1, 0]]:
- the centraliser of A (and of J) in GL(2, ℤ) is ±⟨J⟩;
- the normaliser of ⟨A⟩ is {±JⁿKᵉ}.

**Proof.**
1. **The centraliser is ℤ[J].** e₂ is a cyclic vector of J (Je₂ = e₁). So a matrix commuting with J is determined by
   its value on e₂, and equals aI + bJ. A commutes with X exactly when J does, since A = mJ + I.
2. **Units.** aI + bJ is invertible over ℤ exactly when N(a + bx) = a² + mab − b² = ±1, where x = (m + √(m² + 4))/2 > 1
   and x' = −1/x. Suppose ε = a + bx is a unit with 1 < ε < x.
   - Then |ε'| = 1/ε < 1 and b(x − x') = ε − ε' lies in (0, x + 1).
   - Since x + 1 < 2(x + 1/x) = 2(x − x'), this forces b = 1.
   - Then a = ε − x < 0, and N = ±1 gives a(a + m) ∈ {0, 2}.
   - a = −m gives ε = 1/x < 1. a(a + m) = 2 with a < 0 needs a + m < 0, and then ε ≤ 1/x − 1 < 0.
   - So no unit lies in (1, x); x is the fundamental unit, and the units are ±xⁿ.
3. **The normaliser.** KJK⁻¹ = [[0, −1], [−1, m]] = −J⁻¹, so KAK⁻¹ = A⁻¹.
   - A g normalising ⟨A⟩ ≅ ℤ acts on it by an automorphism, so gAg⁻¹ = A or A⁻¹.
   - A g with gAg⁻¹ = A lies in ±⟨J⟩.
   - A g with gAg⁻¹ = A⁻¹ has K⁻¹g in the centraliser.
   - So the normaliser is ±⟨J⟩ ∪ K(±⟨J⟩) = {±JⁿKᵉ}. ∎

The card wrote "the normaliser of ⟨J_m⟩". That normaliser is only ±⟨J_m⟩, since KJK⁻¹ = −J⁻¹ ∉ ⟨J⟩ and
tr J⁻¹ = −m ≠ m. The claim is for ⟨A⟩ = ⟨J²⟩, the act's group. (In this section A is J²; in § 1 it is φ's
abelianisation.)

**The computed check (N1, N2).** For m = 1 to 60:
- the integer solutions of a² + mab − b² = ±1 with |a|, |b| ≤ 2000 are exactly the ±xᵏ in that box;
- KJK⁻¹ = −J⁻¹ and KAK⁻¹ = A⁻¹;
- among ±Jᵏ with |k| ≤ 20, only J and −J⁻¹ have trace m and determinant −1.

Plant NP (the units taken as ±⟨x²⟩) missed solutions for every m.

## 3. What it means for the system (W-C8 part 4's page)

- **Line 5 (the act and the tick).** The normaliser ±J_mⁿKᵉ (of ⟨A⟩) was open beyond m = 5. It now has a proof by
  hand for every m (not independently checked), with a computed check for m = 1 to 60. With part 1's hand law
  (−1)ⁿ⁺ᵉ for every odd m, line 5 rests on proofs by hand for every odd m, with computed checks for the m computed.
- **Line 7 (the index), on characters.** The twisted gap now has a proof by hand (not independently checked) for every
  hyperbolic monodromy and level, on characters of finite order in characteristic 0:
  - on characters, it is non-zero only at s = −1 (the non-orientable levels), with exactly |T| characters of each
    sign;
  - and, on the orientable levels, the record's data number |T| − 1.
  - The doublets' class index ("non-zero only on orientable levels") stays open beyond the levels computed.
- **Part 3's reading.** Part 3 found two observables that do not vanish at odd ticks; one of them, the characters' h¹
  gaps, now has an exact law, proved by hand (not independently checked). At an odd tick the gaps sit on the χ(μ) = ±1 characters, which W-F4 shows are the
  double cover's matter (the twisted ones) and their untwisted partners.

## 4. Typed

| statement | how checked |
|---|---|
| the gap law and its corollary, every hyperbolic monodromy and level | not independently checked (by hand) |
| G1, G2 on the monodromies and levels named | computed once; expectations committed first; tested against planted errors (1, caught) |
| the normaliser theorem, every m | not independently checked (by hand) |
| N1, N2 for m = 1 to 60 | computed once; expectations committed first; tested against planted errors (1, caught) |
| φ_B is not a non-metallic test | its fibre torsion and determinant: computed once; its trace (3, the bronze tick's) and its conjugacy to J₃: not independently checked (by hand) |

## 5. Files

`relays/chat1_2026-11-14_wf6/`: `wf6_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf6_checks_out.txt`,
`wf6_checks_err.txt` (empty).

This note was read by one session before it was pushed; its corrections are applied. The referee also recomputed the
law independently, in characteristic 0 on its own code (golden levels 1 to 5, bronze 1 and 2, φ_A 1, φ_B 1 and 2), and
N1 by brute force for m = 1 to 10; all agree. NP is weak: ±⟨x²⟩ never contains x, so it fires by construction.

0 of 19.
