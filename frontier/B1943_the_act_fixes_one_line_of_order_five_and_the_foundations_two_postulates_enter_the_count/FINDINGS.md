# B1943 — The act fixes one line of order 5, up to sign, and no other; the foundation's two postulates enter the count

**Verdict: PROVED** (the theorem exact, checked by Smith forms and by enumerating every level to 60, with a planted
control; the scoreboard corrected). Main, 2026-11-14, from the sweep's S73: frame C's joint C02 was typed
FORCED-CLAIMED, "not yet a registered theorem". Register rows P-721, P-850, P-851. 0 of 19.

## Seen first

- **Swept:** `VERDICT topic-sweep /fixed up to sign|Smith form|SE1|SE3|FORCED-CLAIMED|the root's first homology/: 6 of 1684 arcs on main match (PROVED 6); 6 register rows match (DONE 2, QUEUED 4)`.
  - P-721 states det(LR + I) = 5.
  - P-312's general form (the Smith lemma) is on record in the stale-verdicts page (O1).
  - B1925 ties SE1 to the level.
  - B1939 § 1 recomputed the four points of order 5.
- **The literature:** the fixed points of a toral automorphism A on (ℚ/ℤ)² form the kernel of A − I, a group
  ℤ/d₁ × ℤ/d₂ for the Smith invariants of A − I. This is classical.

## The theorem (T-THE-ACTS-FIXED-LINE; `fixed_lines.py`)
- **What LR fixes.** On the fibre's torsion points, LR fixes up to sign exactly the four non-zero points of one line of
  order 5, {(1/5, 2/5), (2/5, 4/5), (3/5, 1/5), (4/5, 3/5)}, and no point of any other order. Each of the four is sent
  to its negative.
- **The Smith forms.** Smith(LR − I) = (1, 1) and Smith(LR + I) = (1, 3).
- **The same holds** for RL, (LR)ᵀ, (LR)⁻¹ and ((LR)ᵀ)⁻¹. This was checked by enumerating every point of exact order N
  for every N up to 60.
- **The control.** The trace-4 act LRR fixes points of orders 2, 3 and 6 (Smith(A − I) = (1, 2)). Caught.

## What it does to the scoreboard
- **C02 is the postulate it rests on.** C02 ("the line class of order 5: the ground's frustrated level") is the level of
  frame C.
  - **The implication is now a registered theorem:** if the frame's line is fixed by the act up to sign, the level is
    5.
  - **The premise is the foundation's SE3** ("the ground is the act itself; its level is the prime that its discriminant
    is, 5"). GENESIS types SE3 POSTULATED, main's entry, "counted in the budget": nothing computed decides it.
  - **C02 is therefore re-typed from FORCED-CLAIMED to CHOSEN,** with the theorem cited. It stays borrowed.
- **SE1 enters the shared block.** SE1 ("the root's first homology is torsion-free") is POSTULATED in GENESIS and
  selects the act (T-ROOT derives what it selects).
  - It was counted nowhere on the board, while SE2, the orientation, is the shared block's S02. The closure programme's
    input budget already counted it, as "the selection criterion" (G:SE1), and SE3 as "the ground". So S03 is the same
    choice under a second name there, and the budget's own count does not change; only the scoreboard was short.
  - It is added as S03 (CHOSEN, its basis the postulate).
- **The headline moves up by one in every frame.** This is the honest count: A from 13 to 14, B from 44 to 45, C from 11
  to 12 borrowed joints. C's twelve are 11 chosen and 1 ansatz.

## What the wall teaches
- **A joint typed "forced" by a seat's word may rest on a postulate of the foundation.** Registering the theorem shows
  what is forced, the implication; the premise stays a choice.
- **A board that lists only some of the foundation's postulates undercounts.** Each one goes where every frame stands
  on it.

## Not claimed
- That SE1 or SE3 is derived. Both stay postulates of the foundation.
- Any value.
- Anything about the big run, whose frame and options are unchanged by this re-typing.
