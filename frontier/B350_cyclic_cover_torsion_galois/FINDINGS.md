# B350 — gate A extension: the cyclic-cover torsion class is a Galois orbit (conditional)

**Status: banked (frontier) as a CONDITIONAL structural result. Attacks gate A (S032-A) in-sandbox,
extending B330 to the first of its named untested classes. Firewalled; nothing to `CLAIMS.md`.**

Gate A asks whether *any* invariant of the single seed is (1) trace-map-invariant, (2) discretely
multivalued, (3) unsymmetrizable — a genuine forced choice. B330 sealed five classes under one
mechanism (*a finite Galois orbit is always symmetrizable*) and named the untested residual. This
probe seals one of those: **Reidemeister/abelian torsion of the cyclic covers**.

## Setup
The figure-eight is fibered with monodromy `A = [[2,1],[1,1]]`, so its `n`-fold cyclic cover is the
mapping torus of `Aⁿ` and the torsion module is `coker(Aⁿ − I)` — the P8 object. The scalar torsion
factors are the Alexander values `Δ(ζₙʲ)`, `Δ(t) = t² − 3t + 1 = charpoly(A)` (the A-sector polynomial).

## Verified (all exact, sympy)
- **(i) The torsion orders are the P8/C5 ladder.** `|det(Aⁿ − I)| = L₂ₙ − 2` for `n = 2..8`
  (5, 16, 45, 121, 320, 841, 2205) — the canonical fixed-field data, identical to the P8
  mapping-torus torsion and the C5 Lucas hierarchy. One ladder, three faces.
- **(ii) The factor multiset is a symmetrizable Galois orbit.** `{Δ(ζₙʲ) : j = 1..n−1}` is closed
  under the full `Gal(ℚ(ζₙ)/ℚ)` (index permutation `j → jk`), and its elementary symmetric
  functions are **integers** (constant term cross-checked against `det(Aⁿ−I)/Δ(1)`). The B330
  lemma verbatim: the object determines the orbit and its symmetric (integer) functions — never
  a member.
- **(iii) The torsion groups by Smith normal form.** `n=2: ℤ/5`, `n=3: (ℤ/4)²` — **independently
  re-deriving B326's cover-torsion module** — `n=4: ℤ/3⊕ℤ/15`, `n=5: (ℤ/11)²`, `n=6: ℤ/8⊕ℤ/40`.
- **(iv) The deck action is fixed-point-free for every `n`, uniformly.** `Aⁿ − I = (A−I)·N` with
  `N = I + A + … + Aⁿ⁻¹` and `det(A−I) = Δ(1) = −1` a **unit**, so `N·ℤ² = im(Aⁿ−I)` exactly
  (verified as lattice equality *and* by brute-force class counting, `n = 2..6`) and the only
  deck-fixed class is `0`. This generalizes B330's `n=3` stress test to all `n` with a one-line
  cause: no canonical distinguished sub-object exists at any level of the tower.

## Honest tier note (MB8: generic ≠ discriminating)
`Δ(1) = ±1` holds for **every** knot in `S³`, so mechanism (iv) is **generic-knot**, not
object-specific. The object-specific content is (i)–(ii): *which* orbit (the trace-3/Lucas
ladder, the P8 = C5 tie). Do not read (iv) as figure-eight forcing.

## Conclusion — CONDITIONAL (worded per the C-guardrail)
The cyclic-cover **abelian** torsion class joins the sealed list: canonical integers at the
fixed-field level, a symmetrizable Galois orbit at the factor level, no distinguished sub-object
at the module level — **no forced choice in this class**. NOT covered: the **nonabelian**
(Ptolemy / adjoint) torsion of the character-variety components (B98/B99 record the geometric
adjoint torsion `τ₁ = −3`, a single rational — canonical — but the class as a whole stays in the
untested residual). "No breach in this class" is `open`-tier consolidation, not universal proof.

## The firewall (held)
A structural (no-value) statement; the torsion tower's canonical data are the same integers the
proven core already owns (P8/C5). Nothing to `CLAIMS.md`.

## The fence
Exact sympy (integer matrices, cyclotomics, SNF, lattice arithmetic); no numerics, no physics
values. `cyclic_cover_torsion.py` · `tests/test_b347_cyclic_cover_torsion_galois.py`.
Related: **B330** (mechanism + the untested-classes list), **B326** (`(ℤ/4)²`, re-derived),
**P8** (torsion ladder), **C5** (Lucas hierarchy), **B98/B99** (adjoint torsion, cited),
**OPEN_PROBLEMS.md** gate A, **K020**. Lit: Fox–Milnor / standard cyclic-cover torsion
(`H₁` of the n-fold cover via `Δ(ζⁿ)`), standard Galois theory.
