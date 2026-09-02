# R50 — B775 (audit/b775-braver-questions) V4 genericity table: the table is right, the committed script is broken

**Claim (FINDINGS_THREE_MOVES.md, Move 1; unrecomputed row #553):** of 8 manifolds with imaginary quadratic trace
field, m004, m003, m025 and R²L² are amphicheiral (V4 = Galois × geometric involution) while m009, m010, RRL, RLL carry
the Galois ℤ/2 only.

**Phase C agent rerun of `v4_genericity_test.py`:** "V4 present: 0; Galois only: 8", m004 itself reported as NOT
amphicheiral, m025 not in the tested list — i.e. the script contradicts the table. Seat's reading of the script: its
`get_symmetry_info()` wraps `symmetry_group()` in a try/except and returns `order: None` on any exception; the line
`hasattr(sym.symmetries()[0], 'extends_to_link')` raises on this SnapPy, so every manifold falls into the except branch
and is then classified "not amphicheiral". The committed script therefore reports a false negative for all 21 inputs
on this bench (the same class of instrument failure B1165 flagged for `isometry_signature`).

**Seat's direct check (SnapPy 3.3.2, `symmetry_group().is_amphicheiral()` + R33 shape fields):**

| manifold | vol | Sym order | amphicheiral | shape field |
|---|---|---|---|---|
| m004 | 2.029883 | 8 | True | x²−x+1 (ℚ(√−3)) |
| m003 | 2.029883 | 8 | True | x²−x+1 |
| m025 | 3.044825 | 6 | True | (algdep did not converge here; table says ℚ(√−3), vol = 3/2·vol(m004) is consistent) |
| R²L² (b++RRLL) | 3.663862 | 8 | True | x²+1 (ℚ(i)) |
| m009 | 2.666745 | 4 | False | x²−x+2 (ℚ(√−7)) |
| m010 | 2.666745 | 4 | False | x²−x+2 |
| RRL / RLL | 2.666745 | 4 | False | x²−x+2 |

**Verdict: the banked table REPRODUCES (8/8) by direct computation; the committed script does not (fragile diagnostics).**
B775's Move-1 conclusion ("V4 is not generic; amphicheirality is a special property; m004's V4 is shared by m003,
m025, R²L² within the class") stands. Fix for the arc: drop the `symmetries()[0]` probe or guard it separately.
