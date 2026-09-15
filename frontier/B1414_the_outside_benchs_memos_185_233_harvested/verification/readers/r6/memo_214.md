# Reader r6 — memo 214 (outside_bench/memos/THE_PERIPHERAL_ROUTE_IS_EXHAUSTED.md)

## 1. HEADLINE
"L71: THE PERIPHERAL ROUTE IS EXHAUSTED, AND THE REASON IS EXACT. CELL 1 = A, CELL 2 = A, CELL 3
= NOT EXECUTABLE AS POSED, CELL 4 = A." No date line in the memo body itself; INDEX.md gives
"1B, banked 2026-09-12."

## 2. CLAIMS
1. CELL 1: `res(ξ) ≠ 0` in H¹(T²; Sym^{2m}) for every m=1..11 (six E₆ exponents + five
   non-exponents); at the six exponents `(h⁰,h¹,periph_inv) = (0,1,1)` matching P2W5-L72's exact
   ℚ(ζ₆) table — grade: **OUTCOME A**.
2. CELL 2: memo 213's identity `f(ξ(λ)) = τ·f(ξ(a))` holds on all of Z¹(T²;V), every m, not just
   the manifold's own cocycle — grade: **OUTCOME A**.
3. CELL 3 (the result): `{(k,0),(0,k)}` are both cusp cocycles, neither a coboundary, but together
   span only **1** dimension (not 2) modulo B¹ in every block m=1..6, with the exact dependence
   `(0,k) + (√−3/6)(k,0) ∈ B¹`, and `√−3/6 = −1/τ` exactly — grade: **NOT EXECUTABLE AS POSED**
   (the two-completion comparison could not run because the proposed basis is not a basis); this
   is explicitly "reported as a non-execution, not converted into an outcome letter."
4. Conclusion from CELL 3: the canonical peripheral data (ker N, coker functional f, τ) reaches
   only a 1-dimensional subspace of the 2-dimensional H¹(T²;V) — there is no canonical second
   coordinate; memo 213's slope is the *whole* canonically readable part, forced — grade: THEOREM
   (derived from the m=1..6 computation, stated as exact).
5. CELL 4: L71's four computable components (B575 integrability, B576 Zariski closure, B270
   cup-product vanishing, memo 213+214 peripheral behaviour) are all already in the record —
   grade: **OUTCOME A**.
6. BENCH ERROR #26: the seal's declared `ker N = ⟨e_n⟩` was wrong (actually `⟨e_0⟩`); corrected
   before any cell was read — grade: logged error, corrected.
7. BENCH ERROR #27: the repair itself declared `{(k,0),(0,k)}` a basis without checking rank —
   grade: logged error, corrected in this same memo (CELL 3's finding).
8. Recommendation (not an action): L71 should be re-posed as a literature/specialist item or
   closed, citing its four computable components — grade: RECOMMENDATION, explicitly not an
   action ("this bench does not edit docs/OPEN_LEADS.md").

## 3. CERTIFICATE
- `certificates/l71_peripheral_full.py` exists; `outputs/l71_peripheral_full.txt` exists (both
  confirmed in `outside_bench/`).
- Seal `seals/L71_PERIPHERAL_EXHAUSTION_PREREG.md` exists; `shasum -a 256` =
  `d5c420834fe2a78a0c0f209ad7f32e0868ec252b8f4f5f9c25a179cc169d4de9`, matching the memo's declared
  post-ADDENDUM-1 hash exactly (full 64 hex chars quoted in memo and in INDEX.md) — **MATCH**.
  (The memo also names a pre-addendum hash `7c44a929fde9…`, not separately re-verified since the
  addendum superseded it before any cell was read, per the memo's own account.)
- Output's tail (CELL 4 block) reads: "[OK] integrability at 2nd order ... [OK] Zariski closure
  per direction ... [OK] cup product at the foundation ... [OK] peripheral behaviour ... CELL 4
  OUTCOME: A (all four present: True)" — **AGREES** with memo §4 verbatim.
- The CELL 1–3 portions of the output were not independently re-printed in full in this read
  (only the tail was captured above); the memo's own quoted numbers (the m=1..6 table in §3) are
  internally consistent and match the "1" entries claimed.

## 4. ON MAIN ALREADY?
- L71 itself (docs/OPEN_LEADS.md line 522): still reads "OPEN" with its 2026-07-xx-era text
  ("The deformed reps are not discrete faithful... quasi-Fuchsian-like family?... OPEN") — **(c)
  NOT ON MAIN** as closed/re-posed; memo 214's recommendation has not been applied.
- CELL 4's cited components ARE on main with exact citations:
  - B575: `frontier/B575_bridge_obstruction/FINDINGS.md:1` — "THE BRIDGE OBSTRUCTION: Q ≡ 0. The
    bridge is open at second order, in every direction." **(a) exact match.**
  - B576: `frontier/B576_deformed_closure/FINDINGS.md:1` — "THE DEFORMED CLOSURE: the chirality is
    exactly the θ-odd motion." **(a) exact match.**
  - B270: `frontier/B270_integrability_cup_product/FINDINGS.md:1` — "integrability recomputed: the
    cup-product obstruction vanishes; deformations are cusp deformations." **(a) exact match.**
  - Memo 213 (`THE_CUSP_CANNOT_TELL.md`) is itself an outside-bench memo, not a B-arc; it is the
    fourth "where" cited by CELL 4's own output table, and is not independently on main.
- The CELL 3 result itself (no canonical second coordinate; `H¹(T²;V)` peripheral image is exactly
  1-dimensional, forced) is **(c) NOT ON MAIN** — no frontier arc found for "peripheral" +
  "1-dimensional" + "H^1(T^2" combination, nor for the exact identity `√−3/6 = −1/τ`.

## 5. NEEDS COMPUTATION HERE
- Claim 1 (CELL 1): recompute `res(ξ)` in `H¹(T²; Sym^{2m})` for m=1..11 directly (the bench's own
  peripheral-cohomology machinery, likely built on the B575/B270 second-order deformation
  complex); confirm `(h⁰,h¹,periph_inv)=(0,1,1)` at the six E₆ exponents against P2W5-L72's table.
- Claim 3/4 (the load-bearing negative — no canonical second coordinate): recompute, for each
  m=1..6, the rank of `{(k,0),(0,k)}` modulo `B¹(T²;V)` and verify the exact algebraic identity
  `(0,k) + (√−3/6)(k,0) ∈ B¹`, confirming `√−3/6 = −1/τ` symbolically (this is the single
  discriminating fact the whole memo turns on — a rank computation over an explicit small matrix,
  cheap to redo independently in sympy).
- Claim 6/7 (bench errors): DOCUMENTARY (process, not a number) — but the underlying fix (`ker N`
  support = `[0]`, i.e. `⟨e_0⟩` not `⟨e_n⟩`, given `ρ(a)=[[1,1],[0,1]]` acting on
  `e_i = x^{n-i}y^i`) is a one-line linear-algebra check worth confirming.

## 6. SUPERSESSION
No later outside-bench memo revisits L71 or memo 214 by name (INDEX.md rows 215–233 and owner
register scanned for "memo 214", "L71"; no hits beyond memo 214's own row and memo 213's
predecessor row). Not superseded on main either, since L71 has not been touched there. Stands as
the bench's own final word on the peripheral route, with an explicit unresolved remainder (the
geometric *naming* of the θ-odd deformation family) correctly flagged as out of scope for
computation.

## 7. GRADE PROPOSAL
**REGISTER** (documentary, with one cheap reproduction owed) — the memo's actual news for main is
an administrative one: L71's four computable sub-questions are already answered by banked arcs
(B575/B576/B270 + this memo's own peripheral result), and what remains is a literature/specialist
naming question, not a computation. That is a row-only update to `docs/OPEN_LEADS.md` (re-pose or
close L71, cite the four components) rather than a new arc. The CELL 3 negative result itself (the
1-dimensional peripheral image, forced) is small, exact, and cheap enough to re-verify and could
be folded into the same row as a one-line theorem citation rather than a full frontier arc.
