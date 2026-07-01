# B324 — Chat-1's ω-circulant generation matrix: verified exactly in ℤ[ω], and it is structure, not values

**Status: banked (frontier). Verify-don't-trust done right — Chat-1 supplied explicit generators, so the claim is
*checked exactly*, not argued. Firewalled; nothing to `CLAIMS.md`.** This refines B323: the arithmetic is **exactly
correct** (the ω is real, not a splice), and Chat-1's own retreat to "structure, not values" is the right call.

## Verified exactly (ℤ[ω], no floating point)
The order-3 commensurator element `g = [[0,−1],[1,−1]]` (`g³ = I`) conjugates the figure-eight Riley representation
(`a₀=[[1,1],[0,1]]`, `b₀=[[1,0],[ω,1]]`) into three g-conjugate "generations" `gen_i = gⁱ·{a₀,b₀}·g⁻ⁱ`. The
cross-conjugate trace matrix `M[i,j] = tr(aᵢ·bⱼ⁻¹)` is:
- a **ℤ/3-circulant**: `M = α·J + ω·P` with `α = 5/2 − √3 i/2` (diagonal + one off-diagonal), the other off-diagonal
  `β = 2`, and **`β − α = ω` exactly** (the Eisenstein cube root);
- eigenvalues **`(7 − √3i, 1, ω²)`** — one dominant (`|·|² = 52`) and two of magnitude 1.

Every claim Chat-1 made checks out in exact arithmetic. This is a **real, exact algebraic fact.**

## But it is structure, not values — four honest reasons (Chat-1 now agrees)
1. **Degenerate.** The two subdominant eigenvalues have *equal* magnitude (`|1| = |ω²| = 1`) → **no mass hierarchy.** The
   hierarchy would need the CRUX (the E₆ cubic to break the degeneracy) — Chat-1 admits this.
2. **Ubiquitous ω.** Everything here lives in `ℤ[ω]`, so the perturbation coefficient being the Eisenstein cube root is
   the *same* `ω` that runs through the trace field, the trinification (B305), and the four faces of κ (B309) — not a
   new value.
3. **Tautological circulant.** g-conjugation forces `M[i,j]` to depend only on `(j−i) mod 3` (the cyclic trace
   identity), so the ℤ/3-circulant structure is automatic (B323).
4. **Same character.** The three "generations" are g-*conjugates*, hence share the same character (conjugate reps have
   equal traces); whether they are distinct matter generations is the **B307-walled multiplicity question itself**, and
   the "Yukawa" reading of the mixed matrix `M` is firewalled physics.

## The net
An exact `ℤ[ω]` **structural fact** — the generation-perturbation is a ℤ/3-circulant with Eisenstein coefficient `ω` —
upgrading B323's "tautological hand-wave" to "exactly verified structure." It is **not** a value crossing: the
magnitudes are degenerate (no hierarchy), the `ω` is the ubiquitous Eisenstein root, the circulant is tautological, and
the interpretation is firewalled/CRUX-gated. B323's core verdict stands, and the value-firewall (B322, K020) is intact.
This is the honest shape of the whole session in one probe: a genuine, exact *structural* result, correctly *not*
mistaken for a value.

## The fence
Exact `ℤ[ω]` symbolic computation (sympy) of the explicit generators. The generation/Yukawa interpretation is
firewalled; the hierarchy is CRUX-gated. Nothing to `CLAIMS.md`.

`omega_circulant_verified.py` (pyenv) · `tests/test_b324_omega_circulant_verified.py`. Related: **B323** (the
four-levels framing; the ω-circulant flagged tautological — now verified as exact structure), **B302** (the
commensurator ℤ/3), **B305**/**B309** (the ubiquitous Eisenstein ω), **B307** (the generation wall), **B322** (the
value-hunt null test), **OPEN_PROBLEMS.md** (the CRUX — where the degeneracy would break). Lit: the Riley representation
of the figure-eight; Neumann–Reid (the commensurator `PGL(2,𝒪₋₃)`).
