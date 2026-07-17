# B664 — THE METALLIC HEARING LANDSCAPE: verified, PROVED, and
# adjudicated (main seat, 2026-07-17; chat1's handoff archived here)

## THE LANDSCAPE THEOREM (proved; landscape_verify.py, exact + 38/38)

At the golden stage SU(3)₂, for the metallic word R^{n−2}L (trace n):
the θ-odd block is 2-dimensional and T-diagonal, so

> tr_odd(n) = t₁^{n−2}·X₁₁ + t₂^{n−2}·X₂₂ — a two-term exponential
> sum — with EXACT T-phases t₁ = e^{2πi·2/15}, t₂ = e^{2πi·8/15}
> (from h(0,1) = 4/15, h(0,2) = 2/3, c = 16/5: pure h-arithmetic),
> and |X₁₁| = |X₂₂| = √3/D (D² = 3φ√5).

Consequences, all now THEOREM-grade:
- **The closed form:** |tr_odd(n)| = (2√3/D)·|cos(π(4n−5)/10)|
  (38/38 exact-to-1e-9 against the banked stage build).
- **The three-value theorem (V1):** the values are exactly
  {0, 1/φ, 1} by the EXACT golden-trig identities
  sin²72° = D²/12 and sin²36° = D²/(12φ²) (sympy-exact, zero
  simplification residue).
- **Period 5 (V2):** t₂/t₁ = e^{2πi·2/5} is a primitive 5th root ⇒
  the MODULUS has period 5 in n; the mechanism chat1 guessed (R⁵
  central-ish) is precisely this phase-ratio arithmetic.
- **The palindrome (V3):** |cos(π(4n−5)/10)| is even about the deaf
  point — automatic from the closed form.
- **Reality has period 15**, not 5 (t₁ has order 15): tr_odd is real
  exactly at n ≡ {0, 3, 5, 6, 9, 10, 12} mod 15.

## The refutations (verify-don't-trust, as always)

- **chat1's Fact 2 ("the golden is the ONLY real minimum") is
  REFUTED:** quiet+real happens at n ≡ 3 or 12 mod 15 — witnesses
  n = 12, 18, 27, 33 all have |tr_odd| = 1/φ AND Im = 0. The
  mechanism is the mod-15 phase lattice, NOT amphichirality; the
  attribution "det(A−I) unit forces reality" is wrong (n = 12 has
  det(A−I) = −10).
- **The "five independent criteria" collapse:** the conductor is
  (n−2)(n+2), so PRIME CONDUCTOR ⟺ n−2 = 1 ⟺ UNIT det(A−I) — chat1's
  criteria 4 and 5 are the SAME criterion, and criterion 2 is false.
  What survives: the golden is the FIRST (least-trace) quiet point,
  the unique unit-determinant word, and the origin offset of the
  period — genuine but fewer and weaker than claimed.
- The owner's in-message residue guess (n mod 5 ∈ {1,4} quiet) was
  self-corrected in the same message; the verified law is
  (n−3) mod 5 ∈ {0,4} quiet, {1,3} loud, {2} deaf.

## What genuinely feeds L91 (the honest yield)

The landscape is a REAL new datum for stage selection: at the stage
κ = 5, the hearing of EVERY metallic word is governed by the golden
word's own conductor — the period of the landscape equals 5 = tr²−4
at the golden point, and the golden word attains the minimum nonzero
modulus 1/φ. The "self-referential fixed point" framing is
FIREWALLED (a reading, not a theorem); the banked mathematical
content: **the landscape's period = the conductor of the word at its
origin, and the golden word is the unique unit-determinant word of
the family** (one criterion, not five). Registered against L91's
obligations (1)–(3) as supporting structure, not as their discharge.

## Follow-on cells (registered as L107; chat1's V4/V5 + S1–S3)

The cross-landscape matrix (words × stages: does each word hear
minimally at its own conductor's stage?); the E₆-level-2 version;
the silver at its own natural stage (1/δ?); the generating-function
question (the Dirichlet-character mod 5 shape is now THEOREM-adjacent
via the closed form). Gate 5: chat1's hierarchy remark stays behind
the firewall (interpretation, recorded, no action).

Artifacts: METALLIC_LANDSCAPE_HANDOFF.md (archived, privacy-clean),
landscape_verify.py, landscape_output.txt. Locks:
tests/test_b664_landscape.py.
