# B1038 — the tower cluster restored: **two Sym bands, and the fit is unique at n = 4**

**Date:** 2026-08-11 · **Lane:** the campaign's **step 5** — *"restorations bank as arcs; re-verify
the identities before restoring, **never restore from memory**."* Gate 5 untouched; zero anchors;
nothing to `CLAIMS.md`.
**Files:** `verify.py` → `results.json` (13 checks, **all symbolic**) · lock
`tests/test_b1038_tower.py` (8).

**The first of B1037's seven restorations, and the largest: six debt rows, one statement.**

---

## 1. THE LAW, RESTORED

> As a GL(2)-module, **`ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`** for the **external monodromy
> fundamental `W = V ⊕ 1`** — two contiguous `Sym` bands whose staircase multiplicities are
> B103's `μ_d` — and the shape is forced by a **dimension surplus with exactly one rank-zero**:
>
> `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2`, **zero iff n = 4.**
>
> **The grading is EXTERNAL, not principal:** `det Sym^d(M) = (det M)^{d(d+1)/2}`, so a `det = −1`
> monodromy gives an **alternating** parity across the blocks, which no all-even-weight Kostant
> grading can match — **inequivalent for every n ≥ 3**. The same parity is B118's fixed-root sign,
> **a function of `d` alone, independent of `n`**.

## 2. WHAT WAS RE-COMPUTED HERE, AND WHY EACH PIECE MATTERS

| re-verified | how |
|---|---|
| the surplus identity **and its unique rank-zero** | symbolically in `n`; roots `{−1, 4}`, and `−1` is not a rank |
| **`Sym^a(V⊕1) = ⊕_{k≤a} Sym^k(V)`**, `a = 0..8` | **the hinge.** B122 flags that a first pass called the module-iso *"automatic"* — true only over the cyclic `⟨M⟩`. Over **GL(2)**, one element's character does **not** imply module-iso; this **functorial** decomposition is what closes the gap |
| the two bands assembling to **exactly `n²−1`** | symbolically in `n`, and pointwise `n = 3..14` |
| the staircase `μ_d = [d≤n] + [d≤n−3] − [d=0] − [d=1]` | `n = 3..9` |
| `det Sym^d(M) = (det M)^{d(d+1)/2}` | against **explicit matrices**, four of them, `d = 1..4` — not asserted from the standard formula |
| **a control on the instrument itself** | two independent routes to the `Sym` character — direct enumeration vs the generating function `∏(1−vt)^{-1}` — agree. *A bug in one would otherwise produce a passing identity.* |

## 3. WHAT IS CARRIED BY CITATION — named, not implied

- **B103's tower construction is not rebuilt.** This arc re-verifies the **assembly** —
  functoriality, dimensions, staircase, parity. That `ρ_n` *is* that module is B122's result,
  **verified there at character level `n = 2..11` and proved at module level `n = 3,4`.** That
  scope travels with the restored row verbatim.
- **B118's Bourbaki fixed-root computation is not re-run.** It is re-verified only in its
  det-parity form — the part that is self-contained here.

*Saying which step is carried rather than recomputed is the difference between a restoration and a
re-assertion.* B1027 registered exactly such a gap as a lead (L155) rather than papering it.

## 4. WHAT THIS RETIRES

**Six rows of `DEBT_LEDGER` §B100–B199 become one curated law:** B117 (the surplus and the
two-sequence) · B122 (the module identity) · B121 (external ≠ principal) · B118 (the fixed-root
sign) — with **B111 and B113 already superseded by B117 in the band's own words**.

> **This is the cluster finding in action.** B1037 measured 37 rows as 17 statements; this is the
> first of them, and it discharges six rows at once. Counting rows would have called this six
> units of work.

---

**Verdict: PROVED.** 13 checks, all symbolic, plus an instrument control.

**Open, and it is B122's own word for it:** the **module-level proof for general `n`** — B122 calls
it *"the prize."* Character level holds to `n = 11`; module level is proved only at `n = 3,4`. The
restored row says so.
