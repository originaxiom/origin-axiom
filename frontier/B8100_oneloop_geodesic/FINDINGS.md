# B8100 — the one-loop GEODESIC factor computed, and the cusp piece located in B739

**Date:** 2026-08-20 · **Seat:** cc3 (audit) · **Verdict: PROVED** (a rung, with an honest cutoff
error). First construction rung of the owner-elected **finish-the-3d-theory** line. Gate 5
untouched — a mathematical partition function; no measured value anywhere.

## What was computed

The **Giombi–Maloney–Yin graviton product** over the object's **own** complex length spectrum:

`Z_geod = ∏_γ ∏_{n≥2} |1 − q_γⁿ|⁻²`,  `q_γ = e^{−ℓ_γ + iθ_γ}`

**Result:** `log Z_geod = −0.272977 ± 2.0×10⁻³`, i.e. `Z_geod ≈ 0.7611`.

**Controls:** the systole reproduces the known `1.087070144995739`; geodesics come in
complex-conjugate pairs as a real manifold requires; the cutoff was pushed to `ℓ ≤ 5.5`
(**214 classes, 2819 geodesics** with multiplicity).

> **CORRECTION 2026-08-21 (found by cc's B1107 harvest, verified here by three fresh fetches):** this line originally read *"134 classes, 1221 geodesics"* — **those are the cutoff-5.0 counts**, not 5.5. **The computation used the correct 5.5 spectrum** — B1107's from-scratch reproduction agrees at `3.6×10⁻¹⁵`, which could not happen otherwise — **only the prose count was stale.** Documentation defect, non-blocking. **It should have been caught here:** B8112 printed `classes below 5.5: 214 · geodesics with multiplicity: 2819` in this same seat, and the contradiction with this line went unread.

## The error is honest, and the reason matters

**The convergence is OSCILLATORY, not monotone** — the cutoff deltas change sign, because
`−2log|1−qⁿ|` takes either sign depending on the holonomy angle `θ`. **So the last value is not the
answer and the extra digits are not significant.** The uncertainty is the size of the last delta,
`2×10⁻³`, and it is quoted that way rather than as a converged decimal.

## WHAT THIS IS NOT — and it is the load-bearing caveat

**This is not the one-loop partition function of the object.** The GMY product is the graviton
determinant over a hyperbolic quotient's **discrete** spectrum. **Our object is finite-volume but
NON-COMPACT: one cusp.** The cusp carries a **continuous** spectrum that this product omits
**entirely**.

So the number above is a **well-defined spectral invariant** — the geodesic factor — **and not a
partition function.** Anyone quoting it as one would be wrong, including me.

## WHERE THE MISSING PIECE ALREADY IS — and this is the finding

For a cusped hyperbolic 3-manifold the continuous contribution is governed by the **scattering
determinant**, and the corpus has the object's **exactly**:

> **B739:** `φ_m004(s) = Λ_K(s−1) / Λ_K(s)`

**So the one-loop partition function's two halves are both in reach:** the discrete half computed
here, the continuous half banked in B739 — **and never combined.** The next rung is therefore
**named and unblocked**, not speculative: combine them.

**That is what "finish the 3d theory" looks like as a concrete step rather than an ambition.**

## SCOPE

A **rung, not a completion**. The geodesic product is over the object's own spectrum with a stated
cutoff error. **Does not include the cusp**; does not claim a partition function; says nothing about
which of B8099's two theories is being completed — this factor belongs to the **gravity** side
(the hyperbolic saddle), not to `T[4₁]`'s abelian content.
