# B187 — the open / interacting many-body collective: the thresholdless arrow survives interactions

**Date:** 2026-06-22. **Status:** Masterplan III, **Track B** (first of two). Extends B183 (the single-particle
open metallic chain) to the **interacting** many-body case S036 named as still open. **Computed, not deferred**
(exact diagonalization of a few fermions). **Result:** B183's thresholdless arrow **persists with interactions** —
a two-body interaction `U` opens **no** protective gap for the permanently-critical metallic collective.
**Firewall-side:** emergent condensed-matter many-body math (`K010` boundary, *not* fundamental); no scale/Λ;
**nothing to `../../CLAIMS.md`**; P1–P16 frozen. Ledger V181. Reproducer `interacting_open.py` (`ALL CHECKS PASS`).

## The setup and the question

B183 (single particle): the open metallic chain (Hatano–Nelson imaginary gauge field) has a **thresholdless**
real→complex (point-gap) transition `g_c = min` Lyapunov `≈ 0`, because the object is permanently critical (B181) —
a *genuine but externally-sourced, dimensionless* arrow. The genuinely-open piece S036 named is the **interacting**
collective. We diagonalize spinless fermions (`n` particles on `L` sites, PBC) with Hatano–Nelson hopping
`e^{±g}` + the metallic Sturmian onsite potential + a nearest-neighbour interaction `U`, and ask: **does `U` open a
protective gap (`g_c(U)>0`), or does criticality keep the arrow thresholdless?**

## The result (`L=14`, 2 fermions; robust across `L=10–16`, 2–3 particles)

| `U` | metallic `g_c` | AA-localized `g_c` |
|---|---|---|
| 0.0 | 0.035 | 1.27 |
| 0.5 | 0.006 | 0.91 |
| 1.0 | 0.001 | 0.82 |
| 2.0 | 0.003 | 0.87 |
| 4.0 | 0.0002 | 0.86 |

- **C1 — the metallic many-body arrow is THRESHOLDLESS at all `U`.** `g_c(U) ≈ 0` across `U=0…4` — interaction opens
  *no* protective gap; the open critical collective gains a complex (irreversible) many-body spectrum under the
  slightest drive, with or without interaction. (If anything, `U` makes it slightly *more* fragile.)
- **C2 — a localized control IS protected at all `U`.** The Aubry–André localized chain keeps a real many-body
  spectrum up to a **finite** `g_c ≈ 0.7–1.4` for every `U` — protection is a localization property, not
  added/removed by `U`; the metallic case is `>10×` more fragile.
- **C3 — robust.** The metallic-thresholdless / localized-protected split holds across system size and particle
  number (`L=10,12,16`; 2–3 fermions).
- **C4 — FIREWALL.** The arrow is genuine (a complex many-body spectrum = non-unitary, irreversible) but `g_c` is
  **dimensionless** (hopping units) and the arrow's **source is the externally-imposed openness** (the imaginary
  gauge field is *input*) — not self-generated. So the interacting open collective adds **no scale** and **no
  self-generated arrow**; it extends B183's verdict to the many-body case.

## What this means for the search (S036)

The **open/interacting** channel — the one B183 explicitly left open — is now **computed**: interaction does not
change the verdict. The permanently-critical metallic collective stays thresholdlessly driven to irreversibility
under an open coupling, *with* interactions; the threshold is dimensionless and the arrow externally sourced, so the
firewall holds. This is the many-body confirmation of B183's "criticality = maximal fragility to the arrow." The
register's **ARROW** ingredient stays "emergent in the open collective, thresholdless, dimensionless, externally
sourced" — now established for the interacting case too.

## Scope / honesty
- Few-body **exact diagonalization** (2–3 fermions, `L≤16`) — the threshold/protection split is robust at this scale.
  The genuinely-interacting **thermodynamic-N** regime (large-N driven-dissipative / many-body-localization phases)
  is the residual **NEEDS-SPECIALIST** (ED caps at small N).
- The PBC fermion boundary sign is simplified; it shifts individual eigenvalues but not the real→complex point-gap
  threshold (= the many-body min Lyapunov), which is the measured quantity.
- Emergent condensed-matter many-body mathematics (`K010` boundary); no physical-magnitude claim; nothing to
  `../../CLAIMS.md`; P1–P16 untouched.

## Anchors
`B183_open_collective_arrow` (the single-particle thresholdless arrow this extends), `B181_criticality_scale`
(permanent criticality — the cause), `B186` (the same trace-map/criticality lineage), `speculations/S036` (the ARROW
ingredient; the open/interacting channel). External: Hatano–Nelson (imaginary gauge field, point-gap / skin effect);
non-Hermitian many-body / interacting topological spectra; many-body localization under non-Hermiticity (the
thermodynamic-N residual).

## Reproduction
`python frontier/B187_interacting_open_collective/interacting_open.py` — C1 metallic thresholdless at all `U`;
C2 the localized control protected at all `U`; C3 robustness over `L`/particle number; C4 the firewall verdict.
Prints `ALL CHECKS PASS`. Fast locks in `tests/test_b187_interacting_open_collective.py` (2 tests, ~0.6s).
