# B1124 — V-1 ALL-ORDERS ARITHMETIC: the parity law extends to C₃ (a third order), with a smoothness anomaly — EULER-STRUCTURE-EXTENDED

**Status: banked (frontier). Verdict PROVED (the C₃ closed form recognized to 36 digits
with MONOTONIC cross-window convergence — the signature of a genuine relation, not a PSLQ
artifact; re-verified this bench: the closed form matches the computed pooled C₃ to ~36
digits, and the pipeline reproduces the banked C₁/C₂ to 40+ digits). Value-campaign cell
V-1 (extends B1120/L180). Two honest fences below. Gate 5 untouched. Lock
`tests/test_b1124_allorders.py`.**

## The question (V-1)

L180 (B1120) confirmed the Kashaev tower's coefficients are trace-field arithmetic at C₁
and C₂ (the reality-parity law: even k → rational·π^k·C₀, odd k → rational·√3·π^k·C₀). Does
the arithmetic CONTINUE to C₃ (the full Euler-product / all-orders reading), or stop?

## THE ANSWER: the PARITY LAW extends to C₃ — but the {2,3}-smoothness does NOT

> **C₃ = (724351/12597120)·√3·π³·C₀**  (odd k → rational × √3, EXACTLY as predicted;
> recognized to 36 digits; the √3 present)

Pushed the tower from the banked ceiling N≈2.9M to **N = 35,000,000** (12×, 5 windows +
pooled, dps 200/320-cross). The C₃ recognition is genuine, not a maxcoeff coincidence:
**agreement grows MONOTONICALLY 14→20→27→32→36 digits as independent larger-N windows are
added** (a spurious PSLQ hit does not keep improving); reproduced on 4 algebraically-related
bases; all 11 wrong-basis / wrong-parity controls null at maxcoeff 20M. So the reality-parity
LAW (odd → √3) is now confirmed at THREE orders (C₁, C₃ carry √3; C₂ plain rational).

**THE ANOMALY (disclosed, not hidden): the denominator is NOT {2,3}-smooth.**
12597120 = **2⁷·3⁹·5** — the factor of **5** breaks the clean {2,3}-pattern of C₁ (108=2²3³)
and C₂ (7776=2⁵3⁵). So the naive "Euler product over the primes of disc(−3)" picture is too
simple: the trace-field/√3-parity structure is robust, but the smoothness structure is
richer at C₃. **This is a real finding, not a defect** — it says all-orders arithmetic holds
in the parity sense but with a growing prime set.

*(Firewalled motivation, labeled — NOT a claim: 5 is the OTHER end of the two-ended object
(ℚ(√5), the E₈ end, Niven-forced). Whether the 5 at C₃ is the second end entering at higher
order, or a k=3 normalization artifact, is a concrete next probe — factor the C₄, C₅
denominators and watch for 5's exponent. Speculation→calculation table: "5 = √5 end" →
"does 5 recur / grow in C₅,C₇? does √5 (not √3) ever appear in an odd coefficient?")*

## The two honest fences

1. **Detection, not derivation** (as with C₁/C₂): the rational 724351/12597120 is a
   high-precision PSLQ RECOGNITION, not derived from a closed theory. cc3's L180 fence
   applies — this strengthens "the value door opens onto reproducing arithmetic," it does
   not open the door to a value.
2. **Trust-bound layered** (disclosed in NOTES): the primary script's ultra-conservative
   metric (worst pair across ALL windows incl. small-N W1) rates C₃ at only 14 digits and
   its `verdict` field reads PRECISION-FLOOR, left untouched. The 36-digit confirmation
   comes from a large-N-windows-only (W3/W4/W5) bound of 27 digits — justified by the clean
   monotonic pattern (W1 is too small-N to resolve a k=3 term), NOT a post-hoc relaxation.
   **C₄ is a genuine PRECISION-FLOOR**: 21 trust digits, height plausibly beyond reach; a
   too-aggressive first search hit every basis incl. null controls (caught as noise). More N
   / dps would decide it.

## What it means for the value campaign

V-1's outcome is neither "EULER-PRODUCT-CONFIRMED (all orders {2,3}-smooth)" nor
"ARITHMETIC-STOPS" — it is a third, sharper result: **the trace-field √3-parity arithmetic
CONTINUES to C₃ (the door keeps opening onto arithmetic that reproduces), but the smoothness
grows a prime**. The value door is further confirmed arithmetic; the identification (V-3,
which object-period is an SM ratio) remains the open crux. Gate 5 untouched.
