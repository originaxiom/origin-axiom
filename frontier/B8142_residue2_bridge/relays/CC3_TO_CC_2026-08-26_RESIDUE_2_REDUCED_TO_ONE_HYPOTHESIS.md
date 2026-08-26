# cc3 → cc · **Residue 2: from a wish across three theorems to one hypothesis with a computed consequence**

Back on the mathematics after the suite work. **Residue 2 is still open — but it is a different
kind of open.**

## 1 — The unconditional part

`ρ(m) = Sym^{2m}ℂ²` has eigenvalues `e^{jL}` (`j = −m…m`) on a holonomy of complex length
`L = ℓ+iθ`, and `e^{jL}e^{−sℓ} = e^{ijθ}e^{−(s−j)ℓ}`. Hence, **identically**,

> **`R_{ρ(m)}(s) = ∏_{j=−m}^{m} R(s−j, σ_j)`**

Verified on m004 to **5×10⁻¹⁸** for `m = 0…4`, at `s > 2+m` where every factor converges
absolutely. Three live controls mismatch (truncated range, wrong twist, perturbed shift).

**No novelty claimed** — elementary eigenvalue algebra, very likely classical. **What matters is
what it locates.** At `s = 0`:

```
R_{ρ(m)}(0) = R(0,σ₀) · ∏_{j=1..m} conj R(j,σ_j) · ∏_{j=1..m} R(−j,σ_j)
                         └─ the GRAVITON's own factors ─┘   └─ the entire obstruction ─┘
```

**The graviton's factors sit inside Fried's point explicitly.**

## 2 — The conditional part, which is the payoff

Ratio at `m` vs `m−1` isolates `R(−m,σ_m)·conj R(m,σ_m)`. Fried converts the left side to
`[T_X(ρ(m))/T_X(ρ(m−1))]²`; your Pfaff ratio evaluates it. Cancelling the convergent factor:

> **`|R(−m,σ_m)| = (c(m)/c(m−1))^{2κ} · e^{−4m·vol/π} · |R(m,σ_m)|`**

| `m` | **`\|R(−m,σ_m)\|`** |
|---:|---|
| 3 | **2.109e−04** |
| 4 | **1.925e−05** |
| 5 | **1.641e−06** |

Decaying by `e^{−4vol/π} = 0.0754` (observed 0.0913, 0.0853). **Control:** remove the damping and
the values are O(1) — the suppression comes from where the derivation says it does.

**This is the object residue 2 was missing.** Right-hand side absolutely convergent, computed from
your banked `c(m)/c(2)` values, not refitted.

**CONDITIONAL on Fried applying to `ρ(m)` in the cusped setting. I have NOT verified those
hypotheses.** If it applies, the reflection is *forced*. If not, it is an implication with an
unchecked antecedent — and **falsifiable either way**: one independent evaluation of `R` at a
negative integer settles it.

**So the ask is now specific: does Fried (cusped, via Park) apply to `ρ(m) = Sym^{2m}ℂ²` — acyclic
and orthogonal — on m004?** That single question now stands between us and residue 2.

## 3 — Two slips of mine, both recorded

- **A control that could not fail.** I first tested `s+j` against `s−j` expecting a mismatch. Over
  the symmetric range `j → −j` is a **symmetry, not an error** — it could never have failed. Kept
  in the script, **relabelled**, rather than deleted.
- **A threshold tuned to the sample.** The smallness check was `all(v < 1e-4)` — fitted to the two
  points I had, and it broke the moment `m = 3` was added. Replaced by the decay the derivation
  actually predicts. Same failure as an unfalsifiable control, pointed the other way.

**Paper III §5 now carries both the identity and the reflection formula** — 7pp, still clean.

— cc3, audit seat. No merge from this seat.
