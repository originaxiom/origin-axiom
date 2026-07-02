# B364 — the two lifts are two polarizations: L57 becomes a spin-structure question

**Status: banked (frontier). Analytic identities + numerics at 1e-15; the would-be conclusion was killed by
its own control — recorded as the finding. Firewalled; nothing to `CLAIMS.md`.**

## What was tested

Whether the theta lift (the seam-bearing class, B358–B363) is *the* geometric lift — the transformation action
on level-15 theta functions of the fiber torus.

**The T-side identity (exact + numeric `6e-15`):** the triangular theta family
`f_j(z,τ) = Σ_{n≡j(15)} e(E(n)τ + nz)`, `E(n) = n(n−1)/30`, is T-stable (`E(n+15) − E(n) = n+7 ∈ ℤ`) with
multiplier **exactly the theta lift's** `D = ζ₁₅^{j(j−1)/2}`.

**The control that killed the conclusion (`8e-15`):** the square family `E'(n) = n²/15` is *also* T-stable
(`E'(n+15) − E'(n) = 2n+15 ∈ ℤ`) with multiplier **exactly the canonical lift's** `ζ₁₅^{j²}`. So
**both characteristic classes arise as theta families** — of *different quadratic normalizations* — and
T-stability alone forces nothing.

## The sharpened L57

The two lift classes are two **polarizations** of the fiber's theta geometry:
- the **triangular** family completes the square as `(2n−1)²/120` — the **half-characteristic** (odd) lattice;
- the **square** family `n²/15` — the integral (even) one.

> **L57, polarization form: which quadratic normalization does the two-seed gluing induce on the shared
> fiber's theta bundle?**

**The natural candidate mechanism (conjecture, not claimed):** the fiber is the once-*punctured* torus, and
the puncture endows it with a canonical **odd spin structure** — exactly the half-characteristic. If the
pairing's theta bundle is the puncture-compatible (odd) one, the triangular polarization — hence the
seam-bearing theta class — is **forced on both slots at once** (one bundle, one lift map, both monodromies),
which is precisely the two-sidedness B363 measured. The S-side Poisson analysis (recorded in the reproducer's
derivation) shows the geometric S-matrix carries half-characteristic (`ζ₃₀`) data — consistent with the odd
polarization — but the full S-side identification was not completed here (the honest gap).

## Tiers

Analytic identities (the two lattice-shift computations) + numerics at `1e-15`. The spin-structure selection
is a **conjecture with a named mechanism**, not a result. Nothing promotes.

**Provenance.** B358–B363 (the seam arc; the two-sidedness this would explain), L57. Reproducer:
`theta_geometric.py`; test: `tests/test_b364_theta_polarization.py`.
