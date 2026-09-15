# memo_191 — WHAT_WE_CAN_ANSWER_OURSELVES.md

## 1. HEADLINE
"**F190-2: two thirds of Q11 are decidable from what this bench already holds**, and `c_eff = 1` turns out to be forced by the *shape* of `Ẑ`, not by our knot." Date: 2026-09-09 (Addendum 1 same day).

## 2. CLAIMS
1. GM §10.2/Remark 3.8 identify the log-VOA for Brieskorn spheres (`(1,p)` singlet, `c = 13 − 6(p+1/p)`) and name the hyperbolic case OPEN in print — DOCUMENTARY / literature-read, graded "PARTLY ANSWERED."
2. Bridge identity `Ẑ^unred_0 = Ẑ_0/(q)_∞` — used as given (later confirmed against primary source in Addendum 1).
3. Measured: `Σ(2,3,5)` (p=30) c=−167.200, c_eff=1.000326; `Σ(2,3,11)` (p=66) c=−383.091, c_eff=1.001480 — c varies by 215.9, c_eff varies by 0.0012 → **CELL = OUTCOME B** (c_eff does NOT depend on p; not reachable by choosing a different sphere).
4. Controls: estimator returns 1 on `1/(q;q)_∞`, 2 on its square, 0 on a bare false theta — instrument validated, not stuck at 1.
5. Q11(a) "known mechanism attaching modular boundary data" — graded PARTLY ANSWERED (yes for Brieskorn, open-in-literature for hyperbolic).
6. Q11(b) "does it carry c_eff = 6" — graded ANSWERED, NEGATIVELY, STRUCTURALLY (6 unreachable via this family).
7. Q11(c) "is the obstruction general or knot-specific" — graded NOT ANSWERED, sharpened to a one-line question (F191-1).
8. Memo 171's earlier "1" reading reinterpreted: same number, "different standing" (was a modelling artifact, now the object's own number) — reclassification, not a new computation.
9. ADDENDUM 1: primary source arXiv:1602.05302 confirms the bridge is GPV (6.50) (unrefined, t=−1), not GM's cited (6.49) (refined) — citation correction, PROVED/confirmed.
10. ADDENDUM 1: §3(c) gets a named candidate — GPV's refined block (denominator `(−qt;q)_∞`) is NOT of the `(false theta)/(q)_∞` shape — candidate, not computed (F191-3, named follow-up, not done).

## 3. CERTIFICATE
`outside_bench/certificates/zhat_unred_ceff.py` EXISTS (185 lines). `outside_bench/outputs/zhat_unred_ceff_out.txt` EXISTS (52 lines). Output tail reproduces the memo's own language verbatim, e.g. "c_eff = 1, and p cancels out COMPLETELY: the two spheres above differ by 216 in c and by less than 0.03 in c_eff. 6 is not reachable by choosing a different 3-manifold in this family" — agrees with the memo's headline and §2 table (output says "differ by 216" vs memo's "215.9" and output "less than 0.03" vs memo's "0.0012" — both are the same underlying finding stated more loosely in the output; no contradiction, just rounding/hedging). No seal is claimed for this memo (none named in the header).

## 4. ON MAIN ALREADY?
1. GM §10.2/Remark 3.8 reading: (c) NOT on main — this is a literature-reading claim internal to the outside-bench lane; "memo 191" is not cited anywhere in `docs/` or `frontier/` outside `outside_bench/`.
2. The c_eff=1 measurement and the Σ(2,3,5)/Σ(2,3,11) numbers: (c) NOT on main as such — `docs/HARVEST_LEDGER.md`, `frontier/B1305_the_cloud_156_178/*`, `frontier/B674_generation_leg/w3_support/route_B.md` reference `c_eff` and Brieskorn-sphere computations from *other* arcs (pre-existing, cited by memo 191 as the source series), but none of them cite memo 191's conclusion back.
3. Q11 itself is a live, widely-tracked item (`docs/CAMPAIGN_STATUS.md`, `docs/RELAY_LEDGER.md`, `docs/HARVEST_LEDGER.md` row 41, `docs/TOE_REQUIREMENTS_LEDGER.md`) but `docs/HARVEST_LEDGER.md:73` only registers a *different* Q11 fork (non-abelian T[M] / another boundary sector, from B1305) as a Phase-3 item — it does NOT reference memo 191's "two-thirds decidable" answer. So: (c) NOT on main.
4. GPV citation correction (Addendum 1): (c) NOT on main.

## 5. NEEDS COMPUTATION HERE
1. The discriminating fact is the c_eff invariance itself: recompute `Ẑ_0` for `Σ(2,3,5)` and `Σ(2,3,11)` as q-series to enough order, form `Ẑ_0/(q;q)_∞`, and fit `c_eff` via the standard modular-anomaly growth-rate estimator (the same one already in the corpus, used at B1305/B674). Expected: c_eff ≈ 1.000 ± 0.002 for both, independent of p. This is a short, bounded rerun (the certificate itself is 185 lines and already does it in under 2 minutes per the memo's own gate).
2. Addendum 1's GPV (6.49) vs (6.50) distinction is DOCUMENTARY (a citation-accuracy check against the arXiv PDF, not a numeric claim) — no computation needed, only a source-text comparison.
3. F191-3 (measure the refined block, denominator `(−qt;q)_∞`) is NOT DONE here — it is an explicitly named but unexecuted follow-up; a verifier should treat it as open, not as a claim to grade.

## 6. SUPERSESSION
No later outside-bench memo revisits or withdraws memo 191 (INDEX.md rows after 191 — 196, 199, 202, 215, 217, and others — do not mention it). Owner register not searched exhaustively for a later reversal, but no addendum to THE_OWNER_REGISTER.md is cited by memo 191 or by later memos as superseding it. Not superseded by anything on main either (main does not cite it at all, so there is nothing on main to conflict with it).

## 7. GRADE PROPOSAL
**REGISTER** (documentary/literature-reading, with one small reproducible numeric cell). The core empirical content (CELL → OUTCOME B, c_eff=1 invariant under p) is a legitimate short computation worth a REPRODUCE-AND-BANK row if a verifier wants the number on record, but the memo's real payload — closing 2/3 of Q11 by reading GM/GPV — is documentary and currently absent from every Q11-tracking document on main.
