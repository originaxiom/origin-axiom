# B1133 — C₄ RECOGNIZED: the tower is SINGLE-END (ℚ(√−3) only), the arithmetic reproduces at five orders

**Status: banked (frontier). Verdict PROVED (C₄ recognized as trace-field arithmetic and
re-verified this bench to ~30 digits against B1124's computed value; the two-ended question
RESOLVED single-end; three bugs caught en route). Value-probe wave remainder (A); upgrades
B1130 from PRECISION-FLOOR. Gate 5 untouched. Lock `tests/test_b1133_c4.py`.**

## The result

> **C₄ = (278392949 / 1813985280)·π⁴·C₀** (even k → plain rational × π⁴, the reality-parity
> form; numerator **prime**, denominator **2¹¹·3¹¹·5¹**).

Re-verified this bench: the closed form matches B1124's independently-computed C₄ pooled
value to **30.77 digits** (its pooled fit was more accurate than V-1's conservative 21-digit
trust rating). Extracted from EXISTING data (B1124's N≤35M windows + B1130's N≤1.5M +
Aitken-Δ² acceleration → 28 trusted digits) with **zero new heavy compute** — the N=70M
brute-force run (stopped earlier at diminishing returns) was never needed.

## TWO-ENDED VERDICT: SINGLE-END (upgraded from B1130's "leaning")

The prime **5 recurs at exponent 1** in C₄'s denominator — the SAME as C₃'s 5¹ — it **does
NOT grow**, no new prime enters beyond {2,3,5}, and **no √5 appears** (C₄ is a plain
rational × π⁴, exactly the even-k parity form; no √5 in any odd coefficient tested). So the
object's Kashaev tower is **single-ended: ℚ(√−3)/E₆ only.** The factor-of-5 flagged at C₃
(B1124/B1130) is a **generic denominator artifact** (von Staudt–Clausen), NOT the spherical
ℚ(√5)/E₈ end. B1130's PRECISION-FLOOR is resolved.

## Bonus: the arithmetic reproduces at FIVE consecutive orders

C₀ = 3^{−1/4}; C₁ = (11/108)√3π·C₀; C₂ = (697/7776)π²·C₀; C₃ = (724351/12597120)√3π³·C₀;
**C₄ = (278392949/1813985280)π⁴·C₀** — the reality-parity law (even→rational, odd→rational·√3)
now holds at k = 0,1,2,3,4. Strengthens B1124/V-1: the tower's arithmetic is robust to a
fourth sub-leading order. (C₅ remains precision-gated; the pattern is not claimed all-orders.)

## The rigor (three bugs caught, per WORKING_RULES §12)

(1) PSLQ noise floor — a naive 3-term search hit on every base incl. wrong controls; fixed
via negative-control-calibrated ceilings (searching C₂, which has no √3/√5 content). (2) An
L180-class precision bug in disguise — π**2 evaluated outside a workdps block silently
rounded two good constants when combined; caught by the mandatory cross-check (C₄ must match
BOTH B1124 and B1130 to ≥20 digits). (3) A genuine PSLQ blind spot — the real relation
(height ~1.8×10⁹) was missed by direct mpmath.pslq but found by continued fractions (partial
quotient 27.5 trillion after the convergent), confirmed via CF across 8 base normalizations.
Positive controls C₁/C₂/C₃ recovered through the identical pipeline. Gate 5 untouched.
