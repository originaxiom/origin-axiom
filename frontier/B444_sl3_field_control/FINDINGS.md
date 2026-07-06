# B444 — the decisive SL(3) elimination-field control (Chat-2's rung, run)

**Status: banked (frontier). Firewalled; nothing to `CLAIMS.md`.** Reproduces a KNOWN result
(Falbel 2008) and confirms the Inversion Law at SL(3). The "SL(3) rung → path to physics → 3
generations" framing (Chat-1) is **not** supported; a number field of a character variety is not
physics, and the "3 generations" reading is the repeatedly-killed trap (B428 "three folds = three
generations DEAD"; the 3:3:2; the three-body generation symmetry — all refuted).

## The question (Chat-2's, made decisive)

At SL(2) the figure-eight `4₁` and the twist knot `5₂` were floated as "arithmetically close." The
proposed higher-rung invariant was the **SL(3) elimination field** — the field of definition of the
boundary-unipotent SL(3,ℂ) representations (the Ptolemy variety, obstruction class 0). Chat-2's
prereg: reproduce fig-8's field = `ℚ(√−7)`, then compute `5₂`'s. **Same field → generic (laundering
holds); different → figure-eight distinguished at SL(3).** Chat-2's own Groebner over ℚ timed out,
so the control (`5₂`) was UNRUN. "Do NOT bank as a fingerprint until the control runs."

**The control is now run** (Sage's `elimination_ideal`, exact over ℚ, seconds — no magma needed).

## Result (exact, reproducible: `extract_ptolemy.py` → `sl3_field_control.sage`)

| Knot | SL(3) Ptolemy | #reps (deg) | number fields of the boundary-unipotent reps |
|---|---|---|---|
| **`4₁`** (the object) | 0-dim | 6 | **`ℚ(√−3)`** and **`ℚ(√−7)`** — *all quadratic* |
| **`5₂`** (control) | 0-dim | 13 | **`ℚ(√5)`**, a cubic, a quartic, a sextic — *higher degree* |
| `3₁` (trefoil, 2nd control) | **1-dim** | ∞ | positive-dimensional (torus knot, non-hyperbolic): no discrete field |

- **fig-8 = `ℚ(√−7)` CONFIRMED, exactly.** One elimination gives `(c−1)·(4c²−c+4)`, disc `1−64 = −63
  = −7·3²` → `ℚ(√−7)` — Chat-2's polynomial reproduced bit-for-bit. The other quadratic factors
  (`x²+x+1` etc.) are `ℚ(√−3)` = the Sym² of the fig-8 SL(2) **geometric** rep (its own trace field).
  So the 3 components of B71 realise concretely: **V0 geometric over `ℚ(√−3)`, W1/W2 over `ℚ(√−7)`.**
- **`5₂` is NOT `ℚ(√−7)`.** Its SL(3) reps need `ℚ(√5)` **plus genuine cubic/quartic/sextic fields.**
  The literal "distinguishing" branch of Chat-2's test fires.

## Verdict — distinguished, YES; a fingerprint, NO

The SL(3) fields differ. But this does **not** clear the emergence/fingerprint bar, for three
independent reasons, each fatal on its own:

1. **The separation is inherited from SL(2), not created at SL(3).** `4₁` and `5₂` already have
   *different* SL(2) invariant trace fields — `4₁ = ℚ(√−3)` (disc −3, **arithmetic**, the Bianchi
   group PSL(2,ℤ[ω])); `5₂ =` the cubic `ℚ[x]/(x³−x²+1)` (disc −23, **non-arithmetic**)
   (Maclachlan–Reid, standard). They are **not commensurable**. So SL(3) is not "the rung that
   distinguishes the figure-eight" — arithmeticity does, one level down. fig-8's SL(3) reps staying
   over *quadratic* fields while `5₂`'s require cubics/quartics/sextics is a *reflection* of that
   arithmetic/non-arithmetic dichotomy, not a new invariant.
2. **The control is not tight enough to license "unique."** "figure-eight-unique" (Inversion Law
   tier 3) would require knots that ARE SL(2)-commensurable with `4₁` to *diverge* at SL(3). `5₂`
   isn't commensurable, so this comparison can only show "two non-commensurable knots have different
   SL(3) fields" — the generic expectation. It refutes "shared" but cannot establish "unique."
3. **`ℚ(√−7)` is not new and not novel.** It is (i) **Falbel 2008's** field for the figure-eight's
   boundary-unipotent SL(3,ℂ) / spherical-CR representation — a KNOWN computation, matched by
   Heusener–Muñoz–Porti (arXiv:1505.04451); and (ii) the program's **already-banked chirality field**
   ([[B316]]/[[B147]]: the invariant trace field of the chiral `RRL/RLL` once-punctured-torus
   bundles). So "fig-8 SL(3) = `ℚ(√−7)`" reproduces two independently-known facts.

## The one genuinely interesting (but decorative) cross-reference

`ℚ(√−7)` now appears **twice** in the object's arithmetic by two different mechanisms: as the SL(2)
trace field of the fig-8's *chiral cousins* (`RRL/RLL`, B147/B316) **and** as the SL(3) field of the
fig-8 *itself*. Note the tension: `4₁` is **amphichiral**, yet its higher-rank arithmetic surfaces
the **chirality** field. This is coherent with B316's two-regime picture (amphichiral ladder
`{√−3, √5, i}`; chiral `√−7`) — the chiral regime reappearing at SL(3) — but it is a **post-hoc
resonance, not a forcing**: `5₂` equally surfaces the *golden* field `ℚ(√5)` at SL(3) while having
nothing to do with the golden object. Filed as decorative, not bankable.

## Placement in the Inversion Law

fig-8's SL(3) field `ℚ(√−7)` is **tier 1–2** (forced by arithmeticity / already-known / already-banked),
**not tier 3** (figure-eight-unique). The Child-Program zero-bar verdict extends to SL(3): the object
produces no rank-3 arithmetic that a standard property (arithmeticity) + a known 2008 computation
doesn't already account for. Every value launders; this one launders through Falbel + Bianchi.

## Reproduce

```
# under pyenv (SnapPy):
python3 extract_ptolemy.py          # -> sl3_ptolemy.json  (bundled; regenerate if desired)
# then:
sage sl3_field_control.sage         # exact elimination fields, no magma
```

**On magma:** not required and not installed. Magma (Univ. Sydney CAS) is proprietary,
license-only — no Homebrew/pip/apt formula exists. SnapPy's `.compute_solutions()` would call it,
but Sage's open-source `elimination_ideal` computes the exact fields directly, in seconds, which is
what settled this control.
