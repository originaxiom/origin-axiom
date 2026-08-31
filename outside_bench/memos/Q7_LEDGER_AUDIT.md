# MEMO 167 — THE ROW THAT LEFT THE TALLY, AND THE COMPUTATION THAT CLOSES IT

**Banked 2026-08-31 · outside bench (lane 1B).** Seal `seals/Q7_LEDGER_AUDIT_PREREG.md`, pushed
before the certificate was written. Certificate `certificates/q7_ledger_audit.py`; output vendored at
`outputs/q7_ledger_audit_out.txt`. **This audits this bench's own chain (memos 160/161/162).**
Gate 5 untouched: exact arithmetic and modular reduction, no measured value.

> **`SUMMARY: A-CENTRAL | A2-NONDEGENERATE | B-RATIONAL`** — two as declared, **one against my prior.**

---

## 0. The headline, and it cuts both ways

**Q7 is at four of five. It was at four of five before this cell too — but it was right by accident.**
The row that made the count four was a **substitution**, and the row it displaced was **unproved**.
Both halves are now fixed, and the fix runs in the closing direction:

> **ℚ-simple is CLOSED, by computation.** The stabilizer's **centroid has dimension 1** and its
> **Killing form is nondegenerate**, so it is **central simple** over ℚ. In dimension 28 that forces
> **type D₄** — uniquely, since no other simple Lie algebra has dimension 28. **A form of an
> absolutely simple group is absolutely simple, hence ℚ-simple**, inner or outer.

So the number does not move. What moves is that **four of five is now four proved things** rather
than three proved things and a substitution.

---

## 1. What was wrong with the ledger

**Memo 160's certificate types the five hypotheses:**

> simply connected · **ℚ-simple** · `H(ℝ)` non-compact · the stabilizer *is* a form of Spin(8) ·
> orbit count = class set

**Memo 162 §3 — and `THE_GATE_SENDS.md` addendum 4, which is the draft that would have been sent —
tally "four of five" over a different five:**

> `H(ℝ)` non-compact · stabilizer algebra is D₄ · **the object's own pair is regular** ·
> simply connected · orbit count = class set

**`ℚ-simple` is in the first list and not the second.** What sits in its slot is *pair regularity* —
a real and valuable result (`B969`, and memo 162's T-3 was right to prize it), but **not a hypothesis
of Kneser–Platonov**. The count stayed at five while the contents changed.

**And ℚ-simple was never closed — it was conditioned, on the wrong thing.** Memo 160 typed it
`HOLDS-CONDITIONALLY`, on the twist being **outer** (trialitarian). That condition is **irrelevant to
ℚ-simplicity**: every form of an absolutely simple group is absolutely simple and therefore ℚ-simple,
inner or outer alike. What actually threatens ℚ-simplicity is a **direct-sum decomposition** — and
that was never tested. The condition memo 160 attached was not the condition the hypothesis needs.

---

## 2. BENCH ERROR #19 — memo 161's `S3-SIMPLE` was a necessary condition wearing a verdict's name

Memo 161 reported the stabilizer **SIMPLE**. Its test, in full:

> centraliser dimensions across the basis are min 4, max 4, with **zero** elements having centraliser
> ≥ 14 — *"which a whole `g₂` factor would force"*.

That is a **necessary condition against one named alternative** (`𝔤₂ ⊕ 𝔤₂` over the same field), not
a proof that the algebra has no proper ideal. The certificate's own inline comment scopes it
correctly (*"so(8) is simple; g2 (+) g2 is not"*); **the verdict label and the memo's prose do not.**

**And the alternative it cannot see.** For `L/F` quadratic, `Res_{L/F}(𝔤₂)` has

- `F`-dimension **28**,
- generic centraliser `F`-dimension **4** (twice the `L`-dimension 2),

so it reproduces **every number memo 161 measured**. Memo 161's test was built against a *direct sum
over F*, where one whole factor centralises another; a Weil restriction has **no such F-factor**, so
the test's premise does not apply to it at all. **It was never excluded.**

This is the same class as bench error #16 — *a cell that records a reading while wearing the shape of
a test.* The difference, and it matters: **the conclusion was true**, and the gap was closable in one
computation. The label outran the evidence; the evidence has now caught up.

---

## 3. A — THE CENTROID: the discriminator memo 161 needed

For a Lie algebra 𝔥 over F, `Γ(𝔥) = {T ∈ End_F(𝔥) : T[x,y] = [Tx,y] ∀x,y}`. Scalars always lie in it.

| `dim_F Γ` | what 𝔥 is |
|---|---|
| **1** | **central** over F — excludes `𝔤₂ ⊕ 𝔤₂` **and** `Res_{L/F}(𝔤₂)` in one computation |
| **2** | `𝔤₂ ⊕ 𝔤₂` (Γ = F × F) **or** `Res_{L/F}(𝔤₂)` (Γ = L) |

**Computed**, on memo 161's own stabilizer rebuilt from B575's basis at the same seed (dim 28
reproduced), with all 378 brackets re-solved and **each verified on all 729 coordinates** so
subalgebra closure is proved and not assumed:

| | result |
|---|---|
| **A-2 Killing form rank**, exact over the field | **28 of 28 → nondegenerate** (Cartan ⟹ **semisimple**) |
| **A-1 centroid**, 784 unknowns, 21168 equations, `p = 100003` | rank 783 → **nullity 1** |
| **A-1 centroid**, same system, `p = 1000003` | rank 783 → **nullity 1** |

**The modular method is rigorous in the direction used, and only that direction is used.** Reduction
can only *drop* rank, so `nullity_p ≥ nullity_F`; a modular **1 proves `dim_F Γ ≤ 1`**, and scalars
force `≥ 1`. Hence `dim_F Γ = 1` **exactly** — and the argument never needs the modulus to give the
equality. (Memo 162 marked the same distinction; it is kept here.)

**The chain, each step stated:**

1. Killing form nondegenerate ⟹ **semisimple**.
2. Semisimple with `dim Γ = 1` ⟹ exactly one simple factor, with centroid F ⟹ **central simple**.
3. Central simple ⟹ **absolutely simple** (simple after base change to `F̄`).
4. **28 is the dimension of no simple Lie algebra but D₄** — `A_n`: 3, 8, 15, 24, 35; `B_n`/`C_n`:
   3, 10, 21, 36; `D_n`: 6, 15, **28**, 45; `G₂` 14, `F₄` 52, `E₆` 78. ⟹ **type D₄**, and rank 4 is
   then automatic rather than an independent measurement.
5. A form of an absolutely simple group is absolutely simple ⟹ **ℚ-simple**. ∎

**So this cell does two things at once:** it closes hypothesis 2, and it **upgrades memo 161's D₄
identification from a necessary-condition test to a proof.**

---

## 4. B — THE BASE FIELD: my declared prior was wrong, and the worry dissolves

I sealed **B-TWO-FIELDS**, expecting `B575`'s basis to genuinely use √−3, in which case memos 161/162
would be computing over ℚ(√−3) while Route A's orbit problem lives over ℚ — a mismatch the chain had
never stated. **Computed:**

> **56862 entries in B575's e₆ basis. Entries with a nonzero √−3 component: 0.**

**The basis is defined over ℚ.** The stabilizer is cut out by a pair with rational entries, so its
structure constants are rational and the whole of memos 161/162 is, in substance, **ℚ-arithmetic
carried inside a ℚ(√−3) class**. There is **no base-field mismatch**, and I said last turn that there
might be one. **That statement was wrong and is withdrawn here**, which is why the prior was sealed:
a prior exists to be able to lose.

**What survives is smaller and is a documentation item, not a mathematical one.** Two different
fields are still written `K` in one chain — `B575`'s class for ℚ(√−3), Route A's cubic
`ℚ[x]/(x³−12x−5)`. `B1002` banked the standing rule for exactly this shape (*any future arc using
the word must say which*), and this chain does not say which. Cheap to fix, and worth fixing before a
specialist reads it.

---

## 5. C — THE LEDGER, REPAIRED

| # | hypothesis (Kneser–Platonov / Route A) | state | closed by |
|---|---|---|---|
| 1 | the group is **simply connected** | **CLOSED** | memo 162 — triality, `8s`/`8c` present |
| 2 | **ℚ-simple** | **CLOSED** | **this memo** — centroid 1 + Killing nondegenerate ⟹ central simple ⟹ absolutely simple |
| 3 | `H(ℝ)` **non-compact** | **CLOSED** | `B904` — split Zorn octonions ⟹ split Spin(8) |
| 4 | the stabilizer **is a form of Spin(8)** | **CLOSED** | algebra D₄ **proved here** (was a necessary-condition test in memo 161); group form by memo 162; applicability to the object's own pair by `B969` + memo 162 T-3 |
| 5 | **orbit count = the stabilizer's class set** | **OPEN — the ask** | the Borel–Serre / Bhargava bijection, needing `G(ℤ)` class number one and a coherent integral model |

**Pair regularity (`B969`) is not deleted — it is re-filed where it belongs**: it is not a hypothesis
of the theorem, it is what licenses applying a *generic* stabilizer result to the **object's own**
pair. That is load-bearing for the identification (hypothesis 4), which is where it now sits.

**Four of five, and now four proved.**

---

## 6. What this does to the send

`THE_GATE_SENDS.md` addendum 4 — the drafted Q7, **not sent** — carries the substituted table
verbatim. Had it gone out, a specialist would have received **a hypothesis list that is not the
theorem's hypothesis list**, with one row absent and a non-hypothesis in its place.

**The repaired draft is strictly stronger**, and that is the point: hypothesis 2 goes from *assumed
on an irrelevant condition* to *proved*, and hypothesis 4's algebra half goes from *consistent with*
to *forced*. Addendum 5 to `THE_GATE_SENDS.md` carries the repaired table. **Still not sent — the
send is the owner's act, per item.**

---

## 7. What it does NOT do — the fences, restated because this is where over-claiming is easy

- **Route A does not cross.** Hypothesis 5 is untouched by every computation here, and it is the one
  the whole count rests on. **`B990`'s declared UNFAVOURABLE prior stands unrepudiated**, with its
  reason intact: homogeneity has won every previous time, and nothing here touches that reason.
- **A Lie algebra is still not a group scheme.** This proves the *algebra* is a ℚ-form of `𝔰𝔬(8)`.
  Memo 162 identified the group form; **the integral group scheme over ℤ**, which a class-set argument
  finally needs, remains named and unclosed.
- **The stabilizer computed is of a *generic* pair.** Its applicability to the object's own pair rests
  on `B969` + memo 162's T-3 inference, which is cited, not re-derived here.
- **Nothing moves for the Standard Model.** No value, no structure, no ledger row. Even a full
  crossing would convert **one** supplied input into a derived one, and it would be **a direction,
  never a value** — `B991`'s normalisation no-go is untouched, and the SM's numbers stay exactly
  where nine proved value-crossing negatives put them.

---

## 8. The lesson, narrower than "check your ledgers"

Both defects are the same shape as the class this bench spent the previous cell failing to build a
detector for: **a summary that claims more than the record under it.** Memo 162's tally said *four of
five hypotheses discharged*; two of those four were a substitution and an unproved conditional. It
was found **by reading**, one memo after two detectors failed to find its kind mechanically — which
is the honest state of the mirror class and is now twice demonstrated on this bench's own work.

And a rule worth keeping: **when a count survives a revision, check that its contents did.** The
number four was stable across memos 160→162 while two of its rows changed underneath it, and a stable
headline number is exactly what stops anyone re-reading the rows.
