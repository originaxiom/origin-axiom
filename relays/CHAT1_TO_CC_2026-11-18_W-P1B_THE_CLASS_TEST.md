# W-P1b: the class test. In the scope, no read-out a frame adopts depends on level 5's Weil class. Two candidates that B1953 prints do: its family Gramians over W's 3 and over W's 2. Covariance ties the labelling of the 24 points to the class, and on frame C the classes' Gramians differ. The iteration passes each class with its own labelling, and fails class 1 with the record's. The class and the labelling are one counted bit, and it is not the hand's

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. It is step 2 of card W-P1
(`relays/CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`, § 5), at the author's word of 2026-11-18.

**Order of work.** Each condition was committed before its script, and each script before its one run. One exception
is disclosed below.
- The condition: `relays/cards/CHAT1_W-P1_STEPS_conditions.md`, step 2 (522248fe8).
- `wp1b_class_test.py` (cd1c14c2e). Its output is at eefd793c5.
- `wp1b_labels.py`, committed at eefd793c5 before its run, with its output at c70a021c5. It had no condition of its own.
  It was written after C2's output had been read, and was committed together with it. J1 re-tests its result under a
  condition.
- Three follow-ups, each with its own condition in the same file. They were added when reading the scope's code found
  quantities the first run had not computed in both classes, and when W-P1b's first version left frame C open:
  - "the sweep's follow-up": condition 859f63845, `wp1b_followup.py` f302754cf, output eb7a7c963;
  - "the two Gramians": condition 317f82de8, `wp1b_gramians.py` 2ec9ed3ca, output 6ddbe8c6c;
  - "frame C's own Gramians in both classes": condition f36bf5b3b, `wp1b_frame.py` fdbbfd09a, output 0c6b24355;
  - "the direct tests", after the second read: condition 0bc0051b2, `wp1b_frame2.py` 795cc05dd, output c28ac330d. It
    was not blind: the read's own numbers were known when its condition was written.

**Typing.** [E] marks what the runs, the record or a standard result establish; [J] marks this seat's judgement.
Nothing here is compared with a measured value.
- Frame C is evaluated only in § 3a, with this seat's own transcription, under the author's ruling of 2026-11-15. That
  ruling lets the seat compute and print frame C's outputs, with nothing compared with data.
- Main's code is not run.

---

## 0. In short

1. **[E] In the scope, no read-out that a frame adopts depends on the class.** Each adopted read-out is a function of
   one of three things, and all three are the same in both classes:
   - End(W) as a G-module, the centre or the determinant;
   - a rational formula in ρ's entries with a rational value (§ 3, lemma 2);
   - charges, or quantities with no W in them.

   Some candidate quantities that are free of the class for every labelling are also listed: the phased sum, Parseval,
   and the existence of the split O = O₃ ⊕ O₂. The table in § 2 takes them arc by arc.
2. **[E] Where the class shows.**
   - (a) **On W alone:** the traces on the 24 elements of order 5 (G1), and what is read from them through a choice
     of fifth roots:
     - B1856's HQ3 angles and sector traces;
     - the triplet's T-exponents (B1923, B1934);
     - the traces of γ's even powers (C5).

     No frame reads any of these.
   - (b) **On W together with the frame's transport:**
     - which labellings of the 24 points by Weyl operators are covariant. For class 2 these are the four scalars,
       B1953's identity among them. For class 1 they are four diagonal matrices of non-square determinant, diag(1, 3)
       among them (J1). This restates W-A2 part B, main's R2, and B1955 § 2's third bullet with its
       `class_is_a_choice.py`, item 2, in the frame's own transport. R2 gives diag(1, 2) for the other class, which
       is diag(1, 3)⁻¹: the same identification taken in the other direction.
     - what is built from products of Weyl operators under that labelling: B1953's two family Gramians and O's
       singular values.
3. **[E] On frame C, B1953's two Gramians differ between the classes** (§ 3a). This is on this seat's transcription of
   frame C, at B1953's two base points, in both readings:
   - each class's operator, with its own labelling, is covariant under T: the W-side Gramian moves by ρ_a(T) to
     1.2e-13. The mismatched pairs fail by 0.11 to 0.30 (L1);
   - S₁ − S₂ exceeds S₁ in its largest entry, by 2.6 to 5.2 times;
   - the Gramians' ratios differ by up to 0.09 over the 3, and by up to 0.58 over the 2;
   - O's singular values, each over the largest, differ by 0.61 to 0.66 (L4).

   B1953 calls the Gramians covariant candidates, not read-outs (its "Not claimed"). Main's JOIN check
   (`physical_main01.py`) finds that, under its hypotheses (a gauge intertwiner), only the phased sum survives. The
   phased sum is free of the class.
4. **[E] Three of the record's sentences claim more than they show.**
   - **B1953, lines 74 and 75.** Its first sentence holds for even couplings: the scalings D(cw) are class 2's own
     labellings, and they give the same Gramians. Its "so the two Weil classes are not told apart" does not follow.
   - **B1953, lines 120 to 122.** "With the other identification of the labels the same operator transforms by the
     other class." The identity-labelled operator fails class 1 (G5). Class 1's operator is another one, with other
     Gramians on frame C.
   - **B1955's title and § 2's first bullet.** "The frame does not see the Weil class" holds for quantities linear in
     the lines, not for products of them.
5. **[E] The iteration tests the class and the labelling together.**
   - With each class's own labelling, both operators are covariant under γ for ten steps (J4, which is J1 iterated).
   - With the record's identity labelling, class 1 fails under γ itself: residual 1.9 (L2).
   - Given a labelling that passes, exactly one class passes it, so the iteration settles the class. It does not
     settle the pair.
   - Under γ alone, 20 labellings pass for each class and 440 pass neither; under T and S together, 4, 4 and 472 (L2).
     By the second read's check, G₃'s ratios depend only on the square class of det K.
6. **[E] The twin and the hand are not the class.**
   - The line's twin, v ↦ 2v, is the scalar 2, of determinant 4, a square. By J1 it is one of class 2's own
     labellings.
   - B1914's symmetries, ±JⁿKᵉ, have determinant ±1, both squares mod 5, so none changes the class. The ones that
     reverse the orientation exchange the twins.
   - B1923's exchange of the triplets is the scaling of the character ψ, which is the class change itself, not the
     twin.
   - The class is the square class of a; Ad(h) changes it by the square class of det h. The hand is the Legendre
     symbol of a symmetry's eigenvalue on the mark's line (B1934, line 44). On B1914's group the hand takes both
     values, while every determinant is a square: K = [[0, 1], [−1, 0]] has hand −1 and determinant +1. So the hand is
     not the class.
7. **[J] So the class, with the labelling, is one counted bit, and it is not the hand's.**
   - It moves no adopted read-out. It moves B1953's two candidate Gramians.
   - It would be fixed if frame C's labels are the fibre's translations (§ 4). That would be consistency with the
     fibre, not a test that the iteration imposes.

---

## 1. The construction and the runs

- **The representations.** ρ_a, a = 1 (the knot's x²/5) and a = 2 (the act's 2x²/5 with the cover's pairing):
  - ρ_a(T) = diag ζ^(ax²);
  - ρ_a(S) = cF with F[x, y] = ζ^(−2axy), and c fixed by S² = (ST)³.
  - Both are genuine on all 120 elements (C0).
- **The labels.** X and Z with XZ = ζ⁻¹ZX, and B1953's D(a, b) = ψ(3ab) XᵃZᵇ. The frame's transport is
  A(T): (a, b) → (a, b − a) and A(S): (a, b) → (−b, a). That is B1953's exact fact with B1951's ρ, which is class 2.

| item | result |
|---|---|
| C1 | in both classes: det ρ = 1 on all 120 elements; ρ(−I) = P; even/odd dimensions 3/2; commutant {I, P}; 6Y eigenvalues −2, −2, −2, 3, 3; ∣tr ρ(g)∣² = the points of 𝔽₅² that g fixes; the signature for W ⊗ W̄ is 1/5 |
| C2 | the classes move the labels by different permutations (2,656 of 3,000 element-label pairs differ) |
| C3, G1 | traces differ on 24 of 120 elements, exactly the 24 of order 5; they agree on every element of order 10; tr ρ₂(g) = tr ρ₁(hgh⁻¹), h = diag(2, 1) |
| C4 | tr ρ(γ²) = −√5 (class 1) and +√5 (class 2); det and ρ(−I) agree (the controls) |
| C5 | tr ρ_a(γᵏ), k = 1 to 10: 1 at odd k, ∓√5 at k = 2 and 8, ±√5 at k = 4 and 6, 5 at k = 10; the fixed line of ρ_a(γ) has dimension 1 and is even, in both |
| labels | in both classes the labels move linearly; each class's label action is K g K⁻¹ for four K, of non-square determinants (2, 3) for class 1 and squares (1, 4) for class 2 |
| G2 | ρ_a(LR) on the even sector: angles 0, 0.2, 0.8 and trace φ (class 1); 0, 0.4, 0.6 and 1 − φ (class 2, B1856's). On the odd sector: 0.3, 0.7 and 1 − φ; 0.1, 0.9 and φ |
| G3 | ρ_a(T)'s exponents on the triplet: {0, 1, 4} (class 1), {0, 2, 3} (class 2), as B1934 and B1923 |
| G4 | Frobenius–Schur indicators +1 (the 3) and −1 (the 2), images of orders 60 and 120, in both |
| G5 | B1953's two phase-free transports hold for class 2 (6.6e-16) and fail for class 1 (1.9) |
| J1 | the labellings K with ρ_a(g) D(Kv) ρ_a(g)⁻¹ = D(K A(g) v) and no phase: for class 2 the four scalars; for class 1 diag(1, 3), diag(2, 1), diag(3, 4) and diag(4, 2) |
| J2 | tr(D(v) P D(w)†) = ζ^(−3ω(v, w)), with ω(v, w) = v₁w₂ − v₂w₁, to 7.9e-16 |
| J3 | synthetic even couplings, seed 11: within a class the four K's Gramians agree to 1.1e-13; Parseval holds in both to 4.5e-13; between the classes G₃ differs (largest entry 174) by (√5/4)(S₁ − S₂) to 1.4e-13; G₃'s ratios are (0.7748, 0.6786) against (0.7624, 0.6636); in the control A(2w) = A(w) the classes agree to 5.8e-14 |
| J4 | ten steps of γ, each class with its own labelling: covariance residual at most 3.1e-14; G₃'s ratios move by at most 1.3e-15; A(γ)¹⁰ = I on the labels, the order being 10 because γ⁵ ≡ −I |
| K1–K3 | frame C: § 3a |

Every expectation set in the conditions was met, except one: step 2's expectation that B1953's read-outs are free of
the class "as their own pages say". What fails is B1953's own phrase, "these read-outs" (line 75): J3 and § 3a
contradict it for the two Gramians, which the page now calls candidates.

## 2. The sweep: every quantity in the scope, by arc

The classes are as the condition fixed them:
- (i) a function of End(W) as a G-module, of the centre, the commutant or the determinant;
- (ii) a function of End(W) as an algebra, here the labelling and products of Weyl operators;
- (iii) a function of W itself: traces, eigenphases, exponents.

"Adopted" means that a frame reads the quantity as its statement about matter or couplings. "Candidate" means a
quantity printed as a frame's output and not declared as its read-out.

| arc, quantity | class | both classes | adopted, candidate, or neither |
|---|---|---|---|
| B1856 HQ1: ρ(−I) is not scalar on ℂ⁵ and is scalar on each sector | (i) | same (C1) | its reading of the parity: adopted, class-free |
| B1856 HQ2: the projective commutant of ρ(LR) is ±⟨LR⟩ | group | same | the symmetry premise: class-free |
| B1856 HQ3: ρ(LR)'s angles and sector traces | (iii) | **differ** (G2) | neither. Its reading, "a ℤ/5 clock on every sector", holds in both, since every ratio is a primitive fifth root (G2) |
| B1856 HQ4: E(6) ≡ I; (LR)ᵏ not scalar on both sectors | group | same | the run of 6: class-free |
| B1923: scaling ψ by 2 exchanges 3 and 3′, read there as the line's twin | (iii) | **differ** by construction (G3) | neither: a lead. The twin, v ↦ 2v, is the scalar 2 of determinant 4 and keeps the class (J1); scaling ψ is the class change itself |
| B1934 (1): 3 + 2, determinant 1, a real triplet, the set of golden traces, −I on the 2 | (i), rational | same (C1, G4) | the dictionary: class-free |
| B1934 (1): the T-exponents on the triplet | (iii) | **differ** (G3) | neither. "The icosahedral triplet plays no role in frame C as built" (B1952, citing B1934 and B1935) |
| B1934 (2): the hand is the Legendre symbol at the mark | no W | same | the hand: a different invariant from the class (§ 0 item 6) |
| B1934 (3): leptons are down transposed mod N iff N divides 5 | charges | same | adopted, class-free |
| B1936: degrees k = 2·6Y mod 5; matter even, the Higgs odd; the Higgs-world candidate | charge arithmetic; its code builds no W | same | adopted or candidate, class-free |
| B1951 D1–D7: the group, P, commutant, 6Y, the centraliser of P, Λ^even, anomalies, Λ¹ | (i) | same (C1; B1951 says so) | the dictionary: class-free |
| B1952 A: the lines of 𝔽_p² fixed by LR | group | same | — |
| B1952 B: the Weyl operators move linearly; the match with B1724's transport | (ii) | linear in both; the identity match only in class 2 (labels, J1) | neither: it is the labelling |
| B1952 C: the fibre's degree-5 thetas carry X, Z and P | a realization | class 2 (main's R3) | neither |
| B1952 D: the Higgs direction's triplet against the Weil triplet's T-phases | (iii) for the Weil side | the printed Weil T-phases are class 2's and differ in class 1; the Higgs triplet is of level 8 | neither |
| B1952 E, F: the rivals' anomalies; the generation blocks on frame C | (i); frame | same | class-free |
| B1953 § 1: twist = degree; the 24 D's are a basis of sl(5); P D(v) P = D(−v); tr(D(v)P) = 1; 6Y = −½ Σ D(v) | label-free | same | class-free |
| B1953 § 1: the phase-free transports with B1951's ρ | (ii) | class 2 only (G5) | neither: the labelling |
| B1953 § 3: the law and its phase table; O's covariance; the split exists; Parseval; the phased sum | (ii) | the same table serves both (J1: no phase); the split exists in both, with different blocks; Parseval holds in both; the phased sum agrees, since tr(D(u)P) = 1 for every u | the phased sum is a candidate, the one main's JOIN keeps: class-free |
| **B1953 § 3–4: the two family Gramians, over the 3 and over the 2** | (ii), products | **differ by (√5/4)(S₁ − S₂)** (J3); **on frame C by up to 0.09 and 0.58 in their ratios** (§ 3a) | **candidates, printed as the frame's outputs** (B1953's "Not claimed", lines 135–136) |
| B1953 § 3: O's 15 singular values | (ii), products | their invariance under T holds for every labelling (§ 3a, K1). The values differ between the classes: on frame C by 0.61 to 0.66 in their ratios to the largest (L4); on synthetic couplings by 0.30 to 0.71 (the first referee's check) | neither: B1953 prints only their invariance |
| B1955 D: the classes' groups, det, ρ(−I) = P, ρ(LR) against multiples of P, the signature | (i), rational | same | — |
| B1955 D: the T-spectrum of the exterior powers | (iii) | differ in their fifth roots between the classes | neither |
| B1955 E: the knot's form x²/5 | not W | one realization of class 1 | neither |
| B1955 F: level 25, the act's roots, the up sector's phases | not level 5's W | — | — |
| `web_wa1_rest.py` 1: the other class needs another Fourier kernel | construction | — | neither |
| `web_wa1_rest.py` 2: Frobenius–Schur indicators and images | rational | same (G4) | neither |
| `web_wa1_rest.py` 3–7: anomalies, the mirror, the axis and the cone points, the frame's triplet at i, the scoreboard | no W | — | class-free |
| `web_review.py` R1: the candidate pairs | construction | — | neither |
| `web_review.py` R2: the label maps by class | (ii) | class 1's map differs by a non-square identification (R2's own output) | neither |
| `web_review.py` R3: the flux-5 modes, from T² and S | a realization | class 2 | neither |
| `web_review.py` R4, R5: the frame's phases, removed by one relabelling | frame | free of the class (J1: neither class's ρ adds a phase) | class-free |

**Outside the condition's scope.** The condition named two of main's checks. Main has others on W-A1 to W-A3, and they
are not swept here: `web_wa1_reps.py`, `web_wa2_readout.py`, `web_wa1_part3.py`, `web_wa1_h2.py` and
`web_wa1_star.py`. Main's JOIN check, `physical_main01.py`, uses a random family that is not even, with B1953's
identity labelling and no ρ. It finds that, under its hypotheses (a gauge intertwiner), only the phased sum survives.

## 3. The proof

**Lemma 1 [E].** End(W₁) ≅ End(W₂) as G-modules. ρ_a(−I) = P, the commutant is span{I, P}, and det ρ_a = 1 in both
classes.
*Proof:* C1. ∣tr ρ_a(g)∣² is the permutation character of 𝔽₅² in both, as in B1955 § 2. ∎

Every quantity of class (i) is therefore the same in both classes.

**Lemma 2 [E].** Let σ: ζ ↦ ζ² be the generator of Gal(ℚ(ζ₅)/ℚ). Then σ(ρ₁) = ρ₂ entry by entry. So a quantity given by
a formula with rational coefficients in ρ's entries is the same in both classes exactly when its value is rational.
*Proof:*
- σ(ρ₁(T)) = diag ζ^(2x²) = ρ₂(T), and σ(F₁) = F₂.
- The constant c is the ratio F²/(FT)³, an element of ℚ(ζ₅), so σ carries it along.
- Such a formula Q has Q(ρ₂) = σ(Q(ρ₁)), and σ fixes exactly ℚ. ∎

The first referee confirmed this in exact arithmetic for all 120 elements.

*Its scope.* An eigenvalue's angle, or its exponent as a fifth root, is not such a formula. Reading one picks an
embedding, ζ = e^(2πi/5), and σ changes the embedding. So the angles and the exponents can differ although they are
rational numbers.

**Proposition [E].** Among the quantities computed from ρ alone, these differ:
- the traces on the elements of order 5 (G1), whose values are irrational;
- the sector traces φ and 1 − φ (G2 computes them on LR; on the even sector ρ(LR) agrees with ρ(−LR), of order 5);
- what is read through the embedding: the angles and the T-exponents (G2, G3).

The rational-valued formulas agree: dimensions, orders, indicators, 6Y, the signature, "scalar or not", and "a
primitive fifth root". These carry all of B1856's, B1934's, B1951's and B1955's readings.

**Proposition [E, on W].** A quantity built from the frame's couplings and from Weyl operators falls outside Lemma 2,
because σ moves the operators' phases and not the couplings.
- Covariance under class a, with the frame's transport, forces the labelling D(Kw) with det K in the square class
  of 2a (J1).
- The phase table is the same in both classes, because ρ_a moves every D(Kw) with no phase.
- Then G₃ − G₂ = Σ ζ^(−3 det K·ω(v, w)) A(v)A(w)† (J2).
  - For even couplings, A(−w) = A(w), this is S₀ + cos(2π·3k/5)·S₁ + cos(2π·6k/5)·S₂, with k = det K.
  - The coefficients of S₁ and S₂ exchange between the square classes.
  - Frame C's couplings are even: B1953, line 54, and § 3a, K1.
- So the classes' G₃ differ by (√5/4)(S₁ − S₂), and G₂'s by its negative. As matrices they agree exactly when
  S₁ = S₂ (J3, both directions). For the eigenvalue ratios that B1953 prints, S₁ = S₂ is sufficient.
- Evenness matters. For odd couplings, even the four labellings within one class disagree (the first referee's
  check).
- G₃ + G₂ = 5 Σ A A† in both classes, so the plain Gramian agrees.
- tr_W(O·6Y) = −(5/2)F for every K, since tr(D(u)P) = 1 for every u. So the phased sum agrees. ∎

**Theorem [E].** In the scope:
- every read-out a frame adopts is the same in both Weil classes;
- B1953's two candidate Gramians differ between the classes on frame C (§ 3a);
- O's singular values differ between the classes on frame C (L4), as on synthetic couplings (the first referee's
  check).

**The bit [E, then J].**
- [E] The object carries both classes (B1955 § 2).
- [E] No symmetry of the bundle exchanges them. Ad(h) exchanges the classes exactly when det h is a non-square mod 5.
  This is standard; C3 tests h = diag(2, 1), and the first referee checked all 480 h. The bundle's symmetries lie in
  GL(2, ℤ) (B1914), whose determinants ±1 are both squares mod 5.
- [E] With its own labelling, each class passes the iteration's covariance (J4). With the record's labelling, class 1
  fails under γ (L2). As an argument: by J1, class 1 realises K·A(γ)·K⁻¹, and A(γ) = [[1, 4], [4, 2]] does not commute
  with diag(1, 3).
- [J] By the card's bins, the pair (class, labelling) is not shown to be an equivalence or a consistency. So, as it
  stands, it is one counted bit. Given either half, the other is settled. § 4 names how it could become a consistency.

## 3a. Frame C itself (W-P1b-H)

This seat's own transcription of frame C (W-F24's and W-F26's code, as W-A1 used it) gives the down coupling Y(τ, w).
- Its cA is computed by quadrature, where main uses a closed form (W-F24's docstring).
- The 24 points are w = (aτ + b)/5, with (a, b) integers mod 5, not both 0.
- A(w) = ζ^(−ab)·Y(τ, w), B1953's table.
- The end's tables are main's JSON, read as W-F24 reads them. At τ + 1 the end is held at L₂(τ), as the end is
  periodic under T, and the triplet is recomputed at τ + 1.

The labelling is B1953's. The second read compared the code: the transcription's characteristic at (a, b) is main's
`parts()` at (i/5, j/5), with the same table. It found Y(τ + 1, (a, b)) = Y(τ, (a, a + b)) to 1e-13, which is main's
transport for T. K1 alone could not detect a relabelling.

| τ, reading | K1: Y even | K1: O's singular values at τ + 1 against τ, class 2 / class 1 | K1: the plant, without the table | K2: ‖S₁ − S₂‖/‖S₁‖ | G₃'s ratios, class 2 / class 1 | G₂'s ratios, class 2 / class 1 |
|---|---|---|---|---|---|---|
| 0.13 + 1.70i, S | 1.7e-15 | 3.8e-14 / 1.6e-14 | 6.8e-2 / 6.8e-2 | 5.2 | (0.6375, 0.1471) / (0.7303, 0.1524) | (0.9275, 0.0718) / (0.3510, 0.1052) |
| 0.13 + 1.70i, S̃ | 2.0e-15 | 9.0e-14 / 3.9e-14 | 4.9e-2 / 4.8e-2 | 2.6 | (0.6160, 0.1492) / (0.6754, 0.1491) | (0.8696, 0.0691) / (0.6450, 0.1981) |
| 0.31 + 1.20i, S | 1.4e-15 | 2.3e-14 / 2.1e-14 | 1.2e-1 / 8.8e-2 | 2.8 | (0.7029, 0.5227) / (0.7718, 0.5412) | (0.8967, 0.1739) / (0.5744, 0.3500) |
| 0.31 + 1.20i, S̃ | 1.7e-15 | 2.0e-14 / 1.7e-14 | 1.0e-1 / 7.3e-2 | 3.1 | (0.6845, 0.5073) / (0.7514, 0.5220) | (0.8917, 0.1716) / (0.6020, 0.4196) |

- [E] **The transcription obeys B1953's law under T.** Y is even. O's singular values keep under T to 1e-13 for every
  labelling, since the D's are symmetric Weyl operators: K1 does not test the class. Without the table they move by
  4.8e-2 to 1.2e-1, the plant. So the table is needed.
- [E] **The class is tested directly (W-P1b-I, L1).** The W-side Gramian Γ = tr_families(O_K O_K†) at τ + 1 against
  ρ_a(T) Γ(τ) ρ_a(T)†:
  - I with class 2, and diag(1, 3) with class 1: within 1.2e-13;
  - the mismatched pairs: 0.11 to 0.30;
  - diag(1, 4), a square but not a scalar: 0.06 to 0.19 in both classes.

  S was not tested, since at −1/τ the end needs its own law (P-864).
- [E] **S₁ ≠ S₂ on frame C.** In the largest entry, their difference exceeds S₁ by 2.6 to 5.2 times.
- [E] **So B1953's two Gramians differ between the classes on frame C.** Their ratios differ by up to 0.09 over the 3,
  and up to 0.58 over the 2. The difference of the G₃'s equals (√5/4)(S₁ − S₂) to 6.4e-16.
- [E] The plain Gramian involves no labels, so it is the same in both classes. Parseval holds in each class to 2.6e-15
  (L3).
- [E] O's singular values, each over the largest, differ between the classes by 0.61 to 0.66 (L4). Class 1's fall
  faster at every point.
- The expectations set in the conditions (K1 to K3, L1 to L4) were met.
- Nothing here is compared with data or with any value on record. Main may compare this transcription with its own.

## 4. What it means

- [J] **The class is not inert for the record's candidates.** It is one bit: the square class of the labelling's
  determinant, relative to the class.
  - It moves no adopted read-out.
  - If the record ever reads the down sector through G₃ or G₂ separately, the class is an input of that read-out.
- [E] **B1953's choice is class 2's.** Its identity labelling is covariant only under class 2 (G5, J1, L1, L2).
  - B1934, line 37, says the Weil representation enters frame C only as the way its level-5 theta characteristics
    transform. So the frame's labels are characteristics, points of the fibre.
  - The fibre's translations by those points act on its degree-5 thetas as the Weyl operators with the canonical
    pairing (B1952 C). Those thetas carry class 2, as main's R3 shows from T² and S.
  - If the frame's point w is paired with the fibre's translation by w, up to a map of square determinant, then the
    labelling is fixed, and by J1 so is the class.
  - That would be consistency with the fibre, not a test the iteration imposes. Coordinate changes in GL(2, ℤ) have
    determinant ±1 and do no harm.
  - This seat has not checked the pairing. It is a question for main's frame code.
- [J] **At τ = i the classes may agree.** There S exchanges the mark and the twin (W-A1, I1). If A(2w) = A(w) holds
  there exactly as matrices, then S₁ = S₂. W-A1 compared ratios, not matrices. Not computed here.

## 5. For main (no data)

1. Check § 3a on main's own frame. On frame C, at B1953's base points, compute O with D(Kw) for K = diag(1, 3), its two
   Gramians and their ratios. This is one line in `weyl_operator.py`'s O. This seat's transcription gives the table
   in § 3a.
2. Mend the record's sentences, each scoped to quantities linear in the lines:
   - B1953, lines 74 and 75;
   - B1953, lines 120 to 122 ("the same operator");
   - B1955's title, § 2's first bullet, and the docstring of `class_is_a_choice.py`.
3. Mend the twin and the triplet:
   - B1923, § 0 and § 2: scaling ψ by 2 is the class change, not the line's twin, which is the scalar 2 and keeps the
     class;
   - B1934, lines 9 and 10 (which repeat B1923's sentence) and line 39 (the lead tying the triplets to the hand);
   - B1955 § 2, line 70: "only the T-phases on the 3 differ". The 2's T-exponents differ too, {1, 4} against
     {2, 3}, and so do the Gramians;
   - the verdict ledger's copy of B1955's title.
4. Say whether frame C's labels are the fibre's translations (§ 4). If they are, the class is fixed at 2 by
   consistency with the fibre. If they are not, the class is one counted bit, an input of B1953's two candidates.

## 6. Typed

- **[E] by the runs:** § 1's table; § 2's "both classes" column; § 3's lemmas and propositions; § 3a; § 0 items 1 to 6.
- **[E] by the record:**
  - each arc's quantity and its standing (§ 2), read at its page through the mask and at its code;
  - B1953's "Not claimed" and lines 54, 74–75 and 120–122;
  - B1955 § 2; B1934, lines 37 and 39; B1952's sentence on the icosahedral triplet;
  - main's R2, R3 and JOIN.
- **[E] standard:** the Galois conjugation of the Weil representation; Ad by a non-square determinant exchanges the
  classes.
- **[J]:** § 0 item 7; the bit's bin (§ 3); § 4, except its first [E] item.
- **Not done:** S on frame C; main's checks outside the condition's scope (§ 2).

## Files

- `relays/chat1_2026-11-18_wp1/`: `wp1b_class_test.py`, `wp1b_labels.py`, `wp1b_followup.py`, `wp1b_gramians.py`,
  `wp1b_frame.py` and `wp1b_frame2.py`, each with `_out.txt` and `_err.txt`; `SCRIPT_SHA256.txt`.
- The conditions: `relays/cards/CHAT1_W-P1_STEPS_conditions.md` (step 2 and its four follow-ups).
- Cited: B1856, B1914, B1923, B1934, B1936, B1951, B1952, B1953, B1955; `checks/web_wa1_rest.py`, `checks/web_review.py`
  and `checks/physical_main01.py`; W-A1 and W-A2 part B; W-F24 and W-F26 (the transcription); card W-P1 § 3.2.

## Provenance

The first version (de057886a) was read by a referee who had not written it. The verdict was sound with corrections.
The referee found the central result correct and new, and checked it independently: Lemma 2 in exact arithmetic,
Ad(h) over all 480 h, J1 with phases allowed, and the closed form for five seeds and other family sizes. Seven items
were required:
1. "The iteration fails neither class" holds only with each class's own labelling. With the record's labelling, γ's
   covariance fails class 1.
2. The tie of the class to the twin and the hand, which the condition asks for, was not examined.
3. The Gramians are B1953's candidates, not read-outs.
4. The proof's "det K in a's square class" was wrong; it is the square class of 2a.
5. Lemma 2 was applied beyond its scope, to angles and exponents.
6. The sweep missed O's singular values.
7. The record's sentences that need mending were incomplete: B1953's lines 120–122, and B1955's title, first bullet
   and docstring.

It also raised eleven smaller points:
- B1953's first sentence holds for even couplings, and frame C is even;
- checks outside the scope;
- "exactly two ways";
- what "the split" agreeing means;
- matrices against ratios;
- the standard source for Ad(h);
- the relation of w and 2w at τ = i;
- three refinements of § 4;
- `wp1b_labels.py`'s missing condition;
- table slips;
- rounding.

Each was checked at its source: B1953's lines 54, 74–75, 120–122 and 135–136; B1955 § 2; B1934, lines 37 to 39; and
B1914 and B1923; all through the mask. J1, G5 and J4 were checked in this seat's outputs. Three numbers on this page
are the first referee's and are marked as such: the 480 h, the odd couplings, and O's singular values on synthetic
couplings.

The corrected version (d7b64d3d4), with § 3a added, had a second read by another referee who had not written it. The
verdict was sound with corrections. The referee found that § 3a's script computes what its condition fixed, and
reproduced its output byte for byte. It confirmed the labelling against main's code, and found no adopted read-out on
record built from products of Weyl operators. Three items were required:
1. K1 does not test the class: O's singular values keep under T for every labelling. A direct test with ρ_a was
   needed.
2. "B1914's symmetries that exchange the twins have determinant −1" was false. K has determinant +1 and also exchanges
   them.
3. Class 1's failure under γ was inferred from T and S.

The three needed numbers, which this seat computed on its own committed script (W-P1b-I, L1 to L4) rather than taking
the read's. They agree with the read's: residuals of 1e-13 against 0.11 to 0.30; 1.9 under γ; and the counts of
labellings. Thirteen smaller points were also applied:
- the wording of "given the labelling";
- the hand against the class;
- the scope of the frame-C claims;
- the points written w = (aτ + b)/5;
- the plant's range;
- Parseval;
- O's singular values, now printed;
- the JOIN check's hypotheses and design;
- "in the scope";
- "not shown to be";
- [E] for B1953's choice;
- the mending list;
- R2's direction.

**Disclosed.** Reading B1953 in full through the mask, before § 3a's run, this seat saw B1953's printed frame outputs
(its lines 88 to 93), which the mask does not hide. The page compares nothing with them, as its condition says. Main may
make that comparison.

The read's corrections are applied in this version.

0 of 19.
