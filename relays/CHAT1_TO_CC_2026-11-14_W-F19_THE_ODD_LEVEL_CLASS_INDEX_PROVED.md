# W-F19: the class index is zero on every doublet at every odd level, proved by hand. A formula from duality reduces the index to the cusp; at odd levels the Klein bottle's twisted duality decides the cup products; the case table accounts for W-F12's counts exactly, and predicted the new silver and bronze counts blind

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free): a proof by hand, with a sealed
check. This note closes card W-F19 (`relays/cards/CHAT1_W-F19_a_proof_of_the_odd_level_class_index.md`, 41a4e85a2).
It takes up the structural item W-F10 and W-F12 left open.

**How it was checked.** The proof is by hand (not independently checked; W-F6's laws are its input and are typed the
same way). The sealed check was computed once, on this seat's own code; expectations committed first; tested against
planted errors (1, caught; weak, see § 3).
- **The sealed run.** The script `wf19_checks.py` (sha256 `47224897…c4bef80a43a47`, pushed at 1de17ccfa) was run once.
  Its output was committed (ec9d699ee) before it was read.
- **Before the seal,** only golden level 1 (two doublets, part 2a's) was run.
- **Not blind, and blind.**
  - The case table was derived knowing W-F12's counts at golden levels 3, 5 and 7, so those are not blind.
  - At silver levels 1 and 3 and bronze levels 1 and 3 no doublet had been computed (W-F6 had computed only their
    characters). The predictions there are blind.
- **Step 1's formula** was derived while card W-F19 was drafted (disclosed in the card).
- **A second computation.** The referee of this note recomputed it on its own code, with a conjugate choice of λ, over
  two other primes (1008001 and 30247561). Every count in § 3 at golden 1 and 3, silver 1 and 3 and bronze 1 and 3
  agrees, and so does every row of the case table and the row pairing. It also checked each sub-step of Step 1 on
  every doublet.

## 1. The theorem

**Setting.**
- G is the group of a level n of a metallic tick: the mapping torus of a hyperbolic automorphism of F₂ = ⟨a, b⟩ with
  determinant −1 (odd n).
- Its orientation character is w (w(t) = −1, w = 1 on the fibre). λ = [a, b], and μ = g⁻¹t with τⁿ(λ) = g λ⁻¹ g⁻¹.
- The cusp group is P = ⟨μ, λ⟩, a Klein bottle group (μλμ⁻¹ = λ⁻¹), with w(μ) = −1.
- Coefficients are in ℂ. A character is of finite order; it is fibre-trivial (ft) or not (fn); and m(χ) = χ(μ).
- A **doublet** is a non-split extension 0 → α → V → β → 0 of characters. ℓ = α/β, and the class is c ∈ H¹(G; ℓ) ≠ 0.
- n(V) is the dimension of the interior classes, ker(H¹(G; V) → H¹(P; V)). r¹(V) = h¹(G; V) − n(V) is the rank of the
  restriction.

**Theorem.** Every doublet at an odd level has class index I_w(V) = n(V) − n(V* ⊗ w) = 0.

**Corollaries.**
- n(V) = 1 on exactly the doublets with ℓ fn, m(ℓ) = −1; β fn, m(β) = +1; α ≠ w. On every other doublet n(V) = 0.
- When the characters are W-F12's (fibre part on the torsion T = coker(A − I), t-value any 2e-th root of unity, e the
  exponent of T), these number
  (|T| − 1)(|T| − 2).
- On the same characters, the h¹ gap h¹(V) − h¹(V* ⊗ w) is +1 and −1 on |T| doublets each, +2 and −2 on |T| − 1 each, and 0 on the rest.

## 2. The proof

### Step 1: a formula valid at every level

For any finite-dimensional module V of a one-cusped mapping torus N with cusp group P and orientation character w:

  **I_w(V) = h⁰(P; V* ⊗ w) + h⁰(G; V) − h⁰(G; V* ⊗ w) − r¹(V).**

*Proof.* N and its boundary are aspherical, and the boundary is incompressible (P injects into G), so group and space
cohomology agree, for the pair as well. Write V′ = V* ⊗ w.
1. n(V) = h¹(G; V) − r¹(V), and n(V′) = h¹(G; V′) − r¹(V′).
2. **Half-lives-half-dies.** The images of H¹(N; V) and H¹(N; V′) in the cusp's H¹ are mutual annihilators under the
   cusp's perfect pairing into H²(∂N; w) ≅ ℂ. The cusp's orientation character is w restricted to it. So
   r¹(V) + r¹(V′) = h¹(P; V).
3. **Lefschetz duality.** h¹(G; V′) = h²(G, P; V), and h³(G, P; V) = h⁰(G; V′).
4. **Euler characteristic of the pair.** χ(N, ∂N) = 0 and h⁰(G, P; V) = 0, so h²(G, P; V) = h¹(G, P; V) + h⁰(G; V′).
5. **The pair's sequence.** h¹(G, P; V) = n(V) + h⁰(P; V) − h⁰(G; V).
6. **Combining 1 to 5:** I_w(V) = h¹(P; V) − h⁰(P; V) + h⁰(G; V) − h⁰(G; V′) − r¹(V).
7. **The cusp.** P's Euler characteristic is 0, so h¹(P; V) − h⁰(P; V) = h²(P; V), and by duality on the cusp this is h⁰(P; V′). ∎

At an orientable level w = 1 and P is a torus. There the same formula holds, and I can be ±1 (golden level 4, § 3).

### Step 2: characters at an odd level

**From W-F6's laws (characteristic 0, finite order):**
- h⁰(G; χ) = [χ = 1];
- h¹(G; χ) = [χ = 1] + [fn, m = −1];
- h²(G; χ) = [fn, m = −1], since G's Euler characteristic is 0 and h³ = 0.

**On the Klein bottle**, where χ(λ) = 1 (λ is a commutator). Fox calculus on μλμ⁻¹λ gives:
- h⁰(P; χ) = [m = 1];
- h¹(P; χ) = [m = 1] + [m = −1];
- h²(P; χ) = [m = −1].

An ft character with m = 1 is 1; an ft character with m = −1 is w.

**Restriction is injective in degree 1.**
- For χ = 1, the class is the t-direction, and on P it is the μ-direction, which is non-zero.
- For fn χ with m = −1, W-F6's class is non-zero on λ. On P no coboundary is non-zero on λ.

**The cup products that matter are non-zero.** If m(χ) = −1, then χ restricted to P is w restricted to P. Then
H¹(P; ℂ) × H¹(P; χ) → H²(P; χ) is the twisted Poincaré duality pairing of the Klein bottle, which is perfect. Both
spaces are one-dimensional, so the product of their generators is non-zero. The connecting map of a doublet's
sequence is the cup product with its class, and it commutes with restriction. So whenever the restricted product is
non-zero, the product on G is non-zero.

### Step 3: the doublet's terms

The class restricts to a non-zero class (Step 2), so the restricted extension is non-split. Write V′ = V* ⊗ w; it is
the extension 0 → β⁻¹w → V′ → α⁻¹w → 0, with the same ℓ. Then:
- h⁰(G; V) = [α = 1];
- h⁰(G; V′) = [β = w];
- h⁰(P; V′) = [m(β) = −1].

So **the theorem holds if and only if r¹(V) = [m(β) = −1] + [α = 1] − [β = w].**

### Step 4: the cases

- **The extension character.** ℓ has a class, so ℓ = 1 or ℓ is fn with m(ℓ) = −1 (written fn⁻).
- **The method.** The snake lemma on the map of the sequences
  0 → coker(H⁰(β) → H¹(α)) → H¹(V) → ker(H¹(β) → H²(α)) → 0
  from G to P gives r¹(V) = (the rank on the left) + (the rank on the right) + (the rank of the connecting map).
- **The connecting map vanishes in every case below:** either the right-hand map is injective, or the right-hand group
  on G is zero.

| case | h¹(G; V) | r¹(V) | n(V) | [m(β) = −1] + [α = 1] − [β = w] |
|---|---|---|---|---|
| ℓ = 1, χ = α = β = 1 | 1 | 1 | 0 | 0 + 1 − 0 = 1 |
| ℓ = 1, χ = w | 0 | 0 | 0 | 1 + 0 − 1 = 0 |
| ℓ = 1, χ fn, m = −1 (cup product non-zero: Step 2) | 1 | 1 | 0 | 1 |
| ℓ = 1, any other χ | 0 | 0 | 0 | 0 |
| ℓ fn⁻, β = 1 (cup product non-zero: Step 2) | 0 | 0 | 0 | 0 |
| ℓ fn⁻, β = w (α fn, m = +1) | 0 | 0 | 0 | 1 + 0 − 1 = 0 |
| ℓ fn⁻, β fn, m(β) = −1, α = 1 | 2 | 2 | 0 | 1 + 1 − 0 = 2 |
| ℓ fn⁻, β fn, m(β) = −1, α fn (m = +1) | 1 | 1 | 0 | 1 |
| ℓ fn⁻, β fn, m(β) = +1, α = w | 0 | 0 | 0 | 0 |
| **ℓ fn⁻, β fn, m(β) = +1, α fn (m = −1)** | **1** | **0** | **1** | **0** |
| ℓ fn⁻, m(β) ∉ {±1} | 0 | 0 | 0 | 0 |

In the bold row the class comes from H¹(G; α). On P it is killed: β is trivial on P, and the connecting map sends
β's invariant vector to the class restricted to P, which spans H¹(P; α). So that class is interior.

In every row r¹(V) equals the last column. ∎

**The corollaries.**
- **The n = 1 count.** Count the bold row: ℓ has |T| − 1 choices (fibre part ≠ 1, t-value fixed by m = −1). β has
  fibre part ≠ 1 and ≠ ℓ's inverse (|T| − 2 choices), with its t-value fixed by m = +1.
- **The gap census.** V ↦ V* ⊗ w maps the rows to one another:
  - the first ↔ the second (+1 and −1);
  - the third ↔ the fourth's fn, m = +1 characters (+1 and −1);
  - "β = 1" ↔ "α = w" (0);
  - "β = w" ↔ "α = 1" (−2 and +2);
  - the rest to themselves (0).

## 3. The sealed check

All expectations were met: E0 to E4, and the plant fired. Exact ranks over one prime field (55456633); the helpers
are W-C8 part 2a's.

| level | \|T\| (exponent) | characters | extension characters | doublets | I_w ≠ 0 | n = 1 (predicted (\|T\| − 1)(\|T\| − 2)) | h¹ gap −2 / −1 / 0 / +1 / +2 |
|---|---|---|---|---|---|---|---|
| golden 1 | 1 (1) | 2 | 1 | 2 | 0 | 0 (0) | 0 / 1 / 0 / 1 / 0 |
| golden 3 | 4 (2) | 16 | 4 | 64 | 0 | 6 (6) | 3 / 4 / 50 / 4 / 3 |
| golden 5 | 11 (11) | 242 | 11 | 2,662 | 0 | 90 (90) | 10 / 11 / 2,620 / 11 / 10 |
| **silver 1** | 2 (2) | 8 | 2 | 16 | 0 | 0 (0) | 1 / 2 / 10 / 2 / 1 |
| **silver 3** | 14 (14) | 392 | 14 | 5,488 | 0 | 156 (156) | 13 / 14 / 5,434 / 14 / 13 |
| **bronze 1** | 3 (3) | 18 | 3 | 54 | 0 | 2 (2) | 2 / 3 / 44 / 3 / 2 |
| **bronze 3** | 36 (18) | 1,296 | 36 | 46,656 | 0 | 1,190 (1,190) | 35 / 36 / 46,514 / 36 / 35 |

- **No doublet at the new levels (in bold) had been computed before.** Every prediction there is met: the index, the n = 1 count
  and the gap census.
- **E0, W-F6's law:** it held on every character at every level.
- **E1, the formula:** step 1's formula held on all 54,942 doublets, with each of its four terms computed directly, and on the 12 record modules at
  golden level 4, where I = +1, 0 and −1 on 4 modules each.
- **E3, the case table:** the pair (n(V), h¹(G; V)) is the table's on every doublet. So the table is checked row by
  row, not only in its totals.
- **The plant:** with h⁰(P; V*) in place of h⁰(P; V* ⊗ w), the formula fails on 58 doublets at golden 3, silver 1 and
  bronze 1. The plant is weak: it changes the formula's first term on every doublet with m(β) = ±1 (2|T|² of them:
  32 + 8 + 18 = 58), so it fires by construction. The referee's plants on its own code were stronger and were caught:
  w dropped from V′ (I ≠ 0 on 12 of 64 at golden 3 and 4 of 54 at bronze 1), and a wrong entry in the table's bold row.
- **Golden level 7** (|T| = 29), not re-run: the corollaries give 28 × 27 = 756 doublets with n = 1 and gaps ±1 on 29
  and ±2 on 28. That is W-F12's census and its referee's n = 1 count.

## 4. What it means

- **W-F10's open item is closed.** At every odd level, the class index on doublets is zero by a proof, not only on the
  doublets computed (W-F12's 51,506 at golden levels 1, 3, 5 and 7, and 52,214 at silver and bronze levels 1 and 3 in
  § 3). The proof rests on W-F6's laws, which are by hand.
- **The scope is wider than stated.** The proof uses only the determinant −1, hyperbolicity (through W-F6's laws, which
  hold for every hyperbolic monodromy) and the once-punctured-torus fibre. It does not use the metallic form.
- **Why odd and even differ.**
  - At an odd level the cusp is a Klein bottle. Every non-trivial character that carries a class restricts to the
    cusp's orientation character, so every cup product the index needs (the trivial character's class against such a
    class) is fixed by the Klein bottle's duality.
  - At an even level the cusp is a torus. The characters carrying classes restrict to the trivial character, and the
    products depend on slopes (B1438's firing law). That is where I = ±1 appears.
- **For W-F15's E2.** E2 typed "the class index is zero on every doublet computed" as "computed on those levels and not
  proved". It now has a proof by hand (not independently checked), granting W-F6's laws.
- **What this does not settle.** The reading E2 built on it, that an odd tick has no existence of its own, still needs
  P-846's condition (counting respects covers).

## 5. Typed

| statement | how checked |
|---|---|
| Step 1's formula (every level) | not independently checked (by hand); computed once on every doublet and record module in § 3; recomputed independently by the referee, sub-step by sub-step, at those odd levels and on every doublet at golden levels 2 and 4 and silver level 2 |
| the theorem and its corollaries (odd levels) | not independently checked (by hand, granting W-F6's laws); computed once at seven odd levels, 54,942 doublets (§ 3); expectations committed first (blind at silver and bronze); tested against planted errors (1, caught by construction); recomputed independently by the referee (golden 1 and 3, silver 1 and 3, bronze 1 and 3; bronze 1, silver 3 and bronze 3 over two primes) |
| W-F12's counts at golden 1, 3, 5 | reproduced |

## 6. Files

`relays/chat1_2026-11-14_wf19/`: `wf19_checks.py` (sealed), `SCRIPT_SHA256.txt`, `wf19_checks_out.txt`,
`wf19_checks_err.txt`.

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
