# B218 — does metallic multiplicity select an emergent theory? Yes: golden, the unique anyon (Jones index)

**Date:** 2026-06-26. **Status:** the probe of the **interaction/multiplicity thesis** (the owner's recurring
question). **Answer: yes, decisively, at the quantum-dimension level** — among all metallic means, multiplicity
selects **golden** as the *unique* anyon-realizable one (the Fibonacci anyon). The deeper chain-level CFT is a
known result, **cited not reproduced** (my in-sandbox ED was inconclusive — flagged honestly). Firewall: standalone
quantum-algebra; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V221**.

## The selection (exact)

A single non-trivial anyon of quantum dimension `d` is realizable as a **unitary** anyon theory iff
`d = 2cos(π/p)` (`d<2`, the quantized **Jones index** `d²<4`) or `d≥2` (the non-quantized continuum,
non-unitary). The metallic means carry `d = λ_m = (m+√(m²+4))/2`:

```
  λ_m < 2  (an allowed quantized anyon dimension)   ⇔   m = 1  (golden).
  λ_1 = 2cos(π/5) = φ   EXACTLY   →   the FIBONACCI anyon  (SU(2)_3, the dual-McKay E₈ point).
  λ_m ≥ 1+√2 > 2  for all m ≥ 2   →   ABOVE the Jones index-4 wall (no finite unitary anyon).
```

So **multiplicity selects golden** as the unique metallic mean whose units carry an anyon theory — the same
distinguished mean as the dual-McKay (B206/B210: golden = Fibonacci/SU(2)₃ = the E₈ point), now seen as the
*unique anyon-realizable* one in the family. This is the precise content of the "d>2 wall" the multiplicity
research flagged.

## The chain-level CFT (CITED, not reproduced — honest)

The golden **anyon chain** (many Fibonacci anyons) flows to a specific emergent CFT — **tricritical Ising
`c=7/10`** (AFM) / **3-state Potts `c=4/5`** (FM) — Feiguin–Trebst–Ludwig–Troyer–Kitaev–Wang–Freedman, PRL 98,
160409 (2007). So golden multiplicity selects a *specific* CFT. **Honest note (verify-don't-trust):** my own
in-sandbox ED did **not** reproduce `c=7/10` — a first anyon-chain Hamiltonian was buggy (gave a *gapped*
artifact, `c≈0`, constant entanglement), and the XXZ proxy at `Δ=λ_m/2` could not resolve the near-critical Néel
gaps at `L≤16` (`Δ=1.207` for silver sits too close to the critical `Δ=1`). So `c=7/10` is **cited**, not banked
from my computation; the chain-level confirmation is a flagged in-sandbox limitation.

## The honest limit of the thesis (firewall)

What multiplicity *selects* is a **dimensionless topological / CFT structure** — an anyon theory, a central charge
— **not** physical content with a scale. Chiral fermions / the Standard-Model content are **theorem-blocked**
(Nielsen–Ninomiya). So the "content from multiplicity" thesis resolves, on this object, to: **interaction selects
a specific topological theory** (golden / Fibonacci / tricritical-Ising) — a genuine positive answer — **but it is
structure, not scale or SM-content**, consistent with the firewall banked across the whole program.

## Honest status / tiers
- the Jones-index selection (`λ_m<2 ⇔ m=1`; `λ_1=2cos(π/5)`): **`[exact]`** (elementary, testable).
- the golden-chain CFT `c=7/10`: **`[cited]`** (Feiguin 2007); my in-sandbox ED **inconclusive** (flagged).
- the firewall framing: structural, firewall-clean. Novelty UNCHECKED (Jones index + golden chain classical; the
  application to the metallic family / the selection framing is the contribution).

## Reproduction
- `python jones_selection.py` — the exact Jones-index selection + the cited chain CFT. (pyenv)
- `tests/test_b218_metallic_anyon_selection.py` — 3 locks (the selection is load-bearing; the CFT is cited).

## Net (the multiplicity thesis, resolved on this object)
Interaction/multiplicity of the metallic units **does** select — uniquely golden, the Fibonacci anyon, flowing
(known) to the tricritical Ising CFT — but what it selects is a **dimensionless topological structure**, not
physical content. This is the most positive honest answer the object supports for the thesis: *selected topology,
not emergent scale.* (Tie-in: golden's uniqueness here = the dual-McKay E₈ point, B206/B210.)
