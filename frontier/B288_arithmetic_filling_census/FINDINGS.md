# B288 — The arithmetic filling census: E₆ is an open-object property, lost on closing

**Status: banked. Math (arithmetic of trace fields) verified two methods; nothing to `CLAIMS.md`.** The CRUX —
*input-E₆ = output-E₆* — re-examined **through the seam**. B281 showed the cusped character variety does not
geometrically distinguish E₆. New question: when we **close** the object (Dehn filling), does the closed manifold
**re-see** the cusped object's arithmetic E₆ datum — `ℚ(√−3) → 3 → SL(2,𝔽₃)=2T → McKay-E₆` (B266/B282) — or is E₆
an **open-object** property destroyed by closing?

## The result (a sharp negative)
- The **cusped (open)** figure-eight has invariant trace field **`ℚ(√−3)`** (`x²−x+1`, disc `−3`) — the E₆ atom.
- Of the **54 closed hyperbolic fillings** resolved over the grid `|p|,|q| ≤ 8`, `gcd(p,q)=1`:
  - **0** re-see `ℚ(√−3)` (none contains `√−3` even as a subfield);
  - **0** are arithmetic (none is imaginary-quadratic, degree 2);
  - all have **higher-degree** invariant trace fields (degrees `3,4,5,6,7,9,10,11,13,14,15,18,19`; plus 24 stragglers
    of degree `>20`).

**So the E₆ arithmetic atom is an OPEN-object property, DESTROYED by closing.** The arithmetic that selects E₆ lives
in the cusp — the interface with the nothing — not in any closing.

## Two methods (verify-don't-trust)
1. **Invariant trace field** via **traces of squares** (lift-independent, the Maclachlan–Reid commensurability
   invariant): `find_field` on `invariant_trace_field_gens`; test `√−3 ∈ kM ⟺ x²+3` has a root in `kM`.
2. **Shape / trace field** (the *larger* field) cross-check: `tetrahedra_field_gens` / `trace_field_gens`. For the
   sampled fillings even this largest field (degree 8–12) lacks `√−3` — so it is absent in every subfield, a fortiori
   in the invariant trace field. Independently **re-verified in pyenv (sympy)** for the cusped field (disc `−3`) and a
   sample of closed fields (`x²+3` stays irreducible over each), so the lock does not merely trust the SnapPy run.

## Interpretation for the CRUX (leaning catalogue)
The seam reframe (B286) said the structure lives in the **bulk/cusp** (the open object) and the actualization is the
**closing**. B288 makes this precise for the E₆ datum: **the E₆-selecting arithmetic is a property of the open object,
and the closing does not re-instantiate it.** So no closing is *arithmetically* distinguished toward E₆ — leaning
**catalogue** for the input-E₆ = output-E₆ CRUX. This is the expected, honest, negative-shaped result, and it
**strengthens** the firewall stance: E₆ is real and object-specific (B282), but it is an open-object invariant, not a
property the closed (actualized) manifold carries.

## Contrast with B287 (the selection axis matters)
B287 found the closing **is** selective for the object's own *dynamics* (the fiber closing re-sees `A=LR`/P1). B288
finds it is **not** selective for the object's *arithmetic* (no closing re-sees `ℚ(√−3)`/E₆). Selection is
**stratified by axis** — exactly the texture B294 will tabulate.

## The fence
Pure arithmetic of trace fields. It does **not** select a Standard-Model world; it records *where* the E₆ arithmetic
lives (the open object). Any "an arithmetic closing = the E₆ world" reading is moot here — there is no such closing in
the grid; the conclusion is the negative. Nothing to `CLAIMS.md`.

`arithmetic_census.py` (sage-python: SnapPy + Sage NF) · `verdict.py` (pyenv, sympy re-check) ·
`tests/test_b288_arithmetic_filling_census.py`. Related: `B282` (E₆ is arithmetic not geometric), `B266` (2T→McKay
E₆), `B276` (ζ₃ probe), `B281` (CRUX scoping), `B286` (the seam), `B287` (the dynamical distinguished closing),
`B125` (metallic arithmeticity).
