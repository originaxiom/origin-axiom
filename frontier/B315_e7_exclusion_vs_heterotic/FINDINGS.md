# B315 — H14 answered: the object's E₇-exclusion *contains* heterotic's E₇-skip; the shared root is pseudoreality

**Status: banked (frontier). Resolves H14 (NOTICED → CHECKED), the audit's "deepest framework-search question."
Firewalled; nothing to `CLAIMS.md`.** *Is the object's `E₈+E₆−E₇` exclusion the same obstruction as heterotic string
theory's E₇-skip?* A rep-theory + arithmetic synthesis grounded in B234 (H20/H30, the overdetermined E₇ exclusion).

## The exceptional trichotomy
The Frobenius–Schur reality of the minimal faithful rep, the McKay group, and the object's character/trace field line
up:

| group | rep | FS | reality | chiral? | McKay | field |
|---|---|---|---|---|---|---|
| **E₆** | 27 | 0 | **complex** | **yes** | 2T | `ℚ(√−3)` (Eisenstein end) |
| **E₇** | 56 | −1 | **pseudoreal** | no | 2O | `ℚ(√2)` (**excluded**) |
| **E₈** | 248 | +1 | **real** | no (adjoint) | 2I | `ℚ(√5)` (golden end) |

Only E₆ is **chiral-capable** (a complex fundamental). E₇'s 56 is pseudoreal (FS = −1, symplectic — Sage-verified in
B234), so it cannot carry chiral matter.

## The two exclusions
- **Heterotic** (`E₈ → SU(3)×E₆` standard embedding, chiral N=1) keeps E₆ (the 27 is complex → chiral matter) and
  **skips E₇ because the 56 is pseudoreal → non-chiral.** Heterotic's reason = **non-chirality.**
- **The object** excludes E₇ by **three independent obstructions** (B234/H20/H30): (1) Diophantine — `48 ≠ p(p²−1)`, no
  congruence quotient `2O ↔ SL(2,q)`; (2) **rep-theoretic — `FS(56)=−1`, non-chiral**; (3) arithmetic — the McKay field
  `ℚ(√2)/2O` has disc 8, but the trace-1 law `disc = t²−4det` gives `disc ≡ 1 mod 4` (trace-1 reaches `{−3` [E₆, cusp
  `det=+1`]`, 5` [E₈, monodromy `det=−1`]`}`; disc 8 needs **even** trace — it appears only at the silver bundle `m=2`,
  not the figure-eight).

## Verdict
**Heterotic's E₇-skip is exactly obstruction (2) — non-chirality — which is one of the object's three.** So the two
exclusions **share** the rep-theoretic obstruction, and **the object's exclusion contains heterotic's** (it adds the
Diophantine and arithmetic obstructions). It is **not** "the same single obstruction" (B234/H30: the group-congruence
and the trace field are distinct objects, independently derived). They **coincide** because E₇ is the **pseudoreal
exceptional**: pseudoreality (`FS(56)=−1`) is the shared **root** — simultaneously heterotic's non-chirality *and*,
through the McKay `2O → ℚ(√2)` field with no trace-1 home, the object's arithmetic exclusion. E₇ is overdetermined-bad
from every angle, and pseudoreality is the single fact underneath.

## The bonus (firewalled `[HOOK]`)
The object's two-ended `E₈ + E₆` structure **mirrors the heterotic standard embedding itself**: `E₈` (golden,
ambient/gauge) → `E₆` (Eisenstein, the matter GUT with the chiral 27), E₇ skipped. That is a structural **rhyme**, not
a physical crossing — the object's arithmetic reproduces the heterotic exceptional chain, but the constructions differ
(a two-ended arithmetic object vs. a 10d string on a Calabi–Yau). Recorded `[HOOK]`, firewalled.

## The fence
Standard rep-theory (Frobenius–Schur indicators; E₇'s pseudoreal 56 Sage-verified in B234) + the McKay character fields
+ the trace-1/unimodular arithmetic (B239). Heterotic-string physics is `[LEAP]`; the shared-root claim is the *math*
(pseudoreality), the "object = heterotic chain" reading is the firewalled `[HOOK]`. Nothing to `CLAIMS.md`.

`e7_exclusion_vs_heterotic.py` (pyenv) · `tests/test_b315_e7_exclusion_vs_heterotic.py`. Related: **B234** (the
overdetermined E₇ exclusion, the Sage FS indicator, H20/H27/H30), **B256** (E₇ = the silver bundle's field), **B210**
(the dual McKay E₆+E₈), **K020** (the two-ended object). Lit: the McKay correspondence (2T/2O/2I → E₆/E₇/E₈); Slansky
(1981); heterotic standard embedding (Candelas–Horowitz–Strominger–Witten 1985).
