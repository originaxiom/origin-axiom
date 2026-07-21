# ⚠️ THE "REFUTED" HALF RETRACTED BY B742 + B745 (2026-07-21) — the criterion was vacuous

**THE "2 = octahedral parent REFUTED" VERDICT BELOW DOES NOT STAND.** The refutation rested on
"2 appears in the bad-prime extraction of every 2-bridge knot" — but the negatives hunt (B742,
audit seat) proved the extraction reports 2 for EVERY monic-in-z input (disc_z mod 2 is always
a square in 𝔽₂[x] — Vandermonde/Stickelberger; false positives on the 2-good curves 11a3 and
37a1). Specificity at p=2 is ZERO, so the observation carried no evidence either way (MB12
vacuity class). The banking seat cross-verified independently (B745, ALL PASS). Status now:
the octahedral-parent half is **OPEN — undecided**, pending genuine (Jacobian-conductor)
2-parts of non-twist 2-bridge character varieties. The one genuine conductor datum in the arc
(4₁ → 40a1, N=40=2³·5, a Whitehead/octahedral child) is CONSISTENT with the claim this file
reported as refuted. **The "5 = golden filling" half STANDS as banked** (recomputed both
seats). The text below is kept for the record with this correction on top.

---

# B225 — the conductor decomposition tested: 5 = golden filling (holds); 2 = octahedral parent (REFUTED)

**Date:** 2026-06-26. **Status:** a verify-don't-trust test of chat1's "game-changer" hypothesis — does the
figure-eight character variety's conductor `40 = 2³·5` decompose as `(octahedral parent 2) × (golden filling 5)`?
**Verdict: the "5 = filling" half holds; the "2 = parent" half is refuted.** Firewall: standalone arithmetic
geometry; **nothing to `CLAIMS.md`; P1–P16 untouched.** Ledger **V228**.

## Foundations (verified, SnapPy)
- Whitehead `L5a1` & Borromean `L6a4` invariant trace field = **ℚ(i)** (disc −4, prime 2; octahedral, vol
  `v_oct`/`2·v_oct`); figure-eight = **ℚ(√−3)** (prime 3, tetrahedral); monodromy = **ℚ(√5)** (prime 5, golden).
- figure-eight character variety = **40a1** (B211), conductor `40 = 2³·5`, model `y²=x(x−1)(x−5)`.

## The pipeline (validated)
A 2-bridge character-variety tool (Riley parametrization in trace coordinates) that **reproduces B211 exactly**:
`Φ(x,z)=z²−(x²+1)z+(2x²−1)`, branch locus `(x²−1)(x²−5)`, bad primes **{2,5} = conductor of 40a1**. (The earlier
buggy version started the Riley word with the wrong generator; fixed to start with `b`, per Riley/B211.)

## SOLID — 5 is the golden filling
The figure-eight z-discriminant (branch locus) is `(x²−1)(x²−5)`. The **`x²=5` branch point is the golden
monodromy discriminant**: `t²−4 = 5` for the trace-3 monodromy `RL`. So the conductor's prime **5 is the golden
filling** — exactly as proposed.

## REFUTED — 2 is *not* the octahedral parent
Prime 2 appears in the character variety of **every** 2-bridge knot computed — both **twist** knots (Whitehead
fillings: `4_1, 5_2, 6_1, 7_2`) **and non-twist** 2-bridge knots that are **not** Whitehead fillings
(`6_2, 6_3, 7_6, 8_3, 8_8, 9_4`). Since 2 appears equally in non-octahedral knots, it **does not discriminate the
octahedral parent** — it is a **universal** feature of 2-bridge SL(2,ℂ) character varieties. (The naive
"`(x²−1)` parabolic factor" mechanism is also refuted: that factor divides the branch locus only for the
figure-eight.) **So `40` does not decompose as `(parent 2) × (filling 5)`** in the proposed form.

| knot | b(p,q) | type | 2 in bad? | bad primes |
|---|---|---|---|---|
| 4_1 | (5,3) | twist (Whitehead) | yes | {2, 5} (= 40a1) |
| 5_2 | (7,3) | twist (Whitehead) | yes | {2, 7} |
| 6_2 | (11,3) | **non-twist** | yes | {2, 11, …} |
| 6_3 | (13,5) | **non-twist** | yes | {2, …} |
| 7_6 | (19,7) | **non-twist** | yes | {2, 19, …} |

## Method limitation (honest)
The bad-prime extraction (discriminant of the branch locus) is **reliable only for low genus** — `4_1` ({2,5},
validated) and `5_2` ({2,7}). For genus ≥ 2 (`6_1` up) it **overcounts** (huge spurious primes from the
disc-of-disc resultant). A genuine determination of the higher-knot conductors needs the **Jacobian conductor**
(the specialist residual). This does not affect the two findings above (the `5`-branch is exact; the `2`-presence
is a robust boolean across the family).

## Honest status / tiers
- pipeline validation (figure-eight = 40a1, bad {2,5}): **`[exact]`** (matches B211).
- `5 = golden filling` (the `x²=5` branch = `t²−4`): **`[exact]`**.
- `2 = octahedral parent`: **`[REFUTED]`** — 2 is universal across 2-bridge character varieties (twist + non-twist).
- higher-knot bad primes: **method-limited** (disc-of-disc overcounts; Jacobian conductor = NEEDS-SPECIALIST).

## Net
chat1's conductor decomposition is **half right**: the prime 5 in `40a1` is genuinely the golden monodromy filling
(the `√5` branch point), but the prime 2 is **not** the octahedral parent's signature — it appears universally in
2-bridge character varieties, so `40 = 2³·5` does not factor as `(parent) × (filling)`. A clean verify-don't-trust
outcome on the "game-changer": one half confirmed, one half refuted. (`B211 → B225`; resolves `L44`.)
