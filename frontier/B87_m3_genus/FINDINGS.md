# B87 (Task 3) — the m=3 metallic curve genus: sequence does NOT decrease to 0; an m=3 refinement

**Date:** 2026-06-05. **Status:** computer-assisted (exact). Standalone low-dim topology / number theory;
**no physics claim** (the spectral-curve physics reading is closed, V34/V65); proven core P1–P16
untouched. Script: `probe.py`. Test: `tests/test_b87_m3_genus.py`.

## What the handoff asked, and what was already known

The CC-web handoff asked for the m=3 spectral-curve genus — "the sequence is 3, 1, ?" — hoping for a
decreasing `3 → 1 → 0` ("gauge theories of decreasing rank"). **This was already answered by V33 /
`physics_probes/SPECTRAL_CURVE_GATE1`:** the spectral-curve genus is **3, 1, ≥2** — `m=2` is a genus
**minimum**, not part of a decreasing family; the "decreasing rank" reading is **refuted** (and this is
the closed physics-probe thread). This stage reconfirms it exactly and **refines the m=3 bound**.

## The exact spectral genus (reconfirmed)

The spectral curve is the hyperelliptic double cover `w² = disc_L(M)` of the degree-2-in-`L`
A-polynomial:
- **m=1** (figure-eight): **genus 3** — branch `(M²−M−1)(M²−M+1)(M²+M−1)(M²+M+1)` (golden + 6th-root).
- **m=2** (m136, silver): **genus 1** — branch `(M²−2M−1)(M²+2M−1)`; `j=1728`, CM by `Z[i]` (forced + isolated).

## The m=3 refinement (NEW)

m=3 (`R³L³`) is degree-2 in `κ` (an irrational double cover). The **trace-relation curve `F_3(x,κ)`** is
the double cover `w² = disc3(x)` with
```
   disc3 = 5x⁴ − 10x³ − x² + 6x + 1 = (x² − x − 1)(5x² − 5x − 1)   (squarefree, two quadratics).
```
A squarefree **quartic** gives a **genus-1 (elliptic)** double cover — so the **m=3 trace-relation curve
`F_3` is genus 1, NOT genus ≥2.** This **refines V33/Gate1**, which argued "irrational → genus ≥2" — but
an irrational squarefree quartic is **genus 1**, not ≥2 (the "irrational" argument was too loose). The
**golden factor `x²−x−1`** appears in `disc3`, **shared with m=1's branch locus** — a small but real
structural link.

## Honest scope

The **spectral (M,L)** curve genus for m=3 — the direct analogue of the m=1,2 spectral genus 3, 1 —
needs the full m=3 `(M,L)` A-polynomial, whose elimination B69 flagged as **"too slow"**; it is a cover
of the genus-1 base `F_3`, so its genus is bounded below by the base (open, `computer-assisted-pending`).
**Settled either way:** the genus sequence does **not** decrease to 0 (`m=1` genus 3; `m=2` genus 1 is a
*minimum*); the m=3 trace-relation curve is genus 1. The handoff's hope (and the web's "3,1,0") is
refuted; this is curve geometry only.

## Reproduce

```bash
python frontier/B87_m3_genus/probe.py
python -m pytest tests/test_b87_m3_genus.py -q
```
