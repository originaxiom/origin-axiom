# B1306 — THE OLDER DEBT, SLICE C: the never-read physics items of four seats — cc3's ρ rebuilt, geodir h¹, the positivity bridge and the cusped one-loop gap; the physics seat's exact e₈ rounds R64–R67; the codex seat's listener-identification finding R033; the hostile-review seat's six certified memos 16–21 — DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 row B1306 (slice C); Review 56's R56-1 payment order (b): the never-read physics
items first. · **Seats pinned (unchanged, the seats have not moved):** cc3 `paper/structure-genesis-first` @ `a31456d2`; fc @ `659487bb`; codex @ `f7a49536`;
the hostile-review branch @ `6fc86147` (golden_gate). · **Read in full before this seal:** the four cc3 FINDINGS (B8081, B8082, B8083, B8102), fc R64–R67, the
codex R033 memo and its output, the hostile memos 16–21 and the MANIFEST rows 16–21; every certificate script's docstring. · **Re-runs** of all seventeen
certificates launched in the pinned worktrees before this seal (receipts `verification/sliceC/*_rerun.txt`); main's own code runs only after it.

## 0. The rule lines

`already_banked.py` at B1306 A's inventories covers these items (rows ABSENT/CITED); the specific checks: "positive words conjugate iff cyclic rotation"
→ no settled arc; "SU(3) level 2 modular data group order 2880" → the paper's own Prop (2880), cc3's B8081; "h¹ principal sl₂ exponents six" → B1297's
d2lib computes twisted h¹ (main's engine); "Kac class order-3 A₂³ D₄×T² 40 45" → B1264 (main's 85 colourings; the split is fc's). Receipt:
`verification/sliceC/already_banked_at_seal.txt`.

## 1. The view from above

These are the items every earlier sweep marked ABSENT on main: results other seats proved and main never read. Three of cc3's four carry scripts and bear on
the paper's own load-bearing statements (a representation the paper cited but never built; a dimension count it admitted it did not compute; a bridge its
arithmeticity proof needed). The physics seat's four rounds settle the one object-specific step of the E₈ family mechanism at the level of Lie-algebra
classes. The codex finding says B1231's identification ledger is a seed, not a census, and names the unpriced listener map — an omission of main's own. The
hostile seat's six memos are the "beat" trilogy (the object's antilinear element and its descent to e₆ and the 27), the S₄ torsor at E₈, a typed negative on
spin, and the unit dictionary for geodesic lengths. None of these decides the chirality bit; each is a verified piece of the structure the bit would have to
live in, and rule 1 says every one gets read, re-run and — where main's machinery reaches — re-derived. **If the slice fails:** a seat result that does not
reproduce on main is the finding (VERIFIED-DIFFERS), recorded in both places.

## 2. The questions (each: re-run in the pinned worktree; then main's own code where named; PASS/FAIL; prior)

| # | item | the seat's verdict (verbatim) | main's own re-derivation (`verification/sliceC/`) | PASS | prior |
|---|---|---|---|---|---|
| C1 | cc3 B8081 ρ rebuilt | "It is built here, from the Kac–Peterson data alone" (SU(3)₂: six weights, c = 16/5; Prop (2880)) | `c_su3_level2.py`: own S and T from the Kac–Peterson formula, the group ⟨S, T⟩ generated numerically at 60 digits with exact hashing; its order and the decomposition B8081 reports | order and decomposition equal B8081's | 0.85 |
| C2 | cc3 B8082 geodir h¹ | "PROVED for the H¹ count; the unobstructedness is registered as owed" (𝔢₆ under the principal 𝔰𝔩₂ by exponent; h¹ = 6) | `c_geodir_h1.py`: B1297's `d2lib` on m004's geometric ρ: h¹(m004; Sym^{2e}ρ) for e ∈ {1, 4, 5, 7, 8, 11} (the E₆ exponents), summed | each summand as B8082 states and the total 6; the "owed" half stays owed | 0.85 |
| C3 | cc3 B8083 positivity bridge | "two positive words in R, L are conjugate in SL(2,ℤ) iff they are cyclic rotations of one another" (exhaustive to length 10) | `c_positivity_bridge.py`: own complete invariant — the Gauss reduction cycle of the fixed-point binary quadratic form — computed for every positive word of length ≤ 9 (2 ≤ … ), compared with cyclic-rotation classes; both directions | the two equivalence relations coincide on every pair through length 9 | 0.85 |
| C4 | cc3 B8102 cusped one-loop gap | "a literature position, each claim cited" (arXiv:2507.05364 is cusp-free by its abstract; the cusped determinants exist in the mathematics) | none possible (a reading); REGISTERED with the two citations checked against the papers' abstracts | — | — |
| C5 | fc R64 | "the object's order-3 element is the family rotation TIMES an E₆ Weyl element" (types: L_g fixed dim 0; w_{A₂} fixed dim 6, fixes all 72 E₆ roots) | `c_e8_types.py` on B1275's own E₈ roots: the Weyl rotation of an A₂ plane has fixed dimension 6 and fixes the 72 roots of its centraliser E₆; the L_g half needs the icosian model and is the seat's (re-run only) | the w_{A₂} half reproduces; L_g REGISTERED from the re-run | 0.9 |
| C6 | fc R65 | "40 of B1264's 85 trinification gradings are trinification elements and 45 are not" (A₂³, dim 24 / D₄ × T², dim 30) | `c_kac_classes.py` on B351's own e₆ roots and B1264's 170 labellings: dim of the fixed subalgebra of exp(2πi h_c/3) = 6 + #{α : α(h_c) ≡ 0 mod 3} → the class split | 80 labellings at 24 and 90 at 30, no other value; 40/45 colourings | 0.85 |
| C7 | fc R66 | "w₃'s Tits lift in the exact e₆ is of order 3 with Ad-multiplicities (24, 27, 27)" (word of length 24) | `c_tits_lift.py`: the seat's word on B351's `exact_e6.py` brackets; nᵢ = exp(ad eᵢ)exp(ad e₋ᵢ)exp(ad eᵢ) as exact 78 × 78 matrices; the product's order and its eigenvalue multiplicities | order 3; multiplicities (24, 27, 27) | 0.8 |
| C8 | fc R67 | "L_g, w_{A₂}, w₃ lift to order-3 elements of E₈ in the SU(9), E₇×U(1) and E₆×SU(3) classes" | main has no exact e₈ bracket table; re-run only, REGISTERED with the seat's receipt | — | — |
| C9 | codex R033 | "B1231 admits an unpriced listener identification absent from its ledger … registering that admitted debt gives 3 UNEARNED > baseline 2" | none needed (a scope finding about main's own ledger, its output re-run): register **I-29 the listener map u** as UNEARNED in `docs/IDENTIFICATION_LEDGER.md` with a dated, deliberate baseline migration (the ratchet gate's rule) | the row exists; the gate passes with the migrated baseline and its reason written | — |
| C10 | hostile 16 FIRST_BEAT | "W = [[1, q],[0,1]] acting by z ↦ z̄ + q, its square is the meridian because q + q̄ = 1" | `c_beat.py`: exact check with q = e^{iπ/3}: W W̄ = [[1, q + q̄],[0,1]] = the meridian shear; the factorisation the memo states | exact identity holds | 0.95 |
| C11 | hostile 17, 18 (BEAT_DESCENT, SIGMA_27) | "Σ = exp(ad qE)∘gal extends the Gieseking element to e₆, Σ² = Ad(tick)"; "Ω² = A₂₇" | re-run only (main's 27-module code is B1011's tensor, not this construction); REGISTERED | — | — |
| C12 | hostile 19 S₄_TORSOR | "W(E₈) realizes the full S₄ on the four A₂ slots … the normalizer is computed exactly" | re-run only; REGISTERED (B1275's E₈ roots could host a normaliser computation; out of this slice's budget, named) | — | — |
| C13 | hostile 20 AW_TYPING (NEGATIVE) | "no transversal pair of the flat cone's order-96 group generates an ADE (SU(2)-type) stabilizer" | re-run only; REGISTERED as the seat's typed negative | — | — |
| C14 | hostile 21 UNIT_DICTIONARY | "every geodesic eigenvalue is a unit of an explicit palindromic quartic … geodesic length is its log-Mahler measure" | `c_unit_dictionary.py`: SnapPy's length spectrum of m004 to length 3.0; for each geodesic the holonomy eigenvalue's minimal polynomial (sympy, degree ≤ 4, palindromic, unit) and its log-Mahler measure against the length | every geodesic in the window obeys it (degree ≤ 4, palindromic, unit, length = log M) | 0.85 |

Grades: VERIFIED where the re-derivation passes; VERIFIED-DIFFERS where it does not (both recorded); REGISTERED where main has no independent means, with
the re-run receipt; C9 is a repair of main's own ledger. No grade below the seat's without a computation.

## 3. Not in this slice

The rows for the harvested-earlier items (slice D); the cc3 paper/process arcs (slice D, rows only); the hostile memos 10–15 and 22–27 already banked as
B1134–B1145 (rows in slice D); any new physics claim.

## 4. Landing list

`frontier/B1306_the_older_debt/{DESIGN_C.md, DESIGN_C.sha256, FINDINGS_C.md}`, `verification/sliceC/` (the seven own scripts with outputs, seventeen
re-run receipts, `already_banked_at_seal.txt`), HARVEST_LEDGER rows, `docs/IDENTIFICATION_LEDGER.md` I-29 + `docs/IDENTIFICATION_BASELINE.json` migration
with its reason, HINT rows, `tests/test_b1306_the_older_debt.py` slice C tests, CHANGELOG + PROGRESS_LOG + CAMPAIGN_STATUS, `arc_verdict.json`.
