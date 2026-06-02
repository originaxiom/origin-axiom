# Changelog

All notable changes to the Origin Axiom repository are recorded here.
Format follows [Keep a Changelog](https://keepachangelog.com/); this project is pre-1.0 and
not yet versioned for release. Detailed working history lives in `PROGRESS_LOG.md`.

---

## [Unreleased]

### Added
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

### Changed
- Project framing locked to the disciplined V4 / Reality-Check line; the optimistic
  `handoff.md` framing demoted to historical record.

### Notes
- This repository consolidates four prior GitHub repositories and the May-2026 session
  archive into a single canonical home.
- The four prior repositories (`origin-axiom-framework`, `origin-axiom-theta-star`,
  `origin-axiom-obstruction`, `00_origin-axiom`) have been archived read-only with
  "superseded by" pointers. They are preserved, not deleted.
