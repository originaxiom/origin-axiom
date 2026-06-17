# B161 — the cancellation-locus stratification: the non-cancellation obstruction, as math

**Date:** 2026-06-18. **Status:** the fragmented lead **L17** (symmetric-phase exclusion) is **formalized** into
one honestly-scoped finding — the mathematical core of the **non-cancellation obstruction** (`speculations/S034`).
The "cancellation" locus `κ=2` (commuting / abelian / periodic) is **non-generic and trivial-when-attained**,
while non-cancellation `κ>2` is **structurally typical and fractured (Cantor)** — but `κ=2` is genuinely
**attained** (B130), so this **refutes fine-tuning, it does NOT claim "forced / empty."** Standalone
character-variety / spectral mathematics; **no Origin-core claim, no physics**; P1–P16 untouched; nothing to
`../../CLAIMS.md`. Ledger V155. Reproducer `cancellation_stratification.py`.

## The reframe (the spine, made precise)

The dead physics question "*does κ source a value of Λ?*" (S014 null-hypothesis; B151 κ scale-free) is replaced
by the live **obstruction** question: *is exact cancellation structurally typical, or a degenerate, non-generic
configuration?* "Non-cancellation" is exactly named in the repo — `κ>2` = Fricke–Vogt positivity = KKT
hyperbolicity = Cantor spectrum; `κ=2` = the commuting/abelian/periodic cancellation locus (P008, K010, B127).
This finding turns that into measurable structure.

> **The honest headline: the value is free; the zero is non-generic.**

## Result 1 — cancellation `κ=2` is non-generic (codim-1, measure-zero) **[exact]**

- **(a)** `{κ=2}` is the single hypersurface `V(x²+y²+z²−xyz−4)` in the `(x,y,z)` character variety, with
  `∇κ ≠ 0` generically on it — so it is **codimension exactly 1** (measure-zero). **[exact]**
- **(b)** On the `φ_m` trace-map fixed locus, **`κ` is free** — the `κ`-elimination ideal is **empty**,
  re-derived here for **m=2 and m=4** (lex Gröbner, eliminate `x,y,z`, no `k`-only generator). So `{κ=2}` is a
  measure-zero set of fibers of a free continuum. (Independent re-derivation of B130; **κ-elimination + Jacobian
  rank, NOT `sp.solve`** — the method note that avoids the false K-G "forced choice".) **[exact]**
- **(c)** Commuting pairs are measure-zero: a random non-commuting `SL(2)` pair commutes with frequency
  `0.000000` (N=5×10⁴) and `κ` spans a continuum (std ≈ 1.7×10³). So the obstruction is **generic to non-abelian
  2-generator dynamics** — *not* special to the metallic family. **[num, null-test]**
- **MB12 (vacuity):** the claim *can* fail — an abelian (diagonal) family has `κ ≡ 2` identically, so "cancellation
  is non-generic" is a **real, falsifiable** statement, true precisely because the dynamics is non-abelian. **[exact]**

## Result 2 — cancellation is the *trivial* fiber; non-cancellation *fractures* it **[exact]+[num]+[proved]**

- **(a)** `κ=2 ⟺ λ=0` (the coupling, `κ=2+λ²`): the **free Laplacian**, spectrum = the **full AC band `[−2,2]`,
  measure 4** — "everything allowed, nothing forbidden": the trivial vacuum has no structure. **[exact]**
- **(b)** For `κ>2` (`λ>0`) the spectral measure **fractures toward 0** (Cantor dust): `|σ| = 4.000` at `λ=0`,
  then `1.817, 0.706, 0.097` at `λ = 0.5, 1, 2` (MB6 control: the periodic case gives the full band, the
  non-commuting case shrinks). Non-cancellation is the **structured residue**. **[num]**
- **(c)** The same contrast holds in the abelianized Ω skeleton: B156's endpoint entropy is **proved 0** in the
  commuting (cancellation) cone vs **`log 2`** for wall-avoiding (non-cancellation) histories. **[proved, cited]**
- The underlying dynamics: the KKT trace map is a **Smale horseshoe (uniformly hyperbolic) for `κ>2`**
  (Damanik–Gorodetski) and degenerates exactly at the `κ=2` boundary — non-cancellation is the hyperbolic,
  structured regime; cancellation is the critical, trivial one. **[established, cited]**

## Reconciliation (the intellectual core): "free value" vs "non-generic zero"

B130 proved `κ` is a **free continuum** and `κ=2`, `κ=−2` are **attained** — so no `Λ`-*value* is ever forced.
That is *not* in tension with the obstruction; it is *why* the obstruction (not a value formula) is the right
target. The two statements are about different things:

- **the value is free** (B130): no discrete `κ`-value is selected — kills value-formulas (S014);
- **the zero is non-generic** (here): within that free continuum the cancellation point `κ=2` is a measure-zero,
  trivial, non-hyperbolic fiber, while non-cancellation is the typical, structured regime.

Net: **non-cancellation needs no fine-tuning to occur** (it is generic); **but it is not "forced"** (cancellation
is attained, not impossible). "Forced / empty / excluded" is **refuted** and is retired from this finding.

## Firewall

Pure character-variety / spectral mathematics. "Non-cancellation" appears only as **motivation** (the physics
reading lives, firewalled, in `speculations/S034` as a Tier-3 `[LEAP]`). **No `Λ` value, no scale** (B151), **no
spectral-mass identification** (S015/B107 dead); the `κ=2 ⟺ λ=0` band is "one particle in a periodic crystal,"
not a particle spectrum. Nothing promotes to `CLAIMS.md`; P1–P16 untouched.

## Anchors
B130/V119 (κ free continuum; the κ-elimination method), B156/V150 (the collapse wall det G=−δ/(m+1); TC-4 no-go;
endpoint entropy 0 vs log 2), B127/B124 (the Fricke–Vogt dictionary; κ=2 = commuting/periodic), B148/V137
(κ=4·I_FV+2), B151/V140 (κ scale-free), K010/K007/P008 (the named object), `speculations/S034` (the firewalled
spine), `docs/OPEN_LEADS.md` L17 (→ BANKED). External: Sütő (1987); Damanik–Gorodetski (the KKT horseshoe).
Ledger V155.

## Reproduction
`python frontier/B161_cancellation_locus_stratification/cancellation_stratification.py` — R1 (codim-1; κ free
m=2,4; null-test; MB12 abelian control) + R2 (λ=0 full band; MB6 fracture). Prints `ALL CHECKS PASS`.
