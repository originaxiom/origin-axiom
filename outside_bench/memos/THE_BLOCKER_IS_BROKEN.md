# MEMO 190 — **MEMO 183 ADDENDUM 4's BLOCKER IS BROKEN**: `f₆, f₇, f₈, …` for `m(5₂)`, by Park's inverted Habiro route, with every step checked against something this bench already owned

**Date** 2026-09-09 · **Lane** outside bench · **Branch** `claude/outside-bench`
**Certificate** `certificates/f52_beyond_f5.py` · **Output** `outputs/f52_beyond_f5_out.txt`
**Data** `data/f52_blocks_beyond.json` · **Gate 5** exact `Fraction` arithmetic. No measured value.

---

## 1. What was blocked

The reduced quantum trace gives `f_0…f_5` for `m(5₂)` and no more. **Memo 183 addendum 4** proved
the sequential single-index fit past `f_5` *cannot close* — `δ_d` determines only
`U_d(0) = Σ_i c_{i,d}Q^i`, not the five `c_{i,d}` separately, so every wrong split is absorbed
into the next correction. **Memo 185** then closed the *naive* cyclotomic route by computation and
named exactly one survivor: Park's **inverted** Habiro series (arXiv:2106.03942), which the bench
did not hold. **It arrived today.**

## 2. The route — and the credit is Park's

**Conjecture 2.**
`F_K(x,q) = −(x^{1/2} − x^{−1/2}) Σ_{m≥1} a_{−m}(K) / ∏_{j=0}^{m−1}(x + x^{−1} − q^j − q^{−j})`,
expanded as a power series in `x`, where `a_m` are Habiro's coefficients **in the
`∏(x + x^{−1} − q^j − q^{−j})` basis** — *the basis memo 185 §8's convention note singled out* —
and `a_{−m}` is their extension to negative index, fixed by the quantum C-polynomial

```
Ĉ_{5₂}(Ê,Q̂,q) = Ê² + (q²+q³)ÊQ̂ + (q⁶ − q³Ê)Q̂² + (−q⁷ + q⁴Ê)Q̂³,
Q̂E^{−m} = q^m E^{−m},   ÊE^{−m} = E^{−(m−1)}
```

plus a boundary ansatz fixing `a_{−1}`.

## 3. Every step controlled against something already held

**R80-1 applies to a paper that is right, not only to one that is wrong.** Nothing here was taken
from the page.

| | control | result |
|---|---|---|
| **C1** | the recursion is **derived here from `Ĉ`**, and must reproduce **both** relations Park prints for `a_{−1}` and `a_{−2}` | PASSED — identical |
| **C2** | the chain's `a_{−1}` must reproduce **every term Park prints**: `−q^{−1} + 1 − q² + q⁵ − q⁹ + q¹⁴ − q²⁰ + q²⁷` | PASSED — and every zero between them |
| **C3** | the forward `a_0…a_3`, converted from **this bench's own `C_m(5₂)`** — from the R-matrix state sum on Park's braid word (memo 185 addendum 3), touching no table and no paper | PASSED — all four |
| **C4** | **Conjecture 2 itself**, checked on a knot with a published answer: `4₁` (`a_{−m} = 1`) against **GM eq (11)**'s four printed blocks | PASSED — identical, **no normalisation factor at all** |

C3 is the one worth pausing on: **two papers' machinery, met through this bench's own computation.**
Our colored Jones of `5₂` → our `C_m` → Park's printed inverted-Habiro `a_m`, exactly.

## 4. The cell

*(A: the route reproduces `f_0…f_5`, computed independently from the large-colour Verma R-matrix
→ the route is live and `f_6`+ are determined. B: it does not, and the blocker stands.)*

```
f_0 : MATCH over q^-1..q^14   (16 coefficients)
f_1 : MATCH over q^-1..q^58   (60 coefficients)
f_2 : MATCH over q^-1..q^58   (60 coefficients)
f_3 : MATCH over q^0 ..q^48   (49 coefficients)
f_4 : MATCH over q^-2..q^25   (28 coefficients)
f_5 : MATCH over q^-3..q^7    (11 coefficients)
```

> **CELL → OUTCOME A.** Every block the Verma trace could reach, reproduced — 224 coefficients in
> total, with the horizons set by the stored block lengths and not by any disagreement.

## 5. Past the blocker

```
f_6 = +q^-4 +q^-3 -2q^-1 -q^0 -2q^1 -4q^2 -q^3 +6q^5 +7q^6 +9q^7 ...
f_7 = +q^-5 -2q^-2 -3q^-1 -2q^0 -q^1 -q^2 +2q^3 +4q^4 +9q^5 +9q^6 ...
f_8 = -q^-4 -2q^-3 -3q^-2 -2q^-1 +3q^1 +3q^2 +6q^3 +7q^4 +10q^5 +6q^6 ...
```

Banked in `data/f52_blocks_beyond.json`. **The depth is not fixed at 8** — the chain runs to
whatever depth is asked of it; 8 is where this run stopped.

## 6. What this does NOT close, stated as plainly as the positive

**Conjecture 2 is a conjecture.** What is established is that it holds **exactly** on `4₁` and
reproduces **all six** independently computed blocks of `m(5₂)`. **The blocks past `f_5` rest on
it, and are labelled as resting on it. They are not theorems**, and no downstream memo may quote
them at a higher strength than this line.

## 7. What it unblocks

Memo 177's ceiling question needed `F_K` for a hyperbolic knot beyond `4₁`, at depth. It now has
`m(5₂)` to arbitrary block index. **Note the standing fence: R83 stopped paying for the `c_eff`
route because its success would not have been evidence, and that is unchanged by having more
blocks.** What the blocks are good for is the *tail* and *structure* questions of memos 184 and
186, which are measurements rather than proxies.

## 8. Named follow-up

**F190-1.** Run the chain deep (`DEPTH` and `XMAX` are parameters) and re-measure memo 184's
`Φ_{m(5₂)}` and `c_edge` with blocks that are no longer fenced at seven coefficients.
