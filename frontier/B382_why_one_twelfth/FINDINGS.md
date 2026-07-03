# B382 (D3(b)) — leg 1 BANKED: the phase-ratio law verified on its exact classical domain

**Status: leg 1 banked (frontier); legs 2–3 (the (γ−I)⁻¹ matching with the ordering correction,
then the slot-constant closed form) pending. Pre-registration: PREREGISTRATION.md (PR #477,
first). Firewalled.**

## The intertwining (exact)

`D·X·D⁻¹ = X·Z` and `D·Z·D⁻¹ = Z` — phase-free, the clean shear on the Heisenberg frame.
The WR-side conjugation carries phases (handled empirically per word by the γ-extraction).

## The phase-ratio law (the formula's core; verified on all 225 shifts per word)

For a word U with group element γ (extracted empirically from the Heisenberg conjugation):

    tr(U · XᵃZᵇ) = tr(U) · ζ₁₅^{Q(a,b)},   Q quadratic,

verified EXACTLY (every shift, exact field division) on all sampled words with `det(γ−I)`
invertible mod 15 — words (1,0), (0,1), (1,1), (2,1), (2,3). The two sampled words where the
ratio is NOT a pure phase — (1,3) and (3,1) — have `det(γ−I) ≡ 5 (mod 15)` exactly: **the
failures are the classical domain boundary of the trace formula, confirmed by the data.**

## The universal linear part

Across every passing word the linear part of Q is the SAME: `+7a + 8b (mod 15)` — the shift
operator's own fingerprint, independent of γ; only the quadratic coefficients carry the word.
(Q-tables banked in `trace_formula.json`.)

## Next legs (named)

Leg 2: derive the X^aZ^b ↔ Weyl-ordering correction and match the empirical Q's quadratic part
to the classical `½·v·(γ−I)⁻¹·v` form — pinning every convention. Leg 3: assemble the slot
constant `Π_H tr(Par·H₁H₂)` from the closed form and identify the origin of the 1/12 among the
three registered readings. KILLS unchanged from the pre-registration.

**Provenance.** PREREGISTRATION.md; P56/P57/P60/P62 (the machinery). Reproducer:
`trace_formula.py` (~3 min); locks: `tests/test_b382_trace_formula.py`.

---

# Leg 2 BANKED: the closed form — and the twist isolated as the half-characteristic term

**The law, every convention pinned by data (fit over all five domain words, then the canonical
cross-check registered-and-passed):**

    tr(U_γ · XᵃZᵇ) = tr(U_γ) · ζ₁₅^{ ½·ω(v,(γ−I)⁻¹v) − ½·ab − ½·ω(v,(1,1)) },   v=(a,b)

- `½·ω(v,(γ−I)⁻¹v)` — the classical Hannay–Berry quadratic (fit α = 8 = 2⁻¹ on the J·(γ−I)⁻¹
  form; the ten equivalent Cayley faces all fit with the forced factor-2 relations).
- `−½·ab` — the X^aZ^b ↔ Weyl-ordering correction (fit s = 7 = −2⁻¹).
- `−½·ω(v,(1,1))` — **the theta twist**: the universal linear part (7a+8b) decodes as the
  half-characteristic shift at the Weyl point (1,1).

**The cross-check (prediction registered in verify_canonical.py BEFORE running):** the canonical
model (C = diag ζ^{8j²} = canonical lift of the same shear; D = C·χ with χ = diag ζ^{−8j})
satisfies the SAME law with the SAME quadratic and ordering constants and **linear part ≡ (0,0)**
— verified on all five words (canonical_check.json; orders 20/12 match). The twist enters the
shifted-trace spectrum as exactly one term: the half-characteristic. "The seam lives at the
half-characteristic point (½,½)·(1,1)" is now an exact trace-formula statement.

**Leg 3 (next):** the slot constant is a DFT of these shifted traces at the FIXED shift (1,1):
via P57, Par·W₁ʲW₂ˡ = ζ₆⁻¹·J⁻¹·T(1,1)·W₁ʲW₂ˡ, so
    Π_H tr(Par·H₁H₂) = ζ₆⁻¹/(o₁o₂) Σ_{j,l} c₁(j)c₂(l) · tr(W₁ʲW₂ˡJ⁻¹) · ζ₁₅^{Q_{jl}(1,1)}
with c₁, c₂ the slot DFT windows and o₁o₂ = 240 — every factor now has a name; assemble and see
which registered 1/12 reading the factorization forces. Reproducers: leg2_fit (inline, banked
in this session's transcript + the fit re-runnable from trace_formula.json), verify_canonical.py.
