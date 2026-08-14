# B972 — L137 SCOUT: is the value/pencil split of B947 a real, pre-statable partition?

**Date:** 2026-08-08 · **Seat:** scouting subagent · **Lane:** MATHEMATICS · Gate 5 untouched.
**Status:** SCOUTING ONLY. Nothing here is sealed, nothing is banked, no verdict is claimed
against any criterion. Every number below was computed in this sandbox; standard facts are
labelled *cited, not re-derived*.

---

## HEADLINE — the recommendation

> **L137 should be CLOSED, and not as "unsealable for want of a criterion". It should be
> closed because the post-hoc observation it registers is REFUTED by material already banked
> in this repository before B947 ran.**
>
> **T** — B914's colorless coupling invariant, the object the LAW_MAP registers as
> *"THE ONE-NUMBER TABLE … all six **normalization-free** colorless couplings EXACTLY equal"*
> — is a value-layer family by the programme's own registry, and it **FAILS** B947's pattern.
> It fails at its banked normalisation (|P_lead| ≥ 4, |P_const| = 5, both > 2) **and it fails
> invariantly** (F ≥ 6; see §4).
>
> So "the thinning holds on the value layer and fails on the pencils" is not merely
> un-sealed — **it is false**. B947 was right to refuse the rescue, and right for a stronger
> reason than it knew.

There **is** something real underneath, and §5 says what it is and how to register it
honestly. It is not a value/pencil distinction.

---

## 1. (a) THE DEFINITIONS, IN THE PROGRAMME'S OWN WORDS

### 1.1 Where the seven come from — and what B941 calls them

The seven families are defined nowhere but in **B941**, and B941 calls **all seven** value
families. Verbatim, `frontier/B941_branch_symmetric/FINDINGS.md`:

> "**Seven banked families** — V (hierarchy), W (the S–A mixing overlap²), d_S and d_A
> (the twist ratios), m_S (the flip mass), μ (charge cubic), κ (compact cubic) — each reduced
> to (Tr, e₂, N) from its banked minimal polynomial."

and its `arc_verdict.json`:

> "The table: **seven banked value families** (V, W, d_S, d_A, m_S, mu, kappa) reduced to their
> elementary symmetric functions…"

and `PROGRESS_LOG.md:9299`:

> "**seven banked value families** (V the hierarchy, W the S-A mixing overlap^2, d_S and d_A
> the twist ratios, m_S the flip mass, **mu and kappa the pencil cubics**)"

**This is the single most important documentary fact for L137.** The arc that *created* the
table calls the whole set "value families", and marks μ and κ with a parenthetical
"the pencil cubics" inside that same phrase. There is a **naming** difference in the record;
there is **no partition** in the record. Re-partitioning B941's table into two classes is an
act B947 performed, not one it inherited.

### 1.2 Each family's actual definition (the defining arc, quoted)

| family | defining arc | what the number IS |
|---|---|---|
| **V** hierarchy | B918 | "the three generation weights v_g² are one K-element's conjugate orbit, v_g² = V(ρ_g), with minimal cubic led by 953⁴ — **the seventh cubic of the √77 family**" |
| **W** mixing² | B930 / B937 | "the same-generation overlap-squared is **ONE K-element** with minimal polynomial …" |
| **d_S, d_A** twists | B916 | "The per-line ratio d_i = q^{H′}_i / q^{H+}_i is a **cubic irrationality of the value field K** (branch-indexed)"; explicit minpolys given in B916's prose |
| **m_S** flip mass | B928 | "**Sheet entry 1 — vacuum-line overlaps** m_S = h_F(S,S)/h(S,S) **∈ K**" |
| **μ** charge cubic | B866 | roots of `det(48×48 minor)(t)` of the **pencil** ad(x₈ + t·x₁₆) — the three distinguished charge lines where the centralizer enhances 30 → 46. `det(...)(t) = c·(500716339200t³ − 159667200t² − 28224t + 1)¹⁶` |
| **κ** compact cubic | B910 / B909 | "the compact pair's **pencil** g14 + s·g22 on the 18-dim core/floor quotient; ν(s) = det, 20-point exact interpolation … ν = c·κ⁶ exactly, **κ(s) = 2771822592000·s³ + 3033676800·s² − 56402640·s − 6859**" |

So in the programme's own terms the honest **definitional** distinction available is:

- **V, W, d_S, d_A, m_S** are *elements of K* — intrinsically-normalised, dimensionless
  ratios (an overlap², a weight, a ratio of two Hermitian forms, a ratio of two H-norms).
- **μ, κ** are *loci in a pencil* — root sets of a determinant along a line
  `A + t·B`, whose coordinate `t` carries a **free ℚ\*-scale**.

That distinction is real, pre-statable, and readable without touching a coefficient.
**It is also not what B947 measured, and it does not survive contact with the data.**

### 1.3 "pencil cubic" is a pre-existing label

The term is not invented at B947. `frontier/B910_kappa_class/FINDINGS.md` heads with
"the Kummer class of the **compact-pencil cubic** κ"; B902 treats "the three cubics —
μ (the charge cubic), B888's generic weight cubic …"; B886 is "THE MATTER PENCIL". The
**label** pre-exists; the **partition of B941's seven** does not.

---

## 2. (b) THE CRUX — three independent findings, each fatal

### 2.1 FINDING 1 (decisive): a banked VALUE family that fails — T

`frontier/B914_ratio_table` banks **T**, the colorless coupling invariant
`T := |c_t|²/(s_i s_j s_k)`, with an explicit degree-3 integer-primitive minimal polynomial
(`results.json → T_single.minpoly_desc_coeffs`). B914's own framing:

> "T is **canonical**: the cubic is the banked integer-primitive ±1 form … and T is invariant
> under the one-real-scale freedom of H"

> "T is invariant under any per-atom complex rescaling … verified as an EXACT identity"

and `docs/LAW_MAP.md:197`:

> "**THE ONE-NUMBER TABLE** | all six **normalization-free** colorless couplings EXACTLY
> equal: T = σ₂(t_K), deg-3"

T is a value-layer object by every criterion the programme applies — dimensionless,
branch-symmetric, ratio-only, normalisation-free, and registered as a law in §F, the section
titled *"The measurement cascade and the value layer."* It was simply **not among B941's
seven**.

**Computed here** (`t_probe.py` → `t_probe_out.json`):

- gate first — the banked 50-digit T **is** a root of the banked cubic
  (relative residual `1.34e-54`); the banked coefficient vector **is** primitive (content = 1);
- `|coeff| digit sizes = [202, 175, 144, 113]`;
- **P_lead** ⊇ {179, 1759, 4889} (each to multiplicity **3**) plus a 174-digit unfactored
  cofactor ⇒ **|P_lead| ≥ 4 > 2**;
- **P_const = {2, 3, 5, 7, 11}** ⇒ **|P_const| = 5 > 2**.

> **T fails B947's pattern on BOTH extreme conditions, and not marginally.**

And the failure is not an artifact of normalisation (`t_newton.py`): over the primes trial
division reaches, **F(T) ≥ 6** — six primes are forced into an extreme, while the two extremes
can hold at most 4 between them (see §4). **No rescaling of T can satisfy the pattern.**

*Honest limit:* |P_lead| is a **lower bound** — the 174-digit cofactor is not factored. The
bound is sufficient: 4 > 2 already decides. B947's statistic is, incidentally, **not
computable** for T without factoring that cofactor — the criterion is only decidable on
families whose coefficients happen to be smooth, which is itself worth registering.

### 2.2 FINDING 2: the two classes are not different arithmetic objects — one field

Computed here by mod-p splitting-type comparison against
**K = ℚ[s]/(s³ − 12s − 5)** (B937's monogenic model of the charge field, `disc = 6237 = 3⁴·7·11`,
`O_K = ℤ[s]`), 138 primes, none dividing any family's support:

| family | primes tested | splitting-type mismatches |
|---|---|---|
| V_hierarchy | 138 | **0** |
| W_mixing_sq | 138 | **0** |
| d_S_twist | 138 | **0** |
| d_A_twist | 138 | **0** |
| m_S_flipmass | 138 | **0** |
| **mu_charge** | 138 | **0** |
| **kappa_compact** | 138 | **0** |

> **All seven B941 families generate the same cubic field K.** The five that hold and the two
> that fail are seven *different elements of one field*, presented in seven different ℚ\*-normalisations.

This is corroborated by three banked results, so the identification is not resting on my
Chebotarev evidence alone: B910's **One-Field theorem** ("κ splits [1,2] over K"), B918's
"[1,2] split over K, root certified exactly" for V, and B937's monogenic model.

**Consequence:** whatever B947's statistic separates, it cannot be an arithmetic property
distinguishing "the value layer" from "the pencils" — there is only one field here. It is a
property of *which element* and *in which normalisation*.

*Honest limit:* splitting-type agreement at 138 primes is Chebotarev evidence, not a proof.
A direct `field_isomorphism` call returned `None` and `maximal_order()` raised a flint
`CoercionFailed` — the same class of sympy failure B937 itself documents ("sympy's
`prime_valuation` raises `CoercionFailed` on these inputs"). I report the splitting-type route
and flag the sympy disagreement rather than suppress it.

### 2.3 FINDING 3: B947's statistic is not an invariant of a pencil cubic

A pencil cubic's coordinate carries a free ℚ\*-scale (the pencil `A + t·B` has canonical
0 and ∞ but no canonical unit). Under `t → t/c` the coefficient vector goes
`(a₃, a₂, a₁, a₀) → (a₃b³, a₂ab², a₁a²b, a₀a³)`, re-primitivised.

**The repo banks μ in two different normalisations, and B866 says so explicitly:**

> "the cubic is THEIR μ | **theirs(13t) − 2197·mine(t) = 0 identically** — same polynomial,
> their ρ = 13t"

Re-derived here (`sp.expand(lhs-rhs) == 0` ✓). B947 used the ρ = 13t form. The statistic:

| μ, same locus | P_lead | P_const | P_mid_only | total support | B947 verdict |
|---|---|---|---|---|---|
| B866's own `t` | {2,3,5,7,11} | **{}** | {} | **5** | fails |
| B941/B947's `ρ = 13t` | {2,3,5,7,11} | **{13}** | {} | **6** | fails |

Same object, two banked coordinates, **different P_const and different total support**. The
reported diagnosis ("const {13}, empty mid-only") is a coordinate artifact. The *verdict*
survives here only because `|P_lead| = 5` is stable — luck, not design.

For the **other two** pencil cubics it does not survive: B888's vacuum- and generic-weight
cubics fail at their banked normalisation but are **satisfiable** at another (§3).

**And the MB12 point.** K's canonical monogenic generator, `s³ − 12s − 5`, gives
`P_lead = {}`, `P_const = {5}`, `P_mid_only = {2,3}` — the pattern **HOLDS**; and its total
support is **3**, so B947's own pre-declared vacuity rule (total ≤ 3 ⇒ EXCLUDED) would have
**excluded** it. For one and the same field, renormalisation reaches *holds*, *fails*, and
*excluded-as-vacuous*. **B947's exclusion threshold is itself not normalisation-invariant** —
worth a line in the ERROR/METHOD record independently of L137.

### 2.4 So: is there a principled, pre-statable criterion?

**A definitional one exists** — "intrinsically-normalised element of K" vs "locus in a pencil
with a free coordinate scale" — and it is genuinely declarable in advance of looking at
outcomes. **But it does not predict the outcome**, because:

- a family on the *value* side (T) fails, and fails invariantly;
- two families on the *pencil* side (B888's) fail only at their banked coordinate;
- the two classes are elements of one field, so no arithmetic mechanism is available to
  make the prediction mean anything.

**A seal built on "value families hold, pencil cubics fail" would be sealing a false
statement.** That is the outcome to report.

---

## 3. (c) OTHER FAMILIES — the sample CAN be enlarged, and enlarging it is what kills the split

All computed here from banked artifacts, with each source arc's own banked identity
reproduced first where one exists.

### 3.1 Two further PENCIL cubics — B888 (`enlarge_probe.py`)

Rebuilt from `frontier/B888_two_fields/pencil_factors.json` using **B888's own `bcubic()`**,
and gated on reproducing B888's banked squarefree discriminant part **77** (both ✓):

| cubic | coeffs (primitive) | P_lead | P_const | P_mid_only | holds? |
|---|---|---|---|---|---|
| **vacuum-weight** (mult-1, field ≠ K) | [2197, 0, −6963104474726400, 2923811689117777920000] | {13} | {2,3,5,7,11} | — | ❌ |
| **generic-weight** (mult-8, field = K) | [2197, 0, −1740776118681600, −365476461139722240000] | {13} | {2,3,5,7,11} | — | ❌ |

Both fail with the **same signature as μ mirrored**: one extreme a single prime cubed (13³),
the other a 5-prime number, empty mid-only. (Compare B910's banked numerator law: *"α_μ carries
13⁶, α_κ carries 19⁶ — each pencil's Kummer element wears its own prime."*)

### 3.2 One further VALUE family — T (§2.1). **This is the counterexample.**

### 3.3 The consolidated table (`final_probe.py` → `final_probe_out.json`)

| class | family | banked-normalisation holds | F | satisfiable by *some* normalisation |
|---|---|---|---|---|
| VALUE | V_hierarchy | ✅ | 3 | yes |
| VALUE | W_mixing_sq | ✅ | 2 | yes |
| VALUE | d_S_twist | ✅ | 3 | yes |
| VALUE | d_A_twist | ✅ | 3 | yes |
| VALUE | m_S_flipmass | ✅ | 3 | yes |
| **VALUE** | **T (B914)** | **❌** | **≥ 6** | **no** |
| PENCIL | mu_charge | ❌ | 5 | **no** |
| PENCIL | kappa_compact | ❌ | 5 | **no** |
| PENCIL | vacuum_weight (B888) | ❌ | 4 | yes |
| PENCIL | generic_weight (B888) | ❌ | 4 | yes |
| (alt coord) | mu @ B866's own t | ❌ | 5 | no |
| (field-canonical) | s³−12s−5 | ✅ (and would be *excluded* as vacuous) | 1 | yes |

Note what happens to the "clean" story as the sample grows: on B941's seven the split reads
5/2 along the naming line; add B888's two and it reads 5 value-hold / 4 pencil-fail (a
tidy 9/9 separation, tempting); **add T and the separation is gone.**

### 3.4 Further enlargements available but NOT computed here

- **`T_row_products` (T³)**, B914 — banked deg-3 minpoly, same factorisation wall.
- **`h_S_B883` / `h_A_B883`**, B914 — the charpoly factors of Mc; `h_S = [1, 0, −535623511707648, 2928461724187049852928]` is already monic (a spectral, not a value, object — classify before use).
- **The sixth cubic of the √77 family.** `docs/LAW_MAP.md:214` and B909 bank a "six-cubic √77 law"; this scout positively identified five — μ, generic-weight, vacuum-weight, κ, and V (B918 calls HIER "the **seventh** cubic of the √77 family") — and did **not** pin the sixth. B911's CMT_DRAFT §7 item 9 already registers the matching open question: *"with six cubics on one resolvent, a completeness question (is there a seventh pencil cubic in the frame, and must it share the resolvent?) — register, do not chase."*

---

## 4. WHAT IS ACTUALLY UNDERNEATH — the invariant the pattern was tracking

The freedom `t → t/c` acts on the p-adic valuation vector by a **tilt**:
`w_d = v_p(a_d) + (3−d)·g`, `g ∈ ℤ`, then subtract the minimum — and `g` may be chosen
**independently at each prime**, since `c` ranges over ℚ\*. Define

> **F(P) := #{ primes p : p cannot be pushed out of BOTH extreme coefficients by any tilt }**
> = # primes whose p-adic Newton polygon of P is not a straight segment of integer slope
> = # primes at which the three roots do not all share one integral p-adic valuation.

`F` is invariant under the whole ℚ\*-orbit, and it is the real content of B947's statistic:

- `|P_lead| ≤ 2` and `|P_const| ≤ 2` **require F ≤ 4** — the two extremes hold at most 4
  forced primes between them. That is the whole "thin extremes" half.
- `|P_mid_only| ≥ 1` requires at least one *unforced* prime to be present. That is the whole
  "fat middle" half.

Computed F values (tilt scan `g ∈ [−60, 60]`, stable against widening from `[−12,12]`):
**V 3 · W 2 · d_S 3 · d_A 3 · m_S 3 · vacuum 4 · generic 4 · μ 5 · κ 5 · T ≥ 6 · s³−12s−5: 1.**

So the honest re-description of B947's result is arithmetic, not taxonomic:

> **B941's five holders are elements of K whose divisors are rationally-generated away from
> exactly two or three primes. μ, κ and T are elements whose divisors are not.**

Reading F for the holders: V's forced primes are **{2, 3, 953}** — 953 to the fourth in the
leading coefficient is precisely B918's *"its denominator ideal is the observer's place to the
fourth power"*, and {2,3} is the norm. The un-forced primes 13, 17, 1129, 421493 are exactly
B946's degree-graded residue, and they are un-forced **because** they live only in `e₁`/`e₂`.
That is the same fact B946 banked, correctly stated and now normalisation-free.

---

## 5. RECOMMENDATION

1. **Close L137.** Not "unsealable" — **refuted**. Record the counterexample (T) by name.
   The value/pencil re-description would have been post-hoc rescue *and* wrong; B947's refusal
   was correct, and this is the strongest possible vindication of the seal discipline.

2. **Do not seal any successor in the B947 coefficient-support form.** It is not an invariant
   of a pencil-coordinate object, and its vacuity exclusion is not invariant either — for one
   field, renormalisation reaches *holds*, *fails*, and *excluded*.

3. **If a successor is wanted, seal the F-form, and seal it against the FULL banked census,
   not a chosen seven.** F is normalisation-free, integer-valued, and non-vacuous (observed
   range 1–6 across ten families, both outcomes live). The question worth pre-registering is
   the mechanism one: *for an element of K, is F ≤ 3 equivalent to some banked structural
   property* (e.g. the divisor being supported on the observer's place plus the norm primes)?
   That question is about the arithmetic of elements of one cubic field — which is what the
   data says this is — and it is falsifiable.

4. **Two by-products for the method record, independent of L137:**
   (i) B947's pre-declared vacuity exclusion (total support ≤ 3) is **not normalisation-
   invariant** — MB12 checks should include "is the criterion invariant under the object's own
   gauge freedom", not only "can it pass and can it fail";
   (ii) B941's table is **seven elements of one cubic field**; any future cross-family
   statistic should say so up front, because it changes what a cross-family agreement could
   possibly mean.

5. **Not re-litigated, and not touched:** B946's exact arithmetic (e₃/λ⁴ = 27, λ = 2304/953
   forced, the degree-graded residue for V) — untouched, and §4 shows *why* the V statement is
   robust while the generalisation was not. B947's own verdict (OUTCOME SPECIAL) — untouched
   and correct. The LAW_MAP row as B947 narrowed it is accurate for the five; it should gain
   the sentence that the value/pencil gloss is now refuted, not merely unclaimed.

---

## 6. FILES

`newton_probe.py` → `newton_probe_out.json` · `enlarge_probe.py` ·
`t_probe.py` → `t_probe_out.json` · `t_newton.py` → `t_newton_out.json` ·
`final_probe.py` → `final_probe_out.json` · `scout.json`

Every figure in this document was produced by those scripts in this sandbox. Cited-but-not-
re-derived: B937's `O_K = ℤ[s]` index-1 claim (I re-derived only `disc(s³−12s−5) = 6237 =
3⁴·7·11` and the splitting-type agreement); B910's One-Field theorem; B918's [1,2] split;
B866's `det = c·μ¹⁶` interpolation; B888's pencil factorisation (I re-derived its squarefree
discriminant part 77 from its own stored factors).
