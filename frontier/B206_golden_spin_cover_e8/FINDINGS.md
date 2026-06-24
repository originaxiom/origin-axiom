# B206 — the golden object's spin shadow is 2I = SL(2,𝔽₅) = McKay-E₈

**Date:** 2026-06-25. **Status:** a verified structural connection — the classical/quantum (trace/spin)
divide of the golden metallic object is exactly `A₅ / 2I = PSL(2,𝔽₅) / SL(2,𝔽₅)`, the McKay realization of
affine `E₈`. Answers the "does the quantum level carry spinorial structure the classical can't?" seam
question: **yes, structurally** (not a φ-rhyme). Ledger **V203**. Firewall: McKay/representation-theoretic
`E₈`, **not** physics `E₈`; nothing to `CLAIMS.md`; P1–P16 untouched.

## The insight

The four faces (character variety / geodesic / quasicrystal / quantum) are shadows of one conjugacy class
`RᵐLᵐ ∈ SL(2,ℤ)`. Its **arithmetic shadow** mod the field discriminant is a finite group. For the **golden**
mean (`m=1`, field `ℚ(√5)`, disc 5) that group is

$$\mathrm{SL}(2,\mathbb{F}_5) \;=\; 2I \ (\text{binary icosahedral}) \;=\; \text{McKay partner of affine } E_8 .$$

| level | group | # irreps | dims |
|---|---|---|---|
| **classical / trace** (SO(3)) | `PSL(2,𝔽₅) = A₅` | **5** | 1,3,3,4,5 |
| **quantum / spin** (SU(2)) | `SL(2,𝔽₅) = 2I` | **9** | 1,2,2,3,3,4,4,5,6 (= affine `E₈` marks) |

The `ℤ/2` between them is the **center `{±I}`** = the spin cover SU(2)→SO(3) = the half-trace `κ=4·I_FV+2`
that recurred all session. The **4 extra irreps `{2,2,4,6}`** are spinorial — what the quantum level sees and
the classical level cannot. The golden monodromy `RL=[[2,1],[1,1]]` reduces mod 5 to an order-10 element of
`2I`. **[all verified: orders 120/60, center 2, 9 vs 5 conjugacy classes, sum-of-squares 120/60.]**

## Golden-specificity (the sharp part)

`SL(2,𝔽_p)` is a binary-polyhedral (McKay/ADE) group **only for `p ≤ 5`** (`p=3 → 2T = E₆`, `p=5 → 2I = E₈`).
Among metallic discriminants `m²+4`, the squarefree field is `5` **only** for `m=1` and `m=4` (the `ℚ(√5)` /
odd-index-Lucas family). So **the golden mean is the unique metallic mean whose spin shadow is the McKay-`E₈`
group** — which is *why* golden, and not silver/bronze, is the one tied to the icosahedron and `E₈`.

## Honest status

- **Solid:** the computation (verified above).
- **Standard ingredients:** `2I ≅ SL(2,𝔽₅)`, `A₅ ≅ PSL(2,𝔽₅)`, McKay `2I↔E₈`, congruence quotients of
  `SL(2,ℤ)`, the spin cover. The contribution is the **assembly** — the metallic monodromy's conductor-5
  shadow = McKay-`E₈`, golden-specific, realizing the classical/quantum = trace/spin = `A₅/2I` divide.
- **Novelty UNCHECKED:** the golden↔`E₈` link is even known in physics (Coldea et al. 2010, golden-ratio mass
  ratios / `E₈` in the Ising chain) and `2I↔E₈`/Fibonacci-anyon links exist; whether *this specific
  metallic-monodromy → conductor-5 → 2I framing* is recorded needs a prior-art pass (L26). **Do not claim
  novelty.**
- **Firewall (hard):** this `E₈` is the **McKay/representation-theoretic** `E₈` (the Dynkin/character graph of
  `2I`). It is **not** a claim that physics' `E₈` gauge group / heterotic string emerges — that bridge stays
  firewalled (the exact oversell the McKay handoff was deflated for).

## Reproduction
- `python golden_spin_cover.py` — orders, conjugacy classes, center, the spinorial count, the golden
  reduction, and the golden-specificity scan. ~1s.
- `tests/test_b206_golden_spin_cover_e8.py` (pyenv) — 4 locks. 4 passed.
