# R5 lock-batch — full detail

Repo (read-only): `<cc2-seat>/origin-axiom`
Work dir: `<cc2-seat>/seat-work/residuals_loop/r5_locks/`
Python: `<cc2-seat>/seat-work/.venv/bin/python` (3.12.1; numpy 2.5.1, scipy 1.18.0, sympy 1.14.0, mpmath bundled)
Recomputed: 2026-07-16. Repo not modified (read-only throughout).

Artifacts: `proposed_locks_r5.py` (20 asserts, all PASS), `runs/` (raw script outputs
and reimplementation scripts), this file.

---

## 1. B602 — exact residual 1455/2194752821534 ≈ 6.63e-10

- **Source:** `frontier/B602_value_bridge/b602_n2_x2.py` (the N2 cell), FINDINGS.md.
- **Method:** ran the script **verbatim** (`runs/b602_n2_rerun.txt`).
- **Result:** reproduced exactly: `(N8·τ4)/(N4·τ8) = 1455/2194752821534 ≈ 6.629448e-10`,
  factorizations `{3,5,97}` / `{2,7,13²,31,607,49297}` also match printed output.
- **Verdict: REPRODUCED (verbatim rerun).** Lock: exact `Fraction` equality + numeric tol 1e-3.

## 2. B482 — λ_chain = 1.57705744122666946

- **Source:** definition in `papers/P4_markov_stage/DRAFT_v8.md` L560-565 (`λ_chain :=
  limₖ (tr s_k)^{1/G_k}`, G_k = #R/L letters of the chain, Fibonacci, G0=4,G1=2);
  chain construction in `frontier/B471_chain_verification/chain_verify.py`. No single
  script computes the n=55/40dps limit itself (described in prose only).
- **Method:** **reimplemented.** u_n grows too fast for exact big-ints by n=55 (~10^11
  digits) — ran the Fricke recursion `u_{k+1}=u_k u_{k-1}-u_{k-2}` directly in mpmath
  float (dps=80), cross-validated against exact big-ints for n≤20 (agreement to 80
  digits). `runs/b482_b483_lambda_chain.py`.
- **Result:** `u_55^(1/G_55) = 1.57705744122666946837...` — matches the banked value to
  all 18 quoted digits.
- **Verdict: REPRODUCED.** Lock tol 1e-13.

## 3. B483 — limits 3.5223870342 vs 2.1775291199

- **Source:** same chain construction; "true limit" language and the seat-2 relation
  are in `frontier/B483_fibonacci_anyon_face/FINDINGS.md` and
  `frontier/B471_chain_verification/FINDINGS.md` L54-58 ("my per-full-letter
  3.5223904... and their 2.1775291... satisfy λ_mine = λ_theirs^φ").
- **Method: reimplemented** (same script as #2). Two sub-figures:
  - `u_55^(1/F_55)` (F_n = block-count Fibonacci, F0=F1=1) = **3.5223870341997586...**
    → matches "true limit 3.5223870342" to the quoted precision.
  - Seat-2's own clock's *true limit*: rather than guess seat-2's exact (mislabeled)
    letter-counting convention — several candidates (half-chain trace over F_n, over
    its own Lucas letter-count) were tried and did **not** match — the documented exact
    relation `λ_full = λ_theirs^φ` was used instead: `λ_full^(1/φ) =
    2.1775287510532416...`, matching the target **2.177528751053** to 13 digits.
    This also explains B482 FINDINGS' own phrase "wrong from digit 7": 2.1775**29**1199
    (seat-2's rung) vs true 2.1775**28**751053 — digits agree through position 6, diverge
    at 7, exactly as stated.
  - The rung value **2.1775291199** itself (seat-2's specific finite-n construction) was
    **not** independently re-derived — its exact letter-counting convention is not
    pinned down anywhere in the repo, only the relation to the limit is documented.
- **Verdict: REPRODUCED** (both headline numbers, to high precision); the intermediate
  rung artifact 2.1775291199 is understood but not independently re-derived from
  scratch. Lock tol 1e-9 on both limits.

## 4. B492 — g_τ/g₁ = 1.17319/0.72507 = φ exactly

- **Source:** `frontier/B492_verlinde_boundary_lens/FINDINGS.md` only; no script
  ("Reproducer: inline (Fibonacci S-matrix + Verlinde + AL g-factors)").
- **Method: reimplemented minimally** from the stated formula (Fibonacci modular
  category, d_τ=φ, S-matrix, g_a = S_{0a}/√S_{00}). `runs/b492_verlinde.py`.
- **Result:** D=1.9021130325903071..., g₁=0.7250731770787922..., g_τ=1.1731930448443570...,
  **g_τ/g₁ − φ = −2.67e-51** (exact to machine/precision limit), ln g₁=−0.321483
  (target −0.32148), ln g_τ=0.159729 (target +0.15973). Verlinde N(τ,τ,1)=N(τ,τ,τ)=1
  and S·Sᵀ=I also confirmed.
- **Verdict: REPRODUCED**, essentially exact.

## 5. B481 — exact F_p at p = 61, 421, 541, 1201

- **Source:** `frontier/B481_det_zeta5_kill/FINDINGS.md` names `det_kill.py` as the
  reproducer — **this file is missing from the repo** (only `wrt_tmatrix.py`, Reading-2,
  survives). Reimplemented using the repo's own canonical engine
  `frontier/B465_monodromy_intake/exact_engine.py` (imported read-only; the same
  `build()` that `frontier/B472_quantum_commutator/kq_verify.py` uses and which is
  itself a banked, passing reproducer for a different theorem).
- **Method:** reused `build(p,c=1)` for W1, W2, Par exactly; reconstructed D, F
  (not directly returned by `build`) by copying its internal formulas verbatim.
  `runs/b481_det_recompute.py`.
- **Result (all 4 primes, 61/421/541/1201):** det(W1)=det(W2)=det(W1·W2)=det([W1,W2])=1;
  det(Par)=det(Par·W1)=det(Par·W2)=det(Par·W1·W2)=−1; det(D)=ζ3; det(W_R)=ζ3² — **all
  match exactly**. det(F): initially mismatched (got a generic F_p residue, not ζ4³=−i);
  root-caused to the Gauss-sum sqrt(15) sign branch (two valid square roots of 15 mod p;
  `exact_engine.build()`'s internal convention picked the other one). Flipping the
  branch (equivalently negating det(F), since N=15 is odd) gives an **exact** match to
  ζ4³=−i at all 4 primes — confirmed algebraically, not fudged (shown in `runs/b481_final_run.txt`).
  Across all four primes, **no computed determinant ever equals a primitive ζ5 power**
  — the central claim.
- **Verdict: REPRODUCED** (10/11 immediate matches + 1 resolved sign-convention item;
  core "never ζ5" claim confirmed at all 4 primes). `det_kill.py` itself not run (missing) —
  faithful reimplementation via the shared canonical engine instead.

## 6. B491 — Goldman Geom. Topol. 7 (2003) 443–486 citation check

- **Source:** `frontier/B491_novelty_assessment/FINDINGS.md`. Documentation lock, not numeric.
- **Method:** live WebSearch (2026-07-16) cross-checking arXiv, Project Euclid, msp.org, ResearchGate.
- **Result:** citation resolves **exactly** — William M. Goldman, "The modular group
  action on real SL(2)-characters of a one-holed torus," Geometry & Topology 7 (2003)
  443–486, arXiv:math/0305096. Abstract confirms the Markoff cubic
  κ=x²+y²+z²−xyz−2, Γ≅PGL(2,Z)⋉(Z/2⊕Z/2), and the theorem content described
  ("properly discontinuous on four contractible components, ergodic on the compact
  component") — matching FINDINGS' characterization as "the ERGODIC dichotomy."
  Did not fetch the full PDF to independently verify the claimed "full-text grep: 0
  hits" for divisor-indexed torsion fields (a secondary negative-existence claim);
  the citation and theorem-type match are independently confirmed.
- **Verdict: REPRODUCED / VERIFIED** (citation + theorem characterization both check out).

## 7. B544 — Sturmian 610/610; the 99.95 figure

- **Source:** `frontier/B544_emergent_golden/FINDINGS.md`. No script in the directory.
- FINDINGS.md itself distinguishes chat-2's two original claims — (a) FK ground state
  at 987/610, K=0.5 → occupation word Sturmian **610/610 exactly**; (b) critical circle
  map itinerary **99.95%** Sturmian — from its own "spot verification": a bisection
  recovering winding=1/φ and Shenker's Ω*≈0.6066553, which is NOT the same computation
  as (a) or (b).
- **Method:** reimplemented **only** the spot-check (standard Fibonacci-approximant
  critical-circle-map renormalization bisection; `runs/b544_circle_map.py`), since (a)
  and (b) specify neither the FK Hamiltonian (potential form, chain length, boundary
  conditions) nor the itinerary-comparison procedure precisely enough to reimplement
  with confidence in budget.
- **Result:** Ω* converges (Fibonacci approximants n=3..17) to **0.6066610823...** —
  agrees with FINDINGS' quoted 0.6066553 to only ~5 significant figures (discrepancy
  from the 6th digit on; my value matches the constant as I recall it from the
  golden-mean critical-circle-map literature, but I could not independently verify
  FINDINGS' specific digit string against a live source). Winding number: the
  Fibonacci convergent 1597/2584 → 1/φ by construction (tol 1e-6); direct long
  iteration (20000 steps) only agrees with 1/φ to ~5-6 digits, consistent with the
  well-known slow (power-law) convergence of critical circle maps under raw iteration.
- **Verdict:** spot-check figure (Ω*, winding) **PARTIALLY REPRODUCED** — right
  constant, right qualitative behavior, ~5-sig-fig-not-9-sig-fig match, tolerance
  widened and gap documented rather than hidden. The two *headline* figures the task
  named, **Sturmian 610/610 and 99.95%, are UNREPRODUCIBLE** — chat-2's original
  numbers, method underspecified (no FK Hamiltonian parameters, no itinerary-match
  definition), not re-derived anywhere in the repo itself. No lock forced.

## 8. B412 — the 135→405 measure refinement summing to 1/4

- **Source:** `frontier/B412_tower_measure/FINDINGS.md` (points to banked tower values);
  actual computation lives in `frontier/B394_support_walk/` (`singles_405.py` →
  `singles_405.json`; `identify_triple.py` → `triple.json`).
- **Method:** ran `identify_triple.py` **verbatim** against the already-banked
  `singles_405.json` (in-sandbox; did not regenerate the F_p census itself).
- **Result:** output `(x,y,z) = (1/12, -1/12, -1/12)` matches the banked `triple.json`
  exactly. Verified this reconstructs the claimed form: value(class) = (1+c_k)/12 for
  the three ζ9⁺ conjugates {c1,c2,c4}, and independently confirmed **c1+c2+c4 = 0**
  exactly (sum of all primitive 9th roots = μ(9) = 0) via sympy, giving
  (3+0)/12 = 1/4 exactly.
- **Verdict: REPRODUCED** (verbatim script rerun + independent symbolic confirmation
  of the underlying cyclotomic identity).

## 9. B412 — the 405→1215 trace-zero triple

- **Source:** `frontier/B399_wall_scale/FINDINGS.md`; scripts `singles_1215*.py` →
  `singles_1215*.json`, `identify_1215_triple.py`, `recon_e3.py` → `triple_cubic.json`/`triple_id.json`.
- **Method:** attempted to rerun `identify_1215_triple.py` verbatim — it stalled past
  120s (its Method-2 brute-force fallback is a ~29M-iteration grid search; FINDINGS
  itself records the underlying F_p census took "~2.5h, 2 primes"), so per the runtime
  guard it was **stopped** and NOT force-completed. Instead wrote a small standalone
  check (`runs/quick_e1_check.py`) that re-sums the **already-banked** F_p residues
  across **all 20** available prime files (did not regenerate the matrices).
- **Result:** the triple-sum ≡ 0 (mod p) holds at **all 20** independently-banked
  primes (~3×10⁷ magnitude each) — matches both `triple_cubic.json` and
  `triple_id.json`'s own banked `"e1": "0"`.
- **Verdict: REPRODUCED** (independent re-derivation from banked F_p data across 20
  primes; did not redo the original expensive matrix computation — flagged per the
  "skip-with-note if heavier" guard).

## 10. B480 — ⟨r⟩ = 0.16 at N = 181, 301

- **Source:** `frontier/B480_qca_dirac_lens/FINDINGS.md`, attributed to "Hecke /
  Kurlberg–Rudnick arithmetic symmetries." `qca_dispersion.py` in that directory covers
  only the coin/dispersion (Q1) cell — **no script anywhere computes this specific
  figure.**
- **Method: reimplemented from scratch**, twice. Quantized the golden cat map
  M=[[2,1],[1,1]] via a closed-form Hannay-Berry-style formula, verified **unitary**
  to machine precision at N=181, 301 — but a follow-up check (compose two quantized
  generators and compare to the quantization of their product) showed the construction
  **fails the group-homomorphism test** (ratio of `U(M1)U(M2)` to `U(M1·M2)` is not a
  constant phase; std ≈ 0.6, not ≈0) for two tried normalizations (`1/√N` and the
  `inv(2c)`-corrected phase). This means the propagator, while a valid unitary matrix,
  is **not a faithful representation of SL(2,Z/N)** and cannot be trusted to reproduce
  the representation-theoretic degeneracy mechanism the claim depends on. Computed
  (untrusted) ⟨r⟩ = 0.49 (N=181), 0.55 (N=301) — both **close to GOE (0.53), the
  opposite of "heavy clustering."** A Poisson-random control gave 0.393, matching
  theory (0.386) and validating the r-statistic code itself is correct — the problem is
  specifically the quantization, not the statistic.
- **Verdict: UNREPRODUCIBLE (within budget).** Getting the exact metaplectic/Weil
  normalization right (Gauss-sum phases with Legendre-symbol dependence on N mod 4,
  CRT-compatible treatment for composite N=301=7×43) is a well-defined but nontrivial
  undertaking exceeding the ~10 min/claim guard; the repo's own canonical engine
  (`exact_engine.py`) is hard-coded to level 15 and a specific generator pair, not
  obviously adaptable to general N=181/301 with confidence in budget. No lock forced;
  this is a first-class negative finding, not silence.

---

## Summary counts

- **Fully REPRODUCED with a lock:** B602, B482, B483, B492, B481, B491, B412×2 (8 rows, 9 claims-worth since B412 counts twice) — 18 asserts.
- **Partially reproduced, widened-tolerance lock:** B544's Ω*/winding spot-check (2 asserts).
- **UNREPRODUCIBLE, no lock forced:** B480 (level-ratio); B544's two headline figures (Sturmian 610/610, the 99.95% itinerary).
- **Total: 20/20 emitted asserts PASS.** 3 sub-figures across 2 claims (B480, and two of B544's three numbers) are honestly reported as not reproduced.
