# THE TWO THREES — the ℤ/3 in B1355's charge sum rule is the object's own 2T/Q₈, so its escape clause is a requirement and not a design choice

*Outside bench, memo 233, 2026-09-15. Seal `seals/THE_TWO_THREES_PREREG.md`
(sha256 `46475ca8c813bde69db705491c086f26b4d82748416e09971d659e35dc60f9d8`, committed `d88b0a70`
**before** the certificate was written). Certificate `certificates/the_two_threes.py`, output
`outputs/the_two_threes_out.txt`, **exit 0, nine controls PASS**. Every number below is from that
certificate (#20).*

---

## 0. WHAT THIS IS NOT — stated first, because the seal fixed the pricing before the run

**The identification is not news.** `B1273` §2 (PROVED) already computes, exactly over ℚ(ω) and for
all 48 surjections, that the descended `3_ρ` has image on Y₃ the Klein four-group

> *"**V₄** (order 4, exponent 2) = **ker(A₄ → ℤ/3)**: the holonomy group of the flat manifold"*

with the three classes *"its three flat directions x, y, z — **permuted by the deck ℤ/3**."* Since
**A₄ = 2T/{±1}** and **V₄ = Q₈/{±1}**, everything else is elementary. This cell **re-derives that
exactly rather than citing it, and claims no priority for it.**

**What no arc states is the consequence.** That is §3.

---

## 1. THE OBSERVATION

| side | source | the triple | the ℤ/3 action |
|---|---|---|---|
| **A** | **B1269**, `THE_ASSEMBLY` §7 — *"the three imaginary quaternion units of **Q₈ ⊂ 2T**, permuted by the **ℤ/3 = 2T/Q₈**"* | {±i, ±j, ±k} | conjugation by w = (1+i+j+k)/2: **i → j → k → i** |
| **B** | **B1273** §2 — the three flat directions of Y₃ = the three non-trivial characters of V₄ | χ_i, χ_j, χ_k | the deck ℤ/3: **i → j → k → i** |

**The natural map (imaginary units mod ±1) → (non-trivial characters of V₄) is ℤ/3-EQUIVARIANT.**
→ **OUTCOME A.**

Supporting exact facts from the same certificate: |2T| = 24, |Q₈| = 8, **Q₈ ◁ 2T with index 3**,
w ∉ Q₈, w² ∉ Q₈, w³ = −1 ∈ Q₈, so **2T/Q₈ = ⟨wQ₈⟩ ≅ ℤ/3**; |V₄| = 4 of exponent 2, |A₄| = 12,
**[A₄ : V₄] = 3**.

---

## 2. THE GAP THIS CLOSES IS A CITATION GAP, AND IT IS EXACTLY THE KIND MEMO 232 §0 WARNED ABOUT

**B1355 cites B1269 zero times and never contains the string `Q₈`.** It attributes the permuting
ℤ/3 to *"the tower's ℤ/3 descent (Y₃, B1301/B1303)"* — a different source for the same symmetry —
and asks *"**whether** the tower's ℤ/3 descent **can** place three CP³/2T apexes on the closing's
E₆ locus"*, i.e. it treats the ℤ/3 as something the designer of a closing may or may not arrange.

Both arcs sit on the same head; neither reaches the other. This is B1307's harvest lag (Q12) inside
a single branch.

---

## 3. THE CONSEQUENCE — the escape clause is FORCED

B1355 §6, verbatim:

> *"∑_α ∫_{U_α} wᵢ = 0 for every harmonic two-form of the compact closing, so with b₂ = 1 the three
> 27s carry U(1) charges summing to zero (a 2 + 1 structure, e.g. (1, 1, −2)), and **a ℤ/3 that
> permutes the apexes and fixes w gives equal charges 3q = 0 and no inflow** — a ℤ/3-symmetric
> triple needs **b₂ ≥ 2 with the ℤ/3 moving the harmonic forms**."*

**The ℤ/3 is not a design choice: the object's own McKay group supplies it.** So the clause is not
an option a closing may decline — it is a **necessary condition on every closing realising
destination item 1** (*"three isolated E₇-enhancement points permuted by ℤ/3 = 2T/Q₈"*,
`THE_ASSEMBLY` §7; the destination ledger's item 1 carries **no DONE marker**, unlike its items 2
and 3).

**Why b₂ = 1 cannot meet it** — *added after the seal and labelled as such in the certificate, so it
is not passed off as preregistered.* H²(X;ℝ) = ℝ^{b₂}, and a ℤ/3-action is a homomorphism
ℤ/3 → GL(b₂,ℝ).

| b₂ | computed | consequence |
|---|---|---|
| **1** | the finite elements of GL(1,ℝ) = ℝ^× are {±1}, of orders 1 and 2 — **no element of order 3** | **every ℤ/3 action on ℝ¹ is trivial** ⟹ the three charges are equal ⟹ 3q = 0 ⟹ q = 0 ⟹ **no inflow** |
| **2** | the companion matrix of x² + x + 1 has order 3 (C ≠ I, C² ≠ I, C³ = I, exact over ℤ) | a ℤ/3 **can** move the harmonic forms |

So the obstruction is **specific to b₂ = 1**, not a general fact about ℤ/3 — the same shape as
B1259's own control (SO(6) elements generically avoid eigenvalue +1 while SO(7) never do).

---

## 4. CONTROLS — nine, all PASS

| # | control | what it did |
|---|---|---|
| **Z1** | the all-heads gap instrument, run **before** the seal, terms stated: `2T/Q`, `Q_8`, `Q8`, `imaginary quaternion units`, `Hantzsche`, `didicosm`, `deck`, `intertwin` | **it changed the cell.** It surfaced B1273 §2, which supplies most of the identification — so the seal was written with the pricing already lowered, instead of the memo discovering it afterwards |
| **Z2** | B1269's, B1273's and B1355's **FINDINGS** read, never their `arc_verdict` summary clause | **#35**'s repair, applied rather than recited |
| **Z3** | **the equivariance test returns BOTH answers** — the natural map: `True`; a deliberately wrong relabelling (i ↔ j transposed): `False` | memo 164 — a test that cannot fail is not a test |
| **Z4a** | `H₁(Y₃) = ℤ/4 ⊕ ℤ/4`, b₁ = 0, by exact Smith form on F(2,6)'s 6×6 relation matrix (diagonal **[1,1,1,1,4,4]**) | reproduces B1273 |
| **Z4b** | **64** homomorphisms F(2,6) → Q₈ and **16** → A₄ | reproduces B1273's fingerprint. **The A₄ count is 16 of 144 pairs — load-bearing**, where the Q₈ count is 64 of 64 |
| + 4 | Q₈ ◁ 2T index 3 · 2T/Q₈ ≅ ℤ/3 · side A a 3-cycle · side B a 3-cycle · V₄ = ker(A₄→ℤ/3) Klein · the post-seal b₂ step | |

Exact arithmetic throughout: quaternions as integer 4-tuples in half-units. **No floats anywhere.**

---

## 5. FENCES

- **X is not constructed.** This is a condition **on** a closing, never a property **of** one.
- **No b₂ of any 7-manifold is computed or inferred.** The record contains none — B1353's `b₂ = 0`
  and B1355's `b₂ = 1` are facts about the 6-dimensional **links** of two cones, both asserted from
  standard theory (B1355's script: *"The topological facts used in the FINDINGS … are stated there,
  not computed here"*) — and **the Q → X bridge is absent from every head** (memo 232 ADDENDUM 1).
- **No generation count.** `I-26` is **UNEARNED**; B1355's *"one 27 per point"* is the literature's
  rule, not re-derived.
- **This is not progress toward chirality.** It sharpens a requirement on an object nobody has built.

**Gate 5 untouched. Nothing promotes to `CLAIMS.md`.**
