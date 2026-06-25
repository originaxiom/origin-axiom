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
the classical level cannot. The monodromy generators **`⟨R,L⟩` surject onto all of `SL(2,𝔽₅)`** mod 5 (BFS
closure = 120 — the genuine shadow is the *whole* `2I`; a *single* element `RL=[[2,1],[1,1]]` generates only a
cyclic order-10 piece, which alone does **not** pin `2I`). **[all verified: surjection 120, orders 120/60,
center 2, 9 vs 5 conjugacy classes, sum-of-squares 120/60.]**

## Golden-specificity — corrected on re-audit (2026-06-25)

`SL(2,𝔽_p)` is binary-polyhedral (McKay/ADE) **only for `p ≤ 5`** (`p=3 → 2T = E₆`, `p=5 → 2I = E₈`; and `3`
never divides `m²+4`, B207). Reducing by the **field discriminant**, golden's disc `=5` gives the McKay-`E₈`
group `2I=SL(2,𝔽₅)`.

**This is NOT unique to golden** — two corrections to the original "only `m=1,4` / golden unique":
- The field is *exactly* `ℚ(√5)` (sqfree`(m²+4)=5`) for the **whole odd-index-Lucas family `m∈{1,4,11,29,76,…}`**,
  not just `{1,4}` (that was a `cap-m≤8` artifact — `m=11→125`, `m=29→845=5·13²` also give field `ℚ(√5)`).
- The `2I=SL(2,𝔽₅)` *shadow* appears for **every `m` with `5∣m²+4`** (`m≡±1 mod 5`, i.e. `{1,4,6,9,11,14,…}`),
  because `⟨R,L⟩=SL(2,ℤ)` surjects onto `SL(2,𝔽₅)` mod 5 for *any* `m` (the shadow group is a property of the
  modulus, not of the individual `m`).

The honest sharp statement: **golden is the *minimal / fundamental* member of the `ℚ(√5)`/`E₈` family** (the
figure-eight, smallest discriminant, the trace-3 root of the Markov tree) — the simplest mean whose field
discriminant is the McKay-`E₈` prime 5 — *not* the unique one. Silver/bronze differ (disc 8, 13) because their
*own* field discriminants are not McKay primes; but `m=4, 11, 29, …` share golden's `E₈` discriminant-shadow.

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
