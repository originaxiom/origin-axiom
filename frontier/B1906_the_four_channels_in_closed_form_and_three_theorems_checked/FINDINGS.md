# B1906 — The four channels in closed form: the residue law by duplication (P-262), the pairing law proved (P-268), the zero law on every line (P-337), and three of the agy lane's theorems checked on main (P-747)

**Verdict: PROVED** (the identity derived and checked at 30 digits; the residues' zero law and P-268's law exact on every case;
det M's zero law on every line of order 1 to 12 at the three τ tried). cc (main), 2026-11-13 (S306p). Main's own derivation
and main's own code; the agy lane's statements were read through the mask and its code was not run. No data. No physical
quantity is computed or compared. **0 of 19.**

## 1. The answer first

- **The four channel kernels of B1656's coupling are products of two theta functions over θ₁, in closed form.** With
  ϑ(a, b; u) = thc(a, b, u, τ) (period τ), a± = a_x ± a_y and b± = (b_x ± b_y)/2 in main's twist coordinates, and
  e = e^{−2πi a_x}:

  | channel | P_s(u) · θ₁(u) |
  |---|---|
  | 1 | −i e · ϑ(a₊ + ½, b₊ + ½; u) · ϑ(a₋ + ½, b₋ + ½; 0) |
  | i | − ϑ(a₊ + ½, b₊; u) · ϑ(a₋ + ½, b₋; 0) |
  | j | − e · ϑ(a₊, b₊ + ½; u) · ϑ(a₋, b₋ + ½; 0) |
  | k | + i · ϑ(a₊, b₊; u) · ϑ(a₋, b₋; 0) |

  Checked against main's bilinear at 40 random points, Re τ outside the strip included: largest relative difference
  1.3 × 10⁻²⁹ at 30 digits. Three planted wrong forms fail (a missing half in b±, the phase of y instead of x, a missing
  half in a₋).
- **So each residue is a product of two theta constants,** one at (q_L + q_R)w and one at (q_L − q_R)w (P-262's "thetas
  at 3w and δw"; q_L + q_R = −3, 3, 3 in the up, down and lepton sectors), and each normalised kernel
  K_s = P_s/R_s = θ₁′(0) ϑ(c_s; u) / (ϑ(c_s; 0) θ₁(u)) depends only on its characteristic c_s mod ℤ².
- **The exact zero law of every residue:** R_s = 0 if and only if (q_L + q_R)w ≡ h_s or (q_L − q_R)w ≡ h_s modulo the
  lattice, with h₁ = 0, h_i = ½, h_j = τ/2, h_k = (1 + τ)/2. On every line of order 1 to 12, three sectors, four channels:
  3,192 of 3,192 agree.
- **B1703's zero at N ∣ 3 and B1701's 27 tied lines follow at once** (3w ∈ lattice gives R₁ = 0 in every sector; 3w a
  non-zero half period kills the one channel whose h_s it is).
- **P-268's law, written.** Where q_L w has exact order 4 and q_R w order at most 2, the channels pair, the partners'
  kernels have equal norms, and R_{s′}/R_s = ±i exactly, so D = Σ c_s R_s² = 0. Every line where the law applies has
  order 4 or 12, so the exact check on all of them (66 line-sectors, 132 pairs, every ratio ±i as a root of unity) is a
  proof for every case, given the identity.
- **The rectangular mirror (P-292, P-337):** at Re τ = 0 the norm is also invariant under (a, b) ↦ (−a, b), so channels
  whose characteristics lie in one orbit of (±a, ±b) have equal norms. **The prediction, written before the census ran:** D = 0 exactly where, grouping the live channels by the classes of the symmetry, each class's Σ R_s² vanishes. Computed from the norms themselves (B1716's instrument, which does not assume the symmetry), on every line of order 1 to 12 in three sectors: 798 of 798 agree at Im τ = 1.3 and 2.1 on Re τ = 0, and at a generic τ. Norms in one class agree to 3.6 × 10⁻¹². The zeros: D ≤ 3.0 × 10⁻¹³ where predicted; elsewhere D ≥ 6.8 × 10⁻⁵. **P-292's family is the 16 order-12 lines with 12α odd and 12β odd,** in the up and down sectors. The other 16 lines with 12α odd, where 12β is even, are not zeros. That is P-337's wording fix, and the agy lane's scoping of its fourth corollary, now computed on main.
- **The agy lane's Theorem E** (relay of 2026-11-07, read through the mask): its identity and its four residues have the
  same form as main's. Its R₁ and R_j are written with b₋ − ½ and e^{−2πi a_y}; by ϑ(a, b − ½) = e^{−2πi a} ϑ(a, b + ½)
  these are main's. Its digits and its counts of lines are behind the mask and were not compared.

## 1a. Seen first

`VERDICT topic-sweep /duplication|Szeg|zero law|rectangular mirror|P-337|P-292|spin structure.{0,20}channel/: 9 of 1644 arcs
on main match (NEGATIVE 3, PROVED 6); 10 register rows match (DECLINED 1, DONE 4, QUEUED 5)`. What bears on it: B1642 (the
zero modes' residue, the antisymmetric pairing), B1716 (det M = ¼ Σ c_s R_s², the rank-one residue matrix, the 0 : 1 : 1,
P-268's law computed, its "if" direction worked out by the referee), P-292 and P-404 (the Re τ = 0 zeros, merged into
P-337), P-337 (the zero law stated: c_s = c(3w + h_s), "every exact zero is isotropy plus the involution or the rectangular
mirror"). The web seat's note of 2026-11-03 on the channel norms claims the law derived; it is registered under P-337 and
not verified on main, and main did not read it for this arc. **Literature:** the product formula for theta functions with
characteristics and their quasi-periodicity; standard.

## 2. The derivation

Write Θ(a, b; u) = thc(a, b, u, 2τ) and ϑ(a, b; u) = thc(a, b, u, τ), thc(a, b, u, T) = Σₙ e^{iπT(n+a)² + 2πi(n+a)(u+b)}.

- **(F1) A half period of 2τ shifts the characteristic.** Θ(a, b; u + τ) = e^{−iπτ/2} e^{−iπ(u+b)} Θ(a + ½, b; u): complete the
  square in 2τ(n + a)² + 2τ(n + a).
- **(F2) The product formula.** ϑ(a₁, b₁; u₁) ϑ(a₂, b₂; u₂) = Σ_{ε=0,1} Θ((ε + a₁ + a₂)/2, b₁ + b₂; u₁ + u₂) Θ((ε + a₁ − a₂)/2,
  b₁ − b₂; u₁ − u₂): put p = n + a₁, r = m + a₂, use p² + r² = ((p + r)² + (p − r)²)/2, and note that n + m and n − m have
  the same parity, which is ε.
- **(P) Its inverse.** Shift b₁ and b₂ by ½: the first factor's b moves by 1, which multiplies the ε-term by (−1)^ε e^{iπ(a₁+a₂)}.
  Solving the two equations for the ε = 0 term:
  Θ(A, c; U) Θ(B, d; V) = ½ [ϑ(A + B, (c+d)/2; u₁) ϑ(A − B, (c−d)/2; u₂) + e^{−2πiA} ϑ(A + B, (c+d)/2 + ½; u₁) ϑ(A − B, (c−d)/2 + ½; u₂)],
  with u₁ = (U + V)/2 and u₂ = (U − V)/2.
- **B1656's bilinear** has entries X_m Y_n over θ₁(u), θ₁(u + τ) and its own phases, where X₀ = Θ(a_x, b_x; u) and X₁ = Θ(a_x, b_x;
  u + τ), and the same for Y. By (F1) X₁ is Θ(a_x + ½, …) times a phase; θ₁(u + τ) = −e^{−iπτ − 2πiu} θ₁(u). Every product has
  U = V = u, so u₁ = u and u₂ = 0, and (P) writes each entry with
  G₀₀ = ϑ(a₊, b₊; u) ϑ(a₋, b₋; 0), G₀₁ = ϑ(a₊, b₊ + ½; u) ϑ(a₋, b₋ + ½; 0), G₁₀ = ϑ(a₊ + ½, b₊; u) ϑ(a₋ + ½, b₋; 0),
  G₁₁ = ϑ(a₊ + ½, b₊ + ½; u) ϑ(a₋ + ½, b₋ + ½; 0):
  θ₁(u) · M = ½ [[G₀₀ + eG₀₁, −i(G₁₀ + eG₁₁)], [−i(G₁₀ − eG₁₁), −(G₀₀ − eG₀₁)]].
  (a₋ − ½ and a₋ + ½ give the same ϑ, since a moves by an integer.)
- **The pairings with εC_s** pick one G each: εC₁ = [[0, 1], [−1, 0]] gives M₀₁ − M₁₀; εC_i = [[0, −i], [−i, 0]];
  εC_j = −I; εC_k = diag(i, −i). That is the table of § 1.

**What follows from the table.**
- ϑ(a, b; 0) = 0 exactly when (a, b) ≡ (½, ½) mod ℤ² (θ[a, b] has one simple zero, at (½ − a)τ + (½ − b)). That is the zero
  law of the residues.
- K_s depends on c_s mod ℤ² only: an integer shift of a changes nothing, and an integer shift of b multiplies ϑ(c; u) and
  ϑ(c; 0) by the same phase.
- **K_{−c}(−u) = −K_c(u)** (n ↦ −n in the sum; θ₁ is odd), so the regularised norm, taken over a region symmetric under
  u ↦ −u (B1716's parallelogram and disc are), is the same for c and −c.
- **At Re τ = 0,** the conjugate of ϑ(a, b; ū) is ϑ(−a, b; u), θ₁ is real on the real structure, and θ₁′(0) is real; so the
  conjugate of K_{(a,b)}(ū) is K_{(−a,b)}(u), and since u ↦ ū keeps the rectangle and the disc, the norm is the same for
  (a, b) and (−a, b).
- **The residue matrix has rank one** (Z2) because every entry's residue is a product X_m(0)Y_n(0) times phases.

**P-268's law, the written proof.** Let x and y be the coordinates of q_L w and q_R w, with x of exact order 4 and 2y in
the lattice. Then d = x − y ≡ c = x + y, and 2c ≡ 2x =: h* is a non-zero half period. Since c_s = c + (½, ½) − h_s,
−c_s ≡ c_{s′} exactly when h_{s′} = h_s + h*: the four channels fall into two pairs, and the partners have equal norms by the
symmetry u ↦ −u. The ratio R_{s′}/R_s is κ_{s′}/κ_s times the phases that the three rules ϑ(a + n, b) = ϑ(a, b),
ϑ(a, b + n) = e^{2πian} ϑ(a, b) and ϑ(−a, −b; 0) = ϑ(a, b; 0) give, so it is a root of unity that can be computed exactly.
The law needs ord(q_L w) = 4; with q_L = 1 for the quarks and −3 for the leptons, w has order 4 or 12. So the lines of
order 1 to 12 contain every case, and on all of them the ratio is ±i (check E4). Then each pair contributes
A(R_s² + R_{s′}²) = 0, and D = 0.

## 3. The checks (`verification/`, main's code)

| | statement | result |
|---|---|---|
| E0 | the table, against B1656's bilinear (40 points × 4 channels) | 1.3 × 10⁻²⁹; three plants fail (2.2, 2.0, 5.1) |
| E1 | R_s = κ_s ϑ(c_s; 0) ϑ(d_s; 0)/θ₁′(0) against a contour mean on the bilinear; Σ R_s² = 0 | 2.6 × 10⁻³⁰ |
| E2 | the zero law of every residue, lines of order 1–12, three sectors, four channels | 3,192 of 3,192; zeros ≤ 2.9 × 10⁻²⁵, others ≥ 0.013 |
| E3 | q_L + q_R = −3, 3, 3; R₁ = 0 on the order-3 lines in every sector; the tied channel's residue on B1701's 27 lines | holds |
| E4 | P-268's law: on its 66 line-sectors every pair has R_{s′}/R_s = ±i exactly | 132 of 132 |
| E5 | the zero law of D on every line, at two τ on Re τ = 0 and one generic τ, from the norms themselves (`the_zero_law_on_every_line.py`, numpy, B1716's instrument) | 798 of 798 at each τ; zero lines: orders 4 (all sectors, 6 each) and 12 (leptons, 48) at every τ; at Re τ = 0 also order 12, up and down, 16 each, exactly the lines with 12α and 12β odd |

## 3a. Theorem C of the agy lane (P-606: B298's degree-2 obstruction), on main (`theorem_c_on_main.py`, exact)

- **Scoped, it holds:** a Galois orbit in a quadratic field has one or two elements, since the group has order 2.
- **Unscoped, B298's headline is false, three ways on m004** (K = ℚ(√−3)):
  - Riley's holonomy (x = [[1, 1], [0, 1]], y = [[1, 0], [−ω, 1]]) satisfies the figure-eight relation, and its image spans
    M₂(K): absolutely irreducible. The commutant of V ⊕ V ⊕ V has K-dimension 9, so a multiplicity of 3 is defined over the
    same field. With χ(x) = χ(y) = ω, the commutant of (χ ⊕ χ̄)^⊕3 has dimension 18. Controls: a wrong y breaks the
    relation; the commutant of V alone is 1.
  - The three non-zero classes of H¹(T²; 𝔽₂), the fibre's non-trivial spin characters, are one orbit under L and R, whose
    image is S₃ (6 elements).
  - O_K/(√−3) = 𝔽₃ (the norm is 3; (ω − 1)/√−3 has minimal polynomial z² − z + 1, so ω ≡ 1). Reduced there, x and y generate
    a group of order 24 with 7 classes and 3 linear characters: SL(2, 𝔽₃). Its other degrees are forced to be 2, 2, 2 and
    3, the only solution of the sum of squares. A 3 again.
- So P-606's verification is done. What it also asks, the scope addenda on B298 and B1161 and the corrected citations, is
  the record's work, for the builder.

## 3b. Theorem A of the agy lane, its level-1 part (P-318's item on B1228), on main (`level_one_on_main.py`, exact)

- For the sixteen simply-laced simple algebras of rank 1 to 8 at level 1, from the Cartan matrix alone: c = rank; the
  primaries are the classes of P/Q (|det C| of them); a class's weight is half its least norm (found by enumeration, and
  checked against the closed forms for A_n and D_n); the T-order is the lcm of the denominators of h − c/24.
- **σ = c/6 = 1 holds for A₆, D₆ and E₆** (T-orders 28, 4 and 12). So "σ = 1 picks E₆ uniquely" (B1228) is false as stated,
  as P-318 already says; **σ = 1 with exactly three primaries holds for E₆ alone.**
- SL(2, ℤ/4) has order 48 and seven elements of order 2; the binary octahedral group has order 48 and one (−1). They are not
  isomorphic.
- Theorem A's metallic part was verified at B1859. With this, the whole of Theorem A is verified on main.

## 3c. Theorem D, not computed

Theorem D classifies the lines on which the lepton spectrum equals the down spectrum. That is a statement about where a
lepton-to-down ratio is one, and such ratios are under the owner's hold on the targets (P-585, P-709). Main does not compute
it while the hold stands. The identity of § 2 would bear on it: the down and lepton sectors share q_L + q_R = 3, so their
kernels and norms are the same on every line, and they differ only through (q_L − q_R)w and the phase e.

## 4. What is not shown

- The identity is derived by hand from classical steps and checked numerically; it is not checked symbolically.
- The two symmetries of the norm are proved in two lines each above; E5 measures them (3.6 × 10⁻¹²).
- That D ≠ 0 off the law is numerical at the τ tried (as at B1716), not proved.
- The lane's own numbers are not compared: the mask hides them.
- The agy lane's note for P-321 (the abelian carrier and the prime selected by the orientation-reversing moves) is not
  checked here; it is still owed.

## 5. What it pays

- P-262: the residue law by duplication, with B1703's N ∣ 3 zero (its second half).
- P-268: the written proof of the "if" direction (the converse at generic τ stays numerical).
- P-747: Theorems A (with B1859), C and E verified on main's own code; D not computed under the hold; the P-321 note owed.
- P-606: verified; the record's addenda are the builder's.
- P-337 (with P-292 and P-404's merge): the zero law on every line of order 1 to 12, at the τ tried: every exact zero of D is a residue's isotropy plus the involution u ↦ −u, or, on Re τ = 0, the rectangular mirror. P-404's eight order-8 lines belong to another coupling (the Weinberg pair's) and are not in this census.

## Files

- `verification/the_duplication_identity.py` → `.json`, `_run.txt` (E0 to E4; mpmath, 30 digits; a few minutes).
- `verification/the_zero_law_on_every_line.py` → `.json`, `_run.txt` (E5; numpy; B1716's functions; about ten minutes).
- `verification/theorem_c_on_main.py`, `verification/level_one_on_main.py` → `.json`, `_run.txt` (exact; sympy).
- They import B1656's functions from `frontier/B1716_the_zeros_derived/verification/b1656_funcs.py` and write nothing else.
- The lock: `verification/test_b1906_the_four_channels.py`.

## Reproduce

```
cd frontier/B1906_the_four_channels_in_closed_form_and_three_theorems_checked/verification
python3 -B the_duplication_identity.py; python3 -B theorem_c_on_main.py; python3 -B level_one_on_main.py
python3 -B the_zero_law_on_every_line.py          # the longest
```
