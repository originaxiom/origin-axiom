# B1745 — THE WEB SEAT'S FRAME LOCKS, ON MAIN (P-358): ALL SEVEN OF THE_NEXT_ATTACK'S LOCKS ON B1656'S FRAME HOLD ON MAIN'S OWN CODE — THE CANONICAL MATRIX (EXACT), ∣V_cb∣ = ∣κ_u − κ_d∣ UNDER THE NULL HIGGS (0.44% MEDIAN), THE UP CHANNEL'S EXACT ZEROS, THE CUSP COEFFICIENTS; WITH B1742–B1744 FOR THE OTHER FOUR

**Verdict: PROVED (a verification on main of a seat's data-free locks).** cc (main), 2026-10-24. No data compared.
**0 of 19.**

## 1. What was checked

The web seat's THE_NEXT_ATTACK (relay row in RELAY_LEDGER; harvest rows 1350–1352) banks the frame's mixing structure as
seven locks (its `frame_lock.py`, all holding on its code). Main's verification, on B1740's instrument via B1742's
`repro.py` and B1736's closed form Y = u hᵀ + h uᵀ − (u·h)1 + w[h]_× (h₀ = 0), in ρ(T)'s eigenframe f₁ = n̄, f₂ = e₁,
f₃ = n:

| lock | statement | where verified on main | result |
|---|---|---|---|
| K1 | F†YF is the seat's canonical matrix, linear in δ, ε (h = f₃ + δf₂ + εf₁, u = a₃f₃ + a₂f₂ + a₁f₁) | here (sympy) | exact: the difference simplifies to the zero matrix |
| K2 | det Y = (h·h)(u·h)(u·u + w²) | B1744 §2 D | exact, with the scalar component (h₀² + h·h)(w² + u·u)(h₀w + u·h) |
| K3 | under the null Higgs n, ∣V_cb∣ = ∣κ_u − κ_d∣, κ_s = [(a₂ − iw)·conj(2a₃) − a₁·conj(a₂ + iw)]/(4∣a₃∣² + ∣a₂ + iw∣²) | here, 192 rows of B1742's grid | median relative error 0.44%, largest 1.6% (the seat: 0.35%, 1.8%), with w = +u₁ in coupling()'s own index order; with w = −u₁ it errs by 71× (median) — the control |
| K4 | the up channel: u₁ = 0 on the order-5 lines, a₂ = 0 on the order-10 lines | here, 90 points | both 0.0 exactly; the other component stays ≥ 0.066 of ∣u∣ (non-vacuous) |
| K5 | the idealised up channel: m₁ = 0, m₂m₃ = ∣a₃∣²∣h·h∣, m₂/m₃ ≥ ∣h·h∣/4 | B1743 §3 | holds (1.1 × 10⁻¹⁵; the bound's minimum ratio 1.009) |
| K6 | the leptons as the down quarks on the ten lines | B1742 §3 | found independently (k even: any Higgs; k odd: no QI component) |
| K7 | the cusp coefficients: R δ/r^½ = 2√2, ε/r = 4; ∂R 4√2, 20 | here, at 0.3 + 3.5i and 4.0i | 2.8284, 4.0000; 5.6569, 20.000 |

The sign of w: B1736 part D writes the antisymmetric term as −u₁[h]_× after permuting coupling()'s index order (j, i, k)
to (i, j, k); a transposition of two indices flips the cross product, so in coupling()'s own order w = +u₁ — which is what
K3 finds.

## 2. Read with it (the seat's, not re-derived on main)

- **READING PRE-SCAN 2** (data-free, all 266 lines at two points, both horocycles; 1 064 rows): Lemma A holds exactly on
  every row, and under the Standard Model's reading (up sees h̄, down sees h) no row has a Higgs direction giving the
  coarse pattern (an up hierarchy, a down hierarchy and a CKM near the identity) — zero rows at every line order.
- **The heavy states** (`exploration/e8_heavy_states.py`): on the rows with an up hierarchy and ∣V_ud∣ > 0.9 under that
  reading, the heaviest up state is nearly null and the heaviest down nearly real, so ∣V_tb∣ ≈ 0.1 (largest 0.35) — the
  2-3 exchange that B1735's and B1741's CKM shows.
- **SEARCH CHECK**: the seat's ℂP² search finds planted directions (to 10⁻²¹) and, on the data, never goes below
  χ²_nine 1 027.7 under that reading (∣V_cb∣ about 24 times measured). The sealed global version is the seat's own next
  test (its step 2); main does not duplicate it.

## 3. What it means

The frame's mixing structure — which part of each sector's matrix carries the light states, the 2-3 tilt as a rational
function of the channels, the determinant — is now verified on two codes. With B1743–B1744: the CKM's 2-3 entry is the
channels' (V_cb = ∣κ_u − κ_d∣ at the null limit), the first generation and the Cabibbo angle are the Higgs's departures
from the null cone (K1's first row and last column, det Y), and under the Standard Model's reading the pattern itself is
out of reach on the record's points (the seat's pre-scan, to be sealed).

## Seen first

`VERDICT topic-sweep /canonical matrix|kappa_u|κ_u|V_cb = |frame lock|eigenframe|exact zeros/ (full text): 15 of 1517 arcs on main match (NEGATIVE 1, PROVED 14)`. Bearing on it: B1736, B1742–B1744, B1691; the seat's THE_NEXT_ATTACK and its `frame_lock.json` (read before this check). **Literature:** standard (unitary frames; the SVD).

## Files

- `verification/frame_locks.py` → `frame_locks.json`, `frame_locks_run.txt` (first run in the audit room,
  `audit/verify_p358/`, and rerun here).
- The lock: `tests/test_b1745_the_frame_locks_on_main.py`.
