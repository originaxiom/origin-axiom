# B972 — L137 BOUNDED WORK: the value/pencil split, tested

**Date:** 2026-08-08 · **Seat:** scouting/bounded-work subagent · **Lane:** MATHEMATICS · Gate 5 untouched.
**Status:** DESIGN + MEASUREMENT ONLY. Nothing sealed, nothing banked. No seal was run.
Every number below was computed in this sandbox by the four scripts named in §8;
standard facts are labelled *cited, not re-derived*.

---

## 0. VERDICT

> **L137 should be CLOSED AS UNSEALABLE, and the reason recorded is stronger than
> "no criterion was found".**
>
> A principled, pre-statable criterion separating the two classes **does** exist
> (§2.1 — *intrinsically-normalised element of K* vs *root-locus in a pencil with a free
> ℚ\*-coordinate*). It is not the obstruction. The obstruction is that **the criterion does
> not separate the outcomes**:
>
> 1. **A value family fails.** **T**, B914's colorless coupling invariant — the object
>    LAW_MAP §F registers as *"THE ONE-NUMBER TABLE … all six normalization-free colorless
>    couplings EXACTLY equal"* — fails B947's pattern on **both** extreme clauses
>    (|P_lead| ≥ 5, |P_const| = 5) and fails **invariantly** (F ≥ 7; no rescaling reaches it).
> 2. **On the pencil side the verdict is not a property of the object.** Two of the four
>    pencil cubics (B888's) **flip** from fail to hold under the pencil's own gauge freedom
>    t → t/c. Their "fail" is a fact about which coordinate got banked.
> 3. **The statistic does not track the taxonomy at all.** Its two extreme clauses are, by
>    the norm identity N(α) = −a₀/a₃ (computed, §5), a statement about the **divisor** of α —
>    over how many rational primes its zeros and poles sit. On the five banked SPECTRAL
>    cubics (neither value nor pencil) the pattern holds 2 and fails 3.
>
> So the sentence L137 exists to promote — *"the thinning holds on the value layer and fails
> on the pencils"* — **cannot be sealed, and its strong half is false.** B947's refusal to
> promote the 5/2 split was correct.

**And the enlargement makes this sharper, not softer.** Adding every additional banked cubic
found in the repo turns 5/2 into **8 of 9 value families holding and 0 of 4 pencils holding**
— a 12-of-13 agreement that is *more* tempting than what B947 saw. The single counterexample
is the most canonical value object the programme has. That is precisely the situation the
seal discipline exists for.

---

## 1. GATE — instrument checks before any verdict is read (all COMPUTED)

B947 required a banked-identity reproduction before reading its own families; this cell
inherits that requirement and adds two more.

| gate | result |
|---|---|
| B946's V-table factorisation `HIER = 953⁴x³ − 2⁸3⁹·13·421493 x² + 2²¹3⁸·17·1129 x − 2³²3¹¹` reproduced from B947's banked coefficients | **PASS** |
| B918's independently banked `hier_cubic` coefficients agree | **PASS** |
| **B947's seven-family verdict reproduced** by an implementation of the criterion written independently from `PREREGISTRATION.md` — same 5/2, same P_lead/P_const/P_mid_only | **PASS** |
| B888's banked squarefree discriminant part **77** reproduced from B888's own stored pencil factors before its two cubics are used | **PASS** (77, 77) |
| T's banked 50-digit value is a root of T's banked cubic; the banked coefficient vector is primitive (content = 1) | **PASS** (rel. residual 1.34e-54) |

No instrument failure. Verdicts below are readable.

---

## 2. TASK 1/2 — the criterion question

### 2.1 The criterion that *is* pre-statable (and it is a real one)

State it before looking at any coefficient:

> **VALUE family** — an element α ∈ K specified by the object as a **ratio of two
> commensurable quantities of its own Hermitian/weight data**, so that α is fixed by every
> normalisation freedom the construction carries. Its minimal polynomial is **canonical**:
> there is no ℚ\*-action on it.
>
> **PENCIL cubic** — the root-locus of a determinant along a line A + t·B. The pencil has a
> canonical 0 and a canonical ∞ but **no canonical unit**, so t → t/c (c ∈ ℚ\*) is a symmetry
> of the object. Its minimal polynomial is canonical only **up to** the induced action
> (a₃, a₂, a₁, a₀) → (a₃, a₂c, a₁c², a₀c³), re-primitivised.

This is declarable in advance, readable without touching a coefficient, and it is the honest
content of the naming difference already in the record (`PROGRESS_LOG.md:9299` calls all seven
"value families" and marks two parenthetically as "the pencil cubics"; B910/B886/B902 use
"pencil cubic" as a label well before B947). **There is a naming difference in the record;
there is no partition in the record.** Re-partitioning B941's table is an act B947 performed,
not one it inherited.

### 2.2 Why it cannot be sealed — three computed reasons

**(a) It is refuted on the value side by T.** *(COMPUTED)*

`frontier/B914_ratio_table/results.json → T_single.minpoly_desc_coeffs`, degree 3,
coefficient sizes [202, 175, 144, 113] digits, content = 1 (gate §1):

```
a₃ (lead)  = 179³ · 1759³ · 4889³ · 632041³ · C₁₅₇        (C₁₅₇ = B₅₃³, B₅₃ unfactored)
a₀ (const) = 2¹⁹² · 3⁶⁰ · 5⁶ · 7¹⁸ · 11⁶
```

- `C₁₅₇` is coprime to 179, 1759, 4889, 632041 by construction (they were divided out fully),
  and C₁₅₇ > 1, so it contributes **at least one further prime**.
  ⇒ **|P_lead| ≥ 5 > 2** — the leading clause fails, **decidably**, without factoring C₁₅₇.
- `P_const = {2, 3, 5, 7, 11}` ⇒ **|P_const| = 5 > 2** — the constant clause fails too.

Both extreme clauses fail, and not marginally. The failure is **not** an artifact of any
normalisation: even granting T the ℚ\*-freedom that only a pencil is entitled to,
**F(T) ≥ 7** (forced primes {2, 5, 11, 179, 1759, 4889, 632041}), while |P_lead| ≤ 2 and
|P_const| ≤ 2 can accommodate at most 4 forced primes. **No rescaling of T satisfies the
pattern.**

*Scope, stated plainly:* this refutes the criterion **on the judgement that T is a value
family**. That judgement is not free, so here is the argument rather than the assertion. The
eight holders are: a generation weight (V), two overlap-squareds (W, X_cross), two twist
ratios (d_S, d_A), two flip masses (m_S, m_A), one gauge-invariant product (u). Every
pre-statable property they share, T also has:

| property of the eight holders | T |
|---|---|
| an element of K | **yes** — mod-p splitting-type agreement with K = ℚ[s]/(s³−12s−5) at **128 primes, 0 mismatches** (COMPUTED); B914's own banked check `T_is_sigma2_of_explicit_K_element` (cited) |
| dimensionless ratio of the object's own data | **yes** — T := \|c_t\|²/(s_i s_j s_k) |
| invariant under the construction's normalisation freedom | **yes** — B914 banks it as an EXACT identity under per-atom complex rescaling, and LAW_MAP §F calls the six couplings "normalization-free" |
| registered in LAW_MAP §F, "the measurement cascade and the value layer" | **yes** |
| branch-symmetric / one number across the table | **yes** — B914's `T_ALL_SIX_EQUAL_EXACT` |

A seat wishing to save the split must produce a pre-statable definition of "value family"
that contains those eight and excludes T. The only properties that would do it are *"was in
B941's list of seven"* and *"has small coefficients"*. The first is the thing to be explained,
not an explanation; the second is a size cutoff chosen after seeing the answer. Both are
gerrymandering. **I record that this is where the refutation rests, rather than hiding it.**

**(b) On the pencil side the verdict is not a property of the object.** *(COMPUTED)*

Scanning the whole ℚ\*-gauge orbit of each pencil cubic (per-prime tilt, g ∈ [−80, 80]):

| pencil cubic | F | banked-coordinate verdict | does some coordinate in its own gauge orbit HOLD? |
|---|---|---|---|
| μ_charge @ B941/B947 (ρ = 13t) | 5 | fails | **no** |
| μ_charge @ B866's own t | 5 | fails | **no** |
| κ_compact @ B910 | 5 | fails | **no** |
| vacuum-weight cubic (B888) | 4 | fails | **YES** — witness P_lead {5,11}, P_mid_only {7,13}, P_const {2,3} |
| generic-weight cubic (B888) | 4 | fails | **YES** — same witness |

Half the pencil sample fails only because of the coordinate that happened to get banked. And
the *diagnosis* is coordinate-dependent even where the verdict is not: the same μ locus reads
`P_const = {13}` in B941/B947's ρ = 13t and `P_const = {}` in B866's own t. (The two are the
same polynomial — B866 banks `theirs(13t) − 2197·mine(t) ≡ 0`, re-derived here.) A statistic
whose value depends on a gauge choice cannot carry a claim about the objects.

**(c) The statistic does not track the taxonomy.** *(COMPUTED)*

Five further banked cubics are neither value elements nor pencil loci — they are spectral
(charpolys, traces, determinants of operators, which carry the operator's scale). The pattern
holds for 2 and fails for 3 (§4). A statistic that splits 2/3 on a third class is not reading
a value/pencil line.

### 2.3 Recommendation

**CLOSE L137 AS UNSEALABLE. Reason to record, verbatim:**

> The value/pencil partition is pre-statable and principled, but it does not predict B947's
> statistic. (i) T (B914), a value-layer element of K that LAW_MAP §F registers as
> normalisation-free, fails the pattern on both extreme clauses and fails invariantly
> (F ≥ 7). (ii) Two of the four pencil cubics hold in some coordinate of their own gauge
> orbit, so on that side the statistic is not an invariant of the object. (iii) The
> statistic's two extreme clauses are a divisor-support condition (N(α) = −a₀/a₃), which
> makes no reference to the taxonomy, and it splits 2/3 on the banked spectral cubics.
> The 5/2 observation is an observation about which nine elements of one cubic field were
> tabulated, and the programme cannot honestly promote it.

**No successor should be sealed in B947's coefficient-support form.** Beyond being
gauge-dependent for pencils, its **vacuity exclusion is also gauge-dependent**: for K's own
generator s³ − 12s − 5 the pattern *holds* with total support 3, so B947's pre-declared
"total ≤ 3 ⇒ EXCLUDED" rule fires — for one and the same field, renormalisation reaches
*holds*, *fails*, and *excluded-as-vacuous*. This belongs in the METHOD/ERROR record
independently of L137: **MB12 should check "is the criterion invariant under the object's own
gauge freedom", not only "can it pass and can it fail".**

---

## 3. TASK 3 — the enlarged census, with the arithmetic shown

B941's seven were **not** the banked census. A scan of `frontier/*/results.json` finds eleven
further banked cubics, including two **siblings of families already in the seven, from the
same defining arcs** — m_A beside m_S (B928 "Sheet entry 2 — A-line overlaps, m_A ∈ K"), and
X_cross beside W (B930/B937, whose divisor law `(X_cross) = 𝔮₂(5)³·𝔓₂(953)⁻¹` is banked).

### 3.1 The new VALUE families — full factorisations

**m_A (B928), the A-branch flip mass — the exact partner of m_S which is one of the seven:**
```
a₃ =  42467328 = 2¹⁹·3⁴          P_lead   = {2, 3}          |P_lead|  = 2  ✓
a₂ = −56070144 = −2¹²·3⁴·13²
a₁ =  19828224 = 2⁹·3²·13·331
a₀ = −2113201  = −29·72869        P_const  = {29, 72869}     |P_const| = 2  ✓
                                  P_mid_only = {13, 331}     ≥ 1            ✓
total support {2,3,13,29,331,72869} = 6 > 3, not excluded    → **HOLDS**
```
(m_S, for comparison: 2¹⁹3⁴ / −2¹³3⁴·151 / 2⁵3²·11·71·349 / −20417473; holds.)

**X_cross (B930/B937), the cross-generation overlap² — the partner of W:**
```
a₃ =  908209 = 953²               P_lead   = {953}           ✓
a₂ =  1049253 = 3·367·953
a₁ =  253875 = 3·5³·677
a₀ = −15625 = −5⁶                 P_const  = {5}             ✓
                                  P_mid_only = {3, 367, 677} ✓
total support 5 > 3               → **HOLDS**   (W's own signature: 953⁴ / … / −5¹², same shape)
```

**u (B937 part A), u := W·d_S·d_A = h′(S,A)²/(h₊(S,S)h₊(A,A)) — gauge-invariant:**
```
a₃ =  28179280429056 = 2³²·3⁸     P_lead = {2,3} ✓
a₂ = −3057647616000 = −2²⁵·3⁶·5³
a₁ =  53136000000 = 2¹⁰·3⁴·5⁶·41
a₀ = −244140625 = −5¹²            P_const = {5} ✓   P_mid_only = {41} ✓   → **HOLDS**
```
*Honest scoping:* u is a **product of three families already in the seven**, so it is a
corroboration, not an independent draw. It is listed as derived.

**T (B914) — the counterexample.** Arithmetic in §2.2(a). → **FAILS**, invariantly.

**T_row_products (B914).** COMPUTED: `rows == cols` exactly, and
`|rows − T³|/|rows| = 3.5e-50` ⇒ **T_row_products IS T³**, a *dependent* corroboration of T,
not a second counterexample. Its minpoly (605/523/431/337-digit coefficients) fails the same
way: |P_lead| ≥ 5, P_const = {2,3,5,7,11}. **I count it as zero additional evidence.**

### 3.2 The new PENCIL cubics — B888's two (rebuilt from B888's own stored factors, gate §1)

```
vacuum-weight  [2197, 0, −6963104474726400, 2923811689117777920000]
generic-weight [2197, 0, −1740776118681600, −365476461139722240000]
   both: P_lead = {13} (=13³), P_const = {2,3,5,7,11}, P_mid_only = {} → FAIL at banked coord
   both: F = 4, and both HOLD in another coordinate of their own gauge orbit (§2.2b)
```
Mirror-image of μ's signature (μ: P_lead five primes, P_const = {13}³). Compare B910's banked
numerator law, *"α_μ carries 13⁶, α_κ carries 19⁶ — each pencil's Kummer element wears its own
prime"* (cited).

### 3.3 The new SPECTRAL cubics — a third class, and it splits

```
colored_twist_trace (B928)  2⁸ / −2⁸·3 / −2²3²·23 / 3·953
    P_lead {2}, P_const {3,953}, P_mid_only {23}, total 4      → HOLDS
colored_twist_det (B928)    2²⁴3⁶ / −2¹⁶3⁵·643 / 2⁶3³·19·7789 / 953³
    P_lead {2,3}, P_const {953}, P_mid_only {19,643,7789}      → HOLDS
octet_flip_trace (B928)     2¹⁶3⁴ / −2¹⁰3⁴·7·79 / 2⁹3²·7·2441 / −7²·523·1483
    P_const {7,523,1483} (3 primes)                            → FAILS
h_S_B883 (B914)             1 / 0 / −2¹²3⁵·7·13·5913601 / 2²⁰3⁶7²·283·276267371
    P_lead {} , P_const {2,3,7,283,276267371} (5 primes)       → FAILS
A_kappa (B938)              2²·3·251·2568641·72037904648483 / 0 / −2¹⁰3⁴·7·13⁵ / 1
    P_lead 5 primes, P_const {}                                → FAILS
```

### 3.4 The consolidated picture — does it change the 5/2?

| class | family | source | new? | HOLDS |
|---|---|---|---|---|
| VALUE | V_hierarchy | B918 | | ✅ |
| VALUE | W_mixing_sq | B930/B937 | | ✅ |
| VALUE | **X_cross_overlap_sq** | B930/B937 | **new** | ✅ |
| VALUE | d_S_twist | B916 | | ✅ |
| VALUE | d_A_twist | B916 | | ✅ |
| VALUE | m_S_flipmass | B928 | | ✅ |
| VALUE | **m_A_flipmass** | B928 | **new** | ✅ |
| VALUE | **u** (derived = W·d_S·d_A) | B937 | **new** | ✅ |
| **VALUE** | **T** | **B914** | **new** | ❌ **F ≥ 7, invariant** |
| VALUE (dependent, = T³) | T_row_products | B914 | new | ❌ |
| PENCIL | mu_charge | B866 | | ❌ (F = 5, invariant) |
| PENCIL | kappa_compact | B909/B910 | | ❌ (F = 5, invariant) |
| PENCIL | **vacuum_weight** | B888 | **new** | ❌ *at banked coord only* |
| PENCIL | **generic_weight** | B888 | **new** | ❌ *at banked coord only* |
| SPECTRAL | colored_twist_trace | B928 | new | ✅ |
| SPECTRAL | colored_twist_det | B928 | new | ✅ |
| SPECTRAL | octet_flip_trace | B928 | new | ❌ |
| SPECTRAL | h_S_B883 | B914 | new | ❌ |
| SPECTRAL | A_kappa | B938 | new | ❌ |
| CONTROL | K's generator s³−12s−5 | B937 | | ✅ *and EXCLUDED as vacuous* |

**Answer to Task 3: yes, they change the picture — in both directions at once.**

- The **value side goes 5/5 → 8/9** and the **pencil side goes 2/2 → 4/4 failing**. Read
  naively that is 12-of-13 and it looks *better* than what B947 saw. **This is the trap.**
- The one counterexample is on the value side, is invariant, and is the family the programme
  itself calls canonical. **One invariant counterexample ends a law claim regardless of the
  score**, and by B947's own pre-declared decision rule ("the pattern fails for at least one
  non-excluded family ⇒ **OUTCOME SPECIAL**") the enlarged census returns **SPECIAL again**.
- Two of the four pencil failures are gauge artifacts, so the clean 0/4 on that side is worth
  less than it looks.
- The spectral class splits 2/3, showing the statistic is not reading the taxonomy.

---

## 4. WHAT THE STATISTIC ACTUALLY MEASURES (COMPUTED, and it is not a taxonomy)

For a primitive integral cubic minimal polynomial with root α, `N(α) = −a₀/a₃`. Computed for
every family:

| family | N(α) = −a₀/a₃ | zeros over | poles over |
|---|---|---|---|
| V | 2³²3¹¹ / 953⁴ | {2,3} | {953} |
| W | 5¹² / 953⁴ | {5} | {953} |
| X_cross | 5⁶ / 953² | {5} | {953} |
| u | 5¹² / 2³²3⁸ | {5} | {2,3} |
| d_S, d_A | 953² / 2¹⁶3⁴ | {953} | {2,3} |
| m_S | 20417473 / 2¹⁹3⁴ | {20417473} | {2,3} |
| m_A | 29·72869 / 2¹⁹3⁴ | {29,72869} | {2,3} |
| μ | 13³ / 2¹⁶3⁴5²7³11 | {13} | **{2,3,5,7,11}** |
| κ | 19³ / 2¹⁴3⁴5³7²11·31 | {19} | **{2,3,5,7,11,31}** |
| T | 2¹⁹²3⁶⁰5⁶7¹⁸11⁶ / (179·1759·4889·632041·B₅₃)³ | **{2,3,5,7,11}** | **≥ 5 primes** |

So B947's two extreme clauses say exactly: **α's poles sit over ≤ 2 rational primes and its
zeros sit over ≤ 2 rational primes.** (*Cited, not re-derived:* for a primitive integral
minimal polynomial, p | a₃ ⟺ α is not p-integral at some place over p, and p | a₀ ⟺ α has a
zero at some place over p. Corroborated by B937's own banked divisors — `(W) = 𝔮₁(5)⁶𝔮₂(5)³·
𝔓₁(953)⁻²𝔓₂(953)⁻¹`, `N(W) = 5¹²/953⁴` — which match the norms computed here exactly.)

Two consequences that matter for any successor:

1. **The pencil half has a deflationary explanation.** μ and κ fail because the *denominator*
   of their norm is the leading coefficient of a determinant along a pencil — 2¹⁶3⁴5²7³11 and
   2¹⁴3⁴5³7²11·31, highly composite by construction. Their *numerators* are single prime cubes
   (13³, 19³) and pass the other clause cleanly. "Pencil cubics fail" is close to automatic and
   is not evidence about the value layer.
2. **The value half is not a law but it is a real regularity**, and it is a regularity about
   **divisors**: the eight holders' zeros and poles sit on the programme's structural places —
   953 (the observer's place), 5, and {2,3} — with the arithmetic residue confined to the
   middle symmetric functions (13, 17, 1129, 421493 for V; 367, 677 for W and X_cross; 41 for
   u; 23 for d_A). The exceptions inside the holders are m_S and m_A, whose numerators bring in
   20417473 and 29·72869 — primes with no structural role established anywhere in the bank
   (B937 §T5 explicitly records *"29 appears in no divisor computed in this cell except m_A's"*,
   cited). **So there is no clean structural predictor of divisor support in the banked
   material.** I checked, and I am not handing over a successor law dressed as one.

---

## 5. MB12 VACUITY LEDGER

| check | result |
|---|---|
| Can B947's criterion **PASS**? | **yes** — 8 value + 2 spectral families pass at their banked normalisation (COMPUTED) |
| Can it **FAIL**? | **yes** — T, 4 pencils, 3 spectral fail (COMPUTED) |
| Is it **decidable** on the material? | **not always** — T's leading coefficient has an unfactored 53-digit cofactor. Here the verdict survives (5 > 2 already decides), but the statistic is only *computable* on families whose coefficients happen to be smooth. Worth registering: **B947's statistic is not an effectively computable function of a banked cubic.** |
| Is it **invariant under the objects' own gauge freedom**? | **NO** for pencils (verdict flips for 2 of 4; diagnosis flips for μ). The vacuity *exclusion* is not invariant either — K's generator holds and is simultaneously excluded. |
| Does the proposed **partition** predict the outcome? | **NO** — refuted by T on the value side; not object-intrinsic on the pencil side; splits 2/3 on spectral. |

---

## 6. IF A SUCCESSOR IS WANTED — the one honest question left (NOT a seal design)

Not offered as a replacement for L137, and deliberately not designed as a cell, because I did
not earn it: the divisor restatement in §4 is *nearly tautological* (the extreme clauses **are**
a divisor-support condition), so restating it and sealing it would be sealing a definition.
The only non-circular successor is the mechanism question —

> For an element α of K arising from the object's Hermitian data, is the support of div(α)
> confined to the structural places {𝔓(953), 𝔮(5), places over 2 and 3}?

— and **§4 already answers it in the negative** on banked material (m_S's 20417473, m_A's
29·72869). A seat that wants this should pre-register the *exceptions* as the target, not the
rule. **Recommendation: do not open a successor register on this line without a mechanism in
hand.**

---

## 7. COMPUTED vs CITED

**COMPUTED here, in-sandbox:** every factorisation in §3 and §4; B946's V-table
reproduction; B918's agreement; the independent reproduction of B947's seven-family verdict
and its 5/2; B888's squarefree discriminant part 77; T's primitivity and root residual
(1.34e-54); T's P_lead lower bound ≥ 5 and P_const = {2,3,5,7,11}; T's leading coefficient
being a perfect cube; F values for all seven + T; the full ℚ\*-gauge-orbit scan for all five
pencil coordinates; T_row_products = T³ (3.5e-50); the mod-p splitting-type agreement of T and
all seven with K = ℚ[s]/(s³−12s−5) (128–130 primes each, 0 mismatches); disc(K) = 6237 = 3⁴·7·11;
μ's two banked coordinates giving different P_const.

**CITED, not re-derived:** B937's `O_K = ℤ[s]` index-1 claim (only disc and splitting types
re-derived); B937's exact place-by-place divisors for W/X_cross/u (their *norms* were
re-derived here and agree); B910's One-Field theorem and its 13⁶/19⁶ numerator law; B918's
[1,2] split; B866's `det = c·μ¹⁶` interpolation; B888's pencil factorisation (its squarefree
discriminant part 77 was re-derived from its own stored factors); B914's
`T_is_sigma2_of_explicit_K_element` and its exact rescaling-invariance identity; the standard
fact that for a primitive integral minimal polynomial p | a₃ ⟺ α has a pole over p and
p | a₀ ⟺ α has a zero over p.

**Honest limits.** (i) T's |P_lead| is a **lower bound** — the 53-digit cube-root cofactor is
unfactored; 5 > 2 decides regardless. (ii) F(T) ≥ 7 counts forced primes below 10⁶ only; a
lower bound, and 7 > 4 decides. (iii) Field identification is by mod-p splitting-type
agreement (Chebotarev evidence), not a proof; a direct `field_isomorphism` call returns `None`
and `maximal_order()` raises flint `CoercionFailed` on these inputs — the same sympy failure
B937 itself documents. I report the route and flag the disagreement rather than suppress it.
(iv) The classification of the five spectral cubics as "neither value nor pencil" is my
judgement, stated so it can be contested; it affects §2.2(c) only, not the refutation in (a).

---

## 8. FILES

`bounded_work.py` → `bounded_work_out.json` (gate, reproduction, census) ·
`arithmetic_detail.py` → `arithmetic_detail_out.json` (factorisations, T³, field, F) ·
`pencil_coord.py` → `pencil_coord_out.json` (gauge orbits, norms) ·
`work.json` (machine-readable verdict) · scouting predecessors: `SCOUT.md`, `t_probe.py`,
`t_newton.py`, `newton_probe.py`, `enlarge_probe.py`, `final_probe.py`.

**Not touched, not re-litigated:** B946's exact arithmetic (e₃/λ⁴ = 27, λ = 2304/953 forced);
B947's own verdict (OUTCOME SPECIAL — correct, and the enlarged census returns it again);
Gate 5; the E6/27/cascade material.
