# B1729 — THE COARSER LINE (P-305, for P-294): WHERE 3 DIVIDES A LINE'S ORDER THE LEPTONS SEE A LINE OF A THIRD THE ORDER, BUT THE FRAME'S OWN LEPTON-TO-DOWN RATIOS SHOW NO GEORGI–JARLSKOG SHIFT THERE

**Verdict: NEGATIVE** (data-free census; the reading criteria were written before the output was read). cc (main),
2026-10-23. No measured number is read. **0 of 19.**

## 0. Seen first

`VERDICT topic-sweep /order 1[3-9]|order 2[0-9]|order 30|order-15|order-30|orders? 13|orders 8.16|order ≤ 16|leptons see|coarser line|3 divides the (line's )?order/ (full text): 58 of 1500 arcs on main match (NEGATIVE 15, PROVED 42, no verdict file 1)`;
the matches are group orders in older arcs. In the mass frame:
- B1703 (the coincidence census to order 16, no masses);
- B1711 (order 9);
- B1720 (threads' fixed lines, at their apexes only);
- B1728 (the line's order as a quotient of hypercharge);
- B1712 and B1713 (mass censuses to order 12).

No mass census had gone past order 12. **Literature:** the Standard Model's ℤ₆ centre; Georgi and Jarlskog (1979).

## 1. The fact and the question

On the line w = ατ + b a field of charge q gets the twist (qα, 2qb) (B1656, B1728). The lepton charges are
6Y(L) = −3 and 6Y(e) = 6, which is 3 × (−1, 2). **So the lepton sector at w is the (−1, 2) sector at 3w.** The quark
charges (Q 1, u −4, d 2) are not multiples of 3. This is the ℤ₃ of the Standard Model's ℤ₆ centre acting trivially on
leptons. On a line of exact order N with 3 ∣ N the leptons therefore see a line of order N/3 and the quarks the full N:
order 15 gives leptons order 5, and order 30 gives leptons order 10, the order of B1726's best rows. Could this coarser
line be where the Georgi–Jarlskog factor comes from (P-294)?

## 2. The census (`verification/frame_r2r1.py`)

Every line of exact order N ∈ {5, 10, 13, …, 30} up to sign, at τ = 0.55 + 3.05i and 0.35 + 2.75i (B1726's band), both
horocycles, down quarks and leptons in one reading (S or S̃, as every menu of B1726 pairs them): 7 344 points, none
masked by an exact zero. Read: the frame's own R2 = (m₂/m₃)_e/(m₂/m₃)_d and R1 = (m₁/m₃)_d/(m₁/m₃)_e.
- **The check:** on order-5 lines R2 = R1 = 1 to 8.6 × 10⁻¹¹ (Y_e = Y_dᵀ, B1728).
- **The criteria, written before the read:** support would be a systematic shift of both log R2 and log R1 toward
  positive values on 3 ∣ N lines relative to the other orders (Georgi–Jarlskog's Clebsch gives log 3 ≈ 1.10 for both);
  against, no difference or opposite signs.

| | median log R2 | median log R1 |
|---|---|---|
| 3 ∣ N (15, 18, 21, 24, 27, 30) | 0.04, 0.34, 0.16, 0.41, −0.02, 0.12 (mean 0.17) | −0.16, 0.26, −0.23, −0.25, −0.16, −0.07 (mean −0.10) |
| other orders 13–29 | mean 0.03 (from −0.22 to 0.20) | mean −0.08 (from −0.33 to 0.34) |

- At every order the frame's own ratios spread widely: interquartile ranges of about 2 units of log R2 and 4 of log R1,
  and 5–95% ranges of about −3.5 to +2 (log R2) and −4.3 to +4.5 (log R1).

## 3. Verdict

- **Against.** R2 moves by about +0.15 in log on 3 ∣ N lines, not systematically (order 27: −0.02) and far short of
  1.10; R1 does not move.
- **The coarser line does not supply the factor.** What decides the frame's lepton-to-down ratios is the particular line,
  not whether 3 divides its order.
- **A reading (labelled).** The spread means a line choice can mimic a hand factor; such a choice is a selection, which a
  calibration has to count (as B1726's free-factor menu does).

## Disclosed

- The question was raised during S192's suite, the census run once in the audit room after S192's push, its criteria
  written first (`audit/` draft, not tracked); the script moved here unchanged except its docstring and root lookup.
- Two τ only; one reading per pair; orders to 30.

## Files

- `verification/frame_r2r1.py` → `frame_r2r1.json`, `frame_r2r1_run.txt`.
- The lock: `tests/test_b1729_the_coarser_line.py`.
