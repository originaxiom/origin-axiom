# B607 — the charge table: the odd sector is charge-mixed except at the two spinor tips

**Status: banked (frontier). Nothing to `CLAIMS.md`; no SM quantities —
this is the math-tier bicharge census registered as B604's follow-on
lead (subsystem/coset framing; any gauge/matter reading stays
firewalled as interpretation). Lock `tests/test_b607_charge_table.py`
(OA_SLOW). Run: `OA_SLOW=1 python3 charge_table.py`.**

## The census (exact; charges are simple-root coefficients ⟨α, ω∨⟩)

Each odd-block line expanded exactly in the θ-odd pair-combination basis
(the B604 machinery), each contribution labeled by its (n_endP, n_endQ)
bicharge — the pair of U(1)-charges under E₆ ⊃ D₅ × U(1) for the two end
choices:

- **22 of the 24 non-Cartan lines are MIXED**: every V(m=4) line and
  every interior V(m=8) line touches both coset classes (0,1) and (1,0)
  (16-content under either end choice); the D₅∩θD₅ core class (0,0)
  joins at |wt| ≤ 6. The two Cartan zeros mix the dual directions.
- **The ONLY pure lines: V(m=8)'s extremal tips wt = ±16, bicharge
  (1,1)** — built on the unique height-8 (16,16) pair: double-spinor
  content under both end choices. These are the only G_SM-gradable
  lines in the entire θ-odd sector.
- The h = 4 expansion coefficients reproduce B604's banked values
  (−443520, −604800) — cross-checked in the lock.

## What it settles

Chat-1's Rosetta question closes in its final quantitative form: the
θ-odd (hearing) sector admits NO subsystem/coset grading anywhere except
the two extremal spinor tips. Under the firewalled gauge/matter reading
this says: the chirality directions are gauge-matter superpositions at
every principal depth, with exactly one exception — the deepest string
vectors are pure double-spinor. Any future SM-facing reading must treat
the two torsions as labels of MIXED lines, and the (1,1) tips are the
unique candidates for a sector-pure anchor.
