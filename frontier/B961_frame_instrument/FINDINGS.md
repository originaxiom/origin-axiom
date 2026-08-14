# B961 — L135: THE FRAME INSTRUMENT, built on this bench

**Date:** 2026-08-08 · **Seat:** cc (banking) · **Lane:** MATHEMATICS / INSTRUMENT.
Gate 5 untouched. **Discharges** the buildable half of L135 (registered by B958).

---

## 1. Why this exists

B958 found that **the repo had no independent construction of the frame or of M12**: B909
verified §LVIII by *running incoming material*, not by rebuilding. So every frame-arc claim
in this programme has been checked against code the bench did not write.
**`frame.py` is the missing infrastructure.**

**What it deliberately does NOT do:** guess the solo seat's frame, floor, or M12. B958's
stated reason for deferral stands — reconstructing their definitions wrongly would produce a
false verification *or* a false refutation. This module supplies the **operations** any frame
claim needs; pinning their specific construction still requires their definitions.

## 2. What it provides

| export | what it does |
|---|---|
| `ad(v)` | exact 78×78 adjoint matrix in the Chevalley basis |
| `killing()` | the **exact** Killing form K(x,y) = tr(ad x · ad y) |
| `centralizer(S)` | {x : [g,x] = 0 ∀g ∈ S} |
| `killing_perp(S)` | {x : K(v,x) = 0 ∀v ∈ S} |
| `derived(S)` | a basis of [S,S] |
| `dim_of(S)`, `cartan_basis()`, `a2_a1_levi()` | dimensions, the standard Cartan, the SMT Levi |
| `self_test()` | every export exercised against a **banked** number |

## 3. The self-test — four banked numbers, all reproduced

| check | value | against |
|---|---|---|
| Killing form symmetric | ✅ | — |
| Killing form rank | **78** (nondegenerate) | e₆ semisimple |
| **dim Z(su(3)_colour)** | **16** | **B958** ✅ |
| **A₂+A₁ Levi: dim / derived / centre** | **14 / 11 / 3** | **B892, B951** ✅ |
| Killing-perp of the Cartan | **72** = 78 − 6 | ✅ |

> **B892's three numbers — dim 14, derived 11, centre 3 — are now derivable from scratch on
> this bench.** That is the first time; before today they were only ever checked by running
> incoming code.

## 4. The self-test earned its keep immediately

The first run returned **derived = 4, centre = 10** instead of 11 / 3. The cause was a real
bug in this module: `sympy`'s `rref()[1]` returns the tuple of **pivot columns**, and I was
using it to index **rows** — silently producing a wrong-dimensional space with no error.

**The banked-number gate caught it; nothing else would have.** A 14-dimensional algebra with
"derived 4, centre 10" is not obviously absurd, and had `derived()` been used first on an
unbanked question the wrong answer would have looked like a finding. The fix is in place
with the trap documented in the source.

## 5. What remains owed

- **The presence side** (solo §LXXXIII–LXXXVI + §XCII) is **still not verified.** This arc
  builds the tools; it does not supply solo's frame definitions.
- **The specific frame, floor and M12** need either solo's definitions stated precisely
  enough to rebuild, or an independent derivation of what "the orthogonal charge frame" is
  from banked structure. Either is a separate cell.

## 6. Honest limits

1. This is an **instrument**, not a result. It asserts no new mathematics about the object.
2. The e₆ structure constants come from `B854_centralizer_exact/e6_centralizer.py` — this
   module wraps and verifies them, it does not re-derive the Chevalley basis.
3. `self_test()` covers the exports against four banked numbers; it is not a proof of
   correctness for arbitrary input.

---

**Verdict: INSTRUMENT.** The bench can now compute centralizers, Killing-perps and derived
algebras in e₆ on its own, and it reproduces B892's and B958's banked numbers from scratch.
The presence-side debt stays open; what closed is the excuse for not being able to check it.
