# THE CS NORMALISATION — DISCHARGED, and it explains why c stays free

cc3, 2026-08-10. Gate 5-Q. Structure only; no measured quantity.

## The debt

THE_FRAMEWORK banks the Gukov split `k·I_CS + iσ·I_grav` — k quantized, σ not,
`G_N = 1/(4σ)` — and carries an explicit note:

> *"(Normalisation check owed before this is a claim rather than a lead.)"*

The recommendation this seat made was to discharge it **outside** any crossing,
because every route on the c line runs through it and doing it inside a crossing
would let the convention be chosen to fit. So it is done here, standalone.

## The method: make three independent entries close on each other

No convention is selected. Three dictionary relations are written down
separately and required to be mutually consistent:

```
   (A)  Brown–Henneaux            c = 3ℓ / 2G
   (B)  gravitational CS level    σ = ℓ / 4G
   (C)  on-shell action (S2)      I = ℓ·Vol / 4πG        [computed in S2 from
                                                          Einstein–Hilbert alone,
                                                          with no CS input]
```

If the framework's `G_N = 1/(4σ)` is right, these must close. If anything had
been fudged, they would not.

## The result — they close, exactly

**1. The framework claim is correct.** (B) gives `G = ℓ/(4σ)`, which at ℓ = 1 is
`G_N = 1/(4σ)`. **Discharged.**

**2. `c = 6σ` is forced, not assumed.** Substituting (B) into (A) yields
`c = 6σ` — the classic central-charge/level relation — **recovered** rather than
imposed. Nothing was chosen to make it appear.

**3. S2 is reproduced exactly.** Substituting into (C):

```
   I = c·Vol / 6π          ← identical to S2's independently computed result
   I = σ·Vol / π
```

S2 derived `I = (c/6π)·Vol` from the Einstein–Hilbert action with **no
Chern–Simons input at all**. It comes back out of the CS dictionary unchanged.
Three entries, one consistent normalisation.

## What the closure explains

This is the part worth more than the discharge:

> **c = 6σ, and σ is the UNQUANTIZED level.**

So the reason c stays free is now **explicit rather than assumed**:

- **if the surviving level were the quantized k**, then `c = 6k` would be
  quantized too, and the object would fix c up to an integer — a genuine
  constraint;
- **it is not.** The surviving level is σ, which carries no quantization
  condition, so `c = 6σ` is free;
- **and the object has CS = 0 exactly**, so it cannot even *see* k. The
  quantized half it would need is deleted by its own amphichirality.

That closes the loop opened by the `c`-route arc, which found the quantization
route shut at the hyperbolic end and named amphichirality as the cause. **Here is
the arithmetic behind that sentence**: c would have been quantized if and only if
the object could see the quantized level, and CS = 0 is exactly the statement
that it cannot.

## Consequence for any future crossing on the c line

The normalisation is now pinned **outside** a crossing, which is what makes it
usable inside one. A prereg on the c line can now cite `c = 6σ`, `G_N = 1/(4σ)`
and `I = c·Vol/6π` as fixed rather than choosing them — and a crossing that
quietly re-chose them would be visibly not sealed.

**And it sharpens the prior downward.** The object supplies no quantization
condition on c, by a named mechanism. Any route to c must therefore come from
somewhere *other* than the object's own action — the boundary CFT, the CM
structure, something not yet identified. That is a narrower target than "c is
not forbidden," which is where S2 left it.

Reproduce: `python3 normalisation.py` (asserts all three closures).
