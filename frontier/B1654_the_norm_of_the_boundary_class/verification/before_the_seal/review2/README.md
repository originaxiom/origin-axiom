# The second pre-seal review of B1654 (read-only, 2026-10-15)

A second read-only reviewing agent checked the revision against the first draft (`../../../design_v1/`) and the first
pass's findings. It found no decisive or major defect and verified every fix: N4(a) with λ = (1, 2, 1) (|shift|/|R|²
≥ 1.45 at all six points, its sign exact); the atan2 angle; K = 24; N5(c)'s four near-corner nodes and the [1.8, 3.4]
window; N2b's direct D at 15 non-named τ (≤ 2.6e-14); N5(d)'s constant K = 8π(1 − 4 ln 2) by hand and its remainder at
Im τ = 4.5 and 5.5; N0's channel check (not tautological: swapping R's keys 2↔4 fails except at τ = i). Its smaller
findings (boolean flags, output paths, this provenance, and text) were applied before the seal; its blindness ledger is
in the preregistration's §0b. Scripts t01–t16, pre2.py and blocks.py; pre2.py execs the instrument's functions only.
