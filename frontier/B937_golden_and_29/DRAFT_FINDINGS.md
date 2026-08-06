# B937 — THE GOLDEN ENTRY IS A RESIDUE CHARACTERISTIC, AND OFF-DIAGONAL MIXING NEVER TOUCHES THE OBSERVER'S PLACE · 29 IS A COINCIDENCE (whitelist printed)

**Date:** 2026-08-06 · **Seat:** computation agent (lane: B930/B931 follow-on, for
cc banking) · **Status:** DRAFT — exact tier for every claim (ideal-lattice
valuations in a monogenic model, cross-gated against B931's two banked models and
against an independent p-adic Newton-lift belt); **no numerics anywhere**, no
measured number contacted.
**Instrument:** `golden29.py` → `results.json` (**118 checks, ALL PASS**, 2.0 s).

---

## THE ONE-LINE HEADLINES

> **A.** The golden field does **NOT** enter. 5 is the residue characteristic of the
> two places carrying the mixing numerator, nothing more — decided exactly, four
> independent ways.
>
> **A′ (the real find).** The **cross-generation** overlap² is supported **entirely
> on the degree-TWO places** — 𝔮₂(5)³·𝔓₂(953)⁻¹ — and the **same-generation** one
> adds **exactly 𝔮₁(5)⁶·𝔓₁(953)⁻²**. The whole difference between diagonal and
> off-diagonal mixing **is the observer's degree-one place**, at 953 with precisely
> d_S's twist exponent (B918's V-pole place). *Off-diagonal mixing never touches the
> observer's place.*
>
> **B.** 29 is **COINCIDENCE**, whitelist printed: 84 whitelist integers, 2 hits,
> naive expectation 84/29 ≈ 2.9 — the hits come in **below** the look-elsewhere
> budget, and they sit on **opposite sides** of the S/A dichotomy and are of
> **different kinds** (a rational trace numerator versus a prime ideal).

---

## Instrument upgrade: K is MONOGENIC — K = ℚ[s]/(s³ − 12s − 5)

B931's divisor work ran in two non-maximal models of K, and in **both** sympy's
`prime_decomp` fails at p = 5 and p = 7; B931 had to fall back on the S₃-resolvent
theorem for the splitting *type* at 5, and valuations there were out of reach. This
cell searches the `round_two` integral basis and finds an **index-1** generator:

> **K = ℚ[ρ]/μ13 = ℚ[s]/(s³ − 12s − 5), disc = 6237 = 3⁴·7·11, O_K = ℤ[s].**

Every place of every prime is then reachable by Dedekind's theorem. Valuations are
computed by **ideal-lattice membership** (P = (p, g(s)), v = max{k : z ∈ P^k}, HNF
over ℤ) — sympy's `prime_valuation` raises `CoercionFailed` on these inputs (its
halting test reads only the last diagonal entry of a matrix it never returns to
Hermite form), so it is not used. Three gates on the new machinery:

- **cross-model gate:** the recomputed divisors of d_S and d_A at 2, 3, 953 equal
  B931's banked tables **place by place**, in a third and independent model;
- **norm identity:** Σ_P f_P·v_P = v_p(N) is checked at every prime of every table;
- **independent p-adic belt:** at each degree-one place the valuation is recomputed
  by Newton-lifting the p-adic root of s³−12s−5 and evaluating — a route sharing no
  code with the lattices. 10/10 agree.

---

## PART A — THE GOLDEN ENTRY

### A1. The exact divisor of the mixing element

B930's same-generation S-vs-A overlap² is one element W ∈ K with minimal polynomial
953⁴x³ − 230571559875x² − 16394578125x − 5¹². Its complete divisor:

> **(W) = 𝔮₁(5)⁶ · 𝔮₂(5)³ · 𝔓₁(953)⁻² · 𝔓₂(953)⁻¹**, N(W) = 5¹²/953⁴

with f(𝔮₁)=1, f(𝔮₂)=2, f(𝔓₁)=1, f(𝔓₂)=2 (both primes unramified, both split [1,2]).

### A2. The 953 lead is DERIVED — and the mixing element is the only object that sees both places

W's entire 953-content is a **pole**, and it is exactly minus the sum of the two
families' twist divisors:

| object | 𝔓₁ (deg 1, the observer's place) | 𝔓₂ (deg 2, the mirror) |
|---|---|---|
| d_S (vacuum twist) | **+2** (B931's tangency) | 0 |
| d_A (A-family twist) | 0 | **+1** |
| **W (the mixing element)** | **−2** | **−1** |

Each family alone sees only *its own* place; **the mixing element sees both at
once**. The banked lead is exactly the norm of that pole ideal:
**N(𝔓₁²𝔓₂) = 953²·953² = 953⁴.** Nothing about 953 is left unexplained in W beyond
what B931 already left open about 953 itself.

### A3. The golden numerator is the twist-free part, and it is a {2,3,5}-object

Both W and **u := W·d_S·d_A = h′(S,A)² / (h₊(S,S)·h₊(A,A))** are gauge-invariant
(numerator and denominator carry the same homogeneity under the atom rescalings), so
their divisors are properties of the object, not of B930's normalisation. Computed:

> **(u) = 𝔮₁(5)⁶ 𝔮₂(5)³ · Q₁(2)⁻¹⁰ Q₂(2)⁻¹¹ · 𝔭₃⁻⁸,  N(u) = 5¹²/2³²3⁸ = 5¹²/2304⁴**

— supported **exactly** over {2, 3, 5}. So: **the value prime is entirely the
twist's, the golden numerator entirely the H₊-normalised mixing element's**, and the
{2,3}-denominator is again exactly B931's 2304 (to the fourth), i.e. the {2,3}-part
of lc(μ13). One more structural fact fell out on the way: **x_o = 0 exactly** — the
same-generation twisted overlap h′(S_g, A_g₊) has zero τ-part, i.e. it lies in K, not
merely in N, so |h′|² is a perfect square in K.

### A4. Is the exponent 12 structural?  Four candidates, computed not guessed

| candidate | verdict | the computation |
|---|---|---|
| 12 = 4 places × 3 | **REFUTED** | 5 has **2** places in K, (e,f) = (1,1) and (1,2) |
| 12 = the D-flip count | **REFUTED** | the banked flip rank is **11** (tr W3+W6+W18 = 151/64+169/64+6 = 11); 11 ≠ 12 |
| 12 = the floor dimension | **MATCH WITHOUT MECHANISM** | Cent(C) has dim 12 (B874/B932); the integers agree and **no computation here carries the floor into the 5-divisor**. Coincidence-level, banked as such |
| 12 = 2×6, the divisor being a square | **REFUTED BY THE COMPUTATION** | this cell's first pass guessed even valuations everywhere (the numerator *is* the square x_e²); the degree-two valuation is **3**, odd, because q_S and q_A are **not** 5-units (v₅N = 4 and 8). The abort is logged |
| **12 = 6 + 6** | **COMPUTED** | the two places contribute **equal local norms 5⁶ each**; and 6 is also the entire 5-content of a cross-generation overlap |
| 12 = 3 × 4 | **COMPUTED** | gcd(6,3) = 3: the 5-part of (W) is the **cube** of an ideal of norm 5⁴. Recorded; no mechanism claimed |

So the exponent is a **balanced place-sum**, not a dimension.

### A5. THE OBSERVER-PLACE LAW (the sharpest thing in the arc)

A cross-generation overlap² (it lies in K — its β-part vanishes) has

> **(X_cross) = 𝔮₂(5)³ · 𝔓₂(953)⁻¹** — supported **entirely on the degree-TWO
> places** of both primes,

hence

> **(W / X_cross) = 𝔮₁(5)⁶ · 𝔓₁(953)⁻²** — supported **only on the degree-ONE
> places**, and at 953 with **exactly d_S's exponent**.

The degree-one place of 953 is B918's **observer's place** — the one carrying the
hierarchy element V's pole (den V = 𝔓₁⁴) and the whole value layer. The reading:
**off-diagonal (cross-generation) mixing is blind to the observer's place; the
diagonal carries it, at 953 to the second power and at 5 to the sixth.** This is
the first place in the record where the *observer's place* separates diagonal from
off-diagonal structure.

### A6. Does ℚ(√5) enter?  NO — decided four ways

1. W has a **degree-3** minimal polynomial, so it **generates K**; the splitting
   field of that polynomial *is* the Galois closure of K. Galois group **S₃**, and
   an irreducible cubic with group S₃ has **exactly one** quadratic subfield in its
   splitting field, ℚ(√disc). Here **squarefree(disc) = 77 = squarefree(disc K)** —
   so the quadratic subfield is **ℚ(√77)**, not ℚ(√5). (Same for the
   cross-generation minimal polynomial: squarefree part 77.)
2. The **whole tower** Mbar = N(τ), τ² = −3, in which every B930 quantity was
   computed: N ∩ ℚ(√−3) = ℚ (because squarefree(disc K) = 77 ≠ −3), so
   Gal(Mbar/ℚ) = S₃ × C₂ with abelianisation C₂×C₂ — **exactly three** quadratic
   subfields, ℚ(√77), ℚ(√−3), ℚ(√−231). ℚ(√5) is none of them.
3. Direct: **x² − 5 and x² + 15 are both irreducible over K** (the second is the
   only other route: (a + bτ)² = 5 forces a = 0 and b² = −5/3).
4. **5 does not divide disc K = 3⁴·7·11** — it is unramified, hence not a
   field-theoretic distinguished prime of K at all.

> **Verdict: 5 is a residue characteristic, not the golden field.** The 5 in the
> banked minimal polynomial is the residue characteristic of the two places carrying
> the mixing numerator. B930's reading "the GOLDEN prime closing… where 5 enters the
> value layer" should be **corrected**: 5 enters as a *place datum*, and ℚ(√5)
> demonstrably does not enter the object's arithmetic.

**Consolation, and it is a real one:** 5's quadratic-resolvent symbol is
(6237 | 5) = **−1** — so **5 joins the belt's transposition Frobenius class**,
the same class as 953, 29, 149, 1129, 421493, 72869, 17681 (all −1), while the
S-mass prime 20417473 remains the lone +1. B931's √77 class law now covers the
mixing prime too.

### A7. The honest residue

B931 **derived** 2304 as the {2,3}-part of lc(μ13). This cell finds **no analogous
derivation of the 5**: 5 divides lc(μ13) to the second power and disc(h_S) to the
second power, but not disc(K). *Where the integer 5 comes from is this arc's open
residue* — exactly parallel to B931's open residue for 953.

---

## PART B — THE 29 WHITELIST

The whitelist was **declared and written into `results.json` before any of it was
computed** (section `whitelist_29_DECLARED_BEFORE_COMPUTE`, with a two-outcome
criterion stating in advance what would count as STRUCTURAL). Printed in full:

| item | what was computed | 29? |
|---|---|---|
| **W29-1** m_A's zero-divisor + controls | m_A: **v = 1 at the degree-one place over 29**, 0 at the degree-two. **m_S, d_S, d_A, W, u, X_cross: 0 at every place over 29** | 1 hit (m_A only) |
| **W29-2** the rotation quadratic 1536x²−2088x+677 | disc = **200256 = 2⁶·3·7·149**; 29 divides the middle coefficient only; irreducible mod 29 | coefficient only |
| **W29-3** every W3/W6/W18 charpoly factor + full charpolys | all discriminants factored | **none** |
| **W29-4** both overlap minimal polynomials' discs | 2¹⁸3⁶5¹⁸7³11·953⁶ and 2¹⁸3⁶5⁶7³11·953² | **none** |
| **W29-5** the 55-entry resultant grid | every pairwise resultant of the 11 pipeline polynomials | **none** |
| **W29-6** 29's place structure in K | unramified, **[1,2]**, (6237 | 29) = −1, transposition class | (the frame) |
| **W29-7** the charge trace Gram + G3, G6, G18, the H₊ weights | Gram = diag(60383232, −79427174400, 247210809753600/13, −222489728778240000/19), det = 2⁷⁶3²⁶5⁸7⁶11² | **none** |

**Bonus finding from W29-2 (new, unrelated to 29):** the vacuum register's and the
A-register's twist-vs-Galois quadratics **share their discriminant exactly** —
disc(1536x²−2088x+677) = disc(1536x²−984x+125) = 200256. **Both registers'
principal angles live in ONE quadratic field, ℚ(√3129), 3129 = 3·7·149.**

### The chain tests (post-whitelist, labelled as such)

- **T1 / opposite sides.** The 29-**place** lives on the **A-family** (m_A vanishes
  there); the S-family flip mass is **29-blind at every place**. Conversely the 29 of
  2088 lives in the **S-register's** rotation quadratic, while the **A-register's own**
  quadratic 1536x²−984x+125 is **29-free**. The two 29s sit on opposite sides of the
  S/A dichotomy.
- **T3 / different kinds.** 2088's 29 is the numerator of a **rational trace**:
  2088/1536 = 87/64 = **Tr_K(m_S) − 1** (the subtracted 1 being the exact unity
  principal angle, the line F∩W3), and 87 = 3·29 = 151 − 64. m_A's 29 is a **prime
  ideal**. No pipeline map carries a trace numerator to a place.
- **T4 / the third 29 is not even an invariant.** B930's W6 compression matrix has
  the entry 29/96. An **explicit unimodular shear** (c = 1) turns the block into
  (−9211/96, 385/4; −443687/4608, 18545/192) — every 29 gone, characteristic
  polynomial preserved. That 29 is a coordinate artifact.
- **T5.** 29 appears in **no divisor computed in this cell** except m_A's.
- **T6.** Mod 29 the W3 quadratic loses its linear term (the two non-unity principal
  cosines² become negatives of each other) and **nothing degenerates** — it stays
  irreducible mod 29 (29 is inert in the shared rotation field ℚ(√3129)).

### Look-elsewhere budget

**84** integers were examined inside the whitelist; **2** are divisible by 29
(N(m_A)'s numerator 2113201 and the coefficient −2088). Naive expectation 84/29 ≈
**2.9** — the observed multiplicity is **below** the budget.

> ### VERDICT: **29 is COINCIDENCE.**
> Opposite families, different kinds, no discriminant, no resultant, no Gram, no
> divisor beyond m_A's, one of the three appearances outright basis-dependent, and a
> hit count under the look-elsewhere budget. What would have made it structural is
> printed in the sealed declaration and did not occur.

---

## What this arc changes in the bank

1. **K is monogenic**, K = ℚ[s]/(s³ − 12s − 5) — a reusable instrument (every place
   of every prime now reachable; B931's p = 5, 7 blind spots are gone).
2. **The 953⁴ lead of the mixing element is derived** as N(𝔓₁²𝔓₂): the mixing element
   is the unique object seeing both places of 953.
3. **The observer-place law** (A5) — off-diagonal mixing never touches the observer's
   degree-one place; the diagonal carries it with exactly d_S's 953-exponent.
4. **The golden reading of B930 is corrected**: 5 is a residue characteristic; ℚ(√5)
   is not in the object's arithmetic. 5 does join the √77 transposition class.
5. **The two registers share a rotation field**, ℚ(√3129).
6. **29: coincidence, banked honestly, whitelist printed.**

## Registered open items (carried forward)

- **R1.** Where the integer **5** comes from — no pipeline-free derivation
  (A7). The 953-analogue of B931's residue #1.
- **R2.** The 5-part of (W) is a **perfect cube** (valuations 6, 3); no mechanism.
  B918's Kummer/cube machinery is the obvious place to test it.
- **R3.** **677** appears both as the W3 rotation quadratic's constant term *and* in
  the x-coefficients of **both** overlap minimal polynomials (677 is inert in K).
  Not on the declared whitelist; recorded as coincidence-level data, registered for a
  future **declared** test, used for nothing here.
- **R4.** **149** (in the shared rotation discriminant 3129 = 3·7·149) is new to the
  record.
- **R5.** Whether 𝔓₁(953) and 𝔮₁(5) are **principal** still needs the class group of
  the disc-6237 cubic field (B931's residue #2, unchanged — though the monogenic
  model makes it a much easier computation now).

## Files

`golden29.py` (the instrument; reads the banked B930/B916/B928/B931 JSON, embeds five
harvested B930 K-elements as declared literals, every one gated) → `results.json`
(118 checks, the declared whitelist, every divisor table, the belts) · run logs 1–4 ·
this draft.

## Depends on

B854 (frame), B883 (the 27), B912 (H₊), B914 (h_S), B916 (D₂, the d-minpolys),
B918 (V, the observer's place), B928 (the flip masses, the K-coordinates), B930 (the
overlap matrices — the two riders come from its FINDINGS), B931 (the valuation
machinery and the divisor map this cell extends and cross-gates against).
