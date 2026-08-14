# GATE 8R2 — PARENT LOCALISATION AT THE GROUND STATE (sealed before compute)

Prereg for a **second, independent calibration control** on the B788 Gates 0–9R Maass bank.
Origin: Chat-1 (relay 2026-07-28). Arithmetic independently verified by cc (`weyl_budget.py`).
Gate 5 + Gate 5-Q binding. **Nothing from this gate reaches CLAIMS.md.**

## Why a second control is needed

B788's entire external calibration currently rests on **one number**: `DCHY2025_EIS_ODD_24_5033`
(de Clerck–Hartnoll–Yang 2025), ε ≈ 24.5033, printed to **4 decimals**, marked "approximately",
read from a **Figure 4 caption**. Gate 8R's celebrated 10-digit agreement is **between two
heights** (y₀ = 0.45, 0.52) — internal solver consistency, which is the correct Hejhal
certification but says nothing about whether the solver targets the right object. Two heights at
one r **cannot** pin truncation, because they share the target.

This matters concretely: **Gate 8 died on truncation**, and Bessel truncation is strongly
r-dependent. The mode budget at r = 24.5 is **3.465×** that at r = 7.07 (verified). A solver
tuned at the high point can still be wrong at the low one.

## The second point (verified, not cited)

Grunewald–Huntebrinker 1996 Table 3 gives the parent ground state λ₁ = 51.014, hence

    r = sqrt(51.014 - 1) = 7.072057692

Three independent corroborations:

| check | value | reading |
|---|---|---|
| Weyl prediction W(T) = 1 | r = 7.047802574 | **0.344 %** from the G–H value |
| W(7.0721) | **1.01036** | it *is* the ground state ⇒ λ₁(m004) ≤ 51.014 is likely **tight on V₁** |
| W(24.5033) | 42.0255 | the existing control sits **mid-spectrum**; this one is the opposite end |

Different **source** (G–H 1996 vs DCHY 2025), different **spectral position** (W ≈ 1 vs W ≈ 42),
and cheaper than the existing control. This is what removes a single point of failure; a second
height at the same r cannot.

## The gate (two-outcome, pre-stated)

> **GATE-8R2 PARENT LOCALISATION.** Run the V₁ solver on r ∈ [6.5, 7.6] at **two heights**.
> **PASS** if exactly one confirmed root lies in **7.072 ± 0.005**.
> **FAIL** if none is found, if more than one is found, or if the root lies outside the window.
> **No precision claim is made or banked from this gate.**

## Framing: localisation, NOT precision — binding

G–H published ~3 significant digits and caveat that the last digit is untrustworthy. So the
target is **weak as a target and strong as a falsifier**:

- A pass localises the ground state and demonstrates the solver is correct at the *low*-r end
  where truncation is least forgiving. It does **not** validate any digit beyond the third.
- A fail is decisive: it exposes an r-dependent truncation defect **before** the ≈2-day Gate 9
  re-run is committed.
- The ±0.005 window is set by the source's own precision, not by what the solver can resolve.
  **Tightening it after seeing the answer is forbidden by this prereg.**

## Provenance caveat, carried forward

The value 51.014 reached cc through a **secondary report** of Table 3, not from cc reading the
primary in-sandbox. It is marked UNVERIFIED in `B790/compute_screening.py` and remains so here.
**Before this gate is executed, the number must be checked against the primary source.** The
Weyl cross-check at 0.344 % is corroboration, not verification — the two are independent, and a
transcription error of the right size would survive it.

## Sequence (as relayed, adopted)

1. Bank the Weyl criterion (this arc, B791). ✅
2. **Gate 8R2 localisation at r ≈ 7.07** — cheap, and may expose a truncation defect before
   two days are spent.
3. Gate 9 re-run on the widened interval [0.5, 15.5] with W(T) as the completeness gate and a
   **budget-derived** screen cap replacing the hand-set `maximum_minima_per_sector = 24`.

— cc, 2026-07-28
