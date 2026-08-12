# THE CONSOLIDATION-DEBT LEDGER — what no CURATED consolidation carries

**CONSOLIDATION REFRESH** (`docs/THE_CAMPAIGN.md`). Working note on a feature branch; nothing
banked from this file, no claim's label changes.

> ## ⚠ THIS FILE HAS BEEN CORRECTED TWICE. Both corrections came from testing the measurement, not from new reading.

> **Correction 1 — the surfaces.** v1 said *"580 of 934 arcs are cited on NO surface a reader
> navigates by"*. **False.** Measured against all thirteen navigational surfaces,
> **absent-from-everything is 0**: the *generated* `docs/views/VERDICT_LEDGER.md` indexes every
> verdicted arc, by construction. `GOVERNANCE` §12 — *"generate the views … everything a reader
> navigates by is a view"* — had already said so. The architecture is **two-tier**, and v1
> measured one tier while describing both.

> **Correction 2 — the regex.** v2 tested only the bare id `\bB239\b`. **`CLAIMS.md` cites its
> evidence by PATH** (`frontier/B239_reconciled_trace_field_law`), where the trailing `_` defeats
> the word boundary. So the test **missed the single most important form of consolidation —
> promotion to a P-claim** — and marked **49 arcs absent that are cited**, nearly all of them the
> promoted P/C/E claims (B67→P23, B71→P24, B239→P48, B264→P50, B354→P55 …).

> **A specific finding of v1/v2 is WITHDRAWN with it:** *"B575 is cited nowhere, yet `CLAIMS.md`
> P51 names it as its own evidence."* **B575 IS cited** in `CLAIMS.md`, both by name and by
> path. **And the first attempt to explain that withdrawal was also wrong:** B575 was not a
> path-form victim. The real cause was a **scope widening** — a band note's accurate claim
> (*absent from `LAW_MAP`/`THE_FRAMEWORK`/`THEOREM_LEDGER`*) was carried into this ledger as
> *"cited on no surface"* without re-checking `CLAIMS.md`. The path-form defect is real and
> separate — it costs 49 arcs — but B575 is not one of them.

| version | curated-absent | substantive debt |
|---|---|---|
| v1 (5 surfaces, bare id, instruments counted) | 579 / 934 | *353* |
| v2 (+ instrument split) | 579 / 934 | *294* |
| **v3 (+ path-form citations)** | **509 / 934 (54.5 %)** | **245** |

**The finding has survived all three passes, smaller each time and better founded.**

---

## §0 — THIS IS THE SECOND DEBT REGISTER, AND THE FIRST ONE IS GATED

> **Added 2026-08-11 by B1033. The defect repaired: this file was built without checking whether
> the repository already had a debt register. It does.**

`docs/REPRESENTATION_TRIAGE.md` (from **L143 / B976**), swept by
`scripts/checks/representation_sweep.py`, lists every *substantial* banked arc cited on no
synthesis surface, with three dispositions — **PENDING / PROCESS / SURFACE** — and the
`representation-sweep` gate **fails the build** when such an arc is untriaged: *"An untriaged
unrepresented arc is the defect."* **Until this section, this file cited it zero times.**

**The two rules differ, and each is right for its own question.**

| | `REPRESENTATION_TRIAGE` (gated) | this ledger |
|---|---|---|
| verdicts | PROVED ∪ NEGATIVE | PROVED |
| substantiality filter | **`claim_one_line` ≥ 500 chars** | none |
| surfaces | **9**, incl. working registers (`OPEN_LEADS`, `CAMPAIGN_STATUS`, `HINT_LEDGER`, `knowledge/INDEX`) | **5 curated consolidations** |
| asks | *"is this represented anywhere a synthesis reader looks?"* | *"is this **distilled** into a curated consolidation?"* |
| count | **10 live** (17 rows, 13 PENDING) | **234** |
| overlap | **6 arcs** | |

Neither number is withdrawn. **What was wrong was publishing one without the other** — the same
defect B1030 filed against `THE_CLAIM` vs B1000, the unreferenced register this time being this
one. **B976**, whose lead created the triage, appears in this ledger's rows and *not* in the triage
— correctly: it is cited on `THE_SM_VERDICT` and `SM_SPECIFICATION_LEDGER`, which are sweep
surfaces and not curated ones. Both registers were behaving as designed; only the cross-reference
was missing.

> **On the count moving: 245 → 251 → 234.** This measurement is a **moving** one by construction —
> every consolidation row added retires a debt row, and this pass added eleven arcs' worth. The
> **234** here is measured against the tree at B1032. The lock bounds the share rather than pinning
> the integer, precisely so ordinary consolidation work does not break it.

### And reconciling them measured something worse than the omission

**The gated register's substantiality bar is a step in time, not a measure of substance.**
Median `claim_one_line` length, by band:

| band | B0–99 | B100–799 | **B800–899** | **B900–999** | **B1000+** |
|---|---|---|---|---|---|
| median chars | 145 | 156–162 | **733** | **2571** | **3084** |
| share ≥ 500 | 0 % | **0 %** | 56 % | 95 % | 100 % |

> ### **Zero of the 731 arcs banked before B800 can ever clear that bar.** The gate that exists to catch *"a row that was never written"* is structurally blind to two-thirds of the corpus.

This is **not a miscalibration.** The register was calibrated on the **eleven** lost cascade arcs
(B860–B873; B862 excluded because another seat had already cited it) and it catches **11 of 11** —
a post-convention block, where the field is an abstract rather than a one-line summary. The bar is
right for the job it was built for, and carries **no stated era scope** while its rule says *"every
**substantial** banked arc."*

**Three further measurements, each recorded because it changes what should be done about it:**

- **The margin on its own calibration block is two characters.** **B862** — same block, the arc
  that **derives the global ℤ₆ form** — has a claim line of **498**. It is outside the calibration
  set only because another seat cited it an hour earlier. Had it not, the headline would have been
  11 of 12, and the miss would have been the block's most consequential member.
- **The obvious fix fails.** A band-relative threshold (≥ 2× band median) recovers **1 of 12** of
  the calibration block. **Tested before proposing, and rejected** — trading a known blind spot for
  an unknown one is worse than naming the known one. *(Registered as **L158**.)*
- The measure the register **rejected** — FINDINGS.md file size — is the **era-stable** one
  (median 2.0–5.5 KB in every band, no step). Its rejection was right *within* the late era
  (B864's FINDINGS is 3.7 KB, short and dense) and does not generalise across eras.

### The consequence for this file, which reverses its own plan

The intention was to **stratify these rows by that bar** — 19 above, 215 below. **That is refused.**
Every one of the 19 is **≥ B870**; applying the bar would silently discard the entire pre-B800
corpus, importing the blindness just measured. **The rows stand unstratified**, and what they are
is unchanged from the correction above: *not unreachable — **not distilled***.

---

## THE MEASUREMENT (v3)

Each of the 934 distinct verdicted arcs tested for a citation of itself — **both** as a bare id
**and** in the `Bnnn_` path form — across the five **curated** consolidations: `LAW_MAP`,
`THE_FRAMEWORK`, `THEOREM_LEDGER`, `CLAIMS`, `THE_LADDER`.

| | count | share |
|---|---|---|
| arcs with a verdict | 934 | 100 % |
| carried by no curated consolidation | **509** | **54.5 %** |
| — of which PROVED | 295 | |
| — — of which `instrument: true` (**not debt by design**) | 50 | |
| **— — SUBSTANTIVE debt candidates** | **245** | |

> ### Every arc is reachable; **245 substantive results have never been carried into a curated consolidation.**

An instrument arc has no law to consolidate, so its absence is correct. A generated view carries
everything, so nothing is lost. **What the number measures is what the distilled layer holds:
when a curated surface is asked whether the programme holds a given law, it answers from a
minority of the record.**

### Limitations, declared

1. **Absence of a citation is absence of a pointer, not of a fact** — a surface may carry the
   content under another arc's name.
2. **The `present` side is untested** — a citation may be a passing mention that does not carry
   the law, so coverage can be overstated in the other direction too.
3. **Therefore every row below is a CANDIDATE, not a verdict**, until its body is read.

---

## By band — substantive debt

> **These are the v3 BASELINE, not a live count** (annotated 2026-08-12, B1050). They are the
> figures as measured when v3 was written, and **consolidation moves them by design** — B0–B99
> reads **19** here and is **16** live, the three retired by B1044's sibling citations (B33,
> B75, B77). The corpus total is **245** here and **190** live. *The baseline is kept as a
> baseline; a table that silently drifts is worse than one that says which day it describes.*

| band | substantive | arcs | rate |
|---|---|---|---|
| B0–B99 | **19** | 85 | 22 % |
| B100–B199 | **37** | 97 | 38 % |
| B200–B299 | **33** | 99 | 33 % |
| B300–B399 | **36** | 97 | 37 % |
| B400–B499 | **39** | 93 | 42 % |
| B500–B599 | **35** | 85 | 41 % |
| B600–B699 | **9** | 84 | 11 % |
| B700–B799 | **8** | 91 | 9 % |
| B800–B1029 | **29** | 203 | 14 % |

**B100–B499 still carries the most — 145 of 245 (59 %)** — but the
path-form correction flattened the profile considerably: the promoted P-claims live exactly there,
and they were being counted as debt. **B400–B499 is now the single densest band.**

---

## THE ROWS — substantive, PROVED, carried by no curated consolidation

245 candidates. ✔ = body read in full.

| arc | body | its own claim, verbatim (truncated) |
|---|---|---|
| **B19** |  | Three exchange conditions have identical solution sets giving exactly plus/minus P, while four weaker formulations leave many candidates. |
| **B21** |  | Under the Goldman/Weil-Petersson bracket from Fricke-Vogt, the half-step trace map is anti-Poisson and its square is Poisson. |
| **B27** |  | The exact eight-dimensional SL(3) Fibonacci trace lift retains the A quadratic sector and splits into symmetric/antisymmetric inverse-trace blocks. |
| **B28** |  | The trace map is equivariant under central-lift sign actions preserving Fricke-Vogt, making B26's sign flip legitimate while the antipodal map is not. |
| **B30** |  | The Fibonacci trace map descends polynomially to canonical PSL sign-quotient coordinates (u,v,w,r), where the half-return becomes a literal period-3 orbit. |
| **B33** |  | SL(2) and SL(3) trace-map Jacobian spectra decompose exactly as symmetric powers of the half-step eigenvalues (Sym^2; Sym^3+Sym^2+trivial). |
| **B34** |  | The central-sign action is Poisson for the Fricke-Goldman bracket, so the sign quotient is natural and the anti-Poisson half-step descends. |
| **B35** |  | The half-step action on central signs has order 3 over F_2, explaining the order-3 projective return via lift-sign topology. |
| **B55** |  | The c=1 fixed-line sector structure is settled for all m: the symmetric sector is mod-4 (Phi_6 / Phi_4 / parabolic degeneration at m=0 mod 4) and the antisymmetric sector is univer… |
| **B57** |  | Classifies integer splitting of the antisymmetric fixed-line quartic for m=1..6 (c=1,3 universal plus m-dependent extras) and kills the class-number coincidence. |
| **B59** |  | Determines the SL(4) fixed-line spectrum numerically (five char(M^k), a new sign sector char(-M^2), degree-3 parity), refuting PC12's (n^2-1-parity)/2 prediction. |
| **B60** |  | Establishes the empirical cross-n tower map for n=3,4: M-powers climb and densify, a sign sector appears at n=4, and the parity block grows. |
| **B61** |  | ESTABLISHED: B60's SL(5) 'conditioning wall' was a rank-23 forward-word coordinate defect, and inverse-word coordinates at dps=60 resolve 22 of 24 multipliers onto the Cayley-Hamil… |
| **B63** |  | The SL(4) metallic fixed-line Jacobian factors over Z[m] into Dickson factors char(M^k) with m-independent structure, L_k=tr(M^k). |
| **B70** |  | The two-block trace-ring obstruction's non-separable content is a single rank-1 coupling a*b*tr(X^2) equal to the e2 invariant, with closure bounded at bidegree (3,3). |
| **B75** |  | degree=rank is a two-parameter (m,n) phenomenon: M^3=L holds on the m=3 metallic bundle as well as the figure-eight, not a figure-eight accident. |
| **B76** |  | The metallic cusp k-set equals the SU(2) quantum-group root-of-unity level set: 2cos(pi/k)=[2]_q at q=e^{i pi/k}, order-2k torsion on both sides. |
| **B77** |  | degree=rank sharpens to the signed scalar-matrix law [A,B]=(-1)^{n-1} mu^n, while the A-to-D unification with the Dickson spectrum is refuted. |
| **B83** |  | The SL(n) figure-eight Dehn-filling A-polynomial family is L=(-1)^{n-1}M^n on the principal component, with the SL(4) member L=-M^4 new. |
| **B100** |  | Two independent published frameworks (Ptolemy variety, Baker-Petersen twisted Alexander) agree with the repo's SL(3) figure-eight character variety and geometric-rep Jacobian. |
| **B101** |  | V0 is the Fuchsian locus of the SL(3,R) Hitchin component, with a 5-dimensional cubic-differential deformation family off it that stays Anosov. |
| **B102** |  | Every irreducible SL(3) figure-eight character is Case I or trB=trB-inverse=1; W1/W2 are excluded from the Hitchin component by ellipticity, not complexity. |
| **B106** |  | Dehn-filling fixed points are partially elliptic with root-of-unity neutral eigenvalues, and degree=rank holds eigenvector-by-eigenvector as L_i = c M_i^k. |
| **B109** |  | The void is a (2,1) saddle of kappa whose linearization has Lyapunov rates ±4log(phi) and a center manifold equal to the tower's parity sector. |
| **B111** |  | The tower's sign structure equals the all-heights opposition-involution closed form plus exactly one degree=rank promotion char(M)->char(M^n). |
| **B113** |  | The proved closed form determines the SL(5) sign sectors at heights 2-4 by theorem and confines degree=rank to the height-1/top-power interface. |
| **B117** |  | The tower is one object, the Sym two-sequence, whose shape follows from a dimension identity; the 'promotion' is really a Sym-1 absence. |
| **B118** |  | The theta=-w0 fixed-root sign is (-1)^(h+1), proved symbolically and verified for n<=12; B112's assumed uniform +1 holds only for odd h. |
| **B121** |  | The tower's SL(2)-action is the external det=-1 GL(2,Z) monodromy, inequivalent to Kostant's principal sl(2) for all n>=3 via the odd-Sym parity obstruction. |
| **B122** |  | The tower equals Sym^n(W) + (Sym^{n-3}(W) - W) for W = V+1, a genuine GL(2)-module identity that unifies B121's external det=-1 action. |
| **B123** |  | The figure-eight's regular triangulation shape e^{i pi/3} gives trace field Q(sqrt-3) and arithmeticity, offered as a third independent m=1 selection criterion. |
| **B124** |  | Reciprocal (lambda,1/lambda) eigenvalue pairing is a generic symplectic fact; exactly one residue is metallic-specific. |
| **B125** |  | SnapPy invariant trace fields show arithmeticity selects m=1 (Q(sqrt-3)) and m=2 (Q(i)) and kills m>=3, overturning the unique-m=1 reading. |
| **B132** |  | The SU(2)_k quantum layer: field content is word-spin-mod-4 quantum-group arithmetic, m=1 is uniquely coherent, vanishing period is |O_K^x|/2, and Lee-Yang is the native physics. |
| **B137** |  | The SL(3) sealing extends to silver m=2: zero irreducible off-sublocus fixed points escape Q(i), once the reducible-locus artifact is filtered out. |
| **B141** |  | The phi-fixed principal tower is reducible for all n>=3 by Q8 finiteness, while the phi-squared geometric tower stays irreducible in Q(sqrt-3): finiteness versus density splits S03… |
| **B142** |  | A Klein-4 argument proves the principal phi-fixed stratum reducible without any search, and the s776 Borromean/SU(3) enhancement claim fails on three counts. |
| **B147** |  | The chiral mirror pair RRL/RLL is fully arithmetic (Q(sqrt-7), integral traces, integer Bianchi ratio), so arithmetic chiral bundles exist. |
| **B150** |  | The SL(2,Z) trace-map action on the Fricke character variety IS the N=2* class-S S-duality mapping-class action; tau-modularity and magnitude are only rhymes. |
| **B154** |  | degree=rank generalizes beyond the figure-eight to the metallic family via the derived meridian mu=A^-m t, with the exponent order-determined rather than rank-determined. |
| **B158** |  | Omega is the ABELIANIZED SPECTRAL IMAGE of the metallic trace-map tower: the bundle-monodromy characteristic polynomials are reciprocal factors of the integer Omega family (L18 res… |
| **B163** |  | The kappa<2 spectrum is control-bracketed as a totally disconnected Cantor set, and no spectral feature encodes the figure-eight geometry at kappa=-2. |
| **B164** |  | The (0,4) Jimbo-Fricke cubic is built explicitly, its Painleve-VI/MCG dynamics exhibited via the three Vieta involutions, and bridged to the once-punctured-torus cubic at the void … |
| **B169** |  | A working Schlesinger/Painleve-VI flow is built and verified monodromy-preserving, carrying metallic dynamical degree lambda_m^2, correcting B164's orbit-norm proxy. |
| **B172** |  | Weaving two distinct metallic chains produces a real persistent spectral gap whose IDS is no single-frequency label — an interaction-born combination gap. |
| **B173** |  | The woven two-seed gap-label group is rank 3 = 1+#distinct quadratic fields (PSLQ-certified), reducing B172's gap to the gap-labeling theorem. |
| **B174** |  | Cusp-gluing two metallic bundles gives a continuum only on the curve-aligned locus; every other GL(2,Z) map forces a finite discrete kappa-fork. |
| **B175** |  | The woven collective spectrum is two-number predictable: frequencies fix every gap height exactly, couplings fix widths by an order-power law at weak coupling. |
| **B176** |  | Golden is genuinely privileged in the woven combination structure (dominates silver and bronze, not a bare-width artifact) but the ordering below it breaks. |
| **B178** |  | One textbook perturbative mechanism underlies both the width law and the golden privilege; the per-frequency structure width~L1^n1 L2^n2 is confirmed contamination-robustly. |
| **B183** |  | Opening the permanently-critical metallic chain gives a genuine irreversible spectrum at zero threshold, with g_c equal to the minimum Lyapunov exponent (localized control exact ln… |
| **B186** |  | The off-axis kappa<2 hyperbolicity hypothesis is certified by three independent diagnostics, the escape rate validated on the Damanik-Gorodetski-proven kappa>2 ground truth. |
| **B187** |  | Exact diagonalization shows the open metallic collective stays thresholdless at all interaction strengths, while the localized control keeps a finite protective threshold. |
| **B191** |  | A coupling 2-cusp connector propagates the kappa-constraint between leaves, so the selection mechanism nests past the pair-cap to N>=3, staying discrete and proliferating. |
| **B193** |  | Chirality and the SU(2)_k eigenvalue field are independent (all four combinations occur), and field-fusion to Q(zeta12) is quantum while classical trace-fields stay disjoint. |
| **B198** |  | Gauge-fixed Newton breached the B157 wall: at SL(5), o=5, m=1 the metallic exponent is [A,B]=+mu^2 (k=2), certified to 23 digits. |
| **B200** |  | Of a cross-chat handoff only R2 survives verification: on-site is the unique finite-range interaction preserving the Fibonacci chain's Sturmian structure. |
| **B201** |  | The silver (m=2) SL(3) character variety Fix(T_2^2) has exactly four dimension-2 components, one more than the figure-eight's three. |
| **B205** |  | The generic-q skein quantum trace map for the metallic family was constructed and verified in-sandbox (central element, quantum Dehn twists, q-Chebyshev structure). |
| **B209** |  | The icosahedral tiling's exterior algebra decomposes into every A5 irrep at multiplicity exactly 4, with the four spinorial 2I irreps completing E8 absent. |
| **B214** |  | The WRT period law extends to arbitrary hyperbolic words as lcm(t-2,t+2) on the principal class and splits by conductor across ideal classes. |
| **B215** |  | The class-field period law's closed form P=lcm(t-2,t+2)/d with d the scalar-reduction depth is verified exact for conductors f in {2,3,4}. |
| **B220** |  | Corrected exact diagonalization shows the antiferromagnetic golden (Fibonacci-anyon) chain is gapless with central charge c=0.71, reproducing tricritical Ising c=7/10 in-sandbox. |
| **B222** |  | Momentum-resolved exact diagonalization recovers the full tricritical-Ising primary content including the h=3/2 supercurrent, confirming the golden chain's emergent N=1 supersymmet… |
| **B226** |  | The object's two supersymmetries are two distinct faces separated by the hyperbolic/non-hyperbolic divide, bridged by SU(2)₃ rather than the figure-eight's geometry. |
| **B229** |  | The tricritical Ising has two distinct 3d-3d bulk realizations — ordinary Seifert over S²(3,4,5) (|H₁|=83) and super over S²(3,3,5) (|H₁|=66). |
| **B232** |  | The ρ_n tower obeys a one-step stabilization recursion ρ_n ≅ ρ_{n−1} ⊕ Sym^n ⊕ Sym^{n−3}, verified exactly to n=8 and on the real Jacobian to n=5. |
| **B233** |  | The ubiquity of '5' is one causal cascade through the field ℚ(√5) plus one genuine coincidence (smallest metallic discriminant = largest McKay prime), not eight miracles. |
| **B234** |  | Recomputation of the two handoffs verified the trace-1 congruence law disc=1−4det (excluding E₇'s ℚ(√2)) and caught one overclaim in each chat. |
| **B236** |  | The ordinary and super TCI cosets are literally the same coset (SU(2)₁×SU(2)₂)/SU(2)₃, and a sweep confirms this pair is the unique such coincidence. |
| **B242** |  | Level-rank duality acts as complex conjugation at κ=5, so SU(2)₃ and SU(3)₂ knot invariants coincide exactly iff the knot is amphicheiral; the three SU(3)'s stay distinct. |
| **B245** |  | Higher-color level-rank duality for the figure-eight extends the SU(2)_k = SU(k)_2 conjugation result beyond the fundamental. |
| **B251** |  | H₁(Mₘ)=ℤ⊕(ℤ/m)² forces only m=1 to be a knot complement, so the E6↔E8 geometric transition is golden-specific. |
| **B254** |  | Verified the arithmetic spine 4₁→ℚ(√−3)→2T→E6 and merged it with the forced quantum chain at (G₂)₁=Fibonacci inside (E₆)₁ by exact central charges. |
| **B255** |  | The tetrahedron (d=3) is the unique regular simplex whose rotation group's binary cover McKay-corresponds to an exceptional Lie group with a complex fundamental. |
| **B256** |  | E7 is the silver member's discriminant field ℚ(√2)→2O, completing the Arnold trinity arithmetically while remaining the one group with no geometric realization. |
| **B257** |  | Characterized the Euclidean transition point as the character-variety discriminant branch point with order-3 Eisenstein meridian and vanishing complex volume. |
| **B258** |  | Resolved H27: the trace field ℚ(√−3) is figure-eight-specific and the discriminant field ℚ(√(m²+4)) metallic, coinciding only at m=1; the quantum face splits into the same two ends… |
| **B260** |  | Identified the SL(2,ℂ) character variety as the Coulomb branch of T[4₁] (A-polynomial verified), dissolving wall #1: zero theorems block object→physics, but no bridge is built. |
| **B262** |  | Reconstructed T[4₁] from its own triangulation: U(1) gauge, 2 chirals, monopole superpotential — abelian, confirming McKay-E6 is arithmetic-only. |
| **B265** |  | The {4,8} deformation directions are E6-Zariski-dense (generate all 78 of e₆), establishing E6-irreducible flat connections on the figure-eight near ρ_prin. |
| **B267** |  | Coherence check passes: the arithmetically-selected E6 and the character-variety E6 are the same Lie object, the McKay exponent set matching the tangent-space grading. |
| **B270** |  | Re-derived rather than cited: the quadratic cup-product obstruction vanishes in the SL(2)/exponent-1 block, and dim H¹=#cusps makes every deformation a cusp deformation. |
| **B271** |  | Identified the amphicheiral τ-breaking (chirality) locus with the E6-irreducibility locus — the 26=e₆/f₄, exponents {4,8} — while wall #4 needs an external 2- or 4-manifold input. |
| **B275** |  | Exhibited an explicit numerical E6 flat connection on the figure-eight with nonzero exp-4 component, a concrete witness off ρ_prin for B274's existence proof. |
| **B276** |  | The figure-eight colored-Jones degenerates at q=ζ₃,ζ₆ with periods 3,6 and values in ℤ[ζ₃], the trace field ℚ(√−3) whose ramified prime 3 yields 2T=McKay-E₆. |
| **B289** |  | The Chern-Simons sign law CS(p,-q) = -CS(p,q) is robust, and its meaning is a Q(sqrt-3) Galois reading; verified by two methods. |
| **B290** |  | The (1,n) core geodesic obeys the Neumann–Zagier ladder ℓ_ℂ=2πi/n+(π/√3)/n²+O(1/n³) with coefficient predicted by the cusp shape; separately, the filling n is not the WRT level k. |
| **B291** |  | A stable min-volume closing m004(±5,1) (vol 0.98137) exists and is non-arithmetic and not the fiber closing, so selection is axis-stratified with no universally distinguished closi… |
| **B301** |  | Complexity of the 27 filters E₆'s maximal subgroups to the chiral set {SO(10), SU(6)×SU(2), SU(3)³} — not a unique SO(10) — and the kept SU(3)³ is B299's trinification triality. |
| **B302** |  | The order-3 symmetry absent from the torsion-free knot group lives in the commensurator PGL(2,O₋₃) as a hidden symmetry, with the figure-eight an index-12 cover of that orbifold. |
| **B304** |  | Extended the forced set from kinematics into gauge dynamics (sin^2 theta_W=3/8, beta-signs, 24=|2T| grading count); refuted Chat-1's saddle-SU(3) claim. |
| **B305** |  | Verified E6 to SU(3)^3 trinification grading at the Eisenstein eigenvalue omega, tying the object's sqrt(-3) arithmetic to the breaking; the saddle is SU(2)^3. |
| **B306** |  | Established the forced E6 principal-grading cascade N=1..6, with a left-right SM-containing group at N=5 and an SU(2)^3 saddle, not Chat-1's dim-14 window. |
| **B311** |  | Trinification sits at a genuine irreducible A-polynomial branch point (upgrading B305), but N=2 is reducible and N>=4 off-curve, so the chain is not realized. |
| **B312** |  | Showed Face IV houses the same E6 as the content via the CIZ level-10 modular invariant, plus both arithmetic ends; the level itself is generic. |
| **B315** |  | Showed the object's E7 exclusion contains heterotic's E7-skip, with pseudoreality FS(56)=-1 the shared root among three independent obstructions. |
| **B316** |  | sqrt(-7) is the CHIRALITY field, not a metallic-ladder member: disc -7 is below the unimodular floor, and Q(sqrt-7) is reached by BREAKING amphichirality (non-palindromic RRL/RLL w… |
| **B318** |  | Split the firewall's two ends: the Eisenstein Z/2 is the geometric amphichiral involution (complex conjugation), the golden Z/2 is arithmetic-only with no geometric tau. |
| **B319** |  | Resolved the woven-vs-single conflict as a false dichotomy: single-operator fractality is monotone (Hurwitz) while the two-body combination ladder is standalone; B176 banks both. |
| **B321** |  | Verified |cusp shape|^2 = h(E6) = 12, giving filling form p^2+12q^2; refuted the pi/6-core-length and Z/3-democracy splices; sharpened the multiplicity gate. |
| **B323** |  | Verified the four-level map: Z/3 exists only at the E6 gauge level and the commensurator, and they are distinct; the omega-circulant Yukawa is tautological and unmatched. |
| **B324** |  | Verified exactly in Z[omega] that commensurator-conjugate generations give a Z/3-circulant trace matrix with Eisenstein coefficient omega and degenerate light eigenvalues - structu… |
| **B327** |  | Proved n1=n2 in the 27|2T branching is forced by self-duality rather than integer spin, reducing the hierarchy CRUX to whether 2T embeds quaternionically in E6. |
| **B334** |  | The Hilbert class field of the seam Q(sqrt(-15)) is exactly the two-ended compositum Q(sqrt5, sqrt-3), verified by splitting law and forms; the 137 reading is dead. |
| **B335** |  | The generation ℤ/3 is the deck transformation of the 3-fold cyclic cover of 4₁, hence an isometry, so every real geometric invariant (and any mass) is exactly degenerate across the… |
| **B337** |  | Structure XOR ordering: the shared arithmetic forcing E6 also forces a degenerate spectrum, while distinct seeds order it but destroy the shared structure. |
| **B338** |  | The object contains its own symmetric-to-broken flow — Dehn filling with CS(1,n) ~ −1/(2n) — but the filling slope is external input. |
| **B343** |  | The deck ℤ/3 acts irreducibly on the object's Klein 2-torsion, forcing exact TBM (θ₁₃=0) rather than TM2; irreducibility explains every blindness. |
| **B344** |  | The deviation space is forced into a symplectic reciprocal pair (lambda, 1/lambda) plus the unpaired central kappa-axis, which is exactly the external scale door. |
| **B345** |  | The Z/3 charges of the deviation modes force an anti-diagonal charge-conservation texture, independent of the E6-exponent grading. |
| **B346** |  | The deviation space's symplectic conjugation lambda->1/lambda is exactly its Z/3 charge conjugation at the symmetric centre, while the E6-exponent split {4,8}/{5,7,11} is an indepe… |
| **B351** |  | An exact integer Chevalley 𝔢₆ (Jacobi verified on all 76,076 triples, the forced Cartan-return sign isolated) yields the principal sl₂, exponents {1,4,5,7,8,11}, and θ with fixed 𝔣… |
| **B352** |  | At dps 100 the second-order cup-product obstruction [z u z] vanishes in all six E6 exponent directions, including the {4,8} escape sector and its polarization mix, so the quadratic… |
| **B353** |  | The hyperelliptic involution induces exactly the E6 diagram involution theta on the tangent space at the principal-geometric representation, verified as an operator identity with e… |
| **B356** |  | Every SL(2,ℂ)-factoring route forces a quaternionic self-dual 2 (det-lemma), and complex 27-dim assemblies with an invariant cubic exist only for A₄ and 2T — the chirality window i… |
| **B357** |  | All six E6 deformation classes restrict nontrivially to the cusp (rank 6/6), the image is Lagrangian, and one universal tau = the cusp shape governs every block. |
| **B359** |  | Exact seam readout: pair (1,3) is seam-dark and (2,3) carries an s-set disjoint from (1,2) — the theta-lift seam form is pair-specific and parity-selective. |
| **B361** |  | Across 8 pairs with zero counterexamples, a level-15 pair invariant carries √−15 exactly when it contains a seed elliptic at both 3 and 5 (m=2,7); the discriminator refutes H-min a… |
| **B362** |  | All three pre-registered seam predictions hit exactly, extending the doubly-elliptic-seed brightness law to 11 pairs with zero counterexamples. |
| **B363** |  | The seam is two-sided: Par-non-commutation is necessary, but all 225 one-sided twists and the one-slot theta lift are dark, so both slots need the theta class. |
| **B384** |  | The Kashaev ladder carries a nonzero sqrt5-component at every 5|N level tested (bet b passes, the valuation bet killed), the m=1 seed constant 1/4 transports exactly to level 45, a… |
| **B391** |  | At general N = 3^a 5^b the value sector exists iff a and b are not both even; both registered predictions (243, 625) hit. |
| **B393** |  | Dark pairs annihilate termwise rather than by cancellation, with the exact law: s-darkness holds iff the 5-side never donates sqrt5 to an imaginary product. |
| **B394** |  | Both registered walk rules died, and the reward is exact: singles take the form (1+c)/12 with support sum frozen at 1 across four levels. |
| **B402** |  | The single-object reality wall has two mechanisms split by seed (m=1 cell-wise local, m=2 aggregate-only), and seam intensity obeys f(gcd(address,15)) with the untwisted canonical … |
| **B410** |  | The coupling criterion separates 4/4 on the full-field product strata (bright iff some X₃·X₅ carries √−15), reducing the crown's why to the banked M1 stratification law. |
| **B412** |  | The single-seed tower is an exact mass-conserving refinement: each parent splits into a cyclotomic orbit summing to it, with trace-zero innovations (an Iwasawa-type measure). |
| **B415** |  | The tower measure's continuum limit is characterized as a Gauss-sum-modulated Haar measure on Z_3 x Z/5; the registered SM-emergence bar was not cleared. |
| **B416** |  | The trace-map flow's destination is exactly a golden-Anosov system (Lyapunov 4 log phi, one conserved kappa, modular symmetry); no SM structure, and the structure is generic. |
| **B417** |  | The object's symbolic face is the Sturmian subshift — complexity n+1, zero entropy, gap group ℤ+ℤφ — named quasicrystal math, SM bar not cleared. |
| **B423** |  | Closed form for the regularized E6 dynamical zeta as a Fibonacci-square product with the apparition-prime spectrum: figure-eight-specific arithmetic, not SM structure. |
| **B424** |  | Gate B's Hessian spectrum is exactly the per-exponent regularized torsions τ_m=(−5)^m∏F_{2j}² — golden to the last term, with no SM mass ratio within 2%. |
| **B425** |  | The geometric holonomy torsion is rational/Eisenstein (adjoint -3), a different object from B423's golden dynamical zeta (-5) — the object has two torsions. |
| **B426** |  | The seam-envelope ratio has the exact cubic closed form (3α²+4α−1)/10, and every Galois-invariant functional of its orbit is <1 — no invariant growth. |
| **B427** |  | Exchange of the two seam slots acts by the Galois element sigma_17, which fixes sqrt(-15); the projector-trace corollary is corrected to symmetrized/antisymmetrized sectors. |
| **B431** |  | The seam's boundary-torus support law confirmed exactly (120 active/120 dark, gated by y = 0 mod 3); two value-level readings corrected as artifacts. |
| **B433** |  | The DGG elimination for m004 returns exactly the Cooper-Long A-polynomial times its sign-twist, verifying Coulomb branch = SL(2) character variety. |
| **B435** |  | The (5,1) child has H₁ = ℤ/5 and exactly 25 = 5² nontrivial abelian E₆ vacua (26 including the trivial one), derived from the 75 Kac solutions modulo the free ℤ/3 centre action. |
| **B436** |  | The child's volume equals 12 times the Borel zeta expression for disc -283 to 64 digits; the '-283 equals figure-eight fingerprint' reading is corrected to a class property. |
| **B439** |  | The child's SL(2,C) vacuum quartic gives 4 irreducible vacua in the -283 trace field, with the unforced slope-7 control giving 6 vacua in a different field. |
| **B446** |  | Derived and out-of-sample verified the fixed-cofactor tower moment law N*Var = S5(m)*C3 (golden 3/8, silver 5/8); every channel launders to banked arithmetic. |
| **B448** |  | The exact T_1 periodic-orbit field tower on the cusp locus kappa=-2 (the Markov surface) gives Q(sqrt-3) at period 2 and Q(sqrt-7) at period 4, with a silver control confirming the… |
| **B449** |  | The disc×disc seam formula is category-confused (5₂ and 6₁ are not fibered), so ℚ(√−15) is restored as the forced compositum of the object's geometry and dynamics ends; the in-fami… |
| **B451** |  | The trace map's leading Ruelle resonance equals the escape rate gamma = 0.4415, certified by three independent estimators after the banked 0.51 was shown to be an early-window arti… |
| **B453** |  | Ethogram E1 (reproduction): the child is IDENTICAL, not merely sharing invariants -- a sharpening of the banked record, with one honest UNDECIDED. |
| **B454** |  | Closure lemma proved: every word trace of any SL(2) representation of ⟨a,b⟩ lies in ℤ[x,y,z], so at the object's seed the word channel can never leave ℚ(√−3), with the collapse ver… |
| **B459** |  | The dual-torus vanishing patterns are verified exactly (120/20/20/10/70, 5 of 16) and identified as the five-subfield lattice of ℚ(√5,√−3), with two new exact facts: no partial van… |
| **B460** |  | The child's length spectrum is tabulated and its per-vacuum Chern-Simons values computed by a two-gate-validated Kirk-Klassen integral matching banked and SnapPy controls. |
| **B463** |  | The centralizer of the principal sl2 in e6 is exactly zero, so the banked E6 route's 4d commutant is finite — no continuous gauge symmetry. |
| **B465** |  | The 8-4-3 monodromy spectrum is exact and fully derived from Fricke's tr(A1A2)=15 plus Egorov, and the SU(3)/SU(4) readings fail at the eigenspace level. |
| **B466** |  | Under sigma the SL(3) Dehn-filling components exchange while V0 is preserved with fixed line p=q; the whole sigma-story is the Gieseking deck action. |
| **B467** |  | Family, residue and wall converge on one Z/2 orientation bit: the CKM scan gives an earned zero and the only odd permutation is the orientation-reversing half-monodromy. |
| **B469** |  | Breath wave 1: the two-register residue equals (−1)^((N−1)/2) at four levels, and every metallic bundle double-covers a non-orientable bundle (X_m²=A_m). |
| **B470** |  | The reflection campaign closed: level-2 trace fields escalate per rung and escape level-1 laundering, while the quantized determinant mirrors the Pisano rhythm. |
| **B472** |  | The exact table tr[W₁ʲ,W₂ˡ] (three independent lifts agreeing) has magnitudes the divisors of 15 and κ_q(1,1)=−1≠κ_classical=−2, with [W₁²,W₂³]=I exactly, derived by CRT (Q₈ mod 3,… |
| **B474** |  | Seat-1's float-based 'zero dark at closure' claim is refuted and the exact 240-point tier-commutator table yields three exact selection-rule laws. |
| **B478** |  | The unexplained +j term is exactly a Heisenberg clock translation: Par·D(m,c)·Par = D(m,c)·Z^{cm}, trace-invisible but address-shifting. |
| **B479** |  | Theorem: the sigma_m-fixed cusp characters are exactly the order-d torsion characters for divisors d>=3 of m, with no non-elliptic components; field labels corrected. |
| **B482** |  | Verified the twisted-Markov handoff: the det -1 Markov spectrum below 3 is exactly {sqrt5, 2sqrt2}, and tr[A,B] = 2 - gap^2/(detA detB) generalizes P4's Lemma 2.2. |
| **B483** |  | The object's golden structure is a face of the Fibonacci-anyon TQFT (tau x tau = 1 + tau is the substitution's own golden recursion), while the 3:8:15 overlay is the forced arithme… |
| **B485** |  | Closed the metallic Alexander law Delta_m(a) = a^2 - (m^2+2)a + 1 for m=1..5 (the monodromy char poly), with genus 3 anchored at m=1. |
| **B488** |  | The metallic family's DGG data obeys two clean laws, gauge U(1)^(2m-1) and H1 = (Z/m)^2 + Z for m=1..8; SU(3) flavor enhancement applies only at m=1. |
| **B497** |  | End(F₂) on the character variety splits into four strata with exact κ-laws, plus two universal laws: κ=2 invariance and a toral classical shadow. |
| **B504** |  | delta_M = 2: at the pointer state (1,1,1), the unique irreducible M-fixed character, the intertwiner t exists and det-normalized satisfies tr(t)^2 = 2 exactly (SVD nullspace, resid… |
| **B508** |  | delta(s) = (s^2+s-1)/(s-1) along the evolution curve, verified OUT-OF-SAMPLE at never-sampled points s=3 and s=-2, with delta=0 exactly at the golden points {1/phi, -phi}. |
| **B513** |  | The three verbs have distinct exact boundary attractors: evolution conserves kappa=-2 (cusp), decoherence flows to 0 (pointer), decimation to 2 (abelian). |
| **B515** |  | Coupling two Fibonacci copies yields the unimodular quartic Pisot number beta=phi(1+sqrt(phi)), so a golden-field 3d Rauzy geometry is real and B514's kill was premature. |
| **B516** |  | Golden 3d self-reference is golden-specific (only phi keeps x->x(1+sqrt x) Pisot), while the 'three dimensions from a Pisot cap' reading is dead. |
| **B517** |  | Within Fibonacci-intertwining couplings the golden-3d bootstrap coupling is unique, (C,D)=(F,F^2), and that canonical coupling is Pisot only for the golden mean. |
| **B522** |  | A formal-slice/BCH filtration argument forces the Sym-tensor-det block form of char(rho_n) for all n and proves the catalog's first arm by Chevalley, reducing the tower conjecture … |
| **B524** |  | Phi is certified iwip with unequal forward and inverse dilatations, so F4-by-phi is word-hyperbolic but not a 3-manifold group; higher-rank Ptolemy keeps DGG gauge abelian. |
| **B527** |  | The Stein-compatible metrics form a 6-dimensional non-polyhedral cone 𝓛⁻¹(PSD(3)) with an ℝP² of extreme rays (7-dim Lorentzian family): compatibility holds, narrowing B526's no-go… |
| **B528** |  | T[4_1]'s 3d-3d gauge group is abelian U(1), computed from the Neumann-Zagier datum; the 'U(N-1) nonabelian generic gauge' reading is a structure-group conflation. |
| **B530** | ✔ | The four-letter object's own grammar is golden at three nested levels, its growth is a mirror plus a symplectic form, and its pure discrete spectrum is certified. |
| **B531** |  | Gap-opening slopes converge (0.1914, 0.1524, ratio 1.2565) and gap 3's period-2 alternation is explained by the negative contracting eigenvalue; closed forms remain open. |
| **B535** |  | One measured Perron number plus the object's own grammar determines the substitution uniquely up to conjugacy; the coupling census saturates at 6 Perron types. |
| **B537** |  | (1,1,5) is proved to be a phantom — not (tr A, tr B, tr AB) for any A,B ∈ SL(2,ℤ) — by Latimer–MacDuffee class-number-1 completeness plus elliptic and hyperbolic slot obstructions,… |
| **B538** |  | The first preregistered reframe test cycle confirms the E8 mass ladder and Fibonacci gap labels class-level with controls, while the SM structural checklist scores 0/3. |
| **B540** |  | The observer flow closes on 12 canonical systems with three fixed points and one ℤ/2 two-cycle, correcting B535's window-length-limited census. |
| **B542** |  | All 17 read-out components decompose exactly into two τ-ladders τ^a(τ−1)^b plus a π-fringe, making the catalog one self-similar unit-lattice object. |
| **B543** |  | The four-letter species chain's measured IDS gap labels reproduce the B535 degree-4 dictionary, 100-2500x off the golden lattice and invariant across coupling sets. |
| **B544** |  | Emergent golden order is verified (Sturmian ground states, Shenker's constant to nine digits) but the carrier holds only the Q(phi) shadow, not the degree-4 layer. |
| **B545** |  | c = 1 is proved the smallest ghost level and an elliptic-lock law replaces the refuted prereg conjecture that ghosts share c = 22's signature. |
| **B546** |  | Sturm-count IDS at N = 10^6 pins the twelve measured gap labels to the Q(sqrt(phi)) dictionary values at 4e-7 and extends the tau-ladder one rung below. |
| **B547** |  | (4,4,16) is a proved ghost and the first all-hyperbolic one, obstructed by an inert prime rather than elliptic rigidity — a second ghost mechanism. |
| **B552** |  | coker(I−M) ≅ ℤ/11 with primitive left generator χ=(1,3,6,7) is conserved by σ and transported unchanged along the observer flow, and it decouples from the double clock. |
| **B553** |  | Verified exact from seat-1's session: |det(A_m - I)| = m^2 (the metallic Weil level), the odd-Fibonacci Markoff cluster, and Z/11-charge-clock decoupling; two errors corrected and … |
| **B556** |  | ESTABLISHED exactly: T(M)=[[M,M],[M^2,M]] sends the golden Fibonacci matrix to the sigma_4 incidence matrix verbatim, and the field doubles at every verified rung (norm-sign + dete… |
| **B557** |  | ESTABLISHED exactly: the escalator's coupling rule (C,D)=(M,M^2) is FORCED at rung 1 and a CHOICE above it (B517 intertwining forces C=p(M)), plus the explicit 8-letter carrier sig… |
| **B560** |  | Chat-3's campaign cells verified and re-derived: localized Z/11 carriers, prefix-independent observer-flow graph, 253-point certified atlas, exact Z[tau] frequency module. |
| **B564** |  | The SL(3) phi-fixed locus contains no irreducible representation: phi-fixedness pins A to finite order, which forces the intertwiner to split block-diagonally. |
| **B583** |  | The meeting stays complex-chiral with no real form, vacuum Dehn-filling probes can never hear chirality, and the corrected interference obeys a quadrature theorem. |
| **B586** |  | The E6 level-2 stage also hears everything (tr_even = 0 exactly, tr_odd = +1) as on the golden stage, -1/phi is stage arithmetic that does not travel, and 4_1's invertibility makes… |
| **B589** |  | The three E₆₂ θ-odd pair amplitudes are exactly the ℤ/7 sine-kernel moduli times 14th-root phases {+3,−2,−1}, certified to 40+ digits. |
| **B590** |  | ESTABLISHED: the V3 blind deliverable (nine size-3 Phi-orbits on the 27, triple intersection 16^16^16 = 6, the singlet's orbit profile (1,16,16)) AND that R1's SEALED verdict was V… |
| **B594** |  | The E6 level-2 hearing law is state-independent and its diagonal coefficients equal minus the banked Z/7 sine-kernel closed forms. |
| **B598** |  | The Kashaev baseline is computed (growth = Vol/2pi, 1-loop constant 3^-1/4) and the exact six-block cusp table built, with the true longitude word corrected. |
| **B599** |  | A Θ-homogeneous pairing vanishes unless the number of θ-odd factors is even (C central, C²=1), subsuming seven banked results; the algebraic face was recomputed in-repo and matched… |
| **B603** |  | Weight purity of the Omega-null state v0 makes every bent state v_m*v0 weight-homogeneous of weight 2m and hence J-isotropic at every block, so all single-generator L1 contractions… |
| **B610** |  | Three universality splits computed: the R^2L bundle's odd trace is complex and zeta-6 phased, never conjugation-closed, and never leaves the unit circle. |
| **B622** |  | The silver RRLL bundle m136's exterior adjoint Reidemeister torsion is exactly -16 = 2-(phi^6+phi^-6), a second negative data point for the exterior sign law, with the fig-8 and si… |
| **B623** |  | The Weyl-Weil reciprocity reduction is proved (96/96) and the conductor identity det(h_w) = sign(w)det(A tensor w - I) derived; odd-kappa reciprocity stays open. |
| **B625** |  | The Deloup–Turaev evaluation matches exactly iff 3|κ (48/48 versus 0/96), correcting B623's parity framing and fixing a real coset-enumeration bug. |
| **B661** |  | The other seat's 'portal couplings' are exactly the SU(3)_2 quantum dimensions 1/D and phi/D — stage-fixed across four words, no new object. |
| **B673** |  | L106 closes: the generation sum rule is two-seat verified (provisional lifted) and all three slots of 27x27 couple under a graded sign rule. |
| **B689** |  | The figure-eight's weight-2 avatar exists only at level 15 = 3*5 (X_0(3) and X_0(5) both genus 0), so the two hands are irreducibly coupled. |
| **B690** |  | The being (3-adic) object nearly realizes its divided-power law (defect ≤2) while the hearing (5-adic) one does not at all — the hands are asymmetric. |
| **B745** |  | Independent cross-verification confirms both revivals, retracting B58's 'not numerically testable' headline and B225's vacuous 2-half kill. |
| **B761** |  | fiber_dim(n)=0 at every rank: each deformation direction is visible from the cusp torus, so the object has no private states. |
| **B767** |  | Two backlog gaps closed by all-level theorems (Binet: DGG rank 2n-1 for all n; Sym^d functoriality: the golden tower's spectral rank never climbs). |
| **B773** |  | The banked level-45 'pair-sector identically zero' wall was a projection artifact: the isolated theta-odd readout is 1/4, reproduced three independent ways. |
| **B774** |  | Of 174 banked negatives, 129 are structurally immune and all 12 load-bearing chord-blind walls harden at theta-odd level — zero overturns. |
| **B776** |  | B685's Habiro leg is corroborated from first principles: the symmetrized product is pure-3 through order 50 with no 5 or 7 in any denominator. |
| **B781** |  | m004 is uniquely selected over its V4-sharing sister m003 by monodromy trace 3 (golden phi^2) and torsion-free H1, closing the V4 residual. |
| **B787** | ✔ | Inversion (iota) is an independent 4th involution raising the torsor rank 3->4 unconditionally, de-welding time's arrow from the basepoint bit; all six doors MISS. |
| **B804** |  | m004's induced cusp spin structure is the bounding one for every spin structure (Arf = 0 by bordism), so its Dirac spectral type is determined but class-level, and leading-order Di… |
| **B852** |  | B451's transfer-operator instrument was structurally incapable of finding a phase transition: uniformly hyperbolic pressure is analytic (demonstrated, second differences 1e-9, doub… |
| **B870** |  | G7 CLOSED -- the central-extension lift obstruction, computed exactly: for the 2-generator 1-relator presentations (SnapPy; relators certified not-proper-powers, so Lyndon aspheric… |
| **B876** |  | THE DESCENT (the joint cell with the solo seat, their priority (a)): inside K1, the IMPOSED fused-chain Levi tower lands exactly (Cartan by iterated centralizers, 40 roots by joint… |
| **B878** |  | The cc3 Wave-1 harvest (branch audit/b775-braver-questions @ cd1447b6, NEVER merged -- integrate-don't-merge): B845's missing '43 eigenvalues to r = 13.5' dataset found and verifie… |
| **B879** |  | The cc3 selection-cochain harvest (packet sha256 e59df18a, 38 files, preserved verbatim; cc3's own reconciliation addendum CHECKED AND CONFIRMED accurate): six claims verified with… |
| **B880** |  | The module-level magic-square signature, computed on this build (the computational half of the M(O,C) identification; B882 is the bibliographic half): so(8) = derived(core) at dim … |
| **B881** |  | Descent stage 2 -- the SM-graded coset commutation table, scoped BEFORE running as the mediation skeleton (B867's S1 X/Y channels), NOT the Yukawa skeleton (that needs the 27 rep, … |
| **B889** |  | Masterplan W3 -- the CANONICAL across-breakings dictionary: the convention problem dissolves into B886's six Pi-blocks (three vacuum lines + three 8-blocks, Galois-permuted, no Lev… |
| **B890** |  | THE SEALED W6 OPENING CELL (prereg ea66fc34 sealed before compute, verified unbroken at banking) RETURNS DISTINCT IN ALL THREE FRAMES, against the disclosed prior: the two foreign … |
| **B891** |  | THE SEALED MATTER-EXTENSION CELL (prereg a08398c5, sealed before compute, verified unbroken) RETURNS DISTINCT IN ALL THREE FRAMES: the two foreign 16-subspaces' 12-piece profiles d… |
| **B895** |  | THE 27-SUITE CLOSED (the last Phase-0 debts): (1) z6c EXACT over Q -- the floor is dim 12, color = su(3) (dim 8, Cartan 2) with exact Casimir spectrum {0 x9, 4/9 x18} on the 27 and… |
| **B905** |  | W8 PAID -- the Kim-torsor literature gate (99-agent adversarially-verified panel, full-text greps of primary sources, report banked): (Q1, CLEAN NEGATIVE, high confidence) the Kim-… |
| **B938** |  | THE SIGN OF FULL FLIP -- NO SWAP, A COSET INVARIANT (blind): testing the level song against the wall pair's full 2-torsion {I, D2, D, D2D}, D ACTS AS THE IDENTITY ON THE COLORLESS … |
| **B943** |  | THE O3 GATE APPLIED RETROACTIVELY -- B922's priority sentence corrected. Review 40 found the asymmetry: B940's prereg invented the O3 gate (no priority word until the sweep reaches… |
| **B965** |  | THE LAW_MAP SCOPE AUDIT, commissioned by the owner after B964 to catch the error class no gate can see. METHOD, mechanical not editorial: for each of LAW_MAP's 165 claim rows, load… |
| **B968** |  | THE SM VERDICT CRYSTALLISED (owner directive, before the programme turns to cosmology, gravity and other unexplained phenomena). docs/THE_SM_VERDICT.md supersedes every scattered s… |
| **B970** |  | L134 WORKER CELL (banked in B978): the twelve exotic states per generation (27 = 16+10+1) given their quantum numbers under the cascade's Levi, plus the cascade's resolving power o… |
| **B973** |  | L135 SCOUT CELL (banked in B978): the frame, the floor and M12 are ALREADY DEFINED in the repo and the reconstruction runs in 1.5 seconds -- definitional archaeology plus validatio… |
| **B974** |  | PHASE A SYNTHESIS (MASTERPLAN v3), written for the banking seat and banked in B978: four leads scouted and worked -- L134 (B970), L132 (B971), L137 (B972), L135 (B973). Three of th… |
| **B976** |  | THE CASCADE RECOVERY -- eleven banked arcs the synthesis layer had forgotten. Prompted by the OWNER, who reported that work around B862 felt like the SM was almost clarified and th… |
| **B1014** |  | THE PROOF-FORM: THE DERIVATION THEOREM CLOSED, THE ANCHOR DOCTRINE LICENSED, THE CLAIM STATED ON ONE PAGE -- executing two owner decisions (approved and confirmed). (1) PROOF-AS-DE… |
| **B1015** |  | THE ANCHOR DECLARATION, SEALED (R11 STEP 0, BINDING ON EVERY FUTURE CROSSING): A1 = l, the dimensionful length unit (its SI realization a convention; no dimensionless number flows … |
| **B1016** |  | L150 CLOSED: SEPARATE -- THE VALUE LAYER HAS TWO INDEPENDENT CHANNELS, AND NOW WE KNOW WHICH LAW GOVERNS WHICH. Sealed 59f51572, declared prior SEPARATE, HELD, by two exact obstruc… |
| **B1020** |  | THE TWO ADMISSIBILITY LEDGERS -- what a crossing MAY compare, settled before any value is looked at: docs/KIND_TABLE.md (living), Part 1 the KIND TABLE (R5's table), Part 2 the RG … |
| **B1021** |  | THE CELL-9 RECEIPT: THE PARENT MAASS EIGENVALUE ENTERS MAIN AT 31 FIGURES, AND THE VALUE WALL'S NULL NOW STANDS ON TWO CERTIFIED EIGENVALUES. Receipt per the B922 pattern (the 89.7… |
| **B1022** |  | cc's PHASE 1 PUBLISHED UNDER THE HASH-FIRST PROTOCOL: the corpus's answer to the three-seat functor question, byte-identical to the digest sealed at 4b3cbfdc BEFORE any other seat'… |
| **B1023** |  | PHASE 2'S CONCESSIONS, V2: TWO DEFECTS FIXED, THEN TWO BLOCKERS ON THE FIX ITSELF -- CONCEDED AND PINNED OPEN, the second correction arriving from cc3 BEFORE the batch banked. ROUN… |
| **B1024** |  | L153 SEALED OUTCOME: SAME (deficit 2). The two torsor generators' 27-shadows GENERATE H^1(<tau>, T_ad[2]) = (Z/2)^2 -- conjugation -> class (0,1), reversal -> class (1,1), independ… |

---

## The three verified end-to-end

1. **B505** — `κ − 2 = 4λ²`: κ **is** the squared coupling of the *measured* quasicrystal chain;
   **κ = 2 ⟺ the free metal**. Restored by **B1027**, which reconciled it with B160's
   `κ = 2 + λ²` first (one identity, two conventions) and found a third route via B36 ∘ B148.
2. **B787** — inversion ι is an independent **fourth** involution; its claim line **overstates**
   its body, and its *"ARMED, NOT PROPAGATED"* relabeling trigger is on no surface.
3. **B530** — *"the object's first complete portrait"*, **83 KB, the largest arc in the corpus**.

## §B100–B199 — DISPOSITIONED (2026-08-11, B1037)

**The campaign's step 6, executed for the first time:** *"a band is DONE when its debt rows are
either **restored** or **explicitly declined with a reason**."* Bodies read, not claim lines.

> ### The finding: 37 rows are **27 arcs in 7 clusters** plus 10 standing alone — **17 statements owed, not 37.**
>
> The clusters are the **arcs' own** claim, not an editorial grouping: B122 says *"B121 and the
> W-identity are **one object**"*; B117 says the B111/B113 framing is *"**superseded**"*. **The
> debt number counts rows; the debt is laws.**

| cluster | rows | the one statement owed |
|---|---|---|
| **the tower** ✅ **RESTORED (B1038)** | B117 · B122 · B121 · B118 · (B111, B113 superseded) | `ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)` for the external `W = V⊕1`, its shape forced by a dimension surplus vanishing **iff n = 4**; the SL(2)-action is the **external `det = −1`** monodromy, inequivalent to Kostant's principal for all `n ≥ 3`, and the θ = −w₀ fixed-root sign is `(−1)^{h+1}` |
| **arithmeticity** | B125 · B147 · B137 · B193 · (**B123 retracted**) | arithmeticity selects **exactly two** metallic members — golden `ℚ(√−3)`, silver `ℚ(i)`, non-commensurable — and does **not** coincide with self-mirror: the chiral pair `RRL/RLL` (`ℚ(√−7)`) is fully arithmetic |
| **φ-fixed reducibility** ✅ **RESTORED (B1039)** | B141 · B142 | finite image ⟹ reducible tower, dense ⟹ irreducible; the φ-fixed principal point is `Q₈`, so `Sym^{n−1}` is reducible at **every** `SL(n), n ≥ 3` — a one-line Klein-4 proof, no search |
| **the collective** | B173 · B172 · B174 · B175 · B176 · B178 | the woven gap-label group is `ℤ + ℤα₁ + ℤα₂` with **rank = 1 + #distinct quadratic fields**; the character-variety face is the same statement — cusp-gluing is a continuum only on a measure-zero locus, a forced discrete fork everywhere else |
| **the metallic exponent** ✅ **RESTORED (B1039)** | B154 · B198 | the peripheral `k` in `[A,B] = ±µᵏ` is **order-determined, not rank-determined** — *"degree=rank" is a coincidence of the principal spectra*, and no closed form `k(o,m)` survives |
| **the open arrow** | B183 · B187 · B186 | `g_c = min_E γ(E)` = the inverse localization length is **zero** for the critical metallic chain — criticality is **maximal fragility**, not robustness — against a control protected at exactly `ln 4` |
| **isomonodromy** ✅ **RESTORED (B1040)** | B169 · B164 · B150 | the trace-map action on the Fricke variety **is** the N=2\* class-S S-duality mapping-class action (τ-modularity is a homonym), and its Painlevé-VI/Schlesinger partner **relocates** the firewall rather than crossing it |

> **The band, measured twice and both figures dated.** As at **B1038** (rows written by B1039
> and later removed before measuring, per §0's rule): **27** in the band, **221** corpus-wide.
> After B1039: **23** and **217** — *exactly the four rows retired, no drift*. Two clusters
> restored, **four rows, two laws**; three clusters remain in this band that this sandbox cannot
> close (arithmeticity needs SnapPy; the collective and the open arrow need heavy numerics), plus
> isomonodromy, whose dimension core is a finite integer check even though its Schlesinger flow
> is not.
>
> ### **RESTORING THE TWO SYMBOLIC CLUSTERS FOUND TWO DEFECTS IN THEM (B1039).**
> Chosen not by size but by **what this sandbox can honestly redo** — `snappy`, `cypari`,
> `cypari2`, `sage` and `flint` are all absent, so restoring on citation alone **would be**
> restoring from memory. Both laws survive; **both arrived carrying a defect a citation-level
> restoration would have propagated onto a curated surface.**
>
> - **B141 Item 3's slogan *"finite image ⟹ reducible tower"* is FALSE** as a general
>   implication. Falsified in-sandbox: **`SL(2,3)` is finite (order 24) and its `Sym²` is
>   IRREDUCIBLE** (algebra dim 9 = 3²). The bound is the **max irrep dimension** — 2 for `Q₈`,
>   3 for `SL(2,3)` — and the two groups sit on **opposite sides of it at exactly `n = 3`**, so
>   it is sharp. *B141's conclusion survives intact; only its stated mechanism was too strong.*
> - **B142's Klein-4 chain needs `A` semisimple** — spectrum `{1,−1,−1}` with a Jordan block at
>   −1 has det 1 and is not an involution. The hypothesis holds at a φ-fixed point, so the proof
>   is sound; it was never written down. **And B142's probe never verified its own lemma** — it
>   exhibited one commuting pair; the universally quantified statement is verified here first.
>
> **Neither defect was reachable by reading claim lines.** Both required recomputing the arc.

> **Dated, as always.** As at **B1039**: **23** in the band, **217** corpus-wide. After B1040: **20** and **214** — *exactly the three rows, no drift*. **Three clusters remain in this band, and none can be closed here:** arithmeticity (needs SnapPy), the collective (PSLQ gap-labelling at N = 4000–128000), the open arrow (Lyapunov exponents, many-body ED). Per `REPRESENTATION_TRIAGE`'s existing word they are **PENDING with the blocker named** — *"marking an arc PENDING does not discharge it; it records that we know"* — and coining a fourth disposition word would repeat the defect §0 files against this very ledger.
>
> ### **AND THE THIRD RESTORATION FOUND A TAG OVER A COMPUTATION THAT WAS NEVER DONE (B1040).**
> The isomonodromy cluster's numerical half is re-runnable here **because it ships with a
> control** — the Schlesinger drift **4.25×10⁻¹⁰** against a non-Schlesinger ODE at **1.63×10¹**.
> *The control is the evidence, not the drift:* RK4 at `h = 0.01` has `O(h⁴)` truncation, so the
> absolute smallness is what a correct integration of **anything** would give.
>
> - **B169's P1 is tagged `[exact]`**, but **no Picard lattice or homological action is computed
>   anywhere in the cluster** — the arcs compute an eigenvalue. The identification of `λ_m²` as the
>   dynamical degree is **Cantat–Loray's**, cited. The algebra does generalise, and is now verified
>   **symbolically in `m`** where the arcs did `m = 1,2,3`.
> - **B164's `6g−6+2n = 2 ⟹ (1,1), (0,4)` was an inline parenthetical** carried by citation; a
>   repo-wide search for `6g−6` returns **two hits, neither a computation**. Proved here — and
>   **explicitly not as a discovery**: `OPEN_LEADS`:209 already records the count as
>   *"classical-known … not a discovery"*. The corpus now **checks** what it had only cited.
> - **B169's two P3 checks pass `True` literally.** Its one formalisable sub-claim, scale-freeness,
>   is checked here for the first time; **the verdict stays POSTULATED regardless.**
>
> **The pattern across four restorations:** B1038 found nothing wrong; B1039 a false slogan and an
> unstated hypothesis; B1040 a mis-tagged claim, a citation standing in for a two-line proof, and
> two assertions that compute nothing. **Every one was invisible from the claim line.**

> ### **PENDING — TOOL-BLOCKED (3 clusters, 12 rows). The word is the triage's, deliberately.**
> `REPRESENTATION_TRIAGE.md` already defines **PENDING** as *"a real object result owed a row on a
> synthesis surface. **This is a debt**"*, and states that *"marking an arc PENDING does **not**
> discharge it. It records that we know."* **That is exactly a tool-blocked restoration**, so the
> blocker goes in the note and not in a new label — **coining a fourth disposition word here would
> repeat the defect §0 files against this very ledger** (a second register beside a working one).
>
> **These rows are NOT added to `REPRESENTATION_TRIAGE.md`**, and that is deliberate too: its scope
> is the `claim_one_line ≥ 500` bar, and **§0 measured that no pre-B800 arc can ever clear it.**
> Borrowing its word is right; borrowing its table would import the blindness §0 documented.
>
> | cluster | rows | blocker, named |
> |---|---|---|
> | **arithmeticity** | B147 · B137 · B193 | **`snappy` absent** — the Maclachlan–Reid conditions, the `ℚ(√−7)` trace field and the integer Bianchi ratio are all SnapPy/PARI computations. `cypari`, `cypari2`, `sage` and `flint` are absent too; verified directly, not assumed |
> | **the collective** | B173 · B172 · B174 · B175 · B176 · B178 | **heavy numerics** — PSLQ gap-labelling against spectra at `N = 4000–128000`. Reachable in principle here, not in a pass |
> | **the open arrow** | B183 · B187 · B186 | **heavy numerics** — Lyapunov exponents and many-body exact diagonalisation |
>
> **The honest form of the campaign's step 6 for these:** a band is done when its rows are
> *restored* or *explicitly declined with a reason*. These are neither — they are **owed, with the
> reason they are not yet paid**. Recording that is not the same as paying it.

**DECLINE — PROCESS (4, firmly correct to omit):** **B100** (*"Nothing here is our discovery; the
methods are **cited**"* — a literature cross-check), **B113** (framing superseded by B117),
**B178** (*"standard nearly-free / KAM perturbation theory"* — the contribution is articulation),
**B106** (its own headline is an honest negative: *"**no mechanism is claimed**"*).

**DECLINE — SUBSUMED (4, zero marginal value):** **B187** ⊂ B183 · **B172** ⊂ B173 ·
**B176** ⊂ B175/B178 · **B111** ⊂ B117.

> ### **DECLINE — RETRACTION, NOT RESTORATION: B123.**
> Its headline — *"the m ≥ 2 metallic manifolds are **not** arithmetic"*, offered as *"a third
> independent selection criterion"* — is **refuted by B125**, which states in its own body that
> *"the 'three independent `m=1` selection criteria' sub-claim is **retracted**"*. The error was
> applying Reid's **knot** theorem to **bundles**. **Restoring B123 as written would restore a
> refuted claim** — the one outcome a consolidation pass must never produce.

> **A measurement note this band forced, recorded because it cost a broken lock.** Acting on a
> disposition **changes the count the disposition was measured against**: B1038's restoration cited
> B117/B122/B121/B118 on `LAW_MAP` and retired them, so this section's **37** stopped holding the
> moment it was acted on — breaking a lock that had passed. **The figure published here is "the
> band as it stood at B1037"**, measured with rows written by **B1037 and later** excluded. The
> exclusion deliberately does **not** reach back to B1024–B1036: those arcs retired B148 and B180
> by ordinary consolidation *before* this band was measured, and rewinding past them would
> over-count the debt at 39. **Tenth instance of one hazard, and the first to break a
> previously-passing lock in another arc.**

**RESTORED SO FAR — 1 of 7.** **The tower** landed on `LAW_MAP` as **B1038**, re-verified
symbolically first (the surplus's unique rank-zero; the *functorial* `Sym^a(V⊕1)` step that makes
it a module identity rather than a character coincidence; the assembly's exact `n²−1`; `det Sym^d`
against explicit matrices; and a two-route control on the instrument itself). **Six rows retired by
one statement.** What B1038 carries by citation rather than recomputing — B103's tower construction,
B118's Bourbaki fixed-root computation — is **named in the row**, and B122's scope travels verbatim:
character level `n = 2..11`, module level proved only at `n = 3,4`.

**RESTORE — the remaining six cluster statements, plus the standalone HIGHs** (B101's *Lorentzian at
exactly `k = 2` and never again*; B109's void saddle; B158's `(p−2)(q−2) = −2(m+1)`; B191's
`dim = Σcusps − 2·gluings`). **Each restoration re-verifies before it restores** (campaign step 5,
the B1010/B1026/B1029 pattern) and banks as its own arc. **Not done here** — this pass
*dispositions*; restoring is the next band's work and is scoped per cluster.

**The honest arithmetic on the number:** 4 rows firmly correct-to-omit and 4 with no marginal
value is **≈22 %** overstatement per row — but the structural overstatement is far larger. **The
band's real debt is ~17 statements against 37 rows.** *If that ratio holds across the corpus, the
231-row figure is a row count, not a work estimate, and the ledger says so here rather than
letting the number stand alone.*

## Dispositions — the rest

**None applied yet.** Read-first. Four restorations were banked this pass, each re-verified before
restoring (campaign step 5): **B1026** (the involution chain), **B1024** (L153, SAME/deficit 2),
**B1027** (κ's transfer-matrix and spectral faces), **B1025** (the suite).


## §B300–B499 — **MAPPED, not dispositioned** (2026-08-11, B1045)

**69 debt rows** — the heaviest stretch in the corpus, and the one the campaign's own diagnosis
calls least consolidated. **This section is a MAP, and the distinction is load-bearing.**

B1037 dispositioned B100–B199 **by reading the bodies**. What follows is **keyword-seeded from
claim lines**, which campaign **step 1 forbids** as a basis for disposition — *"read the bodies,
not the claim lines"*. Published as what it is: **the next pass's starting point, with its error
rate attached.**

| candidate cluster | rows |
|---|---|
| **E₆ selection & grading** | B301 · B305 · B306 · B311 · B312 · B321 · B323 · B327 · B337 · B351 · B352 · B353 · B357 · B463 |
| **the seam / level-15 (√−15)** | B359 · B361 · B362 · B363 · B393 · B402 · B410 · B426 · B427 · B431 · B449 · B459 · B474 · B478 |
| **generations / the deviation space** | B324 · B343 · B344 · **B345** · **B346** · B467 |
| **the (5,1) child** | **B435** · B436 · B439 · B453 · B460 |
| **value / tower measure** | B384 · B391 · B394 · B412 · B415 · B446 |
| **zeta / torsion** | **B423** · B424 · B425 · B451 · B479 |
| **metallic family laws** | B433 · B465 · B469 · B470 · B482 · B488 *(B485 consolidated by B1045)* |
| **standalone** | B304 · B315 · **B316** · B318 · B319 · B338 · B356 · B448 · B454 · B466 · B472 · B483 |

> ### The map's error rate is **5 of 58 (9 %)** — and **two** of the five are arcs whose claim line **explicitly denies** the cluster the keywords filed them under.
>
> **B345** ends *"**independent of** the E6-exponent grading"* and was filed under E₆.
> **B316** says √−7 is *"**NOT** a metallic-ladder member"* and was filed under metallic laws.
> *(**B346** merely **contrasts** with E₆ rather than denying it — an earlier draft counted it as a third denial and the arc's own check corrected that.)* **B423**'s statement is a zeta closed form, not an E₆ fact;
> **B435** is the child's homology.
>
> **That is step 1's argument made concrete:** a claim line's *keywords* can be exactly the words
> an arc uses to say **what it is not**. The five are corrected in the table above (bold), and the
> other 53 assignments are **unverified** — they are hypotheses until a body is read.

**One row is already consolidated.** **B485** — *"the metallic Alexander law
`Δ_m(a) = a² − (m²+2)a + 1`"* — is **B1040's metallic degree in another vocabulary**: the
characteristic polynomial of `M_m²`, whose root is `λ_m²`, verified identical. **No `law-siblings`
fingerprint reached it**, which is that instrument's first measured miss; the fingerprint is
widened, the gate now fires, and the limitation is stated in `LAW_SIBLINGS.md` rather than left to
be rediscovered.

### §B300–B499 — **THE FIRST CLUSTER DISPOSITIONED** (2026-08-12, B1047): the seam / level-15 campaign

**B1045 mapped this band and refused to disposition it**, because the map is keyword-seeded from
**claim lines** and campaign step 1 forbids exactly that as a basis. **B1047 read the bodies of the
largest candidate cluster — the seam / level-15 (√−15) campaign, 14 rows — and dispositions it.**

> ### The dominant finding is not a law. It is that **this cluster's claim lines systematically overstate their own bodies**, in the one direction a consolidation pass cannot survive.

| arc | its `claim_one_line` | its **own body**, same file |
|---|---|---|
| **B359** | *"the theta-lift seam form is pair-specific and **parity-selective**"* | *"A parity selection rule (**OBSERVED PATTERN, not claimed as law**) — **3 data points**"* — and **B360 refuted both readings the very next arc**, verdict NEGATIVE |
| **B361** | *"Across **8 pairs with zero counterexamples** … carries √−15 exactly when it contains a seed elliptic at both 3 and 5"* | *"stated as **a law of the computed range, not proved**"* |
| **B362** | *"extending the doubly-elliptic-seed brightness law to **11 pairs** with zero counterexamples"* | true as stated — but it names the law **B367 kills on the twelfth pair** |

**The bodies were honest at the site every time. The claim lines dropped the tier.** A claim-line
ledger cannot see this band; that is step 1's argument, made concrete a second time.

> ### **DECLINE — RETRACTION, NOT RESTORATION: B359 · B361 · B362.** The B123 pattern, three more instances.
> **B367** — *"the local law (B361) is **REFUTED** at pair (3,4) … **fails on the twelfth pair**"* —
> declares `supersedes: B361`. (3,4) contains **no doubly-elliptic seed** yet is **bright**, with
> the second-largest aggregate `Σs² = 1/192`; and the minimal repair (*"each prime covered by some
> seed"*) dies in the same table, because **(1,3) has the identical covering pattern and is exactly
> dark**. **Restoring these headlines would restore refuted claims.**
>
> **What the retraction does NOT take: the DATA.** B367's own words — *"its **11 confirming pairs
> stand as data**"* — and B359's tables were **superseded by a better table** (B367's full exact
> identification), not refuted. **The declined rows lose their headline, not their arithmetic.**

**RESTORE — B393 · B410, as their OWN `LAW_MAP` row** (*"THE SEAM'S DARKNESS IS TERMWISE
ANNIHILATION, NOT CANCELLATION"*): **s-darkness ⟺ the 5-side never donates √5 to an imaginary
product**, every term individually zero, the dark class itself stratified, and B410's independent
criterion separating **4/4**. **Re-verified before restoring** (campaign step 5): `product_fields.py`
re-run end-to-end in **2m41s**, output **byte-identical** to the banked artifact, and the
refutation's local arithmetic redone from integers. **Four riders travel** — computed range, the
per-side `Π_H` erratum (with `k1_termwise.json` a **negative artifact**), the open residual, and
theta-lift / L57 / firewalled.

**NOT folded onto B1029's `THE SEAM IS THE ENDS' CLASS FIELD` row**, which an earlier draft of this
disposition assumed. Tested: **B393 and B410 mention class field / Hilbert / HCF / B334 exactly
zero times**, and B1029's row mentions neither theta nor darkness. **They share the field `√−15` as
vocabulary, not as statement** — the 9 % error B1045 measured, nearly repeated by the arc that
measured it.

**The band's arithmetic, dated and scoped.** 14 rows mapped to this cluster at B1045; **5
dispositioned here** (B393, B410 restored; B359, B361, B362 declined) — **9 remain**, and they are
**not** declined by silence: B363 · B402 · B426 · B427 · B431 · B449 · B459 · B474 · B478 are
**owed, un-read**, with B408's trap (`SUPERSESSIONS.md` §B) sitting inside the same campaign.
Measured with **B1047 and later excluded** (E37).


> **The corpus figure, and the lock it broke.** Uncited **substantive** PROVED arcs: **204 → 199**,
> against **50** uncited instrument arcs and **634** PROVED arcs in all. **The five retired are
> exactly the five dispositioned** — set-differenced, not subtracted: `B359 · B361 · B362 · B393 ·
> B410`, nothing else moved.
>
> **And that is worth one sentence, because two of those five were DECLINED, not restored.** Naming
> an arc on a curated surface *as refuted* retires it from this count, since the sweep asks
> **"is it cited?"** and not **"is it endorsed?"**. That is the right answer for campaign step 6 —
> *"restored **or explicitly declined with a reason**"* — but it means **the raw debt number cannot
> tell a restoration from a retraction**, and a reader watching only the number would see B359,
> B361 and B362 *"consolidated"*. The dispositions above are where that distinction lives.
>
> **Crossing 200 broke
> `tests/test_consolidation_coverage.py`**, which asserted the absolute band `200 < sub < 280`.
> **That is `E38` (progress-eroded threshold), second instance — a lock that fails because the work
> succeeded** — and the sharper one, because unlike B1033's it was **not** written by this refresh
> and nothing in its prose anticipated it. Repaired as B1033's was: the lower bound is now the
> **share** (uncited-substantive / PROVED, band 0.10–0.45, currently **0.314**); the upper bound
> stays a raw guard, because *that* direction would mean the citation regex stopped matching.
> **The general rule now stated in `ERROR_LEDGER`: any lock whose number the programme is trying to
> move is an E38 waiting for the programme to work.**

### §B300–B499 — **THE SEAM CLUSTER IS CLOSED** (2026-08-12, B1048): the other nine rows

B1047 dispositioned five of the cluster's fourteen. **These are the nine, and the headline is not
the seam.**

> ### The survivor sitting beside the corpus's worst trap is a **THEOREM**, and no curated surface carried it.
>
> **B408** — registered at B1046 as the worst case in the corpus — opens *"THE SEAM DOES NOT
> CONTRACT — the one scale lever stands"* (a registered retracted phrase) over a `NEGATIVE`
> verdict, and its own correction kills it 27 lines
> down. **B426 is the arc that upgrades that correction from a diagnosis to a THEOREM.** Stated
> precisely, because the loose version is false: **B1046's registry DOES name B426** — its B408 row
> says *"B426 upgrades the correction to a theorem — survivor and trap sit side by side"*. **What
> was missing is not the name but the LAW.** Measured with this arc's rows excluded: **B426 appears
> on none of the five curated surfaces.** A reader of the consolidations met the trap and nothing
> that answered it.

**RESTORE — three rows on `LAW_MAP`, each re-verified before restoring (campaign step 5):**

| row | rows retired | the statement |
|---|---|---|
| **THE SCALE WALL CLOSES AT THE LEVEL OF GALOIS THEORY** | **B426** | the ratio's minimal polynomial `1000x³−1500x²+360x−19` in `ℚ(ζ₉)⁺`, `√5`-free; the three "embeddings" are **three Galois conjugates of one number**; `mean = 1/2`, `RMS = √51/10`, `geo = (19/1000)^⅓` — all exact, all below 1 |
| **THE SEAM FIELD IS FORCED, AND ITS LEVEL IS A CONDUCTOR** | **B449 · B427** | 5₂ and 6₁ are **not fibered** (Alexander leading coefficient 2), so the disc×disc reading names nothing for them; for a fibered knot Alexander **is** the monodromy char poly, and level 15 is the **conductor** of `ℚ(√−3,√5)`. The exchange is `σ₁₇`, which **fixes `√−15`** |
| **THE SEAM IS AN ADDRESS PROPERTY** | **B363 · B402 · B478** | necessity (`Par`-non-commutation, and the seam is **two-sided**: 225/225 one-sided twists dark), intensity (`f(gcd(address,15)) = {1:44, 3:32, 5:36, 15:0}`, the canonical point the **unique** dark address), and the shift (`Par·D·Par = D·Z^{cm}`, trace-invisible, address-visible) |

> **B426's own slogan is over-broad and is corrected before restoring.** It writes *"every
> Galois-invariant functional of the orbit is < 1"*. **`e₁ = 3/2 > 1`, and the sixth power mean is
> `1.0134 > 1`.** The exact boundary, computed in the arc: **the power-mean family contracts for
> every `p` below `p* = 5.5932…`** and exceeds 1 only as it degenerates toward `max` — *precisely
> the embedding bias B408's own correction named*. **The wall is not weakened; it is given its
> boundary**, and the defensible form is *"every genuine AVERAGE contracts"*.

**DECLINE — three rows, each on the arc's own words:**

- **B459 — DECLINE, ITS OWN ADDENDUM WITHDRAWS THE HEADLINE, TWICE.** *"The selection structure is
  the **QR-class's at level 15, not the object's**"* (the address axis, an independent control),
  and *"every pair has its own table … which corrects **THIS record's own overreach** — B459's
  'one uniform law, 240/240' was itself (1,2)-specific"* (the seed-pair axis). **An `E34`
  apparatus-inflation shape, caught by the arc itself.** Restoring the *"5 of 16"* headline would
  restore an object-level claim its author withdrew. *(Its registry row at `LAW_SIBLINGS.md` said
  SAME-LAW — OWED; reading the addendum resolves it to DECLINE.)*
- **B431 — DECLINE, CLAIM-LINE GAP AND A PAIR-SPECIFIC TABLE.** Its claim line names **one** gating
  line (`y ≡ 0 mod 3`); the body has **two** (`x ≡ 0 mod 10` as well), plus two value-level
  corrections. **Fifth instance of the gap this cluster keeps producing.** And B459's controls make
  the table the **(1,2) pair's**, not the object's.
- **B474 — DECLINE, ITS OWN WORDS: the correspondence "demands a mechanism".** The (j,l)↔(x,y)
  identification *"is nominal"*, the candidate explanation is CRT-laundering, and *"derivation =
  the next wave"*. **What stands is the float-kill — the seventh — and a float-kill is process.**

**The cluster, closed — and the arithmetic is stated because the first draft of this line got it
wrong.** **14 rows = 8 RESTORED** (B393 · B410 at B1047; B426 · B449 · B427 · B363 · B402 · B478
here) **+ 3 DECLINED — RETRACTION** (B359 · B361 · B362, B1047) **+ 3 DECLINED** (B459 · B431 ·
B474, here). Campaign step 6 satisfied for the whole cluster — *"restored or explicitly declined
with a reason"*. Measured with **B1048 and later excluded** (E37).


### §B0–B99 — DISPOSITIONED (2026-08-12, B1050 · B1051)

**The band the owner's instruction put first, and the last one whose bodies were already read.**
16 live rows (19 at the v3 baseline; B33, B75, B77 retired by B1044's sibling citations).

> ### The finding: **six of the sixteen are one wall, found six times over.**
>
> **B19 · B21 · B28 · B30 · B34 · B35** each establish a different half of a single fact — the
> projective / central-sign quotient is **legitimate** (B28), **canonical** (B30), **Poisson-natural**
> (B34), **symplectic** with the half-step anti-Poisson (B21), **topologically explained** (B35), and
> its generator **pinned to exactly `±P`** (B19). **Every one carries the verdict `STALLED`**, because
> none of it derives the selector. **Restored as ONE `LAW_MAP` row, graded `WALL`** — the campaign's
> own class for a proved impossibility — with each arc's `STALLED` carried visibly.
>
> **Scope, and it travels or the row misleads:** the wall is *"does not **derive** the selector"*, not
> *"no selector **exists**"*. And **B21's negative is a different wall** — *"the physical **spacetime**
> dictionary does not [exist]"* — kept separate rather than merged.

**A near-miss corrected before it inverted the disposition.** Every early arc opens *"Logged
observation, not a claim (`GOVERNANCE.md` §5)"*. A first read took that as **self-declination** and
would have declined eleven rows on it. **It is a firewall header, not a verdict** — B55 carries that
line *and* a `PRODUCES-PROOF-MODULE` block reading *"settled for **all** m"*. **"Not a claim" means
"nothing promotes to `CLAIMS.md`", not "no result."** The verdict token is the signal; the header is
boilerplate. *Same shape as `E6` — matching a string instead of reading the structure it sits in.*

**And the metadata disagrees with the bodies.** All six of the wall's arcs carry `verdict: PROVED`
while their bodies read `STALLED`. **Measured, and the first number was too loose: 14 arcs are in
genuine contradiction** — 12 reading `STALLED`, 2 reading `NEEDS_VALIDATION` — **and all 14 are in
this band.** *A first pass counted 24 by lumping in `PRODUCES-PROOF-MODULE`, `RESOLVED`, `PROVES`
and `CONFIRMED`, which are an older POSITIVE vocabulary and not disagreements at all; two more were
regex artifacts from arcs with no verdict block.* **Six of the 14 are already cited on curated
surfaces — B13, B14, B16, B18 by B1026 and B33 by B1044, both this refresh's own restorations.**
That does not make those rows wrong (B1026 graded itself STRUCTURAL and carried B62's grade
unchanged), but **a reader tracing B16 from `LAW_MAP` meets `verdict: PROVED` over a body that says
`STALLED`, and no row says so.** **Registered as `L166`; no gate built** (two landed in
the last two phases; a third would be the `E34` apparatus-inflation this refresh already recorded
against itself), and **repairing the metadata would change what every downstream sweep counts —
including this ledger's own `PROVED` filter — which makes it an owner call.**
