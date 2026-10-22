# B1704 — WHAT HOLDS τ (P-251): W62'S HOLDING CONDITION ON MAIN — A CONTENT HOLDS τ ONLY IF ITS CUSP COEFFICIENT IS NEGATIVE; THE SIMPLE WAYS TO MAKE IT NEGATIVE HOLD τ AT i OR NEAR ω, WHERE THERE IS NO HIERARCHY; A MINIMUM IN THE HIERARCHY BAND NEEDS NET BOSONS IN THE MATTER'S REPRESENTATION AND A FINE-TUNED CANCELLATION THAT NOTHING ON RECORD SELECTS

**Verdict: PROVED (computed; no data).** cc (main), 2026-10-22. P-251 (B1697 item 7): the SM seat's W62 PH3 ("holding τ
needs net fermions in the trivial sector (W_triv/W_ρ > 31/1024) or bosons twisted along the shrinking cycle") — verify on
main, and ask whether any content meets it. 0 of 19.
- **The condition, on main.** B1686's exact cusp coefficients (ζ(6) units per unit weight, bosons positive, a Weyl
  fermion −2): 2 for a sector untwisted along the shrinking cycle, −31/16 for one twisted along it, −31/512 for the
  matter's comb. A content holds τ off the cusp only if its total is negative (V = −F; a positive total runs to the
  cusp). PH3's threshold is that algebra: 31/1024 = (31/512)/2. **Every content on record has a positive total** (B1686:
  +5.45 matter alone, +9.57 with the Higgs's copies, +57.57 with the gauge fields, +66.57 with the graviton) — **none holds
  τ.**
- **Where a holding content would hold it** (`verification/hold.py`, `hold_rho.py`; F built from B1686's lattice sums
  and PH2's verified shape for the matter, 90·(31/1024)[E(τ, 3) − E(τ, 2)]; the minima of V on Re τ = 0 and ½, y ≥ 0.9):
  - **Adding trivial-sector Weyl fermions** (from 3 on for (a), 15 for (b), 17 for (c)) **holds τ at i** on the axis (y =
    1.00) and near ω on Re τ = ½ (y = 0.91–1.05), the principle's points, where no second-to-third hierarchy exists
    (B1697, B1640).
  - **Adding scalars twisted along the shrinking cycle** flips the sign too, but leaves no minimum on either line inside
    the domain.
  - **A minimum in the hierarchy band (2.1 ≤ Im τ ≤ 3.2) needs net bosons in the matter's representation** (the E(τ, 2)
    term must enter with the boson sign) **and a nearly cancelled cusp coefficient**: matter + Higgs plus 89–95 complex
    scalars in ρ_Q (no gauge fields; Im τ* from 3.08 to 2.13), or with the gauge fields 595–672 of them (with the graviton
    689–780) — about 13–17 per matter Weyl fermion. On the axis these are minima (curvature in Re τ 0.05–0.27 against 11–149
    in Im τ: Re τ barely held); on Re τ = ½ the gauge contents give saddles. Each added scalar moves τ* by 0.01–0.2.
- **What it means.** In this frame the one-loop dynamics on record sends τ to the cusp, and the natural ways to stop it
  stop it at the elliptic points. τ in the band is reachable only by a fine-tuned integer content of bosons in the
  matter's representation, which no principle on record selects. A discrete content would fix τ with no continuous
  number — a possible mechanism, recorded as such, not a derivation.
- **What it does not do.** PH2's shape is a 1% fit (verified, B1686); minima were searched on the two CP lines only; the
  Higgs's copies are those of the line (½, ½) (B1686's three half-period lines give the same totals); no data.


> *Correction 2026-10-22 (found by the SM seat, its relay 197; checked on main, `verification/correction/mirror_check.py`).*
> Re τ = ½ is not a mirror line of V once the Higgs's copies are in: the reflection τ ↦ 1 − τ̄ sends a characteristic
> (a, b) to (a, a − b), swapping the copies at (½, 0) and (½, ½) (mirror pairs: 3 × 10⁻¹⁴ about Re 0, 4 × 10⁻⁹ about Re 1,
> 0.88 about Re ½). So the line minima reported on Re ½ were not critical points (∂V/∂x = 7.7–11.5 there). The
> trivial-fermion contents' minima lie **on the unit arc, between i and ω + 1** (y from 1.00 down to 0.89; at i for (a) + 3
> and (c) + 17, at 0.44 + 0.90 i for (a) + 8 and (c) + 25). The conclusion stands — those minima are far below the band,
> where there is no hierarchy — and so do the axis band minima, which are genuine. "At i or near ω" and "on Re τ = ½ the
> gauge contents give saddles" are corrected accordingly.

## 0. Seen first

`VERDICT topic-sweep /holds? tau|holds? τ|cusp coefficient|runs? to (a|the) cusp|PH3|31/1024|cusp.stab/ (full text): 5 of 1476 arcs on main match (PROVED 5)` —
B1295, B1684, B1686 (W62 on main: every content runs to the cusp), B1691, B1697. None locates where a holding content
would hold τ. **Literature:** the one-loop Casimir potential on a torus as Epstein sums (Kronecker's limit formulas), as
context.

## 1. Files

- `verification/hold.py` → `hold.json`, `hold_run.txt` (trivial fermions; twisted scalars); `verification/hold_rho.py`
  → `hold_rho.json`, `hold_rho_run.txt` (scalars in the matter's representation; the minima's kind). Both import B1686's
  `main_w62.py` (its lattice sums and Chowla–Selberg Eisenstein series).
- The lock: `tests/test_b1704_what_holds_tau.py`.
