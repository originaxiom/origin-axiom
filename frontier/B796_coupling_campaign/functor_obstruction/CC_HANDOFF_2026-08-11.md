# HANDOFF → cc, for 2026-08-11 14:00. Everything from the credit gap, in order.

**cc's pause point:** main `7ea6e720`; B1023/B1024 landed since (`49a1ca7a`,
`3524b889`); B1023 v2 suite was running. **Nothing below is merged — cc3 does
not merge.**

---

## 1. L153 — the cell is nearly decided pre-compute, and the verdict form changed

**A three-seat amendment (chat-2, v2) is ready to drop into `B1024`'s prereg.**
It adds criteria only; the sealed outcome labels, prior and computation are
untouched, and it carries its own reject-if-it-alters-the-cell clause.

**C-i** — surjectivity is not identity: record the **elementwise map**, test
**equivariance** (B916's banked rule), else bank **PARTIAL-UNPINNED**. The target
is **canonically labelled** — the two τ-fixed nodes are the **trivalent node**
and the **branch tip** (Bourbaki α₄, α₂), distinguishable by valence, so no
diagram automorphism exchanges them and the assignment is a *testable claim*.

**C-ii** — the null goes in the seal. **k = 2 governs** (the cell maps two
shadows; golden branch spent on A7): **37.5 %, 1.42 bits**. The verdict *states
k* and cites the matching row. Both failure modes guarded: a bare SAME
overstates, an inflated null under-states.

**C-iii** — report the **joint rank**, not a binary. Overlap → 2, **partial → 3**,
independent → 4. The middle row is unexcluded.

### The mathematics, verified on two independent builds

**The ambient (chat1's, reproduced exactly by cc3 from the E₆ Cartan matrix,
the 27 as the Weyl orbit of ω₁, `T[2] = Q^∨/2Q^∨`):**

| flip count | # of T[2] elements |
|---|---|
| 0 | 1 |
| **12** | **36** = E₆'s positive roots |
| 16 | 27 = dim of the fundamental |

**H¹ lookup, confirmed:** among τ-fixed elements, **flip 12 ⟺ NONZERO class**;
flips 0 or 16 ⟺ trivial. **This converts the cell's core from a cohomology
computation to a two-comparison lookup.**

### What the c-side now reduces to — two checks

1. **Is `D_c ∈ T[2]`?** Not merely 27-visible. **B939's ELEVEN proves this cannot
   be assumed:** `σ_χ− → D2` has **11 flips**, and **11 ∉ {0,12,16}**, so **D2 is
   not a torus element** — B939 says why itself (*"the second wall
   CONJUGATION"*, *"τ-TWISTED dual intertwiner"*, `D2 = ±ρ₂₇(σ_χ−)`).
   **B939 is not in error; the eleven is a banked worked counterexample showing
   the shadow map's image escapes T[2].**
2. **If yes, is it τ-fixed?** `h₁ = h₆`, `h₃ = h₅`. Then the lookup finishes it.

**Still owed:** reversal's shadow, which the prereg already flags as
*"must be constructed if not banked."*

---

## 2. L154 — cc3's prediction, registered before compute, and corrected once

**Prize identified (B1015): A2 = c = 6σ**, the one continuous dimensionless
external coupling.

> **cc3 predicts A2 DISCHARGES** — `c((E₆)₁) = 78/13 = 6`, independently
> `B254: 16/5 + 14/5 = 6`. **A1 (ℓ) does NOT** — σ is dimensionless and supplies
> no length; `c_BH = c_{(E₆)₁}` fixes `ℓ/G₃ = 4`, never `ℓ`.
> **Confidence: weak lean SAME**, lowered from moderate after chat-2's base rate
> (the corpus has one-symbol-two-objects form — two conductors, two levels, L110).
> **Brown–Henneaux's `c = 3ℓ/2G` and level-1 E₆ WZW `c = 6` are a priori
> different objects; their identification is what L154 must ESTABLISH.**

**cc3 has an interest in the A1 half (it protects C3), so cc or chat1 runs the
cell, not cc3.**

---

## 3. cc3's Phase-1 findings (published `df2ec617`, sealed `6d227bae`)

**C1** two functors; Gate 5 is a **policy** and L91's (4) is **discharged** —
cc conceded and found more (Gate 5's own clause cites a satisfied obligation).
**C3** dimensionful: obstructed **up to one unit** — a one-parameter family, not
zero output. **C4** the R11 licensing gap — cc conceded and supplied the T1/T2
pin. **C5 REFUTED by cc** (structure is a third category); cc3 sharpened the fix
to *"no unanchored functor to **SM** values"*, since B1011's values are
unanchored dimensionless values.

---

## 4. From chat-2's handoff

- **M11 is a registered falsifier for cc3's C3.** C3 predicts M11 **splits**:
  `ln 2` per bit available and worthless; `k_B T ln 2` **forbidden** without the
  dimensionful anchor. **Refutes C3: an absolute energy per closing at zero
  anchors.** chat-2 runs it; **not cc3.**
- **M8 supplied L153's method** — but chat-2 insists, correctly, that **M8's
  bridge claim has NOT landed**; *"is B701's obstruction literally a
  contextuality obstruction, and in which sheaf?"* remains untested. **Do not
  merge those in the ledger.**
- **Fold the graph extractor into `scripts/atlas/`** — chat-2's own
  recommendation, citing B1007 against itself.
- **Retraction-audit flag:** **B854 NEGATIVE with 20 dependents; B915 NEGATIVE
  with 10.**
- **Northshield is NOT verification** — he did not check B′ and said he had been
  out of the field a long time. That caveat must survive into anything banked.

---

## 5. PROPOSED for `docs/PRACTICES.md` — not present, checked

Two matching rules, one per side of a relay. **Both were earned four times today.**

> **Sending side.** *When handing another seat a number or a label, state the
> convention it lives in, or express it convention-free.*
>
> **Receiving side.** *`verify-don't-trust` binds to the **premise**, not only
> the arithmetic. A correction from another seat is an input to be checked, not
> an authority to be adopted — **deference is not verification**, and re-deriving
> the numbers inside an unchecked premise is the most convincing way to be wrong.*
>
> **Document-leverage corollary.** *Where a banked artifact does not fix a
> notation, a downstream document uses a convention-free description and asserts
> no numbering — it would not inherit a convention but **establish** one.*

---

## 6. cc3's own error record for the gap — four, all the same shape

| | error | shape |
|---|---|---|
| L154 | predicted against **A1** when the prize was **A2** | right argument, wrong object |
| L153 | *"k = 3, B782's actual rank"* — the cell maps **two** | right computation, wrong question |
| L153 | node labels **{1,3}** — cc3's own 0-indexing, Bourbaki is **{2,4}** | right nodes, wrong names |
| L153 | refuted chat1's type-exclusion via *"27-visible ⟹ operand-type"* | **27-visible ≠ in T[2]** — B939's ELEVEN is the counterexample |

**Three of the four were injected into another seat's work. All four were caught
by another seat, none by cc3.** The arithmetic was never wrong.
