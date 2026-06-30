# B312 — Face IV houses the E₆ *form* (the CIZ level-10 invariant); even the quantum face gives the structural theorem

**Status: banked (frontier). The last in-sandbox frontier (B309's "Face IV ↔ SM-content"), answered. Nothing to
`CLAIMS.md`.** The accurate open question from the κ-unification was: the object is *quantized* as a TQFT (Face IV — WRT,
the quantized character variety, anyons) **and** it *carries* E₆/the cascade (Face III, the content) — but those two
faces had never been connected. The sharp, checkable version: **does Face IV house the *same* E₆ the content carries, or
two different "E₆"s the program has been conflating?** The bridge is the Cappelli–Itzykson–Zuber (CIZ) ADE
classification of SU(2)ₖ modular invariants.

## One E₆, three ADE hats
The shared invariants are **Coxeter number 12** and **exponents `{1,4,5,7,8,11}`**:
- **McKay** — `2T` (binary tetrahedral) → affine `Ê₆` (7 nodes): the **classical (k→∞) / arithmetic atom** (B266).
- **Lie** — the E₆ principal grading: the **cascade** (B305) and the figure-eight's E₆ character-variety grading (B264).
- **CIZ** — the exceptional E₆ modular invariant of **SU(2)₁₀**: the **quantum / Face IV** E₆.
  `Z_{E₆} = |χ₀+χ₆|² + |χ₄+χ₁₀|² + |χ₃+χ₇|²`; the diagonal labels `{0,3,4,6,7,10}`, shifted by +1, **are the E₆
  exponents**. (`h = k+2 ⇒ E₆ at k = 12−2 = 10`.)

So Face IV genuinely houses the E₆ the content carries — it is the *same* E₆ (same Dynkin data), with the McKay atom as
its classical limit and the CIZ invariant as its quantization. **The two faces connect.**

## Face IV houses *both* ends, and the arithmetic is compatible via the triality
- The three CIZ exceptional invariants are **E₆@k=10, E₇@k=16, E₈@k=28** (`k = h−2`). The program's **two ends** —
  E₆ (Eisenstein, `ℚ(√−3)`) and E₈ (golden, `ℚ(√5)`) — are **exactly two of them** (E₇ the unused third). The two-ended
  object's two groups are two of the three exceptional SU(2)ₖ modular invariants.
- The E₆ invariant sits at the 12th root of unity (`k+2 = h = 12`). The figure-eight's trace field **`ℚ(√−3)` embeds in
  `ℚ(ζ₁₂)`**: `√−3 = 1 + 2ω`, `ω = ζ₁₂⁴` (verified symbolically + numerically). This holds because **`3 | 12 = h(E₆)`
  — the E₆ triality**, the same `ℤ/3` (`ω`) of the trinification (B305) and the hidden generation symmetry (B302). The
  object's arithmetic is *compatible* with Face IV's E₆ level through the triality.

## The firewall (and the verdict)
The level `k=10` (and `k=28`) is a property of the **ambient modular category SU(2)ₖ** — *any* link evaluated there sees
the E₆ (E₈) invariant. It is **generic, not object-specifically selected** by the figure-eight. The object-specific
signal stays the **arithmetic atom** (`2T / ℚ(√−3)`, McKay — the classical limit). **So Face IV houses the E₆ *form*,
not the SM values / the specific level.**

**"Face IV ↔ content" is real for the form** (the object touches all three ADE faces of E₆; Face IV houses both ends;
the trace field is compatible via the triality) **and firewalled for the values** (the level is generic). Even Face IV —
the last in-sandbox hope for object-specific content — gives the **structural theorem**: the quantization houses the
*form*, not the *values*.

## What this closes
This **closes the in-sandbox program** on a consistent note: **all four faces of `κ` give the same answer.**

| face of κ | what the object supplies | what is not forced |
|---|---|---|
| existence (P008) | the non-cancellation obstruction `κ≠2` | — |
| geometry (the seam, B286/B294) | chirality/scale/clock *mechanism* at the closing | the specific closing (value) |
| matter (the cascade, B305/B306/B311) | the E₆ structure + the trinification (Eisenstein `ω`) | the SM selection / couplings |
| **quantum (Face IV, B312)** | **the E₆ *form* as the CIZ level-10 invariant; both ends** | **the level / the SM values** |

**Structure yes, scale/values no — now verified across all four faces.** The remaining gates (the `T[4₁;E₆]` CRUX, the
multiplicity question B307, the non-Hermitian DG theorem L19/L20) are genuinely specialist. The in-sandbox math is
exhausted.

## The fence
Pure ADE combinatorics (the CIZ classification, the E₆ exponents) + a cyclotomic embedding (sympy + numeric). The
"quantization *is* the physical framework of the SM" reading is firewalled. Nothing to `CLAIMS.md`.

`face_iv_houses_the_form.py` (pyenv) · `tests/test_b312_face_iv_houses_the_form.py`. Related: `B309` (the four faces of
κ; this frontier named), `B305`/`B306`/`B311` (the cascade E₆; the trinification), `B266`/`B282` (the McKay 2T atom,
`ℚ(√−3)`), `B264` (the fig-8 E₆ character variety, the exponents), `B204`/`B218`–`B230` (Face IV — WRT, Fibonacci/golden
end). Lit: Cappelli–Itzykson–Zuber (1987, the ADE classification of SU(2)ₖ modular invariants); the McKay correspondence;
Ocneanu (quantum subgroups / module categories over SU(2)ₖ).
