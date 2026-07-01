# B339 / H107 — the CS-flow sub-leading coefficient is rational (`1/24 = 1/(2·h(E₆))`), not √−3

**Status: banked (frontier). Tier-1 (flow interior) of the CP/mixing sweep. Firewalled; nothing to `CLAIMS.md`.** The
Dehn-filling flow `CS(1,n) ~ −1/(2n)` (B338) is the chiral order parameter. H107 asked whether its **sub-leading** term
carries a `√3`/`ℚ(√−3)` signature (B290 found the *core-length* `1/n²` coefficient `= π/√3 = 2π/|τ|`). It does not — a
clean negative plus a rational law.

## Result
`CS(1,n) = −1/(2n) + 1/(24 n³) + O(1/n⁵)`.
- **`c₂ = 0` — a theorem, not a fit.** The CP sign law `CS(1,−n) = −CS(1,n)` (B289, amphichirality) makes `CS` **odd** in
  `n`: writing `CS = Σ aₖ/nᵏ`, oddness forces `aₖ(−1)ᵏ = −aₖ`, so **`aₖ = 0` for every even `k`** (`c₂ = c₄ = … = 0`).
- **`c₃ = 1/24` — rational.** Fitted `c₃·24 = 0.99993` over 135 fillings (`n = 6..140`). And `1/24 = 1/(2·|τ|²) =
  1/(2·h(E₆))`, since the cusp shape is `2√3·i`, `|τ|² = 12 = h(E₆)` (B302/B290). Rational → **no `√3`, no `ℚ(√−3)`**.

## Reading (firewall held)
The chiral flow's sub-leading arithmetic is **rational**, tied to the cusp modulus `12 = h(E₆)`, **not** to the
Eisenstein field. So the hoped-for `√−3` signature in the flow is **absent** — consistent with **B336** (the imaginary
seam `√−15` is not a geometric invariant the object reaches; the chiral sector's arithmetic is rational/`ℚ(√−3)`-generic).
A `[HOOK]`: the denominator `24 = 2·h(E₆)`. No value produced. Nothing to `CLAIMS.md`.

## The fence
SnapPy 3.3.2 CS of `m004(1,n)` (recorded 9-digit values + the live 135-point fit) + the amphichirality argument for
`c₂=0`. No physics values. Nothing to `CLAIMS.md`.

`cs_flow_subleading.py` (pyenv/SnapPy) · `tests/test_b339_cs_flow_subleading.py`. Related: **B338** (the flow
`CS~−1/(2n)`), **B289** (the CP sign law `CS(1,−n)=−CS(1,n)`), **B290** (the core-length `1/n²` coeff `π/√3`, `|τ|²=12`),
**B302** (`|τ|²=12=h(E₆)`), **B336** (`√−15` not reached). Lit: Neumann–Zagier (Dehn-surgery asymptotics of CS/volume).
