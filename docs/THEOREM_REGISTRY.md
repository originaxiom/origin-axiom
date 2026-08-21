# THE THEOREM REGISTRY — every theorem and law, mapped for the novelty relaunch

**Created 2026-07-08 (the owner's directive: document everything before the literature
campaign relaunches). Schema per entry: statement / bank / reproducer / lit-status /
search terms for the novelty sweep. Lit-status values: KNOWN (cited, never claimed) ·
DERIVABLE (classical mechanics, banked as exhibit) · NEEDS-LIT (novelty unresolved —
the relaunch targets) · APPEARS-NOVEL (survived a prior sweep). Standing rule: every
future bank that creates a theorem or law adds its line here IN THE SAME PR.**

## Tier 1 — the paper-leading theorems (NEEDS-LIT, highest priority for the relaunch)

| # | statement | bank | reproducer | lit-status / search terms |
|---|---|---|---|---|
| T-UNIQ | tr[A_m,A_n] = 2 − (mn(n−m))²; parabolic ⟺ (m,n) = (1,2). **MECHANISM (P4 panel, verified): for ANY symmetric pair in SL(2), tr[A,B] = 2 − (M₁₂−M₂₁)² with M = AB (since BA = (AB)ᵀ) — the square is the transpose/elliptic involution; the family content is M₁₂−M₂₁ = mn(n−m). Two-line proof; significance weight moves to the Cohn identification** | B471 (+panel) | `chain_verify.py` | **GATED (P4 rounds 1–2)**: PARTIALLY-KNOWN — mechanism classical (Sarnak reciprocal geodesics; Gehring–Martin δ=0 slice; Goldman/Fricke); (1,2) instance VERBATIM in Reutenauer 2009/2019 (the Markoff morphism); books anchor to fixed trace −2, no two-parameter family. OURS: coordinate lemma, metallic parametrization, uniqueness scan (vs Schmutz Schaller 2022, Nielsen) |
| T-MIRROR | **CORRECTED (P4 panel)**: the palindromic-alphabet argument is TWO-BLOCK only (counterexample A₁A₂A₃ = RLRRLLRRRLLL); chain rungs word-mirror verified ≤ 8 (standard-word lemma = the open proof route); word criterion sufficient-not-necessary (the (ℤ/12)² pair); the word-mirror ⟹ amphichiral bridge lemma must be stated | B470 + correction | `hierarchy_verify.py` | **GATED**: PARTIALLY-KNOWN — full criterion proved for closed Sol bundles (Tian–Wang–Wang arXiv:2406.13241, transplants); rev·swap ⟺ conj-to-inverse = Baake–Roberts 1997; symmetry group = GL(2,ℤ)-normalizer (Floyd–Hatcher 1982). OURS: punctured word-form, witnesses, tables |
| T-GIES-FAM | X_m = [[m,1],[1,0]], X_m² = A_m, det −1 ∀m: every metallic bundle orientation-double-covers a non-orientable bundle (m=1: Gieseking; SnapPy gate m000 ✓) | B469 BR2 | `br1_br2.py` | **NEEDS-LIT**: "non-orientable punctured torus bundle orientation double cover", Gieseking family literature |
| T-COLLIDE | 4₁(5,1) ≅ −5₂(5,1) = m003(−2,3); in-window census: 3 collision children incl. the TRIPLE 4₁(1,2) = 5₂(−1,1) = 6₁(1,1) (ℤHS); merge orientation classified | B467 (+census) | `f3_wall.py`, `census.py` | **NEEDS-LIT**: Brakes 1980, Livingston, "knots with common Dehn surgery", "cosmetic surgery pairs twist knots", Whitehead-link symmetry |
| T-BB | the root criterion (tr − 2 = t² AND t \| B − I) — **CORRECTED SCOPE (P4 panel, verified): breathable TRACES = metallic traces t²+2; A_m = the PRINCIPAL breather; family = locus ⟺ h⁺(m²+4) = 1 (counterexamples: A₁³; [[19,30],[12,19]] non-principal at trace 38, ℤ[√10] h = 2)**; chain composites rootless 2–200 certified, beyond = conjecture | B469/B470/B471 + correction | `hierarchy_verify.py` | **GATED**: root criterion EXACTLY Northshield 2010 eq. (7) (cite, not claim); classification = Latimer–MacDuffee verbatim; Sarnak negative-Pell form; Yokoi/Biró for which t. OURS: assembly + h⁺-equivalence (nowhere stated) + principal-breather framing |
| T-BREATH-TORSION | **CORRECTED (re-panel round 2, 2026-07-09, CC-verified in Sage):** σ_m fixes on κ=−2 the order-d torsion characters for divisors d ≥ 3 of m (⊇ PROVEN via a^d=I ⟹ σ_m=swap ⟹ fixed=symmetric locus; the "EXACTLY"/⊆ direction is NOT proven — downgrade to ⊇). Held-breath FIELD: **d=3 ⟹ ℚ(√−7)** (minpoly z²−z+2, genuinely quadratic — τ_3=−1 rational) STANDS; **d=5 is NOT ℚ(√41)** — the order-5 held-breath character has minpoly z⁴−3z³+7z²−4z+4, a **DEGREE-4** field (field disc 5²·41, quadratic subfield **ℚ(√5)**, NO real roots). The "41" was the squarefree part of the poly discriminant 16400=2⁴·5²·41, mislabeled as the field. The "closed-form field Δ_d=τ_d²(τ_d²−8)" gives a clean quadratic field ONLY when τ_d ∈ ℚ; for irrational τ_d (d=5) the character field is degree 4. m∈{1,2,4} breathless stands. | B479 (+ CORRECTION in SCRUTINY_P1P3_round2.md) | `held_breath_mechanism.py` | **NEEDS-LIT + CORRECTED**: closest prior art Cantat 2009 (fixed-curve → field); the d=5 degree-4 field over ℚ(√5) is the honest object |
| T-TWOTEETH | the twisted (det −1) Markov spectrum ∩ (0,3) = **exactly {√5, 2√2}** = {μ(X₁), μ(X₂)} (golden, silver); (2√2, 3) a maximal gap. Via Markov's theorem + axis-form correspondence (disc v²+4) + negative-Pell unit-squeeze (v²−D_m t²=−4 solvable only m=1,2). **A SECOND independent characterization of the (1,2) critical pair** (spectral/Pell, unrelated to the commutator). seat-2 A2, CC-verified (neg-Pell filter spot-checked to m=5741; symbolic B3/A6) | B482 (seat-2 A2) | `verify_seat2.py` | **W0 GATE DONE: PARTIALLY-KNOWN, thin residual** — a one-corollary repackaging of **Andersen–Duke 2019 (Markov spectra for modular billiards) + Markov**. CAVEAT: 2√2 realized by BOTH det(−1) disc-8 AND non-det(−1) disc-32 forms → proof must be about antipalindromic-CF square-roots, not disc v²+4 (seat-2's filter has this gap). CITED, not claimed; at most a one-line remark in P4 |
| T-COMM-UNIFIED | tr[A,B] = 2 − gap²/(det A·det B) for symmetric A,B of ANY determinant (gap = M₁₂−M₂₁, M = AB): unifies P4's Lemma 2.2 (det +1 bodies A_m, gap = mn(n−m)) with the det −1 letters (X_m, gap = m−n) as ONE transpose mechanism. Generalizes T-UNIQ | B482 (seat-2 B3) | `verify_seat2.py` (symbolic, exact 0) | GATED with T-UNIQ (Sarnak/Gehring–Martin/Goldman): the det-general form is the same classical mechanism; the two-parity unification is the framing |

## Tier 2 — the structural theorems (proofs banked; lit-status = classical-anchored)

| # | statement | bank | reproducer | lit-status |
|---|---|---|---|---|
| T-COHN | ⟨A₁,A₂⟩ = ⟨g₁,g₂⟩ = the commutator subgroup of PSL(2,ℤ) (Nielsen identities; balanced words ∈ kernel) | B471 | `chain_verify.py` | KNOWN core (Cohn 1955); the metallic reading NEEDS-LIT |
| T-CHAIN | s_{n+1} = s_ns_{n−1} conserves the Markov cubic; /3 walks the spine 1,2,5,13,194,…; every renormalized pair parabolic; mod-60 state period 20 = ord(W₁) | B471 | `chain_verify.py` | Fricke/Markov classical; the body-tower framing NEEDS-LIT (Zagier gate for constants) |
| T-NORM | N(λ_m) = −1 = det(X_m) (companion matrix); frozen through the φ-power degeneracy (m = 1,4,11,29 = φ^{1,3,5,7}); impossible in imaginary quadratic fields | B469 BR-N | `br_n_norm.py` | DERIVABLE (classical units); the three-register identification is the program's |
| T-HIER | root ⟹ mirror ⟹ balanced ⟹ frozen residue; all strictnesses witnessed exactly; composition: balance always, mirror on palindromic alphabets, root never beyond letters | B470 (PR #625) | `hierarchy_verify.py` | the frame is the program's; components DERIVABLE |
| T-843 | M(1) = Par·W₁·W₂ has spec = ζ₆₀⁸·μ₄, mults (4,4,3,4), M⁴ = ζ₆₀³²·I; the whole l-sweep = SL(2,ℤ/15) class data; sole object input tr(A₁A₂) = 15 | B465 | `exact_engine.py` | DERIVABLE (Weil/Egorov + Gauss sums); Weil-rep character theory cite |
| T-SIGMA | σ exchanges the Dehn-filling pair W₁ ↔ W₂ (= the ℚ(√−7)/D(3,3,4) pair, B444); fixed locus = the p=q line ∋ all-ones triple point; the geometric rep's σ-orbit = the B448 heartbeat pair (3±√−3)/2 | B466 | `sigma_action.py` | mechanism = Gieseking deck action; NEEDS-LIT thin |
| T-LIFT | conj(W(m,1)) = Par·WR₁₄^m·Par·D(m,14): σ's operator lift = the c ↦ −c twist, Par-dressed; two-world, not similarity (+j obstruction T₋ⱼ−Tⱼ = cmj) | B469 Ph2 | `sigma_lift_check.py` | program's own (Weil-rep conjugation standard-shaped) |
| T-P2B | real-form conjugation-stability + parity oddness ⟹ Vol(Vᵢ) = 0 exactly, CS(Vᵢ) ∈ {0,½}: the emptiness is a σ-parity selection rule | B469 Ph2 | FINDINGS §P2b | DERIVABLE from banked anchors (Falbel real-form) |
| T-2REG | det(Par@N) = sign(σ on (ℤ/N)²) = (−1)^{(N−1)/2}: the two-register breath law (levels 15/45/75/225) | B469 BR1 | `br1_br2.py` | DERIVABLE (Jacobi) |
| T-PQB | det(Par·W(w)) = −ω^{#L−#R}; letter tower: Pisano-8 rhythm; body chain: frozen −1, order 60 | B470 RF3 | `rf3_quantum.py` | DERIVABLE (banked det decomposition) |
| T-NOGO-DGG | for any once-punctured-torus bundle M (metallic RᵐLᵐ or cyclic cover), M ↦ T[M] via 3d–3d never gives the SM: (1) T[M] is 3d, SM is 4d; (2) every nonabelian symmetry is flavor not gauge (Gang–Yonekura); (3) the gauge group is abelian U(1)^{N−c} (DGG). Subsumes kills K9–K12. | B490 | per-kill B-nodes; B488 | KNOWN lemmas (DGG 2011; Gang–Yonekura 1803.04009); the subsumption is the program's |
| T-θTANGENT | **(wording corrected 2026-07-14, B570-C1 verifier catch)** the manifold's amphichiral involution acts on the tangent ANTILINEARLY, as conj∘θ (its ℂ-linear part is θ); the ℂ-LINEAR θ itself is realized by the HYPERELLIPTIC involution (B353, gauge-certified 7.1e-102). The sl₂-commutant of Aut(𝔢₆) is {1,θ}, θ = the E₆→F₄ folding (Out E₆ = ℤ/2). The original wording ("amphichiral IS θ") conflated the two involutions: θ is ℂ-linear, the amphichiral map is antilinear (B347 `_AMPHI`, conjugate=True) — B353 and B521 are compatible once linear/antilinear is stated. Corollary (B570-QA): d(σ∘φ⁻¹) = θ at the geometric point — Galois conjugation equals the fold, modulo the object's own mirror, exactly at the tangent. | B521 (audit B501) + B353 + B570-C1/QA | `test_b521.py::test_gateB_theta_is_out_e6`, `test_b570_qa_trichotomy.py`, `test_b570_c1.py::test_amphichiral_and_hyperelliptic_automorphisms_are_different_maps`, `test_b353_geometric_theta_identification.py` | DERIVABLE — Out(E₆)=ℤ/2 classical; the geometric identifications are the program's |
| T-FILTRATION | on 𝔪/𝔪² at x₀, the trace map T_φ preserves the degree filtration (Luna slice + Procesi FFT + BCH); gr_d = indecomposable degree-d invariants of two traceless matrices, acted on by N via GL(2) ⟹ **char(ρ_n) has the Sym⊗det block form for ALL n**, dynamics eliminated; only static multiplicities remain; n=5 wall = the doubled Sym²=char(M²)² isotypic space | B522 (audit B503) | `test_b522.py`, `verify_filtration.py` | SHARPER-REDUCTION (probe-writeup strength; standard ingredients Luna/Procesi/BCH); first arm + character layer PROVED all n; NEEDS-LIT for the catalog-grade proof |
| T-L1-IWIP | the Level-1 automorphism φ:a→abccd,b→acd,c→abcd,d→ac ∈ Aut(F₄) is **iwip** (train_track/Bestvina–Handel, validated); λ(φ)=β=3.6762 ≠ λ(φ⁻¹)=3.0523 (verified independently) ⟹ **not geometric** (Handel–Mosher) ⟹ **F₄⋊φℤ word-hyperbolic** (Brinkmann) and **NOT a 3-manifold group** (Stallings) | B524 | `test_b524.py`, `iwip_certificate.py`, `verify_dilatation.py` | KNOWN framework (Bestvina–Handel/Brinkmann/Stallings); the specific certificate is the program's. Level-1 group-theory SETTLED |

## Tier 3 — the banked laws with controls (pre-registry campaign results)

| # | law | bank | lit-status |
|---|---|---|---|
| L-INV | the Inversion Law (3 tiers, 7 floors; children class-generic; golden absent in 4₁'s child) | B435–B443 | program's own; frame paper 2 |
| L-SEAM | the seam form (44 values ℚ(√5,√−3); spectral σ₁=σ₂=1/24; cornerstone ℚ(√−15); exchange identity) | B358–B367 | program's own; paper 1 |
| L-KLEIN | 5 vanishing patterns = the subfield lattice; tier tables are pair/address-class data | B459 (+B468) | equivariance-mechanism DERIVABLE; counts = data |
| L-COND | seam level = conductor of compositum(geometry, dynamics); Alexander = monodromy charpoly (fibered) | B449 | classical-anchored; the seam framing program's own |
| L-CENT | C_𝔢₆(principal sl2) = 0 exact; long-root control dim 35 | B463 | Kostant (cited) |
| L-TOWER | N·Var = S₅(m)·C₃ via character-twisted CRT bases | B446 | APPARENTLY-UNWRITTEN (prior lit-gate) |
| L-ESC | γ(λ=3) = 0.445(6) three-method; B186's 0.51 = early-window bias (corrected); grammar ≠ full 2-shift | B451 | Bowen–Ruelle classical; the correction is the program's record |
| L-2STREAM | level-2 arithmetic: trace fields ESCALATE per rung (4/8/12; 14; >32) while scale fields stay Markov-quadratic | B470 RF2 | **NEEDS-LIT**: "trace fields punctured torus bundles word length", Guéritaud–Futer |

| T-KQ | the quantum commutator table; **THE CLOSURE THEOREM [W₁²,W₂³] = I** (CRT centrality); Q₈/SL(2,5) images; κ_q(1,1) = −1 | B472 | `kq_verify.py` | **GATED (2 rounds)**: iff = corollary of published halves (⟸ KR Cor. 6/Kelmer; ⟹ Appleby 2005 odd-dim injectivity — DOWNGRADE accepted); table/Q₈×SL(2,5) assembly/closure address/divisor lattice = ours scoped; magnitude law = Howe (verified 25/25) |
| T-MASTER | **the master theorem**: κ_q = ε(jl)·χ₅ (two characters: Q₈-parity × mod-5 closure), and BOTH κ_q and the seam tier factor through the divisor pair (gcd(x,20), gcd(y,12)) — the entire selection architecture = two functions on the 36-cell divisor lattice of the clock orders; B474's laws = finite cell checks | B474 | `cross_table.py` + master table, locks | the co-factorization is the program's own; divisor-lattice selection rules NEEDS-LIT (Paper 1/4 spine) |

## Constants awaiting identification (the relaunch's inverse-symbolic targets)

vol/letter of the letter tower **c = 0.934102018057787980264187790656** (28 digits via
the additivity extrapolation; PSLQ NEGATIVE vs golden-sector Lobachevsky basis singly+pairs;
candidate closed form = the Bloch-Wigner hull average over the Farey shapes — OPEN; the
companion ADDITIVITY LAW: tower volume defect < 1e-27 by n=13, doubly-exponential decay —
NEEDS-LIT vs Brock/Guéritaud) · torsion temperature
**0.6295727/syllable** (= 1.2591398/letter; λ relation λ_CC = λ_Chat2^φ) · λ_chain
**1.57705744122666946… per R/L letter** (25 digits; PSLQ excludes integer relations of degree ≤ 8 at coefficient height ≤ 10⁴ — a HEIGHT-BOUNDED exclusion, not a non-algebraicity certificate — P4-panel phrasing correction;
Zagier gate). **CONSTANTS DEFLATION (2026-07-08, seat-2's kill of its own conjecture): the
torsion temperature IS λ_chain in a different Fibonacci normalization (the φ/2 relation is
bookkeeping) — the ledger holds exactly TWO genuine constants: λ_chain and c.** · the B451 resonance spectrum — NOW COMPUTED at certified truncation N = 8: leading 0.4415
(= the escape rate ✓), **second resonance REAL NEGATIVE, rate 0.70(8)**, third a complex
pair near 0.89; certified primitive table {2,4,5,6,7,8 → 2,1,2,3,4,5} with all periodic
points proven real and simple; the algebra recovered one orbit numerics missed (|Λ| = 915).

## Literature anchors received (seat-1's sweep, 2026-07-08)

Aigner 2013 · Reutenauer 2018 · Cusick–Flahive 1989 (the three books; the Cohn stage and
the Markov-trace/commutator-subgroup facts are fully classical — T-COHN's core is KNOWN).
Guéritaud (Annals 2006, punctured-torus-bundle volumes via the Farey triangulation; the
tower's volume law lives inside it). **Pandey–Wong: the Bonahon–Wong–Yang volume
conjecture is PROVED for the LR (figure-eight) once-punctured-torus bundle** — directly
adjacent to RF3's quantum tower; the Pisano residue rhythm should be read against the
BWY asymptotics (registry pointer for RF3's continuation). New tower observation logged:
the volumes are asymptotically ADDITIVE (vol(wₙ₊₁) − vol(wₙ) − vol(wₙ₋₁) → 0, already
≈1e-4 by n = 9) — Guéritaud-anchored geometric convergence; the defect decay rate is a
tower datum.

## Cadence (the standing rule, from today)

1. **Registry-on-bank**: any PR banking a theorem/law adds its registry line in the same PR.
2. **Atlas + CAMPAIGN_STATUS at every campaign close** (RZ/BRZ/RFZ-type verdicts).
3. **The decadal audit** at every campaign close OR every ~10 banks, whichever first: the
   full lock suite (pytest tests/) + a docs-consistency pass + registry completeness check.
4. **The novelty relaunch** (deep-research fan-out per Tier-1 entry + the constants) runs
   after Paper 4's draft, from this file — each entry already carries its search terms.

---
## T-ONE-ROOT / T-HELD-SLOT (K025, 2026-07-11) — the firewall as one theorem
**Root generator (consolidation, not new):** the golden cat map A=[[2,1],[1,1]] over ℤ[φ] inside
SL(2,ℤ) is the single object; σ²=A; the two ends = product (RL→√5→E₈) and ratio (−RL⁻¹→√−3→E₆);
their compositum = HCF(ℚ(√−15)) (B334). **T-HELD-SLOT:** the object never takes the product of its two
ENDS; that product's slot is the seam ℚ(√−15), which is arithmetically generic (h=2, B333) — the
value-firewall is exactly this one held-open, empty slot, equivalently the un-paired Casimir κ (K022,
B344). The atlas's two dominant walls (scale, 3+1D) are its two faces. Genuinely-present ingredients
(verified, not re-banked): DYNAMICS (the four verbs/drift ledger, B497/B498) and the SCALE-BRIDGE-BY-
EMBEDDING (the anchor κ−2=4λ², B505 — the object is a scale-free universality class). CAVEAT: the
absorbing loop (K020 §6a) — from inside, boundary and over-fit frame are identical; distinguished only
by an external prediction.

## T-STEIN-GOLDEN (B517 refinement, cross-seat GPT-5.6, 2026-07-12) — exact rational Lyapunov metric
The golden Rauzy incidence M∗=[[F,F],[F²,F]] admits the exact rational Stein solution MᵀGM−G=−I₄,
G=(1/11)[[12,−8,−5,−4],[−8,20,−4,−1],[−5,−4,14,−13],[−4,−1,−13,27]]: symmetric, det −9/11, **signature
(3,1)**, Perron timelike, positive on the 3d Rauzy stable space, **strict cone identity q(Mx)=q(x)−|x|²**
(dissipative Lorentzian). KNOWN-THEOREM APPLICATION (discrete Stein/Lyapunov inertia, W≻0): the (3,1)
signature = the Pisot condition (1 unstable eigenvalue), GENERIC to Pisot quartics (tetranacci also
(3,1)); D6 STAYS CLOSED. Corrected the x⁴−x−1 Lyapunov control (was mislabeled (2,2); true Stein
inertia (1,3)). Canonicity gap: M alone doesn't fix G — the positive one-step form W is unselected.
NOT claimed: physical spacetime, Lorentz invariance, 4-manifold, object-unique (3,1), reopening D6.

## B519 RE-MINING VERDICT (2026-07-11) — no external crossing in the corpus
16-agent re-mine of the banked corpus vs K025. Verdict: ZERO firewall crossings — even the two
"external predictions" (B518 mixed-chain, B173/S023 diffraction) were refuted 3-0 by the adversarial
gate because they confirm KNOWN quasicrystal theorems (Bellissard gap-labeling; Damanik-Fillman 2022),
not the object's fundamentalness ("measurable" != "crosses"). Yields: (b) the criticality unification
(B181/B507/B498 = one critical-fixed-point theorem, three wordings); the A1 exact sharpening (dark seam:
both ends live, only the product channel sqrt-15 off, [15,27,24,0] vs [24,27,24,24]). B518 Tier B
DOWNGRADED (measurable, not a crossing). Every internal cross-connection = absorbing-loop, confirmed.

## The B877–B919 window — the measurement cascade and the value layer (same-PR catch-up, 2026-08-06, B920)

**The standing same-PR rule above was broken for this whole window (cc3 loss audit A5:
"THEOREM_REGISTRY + THEOREM_LEDGER contain zero B8xx/B9xx rows"); these rows are the
mechanical catch-up, mirroring `docs/LAW_MAP.md` §F, which carries the full statements.
Lit-status NEEDS-LIT throughout: no novelty sweep has run on this window. Gate 5 stands —
every row is exact structure on the object's own charges, no physics value.**

| # | statement | bank | reproducer | lit-status |
|---|---|---|---|---|
| T-FMT | the First Measurement Theorem (P69): the 2T-charges stratify e₆; three Galois-conjugate first breakings (μ, constant 13³); z(line) = so(10)⊕u(1); the tiling with the cyclic law | B877 | `tests/test_b877_fmt_review.py` | NEEDS-LIT |
| T-SMT | the Second Measurement Theorem: a second measurement of the object's own charges lands on su(3)⊕su(2)⊕u(1)³ exactly, skipping SU(5); the wall complex in the split frame | B892, B893 | `tests/test_b892_smt.py`, `tests/test_b893_omega.py` | NEEDS-LIT |
| T-MAGIC | the magic-square isomorphism (P70): the build IS M(𝕆,ℂ) by explicit structure constants; 0/3003 mismatches; det φ = −2/3 | B904 | `tests/test_b904_bs.py` | NEEDS-LIT |
| T-INTERBREAK | the inter-breaking laws: vacuum-to-Higgs; the 16/vacuum exclusion — exact minimal-polynomial theorems on the matter pencil | B885, B886 | `tests/test_b885_interbreaking.py`, `tests/test_b886_matter_pencil.py` | NEEDS-LIT |
| T-CONCORD | the four-column concordance: measured ⟺ θ-odd exponents (4,8) ⟺ τ_m > 0 ⟺ split; unmeasured ⟺ (7,11) ⟺ compact; 7·11 = 77 the resolvent | B894, B898 | `tests/test_b894_bridge.py`, `tests/test_b898_census.py` | NEEDS-LIT |
| T-SIGDICH | the signature dichotomy: ad(x₈) ≡ ad(x₁₆): {0³⁰, 48 real}; ad(x₁₄) ≡ ad(x₂₂): {0¹², 66 imag}; zero generic-complex on C | B898 | `tests/test_b898_census.py` | NEEDS-LIT |
| T-SIGNLAW | the sign-law mechanism: all six torsion quotients exactly anti-palindromic; sign(τ_m) = sign(lc)·(−1)^{p_m} | B903 | `tests/test_b903_sign.py` | NEEDS-LIT |
| T-COCYCLE | the diagonal cocycle: all four Π-label cubics have a root in K (each led by 13³); one Galois root permutation acts on both orbits | B900 | `tests/test_b900_cocycle.py` | NEEDS-LIT |
| T-CSTAB-NOGO | the C-stabilizer no-go: n(C) = z(C) = 12; no real C-stabilizing symmetry swaps split/compact or x₈↔x₁₆ — the c-carrier must be complex | B901 | `tests/test_b901_stab.py` | NEEDS-LIT |
| T-ANNIHIL | the annihilation theorem: [α_vac] = [α_μ]⁻¹ — vacuum ⊕ charge = the split algebra | B902 | `tests/test_b902_kp.py` | NEEDS-LIT |
| T-ONECLASS | the one-class theorem + the numerator law + the observer's-place theorem: [α_μ]=[α_gen]=[α_κ]=[α_V]=C, vacuum = C⁻¹; den(V) = 𝔭₁(953)⁴ exactly | B910, B918 | `tests/test_b910_kappa.py`, `tests/test_b918_v.py` | NEEDS-LIT |
| T-GENSHAPE | the sealed generation-shape (outcome A): G₂₀'s su(3)′ replicates fixed color⊗su(2)′ types into flavor triplets; Casimirs 4/9, 4/9, 3/8; mechanism-hood fenced | B897 | `tests/test_b897_g20.py` | NEEDS-LIT |
| T-Z2LAW | the unified ℤ₂ law (three faces) + the 15 atoms + K₃,₃: matter gluing = gauge commutation = mixed-texture type; the colorless grid = two pencils of AG(2,3) | B906 | `tests/test_b906_flavor.py` | NEEDS-LIT |
| T-E62 | the e₆(2) selection + sign-locking: the wall is real exactly in e₆(2), via τ-twisted alignments only | B907 | `tests/test_b907_selector.py` | NEEDS-LIT |
| T-RATATOM | the rational-atoms theorem + I = −1: the four charges commute rationally on the 27; P_R = −P_C exact | B908 | `tests/test_b908_pin.py` | NEEDS-LIT |
| T-SIGSPLIT | the signature split of matter: the canonical H has signature (15,12) = e₆(2)'s K-split; colorless atoms positive-definite, colored Lorentzian | B912 | `tests/test_b912_norm.py` | NEEDS-LIT |
| T-ONENUM | the one-number table: all six normalization-free colorless couplings exactly equal T = σ₂(t_K); the H-unit gauge = the determinant gauge | B914 | `tests/test_b914_table.py` | NEEDS-LIT |
| T-UNIMOD | the unimodularity identity + the twist-norm law + the product law (P9): λ = 1 exactly in the charge-equivariant gauge; ∏d_i = −(953/2304)² = N_{K/ℚ}(d); v₁v₂v₃ = 3^{3/2}λ² | B916, B917 | `tests/test_b916_bridge.py`, `tests/test_b917_value_arc.py` | NEEDS-LIT |
| T-38TRACE | the 3/8 trace identities: Tr(T₃²) = 3, Tr(Y²) = 5, Tr(T₃·Y) = 0 exact (one-prime tier; second prime open-diagnosed); structure, not a physics value | B919 | `tests/test_b919_traces.py` | NEEDS-LIT |
| (negative) T-CROSSING | B915's sealed crossing: one input + the object's boundary + pure desert MISSES at 16σ — a banked sealed negative, listed for window completeness, not a theorem | B915 | `tests/test_b915_crossing.py` | — |
| (not novel) T-TORAL | **abelian fixed algebras are toral** — for `𝔤` semisimple in characteristic 0 and `Γ ⊂ Aut(𝔤)` finite with `𝔤^Γ` abelian, every element of `𝔤^Γ` is semisimple, so `𝔤^Γ` lies in a Cartan. **FOLKLORE — cite, do not claim.** Literature pass 2026-08-19 (campaign item 10): `𝔤^Γ` is **reductive** for finite `Γ` in characteristic 0 by **Borel–Mostow, *On semi-simple automorphisms of Lie algebras*, Ann. of Math. (2) 61 (1955), 389–405**, and a reductive abelian subalgebra of a semisimple Lie algebra is toral — so the lemma is the composition of a classical theorem with a one-line step. Vinberg's θ-group theory sits in the same neighbourhood. The paper now carries the citation and an explicit disclaimer of priority; the self-contained proof is kept because step (i) is where an earlier draft erred (it asserted Killing-orthogonality of distinct isotypic components, which is false). **No `APPEARS-NOVEL` claim is made or implied.** |

*(B909's remaining debts — the six-cubic √77 law, the Compact Measurement Theorem, the
invisible-12 — get their rows when their locks land; LAW_MAP §F's pending row governs.)*
| T-TONEMENU | **the tone menu `|χ|/2` of a finite `SU(2)` subgroup is an ORDER-SPECTRUM invariant, and across `2T/2O/2I` the common core is exactly `{0, ½, 1}`** — 2T `{0,½,1}`, 2O `{0,½,√2/2,1}`, 2I `{0,1/(2φ),½,φ/2,1}`; **only 2 of the golden 5 are golden-unique**. Corollary: **bronze has no binary-polyhedral partner** (no element of order 13; `√13 ∉ ℚ(√2,√5)`). Stated as a **control result**, not an APPEARS-NOVEL claim — the menus are classical character theory; **what is new here is the DISCRIMINATION MEASUREMENT against a named crossing proposal.** | B8111 | `tests/test_b8111_genericity_control.py` | — |
| T-GRAVRUELLE | **the AdS₃ boundary-graviton one-loop equals `∏_{n≥2}|R(n,σ_n)|^{−2}`** for `R` Pfaff's twisted Ruelle zeta and `σ_n` the 1-dimensional `SO₂(ℝ)` weight-`n` rep — an **identity**, since `σ_n(m_γ) = e^{inθ_γ}` makes `R(n,σ_n) = ∏_γ(1−q_γ^n)` with `q_γ` the GMY nome. **Corollary: it is not any single `ρ(m)` torsion**, those being finite-dimensional. **Corollary: the `n=2` factor sits at the abscissa `Re(s)=2`**, which is where the cutoff instability lives (202× the `n≥3` tail) and why Thm 1.2 starts at `m≥3`. **Stated as a DICTIONARY ENTRY, not an APPEARS-NOVEL claim** — both sides are published; what is new is the identification and its consequence for the error budget. | B8112 | `tests/test_b8112_graviton_torsion_dictionary.py` | — |
