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

---

# Leg 3 BANKED: the assembly is exact — and the 1/12 decomposes as 1/16 + 1/48

**Gate A (the factorization): 142/142.** Every cell of the Par-table with det(γ′−I) invertible
mod 15 equals `ζ₆⁻¹ · tr(W₁ʲW₂ˡJ⁻¹) · ζ₁₅^{Q(1,1)}` exactly (Q from the leg-2 closed form at
the fixed shift v₀=(1,1); J = ζ₆⁻¹XZ·Par by P57; γ′ = −γ₁ʲγ₂ˡ). Zero mismatches; the 98
boundary cells split by det-class as {3: 26, 5: 68, 15: 4}.

**Gate B (the assembly): the slot constant reproduces exactly** —
t(6,2)−t(6,10)−t(14,2)+t(14,10) → Π_H = (0, 0, −1/12, −1/12), the banked −(φ/6)√−3.

**THE READING (the registered adjudication).** Splitting the slot sum by det-class of (γ′−I):

    class 1 (generic Hannay–Berry cells):   (0, 0, −1/16, −1/16)
    class 3 (3-singular boundary):          0
    class 5 (5-singular boundary):          (0, 0, −1/48, −1/48)
    class 15:                               0
    ─────────────────────────────────────────────────────────────
    total:  −1/16 − 1/48 = −4/48 = −1/12    (exact)

**The 1/12 is the generic metaplectic sum (−1/16) plus exactly one-third more from the
5-ramified boundary (−1/48) — the golden prime's cells; the 3-side boundary is silent.**
Adjudication of the three registered readings: mechanical-240 is REFUTED as mechanism (the
sum is class-weighted, not uniform support-counting — support is 128 cells with classes
{1: 84, 3: 12, 5: 28, 15: 4}); Haar(2T×ℤ/2) and B₂/8 remain numerological faces — neither is
forced by the factorization; the TRUE mechanism is the two-class split above. Residue (named):
derive the −1/16 and −1/48 values themselves from the character magnitudes |tr|² = 15/|det|
per class — the next layer down.

**Bonus lock (the 3-block face resolved):** searching all ±-gradings on the banked table, the
banked 3-block constant (0, 0, −1/12, +1/12) is hit by exactly the gradings
H₁′ = ±(P₄−P₀), H₂′ = ±(Q₈−Q₄) (matched signs) — row 16 absent from the grading, consistent
with its ℚ(√5)-darkness. My symmetric guess (P₄−P₁₆)⊗(Q₄−Q₈) gives a NEW exact sector value
(0, 0, +1/24, −1/24) — banked as data.

**Provenance.** assemble_constant.py (~4 min), decompose_reading.py (~4 min); assembly.json,
reading.json; locks in tests/test_b382_trace_formula.py. Pre-registration: PREREGISTRATION.md
(PR #477, committed first). Firewall: statements about the level-15 theta model.
