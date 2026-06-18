# B163 — the κ-sweep resolved: the κ<2 spectrum is a Cantor set; no figure-eight geometric encoding

**Date:** 2026-06-18. **Status:** the two open items B162 left on lead **L19** are resolved, each with a
built-in control / null-test. **(3a)** the non-Hermitian `κ<2` spectrum is a **genuine Cantor set (totally
disconnected)**, not a curve — control-bracketed numerically. **(3b)** there is **no spectral encoding** of the
figure-eight hyperbolic geometry — the link is the boundary-trace value `κ=−2` alone (B160). Standalone spectral
mathematics; **no Origin-core claim, no physics crossing**; P1–P16 untouched; nothing to `../../CLAIMS.md`.
Ledger V157. Reproducer `kappa_resolved.py`.

## Result (3a) — κ<2 is a Cantor set (totally disconnected) **[num, control-bracketed]**

"Thin / zero-2D-area" (B162) cannot distinguish a Cantor set from a connected curve (both are zero-area). The
decisive feature is **total disconnectedness = persistent gaps at all scales**. Diagnostic: the **largest
spectral gap** = max edge of the minimum spanning tree (MST) of the finite-chain spectrum, normalized by the
diameter, as the chain length `F_k` grows — `→ 0` for a connected curve/band, `→ const>0` for a Cantor set.

| `κ` (via λ) | max-gap/diam at F = 144 / 377 / 987 / 1597 | trend |
|---|---|---|
| `κ=2` (λ=0) **[band control]** | 0.0108 / 0.0042 / 0.0016 / 0.0010 | **→ 0** (connected band) |
| `κ=3` (λ=1) **[Cantor control, Sütő]** | 0.165 / 0.164 / 0.164 / 0.148 | **→ const ≈ 0.16** (Cantor) |
| `κ=1` (λ=i) | 0.056 / 0.058 / 0.057 / 0.058 | **→ const ≈ 0.057** (Cantor-like) |
| `κ=−2` (λ=2i) | 0.185 / 0.183 / 0.183 / 0.182 | **→ const ≈ 0.18** (Cantor-like) |

Both `κ<2` cases hold a **positive normalized gap across a >10× range of chain lengths** — exactly the Cantor
control's behavior, and the opposite of the band control's `→0`. So the `κ<2` spectrum has gaps at all scales:
it is **totally disconnected — a Cantor set in ℂ**. This upgrades B162's "thin/zero-area" to "Cantor". **Honest
scope:** a control-bracketed *numerical* verdict (finite-size extrapolation, F up to 1597) — **not a theorem**:
there is no ground-truth spectral theorem off the real axis (Damanik–Gorodetski's horseshoe covers only the
Hermitian `κ>2` regime), so the all-orders statement stays open.

## Result (3b) — no figure-eight geometric encoding **[num, negative + null-test]**

Falsifiable form: is any spectral feature non-analytic/extremal *exactly* at `κ=−2`, or does any feature hit a
figure-eight invariant only there?

- **Smoothness through κ=−2.** Every feature (`max|Im E|`, Re-extent, Im-extent, 2D-area, max-gap/diam) is
  **smooth** across `κ=−2` — the 2nd difference at `κ=−2` equals the typical value (no kink, no extremum). The
  spectrum does **not** register the cusp opening (the commutator turning parabolic) at `κ=−2`.
- **Null-test on invariants.** No figure-eight invariant (vol = 2.0299, `|√−3|` = 1.732, `2/φ` = 1.236,
  `2cos(π/3)` = 1) is matched specially at `κ=−2`: in every case the **neighbors (κ=−1.8, −2.2) match equally
  well or better**, so any near-coincidence is an artifact of the smooth sweep, not an encoding.

**Verdict:** the κ=−2 spectrum does **not** encode the figure-eight hyperbolic geometry. The figure-eight
connection lives entirely at the level of the **boundary invariant** `κ = tr[A,B] = −2` (B160/B162), not in the
spectral set. The intuitive "the quasicrystal Cantor spectrum *deforms into* the hyperbolic structure" reading
is **refuted at the spectral level** — what deforms is one number (`κ`), not a spectrum-to-geometry map.

## What this settles (the L19 ledger)

- κ<2 Cantor-persistence (3a): **resolved numerically (control-bracketed) — YES.** Theorem off-axis: still OPEN.
- κ=−2 geometric encoding (3b): **resolved — NO** (smooth + null-test).
- So the κ-sweep is one foliated object with a **Cantor spectrum at every κ≠2** (real for κ>2, complex for κ<2)
  and a **single full-band cancellation fiber at κ=2** (B161/B162) — and its only tie to the figure-eight
  3-manifold is the shared boundary trace, not the spectrum.

## Firewall

Spectral / character-variety mathematics. The (3b) negative *sharpens* the firewall: the figure-eight bridge is
the boundary invariant `κ`, not an emergent geometry-from-spectrum crossing. No `Λ`, no scale, no spectral-mass
identification; nothing to `CLAIMS.md`; P1–P16 untouched.

## Anchors
B162/V156 (the κ-sweep; the "thin" result this upgrades and the OPEN items this resolves), B161/V155 (κ=2 the
cancellation wall), B160/V154 (κ=−2 ⟺ λ=2i, the boundary trace), `speculations/S034` (the spine), B67 (the
figure-eight). External: Sütő (1987); Damanik–Gorodetski (the Hermitian-κ>2 horseshoe — the missing off-axis
ground truth). Ledger V157.

## Reproduction
`python frontier/B163_kappa_sweep_resolved/kappa_resolved.py` — (3a) the max-gap/diam table with both controls;
(3b) the smoothness + null-test. Prints `ALL CHECKS PASS`.
