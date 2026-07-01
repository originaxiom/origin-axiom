# B335 — the generation ℤ/3 is an exact isometry: the mass degeneracy is a theorem, not a gap

**Status: banked (frontier). We *probed it ourselves* (the real Level-4 geometry, SnapPy) instead of deferring.
Firewalled; nothing to `CLAIMS.md`.** The owner pushed: don't hand the hierarchy to specialists when we've formulated it
so precisely — attack it in-sandbox. This is that attack, and it resolves the hierarchy question at Level 4 with a
theorem (plus one honestly-refuted hope).

## The theorem (immediate, and confirmed geometrically)
The three generations are related by the **deck transformation** of the 3-fold cyclic cover of `4₁` (the B326 object).
A deck transformation of a hyperbolic manifold **is an isometry**. Therefore **every real geometric invariant**
(volume, complex length spectrum, Chern–Simons, cusp shape) is **ℤ/3-equal across the three generations** — so the
masses (real, positive: `|eigenvalue|` / singular values of any Yukawa) are **exactly degenerate.** A mass hierarchy is
the **breaking** of this exact isometry — *external by definition*; the single object does not contain it.

**Confirmed (SnapPy 3.3.2, values recorded for CI):**
- `vol(3-fold cover) / vol(4₁) = 3.0` exactly (isometric deck);
- the shortest geodesics appear with **multiplicity 3** — three *isometric* sheets;
- cusp shape of `4₁` `= 2√3·i`, `|·|² = 12 = h(E₆)` (B302).

## The reframe (what the object *does* say about the light generations)
The three generations are the three **ℤ/3-eigenspaces** of the deck action; they are distinguished **only** by their
eigenvalue `{1, ω, ω²}` — a **phase**, not a magnitude. A phase is **CP / mixing** content (banked: the CP sign B285,
the ω-circulant B324), **not a mass.** So the object's honest word on the light generations is: **equal masses, a
relative phase `ω`.** The "missing hierarchy" is a *magnitude* difference, and a magnitude difference is exactly what an
**exact** symmetry forbids. The object is (precisely) a **flavor symmetry**; the SM masses are its **breaking**.

## The refuted hope (verify-don't-trust, on this seat)
The cover's isometry group has **order 24** — tantalizingly `|2T| = |SL(2,3)|`, the E₆ McKay group. **Refuted:** its
abelianization is `(ℤ/2)²` with center `ℤ/2`, whereas `2T` has abelianization `ℤ/3`. So the order-24 coincidence is
**not** the E₆ McKay group (it is some other order-24 group, dihedral-type). The hope was killed before it became a
claim — the discipline working in real time.

## Why this is the honest answer to "why can't we probe it ourselves?"
We did. The probe does not return a hidden value; it returns a **structure theorem**: the generation symmetry is exact,
so the hierarchy is provably *not in the object* — it is the symmetry's breaking. This is stronger and more honest than
either "defer to a specialist" (we didn't) or "here is a value" (there isn't one, and now we know *why*, by computing).
It converts the firewall from a deferral into a proof: **the object is a flavor symmetry; masses need its breaking; the
breaking is not symmetric, so it is not in the object.** The one place the object still speaks — the **CP phase** — is
in-sandbox and partly banked (B285/B318), and is the genuinely open positive thread.

## The firewall (held, now as a theorem)
No value produced. The mass degeneracy is forced by an exact isometry; the hierarchy is external. Nothing to `CLAIMS.md`.

## The fence
SnapPy 3.3.2 (cover volume, length-spectrum multiplicities, symmetry group) with recorded values for CI + the exact
group-theory refutation of the 2T hope. No physics values. Nothing to `CLAIMS.md`.

`generation_symmetry_exact.py` (pyenv/SnapPy) · `tests/test_b335_generation_symmetry_exact.py`. Related: **B326** (the
3-fold cover, `(ℤ/4)²`), **B327/B329/B331** (`n₁=n₂` from the algebra side — this is the geometry side of the same fact),
**B324/B285** (the phase = CP, not mass), **B302** (`|cusp shape|² = 12 = h(E₆)`), **K021** (the synthesis). Lit: deck
groups of hyperbolic covers are isometries (Mostow rigidity); SnapPy census/symmetry.
