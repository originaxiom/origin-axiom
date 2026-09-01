# Arcs whose reader found the progress logs and the arc files in DRIFT or CONTRADICTION

(30 arcs of 456 digested; NOT_IN_LOG = 185, CONSISTENT = 241)

## B123_arithmeticity_m1 (main) — CONTRADICTION

- **claim of record:** PROVED — "The figure-eight's regular triangulation shape e^{i pi/3} gives trace field Q(sqrt-3) and arithmeticity, offered as a third independent m=1 selection criterion." (banked SUPPORTED, not TESTED-POSITIVE, per FINDINGS itself)
- **log says:** 2026-06-08: banked V112 SUPPORTED. Later log entry (2026-06-08, same day, B125 heading): 'Overturns the B123/K009 third independent/unique m=1 arithmetic criterion, which mis-applied Reid 1991 (a knot theorem) to bundles.'
- **reader note:** The arc is careful to bank itself as SUPPORTED not TESTED-POSITIVE and names its own gated confirmation step, which is good discipline; but the headline 'third independent criterion' claim is overturned by B125 the same day and B123's own verdict file was never updated to say so.

## B225_conductor_decomposition_test (main) — CONTRADICTION

- **claim of record:** The '2 = octahedral parent REFUTED' half is withdrawn as VACUOUS (the bad-prime extraction reports 2 for EVERY monic-in-z input, so specificity at p=2 is zero) and that question returns to OPEN; what SURVIVES is the prime-5 identification -- 5 in the figure-eight character variety's conductor 40 is exactly the golden monodromy branch point x^2=5. | RETRACTED (authored_by field notes: 'W1-wave1-fanout; verdict corrected by B831')
- **log says:** An extensive multi-entry saga: B742 (2026-07-21) revived the 'REFUTED' verdict as resting on a tautological bad-prime proxy; B745 (2026-07-21) cross-verified the revival (disc_z mod 2 is always a square -- 30 seeded inputs, criterion can never fail); B775 (2026-07-24) reports a genuine octahedral parent WAS later found by a different method (projective mod-3 image = S4), 'resolving the B225-revived question positive'; B818 (2026-07-30) and B826 flag that B225's own arc_verdict.json still said PROVED for some time despite B745's confirmed vacuity finding ('carried, not closed... needs reading, not assuming'); B831 (2026-07-30) finally records the retraction on B225's own file/verdict.
- **reader note:** This is the batch's clearest example of the retraction/correction process taking real time to complete -- a vacuous criterion was flagged, confirmed, but sat unfixed on the arc's own verdict record for at least two review cycles before being formally retracted; the underlying octahedral-parent question was later answered positively by an entirely different method (B775), information not visible from this arc's files alone.

## B259_gravity_brick_wall_map (main) — CONTRADICTION

- **claim of record:** Verified the Mostow metric solves 3d vacuum Einstein exactly (Λ=−1) and produced the honest five-wall map: one theorem, one 122-order gap, three open gaps. | PROVED
- **log says:** PROGRESS_LOG B980 (later): retracts wall #5's specific 'k=3 -> GΛ=2π -> 122 orders from observation' derivation as resting on 'two stacked conflations' (a dropped ħ) — RETRACTED as a statement about this object, while explicitly stating B259's walls #1-#4 and the Mostow-metric theorem stand untouched.
- **reader note:** The differential-geometry theorem (hyperbolic = 3d Einstein with Λ=-1) is solid and computed; but the arc's headline quantitative claim (122 orders, wall #5) is later retracted upstream in the progress log without the retraction being written back into this arc's own files — a stranger reading only this arc would be misled.

## B263_t41_cs_levels (main) — CONTRADICTION

- **claim of record:** no verdict file
- **log says:** PROGRESS_LOG 2026-07-03 (promotion-audit sweep) explicitly flags this arc: 'B263 has no FINDINGS (hygiene)'.
- **reader note:** The Chern-Simons/Neumann-Zagier computation itself is exact and internally consistent, but with no FINDINGS or verdict file this arc has no adjudicated claim of record — a stranger cannot tell whether it was ever banked, and the project's own log confirms the hygiene gap.

## B296_seam_arc_verification (main) — CONTRADICTION

- **claim of record:** claim_one_line: 'Adversarial re-run of every seam-arc probe yields zero refutations and zero firewall leaks, strengthening B287 (homology-forced uniqueness), B288 (174 closings) and B291, with the classical math correctly attributed.' status: PROVED
- **log says:** B855 (2026-08-02) found m003 IS amphichiral (is_amphicheiral()=True), directly contradicting VERDICTS.md's own line that m003 is a 'non-amphichiral control' used to argue the CS sign law is object-specific not a SnapPy artifact; also flagged (B289/B296's 164/164 m136, 168/168 m135 claims) as 'reportedly holding' and 'explicitly NOT verified in this arc — queued for independent recomputation'.
- **reader note:** This is a self-graded red-team: the 'adversarial pass' and its 0-refutations tally are asserted constants, not a re-run reproducer, and the one falsifiable factual claim it leans on (m003 as a non-amphichiral control) is directly contradicted by a later arc's direct computation with no correction visible in these files.

## B300_cross_chat_sm_attempt (main) — CONTRADICTION

- **claim of record:** claim_one_line: 'The three-seat brave SM-from-axiom attempt found no new forcing; the eight external inputs compress to two walls (no coupling-strength emitted; the degree-3 carrier absent).' status: NEGATIVE
- **log says:** B1000+B1001 (2026-08-09): 'Three incompatible counts existed and no arc reconciled them (B717: 4 · B300: 8 · sweep: ~8)' — sealed with declared prior 'OUTCOME B, >4 — expected to correct B717,' i.e. this arc's own 'eight external inputs' figure was one leg of an acknowledged three-way count mismatch, only reconciled ~40 days later.
- **reader note:** The arc's central taxonomy claim (8 inputs -> 2 walls) is asserted prose, not a formal derivation, and its own input count was later flagged in the project's own progress log as one of three disagreeing counts across arcs that took roughly six weeks to reconcile — a genuine, log-attested inconsistency this arc's files do not disclose.

## B872_coset_leg (main) — CONTRADICTION

- **claim of record:** PROVED -- coset leg verified: 32=16+16bar at every enhancement point, two independent legs (LEG A exact over Z: D5 root deletion, charges exactly +-1, single Weyl(D5) orbits, fork-node split; LEG B numeric 40-digit at all 3 Galois roots: kernel 46, center 1, ad(z) splits 16/16 with commutant dim 1 each -- absolute irreducibility -- Killing-isotropic with nondegenerate cross pairing rank 16). CORRECTION recorded in the same FINDINGS: ad(z) spectrum is REAL (+-q, split torus, as required by split form e6(6)), reversing an earlier draft's wrong claim of compact u(1) (spectrum +-i*omega), which was a wrong-stratum artifact caught by the commit-gating lock before banking.
- **log says:** PROGRESS_LOG.md 2026-08-03 title: 'the coset leg verified ... the sector charge is COMPACT; B866's boundary fully closed.' This directly contradicts the FINDINGS.md's own correction section 4, which states the charge splits REAL (not compact) and explicitly calls the compact claim a mis-diagnosis from crashed runs at the wrong stratum, caught by the commit-gating lock BEFORE banking. The log entry as quoted was apparently written before or without incorporating that correction and was never itself corrected in the log text.
- **reader note:** Strong two-leg computation (one exact, one high-precision numeric, one modular cross-check) with a real self-caught error corrected before banking -- exactly the kind of process the locks are supposed to produce. The uncorrected log headline is a genuine propagation gap worth fixing even though the underlying math arc is sound.

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

## B181_criticality_scale (main) — DRIFT

- **claim of record:** NEGATIVE — The criticality scale-door is closed: the metallic chain is permanently critical (zero Lyapunov, no transition), so it is scale-free rather than scale-generating.
- **log says:** Three log entries: (1) 2026-07-11 groups B181 (localization) with B507 (beta-zero) and B498 (driftless walk) as 'ONE critical-fixed-point theorem, three wordings, never joined'; (2) 2026-07-14 B571 repeats this unification claim and separately flags 'B507 has NO lock'; (3) 2026-07-14 B578 states 'B181 domain-disjoint (wording repaired)' as part of a correction — i.e. a later entry walks back the strong B181/B507/B498 unification framing.
- **reader note:** The Lyapunov-exponent computation cleanly and correctly distinguishes a permanently-critical metallic quasicrystal from the Aubry-Andre transition, giving genuine structural (localization-theory) content; however the cross-session log shows a substantive claim built on this arc (unifying it with B507/B498 into 'one theorem') was later retracted as 'domain-disjoint,' and that correction is not visible from B181's own files.

## B265_e6_integrability (main) — DRIFT

- **claim of record:** The {4,8} deformation directions are E6-Zariski-dense (generate all 78 of e6), establishing E6-irreducible flat connections on the figure-eight near rho_prin. | PROVED
- **log says:** PROGRESS_LOG (B853, 2026-08-02) cites B265 as banking that 'ONE AJ operator carries BOTH ends' and as the 'sharpest open item'; B981 cites 'B261: one AJ recursion carries both ends' referencing this bridge's context; the log treats B265's content as standing, consistent with its own three-stage correction history (B265->B272->B273->B274) recorded inside the arc itself.
- **reader note:** The Zariski-density and obstruction-space computations are solid and exact; but the arc's own file shows its headline claim was overstated at write-time and downgraded in-text through two later corrections, while the machine-readable arc_verdict.json record was never revised to match — a downstream consumer reading only the verdict file would inherit the overclaim.

## B299_trinification_triality (main) — DRIFT

- **claim of record:** claim_one_line: 'The commuting (θ,φ) ℤ₃×ℤ₃ are inner E₆ lattice automorphisms acting freely on the 27 as nine 3-orbits — the trinification triality — so no φ-eigenvalue can grade the 27.' status: PROVED
- **log says:** B565 (2026-07-13): 'B299's (theta,phi) IS Boyle's SO(8) triality (100% weight-level match)'; B578/B579 (2026-07-14): 'ω = B299's ℤ/3: VERIFIED' flagged as an attribution error ('not verified'; B578-D8 adjudicating), later B578-D8: 'B299's (θ,φ) on the 27 = {1:9, ω:9, ω²:9} exact' (moot/computed).
- **reader note:** The E6/27-orbit computation itself is genuine and reproducible, but the two seed matrices are imported unverified from an external, non-audited repo, and the progress log attaches to this arc a much stronger claim (identity with Boyle's SO(8) triality) that the arc's own files never make or support.

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

## B796_coupling_campaign (audit/b775-braver-questions) — DRIFT

- **claim of record:** no verdict file (has_verdict: false, no root arc_verdict.json; the arc's most authoritative internal artifact is loss_audit/THE_LOSS_LEDGER.md, which states the whole 44-artifact corpus is unharvested onto main, and cell9_sec16_verdict3.md, a PASS-WITH-CONDITIONS non-authoring review of the Cell 9 rung(i) prereg with execution held on 5 open conditions C2-C7)
- **log says:** PROGRESS_LOG (Review 32, 2026-07-29): 'B796's falsifier and the Bost-Connes harvest' are cited as landing on rung-1 algebraicity; R32-14 records 'B796 in flight, not harvestable' as of that review
- **reader note:** This is a large, unusually self-auditing internal-review campaign (verdicts reviewing verdicts, a claim-drop sweep auditing its own headline, an explicit loss ledger) that produces mostly STRUCTURAL/no-observable-content results (group-descent congruences, line-operator classification, dimensional-weight bookkeeping) plus one flagship numeric computation (Cell 9 rung-i Maass-eigenvalue PSLQ test) that per its own third-pass verdict has still not actually been executed end-to-end. The central physics worry a fresh reader should carry forward is functor_obstruction's own flagged, unadjudicated gap: the programme licenses itself a continuous dimensionless 'anchor' input on theorems that only prove a discrete (bit-counted) deficit, which if real undermines the 'zero free dimensionless parameters' claim advertised elsewhere in the repo.

## B79_mn_table (main) — DRIFT

- **claim of record:** PROVED — "The (m,n) degree table shows d=rank on every cell the rep-search reaches (m=1 at n=3,4; m=3 at n=3), with no cell contradicting it."
- **log says:** not in log
- **reader note:** A useful honest consolidation table, but the PROVED verdict for a pattern confirmed on 3 of 6 cells (with the other 3 unreachable, not merely unattempted) overstates the evidence; no physics content.

## B801_negative_census (main) — DRIFT

- **claim of record:** PROVED -- A preregistered 60-arc sample of the 557 unregistered FINDINGS arcs finds 20% negatives, estimating ~111 unregistered kills and kill_graph coverage of the corpus's negatives at 66% (95% CI 56-80%).
- **log says:** 9 entries; DRIFT flagged in the log itself -- B833 (2026-07-30) found the '66% coverage' figure was a UNIT MISMATCH (comparing a sampling estimate to a different denominator); recomputing arc-for-arc gives 33.5% coverage, not 66%. B801's underlying estimate (111 unregistered negatives, 95% CI 55-168) was later corroborated when the actual census landed at 137 (inside interval).
- **reader note:** This is a meta/bookkeeping census about the repository's own negative-result tracking, not a physics claim; flagged mainly because its own headline number was later shown to be a unit-mismatch error, uncorrected in the arc's own files.

## B806_lexicon_blindness (main) — DRIFT

- **claim of record:** PROVED -- The atlas lexicon is 18 regex sets frozen 409 arcs before the survey, so the concentration it reports is its own; arcs matching zero motifs -- including the programme's current falsifier B798 -- are invisible by construction.
- **log says:** 9 entries; DRIFT explicitly acknowledged and corrected in-arc: the headline 'top-3 motifs cover 93.3%' figure drifted to 0.8845 (B829, three months later 0.8496 in B1008), corrected in place within FINDINGS.md itself via an inline '> DRIFTED -- re-derived 2026-07-30 (B829)' annotation.
- **reader note:** A useful, self-critical meta-audit of the repository's own survey tooling (no physics content); notable for transparently documenting its own numeric drift in place rather than leaving stale numbers standing, which is good practice even though the underlying scripts are not in this arc's own files.

## B817_verdict_wave2 (main) — DRIFT

- **claim of record:** PROVED -- Wave 2's 12 readers reach Fleiss kappa = 0.9312, establishing that wave 1's per-slice PROVED-rate spread was genuine era-difference and not reader bias, while its calibration block exercised only 2 of the 4 verdict categories.
- **log says:** 8 entries; DRIFT explicitly documented -- a later arc (B819) corrected B817's claim that residual unverdicted arcs were 'mostly directories without a FINDINGS.md' (133 of 181 actually DO have one; 116 were simply never assigned to a reader), and another (B818) found 2 of B817's 11 untested-category verdicts were wrong (both RETRACTED-should-be-PROVED).
- **reader note:** A methodologically careful inter-rater-reliability exercise (calibration data fully committed) that is notable for catching its own scope gap (calibration block tested only 2 of 4 verdict categories) and for being corrected twice by later arcs (B818, B819) -- the correction chain is transparent in the progress log even where arc_verdict.json itself does not carry it forward.

## B862_global_form (main) — DRIFT

- **claim of record:** The cascade's step-3 winner, as a group inside SU(5), is S(U(3)xU(2)) = [SU(3)xSU(2)xU(1)]/Z6 (kernel computed exactly, order 6); resolves the SM's own Gamma in {1,Z2,Z3,Z6} ambiguity (Tong 1705.01853), calling this 'the first place in the programme where the selected structure outperforms the SM's own data.' | status: PROVED (verdict file NOT updated after the two addenda).
- **log says:** Log (2026-08-03) records B862 exactly as the FINDINGS state it. B969 (2026-08-08) and B976 quote the 'outperforms the SM's own data' framing approvingly and note B862 was the ONE cascade arc (of B860-B873) that survived synthesis-layer citation. B1210 (2026-08-29) and the THE PAPER currency pass (2026-08-30) flag that sections of the paper draft were 'written from the B862-B1080 band' and needed correction against B1221's later path-independence finding -- consistent with the arc's own 2026-09-01 addendum.
- **reader note:** The Z6-kernel computation itself is correct and exact, but the arc's most-quoted framing ('outperforms the SM's own data', 'for free') has been explicitly deflated by its own later addendum as literature-known and non-novel -- yet the verdict file a downstream reader would consult first still carries the un-deflated framing verbatim.

## B892_second_measurement (main) — DRIFT

- **claim of record:** PROVED (verdict text unedited) -- 'z(x1,y*) = su(3) (+) su(2) (+) u(1)^3 EXACTLY: two measurements of the object's own superselection charges take E6 to the Standard Model algebra, skipping SU(5).' FINDINGS.md itself now opens with a correction banner (added 2026-08-08 by arc B950): the mathematics (dim 14, derived 11, centre 3) is untouched, but the phrase 'the Standard Model algebra' overstates by two abelian factors -- su(3)+su(2)+u(1)^3 is 14-dimensional, the real SM gauge algebra su(3)+su(2)+u(1) is 12-dimensional with ONE abelian factor, not three.
- **log says:** DRIFT/CONTRADICTION over time: the original 2026-08-05 log entry repeats the uncorrected 'take E6 to the Standard Model algebra' framing; later entries (B950 2026-08-08, B951 2026-08-08, B1210 2026-08-29) progressively deflate the claim further -- B951 shows the su(3)+su(2)+u(1)^3 landing is exactly the classified A2+A1 Levi subalgebra of e6 (Borel-de Siebenthal 1949/Dynkin 1952), i.e. not a novel discovery but arriving at a 77-year-old catalogued endpoint from a particular route; B1210 explicitly names this as the paper-spine sweep catching an overstated headline.
- **reader note:** The raw computation (14/11/3, the wall's complex nature) is solid and independently reproduced elsewhere, but the arc's own verdict-of-record still carries an overstated headline ('the Standard Model algebra') that two later corrections (B950: dimension mismatch; B951: this is a 77-year-old classified Levi subalgebra, not a discovery) never propagated back into the verdict file itself -- a textbook SUPERSEDED_UNMARKED case worth flagging prominently.

