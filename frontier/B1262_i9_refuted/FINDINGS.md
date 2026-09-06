# B1262 — I-9 REFUTED: there is no "genus V₄" for discriminant −15, and the row had carried its own discriminator unrun

**Date:** 2026-09-06 · **Seat:** cc · **Status:** NEGATIVE (exact; class-number routine validated on five known values, and a two-directional control)

## Why this arc, and the third move B1261 exposed

**B1261** measured the trade at **15 unpriced inputs : 0 of the SM's 19 numbers**, and named two ways
to move it — **earn** an identification (−1) or **derive** a parameter (+1). The ratchet's own
arithmetic contains a **third**, cheaper than either: **REFUTE** an identification, which also removes
a row from the UNEARNED set.

**I-9** was the obvious candidate, because **the row already contained its own discriminator, written
and never run**: *"the genus group of disc −15 has order 2^(t−1) = **2**, not 4."*

## The computation

| | |
|---|---|
| disc −15 reduced primitive forms | **{(1,1,4), (2,1,2)}** → **h(−15) = 2**, class group **ℤ/2** |
| −15 = (−3)(5), so t = 2 | number of genera = **2^(t−1) = 2** |
| genus group = C/C² with C = ℤ/2 | **ORDER 2** |
| Gal(ℚ(√−3,√5)/ℚ) | **(ℤ/2)², ORDER 4** |

> **There is no "genus V₄" for disc −15.** The genus group is **ℤ/2**. The object the row **names**
> does not exist, so the identification is **false as stated**.

## And the fallback reading fails too, on the programme's own rules

Reading side B as **Gal(ℚ(√−3,√5)/ℚ)** does give order 4, matching the glue's order. But:

- that is an **ORDER MATCH**, and **B1223** established order matching is not a connection —
  *"Direct is not semidirect"*: the groups matched, the **action** did not;
- **B155's own row** calls the glue a **GL(4,ℤ)-class invariant** *"not forced by the spectral type"* —
  **lattice** data, while Gal is **field** data. A map from field data to something **not determined
  by** field data cannot be canonical.

So neither reading survives: the named object doesn't exist, and the substitute rests on exactly the
evidence the corpus forbids.

## Controls (MB12, both directions)

- **The class-number routine is validated against five known values before being trusted** —
  h(−15)=2, h(−23)=3, h(−4)=1, h(−3)=1, h(−47)=5. **This caught a real bug:** a first draft of the
  reduction filter returned **h(−15) = 3** by admitting **(1,−1,4)**, which is *not* reduced (b ≥ 0 is
  required when |b| = a). Without the validation the headline number would have been wrong.
- **The test can come out the other way:** discriminants with t = 3 (**−84**, **−120**) **do** give
  **4** genera — so "order 2" is a fact about **−15**, not about the method.

## The price

**UNEARNED 11 → 10.** The trade moves from **15 : 0** to **14 : 0** — the first reduction, and it came
from running a discriminator the register had been carrying all along.

## Verification

`verification/genus_v4_does_not_exist.py` — standalone.

- **Feeds on:** B1261 (the price and the moves), B1233/B1234 (the proposal), B155 (the glue and its
  "not forced by the spectral type" scope), B1223 (order matches are not connections), B1231.
- **Registers:** **I-9 REFUTED** (documented ratchet lowering 11 → 10).
