# B1322 — L204 VERIFIED: the SM-derivation seat's sm:B1350 ("the V₁₀ direction carries genuine non-self-dual E₆ representations and N(27) = 0 on all of them") re-read on main with main's own Fox calculus at the seat's banked 100-digit points: DESIGN (pre-registration, sealed before any of main's computations)

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §3 (B1299's L204 row: "main's arc for this lead verifies sm:B1350 when its stage 4 lands, with
credit by pin"); the harvest gate reported the landing the same day (NEW after slice B's pin). · **Seat pinned:** the SM-derivation branch @ `7484ad01`
(sm:B1350 PROVED, 2026-09-08 late; its `report_hp.py` re-run launched here in the pinned worktree before this seal), `d722714f` (its harvest-from-main
commit and the relay's fourth note). · **Read in full before this seal:** sm:B1350 FINDINGS §4(d)–(e) and the closing paragraph, `report_hp_run.txt`'s
summary, `v10_direction_points.json`'s structure (four directions × two 27 × 27 matrices at 100 digits + the Newton residual), B1268's addendum "two
precision caps", the relay's fourth note, the CHIRALITY_MAP §6b; the presentation the points satisfy (B1267's `spectrum_law.py`: ⟨a, b | a w b⁻¹ w⁻¹⟩,
w = b a⁻¹ b⁻¹ a, meridian a, longitude w w* with w* = a b⁻¹ a⁻¹ b). **Nothing below was computed with main's own code before the seal.**

## 0. The rule lines

`already_banked.py "V10 direction subregular N(27) non-self-dual E6 representation theta-odd frame"` → B1299 (the hole registered), B1268 (the seat's
V₈ instrument, harvested), B1280/B1298. The claim under test is the seat's, one day old; main has nothing on it beyond L204's registration and slice B's
REGISTERED row for stages 5a–5c. Receipt: `verification/already_banked_at_seal.txt`.

## 1. The view from above

L204 is the last frame in which the cusped object could have carried a net count of 27s: B1280's pairing law paired every other deformation of the E₆
holonomy at every sl₂ germ, and B1299 verified that exactly one direction — the V₁₀ of the 42 at the subregular point — escaped the pairing, pricing
the computation at a day and a 15 % prior that N ≠ 0 there. The seat has now done the computation: along that direction genuine E₆ representations
exist, they are not self-dual, and N(27) = 0 at each. If that holds on main's own code, the θ-odd frame is closed on every sl₂ germ and the head sentence
of the programme loses its last "one direction remains" clause — chirality on the object then lives only outside this frame (the higher-rank components,
the general theorem, the singular G₂ closing). **The one thing it means if main's re-read disagrees:** the disagreement is the finding (VERIFIED-DIFFERS),
recorded on both benches, and L204 stays open.

## 2. Pre-registration (`verification/b1322_l204_verify.py`, main's own code: mpmath at 110 digits, the seat's points loaded as decimal strings)

For each of the four banked directions (class 1, class 2, their sum, their difference): (a) **the point is a representation** — the relator
a w b⁻¹ w⁻¹ evaluates to the identity in the 27 with residual ≤ 10⁻⁶⁰ (the seat's Newton residuals are 10⁻⁶¹ … 10⁻⁶⁸); (b) **it is not self-dual** —
tr ρ(g) ≠ tr ρ(g⁻¹) for g ∈ {a, b, ab} by more than 10⁻¹² (the seat: defects 10⁻⁸ … 10⁻¹¹); (c) **h¹(M; 27) and h¹(M; 27̄)** by main's own Fox calculus on
the one-relator presentation (d⁰: 54 × 27, d¹: 27 × 54; ranks decided by the full pivot spectrum at 110 digits, threshold 10⁻⁵⁰, with the gap printed;
27̄ = the inverse transpose); (d) **h⁰(∂M; 27), h⁰(∂M; 27̄)** — the common fixed space of ρ(a) and ρ(λ), λ = w w*; and [ρ(a), ρ(λ)] ≈ 0 as the peripheral
check; (e) **N(27) := h¹(27) − h¹(27̄)** and the seat's bound −h⁰(∂M; 27) ≤ N ≤ h⁰(∂M; 27̄). **PASS** = at every direction h¹(27) = h¹(27̄) = 0, h⁰(∂M; ·) = 0,
N = 0, non-self-dual, relator ≤ 10⁻⁶⁰ — the seat's table to the entry; **FAIL** = any entry differs (the finding). Prior 0.85 (the seat's re-read at 2000
bits has gaps of thirty orders; the residual risk is a convention mismatch between the loaded matrices and the presentation, which control (a) detects).
**Controls, all before the verdict:** (i) main's Fox code on B1297's exact geometric ρ in Sym^k for k = 0 … 6 must return h¹ = 1, 0, 1, 0, 1, 0, 1 (B1256/B1267,
already B1297's control) — the implementation; (ii) a point perturbed by 10⁻³⁰ in one entry must fail (a) — the relator check can fail; (iii) the same
code at the seat's exact subregular point ρ₀ (rebuilt from the seat's `spectrum_law.py`, read as an input, not trusted) must return h¹(27) = 3, h⁰(∂M; 27) = 3,
N = 0 — the seat's exact stage 0 — so a "0" at the deformed points is a change the code can see.

## 3. Landing list

`frontier/B1322_l204_verified/{DESIGN.md, DESIGN.sha256, FINDINGS.md, arc_verdict.json, verification/{b1322_l204_verify.py, .out, .json, sm_B1350_report_hp_rerun.txt, already_banked_at_seal.txt}}`,
`tests/test_b1322_l204_verified.py`; OPEN_LEADS L204 → CLOSED (with credit by pin), MAIN_GOAL's head sentence and JOIN 1 note, THE_SM_VERDICT banner line,
CHIRALITY_MAP? (the seat's document; main's CAMPAIGN_STATUS), HARVEST_LEDGER row + the sm pin → `d722714f`, RELAY_LEDGER (the fourth note BANKED), the
kill graph (a NEGATIVE-shaped closure of a door: route it), the alias table (B1322 taken, next B1323), CHANGELOG + PROGRESS_LOG + CAMPAIGN_STATUS.
