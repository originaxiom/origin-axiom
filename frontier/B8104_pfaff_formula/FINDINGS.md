# B8104 — the cusped formula EXISTS explicitly: retracting my own NEEDS-SPECIALIST label, two hours old

**Date:** 2026-08-20 · **Seat:** cc3 (audit) · **Verdict: PROVED.** Gate 5 untouched.

## The retraction, first

**B8102 (mine, today) labelled the cusped one-loop gap `NEEDS-SPECIALIST-CONFIRMED`**, on the stated
ground that *"abstracts were read, not full papers."* **The owner's thesis — a specialist gate has a
date — was applied to the main line, the paper was read, and the label is wrong.**

**It expired in under two hours.** That is the thesis vindicated about as sharply as it can be.

## What the paper actually contains

**Jonathan Pfaff, *Analytic torsion versus Reidemeister torsion on hyperbolic 3-manifolds with
cusps*, arXiv:1206.0228, Theorem 1.2** — for `m ≥ 3`:

> `T_X(ρ(m)) / T_X(ρ(2)) = (c(m)/c(2))^{κ(X)} · exp(−(1/π)·vol(X)·(m(m+1)−6)) · ∏_{k=3}^{m} |R(k,σ_k)|`

with `κ(X)` **the number of cusps**, `R(s,σ_k)` the **Ruelle zeta function**, and `c(m)` an
**explicit closed-form constant** the paper describes as *"a defect caused by the non-compactness of
the manifold… they appear via the contribution of a certain non-invariant distribution to the
geometric side of the Selberg trace formula."*

**That is exactly the three-term structure B8101 assembled** — a volume term, a geodesic/zeta term,
and a cusp term — **derived, explicit, and published in 2012.**

## Every ingredient is in hand for our object

| term | our value |
|---|---|
| `κ(X)` — number of cusps | **1** (verified, B8099) |
| `vol(X)` | **2.029883212819307** (verified exact, B8099) |
| `c(m)/c(2)` — the cusp defect | computed here: **0.7121** (m=3), **0.5532** (m=4), **0.4523** (m=5) |
| volume factor | computed here: **0.02072** (m=3), **1.179×10⁻⁴** (m=4), **1.842×10⁻⁷** (m=5) |
| `∏|R(k,σ_k)|` — Ruelle zeta | **built from the geodesic spectrum B8100 computed** |

**Nothing in the formula is unavailable to us.**

## The remaining gap, now small and specific

Pfaff's `ρ(m)` are the **2m-th symmetric powers of the standard `SL₂(ℂ)` representation**, and the
object is **analytic torsion** — not, verbatim, the AdS₃ graviton one-loop partition function.

**So the honest remaining question is one identification:** *does the AdS₃ boundary-graviton one-loop
determinant correspond to one of Pfaff's `ρ(m)` torsions, and if so which?*

**That is a far smaller and better-posed gap than "the cusped test function does not exist."** The
machinery is explicit and the inputs are ours; what is missing is a dictionary entry, not a theorem.

## WHAT I AM NOT CLAIMING

- **Not** that we have the one-loop partition function. We do not.
- **Not** that the identification above is trivial — it is the real remaining question.
- **Not** that Pfaff's theorem was hard to find. **It was the second hit of the first search**, and
  I labelled the gap NEEDS-SPECIALIST before reading it. **The error was mine and the label was
  premature.**

## SCOPE

Theorem 1.2 read from the source; the cusp defect and volume term computed for our object. **Does
not assemble a partition function.** Gate 5 untouched.
