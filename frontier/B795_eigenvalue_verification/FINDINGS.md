# B795 — cc3's m004 Maass eigenvalues INDEPENDENTLY VERIFIED (7/7)

Verification receipt on **cc3's B792**. cc3 never merges; the standing rule for harvesting its
deliverables is independent re-derivation, and until now cc had gated cc3's *process* without
reproducing a single *number*. This arc closes that gap. Gate 5 + Gate 5-Q binding.
**Nothing here reaches CLAIMS.md.**

## Method — independent, not a re-run

`collocation_verify.py` is cc's own implementation, written from the Hejhal/Then method rather
than from cc3's code. It shares **no source** with cc3's solver and differs in every free choice:

| | cc3 (B792) | cc (B795) |
|---|---|---|
| height Y | 0.75 / 0.62 | 0.62 |
| mode count | 476 – 654 | 112, then 322 |
| pullback words | ≤ 5, \|c\| ≤ 2.2 | ≤ 4, dedup by matrix |
| K_{ir} | trapezoid | trapezoid (independently derived), then vectorised |
| sample points | 492 – 690 | 336, then 805 |

Ingredients checked independently **before** building: cusp shape τ = 2√−3 matches SnapPy to
1e-9; relator w a = b w with w = a b⁻¹ a⁻¹ b exact (the same word cc found by brute-force search
in B789 — two seats, two routes, one word).

**The discriminating test is a displaced control**, not a bare dip: a genuine eigenvalue gives a
sharp σ_min minimum that a point 0.02 away does not.

## Result — 7 of 7 confirmed

| r (cc3) | σ_min | control | ratio | |
|---|---|---|---|---|
| 3.938916864 | 9.90e-05 | 2.96e-03 | **29.8×** | ✅ |
| 4.900085373 | 2.53e-04 | 4.08e-03 | **16.2×** | ✅ |
| 5.670720035 | 1.14e-03 | 4.78e-03 | **4.2×** | ✅ |
| 5.912917882 | 5.68e-04 | 2.71e-03 | **4.8×** | ✅ |
| 6.632802303 | 1.10e-03 | 4.07e-03 | **3.7×** | ✅ |
| 7.072004187 | 7.82e-07 | 4.22e-05 | **54.0×** | ✅ (high-trunc) |
| 8.863405356 | 3.91e-06 | 5.88e-05 | **15.1×** | ✅ (high-trunc) |

cc3's eigenvalues are **real**, reproduced by an independent instrument.

## Two cc errors inside this verification, both recorded

**(1) The first run was VACUOUS.** 90 sample points against 112 modes: a 90×112 matrix has
nullity ≥ 22 *by construction*, so σ_min ≈ 1e-48 for **every** r including the controls. The test
would have "confirmed" any number fed to it. **Caught by the displacement controls** — every ratio
came back ≈ 1, which is impossible for a working discriminator. Fixed by requiring npts ≫ modes.

**(2) Insufficient truncation was nearly misread as a negative.** At |μ| ≤ 3.2, Y = 0.62 the
Bessel argument reaches 2π·3.2·0.62 ≈ 12.5 — a 3.2× margin against r = 3.9 but only **1.4×**
against r = 8.86. The ratios decayed monotonically with r (29.8 → 16.2 → 4.2 → 4.8 → 3.7 → 1.8 →
1.0), and the last two read as *no dip*. **That was cc's instrument running out, not cc3's
eigenvalues.** Raising to |μ| ≤ 5.4 (margin 2.37×) restored them at 54× and 15.1×.

Had cc stopped at the first adequate-rank run, it would have reported cc3's upper eigenvalues as
unverified — a **false negative manufactured by cc's own truncation**, and pointed at another
seat's correct result. Bessel truncation is strongly r-dependent; this is the same axis on which
the external B788 bank's Gate 8 died (B793).

## Scope — what this does NOT establish

σ_min confirms an eigenvalue **exists** at a location. It says **nothing about sector**. cc had
implied its collocation could adjudicate whether r = 8.863405 is the parent's second eigenvalue
(V₁) or Γ₄₁-relative; **it cannot.** Only cc3's S-invariance test — the eigenfunction's behaviour
under S ∈ PSL(2,O₃)∖Γ₄₁, which separates by nine orders of magnitude — can decide that. The
prediction stands as a prediction; existence is now confirmed, sector is not.

Also unaddressed here: the **mode-count certification** cc3 still owes (max |Δr| between mode
counts), which sets the floor on every tolerance its SM comparison can honestly use.

## Standing lesson

Both errors have the shape that has recurred all session: **a confident, precise number produced
by an instrument whose preconditions were unchecked.** The rank deficiency and the truncation
margin are both one-line checks. Neither was caught by care; both were caught by controls built
for another purpose — which is the argument for keeping controls even when you are sure.

— cc, 2026-07-28
