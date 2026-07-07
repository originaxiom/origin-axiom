# B458 — Ethogram E5: the per-component CS test — the decisive number is ZERO, and the control shows why that's the finding

**Status: banked (frontier). Firewalled. Prereg: `PREREGISTRATION.md` (PR #600, before
computation). The handoffs' "decisive computation" (Probe 2 / Tests 1+3) — RUN. Verdict:
outcome (a) of the PROBE2 prereg — the figure-eight has NO internal asymmetry at the SL(3)
component level; the 5₂ control shows nonzero per-component CS is GENERIC, making the fig-8's
zero the object-specific datum — and it launders through two banked/known structures. No H1.**

## Machinery (the database bypass)

The Ptolemy database is currently broken server-side (autoindex lists the files; direct GET
404s; Wayback lacks them — documented in-session). Per the prereg's fallback: exact solutions
(sympy, from the same systems as B444) and multi-start-Newton solutions (residuals ≤ 1e-12,
deduped, zero-coordinate branches filtered) fed to **SnapPy's own extended-Bloch machinery**
(`PtolemyCoordinates(...).complex_volume_numerical()` — pure Python, no database).

## The figure-eight (m004): every component is complex-volume-TRIVIAL except the geometric pair

| component | field | complex volume (Vol + i·CS) |
|---|---|---|
| geometric Sym² pair (obs 0) | ℚ(√−3) | **±8.119532851 + i·0** = ±4·Vol(4₁) exactly (the Sym² factor 4 — engine gate ✓) |
| degenerate branches | ℚ | 0 + i·0 |
| **V₁/V₂ (the ℚ(√−7) conic pair)** | ℚ(√−7) | **0 + i·0 AND 0 + i·0** (residuals ~1e-15) |
| obs-1 ℚ(√−3) pair | ℚ(√−3) | 0 + i·0 |

**The decisive number: ΔCS = CS(V₁) − CS(V₂) = 0 — and stronger, CS(V₁) = CS(V₂) = 0
individually, with Vol(V₁) = Vol(V₂) = 0.** The pairing gate is moot (nothing to pair). The
Kashaev invariant's zero phase is not hiding component-level structure; there is none.

## The 5₂ control (m015): rich, generically nonzero — the contrast that makes the verdict

Sym² geometric pair: ±11.312488 = 4·Vol(5₂) exactly ✓ (gate), CS = ∓0.582. The non-geometric
components: volumes ±6.3327, ±3.6176, ±3.1773, ±1.0343 and **nonzero CS throughout** (±0.4810,
±0.6580, ±0.4033, +0.6208, ±0.4831, ∓0.6765, +0.4112, +0.6518, +0.8225). **Per-component CS ≠ 0
is the generic condition.** A knot with "internal CP-violation-shaped component structure" is
unremarkable — 5₂ has it everywhere.

## The verdict

- **Outcome (a) of the handoffs' own prereg fired**: "both components have CS = 0 individually…
  the amphichiral symmetry holds ALL the way down… beautiful, symmetric, and empty."
- **The fig-8's zero LAUNDERS through two banked/known structures**: (i) total amphichirality
  (CS(4₁) = 0, banked) forces the geometric tower's CS; (ii) **the ℚ(√−7) components are
  Falbel's spherical-CR representations** (they land in the real form PU(2,1) — B444's lit
  anchor) — real-form reps are complex-volume-degenerate; zero volume and zero CS is their
  KNOWN geometry, not a new symmetry miracle.
- **The addendum's "enhanced Probe 2" is mooted**: the ℚ(√−7) Galois flip acts on a pair whose
  CS is identically zero — there is no asymmetry to Galois-decompose and no observable for a
  "ℤ/2³ = C×P×T" to couple. HELD stays HELD, now with the computation done.
- **Ethologically** (for the E4 catalog): the organism's distinguishing behavior at this floor
  is *total symmetry* — it is distinguished by having nothing. Consistent with the whole
  corpus: it beats instead of choosing, launders instead of carrying, and vanishes instead of
  violating.
- Adjudication: forced/laundered (knot channel, per prereg). **No H1.** The handoffs' Test 1
  ("what's IN the components") is now answered at the CS resolution: zeros, for known reasons.
  Test 3 (CP on V₁/V₂): answered, zero. Test 2 was closed by banked results (B455 FINDINGS).

## Reproduce
```
python3 component_cs.py     # m004 exact branches -> complex volumes
python3 m015_numeric.py     # the 5₂ control (multi-start Newton -> complex volumes)
pytest ../../tests/test_b458.py
```
