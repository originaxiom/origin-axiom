# s961's firing does not come down to m025 as a module — it comes down only as the mirror pair (chat1, 2026-10-06)

Sealed at `efd8be94` (commit 210b0623) before any cell ran. `firing_descent.py` → `run.txt`. Primes 13, 29, 37, all agree.

| | prediction | prior | outcome |
|---|---|---|---|
| C1 (control) | B1432's s961 census with chat1's own code on s961 = ker w ⊂ π₁(m025) | 75% | **HOLDS**: 16 characters, 16 loci (h¹ = 1), 12 non-square; **72 of 256 fire, all on the non-square loci, 6 each**, index ±1 (36/36); both stacking orders |
| D1 | the mirror deck σ fixes exactly the order-≤2 characters | 95% | **HOLDS**: 4 fixed, orders 1,2,2,2 |
| D2 | σ fixes no firing module; pairs them with equal index | 90% | **HOLDS**: 0 fixed; σ*V is firing for 72/72, same index 72/72 |
| D3 | Shapiro: I(m025; Ind V) = I(s961; V) | 85% | **HOLDS** 72/72 |

**The argument (now checked):** a σ-invariant character of s961 extends to m025, so on the torsion (ℤ/4)² it factors
through m025's (ℤ/2)²: order ≤ 2, a square. Every firing module has a non-square extension character. So no firing
module is σ-fixed, and none descends to m025 as a 2-dim module.

**What it says.** The registered cell closes negatively: on this level the register lemma cannot split a firing count
into two unequal register halves, because no firing module is a pullback. The act-alone state (m025, non-orientable)
carries the firing only as the induced pair {V, σ*V}, and that pair has the same count (D3). The mirror does not flip
the count (D2: equal index within each pair), as GENESIS states for a geometric mirror. Read as structure: the three-fold
firing needs ℤ/4 data that only appears once the register is part of the state (tick 6, not tick 3).

**Fence.** Frame F-CI; object s961 ↔ m025 at the golden act's ticks 6/3; reach *single*. Not a count on a vacuum, not a
generation number, no value. Nothing to CLAIMS/GENESIS/ledgers.
