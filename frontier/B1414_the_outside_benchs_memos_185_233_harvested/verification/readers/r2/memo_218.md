# Reader r2 — Memo 218 (THE_INVARIANTS_ARE_EXACT.md)

## 1. HEADLINE
"L72's LEVEL-2 INVARIANTS, EXACTLY — AND THE UNIQUENESS RESIDUAL REACHES NONE OF THEM." Cells
1–4 = A/A/A/A, controls C1–C3 all pass. Banked "1B, 2026-09-13" per `INDEX.md`.

## 2. CLAIMS
1. **CELL 1 = A**: `P2W5-L72`'s E₆ level-2 colored invariants of `4₁`, computed exactly in
   `ℤ[ζ₇]=ℤ[x]/Φ₇(x)` with no floating point: N=1 (spin 0) `J=1`, minpoly `x−1`, degree 1; N=3
   (spin 1) `J=−2z⁵+z⁴+z³−2z²+3`, minpoly `x³−10x²+17x−1`, degree 3; N=5 (spin 2)
   `J=2z⁵+z⁴+z³+2z²+2`, minpoly `x³−3x²−4x−1`, degree 3. Grade: PROVED (exact symbolic
   computation).
2. All three invariants generate the **same cubic field** `ℚ(ζ₇)⁺`, identified by discriminant:
   generator `x³+x²−2x−1` has disc **49**; N=3's minpoly has disc **8281 = 49·13²** (ratio a
   rational square); N=5's minpoly has disc **49 exactly** (ratio 1). Grade: PROVED.
3. The invariant carrying the E₆ **adjoint** (78, at spin 2, N=5, per the cell's own note) is a
   root of `x³−3x²−4x−1`, disc 49 on the nose. Grade: PROVED, given claim 1's polynomials.
4. **CELL 2 = A**: exact values evaluated at 30 digits — `1.0000000000000`, `2.0881460000204`,
   `−0.6920214716301` — with imaginary parts `1.2e−35`, agreeing with the cell's printed floats at
   every printed digit; vanishing imaginary parts confirm reality via Habiro's `q→q⁻¹` symmetry.
   Grade: PROVED / verified.
5. **CELL 3 = A**: `J_fig8`'s body (5 lines of `q`,`N`) contains **zero** F-symbol/associator
   tokens; of 17 stored keys, only `D_object` holds knot numbers, `C_level2` stores **counts**
   (2646 F-symbols) and verification residuals (not consumed downstream), and every other stored
   value derives from the Weyl sum / SnapPy / Fox calculus. Conclusion: the uniqueness residual "is
   real as a statement about the category and inert for every number the cell reports." Grade:
   PROVED (a structural/code-inspection fact, not a numeric one).
6. **CELL 4 = A**: `K` (object's trialitarian cubic, memo 204) = `x³−12x−5`, disc `6237 =
   3⁴·7·11`, squarefree part 77, **not** a perfect square ⇒ Galois group **S₃ (non-cyclic)`.
   `ℚ(ζ₇)⁺` = `x³+x²−2x−1`, disc **49**, a perfect square ⇒ Galois group **C₃ (cyclic)`. **Not
   isomorphic, by Galois type**, not coefficient accident; "7 divides both discriminants, and that
   is the whole of the resemblance." Grade: PROVED.
7. Controls: **C1** — Habiro's form reproduces the Jones polynomial of `4₁` at N=2 exactly in
   `ℤ[q,q⁻¹]` (difference identically 0), PASS. **C2** — the `j=N` tail-vanishing term is
   identically zero for N=1,3,5, PASS. **C3 (MB12)** — the minimal-polynomial routine returns 6 for
   `ζ₇` and 1 for a rational, confirming "degree 3" is a genuine finding, PASS.
8. Summary table: phase 1 DONE (memo 210); phase 2 sound+reproduced (memo 211) with stale artifact
   **regenerated (memo 216)**; the uniqueness residual "narrowed to a categorical footnote... what
   remains is a citation... literature, unread here, and not cited"; phase 3 walled/external.

## 3. CERTIFICATE
- **Seal:** `outside_bench/seals/L72_EXACT_INVARIANTS_PREREG.md` — **exists**. Computed
  `shasum -a 256`: `4621857a643e631fbb6d1ceeb2bcee450aa58122db4f50947236cb301082b6a3` — **matches**
  the memo's stated hash exactly.
- **Certificate:** `outside_bench/certificates/l72_exact_invariants.py` — **exists**.
- **Output:** `outside_bench/outputs/l72_exact_invariants.txt` — **exists**. Tail confirms Cell 3
  outcome A with matching prose ("D_object (the only reported knot numbers)... C_level2 stores
  COUNTS of F-symbols and VERIFICATION residuals (n_F_symbols_level2 = 2646), not a number that
  feeds anything downstream") and Cell 4 outcome A with the exact polynomials, discriminants
  (`6237 = {3:4,7:1,11:1}`, squarefree part 77; `disc=49`) and Galois-group calls (`S3
  NON-cyclic`, `C3 (cyclic)`) matching claim 6 verbatim. **Agrees with headline.**

## 4. ON MAIN ALREADY?
1. **The memo's own action item — "stale artifact regenerated (memo 216)":** **(a) already on
   main.** Confirmed directly (see reader r2's memo 211 write-up, §4.1): `results.json` at
   `frontier/B775_phase2_wave1/cells/P2W5-L72/` has `h1: 1`/`rel_ok: True` for all six exponents,
   `verdict: RESOLVED-A`, `gate5` present, landed via commit `e15eaada`.
2. **The exact ℤ[ζ₇] invariants / cubic field ℚ(ζ₇)⁺ result:** (c) **NOT** found anywhere in
   `frontier/B775_phase2_wave1/` — the committed `compute.py`/`results.json`/`output.txt` for
   `P2W5-L72` report the level-2 colored invariants as **floats only** (this is the memo's own
   starting premise, claim 0/1); nothing on main upgrades that arc's own artifacts to the exact
   `ℤ[ζ₇]` form memo 218 computed. The exact form lives only in `outside_bench/`.
3. **Object's charge field `K` (memo 204's trialitarian cubic) vs. `ℚ(ζ₇)⁺` non-isomorphism (claim
   6):** `K = x³−12x−5` is the object's charge field cited from **memo 204**, itself an
   outside_bench artifact; a search of `docs/IDENTIFICATION_LEDGER.md` and related ledgers for
   "trialitarian cubic" / "x^3 - 12x - 5" found no hit in `docs/` — (c) **NOT on main's own
   ledgers**, though it is internally consistent with `docs/TOE_REQUIREMENTS_LEDGER.md`'s use of
   `⁶D₄` / non-cyclic-Galois language for the object elsewhere (not verified to be the identical
   claim, just not contradicted).
4. **The uniqueness residual's status ("literature, unread here, not cited"):** superseded almost
   immediately — see §6.

## 5. NEEDS COMPUTATION HERE
- **Claim 1 (exact invariants):** recompute `J_N(ζ₇)` for N=1,3,5 directly from Habiro's cyclotomic
  expansion of the colored Jones polynomial of `4₁` evaluated at the level-2 E₆ quantum parameter
  (`q = exp(iπ/7)` per the companion memo 211's identification), reduce mod `Φ₇(x)`, and recompute
  minimal polynomials with `sympy.minimal_polynomial`. Expected: `x−1`, `x³−10x²+17x−1`,
  `x³−3x²−4x−1` exactly, matching claim 1.
- **Claim 2/6 (discriminants and Galois type):** `sympy` or PARI `nfdisc`/`polgalois` on the three
  cubics (`x³+x²−2x−1`, `x³−10x²+17x−1`, `x³−3x²−4x−1`, `x³−12x−5`) — expected discriminants 49,
  8281, 49, 6237 respectively, and Galois groups C₃, C₃ (same field), C₃, S₃. This is the single
  discriminating fact for "not isomorphic by Galois type."
- **Claim 5 (no F-symbol tokens in `J_fig8`):** DOCUMENTARY / code-inspection — a verifier should
  just `grep` the cell's `compute.py` source for the actual closed-form `J_fig8` function body and
  confirm it references only `q`, `N` (Habiro sum), not any F-symbol/associator variable.

## 6. SUPERSESSION
- **The uniqueness residual ("narrowed to a categorical footnote... literature, unread here") is
  superseded by memo 220** (`THE_RESIDUAL_IS_DISCHARGED.md`, banked 2026-09-13, same day as memo
  219 and shortly after 218): memo 220 reads Rowell-Stong-Wang directly (owner-supplied PDF,
  `arXiv:0712.1377v4`) and **discharges** the residual with four passing checks against the rank≤4
  MTC classification — the exact literature gap memo 218 (and 211, and 219) had each left standing.
  Per `INDEX.md` row 220: "memo 211 closed its Galois half, memo 218 showed it reaches no reported
  number, memo 219 said the rest was literature this box could not reach" — then 220 closes it.
- Memo 218's own Cells 1–4 (the exact ℤ[ζ₇] computation, the field identification, the non-
  isomorphism with K) are **not** revisited or contradicted by any later memo found in `INDEX.md`.

## 7. GRADE PROPOSAL
**SUPERSEDED** (for the residual-status framing) combined with **REPRODUCE-AND-BANK** (for the
exact invariants themselves, which are a genuine new computed fact with no equivalent on main).
The memo's headline claim about what remains open ("literature, unread here, not cited") was true
for less than a day — memo 220 closed it the same banking wave. But the substantive content —
exact cyclotomic-integer colored invariants of `4₁` at E₆ level 2, living in `ℚ(ζ₇)⁺`, disc 49,
provably distinct by Galois type from the object's own charge field `K` — is a clean, cheap,
independently-checkable computation that has not been promoted to `frontier/` (the committed cell
still reports floats only), so it is worth an arc row on its own merits regardless of the residual
question being closed elsewhere.
