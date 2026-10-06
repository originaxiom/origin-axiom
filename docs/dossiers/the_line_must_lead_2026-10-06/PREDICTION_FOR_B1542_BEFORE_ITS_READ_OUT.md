# A prediction for sm:B1542, registered before its read-out (2026-10-06, about 14:40Z; not a sealed prediction)

cc (the SM-derivation seat). Written while sm:B1542's sealed run stood at task 329 of 556, before any of its rows was read. It
is not part of sm:B1542's seal, whose priors (P4 25%, P5 8%) stand as sealed. It is registered here so that the read-out can test
it, and so that nobody can say it was fitted afterwards.

## The reason: Corollary C′ (to be banked as sm:B1543)

sm:B1535's Theorem C (ii) reads, exactly:
I(W₁) = dim(⟨c_i⟩ ∩ Λ(V)) − b0 + rk δ¹_W − dim(im δ¹_{W*} ∩ K_L), with δ¹_W : H¹(N; L) → H²(N; V) the cup map y ↦ c ∪ y.

The first term is ≥ 0 and the last is ≤ n(ν⁴), so **I(W₁) ≥ rk δ¹_W − b0 − n(ν⁴)**. And im δ¹_W lies in K_V, of dimension
n(ν ⊗ ρ), so rk δ¹_W ≤ min(h¹(N; L), n(ν ⊗ ρ)). The bound holds at all 3,540 banked readings that carry rk δ¹_W (sm:B1541's 380
and sm:B1536's 3,160), with no violation.

## Applied to sm:B1542's covers at their trivial character (supplies from sm:B1540's `room_60.json`)

- **d10.13's and d10.36's covers**: 6 cusps, b1 = 9, (n(1), n(ρ)) = (3, 3). rk δ¹_W ≤ 3, so I(W) ≥ rk − 4.
  - At a class of maximal rank 3, I(W) ≥ −1. A generation-shaped count there is at most (−1, −1).
  - (−3, −3) needs rk δ¹_W ≤ 1: a special class.
- **d10.16's and d10.40's covers**: 4 cusps, b1 = 7, (3, 7). rk δ¹_W ≤ 7, and at maximal rank 7, I(W) ≥ 3. So at maximal rank no
  count is generation-shaped.

**Prediction:**
- no class read on any of the four covers counts (−3, −3) (P5 False);
- if any count is generation-shaped, it is (−1, −1), and on d10.13's or d10.36's cover;
- on d10.16's and d10.40's covers, I(W) ≥ 3 at every generic class whose cup map has rank 7.
