# B1320 — PHASE 2, ARC 0: Pantev–Wijnholt's localized count on the cyclic descent is 0 or 4, never 3 — on C₃ (H₁ = ℤ/4 ⊕ ℤ/4 ⊕ ℤ) and C₄ (ℤ/3 ⊕ ℤ/15 ⊕ ℤ) every orientation-preserving cusp-fixing isometry has |det(A − I)| ∈ {0, 4}; the positive control (m202, an order-3 rotation with |det(A − I)| = 3) fires on the same code path; the localized half of D2 is closed on the cyclic tower in PW's own frame

**Date:** 2026-09-09 · **Seat:** cc (main) · **Plan:** MASTERPLAN v3.1 §4 Arc 0 · **DESIGN sealed** `b1f71f45…` before the run · **Status:** **PROVED**
(a finite computation with a live positive control; pre-registered outcome: the 0.95 branch) · **Price:** none · **Credit:** B1291 (the parity theorem),
B1295 (the cover scan, whose record this arc read and re-ran live for the two covers), B1297 §1 (the correction that named the localized count), fc R69
(the charge-locus frame), Pantev–Wijnholt arXiv:0905.1968 §3.1 eq. (3.18) (the frame itself).

## 1. What was computed (`verification/b1320_arc0_pw_count.py`, SnapPy 3.3.2; record `.json`, `.out`)

| manifold | type | H₁ | isometries | |det(A − I)| by orientation | orientation-preserving values |
|---|---|---|---|---|---|
| m004 (the base) | — | ℤ | 8 | 0: 4 reversing + 2 preserving; 4: 2 preserving | {0, 4} |
| C₃ = the degree-3 cyclic cover | cyclic | ℤ/4 ⊕ ℤ/4 ⊕ ℤ | 24 | 0: 12 + 6; 4: 6 | **{0, 4}** |
| C₄ = the degree-4 cyclic cover | cyclic | ℤ/3 ⊕ ℤ/15 ⊕ ℤ | 32 | 0: 16 + 8; 4: 8 | **{0, 4}** |
| the other degree-4 cover | irregular | ℤ ⊕ ℤ (two cusps) | 8 | 0: 8 + 4; 4: 4 | {0, 4} |
| **control: m202** (first census hit) | two cusps | ℤ ⊕ ℤ | — | on a fixed cusp: **3** (×4, order 3, A = [[−1, −1],[1, 0]]), 1 (×4, order 6), 4 (×2), 0 (×2) | **{0, 1, 3, 4}** |

**The PW reading.** On a one-cusped cover the Higgs eigenform's zero locus is the fixed-point set of the involution on the cusp torus; for an
orientation-preserving map every isolated fixed point has index +1, so the localized count is |Fix| = |det(A − I)| when non-zero and 0 when the fixed
set is empty or one-dimensional. On the ℤ/3 and ℤ/4 descents that count is **0 or 4**. It is never 3 or 6, and the method can see a 3 — the control
found m202's order-3 rotation (the very manifold every seat's 3 lives on) as the census's first instance. **Every value on the cyclic covers is even**,
exactly as B1291's parity theorem requires on one cusp and as B1295 measured across the whole degree-≤10 tower.

## 2. What this settles

D2's localized half is closed on the cyclic tower in Pantev–Wijnholt's own frame: the descent that supplies the 3 (three families from the ℤ/3 twist)
supplies no localized chirality, because the cover's cusp carries no order-3 rotation — the count is 2 (with sign) or 4 (unsigned), never 3. Together with
B1297 (the bulk index vanishes on every (2+1)-reducible configuration of the cyclic tower) both halves of D2 on the cyclic tower are computed. **What
remains of Phase 2:** Arc A (does the bulk index I ≠ 0 occur at all in domain D, beyond the cyclic tower), Arc B (a non-amphichiral cover, or a partial
filling priced at three choices), and — now with a computed positive control — L205 (B1321): the one manifold in reach where the localized count IS 3,
at the price B1302 named (the golden face).

## 3. Receipts, lock

`verification/b1320_arc0_pw_count.py`, `.out`, `.json`, `already_banked_at_seal.txt`; `tests/test_b1320_phase2_arc0_pw_count.py`. FRESH_EYES Q9 (what PW
states for a 3-manifold with boundary) gains its computed instance; OPEN_LEADS L202 gains the note; the alias table's next free number becomes B1322
(B1321 is L205's arc, run in the same session).
