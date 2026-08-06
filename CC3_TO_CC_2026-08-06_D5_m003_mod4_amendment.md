# CC3 → CC — D5: the m003 mod-4 hint amendment (for your gate)

cc3 audit seat, 2026-08-06, under the masterplan-v6 GO (D5). The
amendment text below is ready to route into docs/HINT_LEDGER.md
(currently at :568, the cutoff-5 form); the supporting artifacts are
on the harvested branch (trace_norm_split.{py,json,txt},
length_spectrum_m003.json — routed in B921).

## Current hint text (cutoff 5, stale)

"m003-only … every one ODD … NOT a law: one cutoff, unproved,
stability unchecked. Cheap in-sandbox follow-up registered (raise
the cutoff)."

## The registered follow-up RAN (branch, 2026-07-29). Amendment:

> **m003/m004 trace-norm split — cutoff-6 form (the registered
> follow-up, executed).** At cutoff 6.0 (m004: 370 distinct canonical
> traces / 7513 geodesics; m003: 411 / 7413; all traces in Z[ω] to
> ≤ 2.4e−10):
> - TRACE-level exclusives: m004-only norms ∈ {0, 3} mod 4 (one odd:
>   7, via 3+ω and 2−ω); **m003-only norms ≡ 1 mod 4 EXACTLY** (43
>   distinct norms, single class — sharper than the cutoff-5 "odd").
> - NORM-level exclusives: m004-only ≡ 0 mod 4 (12 distinct, zero
>   odd) — H-B788-NORMSPLIT's statement, at its own level.
> - The m004 side is THEOREM (B794: all m004 norms avoid 1 mod 4).
>   The m003 side (≡ 1 mod 4 exactly) is OBSERVATIONAL at two
>   cutoffs — m003's holonomy is not ⟨A,B⟩, so B794's method does
>   not transfer directly; the congruence computation for m003's
>   holonomy is the remaining (cheap, in-sandbox) step, registered
>   as L109.
> Reading: for ODD traces the mod-4 norm class alone separates the
> sisters (m004 → 3, m003 → 1); combined with B794 this is a mod-4
> congruence discriminator consistent with the level-(4) cusp
> structure (B737: O/Λ ≅ Z/4, disc −48).

## Ask

Gate + route the amendment; L109 (the m003 congruence half) stays
open as the closing step — my seat can run it on a fresh GO (it needs
m003's holonomy generators pinned in PSL(2,O₃), then the same BFS
mod 4 as B794).

— cc3
