# B578 — THE DEBT LEDGER
*Synthesis of the debt-clearing campaign. Verifier objections folded in per cell. All claims are structural/mathematical; no physics claims pass the firewall. Verdict vocabulary: CLEARED / PARTIALLY CLEARED / RETRACTION FIRED / BLOCKED / REFRAMED / VOID.*

---

## D1 — Massey third order (the PC26 gate) — **CLEARED, with one scoped correction**

**Owed.** Discharge the numerical conditionality of the banked B370/L53 third-order (Massey) obstruction (dps-100 mpmath) on the independent exact B575 gl(27) build — the same discharge B575 performed for B352 at second order. This was the gate for PC26.

**Computed.** MB13 correctly caught that L53 was already executed as B370 (W2.5); the job was reconcile-and-exactify, not compute-fresh. Exact over ℚ(√−3) on the B575 build: the third-order Massey class **vanishes exactly in all six exponent directions m ∈ {1,4,5,7,8,11}**, including both θ-odd escape directions u4, u8. Two independent extractions agree exactly; the order-2 convention gate matches B575's independently coded cup; vanishing is genuine exactness (raw C3 cochains nonzero: 96/315/456/456/315/456 of 729), not a machinery zero. Positive controls non-vacuous (e.g. obstruction values 1/16!, 1/22!; MB12 random-vector 6/6 nonzero). Smoothness of the local 6-fold is hardened to order 3, exactly. Verifier independently re-ran the build and jets and reproduced everything.

**Verifier objections (folded in, both accepted).**
1. *Runtime self-contradiction:* the correct figure is ~11.6 min (build ~5.9 + jets ~5.7), not "~7 min build-dominated."
2. *Scope overclaim on the secondary retraction:* the delta-class (indeterminacy) computation was mechanically run **only for m ∈ {4,8}** (12/12 checks). The claim "indeterminacy EXACTLY ZERO for all six directions, correcting B370's full rank table (0,1,1,3,4,4)" rests for m ∈ {1,5,7,11} on a plausible bilinearity corollary (B575's Q ≡ 0 polarizes), **not on a computed discriminating fact**. Per house rule, the broader correction is downgraded to *derived corollary, flagged*, until the remaining 4×6 delta-class checks are run.

**Verdict.** CLEARED — the primary debt (exact confirmation of B370, PC26 gate opened) is fully discharged. The indeterminacy correction is CLEARED for m=4,8 only.

**Remains.** [NEW OPEN N1] Run the remaining 4×6 delta-class checks for m ∈ {1,5,7,11} (machinery exists, cheap) before any OPEN_LEADS edit retracting B370's full indeterminacy table.

---

## D2 — Q-C residue transport (L63) — **BLOCKED; claimed proof overturned; L63 remains OPEN**

**Owed.** Answer L63/Q-C: how the B469/B303 orientation residue (−1)^((N−1)/2) transports through the B570 Klein-four ⟨θ,σ⟩ of the geometric holonomy.

**Computed.** The cell claimed a DONE elimination proof ("transports as σ, not θ"). The raw numerics are all genuine and reproduce (det(X_m) = −1 symbolically and at 10 sampled m; tr ρ(ab) = 5/2+√3i/2, disc −3; Jordan types; amphichirality; both cited locks pass).

**Verifier objection (decisive; verdict overturned).** No map is ever constructed from the B469 metallic-tower object (λ_m ∈ ℚ(√(m²+4)), *real* quadratic) into the structure θ and σ actually act on (trace field ℚ(√−3), *imaginary* quadratic). The "θ-type candidate" was an invented stand-in, so the elimination proves nothing about the real θ. Worse: the repo's own locked theorem **T-NORM** (docs/THEOREM_REGISTRY.md, from B469 BR-N) states N(λ_m) = −1 is **impossible in imaginary quadratic fields** — i.e. the residue's norm-realization is structurally forbidden on exactly the axis σ acts on. The headline conclusion contradicts its own cited canon. This is the same category-mismatch ("computed on the wrong object") that quarantined the sibling B570 C5+Q-C cell.

**Verdict.** BLOCKED. The DONE verdict is retracted at synthesis; the numeric re-verifications are kept as an appendix only.

**Remains.** L63 stays OPEN. [NEW OPEN N2] A genuine answer needs either (a) an explicit, derived embedding of the scale-axis object into the E6(ℂ)/character-variety structure with ⟨θ,σ⟩ acting on it, or (b) a reformulation of Q-C that does not require the norm-realization to cross incompatible quadratic-field types.

---

## D3 — Criticality triangle (B181 / B507 / B498) — **PARTIALLY CLEARED**

**Owed.** Reconcile three "criticality" results and supply the missing B507 lock (B507 had FINDINGS + prereg but no reproducer).

**Computed.** (i) B498's Q1b and B507's g_M(κ) proven **one structure at two resolutions** via the tower property of conditional expectation — an exact identity. (ii) The missing B507 lock **built from scratch** (leaf-parametrization Monte Carlo, no rejection); it independently reproduces κ* ≈ 0 (+0.0136 / −0.0019 across runs, within noise of B507's 0.001) and both of B498's exact gates (E[log mult_M] → 0, E[log mult_D] → −2). (iii) B181's γ established as a genuinely separate quantity; no in-repo theorem maps γ onto g_M. Verifier confirmed all scripts, seeds, numbers, and the MB13 citations exactly.

**Verifier objection (folded in, accepted).** The framing "same coordinate κ, different function, at fixed κ" is materially imprecise: B181's tested points require real λ (κ = 2+λ² = 3, 11), while B507/B498's entire analyzed locus is κ ∈ [−2,2] — corresponding to **purely imaginary λ** (per B162's own docstring). The domains are disjoint except at the degenerate boundary κ = 2 (λ = 0, trivial free Laplacian). The corrected statement: B498↔B507 unification is exact; B181 lives on a *disjoint locus* of the same character variety, and no comparison was ever computed. This strengthens, not weakens, the PARTIAL verdict.

**Verdict.** PARTIALLY CLEARED — B498↔B507 identity proven and B507's missing lock supplied (a genuine debt paid); the B181 leg is a corrected non-reconciliation, now with the honest domain-disjointness statement.

**Remains.** [NEW OPEN N3] Whether any principle connects spectral regularity at real-λ κ ≥ 3 to the verb-monoid flow on κ ∈ [−2,2] — currently nothing computed crosses the κ = 2 boundary. The new B507 reproducer should be committed as a lock.

---

## D4 — e3 reconstruction (B399 wall-scale) — **CLEARED, with one diagnosis downgraded**

**Owed.** Reconstruct the third elementary symmetric function e3 of the three census values, which had failed twice (triple_cubic.json UNSTABLE; recon_e3.py rerun), and adjudicate the preregistered sentinel test.

**Computed.** e3 = (ζ9+ζ9⁻¹)/1728 = 2cos(2π/9)/1728, root of x³−3x+1 scaled by 1728; minimal polynomial e3³ − e3/995328 + 1/5159780352 = 0. Verified **20/20 primes, zero exceptions**, for e1 = 0, e2 = −1/48, e3, and the full cubic-root identity on all three census values. **Sentinel adjudication FIRES NEGATIVE**: e3's arithmetic content (1728 = 2⁶·3³, disc 81 = 3⁴) involves only primes {2,3}; none of {17,19,31,79,167} appear. Synthetic control recovered exactly by the same pipeline. Verifier independently recomputed everything from the raw singles files, confirmed the recon_e3.py sign bug and the pf() hang diagnosis.

**Verifier objection (folded in, accepted).** The claim that *triple_cubic.json's* failure was also a wrong-field (ℚ(√5)) assumption was **asserted, not computed** — the generating script no longer exists, and the available evidence (single stored Fraction; AUDIT's "denominator equals a listed prime" signature) points instead to a plain under-determined rational CRT reconstruction. That diagnosis is downgraded to *unverifiable and likely wrong*. Only recon_e3.py's failure is demonstrated to be the wrong-field bug.

**Verdict.** CLEARED — e3 reconstructed exactly, sentinel negative earned, both preregistered tests adjudicated. The failure-autopsy of one of the two prior attempts is corrected in scope.

**Remains.** Nothing on e3 itself. Bank with the corrected autopsy language.

---

## D5 — "kubota" — **VOID (no such debt)**

The payload was the literal placeholder "test," and verifier confirmed by exhaustive grep that **no B578-D5 or "kubota" sub-cell exists anywhere in the repo**; the only Kubota–Leopoldt thread is the unrelated B519/B571 A2 item (itself already quarantined in BURIED_ITEMS.json). This entry is fabricated/synthetic input, carries no discriminating fact, and is **excluded from the tally**. Its "RETRACTION-NEEDED" verdict is itself unearned and void.

---

## D6 — S031 m=3 sealing (K₃ field) — **RETRACTION FIRED**

**Owed.** Port the B137 MB7 off-sublocus sealing method to m=3, premised on the B571-item-B2 / OPEN_LEADS-L68 "correction" that K₃ = ℚ(√13) is quadratic.

**Computed.** The premise is false and the retraction fires **against the B571/L68 correction itself**: fresh SnapPy+cypari at two precisions reproduces B125's banked verdict — K₃ is a degree-6 (see caveat), non-quadratic, non-imaginary-quadratic, non-arithmetic field. The "correction" conflated K_m (invariant trace field, imaginary quadratic only for m=1,2) with ℚ(√(m²+4)) (the unrelated real-quadratic fusion/metallic field, B127 M-4). 13 = 3²+4 is true — about the wrong field. B137's original deferral is **reinstated**; the "CORRECTED 2026-07-14" edit propagated into B137's FINDINGS must be reverted. The MB7 `_dist` test provably cannot port (it is an imaginary-quadratic rationality check). Verifier confirmed everything and **strengthened** the retraction: ℚ(√13) is totally real, and invariant trace fields of hyperbolic 3-manifolds are never totally real (Maclachlan–Reid, already used at B307) — a structural impossibility independent of any numerics.

**Verifier objection (folded in, non-fatal).** The specific **degree-6 minimal polynomial is less certain than stated**: SnapPy's canonical `trace_field_gens`/`find_field` route robustly yields an irreducible **degree-8** polynomial (stable 400–1500 bits), disagreeing with the custom shape-field construction's degree 6. Either way K₃ is non-quadratic (retraction unaffected), but the exact polynomial is not to be banked as settled.

**Verdict.** RETRACTION FIRED — retract B571-B2/L68's "K₃ = ℚ(√13)" and the downstream B137 edit; reinstate the original deferral, with the totally-real impossibility added as the decisive fact.

**Remains.** [NEW OPEN N4] Resolve the degree-6 vs degree-8 discrepancy for K₃ (likely a primitivity subtlety in the shape-field weighted-sum construction used by B125/B137's probe). [NEW OPEN N5] The degree-≥6 field-membership test for genuine m=3 sealing (PARI algdep/nfisincl route hit a real precision wall, honestly left open, not swept to NEEDS-SPECIALIST).

---

## D7 — E6 level 3 (L67, the "level-k prime law") — **CLEARED (negative earned exactly)**

**Owed.** Extend the C3 Kac–Peterson machinery from E6 level 2 to level 3 and test the L67 hypothesis that the θ-odd sector forms a clean single-modulus sine kernel (extending level 2's exact ℤ/7 kernel).

**Computed.** Full level-3 build (k+h∨ = 15): 20 integrable weights, θ-odd dim 8 (4 fixed + 8 swapped pairs), all modular gates pass at 1e-8–1e-13 (S unitary/symmetric, (ST)³ = S², S⁴ = I, S² = charge conjugation, 8000 Verlinde integers ≥ 0, independent q-Weyl cross-check). **L67 REFUTED-as-stated**: the 8 scaled θ-odd magnitudes w = 30|S_odd|² are the exact roots of one integer octic factoring as (w²−10w+20)·(irreducible sextic), the sextic splitting into two Galois-conjugate cubics over ℚ(√5) — a genuine 2+3+3 algebraic mixing of the composite 15 = 3×5, not a per-prime sine kernel. Monodromy ρ(A1)|odd is non-scalar of order exactly 60 (vs 1, 4 at levels 1, 2), angles an index-2 subgroup of (ℤ/60)*. Verifier reproduced everything **from scratch** including an exact-arithmetic pipeline (denominator-135 phases, unitarity to 1.6e-61, all 8 magnitudes digit-for-digit to 20 digits, octic factorization sympy-proven) — the kill is an in-sandbox exact discriminating fact.

**Verifier objections.** None fatal; the cell's own honesty flags (order-60/angle pattern numerical, not exact-theorem-derived) are accurate and stand.

**Verdict.** CLEARED — L67 closed by an exact refutation, replaced by a sharper structural fact (the ℚ(√5)/cubic 2+3+3 split).

**Remains.** [NEW OPEN N6] Derive the order-60 monodromy and the {n ≡ ±1 mod 5} angle set exactly (currently numerical). [NEW OPEN N7] What, structurally, the 2+3+3 ℚ(√5) split of KH = 15 = 3×5 is — the honest successor question to the dead "prime law."

---

## D8 — V3 triality/generations hook — **REFRAMED (moot + reproduces a banked negative)**

**Owed.** V3: "B299 triality orbits ↔ three 16s of Spin(10) under G_SM," plus the proposed reframe "(θ,φ) ~ multiplication by ω on the θ-odd plane; generations = ω-cycling."

**Computed.** V3 is **MOOT**: B576 (via L70) shows no D5 ≡ Spin(10) intermediate is ever forced — the deformed closure jumps from the F4-stable stratum directly to full E6; per B572 clause 9 the F4→Spin(10)×U(1) step is the external "unpaid weld." The reframe is **not well-posed**: it conflates B299's θ (order-3 Weyl element on the 27) with B576's θ-parity (order-2 fold label on the 78; blocks 9/17, which don't even size-match 27) — verified as genuinely distinct objects. What is true in the hook's spirit: (θ,φ) forces an exact 9+9+9 ω-eigenspace split on the 27 (trace 0, sympy eigen-decomposition) — literal "ω-cycling" — but this **reproduces the already-banked B298 negative** ("9+9+9 wrong size"): three 9-dim blocks, not three states. Verifier reproduced all numbers and citations.

**Verifier objections (folded in, both non-fatal).** (1) The atlas `card triality` step was decorative (card ignores its argument); the honest sweep citation is `revive B299`, whose surfaced motifs were checked and don't bear on the reframe. (2) "No Spin(10) intermediate" should be sourced to OPEN_LEADS L70's registry entry (where D5 ≡ Spin(10) is explicit), not to B576's literal text.

**Verdict.** REFRAMED — V3 closed as moot; the reframe adjudicated as a rediscovery of a banked negative; nothing new banked.

**Remains.** Nothing new opened; the class-S/T[4₁;E₆] bridge remains the standing CRUX for any 27↔78 transport.

---

## D9 — "hygiene" — **VOID (no such debt)**

Placeholder payload ("test"); verifier confirmed no D9 sub-cell exists anywhere in CHANGELOG, PROGRESS_LOG, or frontier. An unearned DONE on a nonexistent target. **Excluded from the tally.**

---

## D10 — V5/L66 global duality — **CLEARED**

**Owed.** L66/V5: globalize C2's SL(2,ℂ) biconditional — (A) all traces real ⟺ (B) ρ̄ ≅ ρ ⟺ (C) conjugates into a real form — to reductive G(ℂ), with the descent obstruction identified.

**Computed.** Delivered, with the obstruction pinned exactly to Tate cohomology Ĥ⁰(Gal(ℂ/ℝ), Z(G)) = ℤ/gcd(2,N) for Z = μ_N — the group-level Frobenius–Schur/Brauer ±1. **New sharp E6 fact: Ĥ⁰(Gal, μ₃) = 0** (gcd(2,3) = 1), so at E6 the biconditional holds **unconditionally** — the quaternionic obstruction cannot bite (cleaner than SL(2), where Ĥ⁰ = ℤ/2). The fig-8 E6 holonomy fails all three sides elementarily (tr Ad ρ(a) = 37437270+38799960√3·i non-real): its real-form failure is c-chirality, not cohomological; the theorem governs the deformed locus, where (A) is attainable and the gap⟺c-chirality duality is obstruction-free at E6. Verifier independently recomputed the Tate groups (N = 2,3,4,5,6,7,9,12), the SL(2) descent witnesses, the Sage FS indicators, confirmed the disclosed A1-helper bug as non-load-bearing, confirmed all predecessor citations genuine (globalized, not rediscovered), and — a strengthening — verified the intertwiner-centrality step is a correct proof for any Zariski-dense ρ, not a hand-wave.

**Verifier objection (folded in, minor).** "Galois acting by inversion on μ₃" was asserted without in-sandbox derivation; verifier checked the conclusion is **robust to either action** (trivial or inversion give identical Ĥ⁰ order for every N tested) — so the phrase should be softened, though the headline is unaffected.

**Verdict.** CLEARED — L66 closed positively; the E6-unconditional statement is the deliverable.

**Remains.** Process only: flip OPEN_LEADS L66 to closed and update PROGRESS_LOG/CHANGELOG/CAMPAIGN_STATUS in the banking PR (per standing docs rule); soften the "inversion" phrasing.

---

# HONEST TALLY

| Cell | Debt | Verdict at synthesis |
|---|---|---|
| D1 | B370/L53 Massey exactification (PC26 gate) | **CLEARED** (indeterminacy correction scoped to m=4,8) |
| D2 | L63/Q-C residue transport | **BLOCKED** — claimed proof overturned; L63 stays OPEN |
| D3 | Criticality triangle + missing B507 lock | **PARTIALLY CLEARED** (B498↔B507 proven, lock built; B181 leg disjoint-domain, uncompared) |
| D4 | e3 reconstruction + sentinel | **CLEARED** (one prior-failure autopsy downgraded to unverified) |
| D5 | — | **VOID** (fabricated placeholder; excluded) |
| D6 | S031 m=3 premise (K₃ = ℚ(√13)) | **RETRACTION FIRED** against B571-B2/L68; B137 deferral reinstated |
| D7 | L67 level-k prime law | **CLEARED** (exact refutation; sharper 2+3+3 fact banked in its place) |
| D8 | V3 triality/generations | **REFRAMED** (moot + rediscovered banked negative B298) |
| D9 | — | **VOID** (fabricated placeholder; excluded) |
| D10 | L66/V5 global duality | **CLEARED** (E6 unconditional) |

**Of 8 real debts: 4 cleared (D1, D4, D7, D10), 1 partially cleared (D3), 1 retraction fired (D6), 1 reframed (D8), 1 blocked with its claimed proof retracted at synthesis (D2). 2 submitted cells were void placeholders and are counted nowhere.** Two verifier interventions changed verdicts (D2 DONE→BLOCKED; D5's RETRACTION-NEEDED voided); every other cell absorbed its objections as scope corrections without losing its headline.

# NEW OPENS DISCOVERED

- **N1 (D1):** remaining 4×6 delta-class indeterminacy checks for m ∈ {1,5,7,11} before retracting B370's full rank table (cheap; machinery exists).
- **N2 (D2):** L63 reformulation — either a derived embedding of the scale-axis object into the ⟨θ,σ⟩ structure, or a version of Q-C that doesn't force the norm across incompatible quadratic-field types (T-NORM forbids the naive crossing).
- **N3 (D3):** whether anything connects the real-λ locus (κ ≥ 3) to the verb-monoid flow locus (κ ∈ [−2,2]); nothing computed crosses κ = 2. Plus: commit the new B507 reproducer as a lock.
- **N4 (D6):** K₃ minimal-polynomial degree discrepancy (6 via shape-field construction vs 8 via `trace_field_gens`) — non-quadratic either way, but unresolved.
- **N5 (D6):** the degree-≥6 field-membership test for genuine m=3 sealing (precision wall documented, not NEEDS-SPECIALIST yet).
- **N6 (D7):** exact derivation of the order-60 θ-odd monodromy and its {n ≡ ±1 mod 5} angle set (currently numerical).
- **N7 (D7):** structural meaning of the 2+3+3 ℚ(√5) split of KH = 15 — the earned successor to the dead prime-law.

# BANKING NOTES (firewall)

All cleared items are statements about the object's structure — cohomology classes, number fields, modular data, Galois descent — with no physics claim attached; the D10 "gap⟺chirality" language is the banked C2 duality at the level of representation theory only. The D6 retraction and the D2 overturn both trace to the same failure mode (necessary/cited/analogized read as sufficient); both are now recorded with their in-sandbox discriminating facts. Docs debt for the banking PR: PROGRESS_LOG + CHANGELOG + CAMPAIGN_STATUS entries for D1/D3/D4/D6/D7/D8/D10; OPEN_LEADS updates — L53/W2.5 (exactified), L66 (closed), L67 (closed-refuted), L68 (retraction, reinstate B137 wording), L63 (remains OPEN, annotate T-NORM conflict); revert B137's "CORRECTED 2026-07-14" edit.