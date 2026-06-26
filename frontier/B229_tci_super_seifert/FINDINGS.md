# B229 — the TCI's two 3d-3d bulk realizations are DIFFERENT 3-manifolds (one CFT, two bulks)

**Date:** 2026-06-26. **Status:** the L45 residual completed — the explicit **super-Seifert** realization of the
tricritical Ising, and the 3-manifold form of B228. B228 showed (at the coset level) that the TCI/golden is the
unique metallic chain that is *both* an ordinary and an N=1 super minimal model. This computes the explicit
3-manifold (Seifert) duals and finds they are **distinct 3-manifolds**. Firewall: Seifert/`H₁` bookkeeping + cited
recipes = firewall-clean; the 3d-3d reading is firewalled in `speculations/S040`. **Nothing to `CLAIMS.md`;
P1–P16 untouched.** Ledger **V232**.

## The two recipes (the determinant = the SU(2) level)

Both 3d-3d recipes have the *same* Seifert form `S²((P,P−R),(Q,S),(3,1))`, differing only by the determinant —
which is the SU(2) level used in the GKO coset:

```
   ORDINARY  M(P,Q):   PS − QR = 1      (SU(2)₁;  Gang–Kang–Kim, arXiv:2405.16377)
   SUPER     SM(P,Q):  PS − QR = 2      (SU(2)₂;  Baek–Kang, arXiv:2511.04524)
```

## The tricritical Ising, two labels → two bulk 3-manifolds

| | label | `c` | Seifert | cone orders | base orbifold | `\|H₁\|` |
|---|---|---|---|---|---|---|
| ordinary | M(4,5) | 7/10 | `S²((5,4),(4,1),(3,1))` | (5,4,3) | **S²(3,4,5)** | **83** |
| super | SM(3,5) | 7/10 | `S²((5,4),(3,1),(3,1))` | (5,3,3) | **S²(3,3,5)** | **66** |

Same boundary CFT (`c=7/10`, and B228: the cosets literally coincide), but **different bulk 3-manifold** — the
base orbifolds differ (`S²(3,4,5)` vs `S²(3,3,5)`) and so does `|H₁|` (83 vs 66). So:

> **One CFT (golden/TCI), two distinct bulk 3-manifolds** — distinguished by the SU(2)₁-vs-SU(2)₂ (determinant
> 1-vs-2) structure. The coset coincidence (B228) does **not** lift to a 3-manifold coincidence.

And **only golden is both**: the metallic ordinary models `M(m²+3, m²+4)` have `|P−Q|=1`, while the unitary super
series `SM(p, p+2)` has `|P−Q|=2`; the unique overlap is the TCI `= M(4,5) = SM(3,5)` (the `5` — the golden
discriminant — is shared by both labels).

## Honest status / tiers
- the ordinary TCI Seifert (`S²(3,4,5)`, `|H₁|=83`): **`[verified]`** (B227 reproduces the published TCI example).
- TCI `= SM(3,5)`: **`[verified]`** (the super central-charge formula `c=3/2(1−2(p'−p)²/(pp'))`, arXiv:2405.05746).
- the super recipe `PS−QR=2` + Seifert form: **`[cited]`** — a *verbatim abstract* quote (arXiv:2511.04524), a
  minor variant of the fully-verified ordinary recipe; the cone orders `(P,Q,3)` follow from the recipe form.
- the super TCI Seifert (`S²(3,3,5)`, `|H₁|=66`): **`[computed]`** from the cited recipe — **not** independently
  anchored against a *published worked super example* (the paper's HTML was unavailable). Flagged. (The conclusion
  "different base orbifold" is robust: it needs only the cone orders `(P,Q,3)`, which the recipe form fixes.)
- novelty of the "one CFT, two bulks" framing UNCHECKED.

## Reproduction
- `python super_seifert.py` (pyenv) — both recipes, the TCI comparison, the central-charge verification.
- `tests/test_b229_tci_super_seifert.py` — 5 exact locks.

## Net
The TCI/golden has two distinct 3d-3d bulk realizations: the ordinary one on the Seifert space over `S²(3,4,5)`
(`|H₁|=83`) and the super one on the Seifert space over `S²(3,3,5)` (`|H₁|=66`). Same CFT (B228), different bulk —
the SU(2)₁-vs-SU(2)₂ recipe determinant (1 vs 2) is the discriminating structure. Golden is the unique metallic
chain with both realizations. This completes the L45 thread. (`B224 → B227 → B228 → B229`; firewalled reading
`S040`.)
