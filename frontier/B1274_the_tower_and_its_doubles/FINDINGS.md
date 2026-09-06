# B1274 — THE TOWER AND ITS DOUBLES: the object's cyclic closings carry either one irreducible class of the family system or three characters — never three irreducible classes — so the tree-level hierarchy is excluded on the whole object-supplied tower

**Date:** 2026-09-06 · **Seat:** cc · **Status:** PROVED (exact, all 48 surjections, n ≤ 6) + NEGATIVE (L203 closed) · **Price: unchanged**

## The question (L203, `docs/THE_VIEW_FROM_ABOVE_2026-09-06.md` candidate 3)

B1273 found the three generation classes on the object's own 3-fold closing Y₃ and proved that
character-distinguished generations have zero-diagonal textures (refuted by m₁ ≤ m₂ + m₃). A tree-level hierarchy
therefore needs **three classes of one irreducible local system**. Does any closing in the object's own tower —
the cyclic covers M_n, the branched covers Y_n (the Fibonacci manifolds), their mirror doubles D(M_n) — carry them?

## 1. Descent: the closing's index is the object's ((a), all 48)

The family 3 of E₈ ⊃ E₆ × SU(3) is the real 3 of 2T, and 3_ρ(a) has order 3 for every surjection (B1263: meridian
order 3 or 6 in 2T, 3 in A₄). It descends to the branched cover Y_n — the lifted meridian aⁿ filled — **iff 3 | n**:
computed for n = 2…6 (yes for 3, 6; no for 2, 4, 5). The observer's "slope" H5 lists for the branched tower is the
object's own 3: **n = 3 is the minimal closing that carries the object's holonomy at all.**

## 2. The image: abelian iff 3 | n ((b), all 48)

On the cyclic cover M_n (the kernel K_n of a, b ↦ 1 mod n), the image ρ(K_n) is **all of A₄** when 3 ∤ n (the 3 stays
irreducible) and **the Klein four-group V₄** when 3 | n (the 3 splits into three characters). Exact, by generating
the image from the Schreier generators.

## 3. The counts ((c), exact Fox calculus on the Reidemeister–Schreier presentations, all 48)

| closing | h¹(·; 3_ρ) | cusp h⁰ / h¹ | rank(res) | image | mirror double D(M_n): h¹ for every dial |
|---|---|---|---|---|---|
| M₁ = m004 | 1 | 1 / 2 | 1 | A₄ | 1 … 2 |
| M₂ | **1** | 1 / 2 | 1 | A₄ | 1 … 2 |
| M₃ | 3 | 3 / 6 | 3 | V₄ | 3 … 6 |
| M₄ | **1** | 1 / 2 | 1 | A₄ | 1 … 2 |
| M₅ | **1** | 1 / 2 | 1 | A₄ | 1 … 2 |
| M₆ | 3 | 3 / 6 | 3 | V₄ | 3 … 6 |
| Y₃ (closed) | 3 | — | — | V₄ | — |
| Y₆ (closed) | 3 | — | — | V₄ | — |
| Y₂, Y₄, Y₅ | no descent | | | | |

Shapiro control at n = 2: h¹(M₂; 3) = h¹(m004; 3) + h¹(m004; 3 ⊗ sgn) = 1 + **0** — the sign twist carries nothing.
The double bound is Mayer–Vietoris: h⁰(∂) + 2h¹(M) − h¹(∂) ≤ h¹(D(M_n)) ≤ h⁰(∂) + 2h¹(M) − rank(res) (h⁰(M) = 0).

## 4. The dichotomy, and the verdict

**On the whole tower: one class with the irreducible A₄ image (3 ∤ n) or three classes of characters (3 | n) —
three classes ⟺ abelian image ⟺ zero-diagonal.** The class count does not grow along the irreducible branch
(h¹ = 1 for n = 1, 2, 4, 5: the one generation of B1270 is robust under every cyclic cover), and the doubles of that
branch carry at most 2. **No cyclic cover, branched cover or mirror double of the object (n ≤ 6) carries three classes
of the irreducible family system.** With B1273's theorem, the tree-level hierarchy is excluded on the entire
object-supplied cyclic tower. **L203 closed, negative.**

What this leaves for a diagonal-capable carrier: a closing **outside** the cyclic tower — a non-cyclic finite cover
(the A₄- or 2T-cover, where the 3 becomes trivial and the classes are scalar: zero-diagonal again by the ε-selection)
or a genuinely different local system — or a non-tree-level source (L201). The step back's verdict sharpens: **tree
level is closed by theorems on every closing the object supplies.**

## Controls (MB12)

- All 48 surjections, both meridian-order classes, every n ≤ 6, unbranched and branched; the descent test is a
  computed matrix identity, the image a generated group order, the counts exact ranks over ℚ(ω).
- Shapiro's formula at n = 2 is an independent check of the Reidemeister–Schreier machinery (1 + 0 = 1).
- The double bound is dial-independent by construction (both extremes of rank(res ⊕ res′) are reported).

## Verification

`verification/tower_and_doubles.py` (exact; ~1 min; `SELFTEST: PASS`), run record `verification/tower_and_doubles_run.txt`.
Lock: `tests/test_b1274_the_tower_and_its_doubles.py`. Feeds on B1273 (the machinery and the theorem), B1268 (the cusp
lemma), B1270 (h¹(m004; 3) = 1), B1263 (the 48). Registers no identification change.
