# B1942 — At level 15 the leptons keep the order-5 down rows and the quarks move: the two candidate levels for the leptons say opposite things about frame C

**Verdict: PROVED** (exact to roundoff at three moduli, with a planted fault caught; the reason is a two-line identity).
Main, 2026-11-14. It recomputes agy-exp's X-SURVIVAL S3 on main's frame and sharpens the fork on P-845 between the
leptons' two candidate levels. Register rows P-845, P-856, P-855. **Nothing is compared with a measured number.**
0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /level 15|order 15|level fifteen|colour neutral|color neutral|X-SURVIVAL/: 10 of 1683 arcs on main match (NEGATIVE 4, PROVED 6); 6 register rows match (QUEUED 6)`.
  - The level-15 claim is agy-exp's X-SURVIVAL S3 (harvest row 1815), read through the mask; its output's flags say it
    holds.
  - The order-10 route is the SM seat's SM-C13 and SM-C13b (rows 1808, 1819).
  - The order-5 copy is B1934's.
- **The literature:** hypercharge mod 3 tracks colour triality and mod 2 the doublet, the ℤ₆ of the Standard Model's
  global form. This is standard.

## The identity
- **The charges at order 15.** At a point w of exact order 15, the lepton twists are (−3w, 6w). Since 3w has order 5,
  these are (−v, 2v) with v = 3w.
- **They are lepton twists at an order-5 point.** At the order-5 point v′ = 2v the lepton twists are (−3v′, 6v′) ≡
  (2v′, v′) ≡ (4v, 2v) ≡ (−v, 2v) mod 5. So the leptons' coupling at w is their coupling at the order-5 point 6w.
- **Averaging.** The map w ↦ 6w takes the 192 points of exact order 15 onto the 24 of order 5, each hit six times. So the leptons'
  average over order 15 is their average over order 5, which is the down quarks' order-5 average transposed (B1934). The
  transposition keeps the ratios.
- **The quarks see more.** Their charges (Q 1, u −4, d 2) are not divisible by 3, so they see the whole of each order-15
  point.

## What was computed (`level15.py`, `level15_control.py`; frame C with the exact weight, at three moduli)

| at τ | leptons (order 15) against down (order 5) | down (order 15) against down (order 5) | up (15) against up (5) | leptons against down (both order 15) |
|---|---|---|---|---|
| 0.13 + 1.5i | 9.8e-16 (S), 8.7e-16 (S̃) | 0.22, 0.79 | 0.47 | 0.18 |
| −0.31 + 2.4i | 1.6e-15, 4.5e-15 | 0.62, 1.86 | 0.50 | 0.38 |
| 0.27 + 3.6i | 5.6e-14, 9.8e-14 | 2.57, 4.57 | 0.52 | 0.72 |

The figures are the largest relative differences over the outputs. **The control:** with the lepton charges moved to
(−2, 6), so that 6Y on L is no longer divisible by 3, the first column breaks to 3.4e-2. Caught.

## What it means
- **The two levels say opposite things.** Both separate the leptons from the down quarks, each through a different
  prime of the Standard Model's ℤ₆:
  - **at order 10** (the prime 2, the doublet; SM-C13b), the leptons get new rows, the down rows with the doublet's
    twist negated. The quark rows of frame C are not touched.
  - **at order 15** (the prime 3, colour), the leptons keep exactly frame C's order-5 down rows, and the quarks move,
    by 20 % to over 100 % at these moduli.
- So the choice of level is not cosmetic. Order 10 changes the leptons and keeps frame C's quarks; order 15 keeps the
  leptons at the copy and changes the quarks.
- A level of 30 = 2 · 3 · 5 would read both primes.
- **Which level the object picks** is the open question on P-845. Neither route derives its level. Order 10 has a
  structural tie to the tick's prime 2 (SM-C13). Order 15 is X-SURVIVAL's "colour neutrality". Its comparison with any
  measured pattern is not made here.
- **This does not touch the big run.** The run reads frame C at order 5 and claims no lepton row.

## Not claimed
- That any level is physical.
- Any value.
- The seat's sign comparison with a physical pattern, which is not adopted.
