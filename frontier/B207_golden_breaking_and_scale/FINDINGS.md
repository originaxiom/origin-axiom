# B207 — the golden shadow's breaking lattice + the metallic scale-spectrum

**Date:** 2026-06-25. **Status:** firewall-clean MATH seeding the firewall-content push
(`speculations/S038`): two reproducible probes on the *content-side* questions — symmetry breaking and
scale — that the program had left firewalled. **No physics; nothing to `CLAIMS.md`; P1–P16 untouched.**
Ledger **V204**.

## Part 1 — symmetry breaking: the golden shadow's finite breaking lattice

The golden object's congruence shadow is `2I = SL(2,𝔽₅) = E₈` (B206). Symmetry breaking is `G→H`; computed
as pure finite-group structure:
- **`⟨RL⟩` (the metallic dynamics) is cyclic of order 10** (the 5-fold/icosahedral axis); its **normalizer in
  `2I` is the order-20 dicyclic `2D₅`** — the residual symmetry the dynamics selects.
- **`2I ⊃ 2T (=E₆)` but `2I ⊉ 2O (=E₇)`** — the icosahedral group has no octahedral subgroup (`A₅` has no
  `S₄`). So the golden shadow's finite McKay-breaking goes **`E₈ → E₆` directly, skipping `E₇`.**

**Firewall:** this is finite-group / McKay structure, **not** gauge symmetry breaking; the Lie chain
`E₈⊃E₇⊃E₆` and the finite containment `2I⊃2T` are different things (subgroup containment does not transfer
through McKay). The `E₇`-skip is a real fact about the *finite* shadow.

## Part 2 — scale: the metallic family's dimensionless scale-spectrum

The object is scale-free → no **absolute** scale (B151 stands). Its intrinsic **dimensionless** invariants:
regulator `log λ_m` (= geodesic length/4 = entropy), dilatation `λ_m²`, conformal dimension
`Δ_m=−(ln λ_m/π)²` (B196), WRT period `P(m)` (B204). Hierarchy diagnostics (`m=1..12`):
- regulator `~ 0.91·log(m)` — **logarithmic growth**; consecutive ratio → 1; max/min ≈ 5.2 (O(1)).
- **No intrinsic exponential hierarchy.** So any large hierarchy must come from the quantization **level `N`**
  (volume conjecture `~e^{N·entropy}`) — from quantization, *not* the object's geometry. The firewall holds,
  and this **locates** where a hierarchy would enter (the level, with rate set by the entropy/volume).
- **Golden has the smallest regulator (`log φ`)** → the *least-hierarchical* / extremal point (the same
  extremality that makes it dynamically minimal and arithmetically exceptional — cf. B206).

## Firewall
Finite-group structure + dimensionless invariants only. No scale, no gauge content, no physical-magnitude
claim; nothing to `CLAIMS.md`; P1–P16 untouched. The firewalled physics *reading* is `speculations/S038`
(one-way: S038 cites B207, never the reverse).

## Reproduction
- `python golden_breaking.py` — `2I` order spectrum, `⟨RL⟩`/normalizer (`2D₅`), the `2T`/`2O` (E₆/E₇) test.
- `python scale_spectrum.py` — the dimensionless spectrum + hierarchy diagnostics.
- `tests/test_b207_golden_breaking_and_scale.py` — 2 locks. 2 passed.
