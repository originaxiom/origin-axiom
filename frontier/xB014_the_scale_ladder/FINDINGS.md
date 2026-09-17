# xB014 — PATH A DIES: the ladder is real and generic, and m004 is rank 38 of 40 on the both-faces ratio

**Status: banked (frontier, `sep16-branch`). Verdict NEGATIVE.** Seat `xb`.
**PREREGISTRATION sealed and pushed BEFORE any cell ran** — sha256
`bc8a71ede6107f3f9e271bed29e7f919b7c49e72ea8bddfac38a8980f765f2f2`, commit `63fc1f1`.
**Short by the owner's rule and by the seal's own commitment to one paragraph if the base rate
came back unremarkable. It did.** Gate 5 untouched.

## The one paragraph

**Z1 PASS — B207 is SCOPED, not disputed.** Its banked negative (*"no intrinsic exponential
hierarchy"*) was **re-derived**, and it tested the **m-family** `RᵐLᵐ`: volumes **bounded**
(2.0299 → 6.3914, ratio 3.1) with `log λ_m` **logarithmic**. This arc's **n-tower** `(LR)ⁿ` is a
different family: volumes **linear and unbounded**, torsion **exponential**. B207's negative does
not cover this path. **Z2 PASS** — the tower's homology torsion is **exactly** `L_n²` (n odd) and
`5F_n²` (n even), rate → `log φ² = 0.9624236501`, reproducing Silver–Williams' Mahler-measure
theorem, which was **verified not assumed** (`M(t²−3t+1) = φ²`). **But that growth is generic to
every fibred knot, so the ladder's existence is not news — only the rate is m004's, and the rate is
just its Alexander polynomial, already banked.** **Z3** — the both-faces ratio `log λ / vol =
0.47412759711555`, **constant along the tower** (verified n = 1…5) and combining the **golden**
numerator with the **Eisenstein** denominator (`vol = 24·v₀`, `v₀ ∝ L(χ₋₃,2)`); it is exactly the
quantity B207 named as where a hierarchy would enter. **Z4, THE DECISIVE CELL — the base rate kills
it.** Against Kojima–McShane's bound `1/(3π) = 0.1061`, across 40 once-punctured-torus bundles
(cyclically reduced words, length 2–8), **m004 ranks 38 of 40**; the maximum is `t00000` at
`0.636080` against m004's `0.474128`. **m004 is near the bottom, not extremal. PATH A DIES**, as the
seal's declared weak prior expected.

## One correction made before any verdict

A first draft of Z1 asserted a **magnitude** (`torsion₆ > 100·torsion₂`) and it failed at 320 < 500
— a badly chosen test, not a failed fact. Replaced by the property that matters: the **rate**
converges to `log φ²`, and it does.

## What is not claimed

That a dimensionless ladder is a **scale** in the physical sense, or that it crosses B1012's wall —
that wall concerns a **dimensionful** quantity and a ladder supplies a dimensionless **index**. No
identification (E82), no physics reading. Census cutoff (word length ≤ 8, 40 bundles) **reported**;
a longer-word bundle could rank differently, but m004's position at 38/40 is not marginal.

**Provenance.** `verification/scale_ladder.py` (Z1–Z5) → `reproduce.sh`. Re-derives B207
(**SCOPED**), verifies Silver–Williams and Kojima–McShane as cited literature, builds on xB012 (the
two faces), xB013 Addendum 1 (the tower).
