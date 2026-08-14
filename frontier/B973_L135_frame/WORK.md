# B973 / L135 — WORK: the frame, the floor and M₁₂ are rebuilt on this bench, validated 51/51 against banked numbers, and the presence side's seven legs are now all computable here

**Date:** 2026-08-08 · **Cell:** B973 (work leg; follows this cell's SCOUT.md)
· **Lane:** MATHEMATICS. Gate 5 untouched. Nothing to `CLAIMS.md`. Nothing banked.

**Scout branch taken: (1).** SCOUT.md concluded the frame CAN be reconstructed from
banked material. This leg did it, validated it, and did not stop there.

---

## 0. VERDICT

> **The rebuild ran and the validation gate passed 51/51**, including all three
> mandated checks — **floor = 12, M₁₂ = 12, M₁₂ ∩ core = 0** — at **two primes never
> used on this bench** (41131, 41201). Nothing was tuned; no check was relaxed.
>
> On top of the validated frame, the **weight-line decomposition of M₁₂** — the one
> object SCOUT.md named as *reconstructible but not run* — now runs, and with it
> **all seven** of B958's presence-side legs are computable here. Combined suites:
> **90/90**.
>
> One genuinely new structural fact fell out, and it is an **arithmetic** one:
> **the frame's compact/noncompact split is mirrored in the field the M₁₂ charge
> weights live in.**

---

## 1. WHAT WAS BUILT (`rebuild.py`) — all COMPUTED

Imported `frontier/B961_frame_instrument/frame.py` as instructed; **𝔢₆ was not
reimplemented** (frame.py execs B854's `e6_centralizer.py`, which carries its own
Jacobi/exponent gates).

**Representation, named (house rule 3):** g₈, g₁₄, g₁₆, g₂₂ are **adjoint-sector**
elements — vectors in 𝔢₆ itself, the 2T-invariants of four principal-sl(2) blocks.
Every construction below is a **centralizer or a Killing-perp**, hence
**rank-preserving**. **No 27 VEV appears anywhere in this cell.** Nothing here
reaches, or claims to reach, rank 4.

| stage | object | how | tier |
|---|---|---|---|
| A | the four charges | `INV[8],INV[14],INV[16],INV[22]` from B854 | exact ℚ |
| A | **the frame** | ordered 4-tuple + Killing Gram `tr(ad gᵢ · ad gⱼ)` | exact ℚ |
| A | **the core** | `ker ad(g₈)` | exact ℚ |
| A | **the floor** | `z(g₈,g₁₄,g₁₆,g₂₂) = ker(ad g₁₄ \| core)` | exact ℚ |
| A | su(3)_colour | `derived(floor)` | exact ℚ |
| B | **κ** | det of the compact pencil on core/floor, 19 nodes + 6 surplus | exact ℚ |
| C | the compact walls | `ker(ad g₁₄ + sⱼ ad g₂₂)` at κ's roots | mod p |
| C | **M₁₂** | Killing-perp of span(W₁,W₂,W₃) | mod p |
| C | the μ-walls | roots of `det((ad g₈ + ρ ad g₁₆)\|M₁₂)`, 13 nodes + 6 surplus | mod p |

### 1.1 The validation gate — 51/51 PASS

Mandated three (targets **CITED** from `B911_cmt_document/CMT_DRAFT.md`):

| check | got | banked |
|---|---|---|
| **floor dim** | **12** | 12 |
| **M₁₂ dim** (p = 41131, 41201) | **12, 12** | 12 |
| **M₁₂ ∩ core** (p = 41131, 41201) | **0, 0** | 0 |

Banked cross-checks, all PASS: frame Gram **diagonal**, signature **(2,2)**, norms
digit-identical to the ledger's KF1 values
`+241532928, −317708697600, +988843239014400/13, −889958915112960000/19`;
core **30**; derived(floor) **8**, floor centre **4**, centre of derived(floor) **0**;
ν degree **18** with ν = c·κ⁶; κ = `2771822592000s³ + 3033676800s² − 56402640s − 6859`
**coefficient-identical**, irreducible, κ(0) = **−19³**, disc squarefree kernel **{7,11}**;
Killing rank **78**; wall dims **[30,30,30]**; span **66**; M₁₂ torus-invariant;
charge ranks **[12,12,12,12]**; det₁₂ = c·(cubic)⁴ with M₁₂-kernel **4** at each μ-wall.

**Prime hygiene.** 41131 and 41201 are disjoint from the record's
{40009, 40013, 40037, 40039, 40063, 40123, 40639, 40829} and from the scout's 40883.
So the banked frame numbers now stand at **four independent primes** on **two
independently built copies** of the chain.

### 1.2 One import removed

The μ-walls are **derived from M₁₂ itself** here — `det((ad g₈ + ρ·ad g₁₆)|M₁₂)` is a
12×12 determinant with entries affine in ρ, so **deg ≤ 12 is structural, not assumed**;
interpolated at 13 nodes with 6 surplus check-nodes, it factors as `c·(cubic)⁴` and its
roots are found by exhaustive scan. Those roots then **agree with the CITED solo-lane μ**
`500716339200ρ³ − 2075673600ρ² − 4769856ρ + 2197` at both primes. So the noncompact
cubic is a **conclusion** of this cell, not an input — the normalization hazard
SCOUT.md §2 flags (mixing the solo lane with the g₁₆-integralized B880 lane) cannot
bite, because no external cubic is fed in.

---

## 2. THE B958 SEVEN — now all computable here

B958's `arc_verdict.json` lists the seven legs a rebuilt frame would unlock.

| # | claim | this cell | tier | where |
|---|---|---|---|---|
| 1 | `[M₁₂,M₁₂]` escapes by exactly 4 **into the torus** | dim **16**, ∩M₁₂ **12**, **escape 4**; escape lands in the torus: **True**; ∩core = ∩floor = ∩torus = **4** | mod p ×2 | `presence7.py` |
| 2 | `[floor, M₁₂]` = 12 with **zero** escape | rank **12**, escape **0** | mod p ×2 | `presence7.py` |
| 3 | not a module over the FMT so(10) (escape 50) | z(wall) dim **46**; `[z,M₁₂]` rank **62**, **escape 50** | mod p ×2 | `presence7.py` |
| 4 | centre 0 | centre of derived(floor) = **0** (floor's own centre = 4) | **exact ℚ** | `rebuild.py` |
| 5 | twelve multiplicity-one **colour-blind** weight lines | **12** common eigenlines, all 1-dim, **12 distinct** weight 4-tuples; rank[su(3)_colour, M₁₂] = **0** | mod p ×2 | `weightlines.py` |
| 6 | closure under **exactly** W_frame, three free orbits | closed under all 4 Klein elements; **3 orbits, sizes [4,4,4], free**; **not** closed under any non-W_frame flip | mod p ×2 | `weightlines.py` |
| 7 | the orbit ↔ generation bijection | holds — **and is FORCED by (5)+(6)**, see §3.2 | mod p ×2 | `weightlines.py` |

Legs 1–3 reproduce values the scout saw at one prime; they are here at **two** primes,
with the escape of leg 1 **localized** (it lands in the torus, not merely somewhere
outside M₁₂ — that is a strictly sharper statement than "escapes by 4").

**Trap avoided (SCOUT.md §5.3).** Leg 5 uses `su(3)_colour := derived(floor)`, **not**
`frame.py`'s standard A₂ Levi. The two share a centralizer *dimension* (16) but are
different subalgebras of 𝔢₆; any test finer than a dimension must use derived(floor),
and this cell does.

---

## 3. WHAT IS NEW ON THIS BENCH (house rule 5: everything else is reproduction)

Prior art checked by grep before claiming novelty: `B911_cmt_document` (the frame,
core/floor, κ, M₁₂, μ-walls — all previously built here), `B939_klein_assembly`
(W_frame realized in Aut(𝔢₆)), `B958`/`B961` (dim Z(su(3)) = 16), `B877` (the FMT
weight-line lemma — a **different** weight-line statement, about Π-weights on the
48-block, not about M₁₂). **§1 and legs 1–4 are reproduction.** The following are not.

### 3.1 The weight-line decomposition of M₁₂ — RUN, first time here

The four `ad(gᵢ)|M₁₂` **commute** (computed) and simultaneously diagonalize into
**12 one-dimensional common eigenlines with 12 distinct weight 4-tuples**
(λ₈, λ₁₄, λ₁₆, λ₂₂) — multiplicity one, at both primes. Each charge shows exactly
**6 distinct eigenvalues**, i.e. **3 ± pairs, each value on 2 lines**.

W_frame acts on the weights by the sign rule σ·(λ₈,λ₁₄,λ₁₆,λ₂₂) with σ ∈
{(+,+,+,+), (+,−,+,−), (−,+,−,+), (−,−,−,−)} — this is the Klein group B939 realized
inside Aut(𝔢₆) (`assembly.py:349-353`, **CITED**). The weight set is **closed under all
four**, and — the discriminating half — **not closed under any of** lone-g₈, lone-g₁₄,
lone-g₁₆, or mixed (g₈,g₁₄). So the closure is under **exactly** W_frame, not under the
full sign group (ℤ/2)⁴. That is leg 6, and it had never been run.

### 3.2 Leg 7 is a corollary, not an eighth fact — a REDUCTION

A weight line sits at μ-wall ρ iff λ₈ + ρ·λ₁₆ = 0, i.e. ρ = −λ₈/λ₁₆ (λ₁₆ ≠ 0 on every
line — asserted in code, not assumed). Both nontrivial W_frame elements either fix
(λ₈,λ₁₆) or negate **both**, so **the ratio is constant on each W_frame orbit**. The
three orbits carry three **distinct** ratios (computed), and those ratios **are** the
three μ-roots (computed). Hence each orbit sits entirely at one wall and the map
orbits → walls is injective, therefore bijective.

**So the orbit↔generation bijection is forced by legs 5 and 6 plus ratio-distinctness.**
It is not independent evidence, and the presence side should not count it as such.

### 3.3 The weight field respects the frame's compact/noncompact split — NEW

This came out of a **failure**, recorded rather than tuned away. The first attempt fixed
the two primes 41131 and 41201; at 41201 the decomposition **crashed** — `ad(g₁₄)|M₁₂`
had eigenvalues outside 𝔽_p. Instead of fishing for a passing prime, the splitting
condition was stated as an explicit **prime criterion in advance** and the window was
**scanned and reported** (`weightlines.py`: 4 of 10 admissible), then measured per-charge
over **24 κ-split primes** (`weightfield.py`):

| charge | in 𝔽_p at | residual degrees seen |
|---|---|---|
| **g₈** (noncompact) | **24 / 24** | {0} |
| **g₁₆** (noncompact) | **24 / 24** | {0} |
| **g₁₄** (compact) | **16 / 24** | {0, **12**} |
| **g₂₂** (compact) | **16 / 24** | {0, **12**} |

The reading turns on one check that was **run, not inherited**: κ and μ generate one
cubic field K (CMT_DRAFT.md:78-80, **CITED**), so every κ-split prime should be μ-split —
**verified here at all 24**. Therefore "in 𝔽_p at every κ-split prime" means **"in the
wall field K"**, *not* "rational". Hence:

> **COMPUTED (mod-p evidence, 24 primes):** the **noncompact** charge weights on M₁₂ are
> visible in the wall field K itself, while the **compact** charge weights require a
> **proper extension of K**. When the compact weights fail they fail **totally**
> (residual 12: *no* eigenvalue in 𝔽_p), so the 12 weights split into 6 irreducible
> quadratics — consistent with a single quadratic extension.

**Scope and honesty.** 16/24 is consistent with density ½ (two-sided p ≈ 0.15) — 24
primes **cannot** distinguish a quadratic from a cubic-or-larger extension, and **this
cell does not identify the field.** The natural guess ℚ(√77) is **untestable on this
sample and was not tested**, because every prime in the scan was selected to split κ,
which already forces 77 to be a QR — the check would be **vacuous** (MB12). Naming the
extension is left as a stated open question in §6, not guessed.

---

## 4. MB12 VACUITY STATEMENT — including one check I will not defend

Every gate ran with a control that came out the **other** way, in the same code:

| check | can it fail? demonstrated by |
|---|---|
| frame abelian (6/6) | a random 𝔢₆ pair does **not** commute |
| Gram diagonal | a random 4-tuple's Gram is **not** diagonal |
| triple wall intersection = 12 | generic 30-dim triples in 78 meet in 0; got 12 three times, and it **equals the floor** |
| M₁₂ kernel = 4 at μ-walls | a **generic** ρ gives kernel **0** |
| escape routines | return **0** for `[floor,M₁₂]` and **50** for `[so(10),M₁₂]` in the same function |
| colour-blindness (rank 0) | same routine returns **26** on the core and **12** for the torus on M₁₂ |
| W_frame closure | **four** non-W_frame sign patterns all fail closure |
| ν deg 18 / det₁₂ deg 12 / charpoly deg 12 | degree bounds **structural** (affine-in-parameter matrices), plus 4–6 surplus check nodes each |

**The one I will not call discriminating: `M₁₂ ∩ core = 0`.** It is one of the three
mandated checks and it passed at both primes — but 12 + 30 < 78, so a *generic* 12-plane
misses a 30-plane anyway. I built a control proving the routine **can** return nonzero
(the K-perp of a 66-dim span engineered to contain core directions returns **12**), and
`[M₁₂,M₁₂] ∩ core` returns **4** in the same code — so the check is not *vacuous*. But
passing it is **weak** evidence. **The content of the M₁₂ construction sits in
span = 66**, which is where the discriminating work is: wall dims **[30,30,30]** with
**pairwise and triple intersections all equal to the floor**, closing inclusion–exclusion
3·30 − 3·12 + 12 = 66. Those are the numbers that could have come out otherwise, and did
not.

**Bound direction, stated once and obeyed:** mod-p nullity ≥ char-0 nullity; mod-p rank
≤ char-0 rank. Every Stage-C/weight-line number is therefore **evidence**, not a char-0
certificate. A mod-p rank **0** (colour-blindness) runs the bound the **wrong** way and
is recorded as evidence only — same fence the scout raised.

---

## 5. ERRORS OF MY OWN, RECORDED

1. **Triple-intersection formula wrong in my first draft.** I wrote
   `len(W0) + rank(W1+W2) − rank(W0+W1+W2)`, which is dim(W₀ ∩ (W₁+W₂)) — **not** the
   triple intersection. Caught by re-reading my own code before running, fixed with an
   explicit `inter_basis` (nullspace of [A | −B], pushed back through A).
2. **Fraction leak into the mod-p layer.** The Killing matrix built from `BB` came out as
   `Fraction`; `pow(Fraction, p−2, p)` raised. Fixed by asserting integrality
   (`denominator == 1`) rather than casting silently — the assert is the check.
3. **The 41201 crash** (§3.3) — kept as a result, not tuned away.
4. Inherited from the scout and honoured: basis-reduce bracket vectors **before** any
   dimension formula (the scout's `54 > 30` bug). `presence7.py` and `rebuild.py` both
   call `basis()` first.

The Killing-form shortcut `K[i][j] = Σ_{q,k} BB[i][q][k]·BB[j][k][q]` was **not trusted
blind**: it is cross-checked against `tr(ad eᵢ · ad eⱼ)` from `frame.ad` on 12 random
pairs, exactly, before use.

---

## 6. WHAT IS NOW COMPUTABLE HERE THAT WAS NOT — AND WHAT REMAINS BLOCKED

### Now computable (was not, before this cell)

1. **Any frame-side claim, end to end, without incoming code.** frame → core → floor →
   su(3)_colour → κ → compact walls → M₁₂ → μ-walls, from B854 + `frame.py`, in **~5 s**
   after the 𝔢₆ build. B958's "we verified data we never built" gap is **closed**.
2. **All seven** B958 presence-side legs (§2) — previously **zero** were runnable here.
3. **The weight-line decomposition of M₁₂**, and therefore any question phrased in terms
   of the twelve weights: orbits, stabilizers, wall assignment, colour-blindness.
4. **Wall-field arithmetic of the weights** (§3.3) — a question that could not even be
   *posed* before, because there were no weights to ask it about.
5. **μ without importing μ** (§1.2), so the two-normalization hazard is structurally
   avoided rather than navigated.

### Still blocked

1. **Char-0 exactification — the top open belt, unchanged.** Walls, M₁₂, every weight and
   every presence-side dimension are **mod-p tier**. `CMT_DRAFT.md:268-270` names the fix
   (restriction of scalars over K, the FMT recipe of B877). This cell **added primes, not
   tier**. Four independent primes is not a certificate.
2. **The identity of the compact weight extension** (§3.3). Well-posed for the first time,
   and **not** answerable by scanning more primes for a matching quadratic — that is
   fishing, and the natural candidate is untestable on κ-split primes. The clean route is
   char-0: factor the characteristic polynomial of `ad(g₁₄)` on 𝔢₆ over ℚ (78×78 exact,
   feasible but not attempted here), or exactify M₁₂ over K and read the weights off
   directly. Item 1 subsumes this.
3. **Conjugacy of `derived(floor)` with the standard A₂ Levi** — equal centralizer
   dimension (16 = 16) is **consistent with** conjugacy and is **not a proof of it**.
   Unproved here, as in the scout.
4. **`I-4`: G₂⊕G₂ ⊄ 𝔢₆** (`CMT_DRAFT.md:245`) — still the one unpinned external import.
   Not needed for anything in this cell; needed only to *type* the compact walls as
   so(8)⊕u(1)².
5. **The presence side's own §LXXXIII–LXXXVI / §XCII text** remains incoming material and
   is not in the repo. The repo no longer *needs* it to rebuild — but nothing here
   confirms or denies what that text says, and this cell is **not** a verification of the
   presence side.

### Corrections owed to earlier cells (from SCOUT.md §5, restated because they still stand)

- `B958_presence_scope/FINDINGS.md:11,19` — "no independent construction of M12 … has
  never been independently constructed here" is **incorrect as stated**: `B911_cmt_document`
  contained the construction. B958's *method* (defer rather than guess) was right; its
  *premise* was wrong.
- `B961_frame_instrument/FINDINGS.md:60-62` — the definitions **were** already precise
  enough to rebuild, in `CMT_DRAFT.md` §0 and the §2 ingredient table.
- `CMT_DRAFT.md:190` — the W_frame `[SOLO-TIER, VERIFICATION PENDING]` row is **stale**;
  B939 discharged it, and §3.1 here exercises it on M₁₂.

---

## 7. TIER AND SCOPE, STATED PLAINLY

- **Exact over ℚ:** the frame and its Gram, the core, the floor, su(3)_colour and its
  centre, ν, κ and its arithmetic. These are certificates.
- **Mod p (2 primes):** walls, span, M₁₂ and every M₁₂ property; legs 1–3, 5–7.
- **Mod p (24 primes):** the weight-field split of §3.3.
- **CITED, not re-derived:** the comparison targets in `CMT_DRAFT.md` (frame norms, κ, μ,
  the 30/12/46 dimensions, the one-field theorem κ ≅ μ), and B939's realization of
  W_frame inside Aut(𝔢₆). Everything else in this file is COMPUTED in-sandbox.
- **Nothing is banked.** This is a rebuild plus evidence, not a verification of the
  presence side, and it makes no claim about the Standard Model. Consistent with the
  banked ruling: every construction here is a centralizer or a Killing complement, hence
  rank-preserving, and **no 27 VEV is introduced** — so nothing here reaches rank 4 and
  nothing here claims to.

---

## 8. FILES

`rebuild.py` → `rebuild_results.json` (51/51) · `weightlines.py` →
`weightlines_results.json` (23/23) · `weightfield.py` → `weightfield_results.json`
(24 primes) · `presence7.py` → `presence7_results.json` (16/16) · `work.json`.
Scout probes from the earlier leg: `probe1..probe6`, `scout*.json`, `SCOUT.md`.

**Recommended next cell:** the char-0 exactification pass over K (item 1 above) — it is
now the *only* thing standing between this bench and a certificate-grade frame, and it
would settle §3.3's open field as a side effect.
