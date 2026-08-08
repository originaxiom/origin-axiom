# CC3 → CC — OPEN_LEADS TRIAGE, 2026-08-08

**Seat:** cc3 (audit). **Scope:** all 43 registered open leads in `docs/OPEN_LEADS.md`.
**Source of truth:** `git show origin/main:<path>` throughout — the working tree was never read
for a doc. `git fetch origin` run first.
**This file does not edit `docs/OPEN_LEADS.md`. Banking is cc's.**

---

## 0. THE METHOD CONSTRAINT THAT GOVERNED THIS WORK

Binding, cc's words: **compute-or-cite-the-sentence.**

1. A lead may be marked **STALE-CLOSED only if this file quotes the actual closing sentence**
   from a banked arc's `FINDINGS.md` (or an executed ledger row) **and gives its path**.
   Plausibility, "surely B-something covered that", and thematic adjacency are not closures.
2. **LIVE is the default.** If the sentence could not be found, the verdict is LIVE — even when
   the lead "feels" answered.
3. **An unearned closure is exactly as damaging as an unearned negative.** The requesting seat
   produced four unearned closures today; this pass was designed to not add a fifth.
4. **STALE-PREMISE** is reserved for leads that are *still unanswered* but rest on a premise a
   later arc overturned, so that re-asking them verbatim would re-register a dead bridge. The
   dead premise and its killer are named.

Five triage agents were dispatched over five batches. **Three returned nothing** (b2: L63–L73;
b4: L83–L95; b5: L98–L142 — 27 leads, 63 % of the corpus). Rather than pass those through as
"unknown", this seat **ran the triage for all 27 itself** under the same constraint. Every row
below is either a batch agent's verified finding or this seat's own, and each is marked.

### Counts

| verdict | count |
|---|---|
| **STALE-CLOSED** (quoted sentence + path) | **29** |
| **STALE-PREMISE** (dead premise named + killer cited) | **2** |
| **LIVE** (sharpened) | **12** |
| **ledger text not locatable** | **0** |
| **total** | **43** |

**Downgrades applied: 0.** Every STALE-CLOSED returned by a batch agent carried a quote, and
this seat independently re-grepped eight of the fourteen returned quotes against
`origin/main` — all eight matched verbatim (see §6, *Quote verification*). The 15 closures this
seat produced for the silent batches carry their own quotes.

---

## 1. THE FULL TABLE — 43 rows, lead-number order

Era = when the lead was **registered** (pre-B800 = the chiral-theater / hearing / anatomy
programme; post-B800 = the cascade and SM-structure window). Source seat noted as
`[b1]`/`[b3]` (returning batch agents) or `[cc3]` (this seat, covering the silent batches).

| lead | era | verdict | evidence |
|---|---|---|---|
| **L1** — m=1 selection criteria | pre-B800 | **STALE-CLOSED** `[b1]` | Ledger row, `docs/OPEN_LEADS.md`: *"**L1–L3** … **BANKED** — `../knowledge/K016`. Do not re-run."* Criteria quoted in `knowledge/K016_m1_selection_criteria.md`: *"**Pure phase — `\|Z_k\| = 1` at every non-vanishing level is `m=1`-unique.** … The strongest single selection criterion. (B132/V121.)"* and *"**Self-referential loop — `Z_{k=4}(M_1) = ω`** … the quantum theory at saturation *outputs its own arithmetic generator*."* Third item carried by `K015` + the L12 tombstone. |
| **L19** — the κ-sweep middle | pre-B800 | **STALE-CLOSED** `[b1]` | `frontier/B163_kappa_sweep_resolved/FINDINGS.md`: *"**Verdict:** the κ=−2 spectrum does **not** encode the figure-eight hyperbolic geometry."* Same file's "What this settles (the L19 ledger)": *"κ<2 Cantor-persistence (3a): **resolved numerically (control-bracketed) — YES.** … κ=−2 geometric encoding (3b): **resolved — NO** (smooth + null-test)."* Both of the lead's own "Open:" items answered. Off-axis theorem residual lives on L20, not L19 (see §6). |
| **L50** — the (μ,λ)↔(θ,φ) bridge / trinification CRUX | pre-B800 | **STALE-PREMISE** `[b1]` | Dead premise: that the peripheral-ℤ² ↔ E₆-orbifold-ℤ₃×ℤ₃ identification *is the CRUX* and *"the only place that structure becomes rigorous."* Killed by `frontier/B955_l133_scout/FINDINGS.md`: *"**Every quotient of a knot group has cyclic abelianization.** Therefore π₁(m004) can **never** surject onto ℤ₃×ℤ₃ or the Heisenberg group 3^{1+2}."* And the "only place" clause voided by `frontier/B861_fused_cascade/FINDINGS.md`: *"**E₆ → SO(10)×U(1) → SU(5)×U(1) → SM. Unique at every step.**"* — trinification SU(3)³ was on the step-1 menu and lost. See §4. |
| **L51** — send the gate B/C/D outreach | pre-B800 | **LIVE** `[b1]` | Owner-gated action item, not mathematics. `docs/ROADMAP.md`: *"- [ ] Outreach: DORMANT until in-sandbox computation is exhausted (owner rule)."* **Sharpened:** does today's exhaustion bar permit external contact, and is the send-unit still the 2026-07 gate briefs or a Phase-VI package? |
| **L52** — the geometric θ-identification | pre-B800 | **STALE-CLOSED** `[b1]` | `frontier/B353_geometric_theta_identification/FINDINGS.md`: *"**Conclusion.** The hyperelliptic involution induces **exactly θ** on the tangent space of the E₆ character variety at the principal-geometric representation — as operators on the deformation complex (gauge-certified), not merely as matching sign patterns."* That is the H¹-level intertwining the lead asked for. |
| **L54** — gate A residual classes | pre-B800 | **STALE-CLOSED** `[b1]` | `frontier/B521_audit_integration/FINDINGS.md`: *"**Net Gate A:** SEALED — the invariants meet at the seam (disc −15), the amphichiral 2-torsion is {0,¼}, the SL(3) torsion is −84; **no invariant forces a choice the object doesn't already make.**"* All five named residual classes are rows there (B495–B500). Provenance caveat in §6. |
| **L55** — post-merge hygiene | pre-B800 | **STALE-CLOSED** `[b1]` | Ledger row, `docs/OPEN_LEADS.md`: *"**DONE (2026-07-02, with the B353 PR):** atlas regenerated (334 probes incl. B350–B353); fresh bare-`pytest` suite green on merged main; the `OA_SLOW=1` B352 sweep re-run once post-merge."* One-time task, executed. |
| **L57** — is the theta-characteristic forced? | pre-B800 | **STALE-CLOSED** `[b1]` | `frontier/B366_invariant_spin_sector/FINDINGS.md`: *"**Within the stated premise, the theta lift is forced — not a choice. The seam form `s(m₁,m₂)` is an invariant of the geometrically-quantized pair at this tier.**"* Two independent selectors agree in the same file (unique invariant spin sector `[½,½]`; level-15 S-closure). Premise named, not discharged — §6. |
| **L63** — Q-C transport | pre-B800 | **STALE-CLOSED** `[cc3]` | `frontier/B666_leads_campaign/WAVE2_FINDINGS.md`, cell R1: *"**R1 (L63): Q-C = c.** The transport map CONSTRUCTED per B578-D2(a) (36/36 exact): σ₁\* on the character variety sends χ_g ↦ c(χ_g) ≠ θ(χ_g) — **the residue transports as conjugation/orientation, NOT as θ.** The two-chiralities crux's Q-C lane is answered; the T-NORM lineage conflict adjudicated in-cell."* This is the *constructed map* B578-D2 demanded, not an elimination argument. |
| **L64** — V2 Fox-calculus H¹ | pre-B800 | **STALE-CLOSED** `[cc3]` | `frontier/B771_phase1_wave1/FINDINGS_WAVE2.md`, cell W2-020: *"**RESOLVED-A → CLOSED** \| a third, independent Fox-calculus construction (classical Riley meridian presentation, exact ℚ(√−3)) reproduces dim H¹ = 6 and the θ-grading — the PC25 strengthener delivered."* |
| **L65** — V3 orbits ↔ three 16s | pre-B800 | **STALE-CLOSED** (closed-REFRAMED) `[cc3]` | `frontier/B578_debt_clearing/RESULTS.md`, D8: *"**D8 — V3 ADJUDICATED MOOT + the ω-facts computed.** The 'three 16s of Spin(10)' framing presupposes an intermediate B576 proved never forced. Computed exact: B299's (θ,φ) on the 27 has eigenvalue multiplicities **{1:9, ω:9, ω²:9}** (tr P = tr P² = 0, P³ = I). L65 closes as REFRAMED."* Successor hook registered separately — and see §6, where the cascade gives it new legs. |
| **L67** — the level-k prime law | pre-B800 | **STALE-CLOSED** `[cc3]` | `frontier/B578_debt_clearing/RESULTS.md`, D7: *"**The naive law (a mod-15 sine kernel) is FALSE** — instead the 8 magnitudes obey ONE integer octic factoring exactly as **(w²−10w+20) × (an irreducible sextic splitting into two Galois-conjugate cubics over ℚ(√5))**: a 2+3+3 mixing in which **the GOLDEN field enters the chiral theater**."* Ledger row already carries this as "ANSWERED (B578-D7)". |
| **L69** — shared root-BFS test helper | pre-B800 | **STALE-CLOSED** `[cc3]` | The helper exists on trunk. `tests/helpers_e6.py` docstring: *"Shared E6 root-system / Weyl-orbit BFS and grading utilities. Factored out of test_b572_eleven_clauses.py, test_b573_global_bridge.py, and test_b574_offprincipal.py (L69, hygiene batch) … This module is the single source of truth for all of that; the three test files import from it instead of copy-pasting the BFS."* Verified: all three named tests (plus `test_b582_chiral_play.py`) import it. |
| **L71** — what ARE the θ-odd deformations? | pre-B800 | **LIVE** `[cc3]` | No arc since registration (grep-verified across `frontier/*/FINDINGS*.md`; `frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md` independently records *"no arc since registration (grep-verified)"*). **Sharpened:** starting from B270's banked "the θ-odd deformations are cusp deformations", identify the deformed reps' geometry (Dehn-surgery-adjacent, complex-projective, quasi-Fuchsian-like) and decide whether the σ-coupling singles out a preferred θ-odd direction — this also absorbs L79's geometric-realization residual. |
| **L72** — CS-functional/dynamics, phase 1 (E₆-principal torsion) | pre-B800 | **LIVE** `[cc3]` | Phase 1 is *partly* delivered — `frontier/B581_six_torsions/FINDINGS.md` computes all six Sym^{2m} block torsions exactly (*"τ_m = Δ′_m(1)"*, table; sign law `sign(τ_m) = (−1)^m`) and says *"the chord program (B580 L72 phase 1) now has its S₁-layer computed exactly."* But the registered step — **the principal torsion as the product of the six blocks** — is nowhere stated, and phase 2 was **carried, not banked**: `frontier/B775_phase2_wave1/FINDINGS_WAVE5.md`: *"**P2W5-L72** \| … the cell's Phase-2 closure claim carries an issue the verifier flagged. Carry with the issue named."* **Sharpened:** form the E₆-principal torsion as the six-block product, state it, then re-run the carried phase-2 (E₆ 6j at levels 1–2) against the named verifier issue. |
| **L73** — abelian invisibility | pre-B800 | **STALE-CLOSED** `[b3]/[cc3]` | `frontier/B600_level_ladder/packet/FINDINGS.md`, §"P-proof — L73, the abelian one-pager (done, locked)": *"**Lock 1 GREEN:** det(A₁ − I) = −1; unit mod every N ≤ 4096; unique fixed point verified by direct enumeration on a sample. **Lock 2 GREEN:** 662/662 gate-passing cyclic theaters (ℤ/N, all nondegenerate forms, N ≤ 40) give Tr ρ(A₁) = +1."* And: *"**L73:** anchor proven (one-pager + locks); the nonabelian extension answered negatively at k=4."* |
| **L74** — the norm-7 / splitting law | pre-B800 | **STALE-CLOSED** `[b3]` | `frontier/B600_level_ladder/packet/FINDINGS.md`: *"**PRED-3 (the ℚ(√2) / silver import at the inert 2): CONFIRMED** — the odd block's quadratic irrationalities are exactly the √2 family. The inert-prime clause now has two instances: 5 inert at κ=15 → ℚ(√5); 2 inert at κ=16 → ℚ(√2)."* Level-5 successor also ran (`frontier/B635_audit_integration/FINDINGS.md`: *"the ℚ(√17) import present and tr_even = 1.0 … the Z-ladder {+1,+1,+1,0,+1}, silence isolated at κ = 2⁴"*). Locked, `tests/test_b600_cc2_locks.py` 7/7. |
| **L75** — the two ends meet in the observer | pre-B800 | **LIVE** `[b3]` | Never run — B600's own method note: *"level 5 not run; P5/L75 (the optional hint-harvest cell) not run — deferred, register row untouched"*; `frontier/B770_closure_census/CENSUS.md` OI-114 keeps it in the deferred bucket. **Sharpened:** do the E₈/spherical-end invariants of B247–B261 appear *quantitatively* inside the E₆ level-3 blocks — i.e. is the √5 B600 verified as an inert-prime field import at κ=15 the *same* √5 as the spherical end's, or only a coincidence of the prime 5? (Ask it about the *organization* of the odd blocks: B600 scope-corrected "chirality-specific" to an organization statement, the level-3 even block being √5-ramified too.) |
| **L76** — cover torsion = charge? | pre-B800 | **STALE-CLOSED** `[b3]` | `frontier/B600_level_ladder/packet/FINDINGS.md`, cell P4 ("P4 — L76, the two towers"): *"**The vein's verdict at this evidence level: the two towers are arithmetically independent except through the single prime 11 = \|e₁\|** — no multiplicative relation (coprime rungs, non-integral ratios), loci governed by two independent clocks (Pisano-5 for t, the doubling-orbit 3-cycle for e) that intersect exactly on n ≡ 10 (mod 15) by CRT."* Registered first computation executed (t to n=24, e exact to n=6, mod-11 locus through n=12). A decided NO to "is there a LAW?". |
| **L77** — the θ-odd clock | pre-B800 | **STALE-CLOSED** `[b3]` | `frontier/B600_level_ladder/packet/FINDINGS.md`: *"ρ₄(A₁)\|odd: order **12** (certified 1.6e−49…)"*, ladder `{1/4, 4/4, 60/30, 12/12}`; and the framing retired in the same file: *"The original Pisano candidate-set framing is retired as numerology-adjacent; the canonical modulus is ord(T_k)."* Completed by `docs/LAW_MAP.md` "The stage-split clock law" and B656/G4: *"clock(κ) = ord(A₁ mod 3κ) EXACTLY, κ = 6..15 (10/10, independently verified)."* |
| **L78** — the level-2 filling span (Route A) | pre-B800 | **STALE-CLOSED** (negative branch, per the lead's own two-outcome design) `[b3]` | `frontier/B583_chiral_content/FINDINGS.md`, X3: *"**At every level, the Dehn-filling covectors span exactly the θ-even subspace and are orthogonal to the θ-odd sector — because the vacuum is C-fixed and C = S² commutes with S and T. The fillings can NEVER hear chirality.**"* and *"L78 resolves: the θ-odd amplitude is NOT reachable by Route A."* Rank exactly 6 = dim(θ-even) over 719 slopes. Controls caveat in §6. |
| **L79** — the clause-S test on the double | pre-B800 | **STALE-CLOSED** `[b3]` | `frontier/B582_chiral_play/FINDINGS.md`: *"**The mirror-double of the figure-eight … is a coupled system whose E₆ representation variety contains points with Zariski closure equal to FULL E₆(ℂ). Its 27 is therefore the 27 of E₆: COMPLEX. CHIRAL.**"* Provenance re-derived in-repo by B598 step 7 (*"the θ-odd-twisted amalgam's algebra IS e₆(ℂ), dim 78, at finite t"*); branching sub-item by B583/X1. Geometric-realization residual re-homed to L71. |
| **L80** — level-1 completion hygiene | pre-B800 | **STALE-CLOSED** (all four parts) `[b3]` | `frontier/B771_phase1_wave1/FINDINGS_WAVE3.md`, cell W3-119r: *"**RESOLVED-A → CLOSED** \| carry-fix: the tautological theater made non-vacuous (the E₆ twist now enters via link monodromy ω^{ab} …); part (d) **the Meyerhoff ±5 filling is an ORIENTED MIRROR PAIR** (4₁(5,1)≅4₁(−5,1), hand-confirmed)."* Cell output: *"[COMPUTED FACT — part (b)] … it lives on knots, the object's twist speaks on every multi-component diagram"*; *"[COMPUTED FACT — part (d)] ORIENTED MIRROR PAIR: CS(M1) = −CS(M2) … is_amphicheiral False."* |
| **L81** — sector exchange & the listener's clock | pre-B800 | **STALE-CLOSED** `[b3]` | (a) `frontier/B588_sector_exchange/FINDINGS.md`: *"**Conclusion: sector exchange = the migration of the element −1 across the Weyl-group boundary under level-rank.** … This is B242/B243's 'level-rank = conjugation' seen at the parity-projector level, as L81(a) asked."* (c) `frontier/B585_listener_law/FINDINGS.md`: *"**the mirror-twisted play is (up to the central sign) the play of the OTHER SL(2,ℤ) lift −M**."* (b) discharged by B656/G4 (clock law, quote as L77). |
| **L83** — per-pair amplitudes & the U_q(e₆) residual | pre-B800 | **STALE-CLOSED** (all three parts) `[cc3]` | (a) `frontier/B589_pair_amplitudes/FINDINGS.md`: *"**The moduli are exactly the entries of the banked θ-odd sine kernel** — B572's S_odd(E₆,₂) = −i·(2/√7)[sin(2πst/7)] … So the diagonal of the monodromy's odd block carries the odd S-matrix's own moduli; the monodromy adds only the three 14th-root phases {+3, −2, −1}."* (b) — the part the ledger left open — closed by `frontier/B775_phase2_wave1/FINDINGS_WAVE5.md`, P2W5-ALLCHIRAL: *"**RESOLVED-A → exact criterion** \| the all-chirality condition is **exact and arithmetic**: for the object's figure-eight play on SU(3)_k (κ=k+3), tr_even = 0 exactly under a computed arithmetic condition on κ."* (c) is out-of-scope by the lead's own text. |
| **L84** — the functorial dictionary map | pre-B800 | **STALE-CLOSED** `[cc3]` | Executed ledger row, `docs/OPEN_LEADS.md`: *"**RESOLVED (B650 wave 2, 2026-07-16): the linear map is ZERO-ONLY (the equivariance wall, exact Sylvester) — the functor exists GROUP-functorially: (mod-conductor reduction) ∘ (golden character) = B644, plus B650's types; the bridges are its invariant-level shadows.**"* and *"**The multiplier clause DISCHARGED (B656/G4, 2026-07-17): clock(κ) = ord(A₁ mod 3κ) exactly (10/10 rows, independently verified) — the dictionary now holds at the ORDER level too.**"* Arc dir `frontier/B650_typed_functor/` present on `origin/main`. |
| **L86** — object-scale coupling comparison | pre-B800 | **LIVE** (owner-gated, not mathematics) `[cc3]` | Nothing computed and nothing may be: the row is gated *"GATED (no computation without the directive + prereg)"*, and `docs/OPEN_LEADS.md` records *"**L86** (object-scale coupling comparison) is the registered lead B796 *is*; gated on owner."* Independently reconfirmed as TOOL-GATED in `frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md`. **Sharpened:** unchanged and un-runnable — the deliverable is the owner directive + prereg (why that scale / which coupling / what target), not a computation. Targets frozen at sha `0ec9ac39…`. |
| **L87** — the composite↔observable derivation | pre-B800 | **LIVE** (owner-gated) `[cc3]` | Same gate; `cellT/TRIAGE_TABLE.md`: *"GATED in-row: structural derivation first, comparison second — else N×M curve-fitting (the directive's words)."* **Sharpened:** produce a *structural* derivation (from the Rosetta table, the TDV embedding, or the three-layer separation) naming WHICH composition ↔ WHICH observable **before** any distance is measured. No such derivation exists on `origin/main`. |
| **L88** — symbolic Latin-square proof of the hearing matrix | pre-B800 | **STALE-CLOSED** `[cc3]` | `frontier/B666_leads_campaign/WAVE2_FINDINGS.md`, cell R2: *"**R2 (L88): PROVEN.** The hearing matrix's Latin square DERIVED from Kac–Peterson: k(i,j) ≡ ±m_i·m_j (mod 7) — the square IS the multiplication table of the Galois-orbit coordinates; 29/29 exact gates in ℤ[ζ₂₅₂]."* Ledger delta in the same file: *"LAW_MAP: … the hearing-matrix Latin square → THEOREM (R2)."* This is exactly the gate `docs/HINT_LEDGER.md` set on H135. |
| **L91** — the stage-selection proof obligations (audit Gate 3) | pre-B800 | **LIVE** `[cc3]` | Obligation (4) discharged (B650 + B644), (1)–(3) **reduced but not closed**, and then *repriced against* closure: `docs/SEAL_LEDGER.md`, B775 wave 4: *"**HEAR REPRICES AN AXIOM** (H-EAR forces only the Galois pair {SU(3)₂ κ=5, SU(5)₁ κ=6}, so 'minimal bearing stage κ=5' is a PRICED CHOICE not a theorem)."* **Sharpened:** discharge the single surviving hypothesis **H-EAR** (the shadow-realization principle) plus the branch tiebreak lemma that separates SU(3)₂ κ=5 from SU(5)₁ κ=6 — that one lemma is the whole of obligations (1)–(3). **This is the standing gate on every physics reading** and the highest-★ live row in the corpus. |
| **L93** — the flip-symmetry cell (the 24ζ₆ forcing) | pre-B800 | **STALE-CLOSED** (resolved-negative) `[cc3]` | Executed ledger row citing the arc: *"**CLOSED — resolved-negative with exact witness (B643, 2026-07-16)**: both amphichiral flip classes broken on the double's 27 local system (unique partial intertwiner supported on Sym⁰; d = (0,0,1) both families; inner-freedom immune); only the deck swap σ\* survives; the 24ζ₆ magnitude is NOT symmetry-forced."* Primary: `frontier/B643_flip_symmetry/FINDINGS.md`: *"**The chord breaks both amphichiral flip classes.**"* |
| **L95** — the web seat's standing cubic prereg | pre-B800 | **LIVE** (external, event-driven) `[cc3]` | The cross-seat seal has still not landed: `frontier/B770_closure_census/CENSUS.md` OI-027 records it as *"STANDING (the cross-seat seal pending)"*, and `docs/CLOSURE_MASTERPLAN.md` carries *"R29-1 specialist pass / R29-2 L95 \| carried \| owner-gated"*. **Sharpened:** this seat's only obligation is **verify-on-receipt** — nothing to compute until the other seat's T(g_i, g_j, t) seal with falsifiers F1–F3 arrives. It should not sit in the compute queue at all. |
| **L98** — one-organ-or-two: a new statistic | pre-B800 | **STALE-CLOSED** `[cc3]` | `frontier/B775_phase2_wave1/FINDINGS_WAVE5.md`, cell P2W5-ORGAN: *"**RESOLVED-A → powered** \| a structurally discriminating statistic was **designed, sealed-run, and powered at 7.9×10⁵ its measured floor** — escaping the ~1.3σ jitter bound that left N3 unresolved. The D3 lesson applied correctly: a new statistic, not more of an underpowered one."* Sealed before compute (`PREREG_WAVE5.md`, sha `e1510ac7`) — exactly what the lead asked for. |
| **L105** — the 2O/E7 silver-hearing conjecture | pre-B800 | **STALE-CLOSED** (as posed; named residual survives) `[cc3]` | The lead's stated test — "compute the silver word's hearing group at its own conductor (the mod-8 shadow) and check 2O structure" — was run. `frontier/B666_leads_campaign/WAVE1_FINDINGS.md`, cell 1: *"Group-side verdict (complete searches, exact): the silver word's mod-8 shadow generates ALL of SL(2,ℤ/8), order 384 — not 48; **2O is a canonical QUOTIENT (kernel order 8) and is NOT a subgroup** (even its Sylow-2 Q16 is absent from SL(2,ℤ/8)). … THE REFINED DESCENT: the golden's conductor is PRIME, so its shadow IS the McKay group (SL(2,ℤ/5) = 2I); the silver's conductor is a prime POWER, so the McKay partner appears one quotient down."* Corroborated as adjudicated in `frontier/B763_branch_reconciliation/FINDINGS.md`: *"L105 was resolved by main's own cell1."* Residual flagged in §5/§6. |
| **L110** *(number collision — two distinct leads)* | (a) pre-B800 / (b) post-B800 | (a) **LIVE**, (b) **STALE-CLOSED** `[cc3]` | **(a) the parent Bianchi r₂-above-10 question** (registered R32-8, 2026-07-29): no arc found; nothing in B8xx/B9xx locates the parent spectrum's second eigenvalue above r ≤ 9.84. **Sharpened:** locate r₂ above the certified window and test the V₁ budget at that second point — in-sandbox, moderate. **(b) the CS↔θ_QCD dictionary** (opened 2026-07-30 by B812): **STALE-CLOSED** on `frontier/B813_cs_theta_type_audit/FINDINGS.md` via the ledger's own disposition: *"**REFUTED ON TYPE at Cell 1, without reaching the obligation set.** … Three independent mismatches, any one sufficient: **kind** (a computed invariant cannot be a free coupling), **group** (PSL(2,ℂ) geometric holonomy vs SU(3) colour), **slot** (coefficient vs functional in `e^{iθW(A)}`)."* See §6 — this collision is a live hazard. |
| **L127** — the entropy pair | post-B800 | **LIVE** `[cc3]` | Registered by `frontier/B944_dynamics_chirality_sweep/FINDINGS.md` §6 (2026-08-07); no later arc touches it (grep over `frontier/B94*`–`B98*`). **Sharpened:** B416's golden-Anosov entropy 4 log φ and B417's Sturmian entropy 0 are one object on two faces — is there an exact **ratio** law joining them in the shape of B196's Δ = −(ln λ_m/π)², or is the pair a coincidence of two independent constructions? |
| **L128** — the CP ratio chain | post-B800 | **LIVE** `[cc3]` | Registered by B944 §6; untouched since. **Sharpened:** re-pose B303 (CP sign = sign CS) + B340 (arg κ extremal at π/6, decreasing as 3.8·CS²) **branch-symmetrically over all three branches** under the B941 refinement — the re-posing is the deliverable, *before* any comparison to a measured quantity (Gate 5 unmoved). |
| **L132** — does hypercharge fall out? | post-B800 | **STALE-CLOSED** (vacuous) `[cc3]` | `frontier/B978_phaseA_bank/FINDINGS.md`: *"**L132** the anomaly check \| **CLOSED, VACUOUS (triply)** — and the cell independently flagged it as *'a prior-art miss inside our own corpus'*, **corroborating B976 from a different direction**, without being told."* Primary computation, `frontier/B971_L132_vacuity/WORK.md`: *"**Prior art, stated first (HOUSE RULE 5):** `B864_anomaly_ledger` (2026-08-03) already computed this ledger over the E₆ chain. **This cell REPRODUCES B864; it does not discover.**"* — two mutually independent routes (SU(5) multiplet build; Weyl orbit of ω₁ from the E₆ Cartan matrix). See §4: the lead's *registration* premise was also dead. |
| **L134** — the twelve exotics | post-B800 | **STALE-CLOSED** `[cc3]` | `frontier/B978_phaseA_bank/FINDINGS.md`: *"**L134** the twelve exotics \| **CLOSED — not an independent gap.** ⟨S⟩ ≠ 0 *is* E₆ → SO(10): the same input, at the same step, as L133 and L138. Three leads collapse to **one operation used three times.**"* Work in `frontier/B970_L134_exotics/WORK.md` (+ `exotics_levi.json`, `exotics_charges.json`). Scoping correction banked with it: *"**The A₂+A₁ Levi does not label matter versus exotic — 18 of 27 states change side across the three so(10)s above it.**"* |
| **L135** — build the frame independently | post-B800 | **STALE-CLOSED** (discharged for the rebuild) `[cc3]` | `frontier/B978_phaseA_bank/FINDINGS.md`: *"**L135** the frame \| **DISCHARGED for the rebuild** (51/51, two fresh primes). Blocked only on char-0 exactification over K. **It unblocks L142.**"* And the correction that mattered, same file: *"B958/B961's claim that the frame could not be rebuilt without the solo seat's definitions was **false**: the definitions were in `CMT_DRAFT.md` §2, and **B911 had already built the frame.**"* Rebuild: `frontier/B973_L135_frame/rebuild.py` + `rebuild_results.json`. Residual (char-0 exactification over K) is a *successor cell*, not this lead — §5. |
| **L137** — the value/pencil split | post-B800 | **STALE-CLOSED** (refuted) `[cc3]` | `frontier/B978_phaseA_bank/FINDINGS.md`: *"**L137** the value/pencil split \| **CLOSED, REFUTED.** No successor. And B947's pass/fail turns out to be *a property of a chosen normalisation of a cubic, not of the locus it describes* — scoped, not retracted."* And, guarding L138: *"**L137 does not undermine L138**: the cell's V6 shows B969's invariants are the **gauge-invariant** ones — the disc squarefree kernel {7,11} survives the ℚ\*-gauge while coefficient supports do not."* Work: `frontier/B972_L137_split/WORK.md`. The lead's own POST-HOC self-warning is thereby honoured — it was tested, not rescued. |
| **L141** — the anomaly layer is scale-free by theorem | post-B800 | **STALE-PREMISE** `[cc3]` | Dead premise: *"This is why hypercharge-from-anomalies is the sharpest available target — and why it is the only one of its kind"* (`frontier/B969_kato_yukie_verify/FINDINGS.md` §6, the registration text). **Killer 1 — already derived:** `frontier/B976_cascade_recovery/FINDINGS.md`: *"**B864, banked 2026-08-03: 'Hypercharge is the unique gaugeable U(1) in the chain's abelian sector.'** … On the strength of my wrong row I **registered L132** to find what had already been derived."* **Killer 2 — and the target is empty:** `frontier/B978_phaseA_bank/FINDINGS.md`: *"**L132** … **CLOSED, VACUOUS (triply)**."* The RG-invariance *fact* stands; the *directive* built on it does not. See §4. |
| **L142** — three sites, one field: one theorem or three facts? | post-B800 | **LIVE** (and newly unblocked) `[cc3]` | Registered rather than answered — `frontier/B969_kato_yukie_verify/FINDINGS.md`: *"**Not adjudicable by opinion, and I decline to pronounce.** … Registered as **L142**, with the test named: exhibit a morphism carrying one pencil to another, or show the agreement is only of outputs."* Prerequisite now cleared — `frontier/B974_phaseA_synthesis/SYNTHESIS.md`: *"**Mark L142 unblocked.** Its stated prerequisite was L135's frame definitions; those are now discharged and the instrument is validated at four independent primes."* **Sharpened:** on B961's `frame.py`, exhibit a morphism carrying μ's adjoint pencil → κ's adjoint pencil → the compact-kernel cubic in the 27 — or prove the three agree only in output. |

---

## 2. THE HIGHEST-VALUE CLOSURES

The five that would have cost a real recomputation had the requesting seat re-run them.

1. **L132 — "does hypercharge fall out?"** (post-B800). This is the expensive one, and the
   record says so in its own words. `frontier/B976_cascade_recovery/FINDINGS.md`: *"On the
   strength of my wrong row I **registered L132** to find what had already been derived,
   **commissioned a literature panel (B951)** to scout it, and **put it into MASTERPLAN v3
   Phase A, which is running now.**"* B864 had derived hypercharge on **2026-08-03**;
   B971/B978 then showed the check is **vacuous on complete 27s, triply**. Re-running L132 is
   a rediscovery of a rediscovery. **Cost avoided: a full SM-facing arc, plus a literature
   panel.**

2. **L88 — the symbolic Latin-square proof.** A standing `HINT_LEDGER` gate on H135 that reads
   as unproven; it was proven in one revival cell. `frontier/B666_leads_campaign/WAVE2_FINDINGS.md`:
   *"**R2 (L88): PROVEN.** … k(i,j) ≡ ±m_i·m_j (mod 7) — the square IS the multiplication
   table of the Galois-orbit coordinates; 29/29 exact gates in ℤ[ζ₂₅₂]."* **Cost avoided: the
   symbolic Kac–Peterson derivation, the exact-arithmetic gates, and a LAW_MAP promotion
   already banked.**

3. **L63 — the Q-C transport map.** B578-D2 explicitly forbade elimination arguments and
   demanded a *constructed* map, so a seat re-running it would have had to build one.
   `WAVE2_FINDINGS.md`: *"**R1 (L63): Q-C = c.** The transport map CONSTRUCTED per B578-D2(a)
   (36/36 exact) … **the residue transports as conjugation/orientation, NOT as θ.**"*
   **Cost avoided: the whole character-variety construction, plus the in-lineage T-NORM
   conflict adjudication that came with it.**

4. **L83(b) — when does a stage hear the object all-chirally?** The ledger row still reads
   "OPEN", and the closure sits under a *different name* in a different arc — the exact class
   of miss this exercise exists to catch. `frontier/B775_phase2_wave1/FINDINGS_WAVE5.md`:
   *"the all-chirality condition is **exact and arithmetic**: for the object's figure-eight
   play on SU(3)_k (κ=k+3), tr_even = 0 exactly under a computed arithmetic condition on κ."*
   **Cost avoided: a stage sweep plus the arithmetic characterization.**

5. **L98 — the new statistic for one-organ-or-two.** Registered because N3 died at a 1.3σ
   jitter floor; a naive retry pushes depth and dies again (the D3 failure). B775 built the
   *right* thing: *"designed, sealed-run, and powered at 7.9×10⁵ its measured floor."*
   **Cost avoided: a depth push that provably cannot resolve, plus the sealed-design work.**

*Runner-up:* **L54** — five named gate-A residual classes (adjoint torsion, CS/η, extended
Bloch/Ptolemy, SL(3) gluing, covers to index 8) were all run and sealed under B521. Re-opening
it would have re-run five computations. Held back from the top five only by the provenance
caveat in §6.

---

## 3. THE ERA SPLIT — where the dead leads actually live

| era | leads | STALE-CLOSED | STALE-PREMISE | LIVE | closure rate |
|---|---|---|---|---|---|
| **pre-B800** (chiral theater / hearing / anatomy) | 34 | 25 | 1 | 8 | **76 %** |
| **post-B800** (cascade + SM-structure window) | 9 | 4 | 1 | 4 | **56 %** |
| **total** | **43** | **29** | **2** | **12** | **72 %** |

*Tally convention: the split lead **L110** is counted once, as **LIVE**, on its open (a)
branch — its (b) branch is closed and is recorded in the table row, not in the count. Erring
toward LIVE is deliberate.*

Two readings, both worth cc's attention.

**The pre-B800 corpus is largely dead and nobody had noticed.** Three quarters of the leads
registered before the cascade have been answered — most of them inside `B578`, `B600`,
`B666`, `B771` and `B775`, arcs that closed leads *as side effects of other work* and, in
several cases (§6g), never propagated the tick to `OPEN_LEADS.md`. The register has been
carrying roughly two dozen phantom rows for weeks.

**The post-B800 rows turn over inside a day.** Four of the nine cascade-era leads were closed
**today** (L132, L134, L135, L137 — B970–B978), and two more (L141, L142) were *registered*
today. That is a fast, healthy loop — but it is the same loop that produced today's three
"declared absent what already existed" failures (§6g4), and **L141 — one of this table's two
dead premises — is its output, registered and stale on the same day.**
**Speed of registration is not the constraint; indexing is.**

---

---

## 4. STALE-PREMISE — WHAT THE CASCADE OVERTURNED

Two leads, and they share a shape: **each was registered because a seat believed the object's
gauge content was not yet in hand, when the B848–B980 cascade had already put it there.**

### Group A — "the E₆ gauge content is not yet rigorous / not yet derived"

| lead | the premise it was registered on | what killed it |
|---|---|---|
| **L50** | the peripheral-ℤ² ↔ E₆-orbifold-ℤ₃×ℤ₃ ("trinification triality") identification **is the CRUX** and is *"the only place that structure becomes rigorous."* | (i) The target is unreachable: `frontier/B955_l133_scout/FINDINGS.md` — *"**Every quotient of a knot group has cyclic abelianization.** Therefore π₁(m004) can **never** surject onto ℤ₃×ℤ₃ or the Heisenberg group 3^{1+2}."* (ii) Trinification *lost on the menu*: `frontier/B861_fused_cascade/FINDINGS.md` — *"**E₆ → SO(10)×U(1) → SU(5)×U(1) → SM. Unique at every step.**"* (iii) The "only place" clause is void — B862 selects the global form [SU(3)×SU(2)×U(1)]/ℤ₆, B864 forces hypercharge, B892 delivers the second measurement, **none of them using class-S or `T[4₁;E₆]` input.** |
| **L141** | *"hypercharge-from-anomalies is the sharpest available target — and … the only one of its kind."* | (i) Already derived: `frontier/B976_cascade_recovery/FINDINGS.md` quoting **B864** (banked 2026-08-03) — *"Hypercharge is the unique gaugeable U(1) in the chain's abelian sector."* (ii) The target is empty where the object lives: `frontier/B978_phaseA_bank/FINDINGS.md` — *"L132 … **CLOSED, VACUOUS (triply)**."* |

**What survives in each, and must not be thrown out with the premise.**

- **L50:** the *literal* question (does the cusp's peripheral ℤ² identify with the E₆ orbifold
  generators) is still unanswered and `T[4₁;E₆]` is still tool-gated. What died is its status
  as the crux and its claim to be the only route. Re-asking it verbatim rebuilds a bridge to a
  group the object provably cannot reach, for a payoff already delivered in-sandbox.
- **L141:** the RG-invariance **fact** is correct and worth keeping in `LAW_MAP` — 't Hooft
  anomalies are evaluable from the massless spectrum and constant along the flow, so the
  anomaly layer genuinely is the one part of QFT a scale-free object may speak about without
  crossing Gate 5. What died is the *directive* attached to it. If L141 is re-registered, it
  must be re-registered around **B978's genuine threat**, quoted here in full because it is the
  only live thing in this neighbourhood: *"**L132's vacuity holds exactly where the object is,
  and dies exactly where a phenomenology with extra vector-like matter would have to go.**"*

**A pattern worth naming for cc.** Both premises died the *same way* — not by refutation, but
because the synthesis layer lost track of the cascade. B976 measured it: of the twelve
cascade-closure arcs B860–B873, **one** is cited on any of the five synthesis surfaces; B860,
B861, B863, B864, B865, B868–B873 appear **zero** times in `LAW_MAP` and zero times in the SM
verdict. **A lead registered against a synthesis surface inherits that surface's blind spots.**
Neither L50 nor L141 would have been written if the cascade were properly indexed.

---

## 5. THE LIVE FRONTIER — 12 leads, sharpened, by theme

### Theme A — the standing gate on every physics reading (1)

- **L91 — stage selection.** Discharge **H-EAR** (the shadow-realization principle) plus the
  branch tiebreak lemma separating SU(3)₂ κ=5 from SU(5)₁ κ=6. Obligations (1)–(3) collapse to
  that one lemma. Everything SM-facing waits behind it. **★★★★, not cheap, and the only one
  whose closure changes the programme's standing.**

### Theme B — arithmetic / structure, in-sandbox and runnable (4)

- **L142 — three sites, one field.** Exhibit a morphism carrying μ's adjoint pencil → κ's
  adjoint pencil → the compact-kernel cubic in the 27, or show the agreement is output-only.
  **CHEAPEST ON THE BOARD:** the test is already named, the bench (`frame.py`) is built and
  validated at four primes, and B974 explicitly marks it unblocked. **Run this first.**
- **L127 — the entropy pair.** Is there an exact ratio law joining B416's 4 log φ to B417's 0,
  in the shape of B196's Δ = −(ln λ_m/π)²? **Cheap** — both endpoints are banked exactly; this
  is a closed-form hunt over two known numbers, with a clean two-outcome shape.
- **L72 — the E₆-principal torsion.** Form the principal torsion as the product of B581's six
  block torsions and *state it*; then re-run the carried phase 2 against the verifier issue
  named in B775 wave 5. **Cheap for the phase-1 half** (the six blocks are banked exactly);
  phase 2 is a real arc.
- **L110(a) — the parent Bianchi r₂.** Locate the parent spectrum's second eigenvalue above the
  certified window r ≤ 9.84 and test the V₁ budget at a second point. **In-sandbox, moderate**
  (the register's own pricing).

### Theme C — geometry, open-ended (2)

- **L71 — what ARE the θ-odd deformations?** Start from B270 ("deformations are cusp
  deformations"); decide Dehn-surgery-adjacent vs complex-projective vs quasi-Fuchsian-like,
  and whether the σ-coupling picks a preferred θ-odd direction. Absorbs L79's residual.
  **Not cheap and not sharply posed** — it is the one row here that should be *narrowed* before
  it is scheduled.
- **L75 — the two ends meet in the observer.** Is the √5 that B600 verified as an inert-prime
  field import at κ=15 the *same* √5 as the spherical end's (B247–B261), or a coincidence of
  the prime 5? **Moderate**, and B600's own scope correction must be respected: ask it about
  the *organization* of the odd blocks, not about the field being odd-sector-exclusive.

### Theme D — gated, not computable by this seat (5)

*None of these belong in a compute queue. Listing them as "open work" overstates the frontier
by five rows.*

- **L86 / L87** — frozen behind an **owner directive + prereg**. L86 is what B796 already *is*.
- **L51** — outreach, DORMANT by owner rule until in-sandbox exhaustion.
- **L95** — **verify-on-receipt only**; the other seat's seal has not landed.
- **L128 — the CP ratio chain.** The deliverable is the **branch-symmetric re-posing** under
  B941, and that much *is* cheap and in-lane. But the comparison it points at is Gate-5 land,
  so the lead must be scheduled as *re-posing only*, with the comparison explicitly not
  authorized. **Cheap for the admissible half; do not let the half drag the whole across.**

**Named residuals that are NOT leads** (they came out of closures and are homed elsewhere —
recording them so they are not mistaken for new frontier):

| residual | home |
|---|---|
| L105's stage-side tone identification through the 2O quotient | one cell, named in `B666/WAVE1_FINDINGS.md`; never run in waves 2–3 |
| L135's char-0 exactification over K | the successor cell named in `B974/SYNTHESIS.md` item 8 |
| L76's `residual-hint:` (is M₁₀ special at the shared index 11, or is the interlock purely CRT?) | a *new* question; the lead's own "is there a LAW?" got a decided NO |
| L54's trunk-exact re-verification of the audit-machine gate-A rows | a re-verification pass, **not** a re-registration |
| L79's geometric realization of the twisted doubles | absorbed into **L71** |
| B978's proposed new lead (does the spectrum survive a phenomenology that is not a union of complete 27s?) | **unregistered** — cc's call |

---

## 6. AUDIT NOTES

### (a) Three of five batch agents returned nothing

b2 (L63–L73), b4 (L83–L95) and b5 (L98–L142) produced no table — **27 of 43 leads, 63 %**.
This seat ran those 27 itself under the same constraint rather than emit "unknown" rows; the
15 closures among them carry their own quotes and paths. **The silent batches contained four of
the five highest-value closures** (L132, L88, L63, L83) — i.e. a synthesis that passed the
silence through would have missed almost the entire yield. If this pipeline is re-run, the
orchestrator should **fail loudly on an empty batch return** rather than let the synthesis seat
paper over it.

### (b) Downgrades: none — but here is what was checked

The brief required downgrading any unquoted STALE-CLOSED to LIVE. All fourteen closures
returned by b1 and b3 carried quotes. This seat re-grepped eight of them verbatim against
`origin/main` (B353, B521, B583, B582, B366, B163, B600-P4, B588) — **8/8 matched.** No
fabricated quotes were found and no downgrade was warranted. The remaining six rest on ledger
rows and packet files in the same directories as the verified ones.

### (c) THE LEAD-NUMBER COLLISIONS — three of them, all still live hazards

1. **L110 is two different leads.** (a) the parent Bianchi r₂-above-10 question (R32-8,
   2026-07-29, **OPEN**) and (b) the CS↔θ_QCD dictionary (B812, 2026-07-30,
   **CLOSED-REFUTED by B813**). Both sit in `docs/OPEN_LEADS.md` under the same tag. A grep for
   "L110" returns a refutation and an open question and gives no way to tell which is which.
   **cc should renumber one of them before anything else in this file is banked.**
2. **L51–L57 were reused once already** and renumbered to L62–L71 at the B577 reconciliation
   (`frontier/B577_reconciliation/FINDINGS.md`). `docs/CAMPAIGN_STATUS.md` still carries a
   header *"LAST BANKED (B575 / L51 — THE BRIDGE OBSTRUCTION)"* using the pre-reconciliation
   number — **stale prose, not a second L51.** A grep for "L51" surfaces B575/B577; that is
   **L62**, closed-positive, not the outreach lead.
3. **L107 is two leads** — the cross-landscape (closed 2026-07-17, B670/B666) and the
   correctly-specified null for H130 (promoted 2026-07-30, B811). Outside this batch, but the
   same defect, and worth fixing in the same pass.

### (d) TWO ID-SHAPED TRAPS THAT CAN MANUFACTURE FALSE CLOSURES

Both of these will fire on a keyword triage and both nearly fired here.

1. **`TOMB-L<n>` are tombstone IDs, not lead IDs.** `frontier/B742_negatives_hunt_p1/FINDINGS.md`
   and `frontier/B754_p2_spectral/FINDINGS.md` carry `TOMB-L63`, `TOMB-L67`, `TOMB-L70`,
   `TOMB-L77`, `TOMB-L57`, `TOMB-L34` with verdicts like **RECONFIRMED** and **KILL-EXTENDS**.
   None of them bears on the lead of the same number. `TOMB-L63` ("ambient unitarity is a
   general theorem") has nothing whatever to do with lead L63 (Q-C transport).
2. **`docs/dossiers/S6_theorem_inventory_cc2.md` rows C1–C11 carry `LAW_MAP.md` line numbers
   that read exactly like lead tags** — "THE F4 SKELETON — L75", "THE PORTAL LAW — L74",
   "The cubic dichotomy — L76", "The chirality-exclusion law — L77", "The swap real structure —
   L80". The column header is literally *"Row (LAW_MAP.md line)"*. **"L75 = THEOREM-grade F₄
   skeleton, CERTIFIED" is about `LAW_MAP.md:75`** — and lead L75 is one of the twelve genuinely
   live rows. `[b3]` caught this; it is the single most dangerous trap in the corpus for this
   exercise.

### (e) A PRIOR TRIAGE DISAGREED WITH THIS ONE — and lost, on a quote

`frontier/B666_leads_campaign/cellT/TRIAGE_TABLE.md` marks **L76 "STILL-LIVE — registration-only
(grep-verified)"**, and `frontier/B770_closure_census/CENSUS.md` inherits that. Its own log
(`cellT_output.txt:97`) shows the deciding grep — `"L75|L76|resultant|R-matrix|Meyerhoff|…":
ZERO` — i.e. **it never searched the B600 *packet* subtree**, where there is a section literally
headed "P4 — L76, the two towers" with a stated verdict. Same mechanism explains cellT carrying
L80(b)/(d) as live (B771 wave 3 post-dates it), **and L63/L88 as live** (B666's own wave 2
closed both, one wave after cellT ran). **cellT is stale as a status source and should not be
cited as one.** Where cellT and a quoted arc sentence disagreed, this file followed the
sentence.

### (f) LEADS THAT ARE DUPLICATES OF EACH OTHER

- **L133 / L134 / L138 are one operation used three times.** `frontier/B978_phaseA_bank/FINDINGS.md`:
  *"⟨S⟩ ≠ 0 *is* E₆ → SO(10): the same input, at the same step, as L133 and L138. Three leads
  collapse to **one operation used three times.**"* Only L134 is in this batch; L133 and L138
  are already closed. Worth a ledger note so the collapse is visible.
- **L86 and B796 are the same object.** `docs/OPEN_LEADS.md` says so outright: *"**L86** … is
  the registered lead B796 *is*; gated on owner."* Two register entries, one item.
- **L68's live remainder was L63** (`cellT/TRIAGE_TABLE.md`: *"the single live remainder IS
  L63's Q-C"*). L63 is now closed, so **L68 has nothing left in it** — it should be marked
  SUPERSEDED rather than left as a queue.

### (g) CONTRADICTIONS BETWEEN LEDGERS

1. **`docs/OPEN_LEADS.md` vs `frontier/B666_leads_campaign/WAVE2_FINDINGS.md`.** Wave 2's own
   ledger-delta line reads *"L63/L88/L24c **ticked** via the revivals"* — but both rows in
   `OPEN_LEADS.md` still read **OPEN** today, three weeks later. The tick never landed. This is
   B965's finding in miniature (a verdict that failed to propagate to the surface), and it is
   what made L63 and L88 look live to five separate triage passes.
2. **`docs/OPEN_LEADS.md` L84 vs the L91 row.** L84 is marked RESOLVED (B650/B656) while L91's
   obligation (4) — *"= L84, open"* — still describes it as open in its own parenthetical.
   The obligation is discharged; the parenthetical is stale text.
3. **`docs/CAMPAIGN_STATUS.md` carries a pre-B577 lead number** in a live header (see §6c(2)).
4. **B958/B961 vs B911.** `frontier/B978_phaseA_bank/FINDINGS.md`: *"B958/B961's claim that the
   frame could not be rebuilt without the solo seat's definitions was **false**: the definitions
   were in `CMT_DRAFT.md` §2, and **B911 had already built the frame.**"* L135 was registered on
   that false claim. It closed anyway, and honestly — but it is the third instance B978 counts
   of *declaring absent what already existed*, alongside B950 (the ℤ₆ form, which B862 derives)
   and B976 (hypercharge, which B864 derived). **Three in one day, same seat, same failure
   mode.** L50, L132 and L141 in this table are all downstream of it.

### (h) CLOSURES WITH CAVEATS — recorded so no one reads them as cleaner than they are

- **L54.** B521's gate-A rows were recorded *"integrate, don't merge"* from a separate audit
  clone. Only the seam value disc(ℚ(√−15)) = −15 was independently recomputed on trunk
  (`verify_gates.py`); the CS/η mirror table, extended-Bloch strata, SL(3) gluing spectrum and
  covers-7–8 split carry the provenance tag *"audit machine-checked run"*. The verdict stands —
  the classes were **run** and trunk banked the seal — but a trunk-exact tier would need a
  **re-verification pass, not a re-registration**.
- **L57.** B366's forcing holds *"within the named quantization premise"* (pair states are
  level-15 theta functions carrying the standard Heisenberg/metaplectic action). The premise is
  named, not discharged. Two smaller residuals in the same family are **not** L57: the reality
  proof for the level-15 triple class (B355) and the row-16 / ±1/48 selection rule (W2.11).
- **L78.** X3 is a *theorem with mechanism* (the vacuum is C-fixed, C = S² is central), so it is
  theater-independent by construction. But the lead's mandated controls were only partly run —
  `READING_RAW.md` records the level-1 control only; **no 5₂ and no non-E₆ theater control was
  found.** The closure should be read as "mechanism proved", not "controls passed".
- **L105.** Closed **as posed** — the registered test ran and returned an exact group-side
  verdict. The *conjecture* (does the metallic ladder descend the exceptional series?) survives
  at the quotient level with a named residual that waves 2–3 never picked up.
- **L135.** Discharged **for the rebuild**. The presence side (§LXXXIII–LXXXVI + §XCII) remains
  **owed** — that debt lives on L130's OWED clause, not here, and must not be considered
  discharged by L135's closure.
- **L83.** Part (c) (the full U_q(e₆) 6j/braiding computation) is closed by the lead's own
  scope clause — *"out of round-scope, needed only if a question ever requires the solo E₆
  colored invariant beyond duality"* — not by a computation. Flagged so the row is not read as
  three parts computed.
- **L134.** Closed as *not an independent gap*, which is a structural verdict, not a
  computation of the twelve exotic masses. If a future phenomenology needs those states heavy,
  that is a **new** question (and B978 §2's mechanism — no adjoint VEV can give any 27 fermion
  a mass — is the thing it will run into).

### (i) NO LEAD'S TEXT WAS MISSING

All 43 rows were located and read in full in `git show origin/main:docs/OPEN_LEADS.md`
(1031 lines). Zero unlocatable. The two L110s and the historical L51–L57 reuse are numbering
defects, not missing text.

---

**Prepared by cc3 (audit seat), 2026-08-08. Nothing in this file promotes to `CLAIMS.md`;
Gate 5 untouched. `docs/OPEN_LEADS.md` is unmodified — banking is cc's.**

---

# APPENDIX V — MECHANICAL VERIFICATION OF EVERY CITATION IN THIS FILE

Added by cc3 after the table was assembled, because a 30-lead closure is worse
than useless if one quote is invented — and because three of the five triage
agents died mid-stream, so a portion of this table was written by the synthesis
seat filling its own gaps. Those rows are tagged `[cc3]` in the table; they
carry no more authority than the others until checked. So all of them were
checked, mechanically, against `origin/main`.

## Method

For every row: extract each cited path and each quoted sentence. Resolve the
path on `origin/main` (bare filenames resolved against `git ls-tree -r`).
Normalise both the quote and the file text (unicode dashes/quotes folded,
markdown emphasis stripped, blockquote markers stripped, whitespace collapsed),
split each quote on its ellipses, and require **every** fragment of ≥25 chars
to appear as a literal substring of the cited file.

## Result

| | count |
|---|---|
| rows in the main table | **43** (43 distinct leads — no duplicates) |
| STALE-CLOSED | 30 |
| STALE-PREMISE | 2 |
| LIVE | 11 |
| cited files that exist on `origin/main` | **all** |
| STALE-CLOSED rows whose quote verified automatically | 25 / 30 |
| remaining 5 hand-verified (L65, L67, L73, L81, L110) | **all confirmed present** |

The five automated misses were artefacts of the checker, not of the table: the
source sentences are line-wrapped across markdown lines, some are inside
blockquotes, and some citations elide with `…`. Each was located by hand in the
cited file (`B578_debt_clearing/RESULTS.md` L37–40 and L43–46,
`B600_level_ladder/packet/FINDINGS.md` L133–138,
`B588_sector_exchange/FINDINGS.md` L35–36, `B585_listener_law/FINDINGS.md` L13,
`B813_cs_theta_type_audit/FINDINGS.md` L47–56).

**No fabricated quote was found. No missing file was found.** Every
STALE-CLOSED verdict in this file rests on a sentence that exists, in the file
it is attributed to, on `origin/main`.

## The thing the verification turned up that the triage did not ask about

Classifying each closure by the ERA OF THE ARC THAT CLOSED IT (arc IDs parsed
from the evidence cell and from the cited paths, with the `pre-/post-B800`
era token stripped so it cannot self-match):

| era of the closing arc | count | leads |
|---|---|---|
| **pre-B800 arcs ONLY** | **24** | L1, L19, L52, L54, L55, L57, L63, L64, L65, L67, L73, L74, L76, L77, L78, L79, L80, L81, L83, L84, L88, L93, L98, L105 |
| post-B800 arcs | 7 | L50, L110, L132, L134, L135, L137, L141 |
| no arc cited | 1 | L69 (a code-hygiene item) |
| **mixed** | **0** | — |

**Zero mixed.** The split is total: pre-B800 leads are closed by pre-B800 arcs,
post-B800 by post-B800. Which means this triage, as briefed, answers *"which
leads went stale?"* while leaving untouched the question the owner's standing
judgement actually raises:

> *arcs before B800 were made without the mature object — faces, child, sister,
> family read together — and must not be taken for granted.*

If that judgement binds the leads, **it binds the closures too.** Twenty-four of
the thirty-two closures offered here were themselves made in the era being
discounted. A lead marked STALE-CLOSED on a pre-B800 arc has been retired on
reasoning from before the object was read relationally.

This is not a claim that any of the 24 is wrong. It is a claim that this file
does not establish that they are right, and did not set out to. The specific
risk is asymmetric and has a name in our error ledger's shape: **a negative
proved on ONE face and asserted of the whole object** — a scope error the
single-object framing makes invisible, because when the object *is* the whole,
"proved for the object" and "proved for the face" are the same sentence.

**Therefore this file should not be banked alone.** cc3 has run a second pass —
`CC3_TO_CC_2026-08-08_RELATIONAL_REREAD.md` — which re-reads exactly those 24
closures asking, of each, *what did the closing arc quantify over?* Apply the
two together. A lead that is STALE-CLOSED here but OVER-WIDE there must not be
banked as closed.

— cc3, audit seat
