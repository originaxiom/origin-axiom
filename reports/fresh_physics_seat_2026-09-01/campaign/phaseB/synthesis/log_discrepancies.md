# Arcs whose reader found the progress logs and the arc files in DRIFT or CONTRADICTION

(60 arcs of 770 digested; NOT_IN_LOG = 246, CONSISTENT = 461)

## B1012_branch_verifications (main) — CONTRADICTION

- **claim of record:** verdict PROVED; claim_one_line: TWO BRANCH RESULTS VERIFIED EXACTLY -- k-blindness (dS/dk=-CS identically) sharpened to an EQUIVALENCE with amphichirality, and CROSSING_REQUIREMENTS R4 discharged via a CS-normalisation closure (c=6sigma forced).
- **log says:** B1011-B1013 (2026-08-10): k-blindness verified and sharpened -- dS/dk=-CS identically, so blindness to k IS amphichirality; CS normalisation closure verified, R4 discharged -- matches original FINDINGS, but a later log entry (2026-08-31, B1226) states the equivalence FAILS both ways.
- **reader note:** The core algebraic identity (dS/dk=-CS) is genuinely exact and reproducible; but the arc's headline 'sharpening' -- that k-blindness IS amphichirality -- is a distinct, unverified equivalence claim that was later refuted, and the refutation has not been propagated into this arc's own banked FINDINGS/verdict files despite being caught in an addendum.

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

- **claim of record:** PROVED — Adversarial re-run of every seam-arc probe (B287-B295) yields zero refutations and zero firewall leaks, strengthening B287 (homology-forced uniqueness), B288 (174 closings) and B291, with the classical math correctly attributed.
- **log says:** B855 (2026-08-02) found a correction directly against this arc: 'm003 IS amphichiral' contradicting VERDICTS.md's description of m003 as a 'non-amphichiral control' on the very line the CS-sign-law claim turns on. Separately B842 (2026-08-01) flagged this arc as mislabeled a face-attachment (methodology, not object physics) by the pre-existing corpus classifier.
- **reader note:** This is a self-graded audit of the program's own prior claims, with the grading encoded as hardcoded pass/fail dict literals rather than recomputation — and a later log entry (B855) directly contradicts one of its load-bearing control claims (m003 amphichirality) with no correction recorded here. Pure math/reframe content; STRUCTURAL, not observable.

## B361_seam_local_law (main) — CONTRADICTION

- **claim of record:** verdict PROVED: 'Across 8 pairs with zero counterexamples, a level-15 pair invariant carries sqrt(-15) exactly when it contains a seed elliptic at both 3 and 5 (m=2,7); the discriminator refutes H-min and leaves H-loc standing.'
- **log says:** 2026-07-02: (1,7) BRIGHT refutes H-min, (3,7) BRIGHT with value-echo to (2,3). CRITICAL FOLLOW-UP (2026-07-03, 'B367 step 0'): 'the completed table REFUTES the B361 local law at pair (3,4)' — (3,4) is bright with NO seed elliptic at both primes, killing the banked 'bright iff a both-elliptic seed' rule on its twelfth pair. Log explicitly states 'B361's row updated; its confirming pairs remain valid data.' A 2026-08-30 sweep entry (B1218) separately flags stale row L57 as 'B359/B363 also uncited' but does not mention the B361/B367 refutation status directly there.
- **reader note:** This is the single most load-bearing finding in the batch: the committed arc_verdict.json for B361 claims a proved law with zero counterexamples, but the project's own progress log shows that law was refuted by a later probe (B367, pair (3,4)) without B361's own files being corrected or cross-referenced — exactly the SUPERSEDED_UNMARKED pattern the seat is asked to catch.

## B362_seam_law_confirmations (main) — CONTRADICTION

- **claim of record:** verdict PROVED: 'All three pre-registered seam predictions hit exactly, extending the doubly-elliptic-seed brightness law to 11 pairs with zero counterexamples.'
- **log says:** 2026-07-02: (2,7) BRIGHT, (1,5) DARK, (4,5) DARK as predicted; law now stands at 11 exact pairs, zero counterexamples.
- **reader note:** Directly inherits B361's superseded-and-unmarked defect one probe later; the individual exact computations (which pairs are bright/dark) are presumably still correct, but the generalized 'law' language in both FINDINGS and verdict.json is stale as of the very next day's work and was never corrected in these committed files.

## B505_quasicrystal_anchor (main) — CONTRADICTION

- **claim of record:** PROVED — "kappa - 2 = 4*lambda^2 as a POLYNOMIAL IDENTITY in (E,lambda): the programme's kappa-coordinate IS the squared quasiperiodic coupling of the measured Fibonacci Hamiltonian."
- **log says:** a later log entry (2026-08-01, P5 Phases 0-1) states explicitly: "B505 and B507 carry NO scripts and are not load-bearing."
- **reader note:** A two-line symbolic identity is plausible and easy to verify by hand, but the arc as committed provides no script, and the project's own later audit says exactly that — the PROVED verdict stands unretracted despite this.

## B507_beta_function (main) — CONTRADICTION

- **claim of record:** OPEN — "First-pass beta-function: g_M(kappa) is strongly negative (~-1.05 to -1.25) on the negative-kappa leaves where the object lives, so the measurement verb is NOT marginal there."
- **log says:** 2026-08-01 log entry: "B505 and B507 carry NO scripts and are not load-bearing." Earlier entries (2026-07-11, 2026-07-14) describe the beta-function zero at kappa*≈0 as reproducing under two independent methods and being unified with B181/B498 as one criticality theorem, and note "B507 has NO lock."
- **reader note:** The verdict is honestly left OPEN, which is good discipline, but the headline numeric result (zero of an emergent beta-function at kappa*=0, matched to the pointer state) rests on an unwitnessed 6M-sample run; B520 later reproduces it independently with its own code, which is reassuring but does not retroactively supply this arc's missing witness.

## B872_coset_leg (main) — CONTRADICTION

- **claim of record:** PROVED -- coset leg verified: 32=16+16bar at every enhancement point, two independent legs (LEG A exact over Z: D5 root deletion, charges exactly +-1, single Weyl(D5) orbits, fork-node split; LEG B numeric 40-digit at all 3 Galois roots: kernel 46, center 1, ad(z) splits 16/16 with commutant dim 1 each -- absolute irreducibility -- Killing-isotropic with nondegenerate cross pairing rank 16). CORRECTION recorded in the same FINDINGS: ad(z) spectrum is REAL (+-q, split torus, as required by split form e6(6)), reversing an earlier draft's wrong claim of compact u(1) (spectrum +-i*omega), which was a wrong-stratum artifact caught by the commit-gating lock before banking.
- **log says:** PROGRESS_LOG.md 2026-08-03 title: 'the coset leg verified ... the sector charge is COMPACT; B866's boundary fully closed.' This directly contradicts the FINDINGS.md's own correction section 4, which states the charge splits REAL (not compact) and explicitly calls the compact claim a mis-diagnosis from crashed runs at the wrong stratum, caught by the commit-gating lock BEFORE banking. The log entry as quoted was apparently written before or without incorporating that correction and was never itself corrected in the log text.
- **reader note:** Strong two-leg computation (one exact, one high-precision numeric, one modular cross-check) with a real self-caught error corrected before banking -- exactly the kind of process the locks are supposed to produce. The uncorrected log headline is a genuine propagation gap worth fixing even though the underlying math arc is sound.

## B960_l136_adjoint (main) — CONTRADICTION

- **claim of record:** verdict.claim_one_line: L136 CLOSED -- the adjoint-form hatch closes itself. det(Cartan matrix of E6)=3 -> centre of simply-connected form is Z/3; omega_1 (27's highest weight) not in root lattice, so centre acts nontrivially on the 27; adjoint form E6/Z3 has no 27 at all. Therefore the simply connected form is FORCED wherever the 27 (matter) lives, so B959's torality argument applies unconditionally and 'B959's no-go is complete within the centralizer class: no centralizer construction ... can produce chiral matter at the SM's rank.' Status: NEGATIVE.
- **log says:** B960/L136: the adjoint-form hatch closes itself; B959's no-go is now complete; LAW_MAP wall row upgraded from 'scope: simply connected' to 'unconditional within the centralizer class'. Discharges the single hatch B959 left open. Not contradicted in the log excerpt shown, but note B959's own later (2026-08-20) addendum found a DIFFERENT, non-adjoint-form hatch (the nilpotent stratum) that B960 never addresses and that undermines B960's 'no-go is complete' headline.
- **reader note:** A tidy closing of the specific hatch it names (adjoint-form elementary-abelian rank-2 subgroups), but its 'complete' headline over-generalizes beyond what it actually closed, and was later falsified by a different route (nilpotent stratum) without B960 itself ever being corrected.

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

- **claim of record:** PROVED — The commuting (θ,φ) ℤ₃×ℤ₃ are inner E₆ lattice automorphisms acting freely on the 27 as nine 3-orbits — the trinification triality — so no φ-eigenvalue can grade the 27.
- **log says:** B562 (2026-07-13): grounds 'P13 generations-via-triality (27 splits 9+9+9, the wrong 3)' in B298/B299. B565 (2026-07-14): 'B299's (theta,phi) IS Boyle's SO(8) triality (100% weight-level match)'. B579 (2026-07-14): correction — 'ω = B299's ℤ/3: VERIFIED' is flagged as NOT actually verified pending adjudication. B578 (2026-07-14): 'B299's (θ,φ) on the 27 = {1:9, ω:9, ω²:9} exact' (D8, adjudicated MOOT/computed).
- **reader note:** The core linear-algebra computation (Z3xZ3 acting freely on the 27) is genuinely reproducible and well-scoped as a refutation of a specific external claim; but the provenance of the (θ,φ) matrices is imported/unverified and the log shows an unresolved verification dispute on the closely related ω-identity claim.

## B300_cross_chat_sm_attempt (main) — DRIFT

- **claim of record:** NEGATIVE — The three-seat brave SM-from-axiom attempt found no new forcing; the eight external inputs compress to two walls (no coupling-strength emitted; the degree-3 carrier absent).
- **log says:** B1000/B1001 (2026-08-09): 'Three incompatible counts existed and no arc reconciled them (B717: 4 · B300: 8 · sweep: ~8).' The log flags B300's own count of 8 external inputs as one of three mutually inconsistent counts across the repo, sealed for correction (declared prior 'expected to correct B717').

## B309_kappa_unification (main) — DRIFT

- **claim of record:** PROVED — Unified four banked faces (existence, geometry, matter, quantum) as one commutator trace kappa=tr[a,b] not equal 2, with kappa-2=omega^2 and E6 uniqueness verified.
- **log says:** B1010 (2026-08-10): 'The κ-unification (B309/B518) — κ = tr[a,b] ... was in NEITHER consolidation: LAW_MAP cited it zero times, THE_FRAMEWORK contained zero κ.' B1200 (2026-08-28) later ties this κ to two other independently-derived faces ('FACE 1 the saddle ... FACE 2 the founding obstruction κ−2=u² ... FACE 3 the boundary structure').
- **reader note:** The core algebraic identity (kappa=tr[a,b]=u^2+2, with the two evaluations at u=0 and u=omega) is trivially checkable and correctly framed as a consolidation rather than new physics; the exceptional-group-uniqueness fact is asserted from an uncommitted Sage session rather than shown.

## B342_z3_trimaximal_symmetry (main) — DRIFT

- **claim of record:** claim_one_line: "The object's Z/3 is the (standard) trimaximal symmetry, but its would-be TM2 prediction theta_12 = 35.7 degrees is disfavoured by data relative to TM1." status: NEGATIVE
- **log says:** 2026-07-15 log: 'B322 ... and B342 (the ℤ/3-DFT circulant's TM2 already data-disfavored) were contextual prior art missing from B630's MB12'; 2026-08-30 log: 'B342 goes to the value-negative record, never the paper' — both consistent with the NEGATIVE verdict, but neither log entry notes that B343 (same batch) explicitly supersedes B342
- **reader note:** B342's own content is an honest negative (TM2 disfavoured by data), but it is a superseded intermediate result whose own verdict record does not point forward to B343's correction — a reader of B342 alone would not know its TM2-vs-TM1 framing itself was retracted, not just its ranking.

## B357_e6_boundary_restriction (main) — DRIFT

- **claim of record:** verdict PROVED: 'All six E6 deformation classes restrict nontrivially to the cusp (rank 6/6), the image is Lagrangian, and one universal tau = the cusp shape governs every block.'
- **log says:** 2026-07-02: rank 6/6 certified; Lagrangian image; universal-tau identity tau=-2sqrt(3)i matching cusp shape to 12 digits. IMPORTANT LATER CORRECTION (2026-07-03, 'depth-2 bending is theta-graded'): 'the universal-tau does NOT persist at depth 2; B357's identity is an order-1 rigidity, now sharply bounded' — the universal-tau claim is explicitly narrowed to leading (first) order only by a later probe. Also 2026-07-03 Promotion Audit holds B357 in the same dps-100 computer-assisted class as B352/B353/B370.
- **reader note:** The headline universal-tau result is narrower than the arc's own text states once later work (depth-2 probe) is taken into account — a genuine DRIFT between what this arc's committed files claim and what the project's later record shows. No physics observable named; purely structural math.

## B390_criterion_tensor (main) — DRIFT

- **claim of record:** PROVED: 'Seam brightness is decided by the local theta models at q=3 and q=5 alone (12/12 plus an out-of-sample pass), with dark pairs attributed by an exact rank-2 pairing.'
- **log says:** PROGRESS_LOG.md 2026-07-04 has exactly 1 entry confirming G1 (tensor identity 12/12), G2 (locality 12/12) and out-of-sample PASS ((2,5) predicted dark, verified dark) — matches session-1 FINDINGS; the session-3 attribution addendum is NOT separately logged.
- **reader note:** The strongest arc in this batch methodologically — a real registered out-of-sample prediction that passed — but the progress log under-documents the arc's own later self-correction (the attribution redo), a minor DRIFT in the other direction (log says less than the arc established).

## B393_cancellation_mechanism (main) — DRIFT

- **claim of record:** PROVED: 'Dark pairs annihilate termwise rather than by cancellation, with the exact law: s-darkness holds iff the 5-side never donates sqrt5 to an imaginary product.' (verdict json also carries a creates_law_corrected block dated 2026-08-29.)
- **log says:** PROGRESS_LOG.md log_index has only 1 entry, from a much later (2026-08-29) B1214 re-audit noting B393 as one of 'thirteen real laws recovered' during a creates_law audit — the original 2026-07-04-era banking entries for K1-STRONG and the product-field law are NOT present in the indexed log excerpts.
- **reader note:** A methodologically careful arc that explicitly caught and fixed its own broken first instrument (subfield-coordinate spectra silently dropping content) via a bright-control sanity check before banking the real result; the log excerpt available here just happens to only capture a much later meta-audit mention, not the original work.

## B397_last_census_facts (main) — DRIFT

- **claim of record:** NEGATIVE: 'Both registered local forms of the (2,3) stabilizer are killed (no pointwise sigma_19-fixing, no power-relabel intertwiner) so the stabilization is aggregate, and the inter-model sigma_sqrt5 trace-conjugacy fails, being intra-model only.'
- **log says:** PROGRESS_LOG.md 2026-07-04 (W-C session 1) is the only indexed entry mentioning B397, but it concerns a DIFFERENT claim (the class-group/Hilbert-class-field split-covariance prediction, 'σ_cl pairs slot↔−3block AND B382-face↔B397-face') than this arc's actual FINDINGS content (the (2,3) stabilizer kill and the sigma_sqrt5 trace-conjugacy correction) — the log entry appears to reference an earlier or different facet of B397 not present in this arc's file set.
- **reader note:** Genuine negative results with mostly exact committed data, but one intermediate script (relabel_search.py) was run inline and never committed, so part of the exhaustive relabel-search claim is not independently reproducible by a stranger from the repository alone.

## B399_wall_scale (main) — DRIFT

- **claim of record:** PROVED: 'The seam's 1/12 recruits the golden boundary while the singles' 1/12 is purely generic; the singles tower refines rather than generates scale, and at the 1215 rung Σ=1 and e₂=−1/48 are exact.'
- **log says:** e3 = cos(2pi/9)/864 EXACT later closes 'B399's wall-scale question' (2026-07-23 log entry); a review flags B399's second failed e3 attempt (Jul 9, UNSTABLE) never folded back into triple_id.json.
- **reader note:** Genuinely computed multi-prime CRT reconstruction of a deep-tower value with an honest partial-result banner (e3 pending) at time of writing, but the verdict is PROVED despite an open sub-question, and the log shows the eventual e3 closure happened outside this arc's own committed files — a provenance gap a stranger cannot fully retrace from this directory alone.

## B411_field_dictionary (main) — DRIFT

- **claim of record:** NEGATIVE: 'The gamma-prime field dictionary is killed: it is multi-valued on generic cells and determines the field only on the boundary cells.'
- **log says:** 2026-07-04: hint sweep (B411) — the local/emergent dichotomy; naive field-dictionary killed but localizes the direction, Pi_H is the boundary between local/derivable and emergent/aggregate layers. LATER (B418/TW4, 2026-07-04 same-day entry): B411's 'work upstairs' hope REFUTED — the mirror is not cell-local even in Q(zeta60).
- **reader note:** A well-documented negative-with-payload: a naive dictionary hypothesis is killed but the failure mode is used to name the productive direction (Pi_H as local/emergent boundary); that follow-up hope is itself later refuted in an appended update within the same file, which is good (visible) practice even though the verdict JSON doesn't carry the update forward.

## B412_tower_measure (main) — DRIFT

- **claim of record:** PROVED: 'The single-seed tower is an exact mass-conserving refinement: each parent splits into a cyclotomic orbit summing to it, with trace-zero innovations (an Iwasawa-type measure).'
- **log says:** 2026-07-04: 'what else' (B412) — the tower is a refining MEASURE (Iwasawa-type); exact: mass=1 frozen, parents split into cyclotomic orbits summing to them, innovations trace-zero. Also B741 (2026-07-21) provenance sweep LOCATES B412 as pointing to 'the B399/B408/B426 contraction chain, locked' rather than an independently reproducible cell.
- **reader note:** This is a synthesis/reframing arc, not a computation: it restates already-banked numbers from four other arcs under a new organizing lens (Iwasawa-type measure) with zero independent code or test of its own — verdict PROVED is generous for a directional/interpretive finding with no dedicated reproducibility artifact.

## B414_generation_structure (main) — DRIFT

- **claim of record:** NEGATIVE: 'The Z/3-generations reading fails its privilege test: the object's core multiplicity is Z/2 (class number of Q(sqrt(-15))), and no canonical frame exists.'
- **log says:** 2026-07-04: the structure reframe (S044/B414) — honest engagement with 'we have to see it'; same-day, B422 log entry notes 'B414's last in-object frame door closes; the frame is external.' A 2026-07-24 log entry notes 'B414-r re-decides on a non-vacuous gate' (a later re-decision).
- **reader note:** The core finding (Z/3 is not the privileged multiplicity; Z/2 from the class group is) is a genuine, exact structural fact, well-connected to the earlier no-canonical-frame result; but a later log entry ('B414-r re-decides') suggests this arc's verdict may have been revisited elsewhere without an addendum appearing in this arc's own committed files — a provenance gap worth the seat's attention.

## B426_scale_lever_closed_form (main) — DRIFT

- **claim of record:** The seam-envelope ratio has the exact cubic closed form (3a^2+4a-1)/10, and every Galois-invariant functional of its orbit is <1 — no invariant growth. | PROVED
- **log says:** Chat-2's G1 handoff VERIFIED exact against banked B372 coefficients; B426 later repaired (boundary p*=5.5932; two phrases retracted; two-referent scale-wall note) at 2026-08-14.
- **reader note:** The closed-form computation is solid and reproducible, but the arc's headline claim of record is a retracted overclaim left standing in the two files a reader consults first — a real correction was made and filed, but not propagated into the sealed verdict.

## B451_thermo_d4_resonances (main) — DRIFT

- **claim of record:** claim_one_line: "The trace map's leading Ruelle resonance equals the escape rate gamma = 0.4415, certified by three independent estimators after the banked 0.51 was shown to be an early-window artifact, with a certified primitive-orbit table to n=8."; status: verdict PROVED
- **log says:** Progress log entries B850 and B852 (2026-08-02) state that B451 computed a HORSESHOE, that a uniformly hyperbolic system's pressure function is analytic BY THEOREM, and that B451's setup 'was structurally incapable' of finding a phase transition -- explicitly framed as a critique of what kind of question B451's instrument could ever answer, though the log also says this does NOT reopen B451's own escape-rate/spectral-gap numbers.
- **reader note:** The gate-value correction chronicle (catching B186's own early-window bias, then re-certifying via independent algebra) is a genuinely strong verify-don't-trust example. But the later progress log casts real doubt on the broader interpretive frame this arc sits inside (a uniformly hyperbolic model cannot exhibit a phase transition by theorem) -- a caveat this arc's own files never surface, so a reader relying only on this directory would miss it.

## B465_monodromy_intake (main) — DRIFT

- **claim of record:** PROVED — The 8-4-3 monodromy spectrum is exact and fully derived from Fricke's tr(A1A2)=15 plus Egorov, and the SU(3)/SU(4) readings fail at the eigenspace level.
- **log says:** Three log entries: (1) a later repair-wave note that 'B465-r re-committed the E4 universal it was repairing'; (2) that same repair item resolved as 'B465-r -- the false universal det(sigma-I)=5 at every level AND STAGE scoped to stage l=0'; (3) a REVIEWS.md line placing B465 in the residue-saga scope (B465-B471) alongside the Relation campaign.
- **reader note:** A rigorous, cross-prime-verified exact computation that explicitly refutes a hoped-for SU(3)/SU(4)/Pati-Salam physics reading at the eigenspace level rather than merely failing to match it -- a genuinely disciplined negative result. The log-index drift (B465-r) could not be resolved against this arc's own committed content and should be checked against whatever arc actually carries the 'det(sigma-I)=5' claim.

## B471_chain_verification (main) — DRIFT

- **claim of record:** PROVED — tr[A_m,A_n] = 2 - (mn(n-m))^2, so (golden, silver) is the unique metallic pair whose commutator is parabolic and closes the cusp.
- **log says:** Three entries: (1) 2026-07-24 note that 'The B471 heredity conjecture is now a THEOREM (explicit lattice)'; (2) a Wave-6 note listing B471's 'metallic commutator trace identity with its iff that the golden-silver pair is the unique parabolic one' as one of four items re-verified and promoted to a theorem/law registry; (3) a Review 32 correction noting cc initially 'banked a classical result without its attribution' by presenting the identity as harvested, but that 'B471's own FINDINGS is scrupulous about this' -- explicitly citing Cohn 1955/Markov/Fricke as the classical source, with only the metallic-body READING as novel.
- **reader note:** A carefully self-correcting arc (two honest corrections to an incoming exploratory scout's claims, including a genuine theorem upgrade with closed-form proof and controls) that is explicit and scrupulous about literature attribution (Cohn 1955, Markov, Fricke) throughout, which the log's Review 32 entry confirms was later needed to correct a downstream harvesting error made by a different summarizing process -- the arc itself is not at fault. Purely structural/arithmetic; no measurable physical quantity is proposed.

## B489_self_interaction_tower (main) — DRIFT

- **claim of record:** NEGATIVE — The cyclic-cover tower's laws are classical and verified, but its SM reading is refuted (abelian DGG at every level), claim 4c is false, and the arithmetic echoes are numerology.
- **log says:** Later stabilized (B767, 2026-07-23/25): 'B489 STABILIZED: the cyclic-cover tower has DGG rank 2n-1 for ALL n — structural topology + the Binet identity (torsion=(phi^n-phi^-n)^2>=5 for n>=2), SnapPy-verified n<=16; the kill is no longer underproved.' Promoted to LAW_MAP as 'THE CYCLIC-COVER RANK LAW'.
- **reader note:** The claim here is only verified n<=8 with no committed witness in this arc, but the log shows the same claim was later independently stabilized to ALL n via a clean Binet-formula proof (B767) — so DRIFT is benign here (a later, separately-recorded strengthening of an honestly-scoped original claim), not misrepresentation.

## B516_golden_3d_ladder (main) — DRIFT

- **claim of record:** PROVED — "Golden 3d self-reference is golden-specific (only phi keeps x->x(1+sqrt x) Pisot), while the 'three dimensions from a Pisot cap' reading is dead."
- **log says:** log (2026-07-11 entry) groups B516 with B515/B517 golden-3d reopening; a later entry (B742, 2026-07-21) lists "B516's previously-asserted dim-5 Pisot counterexample" among 30 kills EARNED in a negatives hunt — suggesting the dim-5 claim was itself later scrutinized/killed as a claim, separate from the golden-specificity claim.
- **reader note:** The arc's own author explicitly flags "my binary-only scans falsely showed 0 golden at dim 3 AND dim 5" as a self-caught error, which is good, but a later log entry appears to describe a further kill of the dim-5 claim itself that this seat could not locate in-batch to reconcile against the still-standing FINDINGS text.

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

## B909_frame_arc (main) — DRIFT

- **claim of record:** verdict PROVED: 'THE FRAME ARC BANKED... THE COMPACT MEASUREMENT THEOREM VERIFIED WITH THE CORRECTED INSTRUMENT -- at kappa's genuine roots, FIVE (root,prime) pairs including the fully-split 40039, the compact wall centralizer types uniformly dim z=30, derived>=28, z cap core=18, center 2: z=so(8)+u(1)^2... THE LAW_MAP SECTION-F PENDING ROW: ALL FOUR DEBTS PAID.'
- **log says:** PROGRESS_LOG 2026-08-06: 'B909: THE FRAME ARC BANKED -- the CMT verified with the corrected instrument; the stale-septic catch; the LAW_MAP pending row paid whole. The arc whose absence was cc3's most-urgent audit item, closed.' But a LATER entry (2026-08-08, B958) states: 'B909's directory ships only cmt_correct.py and results.json, with no frame or M12 construction anywhere' and 'B909 verified [section LVIII] by RUNNING THE INCOMING MATERIAL, not by rebuilding on this bench' -- i.e. B909 did NOT independently construct the frame/M12, contrary to how 'verified' reads in the earlier banking entry. A still-later entry (2026-08-08, B978) found B958's premise itself wrong: 'the frame could not be rebuilt without the solo seat's definitions was FALSE -- the definitions were in CMT_DRAFT.md section 2, and B911 had already built the frame; I inspected B909 only' -- so the 'no independent construction anywhere' claim about the programme was itself an absence-claim error (conflating B909 with B911).
- **reader note:** The claim of record rests on a script that cannot be run as committed (a corrupted open() call), and the project's own later audit trail disputes whether this arc did independent construction at all versus re-running inherited material -- a live, self-acknowledged uncertainty in the log that the arc's own FINDINGS/verdict do not reflect. Physics content is structural (Lie-algebra centralizer typing); no observable is named.

## B933_spinor_hejhal_design (main) — DRIFT

- **claim of record:** verdict PROVED, instrument:true; claim_one_line: 'THE SPINOR-HEJHAL DESIGN + A SUCCESSFUL FEASIBILITY PROBE (exploratory, double precision, UNSEALED ...) ... the probe ALREADY RESOLVES A SPECTRUM: first Dirac eigenvalue bracket |lambda_1| = 2.97455058 +/- 1e-6 ... THE LITERATURE BLANK HELD: no prior computed Dirac eigenvalue on ANY hyperbolic 3-manifold.'
- **log says:** 2026-08-06 PROGRESS_LOG: 'the FIRST DIRAC SPECTRUM ON ANY HYPERBOLIC 3-MANIFOLD at probe grade' and restates |lambda1|=2.97455058, 8 digits, three instruments, dim-2 kernel. A 2026-08-07 REVIEWS.md Review 40 entry separately flags that B933's own COMMIT MESSAGE called the probe 'a first on H3' as an unqualified priority sentence resting on an unrecorded-depth literature sweep -- the same review that flagged B922's similar overclaim. An R47 action item ('R47-9: the B933 Dirac correction (owed; the web seat's verified J-commutes)') is listed as still OPEN/owed, not yet resolved as of the read log.
- **reader note:** A real, carefully-designed numerical probe (a Dirac/spinor-Hejhal collocation on m004) with an honestly-labeled exploratory/unsealed status and a documented literature-sweep caveat, but the arc_verdict.json's 'the literature blank held' phrasing outruns the FINDINGS text underneath it, and a flagged priority-claim correction from the review process does not appear resolved inside this arc's own committed record.

## B948_relay_ssb_sweep (main) — DRIFT

- **claim of record:** verdict=PROVED; claim: relays the solo seat's response to B942 (withdrawal of two of its own sections downstream of the dead beta=1 clause), reports a dead-clause sweep across knowledge/philosophy/speculations/story (found CLEAN -- the retracted clause never leaked there) and one stale surface (docs/LAW_MAP.md's B723 row, now superseded); distinguishes a surviving theorem (B736-P2's zeta_K pole fact) from the dead claim it neighboured; records the observer's mechanism as newly OPEN.
- **log says:** 4 entries corroborate the relay and sweep exactly as described; B1004 later finds the retraction still had NOT fully propagated corpus-wide (a retracted clause live in five places across the B500-B800 band), which this arc's 'rooms clean' finding did not anticipate since it only swept knowledge/philosophy/speculations/story, not the full arc corpus.
- **reader note:** A pure record/editorial arc reporting an unwitnessed sweep as clean; the project's own later corpus-wide audit (B1004) found the retraction the sweep was chasing was in fact still live in five places, which this arc's narrower scope did not catch and did not flag as a limitation.

## B949_ignorance_map (main) — DRIFT

- **claim of record:** verdict=PROVED; claim: reads the atlas query tool over 865 mined frontier probes, ranks obstacle-type resolution rates, finds 'source_free' (the Origin Axiom itself) at 0/1 resolved but correctly recorded as a dead direction rather than a blind spot; identifies 'bridge_construction' (5/14, 8 dead) as the real objective frontier; registers L131 (is axiom A7 discharged by B945's Klein-group finding?) explicitly as NOT claimed, citing B945's own word-level limit as the reason for caution.
- **log says:** 4 entries; B979 later closes L131 NEGATIVE, finding A7 IS load-bearing after all (the answer was already stated in section 5 of UNIQUENESS_THEOREM.md, which this arc did not read before registering L131) -- log calls this 'the fourth instance today of declaring open what is banked' across several arcs that day.
- **reader note:** A useful self-correcting census (catching its own near-miss on 'source_free') but the registered L131 lead was itself an instance of the day's recurring failure mode (declaring open what the corpus already answered a section later in the same file), caught by a subsequent arc rather than this one.

## B950_sm_spec_ledger (main) — DRIFT

- **claim of record:** verdict=PROVED; claim: writes docs/SM_SPECIFICATION_LEDGER.md as the first inventory of what the Standard Model itself requires (gauge structure, Z/6 global form, 19/26/28 free parameters, forced-vs-measured split); catches on its first pass that the programme's own banked headline 'su(3)+su(2)+u(1)^3 = the Standard Model algebra' (B892) has dimension 14, not the SM's actual 12, an overstatement by two abelian factors; registers L132 (which u(1) is hypercharge).
- **log says:** 11 entries, the most-cited item in this batch; log records this correction as opening the rank-obstruction line pursued through B952-B954, and separately (B978) records it as one of 'three instances in one day of declaring absent what already existed' (the global Z6 form B950 called 'not addressed' had in fact been derived by B862).
- **reader note:** A valuable and correctly-caught overstatement in the programme's own headline result (14-dim algebra mislabeled 'the Standard Model algebra'), but the correcting document itself repeated the same absence-without-sweep error one section later, caught only by a subsequent arc the same day.

## B959_nontoral_rank4 (main) — DRIFT

- **claim of record:** verdict.claim_one_line (UNCHANGED since 2026-08-08, NOT updated to reflect the addendum): OUTCOME NO-GO (simply connected form), sealed preregistration passed. Inner involutions (all 63 sign-gradings) fix full Cartan -> rank 6 always. Outer automorphism tau swaps 27<->27bar nodes so Fix(tau) makes the 27 self-dual/real -- closes F4 and C4 at once. A4/D5/S5 elementary-abelian rank <=2 -> toral by Steinberg (simply connected form) -> rank 6. 'The object cannot reach chiral matter at rank 4 by any centralizer construction' [this headline is superseded by the 2026-08-20 addendum below, but the verdict.json text itself still reads this way]. Status: NEGATIVE.
- **log says:** B959/L133 outcome NO-GO: every route to rank 4 makes the 27 real (simply connected form); banked-identity gate passed (dim Z=16, reproduced on same instrument as B958); upgrades B952's 'closed by absence' toward 'closed by proof', with the adjoint-form hatch (discharged later by B960) as the honest remaining gap. Later (2026-08-20, per this arc's own addendum) the audit seat's state-the-relation flag plus B1098/B1100 opened a NILPOTENT stratum (non-simply-toral, A2-class continuous holonomy, centralizer su(3)+su(3) rank 4) that B959's Steinberg-torality argument never covered, and B1100 computed the 27 complex there -- so the headline is now re-scoped to 'every TORAL route'.
- **reader note:** A carefully self-scoped no-go with an honestly-named remaining hatch (adjoint form), later shown by the arc's own addendum to have an additional hatch (nilpotent stratum) that actually opens -- but the machine-readable verdict record was never corrected, so any downstream row citing B959's unqualified claim_one_line is citing a claim the arc's own later addendum contradicts.

## B961_frame_instrument (main) — DRIFT

- **claim of record:** verdict.claim_one_line (verdict PROVED, instrument:true): THE FRAME INSTRUMENT -- frame.py provides ad(v), killing(), centralizer(S), killing_perp(S), derived(S) as exact operations over e6, wrapping B854's Chevalley structure constants. self_test() reproduces four banked numbers from scratch: Killing form symmetric, rank 78 (nondegenerate); dim Z(su3_colour)=16 (matches B958); A2+A1 Levi dim/derived/centre = 14/11/3 (matches B892, B951); Killing-perp of Cartan = 72 = 78-6. First run of derived() had a real sympy rref() pivot-column/row indexing bug (silently wrong-dimensional space), caught by the banked-number gate. Does not attempt to guess/reconstruct the solo seat's frame/floor/M12 (deliberately deferred).
- **log says:** B961/L135: THE FRAME INSTRUMENT built on this bench, its own self-test caught a real bug in it; reproduces four banked numbers (rank 78, dim Z=16, Levi 14/11/3, perp-of-cartan 72); explicitly does NOT guess the solo seat's frame/floor/M12, deferring that -- and this deferral was later shown wrong by B978, which found the solo seat's frame definitions already existed in CMT_DRAFT.md sec.2 (already built by B911) and that B958/B961 never checked before deferring.
- **reader note:** This is the strongest arc in the batch on the reproducibility axis: real committed exact-arithmetic code, a self_test cross-checking four independently-sourced banked numbers, and a documented real bug caught by that cross-check -- genuine belt discipline, though the instrument still imports its base structure constants from B854 rather than deriving the Chevalley basis itself.

## B983_grounding (main) — DRIFT

- **claim of record:** verdict PROVED, instrument true; claim: builds three governance artefacts (COMPUTE_THE_PROGRAM.md defining the quantifier discipline, THE_LADDER.md with 30 negatives-as-rungs graded BLIND/HOLE/BROKEN/BOUNDED/OPEN, WORKING_RULES.md section 0) in response to five same-day instances of declaring open/absent what the repo already held.
- **log says:** the grounding: COMPUTE_THE_PROGRAM.md defines the term; THE_LADDER.md maps the negatives as 32 graded rungs; WORKING_RULES.md section 0 binds both.
- **reader note:** This is the corpus's meta-governance instrument, not a physics result -- it exists entirely to prevent the seat from re-declaring banked results as absent, and explicitly states it 'proves nothing about the object.'

