# S2a — INTERNALIZATION SWEEP: law-creating arc bodies, band B1–B400

**Seat:** fresh-physics internalization reader. **Date:** 2026-09-01.
**Product:** digest + flags only. I judge nothing dead or proved; the evaluating seat adjudicates.

## Coverage modulus (exact; no silent truncation)

**Witness identification.** `docs/LAW_MAP.md` (370 lines) and `docs/THEOREM_LEDGER.md` (332 lines) were
**exhaustively grepped** for every `B<n>` reference with n ≤ 400, so no band arc cited anywhere in either
file was missed. Row context was then read for every hit: LAW_MAP lines 1–96 in full, plus lines 106–109,
118, 134, 141–142, 150, 165, 174, 236, 272, 281, 322–346 in full. **LAW_MAP lines not read:** 97–105,
110–133, 135–140, 143–149, 151–164, 166–235, 237–271, 273–321, 347–370 — these rows cite no B1–B400 arc
(per the exhaustive grep) and were skipped. THEOREM_LEDGER: lines 40–90 read in full (all six band hits
live there: C5/C6 B282/B285, C8 B288, C12 B48/B54/B64); rest skipped after the exhaustive grep showed no
other band hits. `docs/CAMPAIGN_STATUS.md` lines 1–60 read (the B1229–B1232 live entries).

**Arc bodies.** All **37** identified witness arcs' `FINDINGS.md` were read **IN FULL** (each file cat'd
end to end; sizes 31–111 lines): B48, B54, B64, B120, B136, B161, B196, B204, B206, B210, B218, B224,
B237, B238, B247, B248, B249, B250, B253, B259, B261, B266, B282, B285, B286, B288, B293, B294, B298,
B299, B300, B303, B307, B309, B317, B340, B399. **No cut was needed** — the whole band list was read.
Companion files (PROOF.md, NOVELTY.md, probe scripts, tests) were NOT read; where a FINDINGS delegates a
proof to such a file I say so in the digest.

**Excluded as non-witnesses (declared):** grep hits `B1`/`B3` at LAW_MAP:118 are cc2 **anatomy cell
labels** inside the B670 F4-skeleton row, not arcs; `B12` hits (lines 174, 346) are the string "MB12"
(the vacuity rubric); `B14` at line 336 is a statement-support citation inside the B1003 axiom-price row
("M² = RL, the golden matrix squared (B14)"), not a witness of any THEOREM/LAW row. Arc dirs B1/B3/B14
exist but were not read.

**Witness-position caveat.** A few band arcs are cited inside a row's *statement* text rather than its
witness column (B196/B317 in the B944 inventory row; B218/B224/B259 in the B980 withdrawal row;
B298/B299 in B987; B300 in B1000; B266 in B993/B727; B307 in B706/B713). I digest them all, marking the
citation role, since the §F-style rows have no separate witness column.

---

## Digests (ordered by arc number)

**B48** (`frontier/B48_sl3_metallic_trace_maps`) — witness of THEOREM_LEDGER **C12** (the chord).
Claims the SL(3) Fibonacci trace lift extends to the whole metallic substitution family on the 8
standard SL(3,ℂ) trace generators, with commutator-trace-pair preservation and algebraic entropy
log((m+√(m²+4))/2). Proof shape: certificate checks via `probe.py` (recurrence sanity, exact SL(3,ℤ)
traces, Jacobian block factorizations) — computed, but the integer fixed-line splitting is
"certificate-backed over an audit rectangle … not yet an independently reviewed human proof." Verdict
line is **NEEDS_VALIDATION**, and the header says "Logged observation, not a claim." Dependencies: B27
(the m=1 lift). FLAG: a self-graded NEEDS_VALIDATION arc sits as witness under a ledger row labeled
THEOREM (C12); C12 does add "recomputed 2026-07-21" and its own locks, so the theorem grade may rest on
the recompute rather than on B48's body — the evaluating seat should confirm which computation carries
the grade.

**B54** (`B54_general_c_exchange_structure`) — witness of **C12**. Claims the exchange
block-diagonalization of the metallic SL(3) fixed-line Jacobian holds for the entire fixed line (all c),
not just c=3, with the c=1 twin polynomials (Eisenstein Φ₆ disc −3 in the symmetric sector, golden
char(M) disc 5 in the antisymmetric — the −3/5 pair of the gluing equation) and the m=1 cyclotomic sweep.
Proof shape: computed symbolically, but the "all c" commutation is verified for **m = 1, 2, 3 only**,
with a structural reason (P-equivariance) argued; B64 later supplies the full symbolic-m proof. Verdict
PRODUCES-PROOF-MODULE. Dependencies: B51 (c=3 case). No red flag beyond the m ≤ 3 scope, which B64
discharges.

**B64** (`B64_parity_mechanism`) — the strongest of the C12 trio. Claims the k(α) sector-assignment law:
even-|k| char(Mᵏ) lands in the P-symmetric sector, odd-|k| in the antisymmetric, mechanism = depth-n
Cayley–Hamilton + P=contragredient (m→−m) + Dickson parity. Proof shape: **PROVEN (symbolic)** in full
symbolic-m form for SL(3); SL(4) assignment verified factor-by-factor; SL(5) row of the tower table is
explicitly "22 numeric (B61) + 2 structural (B62)". Dependencies: B54 (the commutation), B63 (SL(4)
factorization), B58 (the open Λ²V core). FLAG: C12's phrase "sector assignment proven across the tower"
outruns B64's own tower table, where n=5 is numeric+structural, not symbolic — a load-bearing grade
above the witness's stated strength (mitigated by the ledger's "recomputed 2026-07-21" and the
B745 SL(3) anchor lock, which the evaluating seat should check covers the n=5 clause).

**B120** (`B120_tower_determination`) — sole witness of the LAW_MAP **tower height-count closed form**
row (line 75). Claims the (n²−1)-dim trivial-point tower is a function of (n; trace, det) only, with the
corrected height-count closed form (count(n,0)=n−1; 2(n−2) for h∈{1,2}; 2(n−h) for 3≤h≤n−1; 2 at h=n)
and the corrected doubling deficit (n−4)(n+1)/2. Proof shape: computed, verify-don't-trust — it
**corrects three wrong formulas in the incoming handoff**; sum identity verified n=2..8, doubling
n=4..10; the m-universality "why" is a plethysm argument proved only at n=3,4 (B103). Dependencies:
B103/B117/B95/B116. LAW_MAP correctly withholds THEOREM ("the arc states it without a proof-strength
tag"). FLAG (minor): LAW_MAP says "exact on every computed instance n = 2…13" while the arc's FINDINGS
records verification to n=8 (heights) — the n≤13 extension presumably lives in the 2026-07-29 harvest
lock (`tests/test_b534_b533_b120_harvest.py`), not in the arc body; worth one look.

**B136** (`B136_general_amphichirality`) — witness in the B945 row (time-reversal/chirality
independence). Claims the amphichirality criterion for ALL once-punctured-torus bundles: amphichiral ⟺
block-pair sequence invariant under (reverse order + swap components) up to rotation; metallic case
reduces to B134's cyclic palindrome. Proof shape: proved as a corollary of **Goodman–Heard–Hodgson 2008**
(cited mechanism), with an exhaustive lemma check (7380 cases) and SnapPy agreement on metallic and
non-metallic words. The arc is explicit that novelty is a restatement of a published criterion. Clean;
no flag.

**B161** (`B161_cancellation_locus_stratification`) — witness of κ-unification face 1 (existence, B309
row) via "B161–163". Claims cancellation κ=2 is non-generic (codim-1 exact; κ-elimination ideal empty at
m=2,4, exact) and trivial-when-attained (full AC band at λ=0), while κ>2 is typical and Cantor-fractured;
explicitly **refutes** the stronger "forced/empty" reading (κ=2 is attained, B130). Proof shape: mixed —
exact Gröbner/symbolic for the stratification, numerics for the fracture, Damanik–Gorodetski cited for
the horseshoe. Dependencies: B130, B156, P008. Honest about tiers; no flag.

**B196** (`B196_entropy_conformal_dimension`) — cited in the B944 inventory row for "Δ = −(ln λ_m/π)²
exact". Claims the metallic object, under the Gamayun–Iorgov–Lisovyy PVI ↔ c=1 dictionary, is a c=1
four-twist-field conformal block whose one datum is Δ = −(h/2π)², h the topological entropy. Proof
shape: the bridge identities exact, the value verified m=1..4 to 1e-30; **the GIL dictionary itself is
cited**, and the precise PVI channel placement is flagged NEEDS-SPECIALIST in the arc. The LAW_MAP
citation banks only the exact identity, matching the arc's own fence. No flag beyond the standing
NEEDS-SPECIALIST channel question.

**B204** (`B204_metallic_wrt_period`) — witness of κ-unification face 4 and of the melody-theorem note
("the same period B204 PROVED at SU(2)", LAW_MAP line 93). Claims the WRT level-period law
P = lcm(a,b)(4+ab)/gcd(4+ab,4) for all R^aL^b torus bundles (metallic diagonal P(m)=m(m²+4)/gcd(m²+4,4);
m=1 gives period 5), with reality iff a=b. Proof shape: predict-then-confirm on held-out cells, then
**PROVED** via Landsberg–Schaar/2D Gauss reciprocity with the cross-period lemma closed exactly (full
argument delegated to `PROOF.md`, not read here). Two important self-corrections stand in the body:
(i) prior-art — the framework is **Jeffrey 1992**; "Do not claim novelty"; (ii) framing — the invariant
is the **closed Sol mapping torus**, not the cusped bundle. Both honest; the downstream rows use only
the period-5 fact. No flag.

**B206** (`B206_golden_spin_cover_e8`) — witness of the congruence-shadow theorem row (line 142).
Claims the golden monodromy's mod-5 shadow is SL(2,𝔽₅)=2I=McKay-E₈, with the classical/quantum divide
= A₅/2I, verified (surjection order 120, class counts, center). Proof shape: computed (BFS closure) plus
standard identifications. Carries its own same-day **re-audit correction**: golden is NOT unique — the
ℚ(√5) field recurs for the whole odd-Lucas family and the 2I shadow for every m ≡ ±1 mod 5; the honest
statement is "golden is minimal/fundamental, not unique". Also notes the single element RL generates
only a cyclic order-10 piece (consistent with the hearing-group rows). Novelty explicitly UNCHECKED.
No live contradiction; the later B997 uniqueness row is at each word's own conductor, a different
statement, and B1002 reconciles the two "conductor" senses.

**B210** (`B210_dual_mckay_hyperbolic`) — witness of the two-ended-theorem row (line 141, "B210/L37")
and the congruence-shadow row. Claims golden carries BOTH exceptional McKay-congruence groups — E₈ from
the monodromy field ℚ(√5), E₆ from the newly computed hyperbolic trace field ℚ(√−3) — with E₇ excluded
(|2O|=48 no SL(2,p) order), and resolves-negative that the WRT image is 2I (it is order 2880, level 20).
Proof shape: computed (SnapPy/Sage trace fields; mod-3 surjection onto 2T explicitly verified after
correcting a 6th-root slip); carries the **B212 correction** on the silver mod-2 side inline. Arnold-
trinity framing flagged "likely known — do not claim". Dependencies: B206, B207, B212. No flag; the
mod-3 step is verified, not asserted.

**B218** (`B218_metallic_anyon_selection`) — cited in κ-unification face 4 and in the **B980
withdrawal** row ("k=3 is the anyon level of the Jones thread — B218 unitary-anyon index d=2cos(π/5)").
Claims the Jones-index selection: λ_m < 2 (quantized anyon dimension) ⟺ m=1, λ₁ = 2cos(π/5) = φ exactly
— golden is the unique anyon-realizable metallic mean. Proof shape: the selection is **exact and
elementary**; but the chain-level CFT c=7/10 is **CITED (Feiguin et al. 2007), not reproduced** — the
arc says so plainly ("my own in-sandbox ED did NOT reproduce c=7/10 … buggy … cited, not banked").
FLAG (mild, already self-declared): the c=7/10 leg is cited-only; anything downstream leaning on the
chain CFT (B224's premise) inherits that; B224 states the k=3 case was later reproduced in-sandbox
(B220/B222) — confirm those arcs if that leg becomes load-bearing.

**B224** (`B224_golden_unique_susy_metallic`) — cited in the B980 row ("B224 M(4,5)"). Claims golden is
the UNIQUE metallic mean whose anyon chain is superconformal: only M(4,5) among unitary minimal models
is N=1 superconformal, and k=3=m²+2 at m=1. Proof shape: the uniqueness of M(4,5) and the central-charge
arithmetic are **exact** (pytest-locked); the chain→M(k+1,k+2) flow is **cited** (Feiguin–Trebst–
Ludwig) with the k=3 case reproduced in-sandbox per B220/B222; the m ↔ k=m²+2 identification is labeled
a "motivated correspondence", with the honest note that superconformal-uniqueness does not depend on it.
No flag beyond the cited flow leg.

**B237** (`B237_silver_2O_l48`) — witness of the **B1019** one-grammar-one-door row. Claims (GAP
GQuotients, definitive): silver carries NO 2O quotient (the ℚ(√2) match is field-only); golden → 2T
only; bronze → 2T+2I; and 2O is absent from all three — refuting chat1's "all metallic bundles carry 2T
and 2I" (the matrix-mod-p heuristic ≠ π₁ surjection). Proof shape: computed census (GAP on SnapPy
presentations). Also separates geometric-holonomy McKay (2T for golden) from homological-monodromy
McKay (2I) — the distinction the later B699 clarification row leans on. Clean verify-don't-trust catch;
no flag.

**B238** (`B238_su32_levelrank`) — witness in the **B1011 McKay tensor law** row's citation chain.
Claims Z(4₁; SU(2)₃) = Z(4₁; SU(3)₂) = −1/φ exactly, and that this is figure-eight-specific (silver,
bronze, RRL all differ) — a shared-κ=5 level-rank coincidence, not a general equality, with
c(SU(2)₃)+c(SU(3)₂)=5=c(SU(6)₁). Proof shape: computed (numpy; S,T gate-verified against the modular
relations — a Casimir normalization bug was caught by the gate before results were read). No flag.

**B247** (`B247_v1_holonomy_adjudication`) — inside the B247–B261 witness range of the two-ended
theorem row. An adjudication arc: **refutes** both chats' "C_{E₆}(SU(2)_long) = SU(3)×SU(2)×U(1)²"
(Sage branchings: the long centralizer is SU(6), the short is SU(3)×SU(2) with no hypercharge) and
proves the geometric-holonomy-breaks-E₆ bridge false (SL(2,ℂ) has no nontrivial hom into compact E₆ at
all; the E₆-selecting connection (ℚ(√−3)) and the SU(2) arc (ℚ(√5), tr(ab)=φ) are different points with
different fields). Proof shape: computed (Sage branchings, SnapPy ground truth), including a caught
wrong-Riley-root error in chat2's matrices. This is the negative that scopes every later E₆-physics
row; the two-ended row's THEOREM tag is for the ends' existence, which this arc supports. No flag.

**B248** (`B248_e6_e8_geometric_transition`) — witness range member; also the load-bearing citation of
the **B981** row ("B248 proves a cone-angle transition through all three signs"). Claims the dual McKay
E₆+E₈ is realized as the hyperbolic↔Euclidean↔spherical cone-manifold transition, with the spherical
end the ℤ/2 orbifold whose double cover is L(5,2) (det(4₁)=5). Proof shape: computed sweep of the
character-variety curve plus classical citations (Thurston, HLM). Status header is "banked
observation"; B981 upgrades the language to "proves" — the underlying facts (the three rows of the
table) are each computed, so the gap is rhetorical rather than substantive. No flag beyond that
wording delta.

**B249** (`B249_niven_trinity`) — witness range member; cited by B981 ("Niven forces clean quadratics
only at the two ends"). Claims E₆+E₈-and-not-E₇ is ONE arithmetic fact: Niven's theorem makes
2cos(π/n) rational only for n ∈ {1,2,3,∞}, so only the cusp and the ℤ/2 orbifold give clean quadratic
fields; E₇'s ℚ(√2) would need x=√2, irrational. Proof shape: computed table + Niven (classical, cited).
Also the object-specificity note: only m=1 is a knot complement, so the geometric realization is
figure-eight-specific. Novelty flagged APPEARS-NOVEL/specialist-gated in the arc. No flag.

**B250** (`B250_volume_profile`) — witness range member; B981 quotes its headline ("Vol=6Λ(π/3),
CS=0 vs π²/5"). Claims the two end-volumes carry the two arithmetic invariants: hyperbolic
Vol=6Λ(π/3)=2.0299 with CS=0, spherical Vol=π²/5 with CS ∈ (1/5)ℤ — det(4₁)=5 is literally the
spherical volume denominator. Proof shape: computed (mpmath; hyperbolic anchor cross-checked vs
SnapPy); lens-space CS cited (Kirk–Klassen). No flag; note B981 itself records that B259's use of this
row quoted the first clause while the second refuted it — the arc body is fine, the misuse was
upstream.

**B253** (`B253_chirality_capability`) — witness range member; B981 cites it ("E₆ is the only
chirality-capable end"). Claims Part A (Sage-verified): complex-rep capability E₆ yes / E₈ no / E₇ no;
adopts chat-2's valid correction of B252 ("cannot source asymmetry" → "no explicit CP-odd datum;
asymmetry needs external SSB"); and deflates Part B — the "decidable reduction" is NOT object-decidable
(3d not 4d; E₆ a McKay label; gauging τ a choice; CS=0 leaves both branches open). Proof shape: Part A
computed, Part B argued-and-fenced. Careful adjudication; no flag.

**B259** (`B259_gravity_brick_wall_map`) — cited in the **B980** row as the *withdrawn* chain's home
("B259 wall #5"). Claims the gravity brick: Mostow metric solves 3d vacuum Einstein with Λ=−1 (sympy-
verified), action = complex volume, "level k=3 via Smolin/Kodama k=6π/(GΛ) → GΛ=2π" as ingredient 3,
and the five-wall map with wall #5 carrying the "122 orders from observation" quantitative gap. Proof
shape: stone 1 computed; ingredient 3 is arithmetic on top of a **cited physics identification**.
**RED FLAG (the band's sharpest):** the live board's B980 row WITHDRAWS precisely this chain — Smolin's
k is 3+1-dimensional (GΛ dimensionless in d=4 only; B259 dropped the ħ), k=3 has no gravitational
derivation (it is the anyon level), and "the 122-order shortfall was never the object's" — yet
**B259's FINDINGS carries no retraction or correction note**: ingredient 3 and wall #5's 122-order
framing still read as live in the arc body. Anything internalizing B259 from its own file alone would
resurrect a withdrawn claim.

**B261** (`B261_golden_root_aj`) — witness range member; B981 cites it ("one AJ recursion carries both
ends"). Claims the two ends are two regimes of one AJ operator: Kashaev limit exponential (Vol/E₆),
golden root q=ζ₅ periodic with antiperiod 5 ({1,−2,−2,1,0 | −1,2,2,−1,0}); classically the golden
meridian forces L+1/L = −φ³ ∈ ℚ(√5). Proof shape: computed (mpmath/sympy), leaning on the **proved**
AJ conjecture for 4₁ (Garoufalidis, cited). No flag.

**B266** (`B266_arithmetic_selects_e6`) — the "atom" arc, cited in the κ-unification row, the B727
self-audit row, and the **B993** cornerstone row (which reproduces its 48/24=2 surjection count).
Claims the selection chain: trace field ℚ(√−3) → unique ramified prime 3 → π₁ ↠ SL(2,𝔽₃)=2T →
McKay-E₆, every link verified or classical. Proof shape: computed + cited classics, with TWO
corrections banked in the body: (i) the q∈{3,5} justification had skipped q=4 (SL(2,𝔽₄)≅A₅ — the
decisive criterion is the quaternionic 2-dim irrep); (ii) the **R6 addendum: π₁(4₁) does NOT surject
onto A₅ or 2I** (Stuebner 2025, verified in GAP) — so the two-ended E₆/E₈ structure is correct **only
at the FIELD level**; the ends are group-asymmetric. Both corrections are consistent with the later
B699 row's clarification (the 2I is the hearing rep, not the raw holonomy). The evaluating seat should
watch for any surviving row that reads the E₈ end as a group surjection of π₁ — none found in the rows
read here. Novelty: PARTIALLY-KNOWN (Long–Reid, CRS; the selection overlay APPEARS-NOVEL,
NEEDS-SPECIALIST).

**B282** (`B282_e6_is_arithmetic_not_geometric`) — THEOREM_LEDGER **C6** co-witness (with B285) and the
genericity-collapse meta-arc. Claims the E₆ character-variety richness is generic to all hyperbolic
knots (Menal-Ferrer–Porti); the only object-specific content is the arithmetic 2T atom (Reid: unique
arithmetic knot). Proof shape: computed census (SnapPy+GAP; 2T surjections: 4₁ and m003 = 2, four
non-arithmetic knots = 0) + cited MFP genericity. **RED FLAG (internal spin):** the body's headline —
"the 2T surjection … is present *only* for the arithmetic cusped manifolds" — was falsified at larger
sample by B727 (4/13 knots surject, including non-arithmetic 7₂, 7₃, 8₁), and the appended 2026-07-20
corroboration note *records* this but frames it as "STRENGTHENED". The narrow conclusion (only the
arithmetic atom is object-specific) genuinely survives and is strengthened; the specific "only
arithmetic manifolds surject" sentence in the body is refuted and still reads live above the note. A
reader stopping before the appendix gets a false universal.

**B285** (`B285_commutator_phase`) — THEOREM_LEDGER **C6** witness (exact Riley rep, u²+u+1=0; lock
`test_b285_commutator_phase.py`). Claims κ = tr[a,b] = u²+2 = √3·e^{∓iπ/6}: magnitude √3 and |arg| =
π/6 exact and forced by ℚ(√−3); the sign flips between conjugate Riley roots — magnitude forced, sign
external (the object is CP-symmetric, B252). Proof shape: computed exactly; the physics
("CP-violating phase") explicitly firewalled, and chat-2's baryon-number estimate retracted in the
body. Clean; no flag. Feeds B303/B340 consistently.

**B286** (`B286_the_seam`) — witness of κ-unification face 2. Claims the ingredients (selection set,
chirality, CP sign, scale, clock) live at the cusp/seam: exactly 10 exceptional fillings (Thurston,
cited), every generic filling chiral, CS(p,−q)=−CS(p,q), core length ≈ 2π/n, the peripheral pairing as
clock — Curie's principle scoped to closed systems and P011 corrected. Proof shape: computed (SnapPy
table) + argued reframe; the "cusp = the nothing" reading tagged as the P000 interpretive frame. No
flag; the fence is explicit that no SM value is derived.

**B288** (`B288_arithmetic_filling_census`) — THEOREM_LEDGER **C8** co-witness. Claims no closed
hyperbolic filling of m004 re-sees √−3 (or is arithmetic): E₆ is an open-object property destroyed by
closing. Proof shape: computed census, two methods, originally **54/78** fillings with 24 skipped —
and the body carries the **B740 completion note**: the full 78/78 grid was recomputed, verdict stands
"fully earned". C8 cites B288/B740 together, matching. A model of honest coverage-modulus reporting;
no flag.

**B293** (`B293_peripheral_clock`) — witness of κ-unification face 4 and B294's clock row. Claims the
clock is the peripheral symplectic pairing, two ways: Goldman bracket with κ the Casimir (leaves
{κ=const}), and the Neumann–Zagier frame (A·Bᵀ symmetric, unit mixed pairing); a filling slope = a
Lagrangian/polarization. Proof shape: computed, BUT the arc's own red-team caveats matter: (a) the
Casimir check follows from the generic Nambu construction — the identification with the *Goldman*
bracket is "imported … not derived here"; (b) A·Bᵀ symmetric is the generic NZ theorem, not
figure-eight-specific; (c) k_um=−1 is frame-dependent; "Goldman = NZ" is "asserted … not an exhibited
isomorphism". FLAG: this is exactly the **asserted-identification** species the live board's B1231
identification-discipline entry names as the programme's dominant error mode; B293 self-declares it,
but any row leaning on "Goldman = NZ" as computed should be re-typed under the new discipline.

**B294** (`B294_selection_verdict`) — witness of κ-unification face 2. A consolidation-only synthesis
of B287–B293/B295: selective for the object's own structure (the forced Sol fiber closing (0,1)),
axis-stratified, catalogue for SM values (E₆ lost, CP sign external, scale gapped, chiral datum
absent, trajectory gated). Proof shape: consolidation of verified sub-results; the table's rows each
point at a computed arc. Note its "scale ladder" row still carries "the 122-order gap" phrasing
(B290-era) — post-B980 that number is withdrawn as a statement about the object; the row here is
descriptive of B290's math, but the phrase is of the withdrawn family. Minor flag, same family as
B259/B300.

**B298** (`B298_generation_obstruction`) — cited in the **B987** row (doublet-triplet splitting
"EXTERNAL, needing a colour choice — B298/B299"). Claims the figure-eight does not force three
generations: ℚ(√−3) is degree 2, multiplicities are 1 or 2; seven independent routes all fail for the
same reason; plus the "cubic-carrier conjecture" (3 generations need a degree-3 trace field — go find
that knot). Proof shape: computed (field arithmetic + SnapPy 3-fold cover) + the tabled routes. FLAG
(superseded content reading live): B307 subsequently proved the sharpened version — a **cyclic**-cubic
trace field is impossible for ANY hyperbolic knot, and even generic cubics split 1+2 — which kills the
cubic-carrier *direction* as stated ("the carrier is a different, degree-3 object"); B298's FINDINGS
carries no update note, so its closing conjecture reads live though its successor closed it.

**B299** (`B299_trinification_triality`) — B987-row co-citation. Claims (θ,φ) is a genuine ℤ₃×ℤ₃ of
E₆ acting freely on the 27 (9 orbits of 3 — the trinification triality), and **refutes** the handoff's
"H-label = φ-eigenvalue" derivation (free action ⇒ no per-weight grading; the color choice is an
external Wilson-line input). Proof shape: computed (sympy, self-contained matrices; a non-Bourbaki
Cartan re-derived). Independently confirms B282's genericity collapse from outside. No flag.

**B300** (`B300_cross_chat_sm_attempt`) — witness of the **B1000** input-count row (its "~8 inputs"
sweep is one of the three counts B1000 reconciles). Claims Column B collapses to two walls: (A) no
Lagrangian/coupling-strength; (B) the degree-3 carrier (closed negative via B298). Proof shape:
consolidation + verified arithmetic (the E₆+A₂→E₈ det glue; the ℓ_P rod). FLAG (withdrawn-family):
the "Scale = one rod" block is *"conditional on G·Λ = 6π/k, the Alexander relation"* and quotes
"k~10¹²² … the clock having run" — the identification B980 later withdrew (k=3 is the anyon level;
GΛ dimensionless only in d=4). The arc marked it conditional, which is better than B259's bare use,
but no post-B980 note exists in the body.

**B303** (`B303_clock_is_the_cp_sign`) — first witness of the **CP RATIO LAW** row ("CP sign = sign of
Chern–Simons, CS = 0 ⟺ amphichiral"). Claims the CP sign IS the CS sign: cusped CS=0, every closing
has definite sign, mirror flips it, sign constant along a fixed-orientation history; the "clock
gauge-fixes the CP sign" forcing is reduced to two named [LEAP]s (Alexander CS-time; the forced
arrow). Proof shape: computed CS ladder (SnapPy/sage) for the sign law — the part the LAW_MAP row
banks; the reduction is conditional-on-firewalled-leaps and says so. FLAG (mild): the two leaps live in
the same Smolin/Alexander clock family whose GΛ arm B980 withdrew; the *banked* sign law is untouched,
but the arc's "reduced to two named inputs" framing should be re-read against B980 by the evaluating
seat.

**B307** (`B307_totally_real_obstruction`) — cited in the B706 rung-2 wall ("the object provably lacks
the SM discrete structure — B307/B604") and the B713 row. Claims the theorem: **no hyperbolic knot has
a cyclic-cubic trace field** (C₃ ⇒ Galois ⇒ totally real; hyperbolic invariant trace fields always
have a complex place) — three symmetric generations are arithmetically impossible for any single
hyperbolic knot; census-confirmed (500 manifolds: 32 cubic fields, all S₃, zero C₃); also refutes the
naive "degree 3 suffices" via 5₂. Proof shape: a genuine two-line proof from cited standard facts
(Maclachlan–Reid) + computed census. Clean; the strongest small theorem in the band. No flag.

**B309** (`B309_kappa_unification`) — the restored **κ-unification** row's witness (LAW_MAP line 134;
the row records it was ABSENT from the map until B1010 restored it 2026-08-10, identities re-verified
at restoration). Claims one commutator trace κ=tr[a,b] with four banked faces (existence P008/B161–163;
geometry B286/B294; matter B285/B305/B306; quantum B204/B218–230/B293), κ−2=ω², |κ−2|=1, arg=∓π/6 —
a consolidation, explicitly "not a discovery". Proof shape: verified identities + attribution of each
face to a computed arc; the E₆-uniqueness-among-exceptionals characterization labeled generic/textbook.
Dependencies are exactly the band arcs above; its weakest imported leg is B293's asserted Goldman=NZ
(face 4) and B218's cited CFT. No new flag beyond those inherited.

**B317** (`B317_painleve_transcendental`) — cited in the B944 inventory row ("the object is a
transcendental positive-entropy Painlevé-VI solution"). Claims the metallic elements are hyperbolic on
the Fricke cubic ⇒ infinite orbits ⇒ NOT in Lisovyy–Tykhyy's algebraic list ⇒ transcendental, with
entropy h=2log λ_m exact. Proof shape: exact eigenvalue arithmetic + the **cited** Lisovyy–Tykhyy
finite-orbit ⇔ algebraic classification (the load-bearing dichotomy is literature, applied — not
re-proved). Also corrects P010's stale "unrun". Fine; the citation-shaped step is standard and named.

**B340** (`B340_cp_phase_along_flow`) — second witness of the CP RATIO LAW row ("phase arg κ extremal
at π/6, decreasing as 3.8·CS²"). Claims arg κ is extremal (π/6) at the amphichiral cusp and decreases
second-order in CS along (1,n) fillings, with the sign invisible at leading order (deviation even in
CS) — sign stays in the orientation. Proof shape: computed (SnapPy holonomy instrument built for the
purpose); the 3.8·CS² is a fitted scaling over the computed points, not a derived coefficient — the
LAW_MAP row quotes it as "3.8·CS²" without a derivation claim. No flag beyond noting the coefficient
is empirical.

**B399** (`B399_wall_scale`) — witness of the **e₃ CUBIC THEOREM** row (line 72, with B771). Claims
(A1–A3 + phase 1a): the 1215-rung singles resolve to 12 cells at exactly 1/12 plus a ℤ/3 triple with
minimal polynomial t³ − t/48 − e₃, e₁=0 EXACT, e₂=−1/48 EXACT (the seam coefficient's fourth
appearance), sum rule Σ=1 proven at depth 5; W-A closes ("the tower is a resolution generator, not a
scale generator"). Proof shape: computed (multi-prime CRT reconstructions, preregistered branches,
locks in `tests/test_b399_wall.py`). FLAG (split provenance / stale-reading risk): **B399's FINDINGS
ends with e₃ PENDING** ("needs more primes … sentinel adjudication OPEN pending e₃") and was never
updated; the exact closure e₃ = cos(2π/9)/864 that makes the LAW_MAP row a THEOREM lives in
**B771/OI-031** (RESOLVED-A → CLOSED), not in this arc. A reader internalizing B399 alone would grade
the cubic open; the row's grade is only as good as B771, which this sweep did not read (out of band).

---

## Red flags (consolidated for the evaluating seat)

1. **B259 (strong):** the Smolin `k=6π/(GΛ)` → `GΛ=2π` ingredient and the wall-#5 "122 orders"
   framing were withdrawn by the live board's B980 row on two independent grounds, but B259's FINDINGS
   carries **no retraction note** — the withdrawn chain still reads live in the arc body.
2. **B282 (moderate):** the body's universal "2T surjection present ONLY for arithmetic manifolds" was
   refuted at larger sample (B727: non-arithmetic 7₂/7₃/8₁ surject); the appended note records the
   refutation but labels the arc "STRENGTHENED", and the false universal still reads live above it.
3. **B300 / B294 / B303 (mild, same family as #1):** the `G·Λ=6π/k` conditional rod, the "122-order
   gap" phrase, and B303's Alexander-clock leaps are all of the family B980 withdrew; each arc marked
   its use conditional/firewalled, but none carries a post-B980 note.
4. **B399 (moderate):** the LAW_MAP e₃-cubic THEOREM's closing computation is not in the witness arc —
   B399's own record still says e₃ PENDING; the closure is B771's (unread here, out of band).
5. **C12 vs B48/B64 (moderate):** the ledger THEOREM grade sits over a witness trio whose own grades
   are NEEDS_VALIDATION (B48) and, for the SL(5) rung, numeric+structural (B64's tower table); the
   "recomputed 2026-07-21" and the B745/B64-family locks presumably carry the grade — verify they
   cover the "across the tower" clause.
6. **B293 (mild but topical):** "Goldman = NZ" is a self-declared *asserted identification* — exactly
   the error species the live board's B1231 identification-discipline entry now instruments; face 4 of
   the κ-unification row inherits it.
7. **B218 (mild, self-declared):** the chain-level c=7/10 CFT is cited-only (in-sandbox ED failed to
   reproduce); B224's premise leans on B220/B222's later reproduction, not read in this sweep.
8. **B298 (mild):** the cubic-carrier conjecture ("find a degree-3 knot") reads live though B307's
   totally-real theorem closed that direction for all hyperbolic knots; no update note in B298.
9. **B120 (minor):** LAW_MAP claims instances n=2…13; the arc body records n≤8 (heights) / n≤10
   (doubling) — the extension presumably lives in the 2026-07-29 harvest lock, not the arc.
