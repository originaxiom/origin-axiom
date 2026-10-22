# B1710 — W121'S INDEX LAW ON MAIN (P-255): ON A CLOSED ELLIPTIC SURFACE WITH 12χ(O_S) STRINGS THE TRIPLET'S COUNT IS −15χ(O_S) (ρ_T) AND −18χ(O_S) (ρ̄_T) — −30 AND −36 ON K3 — AND NEVER THREE

**Verdict: PROVED (verified on main, given the seat's reduction; no data).** cc (main), 2026-10-22. P-255 (B1708 verified
W121's lifts only). 0 of 19.
- **The exponents, computed** (`verification/the_index_law.py`, ρ_T built from its definition as in B1708): ρ_T(T) has
  exponents **⅛, ⅜, ⅞ (sum 11/8)**, its conjugate **⅛, ⅝, ⅞ (sum 13/8)**; none is an integer, so the natural conditions
  at a string coincide with Deligne's canonical extension (no freedom).
- **The count** (W121's Riemann–Roch on the base, with deg K_C = 2g − 2, deg L = χ(O_S), N = 12χ(O_S) strings, the
  canonical extension at each): index = 3·deg((K_C ⊗ L)^½) − N·Σμ + 3(1 − g) = (3/2)χ(O_S) − 12χ(O_S)·Σμ. Exactly, for
  χ = 1 … 6 and g = 0 … 3: **−15χ(O_S) and −18χ(O_S); the genus cancels in every case; on K3 the canonical extensions
  have degree −33 and −39 and the index is −30 and −36; no case gives ±3.**
- **What rests on the seat.** The reduction of the four-dimensional twisted Dirac index on S to this Riemann–Roch number
  on the base (Leray; the operator W45's, carried over) is W121's reading and is not re-derived here. Given it, W121's law
  holds on main.
- **What it means** (with B1708): on the closed torus-fibred 4d vacua the forced strings overshoot — each lowers the count
  by 11/8 or 13/8 — and no closed solution of this kind gives a chiral three with the natural conditions. Three stays one
  unit at the weave's own cusp, FK10's tagged datum (P-254).

## 0. Seen first

`VERDICT topic-sweep /Riemann.Roch|canonical extension|Deligne|elliptic surface|index law|chi\(O_S\)|χ\(O_S\)/ (full text): 15 of 1482 arcs on main match (NEGATIVE 4, OPEN 2, PROVED 9)` — B1700, B1708 (the
lifts; the twelves), B1641 (W46's index on M₁,₂). **Literature:** Riemann–Roch for flat bundles with Deligne's canonical
extension, as context.

## 1. Files

- `verification/the_index_law.py` → `the_index_law.json`, `the_index_law_run.txt`.
- The lock: `tests/test_b1710_w121s_index_law_on_main.py`.
