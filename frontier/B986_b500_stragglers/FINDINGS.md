# B986 — the B500 depth-5 reopen attempted: the mod-p route computes the eliminants but the test is VACUOUS

**Date:** 2026-08-09 · **Seat:** cc (banking) · **Lane:** MATHEMATICS. Gate 5 untouched.
**Verdict: NEGATIVE on method. L145a stays OPEN.** The attempt failed on the *instrument*, not on
the object, and it was killed by its own control within minutes of being proposed.

---

## What was attempted

cc3's sweep surfaced **B500** — `revival_score` **6**, the highest in the kill graph, and in **no
register**. Its own text downgrades its kill: *"the KILL is PROVISIONAL … **35 words remain
UNCHECKED** (26 timeouts + 9 never-reached — the D/M-heavy tail whose resultant eliminants blow up
to degree **~3000–9280**, beyond in-sandbox `gp`)"*, and **B525** specifies the reopen: *"re-run the
35 (**𝔽_p Gröbner** or longer timeout)."*

**The proposed route.** K = ℚ[t]/(t⁴−t−1) is S₄-quartic with **no intermediate fields**, so the
child is present for a word iff its eliminant *h* has a root in K. If **p is inert** in K then
𝒪_K/p ≅ 𝔽_{p⁴}, and a root in K reduces to a root in 𝔽_{p⁴}. Contrapositive:

> **h mod p has no root in 𝔽_{p⁴} ⟹ h has no root in K.** *(a proof, not evidence)*

with `gcd(h, x^{p⁴} − x)` by repeated squaring — cheap even at degree 9280. And the *whole*
resultant chain runs in GF(p), so the ℚ blow-up never happens.

## What came back

| | |
|---|---|
| **9 words** | eliminant computed, degrees **6450–7896**, root in 𝔽_{p⁴} at **both** inert primes (5, 19) |
| **26 words** | **degenerate** — the resultant chain vanishes identically (positive-dimensional; these are exactly the words needing `hunt_d5.py`'s **saturation** branch, which this script does not implement) |
| **proved absent** | **0** |

## THE CONTROL — RUN IMMEDIATELY, AND IT KILLS THE METHOD

Before reading anything into "9 of 9 have a root", the MB12 question: **can the test ever return
*no root* at these degrees?**

| p | degree | random polynomials **with** a root in 𝔽_{p⁴} |
|---|---|---|
| 5 | 6500 | **28/40** |
| 19 | 6500 | **29/40** |
| 5 | 74 | **33/40** |

> **≈70% of *random* polynomials pass. "All 9 have a root in 𝔽_{p⁴}" is exactly the base rate —
> zero information.**

The **logic** was correct; the **power** is nil. A degree-6500 polynomial has thousands of roots
across small extensions, so the informative outcome (*no* root) essentially never occurs. **A
criterion that cannot fail is not a test** — MB12, applied to this seat's own instrument.

**And the deeper reason, which generalises:** any test of the form *"does h have a root of type X"*
is saturated at these degrees. A discriminating test must use **the specific field K**, not merely
its degree — i.e. an irreducible degree-4 factor over ℚ whose field is ≅ K. That is what B500's
exact route computes and what the mod-p shortcut cannot reach.

## What genuinely stands

1. **A real instrument gain.** The **eliminants that overflowed the PARI stack over ℚ are
   computable in seconds mod p** — degrees 6450–7896 obtained where the exact route died. The
   bottleneck B500 hit is *not* intrinsic; only the *decisive test* is.
2. **The 26 degenerate words are diagnosed, not lost.** They need the **saturation** branch
   (`I.saturation(...)` then `elimination_ideal`), which `hunt_d5.py` already implements and this
   script deliberately does not. That is the concrete next step, and B525's *"𝔽_p **Gröbner**"* is
   most plausibly exactly this — Gröbner *over* 𝔽_p to handle saturation — rather than the
   root-existence test attempted here.
3. **L145a stays OPEN**, now with a sharper statement of what closing it requires: mod-p elimination
   **with saturation** for the 26, plus a **field-specific** (not degree-specific) decisive test for
   all 35.

## Why this is banked rather than discarded

Because the attractive half is already written down and would otherwise be re-proposed. Recording
*"the mod-p route computes the eliminants"* without *"and its decisive test is vacuous"* would hand
a later seat a method that looks like it works. This is the pattern cc3 used hours earlier on its
own selector reading, and the pattern the day's five errors argue for: **propose and refute in the
same file.**

Reproduce: `sage-python fp_reopen.py 2` (the run) and the control inline above.
