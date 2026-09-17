# xB013 ADDENDUM 1 (2026-09-17) — the owner's re-test: the PAIR does not hold, the bit-count is a census artefact, and the two faces supply NO finite selection

**Beyond the seal.** `PREREGISTRATION.md` untouched (`fd3568c3…`). Cells `Y1`–`Y3`,
`verification/verify_the_pair.py`, run at the owner's instruction:

> *"verify first, verify negatives within, verify if the two element set isn't sufficient at the
> end and whether it still needs the whole family at some point."*

**It is not sufficient. Two defects, both this seat's, and both found by asking that question.**

## Y1 — the two faces were defined ASYMMETRICALLY

xB013 defined **Eisenstein as a FIELD** (invariant trace field `ℚ(√−3)`) but **golden as a SINGLE
TRACE** (`|t| = 3`). Field against trace is not a fair pairing, and the asymmetry is what produced
the pair.

| n | tr (LR)ⁿ | t²−4 | √(t²−4) | field | \|t\|=3? |
|---|---|---|---|---|---|
| 1 | 3 | 5 | √5 | ℚ(√5) | yes |
| 2 | 7 | 45 | 3√5 | **ℚ(√5)** | no |
| 3 | 18 | 320 | 8√5 | **ℚ(√5)** | no |
| 4 | 47 | 2205 | 21√5 | **ℚ(√5)** | no |

And it is a theorem, not a table: **`L₂ₙ² − 4 = 5F₂ₙ²`** (verified n = 1…10), so `√(t²−4) = F√5`
for **every** member.

> **Under field-vs-field, the WHOLE tower is golden.** xB013's *"2 of 21"* is an artefact of the
> narrow definition.

**And this reverses a "correction" I made.** xB013's *first* draft of X5 said *"the intersection is
a TOWER"*; I overrode it to a pair. **The first draft was right on this point and my correction was
wrong.**

## Y2 — both sets are INFINITE, so the bit-count is void

Every `(LR)ⁿ` is a cyclic cover of m004 — hence commensurable, hence in the class — and golden by
Y1. Verified `n = 1…6`, volumes exactly `24n·v₀`: m004, m206, s961, t12839, `o10_150696`,
`otet12_00013`.

> **The intersection contains an infinite tower.**

And the finite ratio is **cut-off dependent**, measured:

| cutoff | class | golden (field) | ratio |
|---|---|---|---|
| ≤ 5 tetrahedra | 9 | 4 | 2.25 |
| ≤ 6 | 21 | 6 | 3.50 |
| ≤ 7 | 25 | 6 | 4.17 |

**It does not converge — it grows.** xB013's *"21 → 2, 3.39 bits"* measures the **census window**,
not the mathematics. **WITHDRAWN.**

## Y3 — so what actually selects, and the owner's questions answered

```
class ........................ INFINITE
  --[ both faces ]---------->  golden tower (LR)ⁿ ... INFINITE
  --[ A6 minimality ]------->  pair {m003, m004}
  --[ A5 torsion-free ]----->  m004
```

> **The two faces supply structure but NO finite selection.** They carry an infinite class to an
> infinite tower. **Every finite step is an axiom** — A6 reaches the pair, A5 reaches the member.

**"Is the two-element set sufficient at the end?"** **No** — and it is not even what the faces give.
The pair is the faces **plus minimality**.

**"Does it still need the whole family at some point?"** **Yes, and precisely:** the intersection of
the two faces **IS an infinite family** — the cyclic tower over m004 along its own fibration. The
family is not a fallback for a failed selection; **it is what the faces actually determine.**

## What survives, and what is withdrawn

**Survives:** κ (X1) really is the product of both faces, re-derived exactly. And the intersection
is **not** the whole class — the faces do carve out a **distinguished infinite sub-family**, the
golden tower, and that is real structure.

**Withdrawn:** that the product of the faces **selects**; the **3.39-bit** figure; and the claim
that the minimal both-faces object is a **pair** (it is the pair only after A6).

**This strengthens the owner's original thesis rather than weakening it.** *"Maybe we don't need to
select m004 — maybe reality isn't derivable from m004 alone"*: the two faces, taken seriously and
symmetrically, **determine a family and never a member.** The selection to one manifold was always
the axioms' work, not the mathematics'.

**Provenance.** `verification/verify_the_pair.py` (Y1–Y3) → `reproduce.sh`. Cross-refs xB007 (the
class, the `−I` bit), xB012 (the faces on opposite sides of A5), B425 (the two torsions), B309/B518
(κ).
