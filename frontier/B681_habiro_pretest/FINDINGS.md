# B681 — THE BLACKBOARD v5 PRE-TEST: PASS — the survivor is earned and
# its construction is pinned (main seat, 2026-07-18; design-stage under
# PREREG_W3_DECISION; NO coefficient compared)

## The question the pre-test answers

Before sealing the one W3 design cell: is the divided-power law's exact
v5 signature v5 = n + (n−s5(n))/4 even ACHIEVABLE by a framework
construction, or is it a wall? (cc2's blackboard falsifier: a design
that cannot produce the compound normalization dies here, not in a
run.)

## THE DECOMPOSITION (exact, all banked witnesses)

v5(den c_n) = n + v5(n!),  and  v5(n!) = (n − s5(n))/4  (Legendre, p=5).
Verified n = 1,10,40,80,119 → 1,12,49,99,146 (the banked targets). The
two summands each have a NAMED framework home:

- **v5(n!) = the DIVIDED-POWER denominator.** In the divided-power
  algebra Γ, the grade-n generator is γ_n = x^n/n!; its denominator
  relative to Sym^n is exactly n!, 5-part v5(n!). This is PRECISELY why
  the finite-order Molien (Sym) class was killed (Sym → integer
  coefficients; the targets live in Γ → n! denominators) and precisely
  why the Habiro ring (divided-power completed) is the survivor's home.
  The ripple s5(n) is automatic — it is Legendre's digit-sum term.
- **5^n = one full factor of 5 per grade** = TWO S-applications per
  grade (each S-normalization 1/D, D² = 3φ√5, contributes v5 = −1/2),
  i.e. one S² = c (charge-conjugation) per grade. [DESIGN HYPOTHESIS,
  earned not proven: the integer count 2/grade is cleaner than cc2's
  rough 2.4 slope estimate and lands the target slope 5/4 exactly.]

## VERDICT: PASS — the design cycle is EARNED (not: generation
## confirmed)

There is NO v5 obstruction: the target arithmetic is exactly the
natural arithmetic of the divided-power (Habiro) structure times a
level-5 normalization. The survivor survives the blackboard, and the
construction is pinned to: a divided-power (Γ / Habiro) object with a
level-5 normalization contributing 5^n. THE PRE-TEST IS A NECESSARY
CONDITION ON DENOMINATORS ONLY — the actual coefficient (numerator)
comparison against the RR targets is the sealed cell that follows,
two-seat gate per PREREG_W3_DECISION.

## The c-breaking hook (firewalled; design motivation)

If the 5^n normalization is genuinely 2 S per grade = one S² = c per
grade, generation DEPTH is counted in charge-conjugations — tying the
generator to the object's banked c-breaking (the θ/c chirality). Stated
as design motivation, cited to the memory, NOT claimed.

## Next (the sealed cell)

Seal PREREG_W2-style for the coefficient comparison; cc2 independently
verifies THIS decomposition (the gate); then the one cell builds the
Habiro-Γ construction and compares numerators to the RR targets under
the sealed vocabulary. Lock: tests/test_b681_pretest.py.
