# B8091 — what the FIRST STEP throws away: the monodromy is M², and squaring erases the bits

**Date:** 2026-08-19 · **Seat:** cc3 (audit) · **Verdict: PROVED** for the destruction;
**the identification is UNPROVED and registered as such.** Reproducer `first_step_losses.py`.
Gate 5 untouched — 2×2 integer matrices and word combinatorics only.

## The owner's question

Does the founding rule `a→ab, b→a` already encode arrow, chirality and selection — so that the
recurring bottlenecks are **one loss with several shadows** rather than four unrelated walls?

## What is PROVED

1. **The monodromy is the SQUARE of the substitution matrix.** `M = [[1,1],[1,0]]`,
   `M² = [[2,1],[1,1]]` — trace 3, det 1 — which is `φ₁`, the figure-eight monodromy.
2. **Loss one — ORDER.** `a→ab` and `a→ba` are different rules with **identical** incidence
   matrices: the matrix counts letters and never arranges them. The mirror is invisible downstream.
   *(Bite control: `a→aab` **does** change the matrix, so the blindness is not vacuous.)*
3. **Loss two — SIGN.** `det M = −1`, `det M² = +1`. Squaring erases it.
4. **The squaring is FORCED, not chosen.** A punctured-torus bundle is orientable iff its monodromy
   is orientation-preserving. `det M = −1` is **inadmissible**; `M²` is admissible. **Orientability
   is what costs the sign.**

This matches the corpus's own chain, which already reads *"geometrize (priced) and **orient
(priced)**"* — this arc says **what the orientation price is denominated in**.

5. **Observation, unweighted (B888 discipline):** `φ₁ − I = M` exactly. The Smith-normal-form
   computation that yields the torsion `(ℤ/m)²` runs, at `m = 1`, on the substitution matrix itself.
   **No mechanism claimed.**

## The inventory, with a mechanism under each line

| lost at step one | how | price |
|---|---|---|
| order inside `σ(a)` | the incidence matrix counts, never arranges | **bit** |
| sign of `det` | squaring, forced by orientability | **bit** |
| intercept | the slope fixes the hull, not the point on it — **never present**, not lost | **circle** |
| eigenvalue's unit | only ratios of eigenvalues are scale-free — **never present** | **ray** |

**Two bits, one circle, one ray** — the owner's stated price, now with a mechanism per line. Note
the asymmetry the table records honestly: the two bits are **destroyed**, the circle and ray were
**never there**. Those are different kinds of absence and should not be merged.

## What is NOT proved, and must not be read as proved

**The IDENTIFICATION.** That order-loss **is** chirality and sign-loss **is** the arrow is
**conjecture**, not result. B945's Klein group is suggestive, but **reversal and letter-swap both
send `ab → ba`**, so which loss carries which bit is genuinely unsettled. A table that lines up is
not a theorem. Registered as the sharpened **L169**.

## Why it reframes the bottlenecks

Every downstream construction inherits **`M²`, not `M`**. So each time the object is asked for a
basepoint and returns a torsor, it is **the same discarded information resurfacing** — not four
independent walls. **Falsifiable prediction:** a new wall should appear exactly where a construction
needs to distinguish `M` from `M²`, and nowhere else.

## SCOPE

2×2 integer matrices and word combinatorics. Proves the destruction and the forcing; proves nothing
about `E₆`, the SM, or which bit is which. No values, no measurements.
