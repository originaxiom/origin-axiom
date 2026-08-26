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

## SCOPE

- **Not claimed:** novelty for the identity; that Fried's hypotheses hold for `ρ(m)`; that the
  functional equation holds; that residue 2 is closed.
