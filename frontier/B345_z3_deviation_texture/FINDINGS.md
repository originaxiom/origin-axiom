# B345 — the ℤ/3-graded texture of the deviation space: a forced charge-conservation selection rule

**Status: banked (frontier) as a forced dimensionless TEXTURE (form, like B326 — not a value). Target 2 of the
deviation-structure strategy. Firewalled; nothing to `CLAIMS.md`.**

## The forced texture
The trace-map deviation modes at the symmetric centre `(0,0,0)` are the ℤ/3 eigenvectors, carrying **ℤ/3 charges
`{0,1,2}`** (eigenvalues `{1, ω, ω²}`); the charge-0 (invariant) direction is `(1,−1,1)`. A ℤ/3-invariant coupling of
deviations **conserves charge mod 3**, so a quadratic (mass-matrix-type) coupling `deviationᵢ × deviationⱼ` is nonzero
**only when `chargeᵢ + chargeⱼ ≡ 0 (mod 3)`**:

- **allowed:** `{(0,0), (1,2), (2,1)}` — the **anti-diagonal** texture;
- **forbidden:** `{(0,1), (0,2), (1,1), (2,2)}`.

This *is* the **ω-circulant / democratic structure** (B324) read as a deviation **selection rule**; the **irreducibility**
(B343) is why the charge-`{1,2}` sector has no further invariant sub-line. It is a *texture* (which couplings vanish), a
form — no magnitude.

## Honest cross-check (a genuine finding)
The **B265 exponent split** — `{4,8}` (escape E₆, "gauge") vs `{5,7,11}` (trapped in F₄, "matter") — does **not** align
with the ℤ/3 charge (both sets are `{1,2}` mod 3). So the deviation space carries **two independent structures**: the
ℤ/3 charge grading (this probe) *and* the E₆-exponent grading (B265). They are not one texture — which sharpens the
picture (and is a live input for Target 3, the cross-sector question).

## Tier (honest)
The charge-conservation selection rule is **generic to any ℤ/3**; what is **object-specific** is that the trace-map
tangent action *realises* the ℤ/3 (the deviation modes **are** the charges, B343), with charge-0 `= (1,−1,1)`. Form, not
value. Nothing to `CLAIMS.md`.

## The fence
Exact ℤ/3 eigen-decomposition of the trace-map Jacobian at the centre + the charge-conservation combinatorics (sympy). No
physics values. Nothing to `CLAIMS.md`.

`z3_deviation_texture.py` (pyenv) · `tests/test_b345_z3_deviation_texture.py`. Related: **B324** (the ω-circulant),
**B343** (irreducibility), **B326** (texture-not-magnitude), **B265** (the independent exponent split), **B344** (the
symplectic pairing). Lit: standard ℤ/3-graded selection rules (flavor model-building).
