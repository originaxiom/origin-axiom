# F1 — THE UNIFORM JUMP LAW, THEOREM FORM (cc2, 2026-07-16)
# Evidence: f1_certificates.json — 325/325 EXACT integer identities (no floats).

**Theorem (the uniform jump law).** Let w be a Weyl class with fixed-point group
A_w = Z^6 / B_w Z^6 (elementary divisors d = p^a), q the induced quadratic form
(mu^T C6 B_w^{-1} mu), and G_w(r) the Gauss sum at multiplier r. Then
   |G_w(r)|^2 = prod over elementary divisors p^a of p^(a + min(v_p(r), a)).
Equivalently |term_w(r)| / |term_w(generic)| = prod p^(min(v_p(r), a)/2) — no
odd/dyadic case split.

**Proof shape, odd p (standard local computation):** decompose the p-part of
(A_w, q) into cyclic blocks Z/p^a with unit forms u x^2 / p^a. For multiplier
r = p^v u': the reduced form r q on Z/p^a has radical of index p^(a - min(v, a));
the sum factors as (radical size) x (a nondegenerate Gauss sum on the quotient),
giving |G_p|^2 = p^a * p^(min(v,a)). Multiply over blocks.

**The 2-adic case (the previously priced step):** the coroot Gram C6 is EVEN
(diagonal 2), so every 2-adic block of q is even-type — the local forms are
hyperbolic/E8-type unimodular blocks scaled by 2^a, never odd-diagonal type. For
even-type blocks the same radical count holds with no odd-type correction terms
(the subtlety that motivates the usual case split — odd-type characters mod 8 —
never arises because odd-type blocks never occur). Hence min(v, a) uniformly,
which is exactly what the certificates verify at v_2(r) = 1 (r = 14, 18, 22),
v_2 = 2 (r = 20, 24), v_2 = 3 (r = 16, 24) and beyond, on divisors up to 2^3 and
composite 2^3*5 (d = 8, 40): 325/325.

**Status:** every instance of the law over the full class list x r = 13..25 is an
exact integer identity (Gates 1: 25/25 generic = |det|; Gate 2: 300/300 ratios;
spot checks 6/6 class-function). The remaining distance to a fully self-contained
proof is the general even-type local lemma written out abstractly (textbook
material: Wall, quadratic forms on finite groups; no novelty) — the theorem is
usable now, with each application instance certifiable by one integer computation.

Pairs with: P1's certification (the generic sector sums), Q3-L3 (the discovery),
D2 (periodicity — which now also follows structurally: min(v_p(kappa), a) and the
twist characters depend only on kappa's capped local data).
