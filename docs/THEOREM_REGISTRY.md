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
| T-BREATH-TORSION | the half-monodromy σ_m fixes on the cusp κ=−2 EXACTLY the order-d torsion characters for divisors d ≥ 3 of m (geometric character never fixed — always σ_m-swapped, BR3 wave 2). Held-breath field Δ_d = τ_d²(τ_d²−8), τ_d = 2cos(2π/d): **3\|m ⟺ ℚ(√−7) (order-3), 5\|m ⟺ ℚ(√41) (order-5)**; m∈{1,2,4} breathless (no non-degenerate divisor). Mechanism PROVEN (a^d=I ⟹ σ_m = swap ⟹ fixed = symmetric locus); prime-m components = order-m cyclotomic trace exactly | B479 (+capstone) | `held_breath_capstone.py`, `held_breath_divisor_law.py` | **NEEDS-LIT**: "fixed points of pseudo-Anosov / mapping class on SL(2,C) character variety", "trace map periodic points orbifold", punctured-torus σ-action torsion; natural Paper 3 (σ/residue) result |
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
