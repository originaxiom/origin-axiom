# B93 — det=−1 is exactly the tower's parity (Paper 0, Phase C)

**Status: `proven` / `computer-assisted`.** Standalone number theory / Lie theory; no physics, no
Origin-core claim; proven core P1–P16 untouched. Script `probe.py`; test `tests/test_b93_det_parity_bridge.py`.

The bridge from the foundation (B92) to the tower: `det=−1` is not merely "the simplest slice" — it is
**structurally distinguished**, being exactly the condition that gives the trace-map tower its sign/parity
sectors.

## MyCalc-1 — `det=−1 ⟺ the parity sectors`
For a hyperbolic unimodular 2×2 `N`: `det N=−1 ⟺` eigenvalues `λ>1`, `−1/λ∈(−1,0)` (the small one
**negative**); `det N=+1 ⟺` both positive. The Dickson factor is `char(sign·Nᵏ)=t²−sign·tr(Nᵏ)t+det(N)ᵏ`;
the sign sector `char(−Nᵏ)` is the negative-rooted sector and requires the negative eigenvalue, i.e.
`det=−1`. So the tower's two-sheeted (CPT) structure is a `det=−1` phenomenon — verified per-eigenvalue,
and at the Jacobian level in **B94** (squaring the det=−1 tower to det=+1 removes every `char(−Nᵏ)` and
the `(t+1)` factor).

## MyCalc-4 — Galois vs parity (a clarification, refining the handoff's "Galois = C")
The metallic eigenvalues lie in `ℚ(√(m²+4))`. There are **two distinct ℤ/2 involutions**:
- **Parity / contragredient `P`:** `m→−m` (the diagram automorphism `−w₀`, B62/B64). `L_k(−m)=(−1)ᵏL_k`,
  so `P` permutes `char(Mᵏ)↔char(−Mᵏ)` for odd `k` — the tower's parity split.
- **Galois `g`:** `√(m²+4)→−√`, i.e. `λ↔−1/λ`. It **fixes** every `L_k=λᵏ+(−1/λ)ᵏ` (symmetric in the two
  roots), so it does **not** permute the `char(Mᵏ)` factors — it swaps the two *roots within* each factor
  (the meridian eigenvalue pair).
**So parity ≠ Galois:** the CPT/parity is the contragredient `m→−m`, not the field Galois action; Galois
is the within-factor charge-conjugation. (Handoff Idea-4 conflated them; this is the honest correction.)

## Scope (honest)
MyCalc-1 is the per-eigenvalue structural fact (exact); its Jacobian-level demonstration is B94. MyCalc-4
is an identification/clarification (`computer-assisted`, `k≤4`), not a derivation — and a refinement of a
speculative handoff lens, not a confirmation of it.

```bash
python frontier/B93_det_parity_bridge/probe.py
python -m pytest tests/test_b93_det_parity_bridge.py -q
```
No physics; proven core P1–P16 untouched; outreach dormant.
