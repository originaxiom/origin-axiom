# B916 — THE LAMBDA BRIDGE: 2304/953 vs 1 is NOT a convention — it is a second H, and both numbers are exact invariants

**Date:** 2026-08-05 · **Seat:** cc (computation agent) · **Status:** DRAFT, not banked
**Inputs:** banked B883 `rep27.json`, B912 `results.json` (H±, D), B914 `results.json`
(exact cubic, exact q's, exact couplings); solo handoff 7 `rep27.pkl` / `H27.pkl` /
`cubic27.json` / `tauP.pkl` (dir given by the `HANDOFF7` env var).
**Instrument:** `bridge.py` → `results.json` (53 exact/numeric gates, all PASS,
plus 8 recorded data verdicts; runtime ~40 s).

## The question

Two seats computed "the same" colorless coupling invariant
λ = |c| / √|h_i h_j h_k| on the same nine colorless atom lines:

- **cc (B914, banked):** λ = **1 exactly** — banked B883 27, exact ±1 primitive
  cubic re-solved in that basis, integer H+ from B912.
- **solo (handoff 7):** λ = **2304/953** (= 2⁸3²/953) at 85 digits — their
  realization (which B914 proved is the 27bar), their ±1 cubic, their H.

Hypothesis under test: the factor lives in the normalization relation between the
realizations ("primitive ±1 in its own basis" is basis-dependent).

## The verdict: hypothesis REFUTED — and both seats are right

**The bridge exists and is rigid.** Solving ρ_h(x) S = −S ρ_B883(x)ᵀ for all 78
generators (exact, over ℚ): the two-term equation graph is connected, so S is
unique up to one scale (Schur), and — because BOTH realizations have all matrix
entries in {−1, 0, +1} — the primitive S is a **signed permutation** (det S = 1).
Verified entrywise for all 78 generators. There is no room for any scale factor
in the bridge: **953 cannot come from S** (nor from its determinant or any Gram).

**The cubic is bridge-canonical: t = 1.** The transported handoff cubic
c′(u,v,w) = c_h(Su, Sv, Sw) equals the banked B883 primitive cubic **entry-by-entry
on all 45 triples** (both are 28 plus / 17 minus; both verified as exact derivation
identities for all 78 generators; the handoff kernel is dim 1 and their file spans
it). "Primitive ±1 in its own basis" is NOT basis-dependent here — it is canonical
across the mirror.

**The H's are two different invariant objects — this is the whole factor.**
H′ := Sᵀ M_solo S has the same signed-permutation support π as the banked H+, but
H′ = H+ · diag(D₂) with **11 of 27 signs flipped** (D₂ ≠ B912's D). No scalar s
exists. The solo M is not an error of arithmetic: it is a **different instrument** —
their τ-intertwiner (tauP route): M = P·D_χ with P ρ(τX) = −ρ(X)ᵀ P, τ the
algebra twist with Cartan permutation (5,1,4,3,2,0). Verified exactly: M is **not**
charge-equivariant for any sign on any of the four charges (R₈,R₁₄,R₁₆,R₂₂),
whereas the banked H+ satisfies RₙᵀH + εₙHRₙ = 0 with ε = (−,+,−,+) (re-verified).

**Both λ's are exact, and both are realization-independent:**

| instrument | primal nine (27, B883) | mirror nine (27bar side) |
|---|---|---|
| banked H+ (charge-equivariant) | **λ = 1 exact** (re-verified: c² = −q_iq_jq_k for all six couplings) | **λ = 1 exact** (proved here in Mbar) |
| solo H′ = H+·D₂ (τ-twisted) | **λ = 2304/953 exact** (all six couplings) | **λ = 2304/953 exact** (all six couplings) |

The mirror nine are pinned exactly: the S⁻¹-transported handoff atom lines are
**H+·(primal atom lines)**, line for line (numeric belt < 1e-45; and v = H₊u is
certified exactly as a joint left-eigenline family). The solo seat's 85-digit
2304/953 was independently recomputed from their files (residual 9e-47) and is
**exactified** here: |c|² = (2304/953)²·(q′_i q′_j q′_k) exactly, all six couplings.

## Where 953 lives

The per-line ratio d_i = q^{H′}_i / q^{H+}_i is a cubic irrationality of the
value field K (branch-indexed: the three Galois branches per family):

- S-family minpoly: 2304²x³ + 9123840x² + 5077008x + 953²
- A-family minpoly: 2304²x³ − 1907712x² − **2304·953**·x + 953²

Every coupling triple is a Galois orbit, so its d-product is a K/ℚ-norm:
**∏ d_i = N_{K/ℚ}(d) = −(953/2304)²** exactly, for all six couplings — hence
λ_τ/λ_canonical = |N(d)|^{−1/2} = 2304/953. The prime 953 is the **norm
arithmetic of the H-twist** (the τ-intertwiner vs the charge-equivariant form),
not a normalization and not a property of the lines or the cubic.

## What this changes

1. **Cross-seat reconciliation:** neither pipeline has an arithmetic error. The
   premise "the same invariant" was false at exactly one leg: the H. The two
   seats' (cubic, atoms) agree canonically through the bridge.
2. **The canonical λ of the colorless nine is 1** — with the charge-equivariant
   H the coupling and the H-norm product coincide exactly (c² = −Πq, sign
   included). Democracy is an identity, not a number.
3. **The τ-twisted λ = 2304/953 is a genuinely new second invariant** — the
   discrepancy IS content: it measures the H+-vs-τ-intertwiner twist on the atom
   lines, with 953 = the norm-denominator of the twist ratio d ∈ K. The solo
   seat's "953-family" (their FT3/FT5, CCC = 6λ) now has an exact home.
4. For future cross-seat work: **pin the H by its equivariance pattern**, not by
   "primitive ±1" (both H's are primitive ±1 signed permutations!).

## Files

`bridge.py` (the instrument; env: `HANDOFF7`, optional `SESSION_SCRATCH`) ·
`results.json` (52 checks; S, D₂, d-minpolys, exact λ tables) ·
this draft. Not banked; no docs/log updates yet (frontier draft only).
