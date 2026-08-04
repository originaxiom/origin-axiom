# B880 — the module-level magic-square signature: the three sectors are pairwise-INEQUIVALENT so(8)-modules, each 8⁺⊕8⁻ under tri(ℂ)

cc banking seat, 2026-08-04. The computational half of the M(𝕆,ℂ) identification (B882 is the
bibliographic half). Mathematics scope; nothing to `CLAIMS.md`; Gate 5 untouched.

## 1. What the magic square requires, and what the build shows

M(𝕆,ℂ) = tri(𝕆) ⊕ tri(ℂ) ⊕ (𝕆⊗ℂ)₁ ⊕ (𝕆⊗ℂ)₂ ⊕ (𝕆⊗ℂ)₃ requires the three 16-dim summands to
carry the **three inequivalent triality frames** of so(8) = tri(𝕆), each an 8-pair split by the
tri(ℂ) = u(1)² charges. Computed on the B875 spaces (30 digits):

| quantity | result |
|---|---|
| so(8) = derived(core) | dim **28** exactly |
| each Vᵢ under a plane charge | splits **[8, 8]** (opposite charges) — the 𝕆⊗ℂ pair |
| **dim Hom_{so(8)}(Vᵢ, Vⱼ), i ≠ j** | **0, all six pairs** — certificates ≤ 4×10⁻²⁷ |
| dim Hom_{so(8)}(Vᵢ, Vᵢ) | **4, all three** — M₂ of an irreducible-8 pair, exactly |

Hom spaces by the certified generic-pair method (kernel of two random combinations of the 28
intertwining constraints; every candidate certified against all 28 generators — candidate ⊇
true always holds, the certificate gives ⊆, hence equality).

## 2. What this closes

**The tiling is M(𝕆,ℂ)-shaped at module level, on this build**: pairwise-inequivalent sectors
(the triality relativity — no so(8)-map connects any two frames), the correct pair structure in
each, the cyclic law (B875), the core type (B875), and the bibliographic identification (B882)
— the naming now stands on computation and literature simultaneously.

## 3. Honest boundaries

- Inequivalence is the module-level statement; the finer identification (which sector is
  vector/spinor/cospinor relative to a chosen so(8)-frame) is convention — triality makes the
  labels relative, which is the point.
- An explicit Barton–Sudbery basis isomorphism (structure constants matched generator-by-
  generator) would be the exact-arithmetic capstone — priced, queued behind the 27 build.

`tests/test_b880_signature.py`
