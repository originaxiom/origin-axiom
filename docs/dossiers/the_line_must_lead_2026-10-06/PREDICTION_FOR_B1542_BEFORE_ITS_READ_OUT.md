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

## Amendment, also before the read-out (2026-10-06, about 15:26Z; the run at task 484 of 556, no row read)

The reasoning above used the global maximal rank, min(h¹(N; ℂ), n(ρ)). On these cyclic covers the deck group grades the cup map.
By Shapiro, H¹(N; ℂ) = ⊕_m H¹(d10.x; ψ^m) and H¹(N; ρ) = ⊕_j H¹(d10.x; ψ^j ⊗ ρ), and the cup product and the interior part of
H²(N; ρ) respect (j, m) ↦ j + m. So a class in the ψ^j eigenspace has
rk δ¹_W ≤ B_j = Σ_m min(h¹(d10.x; ψ^m), n(ψ^{j+m} ⊗ ρ)).

The per-power supplies are sm:B1536's banked rows (sm:B1540's construction). The h¹'s follow by half lives from the cusps'
t-periods. The four's h¹ per eigenspace agrees with sm:B1542's control K2 on all four covers. The record is sm:B1543's
graded census (verification/graded_census.json in its folder).

| cover | h¹(ψ^m), m = 0..5 | n(ψ^j ⊗ ρ) | the four's eigenspaces (K2) | B_j on them |
|---|---|---|---|---|
| d10.13, d10.36 | 4, 0, 1, 3, 1, 0 | 2, 0, 0, 1, 0, 0 | ψ⁰ (5), ψ³ (4) | 3, 3 |
| d10.16, d10.40 | 4, 1, 0, 1, 0, 1 | 2, 0, 2, 1, 2, 0 | ψ⁰ (5), ψ² (2), ψ³ (2), ψ⁴ (2) | 3, 3, 4, 3 |

On d10.16's and d10.40's covers, the eigenspace classes (Part B) reach rank 3 or 4 at most. Corollary C′ then bounds them by
I(W) ≥ −1 on ψ⁰, ψ² and ψ⁴, and by I(W) ≥ 0 on ψ³, not by 3.

**The amended prediction:**
- No class read counts (−3, −3). This is unchanged: every graded bound on a non-empty eigenspace is at least 3, and (−3, −3)
  needs rank ≤ 1.
- A generation-shaped count, if any, is (−1, −1). It can be on any subspace of d10.13's or d10.36's cover, or on the ψ⁰, ψ² or
  ψ⁴ eigenspace (or its interior part) of d10.16's or d10.40's cover.
- On d10.16's and d10.40's covers, I(W) ≥ 3 at every class of rank 7. Generic classes of the cusp strata mix the eigenspaces and
  can reach rank 7.

The first registration's "on d10.13's or d10.36's cover" is withdrawn as too narrow. Its reason assumed that every class could
reach the global bound.

## A caveat on both, also before the read-out (2026-10-06, about 15:33Z; the run at task 513 of 556, no row read)

Both registrations assume that a subspace's generic classes reach the cup map's maximal rank (global, or graded on an
eigenspace). sm:B1541's record already shows that they need not. N₄₅'s graded bound is 9 on every eigenspace, but its generic
eigenspace classes reach only 8 (on ζ¹–ζ⁴) and 4 (on ζ⁰). If sm:B1542's generic classes in some subspace fall to rank ≤ 1,
Corollary C′ does not exclude (−3, −3) there. The prediction stands as registered; this is the assumption it rests on.
