# Changelog

All notable changes to the Origin Axiom repository are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/); this project is pre-1.0 and
not yet versioned for release. Detailed working history lives in `PROGRESS_LOG.md`.

---

## [Unreleased]

### Changed
- **Intellectual-architecture reorganization (2026-06-07; docs/org only, no math).** Introduced four governed rooms
  for the evolving speculative ideas, all firewalled (nothing promotes to `CLAIMS.md`; the physics chapter stays
  CLOSED; the mathematics never cites them): **`speculations/`** (the catalog `S001…S021` with a proof-status enum
  incl. `HELD(value-matching)`, the "final theory" exercise `PHYSICS_EXERCISE.md`, per-live-speculation files, the
  DEAD `TOMBSTONES.md`, and `archive/`); **`philosophy/`** (`GOVERNANCE` + `P000–P003` + the migrated `P1–P5`
  register + `METALLIC_FOUNDATIONS`); **`story/`** and **`knowledge/`** (per the priority order); and the one-page
  `ARCHITECTURE.md` (the one-way firewall arrow). **Migration:** `paths/philosophical/{PHILOSOPHICAL_PATHS,
  METALLIC_FOUNDATIONS}.md → philosophy/`; `paths/philosophical/{PHYSICS_RESONANCES, COSMOGONY_FROM_THE_VOID}.md →
  speculations/archive/` (COSMOGONY superseded by the corrected `PHYSICS_EXERCISE.md` — notably the κ=−2 cusp fix
  and the HELD tier). All **live** references redirected (frontier firewall banners, READMEs, REPO_STATE, atlas,
  this file, the repo-map); append-only `PROGRESS_LOG.md` history and historical ledger rows left intact, with a
  migration mapping recorded in `PROGRESS_LOG.md`.

### Added
- **Physics-bridge sweep, Phase 1 — the metallic means are distinct real quasicrystals (2026-06-07, Ledger V108;
  FIREWALLED, no physics promotion).** A brave-but-honest sweep of the bridges to physics. First the **terrain map**
  (`speculations/PHYSICS_BRIDGE_MAP.md`): every bridge classified DEAD (masses/Λ/spacetime/holography/anyons/
  SW-family/SL(n≥3)-Hermitian-chain/tower=Kostant — do not revive), LIVE, or HEAVY. Then the Phase-1 live result
  (`frontier/physics_probes/metallic_spectra.py`, S023, `TESTED-POSITIVE`): the SL(2) Hermitian metallic
  quasicrystals (golden m=1, silver m=2, bronze m=3) are **arithmetically distinct real materials** — the
  gap-labeling module lives in `ℚ(√(m²+4))` = `ℚ(√5),ℚ(√2),ℚ(√13)` (three distinct fields), with distinct RG scale
  `φ_m` and spectral dimension — **even though** the tower *algebra* (the Sym two-sequence `μ_d`) is m-universal
  (B120). The algebra is one object; the physics is a family of distinct, buildable materials. **Honest scope:** 1D
  condensed matter, **not** fundamental physics; the SL(n≥3) extension is blocked (non-Hermitian). Firewalled;
  nothing to `CLAIMS.md`; the physics chapter stays CLOSED; P1–P16 untouched.
- **B120 — the trivial-point tower is determined by `(n; trace, det)` (2026-06-07, Ledger V107; no physics).**
  Banks the Chat-2 exploration interlude (Q2/Q3) + the computed Supplement (S1–S5), verify-don't-trust. The
  `(n²−1)`-dim tower (the Sym two-sequence, B117/B103) is **one object** fixed by two inputs — the unfolding depth
  `n` and the abelianization seed `(trace, det)`. **Q3:** distinct same-`(trace,det)` integer matrices give
  identical towers. **S2 (the deep lead):** the Sym content `μ_d` is m-independent — the `μ_d` are plethysm
  multiplicities of the `GL(2,ℤ)`-rep `ρ_n`, trace-blind; this **reframes the prize as a plethysm** but is a
  *reduction, not a closure* (proved n=3,4; same trace-ring wall). **Q2:** degree=rank **splits** — (I) spectral
  `char(Mⁿ)` factor ⟺ `μ_n=1`, all n / (II) geometric longitude=meridianⁿ, n∈{3,4} (order `{4,3,2,∞}`) — dissolving
  the apparent B117-vs-B119 tension. **Three corrections** (verify-don't-trust): S1's `(n²−3n)/2` → `(n−4)(n+1)/2`
  (the doubling band forced); S5's `2·max(1,n−h−1)` guess refuted **and** a closed form found (heights run 0..n:
  `count(n,0)=n−1`; `2(n−2)` h∈{1,2}; `2(n−h)` 3≤h≤n−1; `2` h=n); S4 confirms B116 is factor-level (the Chat-2
  "n=3 divergence" was a units error). **Governed-folder banking:** `knowledge/K008` (the determination explainer),
  `philosophy/P004` (expansion is interaction-born — `M_m=(twist)ᵐ·(swap)`, the SL(2,ℤ) finite-order-generation
  spine), and the **downgrade** of the Markov-blanket / boundary-open reading to low-rank n∈{3,4} (TWO_SYMMETRY_FRAME,
  S022). The all-`n` prize is unchanged and un-fused: prove the Sym two-sequence `μ_d` (B103), now seen as a plethysm.
- **B118/B119 — the sign-half gate closed + the power-half sharp negative (2026-06-07, Ledger V105–V106; no
  physics).** Chat-2's Path 1 (the gate) and Path 3 (the hard path). **B118 (V105):** B112 proved the `(+1,−1)`
  eigenspace *dimensions* of `θ=−w₀` on the height-`h` roots by a permutation argument; the `⌈`-vs-`⌊` tip is
  decided by the sign θ carries on the lone fixed root (odd `m=n−h`). Path 1 asked whether that sign is `+1` for
  all `(n,h)` (which would make B64 a uniform "`+1` sector = `char(M^h)`" theorem). Realizing θ as the genuine
  *signed* contragredient involution `τ(X)=−J Xᵀ J⁻¹`, the **fixed-root sign `= (−1)^{h+1}`** (symbolic + verified
  `n≤12`) — `+1` for odd `h`, `−1` for even `h`: **NOT a uniform +1.** So B64's "`+1` sector = `char(M^h)`" holds
  only for odd `h` — a **refinement/correction** of B112's unsigned "fixed root is always +1". The `(⌈,⌊)`
  dimensions stand; B112's `char(M^h)=⌈` labeling stays tower-verified `n≤5` (B118 supplies the all-`n` sign).
  Emergent (non-circular): the fixed-root sign `= +1` ⟺ the inversion identity `char(M^{−h})=char(−M^h)` ⟺ `h`
  odd. The θ-split is **not the tower** (the Sym two-sequence, B117; diverges `n≥6`).
  **B119 (V106) — a sharp negative:** `Mᵏ` central on the principal iff `order(a)|k` (`a+1/a=3−n`,
  `order(a)={4,3,2,∞}`); `k=n` is non-central where the principal exists (n=3,4) but **not unique** ⇒ centrality
  does **not** force `k=n` (the proved A-poly B83 pins it), and for **n≥5 the principal does not exist
  irreducibly** (B95) ⇒ `exponent=rank` is an `n∈{3,4}` phenomenon; the brave `k=n` proof cannot be completed. The
  secondary 2n-type gives exponent `n−1` (extends B111). Emergent (B111 ADD2 correction): the cusp order is
  `{4,3,2,∞}`, not a clean `{n−1,n+1,2n}` law (B111 ADD2 conflated three components). The all-`n` tower stays the
  prize = prove the Sym two-sequence `μ_d` (B103).
- **B117 — the interleaving insight: the tower is the Sym two-sequence; the "promotion" is a `Sym¹` absence
  (2026-06-07, Ledger V104; no physics).** The **headline reframing** of the B111–B116 run (the Opus interleaving
  insight, verify-don't-trust). The `(n²−1)`-dim trivial-point tower is **one object** — the **Sym two-sequence**
  (B103/B58) — not two separable halves (sign + power). A **dimension identity**
  `(n+1)(n+2)/2 − (n²−1) = −(n−4)(n+1)/2` (roots `{−1,4}`) **derives** B103's `μ_d = [2≤d≤n]+[0≤d≤n−3]` (n=4 the
  unique perfect fit; n=3 omits `Sym¹`, the unique subset `{0,2,3}`; n≥5 doubles `Sym²..Sym^{n−3}`). So **the
  "promotion" is a `Sym¹` absence** — the B111/B113 "two-halves"/"promotion" framing is **superseded and
  tombstoned** (the height-1 `char(−M)` at n=3 is `Sym³`'s contribution, not a "promoted `Sym¹`"). **degree=rank's
  `char(Mⁿ)` = `Sym^n` presence** (`μ_n=1` ∀n; dim-forced only at n=3 — *not* "by dimension"; rep-theory n=2,4;
  two-sequence form n≥5). `Sym⁰..⁴` product = the B80 proved n=4 tower. **B112 relabeled to three tiers** (the
  `−w₀` multiplicity structure up to the fixed-root label — proved all n; the labeling = B64, pending B118; the
  tower realization with powers — verified n≤5, superseded). **Re-aimed prize:** prove the **Sym two-sequence
  `μ_d`** for all n (B103's open problem).
- **B116 reconciliation + a CORRECTION to B112 (2026-06-07, Ledger V103; no physics).** The B112↔B103
  reconciliation (run to join the prize's two halves) found a **verify-don't-trust correction** instead: the
  **Sym two-sequence (B103) = the actual tower** (it matches the resolved SL(5) and carries `char(Mⁿ)`
  automatically), while the **θ-split (B112) = the tower only `n ≤ 5`** and **diverges at `n=6`** (the banked
  V26/V27). **B112's "sign half proved for all n" is explicitly downgraded to "n ≤ 5"** (the combinatorial lemma
  stands for all n; the *tower-identification* — the V25 gap — holds only n≤5). The all-`n` sign half is **OPEN**;
  the live route is the **Sym two-sequence** proof (B103), the better tower-candidate.
- **The ρ_n sign half PROVED + the five follow-on paths — B112–B115 (2026-06-07, Ledger V99–V102; no physics).**
  **B112 (V99) — the headline:** the **sign half of `ρ_n` is proved for all n**, engine-free — an elementary
  root-system reversal lemma (`θ=−w₀` acts as the reversal on the height-`h` roots of `A_{n−1}`, `(+1,−1)`
  eigenspace dims `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)`, verified all n≤12) × the banked B64 parity assignment ⇒
  `mult char(M^h)=⌈(n−h)/2⌉`, `char(−M^h)=⌊(n−h)/2⌋`. The first catalog piece proved from first principles for all
  n. **B113 (V100):** the proved closed form **resolves the SL(5) sign sectors** at heights 2–4 by proof
  (including `char(M²)²·char(−M²)` = B62's two gauge-corrupted modes the eps-series could not resolve), and
  **localizes degree=rank to height-1 + `char(Mⁿ)`** (the promotion is n-dependent — the power half stays open).
  **B114 (V101):** the covering-degree mechanism is **TESTED-NEGATIVE** (full covering degree `~k^{n−1}`, not `k`).
  **B115 (V102):** the known SL(4) Dehn-filling reps are forced-locus (like SL(3)); off-locus SL(4) + genus-2
  degree=rank scoped **OPEN** with named obstructions. **State of the prize:** the sign half is proved (all n);
  the open piece is the **power half** (the single degree=rank promotion `char(M)→char(Mⁿ)`, localized to the
  height-1/top-power interface).
- **B111 — the tower's sign structure + the degree=rank exponent (2026-06-07, Ledger V98; no physics).** The
  "sign findings" handoff. The opposition-involution all-heights **closed form** (`⌈(n−h)/2⌉` / `⌊(n−h)/2⌋`,
  matching B62 height-2) is **not** the proved tower: `Tower(n) = [closed form, heights 1..n−1]` with **exactly one
  `char(M¹)` promoted to `char(Mⁿ)`** (verified n=3,4) — the single non-bulk piece being `char(Mⁿ)` = the
  **degree=rank** top power. So the tower's **sign half is closed-form** (bulk θ); the only open piece is the
  degree=rank promotion (peripheral). **ADDITION 1 (proved):** on the SL(4) secondary `M⁴=−1` is scalar ⇒ `k=4`
  algebraically impossible (`k=3` forced); on the principal `M⁴` non-scalar ⇒ `k=4` allowed (`k=n` not proven).
  **ADDITION 2:** cusp orders `{n−1,n+1,2n}`; the `ord−1` formula TESTED-NEGATIVE. SL(3) parity corrected to
  `(t−1)(t−det N)`. Opens two leads (`speculations/S022` peripheral ℤ/4 + `TWO_SYMMETRY_FRAME`); `s_n↔c` DEAD.
- **The Final Computation Arc — B108/B109/B110 (2026-06-07, Ledger V95–V97; no physics).** **B108 (V95):** the
  top-priority `θ=−w₀ → c` derivation — the mandatory **hinge fails**; `θ` is an involution (order 2) and predicts
  the order-`≤2` Dehn-filling scalars `c∈{1,−1}` but **not** the order-4 secondary `c=i`, so degree=rank's `c`
  stays **OPEN** (missing a `ℤ/4` ingredient; cusp-spectrum candidate, B95). `θ` *is* confirmed a tower symmetry
  (`[P,J(m)]=0`). **B109 (V96):** the trace-map dynamics at the void (D2) — verify-don't-trust corrected the
  handoff's coordinate-axis facts to the rigorous linearization (`DT₁²` eigenvalues `{1,φ⁴,φ⁻⁴}`; the void's
  center manifold = the tower's root-of-unity parity sector, dim 1@SL2/2@SL3; a (2,1) `κ` saddle) + L5 literature
  (degree=rank `Mⁿ=L` apparently new; the `W₄` anchor real but generic). **B110 (V97):** the off-locus irreducible
  sector of `4₁` at SL(3) is **EMPTY** (HMP's three components all on the forced locus); the higher-rank fork stays
  open. Plus the **dead-ends register** (`docs/atlas/FAILURE_ATLAS.md`: ~30 kills by pattern, REVIVABLE lens) and
  probe updates **S001** (all-`m` amphichiral PROVED), **S006** (Bell → TESTED-NEGATIVE).
- **B107 physics-connection audit — banked as a NEGATIVE (2026-06-07, Ledger V94; POSTULATED/FIREWALLED).**
  Banks the CC-web physics exploration as a first-class **dead-end log**; *all* physical readings are
  **POSTULATED and firewalled** to `speculations/archive/PHYSICS_RESONANCES.md` (Path 8), **nothing to
  `CLAIMS.md`**, the physics chapter stays **CLOSED**, P1–P16 untouched. **A (anchor, verified):** the SL(2)
  metallic trace map `φ_m: a→aᵐb, b→a` **is** the Kohmoto–Kadanoff–Tang / Fibonacci-Hamiltonian trace map —
  `tr[A,B]=x²+y²+z²−xyz−2` (Sütő/Fricke–Vogt) conserved ∀m (symbolic m=1..4), `φ_1=(z,x,xz−y)`. **B (the
  headline negative, verified):** every SL(3) `m=1` tower eigenvalue is `±φᵏ` — **one geometric scale `log φ`**;
  a mass spectrum is a Hessian, not one ratio, so the tower is **re-presented moduli-space monodromy, not new
  physics**. **C:** the tower/torsion `=` masses/dimensions identifications are **withdrawn category errors**
  (only the moduli-space `M_SUSY ≅ M_flat` + three-branch ↔ three-fixed-point map is citable). **D:** citations
  confirmed (GKLP 1305.0937; DGG 1108.4389, 1112.5179). **E:** the one open fork = the off-principal
  multichannel reps. Reproduced (`quasicrystal_anchor`, `tower_roots_are_golden`); locking test; FINDINGS A–E.
- **B106 Dehn-filling anatomy + hygiene (2026-06-07, Ledger V92/V93; no physics).** The trace map at the
  never-computed **third** fixed-point class (Dehn-filling reps, after trivial=tower and geometric=torsion).
  **D1:** three classes, three distinct Jacobian signatures — Dehn-filling **partially elliptic** (SL(3)
  `(1,1,6)`, SL(4) `(4,4,7)`, root-of-unity neutral eigenvalues); honest negative — the stability *type* does
  not encode the degree=rank exponent. **D4:** `Lᵢ=c·Mᵢ^k` per eigenvector (`c` a root of unity). **D3:** `M⁴=L`
  / `M³=L`, conjugates absent. **[V93 hygiene]** the D1 root-of-unity values pass the **B84 gauge-noise gate**
  (seed-stable); the D4 **principal** (`c=−1`) **corroborates** the proved B89/B83 (not new), the new content
  being the **secondary** (`c=i`, numerical), **SL(3) W2**, and the **per-eigenvector method**.
- **B105 three-obstacle correction + sharpened ρ_n target (2026-06-07, Ledger V91; no physics).** A further
  explicit downgrade of B105's "one collision is the common root cause": **n=5 is a structural threshold
  where three *distinct* `A_{n−1}` obstacles degenerate** — degree=rank (B95, eigenvalue `−1`, `A²=I`), the
  tower/eps-series doubling (B62, golden `char(M²)²` from the A₄ height-2 `θ=−w₀` (4,2) split), and trace-ring
  non-closure (engine-free, onset n=4) — different eigenvalues (`−1` vs `φ²`), independent derivations,
  different onset. The open `ρ_n` target is **sharpened**: prove `char(ρ_n)=catalog` by reproducing the
  opposition-involution multiplicities directly from `ρ_n`, the contested n=5 piece being *only* B62's
  `char(M²)²` (the degree=rank `−1` and trace-ring non-closure are separate, untouched problems). The n=4
  scope claim is hedged. Verified (`three_obstacle_distinction()`); banked in B105 (`CORRECTIONS_V91`).
- **The n=5 wall + the ρ_n convergence, with the V90 audit (2026-06-07, Ledger V89 + V90; suite 278+ pass, 1
  skip; no physics).** `frontier/B105_n5_wall_and_convergence/`: the "n=5 Resolution" handoff, then **two
  explicit inference downgrades (V90)**. **N5:** the SL(5) eps-series resolves **21/24** Dickson factors, the
  resolved 21 are **universally catalog-consistent** (across seeds and monodromies); the 3 unresolved are
  supported as `Sym²` by **structural routes** (B62/B89-T/B103). **[V90 Correction A]** the seed-variation of
  the 3 unresolved factors is the eps-series rank-deficiency signature (B84), **uninformative** about the
  truth — so the explicit **n=5 catalog is OPEN** and a structural deviation there is neither ruled in nor
  out (the earlier "coordinate artifact, not structural / formula-doesn't-change" inference is **withdrawn**).
  **[V90 Correction B]** there is **no proved "natural boundary at n=4"** — `char(J(n))=catalog` is a class
  function for **all `n`** (B103); n=4 is a *methodological ceiling*, not a theorem (the earlier "complete at
  n=4 with a proved boundary" is **withdrawn**); the cusp collision is a *candidate* root cause. **Convergence
  + open frontier:** the project converges on one object `ρ_n` (the `GL(2,ℤ)`-rep on the SL(n) trace ring),
  fully characterized n=3,4, **explicit n≥5 OPEN** — the live target being to prove `char(ρ_n)=catalog`
  directly from `ρ_n` + B62's multiplicities. Literature L1 (GKLP 1305.0937) + L4 (Bonahon–Dreyer 1209.3526 /
  Douglas–Sun 2011.01768) cited; H1–H6 / C1–C4 tabulated; physics quarantined.
- **The Dehn-twist route: SL(4) universality + the SL(5) wall (2026-06-07, Ledger V88; suite 274 passed, 1
  skip; no physics).** `frontier/B104_dehn_twist_tower/`: executes the "Dehn-Twist Route" handoff in full —
  build any monodromy's trace map by composing the elementary twists `U,L,S` inside the eps-series (not the
  Procesi ring, the B85 wall). **SL(4) (proven):** the GATE reproduces B80's metallic tower; `J` factors
  through `N`; `char(J(N))` = the two-sequence catalog with **det-sign parity** for **metallic and
  non-metallic** `N` (e.g. `U²L=[[3,2],[1,1]]`, det +1) — the explicit SL(4) catalog is a computed theorem.
  **SL(5):** the engine inherits the eps-series gauge degeneracy (`char(J)≠catalog`, **21/24 Dickson factors
  resolve**, the doubly-degenerate sector, B61/B66) — a **computational** wall, not a rep-theory failure; the
  n≥5 obstruction is isolated to the eps-series degeneracy. Cite B103, B80, B61/B66, Lawton/Procesi.
- **The SL(n) tower as a GL(2,ℤ) representation (2026-06-07, Ledger V87; suite 269 passed, 1 skip; proven
  core P1–P16 untouched; no physics).** `frontier/B103_tower_equivariance/`: a **fourth route** to the
  metallic tower, synthesizing two CC-web handoffs. **Route 1 (universality, all n):** `J_φ(n)` factors
  through the abelianization `N ∈ GL(2,ℤ)` ⇒ `ρ_n` is a `GL(2,ℤ)`-rep ⇒ `char(J)` is a **class function =
  the catalog**, universal for metallic **and non-metallic** monodromies; **det-sign parity** sharpens B94
  (verified at SL(3) via the exact Lawton maps `U,L,S`). **Route 2 (n=3,4 exact over ℚ[m]):** an explicit
  `m`-independent invertible `P` with **`P·J(m)·P⁻¹ = ⊕_d Sym^d(M_m)^{μ_d}`** (intertwiner dim `=Σμ_d²`
  Schur), realizing the module-iso **(M)** constructively + exactly for n=3,4; sign sectors = `det=−1` twists.
  **Reframing:** the all-n tower = **decompose the `GL(2,ℤ)`-rep `ρ_n`**; universality structural (all n),
  explicit `μ_d` open n≥5 (the Procesi wall) — continuation B104. Cite B94, B85/B89-T, B80, Lawton, Procesi.
- **The W1/W2 dichotomy + the R4 boundary-controlled cubic continuation (2026-06-06, Ledger V86; suite 263
  passed, 1 skip; proven core P1–P16 untouched; no physics).** `frontier/B102_hitchin_continuation/`: two
  follow-ons to B101, verified before landing. **D1:** Cayley–Hamilton on `T₁²` forces every irreducible
  `Fix(T₁²)` SL(3) character into Case I (`trA=trA⁻¹`, self-dual) or the `trB=trB⁻¹=1` branch (0 "neither").
  **D2/D3:** realizing B71's components, **W1→`ρ(a)` elliptic `{1,i,−i}`, W2→`ρ(b)` elliptic** ⇒ **not
  Hitchin** (the genuine non-`Sym²` components are excluded by **ellipticity**, the cleaner obstruction; V0's
  geometric rep by complexity, `Q(√−3)`). **D4:** the `{1,i,−i}` spectrum = Task M's `n=3` spectrum (B95).
  **D5:** the boundary-controlled cubic family keeps the cusp real **only to first order** — generic
  second-order complexification; the handoff's `t*≈3.775` geodesic boundary does **not** reproduce
  (ray-dependent); the unipotent-preserving continuation is `open`. Cite Heusener–Muñoz–Porti, Labourie,
  Hitchin/Fock–Goncharov/Goldman/Marquis.
- **The Hitchin-component reframing (2026-06-06, Ledger V85; suite 256 passed, 1 skip; proven core P1–P16
  untouched; physics chapter stays CLOSED; physics chain firewalled).** `frontier/B101_hitchin_reframing/`:
  the geometric component V0 (B71, `Sym²` of the Fuchsian `SL(2,ℝ)` rep) **is the Fuchsian locus of the
  `SL(3,ℝ)` Hitchin / Fock–Goncharov positive component** of the once-punctured torus. **R1** (`STRUCTURAL`):
  the Anosov hallmark + the unique `SO(2,1)` form, signature `(2,1)`. **R2** (`dead`): the symmetric-space
  ladder — the principal `SL(2)` lands in split real forms; Lorentzian only at `k=2`, does not climb ⇒ **no
  tower of spacetimes** (kills the "3+1D at SL(3)" idea structurally). **R3**: `sl(3)=V₂⊕V₄`; `V0={cubic=0}`.
  **R4** (genuinely-new): `H¹(F₂,sl(3)_Ad)=8` splits `3⊕5` (Teichmüller ⊕ cubic) + an explicit Anosov
  deformation leaving V0 and breaking the `SO(2,1)` form. The Hitchin→Higgs→geometric-Langlands→N=4 SYM
  chain (Kapustin–Witten) is **cited context only** (`PHYSICS_RESONANCES.md` Path 7) with the ceiling stated
  (N=4 SYM, *not* the Standard Model / gravity / the universe); three dead-thread heuristics recorded in
  `docs/atlas/FAILURE_ATLAS.md`.
- **Geometry-invariants + literature-bridge pass (2026-06-06, Ledger V80–V84; suite 249 passed, 1 skip;
  proven core P1–P16 untouched; physics chapter stays CLOSED; physics interpretation quarantined).**
  "Compute the numbers, quarantine the interpretation" — bounded quantum-topology invariants on the
  metallic mapping-torus manifolds, banked as mathematics; every physics reading lives only in
  `speculations/archive/PHYSICS_RESONANCES.md` (`SPECULATION`, never promoted).
  `frontier/B96_geometry_invariants/` (V80): metallic volumes strictly monotone (`2.030<3.664<4.814`,
  `m=1`=systole); the volume Hessian is **definite `(0,2)`, NOT Lorentzian** (155/156 fillings of `4_1`
  below `V₀`) — the most-leveraged physics path returns negative.
  `frontier/B97_sl2r_lorentzian/` (V81): the `(2,1)` Lorentzian form is **located** as the
  `so(2,1)=sl(2,ℝ)` gauge algebra on the SL(2,ℝ)/Teichmüller component (toy 2+1 gravity) — structural, not
  emergent; the 3+1 wall untouched.
  `frontier/B98_geometric_jacobian/` (Probe 1, V82): at the **geometric** rep (not the trivial fixed line),
  `char(D T₁²)=(t−1)(t²−5t+1)` = the **adjoint torsion `τ₁=−3`** (twisted Alexander), **NOT** the Dickson
  tower — so the tower is a trivial-rep phenomenon (*consistent with* Daly arXiv:2411.04431 + 3d-3d, cited);
  tower ≠ Kostant branching.
  `frontier/B99_geometric_jacobian_sl3/` (Probe 1c, V83): the SL(3) geometric Jacobian is torsion-type
  (the `c=5` SL(2) torsion pair carried by `Sym²`), not the SL(3) tower.
  `frontier/B100_literature_crosscheck/` (Probes 2+6, V84): the Zickert/SnapPy **Ptolemy variety** of `4_1`
  (2 obstruction classes, 6 trivial-class reps) cross-validates B71 from an independent code path, and the
  **Baker–Petersen** (arXiv:1211.4479) twisted Alexander **is** the B98/B99 geometric Jacobian — two
  published frameworks agree (methods cited, not claimed).
- **Task M — the degree=rank mechanism (2026-06-06, Ledger V79; suite green; P1–P16 untouched).**
  `frontier/B95_degree_rank_mechanism/`: the V75 audit killed "exponent = Cayley–Hamilton degree"; B95
  finds what the exponent reads. The principal spectrum is **forced** by `tr A=tr A⁻¹=1` ({1,i,−i},
  {1,1,ω,ω²}, {1,1,1,−1,−1}, impossible n≥6); at n=5 it degenerates (`A²=I` → dihedral → reducible, no
  irreducible SL(5) principal rep — upgrades B78). So **"exponent = rank" is an n∈{3,4} phenomenon**; the
  mechanism reads the cusp's forced finite-order spectrum, explaining the n≥5 wall on both the tower and
  degree=rank. Corrects the handoff's SL(5) spectrum guess.
- **Paper 0 — the self-reference grounding (2026-06-06, Ledger V76–V78; suite 230 passed, 1 skip;
  proven core P1–P16 untouched; philosophy quarantined).** A foundational thread characterizing the
  metallic family by a condition (`m` free). `philosophy/METALLIC_FOUNDATIONS.md` (quarantined
  motivation, never a claim). `frontier/B92_metallic_classification/` (Layer 1, V76, `proven`): the family
  = the `det=−1`/period-1 slice up to `GL(2,ℤ)` conjugacy (entries ≤5), with MyCalc-2 (conjugacy census)
  and MyCalc-5 (systole/contingency). `frontier/B93_det_parity_bridge/` (Phase C, V77): MyCalc-1
  (`det=−1 ⟺` the tower's parity sectors) and MyCalc-4 (parity ≠ Galois — refines the handoff).
  `frontier/B94_tower_universality/` (G1, V78): **"universal catalog, det=−1 parity"** — the Dickson
  catalog survives any `GL(2,ℤ)` monodromy but the sign/parity sectors are `det=−1`-specific (so `det=−1`
  is structurally distinguished); degree=rank is det-agnostic (two problems).
- **Audit correction (2026-06-05, Ledger V75).** Corrected B90's framing: L1a is a tautology and
  "exponent = rank from Cayley–Hamilton" is refuted (the hinge test); only L1b is genuine. Strengthened
  B89-T with the J(m) cross-check against B80.
- **"Complete the Tower" run (2026-06-05, Ledger V70–V74; suite 220 passed, 1 skip; proven core
  P1–P16 untouched; `EXPERT_OUTREACH.md` dormant).** The CC-web handoff reconciled against `main` and
  the genuine open prizes executed:
  `frontier/B87_m3_genus/` (Task 3, V70) the m=3 spectral-curve genus — sequence `3,1,…`, m=2 a minimum
  (the `3,1,0` reading refuted), m=3 trace-relation curve genus 1;
  `frontier/B88_sl4_census/` (Task 2, V71) the SL(4) Dehn-filling census — **degrees {3,4}**, two
  components (`{1,1,ω,ω²}→M⁴=L`, `{prim 8th}→M³=L`);
  `frontier/B89_sl4_symbolic_M4L/` (Task 1a, V72) **`M⁴=L` PROVED symbolic-exact at SL(4)** over ℚ(ω)
  (upgrades V54 from ~1e-31), via the 10-equation exact ideal + the rank-drop-locus family;
  `frontier/B89T_tower_route/` (Task T, V73) the tower's **cohomological route closed** (a 3rd dead
  shortcut) + the explicit two-sequence **Sym-product** reduction (symbolic-in-m, proved n≤4) to one
  module-isomorphism;
  `frontier/B90_degree_rank_peripheral/` (Task 1b, V74) degree=rank's **uniform peripheral reduction** —
  Lemma 1 (`λ=μX⁻¹μY⁻¹`, `XμX⁻¹=μA`) proved uniformly; reduced to one collapse-lemma, exponent = rank
  from A's degree-n Cayley–Hamilton.
  Net: both flagships (the tower, degree=rank) reduced to one clean lemma each with n≤4 proved; the
  cohomological route closed. Open: Task 6 (genus-2 generality).
- **Comprehensive Paths A–F mandate (2026-06-05, Ledger V53–V59; suite 179 passed, 1 skip; proven
  core P1–P16 untouched).** Two prizes + a fully-labeled speculative tail:
  `frontier/B73_sl4_apoly/` (Path A, V54) the **degree=rank tower law** `Mⁿ=L` on the principal
  Dehn-filling component, confirmed at SL(4) (~1e-39);
  `frontier/B70_trace_ring/symbolic_m_pinv.py` (Path D, V55) the symbolic-m ε-series pinv-limit
  construction, reproducing the SL(3) tower from first principles;
  `frontier/physics_probes/spectral_curve_coulomb_test.py` (Path B, V53) confirms the j=1728 kill;
  `frontier/B74_higher_spin_grading/` (Path C, V56) the W_N parity grading = `−w0` of `A_{n−1}`
  (STRUCTURAL), spectrum diverges, dynamics SPECULATIVE-ANALOGY;
  `frontier/B75_metallic_degree_rank/` (Path F1, V57) the **m-axis** of degree=rank (odd metallic
  bundles m=1,3 give `M³=L`; convention-independent `eig[A,B]=eig(t)ⁿ`);
  `frontier/B76_cusp_quantum_group/` (Path F2/F3, V58) cusp k-set = SU(2)_{k−2} root-of-unity level
  set (closes B69), no categorical family lift (SPECULATIVE-ANALOGY);
  `frontier/B68_aj_conjecture/cyclotomic_numeric.py` (Path E, V59) confirms the V52 AJ bounded negative.
- **Open-paths sweep (2026-06-05, Ledger V43–V52).** `frontier/B71_sl3_apoly/` the SL(3) figure-eight
  A-variety (Fix(T_1²) = 3 components, matches Heusener–Muñoz–Porti / Falbel; `W1=D2→M³=L`,
  `W2=D3→M³L=1`); P1 Dehn-filling exact; P3 m=2 framing = m136; P4 rank-independent meridian; P5
  trace-ring scoping; P6 AJ bounded-negative.
- Full audit of all prior work: `AUDIT_REPORT.md`, `PROVENANCE.md`.
- Phase 0 governance scaffolding: `GOVERNANCE.md`, `CLAIMS.md`, `README.md`, `ROADMAP.md`,
  `PROGRESS_LOG.md`, this changelog, `REPRODUCIBILITY.md`, `docs/ARCHIVE.md`, `.gitignore`.
- Claims ledger established: 10 `proven`, 4 `conditional`, 9 `open`, 10 `dead`.
- `legacy/` — prior history consolidated: curated text under `legacy/reports/`,
  `legacy/handoff/`, with the ~4 GB raw archive git-ignored under `legacy/raw/`.
- Phase A: the `origin_axiom` package (`src/`) and `tests/` suite locking every
  `proven` claim P1–P10 — 33 passing tests. Packaging via `pyproject.toml`.
- Session-3 integration: claims P11–P13 promoted to the proven core (exact-algebra
  results — sl(2) decomposition of `log A`, gluing-equation factorization,
  isospectrality), with tests (suite now 39 passing). Frontier probes B4
  (BKL/Gutzwiller) and B5 (Wheeler-DeWitt) added as logged observations.
- **Phase C kickoff** — `paths/` directory created: 25-path registry (20
  mathematizable E1–E20 across 11 mechanism classes; 5 philosophical P1–P5 in a
  separate register). The project's goal becomes *exhaustively surveying* the
  mechanisms by which "nothing being unstable" could produce reality, with the
  *map of attempted paths* as the deliverable. First batch selected: E14, E11, E5.
- **Session-3 synthesis** — the 2025 field-theory line reconnected to the algebraic
  skeleton. Claims **P15** (Möbius generating vector field `v(τ)=−κ(τ²−τ−1)`) and
  **P16** (derived potential `V(τ)=κ(τ³/3−τ²/2−τ)`) promoted to the proven core as
  exact algebra about A, with tests (`src/origin_axiom/mobius.py`,
  `tests/test_mobius_vector_field.py`, `tests/test_derived_potential.py`). Frontier
  probes **B6–B9** added (field equation, Fisher–KPP creation, particle spectrum
  with the non-exact `m/g≈φ` near-miss, fusion–scattering shared polynomial), each
  with caveats. Synthesis doc + scripts under `docs/SESSION3_SYNTHESIS.md` and
  `scripts/`. Four Oct-2025 genesis documents filed under `legacy/reports/genesis/`
  (historical only). Ledger: **15 `proven`**, 4 `conditional`, 9 `open`, 10 `dead`.
- Roadmap integration started with `docs/atlas/INTEGRATION_MANIFEST.md`, a
  public-safe manifest for migrating atlas, paper-candidate, campaign-synthesis,
  and review-packet material from private staging into the canonical repository.
- Research Atlas skeleton added under `docs/atlas/`: auditor guide, research
  tree, failure atlas, success atlas, glossary, and simulator ecosystem map. This
  is a navigation layer only; governed claims remain in `CLAIMS.md`.
- Paper-candidate registry added under `papers/`: candidate index, artifact
  manifest, and first paper cards for conditional uniqueness, noncommutative
  residue, and the quantum selector / state-integral bridge problem.
- Quantum selector campaign summarized under `docs/atlas/campaigns/`: public-safe
  synthesis of the 232-cycle run, preserving verdict counts, survivors, killed
  routes, stalled bridge classes, and theorem questions without raw run artifacts.
- PC02 validation packet added, giving readers a concise audit path for
  the conditional uniqueness theorem, its tests, caveats, and missing topology
  lemma.
- Noncommutative cancellation residue dossier added as an atlas node, with the
  PC04 paper card updated to point at canonical atlas evidence and the campaign
  synthesis.
- State-integral selector-gap dossier added as an atlas node, with the PC06 paper
  card updated to frame the route as an expertise-bound theorem question rather
  than a solved bridge.
- Atlas/paper integration roadmap closed through R7: manifest now marks R0-R6
  complete and records the final QA, merge, and tag gate for
  `atlas-paper-integration-v1`.
- Post-merge manifest cleanup: R7 marked complete after merge/tag, and stale
  closure wording removed. Existing `atlas-paper-integration-v1` tag left
  unchanged.
- PC02 paper-support lemma added: mapping-torus homology/torsion proof for the
  conditional uniqueness theorem, with PC02 paper card and review packet updated
  for external mathematical review.
- PC02 validation brief added, and PC02 readiness advanced from
  `EVIDENCE_EXISTS` to `NEEDS_VALIDATION` pending independent mathematical
  validation.
- Conditional uniqueness theorem formalized: `docs/UNIQUENESS_THEOREM.md` and
  `tests/test_uniqueness_theorem.py` lock the machine-checked algebra
  `A1-A7 -> A=LR` up to order, while keeping C1 conditional.
- Trace-map character-variety frontier campaign B13-B25 added. B18 establishes
  the canonical half-step trace lift; B22 kills the special parity narrative
  while preserving the special `A` quadratic sector; B25 records the Fibonacci
  spectrum at dimensionless `lambda/h=1` as a finite-approximant numerical
  anchor, initially classified as motivated, not derived. No claims promoted.
- Trace selector package added: B26-B47 refine the `lambda/h=1` selector, and
  `docs/TRACE_SELECTOR_THEOREM.md` formalizes conditional claim C5:
  `T1 -> S1 -> I=1/4 -> lambda/h=1`. The selector is conditional on T1, not
  proven or physical.
- PC11 validation packet added, plus `papers/REVIEWABILITY_INDEX.md` routing
  PC02 and PC11 through reviewability and falsifiability checks. PC11 readiness
  advances to `NEEDS_VALIDATION`, pending independent validation of T1.
- Reviewability/falsifiability workflow added: `papers/VALIDATION_WORKFLOW.md`,
  `papers/VALIDATION_LEDGER.md`, PC02 `REVIEWABILITY_CHECKLIST.md`, and
  validation briefs replace communication-oriented artifacts. No person-specific
  names or private correspondence are tracked in the repo.
- Falsifiability matrix added: `papers/FALSIFIABILITY_MATRIX.md` maps PC02,
  PC04, PC06, PC07, and PC11 to missing objects, validation questions, and
  kill/rescope conditions. PC07 now has a paper card, and public-surface hygiene
  is covered by `tests/test_public_surface_scan.py`.
- Metallic `SL(3)` trace-map intake added: B48 generalizes the B27 `m=1`
  Fibonacci trace lift to the family `a -> a^m b, b -> a`; PC12 now tracks the
  standalone arithmetic candidate with certificate-backed fixed-line controls.
  Raw side-work bundles remain private and are not copied into the repo.
- B49 proof-hardening added for PC12: the fixed-line splitting classification is
  decomposed into a universal splitting criterion, direct split families,
  square-gap propagation, finite strip exclusions, and negative boundary
  controls. PC12 remains `NEEDS_VALIDATION`.
- B50 proof-draft assembly added for PC12: B48/B49 are organized into an
  internal theorem-note skeleton with explicit theorem blocks, reproduction
  commands, non-claims, and draftability gates. PC12 remains `NEEDS_VALIDATION`.
- B51 symbolic-`m` proof module added for PC12: the `c=3` fixed-line Jacobian
  factorization is now verified with `m` formal, via closed-form derivative
  sequences and exchange block diagonalization.
- B52 multichannel Fibonacci bridge control added: the simplest three-channel
  tight-binding model gives `6x6` symplectic transfer matrices and fails the
  PC12 third-order `SL(3)` trace recursion, keeping PC12 mathematical.
- B53 literature screen completed for PC12 (`LITERATURE_POSITIONING.md`): the
  trace-map formula, commutator invariant, entropy, exchange decomposition, and
  symbolic factorization are `STANDARD_REPACKAGE` (Lawton; Baake-Grimm-Roberts;
  Bellon-Viallet); only the fixed-line splitting (Thm 4) is `APPARENTLY_NEW` and
  elementary. PC12 rescaled `THEOREM_NOTE` -> `COMPUTATIONAL_REPORT` (still
  `NEEDS_VALIDATION`).
- B54 general-`c` exchange structure added (`frontier/B54_general_c_exchange_structure/`):
  `[J(m,c),P]=0` proved for symbolic `c` (exchange block-diagonalization on the
  whole fixed line, generalizing B51), with the `c=1` Eisenstein/golden twin
  polynomials (disc -3, 5) echoing P12 and the `m=1` cyclotomic sweep.
- Phase-C path E21 added (`paths/E21_self_evidencing_closure/`): the
  self-evidencing / variational-free-energy framing of `lambda=m` is quarantined
  with verdict `STALLED` (structural analogy only; the exact fact is the single
  identity `4c^2-2=m^2+2`; predicts no observable). Kept out of PC12.
- PC02 draft note reconciled: the formal theorem-note structure (axiom table
  A1-A7, mapping-torus torsion lemma via the Wang sequence, the LR/RL
  based-invariant table, explicit theorem + proof) becomes the canonical
  `papers/candidates/PC02_conditional_uniqueness/DRAFT_NOTE.md`, replacing the
  earlier review-brief draft; the half-step / trace-map / conditional
  spectral-anchor material is retained as a clearly-marked non-theorem appendix.
  Editorial consolidation; PC02 stays `CONDITIONAL_THEOREM` / `NEEDS_VALIDATION`.
- B55 c=1 general-m structure added (`frontier/B55_c1_fixed_line_structure/`):
  the c=1 fixed-line symmetric sector is classified **mod 4** (`Φ₆` for m≡1,3;
  `Φ₄` for m≡2; degenerate `(t−1)²` for m≡0) and the antisymmetric sector is
  `(t−1)(t+1)(t²−mt−1) = char(M)` for all m, proved per residue class. Corrects
  the earlier odd/even reading and completes B54's c=1 row.
- B56 figure-eight invariant-surface negative control added
  (`frontier/B56_figure_eight_invariant_surface/`): the diagonal SL(2,C) reps
  have `I ∈ {4, −17/2 ± 7√5/2}`, none `= 1/4`; the figure-eight ↔ `I=1/4` bridge
  is `DEAD` and the c=1 Eisenstein resemblance is a cyclotomic coincidence. The
  P12 gluing-equation discriminant echo is unaffected.
- B57 general-m Diophantine splitting classification added
  (`frontier/B57_general_m_splitting/`): `{c=1, c=3}` are universal splitting
  points; m-dependent extras classified for m=1..6; the Hilbert-class-field
  coincidence (`h(−15)=2`) is killed for m≥2. Extends PC12's Theorem-4 content.
- E21 self-evidencing controls added (`paths/E21_self_evidencing_closure/`): two
  further session results, integrated as quarantine controls. (i) The Fisher
  information of `D(I)` equals `16/disc(char(M²)) = 16·g_WP(m²+2)` (a
  Goldman/Weil–Petersson coefficient) — exact but a chain-rule identity, geometric
  reading not promoted. (ii) Aubry self-duality at `λ=m` is dead (`λ=m` is the
  trivial fixed point of `λ→m²/λ`; no metal–insulator observable). Both strengthen
  E21's `STALLED` verdict; the Aubry kill is recorded in
  `docs/atlas/FAILURE_ATLAS.md`.
- SL(n) factor-count tower recorded as an **untested prediction** in PC12's
  `DRAFT_NOTE_SKELETON.md`: the rank-two `SL(n,C)` Jacobian is conjectured to
  factor into a parity block plus `(n²−1−parity)/2` degree-2 `char(M^k)` factors
  (confirmed n=2,3; SL(4)→7 untested). Not a claim; a candidate future probe.
- B58 SL(4) tower test added (`frontier/B58_sl4_tower_test/`): an attempt at the
  n=4 prediction. Confirms the mechanism (SL(4) identity recursion `(r-1)^4`,
  cubic derivative sequences) and the obstruction (the fixed-line point is the
  degenerate identity representation, so a representation-based numerical Jacobian
  cannot recover the ambient map). Verdict `NEEDS-EXPERTISE`; the 7-factor
  prediction stays untested. The full `15×15` ambient SL(4,C) trace map (Procesi
  generators + substitution action) is the required next build.
- B59 SL(4) fixed-line factorization added (`frontier/B59_sl4_factorization/`):
  resolves B58 numerically (method validated on SL(3) ground truth to ~4 digits).
  The SL(4) spectrum factors as
  `char(M^-1)char(M)char(M^2)char(M^3)char(M^4) · char(-M^2) · (t-1)^2(t+1)` —
  5 clean `char(M^k)` (k=-1..4), a sign sector, and a degree-3 parity block —
  **refuting** the naive `7 char(M^k) + parity` tower prediction. Numerical, not
  a symbolic proof; no claim promoted.
- B60 SL(n) tower added (`frontier/B60_sln_tower/`): generalizes B59's method and
  builds the corrected cross-n structure map. n=3: powers `{-1,2,3}`, parity
  deg 2; n=4: powers `{-1,1,2,3,4}` + `char(-M^2)` + parity deg 3 (powers climb,
  a sign sector appears, parity grows). **SL(5) unresolved** (`cond(Dx)~1e11`;
  needs a stable high-precision SVD solver or the symbolic ambient SL(5,C) trace
  ring). Numerical, method-validated for n=3,4; no claim promoted.
- B61 SL(5) high-precision factorization added (`frontier/B61_sl5_high_precision/`):
  ports the method to mpmath (dps 60) with a stable SVD pinv, and shows B60's
  "`cond(Dx)~1e11` wall" was a **rank-23** forward-only word set (the 24th
  singular value is the dps zero-floor, mis-read as `1e11` in double precision).
  Inverse-word coordinates (`A,B,A^-1,B^-1`) restore rank 24 at `cond~1e4`, and
  **22 of 24** SL(5) multipliers resolve to the catalog:
  `char(M^-1)·char(M)^2·char(M^2)·char(M^3)·char(M^4)·char(M^5)·char(-M^2)·char(-M^3)·(t-1)^2(t+1)^2`
  (powers climb to 5, sign sectors `-2,-3`, parity deg 4 -- the n=5 tower row).
  The last 2 modes are a **method limit** (fixed-line rank-loss makes the pinv
  `eps->0` limit gauge-dependent; residual scatters across seeds), needing the
  symbolic ambient SL(5,C) ring. SL(3)/SL(4) reproduce to ~4e-14/~3e-9.
  Numerical, high-precision; no claim promoted.
- PC12 made review-ready for an external specialist: a polished, self-contained
  `DRAFT_NOTE.md` (standard blocks Sec 2-5 with citations; the apparently-new
  fixed-line splitting classification in Sec 6; the numerical cross-n tower as a
  labeled Appendix A), plus `REVIEW_PACKET.md` (five sharpened questions) and
  `REVIEWABILITY_CHECKLIST.md`, mirroring PC02. A bounded literature refresh added
  the entropy=spectral-radius citation (arXiv:0812.0853) and found no prior art
  for the Sec-6 splitting or the cross-n tower. `PAPER_CARD` readiness advanced to
  `READY_FOR_REVIEW`; ledger row V12. No claim promoted.
- B62 opposition involution (`frontier/B62_opposition_involution/`): identifies
  B61's 2 unresolved SL(5) fixed-line modes. The B61 numerics cannot decide them
  (`tr(DT0)`/`det(DT0)` scatter across seeds). Identifying the exchange involution
  with the opposition involution `theta=-w0` on the `sl(n)` root system, its
  height-2 eigenspace split is exact and reproduces SL(3) (`char(M^2)`) and SL(4)
  (`char(M^2).char(-M^2)`); for SL(5) it is `char(M^2)^2.char(-M^2)`, so the 2
  unresolved modes are a second `char(M^2)` = {phi^2, 1/phi^2} (residual modes
  positive, corroborating). Completes the SL(5) tower row (22 numerical + 2
  structural). Recorded as a **live structural result**; a symbolic proof needs
  the ambient SL(5,C) trace ring. Ledger V13. No claim promoted.
- B63 SL(4) factorization over Z[m] (`frontier/B63_sl4_symbolic_m/`): establishes
  the metallic SL(4) fixed-line factorization for general `m` and proves
  m-independence. Building the symbolic Procesi trace ring (B58) is harder than
  "one level deeper" -- `e_2(A)` forces the 6-dim `Lambda^2` representation
  (depth-6) or multi-block words `tr((A^m B)^2 A)`; documented as the real reason
  B58 is hard. Instead, SL(4) being gauge-clean, the high-precision Jacobian is
  computed for `m=1..6`, each factor's eigenvalue sum extracted (= exact
  `tr(M^k)`) and interpolated in `m`:
  `char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)` with
  `L_2=m^2+2, L_3=m^3+3m, L_4=m^4+4m^2+2`. The M-power/sign/parity structure is
  m-INDEPENDENT; m=1 reproduces B59. Computer-assisted symbolic (not a hand-built
  trace ring); the explicit `k(alpha)` root map is supplied by B62. Ledger V14.
  No claim promoted; proven core P1-P16 unchanged.
- B64 parity mechanism (`frontier/B64_parity_mechanism/`): proves the tower's
  `k(alpha)` sector-assignment formula as exact symbolic algebra. Depth-n
  Cayley-Hamilton makes the fixed-line Jacobian polynomial in `m`; `P` is the
  contragredient (`m -> -m`); Dickson parity `L_k(-m)=(-1)^k L_k(m)`. Hence
  **even-|k| `char(M^k)` sits in the P-symmetric sector, odd-|k| in the
  P-antisymmetric** (the root-height split B62 identified). Verified in full
  symbolic-`m` form for SL(3) (symmetric=(t-1)(t+1)char(M^2), antisym=
  char(M^-1)char(M^3)); applied to SL(4)'s factorization (even-k {M^2,M^4,-M^2}
  symmetric, odd-k {M^-1,M,M^3} antisymmetric). The depth-4 derivative sequences
  are built; a full symbolic SL(4) Jacobian's one remaining need is localized to
  `e_2 = tr(Lambda^2 A)` (the 6-dim exterior square, the even-k sector). Ledger
  V15. No claim promoted; proven core P1-P16 unchanged.
- B65 symbolic SL(4) Jacobian (`frontier/B65_sl4_symbolic_jacobian/`): determines
  the full 15x15 SL(4) fixed-line Jacobian `J(m)` exactly over `Z[m]` and factors
  `char(J(m))` directly as symbolic algebra. A hand-built trace ring needs
  multi-block reductions (rank check: single-block V+`Lambda^2` traces span only
  12/15), so instead the canonical (seed-independent) degree-4-in-m entries are
  reconstructed from high-precision numerics (SL(4) is gauge-clean) for `m=1..7`,
  over-determined (degree 4 fixed by 5 points, verified on 7); `sympy.factor`
  gives
  `char(J(m))=char(M^-1)char(M)char(M^2)char(M^3)char(M^4)char(-M^2)(t-1)^2(t+1)`.
  Matches B63/B64; `m=1` reproduces B59. The factorization is now *derived*
  (direct factoring of `J(m)`), not matched -- the strongest form short of a
  hand-derived Procesi trace ring (B58, still open). Computer-assisted entries +
  exact symbolic factorization. Ledger V16. No claim promoted; proven core
  P1-P16 unchanged.
- B66 SL(6) numerical tower (`frontier/B66_sl6_tower/`): computes the `n=6` row
  (35-dim) by the inverse-word method to settle the tower multiplicity formula.
  The opposition-involution theta-split sector dims (9 odd-height + 6 even-height
  + 5 parity = 35) are exact (the 9/6 is a root-height count, = |k|-parity only
  for odd n); the |k|=3 region resolves cleanly to exactly two quadratics
  (`char(M^3)`, `char(-M^3)`), so the **|k|=3 multiplicity = 2 — refuting
  `max(n-d,1)=3`** (SL(6) is the first `n` that distinguishes 3 from 2). Honest
  limit: 26/35 resolve, 9 modes gauge-corrupted (the B62 mechanism amplified from
  SL(5)'s 2 modes). Ledger V17. Numerical, no claim promoted; proven core P1-P16
  unchanged.
- B66 validation campaign (`frontier/B66_sl6_tower/{validate,second_m,gauge}.py`,
  `VALIDATION.md`; Ledger V19): stress-tested `mult(|k|=3) = 2` four ways. The
  identical inverse-word pipeline recovers SL(3..6) = 1,1,**2**,2 (SL(5)=2 under
  the same gauge-handling, auto-selected words); m=2 and m=3 give 2 with the |k|=3
  root tracking `L_3(m)`; the |k|=3 eigenvalues are seed-stable while the 8 gauge
  modes scatter (up to 3.8) across base points. Exact-over-Q is the honest
  negative -- the numerical Jacobian is non-canonical (`||dt0(20)-dt0(24)||~7e3`),
  so the from-first-principles exact route for n>=5 remains the trace ring (B58).
- B67 figure-eight A-polynomial from the trace map (`frontier/B67_figure_eight_apolynomial/`;
  Ledger V20): the metallic SL(2,C) trace map's fixed-point set (monodromy
  `phi=[[2,1],[1,1]]=M^2`, trace map `T_1^2`) reproduces the **published Cooper-Long
  (1996) figure-eight A-polynomial exactly** -- `A(M,L)=M^4L^2+(-M^8+M^6+2M^4+M^2-1)L+M^4`.
  A fiber rep extends over the bundle iff its character is `T_1^2`-fixed, so the fixed
  locus `y=z=x/(x-1)` is the A-polynomial curve; the monodromy `t` gives meridian
  `M=eig(t)`, longitude `L=eig[B,A]`, with trace identity `tr[A,B]=tr(t)^4-5tr(t)^2+2`.
  First derivation of this A-polynomial from a trace-map computation -- an independent
  cross-check of the SL(n) tower (B59-B66). SL(3) (Garoufalidis-Thurston-Zickert) is the
  open next step. No claim promoted; proven core P1-P16 unchanged.

### Fixed
- Tower verification pass (Ledger V18). **SL(2)/n=2 parity correction:** the
  `DRAFT_NOTE.md` cross-`n` tower table listed the `n=2` parity block as `none`,
  under-counting the 3-dimensional `SL(2)` variety; the identity-fixed-point
  Jacobian is `(t+1)·char(M^2)` for all `m` (parity eigenvalue = `det(M) = -1`),
  so the block is `(t+1)` — corrected. **B66 labeling:** the `sector_prediction`
  "9 odd-k + 6 even-k" is a root-HEIGHT count, equal to the `char(M^k)` |k|-parity
  count only for odd `n` (SL(4) is |k|-parity `(3,3)` but height `(4,2)`);
  relabeled "odd/even-height" throughout B66 + Ledger V17. The B66 `|k|=3 = 2`
  result (direct root-matching) is unaffected. Both facts, plus
  `char(-M^k)=char(M^{-k})` for odd `k` only and `L_k(-m)=(-1)^k L_k(m)` through
  `L_8`, are now locked in `tests/test_b66_sl6_tower.py`.
- **CORRECTED MISCONCEPTION (B58 Stage 1, Ledger V21).** The scoping guesses that
  the cotangent dimension is `3n^2-10n+11` (=8,19,36) and the excess `2(n-2)(n-3)`
  (=0,4,12) were **never validated and are REFUTED** by the Đoković cross-check.
  Kept visible (not deleted) so they are never re-derived. Actual cotangent (d-sigma
  on `m/m^2` of the two-traceless-matrix trace algebra, modular over F_p, prime-stable):
  `9` (n=3, = Teranishi 11 GL gens − 2) and `30` (n=4, = Đoković, exact per-degree
  distribution), `>= 111` (n=5, PARTIAL lower bound). Actual excess (cotangent − the
  `n^2-1` Jacobian) = `1, 15, >= 87` — a large mixed Dickson+parity multiset, the
  *secondary* trace invariants (n=3: `det[X,Y]`). This **closes the cotangent route to
  the `a_d` multiplicities** (see FAILURE_ATLAS); `a_d` needs the exterior-power
  Cayley-Hamilton hand proof. (arXiv 2603.00816 Ishibashi-Mizuno confirmed real by
  independent search; Kozai 1509.07487 and 2411.04431 pre-2026, fetched.)
  *Forward guard:* no entropy/"spectral-weight" probe was produced; if one is ever
  added, note that it computes `Σ|k|` spectral weight, NOT topological entropy
  (= `n·log μ`, linear) — no `n^2` scaling, no fixed "antisymmetric fraction".

### Added
- B58 Stage 1 (`frontier/B58_stage1/`): the modular-F_p cotangent computation and the
  Sym^{2k}/Kostant diagnostic (Step 2: bare = even-only/overshoot, coupled = odd-only,
  neither = tower — B64's parity split is a sorting, not a formula). Tests in
  `tests/test_b58_stage1.py`.
- Overnight exploratory queue (`frontier/overnight_2026-06-03/`, Ledger V22/V23):
  Job 1 time-reversal = Jacobian-level Dickson parity (corollary); Job 4 SL(7) partial
  (constraints, char(M^3)=a_3=1 at n=7, INCONCLUSIVE); Job 2 SL(3) A-poly Sym^2 NO-GO
  (geometric component is boundary-unipotent/GTZ); Job 3 cross-m m=2 = census m136,
  framing OPEN; Job 5 skipped (gate). Job 6 AJ (`frontier/B68_aj_conjecture/`,
  `frontier/aj_conjecture_check.json`): shelved, NOT promoted (order-2 recursion match
  is below B67's exact-identity bar; q=1 limit unresolved). Literature review in
  `frontier/literature_search.md` (principal-SL(2) / adjoint-torsion / Kozai framing).
- B58 Phase A (`frontier/B58_phaseA/`, Ledger V24–V26): an EXACT `(n^2-1)` fixed-line Jacobian
  engine (`jacobian_closure.py`; eps-series dual numbers over F_p; the least-squares form of
  B66's pinv limit). VALIDATED at n=4 — reproduces B65's `a_d=(1,1,1,1)` exactly, prime-stable.
- Candidate general-`n` `a_d` formula recorded (`frontier/B58_phaseA/CANDIDATE_A_D.md`): the
  opposition-involution θ-split, `a_h=⌈(n-h)/2⌉`, `b_h=⌊(n-h)/2⌋` for `h=2..n-1`, plus an
  OBSERVED height-1/wrap piece (`char(M^1)^{n-3}·char(M^-1)·char(M^n)`) and parity. Reproduces
  the n=3,4,5 towers EXACTLY (integer-valid + dimension-sum `=n^2-1`, n=3..7). **CONJECTURED —
  unproven (needs the trace-ring identification, B58) and incomplete (height-1/wrap observed).**
- B62 proof status clarified (`frontier/B58_phaseA/B62_STATUS.md`): State 3 for the full `a_d`,
  State 2 (verified candidate) for height-2 only; θ-eigenspace dims are exact Lie theory, the
  identification with the Jacobian is unproven.
- **Phase-8 physics-paths sweep (`frontier/physics_probes/`, Ledger V28–V39): robustly negative.**
  A systematic probe of every reachable physics anchor. Headline: real mathematics, **no crossing
  into fundamental or new-quantum physics** — every anchor is special to `n=2`/`m=1`. Metallic
  anyons (V28, closed: categorifiable only at `m=1`, Ostrik rank-2) and SL(n) quasicrystal spectra
  (V29, closed: the symplectic obstruction, `SL(n)=Sp` only at `n=2`) both negative; Chern–Simons
  torsion family (V30, no pattern) with `τ_m` identified as **Porti's adjoint Reidemeister torsion
  form** (V31). The `m136`/`m=2` A-polynomial framing is **RESOLVED** — the m=2 trace-map eliminant
  `M²L²−(M⁴−4M²+1)L+M²` IS census-m136, confirmed by holonomy-match (V32) and an independent
  from-scratch null-space-dim-1 fit (V38). Consolidated in `PHYSICS_PROBES_SUMMARY.md`.
- B69 metallic A-polynomial family + cusp-torsion law (`frontier/B69_metallic_apoly_family/`, Ledger
  V35/V39/V40): VERIFIED m=1..4; cusps at elliptic-torsion `x=2cos(π/k)`. **Novelty: STANDARD_REPACKAGE**
  — the cusp law is the known Baker–Petersen once-punctured-torus-bundle ideal-point structure
  (arXiv:1211.4479), not new.
- B70 trace-ring attack on `a_d` (`frontier/B70_trace_ring/`, Ledger V41/V42): the SL(n) two-block /
  `e₂=tr(Λ²A)` obstruction is **rank-1 at leading order** (pinned exactly to `e₂`; verified SL(4),SL(5)
  on the traceless `sl(n)` tangent), and its full closure is a **bounded, finite multi-generator** set
  (bidegree `≤(3,3)` by `c=n` nilpotency). The two-block barrier is now a precise finite structure —
  computer-assisted characterization, **not PROVEN**. The `SL(3)` GTZ A-polynomial (Track B) is the
  deferred more-tractable follow-on.

### Changed
- **REFUTED (kept visible as honest history): the exact-`Q` "field fix" hypothesis for the n=5
  `a_2` shortfall.** The shortfall is the pinv-limit CONSTRUCTION, not the field/metric — three
  realizations (F_p random metric; F_p `S=I`, prime-stable `= Q` mod `p`; real positive-definite
  mpmath) all return `a_2=1` where the truth is `2`. The `eps->0` least-squares limit is
  non-canonical at the degenerate `char(M^2)^2/(t+1)^2` collision (defective non-Dickson cubic).
  So the pinv / ambient-Jacobian route (B59–B66 + the Phase A engine) **under-counts degenerate
  multiplicities** — *wrong* from n=5, not merely ceilinged at n=6 (FAILURE_ATLAS, sharpened).
- `b_d=[d<=n-2]` DOWNGRADED: an n<=5 match only — it diverges from the θ-split at n=6 (`b_2`:
  1 vs 2). OPEN for n>=6.
- `a_3(n=6)` is now OPEN (Ledger V17 annotated): B66's numerical `1` is understood as the pinv
  under-count at a degenerate collision; the θ-split candidate predicts `2` (better-supported,
  not asserted).
- Strategic state: the pinv / ambient-Jacobian route is EXHAUSTED as a path to *degenerate*
  `a_d`; the B58 trace ring (structural form + identification proof) is the sole remaining route
  that both computes and proves it. The fork — bank the candidate + finding as a written result
  vs commit to the multi-session B58 trace-ring proof — is DEFERRED (human decision).

### Changed
- Project framing locked to the disciplined V4 / Reality-Check line; the optimistic
  `handoff.md` framing demoted to historical record.

### Notes
- This repository consolidates four prior GitHub repositories and the May-2026 session
  archive into a single canonical home.
- The four prior repositories (`origin-axiom-framework`, `origin-axiom-theta-star`,
  `origin-axiom-obstruction`, `00_origin-axiom`) have been archived read-only with
  "superseded by" pointers. They are preserved, not deleted.
