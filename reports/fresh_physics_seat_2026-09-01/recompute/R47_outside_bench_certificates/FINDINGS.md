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
