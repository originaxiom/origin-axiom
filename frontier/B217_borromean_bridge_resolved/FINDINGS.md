# B217 — L40 resolved: the Borromean bridge is the origin of the VOLUME (cusped), not the period (closed)

**Date:** 2026-06-26. **Status:** L40 (the Borromean-surgery bridge) **resolved** — and it resolves the
closed-vs-cusped subtlety the program had banked (V200). The Borromean parent (L31) is the geometric source of the
hyperbolic **volume** (the cusped side); B204's **period law** lives on the **closed** torus-bundle (Sol) side and
is **algebraic** (the trace / Gauss sums). They are two different invariants of two different manifolds sharing
only the monodromy `γ`. Firewall: standalone quantum-topology / hyperbolic geometry; **nothing to `CLAIMS.md`;
P1–P16 untouched.** Ledger **V220**.

## The question (chat1's L40)

Does B204's WRT period law have a *geometric* origin via the Borromean parent (L31), rather than only the
algebraic Gauss-sum one? **Answer, computed: no** — because the period and the Borromean live on different
manifolds.

## The two sides (computed)

- **B204's `Z_k = tr(ρ_k(γ))` is the CLOSED torus bundle (Sol).** Verified: `Z_k(identity) = Z_k(T³) = dim ρ_k =
  k+1` (k=1..5), the closed-3-torus signature; and the figure-eight closed bundle is the period-5 object
  `|Z_3(1,1)| = 1/φ`. **The PERIOD lives here — algebraic (B204/B214/B215/B216).**
- **The CUSPED figure-eight carries the hyperbolic VOLUME.** The Borromean fillings of L31 are the cusped
  hyperbolic bundles (figure-eight knot complement m004 = 2 ideal tetrahedra; the metallic family = Borromean
  Dehn fillings). The invariant the Borromean parent governs is the **volume**, via the Kashaev volume
  conjecture: `(2π/N) log⟨4_1⟩_N → Vol(4_1) = 2.02988` — confirmed with the known Ohtsuki `(3π logN)/N`
  correction (corrected estimate: N=100→2.013, 200→2.021, 400→2.026, 700→2.027 → 2.0299). **The VOLUME lives
  here — geometric (L31).**

## The resolution

The **period** (closed, algebraic) and the **volume** (cusped, geometric) are *different invariants of different
manifolds* sharing the monodromy `γ` — the **closed-Sol / cusped-hyperbolic duality** (V200). The Borromean
parent is the geometric source of the **volume**, not the period.

A Borromean **surgery** presentation of the *closed* bundle (torus bundles are Borromean surgeries) would
reproduce `Z_k` only by **topological invariance** (same manifold ⇒ same RT invariant) — a re-presentation, never
an *explanation* of the period. This **confirms and sharpens chat1's caveat** ("may just reproduce the period
without explaining it"): it can only reproduce, and in fact it governs a *different* invariant (the volume)
altogether. So:

> **The period law's origin is algebraic** (the trace / Gauss sums, B204–B216); **the Borromean/geometric content
> of the family is the VOLUME** (L31 + the volume conjecture). Two faces of the shared monodromy, not one bridge.

## Honest status / tiers
- `Z_k(T³)=k+1` (closed-bundle signature): **`[exact]`**.
- the Kashaev volume conjecture for `4_1`: **`[num, confirmed]`** (a *theorem* in the literature; my numerics
  confirm with the Ohtsuki correction) — the geometric content.
- the resolution (period↔closed↔algebraic vs volume↔cusped↔Borromean): a **structural** conclusion from the
  computed facts + V200; firewall-clean.
- Novelty UNCHECKED (the closed/cusped distinction and the volume conjecture are classical; the resolution of L40
  for *this* family is the contribution).

## Reproduction
- `python closed_vs_cusped.py` — the closed-bundle signature + the volume-conjecture confirmation. (pyenv)
- `tests/test_b217_borromean_bridge_resolved.py` — 2 locks (closed-bundle `k+1` + the volume convergence).

## Net (the WRT-period arc, now complete in-sandbox)
`B204` (metallic closed period) → `B214` (general-word period + Funar) → `B215` (class-field law, f≤4) → `B216`
(f≥8 = genus-theoretic, NEEDS-SPECIALIST) → **`B217` (the geometric side = the VOLUME, cusped/Borromean; the
period is algebraic, closed)**. The algebraic period and the geometric volume are the two faces; the remaining
open pieces are specialist (the f≥8 genus theory).
