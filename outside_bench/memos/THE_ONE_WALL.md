# MEMO 170 — EVERY WALL IS AMPHICHIRALITY, AND THE ESCAPE IS A MOVE NOBODY HAS MADE

**Banked 2026-09-07 · outside bench (lane 1B).** Certificate
`certificates/partial_filling_joint.py`; output vendored. Gate 5 untouched: pure topology.
Written on the owner's *"sit and meditate… what other joints, unifications do you see?"*

---

## 1. THE UNIFICATION — one theorem generates every wall, and the corpus tracks them as three

**`B1227`'s theorem, elementary:** for M amphichiral the mirror μ is a **self**-isometry, so any
isometry invariant `I` valued in an abelian group `A` with `I(μM) = −I(M)` satisfies
**`2·I(M) = 0` in `A`.**

`B1227` records **two** regimes. There is a **third**, and it is the wall the programme is currently
stuck on:

| value group `A` | what dies | where it is recorded |
|---|---|---|
| `ℝ/(½)ℤ` — has 2-torsion | `CS ∈ {0, ¼}`; for m004 **`CS = 0`** ⟹ `∂S/∂k ≡ 0` ⟹ **the quantized sector is deleted** ⟹ **σ cannot be fixed** | `B1227` regime 1 → `B1012` → `B1064` |
| `ℝ` — torsion-free | `I = 0` exactly ⟹ **no real selector can exist** | `B1227` regime 2 → `B1225` |
| **`ℤ` — torsion-free** | **net chirality = 0 ⟹ every closing is vector-like, mirror-paired** | **`B1294`** |

**`B1294` derived the third regime independently a week later and does not cite `B1227` once**
(verified: `grep -c B1227` on its FINDINGS returns **0**).

> **⇒ The σ wall, the selector wall and the chirality wall are ONE THEOREM in three value groups.
> The programme's single defect is that its object is TOO SYMMETRIC.**

This is a **consolidation, not a discovery** — `B1227` says the same of itself, and a topologist
would call the argument immediate. What was missing is the **join**, and the join is worth more than
either half: it says there is no point attacking these three walls separately.

---

## 2. THE ESCAPE IS ALSO ONE ESCAPE — and two seats found it independently without meeting

- **`B1291`** (chirality): *"3 is excluded on a ONE-CUSPED manifold, and **the escape is ≥2 cusps**."*
- **`B1190`/GC-6** (σ): the bridge needs *"**six cusp-boson units** where `T[4₁]` supplies one"*,
  the **one** attributed to the object having **one cusp**.

**Both walls want more cusps. Neither arc cites the other.**

**But covers cannot supply it, and that is now settled from two directions:**

- **memo 169** (this bench, 2026-08-31): 38 covers to degree 8 — **no six-cusped cover**, cusp count
  caps at **3**, and **every cover has `CS ≡ 0`**, since `CS(M̃) = d·CS(M)`.
- **`B1295`** (main, 2026-09-07) extended exactly this to degree 10 **independently**: 87 covers,
  201 cusps, 968 isometries, `|det(A − I)| ∈ {0, 4}` — **never 1, 2 or 3**, so no cusp rotation of
  order 3, 4 or 6 anywhere in the tower.

**Amphichirality is INHERITED by covers.** Going upstairs multiplies cusps a little and changes
nothing about the wall.

---

## 3. THE JOINT NOBODY HAS MADE — and it computes

Two banked facts that have never appeared in the same sentence:

- **`B432`** (long banked): *"All 31 sampled hyperbolic Dehn fillings make the amphichiral object
  **chiral**."* ⟹ **filling BREAKS amphichirality.** But filling **kills the cusp**.
- **Covers** keep and multiply cusps but **inherit `CS = 0`**.

**Neither move alone gives both. The composite does.**

> ### Partially fill a multi-cusped cover: fill some cusps, leave others.

**Searched across all of `origin/main` (frontier + docs): `"partial filling"` 0 · `"partially fill"`
0 · `"partial Dehn"` 0 · `"multi-cusped cover"` 0.** And no arc citing `B1064` also cites `B432`.

**Computed here (SnapPy, covers of m004 to degree 8, one cusp filled):**

> **18 of 22 partial fillings keep ≥ 1 cusp AND have `CS ≠ 0`.**

| cover | cusps | fill | cusps left | CS |
|---|---|---|---|---|
| degree 5 | 3 | (2,1) | **2** | **+0.157590041** |
| degree 6 | 2 | (2,1) | 1 | +0.194458446 |
| degree 6 | 2 | (1,1) | 1 | +0.231670002 |
| degree 7 | 3 | (1,0) | **2** | **±0.041666667 = ±1/24** |

**⇒ The two things the σ bridge needs — a surviving cusp AND a quantized (`CS ≠ 0`) sector — are
simultaneously satisfiable.** `B1064` typed its route **(a)** as *"restore a quantized boundary
sector the object's amphichirality does not delete"* and said **none is known**. This is a candidate,
and it is the first one.

---

## 4. THE COST, WHICH IS SEVERE AND MUST BE PRICED BEFORE ANYONE GETS EXCITED

**These are no longer m004.** A partially-filled cover requires **three new discrete choices** —
*which cover, which cusp, which slope* — and the programme's entire claim is that its object is
**derived, not chosen**. `B432` already flags this in its own words: *"slope selection stays free
input."*

> **So this route BUYS a quantized sector by SPENDING freedom-ledger entries. It may cost more than σ
> is worth.** Deleting one continuous anchor while adding three discrete choices is not obviously a
> win, and the corpus has never priced the trade because it has never had both halves on one table.

**That pricing is the cell this memo recommends, and it is cheap** — the ledger machinery exists.

---

## 5. BENCH ERROR #20 — caught in this cell's own first run

My Test 1 printed **`[amphichirality BROKEN]`** as an unconditional f-string label while reporting
`0 of 10`. Both were meaningless: SnapPy raises **`"The Chern-Simons invariant isn't currently
known"`** for *every* closed filling, so **CS was never computed there at all**. The label asserted
the conclusion the test was supposed to test. Fixed in the committed certificate, which now says the
test is **inconclusive as run**. **`B432`'s chirality result stands on its own instrument, not on
mine.** *Same class as bench error #16 — a cell wearing the shape of a test.*

---

## 6. TWO SMALLER JOINTS, AND ONE THAT MUST NOT BE MADE

**(a) The hexagonal cusp is dead at the base and ALIVE AT DEGREE 10.** `B486` killed the
Eisenstein-cusp route for m004 itself — the cusp is `ℤ + 2√−3·ℤ`, **rectangular**, CM disc **−48**.
But `B1295` reports **16 of 201 cusps ARE hexagonal, in 14 degree-10 covers**. `B1295` notes no
isometry rotates them — which is a statement about the covers' **symmetry groups**, not about what a
hexagonal cusp **supplies to a boundary theory**. **`(E₆)₁` is six free bosons on the E₆ lattice, and
E₆ is a rank-3 `ℤ[ω]`-lattice; a hexagonal cusp is a `ℤ[ω]`-torus.** The substrate my own dead idea
needed **exists two degrees above where I stopped looking.**

**(b) `ν^c` is doing two jobs.** `B1096`: over the derived 16, **`ν^c` is exactly what cancels the
last non-vanishing anomaly invariant**. `B1276`: the forced cubic relations include **`H_u L ν^c`**.
The field the object *derives* rather than imports is simultaneously the anomaly-canceller and a
Yukawa partner. Two seats, two arcs, no cross-reference.

**(c) THE ONE THAT MUST NOT BE MADE.** There are now **three Klein four-groups** in this object:
`B730`'s forced faces `{ℚ(√−3), ℚ(√5), ℚ(√−15)}`; `B1182`'s frame `V₄ = ⟨c, r⟩`; and
`Gal(ℚ(ζ₁₂)/ℚ)`. **`B1182` proved the last two are ONE.** It is tempting to fuse the first as well.
**Do not:** `ℚ(ζ₁₂)`'s quadratic subfields are `√−3, √3, √−1` — they share only `√−3` with `B730`'s
triple. **The two Klein fours are genuinely different**, and fusing them would be exactly the failure
`B1231` names as this programme's dominant error mode: *matching labels in different places and
joining them without a map.*

---

## 7. FENCES

- **Nothing here crosses anything.** §1 is a consolidation of a banked theorem; §3 is an existence
  computation about manifolds, and says **nothing** about whether any `T[M]` has `c = 6`, whether
  `(E₆)₁` attaches, or whether σ is 1.
- **§3's objects are not the object.** Every statement about them is a statement about a *chosen*
  manifold, and §4 is not optional reading.
- `B1064`'s O3 **stands**; this names a candidate for its route (a), it does not discharge it.
- `B486`'s and `B990`'s kills stand. §6(a) is a **substrate** observation, not a revival of the
  refuted argument.
- **Bench error #20 is filed above rather than quietly fixed.**
