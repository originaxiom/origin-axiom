# B118 — the θ=−w₀ fixed-root sign: the closed form `(−1)^{h+1}` (NOT the anticipated uniform +1)

**Chat-2 Path 1 (the gate).** B112 proved the `(+1,−1)` eigenspace **dimensions** of `θ=−w₀` on the height-`h`
roots of `A_{n−1}` are `(⌈(n−h)/2⌉, ⌊(n−h)/2⌋)` — but by a **permutation** argument (no signs). For odd `m=n−h`
there is exactly one θ-fixed root (the middle, `i=(n−h+1)/2`); the 2-cycles each contribute one `(+1)` and one
`(−1)` eigenvector regardless, so the whole `⌈`-vs-`⌊` tip is decided by the sign θ carries on that lone fixed
root. B112 *assumed* it ("the central fixed root sits in the +1 sector"). **Path 1 asked: is that sign `+1` for all
`(n,h)`** — which would make B64 a uniform "`+1` sector = `char(M^h)`" theorem. This probe computes it from the
genuine *signed* contragredient involution — **and the answer is NOT a uniform +1.** No physics; nothing to
`CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

## The computation (genuine, signed — not the bare permutation)

Realize `θ=−w₀` as the contragredient algebra involution on `sl(n)`:
```
   τ(X) = −J Xᵀ J⁻¹,   J_{p,q} = ε_p δ_{q,n+1−p},  ε_p = (−1)^{p+1}   (the standard antidiagonal so/sp form).
```
`τ²=id`, and τ acts on the height-`h` roots **exactly as B112's reversal** (verified). A direct index computation:
```
   τ(E_{i,i+h}) = −ε_{n+1−i} ε_{n+1−i−h} · E_{n+1−i−h, n+1−i}     (image index = the reversal σ(i)),
```
and on the lone fixed root (`n+1−i−h = i`) this is the **scalar**
```
   τ(E_{i,i+h}) = −ε_{i+h} ε_i · E_{i,i+h} = −(−1)^{(i+h+1)+(i+1)} E_{i,i+h} = (−1)^{h+1} E_{i,i+h}.
```

> **FIXED-ROOT SIGN`(n,h) = (−1)^{h+1}`** — independent of `n`; **proved symbolically** (the ε-form residual is
> exactly `0`) and **verified numerically for all `n ≤ 12`** (e.g. `(4,1)→+1, (5,2)→−1, (6,3)→+1`).

## The finding — a refinement/correction of B112 (verify-don't-trust)

The sign is `(−1)^{h+1}`, **not** the uniform `+1` the handoff anticipated: **`+1` for odd `h`, `−1` for even `h`**.
So the genuine *signed* θ does **not** place the fixed root in the `+1` (symmetric) sector for all `h` — B112's
unsigned-permutation reading ("the fixed root is always `+1`") is right only for odd `h`. The fixed root tracks the
**h-parity**, not a uniform sign. The `(⌈,⌊)` **dimensions** (B112) are untouched (they come from the permutation
cycle structure); what is refined is the geometric **sign** on the lone fixed root.

## What this does (and does not) settle for the labeling (B64)

B112's labeling `char(M^h) = ⌈` (the larger sector, including the fixed root) is **tower-verified for `n≤5`** (exact
`n≤4` + B61/B62 at `n=5`); the fixed root sits in `char(M^h)=⌈` in every count-distinguishing tower case `n≤6`
(cross-checked). **B118 supplies the precise all-`n` geometric sign `(−1)^{h+1}`** and identifies it with the
inversion parity (below); it does **not** independently prove the `char(M^h)` labeling for `n≥6` — that is the same
**V25 gap**, and B117 shows the tower is the Sym two-sequence anyway (the θ-split **diverges** at `n≥6`, B116). So
Path 1 returns a **closed-form sign + a correction**, not a uniform-`+1` theorem.

## Emergent (chased inline) — the sign IS the inversion/det identity (a non-circular link)

For `2×2` `det=−1` monodromy, `M⁻¹ ∼ −M`, so `char(M^{−h}) = char(−M^h)` precisely for **odd `h`** (independently
computed from the polynomials; fails for even `h`). The fixed-root sign is `+1` **exactly for odd `h`** — the same
parity. So
```
   fixed-root sign = +1   ⟺   the inversion identity char(M^{−h})=char(−M^h) holds   ⟺   h odd,
```
verified for all `(n,h)`: the geometric eigenvalue and the polynomial identity are **one fact** (`−w₀` inverts the
principal torus).

## Honest scope (B116/B117)

This is the **θ-split** (the bare `−w₀` decomposition), **not the tower** — the tower is the Sym two-sequence
(B117), and the θ-split diverges from it at `n≥6` (B116). The all-`n` tower stays the open prize = **prove the Sym
two-sequence `μ_d`** (B103).

**Ledger:** V105. **Reuses:** `B112.closed_form`, `B58.sym_counts`.
