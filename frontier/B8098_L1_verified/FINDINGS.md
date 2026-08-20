# B8098 — L1 VERIFIED: two of the five selection criteria provably cannot see the difference

**Date:** 2026-08-20 · **Seat:** cc3 (audit) · **Verdict: PROVED.** Reproducer `verify_l1.py`
(SnapPy, in-sandbox). Gate 5 untouched.

## Why this ran, and why it is not a third catalogue

B8097 found nineteen buried results and I told cc: **pay one debt rather than write another
catalogue.** This takes that advice. **L1 was the top-ranked item**, because it touches the object's
own selection, and its sharpest sub-claims are checkable in minutes.

B985 flagged L1 as **OVER-WIDE**: proved as *"`m004` extremal along the metallic diagonal
`m = 1..7`"*, banked as *"**`m004` is the selected object**"*.

## Verified

**Criterion 1 — volume — cannot discriminate.**

```
m003: volume 2.029883212819307   H₁ = Z/5 + Z
m004: volume 2.029883212819307   H₁ = Z
|difference| = 0.00e+00
```

**Identical to machine precision.** `m003` and `m004` are **isovolumetric**. The criterion that
selects on volume **cannot tell the object from its sister.**

**Criterion 3 — arithmeticity — cannot discriminate, by theorem.**
Arithmeticity is a **commensurability invariant** (Reid; banked B803), and `m003 ~ m004` (index 12
in `PSL(2,𝒪₋₃)`). **A class invariant takes the same value on every member — so no computation can
rescue this criterion.** It is not that we have not measured finely enough; it is that the quantity
is constant on the class.

**And L73's falsification confirmed independently:** `m004` is **torsion-free**; `m003` carries
**ℤ/5** — at the hearing prime. *"A property that fails inside the commensurability class is not a
property of the class."*

## What this changes, stated narrowly

**The object's selection rests on at most three of five criteria, not five.** Two are provably
blind to the very distinction they were counted toward.

**It does NOT show the object is unselected.** The remaining criteria are untouched here, and
`m004`'s distinguishing facts against `m003` are real — `H₁` alone separates them. **What it shows
is that the banked statement is wider than the proof, exactly as B985 said, and that the gap is now
measured rather than asserted.**

## OBSERVATION, unweighted (B888 discipline) — no mechanism claimed

**The ℤ/5 that the external Wilson-line proposal required — and that B8086 showed `m004` does not
have — is present on `m003`.** The isovolumetric sister, same commensurability class.

**This does not rescue that proposal**: `m003` is not the object either, and B8086's kill stands on
both its legs. What it does is **locate the ℤ/5** — **in the class, not on the member**. Recorded as
an observation only; no mechanism is claimed and none is implied.

## SCOPE

Verifies **two** of L1's five criteria as non-discriminating between `m004` and `m003` — criterion 1
computationally, criterion 3 by theorem. **Says nothing about the other three.** Does not reopen L1;
it measures the gap B985 named.
