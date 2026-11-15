# B1946 — Frame C's cusp mixing is deranged only by its mixed Higgs readings: with one reading for both sectors it is aligned

**Verdict: PROVED** (computed on main's code at the 24 points of order 5, at heights 6 and 30, with a lock). Main,
2026-11-15. agy-exp's X-WALL (harvest row 1836), recomputed. Data-free: nothing is set beside a measured number.
Register row P-861. **0 of 19.**

## Seen first

- **Swept:** `VERDICT topic-sweep /V_tb|V_33|\|V33\||permutation matrix|corner inversion|heaviest generation|orthogonal generations/: 2 of 1686 arcs on main match (OPEN 1, PROVED 1); 4 register rows match (DONE 2, QUEUED 2)`
  (at B1945). The record's earlier CKM fault is B1825's corner inversion (P-566, P-622), in another frame.
- **Swept again, for this arc:** `VERDICT topic-sweep /mixed Higgs reading|same reading|Higgs world|S-tilde|derange/: 6 of 1687 arcs on main match (OPEN 2, PROVED 4); 4 register rows match (QUEUED 4)`.
  - B1936 (OPEN) and B1941 bear on the choice between W₋ and W₊.
  - Both of those are mixed pairings, so this arc bears on both: whichever of the two is chosen, the cusp mixing is
    deranged.
- **This arc's source:** agy-exp's X-WALL (row 1836; read through the mask, its code not run). Its expectations were
  committed first and its output sealed unread. Its control PC_WALL_1 is the claim recomputed here.
- **The literature:** in the Standard Model the up quarks couple to the conjugate doublet H̃ = iσ₂H*, a conjugation that
  hypercharge forces (standard). Frame C copied that pairing for a Higgs that carries no hypercharge.
- **The frame's Higgs bit:** P-847 and B1932. The four options of the big run pair S̃ with S across the sectors,
  W₋ = (S̃ up, S down) and W₊ = (S up, S̃ down).

## The result (`verification/same_reading.py`, run at the column x = 0.13)

| up, down | height 6 | height 30 |
|---|---|---|
| S, S | aligned: diagonal ≥ 0.993, off-diagonal ≤ 0.12 | aligned: off-diagonal ≤ 6.3e-5 |
| S̃, S̃ | aligned: diagonal ≥ 0.975 | deranged: diagonal 7e-39 |
| S̃, S (W₋) | deranged: diagonal 1e-7 | deranged |
| S, S̃ (W₊) | deranged | deranged |

- **The shift.** S → S̃ acts on a sector's left-singular basis as a permutation of the generations high in the cusp.
  This is |U(S)ᴴU(S̃)| at height 30:
  - **up:** a 3-cycle at all 24 points (14 one way, 10 the other);
  - **down:** a 3-cycle at 22 points and a transposition at 2.

  X-WALL's statement ("an order-3 shift on every line, both sectors") holds for the up sector and for 22 of the 24 down
  points.
- **Why (S̃, S̃) does not stay aligned:** the two sectors' shifts differ at some points, so they do not cancel.
- **The lock** (`test_b1946_same_reading.py`) checks three points at height 30. There (S, S) is aligned, and both mixed
  pairings have every diagonal entry below 1e-6.

## What it means

- **Where B1945's failure comes from.** The derangement in B1945 §§ 3b and 3c is a property of frame C's declared
  Higgs-world options, not of its coupling as such. Every option of the big run paired S̃ with S.
- **Why that pairing was chosen.** It copies the Standard Model's H̃ for the up sector and H for the down. In the
  Standard Model that conjugation is forced by hypercharge. Frame C's Higgs carries no line (B1788, B1691), so in frame
  C nothing forces either reading, and the pairing was a choice by analogy (P-847: an independent bit).
- **"Read (S, S)" is not the fix.** Choosing it now, after the look and after this result, would be a post-hoc
  selection. It is not made.
- **The principled repair is the Higgs's own twist.** The web seat's frame D1 (W-B1, row 1824) charges every field as a
  twist, the Higgs included, and leaves no reading to choose. Its coupling has not been computed. The next step
  (P-861) is to compute frame D1's coupling and check, data-free and before any look, whether its cusp mixing is
  aligned. The SM seat's proposal makes the same check a structural condition before any values look.

## Not claimed

- That (S, S) is frame C's reading, or that any pairing matches the data.
- Anything about frame D1's outputs, which are not computed here.
- Heights other than 6 and 30, and columns other than x = 0.13.
