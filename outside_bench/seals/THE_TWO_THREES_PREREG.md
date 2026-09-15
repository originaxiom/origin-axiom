# PREREGISTRATION — THE TWO THREES: is the ℤ/3 in B1355's sum rule the object's own 2T/Q₈?

*Outside bench, memo 233. Sealed and committed BEFORE the certificate is written.*

## The occasion

Memo 232 ADDENDUM 1 corrected two errors in this bench's lift-axis map. The replacement question is
not about b₂ — that was the corrected error — but about **which ℤ/3** B1355's sum rule is talking
about.

**B1355 §6**, verbatim:

> *"a ℤ/3 that permutes the apexes and fixes w gives equal charges 3q = 0 and **no inflow** — a
> ℤ/3-symmetric triple needs b₂ ≥ 2 with the ℤ/3 moving the harmonic forms."*

and it attributes that ℤ/3 to *"the tower's ℤ/3 descent (Y₃, B1301/B1303)"*.

**B1269** and `docs/THE_ASSEMBLY_2026-09-06.md` §7 attribute it elsewhere:

> *"The three A₁ families are the three imaginary quaternion units of **Q₈ ⊂ 2T**, permuted by the
> **ℤ/3 = 2T/Q₈** … permuted by the object's own arithmetic."*

**Verified before sealing: B1355 cites B1269 zero times and never contains the string `Q₈`.**

## WHAT IS ALREADY BANKED — STATED FIRST, SO THIS CELL'S NOVELTY IS NOT INFLATED LATER

**Most of the identification is already in the record, and this seal says so before the run.**
`B1273` §2 (PROVED) computes, over ℚ(ω), for all 48 surjections:

> *"On Y₃ its image is the **Klein four-group V₄** (order 4, exponent 2) = **ker(A₄ → ℤ/3)**: the
> holonomy group of the flat manifold."*
> *"the three classes are its three flat directions x, y, z — **permuted by the deck ℤ/3**."*

Since **A₄ = 2T/{±1}** and **V₄ = Q₈/{±1}**, the deck ℤ/3 = A₄/V₄ **is** 2T/Q₈ by elementary means.
**So outcome A below is close to forced by banked content, and the identification is NOT this
cell's contribution.** A cell that reported it as a discovery would be inflating a restatement.

**What is genuinely unstated is the CONSEQUENCE:** B1355 poses its sum-rule question about a ℤ/3 it
treats as a *design choice of the closing* ("whether the tower's ℤ/3 descent **can** place three
apexes"). If that ℤ/3 is the object's own 2T/Q₈, the symmetry is **not a choice** — it is supplied
by the McKay group — and B1355's escape clause stops being a design option and becomes a **forced
necessary condition** on any closing realising destination item 1. **No arc states that.**

## THE QUESTION

Is the ℤ/3 permuting Y₃'s three flat directions (B1273) **the same ℤ/3, acting the same way**, as
the 2T/Q₈ permuting the three imaginary quaternion units of Q₈ ⊂ 2T (B1269)?

## THE TWO OUTCOMES

- **A — they coincide equivariantly.** The ℤ/3 of B1355's sum rule is the object's own arithmetic,
  so the escape clause (`b₂ ≥ 2` **and** the ℤ/3 moving the harmonic forms) is **FORCED** on every
  closing realising item 1, not a design choice. Priced as a **synthesis of banked arcs**, not a
  theorem.
- **B — they do not coincide.** Then B1355 §6 poses its question about a different symmetry from
  the one B1269 and `THE_ASSEMBLY` name, and that discrepancy is the finding.

## WHAT IS COMPUTED

1. 2T as 24 unit quaternions (exact, half-integer coordinates); **Q₈ ⊂ 2T**; that Q₈ ◁ 2T and
   **2T/Q₈ ≅ ℤ/3**.
2. The **conjugation** action of a coset representative on the three imaginary units {±i, ±j, ±k}
   — side A's triple and its ℤ/3.
3. **V₄ = Q₈/{±1}**, **A₄ = 2T/{±1}**, and that **V₄ = ker(A₄ → ℤ/3)** — B1273's own sentence,
   re-derived rather than cited.
4. The three **non-trivial characters** of V₄ (side B's triple, = B1273's χ₁, χ₂, χ₃ = the three
   flat directions) and the induced ℤ/3 action on them.
5. **The intertwining test:** whether the natural map (imaginary units mod ±1) → (non-trivial
   characters of V₄) is ℤ/3-**equivariant**.

## CONTROLS

| # | control | catches |
|---|---|---|
| **Z1** | `the_frontier_gap_all_heads.py` run **first**, terms stated, all heads | #34, three instances |
| **Z2** | B1269's, B1273's and B1355's **FINDINGS** read, never their `arc_verdict` summary clause | #35 |
| **Z3** | the equivariance test must **return both answers**: a deliberately wrong relabelling of the triple (two entries transposed) must **FAIL** it | memo 164 — control passing is not instrument working |
| **Z4** | B1273's **fingerprint reproduced**: from F(2,6) = ⟨x₁…x₆ ∣ x_i x_{i+1} = x_{i+2}⟩, `H₁ = ℤ/4 ⊕ ℤ/4` by Smith form, **64** homomorphisms to Q₈ and **16** to A₄ | a drifted presentation; the 16-of-144 count is load-bearing, not a tautology |

## FENCES, BEFORE THE RUN

- **X is not constructed.** Nothing here is a property *of* a closing — only a condition *on* one.
- **No b₂ of any 7-manifold is computed or inferred.** The record has none, and the Q → X bridge is
  absent from every head (memo 232 ADDENDUM 1).
- **No generation count.** `I-26` is **UNEARNED**; B1355's *"one 27 per point"* is the literature's
  rule, not re-derived here.
- **Outcome A is not progress toward chirality.** It sharpens a requirement on an object nobody has
  built.
- Gate 5 untouched; nothing promotes to `CLAIMS.md`.
