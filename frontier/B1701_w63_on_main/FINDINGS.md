# B1701 — W63 ON MAIN (P-246): THE SM SEAT'S W63 REPRODUCED ON MAIN'S OWN TRIPLET; AND WITH THE HIGGS'S DIRECTION TIED TO THE LINE AS W63 TIES IT, EVERY SECTOR'S SPECTRUM IS EXACTLY 0 : 1 : 1 — ON ALL 27 LINES, EVERY τ, BOTH ENDS — SO THE LINE-TIED HIGGS GIVES NO HIERARCHY AT ALL

**Verdict: PROVED (computed; no data).** cc (main), 2026-10-22. P-246 (B1697 item 2): verify W63 on main and redo the
one-line work with the Higgs's direction tied to the line. 0 of 19.
- **(a) W63's cells, on main's triplet** (B1691's R; B1645's Y(a) = a Rᵀ + R aᵀ − (a·R) 1; `verification/w63_on_main.py`):
  at i, 1.5 i, 2.0207 i, 4 i, ω and six seeded points, over 2 000 real directions min m = ½ (to 2.7 × 10⁻⁷, the sphere's
  resolution; never below) and max m < 1;
  m(e_k) = ½ on the imaginary axis; every unit gives 0.565741 at ω (W63's 0.566); isotropic directions give m = 0;
  R·R = 0. W63's verification of B1644 and B1645 stands on main; its claim "the record's Higgs at a line has one real
  unit direction" (p + 3w ≡ 0 has at most one solution among the half-periods) is the half-period arithmetic, checked.
- **(b) The tie at the line, in the frame that sees the line.** W63 combined the tie with the untwisted coupling. On the
  line itself — B1656's twisted four-channel coupling at B1667's canonical end — the tied Higgs (the unit C_{p*},
  p* ≡ −3w, W61's blocks) was computed on **every line with 6w in the lattice and p* a half-period: 27 lines** (nine per
  unit), Re τ ∈ {0, ½}, Im τ = 1.0–4.0, both horocycles, all three sectors and B1660's three up readings (864 rows):
  **m₂/m₃ = 1 to 9 × 10⁻¹⁶ and m₁/m₃ = 0 to 2.4 × 10⁻¹⁶ on every row** — the spectrum is exactly 0 : 1 : 1.
- **(c) The control.** On the same lines the two untied units never degenerate (108 points: ∣m₂/m₃ − 1∣ ≥ 0.080,
  m₁/m₃ ≥ 2.6 × 10⁻⁴); without a line B1656's frame reproduces B1645's values (e.g. at 2 i, large L: 0.885, 0.505, 0.500
  for i, j, k).
- **What it means.** In B1658's terms each sector's spectrum is (1, t, 0); the line-tied Higgs sits exactly at t = 1 — the
  twisted form of B1645's T4 (a Higgs normal to the residue's plane gives (1, 1, 0); B1657 at ω). So W63's "0 : 1 : 2 on
  the axis" holds for the untwisted coupling only; on the line it is 0 : 1 : 1. **The one-line fits with the direction
  tied to the line need no fitting: no τ, end or reading gives any second-to-third hierarchy.** The state W60 and W62
  single out (the half-period lines, where one parity copy of the Higgs is untwisted; B1686) therefore gives degenerate
  heavy pairs in every sector. The hierarchy needs a Higgs that the line does not tie — the covariant ∂R, complex and
  carrying the cusp's unit (B1700).
- **What it does not do.** The mechanism of the exact degeneracy is not derived here (computed to machine precision; a
  symmetry of the untwisted copy is the natural candidate); lines with p* = 0 carry no adjoint copy and are excluded; no
  data.

## 0. Seen first

`VERDICT topic-sweep /W63|parity copy|untwisted copy|p ?\+ ?3w|0 ?: ?1 ?: ?1|degenerate (pair|heavy)|half bound/ (full text): 9 of 1473 arcs on main match (NEGATIVE 1, PROVED 8)` —
B1644, B1645 (the half bound; T4's (1, 1, 0)), B1657 (a Higgs on n at ω gives (1, 1, 0)), B1658 (the twisted spectrum
(1, t, 0)), B1686 (W60's half-period lines, one parity copy untwisted), B1697. None computes the tied Higgs on the line
in the twisted frame. **Literature:** none beyond the cited arcs.

## 1. Files

- `verification/w63_on_main.py` → `w63_on_main.json`, `w63_run.txt`; `verification/b1656_funcs.py` (B1656's functions,
  verbatim).
- The lock: `tests/test_b1701_w63_on_main.py`.
