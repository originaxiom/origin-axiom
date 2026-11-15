# Card W-F24: where frame C's read-out loses the hierarchy, and a read-out that keeps it

**Seat:** the web seat (chat1). **Opened:** 2026-11-15, at the author's request, under his ruling of that morning (status
file): the seat may compute and print frame C's outputs anywhere on the surface, and may not open the data or compare
any output with data. **Kind:** `result:` (data-free) and a proposal.

**Not blind, and after the look.** The big run's negative (B1944) is known to this seat from main's commit headline
(disclosed, status file, 2026-11-15). Nothing here can count as a test of frame C. Anything it proposes needs a new
rule of main's, sealed before any comparison, with this card's forking path counted in the look ledger.

## The question

Frame C's read-out is F̄, the frame averaged over the 24 points of order 5 (B1928), integrated against the path measure
μ on the modular surface. Main reads the negative as the surface average being dominated by the bulk. Two other
averages could also lose the hierarchy, and this card separates the three:
1. the **fibre** average over the 24 points;
2. the **surface** average against μ;
3. the **form** of both: they are arithmetic means of ratios, so they are dominated by the largest ratio present.

## Method

- **The frame:** this seat's transcription of B1656's frame (W-F22's `wf22_outputs.py`) with this seat's own triplet. It is
  not main's code: frame C's ingredients are re-typed.
  - The canonical end comes from B1667's and B1927's tables (their json read; the interpolation is this seat's code).
  - Theorem 90's weight is re-typed from B1932.
  - The horocycle is of length 2 only; the readings are S and S̃.
- **D1, pointwise.** On a grid of the fundamental domain (heights to 6), at each of the 24 points, the two ratios σ₂/σ₁ and
  σ₃/σ₁ of every sector in both readings.
- **D2, the decomposition.** At each τ, the arithmetic and geometric means over the 24 points; then each against μ. The
  loss is attributed to the fibre, the surface or the form.
- **D3, the height law.** How the pointwise log ratios move with Im τ.
- **D4, μ's heights.** The share of μ's time above each height, from random words of 40 letters (own coding of the
  thread, as B1924 and B1928 define it).
- **P, the proposal.**
  - A read-out that is the geometric mean, over the fibre and the surface: exp ∫ (1/24) Σ_p log F(τ, p) dμ.
  - It is argued from a principle: ratios compose (m₁/m₃ = m₁/m₂ · m₂/m₃). The geometric mean is the only quasi-arithmetic
    mean that commutes with composition for every joint law. The proof goes in the note.
  - It is tested only for whether it keeps any hierarchy. Its outputs are printed and compared with nothing measured.

## Expectations (committed with this card, before any frame output is computed)

- **X1.** At a fixed point of order 5, at least one sector ratio's log falls with Im τ over heights 2 to 6 (the frame is
  hierarchical towards the cusp).
- **X2.** At most bulk grid points (Im τ < 1.5), the 24 points' values of at least one sector ratio span more than a
  decade (the fibre carries hierarchy).
- **X3.** At most bulk grid points, the arithmetic mean over the 24 points exceeds the geometric mean by more than a
  factor 3 for at least one sector ratio (the fibre's arithmetic mean is set by its least suppressed points).
- **X4.** μ spends less than 10 % of its time above height 2.
- **X5.** The geometric read-out is smaller than F̄'s integral for every sector ratio. By how much is reported, and nothing
  is predicted about it.
- **Plants.**
  - One ratio, multiplied by 10 at every point, must move the arithmetic fibre mean by a factor of at least 10/24 and the
    geometric one by exactly 10^(1/24).
  - The composition identity must fail for the arithmetic mean and hold for the geometric one on the computed values.

## Not done here

- No data opened.
- No comparison with any measured number.
- No θ̄, nothing at the candidate family's addresses, and nothing of Theorems D and E.
