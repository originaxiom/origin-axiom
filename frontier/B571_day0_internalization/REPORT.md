# THE EXHUMATION REPORT — day-0 internalization campaign (origin-axiom)

**Scope:** 14 verified genuinely-buried items from the full-corpus sweep, the burial-pattern diagnosis, the chirality verdict, and the top-5 revival queue. Every item from the verified list appears below — nothing silently dropped. All claims are firewalled: walls and open questions only, no physics-value claims.

---

## 1. THE RANKED LIST

### A. Unjoined theorems and unverified identifications (kind: math / concept)

**A1. The criticality unification — three banked results are one unwritten theorem** *(confidence: HIGH)*
- **Where:** PROGRESS_LOG 2026-07-11, "B519 RE-MINING CAMPAIGN — VERDICT"; docs/THEOREM_REGISTRY.md:123-124; docs/CLOSURE_2026-07-11.md:77-79.
- **What:** B181 (γ=0 on spectrum), B507 (β-function zero at the pointer), B498 (driftless walk, log|κ−2|→0, PROVED) were flagged as "one critical-fixed-point theorem, three wordings, never joined." Named as the P5 paper's spine — but papers/P5_monoid/OUTLINE.md (19-line stub) mentions none of them, no joint statement exists, and **B507 has no test lock at all** (no tests/test_b507*.py).
- **Why buried:** recognized once in prose, never promoted to a theorem with shared hypothesis + three corollaries, never locked jointly.
- **Revival:** write the single theorem; add one test asserting all three quantities vanish/coincide at the same point in the same run; backfill the missing B507 lock.

**A2. "Tower measure = Kubota–Leopoldt 3-adic L-function" — asserted, never computed** *(confidence: medium)*
- **Where:** same B519 verdict, cell A2, gate (c).
- **What:** B413's exact measure values (|L(χⱼ,μ)|=1/4 ∀χ; 12·L(χ₁) = a ℤ[ζ₉] Gauss sum, norm 9) were closed with "it IS the known Kubota–Leopoldt 3-adic L" — with **zero computation of the standard interpolation values anywhere in the repo**, no test, no CLAIMS/THEOREM_REGISTRY entry. This has the exact shape of the assertion-not-computation error the B525 audit cracked in the sibling cell B1 (see memory: compute-the-discriminating-fact); it was never subjected to the same scrutiny.
- **Revival:** compute genuine Kubota–Leopoldt interpolation values at p=3 for the relevant characters and compare digit-by-digit against B413's banked Gauss-sum values — confirm or retract.

**A3. B54's twin quadratics {disc −3, disc +5} at c=1 — the earliest sighting of the two-ended split, never cross-referenced** *(confidence: medium)*
- **Where:** 2026-06-02, frontier/B54_general_c_exchange_structure/FINDINGS.md.
- **What:** the P-exchange symmetric/antisymmetric sectors of the SL(3) trace-map Jacobian at c=1, m=1 give exactly t²−t+1 (Eisenstein, −3) and t²−t−1 (golden, +5) — the same field pair that later became the load-bearing B247–B261 two-ended structural theorem (ℚ(√−3)/E₆ vs ℚ(√5)/E₈). Grep confirms **zero cross-references between the two literatures anywhere in the repo.**
- **Revival (sharpened):** is the B54 involution P ([J,P]=0, splitting Eisenstein from golden) the same Galois/group-theoretic element that splits the two-ended object into its hyperbolic-ℚ(√−3) and spherical-ℚ(√5) halves — mechanism identity, or two independent apparitions of the same discriminants?

**A4. L34: Fix(φ_m) is genus-0 with #Fix(F_p)=p−1 at m=1, irregular at m=2,3 — a computed asymmetry shelved DORMANT, never explained** *(confidence: medium)*
- **Where:** PROGRESS_LOG 2026-07-01 "in-sandbox attack sweep"; docs/OPEN_LEADS.md row L34.
- **What:** an exact point-count formula and a genus/regularity break across the metallic family, shelved as NEEDS-SPECIALIST rather than killed. Never locked, never revisited. B361/B362's "doubly-elliptic seed" law (m∈{2,7}) is thematically adjacent but is a **different construction** — the correlation was never tested.
- **Revival:** re-run the point count at m=4,5,7 and test whether genus-0/irregular correlates with the B361 doubly-elliptic seed selection rule.

**A5. Probe 4 (B532-I6): the four potential assignments behind the k₂/k₃ range 0.65–15.05 were never tabulated** *(confidence: low)*
- **Where:** PROGRESS_LOG:3246-3247; frontier/B532_last_echo/i6_nine_ingredients.py:343-379.
- **What:** gap positions FORCED (IDS = cumulative Perron frequencies), gap-opening slopes CONDITIONED on potential; the four assignments (Box, Inverted, Perron, Structural) were computed but only the aggregate range survived to prose. Not in FINDINGS, no test, no CAMPAIGN_STATUS entry.
- **Revival:** rerun probe_4_forces(), tabulate per-potential k₁/k₂/k₃, check whether any assignment pins a golden-family constant — potential upgrade CONDITIONED→FORCED for that class.

**A6. B520: S = log((5+√21)/2), √21 = √(3·7) — both factors are B423 apparition primes, never cross-checked** *(confidence: low)*
- **Where:** PROGRESS_LOG:3061-3068; the reading firewalled "to S064" — **which was never written** (S064 is a missing slot in speculations/).
- **What:** 3 and 7 are both members of B423's Fibonacci apparition-prime set {2,3,5,7,11,13,17,19,29,41,47,89,199} for the E₆ torsion. A real, cheap, unexploited cross-check (2 of 13 forced primes — must be Bonferroni'd honestly).
- **Revival:** run the cross-check, compute the coincidence probability against the full prime set, write S064 or kill it.

### B. Explicitly-flagged, never-pursued hooks (kind: hint)

**B1. e₃ of the 1215-rung triple — a preregistered sentinel that silently stalled** *(confidence: medium; the most concrete debt on this list)*
- **Where:** docs/progress/REVIEWS.md Reviews 6–8; frontier/B399_wall_scale/triple_id.json literally reads `"e3": "PENDING (needs primes 7-10)"`.
- **What:** the cubic t³−(1/48)t−e₃ has e₁=0, e₂=−1/48 proven exact (fourth appearance of the 1/48 seam family); e₃'s CRT reconstruction stopped mid-run (AUDIT_2026-07-05 stamped it UNSTABLE), Reviews 9–13 never mention it again. It blocks the preregistered 31-collision + supersingular {31,79,167} sentinel **and** the downstream B412 p-adic L probe (which is also item A2's subject — two buried items on one chain).
- **Revival:** finish primes 7–10, reconstruct e₃, fire the pre-registered sentinel adjudication.

**B2. B137→B160: S031 sealing at bronze m=3 was never run, though the tool exists — and the stated obstacle is wrong** *(confidence: medium)*
- **Where:** frontier/B137 FINDINGS + OPEN_LEADS L6; frontier/B160's bronze Cayley–Hamilton trace map.
- **What:** sealing verified only at m=1 (ℚ(√−3)) and m=2 (ℚ(i)); m≥3 deferred as "non-quadratic K_m" — but **K₃=ℚ(√13) is quadratic** (13 squarefree). The real reason it wasn't run is that nobody combined B160's bronze map with B137's MB7 off-sublocus filter.
- **Revival:** run B137's method with B160's map at m=3: do all irreducible off-sublocus fixed points stay in ℚ(√13)?

**B3. B566-S1: the 11²|e₄ exponent-echo — the first prime-power Weil question, one data point** *(confidence: medium)*
- **Where:** PROGRESS_LOG:113; frontier/B566_self_interaction/RESULTS.md; OPEN_LEADS:184.
- **What:** at the rung where 11² exactly divides e₄, the mod-11 dark-hyperbola pattern recurses one level deeper (9/10 classes wholesale dark, exceptional class recapitulates the base). "Recursion depth = exponent of the prime power" has exactly one data point; the recursion itself is unlocked (tests cover only the surrounding N=p² law).
- **Revival:** find a second prime-power rung and test whether recursion depth tracks the exponent; extend B534's squarefree Weil proof to N=p².

**B4. B123/B125: the order-6 echo — (0,0,0) Jacobian spectrum (λ³+1, 6th roots) and the parabolic cusp both land on ℚ(√−3), banked twice as "observation, not connection"** *(confidence: medium)*
- **Where:** frontier/B123 FINDINGS; reconfirmed untouched by the B125 audit that corrected B123's main claim.
- **What:** the test lock asserts only the raw spectrum, not the connection. No later B-number picks it up.
- **Revival (sharpened):** does z₀=e^{iπ/3} (the ideal-tetrahedron shape generating ℚ(√−3)) appear as an actual eigenvalue/eigenvalue-ratio of the (0,0,0) Jacobian — a literal algebraic map, or two independent apparitions of disc −3? (Note: structurally the same question-type as A3. Two buried items ask "same field, same mechanism?" — see Patterns.)

**B5. B532-I6 Probe 7: the thermodynamic decay base 0.849 — an unidentified numeric residue from a FORCED-verdict probe** *(confidence: low)*
- **Where:** PROGRESS_LOG:3248-3249; i6_phase3_synthesis.py:210.
- **What:** T(n) = h(n)/log β ≈ 0.489·(0.849)ⁿ with plateaus at n=3–4, 9–10, 12–14; the base fails simple identification (not φ⁻²≈0.382, not φ^{−1/2}≈0.786); no test, no FINDINGS entry, never chased past depth 9.
- **Revival:** higher-depth recompute + PSLQ/lindep against log β, φ-family, and the D₄ quartic x⁴−2x³−5x²−4x−1's algebraic numbers.

### C. Chirality-adjacent burials (kind: chirality) — feed §3

**C1. B530-IX vs B524: the √−7 absent/present tension — same day, same repo, never reconciled** *(confidence: medium)*
- **Where:** PROGRESS_LOG ~3216 (B530 movement IX) vs ~3159-3164 (B524 Part 2).
- **What:** Movement IX names ℚ(√−7) "the chirality field" and **proves it absent** from the coupled golden double's growth-arithmetic (only ℚ(√5), ℚ(i), ℚ(√−5) appear). Same-day B524 finds ℚ(√−7) **present** in the SL(3) Ptolemy variety of the actual figure-eight (4 reps split ℚ(√−3)/ℚ(√−7)), firewalled as "internal echo" (= B479's order-3 torsion field). The parallel ℚ(√−3) case got its reconciliation (Movement XXI, forced ℤ/3 twist); √−7 never did.
- **Revival:** run the Movement-XXI-style floor/dynamics reconciliation for √−7: does it reappear at the floor level of B530's object, or is the SL(3) presence a genuinely higher-rank phenomenon invisible to the coupled double? In the dossier's language: determine whether the √−7 chirality sits in the c-column (expected) or touches θ (would be major).

**C2. B559 Probe 2: "one fact, three faces" — CS=0 = amphichirality = Door-2 involution = dark-energy-kill, recorded as a rhyme, never proved as an identity** *(confidence: medium)*
- **Where:** PROGRESS_LOG:558; frontier/B559_blackhole_probes/FINDINGS.md ("Recorded as a rhyme, not a claim").
- **What:** four separately-banked facts chained once; CS=0 is locked, the identity is not; Door 2 tracked OPEN/NEEDS-SPECIALIST independently, never connected back.
- **Revival (sharpened):** show CS(4₁)=0 IS the fixed-point condition of the Door-2 involution C=[[1,0],[−1,−1]] on the character variety: evaluate C's action on the CS functional's defining cocycle / flattening data and check whether C-invariance forces cs=0 algebraically. **This is a concrete sub-case of the dossier's Q-A** (is the orientation involution inner / equal to θ / independent).

### D. Unreconciled conclusion (kind: conclusion)

**D1. The escalator's self-application has only the trivial fixed point λ=0 — never compared to B568's quine result** *(confidence: medium)*
- **Where:** PROGRESS_LOG:608-610; HINT_LEDGER H117 (HOOK/NOTICED, firewalled by design); OPEN_LEADS:181-182 lists it "accounted" but the cross-check was never run.
- **What:** two independently-derived pictures of the object's self-reference — (i) eigenvalue self-application closes only on the empty object (non-trivial self-reference is non-terminating), (ii) B568-Q5: the quine σ is a strict fixed point yet attracts no basin — both say "self-reference never settles into ordinary attraction," derived independently, never explicitly compared.
- **Revival:** a short formal comparison: are (i) and (ii) two corollaries of one statement about the tower map's spectrum (no non-trivial attracting self-fixed structure), or do they constrain different maps? Cheap; mostly re-reading + one sympy check of the escalator map's derivative at λ=0 vs the quine's local dynamics.

---

## 2. THE PATTERNS — what this program buries

Five recurring burial modes, each with the items exhibiting it:

1. **The recognized-but-unjoined identity.** The program is excellent at *noticing* that two banked facts share a structure, and terrible at *promoting* the noticing. It has a vocabulary for this ("observation, not connection", "rhyme, not claim", "internal echo, firewalled", "three wordings, never joined") that functions as a **respectable parking lot with no exit ramp**. Items: A1, A3, B4, C1, C2, D1 — 6 of 14. The firewall discipline is working as sobriety but the parked items have no re-entry cadence. **Fix:** every "observation-not-connection" tag must generate an OPEN_LEADS row with a named discriminating computation, or it is a silent drop.

2. **The assertion that closes a campaign cell.** A "this is already known / this IS X" verdict ends a line without the discriminating fact being computed in-sandbox (A2 Kubota–Leopoldt — the exact error class the B525 audit cracked at cell B1 of the *same campaign*; the audit checked B1 and never swept its siblings). **Fix:** when an audit cracks one cell of a campaign for a method error, audit every cell closed by the same gate.**

3. **The stalled long computation that falls off the review radar.** e₃ (B1 here) was tracked as explicit debt in three consecutive reviews, then vanished from Review 9 onward with the JSON still reading PENDING — and it blocks two downstream preregistered items. **Fix:** reviews should diff the *previous* review's open-debt list, not just report current activity; a debt item may only leave the list via DONE or KILLED.

4. **The prose-only numeric.** Computed numbers that never reach FINDINGS or a test lock: the four k₂/k₃ values (A5), the 0.849 base (B5), the per-item recursion structure behind 11²|e₄ (B3). The pipeline PROGRESS_LOG → FINDINGS → test is leaky specifically for *residues of probes whose headline verdict was already reached* — once the verdict (FORCED/CONDITIONED) is stamped, the supporting numerics evaporate. **Fix:** CONDITIONED verdicts must bank the conditioning table itself.

5. **The wrong stated obstacle.** B2 (m=3 "non-quadratic" — it is quadratic) shows deferrals can encode a factual error that then protects the deferral from revival for weeks. **Fix:** OPEN_LEADS deferral reasons are claims; spot-check them like claims.

Meta-pattern: the program almost never buries *results* (the lock discipline works); it buries **connections, residues, and completions** — the tissue between results.

---

## 3. THE CHIRALITY VERDICT

**Question:** "Are you sure the object has no chirality?"

**Answer: No — and yes, in the only way that was ever claimed.** The precise statement, per the dossier: **there are two distinct ℤ/2 involutions, and the object breaks one while being provably symmetric under the other.**

- **c = complex conjugation / orientation reversal** (τ↔τ̄, √−3↔−√−3, σ↔σ̄, the arrow): the object **breaks c, abundantly and computedly** — the B470 chiral letter-tower (CS≠0 from n=3), the B469 orientation residue (−1)^((N−1)/2) = the norm of the scale, the B568 arrow (σ̄ not conjugate to σ, D_KL≈12 bits, disjoint forbidden bigrams), the B565-H1 real-form theorem (non-real adjoint traces 37437270+38799960√3·i, holonomy in **no** real form of F₄(ℂ)/E₆(ℂ)).
- **θ = Out(E₆) = the E₆→F₄ fold = the 27↔27̄ swap**: the object is **symmetric** — THEOREM-tier. 4₁ is amphichiral (CS=0 exact); amphichiral ⟺ θ-symmetric is one identity (T-θTANGENT); through F₄, 27 = 1⊕26 with the 26 **self-dual, hence self-dual for every subgroup** (B569, pure Lie theory — the stage itself refuses rep-chirality); the chiral index ≡ 0 on the species chain (B565-T3, exact to 1e-14, N=8000).

**Theorem vs open, exactly:**
- **THEOREM:** θ-symmetry of the body; vector-like-ness through the F₄ stage for every subgroup; c-asymmetry of the holonomy (no real form); and — computed in the dossier session — **c ≠ θ on the adjoint** (θ fixes tr Ad, c moves it).
- **OPEN:** whether c and θ can be related on the **27** (not the adjoint) of the geometric holonomy; whether the c-chirality inventory (items 2–5 of the dossier; items C1–C2 above) can ever be carried into the θ-column. **No route currently in the repo does this.** The "two-sides reframe" is correctly placed as hypothesis: the object does live on the complex side (necessary), but complex-domain-ness (a c-fact) is not rep-complexity (a θ-fact) — necessary, not sufficient. Firewall holds: no claim that any measured spectrum follows.

**Sharpest computable next questions** (dossier Q-A/Q-B/Q-C, cheapest last):
- **Q-A (crux):** is ρ̄ conjugate within E₆(ℂ) to ρ (c inner — wall confirmed), to θ∘ρ (c=θ — reframe vindicated), or to a distinct mirror component? Handle: the amphichiral isometry φ with ρ̄≅ρ∘φ; push φ to E₆ and classify. Adjoint evidence already points to "c and θ independent."
- **Q-B:** does θ on the **27** of the geometric holonomy equal c on the 27? (The adjoint can't distinguish — it's self-dual; the 27 can.) Buildable from B347/B565 data.
- **Q-C (cheapest):** trace the B469/B568 orientation residue up through the holonomy: does it act as c (predicted by the BR2 norm-of-the-scale mechanism — closing items 2–5 honestly into the c-column) or as θ (which would be the single most important positive available)? Map-tracking on banked data, no new machinery.

**Buried items C1 and C2 slot directly under this verdict:** C2 (CS=0 = Door-2 involution?) is a sub-case of Q-A; C1 (√−7 absent/present) is a test of whether the "chirality field" label belongs to the c-column at the higher-rank (SL(3)/Ptolemy) level.

---

## 4. THE IMMEDIATE QUEUE — top 5 revival computations

1. **Q-C: which column does the orientation residue live in?** (chirality; cheapest crux-adjacent computation)
   *First step:* load the banked BR2 orientation-double-cover data and the B469 residue (−1)^((N−1)/2) in the sage env; write a sympy script that applies the residue's generator to the E₆ holonomy generators from B565's `realform_adjoint_traces.py` and tests whether its action conjugates tr Ad (c) or fixes it (θ-compatible), on the witness element with trace 37437270+38799960√3·i.

2. **The critical-fixed-point theorem (A1).**
   *First step:* extract the exact hypothesis/statement triples from frontier/B181, B507, B498 FINDINGS; write tests/test_b507_beta_zero.py re-running B507's β-zero computation (the missing lock), then a joint test asserting γ=0, β=0, and E[log|κ−2|-drift]=0 at the same κ in one run.

3. **Finish e₃ (B1).**
   *First step:* rerun frontier/B399_wall_scale's CRT reconstruction for primes 7–10 (avoiding the AUDIT-flagged denominator-collision prime), update triple_id.json, and fire the preregistered 31-collision + supersingular {31,79,167} sentinel; this also unblocks item 4.

4. **Compute the Kubota–Leopoldt discriminating fact (A2).**
   *First step:* in-sandbox, compute the standard 3-adic Kubota–Leopoldt interpolation values L_3(1−k, χ) for the ℚ(√−15)-landscape characters (sympy/pari via sage-python) and diff against B413's banked |L(χⱼ,μ)|=1/4 and the ℤ[ζ₉] Gauss-sum value; verdict = CONFIRMED-with-lock or RETRACT gate (c).

5. **S031 sealing at bronze m=3 (B2).**
   *First step:* one script combining B160's bronze trace map (a,b,c)↦(b,(b²−1)c−ab,(b²−1)(bc−a)−bc) with B137's MB7 off-sublocus root-find + reducible filter, 2 seeds, testing whether every irreducible off-sublocus fixed point lies in ℚ(√13); correct the "non-quadratic" deferral reason in OPEN_LEADS L6 either way.

*(Next in line if the queue clears: A3/B4 as a paired "same discriminant, same mechanism?" computation, and C1's √−7 floor-reconciliation.)*

---
**Honesty notes:** confidence labels are inherited from verification, not inflated; A5, A6, B5 are low-confidence and ranked accordingly; the chirality verdict claims a wall plus open questions, not a positive; nothing here asserts any measured-value correspondence. All 14 verified items are present (A1–A6, B1–B5, C1–C2, D1).