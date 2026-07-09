# LEAD REGISTER — the now-computable frontier (2026-07-04)

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
