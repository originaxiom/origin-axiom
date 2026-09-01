# Arcs whose reader found the progress logs and the arc files in DRIFT or CONTRADICTION

(15 arcs of 200 digested; NOT_IN_LOG = 95, CONSISTENT = 90)

## B123_arithmeticity_m1 (main) — CONTRADICTION

- **claim of record:** PROVED — "The figure-eight's regular triangulation shape e^{i pi/3} gives trace field Q(sqrt-3) and arithmeticity, offered as a third independent m=1 selection criterion." (banked SUPPORTED, not TESTED-POSITIVE, per FINDINGS itself)
- **log says:** 2026-06-08: banked V112 SUPPORTED. Later log entry (2026-06-08, same day, B125 heading): 'Overturns the B123/K009 third independent/unique m=1 arithmetic criterion, which mis-applied Reid 1991 (a knot theorem) to bundles.'
- **reader note:** The arc is careful to bank itself as SUPPORTED not TESTED-POSITIVE and names its own gated confirmation step, which is good discipline; but the headline 'third independent criterion' claim is overturned by B125 the same day and B123's own verdict file was never updated to say so.

## B111_sign_structure (main) — DRIFT

- **claim of record:** PROVED — The tower's sign structure equals the all-heights opposition-involution closed form plus exactly one degree=rank promotion char(M)->char(M^n). NOTE: superseded by B117 per arc_verdict.json (supersedes: none listed for B111, but B117's verdict lists 'supersedes: B111').
- **log says:** PROGRESS_2026-Q2 2026-06-07 banks the closed form + promotion; B550 (2026-07-12, PROGRESS_LOG) processes a later handoff's Promotion-Sign Conjecture and REFUTES it against 'B111's LOCKED exact tower'; B117 (2026-06-07) explicitly states '(3b) The promotion is a Sym^1 ABSENCE (B111/B113 superseded)'; Review 32 (2026-07-29) lists B111 as 'already in CLAIMS.md — banked at the highest tier'.
- **reader note:** The underlying combinatorial computations (parity rule, closed form, promotion diff) look solid and reproducible, but the arc's own verdict file was not updated to reflect that B117 reframes and supersedes its central 'promotion' narrative — a governance gap the seat is specifically told to catch.

## B120_tower_determination (main) — DRIFT

- **claim of record:** PROVED — The trivial-point tower is fixed by (n; trace, det) alone; the height-count closed form and the forced doubling range {2..n-3} are established.
- **log says:** PROGRESS_2026-Q2 2026-06-07 banks Chat-2 Q2/Q3 + Supplement S1-S5, verify-don't-trust, correcting three of the handoff's formulas; PROGRESS_LOG 2026-07-24 promotes B120's height-count closed form to LAW_MAP 'as a law rather than a theorem because its arc states it with no proof-strength tag', with a recorded near-miss where cc's own transcription mis-ordered the clauses at n=2 and produced a false mismatch, caught and attributed correctly to cc's own error.
- **reader note:** Solid corrective work (fixes three wrong formulas from an external handoff with concrete counterexamples/verifications), and it is exactly the kind of arc later independently re-verified by a reviewing pass rather than trusted — the one discrepancy is a verdict-label/proof-strength mismatch between this arc's own PROVED tag and the later review's more cautious 'law' relabeling.

## B131_two_seed_fork (main) — DRIFT

- **claim of record:** PROVED — "Gluing two distinct metallic seeds along cusp tori intersects their A-polynomial curves in finitely many points, collapsing the free kappa into a discrete internal fork."
- **log says:** 2026-06-09: banked V120, resolves S032-B (yes). Later (B134, 2026-06-09): 'B131 (R2): KNOWN, with a framing qualification' -- Kitano-Nozaki 2020 shows the mechanism is gluing-map-driven (not distinctness-driven); B131's math stands but its 'heterogeneity makes the choice' framing is identity-gluing-specific.
- **reader note:** A solid, doubly-validated exact result for the (1,2) case, later found to be a known phenomenon in the literature (Kitano-Nozaki) with a scope-narrowing qualification on its 'heterogeneity, not multiplicity' framing that is not reflected in B131's own verdict file.

## B138_s031_principal_lemma (main) — DRIFT

- **claim of record:** The principal Sym^{n-1} image of an SL(2) rep over K is a trace-map fixed point with all traces in K, for every n; the converse stays open. | PROVED
- **log says:** B775 Phase 2 Wave 6 (2026-07-24) calls this 'a new all-n THEOREM (B138, S031a sealing SL(3)->SL(4))'; the Q2 progress entry describes it more precisely as principal-image PROVED + SL(4) obstruction + object-clarification.
- **reader note:** A clean, reproducible half-proof (Sym-power is Z-defined, so field-membership is trivial) honestly paired with a stated computational obstruction at SL(4); the one problem is a later progress-log entry inflating it to a full theorem, which the arc's own text does not support.

## B145_forced_chirality (main) — DRIFT

- **claim of record:** Chirality cannot be forced: over the catalogued once-punctured-torus bundles the canonical/minimal locus coincides with the self-mirror (amphichiral) family. | NEGATIVE
- **log says:** Campaign 1' — chirality cannot be forced (canonicity <=> self-mirror); parity is contingent. A later log entry (B146) states B145 is 'sound but over-scoped', and a further entry (B147) states 'B145's arithmeticity arm is REFUTED OUTRIGHT — arithmetic chiral o-p-t bundles exist'.
- **reader note:** The combinatorial (metallic-is-self-mirror) half of B145 is solid, but its arithmetic-arm claim was built on the wrong trace field and is refuted by its own immediate successors -- and critically, B145's own FINDINGS/README/verdict files were never patched to reflect that, unlike B141's ADDENDUM pattern which at least sits beside the file.

## B154_silver_bundle_foundation (main) — DRIFT

- **claim of record:** PROVED — degree=rank generalizes beyond the figure-eight to the metallic family via the derived meridian mu=A^-m t, with the exponent order-determined rather than rank-determined.
- **log says:** PROGRESS_2026-Q2 2026-06-16 entry matches the meridian derivation; PROGRESS_2026-Q2 2026-06-17 entry (B157) explicitly states the closed form k=4-m(o-3) from this same arc's FINDINGS is REFUTED by bronze (m=3) data, with only the order-not-rank conclusion surviving.
- **reader note:** The underlying meridian derivation is solid and the arc is commendably self-correcting in its own FINDINGS text, but the verdict file's status (PROVED, superseded_by:null) does not reflect that its own headline closed-form result was refuted one arc later, which is exactly the kind of drift the campaign's claim-of-record convention is meant to catch.

## B759_qp3_integration (main) — DRIFT

- **claim of record:** PROVED — "The theta-odd and theta-even sectors couple at SL(3)=Sym^2 but not at SL(2), with off-block norm sqrt3 = sqrt|disc Q(sqrt-3)|."
- **log says:** PROGRESS_LOG 2026-07-22 logs INTEGRATED as banked; however the SAME-DAY log entry for B764 (2026-07-22) states the general 'coupling = sqrt(d) for trace field Q(sqrt(-d))' law asserted here (FINDINGS section 'The discriminant law') was tested out-of-family at 5_2 and FAILED, replaced same-run by a corrected pair-separation law — this correction is not reflected anywhere in B759's own FINDINGS.md.
- **reader note:** The core linear-algebra computation (off-block Jacobian norms at SL(2)/SL(3)/adjoint) is exact and correctly cross-checked numerically, but the arc's own headline generalization ('coupling = sqrt(d) for any imaginary-quadratic trace field') was falsified the same day by B764 without B759's FINDINGS being updated — a live, uncorrected overclaim sitting in the banked record.

## B75_metallic_degree_rank (main) — DRIFT

- **claim of record:** PROVED — "degree=rank is a two-parameter (m,n) phenomenon: M^3=L holds on the m=3 metallic bundle as well as the figure-eight, not a figure-eight accident."
- **log says:** not in log
- **reader note:** A genuine but partial numerical result (two data points on two axes) presented with appropriate honesty in FINDINGS, undercut by an unqualified PROVED verdict label; no physics content, explicitly self-scoped as standalone topology.

## B766_measurement_torsor (main) — DRIFT

- **claim of record:** PROVED — "The discrete measurement torsor has rank exactly 3 (conjugation, reversal, golden branch), saturating the banked menu; time's arrow and the basepoint bit are one choice."
- **log says:** R29-5 owner-opened; cc3's independent audit re-derived all five action-table entries, RANK-SATURATED CONFIRMED with one derivation upgraded (matrix-level theta on T6, not trace-level). Later arcs (B786, 2026-07-25) flag that 'theta (reversal)' is trace-trivial at every rank and propose the trace-active involution is iota=inversion instead; B787 (2026-07-25) finds iota is a genuine 4th independent involution (rank 3->4, unconditional) that DE-WELDS T7 (time) from T3 (basepoint) — framed explicitly as EXTENDING B766, not overturning it, with B766's rank-3 observer menu stated to 'still stand.'
- **reader note:** The core F2-rank-3 computation is genuinely re-derived independently and looks solid as algebra; but the object being computed (a 'measurement torsor' closing physical existence via Galois involutions) is dressed in physics/observer language that Gate 5-Q itself disclaims as merely structural — later arcs (B786/B787) already revise which involution does the trace-active work, so the theta-generator identification here should not be read as final.

## B775_phase2_wave1 (main) — DRIFT

- **claim of record:** verdict NEGATIVE; claim_one_line: 'Wave 1 tombstones three courier frameworks and walls the mover door (no object-native outer operation); one selection-rule theorem and gamma5's derivation survive.' (arc_verdict.json covers only Wave 1 of the 6 banked waves in this arc directory; Waves 2-6 have no separate arc_verdict entries in this file.)
- **log says:** PROGRESS_LOG.md records each wave as banked (Wave1: 'all 7 upheld'; Wave2: '6 banked, 1 downgrade-carry'; Wave3: '7 banked, 1 carry, 2 theorems, an octahedral parent'; Wave4: '5 results incl. an axiom repriced and a value-field law' -- FINDINGS_WAVE4 itself says 4 banked/4 carry, a mismatch with the log's '5 results'; Wave5: 'four theorems/laws + a powered statistic'; Wave6: 'the repair wave (5 banked, 3 further catches)'). Review 30/31 summarize B775 as opening 'the structural substance' with the T1-mover walled, gamma5 derived, three courier frameworks tombstoned. B1199/B1202 later cite B775/B778 as the source of an already-banked all-p proof for a separately-tracked open item (R5/GC-29), confirming B775's Wave2 PADIC-adjacent content was reused correctly elsewhere.
- **reader note:** This is one of the more methodologically self-critical arcs in the corpus: multiple cells compute exact/symbolic results with genuine negative outcomes (T1MOVER walled, D5 dismissed, ENUM shown decorative, WELD shown base-rate, PD22 self-falsified), and later waves explicitly hunt for and document their own prior waves' overclaims (MB12 vacuity, unearned negatives, forced reasons, undeclared selection). All content is STRUCTURAL/arithmetic (Galois groups, McKay correspondences, trace theorems) with zero SM-observable numbers claimed (Gate 5 self-reported clean throughout) -- appropriately so, since this is explicitly non-observational group theory. The residual risk is bookkeeping, not computation: the single arc_verdict.json undersells five later waves, and at least two Wave-6 carries (B465-r's new false universal, D3-r's disconnected verdict string) are documented defects left uncorrected in the committed cell outputs as of this read.

## B786_torsor_theta_iota (main) — DRIFT

- **claim of record:** claim_one_line: 'The measurement torsor's third generator is inversion ι, not reversal θ (trace-trivial at every rank); the object's self-dual rank-3 theorem is unchanged.' status: PROVED. supersedes: B766.
- **log says:** PROGRESS_LOG 2026-07-25 'B786 — the θ/ι refinement...': C20 text refined + a B786 pointer, 3 locks. A LATER entry (B787, 2026-07-25) states iota=inversion is a genuinely independent 4th involution 'UNCONDITIONAL — sharpens B786's conditional flag' via A5-ambivalence + monodromy inversion, and iota DE-WELDS T7 from T3. A B817 (2026-07-30) audit entry explicitly flags 'B786's claim stopping at its own content instead of reaching into B787's later 4th-involution refinement' as a known scoping gap.
- **reader note:** The core computed result (theta trace-trivial vs iota trace-active at genuine SL(3), object rank 3 unchanged) is small, exact, and reproducible from one committed SymPy cell. The one gap is structural/documentary, not computational: the arc's own record never got a forward pointer to B787's stronger, unconditional version of its 'open door', which is exactly the kind of drift the packet's SUPERSEDED_UNMARKED rule is meant to catch.

## B792_maass_m004_eigenvalues (audit/b775-braver-questions) — DRIFT

- **claim of record:** no verdict file (has_verdict: false; no arc_verdict.json in this arc's directory)
- **log says:** PROGRESS_LOG (2026-08-01, B845/B846): 'B792 is NOT in main' — it is cc3's own arc on a branch that never merges to main; citing it as if it were in main is flagged as a class of error. Main harvested only a partial subset (6 eigenvalues, later completed to 17, to r=9.84) with per-eigenvalue diagnostic fields explicitly marked 'NOT IN MAIN — absent rather than fabricated'. Review 36 separately notes a reviewer's claim of '43 eigenvalues to r=13.5 belonging to B792' is itself wrong — main has 17 to r=9.84.
- **reader note:** The Maass-eigenvalue computation itself is genuinely observable-shaped (named quantities r, lambda with numerical values, cross-checked two ways) and the SM-comparison test is honestly a clean null rather than a fitted hit — good practice; but the arc is not in main, so none of it currently supports any claim made on the trunk, and the physics content (a spectral-geometry eigenvalue set) has no measurable connection to any observed physical quantity beyond the explicitly-reported null.

## B794_congruence_level4 (main) — DRIFT

- **claim of record:** claim_one_line: "Re-derived from scratch: the figure-eight group is congruence of level exactly (4), and every trace norm is 0 or 3 mod 4, refuting the narrower norm-split claim." status: PROVED
- **log says:** PROGRESS_LOG 2026-07-24: Gamma_41 is a congruence subgroup of level (4), mod-4 trace law proved; REVIEWS Review 32 (2026-07-29): naming correction (true PSL order 960, not 1920) promoted into the record along with Z ∩ H = {±I}.
- **reader note:** The two headline theorems (congruence level exactly 4; trace-norm law {0,3} mod 4) are exact, finite, self-contained modular-arithmetic computations that a stranger can rerun byte-for-byte from verify_congruence.py alone — the strongest kind of witness in this batch. But the narrative built on top of them (what it means for the earlier B790 norm-split hint) was revised twice in the same FINDINGS.md and the terse arc_verdict.json one-liner was never brought into line with the final revision, so a reader trusting only the verdict record would get the wrong version of the norm-split conclusion.

## B79_mn_table (main) — DRIFT

- **claim of record:** PROVED — "The (m,n) degree table shows d=rank on every cell the rep-search reaches (m=1 at n=3,4; m=3 at n=3), with no cell contradicting it."
- **log says:** not in log
- **reader note:** A useful honest consolidation table, but the PROVED verdict for a pattern confirmed on 3 of 6 cells (with the other 3 unreachable, not merely unattempted) overstates the evidence; no physics content.

