# B1072 — the matching-capacity floor: seven nulls are one measurement of an instrument

**Date:** 2026-08-17 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS / METHODOLOGY.
**Gate 5:** no physical identification; no value is claimed, derived or promoted. The measured
constants appear only as **precisions**, never as targets to be matched.

**Verdict: PROVED.** Reproducer `capacity.py`, all controls pass.

## The question

`B563`, `B549`, `B558`, `B615`, `B724`, `B743` and `B322` each compared object outputs against
measured constants and each returned null. They are read as seven results about the object. This
cell asks whether they are instead **seven measurements of one instrument's noise floor**.

## The model, and that it is calibrated rather than assumed

Candidates have a **local** density `ρ` (per unit natural log) near a target's magnitude. A target
is matched at relative precision `δ` if some candidate lies within `|ln cand − ln t| < δ`. Poisson
placement gives `P = 1 − exp(−2ρδ)`, and the information a match carries is `−log₂ P` bits.

`ρ` is **not assumed**. It is calibrated from the corpus's own recorded hit counts, per regime:

| regime | calibration | `ρ` (per unit ln) |
|---|---|---|
| sealed φ-expressions (`N = 28957`) | TOMBSTONES H128 (37 hits) and H129 (208 hits) | **2794** |
| PSLQ over the algebraic tower | B743's surrogates, 69% hits at 5 digits | **58559** |

## Controls — and the first model was rejected by one of them

- **C1** the two H128/H129 windows are **independent** and agree on `ρ` to **1.30×**.
- **C2** the PSLQ calibration **predicts** `P = 1.2×10⁻⁶` at 11 digits; B743 observed **0 of 50**.
- **C3** B322 — used in **neither** fit — implies, from its own null mean of 7.6/12 at 1%, a
  spread of **54 decades** for its 6241 ratios, against B724's independently reported ~36.5-decade
  torsion spectrum roughly doubled by ratio-taking. Consistent.
- **C4** direction sanity: `P → 0` at `10⁻¹⁰`, `P → 1` at `4×10⁻²`.

**A first version of this cell scaled `ρ` between regimes by raw candidate count and its own C3
rejected it** — it predicted 12.0 of 12 for B322 against an observed null mean of 7.6. `ρ` is a
*local* density and B322's candidates spread over dozens of decades. The model is per-regime
because that failure forced it; the failed version is recorded here rather than quietly dropped.

## The floor

| regime | `p < 0.05` needs | significant digits |
|---|---|---|
| φ-expressions | `δ < 9.2×10⁻⁶` | **5.0** |
| PSLQ tower | `δ < 4.4×10⁻⁷` | **6.4** |

## Every SM parameter against the stricter floor

**Informative** (a match could carry ≥ 4.32 bits): `m_p/m_e` (18.9 bits), `α_em⁻¹` (15.8),
`m_μ/m_e` (8.6). **No information** (a match is statistically guaranteed): `m_τ/m_μ`,
`sin²θ_W(M_Z)`, `m_W/m_Z`, `|V_us|`, `α_s(M_Z)`, `|V_cb|`, `sin²θ₁₃`, `sin²θ₁₂`, `sin²θ₂₃` —
**nine of twelve.**

## The reading

> The seven nulls compared against targets in the no-information band. **They could not have
> produced evidence in either direction.** They are seven measurements of this floor, and they
> agree with it.

Two consequences the corpus should carry:

1. **A 16σ miss and a 0.04σ hit in that band carry identical information: none.** Both the sealed
   B915 failure and the H128 near-miss sit below the floor.
2. **Every constant that clears the floor is a QED or pure mass ratio.** Not one is a mixing
   angle, a gauge coupling, or a symmetry-breaking parameter — i.e. not one is a quantity the
   programme's structural results speak about. Numerical matching here is not merely weak; it is
   aimed at a sector the object says nothing structural about.

## Scope

**This is a statement about the INSTRUMENT, not about the object.** It does not say the object
lacks any relation to any constant; it says that *comparison at achievable precision* cannot
detect one. It does not retract any of the seven arcs — each is correct as computed — it re-reads
what their agreement means. The density model is calibrated from four recorded counts in two
regimes and would move if those counts were wrong. Gate 5 untouched: no value is derived,
compared, or promoted here.
