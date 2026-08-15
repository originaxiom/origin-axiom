# B1019 — L149 ANSWERED: the endpoint discriminates at the word's own conductor — the siblings have NO DOOR

**Date:** 2026-08-10 · **Seat:** cc · **Sealed:** `ce6b0329` (prior: none confident; a weak
DIVERGES lean, stated as a lean). Gate 5-Q; zero anchors; structure only.

**Verdict: PROVED — outcome DIVERGES, at the entry map itself, for both sealed controls.**

---

## C1 — the entry map, computed exactly (`b1019_cells.py`)

The own-conductor shadow ⟨Rᵐ, Lᵐ⟩ ≤ SL(2, ℤ/(m²+4)), enumerated exactly:

| m | conductor | order | involutions | −I ∈ G | verdict on SU(2)-embeddability |
|---|---|---|---|---|---|
| **1** (golden, control) | 5 | **120** | **1** | yes | **YES — SL(2,5) ≅ 2I** (banked, reproduced) |
| **2** (silver) | 8 | **32** | **7** | no | **NO** — every noncyclic finite SU(2) subgroup has a *unique* involution |
| **3** (bronze) | 13 | **2184** | 1 | yes | **NO** — the full SL(2,13), order 2184. ⚠ **GLOSS CORRECTED 2026-08-15:** this row previously read *"nonabelian SU(2) subgroups cap at 120"*, which is **FALSE** — the binary dihedral groups `Q₄ₙ` have order `4n` and are **unbounded**. The exclusion is **structural, not by order**: the finite subgroups of `SU(2)` are `Cₙ`, `Q₄ₙ`, `2T`, `2O`, `2I`; `PSL(2,13)` is simple, so `SL(2,13)` is **non-solvable** and therefore neither cyclic nor binary dihedral, and `2184 ∉ {24,48,120}`. The arc's CODE enforces the complete ADE conditions correctly; only this prose was loose. Caught in Wave 2, when all three architects independently proposed promoting this arc into the paper's negative control. |

> **Neither sibling's own-door shadow embeds in SU(2). No McKay partner exists. No Lie entry
> exists. The cascade does not land somewhere else for the silver and bronze — it has nowhere to
> BEGIN.** C2 (the chirality gate) and C3 (the walk) are moot: there is no door to walk through.

**Two design-level refutations, recorded in the propose-and-refute discipline:**
1. The seal's own D-series speculation ("a quaternion-type shadow would give a D-diagram") is
   **refuted by the computation**: Q₃₂ has exactly one involution; the silver's shadow has seven.
2. **A first draft of the embeddability criterion used the unique-involution condition alone —
   NECESSARY READ AS SUFFICIENT** (the exact slip the abelianization-proxy rule names). The bronze
   result exposed it (SL(2,13): unique involution, order 2184, embeds in nothing); the criterion
   now enforces the complete ADE conditions, and the slip is kept in the source as a comment.

## C4 — the generic door, for the refinement statement

Through the **generic mod-3 door** the silver reaches the full 2T just as the golden does (B996,
banked) — genericity at that door is exactly why B996 removed the endpoint's confirming power
*there*. **The discrimination lives at the word's OWN door, and only there.**

## C5 — the sealed verdict, and the replacement sentence

**DIVERGES.** Per the sealed grammar, B1009's withdrawn sentence is replaced by:

> **Matching the SM confirms the axioms exactly insofar as the entry is the word's own.** At the
> own-conductor door the golden is not merely unique in *reaching* a McKay group (B997) — it is
> **the only metallic grammar in the tested family with any door at all**: the silver's shadow
> fails SU(2)-embeddability by involution count, the bronze's by order. The endpoint's confirming
> power, removed at the generic door by B996, is **restored at the own door** — where it composes
> with B997's uniqueness proof into a single statement: *one grammar, one door, one cascade, one
> endpoint.*

## Scope, exactly

Computed for m = 2, 3 (the sealed controls) — the all-m statement remains B997's theorem plus this
pair; the family beyond m = 3 is not claimed. "No Lie entry" is relative to **the McKay route the
chain actually uses** (C6: 2T → E₆); a non-McKay entry construction is not excluded by this cell —
that would be a new chain, needing its own C1–C6. No SM value anywhere; the walk (B861) was never
invoked since no entry passed C1.

---

**Verdict: PROVED — DIVERGES. The confirming power of the endpoint is restored at the one door
that exists, and the door belongs to the golden.**
