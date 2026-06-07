# B118 — the θ=−w₀ fixed-root sign (Chat-2 Path 1, the gate)

Computes the sign `θ=−w₀` carries on B112's lone fixed root (odd `m=n−h`) — the one that tips the `(⌈,⌊)`
multiplicity split. B112 *assumed* it was `+1`; Path 1 asked whether it is `+1` for all `(n,h)` (which would make
B64 a uniform "`+1` sector = `char(M^h)`" theorem). **It is not:** the genuine *signed* contragredient involution
gives **`(−1)^{h+1}`** — a refinement/correction of B112, tied to the inversion identity. NO physics; no
`CLAIMS.md`; the `ρ_n` proof stays the prize; P1–P16 untouched.

- **`probe.py`**
  - **`tau()` / `is_involution_and_reversal()`** — `θ=−w₀` as the contragredient involution `τ(X)=−J Xᵀ J⁻¹`
    (standard antidiagonal form); `τ²=id` and acts as B112's reversal (now signed).
  - **`sign_closed_form()`** — the headline: the fixed-root sign **`= (−1)^{h+1}`** (symbolic ε-form residual `0`;
    numeric, all `n≤12`).
  - **`sign_is_not_uniform_plus_one()`** — the correction: NOT a uniform `+1` (`+1` for odd `h`, `−1` for even
    `h`); the `(⌈,⌊)` dimensions are untouched, only the geometric sign is refined.
  - **`inversion_identity()` / `sign_matches_inversion_parity()`** — the emergent **non-circular** link: the
    fixed-root sign `= +1` ⟺ `char(M^{−h})=char(−M^h)` ⟺ `h` odd (`M⁻¹∼−M`, `det=−1`).
  - **`fixed_root_in_char_Mh_tower()`** — B112's `char(M^h)=⌈` labeling, tower-verified `n≤5` (B118 supplies the
    all-`n` *sign*, not an independent all-`n` labeling proof).
- **`FINDINGS.md`** — the derivation, the correction, and the honest scope.

**Result.** The fixed-root sign is the closed form **`(−1)^{h+1}`** (proved all `n`) — **not** the uniform `+1` the
handoff anticipated. So B64's "`+1` sector = `char(M^h)`" holds only for odd `h`; the labeling tracks the h-parity
/ inversion identity. B112's `(⌈,⌊)` dimensions stand; its `char(M^h)=⌈` labeling stays tower-verified `n≤5`.
**Honest scope (B116/B117):** this is the θ-split, **not the tower** (the Sym two-sequence, diverges `n≥6`).

```bash
python frontier/B118_theta_fixed_root_sign/probe.py
python -m pytest tests/test_b118_theta_fixed_root_sign.py -q
```
No physics claim; the `ρ_n` catalog proof stays the central target; proven core P1–P16 untouched.
