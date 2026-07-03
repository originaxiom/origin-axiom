# B377 (D0+D1) — the existence law DERIVED: (line) ⊗ (doublet), odd prime powers, parity on the ramified side

**Status: banked (frontier). The law is DERIVED from exact local censuses and verified against all
six banked level verdicts (five sectors + the census-confirmed 225 death); its three fresh rung
predictions (below) are the acceptance test before any promotion — derive-don't-fit governs.
Substance from a relayed mechanism note was verified and CORRECTED before use (convention offset
in the multiplier parametrization; the "prime-square" reading refined to odd/even parity by OUR
27-census). Campaign D0/D1. Firewalled.**

## D0 — the 225 verdict (the registered-while-running prediction HIT)

The full-multiplicity module-closure census at 225 found **no invariant 2-dim module in any
multiplicity class** (`full_census_225.json`; the prediction in `PREDICTION_BEFORE_CENSUS.md`
was registered while the census was executing). The death is real, and derived below.

## The complete local table (exact, F_p; `local_censuses.json`)

Levels q with theta-model (D_u, WR_u): lines (1-dim invariant) and helicity doublets:
3: line ✓, doublet 90° · 5: NO line, doublet 36°(u QR)/108°(u non-QR) · 9: line, no doublet ·
25: line, no doublet · 27: line, doublet 90° · 81: line, no doublet · 125: NO line, doublet 36°.
Verified against the relayed P-F claim (no 5-line ✓) and the σ_√5 Galois-transport mechanism
(the u=1/u=2 pair at level 5 are exact σ-conjugates with swapped angles ✓).

## The v2 law (derived; uniqueness from line-absence where it bites)

**Doublets exist at ODD prime powers only** (3-side: 3, 27 — both 90°; ramified 5-side: 5, 125 —
angle by the σ-class of the local multiplier). **Lines: always on the inert 3-side; on the
ramified 5-side at EVEN powers only.** The tensor factorization of the level-N theta model into
local models is exact with multipliers from the CRT expansion (at 15: (u₃,u₅) = (2,2) — verified
entrywise; the relayed note's u-values differ by a parametrization convention, same QR-class
sequence). The 5-side multiplier tower: u₅(15·3^k) has QR classes N, R, N, R for k = 0..3.

**Sector@N = any available (local line) ⊗ (local doublet) pairing; phase = the doublet side.**
Derivations against the banked rungs, all exact:
- 15 = 3·5: 5-line absent ⇒ unique pairing (3-line)⊗(5-doublet), class N ⇒ 108° ✓
- 45 = 9·5: (9-line)⊗(5-doublet), class R ⇒ 36° ✓
- 75 = 3·25: 25-doublet absent ⇒ (3-doublet)⊗(25-line) ⇒ 90° ✓ (the mystery angle, explained)
- 135 = 27·5: (27-line)⊗(5-doublet), class N ⇒ 108° ✓ (the 27-doublet pairing is blocked by
  the missing 5-line — uniqueness preserved)
- 225 = 9·25: no doublet on either side ⇒ NONE ✓ (census-confirmed above)

## The acceptance predictions (registered BEFORE the rungs run)

- **375 = 3·125 → unique sector at 108°** ((3-line)⊗(125-doublet); u₁₂₅(375) = 42, class N ⇒
  σ-conjugated 36° → 108°). The earlier "90°, gated on the 125 census" branch is dead (no 125-line).
- **405 = 81·5 → 36°** ((81-line)⊗(5-doublet), u₅(405) = 1, class R). Now derived twice over.
- **675 = 27·25 → EXISTS at 90°** ((27-doublet)⊗(25-line)) — **REVERSING** the earlier naive
  "none" registration: the odd-power 27-doublet flips the verdict. The sharpest falsification
  duel on the board: the naive law says dead, the v2 law says 90°.
KILLS: any rung deviating (wrong phase, wrong existence, non-uniqueness) kills the v2 law as
stated. Promotion of the law is GATED on all three rungs passing.

**Provenance.** B372–B374 (the measured rungs), B376/P59 (the cat-map frame), the relayed
mechanism note (substance verified + corrected; conventions reconciled here). Reproducers:
`local_censuses.py`, `full_census_225.py`; locks: `tests/test_b377_existence_law.py`.
