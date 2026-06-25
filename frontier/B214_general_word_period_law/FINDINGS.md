# B214 — the general-word WRT period law, its class-field refinement, and the Funar deflation

**Date:** 2026-06-26. **Status:** B204's metallic-diagonal period law extends to **arbitrary** hyperbolic words,
and the extension has a **class-field-theoretic refinement** (the period reads the conjugacy / ideal class, not
just the trace) — the genuinely new content. Along the way a tempting over-read ("content from interaction") is
**deflated** by computation, *and* a cross-chat claim ("the three words are all conjugate") is **refuted**:
verify-don't-trust on both. Firewall: standalone quantum-topology / arithmetic; **nothing to `CLAIMS.md`; P1–P16
untouched.** Ledger **V217**.

## (1) The general-word period law (extends B204)

For a hyperbolic word `γ = ∏ R^{aᵢ}L^{bᵢ} ∈ SL(2,ℤ)`, `Z_k(T_γ) = tr(ρ_k(γ))` is Jeffrey's (1992) WRT invariant
of the Sol mapping torus `T_γ` — a **conjugacy-class invariant** of `γ`. Its level-period is, **on the principal
class**,
```
  P(γ) = lcm( det(γ−I), det(γ+I) ) = lcm( tr(γ)−2, tr(γ)+2 ).
```
Verified on words of distinct trace, including **non-symmetric** ones (`tr=5→21`, `8→30`, `7→45`, `14→48`,
`10→24`, `13→165`, `15→221`, `20→198`, …). For a single block this is `lcm(ab, 4+ab)`, which equals B204's
`lcm(a,b)(4+ab)/gcd(4+ab,4)` on the principal class — so B204 is the metallic-diagonal special case.

## (2) The class-field refinement (the new content)

The period is a **conjugacy-class invariant**, and the SL(2,ℤ) conjugacy classes of trace `t` are the **ideal
classes of the order `ℤ[λ]` of discriminant `D=t²−4`** (Latimer–Macduffee; the repo's **B92**). Computing the
period *per class*:

- **At a FUNDAMENTAL discriminant (conductor `f=1`): every class has the same period `= lcm(det±)`.** E.g. `t=5`
  (D=21): both classes → 21. `t=15` (D=221): both classes → 221.
- **At conductor `f>1`: the period SPLITS across classes** — non-principal classes have period `lcm/d` with
  `d | f`:

| t | D=t²−4 | conductor f | periods across classes |
|---|---|---|---|
| 5 | 21 | 1 | {21, 21} — no split |
| 6 | 32 | 2 | {8, **4**} — split by 2 |
| 7 | 45 | 3 | {45, **15**} — split by 3 |
| 18 | 320 | 8 | {80, **40**} — split by 2 |
| 15 | 221 | 1 | {221, 221} — no split |

So the period reads the **form class / conductor**, not just the discriminant — a class-field-theoretic refinement
of B204 (which lived on the metallic diagonal `m≤3`, where `h=1` and the split is invisible). **The exact split
divisor `d|f` per class is the open question** — a candidate "class-field period law".

## (3) The deflation — `|Z|`-equality is *Funar*, not "interaction" and not "all conjugate"

Three two-block words `[(1,1),(2,2)]`, `[(1,2),(2,1)]`, `[(2,1),(1,2)]` (matrices `M₀,M₁,M₂`, all trace 15) give
**identical `|Z(k)|` at every level**. The honest reading, both prior framings corrected by computation:

- The earlier **"content from interaction / Penrose"** read (mine) is **wrong**: identical `|Z|` for the *same*
  monodromy is the *definition* of a topological invariant, not a discovery.
- The relayed claim **"the three are all conjugate ⇒ it's just Jeffrey's theorem"** is **also wrong**: by orbit
  reduction, `M₁ ~ M₂` are conjugate (so *their* shared `|Z|` is Jeffrey), but **`M₀` is NOT conjugate to them**
  (a different class) — yet has the identical `|Z|` and period 221. That is **Funar's phenomenon** (arXiv:1101.0509:
  non-conjugate Sol bundles with identical WRT; same-WRT ⟹ commensurable, *not* homeomorphic). So
  **`|Z|`-equality ≠ conjugacy.**

The genuine, bankable content is therefore the **formula (1)** and the **conductor-split (2)** — not any
"interaction" reading. (`(RL)²` and `R⁵L`, both trace 7, are likewise non-conjugate — different classes, periods
15 vs 45.)

## Honest status / tiers
- (1) the principal-class formula `P=lcm(det(γ−I),det(γ+I))`: **`[num, strongly verified]`** (many words; the
  qualitative periodicity is Jeffrey-proved, the closed value is verified, not yet `[proved]` for all words).
- (2) the conductor-split: **`[num]`** (clean on D=21,32,45,221,320; the exact divisor `d|f` per class = OPEN).
- (3) the conjugacy / Funar facts: **`[exact]`** (integer orbit reduction).
- Novelty UNCHECKED: the WRT-of-torus-bundle = Gauss sum is Jeffrey (known); Funar non-distinguishing is known;
  the **conductor-split closed form** is the candidate-new piece (do not claim — prior-art unrun).

## Reproduction
- `python period_law.py` — the law, the conductor-split, the conjugacy/Funar facts. (pyenv)
- `tests/test_b214_general_word_period_law.py` — 4 locks (the lcm formula + the conductor-split + the Funar
  deflation are load-bearing). All pass.

## Next (the real target, per the corrected strategy)
The **class-field period law**: the exact split divisor `d|f` as a function of the ideal class (B92). And the
**Borromean-surgery bridge** (L31): different classes = different (non-conjugate) filling slopes on the Borromean
parent — does the surgery-coefficient structure reproduce the conductor-split? (Note the Funar caveat: at
fundamental `D` the period does *not* separate classes, so the surgery signal lives at conductor `f>1`.)
