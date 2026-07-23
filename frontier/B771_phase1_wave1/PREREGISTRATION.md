# B771 PREREGISTRATION — PHASE 1, WAVE 1 (the mechanical lane: triage + the first closure batch)

*Sealed before any cell computes. Phase 1 operates on B770's phase-1 rows (census.json,
the frozen Phase-0 snapshot — planning deltas live here, the snapshot stays untouched).*

## Triage of the 56 phase-1 rows (the lanes)

- **DEDICATED (the quartet):** OI-054 WALL-7, OI-055 B685 3-integrality, OI-056
  TOMB-L310, OI-057 TOMB-L34. OI-222 (the quartet meta-row) is SUBSUMED by these four.
  B685 leads (both seats' plans agreed) — it is Wave 1's cell 0.
- **EVENT-DRIVEN / WAIT:** OI-042 (B500 wrap — watcher armed), OI-223 (mutation test
  fires at Review 30), OI-266 (Track L), OI-284 (cosmogony sweep, gitignored),
  OI-303 (R27 owner-gated), OI-340 (sentinels armed). Documented, not launched.
- **PLANNING CORRECTIONS:** OI-311 (the census itself) is DONE-BY-B770 — census-lag,
  not real work. OI-209 carries Gate 5-Q in full if ever run (Q5 absolute).
- **HYGIENE (one later arc):** OI-230 (GitHub-side merges bypass local gates; NB the
  untracked .github/ draft), OI-231 (seal-ledger coexistence residual), OI-232 (R29
  certification gaps). Reserved for a dedicated hygiene arc, not this wave.
- **WAVE 1 (this arc, 13 cells):** below.
- **WAVE 2+ (later arcs):** the remaining mechanical rows (incl. OI-017, OI-020,
  OI-067, OI-068, OI-075, OI-078, OI-082, OI-084, OI-100, OI-105, OI-115, OI-119,
  OI-124, OI-139, OI-147, OI-149, OI-174, OI-180, OI-183, OI-188, OI-192, OI-194,
  OI-197, OI-204, OI-236, OI-237, OI-249, OI-304, OI-307, OI-335) — sealed per-wave
  when launched.

## The 14 unassigned reverts — phases assigned
OI-108, OI-140, OI-263, OI-270, OI-274 → phase 1 (wave 2+); OI-046, OI-058, OI-116,
OI-272, OI-275, OI-290 → phase 2; OI-166 → phase 4 (walls); OI-307 → phase 5
(dossier); OI-303 → owner-gated standing.

## Wave 1 cells and their two-outcome criteria

Cell 0 (OI-055): **B685 3-integrality** — formalize the depth-exposed kill's residual:
prove the 3-only-denominators property at the level the FINDINGS name as open, or
produce the explicit obstruction. Outcomes: PROVEN (symbolic, all-n at the named
level) / OBSTRUCTED (the named blocker, reverts to EXTERNAL).

Cells 1–12, each with outcomes A / B / UNRESOLVED-honest (reverts the row to
EXTERNAL with the obstruction named; forcing a verdict is the failure mode):
1. OI-031 B399 e₃ exact: the depth-5 triple-cubic e₃ has an exact closed form in the
   banked field / provably does not (PSLQ at height with the tolerance-height rule).
2. OI-043 the −1/16 phase sum: CRT closed form exists and is proven / the sum resists
   with the obstruction named.
3. OI-063 L39 Gauss-sum law: the period-content law admits the all-t symbolic proof /
   a counterexample t is found.
4. OI-092 genus-2 CS re-run: the numeric re-run at current precision confirms the
   banked value / diverges (both bankable; ≥2 seeds).
5. OI-146 B332 Bianchi index: the index-3 computation on the √−3 side verifies
   exactly / fails with the discrepancy shown.
6. OI-148 B415 level-27: μ_∞ confirmation completes / refutes.
7. OI-150 B178/B171: the exact gap-power law holds symbolically / the rank-3 label
   corrects it.
8. OI-151 B38/B39 torsion-one identity: proven exactly / counterexampled.
9. OI-173 H103: level-3 unreachability for 2T is a clean theorem (period argument) /
   a reaching sequence exists.
10. OI-186 H112: one identity behind Fricke tr(A₁A₂)=15 and seam conductor 15 is
    derived / the two 15s are shown independent (base-rate honest).
11. OI-189 H115: the golden-norm doubling-transfer reconstructs exactly for n≥2 /
    fails at a named n.
12. OI-200 B645/B678: the D4 ceiling 1.7849887… is identified exactly (PSLQ,
    tolerance-height rule, verified on 10+ digits both directions) / remains
    unidentified at the swept height (bounded-negative).

## Method (binding for every cell)
Exact/symbolic computation preferred; numerics validated at ≥2 seeds/word-sets with
conditioning where applicable; the discriminating fact computed in-cell, never cited;
each cell writes compute.py + output.txt under frontier/B771_phase1_wave1/cells/OI-xxx/;
every cell verdict adversarially verified by an independent rerun before banking;
UNRESOLVED is honest and reverts the row to EXTERNAL. Gate 5 / Gate 5-Q verbatim;
nothing to CLAIMS; no SM values; the one-number pin untouchable.
