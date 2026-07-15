# THE LEVEL-LADDER CAMPAIGN — FINDINGS (seat cc2, 2026-07-15)

**Verdict: OUTCOME B (partial, richly structured) per the locked outcome table.**
Prereg: `CAMPAIGN.md`, sha256 `2c9dea54…f839a4e` frozen before the level-4 run; level-4
readouts banked blind (`outputs/level4_readouts.json`, sha256 `95a0e861…300ff4`) before
comparison. All computations from exact integer data (the ζ_{6κ} exponent-count pipeline);
headline values carry exact-integer or 50-digit certificates. Environment and scripts in the
packet; every number recomputable from the scripts alone.

---

## The headline: the E₆ theater goes silent at the dyadic rung

**Z₄ = Tr ρ₄(A₁) = 0 EXACTLY** at E₆ level 4 (κ = 16) — the integer coefficient vector of
the unnormalized trace reduces to the zero polynomial mod Φ₁₉₂ over ℤ. Moreover
**Tr(Θρ₄) = 0 exactly** (same certificate), so **both parity sectors vanish**:
tr_odd = tr_even = 0 exactly.

- **H133 dies at its own registered gate** ("Z ≡ 1 at every level? Gate: level 4, or a
  proof"): PRED-1/F1 fired. The kill is *structured*: not a random value but an exact zero.
- `residual-hint:` the Z-ladder is {+1, +1, +1, 0, ?}. The zero is selection-rule-shaped
  (both sectors vanish identically) but is NOT forced by the banked θ-parity theorem (B599
  forces zeros of odd-factor-count contractions; Tr ρ and Tr Θρ are not of that form — at
  k ≤ 3 they are nonzero). What does the theater stop seeing at κ = 2⁴ — and does Z return
  at κ = 17? (registered follow-on below.)

## The exact ladder (k = 1..4), all entries certified

| k | κ = k+12 | N | dim odd | Z (exact) | (tr_odd, tr_even) | clock odd | clock even | odd-sector arithmetic |
|---|---|---|---|---|---|---|---|---|
| 1 | 13 | 3 | 1 | +1 | (+1, 0) | 1 | 4 | degenerate (dim 1) |
| 2 | 14 = 2·7 | 9 | 3 | +1 | (+1, 0) | 4 | 4 | ℤ/7 sine kernel (banked B570/B572; reproduced exactly) |
| 3 | 15 = 3·5 | 20 | 8 | +1 | (0, +1) | 60 | 30 | the golden octic, ℚ(√5) (banked B578-D7; reproduced integer-exact) |
| **4** | **16 = 2⁴** | **42** | **17** | **0 (exact)** | **(0, 0)** | **12** | **12** | **ℚ(√2) import + thirds; {2,3}-ramified only** |

New exact level-4 data (nothing in the corpus had level 4):
- 42 primaries, 8 θ-fixed, odd dim 17 (the dimension ledger held).
- ρ₄(A₁)|odd: order **12** (certified 1.6e−49; divisors {6,4} bounded away; eigenvalue
  cross-check agrees). ρ₄(A₁)|even: order 12 as well.
- The 18 distinct odd-block magnitudes w = 32·|S_odd|²: four rationals {4/3, 8/3, 4, 16/3};
  three ℚ(√2) quadratic pairs — **2±√2, 4±2√2, 1±1/√2** (discs 2³, 2⁵ — the silver field);
  two quartics [4,−48,148,−88,1] (disc 2²⁵·17²) and [324,−2160,3348,−888,49] (disc
  2²⁵·3¹⁸·7²) — all p ≥ 5 appear to EVEN powers (index/norm content, not ramification).
- The even block (control): same flavor ((2±√2)/6, (2±√2)/3, (4±2√2)/3, …; quartics with
  17², 241²; one value unidentified at degree ≤ 16 / coeff ≤ 1e14 — banked as an 80-digit
  numeric, priced out honestly). Everything lives in ℚ(ζ₁₉₂) by construction.

## The prediction sheet, scored (P1 frozen → P2 compared)

- **PRED-1 (Z₄ = +1): REFUTED** — Z₄ = 0 exactly. H133 killed at its gate (see headline).
- **PRED-2 ({2,3}-smooth): HOLDS — but the campaign's own red-team note demotes it:** since
  every value lives in ℚ(ζ₁₂κ) and 12·16 = 192 = 2⁶·3, {2,3}-only ramification was
  *envelope-automatic* at level 4. As formulated, PRED-2 could only have fired on a
  computation error. The informative content it was reaching for is PRED-3 and the law's
  reframe below. (Recorded as a prereg self-correction, not silently rescored.)
- **PRED-3 (the ℚ(√2) / silver import at the inert 2): CONFIRMED** — the odd block's
  quadratic irrationalities are exactly the √2 family. The inert-prime clause now has two
  instances: 5 inert at κ=15 → ℚ(√5); 2 inert at κ=16 → ℚ(√2).
- **PRED-4 (Pisano clock): RESCORED BY THE LIT-GATE (see LIT_GATE.md).** The divisibility
  ord(ρ_k(A₁)) | ord(A₁ mod ord(T_k)) is the **known congruence-subgroup property**
  (Bantay 2003; Ng–Schauenburg 2010; Dong–Lin–Ng 2015: ker ρ ⊇ Γ(n), n = ord(T)). Our
  contribution is the exact data on that frame: ord(T_k) = 12, 84, 180, 48 at k = 1..4;
  divisibility holds at every rung (1|12, 4|24, 60|60, 12|12); **equality exactly at
  k = 3, 4** (ρ_k injective on ⟨A₁ mod ord(T_k)⟩), proper quotient at k = 1, 2. The
  original Pisano candidate-set framing is retired as numerology-adjacent; the canonical
  modulus is ord(T_k). New residual question: injectivity on ⟨A₁⟩ for all k ≥ 3?
- **PRED-5 (mechanism): ANSWERED BY THE SAME GATE** — the naive T-content reading was
  negative as computed; the true mechanism is the congruence property above.
- **MB12 vacuity guard:** passed (dim 17, emphatically non-scalar block).

## The law, reframed at its earned strength (the campaign's synthesis)

The naive "one new prime modulus per level" was already dead (B578-D7). What the four-rung
ladder now supports, stated at hint/frontier grade:

1. **The odd block's arithmetic content saturates exactly the odd primes of κ, in a form
   dictated by their ℚ(√−3)-splitting character:** split 7 (κ=14) → the ℤ/7 sine kernel;
   inert 5 (κ=15) → the ℚ(√5) quadratic import inside the octic; no odd prime (κ=16=2⁴) →
   no odd-prime content, and the inert 2 delivers the ℚ(√2) import. (Level 1, κ=13 split,
   is degenerate — dim 1 — and carries nothing; the ladder's data starts at k=2.)
2. **The import is SECTOR-BLIND; the organization is not.** The parity control caught this:
   the level-3 EVEN block is also genuinely √5-ramified (eight {5:1}-disc quadratics), and
   the level-4 even block is also √2-flavored. But the odd sector is low-degree and
   *organized* (one octic at k=3; nothing beyond quartics at k=4), while the even sector
   sprawls (six values beyond degree 16 at k=3, one at k=4). "Chirality-specific" survives
   only as an organization statement, not a field statement — an honest scope correction.
3. **The clocks are congruence-anchored (the lit-gate's mechanism):** ρ_k factors through
   SL(2, ℤ/ord(T_k)) (Bantay / Ng–Schauenburg / Dong–Lin–Ng), so every clock divides
   ord(A₁ mod ord(T_k)) — verified 1|12, 4|24, 60|60, 12|12 — with equality at k = 3, 4.
   The odd clock = 2× the even clock at k=3, equal at k=2,4. Open residual: injectivity
   of ρ_k on ⟨A₁⟩ for k ≥ 3.
4. **Norm echoes across rungs (NOTICED-grade):** the level-2 prime 7 reappears at level 4
   as *norm content* — a quartic constant 49 = 7² (odd block) and 2401 = 7⁴ (even block);
   17 = κ₅ appears as 17² in quartic discs; 241 ≡ 1 (mod 48) as 241². Hint rows proposed
   below; no claim.

**The registered decisive follow-on (NOT run here): level 5, κ = 17** — the first *prime*
conductor after the degenerate k=1, and 17 ≡ 2 (mod 3) is **inert** in ℚ(√−3). The law's
clause (1)+(inert) predicts: the odd block's quadratic irrationalities include a **ℚ(√17)
import**; and the Z-question asks whether the theater's silence at k=4 was dyadic-specific
(Z₅ ≠ 0?) or the start of something else. Either answer banks. (P⁺₅(E₆) = 78 primaries, odd dim 34, by
the comark count; the engine handles it unchanged; ~3–4× the level-4 cost.)

## P4 — L76, the two towers (independent cell)

See `outputs/P4_TOWERS.log` (exact values verbatim). Summary:
- t_n = |det(A₁ⁿ − I)| computed exactly to n = 24; 11-locus = {5, 10, 15, 20} ✓ exactly the
  multiples of 5 (Pisano π(11) = 10).
- e_n = det(I − M_n) computed EXACTLY to n = 6 (fraction-free Bareiss over ℤ); banked
  cross-checks passed: e₁ = −11 ✓, e₄ = −(11²·1459·597049·2169349081) ✓.
- e_n mod 11 (𝔽₁₁ elimination, validated against the exact range): the banked 11-locus law
  **CONFIRMED on n ≤ 10: {1, 4, 7, 10} = exactly n ≡ 1 (mod 3)**
  (`outputs/P4_INTERLOCK_EARLY.log`; the n = 11, 12 extension in the main log).
- **The interlock question (the vein's door): DECIDED — n = 10 is a genuine DOUBLE-11
  point** (11 | t₁₀ and 11 | e₁₀, both by direct computation). The two towers' 11-loci
  interlock exactly on n ≡ 10 (mod 15) — the CRT of the two independent laws (t: Pisano
  n ≡ 0 mod 5; e: doubling-orbit n ≡ 1 mod 3). First shared index 10, next predicted 25.
  `residual-hint:` is anything special about M₁₀'s structure at the shared index (the
  charge and the cover torsion share the prime 11 = |e₁|), or is the interlock purely CRT?
- The mod-11 locus extended through n = 12: {1, 4, 7, 10} — n = 11, 12 non-divisible exactly
  as n ≡ 1 (mod 3) predicts (next hit n = 13).
- **The wide scan is a clean sweep: NO prime 3–79 other than 11 divides any e_n for
  n ≤ 10** — extends the banked "only 11" claim (previously through n = 7) by three rungs
  across all 20 primes.
- **New exact data: e₅ and e₆** (62 and 181 digits, verbatim in the log); gcd(t_n, e_n) = 1
  on the whole exact range n ≤ 6 — the towers are rung-wise COPRIME; the first nontrivial
  common divisor is forced at the interlock n = 10 (both carry 11, so gcd(t₁₀, e₁₀) ≥ 11).
- **The vein's verdict at this evidence level: the two towers are arithmetically independent
  except through the single prime 11 = |e₁|** — no multiplicative relation (coprime rungs,
  non-integral ratios), loci governed by two independent clocks (Pisano-5 for t, the
  doubling-orbit 3-cycle for e) that intersect exactly on n ≡ 10 (mod 15) by CRT.

## P-proof — L73, the abelian one-pager (done, locked)

`outputs/L73_ONE_PAGER.md` + `scripts/p_proof_lock.py`:
- **Lock 1 GREEN:** det(A₁ − I) = −1; unit mod every N ≤ 4096; unique fixed point verified
  by direct enumeration on a sample.
- **Lock 2 GREEN:** 662/662 gate-passing cyclic theaters (ℤ/N, all nondegenerate forms,
  N ≤ 40) give Tr ρ(A₁) = +1 — an independent rebuild of the AP2 ground on the cyclic
  family, now explained by the one-line determinant fact.

## Proposed register updates (for the banking seat; nothing applied from this seat)

- **H133 → TESTED-NEGATIVE at its gate** (level 4 computed; Z₄ = 0 exact). Residual hint
  (mandatory): the Z-ladder {+1,+1,+1,0,?} and the both-sectors-zero structure; new hint
  row proposed: "does Z return at prime conductors (κ=17)?"
- **L73:** anchor proven (one-pager + locks); the nonabelian extension answered negatively
  at k=4; propose the vein's row records the theorem + the Z-ladder.
- **L74:** four-rung data banked; the law restated as saturation-of-odd-primes-of-κ with
  splitting-typed form (split → sine kernel; inert → real-quadratic import, now 2 instances);
  level-5 ℚ(√17) prediction REGISTERED as the decisive test. **Lit-gate (LIT_GATE.md):
  framework fully known (Coste–Gannon/Bantay: ℚ[S] = ℚ(ζ_{ord T}) — level-4 arithmetic lives
  in ℚ(ζ₄₈)); no structural theorem predicts which subfield per level for rank ≥ 2; the E₆
  ladder computation NOT FOUND (needs-specialist before novelty). Rank-1 folklore parallel
  (Ising √2 at κ=4, Fibonacci √5 at κ=5) proposed as a NOTICED row. External corroboration:
  k = 4 is E₆'s first exceptional-modular-invariant level (FSS94 ℓ=7 HSE; Gannon k=4,6,12) —
  the silence coinciding with the extension invariant is a sharp NOTICED-grade mechanism
  hint for Z₄ = 0.**
- **L77:** clock table {1/4, 4/4, 60/30, 12/12} (odd/even) banked; the mechanism is the
  congruence-subgroup property (lit-gate: Bantay/Ng–Schauenburg/Dong–Lin–Ng), with the
  equality-vs-quotient pattern {Q, Q, =, =} as the campaign's own datum; the modulus map
  question is retired in favor of the injectivity residual (LIT_GATE.md).
- **L76:** towers banked per P4 log; the n = 10 interlock decided.
- **New NOTICED rows proposed:** (i) the norm echo (7² and 7⁴ constants at κ=16; 17² in
  discs — earlier/later conductor primes as norm content); (ii) the sector-organization
  asymmetry (odd low-degree, even sprawling); (iii) the parity hop of the trace unit
  ((+1,0),(+1,0),(0,+1),(0,0)); (iv) odd clock = 2·even clock at k=3, equal at k=2,4.

## Method notes (for Review-18-style provenance)

All verification internal (this seat); the engine reproduces three banked rungs exactly
before touching the new one (P0 hard-gates, including the B569 two-word lock at every
level); prereg frozen and hashed before the blind run; readouts banked before comparison;
the one PRED demoted post-hoc (PRED-2, envelope-trivial) is recorded as a prereg
self-correction rather than rescored silently. Caps stated: even-block values beyond degree
16 / coeff 1e14 priced out as numerics; level 5 not run; P5/L75 (the optional hint-harvest
cell) not run — deferred, register row untouched; the modulus map not fit (2 points
were never going to pin it; now 3 constrain it).
