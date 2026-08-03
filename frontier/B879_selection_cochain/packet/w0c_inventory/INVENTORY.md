# W0c — THE GOLDEN-UNIQUENESS INVENTORY
# (seat cc3, selection/cochain campaign; read-only sweep of /Users/dri/oa-seat-cc3/origin-axiom;
# 2026-07-17; every row below cites a file this agent actually opened)

Scope key (per PREREG_SCC.md W0c): **METALLIC SLICE** = the single-block family
`R^{n-2}L` (trace n) used in the SU(3)₂ hearing-landscape work (B664/B665/
B666/B670). **GENERAL FAMILY** = either (a) all cyclic primitive R/L words of
any block structure, or (b) the *other*, symmetric "metallic" tower
`M_m = R^mL^m` (golden m=1, silver m=2, bronze m=3, …) used in the
arithmetic/trace-field/dimension-grammar work (K009, B197, B649, B657,
B662). **These two families are NOT the same object** and the repo's own
prose calls both "metallic" — every GENERAL FAMILY row below states which
of the two is meant. **OBJECT ALONE** = statements purely about the golden
word RL / trace 3 / disc 5, not a family comparison.

Status key follows the repo's own LAW_MAP.md classes: THEOREM (proved,
machine-verified) / LAW (exact on every computed instance, mechanism open
or partial) / CERTIFIED (exact certificate, no mechanism claimed) /
CONJECTURE-OPEN / REFUTED.

---

## PART A — PROPERTIES THAT SINGLE OUT THE GOLDEN OBJECT (banked, standing)

### A1. Prime conductor ⟺ unit det(A−I) — ONE criterion, not two

**Statement:** for the metallic slice `R^{n-2}L`, the conductor factors as
`(n-2)(n+2)`; PRIME CONDUCTOR ⟺ `n-2 = 1` ⟺ UNIT `det(A-I)` — these are
literally the *same* criterion on this family, not two independent ones.
The golden (n=3) is the unique unit-determinant word of the slice.

**Citation:** `frontier/B664_metallic_landscape/FINDINGS.md` (lines 36-42,
"The 'five independent criteria' collapse"). Confirmed independently by
`frontier/B665_landscape_reconciliation/FINDINGS.md` ("Reciprocal
corrections… (i) 'three properties, not five' still over-counts").

**Scope:** METALLIC SLICE (`R^{n-2}L`).
**Status:** THEOREM (exact factorization; 38/38 numeric confirmation
in B664's `landscape_verify.py`).

### A2. THE HEARING LANDSCAPE THEOREM (SU(3)₂) — golden = minimum nonzero modulus + period origin

**Statement:** for every metallic word `R^{n-2}L`, the θ-odd block is
2-dimensional and T-diagonal: `tr_odd(n) = t1^{n-2}X11 + t2^{n-2}X22`,
exact T-phases `t1=e^{2πi·2/15}`, `t2=e^{2πi·8/15}`. Closed form:
`|tr_odd(n)| = (2√3/D)·|cos(π(4n-5)/10)| ∈ {0, 1/φ, 1}` (exact via
`sin²72° = D²/12`, `sin²36° = D²/(12φ²)`); modulus period 5; reality
period 15 (real ⟺ n ≡ {0,3,5,6,9,10,12} mod 15). **The golden word (n=3)
attains the minimum nonzero modulus 1/φ, and the landscape's period (5)
equals the golden word's own conductor (tr²-4 = 5).**

**Citation:** `frontier/B664_metallic_landscape/FINDINGS.md` (full file);
`docs/LAW_MAP.md` row "THE HEARING LANDSCAPE THEOREM (SU(3)₂)".

**Scope:** METALLIC SLICE (`R^{n-2}L`).
**Status:** THEOREM (exact phases + exact trig identities + 38/38
numeric).

### A3. THE SHADOW-CLASS LAW (general form)

**Statement:** `|tr_odd(W)| = 2·|tone(class of W mod 5)|` for ANY word W
(not just the single-L slice) — the hearing modulus is twice the
pentagon-cosine of the word's mod-5 shadow class. Verified witnesses:
RLRL (trace 7) → φ, real; R⁵L (trace 7) → 1/φ, complex — same trace,
different mod-5 class, so **trace alone does not determine hearing**.
All five doubled tones {0, 1/φ, 1, φ, 2} occur across general words; the
single-L family (A2) reaches only {0, 1/φ, 1} — i.e. A2 is the shadow
law's restriction to the metallic slice.

**Citation:** `frontier/B665_landscape_reconciliation/FINDINGS.md`.

**Scope:** GENERAL FAMILY (arbitrary R/L words).
**Status:** LAW (verified witnesses; general form credited to cc2,
verified on this seat's banked stage build).

### A4. Stage-universal form + E6 instance + generating function

**Statement:** `|tr_odd(W)| = |χ_D(shadow(W))|` with D = dim(θ-odd) = the
shadow-irrep dimension, holding at BOTH the golden (SU(3)₂: |χ2| of 2I
mod 5, period 5) and E6 level-2 stages (|χ3| of PSL(2,7) mod 7, period 7,
values {0,1,√2}, 547-word corpus, 6/6 classes). Each stage hears only its
own shadow (RRLL: loud-real at golden, DEAF at E6). Generating function:
`a_n = (φχ0(n) + φ⁻²χ2(n))/2` exact (additive Dirichlet form exact;
Euler-PRODUCT form REFUTED, a3·a7 ≠ a21).

**Citation:** `frontier/B666_leads_campaign/WAVE1_FINDINGS.md` (CELL 3).

**Scope:** GENERAL FAMILY (arbitrary words) × multi-stage.
**Status:** THEOREM-grade on the family (1e-9 numeric on the corpus);
"full projective equivalence… supported, not sealed" per the same file.

### A5. The self-selection half-law (conductor-aligned rows) — delimited

**Statement:** across the 16-word × 12-stage cross-landscape matrix, the
"diagonal" (self-selection: a word hears quietest at its own conductor's
stage) hypothesis HOLDS distinctively on 8/16 rows — minima entirely on
conductor-divisibility stages (golden's 1/φ recurs at κ = 5, 10, 15; the
trace-4 word's minimum sits EXACTLY at its conductor stage κ=12, value
`√3-1`, verified to 1e-9) — and FAILS cleanly on the rest (6/16 rows
non-distinctive; n=11 off-conductor). **Not a universal law; the golden
remains its cleanest instance.**

**Citation:** `frontier/B670_anatomy_full/packet/loop2/b4_landscape/FINDINGS_CC2.md`
(cc2, prereg addendum c6d4fabd); adjudicated in
`frontier/B670_anatomy_full/FINDINGS.md` ("THE CROSS-LANDSCAPE").

**Scope:** GENERAL FAMILY (16 words × 12 stages).
**Status:** LAW, delimited (half — 8/16 rows; explicitly NOT a universal
selection law).

### A6. The clean bifocal split (linear disjointness) vs the silver's entangled Q(ζ8)

**Statement:** the golden's trace field is `ℚ(√-3)` alone (the BEING end);
the hearing generator `√5` is a *different*, disjoint field —
**`ℚ(√-3)` and `ℚ(√5)` are linearly disjoint over `ℚ`** — "the golden is
bifocally CLEAN." The silver's trace field is `ℚ(ζ8) = ℚ(i,√2)`, which
*contains* its own hearing generator `√2` — "the silver is bifocally
ENTANGLED." Sharpened by the subfield theorem (A7): on BOTH objects the
chord data descends to the being field k(Γ); what is golden-special is
only that the trace field itself adds nothing beyond the being field.

**Citation:** `frontier/B663_bifocal_anatomy/BIFOCAL_CLARIFICATION_CC2.md`
(line 63, "the clean split is golden-SPECIAL"); adjudicated + sharpened in
`frontier/B663_bifocal_anatomy/FINDINGS.md` ("THE ENTANGLEMENT STATEMENT");
silver field established in `frontier/B649_silver_holonomy/FINDINGS.md`
(Stage 1, "the trace field contains ℚ(ζ8)").

**Scope:** OBJECT ALONE vs. the silver (a two-object GENERAL FAMILY
comparison, symmetric tower `R^mL^m`, m=1 vs m=2).
**Status:** THEOREM-backed statement (fields exact, both objects; general
mechanism — the subfield theorem A7 — is a THEOREM).

### A7. The subfield law / σ*-equivariance theorem (chord data ∈ k(Γ))

**Statement:** the chord data (σ*-matrix AND the full Y-tensor) is defined
over the object's invariant trace field k(Γ) — proved for the two banked
objects via Galois descent: `Gal(L/ℚ(i))` (silver) acts by
sign-twisted conjugation with exact 1-dim intertwiners; the banked H¹
basis is itself a ℚ(i)-form (15/15 cocycle-level fixings); Y and C are
Galois-fixed ⇒ ∈ k(Γ), FORCED. The golden (fig-8) is the *degenerate*
case where trace field = k(Γ) exactly (Neumann–Reid).

**Citation:** `frontier/B662_successor_campaign/WAVE1_FINDINGS.md`
(CELL D); `frontier/B662_successor_campaign/cellD/PROOF_NOTE.md`.

**Scope:** GENERAL FAMILY (symmetric tower, proved on the two banked
members; general mechanism identified for any member modulo two named
non-automatic steps).
**Status:** THEOREM (two objects).

### A8. The conductor identities

**Statement:** `Δ(-1) = det(A+I) = tr²-4`; `det(A-I) = -1`, the unit (for
the golden A₁, trace 3); the two Gauss conductors t₊/t₋ equal the two
lifts' torsion homologies (`|H₁(Σ₂(4₁))| = 5`, the branched double cover
is the lens space L(5,2)). "The golden 5-tone's conductor det(A+I)=5 is
literally the first homology of the twisted double."

**Citation:** `frontier/B591_chord_manifold/FINDINGS.md` (M1, M2 — "THE
HEADLINE"); `frontier/B588_sector_exchange/FINDINGS.md`; `frontier/
B634_conductor_chord/ERRATUM_1.md` (item 4: "G1 (the conductor
identities) STANDS as computed").

**Scope:** OBJECT ALONE (with the general closed form `Δ(-1)=tr²-4`
applying to any hyperbolic word).
**Status:** THEOREM (identities).

### A9. The one-door theorem (the field's only entry point)

**Statement:** in the Weyl-twisted Weil factorization, of the twelve
Gauss/Weyl-class conductors, only the six signed reflections carry the
non-square `4-t²`; every other conductor (identity, -identity, rotations,
-rotations) is a PERFECT SQUARE. So the object's field `√(t²-4)` can only
enter the stage trace through the reflection coset — "the field has
exactly one door."

**Citation:** `frontier/B620_conductor_mechanism/FINDINGS.md`.

**Scope:** GENERAL (proved for any hyperbolic monodromy trace, verified
on traces 3,4,5,6).
**Status:** THEOREM.

### A10. THE SIGN-HEARS-THE-DISCRIMINANT THEOREM

**Statement:** for `B_w = tI - w - w⁻¹` over a Weyl group on an even-rank
lattice, `det(w) = (-1)^{v_p(det B_w)}` for every w iff `v_p(t²-4)` is
odd. Proved unconditionally (B666 cell 4): self-reciprocal ⇒
`f(ζ)f(ζ̄) = (t-ζ-ζ̄)²`, a literal square, so no ramified split exists at
any prime — both directions plus the exactly-half law are abstract
theorems for any finite-order element of `GL_n(ℤ)`, n even.

**Citation:** `docs/LAW_MAP.md` (§A, "THE SIGN-HEARS-THE-DISCRIMINANT
THEOREM"); `frontier/B666_leads_campaign/WAVE1_FINDINGS.md` (CELL 4).

**Scope:** GENERAL (any finite-order element of GL_n(Z), even rank —
proved on 207,384+ words, all W(D4), all 51,840 W(E6), symbolic m=3..50).
**Status:** THEOREM — unconditional.

### A11. THE CONGRUENCE-SHADOW THEOREM (the ear IS the mod-5 shadow)

**Statement:** on `ker(det) ≅ 2I` of the hearing group, `ρ_hear = χ_golden
∘ (mod-5 reduction)` — the ear at the minimal bearing stage κ=5 hears the
infinite Anosov monodromy through its congruence shadow AT THE CONDUCTOR;
the conductor (5) is literally the modulus of the ear. `tr ρ_hear(RL) =
-1/φ`.

**Citation:** `frontier/B644_mckay_comparison/FINDINGS.md` (full file;
gates M1-M4 all PASS, 0/560 kernel mismatches).

**Scope:** OBJECT ALONE (the golden word, at its own conductor 5).
**Status:** THEOREM (verification strength, elementwise).

### A12. THE HEARING-GROUP THEOREM

**Statement:** the hearing representation's image is `2I × ℤ/3` (order
360; `ker(det)` order 120 = SL(2,5) exactly, class equation
`[1,1,12,12,12,12,20,20,30]`); the golden 2-dim character has
`tr ρ(RL) = -1/φ` — the Anosov monodromy heard as the pentagon.

**Citation:** `frontier/B640_hearing_group/FINDINGS.md`.

**Scope:** OBJECT ALONE.
**Status:** THEOREM (class-table verified).

### A13. The dimension grammar (3/5/1) — THEOREM for the whole metallic (symmetric) family

**Statement:** `h¹(M;27)=3, h¹(D_weld;27)=5, h⁰=1` on both computed
objects (golden disc 5, silver disc 32) — a REDUCTION THEOREM
(B656/G5): the grammar is determined by two local inputs
`(i₁,i₂) = (dim V^holonomy, dim V^{peripheral Z²})`; `(1,3)` forces
`3/5/1`. B662 cell A PROVES `(i₁,i₂)=(1,3)` is metallic-uniform (every
member of `R^mL^m`, via a centralizer-of-parabolic lemma + a Zariski-
density lemma; 30/30 exact on both banked objects) — **upgrading the
grammar from a two-object LAW to a THEOREM for the entire family.**
One-per-block refinement (B657/W0b): 27 = V17⊕V9⊕V1 holonomy-block-
diagonal with (h⁰,h¹) = (0,1)/(0,1)/(1,1) per block.

**Citation:** `frontier/B662_successor_campaign/WAVE1_FINDINGS.md`
(CELL A); `frontier/B662_successor_campaign/cellA/PROOF_NOTE.md`;
`frontier/B657_invariant_line/FINDINGS.md` (W0b).

**Scope:** GENERAL FAMILY (symmetric tower `R^mL^m` — proved uniform for
every member, i.e. this is a family-wide THEOREM, not golden-specific;
listed here because the golden was the first witness and remains the
minimal instance).
**Status:** THEOREM (family-uniform, two objects verified exactly,
proof covers all m).

### A14. THE PORTAL LAW (invariant line couples to everything)

**Statement:** `P(u) = [v0 × u]` (the Jordan-cross polarization of the
invariant line v0) is a rank-5 isomorphism `H¹(D;27) → H¹(D;27̄)`, kernel
0, on both objects. On the golden it is exactly block-diagonal on the
boundary-born/solo-inherited split; sector-respecting is FORCED-candidate
(B662/E: the silver's canonical decomposition also reproduces
block-diagonal — the earlier mismatch was a basis-choice artifact).
Mechanism (B663/A1): v0 is an invertible Jordan element
(`N(v0,v0,v0) = -6 ≠ 0`) — the portal is an isomorphism BECAUSE the heart
is invertible.

**Citation:** `frontier/B657_invariant_line/FINDINGS.md` (W1, W2a);
`frontier/B662_successor_campaign/WAVE1_FINDINGS.md` (CELL E);
`frontier/B663_bifocal_anatomy/FINDINGS.md` (A1).

**Scope:** GENERAL FAMILY (symmetric tower, two objects; FORCED-candidate
pending a third object).
**Status:** LAW + MECHANISM (two objects, exact).

### A15. The minimal period 175560 — closed form

**Statement:** the resonant-phase ladder's exact minimal period is
`P = 175560 = 2³·3·5·7·11·19` (`N0/P = 13,167,000`), closed form: P = the
exponent of the total discriminant group (lcm of all Smith elementary
divisors of the 25 Weyl pencils `B_w = 3I - w - w⁻¹`). Zero aggregate
cancellations — independently cross-checks the resonant-phase law
(A16 below): the two routes agree.

**Citation:** `frontier/B662_successor_campaign/WAVE2_FINDINGS.md`
(CELL G); `frontier/B662_successor_campaign/cellG/FINDINGS_CELL.md`;
`docs/OPEN_LEADS.md` (L100 row, "CLOSED").

**Scope:** OBJECT ALONE (the golden's own ladder — trace 3 / disc 5
family of Weyl pencils at the golden monodromy).
**Status:** CERTIFIED (12/12 gates incl. minimality witnesses).

### A16. The resonant-phase law (the ladder's complete voice)

**Statement:** the resonant phase is a constant ±1 per (class, resonant
profile) with NO dependence on the resonant prime's unit symbol
(`m_w(p)=0` on all 24 class-prime pairs, 101/101 cells). Complete closed
form: `Z(κ) = Σ_classes [certified jump] × [±1 constant] × (κ|5)^[χ5]` —
ONE character (the `disc(A1)=5` Legendre symbol) governs every phase at
every rung.

**Citation:** `frontier/B663_bifocal_anatomy/FINDINGS.md` (A2).

**Scope:** OBJECT ALONE.
**Status:** CERTIFIED (101/101 cells; independently cross-checked by
A15's period computation).

### A17. L104 CLOSED: the CP/δ-chain terminates as CONVENTION

**Statement:** `(Λ³g)·Y = Ȳ` over `K=ℚ(√-3)` has two independent exact
solutions (the wave-1 σ-matrix itself, read K-linearly, det=1; and a
structurally independent Galois-descent certificate). Behind the verdict:
the banked generic trivector type on 5-space is a SINGLE `GL(5,k)`-orbit
over any field — no arithmetic invariant exists. **Consequence: the
framework carries no forced CP-like distinction at the bare 3-form level;
the δ_PMNS chain terminates — no prediction exists.**

**Citation:** `frontier/B662_successor_campaign/WAVE2_FINDINGS.md`
(CELL F); `frontier/B662_successor_campaign/cellF/FINDINGS_CELL.md`;
`docs/OPEN_LEADS.md` (L104 row, "CLOSED… CONVENTION").

**Scope:** OBJECT ALONE (the golden double's Y-tensor).
**Status:** THEOREM (CLOSED, both directions).

### A18. The γ5′ correspondence — candidate functor

**Statement:** the ear's hearing representation IS the Γ5′-doublet 2̂′ —
exact character equality on all 9 conjugacy classes in `ℚ(ζ20)` under the
canonical `Γ5′ = SL(2,Z)/Γ(5) = SL(2,F5)` identification. H129 resolved
with mechanism: weight 5 is FORCED (`M_k(Γ(5)) ≅ Sym^{5k}(2̂)`; numerator
exponents partition the E8 exponents {1,7,11,13,17,19,23,29}; first
n≡0 mod 5 is 25 for both doublets).

**Citation:** `frontier/B662_successor_campaign/WAVE3_FINDINGS.md`
(CELL I).

**Scope:** OBJECT ALONE (the golden's hearing representation).
**Status:** THEOREM (the representation, exact) — PLACEMENT upgraded to
CANDIDATE FUNCTOR (the framework-side modular-form leg, L108, remains
OPEN).

### A19. The Jacobian reality law

**Statement:** `J = μ + 1/μ` real ⟺ amphichiral word (the classical face
of the pairing law), verified on 8 words.

**Citation:** `docs/LAW_MAP.md` (§A, "The Jacobian reality law"), citing
`frontier/B626_jacobian_reality/FINDINGS.md`.

**Scope:** GENERAL FAMILY (8 words, arbitrary block structure).
**Status:** LAW (8 words; proof + discrete-branch IDs open).

### A20. The trace-3 algebraic sieve (torsion-free selection)

**Statement:** among integer traces, only `tr=3` gives a torsion-free
hyperbolic once-punctured-torus-bundle complement — PROVED. Four further
filters (min hyperbolic volume, amphichirality, rank-2 categorifiability,
Eisenstein triangulation) independently point to 4₁ but are "documented,
not proven to uniquely select it" (NEEDS-SPECIALIST).

**Citation:** `CLAIMS.md` (P10).

**Scope:** GENERAL FAMILY (all integer traces / all once-punctured-torus
bundles).
**Status:** PROVEN (the trace-3 sieve itself); the four auxiliary filters
remain NEEDS-SPECIALIST except where sharpened below (A21).

### A21. Volume-minimum among torsion-free bundles (P10's m003 tie broken)

**Statement:** P10's volume filter "ties the sister m003" is broken by
torsion-freeness: m003 carries ℤ/5 torsion (not a positive b++-word
bundle); **among torsion-free / within b++, the figure-eight is the
unique volume minimum**, verified over all 241 b++ bundles to length 10
(next smallest: the LRR/LLR chiral pair at 2.6667). Also (same file,
independent count): among the 2587 cyclically-reduced positive L/R
necklaces to length 14, **LR is the unique minimum-trace (=3) word AND
the unique shortest word.**

**Citation:** `frontier/B197_figure_eight_volume_torsionfree/FINDINGS.md`.

**Scope:** GENERAL FAMILY (all b++ positive L/R necklaces to length 10-14).
**Status:** PROVEN/verified (exhaustive to the stated length; not a
general theorem for all lengths).

### A22. The general amphichirality criterion (word/block-pair form)

**Statement:** a once-punctured-torus bundle with monodromy
`W = R^{a1}L^{b1}...R^{ak}L^{bk}` is amphichiral ⟺ the block-pair
sequence `((a1,b1),...,(ak,bk))` is invariant under (reverse order AND
swap each pair's components) up to cyclic rotation — the exact word
criterion referenced by the W0a prereg (a proved corollary of
Goodman–Heard–Hodgson 2008's anti-palindromic criterion, restated in
block-pair form). On a SINGLE block pair `(a,b)` (as in the R^{n-2}L
metallic-slice family, block pair `(n-2,1)`) this reduces to `a=b`, i.e.
only `n=3` (golden RL). **No banked cell was found that states this
single-block corollary explicitly for the R^{n-2}L slice** — see MISSING
M1.

**Citation:** `frontier/B136_general_amphichirality/FINDINGS.md`.

**Scope:** GENERAL FAMILY (any once-punctured-torus bundle word).
**Status:** THEOREM (proved; exhaustive check to 4 blocks/exponent ≤3,
7380 cases, + SnapPy cross-check).

### A23. The stage-selection state (L91) after B664

**Statement:** to upgrade "κ=5 is the minimal bearing stage" from CHOICE
to THEOREM requires four obligations: (1) why the SU(3) modular family is
selected; (2) why 5|κ becomes equality; (3) why minimal bearing is a
theorem not an axiom; (4) the typed functorial classical→stage map.
**Obligation (4) is DISCHARGED** (B650 types + B644 group functor + the
equivariance wall). **Obligations (1)-(3) remain OPEN.** B664 contributes
SUPPORTING STRUCTURE (not discharge): "the hearing landscape's period is
the golden word's own conductor, and the golden is the family's unique
unit-determinant word — one genuine criterion (the 'five independent
criteria' and the uniqueness-of-real-minimum claims were corrected in
B664)." B670's self-selection half-law (A5) further sharpens this to "a
bounded, checkable selection statement," still not a proof.

**Citation:** `docs/OPEN_LEADS.md` (L91 row, verbatim).

**Scope:** METALLIC SLICE feed into an OBJECT-ALONE question (why κ=5).
**Status:** OPEN (partial — one of four obligations discharged).

---

## PART B — REFUTED / NOT UNIQUE (do-not-soften findings; still banked facts)

These are properties that were *claimed* as golden-uniqueness criteria
somewhere in the record and were subsequently tested and found NOT to
single out the golden object, or to single it out on weaker grounds than
claimed. Reported per the campaign's falsifier discipline.

**R1. Amphichirality is universal across the symmetric metallic tower —
NOT an m=1 selector.** For every m, `M_m² = R^mL^mR^mL^m` is symmetric,
and every symmetric `M ∈ SL(2,Z)` satisfies `S·M·S⁻¹ = M⁻¹` — so the
bundle equals its mirror for the WHOLE family. "m=1 uniquely amphichiral"
is explicitly RESOLVED to "NOT unique — ALL metallic m are amphichiral."
The systole (B92), not amphichirality, is what selects m=1.
— `speculations/S001_amphichirality_theta_zero.md` (PROVED, this round).

**R2. Arithmeticity selects {m=1, m=2} (golden AND silver), not a unique
member.** Computing the invariant trace field directly (SnapPy,
Maclachlan–Reid criterion) gives both m=1 (ℚ(√-3)) and m=2 (ℚ(i))
arithmetic; m≥3 non-arithmetic. This CORRECTS an earlier "unique m=1
arithmetic" claim that mis-applied Reid 1991 (a KNOT theorem) to BUNDLES.
— `knowledge/K009_m1_selection_criteria.md` (criterion 3, citing B125).

**R3. "det(A-I) unit ⟺ amphichiral" is FALSE as a general criterion; the
silver (RRLL) IS amphichiral despite non-unit det(A-I)=4.** SnapPy:
m136 (RRLL, the true silver, trace 6) has |Isom|=8, hence amphichiral.
"The golden is the only amphichiral metallic word" claim rested on this
invalid criterion and is REFUTED. (Consistent with R1 — under the correct
word criterion A22, ALL single-block-pair-symmetric words are
amphichiral, which includes every `R^mL^m`.)
— `frontier/B669_track_h_adjudication/FINDINGS.md`.

**R4. "The golden is the ONLY real minimum" (of the hearing landscape)
is REFUTED.** Quiet+real (|tr_odd|=1/φ AND Im=0) recurs at n≡3 or 12
mod 15 (witnesses n=12,18,27,33); the mechanism is the mod-15 phase
lattice, not amphichirality or unit-det.
— `frontier/B664_metallic_landscape/FINDINGS.md` ("The refutations").

**R5. "Five independent criteria" over-counts; only ONE genuine criterion
(prime conductor = unit det(A-I)) survives on the metallic slice** — see
A1. A second, independent property (real hearing) also survives per
B665's correction, so the honest count is TWO, not five and not one.
— `frontier/B664_metallic_landscape/FINDINGS.md`;
`frontier/B665_landscape_reconciliation/FINDINGS.md`.

**R6. The self-selection (diagonal) hypothesis is NOT a universal law.**
It fails cleanly on 6/16 rows of the cross-landscape matrix (RLRL's
distinctive minimum at κ=10 is itself off-conductor; n=11's minimum has
zero conductor alignment). See A5 for the positive half.
— `frontier/B670_anatomy_full/packet/loop2/b4_landscape/FINDINGS_CC2.md`.

**R7. The volume-tie with m003 is NOT independently resolving** — it
holds only "given torsion-free," which leans on the same filter the
trace-3 sieve already uses, so it is not an independent selection axis.
— `frontier/B197_figure_eight_volume_torsionfree/FINDINGS.md` (Honest
framing section).

**R8. Minor correction: PSL(2,5), not SL(2,5), is simple.** Chat1's
"prime conductor ⇒ simple hearing group" needed the ±I quotient.
— `frontier/B665_landscape_reconciliation/FINDINGS.md`.

---

## PART C — MISSING (expected properties without a found citation)

**M1. Amphichirality of the golden word WITHIN the R^{n-2}L metallic
slice, stated and verified as its own banked cell.** The general
word-criterion (A22, B136) implies algebraically that a single-block-pair
word `(n-2,1)` is amphichiral only when `n-2=1`, which would make golden
the unique amphichiral member OF THIS SPECIFIC SLICE — but no frontier
cell was found that states or verifies this corollary for the R^{n-2}L
family explicitly. B664/B665 only established the (weaker/different)
unit-det=prime-conductor collapse (A1), not amphichirality per se, for
this slice.
*Searched:* `grep -rn "R\^{n-2}L" --include=*.md --include=*.py` combined
with "amphichiral" (no hits); B664/B665/B666/B670 FINDINGS files read in
full — none compute amphichirality for the single-L family.

**M2. "Rank-2 categorifiability" and "Eisenstein triangulation" as
independently banked golden-uniqueness filters** (named in CLAIMS.md P10
and AUDIT_REPORT.md, legacy/handoff/handoff.md). No dedicated frontier
B-number/FINDINGS.md was found that computes or verifies either filter
independently; they remain parenthetical, NEEDS-SPECIALIST per P10's own
text.
*Searched:* `grep -rln "rank-2 categorif\|Eisenstein triangulation"
--include=*.md` (hits: CLAIMS.md, AUDIT_REPORT.md, PROGRESS_LOG.md,
papers/VALIDATION_LEDGER.md, legacy/handoff/handoff.md — all mentions,
no independent derivation file).

**M3. L105 (2O/E7 silver-hearing conjecture)** is registered but NOT
computed/proved — flagged as OPEN, not a banked property, though it
bears on golden-vs-silver uniqueness (the McKay-descent-of-the-
exceptional-series idea).
*Citation of the open status:* `docs/OPEN_LEADS.md` (L105 row: "OPEN
(B663)"); refined but not closed by `frontier/B666_leads_campaign/
WAVE1_FINDINGS.md` (CELL 1: 2O is a quotient not a subgroup of the
silver's mod-8 shadow; stage-side identification still named as residual).

**M4. Prime-conductor primality computed across the GENERAL (arbitrary
block-structure) word family** (beyond dependence on trace value alone,
and beyond the single-L metallic slice A1). No banked cell was found
that tabulates conductor primality over general multi-block R/L words
as a family-wide sweep; this is left to W0a's own enumeration per the
prereg.
*Searched:* `grep -rn "prime conductor" --include=*.md` across
`frontier/` (hits confined to B664/B665/B663/B670/B669's ATLAS.md —
all single-L-slice or object-alone framings).

---

## COUNT

- Part A (banked, standing golden-uniqueness-bearing properties): **23**
  entries (A1–A23).
  - By scope: METALLIC SLICE (R^{n-2}L) = 4 (A1, A2, A23 partial, +A5's
    slice-restriction inside A3); OBJECT ALONE = 9 (A6 partial, A8, A11,
    A12, A15, A16, A17, A18, plus A6's golden-only half); GENERAL FAMILY
    = 10 (A3, A4, A5, A7, A9, A10, A13, A14, A19, A20, A21, A22 — note
    A6/A7/A13/A14 concern the *symmetric tower* `R^mL^m`, not the
    R^{n-2}L slice — see the scope-key disambiguation above).
  - By status: THEOREM/PROVEN/CERTIFIED = 16 (A1, A2, A4 theorem-grade,
    A7, A8, A9, A10, A11, A12, A13, A15, A16, A17, A18 rep-level, A20,
    A22); LAW (exact, mechanism partial or family-partial) = 6 (A3, A5,
    A14, A19, A21 exhaustive-not-general); OPEN/partial = 1 (A23).
- Part B (refuted / not-unique, do-not-soften findings): **8** entries
  (R1–R8).
- Part C (missing — searched, not found): **4** entries (M1–M4).

**Total banked properties inventoried: 23 standing + 8 refuted = 31
banked findings bearing on golden uniqueness, plus 4 documented gaps.**
