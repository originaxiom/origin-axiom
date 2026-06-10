# B151 — firewall confirmation (L15): does any quantity carry a SCALE across the L14 bridge?

**Question.** L14 (B150) made the bridge real (the unit's SL(2,ℤ) symmetry IS the N=2\* duality action). L15 tests the
firewall hardest: in the 3d–3d correspondence applied to the figure-eight, does the complex volume / CS invariant enter
the partition function **only as a dimensionless exponent**, with all dimensionful content in `ℏ↔k` + the squashing
radius and **none** in the invariant? A **reading** task (how the sources assign units), not a sandbox verdict.

**Answer — FIREWALL HOLDS (decisively).** All three primary sources locate the units in `ℏ/k` + the squashing/lens
geometry, never in the invariant:
- **GTZ (1111.2828):** `ĉ(ρ)=i(Vol+iCS) ∈ ℂ/4π²ℤ` — a dimensionless element of a quotient of ℂ by a lattice.
- **Dimofte (1409.0857):** complex CS *at level k*; state-integral on squashed lens spaces `L(k,1)`; `Vol_C` is the
  fixed exponent saddle — units in `k↔ℏ` + geometry.
- **Córdova–Jafferis (1305.2891):** "a squashing parameter controls the imaginary part of the complex CS level" — units
  in `b` + the level.

**Anchor (computed):** figure-eight `Vol = 2.0298832128` (= 2·V_tet), **CS = 0** (amphichiral). Pre-strengthening: CS is
the candidate scale-carrier and it vanishes for the unit, so its complex volume is purely the real hyperbolic volume — no
CS content to carry anything; the unit is the *least* likely object to carry a scale.

**Boundary.** No κ-type / volume-type invariant of the unit can source a physical scale. The unification is a **symmetry
identity (L14)** and **terminates at the firewall (L15)**. Real bridge + confirmed wall = the honest boundary of the
one-object picture; the cosmological-constant question lies on the far side. **A real result, not a failure** — and **not**
a scale-crossing (the blade: a symmetry is not a scale; "the partition function has units" is not a crossing).

**Files.** `probe.py` (anchor via SnapPy + per-source reading + verdict), `FINDINGS.md`,
`../../tests/test_b151_firewall_confirmation.py` (5 passed: anchor + reading honesty structure — no CROSSING without
exhibited primary text).

**Run.** `python -m pytest tests/test_b151_firewall_confirmation.py -q` (pyenv).

Ledger **V140**. Anchors: B150 (L14 bridge), B148 (the unit), K006, STRATEGIC_SYNTHESIS §8. External: 1111.2828,
1409.0857, 1305.2891.
