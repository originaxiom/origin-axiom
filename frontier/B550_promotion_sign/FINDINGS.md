# B550 — The Promotion-Sign Conjecture: REFUTED at n=3; replaced by the uniform meridian rule

Processes chat-1's Promotion-Sign Conjecture handoff (2026-07-09)
verify-don't-trust, against B111's LOCKED exact tower data (n=3 Lawton
Jacobian, n=4 B80 `_Jm_n4_exact`; `tests/test_b111_sign_structure.py`).

## The conjecture

The degree=rank height-1 promotion (one char(M¹) → char(Mⁿ), the meridian →
longitude of B111) has sign (−1)ⁿ: odd n consumes char(−M¹), even n consumes
char(+M¹). The handoff's own evidence table read n=3 and n=5 as "lost
char(−M¹), sign −."

## Verdict: REFUTED at the anchor (n=3)

B111's exact probe, re-run and re-read here, gives the height-1 (char(+M¹),
char(−M¹)) surviving multiplicities:

| n | closed form (+,−) | EXACT tower (+,−) | consumed | conjecture pred | verdict |
|---|---|---|---|---|---|
| 3 | (1,1) | **(0,1)** | char(+M¹) | (1,0) | **conjecture FAILS** |
| 4 | (2,1) | (1,1) | char(+M¹) | (1,1) | agrees (even-n coincidence) |

At n=3 the tower keeps char(−M¹) and loses char(+M¹) — the promotion consumes
the **positive** meridian, sign **+**. The handoff mis-read this as "lost
char(−M¹)." The conjecture predicts tower (1,0); the exact tower is (0,1).
Direct contradiction at the one fully-solved odd rank.

The handoff's n=4 "ambiguity" also dissolves: the exact tower height-1 is
(1,1), a genuine loss of one char(+M¹) from the closed form (2,1) — not the
"no loss / (2,1)" the handoff feared. Same uniform consumption as n=3.

## The replacement: the uniform meridian rule

> **The height-1 promotion ALWAYS consumes char(+M¹) — the meridian char(M) —
> promoting it to char(Mⁿ), for every n.**

n-independent, no sign alternation, no n=4 special case. It reproduces the
exact tower at n=3 and n=4, and it has a clean algebraic reading: the
promotion is literally meridian → longitude (L = c·Mⁿ, B83/B89), and the
meridian ingredient is char(+M¹), the positive one. The full ρ_n height-1
sector is then

  (char(+M¹), char(−M¹)) = (⌈(n−1)/2⌉ − 1, ⌊(n−1)/2⌋),

with heights 2…n−1 the θ closed form untouched, top char(Mⁿ), parity
(t−1)(t−det N).

## The discriminating test (corrects the handoff's target)

The handoff proposed n=6 (B66's SL(6) data). **n=6 does NOT discriminate:**
the conjecture and the meridian rule BOTH predict height-1 = (2,2) there. The
discriminating rank is **n=5**:

  - uniform meridian rule: height-1 = **(1,2)**
  - (the refuted conjecture would have said (2,1))

This sits behind the SL(5) wall (B105/B113 — no exact n=5 tower yet), so it
stands as a FALSIFIABLE PREDICTION: whoever resolves the SL(5) height-1 sign
split tests the meridian rule. (1,2) confirms it and closes the ρ_n catalog;
(2,1) would revive a sign dependence. B66's SL(6) sector — even if its 9/35
gauge-corrupted modes were cleaned — cannot decide this, because n=6 is
non-discriminating by construction.

## Net

The ρ_n prize's promotion half is NOT (−1)ⁿ; the exact data supports the
simpler uniform meridian promotion. One falsifiable prediction (n=5 → (1,2))
now stands as the single computation that would close the catalog. Firewall:
pure character-variety mathematics; nothing to CLAIMS as physics.
Locks: tests/test_b550.py.
