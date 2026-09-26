# B288 — The arithmetic filling census: E₆ is an open-object property, lost on closing

> **CORRECTION OF RECORD (B1376, 2026-09-26; error class E71).** This arc's clause "0 are arithmetic (none is
> imaginary-quadratic, degree 2)" is **withdrawn as read**. It tested arithmeticity with the criterion for a
> **cusped** Kleinian group (Maclachlan–Reid 8.2.3: invariant trace field imaginary-quadratic, integral traces) —
> that criterion decides nothing for a **closed** manifold, which a Dehn filling is. Under the correct cocompact
> criterion (Theorem 8.3.2: exactly one complex place, integral traces, the invariant quaternion algebra ramified at
> every real place), **three of the grid's fillings are arithmetic up to orientation**: `m004(5,1)` — the
> **Meyerhoff manifold**, arithmetic by Chinburg's 1987 theorem, invariant trace field a quartic of discriminant
> `−283` — `m004(6,1)` (`−59`) and `m004(8,1)` (`−31`). This matches B718's own 2026-07 computation exactly; the two
> results sat unreconciled for two months, and the false sentence reached main's paper. **What survives unchanged:**
> none of the fields is imaginary-quadratic (true, and now named `N_IMAGINARY_QUADRATIC`), and no closed filling's
> field contains `ℚ(√−3)` (B740, 78/78) — none of the three arithmetic fields can, since a field with a real
> embedding has no imaginary-quadratic subfield. So **the E₆-selecting arithmetic is still an open-object property**;
> only the stronger, false "= arithmetic" reading falls. `verdict.py` repaired in place
> (`N_ARITHMETIC_COCOMPACT = 3`, `ARITHMETIC_SLOPES`); the lock repaired. See `frontier/B1376_the_arithmetic_fillings/`
> for the full re-derivation (own code, no Sage) and `docs/ERROR_LEDGER.md` E71.

**Status: banked. Math (arithmetic of trace fields) verified two methods; nothing to `CLAIMS.md`.** The CRUX —
*input-E₆ = output-E₆* — re-examined **through the seam**. B281 showed the cusped character variety does not
geometrically distinguish E₆. New question: when we **close** the object (Dehn filling), does the closed manifold
**re-see** the cusped object's arithmetic E₆ datum — `ℚ(√−3) → 3 → SL(2,𝔽₃)=2T → McKay-E₆` (B266/B282) — or is E₆
an **open-object** property destroyed by closing?

## The result (a sharp negative)
- The **cusped (open)** figure-eight has invariant trace field **`ℚ(√−3)`** (`x²−x+1`, disc `−3`) — the E₆ atom.
- Of the **54 closed hyperbolic fillings** resolved over the grid `|p|,|q| ≤ 8`, `gcd(p,q)=1`:
  - **0** re-see `ℚ(√−3)` (none contains `√−3` even as a subfield);
  - **0** are imaginary-quadratic, degree 2 — ***corrected 2026-09-26 (B1376, E71): this is NOT the same statement as
    "0 are arithmetic."*** Under the criterion that actually decides arithmeticity for a closed manifold (the
    cocompact criterion, Maclachlan–Reid 8.3.2), **3 of the 78 ARE arithmetic up to orientation** — `m004(5,1)` (the
    Meyerhoff manifold, Chinburg 1987), `m004(6,1)`, `m004(8,1)`, discriminants `−283, −59, −31` — matching B718's
    July census. None of the three is imaginary-quadratic, so this bullet's original count (0) was always correct;
    only its old gloss "(arithmetic)" was wrong;
  - all have **higher-degree** invariant trace fields (degrees `3,4,5,6,7,9,10,11,13,14,15,18,19`; plus 24 stragglers
    of degree `>20`) — degree here is the invariant trace field's degree, not a bar to arithmeticity (the Meyerhoff
    manifold's is degree 4).

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

---
**B740 completion note (2026-07-21):** this census resolved 54 of the grid's 78 hyperbolic fillings
(24 were skipped by the environment-dependent positivity check / degree ceiling — cc2 register
crack #1). B740 recomputed the ENTIRE 78-filling grid fresh (retriangulation recovery + Sage field
ID to degree 32 + the amphichirality shortcut 4₁(p,q)≅4₁(−p,q), 7/7 isometries verified): **the
verdict STANDS and is now fully earned — no closed hyperbolic filling contains √−3, 78/78.** See
frontier/B740_b288_stragglers/.
