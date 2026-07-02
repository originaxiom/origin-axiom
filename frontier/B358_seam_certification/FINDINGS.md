# B358 — the seam, exactly certified: √−15 lives in the twisted quantum-pair sector, and provably not in the canonical one

**Status: banked (frontier) as an EXACT result (Fraction arithmetic over `ℚ(ζ₆₀)`, zero numerics in the
banked chain; the committed C-tables carry an independent dps-40 numeric spot-check). The campaign's
pre-declared seam-positive escalation, executed: higher precision → *exact*; second independent
construction → *two*. Firewalled; nothing to `CLAIMS.md` — a field-membership statement about quantum
invariants, not physics.**

## What was claimed, and what the escalation found

A cross-session session reported (tier: numerical-exact, recommended CONDITIONAL): the H-projections of
**Par-inserted pair invariants** `tr(Par·P_a·Q_b)` at level 15 carry **nonzero `√−15` coefficients** — exact
small rationals — while single-seed controls carry none. Per the campaign's pre-declared protocol this
triggered: an independent reconstruction, in exact arithmetic, of the *entire* observable class — in **two**
constructions.

## The result — a dichotomy sharper than the claim

Both computed with the same exact engine (`cyclo_engine.py`: `ℚ(ζ₆₀)` as length-16 Fraction vectors mod
`Φ₆₀`; the full `C[j][l] = tr(Par·W₁ʲ·W₂ˡ)` tables; every double `t(a,b) = (1/240)Σ ζ₂₀^{−ja}ζ₁₂^{−lb}C[j][l]`
exactly; Galois H-average over `Gal(ℚ(ζ₆₀)/H) = {1,19,31,49}`; exact solve in `{1,√5,√−3,√−15}`):

| lift | construction | `Par`-behaviour | seam-bearing doubles |
|---|---|---|---|
| **canonical** (B355: `T = e₁₅(x²)`, `S = F₋₂/g`) | pure quadratic multiplier | `Par` **commutes** with the whole image | **0 of 49** nonzero doubles — `s = 0` exactly, every entry |
| **theta** (cross-session: `W_L = diag ζ^{j(j−1)/2}`, `W_R = F W_L⁻¹F⁻¹`) | theta-characteristic Jacobi lift | `Par·W·Par⁻¹·W⁻¹ = X¹Z²` (nontrivial Heisenberg) | **44 of 49** — exact small rationals |

**The flagship value, certified exactly at the claimed label:**
`tr(Par·P₀·Q₄) → t_H = −1/48 − (1/80)√5 − (1/48)√−3 + (1/48)√−15` — coefficient-for-coefficient the
cross-session claim (which had it from a wholly different pipeline: mpmath + Galois-conjugate transport).
**Controls, both lifts:** every single-seed `tr(Par·P_a)`, `tr(Par·Q_b)` has `√−3` and `√−15` coefficients
**exactly zero**. All 49 nonzero doubles of both lifts lie exactly in `H = ℚ(√5,√−3)` (the Hilbert class
field of `ℚ(√−15)`); the exact table also settles the cross-session "height-blocked" 217: at exact level the
theta lift has **44** seam-bearing doubles, not fewer.

## What it means (honest form)

After **five** closed channels (single object B336; classical pair points B354; quantum traces; real
overlaps/flattening; triple phases B355), **`√−15` appears — exactly — in the quantum pairing of two distinct
seeds, and only in the Heisenberg-twisted (theta-characteristic) lift sector; it provably vanishes in the
`Par`-symmetric canonical lift.** Mechanism, both directions verified in-engine: the canonical image commutes
with `Par` (so its Par-traces are parity-refined *real* data — flattened, seam-free), while the theta lift's
`X¹Z²` obstruction is precisely what lets the twisted trace reach the imaginary compositum.

**The seam coefficient is therefore a function of the lift's theta-characteristic** — extra data beyond the
bare pair of representations. The sharp open question (registered as **L57**): is a characteristic **forced**
by the pairing geometry (theta structures on the boundary torus / the gluing frame — the γ-table's quantum
face), or is it a choice? *Forced* would make the seam-bearing table an invariant of the two-seed system —
the strongest structure the multiplicity thesis has produced; *choice* would file it with the lift-dependent
decorations. Nothing is promoted either way.

## Tiers, reproducibility, provenance

- **EXACT:** both C-tables (committed as `C_canonical.json`, `C_theta.json`; regenerable by the engine — ~8
  min pure Fractions), the readout, the dichotomy, the flagship, the controls. Gates inside the engine: exact
  unitarity/orders (`W₁²⁰ = I`, `W₂¹² = I` exactly), `S² = −Par`, the `X¹Z²` obstruction (theta side).
- **Numeric guard:** committed tables spot-checked against fresh dps-40 numeric builds of both constructions.
- **Convention notes:** the theta lift is the cross-session `RL`-frame (`W('RL') = [[1,1],[1,2]]`); the
  canonical lift is B355's `RᵐLᵐ`-frame. Frame and quadratic-character class are part of the lift data — the
  dichotomy statement is at fixed frames as computed; the frame-dependence (γ-axis) is L57's territory.
- Cross-session source: the seam package (handoff + reproducers, received 2026-07-02); its numerical pipeline
  is hereby **verified wholesale** on the theta side and **complemented** by the canonical null.

**Provenance.** Campaign escalation protocol (`docs/OPEN_LEADS.md`, the value-boundary queue); B355 (the
canonical conventions + the flattening/phase nulls this dichotomy explains); B354 (the classical seam-null);
B336 (single-object); the cross-session seam package. Reproducer: `seam_certification.py` (+
`cyclo_engine.py`); test: `tests/test_b358_seam_certification.py`.
