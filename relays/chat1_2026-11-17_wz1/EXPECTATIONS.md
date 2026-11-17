# Expectations, written before any check is run (2026-11-17)

C1. Hecke's period formula for the act. Integrate the non-holomorphic Eisenstein series E(z, s) of PSL(2, Z)
    (E = sum over Gamma_inf\Gamma of Im(gz)^s) along one period of the closed geodesic of LR = [[2,1],[1,1]].
    Expect I(s) = c * 5^(s/2) * Gamma(s/2)^2 / Gamma(s) * zeta_K(s) / zeta(2s), with K = Q(sqrt 5),
    zeta_K = zeta * L(., chi_5), and c a constant independent of s (1/2, 1 or 2 depending on conventions).
    Consequence expected: I(rho) = 0 at the first Riemann zero rho = 1/2 + 14.1347...i, and at the first zero of
    L(s, chi_5). Failure: the ratio varies with s, or I(rho) is not small against nearby values.

C2. m004 and the Bianchi orbifold. Expect vol(m004) = 6 * Lobachevsky(pi/3) = 12 * vol(PSL(2, Z[w]) \ H^3),
    with Humbert's vol = 3^(3/2) * zeta_{Q(sqrt -3)}(2) / (4 pi^2). Failure: mismatch beyond 1e-20.

C3. Congruence. Riley's group <A, B>, A = [[1,1],[0,1]], B = [[1,0],[-w,1]], has index 12 in PSL(2, Z[w]).
    Question: does it contain a principal congruence subgroup Gamma(N) for some rational N in {2,3,4,6,7,8,12}?
    No expectation committed: this seat does not know the answer. Check: index of the image in PSL(2, O/N) equals 12
    for some N (then congruence of level dividing N); the BFS must also reproduce index 12 nowhere above 12.
