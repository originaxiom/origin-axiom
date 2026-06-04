# Gate 0 — the m=2 trace-map curve IS m136's A-polynomial (verified, resolves the framing question)

**Date:** 2026-06-04. **Status:** exploratory, committed. Proven core P1–P16 untouched. Script:
`frontier/physics_probes/spectral_curve_gate0.py` (SnapPy 3.3.2 + numpy). Standalone topology; no
physics claim. This is **Gate 0** of the spectral-curve plan — the make-or-break foundation.

**Question.** The whole "metallic spectral curve / j=1728" thread rests on the m=2 trace-map
A-polynomial `A(M,L)=M²L²−(M⁴−4M²+1)L+M²` being **m136's actual cusp A-polynomial** (meridian M,
longitude L) — not merely the trace-map fixed-locus eliminant in fiber-eigenvalue coordinates. The
repo's overnight Job 3 left this **INCONCLUSIVE** (framing residual ~6.5e-3).

**Verdict: PASS — it is m136's A-polynomial, at framing k=0.**

## Method (calibrated on a known-answer control)

SnapPy gives the actual `(meridian, longitude)` holonomy of m136 on its deformation variety (Dehn
fillings). At each filling the meridian and longitude commute, so their eigenvalues are paired on the
**same eigenvector** — those `(M,L)` lie on the A-polynomial curve. We test whether a candidate
`A(M,L)` vanishes on them, maximized over framing `M→M·L^k` and orientation, using a **robust**
statistic (fraction of points with `|A|/scale<1e-8`, plus median) so abelian/reducible contaminant
points (on `L=1`) don't mask the match.

**Control (validates the method):** the figure-eight `4_1`, where **B67 proved** the trace-map
A-poly equals Cooper–Long. The same pipeline must confirm it.

## Results

| sample | candidate | on-curve fraction | median resid | framing | verdict |
|---|---|---|---|---|---|
| **4_1** (control) | Cooper–Long | **88%** | 6.4e-16 | k=0 | **MATCH** ✓ (method validated) |
| 4_1 | m=2 curve (wrong) | 34% | 2.6e-4 | k=−7 | WEAK (wrong curve) |
| **m136** (target) | **m=2 trace-map eliminant** | **100%** | **1.5e-15** | **k=0** | **MATCH** ✓✓ |
| m136 | Cooper–Long (wrong) | 6% | 5.5e-4 | k=−8 | NO MATCH (wrong curve) |

(The 12% off-curve points for 4_1 are abelian/reducible reps on `L=1`, not on Cooper–Long — expected.)

## What this establishes

- **The m=2 spectral curve is m136's cusp A-polynomial**, with `(M,L)=(eig t, eig[B,A])` =
  `(meridian, longitude)` at **framing k=0** — **no framing shift, no M↔L swap**. This directly
  refutes the Claude-web "swap M↔L for SnapPy" convention flag (consistent with B67: `eig(t)=meridian`).
- The earlier **Job 3 "INCONCLUSIVE" is resolved**: it fit an *unconstrained* candidate (a spurious
  bidegree-(8,1), i.e. a single L-branch over-fit) and scored it by max-residual over abelian
  contaminants. Using the *known* eliminant + a robust statistic + the calibrated 4_1 control gives a
  clean 100% match at machine precision.
- Therefore **j=1728 (CM by `Z[i]`, τ=i) is a genuine invariant of the manifold m136**, not a
  fiber-curve artifact. The spectral-curve thread is anchored to the real A-polynomial — Gate 0 PASS.

(The cypari gluing-variety elimination 0b is redundant here: the 50-point holonomy match across the
deformation variety with a validated known-answer control already establishes the identity at ~1e-15.)

## Status update for prior ledger rows

This **upgrades** the m=2 A-polynomial: previously "verified as the trace-map eliminant, framing/
SnapPy match OPEN" (V23 INCONCLUSIVE, V30 noted unverified). Now: **`M²L²−(M⁴−4M²+1)L+M²` IS m136's
A-polynomial (framing k=0), verified against SnapPy with a calibrated figure-eight control.**

**Next (Gate 1, number-theory first):** the arithmetic→CM hypothesis across m=1,2,3 + a control set.
Proven core untouched.
