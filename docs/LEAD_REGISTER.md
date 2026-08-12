# LEAD REGISTER — the now-computable frontier (2026-07-04)



> ## STATE AT REVIEW 45 (2026-08-13) — L160 closed; the invariant line is the new lead candidate
>
> L160 CLOSED (B1041, exhibited obliquely). NEW candidate at R45-3: the identification of the solo
> invariant line h⁰(M;27) = 1 (surfaced by B1043's entry gate). Cloud leads qL155–qL166 renumber
> at digest (main's next: L161). L159 stays reading-gated; L158 scoped by B1040/B1041's two
> halves. Ledger: Review 45.

> ## STATE AT REVIEW 44 (2026-08-12) — three leads registered this window
>
> **L158** — the V-owner reconciliation (FL-1/FL-5/FL-6; discriminator = the FL-4 cell). **L159** — the gerbe question (the programme's central structure = a non-neutral Tannakian category, cited zero times; the degree-2 neutrality class never computed; READING-GATED on Deligne–Milne). **L160** — the three (ℤ/2)³ cubes (two legs proved in B766; the space-level bridge banked in B733; open only at θ ↔ √−7 + B782-compatibility). L157 amended (the cover struck; the yield pinned). Full statements: `docs/OPEN_LEADS.md`. Ledger: Review 44.

> **State at Review 37 (2026-08-03).** The SM-structure window closed: the selection spine
> (repair → fused principle → termination → anomaly split → registerability keystone → menu
> gate) carries **zero load-bearing imports**; the **First Measurement Theorem** (the object's
> superselection charges stratify e₆; three Galois-conjugate first breakings; triality tiling
> with a cyclic law; matter = the two foreign sectors) is a **two-seat theorem**; **THE
> DESCENT** shows each breaking's matter is exactly one SM generation's multiplet pattern while
> the triple lives *across* the three breakings, not within one. Structure only — no values,
> no generations mechanism, Gate 5 untouched. Ledger: `docs/progress/REVIEWS.md` Review 37.


**What this is.** An exhaustive re-score of the whole non-banked corpus against *today's* toolset,
to find work that "wasn't ready when it was started, is computable now." Method: 5 parallel readers
over **133 non-banked probes** (76 dead + 43 open + 14 dormant) + the five registers
(`OPEN_LEADS`, `OPEN_PROBLEMS`, `HINT_LEDGER`, `TOMBSTONES`, `FAILURE_ATLAS`) + the **deferred
sub-computations inside *banked* work**. Each item was judged on one sharp axis: did it stall on a
**tooling** limit we have since removed (→ a lead), or hit a genuine **wall** (→ not a lead)?
Firewall respected throughout — every lead below is mathematics; nothing promotes to CLAIMS.

## The toolset (the unblockers)

1. **Exact modular-CRT + Fox/Wada engine** (`frontier/B425_geometric_torsion/geometric_torsion.py`)
   — twisted Alexander / Reidemeister torsion at any SL(2,ℂ) rep, and polynomial/eliminant
   reconstruction via CRT over 𝔽ₚ. **Sidesteps the sympy/Sage Gröbner-and-determinant slowness that
   killed most tooling-stalled probes.** By far the dominant unblocker below.
2. **Two-torsions / Eisenstein frame** (B425) — the geometric/holonomy (√−3) side is real and
   computable, distinct from the golden (√5) side.
3. **Exact ℚ(ζ₆₀) cyclotomic engine** (`B358_seam_certification/cyclo_engine.py`) + level-45 fp engine.
4. **Principal-SL(2)/E₆ + involution machinery** (`B347_e6_tangent_gradings/`) — Sym^{2m} cohomology,
   amphichiral/hyperelliptic signs, minuscule decompositions.
5. **mpmath 120-digit + bounded-height CRT reconstruction** with banked constraints.
6. **Recurrence atlas** (`scripts/atlas/query.py`) — obstacle→resolution oracle.

## The headline

The single most coherent high-value campaign is **the metallic A-polynomial program** (Cluster A):
*one* CRT-elimination engine — the (M,L) eliminant of B67/B89 generalized to the metallic monodromy
φ_m — simultaneously yields the spectral-curve genus (B87), the silver/bronze A-varieties
(B201/B203), the exponent law k (B157/B198, via the A-poly slope — **not** raw Gröbner), the
conductor law (B225), and the Weil zeta (L34). Five-plus banked-adjacent results from one build.
Plus two shovel-ready standalone HIGH leads: **e₃** (Cluster C — load-bearing: its prime content
auto-fires the B403/B405/B406 sentinel battery; the reconstruction sentinel is already running) and
**gate-A adjoint torsion** (Cluster B — deepens the value-firewall's one in-sandbox gate; B425 has
already demonstrated the exact engine on this very class).

## Ranked priority (suggested compute order)

| # | ID | what a result settles | tool | now? | cost | score |
|---|---|---|---|---|---|---|
| 1 | **B399** | e₃ exact (depth-5 triple cubic t³−(1/48)t−e₃); **fires B403/B405/B406 sentinels** | #5+#1 | YES | M | HIGH |
| 2 | **B201** | silver (m=2) SL(3) A-variety relations (silver M³=L); only a pipeline bug blocked it | #1 | YES | L–M | HIGH |
| 3 | **B87** | m=3 metallic spectral-curve genus (completes the sequence 3, 1, ?) | #1 | YES | M | HIGH |
| 4 | **L54** | extend the no-forced-choice seal to the nonabelian adjoint/Ptolemy torsion (gate-A) | #1 | YES | M | HIGH |
| 5 | **B157** | the metallic exponent law k in [A,B]=s·µᵏ across the (m,o,n) grid | #1 | YES* | M | HIGH |
| 6 | **B203** | closed-form silver SL(3) A-polynomial (the standing NEEDS-SPECIALIST object) | #1 | PART | M–H | MED |
| 7 | **B198/9** | exact-symbolic k=2 at SL(5) o=5 (certify the numeric), via the A-poly route | #1 | PART | H | MED |
| 8 | **B225** | whether the "5 = golden filling" conductor law holds across the 2-bridge/twist family | #1 | PART | M | MED |
| 9 | **B106** | rank-4 Fix(T₁²) completeness + exact c=i (16-var, below the 25-var wall) | #1+#3 | PART | M–H | MED |
| 10 | **L34** | Weil zeta / aₚ / conductor of the silver–bronze character variety | #1 | PART | M–H | MED |
| 11 | **B412** | the tower-measure's p-adic L-function (downstream of B399's e₃) | #5+#1 | PART | M–H | MED |
| 12 | **L5/L6** | is S031 sealing metallic-special or general (non-metallic o-p-t words)? | #1+#5 | PART | M–H | MED |
| 13 | **B138** | extend the S031 sealing capstone from SL(3) to SL(4) | #1 | PART | M | MED |
| 14 | **B372** | the level-135 pair-channel hierarchy test (the last untested scale lever) | #1+#6 | PART | H | MED |
| 15 | **B269** | does WRT(4₁) carry the 2T = SL(2,𝔽₃) structure at the quantum level? | #3+#4 | PART | M–H | MED |
| 16 | **B204c** | does the WRT level-period law reach beyond SU(2) (SU(N)_k / other RCFT)? | #3 | PART | M | MED |
| 17 | **B84** | the SL(n≥5) tower multiplicities from first principles (rigor upgrade) | #1 | PART† | H | MED |
| 18 | **B185/91** | a genuine metallic 2-cusp connector (geometric realizability of N≥3 units) | #1 | PART | H | MED |

`*` B157/B198: computable via the **metallic A-polynomial route** (the A-poly slope gives k); raw
25-var Gröbner is walled even over 𝔽ₚ (see Walls). `†` B84 has a genuine-math residue (the
degenerate-sector canonicalization); tool #1 enables the symbolic-Procesi route but does not by
itself close it — the gain is "from first principles," not a new value.

**LOW (computable, minor payoff):** B332 (Bianchi index [Γ:Γ∩gΓg⁻¹]=3 on the √−3 side, #2),
B313 (S032-A single-seed invariant classes, #1/#3), B415 (level-27 μ_∞ confirmation, #3),
B174 (genus-2 sole-κ screening, #1), L53+ (order-4 integrability obstruction, #4),
B178/B171 (exact gap-power / rank-3 label via #5), B38/B39 (torsion-one *identity* — but T1
naturality stays walled).

## The clusters (how to actually compute)

**A. The metallic A-polynomial program** — *the master campaign.* Build the CRT (M,L)-eliminant for
φ_m (generalize B67 fig-8 / B89) → reads out, per m: the A-polynomial, its L-slope (**= the exponent
k**, B157/B198), its discriminant (**= genus**, B87, and **bad-primes/conductor**, B225), the SL(3)
lift (**silver A-variety**, B201/B203), and 𝔽ₚ point-counts (**Weil zeta**, L34). Leads 2,3,5,6,7,8,10.

**B. The value-firewall / gate-A sealing** — the deepest in-sandbox firewall form. L54 (adjoint/Ptolemy
torsion Galois-orbit seal, the shovel-ready one), + L5/L6 (general-word), B138 (SL(4)), B313 (S032-A).

**C. The e₃ / tower-arithmetic node** — *load-bearing.* B399 (e₃, fires sentinels; sentinel running)
→ B412 (p-adic L-function) and B372 (pair-channel hierarchy).

**D. SL(n≥5) tower from first principles** — B84 (Procesi trace ring; partial, has a math residue).

**E. Quantum / WRT extensions** — B269 (2T structure), B204c (period law beyond SU(2)).

**F. Misc computable** — B106 (rank-4 census), B185/191 (2-cusp), B332, the LOW list.

## The walls (NOT leads — recorded so we don't revisit)

- **Selector-naturality axiom (T1/S1)** — the C5 "coupling-selector" residual (B14–B47, B38/B39): no
  compute tool manufactures the naturality of the inserted axiom. Genuine.
- **Class-S T[4₁;E₆] / input=output-E₆ / local-theta proof / referee-read** — specialist walls
  (B247–B305 cluster, L50/CRUX, B264-novelty, B391).
- **Structural pinv under-count** (B58/E1) — a₂=2 fails from numerics for a *structural* reason
  (verified exact-𝔽ₚ AND exact-ℚ); "STOP, do not patch"; the value comes from B62 structure.
- **Non-Hermitian, no ground truth** (B163/B192/gate-D, L19-3a/L20) — Damanik–Gorodetski off-axis;
  no target to compute against.
- **Raw 25-var Gröbner** (L22, B199) — stalls over 𝔽ₚ *too*, not just ℚ(ζ); needs Magma/msolve, not
  our CRT. (This is *why* the exponent law must go through the A-poly route, Cluster A.)
- **Interval-arithmetic hyperbolicity** (B165/B186 off-axis Cantor) — a rigorous cone-field proof,
  not a CRT/cyclotomic/E₆ computation.
- **Many-body thermodynamic limits** (B172/B183/B187/B188) — need DMRG/tensor-network/scaling.
- **Physics firewall** (B20/B21/B170/B188/B189/B207, B101/B107/B177/B343/B392/B400/B418) — not math
  leads by construction.

## Caveats (honest scoping)

- **Not everything is CRT-able.** The raw high-variable Gröbner walls (L22) persist even mod p; the
  metallic exponent law is computable *only* through the A-polynomial slope, not brute ideal-membership.
- **PARTIAL ≠ done.** Leads 6–18 each carry a residual "which object / which theorem" component beyond
  the raw computation; the score reflects the computable half.
- **Provenance.** Merged from a 5-reader sweep (2026-07-04); each cell was verified by reading the
  probe's FINDINGS, not inferred. Revisions belong here, not backfilled elsewhere.

## Parked lead (2026-07-10): the trace-map transfer-operator spectrum as the un-laundered dynamical face
The trace map T (κ=tr[A,B] dynamics) is the ONE face of the object that is analytic/dynamical, not a
topological invariant — so no laundering theorem in the program covers its transfer-operator spectrum
(flagged in the Relation Campaign as the strongest H1 candidate). B451/D4 already computed the certified
N=8 Ruelle spectrum at λ=3: leading 0.4415 (escape rate), 2nd 0.705 (gap ≈0.26), 3rd ≈0.89 (complex
pair). UNRUN: (a) higher precision n=9,10; (b) the metallic m-scan (is the resonance spectrum m-dependent
in a structured, non-rescaling way?); (c) the un-laundering test on the ratios; (d) the quantum bridge to
the D1/D2 spectral form factor. A full prereg was drafted then parked when "TM" resolved to Thue-Morse
(B496), not trace map. Revisit as its own campaign.

---

## ⟳ VIEW REFRESH — 2026-07-29 (Review 32)

*This file is a **navigation view**, not substrate (GOVERNANCE §12: "freeze the substrate;
generate the views"). It is regenerated at each decadal review, and from Review 32 the
`views-fresh` gate **fails the build** if a review does not touch it — the mechanism replacing
the written rule that let this file go 19 days stale while ~55 arcs were banked.*

**Reconciliation at this refresh:**
- **Its top-ranked HIGH items are already closed** and must not be re-computed:
  **B399/e₃** cleared (B578-D4, ℚ(ζ₉)⁺-cyclotomic, sentinels clean-negative);
  **B201/B202/B203** resolved (peripheral relations resolved-negatively; the component identity
  resolved); **B225** resolved HALF/HALF (5 = golden filling confirmed; 2 ≠ octahedral parent).
- **B372 is an ID collision** — this file's "level-135 pair-channel" is a different probe from
  OPEN_LEADS's "level-45 tables" (DONE). Treat as two items.
- Live from this register: **B87** (m=3 metallic genus), **L54**, **B106**, **B138**.

**Current live frontier (superseding anything above that conflicts):** the Maass thread is
closed at B797 — 17 certified m004 eigenvalues, one parent + sixteen Γ₄₁-relative, independently
verified 7/7 (B795), with a clean rung-4 SM null that the Listening Protocol had already ruled
inadmissible as evidence. The live campaign is **B796 (coupling)**, gated and launch-approved,
whose falsifier is the **50+ digit Maass algebraicity test** (rung 1 — the only admissible
comparison). Standing open gate on any physics reading: **L91**, obligations (1)–(3).

> **Review 33 (2026-07-29)** — no lead status changed this review; the work was infrastructure and absorption. New registered item **R33-4**: decide LAW_MAP's enforcement posture (lock the load-bearing rows and gate them, or mark the ledger explicitly as an unenforced index). Ambiguity there is what the review found.

> **Review 34 (2026-07-30)** — new: **L107**, the correctly-specified null for H130 — a decision to run, *not* a claim. B580's information-free channel and B686's parametrisation finding stand as the obstruction.

> **Review 35 (2026-07-30)** — no new leads. **L110 closed**: the `CS(m004) = θ_QCD` dictionary is
> **refuted on type** (B813) — computed invariant vs free coupling, PSL(2,ℂ) vs SU(3), and a **role
> collision** (a Chern–Simons quantity would occupy the *coefficient* slot of `e^{iθW(A)}`, where a
> Chern–Simons functional already sits). The refutation is of the **direct identification**, not of
> every possible construction.

> **Review 36 (2026-08-01)** — no new leads. **P5's novelty row closed** after sitting PENDING since
> 2026-07-10: no prior art for the four-strata frame; the κ-laws' delta is the **non-invertible**
> sector; the drift ledger's method is classical so the claim is the ledger.


*Review 38 (2026-08-05): window B890–B906 reviewed — the M(𝕆,ℂ) isomorphism, the sealed generation-shaped verdict, the flavor arc with I = −1, the Kim lit-gate; five promotion candidates listed; next sealed cell: the real-form selector (B907). See docs/progress/REVIEWS.md.*


*Mid-window update (2026-08-05, post-crossing): B907–B917 — e₆(2) selected; the norm/signature; I = −1 exact; the one-number table; THE CROSSING (MISS 16σ, the desert dead, R4b registered); the value-arc convergence with the solo seat. See CAMPAIGN_STATUS and the masterplan v5.*


*Review 39 (2026-08-05): window B907–B919 + the register loop + THE CROSSING reviewed; suite green after hygiene; candidates listed (B908, the value-layer cluster, B912, B914 + R38 leftovers); next sealed: R4b. See docs/progress/REVIEWS.md.*

*Review 43 (2026-08-11): window B1009–B1030 — the switch-verification / fourth-crossing / WHY-campaign window. The fourth crossing died clean **by one degree** (leptonic −120° vs NuFIT 5.2's upper error; refresh pre-committed at the same windows); THE WHY CAMPAIGN opened and its first cells banked — **the freedom ledger lands COMPRESSION (0.000 retroactive designer bits against a 4.585-bit conservative output floor)** and **θ is the value-kernel of the frame action** (the banked θ-triviality, placed); the input floor quantified and adopted: **one unit, two bits, one trit** (+ the J acceptance). All four of the window's disclosed errors were caught by standing rules; one new class (E22, verdict-before-certificate). TOOLBOX.md remains the named reader-standard block (R43-1). See docs/progress/REVIEWS.md.*

*Review 42 (2026-08-09): window B989–B1008, the instruments window. **Two locks were red at HEAD and nobody knew** — four consecutive arcs banked NEGATIVEs without routing them, rebuilding the backlog B836 cleared; the cause is that the ~55-minute suite had not been run to completion, and gates do not cover what locks cover. **Two BLIND rungs had computed arcs behind them** — X1 (B725, cited in its own row) and X2 (B559, **cited nowhere**) — both re-graded SPLIT with the arcs cited inline. B798 stands in full after B1007 withdrew its own cost claim; B806's number superseded by B1008 **without bumping a threshold**. **TOOLBOX.md at lag 638 is now two reviews old and is named as the block.** New: the atlas is epoch-blind (L148), and **project memory — the channel that carries across a model switch — was 51 arcs stale with no gate measuring it.** See docs/progress/REVIEWS.md.*

*Review 40 (2026-08-07): window B909, B914–B941 reviewed — the three crossings all negative, D₂ decoded as the hierarchy's carrier, the value layer proved value-invisible, two precedent numbers banked (the Maass and Dirac eigenvalues), and the branch-symmetric ratio-only phrasing registered as binding on any future crossing. Three real discipline failures caught by the anti-burial locks and fixed; the priority-language asymmetry flagged (B922's unqualified claim predates the O3 gate — panel dispatched). See docs/progress/REVIEWS.md.*

> **Review 41 — 2026-08-09.** This register was **outside** the 43-lead `OPEN_LEADS` triage — a second register nobody swept. Also: **the kill graph carries a revival structure no register indexes** (231 hatches, 220 revival scores, **167 UNTRIAGED**), registered as **L145**. Two registers it cited had **rotted paths** — both files exist at `speculations/TOMBSTONES.md` and `docs/atlas/FAILURE_ATLAS.md`.
