# B165 — toward the off-axis (κ<2) Cantor theorem: a conditional reduction + seed-robust evidence (P2a)

**Date:** 2026-06-18. **Status:** P2a of Masterplan II. B163 showed the non-Hermitian κ<2 spectrum is totally
disconnected (a Cantor set) numerically (MST max-gap, control-bracketed). This stage delivers the honest P2a
outcome: the disconnectedness is **seed-robust** (golden/silver/bronze), and the off-axis Cantor result is reduced
to a single open hypothesis — **uniform hyperbolicity of the complexified trace map** — which is **NEEDS-SPECIALIST**
(Damanik–Gorodetski is Hermitian-κ>2 only; no off-axis ground truth). Standalone spectral mathematics; no scale,
no physics; P1–P16 frozen; nothing to `../../CLAIMS.md`. Ledger V162. Reproducer `cantor_offaxis.py`.

## Results

- **D0 [exact].** The Fibonacci trace map `T(x,y,z)=(2xy−z,x,y)` conserves the Fricke–Vogt invariant
  `I = x²+y²+z²−2xyz−1`. The spectrum is its **non-escaping (bounded-orbit) set** — the object whose topology is
  in question.
- **D1 [num] — seed-robust disconnectedness.** Extending B163's working MST-max-gap-over-diameter diagnostic to
  the **golden (m=1), silver (m=2), and bronze (m=3)** seeds at κ=−2: the gap is **persistent** (≈ 0.206, 0.198,
  0.181 across sizes) and dwarfs the κ=2 band control (≈ 0.002, 0.013, 0.007 → 0). So the κ<2 Cantor structure is
  **not special to the golden seed** — it holds across the metallic family.
- **The conditional theorem (the contribution).** The κ<2 spectrum = the non-escaping set of the complexified
  trace map. **IF** that map is **uniformly hyperbolic** on its non-escaping set (a complex horseshoe), **THEN**
  the spectrum is a Cantor set (totally disconnected) — the standard horseshoe ⟹ Cantor argument. So the open
  theorem is reduced to **one** hypothesis: *off-axis uniform hyperbolicity.* It is supported numerically (B163 +
  D1, three seeds) but its **proof is NEEDS-SPECIALIST** — no off-axis ground truth, and the transfer matrices are
  non-normal (spectral abscissa ≠ top eigenvalue), so the Hermitian-κ>2 methods (Damanik–Gorodetski) do not carry.

## Verify-don't-trust record (two diagnostics that FAILED — do not re-attempt)

In trying to add a *second, independent* numerical diagnostic beyond B163's MST, two attempts **failed to cleanly
separate Cantor from band** and were discarded (recorded so they are not re-tried):
- **ε-component-count** at a fixed fraction of the diameter: the *known-Cantor* control was **flat** (`[4,4,4]`) —
  the bands merge at that scale, so it does not track disconnectedness.
- a **naive trace-map Jacobian "domination" ratio**: contaminated by **escaping** orbits (the κ=2 non-hyperbolic
  control also gave large ratios) — it measures generic escape, not bounded-set hyperbolicity. Genuine
  hyperbolicity evidence requires the bounded set itself, which is exactly the NEEDS-SPECIALIST step.

So **B163's MST-max-gap remains the one clean numerical diagnostic**, now extended seed-robustly here. The honest
P2a yield is: *seed-robust numerical Cantor evidence + a clean conditional reduction + a specialist hand-off* — the
all-orders off-axis theorem stays OPEN (exactly the plan's calibration).

## Firewall
Spectral / dynamical mathematics. No scale, no Λ, no spectral-mass; nothing to `CLAIMS.md`; P1–P16 untouched.

## Anchors
B163 (the MST diagnostic + the κ<2 Cantor result this strengthens), B109 (the trace-map dynamics / void
linearization — the would-be hyperbolicity model), B160/B162 (silver/bronze seeds), K007/K010 (the
Damanik–Gorodetski / Sütő framing — Hermitian-only). Ledger V162. External: Damanik–Gorodetski (the Hermitian-κ>2
horseshoe — the theorem whose off-axis analogue is the open hypothesis); complex/non-normal horseshoe theory
(the specialist domain).

## Reproduction
`python frontier/B165_kappa_cantor_offaxis/cantor_offaxis.py` — D0 (I conserved), D1 (seed-robust MST max-gap),
the recorded failed-diagnostics note, the conditional theorem. Prints `ALL CHECKS PASS`.
