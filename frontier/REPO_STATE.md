# Repository State Report — whole-repo reaudit

**Date:** 2026-06-03. **Type:** MAPPING (not a refactor). **DoD:** this report + a punch-list;
trivially-safe fixes applied, everything non-trivial PROPOSED; no premature closes. Audited at
`main` @ `6d3b5f6` (PR #26).

> ## Update — 2026-06-07 (post-V111) — B122: the tower is Sym^n(W=V⊕1) (unifies B121 + the Chat-2 W-identity)
>
> The two-sequence (B117) re-expressed as a virtual `GL(2)`-module: `ρ_n = Sym^n(W) ⊕ (Sym^{n−3}(W) ⊖ W)`, `W=V⊕1`.
> A **genuine `GL(2)`-module iso** (symbolic in general `(x,y)`, det-independent, n≤8; module-level proved n=3,4 via
> B103). **`W` is B121's external monodromy fundamental** (`det(W)=−1`); the Fricke 3-space `=Sym²V` has `det=+1`
> (internal/Kostant) — so the natural "`W`=Fricke" guess is **killed by B121's external≠internal**, and B121 ⟂ the
> W-identity are **one object** (the monodromy grading *is* `Sym(`external fundamental`)`). `Sym⁴(3-space)=15=sl(4)`
> is the unique saturating order (the n=4 fixed point). **Honest:** a repackaging + a canonical `W`, **not** a
> wall-bypass — module-iso-equivalent to the two-sequence, no functorial `Sym(W)→trace-ring` map (the brave
> functorial test was run and stalled). Re-aims the prize ("prove the tower is *functorially* `Sym^n(W)⊕…`") without
> lowering the wall; the magnitude layer only (signs = the det=−1 layer, B118). K008 extended; the 3+1/spin-2
> readings firewalled (S028). *No physics; nothing to `CLAIMS.md`; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V109) — physics-bridge sweep: distinct metallic materials (Phase 1) + the monodromy/Hitchin grading (Phase 2)
>
> A brave-but-honest sweep of the bridges to physics, all **firewalled** (`speculations/PHYSICS_BRIDGE_MAP.md` maps
> the whole terrain: DEAD / LIVE / HEAVY). **Phase 1 (V108, S023, `TESTED-POSITIVE`):** the SL(2) Hermitian metallic
> quasicrystals (golden/silver/bronze) are **arithmetically distinct real materials** — gap-label fields
> `ℚ(√5),ℚ(√2),ℚ(√13)`, distinct RG scale `φ_m` and spectral dimension — **even though** the tower *algebra* is
> m-universal (B120). The algebra is one object; the physics is a family of distinct, buildable materials (1D
> condensed matter, NOT cosmology; SL(n≥3) blocked, non-Hermitian). **Phase 2 (V109, B121):** the `(n²−1)`-dim tower
> carries two `SL(2)`-actions on the adjoint — the **internal principal** (Kostant, even, `det=+1` = the
> Hitchin/Fuchsian section, B101) and the **external monodromy** `GL(2,ℤ)` (the tower, mixed parity, `det=−1` = the
> mapping class group); they agree only at n=2, and the obstruction for n≥3 **is** `det(M_m)=−1` (odd `Sym^d` = the
> `char(−M^h)` sectors, B112/B118). The banked negative "tower ≠ Kostant" (B89-T/B98) is now **positive**: the
> monodromy is the `det=−1` external action, the Hitchin section's monodromy partner. The Hitchin/Langlands reading
> is firewalled (S024, ceiling N=4 SYM). *No physics in the math; nothing to `CLAIMS.md`; physics chapter stays
> CLOSED; P1–P16 untouched. The all-`n` prize (prove `μ_d`, B103) is untouched.*
>
> ## Update — 2026-06-07 (post-V107) — B120: the tower is determined by (n; trace, det) (banks Chat-2 Q2/Q3 + S1–S5)
>
> The `(n²−1)`-dim trivial-point tower (the Sym two-sequence, B117/B103) is **one object** fixed by two inputs —
> the unfolding depth `n` and the abelianization seed `(trace, det)`. **Q3:** distinct same-`(trace,det)` integer
> matrices give identical towers. **S2 (the deep lead):** the Sym content `μ_d` is m-independent (the `μ_d` are
> plethysm multiplicities of the `GL(2,ℤ)`-rep `ρ_n`, trace-blind) — **reframes the prize as a plethysm**, but a
> *reduction, not a closure* (proved n=3,4; same trace-ring wall). **Q2:** degree=rank **splits** — (I) spectral
> `char(Mⁿ)` factor ⟺ `μ_n=1`, all n / (II) geometric longitude=meridianⁿ, n∈{3,4} — dissolving the apparent
> B117-vs-B119 tension; the lineage rows V47/V72/V74 are annotated. **Three corrections** (verify-don't-trust): S1's
> `(n²−3n)/2` → `(n−4)(n+1)/2`; S5's guess refuted but a closed form found (heights run 0..n); S4 confirms B116 is
> factor-level (the Chat-2 "n=3 divergence" was a units error). **Governed-folder banking:** `knowledge/K008`
> (the determination explainer), `philosophy/P004` (expansion is interaction-born — `M_m=(twist)ᵐ·(swap)`, the
> SL(2,ℤ) finite-order-generation spine), and the **downgrade** of the Markov-blanket / boundary-open reading to
> low-rank n∈{3,4} (TWO_SYMMETRY_FRAME, S022). The prize is unchanged and un-fused: prove the Sym two-sequence `μ_d`
> for all n (B103). *No physics; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V106) — B118/B119: the sign-half gate (a closed-form sign + correction) + the power-half sharp negative
>
> Chat-2's Path 1 (the gate) and Path 3 (the hard path), with the Opus reframing (B117) standing.
> **B118 (V105) — the gate.** B112 proved the `(+1,−1)` eigenspace *dimensions* of `θ=−w₀` by a permutation
> argument; the `⌈`-vs-`⌊` tip is decided by the sign θ carries on the lone fixed root (odd `m=n−h`). Path 1 asked
> whether that sign is `+1` for all `(n,h)` (which would make B64 a uniform "`+1` sector = `char(M^h)`" theorem).
> Realizing θ as the genuine *signed* contragredient involution `τ(X)=−J Xᵀ J⁻¹`, the **fixed-root sign
> `= (−1)^{h+1}`** (symbolic + verified `n≤12`) — `+1` for odd `h`, `−1` for even `h`: **NOT a uniform +1**. So
> B64's "`+1` sector = `char(M^h)`" holds only for odd `h` — a **refinement/correction** of B112's unsigned "fixed
> root is always +1". The `(⌈,⌊)` dimensions stand; B112's `char(M^h)=⌈` labeling stays tower-verified `n≤5` (B118
> supplies the all-`n` sign, not an independent all-`n` labeling proof). Emergent (non-circular): the fixed-root
> sign `= +1` ⟺ the inversion identity `char(M^{−h})=char(−M^h)` ⟺ `h` odd. The θ-split is **not the tower** (the
> Sym two-sequence, B117; diverges `n≥6`).
> **B119 (V106) — a sharp negative on the power half.** `Mᵏ` central on the principal iff `order(a)|k`
> (`a+1/a=3−n`, `order(a)={4,3,2,∞}`). `k=n` is non-central where the principal exists (n=3,4) but **not unique**
> ⇒ centrality does **not** force `k=n` (the A-poly B83 pins it); and for **n≥5 the principal does not exist
> irreducibly** (B95). So `exponent=rank` is an `n∈{3,4}` phenomenon; the brave `k=n` proof cannot be completed.
> The secondary 2n-type gives exponent `n−1` (`Mⁿ=−I` central; extends B111). Emergent: the cusp order is
> `{4,3,2,∞}`, **not** a clean `{n−1,n+1,2n}` law (B111 ADD2 conflated three components).
> **Net.** B118 supplies the all-`n` fixed-root sign `(−1)^{h+1}` (a refinement of B112; the labeling stays
> tower-verified `n≤5`); the positive peripheral power-half mechanism is a sharp
> negative (B119). The all-`n` **tower** stays the prize = **prove the Sym two-sequence `μ_d`** (B103). *No
> physics; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V104) — B117: the interleaving insight (the tower is the Sym two-sequence)
>
> The **headline reframing** of the B111–B116 run (the Opus interleaving insight, verify-don't-trust). The
> `(n²−1)`-dim trivial-point tower is **one object** — the **Sym two-sequence** (B103/B58) — not two separable
> halves (sign + power). A **dimension identity** `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2` (roots `{−1,4}`)
> **derives** B103's two-sequence `μ_d = [2≤d≤n]+[0≤d≤n−3]` (n=4 the unique perfect fit; n<4 omit modules — n=3
> omits `Sym¹`, the unique subset `{0,2,3}`; n≥5 double `Sym²..Sym^{n−3}`). So **the "promotion" is a `Sym¹`
> absence** (B111/B113 framing **superseded/tombstoned**); the height-1 `char(−M)` at n=3 is `Sym³`'s
> contribution, not a "promoted `Sym¹`". **degree=rank's `char(Mⁿ)` = `Sym^n` presence** (`μ_n=1` ∀n; dim-forced
> only at n=3 — *not* "by dimension"; rep-theory n=2,4; two-sequence form n≥5). `Sym⁰..⁴` product = the B80 proved
> n=4 tower. **B112 relabeled to three tiers** (the `−w₀` multiplicity structure up to the fixed-root label —
> proved all n; the fixed-root labeling = B64, pending B118; the tower realization with powers — verified n≤5,
> superseded). **Re-aimed prize:** prove the **Sym two-sequence `μ_d`** for all n (B103's open problem). *No
> physics; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V103) — B116 reconciliation + a CORRECTION to B112
>
> The B112↔B103 reconciliation (run to *join* the prize's two halves) found a **correction** instead (verify-
> don't-trust, banked visibly like V90/V91). The **Sym two-sequence (B103) = the actual tower** (it matches the
> resolved SL(5) and carries `char(Mⁿ)` automatically as `Symⁿ`'s top weight); the **θ-split (B112) = the tower
> only `n ≤ 5`** (= θ-split + one degree=rank promotion) and **DIVERGES at `n=6`** — exactly the banked V26/V27
> (`a₁` 2v3, `a₂` 3v2, `b₂` 1v2). **B112's "sign half proved for all n" is downgraded to "n ≤ 5"** (the
> combinatorial lemma stands for all n; the *tower-identification*, the V25 gap, holds only n≤5). The all-`n`
> sign half is OPEN. **Re-aimed prize:** prove the **Sym two-sequence** for all n (B103's open problem) — the
> better tower-candidate — with the `Mᵏ`-scalar arithmetic (B111) for the exponent. *No physics; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V102) — the ρ_n sign half PROVED + the five follow-on paths (B112–B115)
>
> The five paths B111 opened, computed. **B112 (V99) — the headline:** the **sign half of `ρ_n` is PROVED for
> all n**, engine-free — an elementary root-system reversal lemma (`θ=−w₀` = the reversal on the height-`h` roots,
> `(+1,−1)` dims `(⌈,⌊)`, verified all n≤12) × the banked B64 parity assignment ⇒ `mult char(±M^h)=⌈/⌊(n−h)/2⌉`.
> The first catalog piece proved from first principles for all n. **B113 (V100):** the proved closed form
> **resolves the SL(5) sign sectors** at heights 2–4 by proof — including `char(M²)²·char(−M²)` = B62's 2
> gauge-corrupted modes — and **localizes degree=rank to height-1 + `char(Mⁿ)`** (the promotion is n-dependent;
> power half open). **B114 (V101):** the covering-degree mechanism is **TESTED-NEGATIVE** (full degree `~k^{n−1}`,
> not `k`); the exponent lead stays the `Mᵏ`-scalar arithmetic. **B115 (V102):** the known SL(4) Dehn-filling reps
> are forced-locus (like SL(3)); off-locus SL(4) + genus-2 degree=rank scoped OPEN (obstructions named). **State
> of the prize:** the **sign half is proved (all n)**; what remains is the **power half** — the single degree=rank
> promotion `char(M)→char(Mⁿ)`, n-dependent, localized to the height-1/top-power interface. *No physics; P1–P16
> untouched.*
>
> ## Update — 2026-06-07 (post-V98) — B111 the tower's sign structure + the degree=rank exponent
>
> The "sign findings" handoff (Chat 2 + the Opus supplement, ADDITION 1/2). **B111 (V98)** — the most-leveraged
> computation, done first: the `θ=−w₀` all-heights **closed form** (`⌈(n−h)/2⌉`/`⌊(n−h)/2⌋`, matching B62 height-2)
> is **not** the proved tower — `Tower(n) = [closed form] with one `char(M¹)` promoted to `char(Mⁿ)`** (verified
> n=3,4). So the **sign half of `ρ_n` is closed-form** (bulk θ); the only open piece is `char(Mⁿ)` = degree=rank
> (peripheral). **ADDITION 1** (proved): the SL(4) secondary `M⁴=−1` scalar ⇒ `k=4` impossible (`k=3` forced);
> principal `M⁴` non-scalar ⇒ `k=4` allowed (`k=n` not proven). **ADDITION 2:** cusp orders `{n−1,n+1,2n}`; `ord−1`
> TESTED-NEGATIVE. Corrected the SL(3) parity to `(t−1)(t−det N)`. **Leads (PR #121):** `S022` (the peripheral
> ℤ/4, the successor to θ→c) + `TWO_SYMMETRY_FRAME` (bulk θ + peripheral cusp; degree=rank at the interface);
> `s_n↔c` DEAD. *No physics; the `ρ_n` catalog proof stays the target; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V97) — the Final Computation Arc (B108–B110, the architecture rooms)
>
> The CC-web "Final Computation Arc" + the intellectual-architecture build. **Architecture (PRs #113/#114):** four
> governed rooms `speculations/` (catalog `S001–S021`, the `HELD(value-matching)` tier, the exercise, the DEAD
> tombstones), `philosophy/` (`P000–P003` + migrated `P1–P5`), `story/` (00–08), `knowledge/` (stub) + root
> `ARCHITECTURE.md`; `paths/philosophical/` migrated away (live refs redirected, append-only history kept).
>
> **B108 (V95) — `θ=−w₀ → c`? NO** (the prize, Task 1): the hinge fails — `θ` is an involution (order 2) and
> predicts `c∈{1,−1}` but not the order-4 secondary `c=i`; degree=rank's `c` stays OPEN, missing a `ℤ/4`
> ingredient (cusp-spectrum candidate). **B109 (V96) — the void dynamics (D2):** verify-don't-trust corrected the
> coordinate-axis facts to the linearization `DT₁²` eigenvalues `{1,φ⁴,φ⁻⁴}`; the center manifold = the tower's
> parity sector (1@SL2, 2@SL3); the void is a (2,1) saddle of `κ`; + L5 literature (degree=rank apparently-new;
> W₄ real-but-generic). **B110 (V97) — the off-locus sector of `4₁`/SL(3) is EMPTY** (HMP's 3 components all on the
> forced locus); the higher-rank/other-manifold fork stays open. **Dead-ends register** (PR #118): ~30 kills
> consolidated in `docs/atlas/FAILURE_ATLAS.md` by pattern, the REVIVABLE (n=5-wall) lens foregrounded. Probe
> updates: S001 (all-`m` amphichiral PROVED), S006 (Bell → TESTED-NEGATIVE). *No physics; the `ρ_n` catalog proof
> stays the central target; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V94) — B106 Dehn-filling anatomy + hygiene + B107 physics-connection audit
>
> **B106 (V92) + hygiene (V93):** the trace map at the **Dehn-filling** reps — the never-computed *third*
> fixed-point class (after trivial=tower and geometric=torsion). Three distinct Jacobian signatures; the
> Dehn-filling reps are **partially elliptic** (SL(3) `(1,1,6)`, SL(4) `(4,4,7)`, root-of-unity neutral
> eigenvalues). Honest negative: the stability *type* does **not** encode the degree=rank exponent. `Lᵢ=c·Mᵢ^k`
> per eigenvector; `M⁴=L`/`M³=L`, conjugates absent. **[V93]** the D1 root-of-unity values pass the B84
> gauge-noise gate (seed-stable); the SL(4) principal (`c=−1`) **corroborates** the proved B89/B83 (not new),
> the **new** content is the secondary (`c=i`, numerical), SL(3) W2, and the per-eigenvector method. PR #110.
>
> **B107 (V94, POSTULATED/FIREWALLED):** the CC-web physics exploration banked as a **dead-end log whose
> headline is a NEGATIVE**. **A:** the metallic trace map **is** the KKT/Fibonacci trace map (`tr[A,B]`=Sütő
> invariant, conserved ∀m). **B:** every SL(3) tower eigenvalue is `±φᵏ` — **one golden scale** ⇒ re-presented
> moduli-space monodromy, **not new physics** (the decisive negative). **C:** tower/torsion `=` masses are
> withdrawn category errors; only the moduli-space `M_SUSY≅M_flat` + three-branch↔three-fixed-point map is
> citable. **D:** GKLP 1305.0937, DGG 1108.4389/1112.5179. **E:** the off-principal multichannel fork is open.
> *All physics firewalled to `speculations/archive/PHYSICS_RESONANCES.md` (Path 8); nothing to `CLAIMS.md`; the
> physics chapter stays CLOSED; P1–P16 untouched.*
>
> ## Update — 2026-06-07 (post-V91) — B105 three-obstacle correction + sharpened ρ_n target
>
> A further **explicit downgrade** of B105's "one collision is the common root cause" (verify-don't-trust:
> B95 spectrum + B62 height-2 split re-derived). **n=5 is a structural THRESHOLD where three *distinct*
> `A_{n−1}` obstacles degenerate** — (i) degree=rank (B95, eigenvalue `−1`, `A²=I`, onset n=5); (ii) the
> tower/eps-series doubling (B62, golden `char(M²)²` from the A₄ height-2 `θ=−w₀` (4,2) split, onset n=5);
> (iii) trace-ring non-closure (engine-free, algebraic, onset n=4). Different eigenvalues (`−1` vs `φ²`),
> independent derivations, different onset — **not one collision** (withdrawn). *Kept:* the tower wall and
> the eps-series rank-drop ARE one wall (both B62's `char(M²)²` doubling).
> **Sharpened `ρ_n` target:** prove `char(ρ_n)=catalog` by reproducing the opposition-involution
> multiplicities (`θ=−w₀` eigenspace dims per height-`h` A_{n−1} root space) directly from `ρ_n`; the
> contested n=5 piece is **only** B62's `char(M²)²` — the degree=rank `−1` and trace-ring non-closure are
> separate, untouched problems. Banked: `CORRECTIONS_V91` + `three_obstacle_distinction()` + test; ledger V91.
>
> ## Update — 2026-06-07 (post-V90, current at `main` PR #107) — B105 V90 audit (two inference downgrades)
>
> The CC verification chat flagged two B105 inferences that overreached; **both are withdrawn (V90, banked
> explicitly).** The 21/24 computation and the `ρ_n` thesis stand.
> - **Correction A:** "seed-variation ⟹ gauge noise ⟹ coordinate artifact, NOT a structural change" is
>   **INVALID**. A rank-deficient eps-series returns seed-dependent values at the unresolved sector
>   *regardless of the truth* (B84; Appendix A re-run confirms the true value is buried under the seed-noise).
>   **The explicit n=5 catalog is OPEN; a structural deviation there is neither ruled in nor out.** The
>   genuine evidence is the resolved-21 universal catalog-consistency; the 3 unresolved are supported as
>   `Sym²` by the **structural routes** (B62/B89-T/B103), not by the seed-variation.
> - **Correction B:** "natural boundary at n=4, proved / complete at n=4" **OVERSTATES**. `char(J(n))=catalog`
>   is a class function for **all `n`** (B103) — no mathematical boundary; n=4 is a *methodological ceiling*
>   (eps-series pinv non-convergence + trace-ring non-closure), not a theorem. The cusp collision is a
>   *candidate* root cause, a structural observation, not a proof.
> - **The open frontier (restated):** prove `char(ρ_n)=catalog` directly from `ρ_n` (B103) + B62's
>   multiplicities — around the σ-construction; that would close n≥5 by proof.
>
> **Corrected net:** structure proven all-`n`; explicit catalog through n=4 for all monodromies; **explicit
> n≥5 catalog OPEN**, walled from two methods; one fully-characterized object `ρ_n` (exact/constructive
> n=3,4). *Not* "complete at n=4 with a proved boundary."
>
> ## Update — 2026-06-07 (post-V89, current at `main` PR #105) — the n=5 wall + the ρ_n convergence [V89; see V90 above for the A/B downgrades]
>
> **B105/V89** runs the n=5 computation + the campaign synthesis. Suite **278 passed, 1 skip**; P1–P16
> untouched; no physics. *(The "coordinate artifact, not structural" and "natural boundary proved" framing in
> this block is corrected by the V90 audit above — read V90 first.)*
> - **N5:** the SL(5) eps-series resolves 21/24 Dickson factors; the resolved 21 are universally
>   catalog-consistent; the 3 unresolved are supported as `Sym²` by structural routes (B62/B89-T/B103). The
>   strict "all 3" bar is not met → the explicit n=5 catalog is OPEN (per V90).
> - **H6 (structural observation):** the forced cusp spectra `{1,i,−i}`/`{1,1,ω,ω²}`/`{1,1,1,−1,−1}` — the
>   non-trivial eigenvalues collide first at n=5 (`−1` mult 2); a candidate root cause (per V90).
> - **Convergence:** the project converges on one object **`ρ_n`**, fully characterized n=3,4, explicit n≥5
>   open. Literature L1 (GKLP 1305.0937) + L4 (Bonahon–Dreyer / Douglas–Sun) cited; H1–H6 / C1–C4 tabulated.
>
> ## Update — 2026-06-07 (post-V88, current at `main` PR #103) — the Dehn-twist route: SL(4) + the SL(5) wall
>
> **B104/V88** executes the "Dehn-Twist Route" handoff in full (the continuation of B103): build any
> monodromy's trace map by composing the elementary twists `U,L,S` inside the eps-series — not the Procesi
> ring (the B85 wall). Suite **274 passed, 1 skip**; P1–P16 untouched; no physics.
> - **SL(4) (proven):** the GATE reproduces B80's metallic tower; `J` factors through `N`; `char(J(N))` = the
>   two-sequence catalog with **det-sign parity** for **metallic and non-metallic** `N` (e.g. `U²L`, det +1)
>   — the explicit SL(4) catalog is a computed theorem for all monodromies.
> - **SL(5) (characterized wall):** the engine inherits the eps-series gauge degeneracy — `char(J)≠catalog`,
>   but **21/24 Dickson factors resolve** (the doubly-degenerate sector, B61/B66). A **computational** wall,
>   not a rep-theory failure; the n≥5 obstruction is now isolated to the eps-series degeneracy (a
>   non-degenerate slice would close it).
>
> ## Update — 2026-06-07 (post-V87, current at `main` PR #101) — the SL(n) tower as a GL(2,ℤ) representation
>
> **Headline: a fourth route to the tower, and the module-iso (M) proved constructively + exactly over ℚ[m]
> at n=3,4.** Two converging CC-web handoffs synthesized (verify-don't-trust). Suite **269 passed, 1 skip**;
> P1–P16 untouched; no physics.
>
> - **B103/V87.** **Route 1 (universality, all n):** `J_φ(n)` factors through the abelianization `N∈GL(2,ℤ)`
>   (inner autos trivial on traces) ⇒ `ρ_n` is a `GL(2,ℤ)`-rep ⇒ `char(J)` is a **class function = the
>   catalog**, universal for metallic **and non-metallic** monodromies; **det-sign parity** sharpens B94
>   (verified at SL(3) via the exact Lawton maps; the MCG relations lift; `J(3)` constant on each `N`-class).
>   **Route 2 (n=3,4 exact over ℚ[m]):** an explicit `m`-independent invertible `P` with
>   `P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}` (intertwiner dim `=Σμ_d²` Schur), realizing the module-iso **(M)**
>   constructively; sign sectors = `det=−1` twists.
> - **Reframing:** the all-n tower = **decompose the `GL(2,ℤ)`-rep `ρ_n`**; universality structural (all n),
>   explicit `μ_d` proved n=3,4 / open n≥5 (the Procesi wall); the Dehn-twist composition computes
>   `char(ρ_n)` without the Procesi ring → continuation **B104**.
>
> **Net:** the tower's *structure* (Dickson-product, det-sign sectors) is now understood representation-
> theoretically and the module-iso is exact at n=3,4; the remaining all-n content is the explicit catalog
> `μ_d` = decomposing `ρ_n`. Supersedes the prior "reduced to one module-iso" status with a constructive proof
> at n≤4 + a clean reframing.
>
> ## Update — 2026-06-06 (post-V86, current at `main` PR #99) — the W1/W2 dichotomy + R4 continuation
>
> CC-web handoff (from the verification chat) "the R4 continuation + the W1/W2 dichotomy" (ledger **V86**):
> **verified before landing**; pure character-variety / higher-Teichmüller geometry, **no physics**. Suite
> **263 passed, 1 skip**; P1–P16 untouched.
>
> - **B102/V86 — the W1/W2 dichotomy (D1–D4, SOLID).** Cayley–Hamilton on `T₁²` forces every irreducible
>   `Fix(T₁²)` SL(3) character into Case I (`trA=trA⁻¹`, self-dual) or the `trB=trB⁻¹=1` branch (0
>   "neither"). On B71's *realized* components: **W1→`ρ(a)` elliptic `{1,i,−i}`, W2→`ρ(b)` elliptic**
>   (order-4, not loxodromic ⇒ **not Hitchin**); the geometric V0 point is self-dual, `tr(AB)` a root of
>   `t²−t+7` (`Q(√−3)`). **V0 excluded by complexity, W1/W2 by ELLIPTICITY** (the cleaner obstruction); the
>   `{1,i,−i}` spectrum **is** Task M's `n=3` spectrum (B95). Refines the handoff (W1 on A, W2 on B; `Q(√−3)`
>   is the geometric point not all of Case I).
> - **B102/V86 — the R4 continuation (D5; robust mechanism, headline not reproduced).** The boundary
>   conditions cut the cubic directions to a 9-dim relative family keeping the cusp real **only to first
>   order** (generic second-order cube-root complexification). **The handoff's `t*≈3.775` geodesic boundary
>   does NOT reproduce** (ray-dependent); the unipotent-cusp-preserving continuation is `open`.
>
> **Net:** the genuine figure-eight SL(3) components are pinned out of the real Hitchin component (ellipticity
> for W1/W2, complexity for V0); the boundary-controlled cubic continuation is first-order only.
>
> ## Update — 2026-06-06 (post-V85, current at `main` PR #97) — the Hitchin-component reframing
>
> CC-web handoff "the Hitchin-component reframing" (ledger **V85**): verify two grounding computations, land
> the **mathematics**, **firewall** the physics. Both appendix scripts re-derived independently. Suite **256
> passed, 1 skip**; proven core P1–P16 untouched; physics chapter stays **CLOSED**; the physics chain is
> cited, never claimed.
>
> - **B101/V85 — V0 = the Fuchsian locus of the `SL(3,ℝ)` Hitchin component.** The geometric component V0
>   (B71 — `Sym²` of the Fuchsian `SL(2,ℝ)` rep) *is* the Fuchsian locus of the Hitchin / Fock–Goncharov
>   positive component of the once-punctured torus. **R1** (`STRUCTURAL`): the Anosov hallmark + the unique
>   `SO(2,1)` form, signature `(2,1)`. **R2** (`dead`): the symmetric-space ladder — the principal `SL(2)`
>   lands in split real forms; Lorentzian only at `k=2`, does not climb ⇒ **no tower of spacetimes** (kills
>   the "3+1D at SL(3)" idea structurally). **R3**: `sl(3)=V₂⊕V₄`; `V0={cubic=0}`. **R4** (the genuinely-new
>   computation): `H¹(F₂,sl(3)_Ad)=8` splits `3⊕5` (Teichmüller ⊕ cubic) + an explicit Anosov deformation
>   leaving V0 and breaking the `SO(2,1)` form. Cite Hitchin 1992 / Labourie / Fock–Goncharov / Choi–Goldman
>   / Marquis; the Hitchin→Langlands→N=4 chain cited with the ceiling stated (N=4 SYM, not the SM/gravity/
>   the universe). Three dead-thread heuristics recorded in `docs/atlas/FAILURE_ATLAS.md`.
>
> **Net:** the new SL(3) content is the **5-dim cubic-differential** directions off V0 (exhibited
> infinitesimally and as a finite Anosov deformation); the "spacetime tower" is dead; the physics stays
> firewalled.
>
> ## Update — 2026-06-06 (post-V84, current at `main` PR #95) — geometry invariants + literature bridge
>
> Two CC-web handoffs, run on the project's discipline — **"compute the numbers, quarantine the
> interpretation"** (ledger **V80–V84**). Bounded quantum-topology invariants on the metallic
> mapping-torus manifolds, banked as mathematics; **every** physics reading lives only in
> `speculations/archive/PHYSICS_RESONANCES.md` (`SPECULATION`, never promoted). Physics chapter stays
> **CLOSED**; proven core P1–P16 untouched; suite **249 passed, 1 skip**.
>
> - **B96/V80 — geometry invariants.** Metallic volumes strictly monotone (`2.030<3.664<4.814`,
>   `m=1`=systole); the volume Hessian is **definite `(0,2)`, NOT Lorentzian** (155/156 fillings of `4_1`
>   below `V₀`) — the most-leveraged "physics path" returns negative. `|τ₃|` left open (branch-ambiguous).
> - **B97/V81 — where the Lorentzian lives.** The `(2,1)` form is **located** as the `so(2,1)=sl(2,ℝ)`
>   gauge algebra on the SL(2,ℝ)/Teichmüller component (toy 2+1 gravity) — structural, not emergent; the
>   3+1 wall untouched.
> - **B98/V82 — the trace-map Jacobian at the GEOMETRIC rep (Probe 1).** `char(D T₁²)=(t−1)(t²−5t+1)` =
>   the **adjoint torsion `τ₁=−3`** (twisted Alexander), **NOT** the Dickson tower — so the tower is a
>   trivial-rep phenomenon (*consistent with* Daly arXiv:2411.04431 + 3d-3d, cited); explains why Task T
>   degenerated at the trivial rep. Tower ≠ Kostant branching.
> - **B99/V83 — the SL(3) geometric Jacobian (Probe 1c).** Torsion-type (the `c=5` SL(2) torsion pair via
>   `Sym²`), not the SL(3) tower (real `{−1,3,4}`).
> - **B100/V84 — literature cross-checks (Probes 2+6).** The Zickert/SnapPy Ptolemy variety of `4_1`
>   (2 obstruction classes, 6 trivial-class reps) cross-validates B71 from an independent code path; the
>   Baker–Petersen (arXiv:1211.4479) twisted Alexander **is** the B98/B99 geometric Jacobian. Two published
>   frameworks agree (cited, not claimed).
>
> **Net:** no new path to physics; the chapter stays CLOSED, now reinforced by a decisive computation
> (B96). The genuine value is mathematical — the volume ordering, and the located distinction between the
> two trace-map fixed points (trivial→tower; geometric→adjoint torsion/twisted Alexander).
>
> ## Update — 2026-06-06 (post-V78, current at `main` PR #86) — Paper 0: the self-reference grounding
>
> A new **foundational thread** (CC-web handoff, ledger **V76–V78**): characterize the metallic family by
> a *condition* (`m` free) rather than choosing the seed. The motivation ("what is not-nothing → a family,
> not a point") is **quarantined** in `philosophy/METALLIC_FOUNDATIONS.md` — motivation only,
> never a premise/claim, never promoted; the mathematics uses none of it. Suite **230 passed, 1 skip**;
> scan green; proven core P1–P16 untouched; physics closed.
>
> - **B92/V76 — the classification** (`proven`, computer-assisted). Among non-negative hyperbolic
>   unimodular 2×2 matrices, the dominant eigenvalue is purely-periodic-period-1 **⟺ det=−1** (all 66 with
>   entries ≤5) — the family `{M_m=[[m,1],[1,0]]}` up to `GL(2,ℤ)` conjugacy, `m` free. Three equivalent
>   forms; MyCalc-2 (CF-period a conjugacy invariant → companion per trace); refinement (a) (the naive
>   premises admit det=+1, so det=−1 is the operative condition); MyCalc-5 (systole: `m=1` minimal → the
>   member is contingent on a metric).
> - **B93/V77 — det=−1 is exactly the tower's parity** (`proven`/`computer-assisted`). MyCalc-1
>   (`det=−1 ⟺` a negative eigenvalue `−1/λ` ⟺ the `char(−Nᵏ)` sectors); MyCalc-4 (the parity `m→−m`
>   and the field Galois `√→−√` are *distinct* ℤ/2's — corrects the handoff's "Galois = C").
> - **B94/V78 — tower universality DECIDED** (G1; `computer-assisted`, exact SL(3)/SL(4)). Squaring the
>   proved metallic Jacobian to a det=+1 monodromy: `char(J²)` factors **exactly** over the catalog
>   `char(Nᵏ)` (universal) but **every** sign sector `char(−Nᵏ)` and the `(t+1)` vanish ⇒ **"universal
>   catalog, det=−1 parity."** So `det=−1` (B92) is structurally distinguished. G3: degree=rank is
>   det-agnostic (figure-eight is det=+1, B89) ⇒ the tower and degree=rank are two problems.
>
> **Net:** Layer 1 (the classification) is `proven`; `det=−1` is shown structurally distinguished (it is
> exactly the tower's parity condition); the universality question is decided (universal catalog, det=−1
> parity). OPEN: Phase L2 (the Lawvere/renormalization fixed-point attempt — research-level), G2/G4
> (literature grounding), and the Paper 0 write-up.
>
> **Task M (B95/V79) — the degree=rank mechanism** (separate CC-web redirect; replaces the refuted CH
> route of V75). The principal spectrum is **forced** by `tr A=tr A⁻¹=1` (eig 1 at mult n−2): `{1,i,−i}`
> (n=3), `{1,1,ω,ω²}` (n=4), `{1,1,1,−1,−1}` (n=5), **impossible at n≥6**. At n=5 it has `A²=I` ⟹ `A,B`
> involutions ⟹ dihedral ⟹ **reducible** (no irreducible SL(5) principal rep — upgrades B78). So
> **"exponent = rank" is an n∈{3,4} phenomenon**; the mechanism reads whether the cusp's forced
> finite-order spectrum admits an irreducible rep, explaining the n≥5 wall on both the tower and
> degree=rank. Corrects the handoff's SL(5) guess. Full degree classification open.
>
> ## Update — 2026-06-05 (post-V74, current at `main` PR #82) — the "Complete the Tower" run
>
> The CC-web **"Complete the Tower"** handoff was reconciled against `main` (most of it predated V60–V69)
> and the genuine open prizes executed (ledger **V70–V74**). Suite **220 passed, 1 skip**; proven core
> P1–P16 untouched; `EXPERT_OUTREACH.md` dormant; physics chapter stays closed. **Headline: `M⁴=L` is now
> PROVED symbolic-exact at SL(4), and both flagships (the tower, degree=rank) are reduced to one clean
> lemma each with the n≤4 cases proved.**
>
> - **B87/V70 — m=3 genus (Task 3).** The spectral-curve sequence is `3, 1, …` with **m=2 a minimum**
>   (the handoff's hoped-for `3,1,0` is refuted, V34); the m=3 trace-relation curve is **genus 1**
>   (`disc₃=(x²−x−1)(5x²−5x−1)`, squarefree quartic — sharpens V33's loose "≥2").
> - **B88/V71 — SL(4) census (Task 2).** Exactly **two** clean Dehn-filling components at rank 4:
>   `{1,1,ω,ω²}→M⁴=L` (principal, `c=−1`) and `{prim 8th}→M³=L` — **degrees {3,4}**. The degree is the
>   robust invariant; not every bundle rep is on a Dehn-filling component.
> - **B89/V72 — `M⁴=L` PROVED symbolic-exact (Task 1a).** Upgrades V54 (~1e-31) to a theorem over ℚ(ω):
>   eliminating `B` collapses the bundle relations to one matrix equation; `A³=I` gives a 10-equation
>   exact ideal; the rank-drop locus `t11=ω·t22` gives an explicit 4-parameter family on which
>   `[A,B]·det(t)²=−det(t)·μ⁴` is a pure polynomial identity. (Trap banked: the generic gauge slice is
>   `det t≡0`/vacuous; real reps live on the rank-drop locus.)
> - **B89-T/V73 — the tower's cohomological route CLOSED (Task T).** `H¹(F₂;ad ρ)` at the (trivial-rep)
>   fixed line gives `char(M)^{n²−1}≠tower` — a **third dead shortcut** (after B84 numerics, B85 `Λ²V`).
>   Advance: the all-n tower = the explicit **two-sequence Sym product** `∏char(Sym^d M_m)`, verified
>   **symbolic-in-m** = the proved (n≤4)/structural (n=5) tower (B58 had only m=1), reducing it to **one
>   module-isomorphism**; predicts `a₃(n=6)=2` (overruling B66's gauge-corrupted pinv).
> - **B90/V74 — the peripheral form of degree=rank (Task 1b)** — *corrected by the V75 audit (below).*
>   `XμX⁻¹=μA` (L1b) is genuine and proved uniform (the meridian form of the bundle constraint); but L1a
>   `λ=μX⁻¹μY⁻¹` is a **tautology** and "exponent = rank from Cayley–Hamilton" is **REFUTED**. degree=rank
>   stays PROVED only at **n=3,4** (B71, B89); uniform-n is OPEN (not reduced to L1b+CH).
> - **V75 — CC-web audit correction.** The hinge test: both SL(4) Dehn-filling components satisfy L1b and
>   have 4×4 A (CH degree 4) but give different exponents (principal→`M⁴`, secondary `{prim 8th}`→`M³`),
>   refuting "exponent = CH degree = rank." L1a holds on random non-bundle `(A,t)` (a tautology). POSITIVE:
>   B89-T's two-sequence Sym product equals B80's **actual** symbolic `J(m)` char poly at n=4 exactly.
>
> **Net (honest, post-audit):** `M⁴=L` PROVED symbolic-exact (B89); the tower's all-n proof reduced to a
> **GL(2,ℤ)/Sym plethysm** module-iso (B89-T, conjectural, n≤4 confirmed against the real `J(m)`); the
> cohomological route closed. degree=rank is PROVED n=3,4 only and **not** uniformly reduced (B90 = a
> reformulation; only L1b genuine). The tower and degree=rank are TWO problems, not one. OPEN: the tower
> plethysm (rep theory), degree=rank uniform-n (spectrum/root-order, not CH), Paper-0 family
> classification, Task 6 (genus-2). `EXPERT_OUTREACH.md` stays dormant/uncommitted; physics closed.
>
> ## Update — 2026-06-05 (post-V69, current at `main` PR #76)
>
> The **unification push** (ledger **V66–V69**) tied the work into one object — the SL(n) figure-eight
> character variety — and produced a paper skeleton. Suite **201 passed, 1 skip**; proven core P1–P16
> untouched; `EXPERT_OUTREACH.md` dormant.
>
> - **B83/V66 — the `Aₙ` family** `L=(−1)ⁿ⁻¹Mⁿ` (the peripheral A-variety of the principal Dehn-filling
>   component); **SL(4) `L=−M⁴` is NEW** (the first SL(4) figure-eight A-polynomial from the trace map),
>   unifying Cooper–Long(SL2)/Falbel(SL3). Mechanism: exponent = rank = the filling slope.
> - **B84/V67 — I1 refuted.** The SL(5) tower barrier is genuine **non-convergence** of the pinv-limit
>   (even gauge-invariant power sums scatter), not a fixable gauge artifact. The path is symbolic σ.
> - **B85/V68 — the lynchpin reduced.** Λ² functoriality (new, real) does NOT break the degeneracy (a
>   root-system fact); the all-n tower from first principles reduces to one symbolic `e₂/Λ²` closure; no
>   numerical/representation shortcut remains.
> - **B86/V69 — the synthesis + paper skeleton** (`papers/SLN_FIGURE_EIGHT_SKELETON.md`): three threads,
>   one object; novelty positioned (the `Aₙ` family / SL(4) A-poly is `APPARENTLY_NEW`, the #1 external
>   check). Physics chapter stays closed.
>
> **Headline of the push:** the SL(4) figure-eight A-polynomial (`L=−M⁴`) + the `Aₙ` family is the new
> result; the SL(5)+ tower from first principles is reduced to one symbolic step (the `e₂/Λ²` closure).
>
> ## Update — 2026-06-05 (post-V65, current at `main` PR #72)
>
> A follow-on run (ledger **V60–V65**) hardened degree=rank and proved the SL(4) tower from first
> principles. Suite **191 passed, 1 skip**; proven core P1–P16 untouched; `EXPERT_OUTREACH.md` dormant.
>
> - **B80/V62 — the SL(4) metallic tower from first principles** (the headline). `char(J(m))` factors
>   EXACTLY as the Dickson tower over ℚ[m] via the **CRT/F_p** symbolic-m Jacobian (exact F_p ε-series
>   `DT_0(m)` over 5 primes → interpolate in m → CRT + rational-reconstruct → ℚ[m] → `sympy.factor`).
>   Resolves the B70 SL(4) stall; char poly identical to B65; the e₂ two-block closure is automatic.
> - **B81/V63 — SL(5) blocked**: `char(DT_0(5))` scatters across seeds (gauge-corrupt at the
>   doubly-degenerate `char(M²)²` sector — the residual `e₂/Λ²` barrier, B58); SL(4) is seed-invariant,
>   which is why B80 works. The barrier is now precisely localized as char-poly seed-scatter.
> - **B77/V60 — degree=rank refined** to the signed law `[A,B]=(−1)ⁿ⁻¹μⁿ`; the A↔D unification REFUTED
>   (meridian/longitude eigenvalues are generic, not the Dickson roots — degree=rank is peripheral).
> - **B78/V61 — n=5 method-limit** (SL(5) yields only reducible reps numerically); **B79/V64** — the
>   `(m,n)` table: degree=rank `=rank` on every computable cell, even-m + rank-4-metallic cells OPEN.
> - **B82/V65 — consolidation + the physics chapter formally CLOSED** (the 0-for-many record
>   V28/V29/V34/V56/V58 — the kernel is always invariant theory of `sl(n)`, never a 3+1D crossing).
>   degree=rank at SL(3) is KNOWN (Falbel); the general pattern is APPARENTLY_NEW pending an external
>   literature check (the one result most worth checking).
>
> ## Update — 2026-06-05 (post-V59, current at `main` PR #66)
>
> Since the post-V42 block below, two governed exploration runs were banked (ledger **V43–V59**;
> proven core P1–P16 still untouched and test-locked; suite **179 passed, 1 skipped**;
> `EXPERT_OUTREACH.md` dormant/untracked). The work split into two campaigns:
>
> - **Open-paths sweep (V43–V52)** — B71 SL(3) figure-eight A-variety (Fix(T_1²) = 3 components,
>   matches Heusener–Muñoz–Porti / Falbel; Dehn-filling `W1=D2→M³=L`, `W2=D3→M³L=1`); P1 Dehn-filling
>   exact (50-digit); P3 m=2 framing resolved (=m136); P4 SL(4) rank-independent meridian; P5
>   trace-ring scoped; P6 AJ bounded-negative.
> - **Comprehensive Paths A–F mandate (V53–V59)** — the two prizes plus the speculative tail:
>   - **A (V54, B73)** degree=rank tower law CONFIRMED at SL(4) (`M⁴=L` on the principal Dehn-filling
>     component, ~1e-39); SL(2) degenerate, a 2nd SL(4) component gives `M³=L`.
>   - **D (V55, B70)** the symbolic-m ε-series pinv-limit construction BUILT — reproduces the SL(3)
>     tower from first principles (resolves the V51 stall); SL(4) build at L=12 over ℚ is the open
>     continuation (→ the a_d proof at n=4).
>   - **B (V53)** CONFIRMS the V34 j=1728 kill (isolated, silver-mean-forced, no Coulomb family).
>   - **C (V56, B74)** higher-spin/W_N: the parity grading is a LITERAL shared object (−w0 of A_{n−1});
>     spectrum diverges; dynamical reading SPECULATIVE-ANALOGY.
>   - **F1 (V57, B75)** the m-axis of degree=rank — odd metallic bundles m=1,3 give `M³=L` at n=3; a
>     two-parameter `(m,n)` rank invariant (convention-independent `eig[A,B]=eig(t)ⁿ`). Open: even-m,
>     rank-4-metallic corners.
>   - **F2/F3 (V58, B76)** cusp k-set = SU(2)_{k−2} root-of-unity level set (closes B69 reconciliation);
>     no categorical family lift (V28) → SPECULATIVE-ANALOGY. F3 subsumed by V56.
>   - **E (V59, B68)** smarter AJ retry confirms V52 (no clean recursion at |q|=1; literature theorem).
>
>   **Honest headline:** the math is real (degree=rank + the tower factorization + the A-polynomial
>   connection); every physics bridge returned negative or "same Lie algebra / just roots of unity."
>   The two real open continuations both need the **SL(4) ambient trace ring**: the symbolic-m SL(4)
>   Jacobian (D → a_d proof) and the rank-4 / even-m degree=rank corners (A/F1).
>
> ## Update — 2026-06-04 (post-V42, current at `main` PR #48)
>
> The body below is the 2026-06-03 snapshot (ledger V1–V23, PR #26). Since then the **exploratory
> Phase-8 work** has been banked (ledger **V24–V42**; proven core P1–P16 still untouched and
> test-locked). What changed:
>
> - **Physics-paths sweep (V28–V39)** — a systematic probe of every reachable physics anchor, banked
>   in `frontier/physics_probes/` (see its `PHYSICS_PROBES_SUMMARY.md`). Honest headline: **no physics
>   crossing.** The two genuinely-open real-physics targets are closed negative — metallic anyons
>   (V28: categorifiable only at `m=1`, Ostrik rank-2) and SL(n) quasicrystal spectra (V29: the
>   symplectic obstruction, self-adjoint 1D transfer matrices are `Sp(2p,R)`, `SL(n)=Sp` only at
>   `n=2`). The reachable physics (golden anyon, Fibonacci quasicrystal) is special to `m=1`/`n=2`,
>   not general. The Chern–Simons/torsion family (V30/V31) is genuine topology with no clean new
>   pattern; `τ_m` is identified as **Porti's adjoint Reidemeister torsion form**.
> - **m136 / m=2 A-polynomial RESOLVED (V32 Gate-0 + V38 independent fit).** The m=2 trace-map
>   eliminant `M²L²−(M⁴−4M²+1)L+M²` IS the census-m136 A-polynomial (holonomy-match + a from-scratch
>   null-space-dim-1 fit, no Sage). The `j=1728`/CM-by-`Z[i]` spectral-curve thread (V32–V34) is banked.
> - **B69 metallic A-polynomial family + cusp-torsion law (V35/V39/V40)** — VERIFIED m=1..4; the cusp
>   law is a **STANDARD_REPACKAGE** (Baker–Petersen once-punctured-torus-bundle ideal points), not new.
> - **B70 trace-ring attack (V41/V42)** — the SL(n) two-block / `e₂` obstruction is **rank-1 at
>   leading order** (pinned exactly to `e₂=tr(Λ²A)`), and its full closure is a **bounded,
>   finite multi-generator** set (bidegree `≤(3,3)`, by `c=n` nilpotency). The two-block barrier is now
>   a precise finite structure — computer-assisted characterization, **not PROVEN**.
> - **B68 AJ-conjecture probe (shelved, no claim).** Order-match (recursion order 2 = A's L-degree)
>   only; the exact `q=1` identity below B67's bar.
>
> **Open-door updates vs §3 below:** the *m136/m=2 framing* door is **CLOSED-RESOLVED** (V32/V38).
> The **B58-proper `a_d` trace ring** door is **sharpened, not closed** (B70: the obstruction is the
> bounded `≤(3,3)` `e₂` two-index set — the precise remaining content). The **SL(3) figure-eight
> A-polynomial (GTZ)** door remains OPEN (deferred as the more-tractable Track B). The AJ `q=1` and
> SL(5) cotangent-count doors are unchanged. Outreach (`EXPERT_OUTREACH.md`) stays dormant/uncommitted.

## 0. Verdict

Foundation is clean. One branch (`main`), no orphans. The 15-claim proven core (P1–P16, P14
unused) is unchanged and test-locked. All SL(n) trace-map tower work lives in `frontier/`/PC12
with honest labels — **nothing from the tower is masquerading as proven core.** The refuted
formulas (`3n^2-10n+11`, `2(n-2)(n-3)`, `mult(3)=3`/`max(n-d,1)`) have **no surviving assertions
as true** — every occurrence is in a "refuted / corrected-misconception / brief's" context. The
new cotangent-subtraction kill is present and correctly stated. Suite green (141 passed, 1
intentional skip). One trivially-safe fix applied (stale `(uncommitted)` ledger statuses); 4
non-trivial items proposed below. Open doors are all honestly labeled — they are KNOWN, not
resolved.

## 1. Branch inventory

| branch | status | last commit | purpose |
|---|---|---|---|
| `main` | active | `6d3b5f6` (PR #26) | trunk |

After `git fetch --prune`, **only `origin/main` remains.** Every feature branch was merged and
deleted; the work is verified present in `main` (dirs `frontier/B55,B56,B60–B65,B66,B67,B68`,
`papers/candidates/PC12_*`, `paths/E21_*` all exist). Merged via PRs #16–#26 (this-session work)
and earlier-session merges (B55/B56 = c1-structure, B60, E21, pc12-literature, pc12-review-ready).
**No orphaned or abandoned branch.** (The transient pre-prune listing of b61…pc12-review-ready was
stale local remote-tracking refs, now pruned.)

## 2. Claims inventory (proof-status labels)

**Proven core — `CLAIMS.md`, 15 claims, each test-locked** (status labels: proven/conditional/open/dead):
- P1–P6, P8, P10–P13, P15, P16 — exact algebra / standard sieve. Correctly `proven`.
- **P7** — "Sympy-verified" exact gluing identity. `proven`; *computer-assisted-exact* (defensible).
- **P9** — figure-eight / m003 census data (vol, H1, CS, amphichirality). `proven`; *SnapPy/known-facts,
  software-verified* (these are established census facts, but the label rests on software + literature,
  not a hand proof). **FLAG (mild):** label as software-verified census data.
- Conditional: **C1, C5** — correctly `conditional` (axioms motivated, not forced).
- Field-theoretic lift (P15/P16 → field equation, B6–B9) — explicitly **"conjectured, not proven."** Correct.

**Frontier ledger (`VALIDATION_LEDGER`, V1–V23)** — labels reviewed; the SL(n) tower rows are
correctly qualified:
- V14 (B63) "**PROVEN (computer-assisted, over Z[m])**" — correctly qualified (good template).
- V16 (B65) "SYMBOLIC FACTORIZATION (computer-assisted entries)" — correct.
- V17 (B66) "REFUTED (numerical, high-precision)", V19 "VERIFIED (numerical, multi-axis)" — correctly numerical.
- V20 (B67) "VERIFIED (exact derivation)" — exact symbolic, correct.
- V21 (B58) "DEAD (route closed) + VALIDATED (cross-check)" — correct.
- V22 "VERIFIED (symbolic corollary)", V23 "CONSTRAINTS + NO-GO + OPEN" — correct.
- **FLAG: V15 (B64) "PROVEN (symbolic)"** — sympy-verified symbolically for SL(3) and applied as a
  *structural mechanism* (depth-n CH + P=contragredient + Dickson parity) for general n. The general-n
  statement is the mechanism, not a complete hand proof; the bare "PROVEN" mildly overstates it.
  **Proposed** requalification below.

No tower result (B59–B68) is labeled `proven` in the core; all are frontier/PC12 with qualified labels.

## 3. Open doors (located, honestly labeled — KNOWN, not resolved)

| door | status | what closing it takes |
|---|---|---|
| **B58 proper** — `a_d` multiplicities via exterior-power / multi-block (`e_j`, `Λ²V`) CH recursion | OPEN. The cotangent-subtraction and Sym^{2k}/principal-SL(2) routes are CLOSED (B58 Stage 1, V21); the hand proof is the remaining path. | The Λ²V multi-block trace-ring recursion (a from-first-principles symbolic derivation). |
| **m136 / m=2 framing** (overnight Job 3) | OPEN/INCONCLUSIVE. m=2 monodromy `[[5,2],[2,1]]=R^2L^2` bundle = census m136; the B67 (figure-eight) framing does not transfer (best framing residual ~6e-3). | The correct meridian/longitude framing for m≠1, or a symbolic elimination as in B67. |
| **Boundary-unipotent SL(3) figure-eight A-polynomial (GTZ)** (Job 2) | OPEN. The principal Sym^2 lift is the WRONG SL(3) component (NO-GO: nullity unstable 3/3/5/4); the geometric component is boundary-unipotent. | Build boundary-unipotent SL(3,C) reps and compare to Garoufalidis-Thurston-Zickert. |
| **AJ q=1 recursion limit** (Job 6, shelved) | OPEN. The colored Jones has a minimal order-2 recursion (= A's L-degree), but the exact `recursion|_{q=1} = A` identity is unresolved (convention M_rec=q^N=meridian^2; q→1 nullspace ill-conditioned). | The exact q-deformed recursion coefficients + a careful q=1 limit. |
| **SL(5) cotangent full count** (B58 n=5) | PARTIAL only: dim ≥ 111 at deg≤11, single prime, still rising — NOT a validated count. | Cyclic-word / Procesi reduction (brute-force `2^d` words to degree ~14 is memory-infeasible). |
| **PC12 Thm 4** (fixed-line integer splitting) | OPEN (external): `APPARENTLY_NEW`, specialist read pending (V12). | An independent character-variety / algebraic-dynamics specialist evaluation. |

Test "skips" are NOT open doors: `RUN_SLOW` (n=4 recompute) is an intentional opt-in;
`test_snapdata` uses `importorskip("snappy")` (SnapPy is installed, so it runs).

## 4. Consistency check (refuted claims + conventions)

- **`3n^2-10n+11` / excess `2(n-2)(n-3)`** — NO surviving assertion as true. All 8 hits are in
  corrected-misconception / "brief's" / refuted context (B58 FINDINGS, CHANGELOG, PROGRESS, ledger
  V21, step1_cotangent.py). ✓
- **`mult(3)=3` / `max(n-d,1)`** — NO surviving assertion as true. All hits labeled REFUTED (B66
  FINDINGS/README/VALIDATION/probe, CHANGELOG, PROGRESS, ledger V17/V19/V23, frontier/README). ✓
- **Parity-sign / pre-correction tower** — the SL(2)/n=2 parity correction `(t-1)→(t+1)` (V18) is
  consistent everywhere; the DRAFT_NOTE n=2 row reads `(t+1)`; no surviving n=2 `(t-1)`. The B66
  "9 odd-k / 6 even-k" relabel to root-HEIGHT (V18) is consistent across B66 docs + ledger. ✓
- **Probe-3 terminology** — the forward guard is present and correct in CHANGELOG (L301-302) and
  PROGRESS_LOG (L1931-1932): "`Σ|k|` spectral weight, NOT topological entropy (= n·log μ, linear);
  no n^2 scaling, no fixed antisymmetric fraction." No entropy-mislabel survivor. The PC12
  "algebraic entropy = log μ_m" (Bellon-Viallet, = log spectral radius) is the LEGITIMATE,
  distinct notion — no conflict with the guard. ✓
- **Stale (not contradictory) statuses found** — see punch-list: 11 ledger rows carried
  `(uncommitted)` though merged (FIXED); PC12 docs predate B58/B66/B67 (stale, not contradictory;
  PROPOSED update).

## 5. Test / suite state

- **142 collected; 141 passed, 1 skipped.** Suite green.
- Coverage: proven core P1–P16 (`test_algebra`…`test_derived_potential`, `test_uniqueness_theorem`,
  `test_snapdata`); the tower B61–B68 (`test_b61_sl5` … `test_b67_figure_eight_apolynomial`,
  `test_b58_stage1`); PC12 (`test_sl3_metallic_trace_maps`, `test_sl3_symbolic_m_factorization`,
  `test_pc12_draft_skeleton`, …); public-surface scan (`test_public_surface_scan`, 3 checks).
- Skips: `test_b58_stage1::test_n4_recompute_dim_30` (opt-in `RUN_SLOW`, ~40s); `test_snapdata`
  guarded by `importorskip("snappy")` (SnapPy 3.3.2 installed → runs).
- Forbidden tokens: `test_public_surface_scan` passes; no AI-assistant / surname hits in
  tracked surface. "Origin Axiom" in math code: the only hits are `from origin_axiom import …`
  PACKAGE imports in the OLD physics probes (B1/B5/B6/B8/B9) — legitimate code (the proven-core
  package is named `origin_axiom`), NOT promotional framing; the trace-map probes B48–B68 are clean.

## 6. Kill-ledger coherence

`docs/atlas/FAILURE_ATLAS.md` is a prose-category obstruction map; **there is no `#N` kill-counter
convention** in the repo (the "#25/#26/#27" numbering is external/informal — recorded here so it is
not mistaken for a repo invariant). Documented kills/obstructions: source-free-zero, commutative
cancellation, selector/measure/units-inserted, gauge/particle-dictionary-missing, 3+1D-bridge-missing,
observable-missing, numerology-killed-by-controls, **figure-eight I=1/4** (B56, ledger V4 DEAD),
**Aubry self-duality at λ=m** (B57, ledger V7 DEAD), **fixed-line Jacobian needs the ambient trace
map (SL(n)≥4)**, and the **NEW "Cotangent-Subtraction Route To The Tower Multiplicities — CLOSED"**
(B58, present and correctly stated, reinforcing: the Sym^{2k}/principal-SL(2) decomposition is dead
from the multiplicity side too, and the numerical rep-perturbation tower is exhausted at n≥6 by gauge
degeneracy). **No kill silently revived;** the ledger DEAD/route-closed rows (V4, V7, V21) match the
atlas.

---

## Punch-list

**APPLIED (trivially-safe):**
- [x] `VALIDATION_LEDGER`: 11 stale `(uncommitted)` commit-statuses → `(merged)` (branches verified
  deleted, work present in `main`). Stale text only; no claim content changed.
- [x] Verified the Probe-3 forward guard is present and correct (no edit needed).

**PROPOSED (non-trivial — NOT applied; review before changing):**
- [ ] **V15 (B64) label.** Requalify "PROVEN (symbolic)" → e.g. "computer-verified symbolic for
  SL(3); structural mechanism for general n" — the general-n statement is the mechanism, not a
  complete hand proof. (Claim-status judgment; do not silently downgrade.)
- [ ] **PC12 docs** (`DRAFT_NOTE.md`, `PAPER_CARD.md`, `FALSIFIABILITY_MATRIX.md`,
  `LITERATURE_POSITIONING.md`). They predate B58/B66/B67 and do not mention: the SL(6) multiplicity
  result (`|k|=3 = 2`, `max(n-d,1)` refuted, B66), the figure-eight A-polynomial derived from the
  trace map (B67), or the cotangent-route closure (B58). Stale, not contradictory — propose folding
  these into the PC12 appendix/positioning before any external hand-off.
- [ ] **CLAIMS.md "Last updated 2026-05-29"** — refresh, noting the proven core (P1–P16) is unchanged
  through all B58–B68 frontier work (so the date lag is not claim drift; a one-line note suffices).
- [ ] **CLAIMS.md P7/P9 provenance** — optional footnote that P7 is sympy-verified and P9 is SnapPy /
  census data (software/literature-verified), to keep the "proven" basis explicit. Minor.

**No premature closes:** every open door in §3 is left open and labeled; the goal was to KNOW them.
