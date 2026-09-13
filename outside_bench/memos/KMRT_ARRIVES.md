# Memo 222 — KMRT ARRIVES: the record's most load-bearing unverified claim HOLDS, and the object's algebra is SPLIT

**Certificate:** `outside_bench/certificates/kmrt_arrives.py` ·
**Output:** `outside_bench/outputs/kmrt_arrives.txt` ·
**Seal:** `outside_bench/seals/KMRT_ARRIVES_PREREG.md`
(sha256 after ADDENDUM 1: `8a936c7709deed8892998a1acd5f62cb892dff944fe227aa74f6c3ce49833dba`;
pre-addendum `4eaefd038c97b80b08c35d3fe2be41d3e9e3ef62fb319a330afb1ec0dddfbabf`, committed
before the certificate was written).

**Source:** *The Book of Involutions*, Knus–Merkurjev–Rost–Tignol — supplied by the owner on
2026-09-13, sha256 `e3d1e114505a45d8c9288d0827cfa3877123d553a6648eb07c40baee7ddb0a4d`,
1,825,409 characters extracted. **It is a DRAFT: every internal cross-reference renders as
`(??)`.** Section numbers, titles, running heads and page numbers are intact and are what the
certificate anchors on; **no claim here rests on a reference that renders as `(??)`.** The
book is not committed to this repository.

| cell | question | outcome |
|---|---|---|
| 1 | does KMRT's own definition type the object's cubic ⁶D₄? | **A** |
| 2 | is a cyclic composition available over `K`? | **A** |
| 3 | is memo 204's pinned shape KMRT's normal form? | **A** |
| 4 | does the classification decide memo 204's open `E`-question? | **B** |
| 5 | is the bench's own citation right? | **A** |
| 6 | could `(a,77)_K` have been non-split at all? — **NOT PREREGISTERED** | **A** |

**C1–C7 all PASS** (C2 is N/A: CELL 4 produced no examples to check).

---

## 1. What was at stake, in the record's own words

Memo 203 reached its trialitarian conclusions **from search-result summaries with no full text
obtained**, and flagged itself:

> *"the section-3 correction is THE MOST LOAD-BEARING AND THE LEAST VERIFIED ITEM and should
> be checked against KMRT or Knus–Tignol by a seat with document access **BEFORE the record is
> edited**."*

**The record was then edited anyway.** Memo 204 used that correction to type the object **⁶D₄**
and to **REFUTE B882's ³D₄ naming**. So a banked refutation has been resting on an unverified
summary for two days. That is what this memo settles.

## 2. CELL 1 (A) — the correction HOLDS, verbatim

KMRT **§43.C**, quoted from the supplied text:

> *"We say that a trialitarian algebra `T = (E, L, ∆, σ, αᵢ)` of type **¹D₄** if `L` is split,
> **²D₄** if `L = F × K` for `K` a quadratic separable field extension over `F` isomorphic to
> `∆`, **³D₄** if `L` is a **cyclic** field extension of `F` and **⁶D₄** if `L ⊗ ∆` is a
> Galois field extension with group `S₃` over `F`."*

Every quantity that sentence tests, computed for `K = ℚ[x]/(x³−12x−5)`:

| clause | test | `K` |
|---|---|---|
| ¹D₄ | `L` split | `x³−12x−5` irreducible → **no** |
| ²D₄ | `L = F ×` quadratic | `L` is a cubic field → **no** |
| ³D₄ | `L` **cyclic** | `#Aut(K/ℚ) = 1`, disc `6237` not a square → **no** |
| **⁶D₄** | `L ⊗ ∆` Galois with group `S₃` | `K ⊗ ∆ = x⁶−30x⁴+225x²−308`, degree 6, **6 automorphisms**, order 6, **non-abelian** → **YES** |

> **Memo 204 was right, and B882's ³D₄ naming is refuted by KMRT's own definition rather than
> by a search summary.** The one clause the object satisfies is the ⁶D₄ clause; it satisfies
> none of the other three.

*Operational note on reading a label off a tool:* PARI names `S₃` acting on **six** points
**`D_6(6) = [3]2`** — the dihedral group of order 6 **is** `S₃`. The certificate's first
version tested the label **string** and returned the wrong outcome. The test used is now
**order 6 and non-abelian**, which is what the sentence actually asks. *(Bench error #22's
class: read the structure, not the printer's name for it.)*

## 3. CELL 2 (A) — and the cyclic/twisted distinction is real

KMRT **§36.B**, verbatim: *"Let `(L/F, ρ)` be a **cyclic** `F`-algebra of degree 3 with `ρ` a
generator of the group `Gal(L/F) = A₃`"* … *"Observe that the **choice of a generator ρ** of
the group `Gal(L/F)` **is part of the datum** defining a cyclic composition."*

`#Aut(K/ℚ) = 1`. **The `ρ` that §36.B makes part of the datum does not exist over `K`.** Memo
203's reading is exact.

And **§36.C** supplies what replaces it — *"we first extend the construction of a twisted
composition `C ⊗ L` … for `L` cyclic to an **arbitrary cubic étale algebra** `L`"* — by
descent from `L ⊗ ∆`, which **is** cyclic over `∆`. So "the two cases are treated by different
theorems" understates it: KMRT gives the object's case a **named construction**, `Γ(C, L)`.

## 4. CELL 3 (A) — memo 204's pin is KMRT's normal form, with the slots identified

**Thm 43.8:** *"`M₄(Q)` admits a trialitarian structure `T(Q)` **if and only if**
`N_{L/F}([Q]) = 1` in `Br(F)`."*
**Prop 43.9:** `N_{L/F}([Q]) = 1` ⟺ *"`Q ≃ (a,b)_L` with **`b ∈ F×`** and `N_L(a) = 1`."*

Memo 204 addendum 4 wrote the object's commutant as *"`(77, b)_K` with `b` **unknown**"*.
**KMRT fixes which slot is which:** the rational element is the **second** slot, and the
unknown is the **norm-one element of `K`**. So the object's candidate is

```
Q = (a, 77)_K ,   a ∈ K× ,   N_{K/ℚ}(a) = 1
```

and **43.11** says *every* such `a` yields a trialitarian algebra `E(a) = M₄(Q)`.

## 5. CELL 4 (B) — the preregistered search found nothing

342 admissible `a = x³/N(x)` (`x = c₀ + c₁t + c₂t², cᵢ ∈ [−3,3]`), norm-one identity checked
rather than assumed: **0 of 342 gave a non-split `(a,77)_K`.**

Preregistered outcome B is *"reported as a NOT-FOUND over a stated family, never as a proof of
nonexistence."* It is reported that way. **§6 is what changes it.**

---

## 6. CELL 6 (A) — **NOT PREREGISTERED**, and it is the result

**Filed under seal ADDENDUM 1, after CELL 4's outcome was read**, because standing rule
**R121/memo 213** requires it: *when a statistic comes out identical across every case, ask
whether it COULD have differed before banking the constancy.* Nothing in this section is
preregistered.

Let `n_p` := the number of primes `w` of `K` above `p` at which `77` is **not** a square in
`K_w` — the number of primes above `p` where `(77, ·)_K` is *capable* of ramifying at all.

`disc` of the sextic `M = K(√77)` is `3⁸·7³·11³`, **so `M/ℚ` ramifies only at 3, 7, 11.**

| `p` | `(e,f)` of the primes of `K` | `v_w(77)` | `n_p` |
|---|---|---|---|
| 2 | `[1,1], [1,2]` | `0, 0` | **1** |
| 3 | `[3,1]` | `0` | **1** |
| 7 | `[1,1], [2,1]` | `1, 2` | **1** |
| 11 | `[1,1], [2,1]` | `1, 2` | **1** |

and over every `p < 500`, `n_p` is **constant on each splitting pattern** (a non-constant
observation would have failed the run):

| pattern | `n_p` | first `p` |
|---|---|---|
| `f=[1,2]`, `e=[1,1]` (transposition) | 1 | 2 |
| `f=[3]`, `e=[1]` (3-cycle) | 0 | 13 |
| `f=[1,1,1]` (identity) | 0 | 73 |
| `f=[1]`, `e=[3]` (ramified) | 1 | 3 |
| `f=[1,1]`, `e=[1,2]` (ramified) | 1 | 7 |

> **`n_p ≤ 1` for EVERY rational prime `p`.** Exhaustive, not a sample: the primes ramified in
> `M` are exactly `3, 7, 11` and all three are computed individually; every unramified `p`
> falls into one of exactly **three** Frobenius classes in `S₃`, each with a computed
> representative, and `n_p` is a function of the class.

### The deduction

Two standard inputs, one of them KMRT's own:

* **Prop 43.6**, verbatim: *"For any trialitarian algebra `T = (E, L, σ, αE)` the central
  simple `L`-algebra `E` satisfies `N_{L/F}([E]) = 1 ∈ Br(F)`."* **This is not an assumption
  about the object — it holds for every trialitarian algebra.**
* Corestriction is additive on local invariants, and a quaternion class has `inv_w ∈ {0, ½}`.
  So `N_{K/ℚ}([Q]) = 1` says the ramified primes of `Q` lie over **each** rational prime in
  **EVEN** number.

Let `Q` be **any** quaternion algebra over `K` containing `K(√77)` as a maximal subfield, with
`N_{K/ℚ}([Q]) = 1`:

1. it can ramify at **at most one** prime above each rational prime (`n_p ≤ 1`);
2. the norm condition forces an **even** number above each rational prime;
3. so it ramifies at **no finite place**;
4. and `77 > 0` in all three real embeddings, so at **no real place** either.

**A quaternion algebra unramified at every place is split.**

> ### `E` IS SPLIT.
> Memo 204 addendum 4's open question — *"is `E` split over `K` itself?"*, the item it handed
> off as *"a question a seat with a number-theory package could answer directly"* — is
> **ANSWERED**, and answered without the 48×48 commutant that was *"twice killed by resource
> limits"*.
>
> **And CELL 4's outcome B was the true answer, not a search limit: there was never a
> non-split example to find.**

### CONTROL C6 — the count could have differed, and dramatically

The same `n_p`, with `77` replaced:

| `b` | max `n_p`, `p < 300` | attained at |
|---|---|---|
| **77** | **1** | 2 |
| 5 | **3** | 73 |
| 13 | **3** | 73 |
| 33 | **3** | 73 |
| −1 | **3** | 139 |
| 3 | **3** | 137 |

> **Every other `b` tested reaches the maximum possible value 3.** `n_p ≤ 1` is a property of
> **77 over this `K`**, not of the instrument.
>
> **INTERPRETIVE — and this is the part worth keeping.** The reason is not arithmetic luck.
> `77` is the squarefree part of `disc(K)`, so `ℚ(√77)` is `K`'s **quadratic resolvent** and
> `K(√77)` is `K`'s **Galois closure**. For a generic `b`, `K(√b)` is not Galois over `ℚ` and
> the count is unconstrained. **The object's algebra is split because the quadratic face it
> carries is its own discriminant field** — the same fact that made the object ⁶D₄ in CELL 1
> and that killed B882's ³D₄ in memo 204. One fact, three consequences.

### What `[E] = 1` then buys

**Prop 44.16(1)**, verbatim: *"If `T = (E, L, σ, αE)` is a trialitarian algebra such that
`[E] = 1 ∈ Br(L)`, then there exists a twisted composition `Γ = (V, L, N, β)` such that
`T = End(Γ)`."* And **(2)** classifies those: `End(Γ) ≃ End(Γ′)` iff `Γ′ ≃ Γ_λ` for some
`λ ∈ L×`.

> The object's trialitarian algebra is `End(Γ)` for a **twisted composition over `K`**,
> classified up to `Γ → Γ_λ`, and §36.C constructs such `Γ` for an arbitrary cubic étale `L`
> by descent from `L ⊗ ∆`. **Memo 203 §4 guessed at exactly this** — *"B882's question becomes
> concrete and FINITE … A computation, not a citation"* — from search summaries. It is now a
> named object with a construction and a classification.

---

## 7. CELL 5 (A) — BENCH ERROR #29, and it is small

The bench's standing ask has read **"KMRT Ch. VII §43 and §44.B"** since memo 203. In the
supplied draft, **§43 and §44 are Chapter X** (*"X. TRIALITARIAN CENTRAL SIMPLE ALGEBRAS"*)
and **§36 is Chapter VIII** (*"VIII. COMPOSITION AND TRIALITY"*). The **section** numbers in
the ask were right; the chapter was not. Nothing downstream used the chapter number.

## 8. What is NOT claimed

* **This does not show the object's commutant IS a trialitarian `E`.** That is memo 204
  addendum 4's derivation, used here as an **input** and labelled as one. The deduction is
  conditional on it, and on the ⁶D₄ typing that CELL 1 verified.
* **The `F`-symbol / gauge questions of memos 218–220 are untouched.** Different object.
* CELL 6 is **not preregistered**, and no table in it may be cited as if it were.
* **Gate 5 untouched. Nothing promotes. No arc is retracted.** `docs/` and `frontier/` are not
  edited by this bench.

## 9. Operational — four silent failures, one class, and a rule

The certificate was wrong four times before it was right, and **every failure exited 0**:

1. a multi-line `for(...)` in a GP **file** is a syntax error *per line* — the loop never ran,
   the loop variables stayed **symbolic**, and a "hit" was reported from a symbolic expression;
2. a function definition's own braces **nested** inside `gp_block`'s wrapper braces broke the
   parse and **every table came back empty** — while `max n_p` printed a confident `0`;
3. `arg` is a **reserved GP function name**;
4. the helper **discarded stderr**, which is why all three were silent.

The first of these produced a **false CELL 4 hit** that was caught only because its printed
`a` was visibly symbolic. The second produced **`n_p = 0` everywhere**, which was caught only
because it **contradicted Chebotarev** — an empty extension cannot have every prime split.

> **RULE ADDED (#25): a subprocess that exits 0 is not a subprocess that worked.** Capture
> `stderr` and treat it as fatal, and check every table the subprocess was supposed to fill
> for **emptiness** rather than trusting it. Both are now in the certificate.
>
> **And the check that actually saved this memo was a THEORY CHECK, not a control:** `n_p = 0`
> for all `p` was arithmetically impossible, and noticing that is what exposed a wrong API
> indexing. *Controls catch what you thought to guard; a contradiction with a theorem catches
> what you didn't.*

---

*Every number above comes from `outside_bench/outputs/kmrt_arrives.txt`.*
