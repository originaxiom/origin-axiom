# B1239 ADDENDUM (2026-10-04, from B1472; the sep16 lane's xB033 read): the closed statement needs two inputs, and the sign law is now sourced

This arc reached "cs ∈ {0, ½} mod 1 for every closed amphichiral manifold" through APS (3η ≡ 2cs + τ mod 2) with η = 0 under
an orientation-reversing isometry. The shorter route (the lane's): for closed M, cs is well defined mod 1 (CGHN §5A); an
orientation-reversing self-isometry gives cs ≡ −cs mod 1; so 2cs ≡ 0 and cs ∈ {0, ½}. No η, no τ. Both routes use the sign
law cs(M̄) = −cs(M), which this arc used without a source: it is definitional — cs(M) is the integral of the Chern–Simons
3-form over the oriented manifold (Meyerhoff's definition for hyperbolic M through the Riemannian connection), and reversing
the orientation reverses the integral; likewise η(M̄) = −η(M), the odd signature operator changing sign with the orientation
(Atiyah–Patodi–Singer I). SnapPy's convention checked in B1472: cs(M) + cs(M̄) ≡ 0 to 1.1·10⁻¹⁵ (mod 1) on 150 closed census
manifolds by this arc's cusped-parent route and to 5.6·10⁻¹⁶ (mod ½) on 150 cusped. The 37 of 37 stands; the lane reproduced
it at 10⁻⁶⁴ and found its own stricter predicate (is_full_group) over-strict, this arc's right.
