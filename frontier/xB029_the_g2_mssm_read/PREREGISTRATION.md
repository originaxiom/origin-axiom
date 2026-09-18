# xB029 — PREREGISTRATION (sealed before the verification code exists)

**Seat `xb`, `sep16-branch`, 2026-09-18. Sealed, hashed and pushed before any cell runs.**

## P0

**B. S. Acharya, K. Bobkov, G. L. Kane, P. Kumar, J. Shao, *The G₂-MSSM — An M Theory motivated
model of Particle Physics*, arXiv:0801.0478v2 (MCTP-07-43, UCB-PTH-08/01).** The owner supplied the
PDF. **The record cites Acharya–Witten (chirality at conical singularities) and Acharya
hep-th/0212294 (moduli fixing on H³/Γ) — it has never cited this paper.** New row.

Named mathematics and source quotation only. **No value, no generation count, no physics reading,
nothing to `CLAIMS.md`. Gate 5 absolute.**

## WHY THIS SOURCE SITS ON THE RECORD'S OWN CHAIN

The framework is M theory on a singular G₂ manifold: **non-abelian gauge fields localised on
three-dimensional submanifolds**, chiral fermions at conical singularities, a **GUT group broken by
Wilson lines**. That is the record's closing, in the literature, by the author whose
hep-th/0212294 the record already cites for **flat connections on hyperbolic 3-manifolds**.

## THE CONFIGURATION AXES — declared first (xB017 Addendum 4's rule)

| axis | values | this arc |
|---|---|---|
| **what is read** | the whole paper / the visible-sector assumptions / Appendix A | **all three; §I.B and Appendix A are the load-bearing ones** |
| **what is verified** | the source's arithmetic / the record's claims about it / a new computation | **all three** |
| **the 3-manifold** | lens spaces `S³/Z_k` (the source's only worked case) / the record's object and tower | **both** |
| **the sector** | hidden (`P_eff` lives here) / visible (the record's object lives here) | **both, and the fence between them is declared in G3 BEFORE it is measured** |

## THE CELLS

**G1 — THE SOURCE'S OWN ARITHMETIC, recomputed.** Not a summary — a check.
(a) **Eq. (8):** `P_eff = 28(Q−P) / (3(Q−P) − 8)`.
(b) **Eq. (A9)/(A12)** on the source's own worked example: `P = 15, Q = 18, M = 10, λ = 80, k = 99`,
`G = P + M + 1`, `T_O = −log k`, `T_λ = log(4 sin²(Gπλ/k))`, `P_eff = −T_O − M·T_λ`.
(c) the moduli-count bound `N < 14Q / ((3(Q−P) − 8)π)`.
*Predictions, sealed:* (a) gives **exactly 84** at `Q−P = 3` and **exactly 28** at `Q−P = 4` — **both
numbers appear in the source's own text**, so this is a closed check. (b) reproduces the source's
stated **`P_eff = 58`** to within rounding. (c) is consistent with the source's sentence that larger
`Q−P` forces small `N`.
*Kill condition, binding:* **any of the three failing to reproduce is the headline**, and the
register row is graded down accordingly rather than the arithmetic being quietly adjusted.

**G2 — ASSUMED vs DERIVED, by quotation and not by memory.** Every entry must carry a **verbatim
quote** from the PDF or it does not go in the table.
*Prediction, sealed:* the visible sector's **GUT group**, its **Wilson-line breaking**, its **MSSM
chiral spectrum** (hence **the count of three**) and its **Yukawa couplings** are **assumed, none
derived**; and the source says so in its own words.
*Why this cell exists, and it is not rhetoric:* this seat's own standing negatives are a generation
count that is **fixed at one and never three** (xB026) and **no derived value** anywhere. **If the
leading M-theory-on-G₂ phenomenology programme assumes exactly those, then they are the field's open
problems and not this seat's peculiar failure** — a calibration the record should carry. **It is
equally not a licence:** an assumption shared with the literature is still an assumption, and this
cell must say so in the same breath.
*Kill:* if the source **derives** any of the four, the calibration is wrong and **that** is the
headline.

**G3 — THE ONE NEW LEAD, computed rather than admired.** Appendix A expresses the hidden-sector
threshold correction through the **Ray–Singer analytic torsion of the three-manifold**, computes it
**only for lens spaces**, needs an unnaturally large `k`, and says in its own words that **it is not
known how to compute the torsion for other three-manifolds**. **The record's bench computes torsion
of hyperbolic 3-manifolds.** Read (A12) at its natural generality,
`P_eff = log|Tor H₁(Q̂)| − M·log τ(Q̂; ρ_λ)`, and measure the **first term alone** — the term that
needs **no tuned flat connection** — on the record's own object and its tower
`b++(LR)ⁿ` (xB027's borrowed driver).
*Predictions, sealed, and they are exact:*
- **`|Tor H₁(Xₙ)| = L₂ₙ − 2`** exactly, for every `n`, where `Lₘ` is the Lucas sequence — because the
  figure-eight's Alexander polynomial is `t² − 3t + 1` with roots `α = (3+√5)/2`, `β = 1/α`, and
  `∏_{j=1}^{n−1}|Δ(ζⁿ_j)| = (αⁿ−1)(1−βⁿ) = αⁿ + βⁿ − 2 = L₂ₙ − 2`. First values **1, 5, 16, 45, 121,
  320**.
- growth constant **`log α = 0.9624237…` per degree**, i.e. **`0.4741` per unit volume** — against the
  Bergeron–Venkatesh closed-tower rate **`1/(6π) = 0.05305`**, a factor **8.94**.
- **the first `n` with `log|Tor H₁(Xₙ)| ≥ 84` is `n = 88`** (`87 → 83.73`, `88 → 84.69`), at volume
  **≈ 178.6** — against **≈ 1583** if the BV rate governed.
*Kill conditions, binding:* the closed form failing at **any** `n` ≤ the range run; or the measured
growth constant differing from `0.9624237` by more than **1 %**; or the crossing degree not being 88.
*Vacuity control, required:* `|Tor H₁|` must be **shown to grow** — an all-trivial column would make
the crossing meaningless — and `n = 1` must give **no torsion**, matching `H₁(m004) = ℤ`.
**TWO FENCES DECLARED NOW, BEFORE THE NUMBER EXISTS:**
1. **SECTOR.** `P_eff` is a **hidden-sector** quantity. The record's closing puts the object in the
   **visible** sector (E₆ + Wilson lines, L220/L221). **A number computed on the object's tower is
   therefore about a DIFFERENT three-cycle than the one the closing uses**, unless a design choice is
   made that nobody has made. **This cell may not be read as "the object tunes the cosmological
   constant."**
2. **COMPACTNESS.** `Q̂` must be a **compact** associative three-cycle. **The tower members are
   CUSPED.** The closed counterpart is the branched cyclic cover, and **whether the closed side keeps
   the rate must be MEASURED, not assumed** — a cell that measures only the cusped side and reports a
   physics-shaped number has skipped the step that matters.

**G4 — THE VERDICT**, naming every axis held fixed, and the register row.

## WHAT THIS ARC WILL NOT CLAIM

Not that the record's object tunes anything · not that `P_eff` has been computed for any G₂
compactification (the **ratio** `C₁/C₂` needs both hidden sectors, their volumes and a cutoff, none of
which this arc has) · not that an assumption shared with the literature is thereby discharged · **no
crossing of Gate 5** · no identification · nothing to `CLAIMS.md`. **The post-2008 experimental status
of this paper's predictions (light gauginos, sub-TeV gluinos, wino LSP) is NOT settled here and is
registered as CITED-UNREAD/OPEN rather than answered from memory.**

## THE SEAT'S PRIOR, DECLARED

G1 reproduces · **G2 confirms, and the honest reading is a calibration, not an excuse** · **G3's
closed form holds and the crossing is 88 — and this seat expects FENCE 2 to be the one that bites**,
because the attractive growth rate is a property of the **cusp's** Alexander polynomial and the
compact cycle the construction needs is the **closed** one · **G4: this arc's best outcome is a
well-posed lead and a corrected register, NOT a bridge — and if it reads as a bridge, it is
over-claiming.**
