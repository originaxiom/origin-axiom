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

## Part 3 — scale, computed: the metallic bundle volumes are bounded (SnapPy)

The hyperbolic volumes of the metallic once-punctured-torus bundles `RᵐLᵐ` (`= twister bundle('aᵐBᵐ')`,
m=1 = figure-eight), canonized to geometric triangulations:
- **golden (m=1) = 2.02988 = `2·v_tet`** (figure-eight = two ideal tetrahedra; the **minimal** cusped
  hyperbolic volume) — the floor.
- **silver (m=2) = 3.66386 = `v_oct`** (one regular ideal octahedron; census **m136**), exactly.
- `Vol_m` increasing, Aitken-³-accelerated **limit → `2·v_oct = 7.32772`** (= Vol(Borromean rings)) as
  `m→∞`. So the volumes are **bounded** in `[2.03, 7.33)`, golden at the floor.

**Correction (verify-don't-trust):** an initial pass misread the volumes as growing *linearly*; canonizing to
geometric triangulations shows they **converge** (increments decay `1.63,1.15,0.76,…`).

**Scale read:** the volume-conjecture exponential rate `|⟨RᵐLᵐ⟩_N| ~ e^{N·Vol_m/2π}` **saturates** (`Vol_m`
bounded by `2·v_oct`) — the object cannot supply an *unbounded* exponential rate; all unbounded scale is the
quantization **level `N`**. This *confirms and sharpens* the firewall (B151): no absolute scale, and even the
intrinsic rate is bounded. Golden = the minimal rate.

## Firewall
Finite-group structure + dimensionless invariants + hyperbolic volumes only. No scale, no gauge content, no physical-magnitude
claim; nothing to `CLAIMS.md`; P1–P16 untouched. The firewalled physics *reading* is `speculations/S038`
(one-way: S038 cites B207, never the reverse).

## Reproduction
- `python golden_breaking.py` — `2I` order spectrum, `⟨RL⟩`/normalizer (`2D₅`), the `2T`/`2O` (E₆/E₇) test.
- `python scale_spectrum.py` — the dimensionless spectrum + hierarchy diagnostics.
- `python scale_volume.py` — the metallic bundle volumes (SnapPy): golden=2 v_tet (min), silver=v_oct,
  Aitken limit → 2 v_oct.
- `tests/test_b207_golden_breaking_and_scale.py` — 3 locks (the volume lock is SnapPy-gated). 3 passed.
