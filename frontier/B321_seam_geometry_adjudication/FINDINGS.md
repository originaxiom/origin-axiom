# B321 — The self-realizability / seam-geometry arc, adjudicated: one real certificate, two splices, one sharpened gate

**Status: banked (frontier). Verify-don't-trust on the long cross-chat "self-realizability" (Chat-2) + "seam geometry"
(Chat-1) arc. Firewalled; nothing to `CLAIMS.md`.** The arc ran many swings; this separates the one genuinely-new
verified fact from the banked reframes and the splices — engaging (not dismissing), as the brave-partner discipline
requires.

## Verified (new, real, firewalled): `|cusp shape|² = h(E₆) = 12`
The figure-eight cusp shape is **`2√3·i`** (SnapPy: `0 + 3.4641…i`, `|shape|² = 12.000000`), and `h(E₆) = 12` (the
Coxeter number). Both root in `ℚ(√−3)` — the cusp via the trace field, `h(E₆)` via `2T → McKay → E₆`. So the Dehn
fillings' core-length quadratic form is **`Q(p,q) = |p+qτ|² = p² + 12q²`, with coefficient `h(E₆)`.** A genuine,
striking certificate — the cusp geometry and the E₆ Coxeter number meet at the shared Eisenstein arithmetic.
**Caveat:** `|τ|²` is *not* `SL(2,ℤ)`-invariant (basis-dependent), so this is a certificate/coincidence, not a canonical
invariant identity — and any physics reading is firewalled.

## Refuted (splice): "the CP phase `π/6` *is* the core geodesic length of the filling `(6,3) = 3×(2,1)`"
Three problems, one of which Chat-1 half-flagged itself:
- **`gcd(6,3) = 3`** → `(6,3)` is *not* a primitive Dehn slope (only coprime `(p,q)` give distinct fillings).
- **"`core(6,3) = core(2,1)/3`" is the trivial quadratic scaling** `Q(3z) = 9Q(z)` (`√Q(6,3)=12=3·4=3·√Q(2,1)`) — *not*
  a "generation ℤ/3 acting on the `(2,1)` direction."
- It **equates an angle** (`arg(κ) = ±π/6`, B285) **with a length** (a core geodesic) — a dimensional splice.

So `π/6 = π/6` is one number matching under a non-primitive, trivially-scaled, dimensionally-mismatched identification.
Not meaningful.

## Refuted: "the democratic Yukawa `(3λ,0,0)` is forced rank-1 by the ℤ/3 (`|ω|=1`)"
`|ω|=1 ⇒ Q(ωz)=Q(z)` is true but *trivial* (a rotation preserves the norm); it does **not** produce the all-ones matrix.
**B320 already proved** a ℤ/3-invariant matrix is a generic *circulant* (rank 3); the rank-1 all-ones needs
*S₃*-democracy. So "ℤ/3 → democratic rank-1" **contradicts B320**, is firewalled physics, and presupposes the
B307-gated three generations.

## Reframe (banked content, re-described): "self-realizability"
The reframe — *the object self-determines a value by which configuration realizes its golden identity* — is a real,
useful re-reading of the firewall's *interior*, but its two "crossings" are **banked results reframed**: the CP sign =
the object's **chirality** (`Im w > 0` selects the geometric structure vs its mirror) is **B285/B318**; the scale `k=3`
(`2cos(π/5)=φ`) is **B313**. The "flow-selection" version was **correctly killed** by Chat-2 (`σ=[[2,1],[1,1]]` is
orientation-preserving, so the flow cannot select a handedness) — a clean self-catch.

## The genuine residue: the sharpened multiplicity gate
Chat-2's honest self-correction is the valuable output. **Single-object** self-realizability → 1 generation (B307).
**Relational** self-realizability — via the *intrinsic* commensurator `ℤ/3` (Eisenstein units of `ℚ(√−3)`,
`PGL(2,𝒪₋₃)`, B302) — is **untested**, and is where a genuine "3" could live. Stated with a **refutation condition**
(so it is not the absorbing loop): it **opens** iff the commensurator `ℤ/3` gives three *symmetric copies of the 27*;
it **closes** iff those are the trinification factors (color/L/R, B302/B305 — the *wrong* 3) or fail to be symmetric
matter copies. This is the standing multiplicity gate (B302/B307) **sharpened** — it belongs in `OPEN_PROBLEMS.md`.

## The net
The arc produced one real certificate (`|τ|²=h(E₆)`), two splices (both refuted, one self-flagged), a useful reframe of
banked content, and one genuine sharpening of the multiplicity gate. It is another instance of the absorbing-loop
caveat (K020 §6a) — the exciting new "seam encodes the SM parameters" angle reduces to `Q=p²+12q²` (the cusp norm form)
+ splices — but honestly adjudicated by computation. The specialist gate stands, now sharper.

## The fence
The SnapPy cusp shape (`|shape|²=12`) + the elementary quadratic-form / primitivity checks + the B320 result. All
physics readings firewalled. Nothing to `CLAIMS.md`.

`seam_geometry_adjudication.py` (pyenv) · `tests/test_b321_seam_geometry_adjudication.py`. Related: **B285**/**B318** (CP
sign = chirality), **B313** (k=3), **B320** (Z/3 → circulant, rank-1 needs S₃), **B302**/**B305**/**B307** (the
commensurator ℤ/3 / trinification / the generation theorem), **B290** (the cusp shape `2√3·i`), **B266**/**B282** (the
`ℚ(√−3)` atom, `h(E₆)` via `2T`). Lit: Neumann–Zagier (Dehn filling / core lengths); the McKay correspondence.
