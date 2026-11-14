# W-F22: B1922's negative half, checked again. S* does not repeat in one turn of the golden thread; S and S̃ do. The reason is shown independently: S*'s components are not covariant under γ. R82-1's item 12 holds at (1/5, 2/5). But S* is covariant under γ³, so it should repeat in three turns. On the golden thread, the S* exclusion rests on requiring one-turn periodicity

**From:** the web seat (chat1). **To:** main (cc). **Kind:** `result:` (data-free). It answers M31's first ask (which
main numbered W-F21; that number was already in use, so this is W-F22) and closes card W-F22
(`relays/cards/CHAT1_W-F22_b1922s_negative_half.md`, 2d154116d).
- **Amendment.** The card was amended before any run (9666cde7c) to add the output-level check, which the author
  approved on 2026-11-14 in the evening (status file).

**How it was checked.** Computed once; expectations committed first.
- **Two scripts, of different independence.**
  - The structural checks (`wf22_checks.py`) run on this seat's own code: its own theta series, Serre derivative, fit
    and criterion.
  - The output-level check (`wf22_outputs.py`) runs a re-typed transcription of B1723's `b1656_funcs.py`, with this
    seat's own triplet. It keeps the same functions, names, expressions and quadrature parameters; only NK is 30 in
    place of 24. It prints deviations only.
- **The seals and runs.** Both scripts were sealed at 9666cde7c and run once each. Their outputs were committed
  (e2354f701) before they were read.
- **Planted errors.**
  - The structural checks: 1 planted, 1 caught.
  - The output-level check: its one plant was vacuous (§ 4), so that check was not tested against a planted error.
- **Expectations not met as written.** Four, all disclosed in § 4: L1, O1 and O2 at their third point, and the second
  plant. O4 came out inconclusive, as its own clause allowed.
- **What was computed.** No output of the frame was printed or kept. The frame was evaluated only along the golden
  thread and at the three lines named, as the author's ruling allows.

## 1. Results

| line | result |
|---|---|
| L1 | Among B1713's 266 lines, γ fixes up to sign the trivial line (0, 0), (1/5, 2/5) and (2/5, 4/5). The expectation named only the last two; it missed (0, 0), which every element fixes. **The non-trivial lines are exactly the predicted two** |
| L1, reported | γ² fixes 7 lines up to sign: (0, 0), four of order 3, and the two of order 5. γ³ (≡ I mod 4) fixes 18: lines of orders 1, 2, 4, 5 and 10 |
| L2 | γ and γ² are not in Γ⁰(2), and γ³ = [[13, 8], [8, 5]] is in Γ(2) |
| C2 | ρ(g) fitted for T, R, γ, γ², γ³. The fourth-point residuals are at most 3e-18, and ρ(T) is W-B1's hand matrix (1e-20) |
| C0 (control) | S̃ is covariant under all five, as B1724 found for SL(2, ℤ) (residuals at most 8e-16) |
| C1 | **S* is covariant under R and γ³** (residual 8e-16). It is **not covariant under T, γ and γ²** (residual 2.0). This holds at the level of the reading's components, on this seat's own code, with no frame involved |
| O1 | The own line (2/5, 4/5), under γ, at three points of the thread: S and S̃ repeat, with deviations 3e-10, 1e-9 and 8e-5. **S* does not repeat: 2.7, 1.5 and 2.7** |
| O2 | The line (1/5, 2/5), under γ: S and S̃ repeat, with deviations 8e-11, 8e-10 and 6e-5. S* does not: 3.2, 1.8 and 4.9. **R82-1's item 12 holds.** The third point is not met as written (6e-5 against 1e-6; § 4) |
| O3 | The line (1/5, 3/5), which γ does not fix: every reading deviates (2.1 to 5.1) |
| O4 | The own line under γ³ (three turns), at the symmetric point and one shifted point (the lower image at Im τ 0.12 and 0.11). S and S̃ deviate by 8e-4 and 6e-2, which they should not. S* deviates by 2e-3 and 6e-2, of the same order. **Inconclusive** |

## 2. What it means

**B1922's negative half, checked again.**
- In one turn of the golden thread, at the own line, S* does not repeat: it deviates by order one at every point.
- S and S̃ repeat to 1e-9 or better at the two points of good height.
- The deviations agree with B1922's table to every digit shown, the third point's 7.8e-5 included.
- The frame code is a transcription of B1723's. So at the frame level this is not "recomputed independently" in the
  record's sense (code that shares none with the first).
- **What is independent is the reason:** S*'s components are not covariant under γ (C1, on this seat's own triplet, fit
  and criterion). Whether that meets A7's independent second computation is main's to judge.

**R82-1's item 12 holds.**
- γ acts on lines by (a, b) ↦ (a − b, 2b − a). Its non-trivial fixed lines up to sign are the four points
  k·(2/5, 4/5), k = 1 to 4, which form two classes: the own line and (1/5, 2/5).
- The frame repeats at both, for S and S̃.
- B1922's "at a line γ does not fix they do not" (periodic.py) is right. Its "and not at any other line" (FINDINGS § 0)
  is not: up to sign there is exactly one other non-trivial line, and the frame repeats there too.
- R82-1's "false on two lines" holds in substance. Up to sign the count is one line, (1/5, 2/5) = −(4/5, 3/5).

**S* repeats in three turns, so the exclusion rests on a premise.**
- γ³ ≡ I mod 2 (L2), and S*'s components are covariant under γ³ (C1).
- B1724 found S* covariant at the frame level under Γ⁰(2), which contains Γ(2).
- So along the golden thread, at the own line (γ³ fixes it up to sign, as γ does), S* should repeat after **three**
  turns.
- The output-level check of this was inconclusive (O4). Three turns force the points down to Im τ about 0.12, below the
  frame code's reach (B1724 met the same failure near Im τ = 0.1). A frame in extended precision, such as B1940's, might
  settle it, if the failure is one of precision and not of the quadrature.
- **What "S* does not repeat along a thread" covers.**
  - It is true for one turn of the golden thread, and of any thread whose word lies outside Γ⁰(2).
  - For a word inside Γ⁰(2) that fixes a line up to sign, S* should repeat in one turn (a prediction, from B1724). An
    example is R³T² = [[1, 2], [3, 7]] (trace 8), which fixes (1/5, 1/5) and (2/5, 2/5) up to sign.
  - For every word w, at a line w fixes up to sign, S* should repeat along w's thread after k turns, where k is the
    least power with wᵏ in Γ⁰(2) (1, 2 or 3).
  - Its average over k turns does not depend on where it starts, just as S's average over one turn does not.
- **So, on the golden thread, removing S* requires one-turn periodicity:** each word's average is taken over one
  traversal.
  - B1922 states this as a requirement (§ 0: "That needs its outputs to repeat after one period of the thread's
    geodesic"). It does not weigh an average over a power.
  - The rule's A7 uses it without stating it ("S* does not repeat along a thread").
- **Without that premise, the exclusion needs another ground, and B1724's sheet condition gives none on the golden
  thread.**
  - B1724: S* is covariant only under Γ⁰(2), so its rows depend on which of three sheets τ is on, and S* is used only
    with all three sheets sampled.
  - But Γ⁰(2), Γ⁰(2)γ and Γ⁰(2)γ² are the three cosets, so the three-turn average passes once through each sheet.
  - For a word whose image in S₃ has order 1 or 2, the k-turn average stays on one or two sheets, and B1724's condition
    does bear on it.
  - Whether B1928's average over the weave's threads meets the condition is main's to judge.
- **For the run as frozen:** the four declared options exclude S*. With the premise stated, nothing changes before the
  look.

## 3. Typed

| statement | how checked |
|---|---|
| S* does not repeat in one turn; S and S̃ do (own line) | computed once, on a transcription of B1723's frame code with this seat's own triplet; agrees with B1922's deviations to every digit shown; expectations committed first |
| S* not covariant under γ at the level of its components (the reason for the negative half) | computed once on this seat's own code (C1); expectations committed first |
| the frame repeats at (1/5, 2/5) for S and S̃ | computed once, on the transcription; expectations committed first (not met as written at the third point, § 4) |
| the two non-trivial γ-fixed lines among the 266 | computed once; expectations committed first |
| S*'s components covariant under R and γ³, not under T, γ, γ² | computed once on this seat's own code; expectations committed first |
| S* repeats in three turns at the frame level; in one turn for a word inside Γ⁰(2) | a prediction (from C1 and B1724's frame-level covariance; O4 inconclusive) |
| on the golden thread, the exclusion of S* rests on one-turn periodicity | a reading |

## 4. Not met as written, and the plants

- **L1.** The expectation named two lines. The run found three, the extra being the trivial line (0, 0), which every
  element fixes. The two non-trivial lines are exactly the predicted ones.
- **O1 and O2 at the third point.** S and S̃ deviate by 8e-5 (own line) and 6e-5 (1/5, 2/5), against the stated bound
  of 1e-6.
  - That point sits at Im γτ = 0.32, and B1922's own run shows the same 7.8e-5 there.
  - This reads as the frame's precision at that height, not as non-repetition: S* deviates by order one there.
- **O4.** Inconclusive, as its own clause allowed (S and S̃ fail at that height).
- **The plants.**
  - The first, weight 1/2 in place of 3/2 in the structural fit, failed the fourth-point check for every g with c ≠ 0.
    It was caught.
  - The second, the end left untransported, did not fire, and it tested nothing.
    - It was placed at the symmetric point, where |τ + 1| = 1, so the end's shift is zero there.
    - At the other two O1 points |τ + 1| is 1.118 and 1.871, so the transport is exercised there, but no plant was
      placed there.

## 5. Files

`relays/chat1_2026-11-14_wf22/`: `wf22_checks.py` and `wf22_outputs.py` (sealed), `SCRIPT_SHA256.txt`,
`wf22_checks_out.txt`, `wf22_outputs_out.txt`, and the two error files (empty).

This note was read by one session before it was pushed; its corrections are applied.

0 of 19.
