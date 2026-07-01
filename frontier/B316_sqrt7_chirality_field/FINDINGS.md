# B316 — H32 answered: `√−7` is the *chirality* field, not a metallic-ladder rung

**Status: banked (frontier). *Refines* H32 (already CLOSED by B235). Firewalled; nothing to `CLAIMS.md`.** B234
(chat-2's trace-1 congruence law) predicted `ℚ(√−7)` as "the next imaginary rung after `{5, −3}`," and **B235 closed
H32**: `ℚ(√−7)` does *not* appear in the figure-eight's covers (≤deg 6, all keep `ℚ(√−3)`) or the metallic ladder ("the
trace-1 ladder closes at `{√5,√−3}` by unimodularity"). B316 **refines** that closure two ways: (i) the *precise*
floor mechanism, and (ii) the cross-reference — noted nowhere in B235 — that `ℚ(√−7)` **does** appear in the object's
broader family, as the *chirality* field (B147). Together they complete the picture: the ladder is amphichiral, `√−7`
is chiral.

## The metallic imaginary floor
The metallic monodromy is unimodular (`det = ±1`); a trace-`t` element has `disc = t²−4·det`. On the **imaginary** side
(`disc < 0`), the reachable discs are exactly:
- `det=+1, t=0 → −4` (`ℚ(i)`, the `RRLL` bundle),
- `det=+1, t=1 → −3` (`ℚ(√−3)`, the `RL` = figure-eight bundle).

So the imaginary metallic ladder **floors at `disc = −4`** (`|disc| ≤ 4`). These are the **amphichiral** fields.

## `ℚ(√−7)`: permitted by the congruence, forbidden by the floor
- `−7 ≡ 1 (mod 4)` — it **passes** the trace-1 congruence law (`disc ≡ 1 mod 4`).
- but `−7 < −4` — it is **below the unimodular imaginary floor**, so **unreachable by any unimodular monodromy**.

The two conditions are *distinct*: the congruence is necessary but not sufficient; the floor is the additional
constraint. `−7` is permitted-by-congruence, forbidden-by-floor.

## Yet `√−7` is in the object's arithmetic — as the chirality field
Cross-referenced against **B147** (verify-don't-trust confirmed): the **chiral pair `RRL/RLL`** are *arithmetic*
once-punctured-torus bundles with invariant trace field **`ℚ(√−7)`** (a mirror pair; `vol = 3 ×` the Bianchi covolume
of `ℚ(√−7)`). The amphichiral bundles in range give `RL → ℚ(√−3)`, `RRLL → ℚ(i)`.

## Verdict
The metallic imaginary ladder `{ℚ(√−3), ℚ(i)}` does **not** extend to `ℚ(√−7)` — `disc −7` is below the unimodular
floor. `ℚ(√−7)` is reached instead by **breaking amphichirality** (the non-palindromic `RRL/RLL` words, B147). So
**`√−7` is the chirality field** — a third arithmetic at a *different mechanism*, not a monodromy-ladder rung. H32's
prediction (`−7` appears in the object's data) is **confirmed**, but the mechanism is corrected: it is *chirality*, not
the ladder. The object's arithmetic self-generation has two regimes: **amphichiral** (the metallic ladder — the two
ends `ℚ(√−3)` Eisenstein / `ℚ(√5)` golden, plus `ℚ(i)` at the floor) and **chiral** (`ℚ(√−7)`). The imaginary
quadratic *field* is a chirality signature: amphichiral floors at `{−3, −4}`; chirality gives `−7`.

## The fence
Elementary unimodular arithmetic (`disc = t²−4det`, the imaginary floor) + the congruence check + the cross-reference to
B147's banked arithmeticity of `RRL/RLL`. Nothing to `CLAIMS.md`.

`sqrt7_chirality_field.py` (pyenv) · `tests/test_b316_sqrt7_chirality_field.py`. Related: **B147** (the arithmetic
chiral `RRL/RLL` bundles, `ℚ(√−7)`), **B234** (the trace-1 congruence law, the H32 prediction), **B239** (the unimodular
`disc = t²−4det` reconciliation, the `disc=−4` floor), **K017** (chirality is contingent; `RRL/RLL` chiral arithmetic),
**K020** (the two-ended amphichiral arithmetic). Lit: Maclachlan–Reid (arithmetic hyperbolic 3-manifolds; Bianchi
groups).
