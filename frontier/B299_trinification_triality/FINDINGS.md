# B299 — The (θ,φ) Z₃×Z₃ is the E₆ trinification triality; the heterotic E₆ is generic

**Status: banked (frontier). Structural backbone verified; the specific derivation claim refuted; nothing to
`CLAIMS.md`.** From the Chat-1 cross-chat handoff, which carried material from an external heterotic exploration
(ChatGPT's `origin-sm-dynamics` repo, assessed separately). We verify the backbone *and* refute the load-bearing
derivation claim, both **self-contained in origin-axiom** (the matrices are embedded; no dependency on the external
repo).

## Verified (the backbone holds)
- **`θ, φ` are a genuine commuting Z₃×Z₃ of E₆:** order 3, det 1, commute, eigenvalues `{1,1,ω,ω,ω²,ω²}`, fixed dims
  2/2, common fixed 0.
- **They preserve a genuine E₆ Cartan matrix** (det 3, the E₆ Dynkin diagram — chain `1-2-3-4-5` + node 6 off node
  3), which I re-derived by solving the common-invariant-form system (the *Bourbaki* ordering failed). So they **are**
  E₆ lattice automorphisms, in a non-Bourbaki simple-root ordering, and **inner** (det +1, order 3 ⇒ in `W(E₆)`).
- **★ On the 27 (the minuscule rep), `θ` and `φ` each act FREELY: 9 orbits of size 3, zero fixed weights.** This is
  the structure of the **E₆ trinification triality** — the inner ℤ₃ that cyclically permutes the three SU(3)'s of
  `E₆ ⊃ SU(3)³`, `(3,3̄,1) → (3̄,1,3) → (1,3,3̄)`.

## Refuted (a clean negative — the handoff agreed it would be bankable)
- **"H-label = φ-eigenvalue on the 27" FAILS.** φ acts *freely* (no fixed weights), so there is **no per-weight
  φ-eigenvalue** to grade the 27. The colored-vs-electroweak (doublet-triplet) split requires **choosing which SU(3)
  is color** — an external Wilson-line/vacuum input that *breaks* the triality. The split is **not forced** by
  `(θ,φ)`. (This was ChatGPT's 100-run wall; it is *not* closed by this — and we learn precisely why.)

## Consequence
This **independently confirms B282 (the genericity collapse) from the outside**: a whole heterotic framework reaches
E₆ + the trinification structure **without ever touching `4₁`'s object-specific arithmetic atom** (the `2T` from
`ℚ(√−3)`). The structure is genuine E₆; the actualization (the color choice, the orbifold, the splitting) is
external. Together with the heterotic sidequest assessment, this is the **second external confirmation** that
generic-E₆ is cheap and the arithmetic is the signal.

## The one place it could become rigorous
The verified-new piece — the cusp's two cycles `(μ,λ)` ↔ the two orbifold generators `(θ,φ)` ↔ E₆'s three SU(3)'s —
would need **class-S for type E₆** (`T[4₁;E₆]`) to make rigorous. That is the **CRUX / specialist gate** the whole
program keeps returning to. Recorded as the standing open lead.

## The fence
Pure E₆ Lie/lattice computation (sympy, self-contained). A genuine structural identification + a clean refutation of
the derivation claim. Nothing to `CLAIMS.md`.

`trinification_triality.py` (pyenv: the embedded θ,φ + E₆ Cartan; Z₃×Z₃ verification; the 27-weight orbit structure)
· `verdict.py` · `tests/test_b299_trinification_triality.py`. Related: `B282` (genericity collapse — confirmed),
`B298` (the generation obstruction / the 9+9+9), `B266` (the arithmetic 2T→McKay-E₆), `B271` (amphichirality =
E₆ outer auto), `B292` (multiplicity tripartite). The external exploration: assessed in this session's notes.
