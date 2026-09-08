# B1304 addendum (2026-09-08) — two lemmas the criterion proves, and their check on every pair of levels

`verification/two_lemmas.py` (record `two_lemmas_run.txt`; the small levels' support files added to B1303's directory
for the check).

**Lemma 1 (pullback exactness).** Let d | n and let ψ be a character of H₁(Y_d), pulled back to Y_n (the same functional
on ℤ², Φ^d-invariant). The sequence x_k = ψ(Φ^k a) is d-periodic, so P_n(ψ) = P_d(ψ)^{n/d}; P_d(ψ) is unipotent
(B1304 §2), and a unipotent U = I + N with U^k = I has N = 0. Hence **h¹(Y_n; π*ψ) = h¹(Y_d; ψ)**: the pulled-back part
of Y_n's support is exactly the pullback of Y_d's support. Two consequences: the transfer's injectivity (B1301 §1 (c)) is
an equality on the tower; and the lens space Y₂'s characters, at h¹ = 0, stay at 0 on every even level — the law's
ramified clause is Lemma 1 plus Y₂ = L(5, q).

**Lemma 2 (Galois closure).** For k prime to the order of ψ, x_k(ψ^k) = x_k(ψ)^k, so P(ψ^k) = σ_k(P(ψ)) with σ_k the Galois
automorphism ζ ↦ ζ^k, and **h¹(Y_n; ψ^k) = h¹(Y_n; ψ)**: a character is in the support iff every generator of the cyclic
group it generates is. (This is why the eigenlines enter whole and why B1300's theorem could use "S closed under units".)

**Checked** on the banked supports: for every pair d | n with 2 ≤ d < n ≤ 21 (29 pairs), every character of Y_d
pulled back to Y_n has the same h¹ on both, and the Φ^d-invariant characters of Y_n's support are exactly those pullbacks;
and every support of levels 2 … 21 is closed under ψ ↦ ψ^k for k prime to the order.

What the two lemmas do not give is the even-level clause of the law (a character of Y_n not pulled back from Y_{n/2},
n even, has h¹ = 0): with ψ′ = t^{n/2}ψ the product splits as P_n(ψ) = P_{n/2}(ψ′) P_{n/2}(ψ), and for the eigencharacters
with u^{n/2} ≡ −1 one has ψ′ = ψ⁻¹ and P_{n/2}(ψ′) the complex conjugate of P_{n/2}(ψ), so the clause says that a rank-one
nilpotent N is never purely imaginary in the sense conj(N) = −N there — verified through Y₂₁, not proved (L210(iv)).
