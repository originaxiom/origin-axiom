# B227 / L45 — the metallic SUSY chains have explicit Seifert 3-manifold duals (largest cone order = the metallic discriminant)

**Date:** 2026-06-26. **Status:** L45, the concrete lead that emerged from the L43 scout (B226). B224 showed the
metallic chains flow to unitary minimal models `M(m²+4, m²+3)`; this gives each one an explicit **Seifert
3-manifold dual** via the verified Gang–Kang–Kim 3d-3d recipe, and finds a clean arithmetic pattern. Firewall:
the Seifert/`H₁`/Euler bookkeeping + the cited recipe are firewall-clean math; the 3d-3d *reading* is firewalled
in `speculations/S040`. **Nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V230**.

## The construction (recipe verified from arXiv:2405.16377)

`M(P,Q) ↔` Seifert `S²((P, P−R), (Q, S), (3,1))` with `PS−QR=1` (`(R,S)` mod `ℤ(P,Q)`). For the metallic family
`P = m²+4` (= the **metallic discriminant**), `Q = m²+3 = P−1`, the condition `PS−QR=1` is solved by **`(R,S)=(1,1)`
for all `m`** (since `P−Q=1`). So

```
   metallic chain m  →  M(m²+4, m²+3)  →  Seifert  S²((m²+4, m²+3), (m²+3, 1), (3,1)).
```

**Verified:** `m=1` reproduces the paper's TCI Seifert `S²((5,−1),(4,5),(3,1))` — the same 3-manifold (the two
`(R,S)` differ by `(P,Q)`, the same class; `|H₁|=83` in both presentations).

## The family and its pattern

| m | minimal model | cone orders | \|H₁\| | Euler number e |
|--:|:--|:--|--:|:--|
| 1 (golden/TCI) | M(5,4) | (5, 4, 3) | 83 | −83/60 |
| 2 (silver) | M(8,7) | (8, 7, 3) | 227 | −227/168 |
| 3 (bronze) | M(13,12) | (13, 12, 3) | 627 | −209/156 |
| 4 | M(20,19) | (20, 19, 3) | 1523 | −1523/1140 |
| 5 | M(29,28) | (29, 28, 3) | 3251 | −3251/2436 |

- **Cone orders `(m²+4, m²+3, 3)`** — the base orbifold is `S²(m²+4, m²+3, 3)`, and the **largest cone-point
  order is the metallic discriminant `m²+4`** (the sequence 5, 8, 13, 20, 29, 40, 53, …). Golden (`m=1`) =
  `S²(5,4,3)`.
- **`|H₁| = 4m⁴ + 28m² + 51 = (2m²+7)² + 2 = (2P−1)² + 2`** — a clean quartic; `H₁` is finite (`b₁=0`).
- **Euler number** `e = −|H₁| / (3·P·Q)` (so `|H₁| = α₁α₂α₃·|e|`, the standard relation — a consistency check).
- All base orbifolds are **hyperbolic** (`1/(m²+4)+1/(m²+3)+1/3 < 1`) → `SL₂~` / **non-hyperbolic** 3-manifolds,
  consistent with B226 (minimal models come from non-hyperbolic 3-manifolds).

So the metallic SUSY chains pick out the **subfamily of unitary-minimal-model Seifert spaces whose largest cone
order is a metallic discriminant** — tying B224 concretely to the active Gang et al. 3d-3d minimal-model program.

## Honest status / tiers
- the recipe application + the Seifert data + `|H₁|`/Euler invariants: **`[exact]`** (pyenv `fractions`; the
  `|H₁|` det formula cross-checked with sage-python Smith form; `m=1` validated against the published TCI).
- the recipe `M(P,Q)↔`Seifert: **`[cited]`** (Gang–Kang–Kim arXiv:2405.16377, verified real).
- the pattern (cone order = discriminant; quartic `|H₁|`): a **clean observation**, but it is the metallic
  *subfamily* of a general construction — not a deeper distinction. **Novelty UNCHECKED.**
- **Follow-on (not done):** B224's "golden is the UNIQUE superconformal one" becomes, in 3-manifold terms, "the
  golden Seifert `S²(5,4,3)` is the unique metallic one ALSO realized as a SUSY-minimal-model Seifert space" —
  needs the SUSY-minimal-model recipe (JHEP 01(2025)027 / JHEP 03(2026)066). A real next step.

## Reproduction
- `python metallic_seifert.py` (pyenv) — the family, the pattern, the TCI validation.
- `tests/test_b227_metallic_seifert_duals.py` — 4 exact locks.

## Net
Each metallic SUSY chain (B224) has an explicit Seifert-3-manifold dual `S²((m²+4, m²+3),(m²+3,1),(3,1))`, with
the metallic discriminant `m²+4` as the largest cone-point order and `|H₁|=(2m²+7)²+2`. A concrete bridge from the
repo's metallic/golden structure to the active 3d-3d minimal-model program. (`B224 → B226 → B227`; firewalled
reading `S040`; the SUSY-uniqueness-as-Seifert-overlap is the open follow-on.)
