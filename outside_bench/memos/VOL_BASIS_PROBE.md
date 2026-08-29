# THE VOLUME-IN-BASIS PROBE — the corner is closed NEGATIVELY: even with the object's own canonical regulator in the basis, no SM target involves a regulator
## (outside bench memo 141, 2026-08-29; seal `seals/VOL_BASIS_PREREG.md`, committed and pushed BEFORE any computation; outcome **V-NEG**, as preregistered)

**The corner.** Memo 139 found, while re-checking a staleness flag, that
**B1137's regulator basis omits the complex volume** — while **B1209**
banks (citing Lee) that the complex volume **is** a Beilinson regulator
over ℚ(√−3), the object's own field. **The object's most canonical
regulator was absent from the regulator probe.**

**The honest prior, written into the seal: a ninth value-crossing
negative.** The cell was run to close the corner, not to expect a hit.

## THE TWO PRE-STEPS, BOTH OF WHICH COULD HAVE KILLED THE CELL

**Seal §4 — hygiene (target-free).** PSLQ at **dps 220, H = 10⁶** against
B1137's 25-element pruned basis: `vol`, `vol_pinorm`, `vol_over_zetaK2`
all **INDEPENDENT**, **0 dropped**. The corner is a genuinely new
direction, not a redundancy. *(B1137's own hygiene check found and dropped
six exact redundancies, so the instrument does detect dependence.)*

**Seal §5 — the gating reproduction control.** Full 216-cell grid on the
**unmodified** basis, in this bench's hands, at the pinned commit:

| | control (25 entries) | extended (28 entries) |
|---|---|---|
| cells | 216 | 216 |
| raw PSLQ relations | 117 | 108 |
| passing `involves_V` | 117 | 108 |
| **passing `involves_regulator`** | **0** | **0** |
| targets involving a regulator | **NONE** | **NONE** |

**B1137's headline — *"0 of 18 targets involve a regulator at all"* —
reproduced exactly.** Only then was the extended run authorized.

## THE RESULT — OUTCOME V-NEG

> **With `vol`, `vol_pinorm` and `vol_over_zetaK2` in the basis, ZERO of
> the 18 sealed SM targets yields a bounded-height algebraic combination
> involving any regulator.**

**B1137's DISJOINT verdict extends to a basis containing the object's own
canonical regulator.** The corner memo 139 named is **closed
negatively**, and this is the **ninth** value-crossing negative in the
record.

## THE 117 → 108 DIFFERENCE, EXPLAINED RATHER THAN WAVED

Nine cells found a raw relation in the control and not in the extended
run — **all nine are the same target, `|Vub|`**, evenly across D and H.
The reason is exact: **|Vub| carries `digits = 1`**, so it truncates to
0.004, and its "relation" is literally

> **−1 + 250·V = 0**, i.e. **V = 1/250**, with **every regulator
> coefficient zero.**

That is precisely the **V-alone tautology** B1137 itself identified and
gated. Adding basis directions perturbed PSLQ's convergence on that one
degenerate case. **Its content was zero in both runs, and no hit is
masked** — the decisive column (`involves_regulator`) is **0 in both**.

## WHAT THIS BUYS, STATED WITHOUT INFLATION

**It does not** discover anything. **It removes a named way the record's
strongest negative could have been wrong.** The value wall's regulator
probe now stands on a basis that includes the object's own complex
volume, which it previously did not — and the finding that it *didn't*
came from re-checking my own false-positive staleness flag, not from a
search for it.

**Gate 5:** measured values entered **only as comparison targets for a
computed negative**. The B743 targets were loaded verbatim,
**sha256 `e93efeaa132bf7c1a6e0a3a9d41a436ff03d2aea5f626a2b404a5ef8a317e101`**,
18 targets, not re-selected here. **No measured value touched the basis.**
Vol(m004) was **computed** from ½·Im Li₂(e^{2iθ}) at θ = π/3 — matching
the known value to 30 dps — **not quoted**.

**Fence.** This tests bounded-height algebraic combination at the declared
heights and precision, exactly as B1137 did. It is not a proof that no
relation exists at any height. Seal §3's four hit-gates were never
reached, because no candidate passed the first.
