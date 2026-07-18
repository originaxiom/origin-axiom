# THE DIVIDED-POWER LAW (main seat, 2026-07-18; found by interrogating
# the negatives; exact, two-outcome, all-n verified)

## The law

The 5-adic denominators of the target carrier (q;q)^{-3/5} are EXACTLY
the divided-power denominators: for every n = 1..120,

    v₅(den c_n) = v₅(5ⁿ · n!) = n + (n − s₅(n))/4     (s₅ = base-5 digit sum)

EQUALITY at all 120 coefficients — the leading 5-adic term never
cancels. All five banked kill witnesses (1, 12, 49, 99, 146 at
n = 1, 10, 40, 80, 119) are reproduced exactly. The asymptotic slope
is p/(p−1) = 5/4 — explaining the observed secant band [1.205, 1.25]
exactly (it creeps to 5/4 as the digit-sum ripple thins).

## The mechanism reading (what the eight kills + this law say together)

1. The targets are, 5-adically, a GENUINE EXPONENTIAL: c_n = a_n/(5ⁿn!)
   with a_n 5-integral — the divided-power fingerprint of exp at p = 5
   (mechanism sketch: (q;q)^{−3/5} = exp(−(3/5)log(q;q)); the log has
   1/m-integral coefficients; the 3/5 contributes one 5 per power, exp
   contributes n! — the EQUALITY at every n is the computed content).
2. The denominators COUNT OPERATIONS, not values: one 5 per grade plus
   a full n! symmetrization — the plethystic-exponential shape with
   per-grade normalization 1/(5m). A fixed operator produces none of
   this (the kills); a grade-growing construction must produce ALL of
   it, ripple included.
3. THE FRACTIONAL WEIGHT CLOSES ITS LOOP: weight 1/5 is where the
   banked golden-rotation lift became finite-order, and 1/5 is exactly
   the fractional power whose 5-adic shadow is the divided-power
   denominator ladder. The generator must "take a 5th root" — the one
   operation no integral construction performs.
4. THE BIFOCAL ARITHMETIC ASYMMETRY: the being prime 3 appears in NO
   denominator (verified all 120). Generation DEPTH is purely a
   golden-prime phenomenon; the being end can enter only integrally
   (numerators/structure constants). Consistent with, and sharpening,
   the bifocal adjudication.

## The design consequence (class 7's obligation, sharpened to exact)

Any surviving depth-graded design must reproduce v₅ = n + (n−s₅(n))/4
EXACTLY — including the base-5 digit-sum ripple — not merely a slope
in [1.205, 1.25]. This is a per-n blackboard falsifier.

## Gate-neutrality note

Banked during the W3 gate window: this law changes NO class-list entry
and NO exclusion verdict — it sharpens a design obligation of the
already-named candidate-survivor. The enumeration comparison is
untouched. Script: divided_power_law.py (+ output); lock
tests/test_divided_power_law.py.
