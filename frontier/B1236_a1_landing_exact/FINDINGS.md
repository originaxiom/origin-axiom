# B1236 — THE A₁ LANDING AT EXACT MULTIPLET GRADE (codex R035, verified and re-implemented here)

**Date:** 2026-09-02 · **Seat:** cc (main) · **Source:** codex memo R035 (`certificates/r035_a1_su6_sm_branching/` on the codex seat branch, source commit 864c6b75, seven pinned blobs all present on main) · **Verdict:** PROVED (compatibility theorem) · **Gate 5:** untouched — no measured value anywhere.

## THE PRIZE (importance axis, stated first)

B1098 opened the non-abelian hatch and found **two** SM-compatible strata among the twenty sl₂ classes of e₆: the A₂ (trinification, rank exactly 4 — the selected landing) and the **minimal A₁** (centralizer su(6), rank 5, "one extra u(1)"). B1100 gave the A₂ landing its matter content, but only at **collapse/float grade** — the exact value-match is still a named residual there.

**The A₁ landing now lands at EXACT multiplet grade.** Reading the unbroken algebra as the A₁'s centralizer su(6), embedding su(3)⊕su(2)⊕u(1) by 6 = (3,1)_{−1/3} + (1,2)_{1/2} + (1,1)_0, the 27 = (Λ²6, 1) + (6̄, 2_E) restricts to

  (3,2)_{1/6} + (3̄,1)_{−2/3} + 2(3̄,1)_{1/3} + (3,1)_{−1/3} + 2(1,2)_{−1/2} + (1,2)_{1/2} + (1,1)_1 + 2(1,1)_0

— the standard SM-shaped E₆ 27 (one generation + D, D^c, H_u, H_d, S), **as a multiset of irreps, exactly, in exact arithmetic**. And the hypercharge direction is **unique**: the (6̄,2_E) term forces −a, −b, −c into the target's (3̄,1) / (1,2) / (1,1) charge sets; tracelessness leaves two triples; exactly one reproduces the target.

Under THE LENS this is a specification, read the right way round: **the first stratum where the full SM-shaped content is reproduced at multiplet grade is the A₁, at the price of one extra u(1) and the A₁'s selection** (B1098 priced the A₂ at ~4.3 bits; the A₁ has no selection mechanism claimed either). The ingredient is present; what is missing is the selection and the extra-u(1) breaking — both named, neither claimed.

## Evidence grade (second)

Textbook-standard Lie theory (Slansky; B280 banked the 27 = (15,1)+(6̄,2) branching in 2026-06). **No object-specific content** enters the branching — the object enters only through B1098's claim that its composed holonomies land on sl₂ classes of e₆ and that the A₁ is one of them. The target is the standard SM-shaped 27 — labels, not numbers — with the same status as B1100's "banked 6Y multiset". Codex's own fences are correct and are adopted verbatim: *compatibility, not prediction; does not select the A₁ stratum; the extra u(1) is not broken; matter/spin/chirality/generations/dynamics/values remain open.*

## The six cells (`verification/a1_su6_branching.py`, exact fractions, no floats)

1. **The hit.** Y₆ = diag(−1/3,−1/3,−1/3, 1/2,1/2, 0) → the 27 branches to the target exactly (dimension 27, every multiplicity).
2. **Uniqueness within support.** Two traceless triples survive the (6̄,2_E) support constraint — (−1/3, 1/2, 0) and (2/3, −1/2, −1) — and only the first gives the full target (the second produces a (3̄,1)_{4/3}).
3. **Control — histogram ≠ multiplets.** (−1/6, 1/2, −1/2) reproduces the target's *charge histogram* (6,6,4,3,3,2,2,1) and fails at multiplet level. This is why the present cell is strictly stronger than B1100's collapse-form test, which is histogram-level.
4. **Control — the external reading.** Calling 2_E itself the weak SU(2) (the su(6)⊕su(2)_L embedding, 6 = 3̄ + 1 + 1 + 1) **also** reproduces the target abstractly. It is excluded by **type**, not by content: the A₁ is the holonomy's own sl₂ and the unbroken algebra is its *centralizer*; a non-abelian factor is not in its own centralizer. So under the centralizer reading the object's A₁ can only ever be the SU(2)_R-like factor of SU(6)×SU(2), never SU(2)_L — a typing fact worth holding onto.
5. **Control — the diagonal rescue fails.** Taking weak = diag(su(2)_W, 2_E) turns the internal branch's (2_W, 2_E) piece into 1+3: a weak triplet the target does not contain.
6. **The extra u(1), exhibited.** The commutant of su(3)⊕su(2) in su(6) is the traceless block-scalars (x,x,x,y,y,z) — rank 2. Y₆ is one direction; X = (1/3, 0, −1) is an independent second. B1098's "one extra u(1)" now has its direction written down.

## What this changes and does not

**Changes.** B1098's A₁ row is upgraded from "SM-compatible (embedding note)" to "SM-shaped 27 reproduced exactly at multiplet grade, Y unique within support" (addendum). B1100's residual (exact value-match at A₂) acquires a comparison: the A₁ has no such residual. The cascade point N=2 of B306 (SU(6)×SU(2)) and B1098's minimal A₁ are the same maximal subgroup; B311 found the N=2 point **reducible** on the character variety — that fact is untouched here and remains the reason the A₁ is a *stratum*, not the landing.

**Does not change.** Chirality (the wall stands — one 27 is one generation plus vector-like exotics, B280/B298), generations, the A₁ selection, the extra-u(1) breaking, any value. Nothing to CLAIMS.

## Identifications (B1231 rule)

**None declared.** The cell exhibits an embedding and shows the 27 branches to a target; it does not assert that the centralizer's su(3)⊕su(2)⊕u(1)_Y *is* the physical gauge algebra. The day a seat writes that sentence it is a new register row (UNEARNED until the selection and the extra u(1) are priced). I-10 (the A₁ lift ≡ Lorentz spin, UNEARNED from R034) is **not used** here — the memo's "spin map unearned" fence is exactly this.

## Verification

`bash verification/reproduce.sh` (< 1 s). Lock: `tests/test_b1236_a1_landing_exact.py` (runs the script, asserts the six cell lines and the VERDICT). Codex's certificate was **not copied**: this is an independent implementation (different bookkeeping — irreps keyed (colour, weak, Y) directly, the support sets derived from the target rather than listed), agreeing on every line of codex's recorded output.
