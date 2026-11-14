# W-C8, part 1: main's tick-parity law holds on this seat's code, and the metallic ticks have a mark exactly when m is odd

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `verify:`. Part 1 of card W-C8
(`relays/cards/CHAT1_W-C8_the_one_tick_object_and_the_foundational_system.md`, 981b62bc6), proposed and approved in M19.

**How it was checked.**
- **Main's check:** recomputed independently, on this seat's own code; expectations committed first.
- **The metallic part:** computed once; expectations committed first.
- **The run:** the script was sealed (sha256 `815c0c68…336ab531`) and run once. Every expectation was met.
- **Planted errors (1):** a mark test that accepts any non-zero kernel vector, whatever its order. It accepts every m, as
  it must, so the order condition is what does the work.
- **Main's output:** `tick_parity_run.txt` was read through the mask only after this seat's output was committed
  (1b783ac46). `tick_parity.py` was not opened.

## 1. The golden thread

| line | result |
|---|---|
| P1 | The search (entries at most 12) finds 44 elements of the normaliser of ⟨LR⟩ in GL₂(ℤ), in **8 classes** modulo ⟨LR⟩. They are exactly ±JⁿKᵉ, n and e in {0, 1}, with J = [[1, 1], [1, 0]] and K = [[0, 1], [−1, 0]]. **J² = LR, K² = −I and KJK⁻¹ = −J⁻¹** hold exactly |
| P2 | At the mark, the line of (1, 2) mod 5: **J acts by 3, K by 2.** The hand of ±JⁿKᵉ is **(−1)ⁿ⁺ᵉ on all eight classes**. The control, (−1)ⁿ alone, fails |

Main's run says the same on every line the two share:
- the three relations;
- the parity law (main: n < 8);
- J alone, commuting with the act, exchanges the mark's pairs.

So the claim that the hand at the mark flips exactly when the act is undone is false here, as main found. The tick flips
it without undoing anything. What holds is the parity of ticks plus undoings. That is B1914's orientation sign, det X times B1914's sign for keeping or inverting the act, which here is
det X · (−1)ᵉ = (−1)ⁿ⁺ᵉ. This seat also computed it in W-C5. Main's J and K are W-C5's M and J.

## 2. The metallic ticks, J_m = [[m, 1], [1, 0]], A_m = J_m², N = m² + 4

| m | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| N | 5 | 8 | 13 | 20 | 29 | 40 | 53 | 68 | 85 | 104 | 125 | 148 |
| a mark (a line of order N sent to −1) | yes | no | yes | no | yes | no | yes | no | yes | no | yes | no |
| J_m's scalar λ | 3 | — | 8 | — | 17 | — | 30 | — | 47 | — | 68 | — |

- **A mark exists exactly for odd m** (P3), on m = 1 to 12. A_m + I has Smith form diag(1, N) for odd m, and diag(2, N/2)
  for even m. For even m, every vector the act sends to its opposite mod N has order at most N/2.
  - **The reason holds for every m:** the gcd of the entries of A_m + I is gcd(m² + 2, m, 2) = gcd(m, 2), and
    det(A_m + I) = N. So the Smith form is diag(gcd(m, 2), N/gcd(m, 2)). The kernel mod N is ℤ/d₁ × ℤ/d₂, whose
    largest order is d₂. So a line of order N exists exactly when m is odd. This seat worked that out by hand. The
    computation covers m = 1 to 12.
- **For odd m** (P4), the mark is the line of (m, 2) mod N:
  - J_m acts on it by λ = m · 2⁻¹ mod N, with **λ² = −1 mod N**;
  - K acts by −λ;
  - λ ≠ ±1.

  So the hand of ±J_mⁿKᵉ is again (−1)ⁿ⁺ᵉ, and **the parity law holds at every odd metallic ground computed.**
- **The search** (entries at most 30) finds the normaliser of ⟨A_m⟩ in the same eight classes ±J_mⁿKᵉ for m = 1 to 5
  (P5).

This bears on main's tagged speculation in part 4: "the tick acting as a square root of −1 mod N needs m odd". For the
mark at level N itself, it holds, by the Smith form. More strongly, by the referee's arithmetic: for even m, 4 divides
N, and −1 is not a square mod 4, so no square root of −1 mod N exists at all.

## 3. What the wall teaches

For even m, the factor 2 shared by every entry of A_m + I leaves no line of full order at the ground's own level. So the
even metallic grounds have no mark of the golden kind at level N. Among the metallic grounds, the golden one is the
first with a mark, not the only one: 3, 5, 7, … have one too. So the mark alone does not single out the golden act.
Whatever does must be another clause, minimality or something else. Part 4 takes that up.

## 4. What was not checked

- A mark for even m at a level other than N.
- Whether J_m and K generate the whole normaliser for every m. The search covers m up to 5, with entries up to 30.

## 5. Files

`relays/chat1_2026-11-14_wc8/`: `wc8_part1_checks.py` (sealed), `SCRIPT_SHA256_part1.txt`, `wc8_part1_out.txt`,
`wc8_part1_err.txt`.

This note was read by one session before it was pushed, and its corrections are applied.

0 of 19.
