# W-P1b: the class test. Every read-out on record but one is the same in both Weil classes. The exception is B1953's two family Gramians, over W's 3 and over W's 2: covariance ties the labelling of the 24 points to the class, and the Gramians depend on the labelling's square class. On synthetic couplings they differ by (√5/4)(S₁ − S₂); on frame C that is one computation on main. B1953's argument that they do not differ uses class 2's own labellings. The iteration over one period fails neither class, so the class is a counted choice

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` data-free. It is step 2 of card W-P1
(`relays/CHAT1_TO_CC_2026-11-18_W-P1_THE_PROCESS_READING.md`, § 5), at the author's word of 2026-11-18.

**Order of work.** Each condition was written and committed before its script, and each script before its one run.
- The condition: `relays/cards/CHAT1_W-P1_STEPS_conditions.md`, step 2 (522248fe8).
- `wp1b_class_test.py` (cd1c14c2e), and its output (eefd793c5).
- `wp1b_labels.py` (eefd793c5), and its output (c70a021c5).
- Two follow-ups, each with its own condition in the same file. They were added when reading the scope's code found
  quantities the first run had not computed in both classes:
  - "the sweep's follow-up": condition 859f63845, `wp1b_followup.py` f302754cf, output eb7a7c963;
  - "the two Gramians": condition 317f82de8, `wp1b_gramians.py` 2ec9ed3ca, output 6ddbe8c6c.

**Typing.** [E] marks what the runs or the record establish; [J] marks this seat's judgement. Nothing here is compared
with a measured value. No frame is run: the frame's quantities are read from main's code and pages, and J3 uses
synthetic couplings.

---

## 0. In short

1. **[E] Every read-out on record in the scope is the same in both classes, except one family.** Each is a function of
   one of these:
   - End(W) as a G-module, the centre or the determinant, which agree in both classes;
   - a rational number computed from ρ alone, and such a number is the same in both classes (§ 3, lemma 2).

   The table in § 2 takes them arc by arc.
2. **[E] On W itself, the class shows in exactly two ways.**
   - (a) The traces on the 24 elements of order 5 (G1), and what is built from them:
     - B1856's HQ3 angles and sector traces;
     - the triplet's T-exponents (B1923, B1934);
     - the traces of γ's even powers (C5).

     No frame reads any of these.
   - (b) Which labellings of the 24 points by Weyl operators are covariant. For class 2 these are the four scalars,
     B1953's labelling among them. For class 1 they are four diagonal matrices of non-square determinant, such as
     diag(1, 3) (J1). This restates W-A2 part B, main's R2 and B1955 § 2, item 2, in the frame's own transport.
3. **[E on W; open on frame C] (b) is read by B1953's two family Gramians,** W traced over its 3 and over its 2.
   - Their sum is 5 times the plain Gramian in both classes (Parseval), so the sum does not depend on the class.
   - Nor do the phased sum (the hypercharge component) and the split O = O₃ ⊕ O₂.
   - Their difference does depend on the labelling. On synthetic even couplings, G₃(class 1) − G₃(class 2) =
     (√5/4)(S₁ − S₂) to 1e-13. Here S_j is the sum of A(v)A(w)† over the pairs of points whose symplectic product is
     ±j.
   - The two agree when A(2w) = A(w), the control. On frame C, whether S₁ = S₂ is one computation on main's frame.
4. **[E] B1953, lines 74 and 75, does not show what it says.** Its scalings D(cw), for c = 2, 3 and 4, are class 2's own
   covariant labellings (J1), so they cannot tell the classes apart. No code on record computes them.
5. **[E] The iteration over one period fails neither class.**
   - Both classes' operators stay covariant under γ for ten steps, and γ's label action has order 10 (J4).
   - G₃'s ratios are unchanged along the way.
   - ρ_a(γ) has a one-dimensional even fixed line in both classes (C5).
   - Its traces differ only at γ's even powers below the tenth, by sign.
   - No element of GL(2, ℤ) exchanges the classes: ±1 are squares mod 5.
6. **[J] So the class is a counted choice, and it may not be inert.**
   - Class 2 comes from the cover's pairing and from the fibre's flux-5 modes; class 1 from the knot's discriminant
     form (B1955; card W-P1, § 3.2). B1953's labelling is class 2's.
   - If S₁ ≠ S₂ on frame C, the choice moves B1953's two Gramians. If S₁ = S₂, it moves no read-out on record.

---

## 1. The construction and the runs

- ρ_a, a = 1 (the knot's x²/5) and a = 2 (the act's 2x²/5 with the cover's pairing):
  - ρ_a(T) = diag ζ^(ax²);
  - ρ_a(S) = cF with F[x, y] = ζ^(−2axy), and c fixed by S² = (ST)³.
  - Both are genuine on all 120 elements (C0).
- The labels: X and Z with XZ = ζ⁻¹ZX, and B1953's D(a, b) = ψ(3ab) XᵃZᵇ. The frame's transport is
  A(T): (a, b) → (a, b − a) and A(S): (a, b) → (−b, a), which is B1953's exact fact with B1951's ρ, the class-2 one.

| item | result |
|---|---|
| C1 | in both classes: det ρ = 1 on all 120 elements; ρ(−I) = P; even/odd dimensions 3/2; commutant {I, P}; 6Y eigenvalues −2, −2, −2, 3, 3; ∣tr ρ(g)∣² = the points of 𝔽₅² that g fixes; the signature for W ⊗ W̄ is 1/5 |
| C2 | the labels move linearly in both classes, by different maps (2,656 of 3,000 element-label pairs differ) |
| C3, G1 | traces differ on 24 of 120 elements, exactly the 24 of order 5; they agree on every element of order 10; tr ρ₂(g) = tr ρ₁(hgh⁻¹), h = diag(2, 1) |
| C4 | tr ρ(γ²) = −√5 (class 1) and +√5 (class 2); det and ρ(−I) agree (the controls) |
| C5 | tr ρ_a(γᵏ), k = 1 to 10: 1 at odd k, ∓√5 at k = 2 and 8, ±√5 at k = 4 and 6, 5 at k = 10; the fixed line of ρ_a(γ) has dimension 1 and is even, in both |
| labels | each class's label action is K g K⁻¹ for four K: non-square determinants (2, 3) for class 1, squares (1, 4) for class 2 |
| G2 | ρ_a(LR) on the even sector: angles 0, 0.2, 0.8 and trace φ (class 1); 0, 0.4, 0.6 and 1 − φ (class 2, B1856's). The odd sector: 0.3, 0.7 and 1 − φ; 0.1, 0.9 and φ |
| G3 | ρ_a(T)'s exponents on the triplet: {0, 1, 4} (class 1), {0, 2, 3} (class 2), as B1934 and B1923 |
| G4 | Frobenius–Schur indicators +1 (the 3) and −1 (the 2), images of orders 60 and 120, in both |
| G5 | B1953's two phase-free transports hold for class 2 (6e-16) and fail for class 1 (1.9) |
| J1 | the labellings K with ρ_a(g) D(Kv) ρ_a(g)⁻¹ = D(K A(g) v), with no phase: class 2 the four scalars; class 1 diag(1, 3), diag(2, 1), diag(3, 4), diag(4, 2) |
| J2 | tr(D(v) P D(w)†) = ζ^(−3ω(v, w)), ω(v, w) = v₁w₂ − v₂w₁, to 8e-16 |
| J3 | synthetic even couplings, seed 11: within a class the four K's Gramians agree to 1e-13; Parseval in both to 5e-13; between the classes G₃ differs (largest entry 174), equal to (√5/4)(S₁ − S₂) to 1e-13; G₃'s ratios (0.7748, 0.6786) against (0.7624, 0.6636); the control A(2w) = A(w): the classes agree to 6e-14 |
| J4 | ten steps of γ, both classes: covariance residual at most 3e-14; G₃'s ratios move by at most 1e-15; A(γ)¹⁰ = I and ρ_a(γ)¹⁰ = I |

Every expectation set in the conditions was met, except step 2's expectation that B1953's read-outs are class-invariant
"as their own pages say". J3 contradicts that for the two Gramians on synthetic couplings.

## 2. The sweep: every quantity in the scope, by arc

Classes as the condition fixed them:
- (i) a function of End(W) as a G-module, of the centre, the commutant or the determinant;
- (ii) a function of End(W) as an algebra, here the labelling and products of Weyl operators;
- (iii) a function of W itself: traces, eigenphases, exponents.

"Read" means a frame reads it as a statement about matter or couplings.

| arc, quantity | class | both classes | read by a frame |
|---|---|---|---|
| B1856 HQ1: ρ(−I) scalar on ℂ⁵, on each sector | (i) | same (C1) | its reading of the parity |
| B1856 HQ2: the projective commutant of ρ(LR) is ±⟨LR⟩ | group | same | the symmetry premise |
| B1856 HQ3: ρ(LR)'s angles and sector traces | (iii) | **differ** (G2) | no: its reading, "a ℤ/5 clock on every sector", holds in both (every ratio is a primitive fifth root, G2) |
| B1856 HQ4: E(6) ≡ I; (LR)ᵏ non-scalar on both sectors | group | same | the run of 6 |
| B1923: the twin's scaling exchanges 3 and 3′ | (iii) | **differ** by construction (G3) | no: entered as a lead |
| B1934 (1): 3 + 2, determinant 1, real triplet, the set of golden traces, −I on the 2 | (i), rational | same (C1, G4) | the dictionary |
| B1934 (1): T-exponents on the triplet | (iii) | **differ** (G3) | no: "the icosahedral triplet plays no role in frame C as built" (B1952, citing B1934 and B1935) |
| B1934 (2): the hand is the Legendre symbol at the mark | no W | same | the hand |
| B1934 (3): leptons are down transposed mod N iff N divides 5 | charges | same | yes, class-free |
| B1936: degrees k = 2·6Y mod 5; matter even, Higgs odd; the Higgs-world candidate | (i), via 6Y | same (C1) | yes, class-free |
| B1951 D1–D7: the group, P, commutant, 6Y, the centraliser of P, Λ^even, anomalies, Λ¹ | (i) | same (C1; B1951 says so) | yes, class-free |
| B1952 A: the lines of 𝔽_p² fixed by LR | group | same | — |
| B1952 B: the Weyl operators move linearly; the match with B1724's transport | (ii) | linear in both; the identity match only in class 2 (labels, J1) | no: it is the labelling itself |
| B1952 C: the fibre's degree-5 thetas carry X, Z and P | a realization | class 2 (main's R3) | no |
| B1952 D: the Higgs direction's triplet against the Weil triplet | — | the Higgs triplet is of level 8, not 5 | no Weil class read |
| B1952 E, F: the rivals' anomalies; the generation blocks on frame C | (i); frame | same | class-free |
| B1953 § 1: twist = degree; 24 D's a basis of sl(5); P D(v) P = D(−v); tr(D(v)P) = 1; 6Y = −½ Σ D(v) | label-free | same | yes, class-free |
| B1953 § 1: the phase-free transports with B1951's ρ | (ii) | class 2 only (G5) | no: the labelling |
| B1953 § 3: the law and its phase table; O's covariance; the split O₃ ⊕ O₂; Parseval; the phased sum | (ii) | the same table in both (J1: no phase); the split, Parseval and the phased sum agree | yes, class-free |
| **B1953 § 3–4: the two family Gramians, over the 3 and over the 2** | (ii), products | **differ by (√5/4)(S₁ − S₂)** (J3) | **yes: printed as the frame's outputs** |
| B1955 D: the classes' groups, det, ρ(−I) = P, ρ(LR) against multiples of P, the signature | (i), rational | same | — |
| B1955 E: the knot's form x²/5 | not W | one realization of class 1 | no |
| B1955 F: level 25, the act's roots, the up sector's phases | not level 5's W | — | — |
| `web_wa1_rest.py` 1: the other class needs another Fourier kernel | construction | — | no |
| `web_wa1_rest.py` 2: Frobenius–Schur indicators and images | rational | same (G4) | no |
| `web_wa1_rest.py` 3–7: anomalies, the mirror, the axis and the cone points, the frame's triplet at i, the scoreboard | no W | — | class-free |
| `web_review.py` R1, R2: the candidate pairs; the label maps by class | (ii) | the class-1 map differs by a non-square identification (R2's own output) | no |
| `web_review.py` R3: the flux-5 modes | a realization | class 2 | no |
| `web_review.py` R4, R5: the frame's phases, removed by one relabelling | frame | class-free (J1: no phase from ρ in either class) | yes, class-free |

## 3. The proof

**Lemma 1 [E].** End(W₁) ≅ End(W₂) as G-modules. ρ_a(−I) = P, the commutant is span{I, P}, and det ρ_a = 1 in both
classes. *Proof:* C1. ∣tr ρ_a(g)∣² is the permutation character of 𝔽₅² in both, as in B1955 § 2. ∎ Every quantity of
class (i) is therefore the same in both classes.

**Lemma 2 [E].** Let σ: ζ ↦ ζ² be the generator of Gal(ℚ(ζ₅)/ℚ). Then σ(ρ₁) = ρ₂ entry by entry. A quantity given by
a rational formula in ρ's entries is therefore the same in both classes exactly when its value is rational.
*Proof:*
- σ(ρ₁(T)) = diag ζ^(2x²) = ρ₂(T), and σ(F₁) = F₂.
- The constant c is the ratio F²/(FT)³, an element of ℚ(ζ₅), so it is carried along with them.
- A formula Q has Q(ρ₂) = σ(Q(ρ₁)), and σ fixes exactly ℚ. ∎

**Proposition [E].** Among the quantities computed from ρ alone, those that differ are of class (iii) with irrational
values:
- the traces on the elements of order 5 (G1);
- the sector traces φ and 1 − φ on them (G2 computes them on LR; on the even sector ρ(LR) agrees with ρ(−LR), of
  order 5);
- the choice of fifth roots: angles and exponents (G2, G3).

The labelling, class (ii), is not computed from ρ alone; J1 gives it.

The rational ones agree: dimensions, orders, indicators, 6Y, the signature, "scalar or not", and "a primitive fifth
root". These are all of B1856's, B1934's, B1951's and B1955's readings.

**Proposition [E, on W].** A quantity built from the frame's couplings and from Weyl operators is a different matter.
Lemma 2 does not reach it, because σ moves the operators' phases and not the couplings.
- Covariance under class a forces the labelling D(Kw) with det K in a's square class (J1). The phase table is the same
  in both classes, because ρ_a moves every D(Kw) with no phase.
- Then G₃ − G₂ = Σ ζ^(−3 det K·ω(v, w)) A(v)A(w)† (J2). For even couplings this is S₀ + cos(2π·3k/5)·S₁ +
  cos(2π·6k/5)·S₂, with k = det K. The coefficients of S₁ and S₂ exchange between the square classes.
- So the classes' G₃ differ by (√5/4)(S₁ − S₂), and agree if and only if S₁ = S₂ (J3, both directions).
- G₃ + G₂ = 5 Σ A A† in both. So the plain Gramian, the phased sum (tr_W(O·6Y) = −(5/2)F for every K) and the split
  agree. ∎

**Theorem [E for the record's pages and code; the one open item named].**
- Every read-out on record in the scope is the same in both Weil classes, except B1953's two family Gramians taken
  separately.
- Those agree between the classes exactly when frame C's down coupling satisfies S₁ = S₂.

**The counted choice [E, then J].**
- [E] The object carries both classes (B1955 § 2).
- [E] No element of GL(2, ℤ) exchanges them: Ad(h) exchanges them exactly when det h is a non-square mod 5 (C3, with
  h = diag(2, 1)), and integral matrices have det ±1, both squares.
- [E] The golden iteration imposes no test that one class fails (J4, C5).
- [J] By the card's bins it is neither an equivalence nor a consistency, so it is counted.

## 4. What it means

- [J] **The class is not known to be inert.** It is one bit, the pairing's square class. It moves B1953's two Gramians
  unless frame C has S₁ = S₂. If the record ever reads the down sector through G₃ or G₂ separately, the class is an
  input of that read-out.
- [J] **B1953's choice is class 2's.** Its identity labelling is covariant only under class 2 (G5, J1). The fibre's
  translations by the 24 points act on its degree-5 thetas as the Weyl operators with the canonical pairing (B1952 C),
  and those thetas carry class 2 (R3). If the frame's point w is paired with the fibre's translation by w, the
  labelling and with it the class are fixed. That would move the class from "counted" to "consistency".
  - This seat has not checked that the frame's labels are the fibre's translations up to a square-determinant map.
  - That is a question for main's frame code.
- [J] **The record's sentence needs mending.** B1953, lines 74 and 75: "Scaling the labels (D(cw) for c = 2, 3, 4)
  gives covariant operators too, with the same two Gramians. So the two Weil classes are not told apart by these
  read-outs." The scalings are class 2's own labellings. The class-1 operator is D(Kw) with K = diag(1, 3). B1955 § 2's
  "fixes an identification of the labels, not a class" holds in that both classes have a covariant operator. Each has
  its own labelling, and the labelling is what the Gramians see.

## 5. For main (no data)

1. On frame C, at B1953's base points, compute O with D(Kw) for K = diag(1, 3), its two Gramians and their ratios.
   Equivalently, compute S₁ − S₂ for A(w) = ζ^(−ab)Y(τ, w). This is one line in `weyl_operator.py`'s O. Expected [J]:
   S₁ ≠ S₂, as nothing in the frame's law relates the points w and 2w at one τ.
2. Mend B1953 lines 74 and 75 by the result.
3. Say whether frame C's labels are the fibre's translations (§ 4). If they are, B1953's labelling is the fibre's, and
   the class is fixed at 2 by consistency with the fibre. If they are not, the class is counted.

## 6. Typed

- **[E] by the runs:** § 1's table; § 2's "both classes" column; § 3's lemmas and propositions; § 0 items 1 to 5.
- **[E] by the record:** each arc's quantity and whether it is read (§ 2), read at its page through the mask and at its
  code; B1955 § 2; B1952's sentence on the icosahedral triplet; main's R2 and R3.
- **[E] standard:** Galois conjugation of the Weil representation; Ad by a non-square determinant exchanges the
  classes.
- **[J]:** § 0 item 6; § 4; § 5's expectation.
- **Not done:** frame C's own Gramians in class 1, which needs main's frame; O's full singular values under a
  non-square labelling.

## Files

- `relays/chat1_2026-11-18_wp1/`: `wp1b_class_test.py`, `wp1b_labels.py`, `wp1b_followup.py`, `wp1b_gramians.py`, each
  with `_out.txt` and `_err.txt`; `SCRIPT_SHA256.txt`.
- The conditions: `relays/cards/CHAT1_W-P1_STEPS_conditions.md` (step 2; its two follow-ups).
- Cited: B1856, B1923, B1934, B1936, B1951, B1952, B1953, B1955, `checks/web_wa1_rest.py`, `checks/web_review.py`,
  W-A2 part B, card W-P1 § 3.2.

0 of 19.
