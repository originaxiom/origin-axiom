# B348 — gate A extension: the Bloch class is a self-symmetrized Galois orbit (conditional)

**Status: banked (frontier) as a CONDITIONAL structural result. Attacks gate A (S032-A) in-sandbox,
extending B330 to another of its named untested classes. Firewalled; nothing to `CLAIMS.md`.**

The figure-eight decomposes into two regular ideal tetrahedra of shape `z₀ = e^{iπ/3}` — a root of
the **P12 Eisenstein factor** `z² − z + 1` — so its (pre-)Bloch / scissors-congruence class is
`β = 2[z₀]` over the Eisenstein end `ℚ(√−3)`. Gate A asks whether this class is a forced choice.

## Verified
- **(i) The Galois action swaps the roots** (exact): `z₀`, `z̄₀` are exactly the two roots of the
  P12 Eisenstein quadratic; `√−3 → −√−3` exchanges them.
- **(ii) THE SEAM IDENTITY** (exact, the probe's one genuinely new observation):
  `1 − z₀ = z̄₀`. At the Eisenstein point the standard **Bloch duality involution** `z → 1−z`
  (under which `D(z) + D(1−z) = 0` for *all* `z` — a generic dilogarithm identity) **coincides
  with the arithmetic Galois conjugation**. Moreover `z(1−z) = 1 ⇔ z² − z + 1 = 0` — the
  Eisenstein quadratic is *exactly* the locus where the generic analytic involution and the
  object's arithmetic involution are the same map. (This is the Bloch-group face of the
  K020 pattern: the object sits where generic structure and its own arithmetic fuse.)
- **(iii) The orbit is symmetrizable** (30 dps, independent of SnapPy and of the stored constant):
  `D(z̄₀) = −D(z₀)`, so the class orbit is `{β, −β}` with Bloch–Wigner values
  `{+Vol(4₁), −Vol(4₁)}` (`2D(z₀) = 2.029883212819307… = Vol`); symmetric functions: **sum = 0**
  (canonical), fixed-field datum `|2D| = Vol`. The object hands you the pair, never a signed member.
- **(iv) The residual "choice" is the orientation — and the object's own symmetry kills it.**
  The sign of `β` is the orientation of the manifold. 4₁ is **amphichiral** with `CS = 0`
  (P9; live SnapPy checks in `tests/test_snapdata.py`), i.e. the object possesses an
  orientation-reversing self-map realizing the Galois swap **geometrically** (B318). So the orbit
  `{β, −β}` is not merely symmetrizable — it is **self-identified**: B318's "amphichirality is the
  geometric firewall" lands in the Bloch group. Also verified: `D ≡ 0` on the fixed field ℝ —
  the symmetric locus is exactly where the invariant carries no value.

## Honest scope (C-guardrail)
This seals the object's **own** Bloch/scissors class (the concrete element `β = 2[e^{iπ/3}]`).
The full extended-Bloch / `K₃^{ind}` theory (torsion of `B(ℚ(√−3))`, the Rogers-lift `ℤ·π²`
ambiguity, general scissors congruence) is **not** covered and stays in the untested residual.
"No breach in this class" is `open`-tier consolidation, not universal proof.

## The firewall (held)
A structural (no-value) statement: the only fixed-field values produced are ones the proven core
already owns (Vol from P9, the quadratic from P12, `CS = 0`). Nothing to `CLAIMS.md`.

## The fence
Exact sympy for (i)/(ii); mpmath 30 dps for the Bloch–Wigner values (both core deps; no SnapPy
needed). `bloch_class_galois.py` · `tests/test_b348_bloch_class_galois.py`.
Related: **B330** (mechanism), **B318** (amphichirality = the geometric firewall), **P9** (Vol,
CS, amphichirality), **P12** (the Eisenstein factor), **B285** (the CP `ℤ/2` on `ℚ(√−3)`),
**OPEN_PROBLEMS.md** gate A, **K020**. Lit: Bloch–Wigner `D` (Zagier, "The dilogarithm
function"); `Vol(4₁) = 2D(e^{iπ/3})` (Milnor / Thurston, standard); Neumann–Yang (Bloch
invariants of hyperbolic 3-manifolds).
