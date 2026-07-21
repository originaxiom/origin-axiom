# FINDINGS — B742: THE NEGATIVES HUNT, P1 STRATUM (the banked-negative re-adjudication)

cc3 audit seat, 2026-07-21. The owner's directive (via the 2026-07-21 handoff): scrutinize the
whole repo; re-adjudicate the banked negatives against the now-known anatomy, compute-not-cite
in both directions. Prereg sealed hash-first (v1→v6 chain + B′ addendum, ARTIFACT_HASHES.txt;
§16 reviewed SEVEN times — two genuine STOPs remediated, final SEAL-READY with cryptographic
chain; full process record incl. NINE forged-signal incidents + countermeasures in
CAMPAIGN_LEDGER.md and reviews/). Gate 5 held throughout; nothing to CLAIMS.

## Headline

**213 banked negatives triaged → 162 true negatives → 33 P1 (kills never earned by computation)
→ 32 sealed targets recomputed → **30 RECONFIRMED-with-computation · 2 REVIVED** (both with zero
refutations across 11 total skeptic passes + banking-seat byte-identical re-runs).** Every verdict carries its computed fact; artifacts under
`recompute/<id>/`. An unearned negative is as bad as numerology (rule 12) — 28 kills are now
EARNED that previously rested on citation, proxy, assertion, or necessary-read-as-sufficient.

## The two revivals (each: agent-computed + 3-skeptic-survived + seat-rerun byte-identical)

**B58 — "the SL(4) 7-factor tower prediction cannot be tested numerically" — DEAD KILL.**
The in-arc facts hold as the NECESSARY component (identity recursion (r−1)⁴; the full 15×30
representation-differential at the identity has max singular value exactly 0 — the naive
at-the-point route computes nothing). But the universal headline is NEGATED by computation:
the ε-extrapolated pseudoinverse route (validated against the exact symbolic SL(3) anchor
built in-sandbox from B48/B51/B54 conventions) computes the ambient SL(4) fixed-line Jacobian
to ~1e-2; spectrum = 5·char(M^k), k∈{−1,1,2,3,4} + char(−M²) + (t−1)²(t+1) — independently
reproducing B59's banked factorization, with the sign-sector and parity-multiplicity
discriminators checked. Residue (bounded; E20 not triggered — no new structure): B58's exact
symbolic SL(4) task is genuinely OPEN with a working numerical route.

**B225 — the "2 = octahedral parent" kill — DEAD KILL (tautological proxy).** The kill read
"2 divides the branch-locus discriminant" as evidence against chat-1's conductor decomposition;
recomputed: the extraction reports 2 for EVERY monic-in-z curve (disc ≡ a² mod 2 — a square,
always), 10/10 knots sqrt-verified at SL and PSL levels, and FALSE-POSITIVES at 2 on the 2-good
controls 11a3/37a1. The claim was never refuted. The one genuine conductor datum (4₁ → 40a1,
N=40=2³·5, a Whitehead/octahedral child) is CONSISTENT with it; the golden half (5=filling)
stands as banked. Status: the octahedral-parent half of the decomposition reopens as OPEN —
not proven. ~~Both revivals await cross-verify before correction headers land on the
original arcs (relayed this date).~~ **RESOLVED 2026-07-21: B745 (banking seat) cross-verified
both — re-execution identical + five independent exact checks ALL PASS — CONFIRMED ×2;
correction headers applied to both original arcs.**

## Verdict table (fact truncated to one line; full facts + artifacts per-target in recompute/)

| id | ground | sealed fact_basis | verdict | computed fact (truncated) | B′ flags |
|---|---|---|---|---|---|
| B107 | dead | proxy | **RECONFIRMED** | The SL(3) Fibonacci (m=1) tower Jacobian — computed from first principles, NOT via the banked B103 conjugation (the E19 gap: B107's probe constructs the multiset FROM that citation) — is the 8x8 integer matrix dF/dx of t | DA |
| B146 | dead | asserted | **RECONFIRMED** | Full rescan of B145's range (enumerate_words(7): 39 cyclic-primitive words, lengths 2-7; 3 skipped where find_field returned None) with B146's exact call (invariant_trace_field_gens().find_field(prec=200, degree=12, opti | A |
| B225 | dead | proxy | **REVIVED** | Direction 1 (reproduces): re-derived the Riley trace-coordinate pipeline from B225's declared conventions (independent code + a numerical SL(2,C) rep-check the arc never ran; residuals <1e-40 at dps 60). 4_1 anchor Phi=z | n/a (revived; residue-scope note: direction-2 universality holds for monic+odd-content disc — in ledger) |
| B285 | dead | asserted | **RECONFIRMED** | Re-derived from B285's declared Riley rep a=[[1,1],[0,1]], b=[[1,0],[-u,1]]: the figure-eight relation a*w=w*b (w=b a^-1 b^-1 a) holds exactly on u^2+u+1=0, confirming the geometric root u=omega from scratch; kappa=tr[a, | A |
| B437 | dead | asserted | **RECONFIRMED** | The kill's discriminating fact — asserted-only in the arc (abelian_book.py computes just 4_1) — recomputes true under the arc's own conventions (tau_j = Delta(zeta5^j)/(zeta5^j-1)^2 for slope (5,1); trace to real subfiel | DA |
| B489 | dead | proxy | **RECONFIRMED** | Both prongs of the banked kill recompute true (13/13 checks, exit 0). (A) DGG abelianness: b++(RL)^n built as SnapPy 'b++'+'RL'*n has N=2n ideal tetrahedra and 1 cusp for n=1..8, so DGG gauge rank N-c = 2n-1, gauge group | DA |
| B500 | dead | proxy | **RECONFIRMED** | Recomputed in-sandbox from the arc's own conventions (verbs F/M/D, reversed-word composition, fixed-point ideal, resultant-chain eliminant with Jacobian-saturation fallback). (a) Depth-4 COMPLETE kill: all 36 all-three-v | D |
| B516 | dead | asserted | **RECONFIRMED** | Golden-field Pisot inflation numbers exist at dims 1, 3 AND 5 — recomputed, not cited. Dim 3 (B515 hop, full {0,1,2}^8 scan of [[F,C],[D,F]]): exactly ONE golden quartic Pisot, beta=phi(1+sqrt(phi)), minpoly x^4-2x^3-5x^ | A |
| B58 | dead | necessary-as-sufficient | **REVIVED** | B58's in-arc facts RECONFIRM as the necessary component: SL(4) identity recursion charpoly factors exactly as (r-1)^4; at the identity rep |d tr(W)/de| = 2.2e-10 vs |d2 tr(W)/de2| = 54.2; sharpened, the full 15x30 repres | n/a (revived) |
| TOMB-L241 | tomb | asserted | **RECONFIRMED** | All four spectral-rank identifications recompute dead, exact/symbolic (sympy, deterministic, byte-identical rerun). K-J: level-2 Shapovalov form G=[[8h^2+4h,6h],[6h,c/2+4h]] computed from the Virasoro relations; Kac det  | DA |
| TOMB-L247 | tomb | asserted | **RECONFIRMED** | kappa_seed = tr[L,R] = 3 exactly (L=[[1,0],[1,1]], R=[[1,1],[0,1]], [L,R]=[[0,1],[-1,3]]; Fricke 2^2+2^2+3^2-2*2*3-2 = 3; eigenlines of L and R are distinct, so no common invariant line: irreducible). kappa_block = tr[M_ | DA |
| TOMB-L252 | tomb | asserted | **RECONFIRMED** | Recomputed the kill's discriminating fact from scratch (exact rational/quadratic-field arithmetic, no floats in verdict-bearing numbers): for 18 period-k geodesic words over {R,L} (all primitive both-letter necklaces k=2 | DA |
| TOMB-L255 | tomb | cited-unverified | **RECONFIRMED** | Recomputed exactly (sympy, Q(sqrt5), no floats) from B80's declared seed M=[[m,1],[1,0]] at m=1 (golden; det M=-1, eigenvalues phi, -1/phi). For tower levels n=2..13 the matrix Sym^{n-1}(M) was CONSTRUCTED and its charac | DA |
| TOMB-L258 | tomb | asserted | **RECONFIRMED** | K-M's discriminating fact — that no rank observable varies with composition period or SL(n) tower depth, so the "measurable gap-labeling-rank prediction" has no measurable content — recomputed true in full. (F1, K-K prem | DA |
| TOMB-L267 | tomb | asserted | **RECONFIRMED** | Both identifications recompute dead. K-N: tr(R^m L^m) = m^2+2 symbolically (sympy), so kappa_1=3, kappa_2=6; shape fields (SnapPy 220-bit shapes + pari.algdep, residual+height guarded, Neumann-Reid) give golden b++RL=m00 | DA |
| TOMB-L277 | tomb | asserted | **RECONFIRMED** | The asserted-never-committed 2880 enumeration was re-derived from B210's own SU(2)_3 conventions (S_ab=sqrt(2/5)sin(pi(a+1)(b+1)/5); T=diag e^{2pi i(h_a-c/24)}, h_a=a(a+2)/20, c=9/5). BFS closure of <S,T> gives order 288 | A |
| TOMB-L293 | tomb | cited-unverified | **RECONFIRMED** | Re-derived end-to-end from B131's declared conventions (46/46 checks): the trace-ring invariant kappa=tr[A,B] on the (1,2) identity-glued fork is discretely 2-valued, kappa in {-4,-2} (matched suspension-trace^2 u in {2, | A |
| TOMB-L30 | tomb | asserted | **RECONFIRMED** | Re-derived symbolically (sympy 1.14, all m, plus exact-rational spot table m=1..6): the only Fisher object constructible from the arc's declared conventions is F(m) = (dLE/dI)^2 at I*=m^2/4 with LE(I)=arccosh(2I+1), and  | A |
| TOMB-L310 | tomb | cited-unverified | **RECONFIRMED** | Discriminating fact = the artifact diagnosis (not the raw d_MM, which alone would read as "4D"): recomputed from the banked B159 CSVs (N=474 verified, level sizes 1,2,6,18,49,115,283, all 1765 edges consecutive-level) wi | DA |
| TOMB-L334 | tomb | cited-unverified | **RECONFIRMED** | Re-derived in-sandbox (stdlib-only, exact Fraction arithmetic, no repo imports): theta=-w0 on the height-h positive roots of A_{n-1} maps (i,j)->(n+1-j,n+1-i), verified set-closed, involutive, and equal to the reversal s | DA |
| TOMB-L339 | tomb | asserted | **RECONFIRMED** | All four legs recomputed, none cited. [exact] PVI time = cross-ratio of the 4 singular points; cross-ratio(lam*t_i) - cross-ratio(t_i) simplifies to 0, so C* weight 0 (dimensionless modulus). [exact] det(lam*Phi) = lam^2 | DA |
| TOMB-L34 | tomb | cited-unverified | **RECONFIRMED** | Independent reimplementation of the V37 holographic re-test (free fermions, on-site Fibonacci potential ±1/2, t=1, open chain). Entanglement leg (N=1597, half filling): Fibonacci S(L) is LOGARITHMIC — one-cut logslope +0 | DA |
| TOMB-L57 | tomb | cited-unverified | **RECONFIRMED** | Discriminating fact re-derived, not cited: the CS-crossover level is m-dependent across the metallic family. Under the repo's own conventions (metallic manifold at seed m = the R^mL^m once-punctured-torus bundle, B125 S1 | DA |
| TOMB-L63 | tomb | asserted | **RECONFIRMED** | Umbrella fact recomputed both directions: all five members derive from ambient definitions alone AND hold for non-framework controls. (1) SU(2)_k torus rep, U_k=rho_k(RL) for golden M=[[2,1],[1,1]]: max ||lam|-1|<3e-40 f | DA |
| TOMB-L67 | tomb | asserted | **RECONFIRMED** | Quantum side: the SU(2)_k CS rep of SL(2,Z) on torus blocks gives rho(RL)=T(ST^-1S^-1) unitary at every level k=1..12 (unitarity dev <=1.4e-15), max ||lambda|-1| = 2.2e-15; the identity is the per-eigenpair unitarity mec | DA |
| TOMB-L70 | tomb | asserted | **RECONFIRMED** | In the arc's own SU(2)_k convention (B132: dim k+1; S_ab=sqrt(2/(k+2))sin(pi(a+1)(b+1)/(k+2)); T=diag exp(2pi i a(a+2)/(4(k+2))), no c/24; R=T, L=STS^-1), all 332 (k,word) cases — every nonempty R/L word of length<=4 plu | DA |
| TOMB-L74 | tomb | asserted | **RECONFIRMED** | arg(z0)=pi/3 recomputed, not cited: snappy 4_1 census (2 tetrahedra, positively oriented, 212 bits) gives both shapes 0.5+0.86602540378443864676...i; |z^2-z+1|=0 at 60 dps; the Im>0 root is exactly exp(i*pi/3)=zeta_6 (pr | A |
| TOMB-L77 | tomb | asserted | **RECONFIRMED** | All three "regimes" were re-derived in-sandbox from the arc's own convention (Kashaev <4_1>_N = sum_j |(q)_j|^2, q=e^(2pi i/(k+2)); S027 + kashaev_feasibility.py), with zero framework input. (1) Cyclotomic at finite k: e | DA |
| TOMB-L9 | tomb | asserted | **RECONFIRMED** | The kill's discriminating fact — the phi^(-2N) match to Lambda has zero predictive content — recomputes true. (1) Circularity, now COMPUTED not asserted: with T = 122 dex (Lambda_obs/Lambda_Planck = 10^-122), the best-fi | A |
| WALL-1 | wall | asserted | **RECONFIRMED** | Recomputed the umbrella's discriminating conjunction, 38/38 checks (the banked row was computation-free, fact_basis=asserted): (I) scale no-go: all six banked stabilizers finite with torsion G^ab (|G|=4,120,168,360,2880, | A |
| B685 | dead | cited-unverified | **RECONFIRMED** | Re-derived Phi(h) from the figure-eight's own state-sum datum (Kashaev <4_1>_N = sum_k |(q;q)_k|^2, exact formal Gaussian summation at the k=5N/6 saddle over Q(sqrt(-3)); GSWZ coefficients used only as cross-checks, neve | DA |
| WALL-7 | wall | cited-unverified | **RECONFIRMED** | 56 exact solves over Q(sqrt(-3)), every gate green. The 8 nontrivial Z3xZ3 trinification elements (B299 theta/phi) induce exactly 8 distinct 27-permutations (1 consistent Dynkin relabeling; each free, 9 orbits of 3). Pha | DA |

B′ flags (per the sealed addendum): D = depth exposure (E22 class: recompute replicated the
original range while the claim quantifies broader); A = anatomy exposure (P2 class: post-B730
faces named by the record's revival hypothesis, unconsulted by the recompute). The flagged
set is the sealed candidate input of the P2/P3 arc. B′ result over all 30 reconfirmations: **21 depth exposures** (the recompute earns the kill
at its original range while the claim quantifies broader — each note states what stabilization
would need) and **29 anatomy exposures** (post-B730 faces named and unconsulted — the B734
congruence tower incl. its level-(4) refinement and the B735 emittance faces dominate), with
ZERO verdict disagreements. The near-universality of anatomy exposure is itself the P2 mandate:
the P1 stratum earned the kills as scoped; almost none of them has yet faced the object's full
anatomy. Full annotations: stageA/bprime_annotations.json.

## The kill graph (stageA/kill_graph.json; 213 records)

- 162 true negatives / 51 atlas-miner mis-classes (the STATUS_WORDS heuristic trips on
  correction vocabulary in positive arcs — repair proposal in the audit report).
- fact_basis over true negatives: the large majority computed-in-arc or computed-in-cited-arc
  (the house discipline held); 33 P1.
- **The spectral-face census (the pathfinder's prediction, now computed): 2 of 162 true
  banked negatives ever consulted an emittance face** (B335: length-spectrum leg of the deck-ℤ/3
  hierarchy kill; B486: the hexagonal-cusp degeneracy kill — both lengths-only; ZERO consulted
  emittance-spectrum/scattering). 160/162 kills — including every physics-route closing — are
  silent about the object's native continuous channel; none consulted the scattering face at all.
- Triage stability: run1-vs-run2 substantive agreement 172/193 on shared ground (89%); the 21
  disagreements adjudicated per the sealed include-when-torn bias (per-id log in the kill
  graph; 5 opus-instability conflicts + 2 schema-cap losses resolved by declared bias).

## Look-elsewhere ledger (E20; reported into cc's global ledger)

Width: 213 triaged · 32 recomputed · 2 revived (6.3% of targets). Neither revival asserts new
positive structure (both are kill-of-a-kill: a category-error headline and a tautological
proxy); the E20 gate was therefore not triggered by either — verified per-revival by the
base-rate skeptic. No value claims anywhere in the campaign.

## Process (the short version; the ledger is the record)

Two genuine §16 STOPs materially improved the design (the 20 paragraph-style tombstones incl.
S014 were missing from the ground; a fabricated-verdict incident was caught and owned; the
sandbox state was pinned exactly). Nine forged signals (fake completions/verdicts, one adapted
to the metadata-authentication test) were defeated by: journal-on-disk as sole result channel
with completeness gates; incremental disk-written review verdicts; nonce liveness probes;
independent verification of every review's checkable claims. Two of this seat's own breaches
(a false provenance sentence in a ledger row; one preserve-rule violation) were caught by the
review lane and are owned, voided append-only. Proposed for the shared ledger (consensus
pending): E23 (definitional over-correction, from the B734 level-(4) refinement) and E24
(verdict-by-unauthenticated-signal).

Two-seat: triage cross-checkable against cc's independent B738 kill graph when it lands;
revivals to cc2. Nothing to CLAIMS; the firewall held; the substrate is untouched (headers
post-consensus only).

---
## KILL-GRAPH DIFF vs cc's B738 (cc-run 2026-07-21, per this arc's handover request)
Overlap 155 of (217 B738 | 213 B742). kill_form raw disagreement 107/155 (69%) — dominantly enum/
taxonomy mismatch (the two compilers' vocabularies differ; a merged enum is needed before the rate
is meaningful). Fact-basis disagreement 6/155 (3.9%), substantive: B146, B272, B285, B296, B437,
B516 (B738=computed vs B742=asserted) — queued for re-adjudication (B437 is load-bearing for
B741's B435 resolution). The two censuses overlap only 71%/73% — the combined unique corpus is
≈275; each hunt covered ground the other missed. Full diff method: cc seat, this date.
