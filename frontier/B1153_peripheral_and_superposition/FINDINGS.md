# B1153 — THE PERIPHERAL IDENTITY + THE SUPERPOSITION SPEAKS: cloud memos 54–55 verified by reproduction — tr(ab⁻¹)=gal(κ) is the Riley relation in disguise (the full fixed locus completed), and C4's honest negative closes *positive* as the exact 2-fold GUE superposition of ζ·L(χ₋₃)

**Status: banked (frontier). Verdict PROVED-BY-REPRODUCTION (both self-contained certs re-run on THIS
bench's pyenv 3.12.1 exit rc=0 — every claim a preregistered assert — and reproduce byte-identical).
PLUS memo 54 independently sympy-confirmed. Harvest arc — the cloud seat's memos 54–55
(`origin/outside-bench` `0c7f8b5a`, primary source shared-remote). Integrate-don't-merge. Gate 5
untouched. Lock `tests/test_b1153_peripheral_and_superposition.py`.**

## The two cells (memos 54–55), reproduce-verified

| memo | cell | claim (verified reproducing, rc=0) |
|---|---|---|
| **54** | THE PERIPHERAL IDENTITY + THE FULL FIXED LOCUS | **PART I:** **tr(ab⁻¹) = gal(κ)** is a *peripheral* identity. Deriving the m004 nonabelian trace relation in-run as `P(x,z)=z²−x²z+2x²−z−1`, one gets `S−3 = P + (x²−4)` with quotient exactly 1 (S := tr(ab⁻¹)+κ). So on the component (P=0): **tr(ab⁻¹)+κ = 3 + (tr a−2)(tr a+2)** — it holds tr(ab⁻¹)=gal(κ) **precisely where the meridian is parabolic** (P(2,z)=z²−5z+7, both geometric characters, scheme-theoretically), with defect **exactly x²−4** off it. The object's "3" is the cusp condition — the **Riley relation in disguise**, a **fourth TRACE THREE** appearance (memo 49). **PART II:** the memo-43 trace map's **full fixed locus** on the cusped surface is exactly **3 points** (Gröbner elim `z²(z²+12)`, scheme length 4=1+1+2): the κ-pair (simple, coords κ/gal κ) + **(0,0,0)** (codex's point, non-reduced mult 2). Conjugation swaps the κ-pair and **fixes** the origin — the mirror's free orbit is still exactly the κ-pair. Closes codex OA-C1082/OA-C1083; completes memo 43. *[extraction error machine-caught in-run before any claim.]* |
| **55** | THE SUPERPOSITION SPEAKS (C4 closes positive) | Executes **B1151's named follow-up** on **B1151's own committed data** (main @ 522c7caa). The 2-fold GUE superposition surmise `E(s)=E_W(f₁s)·E_W(f₂s)`, CDF=1+E′(s), fractions f_ζ=0.4522 / f_L=0.5478: **S1 — merged vs superposition D=0.02400** (vs single-GUE 0.13359), *below* even the factors' own single-GUE residuals (0.040/0.049), passing the preregistered D gate (D<0.06 and D<D_single/2) with a **5.6× margin** (p=0.0037 fails strict 0.01 exactly as B1151's fence predicts for any surmise-level model at n≈5459). **Control C1** — each factor *rejects* the superposition (D≈0.18) while fitting single-GUE (0.04): the model wins **only** where the product structure is real. Anchors A1/A2 reproduce B1151 (0.0401/0.0487/0.13359). |

**Independent check (sympy, this bench):** `S−3−(P+(x²−4)) = 0`; `P(2,z)=z²−5z+7`; the fixed-locus
elimination `z²(z²+12)` has roots {0 (mult 2), ±2√3 i} = 3 points, length 4. memo 54's PART I identity
and PART II locus confirmed with a derivation **distinct** from the cert.

## Why this batch matters — the through-line

The **peripheral (cusp)** reading of memos 41/43/49 is sharpened to an **identity** — tr(ab⁻¹)=gal(κ)
*is* the Riley/parabolic relation, and the object's "3" is the cusp condition (a fourth trace-3
appearance); and the **spectral** C4 arc, banked as an honest negative (B1151), **closes positive**:
the merged ζ_K spacing is the exact 2-fold GUE superposition of its two factors. Both are
peripheral/spectral facts about the *same* object (the cusp voice's numerator Λ_K = ζ·L(χ₋₃)), and
both are **generic** — no object-specificity, no firewall crossing.

**B1151's negative and memo 55's positive are two halves of one statement:** ζ_K's nearest-neighbour
statistics see exactly its factorization — two independent GUE spectra with no cross-repulsion, no
more and no less.

## Codex Wave-3 corrections adopted (into B1148/B1149; the banked math is unchanged)

memo 54 carries three codex-Wave-3 corrections to earlier memos, adopted at point of occurrence — all
**terminology / scope**, the exact identities untouched (see the dated addenda in B1148/B1149):
- **"antiunitary" → "semilinear"** (memos 45/46/50): β_Ψ is Galois-semilinear; β_Ψ²=ρ_Ψ(a) is a
  nontrivial unipotent, never unitary for a positive-definite form, and no Hermitian metric was
  constructed. Every exact identity (β_Ψ² = the meridian; C_Ψ commuting; the depth grading) stands.
- **the carrier is "*a*" carrier, not "*the* minimal" one** (memo 46, codex OA-C1087): built on the
  *banked* minimal-A1 bridge (a choice, memo 29), its properties are theorems but its selection is not.
- **memo 43's fixed pair is "*a* second" point, not "*the*"** (codex OA-C1082): the locus also contains
  (0,0,0) — memo 54 PART II — with the mirror-free orbit still exactly the pair.

## Honest fences

memo 54 PART I is rational polynomial algebra (no algebraic numbers touched); PART II is
interpolation-plus-verification (traces are polynomial coordinates on X(F₂), CITED-standard, + a
40-sample exact verification + a Gröbner computation over ℚ). memo 55 is **generic** throughout — the
2-fold GUE superposition is the expected class for *any* product of two L-functions (the B1142/B1151
fence); no object-specificity, **no firewall crossing**; the named residual (exact Gaudin per-factor +
higher-order unfolding) stands. Data note: the committed ζ file carries **2469** zeros (B1151's prose
said 2468) — immaterial, the anchors reproduce. Gate 5 untouched throughout.

## Discipline

Verified by reproduction (self-contained certs, our pyenv, **rc=0 = every preregistered assert
GREEN**, verdicts byte-identical — `verification/reproduce.log`, 2/2) + an independent sympy
cross-check of memo 54 (`verification/independent_check_memo54.txt`). Primary source shared-remote
(push-before-cite satisfied; certs on the source, runner `verification/reproduce.sh` provenance-headed
per L183; memo 55's c4data zeros are the cloud's verbatim vendor of *this seat's* B1151 scan). Cloud
seat credited (memos 54–55); codex credited (the Wave-3 OA-C10xx rows driving memo 54 + the three
corrections). Gate 5 untouched.
