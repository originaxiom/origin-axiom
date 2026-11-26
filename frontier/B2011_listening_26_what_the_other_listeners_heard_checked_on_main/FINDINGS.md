# B2011 — Listening 26: what the other listeners heard, checked on main — one rate law at the primes 3, 5 and 7, a level that breaks B2005's pattern, and every computed step of a proof for every rung

**Verdict: PROVED for its checks (exact: FLINT over the integers and modulo primes, sympy, numpy on every point to mod 6561);
the all-k assembly read, not checked line by line.** Main, 2026-11-26, in the author's /loop "continue the listening line".
Data-free. 0 of 19.

## Seen first

- **B1996 and B1997:** the slow decay up the 3- and 5-towers, and its closed form at mod 81 alone.
- **B1987:** the 7-tower's 0.928 at mod 343.
- **B2002, B2003 and B2005:** the halving and the two correlations this arc tests.
- **B2009:** the stabiliser condition. **B2000:** the linearisation at (3,3,3).
- **Swept:** `VERDICT topic-sweep /honeycomb|Bloch|mod 135|1 \+ 4 ?cos|half-scale|all-k|every 3\^k/: 14 of 1752 arcs on main match (NEGATIVE 1, OPEN 3, PROVED 10); 2 register rows match (QUEUED 2)`.
- **The literature (standard):** Bloch theory for a periodic operator on a lattice quotient (here a honeycomb torus); the
  bipartite spectrum's ± symmetry; Hensel lifting of a congruence with a non-vanishing linear term.

## Why this arc

The author asked how we know we listened properly and nothing escaped our ears. Main's answer was that we don't yet: the
locks show what we heard is there, not that we heard everything. The first guard named was to read the other listeners
before computing again. Three deliveries had arrived since the pins; two bear on this line, and both are checked here on
main's own code (B1996's orbits, B2002's sectors, B2000's linearisation), not by running the seats' scripts.

## What escaped main's ears, heard by another listener

- **One law for the slow decay at the primes 3, 5 and 7 (agy-exp's NH-2).** Λ(M) = √(w + √(w² − 4)), w = (1 + 4cos(π/M))/2.
  On the largest orbit over the common point, Λ(M)/2 is main's slowest decay of W₊ = P_L + P_R:

  | level | orbit | main's slowest decay (double) | Λ(M)/2 | M | the exact factor of Λ(M) divides W₊'s polynomial |
  |---|---|---|---|---|---|
  | mod 27 | 72 | 0.707106781186549 | 1/√2 | 3 | over ℤ, twice |
  | mod 81 | 648 | 0.957649082367045 | 0.957649082367038578 | 9 | over ℤ, twice |
  | mod 125 | 120 | 0.838930829110233 | 0.838930829110230502 | 5 | over ℤ, twice |
  | mod 343 | 1176 | 0.927582649145770 | 0.927582649145759845 | 7 | over ℤ, six times |
  | mod 625 | 3000 | 0.994710391601242 | 0.994710391601228578 | 25 | modulo three 62-bit primes |

  Main had these numbers (B1987, B1996) and the closed form at mod 81 alone (B1997). It had not heard that they are one law,
  with M the level's period (3, 9 on the 3-tower; 5, 25 on the 5-tower; 7 at 343). The law is credited to agy-exp.
- **B2005's pattern is not a law (agy's C60).** At mod 135 = 27 · 5 the orbit of (3,3,3) has 2880 points and C fixes 3. ρ
  factors through G₁₃₅, because the orbit reduces onto the mod-27 orbit and ρ factors through G₂₇. Yet the halving fails:
  the gcd of p_neutral(2x)/2^d with the charged polynomial has degree 949 of 959, and the 10 charged roots left over are
  exactly those of (x² − 2x − 2)(x² + 2x − 2)(x³ − 3x − 1)(x³ − 3x + 1). B2005 found "the halving holds exactly where ℤ₆
  survives" in the eleven levels it ran; mod 135 is a twelfth where ℤ₆ survives and the halving does not. Main's own
  sentence of 2026-11-26 ("the halving fails exactly at the levels where the character doesn't survive") is wrong and is
  withdrawn. What decides is B2009's condition on the stabiliser, not the survival of ℤ₆. The level is credited to agy.

## The checks (expectations hashed before the run)

| id | result |
|---|---|
| A1 | **holds**, as above (`c60_levels_run.txt`) |
| A2 | **holds:** at mod 45 (320 points, C fixes 2) the gcd is x²(x − 2)(x + 2) |
| A3 | **holds exactly over ℤ** (`halving243_exact_run.txt`): at mod 243 (5832 points; neutral dimension 1946, charged 1943) p_neutral(2x)/2^d = (x² − 9) x S(x), each sector's polynomial fixed by 90 primes of 62 bits past the 7^d bound (44 minutes). B2003 had it to 10⁻⁸. The seat's quoted x² coefficients (−11,688 and −2,913) belong to its own reduced blocks and were not compared |
| A4 | **holds at every k run, k = 2 to 8 (mod 9 to mod 6561)** (`ingredients_run.txt`): ε splits the orbit in equal halves that each of the six moves exchanges; main's six moves and the seat's six give the same images; C's fixed points are 3, all in O⁺, for k ≥ 3 (at mod 9, 2, one in each half); γ rises by 1 under C and under s₂s₃, s₃s₁, s₁s₂ on O⁻; around each point of O⁺ the six γ values are 0, 0, 1, 1, 2, 2; J_k (k ≥ 4) is a bijection of O⁻, commutes with all six sᵢsⱼ, and J_k C = τ C J_k |
| A5 | **holds, k = 2 to 8:** the orbit is the whole congruence set; |S_k| = 8 · 3^{2k−4} (4,251,528 at mod 6561), one component of L and R |
| A6 | **holds:** [C⁻¹, σ]³ is the identity at mod 27 and 81 and of order 3 at mod 243, moving every point |
| A7 | **holds:** P₆ divides p_neutral at mod 81, twice; its largest root is 2√(5 + 4cos(π/9)) to 25 digits; Φ₁₈(−2) = 73, Φ₆(−2) = 7 |
| B1 | **holds**, as above (`honeycomb_run.txt`); the double-precision difference is at most 1.4 × 10⁻¹⁴ |
| B2 | **holds:** S₆ = Σ_k C^k (J_L + J_R) C^{−k} at a general point is diag(x + y + 2z + 2, x + y − z + 2, x + y − z + 2) in C's charge basis; averaged over the point's three rotations the ratio is (4s + 6)/(s + 6) identically; 14/5 at (3,3,3), 3, 17/5, 26/7, 73/19, 425/107 along ω's tree, limit 4 |
| B3 | **holds:** the 648-point orbit mod 81 (it contains (3,3,3)) is {0,1} × (ℤ/18)² with the card's L and R, from 3 base points; L² and R² commute, have order 18, and generate 324 |
| B4 | **holds:** the lowest-degree part of (L after R)³ − id is (x(z² − y²), y(x² − z²), z(y² − x²)); for R after L it is the negative |

## Reading the all-k argument (post hoc, labelled; main's derivation, written after the runs)

- **Each computed step does not depend on k once k ≥ 4.** J_k(v) = v + 3^{k−2} δ(v), with δ a function of v mod 27. A
  Vieta flip is quadratic, so s(v + 3^{k−2}δ) = s(v) + 3^{k−2} Ds(v) δ mod 3ᵏ when 2k − 4 ≥ k. The condition J sᵢsⱼ = sᵢsⱼ J
  is then a congruence mod 9 between quantities fixed by v mod 27, the same at every k ≥ 4. The orbit reduces onto the
  mod-27 orbit, and ε is fixed by v mod 9. So the check at mod 81 is the check at every k ≥ 4; mod 243 to 6561 repeat it.
  The same holds for γ (k ≥ 3) and for J_k keeping the congruence set (a condition mod 27 for k ≥ 5).
- **J_k C = τ C J_k, by hand for every k ≥ 4.** The first coordinates agree. In the second, J(Cv) − C(Jv) is
  3^{k−2} · 3c = 3^{k−1} c; in the third, −3^{k−1} a ≡ 2 · 3^{k−1} a. Since (z + 3^{k−2}·)/3 ≡ c and (x + 3^{k−2}·)/3 ≡ a
  mod 3 for k ≥ 4, this is τ exactly.
- **The count |S_k| = 8 · 3^{2k−4} for every k.** For u in S_{k−1}, κ(u + 3^{k−1}m) ≡ κ(u) + 3ᵏ · 2(am₁ + bm₂ + cm₃)
  mod 3^{k+1} (k ≥ 3). The linear form is non-zero since a, b, c are units, so each point has exactly 9 lifts.
- **What remains for a proof for every k:**
  - that S_k is one orbit at every k, verified here to mod 6561. A route: kernel elements at one level, cubed, act on the
    next level's fibres by the same shifts. That is a sketch, not checked;
  - the seat's assembly of the steps (the bipartite Schur block, the Euler-index count, the induction over the fibre's
    characters), read and coherent, not checked line by line.

  Main's record keeps the identity as exact at mod 27 and 81 (B2002) and at mod 243 (A3 above), and as an argument for every k
  whose computed steps hold for every k.

## Disclosures

- The card was hashed before any run (`EXPECTATIONS_HASHED.md`).
- `honeycomb.py`'s first run stopped before printing anything. At M = 3, w < 2 and Λ is complex; its modulus is now compared.
  The fix is commented in the script.
- `symbolic.py`'s first run wrote ω as exp(2πi/3). Sympy left (−1)^{1/3} unsimplified, and two comparisons printed False
  while the node values were right. That run is kept as `symbolic_run_first_unsimplified.txt`; ω is now written in radicals.
- The first call of `c60_levels.py` failed in the shell (no `timeout` command) before Python started.
- The claims are rebuilt on main's own code. The seats' scripts were read for definitions (C60's producer), not run.
- **Not checked here:**
  - agy-exp's NH-3 collapse at mod 243 and its NH-5. NH-5 is elementary; its positive split imports i and an L–R asymmetry,
    which the whole does not supply, as in B2008;
  - C60's 7,776 non-conjugate elements, and its section 1 (M18's concessions, and the dated decline on P-884's E3b,
    registered);
  - whether B2009's stabiliser condition predicts mod 135: G₁₃₅ carries the mod-5 orbit of 40 points, too large for a
    character table.
- agy-002's A2-WHOLE-INSTRUMENT is on the order-30 line, on hold, and is registered only (harvest row 2012).
- Nothing is compared with data.

## Credit

- **agy-exp:** the rate law across the primes 3, 5 and 7 (NH-2), the honeycomb torus at mod 81 (NH-1), the cubic term
  (NH-3) and the outward ratio (NH-4).
- **agy:** the level mod 135 that breaks B2005's pattern, the mod-45 gcd, the commutator's waking at mod 243, the sextic at
  mod 81, and the all-k argument whose every computed step holds on main for every k.
