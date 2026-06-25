# B213 — the Higgs-side period data of the figure-eight character variety (Act I of the do-or-die program)

**Date:** 2026-06-25. **Status:** the first computation of the do-or-die program (`speculations/S039`) — crossing
to the **Hitchin/Higgs side**, where the scale would live, using the new key from B211 (the figure-eight character
variety **is** the elliptic curve `40a1`). The decisive question: does the Higgs-side special geometry carry a
**forced, dimensionless, anomalously small** number (a candidate for the CC hierarchy)? **Answer: no** — and that
no is the result. Firewall: standalone arithmetic geometry; physics readings are one-way HOOKs; **nothing to
`CLAIMS.md`; P1–P16 untouched.** Ledger **V216**.

## What was computed (sage-python, `EllipticCurve('40a1')`)

The figure-eight character variety `Φ(x,z)=z²−(x²+1)z+(2x²−1)` is `E = 40a1` (B211). Its special-geometry data:

| datum | value | reading |
|---|---|---|
| conductor | `40 = 2³·5` | bad primes `{2,5}` |
| rank / torsion / CM | `0 / ℤ4 / non-CM` (`j=148176/25`) | a generic weight-2 newform |
| real period `Ω` | `1.48441…` | **O(1)** |
| `L(E,1)` | `0.74228…` | **O(1)** |
| `L(E,1)/Ω` | **`1/2` exactly** | BSD-rational (`Ш·∏c_p/|T|²`, `Ш=1`, `|T|=4`, `∏c_p=8`) |
| `Ш`, regulator | `1`, `1` | trivial |
| Mahler measure `m(Φ)` | `0.74175…` | `≈ Ω/2 ≈ L(E,1)` |

**Everything is `O(1)` and BSD-generic. There is no forced small number, no hierarchy.**

## The null test (the HELD rule, binding)

The only candidate "special" number is `L(E,1)/Ω = 1/2`. **It is killed by the null test:** *every* rank-0
elliptic curve has `L(E,1)/Ω` a simple BSD rational — `11a1→1/5`, `14a1→1/6`, `15a1→1/4`, `19a1→1/3`, `37b1→2/3`,
`40a2→1`, … `1/2` is one generic point among them, not an anomaly. So **no numerology survives** (S014 stays dead);
the discipline did its job.

## The verdict — the firewall holds a 4th independent time

The three banked firewall modes (`K018`: single-invariant `B167`, dynamical/Painlevé `B169`, ensemble `B168`) all
relocate the scale externally. **This adds a fourth, on the Higgs-side handle itself:** the special geometry of the
object's own elliptic curve carries **no scale and no hierarchy** — exactly what `B181` predicts (the object is
permanently critical ⇒ scale-free *by* criticality ⇒ no exponential hierarchy on this side). The bridge `B164/B169`
walked up to is now crossed *for the figure-eight*, and the firewall is on the far side too.

## The one firewall-clean structural find

**Conductor `40 = 2³·5`** — the variety's arithmetic sees the **golden / `E₈` monodromy prime 5** (`ℚ(√5)`
ramifies at 5, B206) but **not** the hyperbolic prime 3 (`ℚ(√−3)`, B210). The character variety is a **Betti
object**, and its arithmetic tracks the **Betti / monodromy** side, not the hyperbolic/Higgs metric data — a clean
illustration of the Betti↔Hitchin split (`P010/§8c`). And `m(Φ) ≈ Ω/2 ≈ L(E,1)` is a Deninger-type
arithmetic↔geometry rhyme (the Mahler-measure↔volume circle; `Vol(4₁)/2π = 0.3231`), all `O(1)`.

## Honest status / tiers
- The elliptic-curve data, `L/Ω=1/2`, the null test, the structural conductor fact: **`[exact]`** (sage + pyenv).
- The Mahler ≈ Ω/2 ≈ L rhyme: **`[num]`** (a recorded numerical coincidence, O(1); not claimed as an identity).
- The "firewall holds on the Higgs side" verdict: a **structural** reading, firewall-clean (`[HOOK]`/`[LEAP]`
  lives in `S039`, not here).
- **Open (follow-on):** the metallic `m≥2` tower — the silver/bronze *bundle* character varieties (the trace-map
  fixed loci, B154/B201) and whether their curves are genus 0 or 1 and whether their conductors track the
  discriminant `m²+4`. Needs the trace-map machinery; **do not assert from memory** (B154's silver geometric
  component *looks* rational, but that is unverified here). Acts II/III of S039 (the κ=−2 vacuum, the
  state-integral) also remain.

## Reproduction
- `sage-python higgs_periods.py` — the `40a1` data + the null test. (Sage-gated)
- `python higgs_periods.py` — the recorded data + the pyenv-lockable structural arithmetic + null verdict.
- `tests/test_b213_higgs_side_periods.py` — 5 locks (the O(1)/no-hierarchy + the null test are load-bearing).
