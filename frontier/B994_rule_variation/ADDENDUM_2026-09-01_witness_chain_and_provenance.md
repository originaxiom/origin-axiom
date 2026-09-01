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

## 5. CORRECTION (2026-09-01, later the same day; owner's rule "before you conclude we don't have something, sweep the repo first")

The absence claim in §2 l.34 and §3 P2 — *"no menu for parents SU(6)×SU(2), SU(3)³ or
Pati-Salam exists in any committed file"* — was made before a full-repo sweep and is **wrong as
stated**. The sweep (`reports/fresh_physics_seat_2026-09-01/sweeps/sweep_absence.sh
'pati.?salam' 'pati'`, all seven remote heads + deleted-file history) finds:

- **No committed *output*** keys a menu by those three parents. B869's `results.json` visits
  neither `su(2)+su(6)`, `su(3)+su(3)+su(3)` nor `su(2)+su(2)+su(4)+u(1)` (its cascade goes
  through the SO(10) winner), and B873's completed menus are keyed E₆ / SO(10) / SU(5) only.
- **Committed *code* generates them.** `frontier/B869_false_positive_control/
  false_positive_control.py` (on main) descends *any* su/so state (`all_descents`:
  maximal-rank su(n)→su(k)×su(m)×u(1), strip-su(2), and the `SO_MENUS` table incl. the
  Pati-Salam branching of 16/10/1). Running that engine unmodified on the three parent states
  (`sweeps/p2_parent_menus_from_b869.py`, output `p2_parent_menus_from_b869_output.txt` beside it) gives:

  | parent (B869 engine) | menu it generates (dim, registerable) | B861-rule endpoint |
  |---|---|---|
  | SU(6)×SU(2), dim 38 | SU(5)×SU(2)×U(1) 28 ✓ · SU(4)×SU(2)²×U(1) [= Pati-Salam×U(1)] 22 ✓ · SU(3)²×SU(2)×U(1) 20 ✓ · SU(6)×U(1) 36 ✓ | su(3)+su(2)+3u(1) |
  | SU(3)³, dim 24 | su(3)²×su(2)×u(1) 20 ✓ (three positions, one orbit) — **no Pati-Salam, no SU(5)×U(1) option** | su(3)+su(2)+3u(1) |
  | Pati-Salam×U(1), dim 22 | su(3)×su(2)²×2u(1) 16 ✓ · su(2)⁴×2u(1) 14 ✗ · su(4)×su(2)×2u(1) 20 ✓ (×2) | su(3)+su(2)+3u(1) |

  So P2 should read: **the parent-keyed menus have a committed generator (B869) but were never
  run for these parents and are in no committed output; B994 did not use them.** This
  *strengthens* D10: the committed engine's SU(3)³ menu contains no Pati-Salam and no
  SU(5)×U(1) rung, confirming that `SU(3)^3→Pati-Salam→SM` and `SU(3)^3→SU(5)xU(1)→SM` are
  positional artefacts. It also *supports* B994's endpoint claim on a real subgroup basis: all
  three parents land at su(3)+su(2)+u(1)ⁿ under the committed rule (the extra u(1)s are the
  engine's maximal-rank convention; registerability strips abelian factors).
- **P3 stands** after the same sweep (`sweep_absence.sh 'b994|rule_variation'`): no B994
  generator on any head; no deleted file matching `B994*`/`rule_variation*` in history.
- Propagation site found by the sweep: `frontier/B1221_global_form_path_independence/
  FINDINGS.md` l.11–13 repeats "others through SU(3)³ and Pati-Salam"; B1221's own result is
  path-independent (kernel of the SM on the 27) so its verdict does not depend on the chain, but
  the sentence inherits D10.

§4's proposal simplifies accordingly: the "three missing menus" need no new computation — run
B869's engine on the three parents (the script above does it) and rewrite the chain exhibit over
its output.
