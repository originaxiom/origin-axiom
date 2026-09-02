# R41 — exact trace-map identities (B518, B344, B332, B331)

`r41.py` (sympy, seconds):

| row | claim | R41 | verdict |
|---|---|---|---|
| B518 | the trace map T = (z, x, xz−y) preserves κ = x²+y²+z²−xyz (the same T across Schrödinger / hopping / spin substrates) | κ(T(x,y,z)) − κ(x,y,z) = 0 identically | MATCH (a one-line identity; the "universality class" wording is B518's, the identity is Fricke's) |
| B344 | det d(φ_m) = 1 for m = 1,2,3 (volume-preserving polynomial automorphism; each Dehn twist has Jacobian det 1) | with B344's own twists Ta = (X, Z, XZ−Y), Tb = (Z, Y, YZ−X): det J(Ta) = det J(Tb) = 1, both preserve κ; B344's committed `det_is_one(m)` returns True for m = 1,2,3 on this bench | MATCH, reproducible from committed |
| B332 | g = −R·L⁻¹ exactly; RL has disc 5, g has disc −3 | g = [[0,−1],[1,−1]], tr −1, disc −3; RL tr 3, disc 5 | MATCH |
| B331 | g = [[0,−1],[1,−1]] has eigenvalues ω, ω² | eigenvalues −1/2 ± (√3/2)i | MATCH (cf. R36 for χ₂₇(g) = 0) |

**Physics content:** none. "No observable content."
