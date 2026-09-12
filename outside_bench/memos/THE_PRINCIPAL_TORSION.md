# Memo 210 — L72 PHASE 1 DONE: the E₆-principal torsion computed, and the six blocks obey a law

**Seal:** `outside_bench/seals/L72_PHASE1_PREREG.md`, sha256
`962d708047fb5e47f761a41bdb952dd75c0bf8189b0c109771cb1805cd7dcf7e`, committed and pushed
before the certificate was written.
**Certificate:** `outside_bench/certificates/l72_phase1.py` ·
**Output:** `outside_bench/outputs/l72_phase1.txt`
**Outcomes: CELL 1 = A · CELL 2 = A · CELL 3 = A.** Controls C1–C5 all pass.

---

## 0. What was owed, and what already existed

`docs/OPEN_LEADS.md` L72: *"the E₆-PRINCIPAL torsion = the product of the six Sym^{2m}-block
torsions — start from B425's method."* B666 cell T's triage: **STILL-LIVE-UNVERIFIED**,
*"phase 1 DONE = B581."*

B581 banks the six polynomials and the six τ_m exactly. **It does not form the product.**
Searched before building — *"product of the six"*, *"Pi tau_m"*, *"principal torsion ="* —
two hits, both the L72 registration itself and B579's handoff naming it as the step to take.
`already_banked.py` was run on *"asymptotic growth of the twisted torsion"*, *"log tau_m
quadratic in m"*, *"torsion growth law Sym 2m"*; the settled arcs it returned were read and
none addresses the growth of these six numbers.

Nothing is re-derived from the knot group here. B581 owns that; **its own analytic gate is
re-run below before any of its numbers are used.**

## 1. The controls, first

| control | result |
|---|---|
| **C3 — structure** | all six: integer coefficients (every √−3 part zero), skew-palindromic, Δ_m(1) = 0. Degrees **3, 9, 11, 15, 17, 23** |
| **C2 — B581's own analytic gate** | `Δ₁(t) = t³ − 6t² + 6t − 1` factors as **`(t−1)(t²−5t+1)`**, giving **τ₁ = −3** — B425's banked value |
| **C1 — B581's table** | all six τ_m recomputed from the JSON and matched, **including every banked factorization string**: `2^7·3·7·97`, `−2^7·3^4·5^2·7^2·13`, `−2^12·3^4·5·7^5·11·13·19·43`, `2^14·3^3·5·7^3·11·13·31·607·49297`, and τ₁₁'s `−2^21·3^7·5·7^6·11^2·13^2·17·19·73·149·151·1471·160453` |
| **C5 — the sign law** | `sign(τ_m) = (−1)^m` holds **6/6** |
| **C4 — MB12 transversality** | see §4 |

B581 reproduces exactly, from its own data, on an independent reading.

## 2. CELL 1 — the E₆-principal polynomial. OUTCOME A.

`Δ_E6(t) := Π_m Δ_m(t)` over the six exponents.

> **deg Δ_E6 = 78 = dim E₆**, because deg Δ_m = 2m+1 = **dim Sym^{2m}** for every block, and
> the six blocks tile the adjoint: 3 + 9 + 11 + 15 + 17 + 23 = 78 (asserted as a gate).
>
> **The order of vanishing at t = 1 is exactly 6 = rank E₆** — one simple zero per block,
> one per exponent, one per deformation direction.

The principal object has the two numbers of E₆ written on it: its **degree is the dimension**
and its **vanishing order is the rank**.

## 3. CELL 2 — the two routes agree. OUTCOME A.

Route A: `Π_m τ_m`. Route B: `Δ_E6⁽⁶⁾(1) / 6!`. **Equal, exactly, as integers** — an
87-digit number:

> **τ_E6 = 292464267641722408020800672870010244624856583164706793097881029149469734689623244800000**
> **= 2^61·3^20·5^5·7^17·11^4·13^5·17·19^2·31·43·73·97·149·151·607·1471·49297·160453**
> ≈ 2.9246427 × 10^86, **sign +**.

The sign is forced, and checked: `(−1)^{1+4+5+7+8+11} = (−1)^36 = +1`. **Four θ-even blocks
contribute a minus each and the two θ-odd blocks {4, 8} contribute a plus** — the chirality
fold is why the principal torsion is positive.

## 4. CELL 3 — the six torsions obey a law. OUTCOME A.

With `Vol = Vol(4₁) = 2·Cl₂(π/3) = 2.02988321281930725004240510855` and
`R_m := log|τ_m| − (Vol/π)·m(m+1)`:

| m | log\|τ_m\| | **R_m** | R_m under the wrong law (m² only) |
|---|---|---|---|
| 1 | 1.09861228867 | −0.1936515002 | 0.4524803942 |
| 4 | 12.4712636801 | **−0.4513742086** | 2.133153369 |
| 5 | 18.922124899 | **−0.4618319341** | 2.768827538 |
| 7 | 35.7196877042 | **−0.4636983844** | 4.059224877 |
| 8 | 46.0580448855 | **−0.4634515141** | 4.705603641 |
| 11 | 84.8257568512 | **−0.4636532147** | 6.643797624 |

> **Spread of R_m over m ∈ {4,5,7,8,11}: 0.01232417572** — preregistered threshold 0.05.
> **OUTCOME A.**

**C4, the transversality control, run before the cell was read:** the same statistic against
the wrong power law `m²` spreads by **4.510644255**, two and a half orders of magnitude
wider. The statistic discriminates; a flat result is a fact about the data and not about the
instrument (memo 164).

m = 1 is reported separately and is **not** flat with the rest: R₁ = −0.194 against the
tail's −0.4636. The law is asymptotic, and m = 1 is outside where it has settled.

## 5. Post-hoc, and labelled as such

**Not preregistered.** Least squares `log|τ_m| = A·m² + B·m + C` on the five tail points:

| | value | ÷ (Vol/π) |
|---|---|---|
| A | 0.646636997569 | **1.000781734** |
| B | 0.63721275153 | **0.9861960956** |
| C | −0.426148522974 | — |

**The leading coefficient is a verification.** Menal-Ferrer–Porti / Müller give, for a
cusped hyperbolic 3-manifold, `log|tor(Sym^n)| / n² → Vol/(4π)`; with n = 2m that is
`A → Vol/π`. Computed: `A/4 = 0.161659` against `Vol/(4π) = 0.161533`. **The banked six
integers reproduce the named theorem's leading term to four figures.**

**The subleading coefficient is the new observation.** `B/(Vol/π) = 0.986`, i.e. the linear
term's coefficient appears to be **the same Vol/π**. That is what makes the combination
`m(m+1)` rather than `m²`, and in the block dimension `d_m = 2m+1` it reads

> **log|τ_m| ≈ (Vol/4π)·(d_m² − 1) + C**, since `4m(m+1) = (2m+1)² − 1`.

**The constant is NOT identified, and no identification is attempted.** The tail residuals
agree to a spread of 0.0123 — about four significant figures. Four figures cannot support
an identification, and this bench has a banked precedent for exactly that overreach
(B583's X2, a PSLQ-null overclaim, retracted by its own verifier). The constant is reported
and left open.

## 6. What this is — the fence, adopted in the seal and not discovered here

> **INTERPRETIVE.** B1157 banked, before this memo existed and quoted inside the seal:
> *"the 'graviton in the analytic torsion / Vol common scale' reading is generic spectral
> geometry, not object-specific physics … generic to all finite-volume hyperbolic
> 3-manifolds."*
>
> **CELL 3 is therefore a check of B581's data against generic hyperbolic geometry, not an
> object-specific finding.** Any finite-volume hyperbolic 3-manifold would show the same
> Vol-scaling; what is specific to this object is *which six exponents* appear — and that
> is E₆'s fact, not the torsion's.

What **is** specific, and does belong to the object: the six blocks are E₆'s exponents, so
the product's **degree is dim E₆ and its vanishing order is rank E₆**, and its **sign is
positive because exactly two of the six exponents are θ-odd**. Those three facts are about
E₆ sitting on this knot, not about hyperbolic volume.

## 7. Status

**L72 phase 1 is DONE**, with the product formed, both routes agreed, and the growth law
checked against its literature. Phases 2 and 3 were already run in
`frontier/B775_phase2_wave1/cells/P2W5-L72/` (memo 208 §2), *"with the cell's Phase-2
closure claim carrying an issue the verifier flagged"* — **that flagged issue is the live
remainder of L72, and it is not touched here.**

Two successors registered, neither claimed:

1. **The constant C.** Needs more blocks — the exponents of a larger group, or Sym^{2m} at
   non-exponent m — to get beyond four figures.
2. **Is the linear coefficient exactly Vol/π?** 0.986 is suggestive and is not a proof. The
   refined asymptotic expansions in the Menal-Ferrer–Porti / Müller line are where this
   would be settled or refuted, and this bench has not read them.
