# B208 — the WRT period and the congruence shadow are the same arithmetic

**Date:** 2026-06-25. **Status:** unifies B204 (the WRT level-period, Face IV) and B206 (the congruence
shadow, Face I) — they are not two threads but **two reads of one homological invariant**, `det(γ+I)=m²+4`.
Firewall-clean arithmetic; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V207**.

## The connection

For `γ = RᵐLᵐ = [[1+m², m],[m,1]]`, `det(γ+I) = m²+4`. Both banked threads read from it:
- **B204 (quantum, Face IV):** the WRT level-period `P(m) = m·(m²+4)/gcd(m²+4,4)` — built from `m²+4`.
- **B206 (arithmetic, Face I):** the congruence shadow is `SL(2, p)` at the ramified primes of the field
  `ℚ(√(m²+4))`; the field radicand is `squarefree(m²+4)`.

**Verified:** `squarefree(m²+4)` (the field radicand) **always divides `P(m)`** (checked m=1..300). So the
WRT period *contains* the field radicand — the quantum invariant and the arithmetic shadow are governed by the
same number `m²+4`.

## The golden collapse

At `m=1`, `m²+4 = 5` is prime — so it is simultaneously the period, the discriminant, and the McKay prime:

$$P(1) = 5 \;=\; \det(\gamma+I) = 5 \;=\; \mathrm{disc}\,\mathbb{Q}(\sqrt5) = 5 \;=\; \text{the McKay prime},\ \mathrm{SL}(2,\mathbb{F}_5)=2I=E_8.$$

The three "5"s are the same 5. The quantum period (Face IV) and the arithmetic shadow `2I=E₈` (Face I) are not
a coincidence of two threads — they are the single number `5`, for the single reason that `det(γ+I)=5` at the
golden point. For silver (m=2): `m²+4=8`, radicand 2, `SL(2,𝔽₂)=S₃` (degenerate); for bronze (m=3): `13`,
`SL(2,𝔽₁₃)` (generic simple). Golden is the unique point where `det(γ+I)` is the McKay-E₈ prime.

## Honest status
A verified connection between two banked results (B204, B206), firewall-clean; the contribution is the
unification (period and shadow = same `m²+4`; golden collapse to 5). Standalone arithmetic / quantum-topology;
nothing to `CLAIMS.md`.

## Reproduction
- `python period_congruence.py` — the table + `radicand | period` (m=1..200) + the golden collapse.
- `tests/test_b208_period_congruence_unification.py` — 3 locks. 3 passed.
