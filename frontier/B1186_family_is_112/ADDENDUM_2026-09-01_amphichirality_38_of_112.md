# ADDENDUM (2026-09-01, fresh physics seat) — "amphichirality 112/112" is false; the true count is 38/112. Also: t06829 has 8 tetrahedra, not 7

**Scope.** Corrects line 44 ("Amphichirality strengthens a third time: 112/112 (14/14 → 83/83
→ 111/111 → 112/112)") and the t06829 tetrahedron count at line 25. The 112 enumeration itself,
the exact ℚ(√−3) certificate of t06829 (max shape denominator 98, next 49), the 3×Vol(m004)
volume, and the H₁ = ℤ non-separation at 112-scope all **reproduce** and stand (Ring R2 cell
R20, R2_REPORT). Original FINDINGS.md left unedited.

**The amphichirality chain 14/14 → 83/83 → 111/111 → 112/112 was one instrument repeated four
times**, `reverse_orientation()` + `is_isometric_to()`, which is orientation-blind in SnapPy
and returns `True` on every input. It "strengthened" only because the family grew. Recomputed
with `symmetry_group().is_amphicheiral()` over the committed 112 list:

- **38 amphichiral, 74 chiral.**
- Amphichiral members: CS mod ½ ∈ {0 (25 members), ¼ (13 members)} — B1224's 2-torsion law
  verified on every one.
- Chiral members: CS mod ½ takes nine further values (1/12, 1/8, 1/6, 5/24, 7/24, 1/3, 3/8,
  5/12, 11/24) and also 0 (22 members) and ¼ (16 members) — CS ∈ {0, ¼} is necessary, not
  sufficient, for amphichirality, as B1226 already showed on m208.
- Data: `reports/fresh_physics_seat_2026-09-01/recompute/R20_family_separator/seat_cs_h1_table.json`
  (name, amphichiral, H₁, CS mod ½, vol/V_Gieseking for all 112).

**Consequence for this arc's family statements.** "Every member is amphichiral" and any
"amphichirality is a family invariant" phrasing are **withdrawn**. What *is* family-wide and
verified: all shapes in ℚ(√−3); volume an integer multiple of the Gieseking volume;
commensurability class. What is a 38-member sub-property: amphichirality. What is m004's
alone among the 14 and 21 but not among the 112: H₁ = ℤ (o10_150700: H₁ = ℤ, ten regular
ideal tetrahedra, chiral, CS = −1/12, symmetry group ℤ/2, not a cover of m004 or of m000 —
`seat_spotcheck_d5.txt`).

**t06829** has **8** ideal tetrahedra in the census triangulation (`num_tetrahedra()`), not 7;
the exact certificate and the 2-cusp / 3×volume facts are unaffected.

Ledger: R2_REPORT D5, D6 (typo note), V9. Error-class E27/E40 (instrument that cannot fail) →
E53 (propagated as a strengthening).
