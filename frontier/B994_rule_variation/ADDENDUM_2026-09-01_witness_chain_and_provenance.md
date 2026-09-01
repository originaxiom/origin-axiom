# ADDENDUM (2026-09-01, fresh physics seat; finding for the banking seat to re-verify) — the exhibited chain `SU(3)^3 -> Pati-Salam -> SM` is not a chain of subgroups; two E51-class provenance gaps

**Scope.** This note corrects the path-dependence *witness* in `FINDINGS.md` lines 22–30 (the
six chains) and records two provenance gaps. It does not touch the endpoint claim, which
reproduces. The banked FINDINGS and `results.json` are left unedited, per house discipline;
nothing here is banked by this seat.

## 1. The endpoint claim reproduces (MATCH)

Reconstructing the menus from B861's committed `results.json` (step1 parent E₆: SO(10)×U(1) 46
✓, SU(6)×SU(2) 38 ✓, SU(3)³ 24 ✓, Sp(8) 36 ✗; step2 parent SO(10): SU(5)×U(1) 25 ✓,
Pati-Salam 21 ✓; step3 parent SU(5): SU(4)×U(1) 16 ✗, SM 12 ✓) and applying the step-k menu
positionally (whatever the parent) gives registerable-per-step [3,2,1], 6 chains, all ending at
SM, max-dim = first-listed, min-dim = last-listed — every banked number exactly
(`reports/fresh_physics_seat_2026-09-01/recompute/R27_b994_provenance/recompute_r27.py`).

Restatement note (R3_REPORT V19): given B861's menus, "endpoint is rule-independent" is exactly
`len(registerable at step 3) == 1`, i.e. B861's step-3 uniqueness restated. A planted positive
(make SU(4)×U(1) registerable → 12 chains, two endpoints) shows the check is not structurally
vacuous, only redundant with B861.

## 2. The witness is wrong (DISCREPANCY, R3_REPORT D10)

The alternative chain exhibited for path dependence, **`SU(3)^3 -> Pati-Salam -> SM`, is not a
chain of subgroups.** su(4) is simple of dimension 15 > 8 = dim su(3), so any homomorphism
su(4) → su(3)³ has nonzero kernel and, by simplicity, is zero; hence Pati-Salam
SU(4)×SU(2)×SU(2) ⊄ SU(3)³. Likewise SU(5)×U(1) ⊄ SU(3)³ (su(5), dim 24, simple, cannot inject
into the non-simple su(3)³). Exact check in
`recompute/R27_b994_provenance/embedding_check.txt`; the rank argument was also re-done by
hand by the seat. Two of the six banked chains are group-theoretically void.

Typed cause: **positional menu application** — the SO(10) menu was applied to the parents
SU(6)×SU(2) and SU(3)³, and the SU(5) menu to the parent Pati-Salam. Menus are keyed by parent
in B861; no menu for parents SU(6)×SU(2), SU(3)³ or Pati-Salam exists in any committed file.

What is still true: path-dependence *per se* — max-dim and min-dim rules choose different
step-1 subgroups (SO(10)×U(1) vs SU(3)³) — is genuine. Only the exhibited chain is the wrong
witness. Walking E₆ with the menus that actually exist gives 4 terminal paths with endpoints
{SM, Pati-Salam, SU(6)×SU(2), SU(3)³}: only the SO(10) → SU(5) branch reaches a level-3 menu.
B994's own quantifier ("menu arithmetic, not the manifold") is confirmed and is stronger than
stated: arithmetic over a positional list, not over the subgroup lattice.

## 3. Provenance (E51-class, R3_REPORT P2 and P3)

- **P2.** Menus for the parents SU(6)×SU(2), SU(3)³ and Pati-Salam — relied on implicitly by
  five of the six chains — exist in no committed file.
- **P3.** No generating script for this arc's `results.json` exists anywhere in the repo (grep
  for its keys hits only the results file; git history shows no deleted `.py`). The FINDINGS
  phrase "verbatim from the code" refers to B861's `fused_cascade.py`, not to a B994 generator.

Every menu *entry* B994 cites (the eight options with dims and registerability) does exist in
B861's `results.json` — no entry is prose-only.

## 4. Proposal (owner / banking-seat action, not taken here)

Rewrite the six-chain exhibit over the subgroup lattice with parent-keyed menus (which needs
B861 to commit the three missing menus, or a fresh cascade that computes them), and commit a
generator for `results.json`. Until then the arc's endpoint claim stands as banked and its
path-dependence exhibit should be read as "different step-1 choices", not as the printed chain.
