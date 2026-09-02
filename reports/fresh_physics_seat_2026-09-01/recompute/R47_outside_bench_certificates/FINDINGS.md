# R47 — cloud's outside-bench certificates (origin/claude/outside-bench) rerun on this bench (Phase D, tier D-2)

Fourteen certificates from `outside_bench/certificates/` selected for chain relevance (breaking chain, SUSY, anomaly,
Yukawa, carrier, parity), run in an isolated worktree (`PYTHONPATH=<worktree>:<worktree>/outside_bench`, 900 s cap).
**All 14 exit 0 with their own PASS/verdict lines**; outputs in `*_output.txt`. Every one rebuilds the same E6/27 stack
first (stage 1: ρ27 respects all 3003 Chevalley brackets; stage 3: the m004 relator acts as identity on the 27) and
then prints its FACTs. The seat's reading of what each certifies, in the script's own words:

| certificate | certifies (structure only, all state "Gate 5 untouched / no values") | notes for the chain |
|---|---|---|
| `breaking_chains.py` (10.8 s) | with hypercharge forced, the 27 offers exactly TWO SM-safe vev directions (the ν^c-like and S-like neutral lepton-block states of this frame), so the standard E6 double-breaking is the only SM-preserving chain (necessary-condition level); surviving torus dim 4 = rank SM; both vev directions are lock-odd (the unique chain breaks the lock; neither ψ-parity nor the lock pattern survives) | this is the cited-not-rerun item of B1162 D3 (sweep #1207): it runs and passes here |
| `susy_test.py` (9.9 s) | no odd operator squaring to the meridian exists on the carrier: π₁-equivariant commutant odd part = 0 (Def. A); 27 multiplicity-free with connected weight graph ⇒ e6-commutant on Ψ = gl₂ ⊗ I, which cannot square to A₂ ⊗ A₂₇ (Def. B); the beat is even and Galois-semilinear (Def. C) | B1162 D5 (SUSY no-go) runs and passes here |
| `anomaly_payment.py` (10.5 s) | full 27 cubic anomaly tensor = 0 (56 components); T_dark = −T_16 in every component; T(16)/T(10) = 2; "reproduced-not-predicted (B950)" | integer identities; the seat's R03 agrees |
| `b2_yukawa.py` (22.8 s) | the closing admits exactly 4 independent Yukawa-shaped couplings on one 27; e6 selects the single Jordan combination | structure count |
| `yukawa_texture.py` (11.3 s) | Y-conservation gate PASS; role table for the 8 coupling classes; **"the record's OWN up-type Yukawa shape has 6 nonzero entries: the object's kinematics ALLOWS the up-Yukawa that cc's bundle cohomology FORBIDS (SEAM-Y μ_u = 0). The two walls are now proven DIFFERENT facts: SEAM-Y is a property of the heterotic dressing, not of the object's coupling structure"** | a live mechanism disagreement between cloud (kinematic texture allows) and codex/cc (heterotic dressing forbids, r017 reruns PASS in R46). Both certificates pass; they answer different questions. Main's "up-Yukawa = 0" (B1167) should be read as dressing-level, and B1185's "6-nonzero on object channel vs rank 0 in dressing" already records this |
| `family_yukawa.py` (6.3 s) | on the G-3 family triplet the bracket-induced coupling is exactly ε_family ⊗ C_Jordan (1620 entries); same-family Yukawas identically zero in this (E8) channel; "E8 is not object-paid (G-3 fence stands)" | three-family structure is E8-channel, not object-paid, by the certificate's own fence |
| `yukawa_carrier.py`, `yukawa_clock.py` (14 s, 26 s) | Y = ε ⊗ C is the unique coupling-shaped invariant on the carrier; over the meridian's chain grading every nonzero block has s₁+s₂+s₃ odd, no forbidden block hit | |
| `carrier.py`, `dark_carrier.py` (12 s each) | Ψ = ℂ² ⊗ 27 is an exact π₁-module; class content 1:2, 16:32, 10:20, locked 2/12/10; joint cusp-fixed space dim 12 | kinematics only |
| `a5_parity_lemma.py`, `klein_parity.py`, `twist_parity.py` (0.1 s, 11 s, 23 s) | projective ⇔ even orbit (adjoint data alone); the Klein group splits under the banked mirror realisation; signature class parity-mixed | |
| `principal_witnesses.py` (2.2 s) | runs clean, prints witnesses, no PASS/FAIL grammar | |

**What this changes.** (1) The two B1162 items cited-not-rerun (D3 breaking chain, D5 SUSY no-go) now have a rerun on a
third bench: both pass; sweep verdict #1207 gets that note. (2) The up-Yukawa question has two passing certificates with
opposite headlines on different objects (kinematic texture vs heterotic dressing); the relay should carry that as a
mechanism disagreement, not as a contradiction. (3) Nothing here is a value: every script fences Gate 5 itself.

**Addendum (02:20 UTC).** The outside-bench certificates that read the corpus through `_oa_source.py` pin the commit
`3c58527bc3851ae44fef4f48ecc1eac8aa9dd41b`, which is not on any fetched branch (Phase D agents reported CANNOT_RUN for
`anatomy_reconcile.py` and `d2_scope.py`). Fetched by SHA from origin (GitHub serves it), after which both run clean:
`anatomy_reconcile.py` → "R4 — THE VERDICT (criterion fixed in advance): ORTHOGONAL AXES"; `d2_scope.py` exit 0
(outputs added). Any further pinned-commit CANNOT_RUN rows in the Phase D digest are re-run by hand the same way.

**Addendum 2 (04:50 UTC) — the Phase D digest's remaining non-PASS rows, resolved by hand.** `vol_hygiene.py` needs
`frontier/B1137_regulator_probe` on the path (it imports `basis`/`regulators` from there); with that it passes: vol,
vol_pinorm, vol_over_zetaK2 all INDEPENDENT of the existing regulator basis → KEEP, DROPPED 0 (`vol_hygiene_output.txt`,
84 s). `p3_claim_trace.py` writes its JSON to another session's hard-coded scratch path and is a human-review dump, not a
certificate. Its pinned commit 89affd5b is not fetchable by SHA. `q7_ledger_audit.py`, `vol_basis_probe.py` and
`c4_gue_larget.py` (agent TIMEOUTs at 600 s) are rerunning with 40–90 min budgets; rows follow.

**Addendum 3 (05:45 UTC) — `q7_ledger_audit.py` (agent TIMEOUT at 600 s; seat rerun 10 m 25 s, exit 0):** rebuilds B575's
exact E6 ⊂ gl(27) over ℚ(√−3); memo 161's stabiliser of a generic (x,y) pair reproduces (dim 28, exact nullspace), its
bracket closes, its Killing form has rank 28/28 (nondegenerate), and the centroid {T : T[x,y] = [Tx,y]} has nullity 1
modulo two large primes, which (reduction can only drop rank, scalars give ≥ 1) proves dim_F Γ = 1 exactly — the
stabiliser is central-simple over its field. PASS. (`c4_gue_larget.py` and `vol_basis_probe.py` still running.)

**Addendum 4 (06:25 UTC) — `vol_basis_probe.py` (agent TIMEOUT at 600 s; seat rerun 34 m 29 s, exit 0):** re-derives
B1137's regulator-probe machinery at the pinned commit, extends the pruned 25-entry regulator basis with Vol(m004)
(computed from the dilogarithm), and re-runs the 18 sealed B743 targets × 3 degrees × 4 PSLQ bounds: CONTROL
cells = 216, raw = 117, involves_regulator = 0, targets_with_regulator = 0; EXTENDED (+vol) cells = 216, raw = 108,
involves_regulator = 0, targets_with_regulator = 0. Adding the volume to the basis changes nothing: no sealed target
hits a regulator or the volume. Honest negative, consistent with B1137/B8110. PASS (as a negative).
`c4_gue_larget.py` (GUE spacing test on ≥ 3000 zeros of ζ and L(χ₋₃)) is still computing zeros under its 90-minute
budget; it is a literature-facing statistical test, not chain-critical, and its row lands when it finishes.
