# REVIVABLE — the revivable-kill frontier

> **GENERATED FILE — do not hand-edit.** Regenerate with
> `python3 scripts/revivable/build_revivable.py`; verify with `--check`.
> Source: `frontier/B738_pathfinder_compiler/kill_graph.json`,
> **sha256 `b424c68d1afc4fc0f817648ed4bf54ea375b4b2b8aa8125e505af6a290d388b4`** (algorithm: SHA-256 over the raw file bytes),
> read from **origin/main**.

> ⚠︎ **Source versions disagree.** working tree graph has 217 entries; origin/main has 741. Generated from: origin/main.
> An index built from a stale graph is confidently wrong, which is the
> failure this file exists to prevent — so the discrepancy is printed
> rather than resolved silently.

**What this is.** The kill graph records, for many killed claims, an
explicit route back — a `hatch` naming the escape and a `revival_score`
(0–6) rating it. That is a lead structure, and no register indexed it, so
"what are the most revivable kills?" could not be asked of any ledger.
This file is that index. It asserts nothing new: every row is the kill
graph's own annotation, re-presented so it can be queried and ranked.

**How to read a row.** `killed` is what was refuted. `hatch` is the route
the graph says could still work. `score` is the graph's own rating of that
route. `registers` is which ledgers name the id at all — **blank means the
item is invisible to every register**, which is the reason this file exists.

## Summary

| | count |
|---|---|
| entries in the kill graph | 741 |
| with a named hatch **and** a revival score | **135** |
| — of those, hatch is a short route name | 132 |
| — of those, hatch is a full prose paragraph | 3 |
| scoring ≥ 4 | 28 |
| **named in no register** | **35** |
| `UNTRIAGED` (no hatch, no score, never assessed) | **167** |

The `UNTRIAGED` 167 are the honest limit of this index: they
carry no hatch and no score, so they are not ranked here. Until they are
triaged, this file describes the assessed portion of the graph, not the graph.

## Score ≥ 4 — the front of the queue

Ranked by score, then by whether any register names them (unregistered first — those are the ones nothing else will surface).

| id | score | hatch | registers | claim killed |
|---|---|---|---|---|
| **B500** | 6 | `deepen-past-plateau` | — | 'The child (x⁴−x−1, d_K=−283) is a short word': COMPLETE at depth 4 (all 36 three-verb words solved exact, airlock never fired); PROVISIONAL at depth 5 — 115/150 words analyzed with 0 hits, but 35/150 (23%) UNCHECKED (26 bare timeouts logged pre-analysis + 9 never reached), per the B525 audit corre… |
| **B111** | 5 | `nonlinear-transport` | — | The s_n↔c bridge: the tower's sign character s_n carrying the peripheral scalar c. Killed: s_n ∈ {±1} (order ≤2) cannot equal the order-4 secondary c=i — the same parity/order obstruction that killed θ→c (B108). Secondary tested-negative: the k=ord−1 exponent formula fails the all-four hinge. |
| **B477** | 5 | `deepen-past-plateau` | — | The candidate universal linear sterility law (sterile obstruction class = fertile class with one Z/2 sign-flip, a coset in H^2(M,∂M;Z/2)) — refuted as universal by s776's count (3 fertile classes, not a power of 2). |
| **B712** | 5 | `native-continuous-channel` | — | That the object's own continuum (the A-polynomial deformation curve, its one continuous modulus) carries a canonical non-degenerate real anchor for a real parameter. Killed: the canonical complete-structure point has imaginary-quadratic cusp shape tau=+/-2sqrt(-3) (no real embedding); the only both… |
| **B183** | 5 | `native-continuous-channel` | LEAD_REGISTER | Opening the metallic collective self-generates an arrow with an intrinsic scale: refuted -- a genuine non-unitary arrow appears but is thresholdless (g_c~0 from criticality), dimensionless, and externally sourced (the imaginary gauge field is input). |
| **B252** | 5 | `nonlinear-transport` | HINT_LEDGER | The object carries an intrinsic complex-conjugation-odd (chiral / CP-odd) invariant that could prefer 27 over 27-bar (i.e. the object sources matter). |
| **B399** | 5 | `native-continuous-channel` | OPEN_LEADS, LEAD_REGISTER, CAMPAIGN_STATUS | That the singles tower generates a SCALE: both 1215-rung candidates (CAND-FIX 12 cells / CAND-DEG 36 cells) killed (actual: 24 cells, 45-residue frozen), and W-A closes with 'the tower is a RESOLUTION generator, not a scale generator' — monotone contraction, every value in [−1/12, 1/4], total froze… |
| **B401** | 5 | `deepen-past-plateau` | HINT_LEDGER, CAMPAIGN_STATUS | The registered class-sorting bet 'seam-channel primes are non-principal-or-ramified in ℚ(√−15)' — killed by 7 (inert) sitting in the bright (3,4) Gram spectrum. |
| **B433** | 5 | `route-through-atom` | CAMPAIGN_STATUS | The 3d-3d route yields physics in-sandbox: internal units/scale and the E6 assembly T[4_1,E6]. The SL(2) calibration itself SUCCEEDED (Coulomb branch = character variety, exact, two independent routes); the death is that scale enters only via external embedding (R/CY) and the E6 assembly is the pri… |
| **B685** | 5 | `recompute-cited` | OPEN_LEADS, OPEN_PROBLEMS, HINT_LEDGER, CAMPAIGN_STATUS | The W3 sole survivor's last realization, and with it the whole generation leg: a framework-derivable generator produces the {2/5, 3/5} 5-adic flavor streams. KILLED-AT-SUPPORT: Route B had ASSUMED the Nahm datum A=2 (the (2,5)/golden Lee-Yang system), contradicting the geometry (disc -3, pure being… |
| **B374** | 4 | `deepen-past-plateau` | — | Three serial tower laws: the pinned-exponent law (killed at N=135), the pentagon-pair phase law {36°,108°} (killed at N=75: phase 90°, trace 0), and the sector-EXISTENCE law itself (killed at N=225: no invariant sector at the first mixed m=15). |
| **B394** | 4 | `infinite-tower` | — | The naive CRT support-walk rule for the singles tower (both registered candidates for the level-405 support — 59 and 86 mod 135 — killed: actual support a≡31 mod 45, twelve cells). |
| **B706** | 4 | `native-continuous-channel` | — | That the SM flavor freedom matches the object's structure: rung 1 (SM ratios algebraic over Q(sqrt5)) -- no low-height PSLQ relation, generic; rung 2 (SM freedom organizes as the F2-seam) -- KIND mismatch: discrete orientation bits vs ~19-26 continuous real parameters. The Cabibbo 9/40 candidate ki… |
| **B107** | 4 | `native-continuous-channel` | OPEN_LEADS, HINT_LEDGER, LEAD_REGISTER | The metallic/SL(n) tower eigenvalues as a spectrum of new physics (masses / operator anomalous dimensions; torsion=masses). Killed twice over: (B) every Fibonacci tower eigenvalue is ±φ^k — one geometric scale log φ, re-presented moduli-space monodromy, not a fluctuation spectrum; (C) category erro… |
| **B166** | 4 | `native-continuous-channel` | OPEN_LEADS | That the higher-rank metallic system is a quantum (self-adjoint) operator inheriting SL(2)'s Cantor spectrum. Killed structurally: SL(n≥3) ≠ Sp — a self-adjoint 1D operator's transfer matrices preserve the Wronskian symplectic form, so SL(n≥3) is not the transfer group of ANY self-adjoint operator … |
| **B191** | 4 | `enumerate-landing-sites` | OPEN_LEADS | Chaining N>=3 units through connectors converges to a forced-unique selection: refuted -- the kappa-selection nests through a coupling 2-cusp connector but stays discrete-and-proliferating (fork grows with connector complexity: T:9, T^2:10, S:16, ST:32; never collapses to 1). |
| **B225** | 4 | `route-through-atom` | OPEN_LEADS, LEAD_REGISTER, CAMPAIGN_STATUS | Conductor 40 = (octahedral parent 2) x (golden filling 5): the '2 = octahedral parent' half (the '5 = golden filling' half HOLDS, exact). |
| **B307** | 4 | `infinite-tower` | OPEN_PROBLEMS, HINT_LEDGER, CAMPAIGN_STATUS | 'Three symmetric generations from a single knot's cyclic-cubic (C3) trace field' -- theorem: C3 fields are totally real, hyperbolic invariant trace fields always have a complex place; the two are disjoint, so NO hyperbolic knot has a C3 trace field. |
| **B367** | 4 | `route-through-atom` | OPEN_LEADS | The seam value map s(m1,m2) is a function of CRT-local data at level 15 (uniform local-symbol product formula at declared complexity); plus the B361 local law |
| **B372** | 4 | `infinite-tower` | OPEN_LEADS, HINT_LEDGER, LEAD_REGISTER | The seam is a level-15 accident (prereg null: the sqrt(-15) content does not persist at level 45) |
| **B385** | 4 | `deepen-past-plateau` | HINT_LEDGER | That the bright/dark discriminator is cheap: γ-group-theoretic (kill 1: identical invariant profiles) or word-grid-statistical (kill 2: identical det-class distributions on the riddle pair); plus the translation-kill criterion draft (voided by its registered 12/12 failure, built on the Π_H/DFT comm… |
| **B412** | 4 | `infinite-tower` | HINT_LEDGER, LEAD_REGISTER | The single-seed tower is a value hierarchy / runs a scale. Killed and reframed: the tower is a mass-conserving refining MEASURE (Iwasawa-type p-adic distribution on lim Z/3^k x Z/5) — mass 1 at every level, cyclotomic-orbit splits, trace-zero innovations. |
| **B428** | 4 | `enumerate-landing-sites` | OPEN_LEADS, CAMPAIGN_STATUS | Fermionic content upstairs: (Wall 1) the E6 level-1 27 carries fermions — killed, no theta=-1 object at level 1 or 2 (Z/3 Eisenstein anyons only); (Wall 2) the principal sl2 bridge gives spinorial matter — killed, all blocks odd-dimensional/bosonic (27 = [17,9,1]); addendum: 'three folds = three ge… |
| **B515** | 4 | `deepen-past-plateau` | CAMPAIGN_STATUS | B514's premature kill 'golden can only inflate 1d — golden 3d is degree-dimension impossible' — KILLED BY COUNTEREXAMPLE: beta = phi(1+√phi), the unique unimodular quartic Pisot golden inflation from coupling two Fibonacci copies (min poly x⁴−2x³−5x²−4x−1, field Q(√5,√phi) ⊃ Q(√5), genuine 3d Rauzy… |
| **P21 — the framework search** ⚠︎ | 4 | `enumerate-landing-sites` | n/a | Some external SM/GR framework (heterotic, LQG, asymptotic safety, causal sets, NCG) hosts the object's full signature set |
| **W10-B660/B666** ⚠︎ | 4 | `native-continuous-channel` | n/a | The framework can output any dimensionful quantity AS A VALUE (masses, VEVs, Lambda, cross-sections, running couplings) |
| **W11-B706** ⚠︎ | 4 | `native-continuous-channel` | n/a | The SM flavor freedom matches the object -- rung 1: SM flavor ratios are low-height algebraic over the audible field Q(sqrt5); rung 2: the object's seam torsor has the SM freedom's structure |

## Score ≤ 3

Same ordering. Lower-rated routes, kept for completeness.

| id | score | hatch | registers | claim killed |
|---|---|---|---|---|
| **B182** | 3 | `infinite-tower` | — | Superposition (weaving) of multiple metallic units selects a unique structure: refuted -- the gap-label module rank grows as 1+N (distinct fields), proliferation not selection-to-unique. |
| **B184** | 3 | `enumerate-landing-sites` | — | The interaction of multiple units forces a gauge group: refuted -- distinct-field interaction breaks the global inflation symmetry (cross-product escapes the module) and only multiplies per-unit SL(2,Z) dualities, a growing product, not a selected Lie/gauge group. |
| **B197** | 3 | `route-through-atom` | — | Chat2's headline that the figure-eight selection is independently overdetermined: deflated -- the volume filter is unique only GIVEN torsion-free (the same condition the trace-3 sieve uses, not an independent axis), and shortest-word/min-trace are correlated; trace-3 sieve remains the only proof. |
| **B489** | 3 | `enumerate-landing-sites` | — | The SM reading of the self-interaction (cyclic fiber cover) tower: no gauge enhancement anywhere — DGG is abelian U(1)^{2n−1} at every level n=1..8 (the handoff's own falsification test resolves NEGATIVE); covers are not twist knots so Gang-Yonekura does not apply; 4c 'm206(3,1)=5₂' refuted on a wr… |
| **B52** | 3 | `enumerate-landing-sites` | — | The naive three-channel Fibonacci tight-binding model supplies the PC12 physics bridge (a physical realization of the SL(3) character-variety recursion). |
| **B526** | 3 | `enumerate-landing-sites` | — | That the 'UNDENIABLE PHYSICS CROSSING' package contains a crossing (it states the opposite), and that M* can be an isotropic positive-Stein time evolution with the canonical Perron-weighted tetrahedral metric S_tet (the isotropy-Stein no-go, via non-normal transient growth). |
| **B548** | 3 | `route-through-atom` | — | Un-hideable iff self-priored/Pisot — un-hideability as a discriminating special property of the object. |
| **B668** | 3 | `enumerate-landing-sites` | — | Cell F1/F-prime: a resurgent S2 (subleading asymptotic coefficient) is extractable from the Z-ladder -- dies against the program's own melody theorem: the ladder is exactly periodic (P = 175560, B662/G), a periodic sequence has ZERO asymptotic 1/k content, the trans-series expansion has no meaning … |
| **B669** | 3 | `native-continuous-channel` | — | chat1's amphichiral-suppression mechanism: 'the chiral word's |Z_k|^2 grows while the amphichiral golden's stays bounded' (the cosmological-constant route, k~10^60 => Lambda~10^-120). Refuted: every metallic-trace ladder has finite exact q-support => exactly periodic => BOUNDED; boundedness is cert… |
| **B693** | 3 | `infinite-tower` | — | chat1's hope that the inert-5 Hecke structure of the base-changed Bianchi form carries golden (phi) or the good-prime 3^2 richness: a_(5) = +1, the trivial Steinberg value in Q, exactly computed; the faces couple but the coupling is being-arithmetic. |
| **B726** | 3 | `deepen-past-plateau` | — | The owner's clean-closure hypothesis that the bare two quadratic faces Q(sqrt-3) + Q(sqrt5) close the Born-content gap (B725). Killed: the interference PHASE is zeta_5-cyclotomic and the amplitudes quartic -- neither lives in a bare quadratic face (Q(sqrt5) is totally real, no phase); also killed t… |
| **B120** | 3 | `native-continuous-channel` | HINT_LEDGER | That the trivial-point tower carries structure beyond (n; trace, det) — independent data that could seed anything more (values, spacetime). Killed: distinct integer matrices with equal (trace,det) yield identical towers (verified n=3,4,5; 8/15/24 roots match), forced by the Sym-decomposition; the t… |
| **B146** | 3 | `enumerate-landing-sites` | OPEN_LEADS | B145's arithmetic arm ('every imaginary-quadratic-trace-field o-p-t bundle is amphichiral / no arithmetic chiral o-p-t bundle') — REFUTED: recomputed with the correct INVARIANT trace field, RRL/RLL are chiral with invariant trace field Q(√−7). Plus the surviving negative B1: no selection using only… |
| **B154** | 3 | `deepen-past-plateau` | OPEN_LEADS | The rank-based reading of the degree=rank exponent ('k=n is fundamental') and the closed form k=4−m(o−3). Killed: off-principal data gives k=4 at BOTH n=3 and n=4 (order-determined, rank-independent — 'degree=rank' is a principal-spectrum coincidence via B95), and the closed form was later REFUTED … |
| **B157** | 3 | `deepen-past-plateau` | OPEN_LEADS, LEAD_REGISTER | The empirical closed form k=4−m(o−3) for the metallic degree=rank exponent — REFUTED by computed bronze (m=3) counterexamples ((3,4)→3 vs predicted 1; (3,6)→1 vs predicted −5); any ≤3-parameter affine/modular law is an overfit of the sparse grid. Survives: order-determined, rank-independent; exact … |
| **B165** | 3 | `deepen-past-plateau` | OPEN_LEADS, LEAD_REGISTER | The in-sandbox provability of the off-axis (κ<2) Cantor theorem: reduced to ONE open hypothesis (uniform hyperbolicity of the complexified trace map on its non-escaping set) and marked NEEDS-SPECIALIST — Hermitian-κ>2 methods (Damanik–Gorodetski) do not carry (non-normal transfer matrices, no off-a… |
| **B172** | 3 | `deepen-past-plateau` | OPEN_LEADS, LEAD_REGISTER | The probe's own first-draft claim of 'clean IDS-convergence to the (3,−3) label' — self-refuted (residual plateaus at ~2e-4, fixed reference drifts past N~1e5); sharp label certification is method-limited → NEEDS-SPECIALIST. Also: genuine small-label (sum ≤3) combination gaps essentially absent acr… |
| **B185** | 3 | `enumerate-landing-sites` | LEAD_REGISTER | Iterated gluing constraints select a forced-unique value: refuted -- gluing selects continuum->discrete (kappa-fork) but the fork has size >1, multiplies under composition, and is choice-dependent; literal N>=3 all-unit interaction is impossible (1-cusp pieces cap connected gluings at pairs, exact … |
| **B237** | 3 | `infinite-tower` | OPEN_LEADS, HINT_LEDGER | Silver bundle pi_1 carries a binary octahedral (2O) quotient; plus chat-1's supporting claim 'all metallic bundles carry 2T and 2I'. |
| **B247** | 3 | `native-continuous-channel` | OPEN_LEADS, HINT_LEDGER, LEAD_REGISTER | V1: E6 -> SM gauge group via the figure-eight's holonomy in SU(2)_long (centralizer = SU(3)xSU(2)xU(1)^2 refuted -> SU(6); and 'geometric holonomy lives in SU(2)' refuted). |
| **B272** | 3 | `route-through-atom` | HINT_LEDGER | B268's 'REDUCED -- no math obstruction left' for the E6 bridge (i.e. that input-E6 = output-E6 is forced); plus B265 'E6-irreducible connections EXIST' and B267 'five independent invariants imply one E6' as framed. |
| **B294** | 3 | `enumerate-landing-sites` | HINT_LEDGER | 'The seam closings SELECT a distinguished SM-valued world' -- refuted as stated: selective for the object's own structure, catalogue for SM values (E6 lost on closing, CP sign external, scale gapped, chiral datum absent, trajectory gated). |
| **B295** | 3 | `nonlinear-transport` | HINT_LEDGER | Three at once: 'Curie forbids the sign' (P011's argument -- refuted, SSB loophole); 'an SSB double-well is available' (the V(tau) potential is the wrong object); 'tau is gauged so the sign is pure gauge' (stop-gated, eta link unverified). |
| **B321** | 3 | `native-continuous-channel` | OPEN_PROBLEMS | The CP phase pi/6 IS the core geodesic length of the (6,3) Dehn filling, and Z/3 forces the rank-1 democratic Yukawa |
| **B343** | 3 | `nonlinear-transport` | HINT_LEDGER, LEAD_REGISTER | The object selects a TM2 (or any) TBM-breaking direction; killed to: the object forces exact TBM (theta_13 = 0, experimentally excluded), all deviation external |
| **B361** | 3 | `deepen-past-plateau` | OPEN_LEADS | The seam local law: bright iff the pair contains a seed elliptic at both primes (doubly-elliptic law, 8 pairs, zero counterexamples) |
| **B365** | 3 | `enumerate-landing-sites` | OPEN_LEADS | Polarization selection happens at the S-closure level (triangular family S-closed on its own 15-dim span, square not -- prereg) |
| **B389** | 3 | `nonlinear-transport` | CAMPAIGN_STATUS | That the banked mirror law t(a,−b)=τ₃(t(a,b)) is a shadow of group inversion (dihedral mechanism M1/M2: inversion law t(−a,−b)=t(a,b) and the a-flip reduction). |
| **B392** | 3 | `enumerate-landing-sites` | LEAD_REGISTER | Three wall probes: the tricritical-Ising identification of the sector (T-spectrum no-match, completing the earlier S-level no-match — dead at both modular levels); the θ-grading↔seam exponent alignment (E₆∖F₄ lines {4,8} vs seam {6,14}/{2,10} — structural analogs only); and the support-residue pred… |
| **B400** | 3 | `nonlinear-transport` | LEAD_REGISTER | That a canonical 3×3 frame (mixing-matrix-type object) links the (2,3) Mercedes triple and the golden seam line: the golden line is EXACTLY orthogonal to the Mercedes plane (both projections identically zero) via support disjointness in the shared W₂-label space — any linking object requires arbitr… |
| **B406** | 3 | `route-through-atom` | HINT_LEDGER, LEAD_REGISTER, CAMPAIGN_STATUS | The 'modular correspondence = quantization map' lead between 15a1 and 40a1: the a_p ≡ mod-4 congruence at every good prime < 200 is FORCED BY TORSION (ℤ/8 on 15a1, full 2-torsion on 40a1 ⇒ both a_p ≡ p+1 to the relevant modulus); mod 8 nothing survives — the two curves share only conductor-arithmet… |
| **B411** | 3 | `native-continuous-channel` | HINT_LEDGER | The naive arithmetic dictionary: a cell's H-field-type (sqrt5/sqrt-3/sqrt-15 active) is a function of gamma'-class arithmetic invariants (chi_-3(det), chi_5(det), gcd(det,15)). Killed: multi-valued on generic invertible-det cells (6 H-types share one class label); single-valued only on boundary cel… |
| **B444** | 3 | `enumerate-landing-sites` | OPEN_LEADS | The SL(3) elimination field as a figure-eight fingerprint feeding a path-to-physics / 3-generations dictionary (Chat-1's framing). The fields DO differ (4_1 = Q(sqrt-3), Q(sqrt-7); 5_2 needs Q(sqrt5) + cubic/quartic/sextic) but three independently fatal reasons kill the reading: separation inherite… |
| **B521** | 3 | `native-continuous-channel` | CAMPAIGN_STATUS | Some peripheral invariant forces a choice the object doesn't make (Gate A) and the intrinsic commensurator Z/3 realizes three symmetric 27-copies, i.e. a generation-3 (Gate C); jointly, that the audit gates leave a crossing open. |
| **B523** | 3 | `route-through-atom` | CAMPAIGN_STATUS | That some negative was a wrong leap; specifically that the (3,1) Lorentzian causal structure is object-specific — C3/Malament run: the four-verb monoid carries four different causal types, no single preserved cone; the proper (1,3) cone belongs to the evolution verb alone and is generic to any 2-re… |
| **B536** | 3 | `route-through-atom` | OPEN_LEADS, HINT_LEDGER, CAMPAIGN_STATUS | Seat-1's Phase 2-3 measurement-architecture specialness: period-6 post-measurement cycle (NOT REPRODUCED — natural lift gives period 20, convention-dependent), S=1.0620 (natural lift 0.5623, convention-dependent), 'measurement eliminates darkness' as special (CONFIRMED but GENERIC — every state tes… |
| **B572** | 3 | `nonlinear-transport` | OPEN_LEADS, CAMPAIGN_STATUS | The eleven-clause 'SM from sigma end-to-end' chain (17th): clause 8's branching 27|_principal = V3+V7+V17 and its title claim 'sigma distinguishes 27 from 27bar', plus the zero-cost accounting for the F4->Spin(10)xU(1) selector switch. |
| **B574** | 3 | `native-continuous-channel` | OPEN_LEADS, CAMPAIGN_STATUS | The off-principal escape route: 'the minimal nilpotent of E6 has centralizer D5=Spin(10)', so intersecting the minimal-nilpotent locus with the non-real locus escapes the fifth (vector-like) wall. |
| **B632** | 3 | `enumerate-landing-sites` | OPEN_LEADS, CAMPAIGN_STATUS | A symmetric mass-matrix-shaped (Yukawa) texture with three diagonal values exists at class level on the solo complement -- DISSOLVED-BY-OBSTRUCTION (O1: cd=2 kills scalar triples; O2: H^2(M;C)=0 + graded-commutativity force antisymmetry, zero diagonal); audit corrections also killed 'the double res… |
| **B66** | 3 | `deepen-past-plateau` | OPEN_LEADS | The multiplicity formula max(n-d,1) for the odd-k degree-3 factor across the SL(n) tower (predicting 3 at n=6): refuted -- the |k|=3 multiplicity at SL(6) is exactly 2, same as SL(5); it does not grow with n. Plus the honest method-limit: 9 of 35 modes gauge-corrupted, the numerical Jacobian is not… |
| **B664** | 3 | `enumerate-landing-sites` | OPEN_LEADS | chat1's selection claims for the golden word: 'the golden is the ONLY real minimum' (refuted -- quiet+real at n = 3 or 12 mod 15; witnesses n=12,18,27,33 with |tr_odd|=1/phi and Im=0), the 'five independent criteria' (collapse: criteria 4 and 5 are the same, criterion 2 false), and 'det(A-I) unit f… |
| **B720** | 3 | `recompute-cited` | OPEN_LEADS, CAMPAIGN_STATUS | That an external program owns the discrete->continuous coupling bridge and meets the object: renormalization/Connes-Marcolli (NO-MATCH: cosmic Galois is mixed-Tate over Z[i], Gaussian -- wrong cyclotomic branch vs Eisenstein Q(zeta_3)); holography (NO-MATCH: needs higher-dim bulk; 3d gravity has no… |
| **S015 — tower eigenvalues = masses / operator dimensions** ⚠︎ | 3 | `native-continuous-channel` | n/a | The SL(n) tower eigenvalues are a physical mass/operator-dimension spectrum |
| **W4-B604/B607/B608** ⚠︎ | 3 | `enumerate-landing-sites` | n/a | The theta-odd principal blocks align with G_SM sectors (a pair-to-block assignment exists; a gauge/matter or subsystem/coset grading of the hearing sector exists) |
| **W7-rebase** ⚠︎ | 3 | `recompute-cited` | n/a | The naive Z/3 triality acts on H^1(D;27) giving chat-1's 3+2 generation split |
| **B373** | 2 | `deepen-past-plateau` | — | The pinned-exponent law: the level-45 minimal sector's eigenvalue exponent is pinned at ±6 with phase 9π/N → 0 along the 3-tower (gapless-trending reading feeding the tower-limit door PD2.2). |
| **B409** | 2 | `nonlinear-transport` | — | B407's alignment promoted to a universal count-conservation transport theorem ('table anatomy = product stratification'): holds on only 4/6 pairs; fails at the high-multiplicity bright pairs (1,2) and (2,4), where DFT+Π_H maps products to cells NON-INJECTIVELY (merging/cancellation) so stratum coun… |
| **B472** | 2 | `deepen-past-plateau` | — | That the quantum stage at the generators is the quantization of the classical criticality (killed: kappa_q(1,1) = -1 != kappa_classical = -2; quantum closure relocates to CRT-central addresses, [W1^2,W2^3] = I exactly via Q8 mod 3 and SL(2,5) mod 5), plus seat-1's computed values (tr = 1, 'cost of … |
| **B476** | 2 | `enumerate-landing-sites` | — | Seat-1's 'critical interaction algebra = SM gauge algebra' (dim span 36 = 4x9 = gl(2)⊗gl(3) ⊃ su(3)+su(2)+u(1)) — ninth float-kill; exact SVD ranks are 49, 5, 13, and 5x13=65≠49 (does not factor). |
| **B487** | 2 | `native-continuous-channel` | — | Seat-1's 'T[S³\4₁] has the SM gauge group SU(3)xSU(2)xU(1)' from Gang-Yonekura 2018 (13th kill) — the SU(3) is a GLOBAL FLAVOR symmetry of a 3d N=2 U(1) gauge theory; SU(2)xU(1) is its own unenhanced subgroup (one symmetry, not three factors); matter is two U(1) chirals, not SM fermions. |
| **B516** | 2 | `deepen-past-plateau` | — | 'Three spatial dimensions forced by a Pisot dimension cap' — DEAD: golden-field Pisot inflation exists at dims 1 (phi), 3 (beta), AND 5 (three-copy coupling scan); the x→x(1+√x) recursion's break at dim 7 is construction-specific, so 3 is not dimension-selected. |
| **B525** | 2 | `recompute-cited` | — | Both directions at once: (master) the object produces physics — CONFIRMED dead under 5 adversarial lenses; and (meta) the banked negatives were all sound — 3 of 9 CRACKED (B519-NOCROSS retracted, C3-CONE certificate bug, CHILD-NOTSHORT downgraded), 2 SHAKY, all on the same failure form. |
| **B553** | 2 | `deepen-past-plateau` | — | Seat-1 session-3 overclaims: the 'spectral bridge' paper target (killed as KNOWN — KKT 1983/Casdagli/Roberts, banked kappa=2+lambda^2), the SL(5) dimension slip (n-1=4; operative dim is n^2-1=24), 'prime natural level' phrasing (level is m^2, and 1 is a unit); plus this node's OWN earlier over-defl… |
| **B604** | 2 | `enumerate-landing-sites` | — | Chat-1's Rosetta asks: 'which theta-odd pair goes to the V8 block and which to V16' (a pair-to-block assignment), their D5/16 pair-label table at heights 2-3, and ask 3's premise 'which torsion (tau4/tau8) corresponds to which SM coupling'. |
| **B624** | 2 | `deepen-past-plateau` | — | The odd hearing trace is an observable independent of the Weil-coset assembly (and the B618 12|k vs B621 4|k gates contradict): killed by the derived identity -- trace(B_odd) is the SAME twelve-term Gauss assembly up to a fixed framing phase w^-1, the two gates being the two coset copies (align at … |
| **B672** | 2 | `enumerate-landing-sites` | — | Two kills inside a firing arc: (1) the A4 branch -- NO cusp quantization exists (the A4 weight lattice's commutant is Q(zeta5), unique quadratic subfield Q(sqrt5) REAL; both rational systems for z^2 = -12 empty), completing stage selection to the single branch {SU(3)2, 2-hat-prime} modulo H-CUSP; (… |
| **B677** | 2 | `enumerate-landing-sites` | — | G1 wave-1 generator candidates: T0 (Tube(Fib) Hochschild classes) killed by theorem -- Tube(Fib) is semisimple (dim 7, built from first principles) so HH^{>=1} = 0 identically; the character-shaped candidates killed on the NEW value-irrationality axis -- every weld-weighted combination has a genuin… |
| **B698** | 2 | `enumerate-landing-sites` | — | The strong reading of S067 row 2 -- that the level-15 meeting's analytic content (special L-values) ENTANGLES being-prime 3 and hearing-prime 5. Killed: L(E,s) factors into independent local factors by Flath's tensor-product theorem; PSLQ (60 digits) finds no hidden relation; base-rate control show… |
| **B711** | 2 | `recompute-cited` | — | That the two Z/2's (amphichirality and the Q(sqrt-3) Galois involution) degenerate into one locked symmetry. Killed: they are distinct commuting involutions acting ORTHOGONALLY -- Galois swaps rho_geom and its conjugate as a free 2-orbit inside Fix(amphichirality); the two are the non-identity legs… |
| **B721** | 2 | `enumerate-landing-sites` | — | cc2's LEAD 1: that B701's measurement torsor IS the CMR arithmetic KMS-torsor over Q(sqrt-3) (thermal time = the observer's chosen KMS state's modular flow). Killed as rung-mismatch: the being-Z/2 is the QUOTIENT Gal(K/Q), the CMR torsor the KERNEL Gal(K^ab/K) -- complementary in one exact sequence… |
| **B101** | 2 | `enumerate-landing-sites` | LEAD_REGISTER | The 'tower of spacetimes up the ranks' / '3+1D at SL(3) via phase-space dimension': Lorentzian signature climbing the SL(n) rank ladder. Killed: the principal sl(2) invariant form lands in split real forms Sp(k+1,R)/SO(p,p±1); Lorentzian (one timelike) occurs at exactly k=2 (SO(2,1)) and does NOT c… |
| **B128** | 2 | `enumerate-landing-sites` | OPEN_LEADS | The 'single torsion Z/n → SU(n) center → gauge group' bridge. Killed by two independent computed reasons: (1) empirical — torsion tracks periodicity/symmetry-order, not chirality (achiral doubles single-torsion, achiral periodic triples doubled, chiral (1,2,3) single Z/157); (2) interpretive — cent… |
| **B132** | 2 | `route-through-atom` | OPEN_LEADS | S7/S5 (withdrawn by B133 control): 'chirality determines the SU(2)_k eigenvalue field (achiral→Q(√−3), chiral→Q(ζ₁₂)) and chiral fragility drives the Z_k vanishing / selects the symmetric vacuum'. Killed: achiral words alone span all three fields (RRLL→Q(ζ₁₂), RRRLLL→Q(√−3), RLRLRL→Q) and achiral w… |
| **B140** | 2 | `recompute-cited` | OPEN_LEADS | The B139-G hedge: 'genus ≥ 2 might be where chirality stops being a mere CS-sign' (the chirality firewall might be genus-1-specific). Killed by the standard orientation-reversal theorem (mirror has same volume, opposite CS, conjugate-isomorphic trace field — genus-independent). Also retracts (compu… |
| **B161** | 2 | `route-through-atom` | OPEN_LEADS, HINT_LEDGER | 'Cancellation (κ=2) is forced/empty/excluded' and, upstream, 'κ sources a value of Λ' (S014). Killed both ways: κ is a FREE continuum on the trace-map fixed locus (κ-elimination ideal empty, re-derived m=2,4 — no value ever selected) and κ=2 is attained (B130), so 'forced/empty' is refuted; what su… |
| **B279** | 2 | `recompute-cited` | HINT_LEDGER | 'tau could SWAP the two spin structures of 4_1' (chat-2's chiral branch: swap -> chiral matter possible). |
| **B299** | 2 | `route-through-atom` | OPEN_LEADS, OPEN_PROBLEMS, HINT_LEDGER, CAMPAIGN_STATUS | 'H-label = phi-eigenvalue on the 27': that the (theta,phi) Z3xZ3 forces the colored-vs-electroweak (doublet-triplet) split -- phi acts FREELY on the 27 (9 orbits of 3, zero fixed weights), so no per-weight eigenvalue exists; which SU(3) is color is an external triality-breaking choice. |
| **B310** | 2 | `route-through-atom` | OPEN_PROBLEMS, HINT_LEDGER | The E6 breaking cascade is realized object-specifically on the figure-eight character variety with equal pi*i/3 deformation spacing tied to the cusp shape |
| **B313** | 2 | `route-through-atom` | OPEN_PROBLEMS, HINT_LEDGER, LEAD_REGISTER | The SM chiral fermions ARE the Fibonacci anyons (27 -> 7 under the (G2)_1 bridge), and the figure-eight is forced as a theorem |
| **B320** | 2 | `route-through-atom` | OPEN_PROBLEMS | The mod-7 -> Fano -> G2 -> color-SU(3) chain selects color object-specifically; the firewall Z/2 and generation Z/3 fuse into one problem; observer=seam is proven mathematics |
| **B335** | 2 | `native-continuous-channel` | OPEN_PROBLEMS | The mass hierarchy is in the object (the three generations carry a magnitude ordering) |
| **B360** | 2 | `deepen-past-plateau` | OPEN_LEADS | Seam brightness follows seed parity: bright iff the pair contains the even seed (prereg), or the opposite-parity variant |
| **B364** | 2 | `enumerate-landing-sites` | OPEN_LEADS | T-stability forces the theta lift as THE geometric lift (the seam-bearing class is selected at the T-level) |
| **B418** | 2 | `enumerate-landing-sites` | LEAD_REGISTER | B411's upstairs hypothesis: the emergent symmetries (mirror t(a,-b)) become cell-local upstairs in Q(zeta60), realized by a Galois element on the raw pre-Pi_H table. Killed: all 16 elements of (Z/60)* tested, none realizes the mirror cell-wise; emergence is INTRINSIC. |
| **B440** | 2 | `route-through-atom` | OPEN_PROBLEMS, CAMPAIGN_STATUS | A figure-eight-unique feature in the child's SL(2,C) vacuum spectrum (and the interim 'golden inversion' reading, retracted as a chart/parametrization artifact). Killed: 4_1 and 5_2 children both have exactly 4 irreducible vacua in the identical -283 field; count differences elsewhere track A-polyn… |
| **B561** | 2 | `enumerate-landing-sites` | OPEN_LEADS, OPEN_PROBLEMS | The figure-eight's Eisenstein Z/3 selects SU(3)^2 (A2xA2~) inside F4, continuing the chain E6->[theta]F4->[Z/3]SU(3)^2->SM; plus the Klein-four/golden-conjugation follow-up selector and the cusp-boundary 6->4 reduction reframe. |
| **B58** | 2 | `deepen-past-plateau` | OPEN_LEADS, LEAD_REGISTER, CAMPAIGN_STATUS | The brief's cotangent (singular trace-ring) route to the tower multiplicities a_d: cotangent dim = 3n^2-10n+11 with excess 2(n-2)(n-3) over the Jacobian -- i.e. the cotangent cleanly yields a_d; also (Step 2) that the Sym^2k principal-SL(2) decomposition reproduces the tower. |
| **B585** | 2 | `enumerate-landing-sites` | OPEN_LEADS, CAMPAIGN_STATUS | Two preregistered items: LAW-E (the theta-even channel law; failed hold-out at kappa=17,18) and the M1 mechanism '5|kappa <=> sqrt5 in Q(zeta_kappa)' (tone fires iff the stage field contains the word's trace field; silver 8|kappa, bronze 13|kappa, RRL 12|kappa all refuted). |
| **B699** | 2 | `enumerate-landing-sites` | CAMPAIGN_STATUS | That golden hearing is BORN in the surgery coupling of a 5-split object (Whitehead) to a 5-inert one (figure-eight); sub-claim '5-inert necessary for golden SL(2,5) capacity'. Killed: the 5-SPLIT Whitehead fills SL(2,5) too (two seats, two methods), and filling is generic by strong approximation --… |
| **K-A/K-B — det=−1 breaks chirality / selects SM chiral structure** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | det=−1 breaks chirality and selects the Standard-Model chiral structure |
| **K-E — a forced dimensionful scale or non-generic physical ratio** ⚠︎ | 2 | `native-continuous-channel` | n/a | The object forces a dimensionful scale or a non-generic physical ratio (α⁻¹, m_p/m_e, sin²θ_W) |
| **K-F — single torsion ℤ/n → SU(n) center → gauge-group bridge** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | H₁ torsion tracks chirality and its ℤ/n is an SU(n) center selecting a gauge group |
| **K-I — Borromean rings (s776) show SU(3) gauge enhancement** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | s776's S₃-invariant SL(2,ℂ) character variety of dim 2 = rank SU(3) → non-abelian gauge enhancement |
| **Math-kill — θ → c (opposition involution predicts degree=rank scalar)** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | θ=−w₀ predicts all four per-eigenvector Dehn-filling scalars c |
| **P13 — generations via commensurator-triality-on-27** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | E₆→SU(3)³ triality on the 27 gives three symmetric generations |
| **S016 — Goldman metric (1,1) Lorentzian** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | The Goldman/Weil–Petersson form on the character variety is Lorentzian (1,1) |
| **S019 — Fisher metric on CS level k** ⚠︎ | 2 | `recompute-cited` | n/a | An information-geometry (Fisher-metric) reading of the Chern–Simons level |
| **S021 — entanglement = holographic** ⚠︎ | 2 | `route-through-atom` | n/a | The Fibonacci critical chain's entanglement signals holography |
| **S032-A — the literal universal no-escape form (probation P1)** ⚠︎ | 2 | `enumerate-landing-sites` | n/a | NO invariant escapes the trace ring's discretely-multivalued-and-unsymmetric behavior (literal universal S032 Gate A) |
| **W8-B643/B658** ⚠︎ | 2 | `nonlinear-transport` | n/a | Some orientation-reversing (mirror) symmetry of Isom(4_1)=D4 survives the coupling as a symmetry of the weld double's 27 local system |
| **W9-B644/B650** ⚠︎ | 2 | `nonlinear-transport` | n/a | A nonzero C-linear monodromy-equivariant map exists from the classical A1-module to the theta-odd hearing plane (module-linear classical->stage transport) |
| **B219** | 1 | `deepen-past-plateau` | OPEN_LEADS | The WRT period depends on a genus/spinor-genus invariant beyond (trace, content): killed -- exhaustive at f=8 (all 542 class-reps, all four genera: every content-1 class has period exactly 80 = lcm/content, regardless of genus signature), mechanism proved (Klein-four 2-torsion of (Z/2^k)^x for k>=3… |
| **B332** | 1 | `recompute-cited` | OPEN_LEADS, LEAD_REGISTER | The founding letters yield particle-dictionary content: the 1/4 volume-suppression fits SM ratios, 16 = 4 + h(E6), and g = -R L^{-1} is the generation-cycling deck element |
| **B435** | 1 | `route-through-atom` | OPEN_PROBLEMS, CAMPAIGN_STATUS | The founding inheritance reading: H1(child)=Z/5 is a parent birthmark (golden-prime inheritance). Killed by correction #562: H1 = Z/p for EVERY knot at slope p (trefoil control) — numerator-forced, not inheritance. The exact counts (26 = 25+1 abelian E6 vacua) stand. |
| **B437** | 1 | `route-through-atom` | CAMPAIGN_STATUS | The golden return as inheritance: the child's abelian floor speaks the parent's golden language (Tr tau in Q(sqrt5) = parent memory). Killed: trefoil(5,1) gives the SAME field Q(sqrt5) — the field is a theorem about the integer 5 (Q(sqrt5)=Q(zeta5)+), numerator-forced. Also the 'Lucas-square law is… |
| **B60** | 1 | `deepen-past-plateau` | OPEN_LEADS | 'SL(5) does not resolve at double precision -- cond(Dx) ~ 1e11 conditioning barrier' (five failed extraction attempts; the SL(5) row of the cross-n tower left UNRESOLVED). |
| **B734** | 1 | `infinite-tower` | CAMPAIGN_STATUS | Primarily kills B731's negative ('m004 non-congruence / no finite congruence observer' — retracted); surviving negative content: the object-level observer cannot be the abelian CMR/ray-class refinement (abelian GL(1) type mismatch vs the non-abelian Bianchi tower) and the Shimura-KMS route is obstr… |
| **B736** | 1 | `native-continuous-channel` | OPEN_LEADS | Two claims, both two-seat OUTCOME B: (Path B) m004's own single-level non-abelian Bianchi congruence observer (order-2560 image in PSL(2,O3/(8))) carries a Bost-Connes beta=1 SSB with symmetry-breaking Galois action — NO; (Path C) the framework reduces at least one of the ~24 SM free parameters — N… |
| **Math-kill — s_n = c (tower sign predicts degree=rank scalar)** ⚠︎ | 1 | `enumerate-landing-sites` | n/a | The tower sign s_n∈{±1} equals the degree=rank secondary scalar c=i |
| **W1-hardened-record** ⚠︎ | 1 | `native-continuous-channel` | n/a | SM parameter VALUES are derivable from the solo object's numbers (any banked amplitude/tone/ratio/matrix matches a measured SM value beyond base rate) |
| **W2-typing-wall-1prime** ⚠︎ | 1 | `nonlinear-transport` | n/a | A Yukawa-type (symmetric) family tensor for identical generations exists at the classical-cohomology level (solo or double) |
| **W3-B632** ⚠︎ | 1 | `enumerate-landing-sites` | n/a | A symmetric mass-matrix-shaped object (a scalar-valued symmetric texture on H^1) exists at class level on the solo complement |
| **B731** | 0 | `deepen-past-plateau` | — | m004 (the figure-eight knot group) is a congruence subgroup / has a finite congruence observer — B731 concluded NON-congruence (congruence closure index 6 < geometric 12) and declared the object-level-observer door NO-GO. |
| **B216** | 0 | `recompute-cited` | OPEN_LEADS | An elementary f>=8 period law exists: WRONGLY killed -- B216 proclaimed the f>=8 split genus-theoretic/NEEDS-SPECIALIST from a proxy invariant (scalar-depth tested against +/-I only), missing that sqrt(1) mod 8 = {1,3,5,7}; the 'obstruction' class was ≡5I (mod 8), true content 8. OVERTURNED by B219… |
| **S014-null-clause correction (B565 exhumation)** ⚠︎ | 0 | `recompute-cited` | n/a | The epitaph clause '~60% of random constants match as well' supporting the S014 kill |

## Hatches written as prose, not as a route name

These entries state their escape as a full paragraph rather than one of
the seven short route names. They are not lesser — several are the most
carefully reasoned in the graph — but they cannot be grouped by route,
so they are listed separately and the hatch text is given in full.

**B849** — score 4 — registers: OPEN_LEADS, CAMPAIGN_STATUS

- *killed:* That the claimed beta=1 SSB has an order parameter at the manifold level, and that chirality (= complex conjugation) is it.
- *hatch:* If the programme's thermal system is shown to be BC/CMR-type over the CONDUCTOR-4 order O_4 rather than the maximal order O_K, then Cl(O_4) = Z/2 is a genuine object-specific symmetry (m003 sits at O_K with h=1) and a STATE-level order parameter may exist. The generator would be a Frobenius coprime to the conductor -- smallest Frob_7, NOT Frob_2, since 2 | 4. This kill is about the MANIFOLD level only.

**B854** — score 3 — registers: —

- *killed:* That a non-abelian gauge algebra (su(2)+u(1), read as electroweak) arises as the centralizer of the object's finite holonomy image 2T inside the E6 its arithmetic selects.
- *hatch:* 2T enters via the PRINCIPAL SL(2). A NON-PRINCIPAL embedding of 2T in E6 has a different centralizer and none was computed -- that is the one honest way this route could still yield a non-abelian algebra. Separately, the conformal-embedding route (B254) is untouched by this kill, though its 'U(1)' factor is really (A1)_1 = SU(2) at level 1, since c((A1)_1) = c(U(1)) = 1 exactly.

**B850** — score 3 — registers: CAMPAIGN_STATUS

- *killed:* That the foliation-algebra type (the internal-clock route that would make the SSB genuinely spontaneous) is object-specific to m004.
- *hatch:* If the standard ratio-set reduction FAILS for cusped foliations -- m004's flow is not uniformly hyperbolic and the foliation carries an INFINITE transverse measure, which is why compact-Anosov => III_lambda does not transfer -- then the type is not settled by length-spectrum density and the genericity does not follow. That is the one open step and it is named in the seal.

## ⚠︎ Ids that are not arc ids

The graph's `id` field is not uniformly an arc id. These entries are
kept and flagged rather than dropped or coerced; their `registers` column
reads `n/a` because register lookup is arc-keyed and cannot answer for
them. **Anything else keyed on `id` will mis-handle these silently.**

- `K-A/K-B — det=−1 breaks chirality / selects SM chiral structure`
- `K-E — a forced dimensionful scale or non-generic physical ratio`
- `K-F — single torsion ℤ/n → SU(n) center → gauge-group bridge`
- `K-I — Borromean rings (s776) show SU(3) gauge enhancement`
- `Math-kill — s_n = c (tower sign predicts degree=rank scalar)`
- `Math-kill — θ → c (opposition involution predicts degree=rank scalar)`
- `P13 — generations via commensurator-triality-on-27`
- `P21 — the framework search`
- `S014-null-clause correction (B565 exhumation)`
- `S015 — tower eigenvalues = masses / operator dimensions`
- `S016 — Goldman metric (1,1) Lorentzian`
- `S019 — Fisher metric on CS level k`
- `S021 — entanglement = holographic`
- `S032-A — the literal universal no-escape form (probation P1)`
- `W1-hardened-record`
- `W10-B660/B666`
- `W11-B706`
- `W2-typing-wall-1prime`
- `W3-B632`
- `W4-B604/B607/B608`
- `W7-rebase`
- `W8-B643/B658`
- `W9-B644/B650`

## Verifying this file

1. `python3 scripts/revivable/build_revivable.py --check` — exits nonzero
   if this file does not match the current graph.
2. Re-run without `--check` twice; the output is byte-identical (no
   timestamps, deterministic ordering), so any diff is a real graph change.
3. Spot-check a row against its source: every field is copied from the
   graph entry of the same `id`; nothing is inferred or summarised.
4. The graph **and** the registers are read from the same ref, so the
   `registers` column compares one snapshot against itself. Mixing refs
   there would silently misreport what is registered.

