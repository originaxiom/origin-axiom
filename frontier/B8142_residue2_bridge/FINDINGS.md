# B8142 — residue 2 reduced twice: the Sym-power Ruelle zeta factors over the twist family

**Arc dated:** 2026-08-26 · **Seat:** cc3 (audit) · **Lane:** MATHEMATICS.
**Gate 5:** no physical identification; no Standard-Model quantity appears.

## The identity

For `γ` of complex length `L = ℓ + iθ`, the holonomy has eigenvalues `e^{±L/2}`, so
`ρ(m) = Sym^{2m}ℂ²` has eigenvalues `e^{jL}`, `j = −m…m`. Since

```
    e^{jL} · e^{−sℓ}  =  e^{ijθ} · e^{−(s−j)ℓ}
```

the `j`-th eigenvalue contributes exactly the `σ_j`-twist evaluated at `s − j`. Hence

> **`R_{ρ(m)}(s) = ∏_{j=−m}^{m} R(s − j, σ_j)`**

**Verified on m004** for `m = 0,1,2,3,4` at `s > 2+m`, where every factor converges absolutely, to
`|diff| ≤ 5×10⁻¹⁸`. Three live controls mismatch: a truncated `j`-range (2.4e−02), a wrong twist
`σ_{2j}` (3.3e−02), a perturbed shift (1.2e−03).

**No novelty is claimed for the identity** — it is elementary eigenvalue algebra and very likely
classical. **The contribution is what it locates.**

## At Fried's point

```
R_{ρ(m)}(0) = R(0,σ₀) · ∏_{j=1..m} conj R(j,σ_j) · ∏_{j=1..m} R(−j,σ_j)
                        └── the GRAVITON's own factors ──┘   └── negative arguments ──┘
```

**The graviton's factors sit inside `R_{ρ(m)}(0)` explicitly.** If Fried applies to `ρ(m)` — whose
hypotheses (acyclic, orthogonal, cusped extension) **are not checked here** — then
`T_X(ρ(m))² = R_{ρ(m)}(0)`, and the graviton's factors sit inside the analytic torsion.

## Residue 2: reduced twice, not closed

| stage | the target |
|---|---|
| B8133 | relate the family at `0` to its values at the **positive** integers |
| **first reduction** | evaluate the family at the **negative** integers, `R(−j, σ_j)` |
| **second reduction** | **establish the functional equation** for `R(s,σ_k)` on m004 |

The second step follows because **`s ↔ 2−s` maps `2+j ↦ −j`**, and `R(2+j, σ_j)` **converges
absolutely** for `j ≥ 1`. So the reflected factors are images of arguments *above* the abscissa,
where everything is computable — and m004's scattering determinant is already known in closed form,
`φ(s) = Λ_K(s−1)/Λ_K(s)` with `φ(s)φ(2−s) = 1`.

> **The target moved from a vague cross-theorem wish to a single standard object with existing
> literature. That is the progress. Residue 2 is NOT closed.**

## ⚠ A control of mine that could not fail

I first wrote a control using `s+j` in place of `s−j`, expecting a mismatch. **It matched** — because
over the symmetric range `j = −m…m`, the substitution `j → −j` maps `{R(s−j,σ_j)}` onto itself. **`s+j`
is an identity, not an error; the control could never have failed.**

A control that tests a *symmetry* instead of the *claim* is vacuous. It is kept in the script,
**relabelled as a symmetry**, so the vacuity stays visible rather than being quietly deleted.


## The reflection formula that Fried + Pfaff jointly force

The identity gives `R_{ρ(m)}(0)/R_{ρ(m−1)}(0) = A_m·B_m` with `A_m = R(−m,σ_m)` and
`|B_m| = |R(m,σ_m)|`. Fried turns the left side into `[T_X(ρ(m))/T_X(ρ(m−1))]²`; Pfaff's ratio
evaluates that as `(c(m)/c(m−1))^κ · exp(−2m·vol/π) · |R(m,σ_m)|`. Squaring and cancelling `|B_m|`:

> **`|R(−m, σ_m)| = (c(m)/c(m−1))^{2κ} · exp(−4m·vol/π) · |R(m, σ_m)|`**

For m004 (`κ = 1`, banked `c(m)/c(2)` from B8104/B8112, `|R(m,σ_m)|` from `bridge.py`):

| `m` | `c(m)/c(m−1)` | `\|R(m,σ_m)\|` | `exp(−4m·vol/π)` | **`\|R(−m,σ_m)\|`** |
|---:|---|---|---|---|
| 3 | 0.7121142418 | 0.9687980563 | 4.292e−04 | **2.109e−04** |
| 4 | 0.7767739989 | 0.9852054775 | 3.238e−05 | **1.925e−05** |
| 5 | 0.8176395289 | 1.0052425571 | 2.442e−06 | **1.641e−06** |

Successive values decay by `≈ exp(−4·vol/π) = 0.0754` (observed 0.0913, 0.0853), and a control
confirms the suppression comes from the damping: removing it leaves O(1) values.

**This is the object residue 2 was missing** — a relation between the family at negative and
positive arguments, right-hand side absolutely convergent and already computed. **It is
CONDITIONAL** on Fried applying to `ρ(m)` in the cusped setting, which is **not verified here**. If
Fried applies, the reflection is *forced*; if not, this is an implication with an unchecked
antecedent. Either way it is **falsifiable**: an independent computation of `R` at a negative
integer confirms it or refutes the antecedent.

**Residue 2 is still not closed** — but it has moved from *a wish across three theorems* to
*verify one hypothesis, and the formula follows*.

## ⚠ A second instrument slip, opposite in kind

The smallness check was written `all(v < 1e-4)`. **That threshold was tuned to the two data points
then available** and broke the moment `m = 3` was added (2.1e−04). Fitting a check to the sample
rather than to the claim is the same failure as a control that cannot fail, pointed the other way.
Replaced by the claim the derivation actually makes — decay by `exp(−4·vol/π)`. An earlier version
also excluded `m = 3` needlessly, having forgotten `c(2)/c(2) = 1`.

## SCOPE

- **Not claimed:** novelty for the identity; that Fried's hypotheses hold for `ρ(m)`; that the
  functional equation holds; that residue 2 is closed.
