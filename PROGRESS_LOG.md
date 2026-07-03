# Origin Axiom — Progress Log

Append-only, chronological. Never edit past entries. Each working session adds a dated
entry. When this file grows large, older entries roll into `docs/progress/` by quarter.
Governed by `GOVERNANCE.md` §9.

---
*(2026-07-03: entries for 2026 Q2 (May–June) rolled verbatim into
`docs/progress/PROGRESS_2026-Q2.md` per §9. The live log continues below.)*

---

## 2026-07-01 — Catch-up: the structural-theorem + specialist-handoff arcs (B161–B325)

This is a single catch-up entry; the detailed working history since the June-17 entry (B160) is not backfilled
here — it lives in `CHANGELOG.md` (arc-level, newest-first) and each `frontier/B###/FINDINGS.md`.

Two arcs closed the gap from B160 to the current frontier B325, all firewalled, **zero `CLAIMS.md` promotions**:

- **The structural-theorem arc (B231–B314).** The four-faces object sharpened into one proven statement — *the object
  forces the form of physics (E₆, the cascade, `κ`, both arithmetic ends), never its physical values.* Mechanized as a
  **Galois theorem**: every discrete invariant is a Galois orbit of the object's own arithmetic (`√−3→−√−3` CP sign,
  `√5→−√5` WRT data). The two-ended object, the arithmetic atom `4₁→ℚ(√−3)→2T→E₆`, the E₆ character variety, the
  cascade (generic Slansky + the Eisenstein `ω`), Face IV houses the *form*, the four faces of one `κ`. Consolidated in
  `knowledge/K020`, `philosophy/P013`.

- **The specialist-handoff arc (B315–B325).** The forgotten leads and three-seat cross-chat handoffs run to conclusion
  and the frontier mapped to a specialist handoff (`docs/OPEN_PROBLEMS.md`, four gates: the in-sandbox `S032-A` +
  the `T[4₁;E₆]` CRUX / multiplicity / non-Hermitian Damanik–Gorodetski). Headline: **the value hunt, run** — the
  object's Dehn-filling invariants match the SM's dimensionless parameters *at chance* (`p≈0.5`, a null test), so the
  value-firewall is now confirmed *empirically*, not just proven (B322). Plus the four-level framework (B323), the
  exact ω-circulant (structure not values, B324), and the "ℤ/3-protection" refutation (B325).

Also: the recontextualization audit + masterplan (`docs/RECONTEXT_AUDIT_AND_MASTERPLAN_2026-07.md`) and a full
documentation consolidation (this pass) bringing the entry-point / narrative / ledger docs current to B325.

---

## 2026-07-01 — The in-sandbox attack sweep (B329, B330; L34 DORMANT; S046; R7)

A "research / get-informed / meditate / sober / attack" push on the computable frontier (owner directive: *don't give
up*; the standing compute-before-deferring mandate). Four sequenced targets, all firewalled, **zero `CLAIMS.md`
promotions.**

- **B329 [VERIFIED] (Target 2).** `27|₂T` computed for *both* natural embeddings from a from-scratch, orthonormality-
  verified 2T character table: principal (quaternionic SU(2)) `= 3·1⊕3·1′⊕3·1″⊕6·3`; trinification (complex SU(3))
  `= 9·1⊕3·1′⊕3·1″⊕3·2′⊕3·2″`. **Both give `n₁=n₂` → Level 4** — tightens B327 (even the complex SU(3) route can't split
  the light generations; the 27's balanced `3/3̄` restores reality; non-vacuity witnessed). `OPEN_PROBLEMS` gate B updated.
- **B330 [CONDITIONAL] (Target 3, gate A/S032-A).** The no-forced-choice capstone via one Galois-symmetrization
  mechanism: folded B130+B314+B318, stressed two fresh classes (B326 cover-torsion `(ℤ/4)²` — irreducible deck action, no
  distinguished sub-object; cohomology `H¹` — canonical integer). **Five classes sealed**, no forced choice among them.
  Worded per the **C-guardrail** (`open`, not universal proof; untested classes named). Gate A updated.
- **L34 (Target 1) → DORMANT.** The m=1 `40a1` was a *2-bridge-Riley* artifact; the intrinsic trace-map fixed locus
  `Fix(φ_m)` is genus-0 (`#Fix(𝔽_p)=p−1`, m=1) / irregular (m=2,3). Full silver/bronze canonical-component arithmetic =
  NEEDS-SPECIALIST (R7-confirmed Baker–Petersen gap). Data recorded in `OPEN_LEADS.md` L34.
- **H14 (Target 4).** Already resolved by **B315** — checked, not re-banked (no duplicate probe).
- **Research → `NOVELTY_AUDIT.md` R7**: four cited verdicts. **Meditate → `speculations/S046`** (firewalled): "the value
  lives at the seam"; new hints **H103–H106** in `HINT_LEDGER.md`.

Nothing promoted to `CLAIMS.md`; P1–P16 untouched; firewall intact.

## 2026-07-01 — External audit + robustness hardening (fresh-clone reproduction pass)

An independent audit session (fresh clone, fresh environment, SnapPy 3.3.2 installed) ran the full claim-by-claim
verification the repo invites in `README.md` §"How to navigate." Findings and fixes, **zero label changes, zero
promotions**:

- **Fresh-environment reproduction: the suite was NOT green** — 3 frontier locks failed deterministically
  (`test_b101` unipotent-cusp, `test_b106` roots-of-unity + anatomy scalar) from ill-conditioned certificates
  (eigenvalues of a defective matrix; a 1e-2 neutrality window capturing a hyperbolic pair at 7e-3; a
  Galois-conjugate branch `c=−i` vs `c=+i`). All three re-certified structurally (nilpotency residual,
  measured-gap window, conjugation-closed comparison); banked as guard **MB13** in `REPRODUCIBILITY.md`.
  The *findings* of B101/B106 were confirmed correct; only the certificates were fragile.
- **Claim-by-claim test audit (P1–P16, C1, C5):** 12/15 proven claims verified LOCKED by exact symbolic tests.
  Hardened the rest: **P9** was circular (constants mirrored back at themselves; `H₁`, amphichirality, sister
  torsion untested) — now recomputed independently (dilogarithm volume, no SnapPy) plus live SnapPy cross-checks
  for every clause; **P5** count-partition was tautological and the `β_c` thresholds untested — now brute-force
  word-ensemble sums + exact growth-rate assertions; **P4** parameter point now *derived* as the unique solution,
  weak-cooperativity actually asserted; **P11** `log(A)` now derived independently by exact eigendecomposition;
  **P10** three of the four documented auxiliary filters (min volume, amphichirality, Eisenstein triangulation)
  now live-checked against SnapPy. **C5** was the one ledger entry with no executable evidence — the post-T1
  algebra is now locked by `tests/test_trace_selector_c5.py` (including the Lucas-hierarchy ↔ P8 torsion-ladder
  identity).
- **Documentation drift corrected:** the frontier stands at **B346** (345 probe directories), while GOVERNANCE §7
  said B314 and README/ROADMAP said B325 with stale test counts (~1113/304 vs actual 1197/325 after this pass) —
  exactly the "credibility bugs" class the 2026-07 masterplan flagged. Ceilings and counters refreshed.

Suite after hardening: green — 1195 passed, 4 skipped, 0 failures (SnapPy installed, so the previously-skipped
SnapPy-gated cross-checks were exercised). P1–P16 untouched; firewall intact; nothing promoted.

## 2026-07-01 — Gate A extensions: B350 (cyclic-cover torsion; originally numbered B347, renumbered on merge with main's B347 PR #424) + B348 (Bloch class)

Continuation of the external-audit session: the two in-sandbox gate-A probes queued by the audit were run to
conclusion. Both extend B330's Galois-symmetrization mechanism to classes it named as untested; both are
**CONDITIONAL** per the C-guardrail; **zero promotions**.

- **B350 [VERIFIED, exact].** The cyclic-cover **abelian torsion** class: orders = the P8/C5 Lucas ladder
  (`|det(Aⁿ−I)| = L₂ₙ−2`, n≤8); the factor multiset `{Δ(ζₙʲ)}` Galois-closed with integer symmetric functions
  (constant term cross-checked against the resultant); torsion groups by SNF (n=3 = `(ℤ/4)²`, independently
  re-deriving B326); deck action fixed-point-free **uniformly in n** (`det(A−I)=Δ(1)=−1` a unit ⟹
  `N·ℤ² = im(Aⁿ−I)` exactly). **MB8 tier note recorded:** `Δ(1)=±1` for every knot — the fixed-point-freeness
  is generic-knot, not object-specific; the object-specific content is *which* orbit (the trace-3/Lucas ladder).
- **B348 [VERIFIED, exact + 30 dps].** The object's **Bloch/scissors class** `β=2[e^{iπ/3}]`: Galois orbit
  `{+β,−β}` = `{±Vol(4₁)}`, sum 0; the residual sign = orientation is killed by amphichirality (B318's geometric
  firewall in the Bloch group — *self*-symmetrized); `D≡0` on the fixed field. New observation banked: **the seam
  identity** `1−z₀ = z̄₀` — at the Eisenstein shape the generic Bloch duality involution `z→1−z` coincides with
  the arithmetic Galois conjugation, and `z(1−z)=1 ⇔ z²−z+1=0` (the P12 quadratic is exactly that locus).
- **Gate A updated** (`OPEN_PROBLEMS.md`): **seven classes** sealed under the one mechanism; the untested residual
  restated precisely (nonabelian Ptolemy/adjoint torsion — with B98/B99's rational `τ₁=−3` noted as canonical;
  CS/η beyond the banked `CS=0`; irregular covers; `SL(n≥3)` gluing invariants; extended-Bloch/`K₃` torsion).

Locks: `tests/test_b347_cyclic_cover_torsion_galois.py`, `tests/test_b348_bloch_class_galois.py`. P1–P16
untouched; firewall intact; nothing promoted.

## 2026-07-01 — Gate A extension B349 (irregular covers) + the Gates B–D outreach package

Continuation of the gate-A sweep. **CONDITIONAL** per the C-guardrail; **zero promotions**.

- **B349 [VERIFIED, SnapPy].** All covers of 4₁ through index 6: the census per index is a canonical
  **multiset** (banked exact: index 4 = 1 cyclic + 1 irregular `ℤ²`; index 5 = 1 + 3; index 6 = 1 + 10);
  the cyclic members' `H₁` torsion equals B350's `coker(Aⁿ−I)` SNF **exactly** (`[5]`, `[4,4]`, `[3,15]`,
  `[11,11]`, `[8,40]`) — independent-route cross-validation; **every** within-index invariant multiplicity
  collapses to a **single isometry class** (index 5: the twin `ℤ/2⊕ℤ²` pair, 4 isometries; index 6: the
  4×`ℤ/3⊕ℤ²`, 2×`ℤ/12⊕ℤ`, 2×`ℤ/5⊕ℤ²` groups) — the object never distinguishes a member; the "distinction"
  is non-conjugate subgroups with one geometric quotient, invisible to every manifold invariant. MB note:
  `is_isometric_to` is orientation-blind, which is *sufficient here* (any self-identification defeats a
  forced choice; no chirality claim made). Index ≤ 6 = a computational horizon, not a theorem.
- **Gate A now: eight classes sealed** under the one Galois-symmetrization mechanism (`OPEN_PROBLEMS.md`
  updated; untested residual restated: nonabelian Ptolemy/adjoint torsion, CS/η beyond `CS=0`, irregular
  covers beyond index 6, `SL(n≥3)` gluing invariants, extended-Bloch/`K₃` torsion).
- **The Gates B–D outreach package** (`frontier/EXPERT_OUTREACH.md`, new 2026-07 section): one bounded,
  proof-status-honest question per gate; expert picks (addresses to verify before sending); what we supply
  per gate (including the refuted routes so they are not re-walked); sequencing/hygiene rules — one gate,
  one expert, one question; log every send/reply; a "known, see X" reply closes a gate honestly and is a
  good outcome.

Locks: `tests/test_b349_irregular_covers_galois.py` (SnapPy-gated). P1–P16 untouched; firewall intact;
nothing promoted.

## 2026-07-02 — Cross-chat relay disposition: PR #424 absorbed; probe-ID collision resolved (B347→B350)

The owner relayed the peer session's ("CC") message correcting an earlier "E6 → SM dictionary" handoff and banking
the correct replacement as **B347_e6_tangent_gradings** (PR #424, merged to main). Disposition in this branch:

- **Merged main** (`10f6673`) into the audit branch; the only delta was PR #424 (self-contained probe + test +
  atlas). **Verified in this sandbox:** all 6 B347 tests green (MB6 — reproduction run, not trusted).
- **Probe-ID collision resolved:** this branch had independently banked a *different* B347 (the gate-A
  cyclic-cover torsion probe, same day, parallel sessions). Renumbered ours **B347 → B350** everywhere (probe dir,
  lock test, OPEN_PROBLEMS, CHANGELOG, this log); main's B347 = the E₆ tangent probe stands. A **multi-session
  probe-ID hygiene rule** is added to `REPRODUCIBILITY.md` so this class of collision is caught at banking time.
- **Gate B updated** (`OPEN_PROBLEMS.md`): B347's banked facts added to "Settled" — `dim H¹(π₁(4₁),𝔢₆) = 6 = rank`,
  uniform per exponent (degenerate-cascade reading refuted); amphichirality = uniform real structure (no split);
  hyperelliptic involution = the E₆→F₄ folding at the tangent level (`{4,8}` = the 26 coset = the escape sector).
  The relay's §3 in-progress items (per-exponent `H²=1`, θ-even reduction of the cup-product obstruction to the F₄
  blocks) are **noted but NOT banked** — they live in the peer session until a probe with tests lands.
- **Relay corrections acknowledged where they touch this branch:** none of the killed items (the G₂⊕A₂ mislabel,
  the `(2.05)^exponent` numerology, the two numeric slips) had entered this branch's documents.

Zero promotions; P1–P16 untouched; firewall intact.

## 2026-07-02 — Suite hygiene: the global-dps test-order failure class (MB13 §4)

The post-merge full-suite run failed **all 6 B347-E₆ locks** while every one passed in isolation. Root-caused
and fixed:

- **Mechanism:** `mp.mp.dps` is a global; B302 lowers it to 25 at call time; in alphabetical suite order B302's
  test runs before B347's, so the E₆ tangent computation (needs ~55+ dps for its 1e-50 residual gates) ran at
  25 dps. Minimal deterministic repro: `pytest test_b302_* test_b347_*` (6 failures in 9 s). Three older probes
  (B264/B265/B276) had already independently discovered this and carry inline "self-guard" comments — the
  pattern existed but was not yet a written rule.
- **Fixes:** B347 now re-asserts `dps=70` at every public entry point (the self-guard idiom); B302 is
  raise-only (`max(mp.mp.dps, 25)` — never lowers the shared global); B348's Bloch–Wigner uses scoped
  `mp.workdps` (it was itself a polluter-in-waiting). **MB13 extended with §4** (the test-order sibling):
  entry points own their precision; no probe may lower the global; "passes alone, fails in suite" is the tell.
- Also observed once (first post-merge run only): a transient `test_b207` failure that did not reproduce in
  either subsequent full run — logged as an unreproduced flake, not diagnosed, not papered over.

Zero promotions; no mathematical content changed — certificates only.

## 2026-07-02 — B351: the exact Chevalley 𝔢₆ (the cup-product program unblocked)

Seat note: the owner paused the peer session ("CC"); this session is now the main seat. The peer's
in-progress item — the `{4,8}`-integrability cup product, stalled at "signed structure constants failed
Jacobi" — is therefore picked up here. Part 1 banked as **B351** (`frontier/B351_exact_e6_chevalley/`):

- **The blocker removed, exactly.** Frenkel–Kac asymmetry cocycle on the E₆ root lattice; the full Jacobi
  identity verified on **all 76,076 basis triples over the integers: 0 violations**. The trap that killed
  the earlier attempt is isolated and documented at the fix site: with `[e_α,e_{−α}] = +h_α` exactly 1440
  mixed triples `(e_α,e_{−α},e_β)`, `(α,β)=−1`, violate Jacobi by `2e_β`; the Cartan-return sign is forced
  to `−h_α` by the cocycle convention (hand-derivation in the module).
- **The principal sl₂ and the exponents, exact:** `c = 2A⁻¹𝟙 = (16,22,30,42,30,16)`; `[h,e]=2e`,
  `[h,f]=−2f`, `[e,f]=h`; `dim ker(ad e) = 6` with ad-h weights `{2,8,10,14,16,22}` — the B347 framing
  `𝔢₆ = ⊕ Sym^{2m}` now exact.
- **θ built and verified:** automorphism on all pairs, involution, fixed = **52 = 𝔣₄**, minus = **26**;
  commutes with the principal sl₂; acts on the six exponent lines by **exactly `(−1)^{m+1}`** (+1 on
  `{1,5,7,11}`, −1 on `{4,8}`). This settles B347's flagged question at the algebra level: the
  hyperelliptic `(−1)^{m+1}` grading *is* the θ-grading `𝔢₆ = 𝔣₄ ⊕ 26`. The geometric identification
  (that the manifold's involution induces θ on the character variety) remains open — part 2 territory.
- **Next (part 2):** map B347's numeric `H¹` cocycles (`m ∈ {4,8}`) into this exact basis and evaluate
  `[z ∪ z] ∈ H²(4₁,𝔢₆)` against the four F₄ blocks (B265/B270).

Lock: `tests/test_b351_exact_e6_chevalley.py` (7 tests; pure ints/Fractions, 0.2 s). Zero promotions;
P1–P16 untouched; firewall intact.

## 2026-07-02 — B352: the cup-product obstruction computed — all six directions unobstructed at 2nd order

Part 2 of the `{4,8}`-integrability program (the B265/B270 open item; the peer session's stalled push, taken
over after the seat change). **Result: the obstruction `[z∪z] ∈ H²(π₁(4₁),𝔢₆)` vanishes for all six exponent
directions and the `{4,8}` polarization mix** — classes ≤ `1e-52` while the raw second-order cochains reach
`9.4e16`, so the vanishing is exactness (second-order deformations exist), not triviality. The θ-odd escape
sector is locally **real at second order**.

- **Controls (all clean):** the `m=1` direction = the actual A-polynomial curve → class `≤ 2.4e-62` ✓; random
  coboundary → `≤ 4.6e-74` ✓; **MB12 positive control** — the H² pairing functionals give `0.10–0.36` on random
  vectors, so the zeros are information; **θ-parity signature** — the `{4,8}`-block components sit 5–10 orders
  below the F₄-block floor (exact-zero by the B351 θ-grading vs numerical floor).
- **Machinery integrity:** relator identity to `9e-54`; the assembled `Ad ρ` preserves the exact B351 bracket to
  `5e-71`; cocycle residuals ≤ `2.6e-51`; ad-solve residuals ≤ `3.5e-56`. dps 100, MB13-§4 self-guarded.
- **Two honest architecture failures banked in the module docstring:** (1) double precision cannot span the
  `e^{±2mμ}` block range (numpy build: relator residual `1e+49`); (2) Euclidean normalization of the chain basis
  is not invariant (transported structure constants `1e-6..1e+73`, singular Gram). Working design: two-basis —
  exact integer root-basis brackets/Gram (B351) ⊕ block-diagonal chain-basis group action (antidiagonal
  closed-form intertwiners), vectors crossing via `S` at dps 100; rank decisions by structural rank + >20-order
  cliff assertions (the genuine block spectra span ~25 orders before a >60-order cliff).
- **Honest tier:** numerical (50+-order margins), second order only (no Goldman–Millson formality for knot
  groups), one point (the principal-geometric rep). Landing: exactly what a Menal-Ferrer–Porti-type smoothness
  theorem at exceptional type would predict — evidence for it, not a proof.
- **Gate B updated** (`OPEN_PROBLEMS.md`): the CRUX `T[4₁;E₆]` now has a genuinely 6-dim local moduli at second
  order; still open — the geometric θ-identification, all-orders integrability, the state integral itself.

Locks: `tests/test_b352_cup_product_obstruction.py` (structural tier ~18 s always-on; the full 741-s sweep gated
behind `OA_SLOW=1`, reproducer documented). Zero promotions; P1–P16 untouched; firewall intact (dimensions and
vanishing classes are *form*, K020).

## 2026-07-02 — PR #425 merged + verified; B353 closes L52 (the geometric θ-identification); L55 hygiene done

- **The audit branch (PR #425) merged to main and cross-verified.** B351's Jacobi claim confirmed by an
  **independent second implementation** (full Frenkel–Kac convention incl. the diagonal `Σaᵢbᵢ` term: the
  Cartan-return sign *emerges* as `−1` uniformly; 0 violations over 4000 random triples; the failing family under
  the `+h_α` convention is **exactly 1440 triples**, matching B351's count digit-for-digit). B352's controls
  (MB12 positive pairing; the `m=1` real-curve control; the θ-parity signature — `{4,8}`-block components 5–10
  orders below the F₄ blocks, the forced-zero fingerprint) reviewed and accepted.
- **B353 — the geometric θ-identification (L52, B347's last open item): DONE.** θ transported through the B352
  `S`-intertwiner into the geometric chain basis **is** the block-scalar `⊕ₘ(−1)^{m+1}Id_{2m+1}` (full 78×78
  identity, residual `7e-102` — Schur made exact); θ commutes with the holonomy Ad-image (`2e-88`), so the
  σ-twisted and θ-twisted Fox complexes coincide; per-line **gauge certificates** `J(z₀)=(−1)^{m+1}z₀+d⁰v`
  (residuals `9.9e-72…3.6e-79`). **The hyperelliptic involution induces exactly θ** on the E₆ tangent at the
  principal-geometric rep — operator-level, not sign-matching. Global variety-level statement: scope note only.
- **L55 hygiene:** atlas regenerated (334 probes, B350–B353 mined); fresh bare-`pytest` suite green on merged
  main; the `OA_SLOW=1` B352 sweep re-run once post-merge. Next free ID: **B354**.

Locks: `tests/test_b353_geometric_theta_identification.py` (3 tests, ~19 s). Zero promotions; P1–P16 untouched;
firewall intact (an involution identification is *form*, K020). Next in the arc: L53 (third-order/Massey), L54
(adjoint-torsion Galois), L51 (owner outreach send).

## 2026-07-02 — B354: the interface-pairing certificates (cross-session verified layer) + B332 correction + L56

- **Cross-session integration under verify-don't-trust.** A solo scrutiny-seat session delivered the
  "multiplicity × outer-nothing" interface-pairing computation (handoff + self-certifying reproducer, received and
  re-run — all four stage gates pass). Verified layer banked as **B354**; the rest tiered honestly.
- **Lineage correction folded in:** the golden/silver interface relations, the `(1,2)` intersection and its
  `κ∈{−4,−2}` fork are **B131/V120** (banked June 9; Kitano–Nozaki 2020 prior art, NOVELTY_AUDIT R2) — the
  cross-session "first column of a table nobody has" framing is corrected; B174 has the same-seed gluing landscape.
- **New and verified (B354, all exact sympy):** (1) the **strong-channel kill** re-derived by Gröbner —
  `Fix(T_i)∩Fix(T_j) = {(0,0,0),(2,2,2)}` for `(1,2)` and `(1,3)`, = `Fix(T_a)∩Fix(T_b)` (bulk sharing is
  family-universal, carries no pair data); (2) the **exact pair-point certificates** — irreducible minpolys
  (quintic `(1,3)`, cubic `(2,3)` in `T=m²`) whose κ-images reproduce B131's banked numeric forks on all 8 values;
  (3) the **classical seam-null** — prime odd degrees ⇒ no quadratic subfield ⇒ no `√−15` in the classical pair
  arithmetic (third channel closed after B336); (4) the **divisibility law** `RᵐLᵐ≡I mod p ⟺ p|m` (exact, one
  line — the mechanism under the parity texture and the bronze mod-3 scalar); (5) the **parity-texture exact legs**
  (golden `l=−2` fiber `{1,4}`, silver `{4}` only). CONDITIONAL: bronze pair-specificity (numerical, 900-start
  null reproduced; exact `A_bronze` elimination open).
- **B332 FINDINGS annotated (the deck correction, verified):** the generation deck of the 3-fold cyclic cover acts
  via the **hyperbolic monodromy `A`**, not the elliptic `g` (`det(A−I)=−1` ⇒ cover unwraps the base). B343/TBM
  unaffected (`A` and `g` share charpoly `x²+x+1` mod 4 — checked); two-level structure: torsion = democratic,
  fiber = `φ²`-ordered. The algebra `g=−R·L⁻¹` stays true; the "generation-cycling element" reading retracted.
- **L56 registered:** the quantum-pair program (Weil traces, level-15 overlap fingerprint tables, the flattening
  no-go, the level-45/phase-table next shots) — spot-checks pass (the claimed `(1,2)`-only quartic: irreducible,
  4 real roots in `(0,1)`, factors over `ℚ(√5)`, disc `3¹⁴·5⁷`) but **BLOCKED on the Weil reproducer**; nothing
  from that layer banked.

Locks: `tests/test_b354_interface_pairing_certificates.py` (6 tests, <1 s, exact). Zero promotions; P1–P16
untouched; firewall intact (forks, certificates and textures are *form*; the pre-registered SM/PMNS construction
cross-session was killed by its own declared null — the discipline held).

## 2026-07-02 — The value-boundary queue registered; B355 (W1.1): the Weil layer independently, the phase null fired

- **The campaign registered** (`docs/OPEN_LEADS.md`, "The value-boundary queue"): compute each genuinely-open
  relational channel (multiplicity/gluing/quantization) to a two-outcome verdict; pre-registered nulls; MB guards
  per probe; atlas/FAILURE_ATLAS consult first (this cut one planned probe *at planning stage* — the `2T↪E₆` fork
  was already banked as B329; `OPEN_PROBLEMS` Gate B synced accordingly).
- **B355 — the Weil layer, independently (W1.1).** `W_N` for `SL(2,ℤ/N)`, N=3,5,15, built from scratch with the
  conventions *earned*: a systematic `(c,d,μ)` search returns exactly `d≡−2c`, `μ=g_c(N)` as the
  relation-satisfying family. Five gates pass (relations; the composite-level Gauss `tr ρ₁₅(T)=i√15` — the
  CRT-twist catch; twisted-factor trace multiplicativity; word well-definedness; `⟨R,L⟩=SL(2,ℤ/15)`, order 2880).
- **The cross-session quantum layer (L56): VERIFIED** — trace table (all 1; bronze 3 at N=3,15), the
  operator-level divisibility law (`ρ_N(A_m)=1 ⟺ N|m`, incl. seed-15 at the seam level), and the fingerprint
  tables recomputed in gauge-invariant projector form: (1,2) has **11 distinct values** incl. the exclusive
  quartic `2025T⁴−3375T³+1935T²−435T+31`; (2,3) is quartic-free, golden-tower only; every recognized quadratic
  disc is `5·square` — the flattening no-go confirmed. L56 → RESOLVED.
- **The new result (pre-registered null — FIRED):** the gauge-invariant *triple phases* `tr(P_iQ_jR_k)` across
  the three seeds are **all exactly real** — 605/605 (numpy sweep; mpmath spot floor `1.6e-40`). The phase
  aperture at level 15 is **empty**; the flattening extends to Bargmann-type triples. Mechanism ingredient
  verified: complex conjugation implements `Ad(diag(1,−1))` on the image (`conj(T)=T⁻¹`, `conj(S)=S⁻¹`); the
  full reality proof for the triple class is the named residual. Remaining aperture in this lane: level 45 (W1.4).

Locks: `tests/test_b355_weil_layer_independent.py` (6 tests, ~56 s). Zero promotions; P1–P16 untouched; firewall
intact (fingerprints and nulls are *form*; recognitions are numerical-tier, honestly labeled).

<!-- New entries go ABOVE this line, newest first is also acceptable — pick one order and keep it.
     This log uses oldest-first. -->

## 2026-07-02 — B356 (W1.2): the σ-stability quick pair — the chirality window is exactly the Eisenstein ω

- **The det-lemma (exact, all binaries):** the det-character of a 2-dim irrep is trivial **iff** it is
  quaternionic (FS = −1) — verified across 2T/2O/2I/S₄ from concretely-built groups with derived, exactly-gated
  character tables. Every `SL(2,ℂ)`-factoring route forces the quaternionic 2: B327's "complex 2′/2″ escape" is
  closed at the determinant level. **Mod-3 blindness:** `ω^k−1` divisible by `(1−ω)` ⇒ the mod-`√−3` route
  cannot see the twist.
- **H104 RUN — the chirality scan** over `{A₄,S₄,2T,2O,A₅,2I}` (all faithful 27-dim assemblies with
  `(Sym³V)^G ≠ 0`): complex (chiral-candidate) assemblies exist **only for A₄ (1028/1089) and 2T
  (70262/71192)** — exactly the two groups with `ℤ/3` abelianization (the ω-characters); `S₄/2O/A₅/2I` are
  closed by the **reality theorem** (all characters real ⇒ every assembly self-dual). The factor-route
  identities (SU(2)-factoring / single-SU(3)-factor / diagonal trinification ⇒ σ-stable, every finite G) are
  stated and generalize B329's two computations.
- **Method note:** no transcribed tables — groups built concretely (Hurwitz/icosian quaternions;
  permutations), tables derived from tensor powers + concrete abelianization characters (A₅ via the icosahedral
  seed; the `φ↔1−φ` ambiguity is the Galois table-automorphism, verdict-invariant), snapped to exact values and
  gated by exact orthonormality + FS + `Σd²=|G|` (the gates caught two real development bugs).
- **H103 sharpened** (wave 2): whether any ω-window assembly is *realized* by a genuine `E₆`-conjugacy class
  with nondegenerate invariant cubic — a finite question. Ledger rows updated (HINT_LEDGER H104 → RUN).

Locks: `tests/test_b356_sigma_stability_scan.py` (4 always-on ~1 s; the full 2T/2O/2I sweep under `OA_SLOW=1`
with the banked counts). Zero promotions; P1–P16 untouched; firewall intact (windows and closures are *form*).

## 2026-07-02 — B357 (W1.3): the E₆ boundary restriction — rank 6/6, Lagrangian certified, the universal-τ identity

- **rank(r) = 6/6:** every B347 tangent class restricts to a nonzero class in its 2-dim boundary block (class
  residuals at per-block floors, `1.5e-60…1.1e-27`) — **no peripherally-invisible E₆ deformations**; with
  block-orthogonality of the Killing pairing this **certifies the image of `H¹(M,𝔢₆) → H¹(T²,𝔢₆)` is
  Lagrangian** (6 = half of 12) — the classical integration-cycle statement a `T[4₁;E₆]` state integral needs.
- **The universal-τ identity:** on every cocycle of every block, the leading NZ functionals satisfy
  `K(z(λ),h) = τ·K(z(µ),h)` with one constant `τ = −2√3·i` = the cusp shape (SnapPy control to 12 digits),
  **uniform across all six exponents** (deviation ≤ `1.3e-52`) — the leading peripheral datum does NOT split by
  exponent; no "higher cusp shapes" at first order. Mechanism (stated): `U = exp(N̂)`, `V = exp(τN̂)` share one
  nilpotent; `K(·,h)` kills `im N̂ ⊕ ker N̂`.
- **Controls (MB12):** ω nondegenerate on the honest orthonormal `H¹` basis in every block (dets nonzero,
  antisymmetry ≤ `1e-55`); `φ_µ ≠ 0` in every block. A first (invariant-line) basis was ω-degenerate and
  mis-spanned `H¹` — caught by exactly these gates and replaced; the depth-2 canonical Gram is the named
  follow-up (the τ-identity shows the naive two-functional coordinates have rank 1).

Locks: `tests/test_b357_e6_boundary_restriction.py` (2 always-on ~2 s; all-six sweep under `OA_SLOW=1`).
Zero promotions; firewall intact (ranks, Lagrangians and τ are *form*).

## 2026-07-02 — B358: the seam, exactly certified — √−15 lives in the twisted quantum-pair sector (and provably not in the canonical one)

- **The escalation protocol ran as pre-declared** (higher precision → exact; second independent construction →
  two): the cross-session Par-inserted seam claim was rebuilt in EXACT Fraction arithmetic over `ℚ(ζ₆₀)`
  (`cyclo_engine.py`; the full `C[j][l] = tr(Par·W₁ʲW₂ˡ)` tables; exact Galois H-average; exact solve in
  `{1,√5,√−3,√−15}`).
- **The dichotomy (the result):** the **theta/Jacobi lift** (cross-session construction;
  `Par·W·Par⁻¹·W⁻¹ = X¹Z²`) carries `√−15` in **44/49** nonzero doubles — exact small rationals; flagship
  `tr(Par·P₀Q₄) → −1/48 −(1/80)√5 −(1/48)√−3 +(1/48)√−15`, certified coefficient-for-coefficient at the
  claimed label. The **canonical lift** (B355; `Par` commutes with the image) has **`s ≡ 0` exactly on all
  doubles**. Single-seed controls: `r = s = 0` exactly, both lifts. The exact table also settles the
  height-blocked 217 from the cross-session run.
- **Meaning (honest form):** after five closed channels, `√−15` appears **exactly, and only, in the
  Heisenberg-twisted sector of the two-seed pairing** — the seam coefficient is a function of the lift's
  theta-characteristic. **L57 registered:** is the characteristic *forced* by the pairing geometry (theta
  structures / gluing frame), or a choice? Nothing promoted either way; field-membership statement, not
  physics.
- Committed exact C-tables (regenerable) + independent dps-40 numeric spot-checks of both.

Locks: `tests/test_b358_seam_certification.py` (4 always-on ~1 s; full counts under `OA_SLOW=1`). Zero
promotions; firewall intact.

## 2026-07-02 — B359: the seam form — pair-specific and parity-selective, exactly

- **Three exact paths to the flagship first:** the cross-session symbolic certificate (integer vectors mod
  `Φ₆₀`, Galois-norm inversion) was run on this machine and **PASSES** — `s = 1/48` exactly — joining B358's
  two independent exact computations.
- **The seam form (the L57 opener, run the day it was proposed):** extending B358's engine to seed 3, both
  lifts, all exact: **(1,3) golden×bronze is seam-DARK** (0 of 39 doubles, exactly); **(2,3) silver×bronze is
  bright with its own disjoint value set** `s ∈ {±1/144, ±1/288}` (the bronze pair's denominators carry `3²`);
  the canonical lift is 0 everywhere (the dichotomy control, again). So the twisted-sector seam data is
  **pair-specific** — and **selective**: both bright pairs contain the even seed; the odd–odd pair is dark —
  the parity texture (B354/B356) surfacing at the seam level. **Observed pattern (3 points), with the
  pre-registered prediction: (1,4) bright, (3,5) dark.**
- Committed exact artifact (regenerable; OA_SLOW regeneration lock); B358's guards cover the shared engine.
  L57 (is the characteristic forced?) remains the governing question; nothing promotes.

Locks: `tests/test_b359_seam_form.py` (3 always-on <1 s; full regeneration under `OA_SLOW=1`). Zero
promotions; firewall intact.

## 2026-07-02 — B360: the selection rule, tested — both parity readings die; silver-selectivity survives

- **The pre-registered B359 predictions ran (exact, theta lift): (3,5) DARK ✓ — but (1,4) DARK ✗** (the
  "contains an even seed" reading refuted) **and (2,4) BRIGHT** (36/49; `s ∈ {±1/120,±1/240,±1/480}` — the
  "opposite parity" reading refuted too). Three points did not make a law; the declared test killed both
  readings in one run.
- **Surviving rule (6 pairs, exact): bright ⇔ the pair contains silver (m=2)** — the unique seed among 1–5
  that is **regular-elliptic at 5 and nontrivial at 3** (`disc(A_m) = m⁴+4m² ≡ 0 mod 5` for m∈{1,4,5};
  `3|m` trivializes m=3). Two hypotheses separate — H-min (the `A₂` residue class specifically) vs H-loc
  (any 5-elliptic ∧ 3-nontrivial seed) — with the **pre-registered discriminator: pair (1,7)** (m=7 qualifies
  under H-loc): bright ⇒ H-loc, dark ⇒ H-min.
- New exact data: (2,4)'s `s`-set is a subset of (1,2)'s denominators (no new primes), unlike (2,3)'s
  bronze-`3²` values — the value-map (pair ↦ s-set) keeps accumulating structure for the post-L57 pass.

Locks: `tests/test_b360_seam_selection_rule.py` (3 always-on <1 s; regeneration under `OA_SLOW=1`). Zero
promotions; firewall intact; everything remains lift-sector mathematics pending L57.

## 2026-07-02 — B361: the seam's local law — the discriminator decides H-loc

- **(1,7): BRIGHT** (20/31, `s ∈ {±1/48, ±1/96}`) ⇒ H-min (literal contains-2) **refuted**; **(3,7): BRIGHT**
  with the **value-echo** — its `s`-set is *identical* to (2,3)'s (`{±1/144, ±1/288}`).
- **The law (8 pairs, exact, zero counterexamples): the Par-inserted pair invariant carries `√−15` iff the
  pair contains a seed elliptic at both primes** (char poly irreducible mod 3 and mod 5; m = 2, 7 qualify;
  m = 1, 4 are 5-parabolic, m = 3 is 3-trivial, m = 5 is 5-trivial). The shape is exactly natural for
  `√−15 = √−3·√5` — one seed carrying both primes' quadratic data — **and the single-seed controls stay
  exactly clean: the key needs the lock; multiplicity remains essential.**
- The value-map (pair ↦ s-set) is finer than partner-only ((1,7) ≠ (1,2) sets but (3,7) = (2,3)) — real
  structure registered for the post-L57 pass. Next cheap discriminators pre-registered: (2,7) bright,
  (1,5)/(4,5) dark. Stated as a law of the computed range, not proved; theta-lift sector pending L57.

Locks: `tests/test_b361_seam_local_law.py` (3, <1 s). Zero promotions; firewall intact.

## 2026-07-02 — B362 + B363: the law at 11 pairs; the seam's lift anatomy — two-sided and class-bound

- **B362 (EXACT): three pre-registered predictions, three hits** — (2,7) BRIGHT (12/17, `s`-set = (1,7)'s),
  (1,5) DARK, (4,5) DARK. **The local law stands at 11 exact pairs, zero counterexamples:** bright ⇔ the pair
  contains a doubly-elliptic seed (m ∈ {2,7} among m ≤ 7).
- **B363 (the L57 opener):** the seam as a function on the lift torus. Verdicts: canonical×canonical dark in
  **both frames**; **all 225 one-sided Heisenberg twists dark**; **theta×canonical dark in either slot
  order**. With the exact bright theta×theta side: **the seam is TWO-SIDED — it requires the theta class in
  BOTH slots** (bilinear in the characteristic — the lift-sector echo of `√−15 = √−3·√5` and of the
  multiplicity theme). The **Par-lemma** (one line): Par-commuting lifts force real Par-traces ⇒ `s ≡ 0` —
  non-commutation is *necessary*; the scan shows it is *not sufficient*. The theta lift is not a Heisenberg
  twist of the canonical lift — it lives over the non-square quadratic-character class (`c = 2⁻¹ ≡ 8 mod 15`).
- **L57, restated sharply:** does the two-seed pairing geometry force the theta class on both slots
  simultaneously? (A theta structure on the *gluing* torus would decorate both boundary restrictions at once —
  the encouraging shape.) Analytic step, not a scan; now the program's sharpest open question.

Locks: `tests/test_b362_seam_law_confirmations.py` + `tests/test_b363_seam_lift_anatomy.py` (6 always-on,
<1 s). Zero promotions; firewall intact.

## 2026-07-02 — B364: the two lifts are two polarizations — L57 becomes a spin-structure question

- **Tested:** is the theta lift *the* geometric lift (the level-15 theta-transformation action)? **T-side:**
  the triangular family (`E = n(n−1)/30`) is T-stable with **exactly the theta lift's multiplier** (analytic
  identity + `6e-15`). **The control killed the conclusion:** the square family (`n²/15`) is *also* T-stable
  with **exactly the canonical multiplier** (`8e-15`) — both classes arise as theta families; T-stability
  forces nothing.
- **L57 sharpened to polarization form:** the two lift classes = two polarizations (half-characteristic/odd
  `(2n−1)²/120` vs integral `n²/15`); *which does the two-seed gluing induce on the shared fiber's theta
  bundle?* **Named candidate (conjecture): the puncture's odd spin structure selects the half-characteristic**
  — one bundle, one lift map, both monodromies ⇒ the theta class forced on both slots at once (exactly B363's
  measured two-sidedness). Honest gap: the S-side identification (Poisson shows half-characteristic `ζ₃₀`
  data; not completed).

Locks: `tests/test_b364_theta_polarization.py` (2, <1 s). Zero promotions; firewall intact.

## 2026-07-02 — Wave 2 (the probation campaign) registered

The post-seam queue: W2.1/W2.2 the L57 endgame (S-side identification + the odd-spin argument — the seam arc's
probation gate); W2.3 the value-map `s(m₁,m₂)` (pre-registered local-symbol functional form); W2.4 the
cover-tower pairing (`tr(A₁³)=18` ⇒ the golden 3-fold cover IS the m=4 seed — the seam × generation-deck
question made computable); W2.5 dynamics (L53 + depth-2 Gram); W2.6 the cyclic-dilog bridge (seam data →
Kashaev `q=ζ₁₅` partition-function shadow — the values-meet-dynamics candidate); W2.7 sweepers; W2.8 the owner
outreach + a firewalled gravity reconnaissance. All two-outcome; everything on probation pending L57.

## 2026-07-03 — B365 (W2.1): S-closure fails for both (the metaplectic doubling); the vanishing signature discriminates

- **My pre-registered closure prediction was REFUTED by its own test** (both families' S-projection residuals
  ≈ 0.63): the corrected Poisson algebra shows the half-shift `(−1)^m` twist — **at odd level the S-transform
  forces the level-30 metaplectic doubling for BOTH polarizations**; the two 15-dim lifts are graded slices of
  the level-30 theta space. Selection does not happen at the S-closure level. (The campaign's second
  self-refuted prediction; both redirected the question productively.)
- **The surviving discriminator — the half-period vanishing signature:** the **triangular** family vanishes at
  **exactly one** half-period (`z = 1/2`, one basis function, exact at `3.3e-21`) and nowhere else; the
  **square** family vanishes at **all four** half-periods. Single-distinguished-point = the odd-theta
  signature — and the once-punctured fiber has exactly one marked point. **W2.2 sharpened to a concrete
  identification: the puncture's position in the fiber quantization ↔ the `z = 1/2` point of the triangular
  polarization.** The seam arc remains on probation pending that argument.

Locks: `tests/test_b365_polarization_signature.py` (2, <1 s). Zero promotions; firewall intact.

## 2026-07-03 — B366 (first installment): the invariant spin sector lives in the seam-bearing class

- **Two exact lemmas:** (1) `SL(2,ℤ)` fixes only the origin among the fiber's 2-torsion (the puncture = the
  unique invariant point; the three half-periods one orbit); (2) the odd characteristic `[½,½]` is the unique
  invariant spin structure (both generators fix it; the three evens form one orbit).
- **With the B364/B365 identification** (`T+=[½,0]` — its B364 T-multiplier independently matches `T` fixing
  `[½,0]`; `T−=[½,½]`; `S+=[0,0]`; `S−=[0,½]`): **the seam-bearing (a=½) class contains the unique invariant
  spin sector; the canonical (a=0) class contains none.** The gate's forcing argument has its exact skeleton:
  an MCG-equivariant single-sector quantization of the punctured fiber can only use the invariant sector.
- **Pre-registered, not yet passed:** the classical S-mixing prediction `T−→T−, S+→S+, T+↔S−` — three quick
  numerical ansatz attempts failed for three recorded reasons (degenerate strip; mis-derived prefactor;
  conflated growth measurement); the derivation-first S-transformation redo is the named next step. **The
  seam arc remains ON PROBATION until it passes.**

Locks: `tests/test_b366_invariant_spin_sector.py` (3, exact, <1 s). Zero promotions; firewall intact.

## 2026-07-03 — B366 part 2: the derived S-transformation — the closure dichotomy (W2.2 verdict)

- **The pre-registered naive S-mixing pattern FAILED** (`T−→T−, S+→S+, T+↔S−` is NOT how the geometric `S`
  acts at level 15) — the 4th failed-and-sharpened prediction of the arc; superseded by the derivation.
- **Two exact closed formulas** (one Jacobi inversion each; `j`-dependence cancels identically in both
  prefactors): the **triangular family is S-closed at fixed τ** — image = same family at `z + (τ+1)/30`
  (a 30-torsion Heisenberg translation), `ζ₃₀` kernel, prefactor `e((30z+1)²/120τ)`; the **square family
  exits** — image at `(z/2, τ/4)` (a rescaling, not a Heisenberg operation; B365's doubling from the S side).
  Verified 7.1e−12 / 1.2e−10, twist-shift identity 1.1e−15, half-K stable; no fits, no free parameters.
- **The gate's verdict, premise named:** within the standing premise (pair states = level-15 fiber theta
  functions with the standard Heisenberg/metaplectic action), a modular quantization needs `S` to act on the
  state space at the given modulus — only the seam-bearing class has that; part 1's invariant-spin selector
  agrees. **The theta lift is forced at this tier; the seam form is an invariant of the quantized pair.**
  The premise stays a named modeling assumption; nothing promotes.

Locks: `tests/test_b366_s_transformation.py` (3, <1 s). W2.2 RESOLVED; next: W2.3 (the value-map).

## 2026-07-03 — W2.4/B368 premise corrected (verified): equal trace ≠ same seed

- The queue row's premise (`tr(A₁³) = 18 = 4²+2` ⇒ the golden 3-fold fiber cover IS the m=4 seed) is
  **refuted by exact integer arithmetic** (cross-checked in-sandbox): fixed-point binary forms
  `(RL)³ → (8,−8,−8)`, content 8, primitive disc **5**; `R⁴L⁴ → (4,−16,−4)`, content 4, primitive disc
  **20**. Primitive discriminants are conjugacy invariants ⇒ not conjugate. The genuine cover tower is
  `(RL)^k` (disc 5, unit powers) — a different column from the metallic family (disc `m²(m²+4)`).
- B368 re-scoped accordingly in `OPEN_LEADS` (W2.4); equal-trace-different-seam is an independent
  finer-than-spectrum instance for the ledger.

## 2026-07-03 — B367 (W2.3) step 0: the exact six-pair s-matrices — every pre-registered check passed

- Pre-registration committed BEFORE computing (PR #442). Fresh theta-lift Weil matrices (W_m = WR^m·D^m,
  ℚ(ζ₆₀) engine), all six pair s-matrices **fully identified exactly** (no PSLQ). Gates: orders
  (20,12,6,20), projector sums/idempotence exact, single-seed controls clean, **all row/col sums exactly 0**.
- **Reconciliation complete — three independent computations now agree on every comparable entry:** the 8
  relayed (1,2) entries exact (S0.2); the relayed 11×11 (1,2) matrix reproduces entry-by-entry with its
  structure now exact — **rank 4, Coxeter-odd, {4,8}-sector = rows {0,4} disjoint** (S0.6); the (2,3)
  ±1/144 entries exact AND **the pre-registered ±1/288 prediction HIT** (the height-blocked entries; S0.3);
  the (1,3)/(1,4) zeros upgrade to **exact tier** (S0.4); first complete (2,4)/(3,4) tables — value sets
  {±1/120,±1/240,±1/480} and {±1/48,±1/96} (S0.5).
- **Exact aggregates Σs² (supersede all partial values): 43/7200 · 1/192 · 3/3200 · 1/2304 · 0 · 0**
  ((1,2) > (3,4) > (2,4) > (2,3) > the two exact zeros). V1 denominator hypothesis holds on all data
  (2^a·3^b·5^c, a≤5, b≤2, c≤1).
- Locks: `tests/test_b367_step0.py` (5 always-on + 1 OA_SLOW regen). The V3 local-symbol search + null +
  held-outs run NEXT, exactly as pre-registered — no formula claim is licensed by step 0.

## 2026-07-03 — B367 step 0 (continued): the completed table REFUTES the B361 local law at pair (3,4)

- (3,4) is **bright** ({±1/48, ±1/96}, Σs² = 1/192, second-largest) with **no seed elliptic at both
  primes** — the banked "bright ⇔ a both-elliptic seed" rule (11 pairs) dies on the twelfth pair. The
  covering repair dies on (1,3) (identical covering pattern, exactly dark). W₁/W₄ have identical level-15
  spectra ⇒ **support is strictly finer than spectra + ellipticity types.** Two independent computations
  agree on (3,4). B361's row updated; its confirming pairs remain valid data.

## 2026-07-03 — suite hygiene note (pre-existing, tracked): one intermittent flake per full run

- Two consecutive full runs each showed ONE failing test, a DIFFERENT one each time (b207 volumes
  monotonicity, then b137 m=2 sealing) — both pass standalone and in targeted groups, both untouched by the
  merged diffs (which were additive). Reads as load/ordering sensitivity (SnapPy retriangulation randomness
  / sympy cache pressure), not mathematics. Tracked as a hygiene item; targeted verification (both flaked
  tests + all diff-adjacent locks: 21 passed) gates the current merge.

## 2026-07-03 — B367 (W2.3) COMPLETE: the V3 verdict is outcome (B) — the value map is not CRT-local

- The pre-registered model (`s = X3[3-local] · X5[5-local] · X4[4-part]`, exact multiplicative tensor
  completion) **fails on the true data; 0/200 matched random tables pass** (the test has teeth). Diagnosis,
  exact and graded: (2,4) and (2,3) factor individually; **(1,2) (rank 4) and (3,4) (the law-breaker) do
  not**; every two-pair joint is inconsistent (even (2,3)+(2,4), sharing seed 2). Ranks: 4, 2, 1, 2 —
  rank alone does not decide factorability.
- **Probe conclusion: neither the support (the refuted law) nor the values (V3) factor through
  (m mod 3, m mod 5, CRT labels)** — the seam form is an eigenbasis-geometry invariant in a strong sense.
  Per the pre-registration the lead closes at this complexity (open at higher complexity, not
  "impossible"); the exact six-pair table is the banked exhibit. Any finer-input model (fixed-point form
  discs; Galois-cocycle data) requires a NEW pre-registration before computing.
- Locks: +1 (the V3 verdict + graded diagnosis). W2.3 CLOSED; queue advances (B368 corrected scope, W2.9
  concatenation-kill, W2.5).

## 2026-07-03 — B369 (W2.9) DONE: concatenation kills the seam (prediction hit) + the rotation-Galois identity

- **The registered prediction HIT, 6/6**: every two-block word `R^{m₁}L^{m₁}R^{m₂}L^{m₂}` tested
  ((1,2),(2,1),(1,3),(2,3),(3,4),(1,4)) is **seam-null** — zero √−3/√−15 in every eigenprojector readout,
  exactly. Sharpest instance: the (3,4) word is clean while the (3,4) PAIR is bright at Σs² = 1/192. **The
  seam lives in the unglued pair relation; gluing the same blocks into one monodromy kills it.** The
  single-object wall extends to these first non-seed single objects (word orders 4,4,20,20,4,10).
- **One design-error gate, diagnosed into a finding**: the naive rotated-word multiset gate failed because
  it tested a non-invariant (the readout is (lift,Par)-sector data; Par-conjugation = the X¹Z² Heisenberg
  twist). The exact structure: **rotation acts by the √5-Galois involution, exponent-wise:
  r₍₂,₁₎(a) = σ(r₍₁,₂₎(a))**. Same manifold, lift moved by Heisenberg, arithmetic moved by Galois.
- Locks: `tests/test_b369_concat_kill.py` (4, exact, <1 s). The June word-trace lead fully resolved.

## 2026-07-03 — B368 (W2.4, corrected scope) DONE: the seam sees the deck equivariantly

- **The deck identity, exact (all 240 cells):** `t_cover(a,b) = t_base(7a mod 20, b)` — the (RL)³ cover's
  pairing against m=2 is the base (1,2) pairing relabeled by the deck's exponent action `a↦3a` (forced by
  `P_a(W₁³)=P_{7a}(W₁)`, gcd(3,20)=1; verified against the banked B367 table). **Covers create no new seam
  content against a fixed partner; the form is ψ³-equivariant, not blind.**
- Cover exponent list = `3·K1 mod 20 = {0,2,3,5,7,8,12,13,15,17,18}` — the relayed cross-session list now
  verified. Tower singles `W₁^k` (k=2..5) all clean — the wall extends up the tower.
- **Trace-18 twins split at the seam:** the cover pair carries the base's 14 values (±1/48…±1/480); the
  m=4 seed pair carries {±1/120,±1/240,±1/480} — equal trace, equal lift order, different seam forms.
- Gate-C reading (firewalled): a ℤ/3 deck does not manufacture seam-distinct generation sectors — the
  sheets carry relabeled copies of one form. Locks: `tests/test_b368_cover_tower.py` (4, exact).

## 2026-07-03 — W2.8 prep: the outreach package upgraded (Brief S added)

- `frontier/EXPERT_OUTREACH.md`: **Brief S (new, the lead exhibit)** — the pair-level Weil invariant
  (the seam law) as a bounded prior-art question for a modular-data/Weil-representation specialist
  (type-matches named with verify flags; Deloup–Turaev reciprocity flagged as the closest known
  neighborhood). Gates B and C "what we supply" upgraded in place (the exact 𝔢₆, the certified boundary
  Lagrangian + universal-τ; the ψ³ deck equivariance + the chirality window). Sequencing updated: Brief S
  first. **Sending remains the owner's action**; log sends/replies here.

## 2026-07-03 — W2.5 opened: B370 pre-registration committed (third-order Massey + depth-2 Gram)

- `frontier/B370_massey_depth2/PREREGISTRATION.md`: leg A = the third-order Maurer–Cartan obstruction
  per exponent direction (the order-3 Fox/BCH relator expansion DERIVED SYMBOLICALLY FIRST — the B366
  lesson — validated on the m=1 integrable control before any verdict; Massey class read modulo its
  indeterminacy with an MB12 transverse-pairing control); leg B = the depth-2 boundary Gram against
  unchanged B357 conventions with three declared readouts (symmetry / τ-persistence / θ-blocks). Both
  legs two-outcome; completes the Gate-B classical-germ package. Execution next session (fresh context
  for the derivation; machinery = B352's two-basis architecture, dps 100).

## 2026-07-03 — W2.8/L51 set DORMANT (owner directive): compute first, outreach only at exhaustion

- Owner directive (reaffirming the standing compute-first rule): **no external contact of any kind until
  the in-sandbox computational paths are exhausted.** The outreach briefs (incl. Brief S) remain banked as
  preparation artifacts only; nothing has been sent, and nothing will be without the owner's explicit
  decision at the exhaustion point. The live queue is computational: B370 execution, the level-45
  sweeper, the (1,3)/(3,4) discriminator, the finer-input value-map re-registration.

## 2026-07-03 — GOVERNANCE amendment: the promotion-audit lane + automated gates + the decadal review

**Rationale (owner-approved; §10-compliant — additive discipline, no rule weakened):** Phase B ran with
the §5 promotion gates idle ("zero promotions" was practice, not law), leaving `CLAIMS.md`
unrepresentative of the project's load-bearing exact results and creating an epistemic asymmetry
(refutations bank decisively; positives could never graduate). The staging principle (§6.2 — verification
attaches at promotion) was designed expecting promotions to fire; they never did. Instituted:

- **§5.1** — the mathematics lane (eligibility is independent of physics readings; the framing lock
  governs interpretation, never eligibility) + the **Certified data** ledger section (`E`-ids) + the
  **promotion audit** (periodic §5-bar sweep of `frontier/`; promotions only through the gates, logged).
  The celebrated metric changes: not "zero promotions" but "promotions with zero unmarked retractions."
- **§11** — automated gates (`scripts/gates/gates.py`, suite-locked by `tests/test_repo_gates.py`;
  7 gates green at institution: framing lock, claims integrity, one-way firewall, append-only log,
  atlas freshness, attribution, forbidden artifacts) + the **decadal review** (every ~10 merges;
  ledger `docs/progress/REVIEWS.md`, seeded with Review 0 at this commit's anchor).
- Propagated: `CLAIMS.md` header + Certified-data section; `ARCHITECTURE.md` ledger row; `README.md`
  zero-promotions lines. The physics firewall, the one-way room rule, HELD, and every §5/§6 bar are
  untouched. The promotion audit itself is registered in `OPEN_LEADS` as a dedicated session.

## 2026-07-03 — the promotion-audit sweep (collection stage) COMPLETE

- Four parallel strict sweeps over frontier/B1–B369 FINDINGS (instruction: when in doubt, NOT).
  **Yield: 63 candidates** — 33 PROVEN-tier, 7 CONDITIONAL-tier, 20 DATA-tier (E-ids), 3
  adjudicate-tier (dps-100 computer-assisted) — of ~350 probes; 297 NOT with recorded reasons.
- Compiler flags for adjudication: B368/B369 mis-triaged NOT (pre-reform stamps read literally —
  re-read); B263 has no FINDINGS (hygiene); correction-chain candidates (B112, B131, B92/B95/B153,
  B134/B136, B204) adjudicated with their qualifications; B370 classified when leg A banks.
- Worksheet: `audit/PROMOTION_AUDIT_WORKSHEET.md` (private audit room; iCloud-synced). The
  adjudication session (task #167) re-reads every candidate, runs §6, verifies locks, writes scoped
  statements, and promotes survivors in ONE reviewed PR. Bar, never importance (owner-confirmed).

## 2026-07-03 — B370 leg A DONE: all six E₆ tangent directions unobstructed at THIRD order

- Jet-arithmetic method (no BCH transcription; self-gating P₁/P₂/P₃), dps 100, 2.9 h. Controls:
  coboundary class 6.2e−87 (exact tier), the integrable m=1 control 9.6e−62 (floor). **Every
  direction's third-order class sits 5–10 orders below its own P-gates** — m=4: 8.5e−63, m=5:
  3.8e−61, m=7: 1.2e−55, m=8: 3.1e−54, m=11: 1.1e−48 (floors grow with the Sym-block range, the
  B352 pattern). MB12 non-vacuous on every nontrivial indeterminacy span (ranks 0,1,1,3,4,4).
- **The 6-dim local moduli's integrability evidence reaches order 3, escape sector included.**
  Honest tier: computer-assisted; order 4+ untested; leg B (depth-2 boundary Gram) runs next.
- Locks: `tests/test_b370_massey.py` (4, from the banked JSON). Pre-registration honored end-to-end.

## 2026-07-03 — B370 leg B: two gate-blocked runs, bug localized (no verdicts read)

- The pre-registered first-order τ-gate stopped both leg-B executions (τ spread 3e+04 vs the banked
  uniform −2√3·i) — the depth-2 readouts were never interpreted. Isolation test localizes the bug to
  the root→TG bridge: B352's chain basis relates to TG's symrep basis by the **antidiagonal
  intertwiners** (`_intertwiner(m)`), not a diagonal rescale. Fix identified (compose the bridge with
  the intertwiner); the m=1 τ-gate is the acceptance test. δ = φ_λ − τ·φ_µ stays the right invariant.
- Method note: the gate design paid for itself twice — two O(1) "defect matrices" were produced and
  correctly discarded as convention artifacts before any interpretation.

## 2026-07-03 — B370 leg B DONE (W2.5 COMPLETE): the universal-τ is strictly first-order, and the
## depth-2 bending is θ-graded

- The τ-gate certified the pipeline on the third run (the fix: compose the root→TG bridge with B352's
  antidiagonal intertwiners): **τ = −2√3·i uniform across all six directions, spread 1.4e−63**;
  off-diagonals at floor. Two earlier O(1) "defect matrices" were gate-rejected as convention
  artifacts — never interpreted.
- **Verdicts (relative to per-entry φ-scale):** (1) δ ≢ 0 at relative scale 1.017 — **the universal-τ
  does not persist at depth 2**; B357's identity is an order-1 rigidity, now sharply bounded.
  (2) **θ-graded bending**: F₄-target blocks saturate (0.99–1.00) while escape-sector targets are
  ~3× suppressed (0.33) — the depth-2 germ sees the E₆→F₄ fold. (3) Mixed symmetry (data).
- **W2.5 COMPLETE ⇒ the Gate-B classical germ is complete**: orders 1–3 integrable + Lagrangian +
  universal-τ (order 1) + the depth-2 τ-defect matrix with its θ-grading. +1 lock (leg B gates+verdicts).

## 2026-07-03 — THE PROMOTION AUDIT EXECUTED: 61 entries promoted (P17–P55, C6–C12, E1–E15); 6 held

**Protocol applied uniformly per candidate** (GOVERNANCE §5/§5.1/§6): FINDINGS re-read; the five
red-team questions answered; the test lock verified standalone (281 tests across five batches: 24 +
61 + 69 + 90 + 37); the independent-second-path leg checked; a scoped statement written; label
assigned by the bar, never importance (owner directive). Sweep provenance: four parallel strict
triage passes over frontier/B1–B369 (63 candidates of ~350 probes; 297 NOT with recorded reasons).

**Promoted: 39 proven (P17–P55), 7 conditional (C6–C12, each with its premise in the statement),
15 certified-data (E1–E15).** Scoping decisions of record: B112 promotes ONLY its Tier-1 lemma (its
own relabel warning governs); B90 promotes ONLY L1b (tautology + refuted mechanism excluded); B153
excludes the numerical non-semisimple leg; B134/B136 are corollaries of the published GHH-2008
criterion (cited) + exhaustive certificates; B204 cites the Jeffrey-1992 framework (novelty not
claimed); B65+B80 and B273+B274 each merge into ONE claim with two independent evidence paths;
B131 is scoped to its exact (1,2) fork; B211/B240 promote data with novelty explicitly not claimed.

**Held, with reasons: 6.** B63 (subsumed by P22's two-path claim); B196 (identities subsumed by E6;
placement NEEDS-SPECIALIST); B352/B353/B357/B370 (the dps-100 computer-assisted class — their own
FINDINGS describe evidence-not-proof; a future "exact-core extraction" pass is the named route).

The proven core P1–P16 is untouched; the physics firewall is untouched; every O-target remains
open; nothing physics-adjacent moved. The ledger now represents what the project knows, at the
strength it knows it. (New metric in force: promotions with zero unmarked retractions.)

## 2026-07-03 — B371: the minimal two-state sector — verified, banked, promoted (P56, P57)

- A relayed cross-session probe (pre-registered there before computation, with kill conditions and an
  honest errors ledger) answered the owner's "can we compute a photon?" with **NO at the physics level**
  and a well-posed slot question at the math level. **Independently re-verified here from scratch,
  every claim exact** (`slot_verification.py`): the 2-dim invariant sector, global dihedral relation,
  helicity pairing ±ζ₆₀⁹, pentagon-angle golden action (1−φ exactly), the true parity J = Ŝ²
  (monomial j→1−j, commutes exactly), the Weyl identity J·Par = ζ₆⁻¹·X·Z, and the seam self-coupling
  at ±1/48 on exactly {6,14}×{2,10}. The value stratification of the (1,2) table = the prime-3 parity
  split (rigid rows {0,4,6,14} + silent 16 = the trivial-at-3 tower).
- **Promoted at banking (§5.1 steady state): P56 (the sector), P57 (the parity + Weyl identities)** —
  exact, locked (4 tests), two independent computation paths. FIREWALL intact: a photon-shaped slot
  is not a photon; no physics noun earned.
- **Registered open (fresh pre-registration required): the row-16 silence** — no forcing law survives
  the exact data (three involutions killed); localized to the XZ block-diagonal on the 3-dim block;
  the selection-rule derivation of ±1/48 as the unique allowed sector↔sector XZ element is the target.

## 2026-07-03 — B372 (W2.7) DONE: the seam is a LEVEL-FAMILY phenomenon (null refuted); E16

- CRT/F_p engine (toolbox row 6), gate-anchored on the banked level-15 flagship (exact
  reproduction), 3 primes, held-out embeddings, zero identification failures.
- **Q1 (the wall): HOLDS, cleaner than at 15** — singles = four cells ≡ 1 mod 15, each exactly 1/4,
  purely rational. **Q2: the pre-registered null REFUTED** (the arc's 5th productive failure):
  **all 144 pair cells carry imaginary components; 144/144 carry √−15-type content; every cell has
  genuine ℚ(ζ₉)⁺ dependence** — the seam persists at 45 and its home GROWS to the 12-dim compositum.
  Denominators stay 15-smooth × 2-power (≤ 2880).
- E16 promoted at banking (the exact table; certified data). Follow-on lead registered: the value
  tower's growth with the level (the conductor structure of the seam). Task #161 completed.

## 2026-07-03 — B373 (PD1.1) the kill test: MOVED — gapless-trending; the relayed bet loses; E17

- **Exactly one invariant two-state sector at level 45: exponents {6,54}** — the exponent pinned at
  ±6 while ord grows (20 → 60), so the quasi-energy moved 108° → 36° (= 108/3) with
  `tr ρ(A₁) = φ` exactly (2cos 36°). Silver pinned at 60° (seed-dependent — data). Helicity and the
  global dihedral relation persist. The pre-registered MOVED outcome hit verbatim; the independent
  "pinned/anyon-shaped" bet is the refuted branch at this rung.
- **The tower door (PD2.2) is ALIVE**: phase ~ 9π/N → 0. Pre-registered for level 135 BEFORE
  computing: unique sector at ±6 of ord 180 (±12°, trace 2cos 12°), pairing + dihedral persist.
- E17 promoted at banking. The priced-doors campaign's first verdict: the mass-word's costume moves
  from "possibly anyon" to "lattice-artifact phase, gapless-trending" — still zero physics nouns earned.

## 2026-07-03 — B374 (rung 3): the pinned-exponent law REFUTED — the pentagon-pair oscillation

- Level 135: **the unique invariant sector is {54, 126} — phase ±108° again** (ord 180; dihedral
  global; cross-prime confirmed). B373's registered kill fired: the "gapless-trending, 9π/N" reading
  is dead at rung three (the sixth productive failure). The exact three-rung law: phase pinned to the
  pentagon pair {36°, 108°}, alternating with the 3-adic parity of N = 15·3^k; traces alternate
  1−φ / φ / 1−φ. The mass-word reading returns to anyon-shaped on this tower; the gapless hinge is
  CLOSED along 15·3^k as measured.
- **E17's extrapolation clause corrected in place** (marked, logged; the level-45 data stands).
- Pre-registered before computation: level 75 (5-tower) — pentagon-pair membership (weak form);
  level 405 — alternation continues (36°). B373's FINDINGS carries the refutation cross-reference.

## 2026-07-03 — the 75-rung (5-tower): the pentagon-pair prediction also killed — phase 90°, trace 0

- Unique sector {25, 75} of ord 100: **±90°, golden trace exactly 0** (quarter-turn). Seventh
  productive failure. Four exact rungs: phases 108/36/108/90; a/N = 2/5, 2/15, 2/5, 1/3; ord = 4N/3
  uniform. **The surviving law: existence + uniqueness of the invariant two-state sector at every
  level tested (two tower directions), with helicity and ord = 4N/3.** The phase-map riddle
  registered (3-part/5-part arithmetic of N); next datum N = 225, NO phase prediction registered.

## 2026-07-03 — B375 (PD1.3): the four-qubit compilation + the exact protocol theorem (P58)

- The algebra generated by TWO primitives (exact diagonal + exactly-unitary DFT ⊕ 1); WR̂ from the
  primitives equals the banked generator as an identity; the 240-word Hadamard-test protocol with the
  declared weights reproduces the banked seam cells EXACTLY (flagship + the minimal-sector's ±1/48).
  The κ-word's Weil trace is exactly 1. P58 promoted at banking (exact + locked).
- The κ-letter deliverable's in-sandbox half is complete: ±1/48 as an instrument reading, in exact
  arithmetic. Hardware = owner decision (out of campaign scope); feasibility honestly estimated in
  CIRCUIT.md (~10⁶ shots/word to resolve 1/48; synthesis depth = the engineering question). The
  letter/spirit firewall stated and governing.

## 2026-07-03 — N=225: NO invariant sector — the existence law dies at the first mixed level

- ord = 300 = 4N/3 ✓; sixteen mult-1 pairs; **zero invariant** (cross-prime). Eighth registered
  kill. Five-rung law in m = N/15: sectors at prime-power m (1, 3, 5, 9), none at m = 15 = 3·5.
  **The minimal sector lives on prime-power towers only.** Refined preregs committed: 405 exists
  (36°), 375 exists, 675 none. The tower/continuum reading must survive sector-death at mixed levels.

## 2026-07-03 — the Recognition campaign registered (PR #466) + R1 first pass: the classics miss

- Phase 0 delivered: the Constraint Document (C-1…C-12) — every exact fact a candidate generating
  theory must reproduce. Four recognition sweeps pre-registered with kills.
- R1 first pass: **Rademacher Φ(A_m) ≡ 3 across the metallic family** (new exact datum; constant ⇒
  killed as the phase generator); Dedekind s(1,m) killed by the affine criterion. The level-indexed
  zoo (Weil/Maslov index of the A₁-action at level N; η-quotient multipliers) is the registered
  continuation.

## 2026-07-03 — B376 (R1): RECOGNITION HIT — the tower is the quantized golden cat map (P59)

- **π(N)/2 = ord(A₁ mod N) = the measured Weil order at ALL FIVE levels** including the sector-less
  225. "ord = 4N/3" was coincidental; the Pisano identity is structural. Predictions registered:
  500/540/900 at N = 375/405/675.
- The frame (Hannay–Berry; Kurlberg–Rudnick Hecke theory) is KNOWN mathematics — cited, not claimed.
  What it buys: the phase-map riddle → cat-map doublet eigenvalues; the prime-power existence law →
  ℤ[φ]-splitting arithmetic (5 ramifies, 3 inert) with the R2 obstruction as character misalignment;
  **Phase 2's derive-don't-fit target fixed**: derive the existence law, a(N), and ultimately the
  C-5 seam tables from cat-map Hecke theory — breakthrough if it derives, sharpest boundary if not.

## 2026-07-03 — B377 (D0+D1): the existence law DERIVED; the 225 prediction HIT; three rung
## predictions registered (one REVERSED by our own 27-census)

- **D0:** the full-multiplicity census at 225 = NONE — the prediction registered while it ran, HIT.
- **The complete local table** (3,5,9,25,27,81,125 exact): doublets at ODD prime powers only
  (3-side 90°; ramified 5-side 36/108 by σ-class); lines always on the inert side, EVEN powers only
  on the ramified side. Tensor factorization verified with corrected multipliers ((2,2) at 15 —
  the relayed note's values were a parametrization offset, caught by our failed-then-fixed check).
- **The v2 law derives all six banked verdicts** incl. 75's 90° and the 225 death. Acceptance
  predictions registered BEFORE the rungs: **375 → 108°** (the 90° branch died with the missing
  125-line), **405 → 36°**, **675 → EXISTS at 90°** (REVERSING the naive "none" — the odd-power
  27-doublet flips it). Law promotion GATED on all three.
- Governance note of record: campaign and labor decided HERE; the relayed material entered as
  substance only, verified and corrected before any use.

## 2026-07-03 — B379 (D3(b) opener): the reduction theorem + closed form VERIFIED; P60; the
## W2.11 gap is now ONE number + ONE reality proof

- The relayed selection-rule hunt (owner-directed; pre-registered there before computation)
  verified item-by-item here: **T1 the reduction theorem, 13/13 cells component-exact** (both
  seats' first checkers independently hit and fixed the same real-subfield trap — cross-validating
  the machinery); **T2 the closed form exact**: the rigid sector = one constant with two Galois
  faces (−(φ/6)√−3 and its σ_√5 conjugate), so ±1/48 = ±(1/4)·(1/12); the Weyl form holds with J
  verified scalar on both blocks. The support pattern is now DERIVED. Their H2/H3 kills recorded.
- **Row 16 is ℚ(√5)-dark** (banked-data-exact; σ₄₉ pairs rows 4↔16). The remaining W2.11 gap:
  (1) derive the 1/12; (2) prove t(16,·) ∈ ℚ(√5). P60 promoted at banking.

## 2026-07-03 — the seam form's exact Gram spectrum: the doublet is a theorem; the prime 23 appears

- Relayed SVD observations verified by exact char poly: Gram spectrum = {1/576, 1/576, 1/768,
  23/19200} exactly (all rational; perfect-square discriminant; trace = the banked 43/7200).
  **1/576 = 1/24² is a double root** — the two strongest observables (escape vs the non-exponent
  {2,10} columns) are exactly degenerate at the Haar strength 1/24 = 1/|2T|. **23 is the first
  prime outside {2,3,5} in the program's exact values** — flagged, not interpreted. The relayed
  reciprocal-ratio claim did not reproduce as stated (returned for specification). C-5 constraints
  sharpened for D3(c); lock added.

## 2026-07-03/04 — B380: the Galois covariance laws verified (P61); the F₄ reciprocal duality
## confirmed after a wrong-object correction on the verifying side

- The relayed pre-registered census verified cell-exactly: **σ₃₁ is a proven symmetry of all six
  tables** (odd rows of (1,2) pair up — half redundant); **the mirror is conjugation**
  (t(a,−b) = τ₃(t(a,b)), full-vector — mirror-column reality now derived); the τ₃-relabel laws
  exact on four tables + the tower domain measured exactly (36 odd fails); √5-flippers fail
  everywhere (the P60 conjugacy is trace-level only); **(2,3) is stabilized by the entire
  √5-fixing half-group** (all 8 — verified).
- The earlier "returned" reciprocal-ratio claim: VERIFIED once the right object was specified
  (K2-columns 1,5): ratios {−4,−1/4}∪{−3/2,−2/3} reciprocal pairs; equal-norm F₄ Gram
  (49/115200; ⟨v₁,v₅⟩ = −13/57600) — reconciled with the banked canonical spectrum.
- Intake recorded (hints): 1/48 = Haar(2T×ℤ/2) = B₂/8; the McKay node map; the dilog-bridge
  negative. Residues ranked in FINDINGS (row-16 reality still the stubborn one). P61 promoted.

## 2026-07-04 — B381 (D2 COMPLETE): the seam is a twist invariant (P62)

- No intertwiner in the exhaustive natural family: the theta and canonical lifts are genuinely
  inequivalent — the half-characteristic twist (cocycle ζ₁₅^{−j(j+1)/2}, exhibited) is structure.
- The mechanism is a commutant fact: Par central in the canonical model (the B358 null = a
  corollary); Par−J = the Weyl step in the theta model. **seam ≠ 0 ⟺ the twist is carried.**
- The chain now closes: premise ⇒ twist forced (C6) ⇒ seam exists (P62) ⇒ support forced (P60)
  ⇒ symmetries forced (P61); the rigid sector's one remaining freedom = the 1/12. D2 ✅.

## 2026-07-04 — B382 leg 1: the phase-ratio law verified on its exact classical domain

- `tr(U·XᵃZᵇ) = tr(U)·ζ₁₅^{Q(a,b)}` with Q quadratic — exact on all 225 shifts for every sampled
  word with det(γ−I) invertible; the two non-invertible words fail as pure phases — **the domain
  boundary confirms itself**. The D-side intertwining is phase-free (DXD⁻¹ = XZ). Universal
  linear part (7a+8b) — the shift's own fingerprint. Legs 2–3 (ordering correction + the slot
  constant in closed form) named and pending.

## 2026-07-04 — B382 leg 2: the closed form; the twist IS the half-characteristic term

- tr(U·XᵃZᵇ) = tr(U)·ζ₁₅^{½ω(v,(γ−I)⁻¹v) − ½ab − ½ω(v,(1,1))} — all conventions pinned by the
  ten-face Cayley fit (α=2⁻¹, s=−2⁻¹). Registered cross-check PASSED: the canonical model gives
  the SAME quadratic+ordering with linear part (0,0) — the theta twist enters the trace formula
  as exactly one term, the half-characteristic −½ω(v,(1,1)) at the Weyl point. Leg 3: assemble
  the slot constant as the (1,1)-shifted DFT (o₁o₂=240 in view).

## 2026-07-04 — B382 leg 3: the assembly exact; THE 1/12 DECOMPOSES AS 1/16 + 1/48

- Gate A: 142/142 domain cells of the Par-table equal ζ₆⁻¹·χ·ζ₁₅^Q — the whole table IS the
  trace formula on its domain. Gate B: the slot constant reassembles exactly to (0,0,−1/12,−1/12).
- THE READING: det-class split = generic −1/16 + 5-boundary −1/48 (classes 3, 15 silent) — the
  1/12 is the Hannay–Berry generic sum plus one-third more from the golden-ramified cells.
  Mechanical-240 REFUTED as mechanism; Haar/B₂ remain numerological faces. Residue: derive
  −1/16, −1/48 from |tr|² = 15/|det| per class. Bonus: the banked 3-block face's grading
  identified as ±(P₄−P₀)⊗±(Q₈−Q₄); new exact face value ±1/24 for (P₄−P₁₆)⊗(Q₄−Q₈).

## 2026-07-04 — B383: the row-16 reality THEOREM (proved) + the ζ₅-spectrum mechanism

- t(16,b) ∈ ℚ(√5) for ALL b — finite exact verification (T1); the darkness is a zero of the
  anti-table's ζ₅-spectrum at exactly the 16-exponent (T2), distinguishing 16-dark from
  4-bright by character exponent alone (T3; new exact row-4 values banked). The P60 residue
  is closed: row-16 silence = reality theorem + mirror law.

## 2026-07-04 — B382 leg 4: the magnitude law |χ|² = #Fix(γ′) — unit on generic cells

- All 240 cells: |χ|² = the fixed-point count (1/9/5/25/45 by class) — the twist is pure
  phase; the −1/16 is a pure phase-sum identity (84 unit terms). Residue named: its CRT
  ζ₃×ζ₅ closed form. Per-cell class partials banked; they recombine to −1/16 / −1/48 exactly.

## 2026-07-04 — THE ACCEPTANCE DUEL: 3/3 — the v2 existence law PROMOTED (P63); D1 CLOSED

- 375: 108°/ord 500 ✓✓✓ · 405: 36°/ord 540 ✓✓✓ · 675: exists 90°/ord 900 ✓✓✓ — nine registered
  sub-verdicts, all correct, three phases distinguished by QR class. Root cause of the 405
  stall found and fixed (primes lacked ζ₈₁ — silent floor-division corruption; now ≡1 mod
  40500 + order cap). PROMOTIONS: P63 (v2 law), P64 (B382 trace formula + 1/16+1/48), P65
  (B383 row-16 theorem). B384 T1 landed: ⟨4₁⟩_N is NOT rational at general N — exact Galois
  components extracted; the √5-part is NONZERO at every 5|N level (2 at N=5; 2023/4 at 15;
  13100 at 25; 71150671/4 at 45; ~1.3e20 at 135): registered bet (b) PASSES — golden content
  in the Kashaev ladder at our levels. Scaling gate consistent (2π·log/N decreasing 4.93→2.36).

## 2026-07-04 — B384 T2: the tower transports the m=1 seed constant EXACTLY (1/4, identity)

- Coset 1 + (ord/4)ℤ at both 15 and 45, same value (1/4) — first exact cross-level constant
  equality (the level-45 companion step). m=2: same ord-12 grid + denominator family, extra
  basis components at 45 — relabel law OPEN. T3 (the (S,T) seam block) next; then D5.

## 2026-07-04 — B384 T3 + D5: the campaign wrap — D0–D5 COMPLETE

- T3: the slot's S-compression is TRIANGULAR (F(6,14)=0 exact) — NO-MATCH to 2-anyon/U(1)_k
  blocks at sector level; g(15) = √−15 (the seam radical normalizes S); twist diagonal
  h=(3/10,7/10); tr(F|slot) = −(5/16φ)(3−√−3). D5 synthesis written into RECOGNITION.md
  (6 derived, 5 resisted, residue queue priced); PRICED_DOORS PD1.2/PD3.1 rows updated.
  The Derivation Campaign's registered program is COMPLETE.

## 2026-07-04 — B385 T1: double kill — the bright/dark discriminator is character-level

- Kill 1: no γ-group invariant separates (bright (2,3) ≡ dark (1,3) profiles). Kill 2: the
  word-grid det-class distribution fails on exactly the riddle pair ((3,4) ≡ (1,3):
  {63,21,27,9}/120). DERIVED continuation: D·C⁻¹ = Z^{−8} exactly — theta words = standard
  lift × T(v_word); the discriminator must live in the accumulated word-shift map's 5-part.

## 2026-07-04 — B385 T2-partial: the v_word map separates the riddle pair (first layer that does)

- W-word = U_std(γ′)·T(v_word)·phase derived and sanity-locked; the 5-part support sets are
  disjoint bright-vs-dark; (3,4): 12 vectors vs (1,3): 18. Criterion extraction = next
  (property scan registered in FINDINGS).

## 2026-07-04 — B385 T2b: darkness is SPECTRUM-cancellation (dark (1,3) has 44/120 anti cells,
same as bright (3,4)) — the P65 mechanism at pair scale; 3 scan nulls; 4 bright-exclusive
joint labels on the riddle. Criterion open, true form named (window-cancellation identity).

## 2026-07-04 — B385 correction: the criterion draft KILLED by its own 12/12 test

- Two self-caught errors: the banked split is s-only (my T2b counts were z∨s — data true,
  reading corrected in place); and the Π_H/DFT commutation fallacy voided the translation-kill
  logic (third appearance of the trap this session). Continuation reframed: field-level
  quasi-periods C[j+dj,l+dl] = ζ₆₀^r·C[j,l], which commute with the DFT.

## 2026-07-04 — B385 T3 + staging: quasi-period ladders found ((1,5)/(4,5): 9 elements,
r = 36k twists, forcing support 6); presence doesn't separate. The criterion arc STAGED with
the honest ledger (one data-level separator, five nulls, one voided draft). Next: the CRT
closed form of −1/16 (P64 residue).
