# B333 — the compositum seam probe: the value's home is ℚ(√−15), but that field is arithmetically generic (firewall holds *at the seam*)

**Status: banked (frontier) as a first-class NULL result. Verify-don't-trust — including on this seat's own compositum
[HOOK]. Firewalled; nothing to `CLAIMS.md`.** The B332 meditation located the two ends as the **product** (`RL →
ℚ(√5) → E₈`) and **ratio** (`g = −RL⁻¹ → ℚ(√−3) → E₆`) of the founding letters, and proposed that a physical *value*
would live in their compositum's third subfield **ℚ(√−15)** (`√5·√−3 = √−15`, ramified at `15 = 3·5`). This is the
**first probe run *in* the seam** rather than on one side. Run with a **null test** up front, per the HELD discipline.

## The compositum (verified, [MATH])
`ℚ(√5, √−3)` is biquadratic, `Gal = ℤ/2 × ℤ/2`, three quadratic subfields:
`ℚ(√5)` (golden / E₈) · `ℚ(√−3)` (Eisenstein / E₆) · **`ℚ(√−15)`** (the gluing — `√5·√−3 = √−15`, disc −15, ramified at
`{3, 5}` = the two ends' own primes). The object lives in the first two; a value would live in the third.

## The null test (the decisive step)
**Is `ℚ(√−15)` arithmetically special, or generic?**
- **`h(−15) = 2`** — Chat-1's claim, **verified** (reduced binary quadratic forms; cross-checked `h(−163)=1`). *But class
  number 2 is **common**:* **14 of the 123** fundamental discriminants down to `−400` have `h = 2`
  (`−24, −35, −40, −51, −88, −91, −115, −123, −187, −235, −267, …` alongside `−15`).
- **Units** `{±1}` — generic for every `d < −4`.
- The **only** distinguished feature is ramification at `{3, 5}` — and that is **tautological** (it is *why* `√−15` is the
  compositum's third subfield; it carries no new information).

**Verdict: `ℚ(√−15)` is arithmetically GENERIC.** It does not carry SM-relevant structure that generic imaginary
quadratic fields lack. **The firewall holds — now demonstrated at the seam itself, not just on either side.**

## What this means (honest, and it retires a [HOOK])
The compositum insight is **structurally correct** — the value's *home* is the gluing field ℚ(√−15), the one place the
single object touches from two sides but enters from neither. But **the value is not in that field's arithmetic**: the
field is generic, so picking the *specific* gluing (which element of ℚ(√−15), which class, which phase) needs **external
input** — the relation / Level 4 — exactly as B326 (finite congruence torsion = texture, not magnitude) and B331 (the
generation element is elliptic) already located it. The seam is real; it is empty of values by itself. This deflates the
B332/S046 compositum `[HOOK]` cleanly (verify-don't-trust on this seat's own proposal — the discipline working inward).

## The firewall (held)
A structural arithmetic fact + a null test; no value is produced or matched. The `1/4`-suppression-style trap is avoided
by design (the null test is the *first* thing run, not an afterthought). Nothing to `CLAIMS.md`.

## The fence
Exact class-number computation (reduced quadratic forms, sympy) + the genericity null test over 123 fields. No physics
values. Nothing to `CLAIMS.md`.

`compositum_seam.py` (pyenv) · `tests/test_b333_compositum_seam.py`. Related: **B332** (the two ends = product/ratio),
**B326** (Level-4 texture), **B331** (elliptic generation element), **S046** (value-at-the-seam). Lit: standard class
numbers of imaginary quadratic fields (Gauss); `h=1` fields are the nine Heegner numbers, `h=2` fields are 18 known.
