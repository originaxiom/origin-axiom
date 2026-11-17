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

## The second computation (the web seat's W-F26, harvest row 1839)

- **It agrees at the two points it computes,** the mark and the twin, on the web seat's own code. Its card was sealed
  first.
  - When both sectors take the same reading, |V| is the identity. In both declared worlds it is a cyclic permutation.
  - Its referee ran main's frame_mp to height 12 and got the same result.
- **One difference, stated.** At those two points the seat finds (S̃, S̃) aligned up to height 12. Main finds (S̃, S̃)
  deranged at height 30 at other points. This is not a conflict: the two computations cover different points and
  heights.

## Added 2026-11-17: at τ = i the two readings coincide (`verification/readings_coincide_at_i.py`)

The web seat's W-A1 (H1 and H3; harvest row 1846) found that at τ = i the Higgs triplet's third component vanishes, so
S̃ = S there. On main's frame code, at four points of order 5 and in both sectors, the two readings' couplings differ
by at most 2.8e-33 at τ = i. At the controls 1.3i and 0.05 + 0.9i they differ by 0.26 to 0.73.
- So at τ = i the choice of reading is settled by equivalence. That is a statement at one point. The point is in the
  bulk, where the frame has no large hierarchy, and the web seat's sealed look there failed (W-L1, the look ledger).
- It bears on P-847: the reading is a free bit everywhere except at that point.

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
