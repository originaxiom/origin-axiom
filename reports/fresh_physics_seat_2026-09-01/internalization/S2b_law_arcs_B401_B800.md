# S2b — INTERNALIZATION SWEEP: law-creating arc bodies, band B401–B800

*Sweep seat, 2026-09-01. Product: digest only — no adjudication. Every entry below is
(claim / proof shape / dependencies / red flags), 3–6 sentences. The evaluating seat
judges; this file flags.*

## COVERAGE MODULUS (read this first — exactly what was read and what was not)

**Selection rule applied.** An arc qualified if its number lies in 401–800 AND it is cited
as a witness in a docs/LAW_MAP.md row of strength THEOREM / LAW / WALL / CERTIFIED /
THEOREM-grade / THEOREM-backed / CLOSED-NEGATIVE-RECORD, or anywhere in
docs/THEOREM_LEDGER.md (any link label). LAW_MAP was read in full (all 370 lines, in
4 paged reads); THEOREM_LEDGER in full (332 lines); the P3 paper's chain table
(papers/P3_THE_PAPER/main.tex lines ~280–335 + section skim) was cross-checked against the
ledger; docs/CAMPAIGN_STATUS.md top entries (B1225–B1232) were read for live-board
contradictions.

**Read IN FULL (FINDINGS.md unless noted):** B437, B471, B489, B518, B533, B534,
B565 (RESULTS.md — no FINDINGS.md exists), B581, B584, B585, B587, B588, B591, B592, B593,
B596, B601, B604, B605, B607, B608, B611, B613, B615, B616, B617, B618, B620, B621, B624,
B626, B627 (SEALED_SILVER_TORSIONS.md — no FINDINGS.md), B628 (COMPARISON_DESIGN.md incl.
run — no FINDINGS.md), B631, B632, B634 (ERRATUM_1.md — no FINDINGS.md), B637, B638, B639,
B640, B641, B642, B643, B644, B645, B646, B647, B649, B650, B651, B652 (GATE_B_VERDICT.md —
no FINDINGS.md), B654, B656, B657, B658, B660, B662 (CAMPAIGN_SYNTHESIS + WAVE1 + WAVE2 +
WAVE3 findings), B663, B664, B665, B666 (CAMPAIGN_SYNTHESIS + WAVE1_FINDINGS), B670, B672,
B674, B675, B680, B683, B684, B685, B691, B692, B693, B694, B695, B696, B698, B699,
B700 (one file also carrying the B701 phase-2 cells), B702, B704, B705, B706, B707, B708,
B713, B714, B715, B716, B730, B731, B733, B734, B736, B737, B739, B740, B743, B745, B746,
B747, B748, B749, B750, B751, B752, B753, B754, B755, B756, B757, B759, B760, B761, B762,
B764, B766, B769, B771, B775, B782, B785, B786, B789, B790, B791, B794.

**CUTS (declared, none silent):**
- **B666 WAVE2_FINDINGS.md and WAVE3_FINDINGS.md not read** — the campaign synthesis table
  (read) summarizes every cell verdict; wave-2/3 cell detail (cells 2, 7–10, R1–R3, S,
  W31–W35, A′, B′, C′) is digested from the synthesis + the LAW_MAP rows that cite them,
  not from the wave files. Any load-bearing detail unique to those two files is uncovered.
- **B659 (novelty dossier: DOSSIER.md, 213 lines) not read** — cited as witness in the
  subfield-law and twist-frame rows (as a literature-sweep restatement, Neumann–Reid). Its
  content is digested only through those rows and B662/D.
- **B662 and B666 per-cell artifacts** (cellA…cellI, cell1…cellW35 directories) not opened;
  wave findings + synthesis only.
- **PLACEMENT-only arcs skipped by the selection rule** (they witness no THEOREM/LAW row
  and no ledger link): B709–B712, B717–B729, B732, B735, B763, B765, B767, B768, B770,
  B772–B774, B776–B781, B787, B793, B795–B799. Where one of these corrects a read arc
  (e.g. B701 inside B700's file; B732 surviving via B734) it is covered there.
- **B758** (the arc that created THEOREM_LEDGER) — covered by reading the ledger itself,
  its product; the arc directory was not separately opened.
- **B780** (retracted Galois-reversal gate) not read — cited in LAW_MAP row 70 only as a
  named retraction/error-class exemplar ("the retractions B780/B784"); note B784 has no
  directory on main at all (it was a cc3-branch arc).
- **B788** (external Maass Gates-0–9R bank) — does not appear under frontier/ in the
  directory listing used for this sweep; digested only through its receipts B790/B791/B794.
- **B791 read in full across two pages** (all 207 lines). **B533 read in full across two
  pages** (all 388 lines).
- FINDINGS files were the unit of reading; compute.py/output.txt artifacts were NOT re-run
  or opened. This sweep verifies nothing; it reports what the record says about itself.

---

## A. The torsion / conductor / hearing-trace family (the κ-arc)

**B581 (six torsions).** Claim: the six twisted Alexander torsions τ_m of the fig-8 at
Sym^{2m}(ρ_geo), m ∈ E₆-exponents, are exact integers with sign(τ_m) = (−1)^m — positive
exactly at the θ-odd exponents. Proof shape: exact Wada/Fox computation over ℚ(√−3),
blind-then-compare protocol, with a Review-17 units note (raw JSON must be
monic-normalized or every sign flips). Dependencies: B353 grading, B425 analytic gate.
Flags: the "jewels = torsion ratios" guess died honestly in-arc; sign law at this point
empirical (later proved by B617); the m=1 BTZ-quadratic and 7-adic patterns are recorded
hints, not laws.

**B617 (sign-law family theorem).** Claim: sign det′(I−Sym^{2m}A) = (−1)^m for EVERY
hyperbolic A ∈ SL(2,ℤ), closed form τ_m = (−1)^m(tr²−4)^m∏U_{j−1}(tr/2)². Proof shape:
symbolic pairing identity (each k↔2m−k factor pair is negative), verified against banked
B423/B616 values and three objects. Consequence honestly stated in-arc: the bundle-level
sign law carries NO object information (pure parity), relocating the informative question
to the exterior torsions. Feeds the conductor-unification hypothesis (base tr²−4 = the
hearing gate). Clean; no flags.

**B616 (held-out control).** Claim: the second object's amplitude family matches SM targets
at exactly noise level (STILL-AMBIGUOUS verdict), and its bundle torsions obey the same
(−1)^m sign pattern (which motivated B617's theorem). Proof shape: one mechanical sealed
run. Flag carried in-file: the object called "m136" here is actually the R²L trace-4
bundle (B621 naming correction, header present) — the census name was wrong, the math
stands.

**B618 (conductor prediction, third object).** Claim: the tr-5 bundle's eigenvalue-field
content (√21) enters the odd hearing trace exactly at the registered base-gated levels
{14,21,35,42} — a registered-before-run prediction that PASSED, making the conductor
unification predictive-tier on three objects. Proof shape: sealed prediction + scan κ≤45.
Carries the same m136-naming correction header. Flag: the observable used differs from
B621's Weil-coset gate (reconciled later by B624).

**B620 (conductor mechanism).** Claim: in the Weyl-twisted Weil factorization the twelve
Gauss conductors are det(A⊗(±w)−I₄); all non-reflection conductors are perfect squares, so
the object's field √(tr²−4) can enter only through the six signed reflections — "the field
has exactly one door" (the one-door THEOREM row). Proof shape: reflection line symbolic;
the other closed forms by exact 4-point interpolation; verified on two objects at bearing
vs silent levels. One in-run correction disclosed (reflection index set). No flags.

**B621 (κ-gating law).** Claim: write tr²−4 = 3^v·m; the reflection coset carries field
content iff m | κ, the 3-part being absorbed by disc(A₂) — verified with an exclusivity
control, zero exceptions κ = 4..27, three objects. Proof shape: derived rule + verified
scan (workflow seat, verified in-loop). Also carries the binding object-naming correction
(census m136 = silver RRLL; the trace-4 object mislabeled in B610/B616/B618/B619). Flag:
the B618-vs-B621 gate discrepancy is registered in-arc and resolved by B624 — a reader
citing B621 alone sees the reconciliation as open.

**B624 (observable bridge).** Claim: the B601/B610 odd hearing trace IS the Weil twelve-term
Gauss assembly (Cm is itself the signed Weyl reflection), resolving B618's {12,24} vs
B621's 4|κ with no contradiction; bridge constant a fixed framing phase. Proof shape:
definitional identity + 6/6 numeric tables. Flag stated in-arc: the κ = 28..40 generality
sweep was resource-killed and NOT claimed — the row's "0 exceptions" is κ ≤ 24.

**B591 (chord manifold).** Claim: the golden 5-tone's conductor is literally first homology
— the plain lift's torsion is det(A−I), the mirror-twisted lift's det(A+I); Δ(−1) = 5 =
|H₁(Σ₂(4₁))|; the monodromy-twisted complement double is an integral homology sphere.
Proof shape: exact SNF + SnapPy; L(5,2) identification CITED-standard with in-sandbox
verification. Terminology correction applied in-file (Haken, not graph manifold). Feeds
the conductor-identities THEOREM row with B588/B634. No flags.

**B588 (sector exchange).** Claim: level-rank sector exchange = migration of −1 across the
Weyl-group boundary (−1 ∈ W(A₁), ∉ W(A₂)); the same unit-plus-√5-Gauss-sum arithmetic
assembles to −1/φ in the all-even sector on one stage and the all-odd on the other. Proof
shape: exact rank-1 decomposition verified κ′ = 3..20 + integer membership fact + the
κ = 5 ingredient identity. Residual named (per-term reciprocity, later closed by B666/R3).
No flags.

**B634 (conductor chord — ERRATUM only).** The arc's surviving citation in the THEOREM row
is its G1 conductor identities; the ERRATUM corrects its own prereg on three points (the
−A₁ bundle is the closed Sol torus bundle, not cusped; "the conductor selects κ=5" demoted
to the gating law + the minimal-bearing CHOICE; gates G2–G5 superseded — G4's closed-
manifold symmetric-texture claim was mathematically false). Flag: this is an arc whose
sealed prereg contained false statements corrected only by erratum; the surviving G1 is
narrow.

**B596 (cat-map clock null → derived).** Claim: the θ-odd clock is NOT the naive cat-map
period (registered prediction FAILED, banked as failed); ADDENDUM: B656/G4 later derives
the whole table as clock(κ) = ord(A₁ mod 3κ) with κ=4,5 as the law's own anomaly clauses —
DATA → DERIVED, in-file. Proof shape: blind sweep then cross-seat derivation independently
verified 10/10. Good self-correction hygiene; no flags.

**B601 (pairing + trace law).** Claim: the odd hearing form's spectrum is conjugation-closed
at every level (basis-independent), and trace(B_odd) = [5|κ]/φ − [4|κ] with the mod-4
clause confirmed on registered discriminating predictions (κ=16, 40); LAW-O is
stage-universal across the two quantum models. Proof shape: exact scan on 14+ κ-points,
prediction-first for the new clause. Witness for the trace-law LAW row (mechanized
end-to-end later by B666/R3). No flags.

**B611 (two-law test).** Claim: both sealed predictions FAILED as sealed — P1 on a
degenerate dim-1 edge (the four-object pattern above it is perfect), P2 dissolved because
B_odd is unitary BY CONSTRUCTION (the "unit-circle departure" discriminator was vacuous —
an MB12 miss superseding B609's exploratory row). What replaces them is the three-layer
separation (pairing = chirality, trace = field, matrix elements = coupling). Proof shape:
sealed two-outcome runs honored as failed + exact diagnosis. Exemplary negative
bookkeeping; no flags.

**B613 (closure theorem).** Claim: modular-data axioms + GHH anti-palindromicity ⟹
conj(W) = Q⁻¹WᵀQ with Q = P·S·C preserving the C-grading — amphichiral weld ⟹
conjugation-closed odd spectrum at EVERY level (one-way theorem). Proof shape: three-
ingredient axiomatic proof + exact-numeric suite (4 levels × 4 amphichiral witnesses 16/16;
12/12 chiral controls fail). The converse stays empirical — stated. No flags.

**B626 (Jacobian reality law).** Claim: J = μ+1/μ is real exactly for amphichiral words and
complex for chiral ones (8 words) — the pairing-chirality law's classical face; the naive
crossover laws refuted. Proof shape: exact character-variety computation; discrete-branch
identifications honestly left unresolved (so no exterior sign claim is made). LAW row
matches the arc. No flags.

**B627 / B628 (silver exterior torsions, sealed + compared).** B627: the six silver
exterior torsions sealed hash-first (m=1,4,5 exact integers; m=7,8,11 complex,
PSLQ-unidentified), extending the exterior sign law to 6/6 on Re — the LAW row's "silver
6/6" witness. B628: the sealed comparison ran null-compatible on both grids — the exterior
families are SM-silent on both objects, completing Branch 3's held-out round. Proof shape:
hash-first sealing, identical frozen protocol to B614/B615. Flag: three of the six silver
values remain exact-form-unidentified; the sign law there is a statement about numerically
computed real parts.

**B615 / B631 (the stopping-rule record).** B615: the sealed fig-8 value comparison came
back AMBIGUOUS (corrected Šidák p = 0.078) with two coding bugs disclosed (fixed toward
compliance with the sealed design) and PDG targets taken from the assistant seat's
knowledge (disclosed). B631: the matrix-level comparison (odd hearing form vs PMNS) is
STRUCTURED-NULL at p = 0.700 with pipeline controls added by addendum (positive control,
power demonstration ε=0.02 → p=0.0003), firing the stopping rule: "the mathematics
publishes as mathematics." Together with B616/B627/B628 these witness the CLOSED NEGATIVE
RECORD row. Flags: B615's targets-from-memory and post-seal MB13 sweep are disclosed
in-file; the record row depends on the disclosed-but-real protocol wobbles having not
changed match rows (asserted in-file).

## B. The ear / hearing-group family

**B584 (θ-listener).** Claim: bare knot states are θ-even (third unhearability); the
antiphase mirror channel tr_odd = ½(Z − Z_C) hears everything at SU(3)₂ — the entire
banked −1/φ is θ-odd, and the θ-even block is a perfectly cancelling order-20 clock. Proof
shape: preregistered blind computation on banked B238/B245 machinery, falsifiers survived.
Foundation of the coupling-thesis row. No flags.

**B585 (listener law).** Claim: the naming theorem (the C-twist plays the OTHER SL(2,ℤ)
lift −M); LAW-O (tr_odd = [4|κ] − [5|κ]/φ) with held-out hits 5/5 including the κ=20
collision; LAW-E FAILED its holdout (banked dead); the field-containment mechanism M1
REFUTED by its own preregistered predictions. Proof shape: blind table + holdouts. The
clock table honestly lawless (until B656/G4). Excellent negative hygiene; no flags.

**B587 (Weil mechanism).** Claim: Z(W; SU(3)_k) is the signed Weyl average of twelve Gauss
sums with conductors det(A⊗(±w)−I₄); LAW-O re-derived at every κ; the golden −1/φ IS
Gauss-sum arithmetic; why only the golden word is clean (unit det(A−I)). Proof shape:
exact decomposition identity verified 3 words × 17 κ; the framework known and cited
(Jeffrey 1992); per-term proof deferred (closed later by B666/R3). No flags.

**B592 (mirror listener + OPEN matrix).** Claim: the closed mirror listener is DEAF (θ-odd
channels identically zero for C-symmetric states — the fourth unhearability, with proofs);
on the OPEN matrix the twist's entire imprint is the sign flip M_odd → −M_odd (the
SIGN-FLIP THEOREM), parity conserved. Proof shape: prereg reconstruction (the original
never reached the seat — disclosed), 4 controls, one in-diagnosis bug caught by the MIXED
rule; the handoff's 5₂ trace-field slip corrected in-file. Flags: the prereg was a
reconstruction of a lost relay; the verdict landed outside the sealed outcomes table and
was banked under the handoff's own extension rule.

**B593 (Round-4 hearing law).** Claim: a dial-displaced listener hears chirality at second
order — A_t − A_u = −2ε²·u†M_odd u exactly, with the golden-pentagonal closed amplitude
u₃†M_odd u₃ = 1/(2φ) + i·sin(2π/5)/√5 verified symbolically over ℚ(ζ₂₀); R4-B null
(non-invertible knot's fundamental state is not the third entity). Proof shape: prereg +
adversarial verification addendum (exact sympy re-derivation; braid-closure pinning).
Flags: the caveat is explicit that "reverse = reversed-word closure" is a cited lemma; and
NOTE the live board (B1231) now types the listener map u itself as an unpriced
IDENTIFICATION — the arcs downstream of B593's u carry that unstated (see red flags).

**B640 (hearing group).** Claim: the θ-odd hearing rep has image 2I × ℤ/3 (exact class
equation = SL(2,5)), tr ρ(RL) = −1/φ, orders reconciled (four banked orders, four
operators); the handoff's universal tone law CORRECTED in scope (fails 232/360). Proof
shape: class-table-strength verification at 60–80 dps; Ng–Schauenburg CITED-KNOWN for the
level. Flags: the first run produced garbage from a float64 leak (caught by gates,
disclosed); the "2I" here is the HEARING rep, not the raw mod-5 holonomy (SL(2,𝔽₂₅)) — the
disambiguation lives in B699/LAW_MAP, not in this file (a reader of B640 alone can misread;
see red flags).

**B641 (twist-frame tone law).** Claim: Re(ζ⁻¹ūM_odd u) is ear-independent on all 360
elements; five absolute tones {0, 1/(2φ), 1/2, φ/2, 1} with exact multiplicities;
Plancherel split 1/4 + 1/4 exact. Proof shape: five sealed gates at 60 digits; exhaustive
but floating-point (the LAW_MAP row honestly downgrades to CERTIFIED with mechanization
delegated to B654/B1011). No flags beyond that stated grade.

**B642 (Galois ear).** Claim: at the Galois-conjugate stage all three sealed predictions
confirm — same group, same tone set, tr ρ(RL) = +φ exactly — K020-in-the-ear. Proof shape:
sealed 3/3 prediction-first at 60 digits, one new instance. The arc itself says "still a
placement, not a derivation," and the LAW_MAP row preserves that. Later effectively
derived by B644/B700. No flags.

**B644 (congruence shadow).** Claim: ρ_hear = χ_golden ∘ (mod-5 reduction) elementwise
(M2 0/560 mismatches) — the conductor is the ear's modulus; upgrades the McKay ear
placement to DERIVED and gives B642 its mechanism. Proof shape: sealed gates; the M3
reference tables in the prereg were internally INCONSISTENT as characters (a sealing error,
disclosed and adjudicated — the factorization content passed as sealed; the corrected
table verified by exact character arithmetic). Flags: the M3 sealing error is the arc's
own MB12 catch, honestly handled but means one sealed clause was vacuous as written;
novelty explicitly NEEDS-SPECIALIST.

**B646 / B651 (cc2 wave-2/wave-3 integrations).** Claim: the level-ladder organ — the
corrected generic-silence law Z(κ) = (1−(κ|5))/2, the uniform jump law (→ 325/325 exact
certificates), the melody theorem Z(κ)=Z(κ+N₀) (6/6 sealed pairs), the PSL-factoring
theorem, the splitting law, the stage-split clock law — verified on receipt (seals
re-hashed 11/11 and 21/21; decisive rungs re-run; independent arithmetic). Proof shape:
cross-seat verify-don't-trust with named unrebuilt parts (the heavy level-7/8 enumerations
banked on the sender's sealed two-pipeline identity — stated). Flags: B646's NOTICED
inert⟺even correlate DIED at r=23 (dated correction in-file, prediction-first kill) — the
splitting-law row still lists the correlate as "(3/3, NOTICED)" in its upgrade path; two
lock-gap tickets (B544/B480 unreproducible-as-banked) opened here and later closed by
B666/cell 6 with one banked value corrected (B480's ⟨r⟩ = 0.16 was float noise).

**B654 (listening synthesis).** Claim: Q-FIELD — the chord's field of definition = the
tetrahedral SHAPE field (pre-stated candidate refuted, better law found); Q-PERIOD — N₀ =
75·lcm{d²} exactly (HINT-grade read); Q-AREA — the defect factor 2 is UNIVERSAL (area law
refuted); the tone–character identification (tones = |χ_golden|/2 with exact
multiplicities) and Plancherel-as-Schur verified; several chat1/cc2 claims refuted exactly
(exponent pairing; silver SL(2,7); 24-as-invariant). Proof shape: sealed prereg,
exact-on-banked-data. No flags; note the tone mechanization here is what upgrades B641.

**B656 (digest integration).** Claim: G4 conductor-clock law (independently confirmed
12/12); G1 sign-hears-the-discriminant theorem (confirmed on a Weyl group and words
OUTSIDE the discovery battery, 192/192 vs exact halves); G3 mirror generic law +
sector-carry (13/13 gate, retro-explains the dead P4 correlate); G2 generic-period-5
reduction; G5 dimension-grammar reduction theorem ((i₁,i₂) determine the whole grammar).
Proof shape: received packet 7/7 seals + this seat's independent verifications per cell.
No flags.

**B666 (leads campaign — synthesis + wave 1 read).** Claim highlights: the stage-universal
hearing law |tr_odd| = |χ_D(shadow)| with the E₆/PSL(2,7) instance and the
generating-function theorem (Euler-product form REFUTED); R21-9 proven unconditionally
(pair products are literal squares — the sign-theorem's last asterisk falls); L105 refined
(2O is a canonical quotient of SL(2,ℤ/8), NOT a subgroup); cell 6 corrected a banked value
(B480); wave 2/3 (digested from synthesis only — see cuts): the fifth wall + cup-invariant
table (L106), the glued cubic nondegenerate (L92), per-term Landsberg–Schaar PROVEN
(LAW-O mechanized — the trace-law row's "B666 cell R3"), the scale-torsor no-go as a
standalone theorem (wall 10's upgrade, "B666 cell S"), bronze→2T/E₆ descent, stage
selection reduced to H-EAR with the Galois pair {SU(3)₂, SU(5)₁}. Proof shape per
synthesis: ~30 sealed cells, every verdict on a sealed outcome. Flags: this sweep did not
read waves 2–3 in the original; the widely-cited R3 (Gauss-sum mechanization) and S
(scale-torsor theorem) cells are digested at one remove; the LAW_MAP hearing-landscape row
itself marks the "any word" generalization as CONJECTURE (547-word corpus "supported not
sealed") — the row and the synthesis are consistent but a casual reader of the synthesis
alone would over-grade it.

**B664 / B665 (metallic landscape + reconciliation).** Claim: the single-L landscape
closed form |tr_odd(n)| = (2√3/D)|cos(π(4n−5)/10)| with exact phases and golden-trig
identities (THEOREM); chat1's "golden-only real minimum" REFUTED (witnesses n=12,18,27,33)
and the five-criteria collapse to two; the general shadow-class law |tr_odd(W)| =
2|tone(W mod 5)| (trace does NOT determine hearing). Proof shape: exact verification
38/38 + witness checks; three seats reconciled with reciprocal corrections both
directions. No flags — but note the LAW_MAP row's CONJECTURE label for the general form
governs.

**B672 (grading hunt + branch tiebreak).** Claim: the weight-5 doublet streams ARE
Rogers–Ramanujan objects (comp2/comp1 = R(q) exactly, 301 coefficients, two routes); and
the branch-tiebreak lemma — the cusp lattice ℤ[2√−3] embeds canonically in the A₂ weight
lattice (index 4, iso mod 5) while A₄ admits NO cusp quantization — stage selection
completes to {SU(3)₂, 2̂′} modulo the named principle H-CUSP. Proof shape: exact integer
arithmetic + computed dichotomy. Prior-art of the quintic identities NEEDS-SPECIALIST
(stated). No flags.

**B675 (H-CUSP sweep).** Claim: the cusp field predicts the hosting stage family both ways
(silver: Λ = ℤ+2iℤ over ℚ(i) quantizes A₃ index 2, cannot quantize A₂/A₄; SU(4)₁ = the
conductor-8 stage hears exactly the mod-8 class); the quantization-index law (index =
cusp-order conductor, iso ⟺ coprime); bronze CERTIFIED deaf (S₄ Galois octic, exact
end-to-end, Kronecker–Weber). Proof shape: pre-sealed three-outcome addendum; the bronze
upgrade corroborated → certified with the trust boundary stated (census data + sympy
primitives as instruments). Flag: the SU(4)₁ hearing check is numeric-at-two-precisions
("flagged" in-arc) while the LAW row says "exact both ways" — the lattice side is exact,
the hearing side numeric.

**B680 (arithmetic meditation).** Claim: Vol(4₁) = (3√3/2)·L(χ₋₃,2) verified to 40 digits
(classical — Zagier; its absence from the record was the point), and 5 is inert in ℚ(√−3).
Proof shape: direct high-precision verification + registered leads (Reid-uniqueness ↔ L91;
DEAF=NON-CM). Flags: the LAW_MAP row now carries the B1136 FAMILY-LEVEL scope note (m003
shares the identical volume) — B680's own file does NOT carry that scope note; and the
"monofocal one level up" reading floated here was REFUTED by B683/L2 (honestly, in B683).

**B683 (arithmetic ledger).** Claim: L1 — the divided-power law v₅(c_n) = n+v₅(n!) PROVED
unconditional all-n (5-adic strict dominance); L2 — the inert-5 monofocal reading NOT
SUPPORTED (√5 degenerates in char 5); L3 — m(A_{4₁}) = Vol/π exactly and NOT a rational
multiple of L′(E₁₅,0) (K₃ ≠ K₂). Proof shape: symbolic proof + PSLQ + main-seat
verification. Model self-correcting arc; no flags.

**B684 (loop-7 close).** Claim: G1 sum rule is a theorem of the cubic (kernel derived);
G2 own-channel law (golden 1/φ at SU(3)₂, silver 1/δ at SU(4)₂ — level 2 of the own
family); G3 D4 value catalogue closed + golden period proven 20. Proof shape: cc2 packet
with main-seat spot-checks. **FLAG (live):** the 2026-08-19 addendum (B1072) reports the
silver SU(4)₂ ladder carries a k-indexing/inversion defect — four independent builds get
δ at k=2 where this arc's ladder says 1/δ — affecting the VALUE attribution of the G2
headline (structure stands); the LAW_MAP own-channel row (row 53) still reads "LAW
(2 instances, exact)" with no B1072 caveat. Contradiction between arc addendum and live
LAW_MAP surface.

**B685 (generation terminal).** Claim: the terminal no-go — no framework-derivable
generator produces the {2/5,3/5} streams: the Molien route gives algebraic integers, the
Habiro object is integral away from 3 (GSWZ pure-3), and the targets need growing 5-power
denominators (B683's theorem); the object generates BEING (3) not HEARING (5). Proof
shape: killed-at-support under the sealed design run; includes the B682 correction (a real
misreading of GSWZ eq (2), owned and fixed). Dependencies: GSWZ arXiv:2412.04241 (external
theorem — the premise later recomputed in-repo by B755 cell 3 and proven conditional-form
in B771/OI-055). Scope: "relative to the sealed universe" — stated in the row. No new
flags.

## C. The chord / coupled-object family

**B632 (cubic route).** Claim: h¹(M;27) = 3 exactly (17+9+1 principal blocks); the cubic
invariant unique and explicit; O1/O2 kill any class-level symmetric mass-shaped object on
the solo complement (the wall); Ω rank 2 with 1-dim kernel (audit-corrected from "full").
Proof shape: sealed preregs per cell, exact Fox calculus over ℚ(ω), an instrument bug
caught by its own coboundary control and disclosed; the audit seat's 162/162 verification
adopted as the lock, with binding language corrections (v₀ = invariant-section generator,
NOT "forced vev"; three inequivalent modes, NOT "generation slots"). Flags: the corrected
language matters — several later physics-adjacent readings quote the older "three
generations" flavor; the in-file corrections section is the authority.

**B637 (corrected cell 3).** Claim: the dimension table (h¹(D;27) = 5 generically, 2 at
the full-E₆ bends m=4,8) confirmed on a method-disjoint pipeline; all four D₄ gluings
compatible (nine doubles); the alternating cubic 3-form is NONZERO (discovery branch) with
the core law Y[023] = 24ζ₆·Y[123] exact on 9/9 doubles and the zero law Y[01k] = 0. Proof
shape: sealed preregs; part 2b QUARANTINED once when class-level gates failed, repaired
via two real bugs found by a formal chain machine, then all gates green — the failed
tables kept on disk. Flags: magnitudes are declared basis-dependent (the invariant content
is patterns/identities); the 24ζ₆ ratio was LATER adjudicated GAUGE (B647 cell 3) — the
LAW row carries that; three-pipeline agreement noted incomplete until cc2's packet landed
(it did, in-file).

**B638 (swap mechanism).** Claim: the deck involution acts antilinearly on H¹(D;27) with
Eisenstein-unit diagonal; Y∘σ* = conj(Y); the phase geometry of the core law is
theorem-grade; the magnitude 24 NOT forced (the first-draft "proved" claim corrected
in-file — the σ*-system leaves 10 real dimensions). Proof shape: exact solve + closure
derivation with honest partial. Flag: B649/3b-i later showed the "Eisenstein-unit
spectrum" wording is Hilbert-90 gauge-slack — the invariant is the real structure + field
of definition; B638's file carries no header for this (the precision note lives in B649
and the LAW row).

**B639 (conjθ cubic).** Claim: the λ↦+λ conjugate gluing is rigid (1-dim intertwiner
space, no invertible element — the λ-rigidity THEOREM); θ fixes the holonomy pointwise so
the twist lives irreducibly in the fiber identification (the θ-fiber-pairing THEOREM);
the form-adjoint realization OBSTRUCTED (final). Proof shape: three exact probes + a
constructed pairing that provably does not glue. cc2's withdrawn h¹=3 recorded. No flags.

**B643 / B658 (flip walls).** Claim: the chord breaks all four orientation-reversing
families of Isom(4₁)=D₄ — each admits exactly one partial intertwiner, d = (0,0,1),
supported on the invariant line alone; wall 8 is total, and the double's 27-cohomology
symmetry is σ* exactly. Proof shape: exact 172-condition solves per family, inner
corrections excluded by the Ad(w) argument; B643's first candidate honestly failed and
was refined before the theorem landed. The common-retreat-to-v₀ observation is registered
as HINT only. No flags.

**B645 (dial law).** Claim: the unit cross-ratio law ((Y[023]Y[134])/(Y[034]Y[123]) = 1
exactly on all six 024-silent doubles) and the 13-adic dial deviation on the lit class.
Proof shape: exploratory-EXACT on banked tables with NO PREREG — stated explicitly in-file
per the cc2 flag, artifacts hashed post-hoc with that label. Flag: the no-prereg status is
disclosed; every claim is an exact re-runnable identity, but the arc is the band's clearest
example of post-hoc-exploratory banking (later independently verified by cc2 in B646/N4).

**B647 (core mechanism).** Claim: swap + zero laws are not sufficient (residual dim 6);
the ANOMALY CHARACTERIZATION — Y = ½·conj(the swap's single-certificate chain defect),
exact; cell 3 GAUGE ADJUDICATION — the 24ζ₆ core ratio is pipeline-gauge (any unit
achievable by rescaling), the cross-ratio is the invariant carrier. Proof shape: exact
sympy; R20-5 resolved by dissolution. Important deflation: the "24ζ₆ law" is a
convention-relative regularity — the LAW row carries this correctly. No flags.

**B649 (silver holonomy, stages 1–3b-ii).** Claim: the exact silver SL₂(L) holonomy
(L = ℚ(s,i), s⁴ = 8s²+16), the 27-lift in E₆ exact, the 3/5/1 dimension grammar
REPRODUCES on the second object, the swap real structure reproduces (σ*-matrix defined
over ℚ(i)), the silver Y-tensor: zero-law shape and σ*-law reproduce, the 24ζ₆ ratio does
NOT (scope refinement), deviations 13·211-adic. Proof shape: five sealed stage preregs,
three failed runs caught by exact gates (kept), ERRATA section from cc2's reciprocal
receipt (a false witness sentence, an understated residual, two stale-prose-in-sealed-
artifact instances — the E13 class). Flags: the errata are exemplary but confirm sealed
artifacts here contained stale prose; the arc is the source of the Hilbert-90 precision
note governing B638's wording.

**B650 (typed functor + equivariance wall).** Claim: the type system (quantities only, R0
added after its single disclosed revision cycle); wave 2 — the Sylvester solve returns
T = 0 uniquely (THE EQUIVARIANCE WALL: no linear monodromy-equivariant classical→stage
map exists; disjoint spectra), and the sought functor exists one level up as
group-functorial (mod-conductor ∘ character = B644). Proof shape: exact solve + held-out
type battery. Witness for wall 9. No flags.

**B657 (invariant line).** Claim: v₀ is NOT the Spin(10) gauge singlet (the relayed
dark-sector label dies — v₀'s coefficient at the singlet weight is exactly 0);
one-per-block (each principal block carries exactly one H¹ class; the invariant-line class
IS the Betti class); the portal P(u) = [v₀ × u] is a rank-5 isomorphism, silver control
form-matches deep. Proof shape: cc2 packet, W0a/W0b reproduced bit-identically on the main
seat, W1's matrix re-derived independently. The sector-respecting property honestly left
basis-open (L102 — later resolved BLOCK-DIAGONAL by B662/E). No flags.

**B660 (structure campaign).** Claim: S1 γ₅′ correspondence CONSISTENT-NOT-SELECTIVE
(placement); S2 CP question OBSTRUCTED-CONVENTION (its X³-cubic obstruction later shown a
monomial-ansatz artifact by B662/F — noted); S3 the DIMENSIONFUL NO-GO wall assembled
(typing + N=1 + no-scale + finite-shadow); S4 the v₀-mediated trilinear antisymmetric
with the solo block zero — later corrected BASIS-LOCAL by B662/H (invariant content
survives). Proof shape: cc2 packet with independent recomputation of the decisive S2
cubic. Flags: two of its four cells were subsequently corrected/superseded in parts
(S2 by B662/F CONVENTION; S4's zero restated basis-free) — both corrections are recorded
in B662 and the LAW_MAP rows, not as headers on B660's file.

**B662 (successor campaign, 9 cells).** Claim: cell A — (i₁,i₂) = (1,3) PROVEN
metallic-uniform, upgrading the 3/5/1 grammar to a THEOREM for the family; cell B — the
adjoint 78 gives (0,6,0,6) with one-per-block (third module); cell D — the subfield
theorem (chord data ∈ k(Γ) by Galois descent, 15/15 cocycle-level); cell E — the silver
portal block-diagonal in the canonical decomposition; cell F — L104 CONVENTION (single
GL(5,K)-orbit theorem; the δ_PMNS chain terminates — no prediction exists); cell G — the
melody's exact minimal period P = 175560 CERTIFIED with closed form and true minimality
witnesses; cell H — the Massey wall + nonzero cup classes (and the honest correction of
B660/S4); cell I — the ear IS the Γ₅′ doublet 2̂′ with H129's weight-5 FORCED (E₈
exponents). Proof shape: one sealed campaign prereg, five/three/one-cell waves, main-seat
spot-verification of every decisive fact. This campaign is the band's densest LAW→THEOREM
upgrade point. Flags: corrections it emitted (S4 basis-local; G2 cap shorthand) are
recorded here rather than on the source arcs.

**B663 (bifocal + anatomy loop 1).** Claim: the bifocal entanglement statement sharpened
(golden trace field = being field alone; silver = compositum; chord data descends to k(Γ)
on both); A1 the heart is an invertible Jordan element (portal mechanism); A2 the
resonant-phase law (complete voice closed form, one character governs every phase); A3 the
deep-3 kill is a block central character (per-primary residue hypothesis falsified 73/73).
Proof shape: relays verified item-by-item; the S-entry correction (1/D ∉ ℚ(√5)) checked
symbolically. Also disciplines the "held-out by chronology" idea (postdiction) and gates
the δ_PMNS chain (later closed by B662/F). No flags.

**B670 (anatomy loops 2–3).** Claim: the F4 skeleton (stab(v₀) has dim 52 = f4,
independently recomputed; ρ(π₁) ⊂ F₄(v₀) for both banked holonomies — the metallic-
universal frame); the vector cup nonzero on all six off-diagonal solo pairs with the cubic
as its contraction shadow (cc2's own slot-wise correction adopted); the cross-landscape
half-law (self-selection holds distinctively on 8/16 rows); Track H refuted independently
twice. Proof shape: packet with 17/22 seals (five mismatches dispositioned, two flagged
back — stated). Flag: the seal-mismatch disposition is in-file; the "every metallic"
F4-generalization is explicitly scoped as plausible-not-written-down (the LAW row carries
this).

**B674 (generation leg route 1).** Claim: the Γ(5) twisted tower is trace-silent
(tr(A₁*|H¹(Γ(5),Symᵐ)) = 0 identically, two independent routes) — kill #7; inside the
miss, the GOLDEN-ROTATION discovery: the canonical weight-1/5 lift of A₁ is elliptic of
order 10 with tr = φ EXACTLY. Proof shape: exact rank/Shapiro/Mayer–Vietoris + 2.5e-71
numeric + exact ℤ[φ]. Witness for the golden-rotation THEOREM-grade row. No flags.

## D. The Eisenstein / level-15 / two-object family

**B691 (totient root).** Claim: the being/hearing asymmetry reduces to φ(3) = 2 prime
(irreducibly minimal self-conjugate doublet = the object's own shape roots) vs φ(5) = 4
composite (golden Gaussian periods) — the arithmetic root of B685. Proof shape: two-route
gate (cc2 + independent re-derivation), exact Galois arithmetic. No flags.

**B692 (level-15 literature).** Claim: the fig-8 A-polynomial ↔ conductor-15 curve 15a8 is
PRIOR ART (Borot–Eynard §6.1.5 verbatim); Bianchi base-change is an active field; the E₆/
bifocal/totient synthesis found nowhere — NEEDS-SPECIALIST for the bar. Includes a
self-correction (the g₂/g₃ "garbled" accusation softened to a convention difference).
Proof shape: independent web search + in-seat arithmetic (Atkin–Lehner reconciliation).
No flags.

**B693 / B694 / B695 (loop E-3).** Claim: base change of 15a to ℚ(√−3) gives a_(5) = +1
(two seats, three legs) and BEING IS FORCED — a rational newform's base change has Hecke
field ℚ, so φ is a priori unreachable; E-3b: the level-15 form is irreducible (59/60
primes falsify factorization — the faces genuinely MEET) but c-SYMMETRIC — the
opposite-AL-signs "chirality" reading FALSIFIED as generic even-rank (cc's own over-read,
owned in B695). Proof shape: exact Euler-factor identities + LMFDB cross-checks + the
falsification of the seat's own prior reading. Exemplary; no flags.

**B696 (Eisenstein campaign close).** Claim: campaign closed with an adversarial
completeness critic — the golden's sum-rule locking is GOLDEN-ONLY (silver solo classes
rank 3, four minors recomputed independently); exhaustion declared on banked data with the
residue priced. Proof shape: two-seat verification + 2-agent gap re-pricing. No flags.

**B698 (the meeting probed).** Claim: the level-15 meeting is a PRODUCT, not a fusion —
Flath's tensor-product theorem (primes independent by construction), PSLQ empty with a
base-rate control; the meeting's ONE new invariant is the genus-theory ℤ/2 (h(ℚ(√−15)) =
ℤ/2); the being hand keeps K₃ while the meeting's is K₂ (different curves in one isogeny
class; the 2.37% near-miss named as a numerical trap). Proof shape: sealed prereg, two
literature sweeps, 60-digit PSLQ. No flags.

**B699 (two-object surgery).** Claim: the mod-5-capacity falsifier FIRES — the 5-split
Whitehead holonomy fills SL(2,5) and the fig-8 raw holonomy fills SL(2,𝔽₂₅) (both generic
by strong approximation), so golden capacity settles nothing; the hearing is a
BUNDLE/monodromy phenomenon; the B640 "2I" clarified as the hearing rep, not the raw
image. Proof shape: two seats, two methods each. **Scope-corrected 2026-07-22 (B756):**
the general "5-inert ∧ fibered ⇒ golden" gloss is REFUTED with five-plus exact
counterexamples — the correction clause is carried on the LAW_MAP row and in B756; B699's
own file does not carry a header (the row governs). Flag: reading B699's file alone
overstates the general reading it later lost.

**B700 (+B701) (fiber functor, cells 1–5 + phase 2).** Claim: at every prime stage the
hearing selects one of exactly two (p−1)/2-dim irreps with character field exactly ℚ(√p*),
swapped simply-transitively — measurement = a stage-uniform ℤ/2 fiber-functor torsor,
realized three-sided at the golden stage (irreps / Coste–Gannon modular data / weld-cubing
W^k↦W^{3k}); cell 2: the three ambiguities are the three involutions of V₄ with
being·hearing = meeting as the Galois group law; PHASE 2 (B701): the canonical torsor-iso
is OBSTRUCTED (irreps genuinely symmetric, MTC unitarity-pointed) and the obstruction IS
the observer-coupling thesis — two-seat convergent. Proof shape: sealed preregs per cell,
base-rate gates passed, chat1's W² corrected to W³ in-file. Dependencies: classical
Schur/Frobenius Gauss-sum characters. No flags — note this is the structural base the
later B957 correction (torsor group is ℤ/2, never the idèle class group) VINDICATES rather
than harms.

**B702 / B705 (metallic hearing law → audibility).** Claim: B702's headline law
("metallic hearing ⇔ real-quadratic SWAP field") was RETRACTED IN-FILE same-day (it
conflated the being-face swap with the hearing-face weld — both swap fields are
imaginary); what survives: the silver core ratio exact-ℚ(i)-and-not-24ζ₆, the
torsion-vs-nontorsion swap asymmetry, and the AUDIBILITY LAW (a stage hears a metallic
tone ⟺ ℚ(√p*) real ⟺ p ≡ 1 mod 4), established in B705's campaign along with the
quantum-topology confirmation of B699 (V(4₁)(ζ₅) = 1−√5 real vs Whitehead complex) and
the golden's three-way uniqueness. Proof shape: cc2 self-correction verified by cc; Jones
calibration exact. Flags: the LAW_MAP row correctly leads with the retraction; B705's cell
B N=3 Whitehead honestly INCONCLUSIVE (a cabling bug, disclosed).

**B704 / B708 (the seam; Kim dictionary).** Claim: the per-stage torsors assemble into ONE
𝔽₂-vector space (multiquadratic Galois, stages = basis, meetings = genus sums; verified
(ℤ/2)³ for {−3,5,−7}); B708: the seam and its structure reproduce inside Kim's arithmetic
CS at (ℚ, ℤ/2) with an exact dictionary — two-hands coupling = Morishita linking lk(3,5)=1,
audibility = non-linking with the archimedean prime. Proof shape: multiquadratic
Galois/genus theory; Hilbert symbols verified for stages {3,5,7,11,13}. Honest caveats
in-file: the structural inclusion is Kummer-tautological (only the dictionary is the
meeting); the full arithmetic-CS ACTION is NEEDS-SPECIALIST. No flags.

**B707 (where we meet).** Claim: the program's genuine top-down twins are Kim
(arithmetic CS), Scholze/GSWZ (Habiro ring of ℚ(√−3)), and Lee (regulator = CS invariant);
Turok is method-only. Proof shape: three adversarial literature digests; includes the
citation-flag reversal saga (two 2026 Galakhov–Morozov arXiv IDs first flagged
"likely FABRICATED" on a volume heuristic, then verified REAL by direct fetch and
reinstated, heuristic retired). Flag: that episode is disclosed and is the band's
cautionary tale on citation-verification heuristics; the arc is a literature placement,
THEOREM-grade only for the B708 dictionary it spawned.

## E. The observer / chain family (Parts I–IV of THE CHAIN)

**B713–B716 (the four frontiers).** Claim: chirality (B713 — σ_ω ≡ 0 forced by
amphichirality; the chirality bit is a disc-−3 Galois torsor; triality is gauge-only since
Isom(4₁) = D₄ has no order 3), the physics spine (B714 — rungs 0–6 object-forced,
6′/6″ NEGATIVE, values ⊥), native gauge = complex CS of E₆(ℂ) in NO real form (B715 —
non-real adjoint trace excludes all real forms; the ℤ/11 is UV-arithmetic,
non-descending; 6′ fully closed three-legged), time/4d/signature are the observer's
(B716 — no-arrow Anosov suspension, Ω₃^SO = 0 non-uniqueness, isotropy kills canonical
Wick rotation; the joint space-half: 4₁(5,1) ≅ 5₂(5,1) — being washes out). Proof shape:
sealed preregs, 16-agent compute→3-skeptic loops each, verified-on-receipt; one real bug
(a silent √−3→√3 no-op that spuriously gave OUTCOME A) caught by the verify loop in B713
and disclosed. These are PLACEMENT rows in LAW_MAP but enter the ledger as C18's banked
reading. Flags: B715's probe 1 (T7 full-content gaugeability) is honestly CONTESTED →
INCONCLUSIVE — cited summaries sometimes flatten this.

**B730 (forced faces + cosmos).** Claim: the object's intrinsic arithmetic forces EXACTLY
three quadratic faces = one V₄ (being/hearing/meeting), with ℚ(√−7) proven a stage three
independent ways (Neumann–Reid rigidity; A-poly branches; the SL(n)-tower angle where
adjoining √−7 explodes V₄ to (ℤ/2)³); cosmic topology: flat-universe data null, but
m004's (5,1) child IS the Thurston manifold — distinguished-by-math, physics NIL. Proof
shape: three-way convergence (owner asked two seats separately), load-bearing facts
re-verified in-sandbox. Ledger C7. No flags.

**B731 → B734 (congruence saga).** B731 claimed m004 NON-congruence and is RETRACTED with
a banner (E22: the 2-adic index plateau at 6 through level 4 was not stabilization); B734:
m004 IS congruence at level (2)³ = (8) (index 12 reached; sisters at successive 2-adic
depths), two-seat. Proof shape: direct index computation with the SL/PSL-center
bookkeeping that also generated E21. Flags: B734 itself flags the result as
Serre-base-rate-defying and PENDING literature replication — that caveat should travel
with any citation; note the separate B794 result (Γ₄₁ congruence of level (4) in the
SL-kernel convention) is a DIFFERENT filtration convention, reconciled in the LAW_MAP
mod-4 row and E23 — a reader can easily conflate the two levels ((8) PSL-geometric vs (4)
SL-kernel).

**B733 (observer space).** Claim: the menu of observers is a BOUNDED discrete 𝔽₂-space —
one global conjugation bit at every congruence depth (INERT2: one Frobenius across all
inert primes simultaneously), diagonal rank saturating at 3; never a continuum. Proof
shape: sealed 3-probe campaign + two-seat consensus resolving both flagged opens. Feeds
C20's rank saturation. No flags.

**B736 (A+B+C campaign).** Claim: the object-level observer is OBSTRUCTED (finite level ⇒
no β=1 SSB — the SSB IS the ζ_K pole, an infinite-tower object; H³ not Hermitian ⇒ no
Shimura), and the parameter-reduction no-go is rigorous (0/24 SM parameters; equivariance
wall T=0 recomputed; kind-mismatch; bounded ceiling). Proof shape: sealed joint two-seat
campaign, both headline verdicts converged; the "no landing site" leg RESTATED by addendum
(it over-reached — the C-cal/JUNO conditional route is the one live landing, low-weight).
Ledger C17 (part). Flag: the addendum's restatement matters for anyone quoting "three
obstructions" — the rigorous kill rests on two.

**B737 / B739 (candidate zero; character rigidity).** Claim: φ_m004(s) = Λ_K(s−1)/Λ_K(s)
exactly with Res φ = 2√3/vol (a new one-cusp exact-transfer lemma); the crux composition
(voice = SSB carrier) DIES (MB12 vacuity + object-deletion); B739: the continuous
spectrum is character-rigid — one channel, Fourier support restricted, NO conductor-(4)/(8)
character anywhere in the continuous part (proven-in-sandbox modulo three named classical
inputs, source-verified exhaustion). Proof shape: sealed preregs, skeptic loops (round-1's
positive killed), 0/3 refutations. Ledger C10. Flags: B739's honest bounds are explicit
(scalar weight-0 only; classical inputs cited not re-proven); note the H-EAR
correction history — the "voice carries no golden" leg from these arcs' era was later
re-typed by B857 as a splitting-type statement (5 inert in ℚ(√−3)), a correction carried
on the LAW_MAP row but NOT in B737/B739/B746's own files.

**B740 / B747 / B748 (the census triple).** Claim: on the completed 78-slope grid no
closed hyperbolic filling's invariant trace field contains √−3 (B740 — upgrading B288's
asserted-on-54 to earned, two seats two methods), nor √5 (B747), nor √−15 (B748) — the
entire forced V₄ is interface-only (census fact, stated as such). Proof shape: exact field
computations + the amphichirality shortcut (verified 7/7 isometries); cc2's disjoint
pipeline closed residuals mutually. Ledger C8. Flag preserved in-file: cc2's lindep
fallback produced 20 FALSE "CONTAINS" witnesses (the unbounded-coefficient trap) — caught;
the standing lesson is recorded.

**B743 (rung-1 widened).** Claim: the CM-collapse THEOREM (real elements of ℚ(√−3,√5) are
exactly ℚ(√5), killing the V₄/cyclotomic widening) + a noise-floor-calibrated PSLQ sweep
with 0 gated hits — and the instrument independently re-found and correctly REJECTED Koide
Q = 2/3 as rational/zero-object-content. Proof shape: cc2 package, cc verify-on-receipt
(4 exact spot-checks incl. j = −1/15 and the 683σ non-near-hit). Also the witness that
untestable targets are NAMED (digit-budget honesty). No flags.

**B745 / B755 (revivals + carried recomputes).** Claim: B745 cross-verifies the two audit
revivals (B58's SL(4) tower numerically testable after all; B225's 2-half vacuous —
retracted as kill, reopened); B755 locates 5/5 carried discriminating facts by recompute —
including cell 3's from-scratch reproduction of the GSWZ eq (1)/(2) coefficients from the
Kashaev sum with an out-of-sample N-prediction at 0.2% (replacing a VACUOUS lock), and the
1/4-numerology null computed in-repo. Proof shape: sealed preregs; independent-layer
checks; instrument traps logged (pslq working-precision; parity trap). No flags — these
two arcs are the band's model recompute discipline.

**B746 (golden ledger).** Claim: 10/12 structural floors carry FORCED-golden appearances;
the voice (F11) carries NONE — the two-column law (golden = dynamical/hearing column;
Eisenstein = geometric/being column). Proof shape: sealed prereg with a 65% base-rate
guard (mention never counts), 4 spot-checks, grep-verifiable absences. **Flag:** F11's
"zero golden markers" leg is exactly what B857 (2026-08-02) re-typed — the supporting grep
predated B797's Maass work, and the exact fact is a_K(5) = 0 by inertness with the
blindness MUTUAL and NOT a property of voices; the correction lives on the LAW_MAP H-EAR
row (clause iii) but B746's file carries no correction header. A reader of B746 alone
gets the superseded framing.

**B749 (genesis forks).** Claim: the axiom chain priced — 4 ROBUST, 2 FRAGILE (F5
orientation: the discarded sibling IS the Gieseking, m004's own parent; F6 closure: Sol
keeps the HEARING — contra-prior), F8 GEOMETRY-NECESSARY (the combinatorial carrier sees
only ℚ(√5); ℚ(√−3) is bought at geometrization). Proof shape: cc3 branch, journal-gated
10-agent execution, two §16 reviews (one real STOP remedied — the false quadratic=metallic
universal), priors recorded pre-compute with one falsified and reported. Ledger C1–C5
prices. Flag (ledger-side, resolved): the C1/C2/C4 lock citations were wrong until B1003
wrote the missing F2/F8 locks — the B998→B1003 saga is recorded in the ledger's own
footnote (and the E53-class note that the audit's remedy had already closed the gap);
C2's F3 test still does not exist per the stamped note.

**B750 (lack ledger).** Claim: every banked refusal-to-close falls into exactly three
sealed classes (no basepoint ×8 / no bandwidth ×3 / no name-transmission ×2), X empty,
with can-fail witnesses. Proof shape: sealed enum + admission criteria + citation-
existence checks; an assembly arc asserting no new mathematics. Ledger C16. No flags.

**B751 / B752 / B753 (the α_s adjudication cluster).** Claim: the "1/(2φ³) = α_s" claim is
NOT EARNED (per-letter attribution unbanked; Im part 0.4253 silently dropped; scale
knob-dependent; base-rate null; later a THIRD insertion — Re vs Born |·|²); B752 kills
Op-1 by the handoff's own rule and dissolves Op-3 three ways (Cayley–Hamilton; wrong
trace; repelling fixed point); B753 computes the kind-correct object — the unistochastic
overlap matrix with |B₀₀|² = 1 − p = 1/(φ√5) exact, twist-invariant, and pins the JUNO
registration to 0.30902 unchanged. Proof shape: sealed preregs, two/three-seat
convergence, the courier's sign puzzle resolved as the B592 sign-flip theorem (both
seats right about different operators). Ledger C17 components + C13. No flags — but note
these are the arcs that make the H-TUROK pin's status precise (hint, no mechanism).

**B754 (P2 spectral stratum).** Claim: 19 flagged negatives re-adjudicated against the
frozen spectral surface — 17 KILL-EXTENDS, 2 FACE-IRRELEVANT, 0 FACE-OPENS; WALL-1 gains
four spectral mechanisms; two skeptic overrides (a 37-class census the cell should have
run; a field conflation corrected). Proof shape: cc3 journal-gated campaign, adversarial
skeptics, later gate-coverage re-execution (8/19 by cc + 8/19 by cc3, zero divergence,
per B756's addendum). Ledger C17 (part). No flags.

**B756 / B757 (remaining doors; two-ℤ/3).** Claim: B756 — the B699 general gloss refuted
with exact counterexamples (counterexample count honestly stated reading-dependently:
4 field-reading / 5 seed-reading / 6 with cc's own extra); the hearing multiplication law
proved as an exact iff (a_m·a_n = a_mn ⟺ a residue condition, exact defect (1−√5)/2 —
ledger C15); DOOR6 re-executed to byte-identical depth. B757 — the two-ℤ/3 identity
DISSOLVED (torsion-free vs order-3 at element level; the mod-4 coincidence is one
conjugacy class in GL(2,ℤ/4) — E20-forced). Proof shape: verify-on-receipt + in-seat
recomputation; sealed preregs. No flags.

**B759–B762 (the QP forks).** Claim: QP-3 INTEGRATED (chord/sum coupling emerges at SL(3),
fraction 15/32; the discriminant law — later scope-corrected by B764); QP-4 NO-HATCH (no
object-native operation signs the chord; {ζ₅,ζ₅⁴} inseparable; five operations fail);
QP-2 FLAT (fiber_dim = 0 at n = 2,3,4 — no private states; double-method with a HALT that
caught a convention bug); QP-1 QUINE (m004 unique among 203,123 census manifolds on its
spectral dataset; the sister separated by cusp shape). Proof shape: cc3 sealed preregs,
double-method cross-validation. Ledger C18's four priced forks. Flag: QP-3's original
√|disc K| law was corrected within a day by B764 (below) — the ledger's C19 carries the
correction; the QP-3 file's "discriminant law" section is superseded as a general claim.

**B764 (C19 comparator).** Claim: the sealed 5₂ prediction (√23) FAILED and the corrected
law was found in the same run — the off-block equals the geometric Riley pair separation
|u−ū| ALWAYS (= √|disc K| identically only for imaginary-quadratic Riley fields, now
proven rather than induced). Proof shape: sealed prediction + 40-digit factorization
verification. The record's advertised first demonstration that chain links are falsifiable
objects. No flags.

**B766 / B769 / B782 (measurement torsor; T1; C22).** Claim: the discrete closing space
has 𝔽₂-rank EXACTLY 3 (c, θ, γ₅; γ₃ ≡ c) with time's arrow = the basepoint bit and
chord = c⊕θ, RANK-SATURATED against B733's menu; T1 is a discrete 3-frame torsor whose
fixedness is FORCED (abelian triviality) with no invariant continuous modulus at the
geometric point; C22 — the closing action is free ⟹ no equivariant section (choice is
symmetry-breaking) with the corollary honestly labeled definitional (the B784-audit
COROLLARY class). Proof shape: sealed preregs; cc3 audit upgraded a hardcoded θ-entry to
a derived matrix-level one (the trace-blindness lesson); C20 later strengthened (computed
flip-vectors; ι-vs-θ distinction via B786). Flags: this cluster is the origin of the
recurring c-odd/θ-odd conflation class — the C21 mechanism was corrected once (2026-07-25)
and the guard lemma (LAW_MAP row 70) exists precisely because two retractions (B780,
cc3's B784) came from it.

**B769 (see above) / B775 (phase-2 wave 1).** B775 claim: P2-T1MOVER — the realized
subgroup of Out(V₄) = S₃ is {identity}: the T1 3-frame choice is unbroken by any
object-native operation (a chain no-go, C23), with the scope honesty that I2 and the
fixed-point argument share a premise; P2-AABB — γ₅ genuinely DERIVES from σ:a→ab
(disc 5), c and θ do not (1/3 derived, 2/3 analogy); three courier frameworks tombstoned;
P2-SELRULE a genuine theorem. Proof shape: 14 agents, all upheld; one self-caught
false-positive trap (symbols auto-collapsing conjugates) disclosed. No flags.

**B771 (phase-1 wave 1).** Claim: 13 open-item cells — highlights: e₃ = cos(2π/9)/864
EXACTLY (the ζ₂₇ rung of the Chebyshev trisection tower; three routes) → the e₃ THEOREM
row; L39's period formula proved all-t (the L39 THEOREM row); OI-055's conditional kill
proved all-n in-cell with the single premise identified as the GSWZ theorem (EXTERNAL);
two verifier catches (a circular scale choice; a lost report re-run rather than
reconstructed). Proof shape: 25 agents, every verdict adversarially re-run, cc
hand-spot-checks. No flags.

**B785 / B786 / B789 (cc3 gate harvest; θ/ι; the intertwiner).** Claim: B785 harvests
H1–H3 (B768 correspondence; B489 all-n Binet closure; TOMB-L255 all-d spectrum) with the
b769 "tangent frames align" mechanism EXPLICITLY EXCLUDED at the gate (the conflation
class); B786: the character-variety third generator is ι (inversion), θ being
trace-trivial at every rank — the object's rank 3 unconditional (self-dual collapse), the
full-variety rank-4 left conditional on cc3's corrected S; B789: the explicit intertwiner
Q = S_ι·S_sd⁻¹ conjugating ρ∘(transpose∘reversal) to ρ — with V2 (descent to the knot
group) new to both seats, the group-level identity proved FALSE (abelian obstruction), and
a guessed-relator near-miss disclosed (a wrong relator almost produced a fabricated
negative). Proof shape: re-derivation from scratch under the cc3-never-merges rule. These
three arcs are the θ-triviality guard's constructive spine. No flags.

**B790 / B791 / B794 (the Maass receipts).** Claim: B790 adjudicates the Maass handoff —
Tests 1–3/5 VACUOUS (no data exists; the LMFDB Hecke-vs-Laplace conflation named), the
length-spectrum side computed (m004 ≠ m003; traces exactly ℤ[ω] — forced, stated as such),
and L3's four apparent SM matches (incl. ℓ₀/ℓ₅₁ ≈ sin²θ_W to 4 figures) adjudicated an
EARNED MISS — after a three-attempt null saga in which BOTH first-pass nulls were wrong
(uniform never preregistered; "Weyl-matched" miscoded e^ℓ for e^{2ℓ}; two repairs
disagreeing 200×) and four Chat-1 challenges were all conceded (C1–C4, incl. H0-scope
import). B791: the Weyl completeness criterion banked with two posted corrections (the
per-sector count factor; the multiplicity trap — cc misapplied its own corrected criterion
within the hour), the λ₁ = 51.014 "fabricated" escalation withdrawn after cc3's
independent solver corroborated it, and the honest status line "the chain from raw
generators to a certified spectral parameter is verified at its two ends and unverified in
the middle; the door is unlocked, unopened." B794: Γ₄₁ congruence of level exactly (4) in
the SL-kernel convention + the mod-4 trace-norm law N(tr) ≡ {0,3} (never 1) — with the
PSL-naming corrected (1920 = |SL/{±I}|, not PSL; B731's 6 and B794's 12 both right in
different groups), and the silent-discard filter episode (cc's tolerance filter dropped
the long geodesics carrying disconfirming norms — the new error class "a filter that
discards data must report its discards"), plus the B920 level reconciliation of the
norm-split hint. Proof shape: receipts with prereg seals preserved byte-exact through a
renumbering. Flags: this cluster is the band's densest concentration of
disclosed-but-real instrument failures (permissive-direction null errors, hand-set caps,
silent filters); everything load-bearing was corrected in-file, but any citation of B790's
first-pass numbers is stale.

## F. Older harvest rows (§A/§C late additions)

**B437 (child abelian book).** Claim: the "golden return" RETRACTED as inheritance (the
trefoil control: every knot at slope 5 gets ℚ(√5) — numerator-forced); the Lucas-square
law survives as formula; the INVERSION LAW (inherited-looking = generic; special =
parent-disjoint), sharpened by B438 to three tiers with figure-eight-UNIQUE = none found.
Proof shape: surgery formula + controls added by adjudication. **Flag:** the LAW_MAP
H-EAR row (clause iv) cites B437 as "children keep golden traces in their abelian towers
while losing every face" — B437's own correction says the field-return is slope-generic,
not parental hearing survival; the value-level (Alexander-data) reading is the survivable
one, and the row's compressed phrasing leans on the retracted framing. Worth the
evaluating seat's eye.

**B471 (chain verification).** Claim: tr[A_m,A_n] = 2−(mn(n−m))² symbolically, so
(golden, silver) = (1,2) is the UNIQUE metallic pair whose commutator closes the cusp —
with the attribution corrected 2026-07-29 (classical territory, Cohn 1955 — cited not
claimed; the metallic-body reading is the program's). Proof shape: symbolic identity + P4
adversarial-panel corrections (the "alphabet = root locus" claim refuted twice-over, and
the corrected class-number-conditional statement). Flag: the harvest row's own note that
cc's first LAW_MAP transcription omitted the Cohn attribution the arc had carefully
recorded — an attribution near-miss caught at review.

**B489 (self-interaction tower).** Claim: the cyclic-cover tower with torsion |L(2n)−2|
(classical Fox–Weber), vol = n·v₄ exact, abelian DGG rank 2n−1 at every level (blocking
the Gang–Yonekura SU(3) hope — the handoff's own falsification test resolved negative);
4c refuted on a wrong volume; §3's "tower generates the program's numbers" graded largely
numerology with only the n=2 5 = det(4₁) link structural. Proof shape: independent SnapPy
+ exact matrix recomputation; later stabilized all-n by B785/H2 (Binet). No flags.

**B518 (K025 confirmation).** Claim: κ−2 is a substrate-independent scale-free
universality class (tier A confirmed); tier C upgrades the root dictionary to derivation
(RL/−RL⁻¹/seam); tier B's "firewall crossing" label CORRECTED in-file (B519's adversarial
gate refuted it 3-0 — the mixed-chain 2×2 table confirms known gap-labeling additivity,
not fundamentality). Proof shape: trace-map computation + in-file correction. Flag: the
κ-unification LAW_MAP row cites B518 as the universality-class witness — accurate — but
tier B's original crossing framing survives in some older prose; the correction is
in-file and governs.

**B533 (coupling invariance).** Claim: the coupling carries exactly 5 (→ 6 at longer
windows, B535-scoped) discrete algebraic fingerprints; the audit REVERSED the original
"not GL(4,ℤ)-conjugate" claim — all induced matrices are ONE class (Latimer–MacDuffee +
h(ℚ(√φ)) = 1 proven end-to-end + explicit conjugators), so the five types are five
markings of one object; the τ = √φ Perron identity β = 1/(√φ−1) proven; Gate 3's SM-ratio
lattice search closed with a CORRECTED false-positive control (the original 7-vs-1.2
excess was a control-mismatch artifact). Proof shape: exact/symbolic audit
(Fable-5-labeled) upgrading and correcting the numeric first pass; census scope pinned to
length ≤ 3 with the B535 completion noted. Flags: three original claims (S1 spectrum, S2
conjugacy, S3 mixing) were wrong as first banked and are corrected in place — the LAW_MAP
harvest row states the corrected form; the arc is a case study in numeric-residual
conjugacy tests being broken.

**B534 (dark hyperbola).** Claim: T(j,l) = 0 ⟺ jl ≡ −4 (mod p), (j,l) ≠ (2,p−2), with
magnitude spectrum {0,1,√p} — PROVED for all odd primes (complete-the-square Gauss-sum
argument), power-set magnitudes at square-free N, asymptotic darkness (Mertens), and the
all-n tower torsion law — all upgraded from float to exact with zero floats in decisive
computations. Proof shape: direct proofs + exact group-ring verification at 12 primes.
Convention caveat pinned in-file (the theta-lift, not the B476 pair). No flags.

**B565 (gauge-behavior campaign; RESULTS.md).** Claim: the wall-5 witnesses — chiral
index ≡ 0 (T3: exact chiral symmetry, amphichiral pairing exact); the ℤ/11 closed by
decoupling (T1); no real form (H1: non-real adjoint traces — the same fact B715 reuses);
the two-faces compactness split (algebra face provably non-compact, measurement face
compact-finite); plus the 123-negative exhumation (113 sound, one cracked component —
S014's "~60% null" clause never computed in-repo and irreproducible, epitaph corrected).
Proof shape: 44-agent campaign, adversarially verified, two framing rejections recorded
(R4's false corroboration struck by the verifier against the cell's own unreported rank
data). Flags: R2/R3 are honest PARTIALs sometimes cited as closed; the S014 epitaph
episode is the band's cleanest documented case of an uncomputed number sitting in a
tombstone for months.

**B604 / B605 / B607 / B608 (the Rosetta/wall-4 block).** Claim: the pair-to-block
assignment DOES NOT EXIST (B604 — chat-1's D₅/16 table refuted at h = 2,3; the principal
grading and θ-pair decomposition are incompatible); the amphichiral involutions are FREE
glides (B605 — the handoff's reflection conclusion refuted; the Gieseking deck
identification closes it exactly); the odd sector is charge-mixed except the two spinor
tips (B607), and the mixing goes down to the roots (B608 — 9/12 pair-combos class-mixed;
the only G_SM-gradable lines are the (1,1,2) tips). Proof shape: exact root-system
computations with verify-don't-trust refutations of the incoming handoffs; one
accounting iteration disclosed (B608's first C3 draft double-counted). Witnesses for
walls 4/5 and the no-sector-alignment leg of B706. No flags.

**B652 (Gate B verdict).** Claim: the freedom count N = 1 (discrete, binary — the Galois
branch of the golden character); chord/ladder/scale organs N = 0; PASS with two named
binding residues (A3 coupling-inventory completeness bounded; A4 stage-selection
obligations open — "stage = choice" qualifier mandatory on any Phase-C verdict). Proof
shape: sealed grammar table + vacuity checks both ways. Witness for GATE B's N = 1
discrete in wall 10's assembly. No flags.

**B706 (rung-2 SM freedom).** Claim: NO-MATCH at both rungs — the SM flavor ratios are
PSLQ-generic over the audible field (rung 1, two seats), and the object's freedom is
discrete 𝔽₂ vs the SM's continuous ~19 reals (rung 2, a KIND mismatch); the Cabibbo 9/40
candidate killed by field-mismatch + no-mechanism, not base-rate. Proof shape: sealed
Gate-5-SM design, two-seat double verification. Wall row 11's witness. No flags.

---

## RED FLAGS (assembled for the evaluating seat; file/arc + one sentence each)

1. **B684 (frontier/B684_loop7_close) vs LAW_MAP row 53 (own-channel law):** the arc's
   2026-08-19 addendum (B1072) reports a k-indexing/inversion defect in the silver SU(4)₂
   ladder affecting the VALUE attribution of "silver hears 1/δ at SU(4)₂," but the LAW_MAP
   row still reads "LAW (2 instances, exact)" with no caveat — a live-surface/arc-body
   contradiction.
2. **B746 (golden_ledger F11) and B737/B739:** the "voice carries zero golden markers" leg
   was corrected by B857 (grep predated the Maass work; the exact fact is mutual
   inertness, NOT a property of voices) — the correction lives only on the LAW_MAP H-EAR
   row; the three arc files carry no correction headers and read as live in the superseded
   framing.
3. **B437 vs LAW_MAP H-EAR clause (iv):** the row's "children keep golden traces in their
   abelian towers while losing every face" compresses a claim B437's own trefoil-control
   correction retracted as inheritance (the field-return is slope-generic); the surviving
   content is Alexander-data values only — the row leans on the retracted framing.
4. **B699 (two_object_surgery):** the general "5-inert ∧ fibered ⇒ golden" reading was
   refuted (B756, five-plus counterexamples) — carried on the LAW_MAP row and in B756 but
   NOT as a header on B699's own FINDINGS; reading the arc alone overstates it.
5. **B640 (hearing_group):** "im ρ ≅ 2I×ℤ/3" is the HEARING rep, not the raw mod-5
   holonomy (which fills SL(2,𝔽₂₅)); the disambiguation lives in B699/LAW_MAP only —
   B640's file is silently misreadable.
6. **B645 (dial_law):** banked with NO preregistration (disclosed in-file, hashes
   post-hoc) — every claim is an exact identity, but it is the band's clearest
   exploratory-post-hoc law bank.
7. **B644 (mckay_comparison):** the sealed M3 reference tables were internally
   inconsistent as characters (the vacuity class), adjudicated post-run — one sealed
   clause could never have passed as written.
8. **B790/B791 (Maass receipts):** both first-pass nulls were wrong (one never
   preregistered, one miscoded e^ℓ for e^{2ℓ}), a "fabricated" escalation was withdrawn,
   the completeness criterion was misapplied by its own author within an hour, and cc's
   verification filter silently dropped disconfirming long geodesics — all corrected
   in-file, but any citation of first-pass numbers is stale, and the Maass door itself is
   "unlocked, unopened" (no certified m004 eigenvalue exists in these arcs; B797/B795 are
   outside this band's read set).
9. **B731 vs B734 vs B794 (congruence levels):** three different correct statements in
   three different filtrations — PSL-geometric level (8) (B734), SL-kernel level (4)
   (B794), and B731's retracted non-congruence — are easily conflated; B734's own
   Serre-defying caveat (pending literature replication) should travel with citations.
10. **B615 (comparison):** the frozen PDG targets were recorded from the assistant seat's
    knowledge and two null-arithmetic bugs were fixed after a first statistics printout
    (disclosed) — the CLOSED-NEGATIVE-RECORD row rests on these disclosed wobbles not
    having touched match rows, which is asserted, not re-verified, in-file.
11. **B675 (hcusp):** the LAW row's "silver exact both ways" includes an SU(4)₁ hearing
    check the arc itself flags as numeric-at-two-precisions, not exact.
12. **Listener-map identification (B592/B593 lineage vs live board):** B1231's
    identification discipline (live board, 2026-09-01) types the listener map u itself as
    an unpriced identification "performed for free for two years" — none of the band's
    hearing/coupling arcs state this; every LAW row downstream of B593's matrix elements
    (H-EAR clause iv, the McKay tensor row's consequences, the coupling-rigidity row)
    inherits an input the current discipline says was never priced.
13. **B660 (structure_campaign):** two of its four cells were later corrected in part
    (S2's cubic obstruction shown a monomial-ansatz artifact by B662/F; S4's zero shown
    basis-local by B662/H) with the corrections recorded downstream, not as headers on
    B660 — the wall-10 assembly leg (S3) is unaffected.
14. **B666 wave-2/3 detail unread (this sweep's own cut):** the widely-cited R3
    (Landsberg–Schaar mechanization of LAW-O) and S (scale-torsor theorem) cells are
    digested here only via the campaign synthesis — if the evaluating seat needs their
    proof shapes verified, the wave files must be opened.
15. **B627 (silver exterior torsions):** three of six values (m = 7, 8, 11) remain
    exact-form-unidentified complex numbers; the exterior sign law's "silver 6/6" is a
    numeric-real-part statement at those exponents.
16. **B471 harvest attribution:** the arc recorded Cohn 1955 carefully; the first LAW_MAP
    harvest transcription dropped it (corrected 2026-07-29) — a near-miss of claiming
    classical territory, caught, worth remembering as a class.

*End of S2b digest. No claim above is adjudicated here; row-vs-arc discrepancies are
flagged for the evaluating seat, not resolved.*
