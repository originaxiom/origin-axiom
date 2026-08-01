# P5 Phase 0 — the claim-resolution table

cc banking seat, 2026-08-01. **The gate on everything else.** The outline asserts *"all THEOREM-tier,
banked, reproducers green"*; this resolves that claim row by row. **Rows that cannot be resolved do
not enter the paper.**

## Result: the premise holds, with two qualifications

| # | claim | arc | reproducer | lock | state |
|---|---|---|---|---|---|
| 1 | four-strata classification (Hopf × det, κ-laws, witnesses) | **B497** | `verify_monoid.py` | `test_b497_monoid.py` | **green** |
| 2 | U1/U2 — κ = 2 conserved, toral floor | **B497** (+B160–B165) | `verify_monoid.py` | `test_b497_monoid.py` | **green** |
| 3 | drift ledger: `E[log mult_D] = −2` (Fourier), `E[log mult_M] = 0` (convex) | **B498** | `c3_orbits.py` | `test_b498_mixed.py` | **green** |
| 4 | singular-verb dichotomy — BS(1,2) vs atoroidal/Mutanguha | **B497** (Q3 exact), **B524** (hyperbolicity) | `phase23_run.py` | `test_b497_monoid.py` | **green**, one caveat → Phase 1 |
| 5 | measurement algebra at its level (U2-toral, φ(a),φ(b)) | **B497** | `verify_monoid.py` | `test_b497_monoid.py` | **green** |
| 6 | monopoly death + wild S₄ + classical-floor torsion factory det(N±I) | **B498** | `q2_depth3.py` | `test_b498_mixed.py` | **green** |
| 7 | Q1b reduction lemma | **B498**, B507 | `q2_depth3.py` | `test_b498_mixed.py` | **green** |

**18 locks pass** (`test_b497_monoid.py` + `test_b498_mixed.py`). `verify_monoid.py` runs green now:
`U2 classical floor toral … True`, `witnesses … True`, Fibonacci degree ledger
`[2,3,5,8,13,21,34,55]`, `F_p guard … True`. `c3_orbits.py` reproduces the drift table
(`F80/D20 → −5.26/−4.66` across two seeds; units-only → `+0.15/+0.07`).

## Qualification 1 — the naive keyword probe was wrong, and that is the lesson

A first probe for the outline's own phrases returned **`torsion factory`: 0 arcs, `U2-toral`: 0 arcs**
— which would have read as "not banked". **It was a phrasing artifact:** both live in B497/B498 under
different words. **A claim table built by grepping the outline's vocabulary would have deleted two
true rows.** Resolution was done by reading.

## Qualification 2 — two arcs carry no reproducer

**B505** (`quasicrystal_anchor`) and **B507** (`beta_function`) hold **no scripts**. Neither is
load-bearing for the seven rows above — every row resolves to B497 or B498 — but the outline's
"anchor" language should not imply they are.

## What Phase 0 changes about the paper

Nothing is deleted. **The premise survives contact**, which is worth stating precisely because this
session's dominant error was accepting exactly this kind of inherited "all banked, all green" claim
without decomposing it. Here it decomposed cleanly.
