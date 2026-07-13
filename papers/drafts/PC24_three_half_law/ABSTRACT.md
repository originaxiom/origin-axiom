# PC24 — Abstract and significance

## Title

**The 3/2 Law: Minimal Self-Coupling Growth of a Block-Matrix Substitution Tower**

## Abstract

For a non-negative integer matrix $M$ define the escalator functor
$T_k(M) = \begin{pmatrix} M & M \\ M^k & M \end{pmatrix}$ and the tower
$M_0 = F$ (the Fibonacci matrix), $M_{n+1} = T_2(M_n)$. We prove an elementary
Perron law: if $M$ is primitive with Perron eigenvalue $\lambda$, then
$T_k(M)$ has Perron eigenvalue $\lambda(1+\lambda^{(k-1)/2})$, so the
log-Perron growth exponent of the $T_k$-tower is $(k+1)/2$; $k = 2$ is the
minimal coupling with super-multiplicative growth, giving the exponent $3/2$.
Numerically $\lambda_n \sim \varphi^{\,C(3/2)^n}$ with $C = 2.4283$. The
spectrum doubles exactly via $\mu \mapsto \mu(1\pm\sqrt\mu)$, which doubles
the Perron field at each of the first five rungs (a norm-sign proof) and
generates a second, arithmetic tower: the charge
$e_n = \det(I - M_n) = -1, -11, -809, -18845089, \dots$ satisfies
$e_{n+1} = \operatorname{Res}(p_n, g)$ for the single fixed cubic
$g = x^3 - x^2 + 2x - 1$ (discriminant $-23$), admits the golden-norm closed
form $e_n = N_{\mathbb{Q}(\sqrt5)/\mathbb{Q}}(g_n(\varphi))$ (proved for
$n \le 3$ via an explicit resultant transfer), and grows with log-exponent 3
while the field grows with exponent 2 and the Perron-log with exponent 3/2.
The prime divisors are orbit-selected ($11 \mid e_n$ exactly at
$n \equiv 1 \pmod 3$ within the computed range; $3, 5, 7, 13, 23$ never
appear), and we show there is no simple closed period law. The Galois groups
of the rung polynomials are $D_4$ and $8T15 = \mathrm{SmallGroup}(32,43)$,
both exact; our own conjecture $|G_n| = 2^{2n+1}$ is refuted at rung 3 by a
Chebotarev census ($P \approx 5.8\times10^{-37}$), consistent with the proved
sub-fullness of arboreal images for post-critically finite quadratic
iterations (Pink; Benedetto–Ghioca–Juul–Tucker). The tower carries a canonical
operator-algebraic reading: $K_0(\mathcal{O}_{M_n}) = \mathbb{Z}/|e_n|$ is
cyclic at every verified rung, giving
$\mathcal{O}_{M_1} \cong \mathcal{O}_{12}$,
$\mathcal{O}_{M_2} \cong \mathcal{O}_{810}$ and
$\mathcal{O}_{M_3} \cong \mathcal{O}_{18845090}$ by Kirchberg–Phillips
classification, with a unique KMS state at inverse temperature
$\beta_n = \log\lambda_n$ — the growth law is also a temperature law.

## Significance statement

Just as the golden ratio is the growth rate of the minimal non-trivial
self-substitution, we show that 3/2 is the growth exponent of the minimal
non-trivial self-*coupling* — one elementary block-matrix rule applied to
itself — and that this single rule simultaneously generates a square-root
field tower, an integer "charge" sequence governed by one fixed cubic acting
as norms from $\mathbb{Q}(\sqrt5)$, an arboreal Galois tower with exactly
identified small groups, and an exactly classified family of Cuntz algebras.
The paper pairs each closed form with its honest boundary: a refuted
conjecture (the Galois-order formula, killed by a census of 11255 primes) and
a proved-as-far-as negative (no closed period law for the charge primes) are
presented as results, with the census methodology reusable. The work connects
substitution dynamics, arboreal Galois theory and C\*-algebra classification
through a single two-line functor, with every claim carrying an explicit
status label and a machine-verified computation.

## Target journal

*Experimental Mathematics* (primary target: a focused article whose theorems
are elementary but whose exact tower data, census methodology and clearly
labelled open conjectures fit the journal's remit). Alternative: a short note
in a general venue of the *Advances in Mathematics* communications type if the
per-rung engine (Conjecture 4.4) is closed before submission.
