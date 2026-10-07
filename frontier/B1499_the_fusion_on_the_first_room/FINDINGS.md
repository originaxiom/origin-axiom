# B1499 — THE FUSION ON THE FIRST ROOM: on o10_150691 at ν = (i, 1, 1) the two orders fuse into an exact irreducible module that counts (0, 0) with no interior class on either side — the count is the order here too, and the room is not used by any rank-five module near the split point, split or fused

**Verdict: NEGATIVE** (scoped: F-HE, rank-five modules near V ⊕ 1 on o10_150691 at the two-class order-four characters)
— F1, F2, F3 hold, **F4 fails**. cc (main), 2026-10-07. Sealed `10786bcca` (sha256 0f712c31) before any obstruction or
fusion was computed there. The cover is chosen (FK14); a selection's negative. No physical quantity. **0 of 19.**

## 0. Seen first, and literature

As sealed (B1498's sweep): B1486 (the method and its pattern: the fusions count (0, 0)), B1466, B1497–B1498.
**Literature:** none. Seen: the split readings only.

## 1. Results (`fusion_o10_150691_2_0_0.json`)

| | sealed prediction | prior | result |
|---|---|---|---|
| **F1** | each order a cocycle; the mixed direction c + d unobstructed at second order | 75% | **HOLDS**: first-order residuals ~10⁻³⁸; the mixed direction's second-order residual 2.5·10⁻³⁶ against ∥Q∥ = 2155 (rank of the linear map 34) |
| **F2** | a converged fusion with commutant dimension one | 70% | **HOLDS** at ε = 0.1: the Newton iteration reaches the arithmetic floor (residual ~10⁻³⁶, relative ~10⁻³⁹; see §3), at distance 2.34 from the split point; commutant dimension 1, no invariant line, no dual invariant line — irreducible; the same at ε = 0.02 (commutant 1, no invariant lines) |
| **F3** | every converged fusion counts (0, 0) | 70% | **HOLDS**: (I, I(Λ²)) = (0, 0), with n = n* = 0 — no interior class on either side; the same at ε = 0.02 |
| **F4** | some irreducible fusion has I ≠ 0 | 20% | **FAILS** |

The split point's own readings: S = V ⊕ 1 counts (0, 0) (n = n* = 3); W₁ = the extension by c counts (0, −1); W₂ by
d counts (0, +1) — the two orders opposite on the Λ² side, as at the silver members (B1486), and zero on the 10′ side
here (B1498).

## 2. What it says

On the first object of the family with room, at the characters where the four has two classes and the seat's cap
allows two, every rank-five module near the split point reads nothing on the 10′ side: the split extensions zero
(B1498), the irreducible fusion zero with no class at all. The room (1), the second supply (2), the cap (2) and the
floor (1) are present at one character and nothing near V ⊕ 1 uses them. With B1486 (the silver members) and B1466
(m004's counted point) the pattern is now in three places: **the count lives at the reducible point, as the choice of
order, and the irreducible neighbours carry nothing.** The branch is closed; what remains for the smooth standard on
this object is nothing near the split point — a count there would need a module of a different kind.

## 3. Disclosed

- **The convergence criterion.** The sealed threshold (10⁻⁴⁰ absolute) is below the arithmetic floor at 40 digits on
  these relators (norms ~2·10³): the sealed run's ε = 0.1 reached ~10⁻³⁶ and stayed, and the instrument skipped the
  count (`sealed_run/`). The criterion was loosened to 10⁻³⁰ absolute ("at the floor", relative ~10⁻³³), both flags
  recorded, ε = 0.005 dropped (each seed takes about thirty minutes; two decide), and the run repeated. B1486 recorded
  the same stall at one seed.
- The class of V over the line is the generic member of B1498's pencil (random λ, seed 1499); the class of the line
  over V a random combination of the two classes of H¹(V*). One character of the eight (the deck and Galois carry the
  others: B1497–B1498 read them alike).
- Not blind to B1486's pattern.

## 4. Files

`verification/fusion.py` (sealed; the criterion corrected as above), `fusion_o10_150691_2_0_0.json`, `fusion_run.txt`,
`sealed_run/`; `ARTIFACT_HASHES.txt`. Test: `tests/test_b1499_the_fusion_on_the_first_room.py`.
