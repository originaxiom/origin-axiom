# B1282 addendum (2026-09-08) — verified exactly by main, and an environment note on step (1)

Main's **B1302** *the sibling m202, where three appears* re-derived this arc with an exact holonomy in SL(2, ℤ[ω])
(tr a = tr b = ω̄, tr ab = √−3, both cusps trace +2): h¹(m202; Sym^k) = 2 for every even k ≤ 22, the inversion the scalar
(−1)^(k/2+1) on every slot (= θ_D on e₆'s six slots), the order-3 rotation (ω, ω̄) on k ≡ 2 mod 6 and trivial on k ≡ 4
mod 6 — this arc's claim, **VERIFIED EXACTLY**; the addendum's Alexander-polynomial facts verified too (seven ±1
monomials, no primitive specialisation divisible by t² − 3t + 1, Δ(t, t) = −(2t² + 3t + 2)). Main adds that m202's two
peripheral classes generate H₁ = ℤ² (elementary divisors 1, 1), so the sibling has no non-trivial cusp-trivial character
and the descent's twist mechanism has no sector there.

**Environment note.** On main's bench `sibling_germ.py` asserted at its step (1): the word search found 62
automorphisms in 4 classes instead of 180 in 12 — SnapPy's choice of relator differs between installations and the search
over words of length ≤ 5 depends on it. The counts were never the claim (step (2)'s realisation of θ by the inversion
is), so the script now prints an environment note instead of asserting the counts and requires only that the inversion
(A, B) is among the automorphisms found; the lock keeps the 180/12 as this bench's expectation.
