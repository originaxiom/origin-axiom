# The 3/2 Law: Minimal Self-Coupling Growth of a Block-Matrix Substitution Tower

**Author:** originaxiom

**Status of results.** Every result carries one of four labels: [PROVED] — an exact symbolic
argument or exact (integer/algebraic) computation proving the stated instance; [COMPUTED] — a
numerical or statistical computation, with its precision stated; [CITED] — a literature result
used but not re-proved; [CONJECTURE] — an open statement, with the evidence for and against it
stated plainly.

---

## Abstract

For a non-negative integer matrix $M$ define the *escalator functor* $T_k(M) = \begin{pmatrix} M
& M \\ M^k & M \end{pmatrix}$ and the tower $M_0 = F$ (the Fibonacci matrix), $M_{n+1} =
T_2(M_n)$. We prove an elementary Perron law: if $M$ is primitive with Perron eigenvalue
$\lambda$, then $T_k(M)$ has Perron eigenvalue $\lambda(1+\lambda^{(k-1)/2})$, so the log-Perron
growth exponent of the $T_k$-tower is $(k+1)/2$; $k=2$ is the minimal coupling with
super-multiplicative growth, giving the exponent $3/2$; numerically $\lambda_n \sim
\varphi^{\,C(3/2)^n}$ with $C = 2.4283$. The spectrum doubles exactly under $T_2$ via $\mu
\mapsto \mu(1\pm\sqrt{\mu})$, which doubles the Perron field at each of the first five rungs (a
norm-sign proof) and generates a second, arithmetic tower: the *charge* $e_n = \det(I - M_n) =
-1, -11, -809, -18845089, \dots$ obeys $e_{n+1} = \operatorname{Res}(p_n, g)$ for the single
fixed cubic $g = x^3 - x^2 + 2x - 1$ (discriminant $-23$), admits the golden-norm closed form
$e_n = N_{\mathbb{Q}(\sqrt5)/\mathbb{Q}}(g_n(\varphi))$ (proved for $n \le 3$), and grows with
log-exponent $3$ while the field grows with exponent $2$ and the Perron-log with exponent $3/2$.
The prime divisors are orbit-selected — $11 \mid e_n$ exactly at $n \equiv 1 \pmod 3$ within
reach, while $3,5,7,13,23$ never appear — with no simple closed period law. The Galois groups of
the rung polynomials are $D_4$ and $8T15 = \mathrm{SmallGroup}(32,43)$, both exact; our own
conjecture $|G_n| = 2^{2n+1}$ is *refuted* at rung 3 by a Chebotarev census ($P \approx
5.8\times10^{-37}$). Finally, $K_0(\mathcal{O}_{M_n}) = \mathbb{Z}/|e_n|$ is cyclic at every
verified rung, giving $\mathcal{O}_{M_1} \cong \mathcal{O}_{12}$, $\mathcal{O}_{M_2} \cong
\mathcal{O}_{810}$, $\mathcal{O}_{M_3} \cong \mathcal{O}_{18845090}$ by Kirchberg–Phillips
classification, and a unique KMS state at $\beta_n = \log\lambda_n$: the $3/2$ law is also a
temperature law.

---

## 1. Introduction

The golden substitution $a \mapsto ab$, $b \mapsto a$ is the minimal non-trivial
self-substitution: its incidence matrix $F$ has Perron eigenvalue $\varphi$, the smallest Pisot
number arising this way, and the resulting combinatorics (Fibonacci word, golden quasicrystal)
is the standard testbed of substitution dynamics [1, 2]. This paper studies what happens when
the same minimality principle is applied one level up: instead of substituting a letter into a
word, we couple a whole substitution system to itself through the pair $(M, M^2)$, and iterate.

Concretely, define for a non-negative integer $N \times N$ matrix $M$ the block matrix

$$T_k(M) \;=\; \begin{pmatrix} M & M \\ M^k & M \end{pmatrix} \qquad (k \ge 1),$$

and set $T = T_2$. Starting from the Fibonacci matrix $F$, the tower $M_n = T^n(F)$ consists of
non-negative integer matrices of size $2^{n+1}$; each is the incidence matrix of a primitive
substitution on $2^{n+1}$ letters (Section 8 exhibits the rung-2 substitution explicitly). The
first rung is itself distinguished: $T(F)$ coincides *verbatim* — not merely up to conjugation —
with the incidence matrix of the 4-letter substitution

$$\sigma_4:\quad a \mapsto abAAB,\quad b \mapsto aAB,\quad A \mapsto abAB,\quad B \mapsto aA,$$

which arose independently in our programme; this identity [PROVED, exact] is what motivated the
tower.

The paper establishes three groups of results. **(1) The 3/2 law** (Section 3): the Perron
eigenvalue of $T_k(M)$ is $\lambda(1+\lambda^{(k-1)/2})$ — an elementary theorem — so the
tower's log-Perron growth exponent is $(k+1)/2$; $k=2$, the minimal coupling with
super-multiplicative growth, gives exactly $3/2$. What $\varphi$ is to the word, $3/2$ is to the
tower. **(2) The charge tower** (Sections 4–5): the spectrum doubles exactly via $\mu \mapsto
\mu(1\pm\sqrt\mu)$; one consequence is analytic (the Perron field doubles at every verified
rung), the other arithmetic — the integers $e_n = \det(I - M_n)$ form a second tower, generated
by a single fixed cubic through a resultant recursion, expressible as norms from
$\mathbb{Q}(\sqrt5)$, with orbit-selected prime divisors and log-growth exponent $3$. **(3)
Galois and operator-algebraic structure** (Sections 6–7): exact Galois groups $D_4$ and
$\mathrm{SmallGroup}(32,43)$; the natural guess $|G_n| = 2^{2n+1}$ refuted at rung 3 by a census
(presented as a result, not a footnote); Cuntz algebras with cyclic $K_0$ of order $|e_n|$,
classified exactly at the first three rungs.

**Scope and precedents, stated up front.** The qualitative frames here are not new, and we cite
them as such: coupled and graph-directed substitution systems are classical [1, 2]; torsion
groups as invariants of substitution systems go back to Kellendonk's integer group of
coinvariants [6]; the $K$-theory identification $K_0(\mathcal{O}_A) = \operatorname{coker}(I -
A^t)$ is textbook [3, 12]; and the qualitative sub-fullness of arboreal Galois images for
post-critically finite quadratic iterations is a proved theorem of Pink and of
Benedetto–Ghioca–Juul–Tucker [8, 9, 7]. Our claims are narrower: the functor $T_k$ and its
$(k+1)/2$ Perron law, the exact tower data (fields, Galois groups, charges), and the charge
arithmetic. A literature search targeted at exactly these items found no match; Section 9 states
the limits of that search.

---

## 2. The tower

**Definition 2.1.** $F = \begin{pmatrix}1&1\\1&0\end{pmatrix}$; $T_k(M) = \begin{pmatrix} M &
M\\ M^k & M\end{pmatrix}$; $T = T_2$; $M_0 = F$, $M_{n+1} = T(M_n)$, so $M_n$ has size
$2^{n+1}$. Write $p_n(x) = \det(xI - M_n)$ for the characteristic polynomial, $\lambda_n$ for
the Perron eigenvalue, $d_n = \det M_n$, and $e_n = \det(I - M_n) = p_n(1)$.

**Proposition 2.2 [PROVED].** *If $M$ is primitive then $T_k(M)$ is primitive.* Every block of
$T_k(M)^m$ is a sum of products of $m$ factors, each $M$ or $M^k$, hence a sum of powers $M^j$
with $m \le j \le km$; if $M^j > 0$ for all $j \ge K$, all blocks are positive once $m \ge K$.
$\square$

**Basic data [PROVED, exact / COMPUTED as noted].** The characteristic polynomials of rungs 0–4
have degrees $2, 4, 8, 16, 32$ and are all irreducible over $\mathbb{Q}$ [PROVED, exact
factorisation]. The first three are

$$p_0 = x^2 - x - 1,\qquad
p_1 = x^4 - 2x^3 - 5x^2 - 4x - 1,$$
$$p_2 = x^8 - 4x^7 - 56x^6 - 152x^5 - 205x^4 - 192x^3 - 134x^2 - 56x - 11.$$

The Perron eigenvalues are $\lambda_0 = \varphi = 1.618\dots$, $\lambda_1 = 3.676205\dots$,
$\lambda_2 = 10.724751771861389\dots$, $\lambda_3 = 45.8469\dots$, $\lambda_4 = 356.278\dots$
[COMPUTED, to the digits shown]. The determinants are $d_n = -1, -1, -11, -97889, \approx
-1.8\times10^{17}$ [PROVED, exact].

---

## 3. The Perron law and the 3/2 growth exponent

**Theorem 3.1 (Perron law) [PROVED].** *Let $M$ be a primitive non-negative matrix with Perron
eigenvalue $\lambda$. Then the spectral radius of $T_k(M)$ is*

$$\mu \;=\; \lambda\bigl(1 + \lambda^{(k-1)/2}\bigr).$$

*Proof.* Let $v > 0$ be a Perron eigenvector of $M$ and set $w = (v,\; c\,v)^t$ with $c > 0$ to
be chosen. Then $T_k(M)\,w = \bigl((1+c)\lambda v,\; (\lambda^k + c\lambda)v\bigr)^t$, which is
proportional to $w$ iff $\lambda^k + c\lambda = c(1+c)\lambda$, i.e. $c^2 = \lambda^{k-1}$.
Taking $c = \lambda^{(k-1)/2} > 0$ gives $T_k(M)\,w = \mu w$ with $\mu = \lambda(1 +
\lambda^{(k-1)/2})$ and $w > 0$ strictly positive. For a non-negative matrix, an eigenvalue with
a strictly positive eigenvector equals the spectral radius (Collatz–Wielandt). $\square$

**Corollary 3.2 (the 3/2 law) [PROVED].** *Along the $T_k$-tower, $\log\mu / \log\lambda \to
(k+1)/2$ as $\lambda \to \infty$. In particular $k = 1$ gives exponent $1$ (no
super-multiplicative growth: $\mu = 2\lambda$), and $k = 2$ — the minimal coupling with exponent
$> 1$ — gives exponent $3/2$. For the tower $M_n = T^n(F)$:*

$$\lambda_{n+1} = \lambda_n\bigl(1 + \sqrt{\lambda_n}\bigr), \qquad
\frac{\log \lambda_{n+1}}{\log \lambda_n} \longrightarrow \frac32 .$$

The $\lambda$-law holds *exactly* at every rung by Theorem 3.1 and Proposition 2.2. The
log-ratios through rung 7 are $2.705,\ 1.822,\ 1.612,\ 1.536,\ 1.509,\ 1.501,\ 1.500$
[COMPUTED], monotonically decreasing to the proved limit.

**Proposition 3.3 (asymptotic constant) [COMPUTED].** $\lambda_n \sim \varphi^{\,C\,(3/2)^n}$
with $C = 2.4283$: the estimates $\log\lambda_n / ((3/2)^n \log\varphi)$ for $n = 1,\dots,7$ are
$1.80,\ 2.19,\ 2.36,\ 2.41,\ 2.426,\ 2.4282,\ 2.4283$, converging to four significant figures.
Existence of the limit follows from the $\lambda$-law ($\log\lambda_{n+1} =
\tfrac32\log\lambda_n + \log(1 + \lambda_n^{-1/2})$, with corrections summable against
$(3/2)^{-n}$); no closed form for $C$ is known.

Corollary 3.2 is the point of the title: the golden substitution is the minimal non-trivial
self-*substitution* and its rate is $\varphi$; the escalator $T_2$ is the minimal non-trivial
self-*coupling* and its rate is $3/2$.

---

## 4. Spectral doubling and field growth

**Proposition 4.1 (spectral doubling) [PROVED].** *Let $M$ be an $N \times N$ matrix with $N$
distinct non-zero eigenvalues. Then $T(M)$ is diagonalisable with spectrum exactly*

$$\operatorname{spec} T(M) \;=\; \bigl\{\, \mu(1 \pm \sqrt{\mu}) \;:\; \mu \in \operatorname{spec} M \,\bigr\}.$$

*Proof.* For an eigenpair $(\mu, u)$ of $M$ and $c$ with $c^2 = \mu$, the computation in Theorem
3.1 shows $(u, \pm c\,u)^t$ is an eigenvector of $T(M)$ with eigenvalue $\mu(1 \pm \sqrt\mu)$.
For fixed $\mu \ne 0$ the pair spans $\{(u,0),(0,u)\}$; across distinct eigenvalues the $u$'s
are independent, so the $2N$ vectors are a basis. $\square$

Every rung applies (charpolys irreducible, hence simple spectra; $d_n \ne 0$). Two exact
consequences follow.

**Corollary 4.2 (characteristic-polynomial recursion; determinant telescope) [PROVED].**

$$p_{n+1}(x) \;=\; \pm\operatorname{Res}_t\!\bigl(p_n(t),\; x^2 - 2tx + t^2 - t^3\bigr),
\qquad d_{n+1} \;=\; d_n^{\,2}\, e_n .$$

*Proof.* The first identity is Proposition 4.1: the two branches contribute the quadratic factor
$(x - \mu(1+\sqrt\mu))(x - \mu(1-\sqrt\mu)) = x^2 - 2\mu x + \mu^2 - \mu^3$ per eigenvalue. The
second is the commuting-block formula $\det T(M) = \det(M\cdot M - M\cdot M^2) = \det(M)^2
\det(I - M)$. $\square$

**Theorem 4.3 (field doubling, rungs 0–4) [PROVED].** *For $0 \le n \le 4$: $\sqrt{\lambda_n}
\notin \mathbb{Q}(\lambda_n)$. Hence the extension $\mathbb{Q}(\lambda_n, \sqrt{\lambda_n}) /
\mathbb{Q}(\lambda_n)$ is quadratic at each of the first five doubling steps, and — with the
verified irreducibility of $p_0,\dots,p_4$ — the Perron fields $\mathbb{Q}(\lambda_n)$ have
degrees $2^{n+1} = 2, 4, 8, 16, 32$.*

*Proof (norm-sign argument).* Since $p_n$ is irreducible of even degree $2^{n+1}$, the field
norm of $\lambda_n$ is the product of all conjugates,
$N_{\mathbb{Q}(\lambda_n)/\mathbb{Q}}(\lambda_n) = p_n(0)\cdot(-1)^{2^{n+1}} = \det M_n = d_n$.
By the telescope, $d_{n+1} = d_n^2 e_n$, and $e_n < 0$ at every verified rung ($e_n = -1, -11,
-809, -18845089, -228654672055316545291$ for $n = 0,\dots,4$ [PROVED, exact]); with $d_0 = -1$
this forces $d_n < 0$ for all verified $n$. If $\sqrt{\lambda_n} \in \mathbb{Q}(\lambda_n)$ then
$d_n = N(\lambda_n) = N(\sqrt{\lambda_n})^2 \ge 0$, a contradiction. $\square$

**Conjecture 4.4 [CONJECTURE].** For all $n$: (i) $p_n$ is irreducible over $\mathbb{Q}$; (ii)
$e_n < 0$. Under (i)–(ii) the proof of Theorem 4.3 propagates to every rung and
$[\mathbb{Q}(\lambda_n) : \mathbb{Q}] = 2^{n+1}$ for all $n$. Both hypotheses are per-rung
checkable; both are verified at rungs 0–4, and (ii) also at rung 5 ($e_5 < 0$, a 62-digit
integer). No proof for general $n$ is known.

**Proposition 4.5 (magnitude-degeneracy law) [PROVED for $n \le 4$].** *For $0 \le n \le 4$ the
matrix $M_n$ has exactly two real eigenvalues, and every pair of distinct eigenvalues sharing
the same modulus is a complex-conjugate pair; hence the number of such pairs is exactly*

$$\frac{2^{n+1} - 2}{2} \;=\; 2^n - 1 \qquad (= 0, 1, 3, 7, 15).$$

The two per-rung facts (exactly two real roots; no accidental modulus coincidences beyond
conjugation) are established by exact computation at each rung; the count is then forced.
Whether the pattern persists for all $n$ is open [CONJECTURE].

**Remark 4.6 (departure from the cyclotomic world) [COMPUTED + CITED].** $\lambda_1$ has
non-abelian Galois closure $D_4$ (Section 6), hence is not a cyclotomic integer; by
Calegari–Morrison–Snyder [10], no fusion category of any rank has an object of dimension
$\lambda_1$ (corroborated by an exhaustive rank-4 search: of 92 candidate rings with the correct
characteristic polynomial, none is a fusion ring). Rung 0 categorifies ($\varphi \in
\mathbb{Q}(\zeta_5)$, the Fibonacci category); the tower provably leaves the fusion-categorical
world at rung 1.

---

## 5. The charge tower

Set $e_n = \det(I - M_n) = p_n(1)$, the *charge* of rung $n$ (the terminology records that
$\operatorname{coker}(I - M_n)$ is the standard torsion invariant of the associated substitution
system; cf. [6] and Section 7).

**Data [PROVED, exact].**

| $n$ | $e_n$ | factorisation |
|---|---|---|
| 0 | $-1$ | — |
| 1 | $-11$ | prime |
| 2 | $-809$ | prime |
| 3 | $-18845089$ | prime |
| 4 | $-228654672055316545291$ | $-11^2 \cdot 1459 \cdot 597049 \cdot 2169349081$ |
| 5 | $\approx -1.455 \times 10^{61}$ (62 digits) | $-(6433367189401 \cdot 19807876161211 \cdot 114192827433802916537068946505308579)$ |

The naive law "one new prime per rung" — true through $n = 3$ — is *refuted* at $n = 4$: $e_4$
is composite and the base prime 11 recurs with multiplicity two [PROVED, exact].

### 5.1 One fixed cubic

**Proposition 5.1 [PROVED].** *Let $g(x) = x^3 - x^2 + 2x - 1$ (discriminant $-23$). Then*

$$e_{n+1} \;=\; \prod_{\mu \in \operatorname{spec} M_n} \bigl((1-\mu)^2 - \mu^3\bigr)
\;=\; \det\!\bigl(I - 2M_n + M_n^2 - M_n^3\bigr) \;=\; \operatorname{Res}(p_n,\, g).$$

*Proof.* By Proposition 4.1, $e_{n+1} = \prod_\mu (1 - \mu(1+\sqrt\mu))(1 - \mu(1-\sqrt\mu)) =
\prod_\mu ((1-\mu)^2 - \mu^3) = \prod_\mu (-g(\mu))$; the number of factors $2^{n+1}$ is even,
and for monic arguments $\operatorname{Res}(p_n, g) = \prod_{p_n(\mu)=0} g(\mu)$. $\square$

Verified exactly through rung 5: the resultant reproduces $-11, -809, -18845089,
-228654672055316545291$ from the preceding characteristic polynomials [PROVED, exact]. The
entire arithmetic tower is one fixed cubic evaluated over the growing spectra; all charge primes
$(11, 809, 1459, 597049, 2169349081, \dots)$ come from $g$.

### 5.2 The golden-norm closed form

**Theorem 5.2 [PROVED for $n \le 3$].** *Define the doubling transfer on polynomials by $D(G)(y)
= \operatorname{Res}_t\bigl(t^2 - 2yt + y^2 - y^3,\; G(t)\bigr)$, and set $g_1 = g$, $g_{n+1} =
D(g_n)$ (so $\deg g_n = 3^n$). Then, with $\varphi = (1+\sqrt5)/2$,*

$$e_n \;=\; N_{\mathbb{Q}(\sqrt5)/\mathbb{Q}}\bigl(g_n(\varphi)\bigr)
\qquad (n = 1, 2, 3).$$

At $n=1$ directly: $g_1(\varphi) = 3\varphi - 1 = (1+3\sqrt5)/2$ and $(3\varphi-1)(3\varphi'-1)
= -11$. At $n = 2, 3$: $g_2 = D(g_1)$ (degree 9) gives $N(g_2(\varphi)) = -809$, and $g_3 =
D(g_2)$ (degree 27) gives $N(g_3(\varphi)) = -18845089$, both in exact $\mathbb{Q}(\sqrt5)$
arithmetic, cross-checked against $\det(I - M_n)$. The charge tower is a single cubic walking on
$\varphi$, pushed up by one fixed resultant transfer. Whether the closed form holds for all $n$
is [CONJECTURE] (the transfer construction is defined for all $n$; the norm identity is proved
only where computed).

**Proposition 5.3 (two-step transfer polynomial) [COMPUTED, exact instances].** With $G(v) =
-v^9 + 3v^8 - 5v^7 + 2v^6 - 4v^5 + 3v^4 - 8v^3 + 6v^2 - 4v + 1$ (degree $9 = 3^2$),

$$e_{n+1} \;=\; \det G(M_{n-1})$$

holds exactly for $n = 1, \dots, 4$, reproducing $e_2, e_3, e_4, e_5$. (This is the one-step law
of Proposition 5.1 composed through one doubling; a fixed degree-9 kernel drives the charge two
rungs at a time.)

### 5.3 Orbit-selected primes; no closed period law

**Proposition 5.4 (divisibility mechanism) [PROVED].** *For a prime $p$: $p \mid e_n \iff 1 \in
\operatorname{spec}(M_n) \bmod p \iff$ the doubling orbit $\mu \mapsto \mu(1 \pm \sqrt\mu)$ of
the golden pair $\{\varphi, \psi\}$ in $\overline{\mathbb{F}}_p$ reaches $1$ at rung $n$;
equivalently $p \mid e_{n+1} \iff p_n$ and $g$ share a root mod $p$.* (Immediate from $e_n =
p_n(1)$ and Proposition 5.1.)

**Computed phenomenology [COMPUTED / PROVED as noted].**

- **$p = 11$ has period 3.** $11 \mid e_n$ exactly at $n = 1, 4, 7, 10$ within
the computed range $n \le 11$ (matrices to size $4096$; independent modular determinants)
[PROVED, exact, for $n \le 11$] — the base charge $\mathbb{Z}/11$ recurs every three rungs, with
multiplicity 2 at $n = 4$. The all-$n$ law "$11 \mid e_n \iff n \equiv 1 \pmod 3$" is
[CONJECTURE] beyond the range.
- **$p = 809$ has large period** ($> 9$): it appears only at $n = 2$ for
$n \le 11$ [PROVED, exact, in range].
- **Sparsity.** Among all primes $3 \le p \le 79$, only $11$ divides any $e_n$
for $n \le 8$ [PROVED, exact, in range].
- **Necessary is not sufficient.** $g$ has a linear root mod $p$ for
$p \in \{5, 7, 11, 17, 19, 23, 809\}$ and is inert for $p \in \{3, 13, 29\}$; yet $5$ and $7$
divide no $e_n$ in range — the orbit must actually *reach* the root, and for these primes it
does not (within reach). Moreover $19, 61, 79$ share $11$'s factorisation type for $g$ and its
quadratic-residue condition, and none divides any $e_n$ in range: no congruence or factorisation
condition we tested determines appearance.

**Conclusion (a proved-as-far-as negative).** A prime's period in the charge tower is a genuine
finite-field doubling-orbit return time — computable per prime by iterating $\mu \mapsto
\mu(1\pm\sqrt\mu)$ in the splitting field — and is *not* reducible to any closed form in $p$
that we could find. The mechanism is fully characterised (Proposition 5.4); "which primes, with
what period" appears intrinsically dynamical, and we state this plainly. A further subtlety:
eventual periodicity of $e_n \bmod p$ is automatic for linear recurrences but *not* obvious for
this non-linear tower (the ambient field degree grows), so even "$5$ never divides $e_n$"
remains open pending a periodicity lemma.

### 5.4 Three exponents

Per rung, three growth rates coexist [COMPUTED]:

- the **field** doubles: degree $2^{n+1}$ (exponent 2, Theorem 4.3);
- the **Perron-log** grows by $3/2$ (Corollary 3.2);
- the **charge-log** grows by $3$: $\log|e_{n+1}| / \log|e_n| =
2.79,\ 2.50,\ 2.80,\ 3.00 \to 3$, forced by the degree-tripling of $g_n$ in Theorem 5.2.

Consequently the "per-site free energy" $f_n = \log|e_n| / 2^{n+1}$ has no thermodynamic limit:
it is strictly increasing and diverges as $(3/2)^n$, with $f_n / (3/2)^n \to 0.29$ approximately
[COMPUTED]. The $3/2$ of Section 3 reappears as the divergence rate of the charge density.

---

## 6. Galois structure: exact groups, a refuted conjecture, arboreal scoping

**Theorem 6.1 (exact Galois groups) [PROVED, exact computation].** *Let $G_n =
\operatorname{Gal}(p_n)$. Then $G_0 = \mathbb{Z}/2$; $G_1 = D_4$ (transitive group $4T3$; order
8, non-abelian, signature $(2,1)$); and $G_2 = 8T15 = \mathrm{SmallGroup}(32, 43) = C_8 \rtimes
(C_2 \times C_2)$, of order 32.* The rung-2 identification is exact (computer algebra), and
independently corroborated by a Frobenius census matching the theoretical conjugacy-class
fractions to within $0.006$ [COMPUTED].

In particular the natural guess $G_n \cong (\mathbb{Z}/2)^{n+1}$ (abelian Kummer tower) is
refuted already at rung 1: the doubling extensions interleave non-trivially. What survives of
it: $e_n \in \mathbb{Z}$ is Galois-invariant, and the non-abelian $D_4$ — with its complex
embeddings — is exactly the mechanism behind the conjugate-pair degeneracies of Proposition 4.5
and the non-cyclotomicity of Remark 4.6.

**Proposition 6.2 (a refuted conjecture, kept as a result) [COMPUTED].** The orders $|G_1| = 8 =
2^3$ and $|G_2| = 32 = 2^5$ suggest $|G_n| = 2^{2n+1}$. This conjecture — ours — is **refuted at
rung 3**: under $|G_3| = 128$, a Chebotarev census over $11255$ primes should produce $\approx
87.9$ identity-Frobenius hits; the census observed **1**, an outcome of probability $\approx 5.8
\times 10^{-37}$ under the conjecture. The data are consistent with $|G_3| \gtrsim 2048$: the
tower grows *faster* than the formula. We include the refutation deliberately: the census
methodology (class-fraction matching at rung 2, identity-hit counting at rung 3) is the reusable
content, and a two-point extrapolation died by it.

**Remark 6.3 (arboreal scoping) [CITED + COMPUTED].** The doubling step $\mu \mapsto \mu(1 \pm
\sqrt\mu)$ is a quadratic correspondence of post-critically finite type, so the tower $\{G_n\}$
embeds in the automorphism tower of the binary rooted tree, and the *qualitative* expectation —
sub-fullness of the image, with widening index — is a proved theorem in the
arboreal-representation literature: Pink [8] and Benedetto–Ghioca–Juul–Tucker [9]; see Jones's
survey [7]. Our exact data match this frame: the image is **full** at depths 1–2 (orders 2 and
8) and has **index 4** at depth 3 ($32$ against $2^7 = 128$) [PROVED, exact]. We claim only the
exact identifications; the qualitative collapse is [CITED].

**Remark 6.4 (arithmetic linking of the charge primes) [PROVED computation; CITED framework].**
In Morishita's arithmetic-topology dictionary [11], $809 \equiv 1 \pmod 4$ and $(809/11) =
(-11/809) = -1$ give $\mathrm{lk}_2(11, 809) = 1$: the first two charge primes are non-trivially
linked in $\operatorname{Spec} \mathbb{Z}$. A curiosity with teeth or a coincidence — recorded
without further claim.

---

## 7. The Cuntz-algebra reading

Each $M_n$ is a primitive integer matrix, hence defines a Cuntz–Krieger-type algebra
$\mathcal{O}_{M_n}$ with $K_0(\mathcal{O}_{M_n}) = \operatorname{coker}(I - M_n^{\,t})$ and $K_1
= \ker(I - M_n^{\,t})$ [CITED: Cuntz–Krieger [3]; for the substitution context Anderson–Putnam
[12]; the coinvariants reading Kellendonk [6]].

**Proposition 7.1 [PROVED, exact, rungs 1–3].** *$K_1 = 0$ (since $e_n \ne 0$), and
$K_0(\mathcal{O}_{M_n}) \cong \mathbb{Z}/|e_n|$ is* cyclic *at every verified rung: the Smith
normal form of $I - M_n$ has a single non-trivial invariant factor, for $n = 1, 2, 3$.*

**Corollary 7.2 (exact classification) [COMPUTED + CITED].** By the Kirchberg–Phillips
classification of purely infinite simple nuclear C\*-algebras [4], an algebra with $(K_0, [1],
K_1) = (\mathbb{Z}/m, \text{ generator}, 0)$ is $\mathcal{O}_{m+1}$. The class $[1]$ is a
generator at the verified rungs (checked coprime at rung 3; automatic at rungs 1–2 where $|e_n|$
is prime once $[1] \neq 0$, which is verified), giving

$$\mathcal{O}_{M_1} \cong \mathcal{O}_{12}, \qquad
\mathcal{O}_{M_2} \cong \mathcal{O}_{810}, \qquad \mathcal{O}_{M_3} \cong
\mathcal{O}_{18845090}.$$

The identifications are ours; the classification theorem is [CITED].

**Remark 7.3 (KMS temperature ladder) [CITED + COMPUTED].** By Exel's Ruelle–Perron–Frobenius
theory for gauge actions [5], each $\mathcal{O}_{M_n}$ carries a *unique* KMS state for the
gauge action, at inverse temperature $\beta_n = \log \lambda_{\mathrm{PF}}(M_n) =
\log\lambda_n$, built from the Perron eigenvectors already computed. Hence, by the 3/2 law,
$\beta_{n+1} / \beta_n \to 3/2$: the growth law is a temperature law. Honest boundary: a
primitive finite matrix yields exactly one KMS temperature per rung — there is no phase
transition here.

---

## 8. The explicit rung-2 carrier

Every rung is realisable: a non-negative integer matrix is the incidence matrix of a
substitution, and primitivity persists (Proposition 2.2). At rung 2 we make this concrete.

**Proposition 8.1 [PROVED, exact].** *Reading column $j$ of $M_2 = T(M_1)$ as the Parikh vector
of letter $j$'s image yields a primitive substitution $\sigma_8$ on 8 letters with image lengths
$(23, 14, 18, 11, 10, 6, 8, 4)$:*

```
1 -> 1 2 3 3 4 5 5 5 5 5 6 6 6 7 7 7 7 7 7 8 8 8 8
2 -> 1 3 4 5 5 5 6 6 7 7 7 7 8 8
3 -> 1 2 3 4 5 5 5 5 6 6 7 7 7 7 7 8 8 8
4 -> 1 3 5 5 6 6 7 7 7 8 8
5 -> 1 2 3 3 4 5 6 7 7 8
6 -> 1 3 4 5 7 8
7 -> 1 2 3 4 5 6 7 8
8 -> 1 3 5 7
```

*with incidence matrix exactly $T(M_1)$, primitive (its square is positive), and satisfying the
seed invariant: letter 1 occurs exactly once, at position 0, in every image* (row 1 of $T(M_1)$
is all-ones, as at rung 1 where the seed letter of $\sigma_4$ has the same signature — the
invariant lifts). Only the Parikh columns are matrix-forced; the intra-image order is a gauge,
and seed-first is the representative realising the invariant.

**Rung-2 field data [PROVED, exact / COMPUTED].** $K = \mathbb{Q}(\lambda_2)$ has degree 8,
signature $(2, 3)$ — not totally real, not Galois — with subfield tower $\mathbb{Q} \subset
\mathbb{Q}(\sqrt5) \subset \mathbb{Q}(\sqrt5, \sqrt\varphi) \subset K$ of degrees $2, 4, 8$, and
polynomial discriminant $-2^{16} \cdot 5^4 \cdot 59^2 \cdot 12641^2$.

---

## 9. Limitations

What this paper does **not** establish.

1. **All-$n$ statements are conditional.** Irreducibility of $p_n$ and
   negativity of $e_n$ are proved only at rungs 0–4 (negativity also at rung
   5). Field doubling for all $n$ (Conjecture 4.4), the $2^n - 1$ degeneracy
   law for all $n$, and the golden-norm closed form for $n \ge 4$ are open.
2. **$C = 2.4283$ is numerical** — four significant figures from seven rungs;
   no closed form, and we do not know whether one exists.
3. **The rung-3 Galois group is not determined.** $|G_3| \ne 128$ holds with
   overwhelming statistical confidence and the census is consistent with
   $|G_3| \gtrsim 2048$, but the refutation is a census argument, not an exact
   computation, and no replacement formula is proposed.
4. **No period law.** Section 5.3's negative is bounded by the computed range
   ($n \le 11$, primes to 79); eventual periodicity of $e_n \bmod p$ —
   automatic for linear recurrences — is unproved for this non-linear tower,
   so even the observed exclusions ($5, 7, \dots$) hold in range only.
5. **The functor is a canonical choice, not a forced one.** Within the
   operations we examined, alternatives do not escalate — covers and
   higher-block presentations preserve the Perron eigenvalue (classical) —
   but "only coupling escalates" is scoped to the operations considered.
6. **Novelty is scoped, not absolute.** Graph-directed substitutions,
   coinvariant torsion invariants, Cuntz–Krieger $K$-theory and qualitative
   arboreal sub-fullness are prior art [1, 2, 6, 3, 12, 8, 9]. Our targeted
   search found no prior occurrence of the functor $T_k$, the $(k+1)/2$ law,
   or this tower's exact data; a finite search cannot prove absence.
7. **No claims outside mathematics.** The tower is studied as a
   combinatorial-arithmetic object; no interpretation beyond the stated
   theorems is asserted.

---

## 10. Outlook

Three directions seem ripest. **(i) Close the per-rung engine.** Conjecture 4.4 reduces all-$n$
field doubling to two checkable facts; a proof of $e_n < 0$ (e.g. via the golden-norm form) plus
an irreducibility argument would make Sections 4–5 unconditional. **(ii) Determine $G_3$.**
Pink's closed forms for iterated monodromy groups of quadratic correspondences [8] against the
census is the discriminating computation; the field-degree criterion of
[9] may promote the depth-2 fullness to a clean theorem. **(iii) The charge
arithmetic.** A periodicity lemma for $e_n \bmod p$ would turn the exclusions of Section 5.3
into theorems; the linking phenomenon of Remark 6.4 invites higher (Rédei-type) invariants of
the charge primes — noting that $11 \equiv 3 \pmod 4$ requires the twisted form of the Rédei
symbol. Separately, the $(k+1)/2$ family for $k \ge 3$ has not been explored beyond the Perron
law and may have a quite different arithmetic.

---

## Methods and computations

All exact claims were computed in integer/symbolic arithmetic (characteristic polynomials,
resultants, Smith normal forms, exact $\mathbb{Q}(\sqrt5)$ norms), with Galois groups by exact
computer algebra (PARI-class algorithms) and, at rung 2, an independent Frobenius census (class
fractions to $0.006$). Perron data used power iteration cross-checked against the exact
$\lambda$-law; the rung-3 census used $11255$ primes; modular determinants (matrices to size
$4096$) verified the divisibility patterns of Section 5.3. Every numbered fact is locked in an
accompanying machine-verified test suite.

---

## References

[1] M. Queffélec, *Substitution Dynamical Systems — Spectral Analysis*, 2nd
ed., Lecture Notes in Mathematics 1294, Springer, 2010.

[2] M. Baake and U. Grimm, *Aperiodic Order. Volume 1: A Mathematical
Invitation*, Encyclopedia of Mathematics and its Applications 149, Cambridge University Press,
2013.

[3] J. Cuntz and W. Krieger, A class of C\*-algebras and topological Markov
chains, *Invent. Math.* **56** (1980), 251–268.

[4] N. C. Phillips, A classification theorem for nuclear purely infinite
simple C\*-algebras, *Doc. Math.* **5** (2000), 49–114; E. Kirchberg, unpublished; see also M.
Rørdam, *Classification of Nuclear C\*-Algebras*, Springer, 2002.

[5] R. Exel, KMS states for generalized gauge actions on Cuntz–Krieger
algebras (an application of the Ruelle–Perron–Frobenius theorem), arXiv:math/0110183.

[6] J. Kellendonk, The local structure of tilings and their integer group of
coinvariants, *Comm. Math. Phys.* **187** (1997), 115–157.

[7] R. Jones, arXiv:1402.6018 (survey of arboreal Galois representations).

[8] R. Pink, Profinite iterated monodromy groups arising from quadratic
polynomials, arXiv:1307.5678.

[9] R. Benedetto, D. Ghioca, J. Juul and T. Tucker, arXiv:2411.06745
(arboreal Galois images of quadratic maps).

[10] F. Calegari, S. Morrison and N. Snyder, Cyclotomic integers, fusion
categories, and subfactors, *Comm. Math. Phys.* **303** (2011), 845–896.

[11] M. Morishita, Analogies between knots and primes, 3-manifolds and number
rings, arXiv:0904.3399; *Knots and Primes*, Universitext, Springer, 2012.

[12] J. E. Anderson and I. F. Putnam, Topological invariants for substitution
tilings and their associated C\*-algebras, *Ergodic Theory Dynam. Systems* **18** (1998),
509–537.

