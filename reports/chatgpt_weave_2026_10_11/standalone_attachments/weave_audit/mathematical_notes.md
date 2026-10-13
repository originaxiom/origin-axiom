# Independent mathematical audit of *A Weave of Two Records*

**Date:** 10 October 2026.  
**Basis:** the supplied nine-page PDF and selected public repository records.  
**Repository snapshot consulted:** `6c148ddd495d133213140995976ff08849793d5d`.  
**Scope:** independent selected-claim verification, not certification of the entire repository, its history, all 1,400 computations, or all 7,000 checks.

The executable `verify_weave.py` imports no code from the Origin Axiom repository. Exact calculations use rational/Gaussian-rational polynomial linear algebra and integer cyclotomic exponents. Numerical calculations use direct theta series in tau and an independent Dedekind eta product. They are not interval certificates.

## 1. A proof of the golden spectrum on the entire axis

### Statement

Let theta_2, theta_3, theta_4 denote the standard Jacobi theta constants and eta the Dedekind eta function. For

\[
C=\{\tau\in\mathbb H:|\tau-\tfrac12|=\sqrt5/2\},
\qquad F(\tau)=\sum_{p=2,3,4}\left|\frac{\theta_p(\tau)}{\eta(\tau)}\right|^4,
\]

one has **F(tau)=8 at every point of C**. Consequently the symmetric matrix

\[
Y(\tau)=\begin{pmatrix}
0&\theta_4^2&\theta_3^2\\
\theta_4^2&0&\theta_2^2\\
\theta_3^2&\theta_2^2&0
\end{pmatrix}
\]

has normalized singular values **1 : phi^(-1) : phi^(-2)** throughout C.

This is an analytic derivation made in this audit from a classical modular equation. It is not a claim that the classical equation is new, or that these singular values describe physical fermion masses.

### Classical input: Ramanujan's degree-five equation

Write alpha=lambda(z), beta=lambda(5z), where lambda=theta_2^4/theta_3^4. For positive imaginary z, Ramanujan's degree-five equation reads

\[
\sqrt{\alpha\beta}+\sqrt{(1-\alpha)(1-\beta)}
+2\{16\alpha\beta(1-\alpha)(1-\beta)\}^{1/6}=1.
\]

A precise accessible reference is M. C. Mahesh Kumar, B. N. Dharmendra and P. S. Guruprasad, *Modular equations of ratio's of Ramanujan quantity*, Palestine Journal of Mathematics 6(1) (2017), 173–178, Lemma 2.7, equation (2.8), p.175. That lemma cites B. C. Berndt, *Ramanujan's Notebooks*, Part III (1991), Entry 13(i), p.280.

Using theta_3^4=theta_2^4+theta_4^4 and theta_2 theta_3 theta_4=2 eta^3, multiply by theta_3(z)^2 theta_3(5z)^2. With u_p=theta_p^2 the result is

\[
u_3(z)u_3(5z)-u_2(z)u_2(5z)-u_4(z)u_4(5z)
=8\eta(z)^2\eta(5z)^2. \tag{1}
\]

All roots in the first step are positive on the positive imaginary axis. Equation (1) then extends to the entire upper half-plane by the identity theorem, because both of its sides are holomorphic there. This avoids assuming a global branch for the fractional powers in the original modular equation.

### Bringing the geodesic into the identity

For tau in C, one has 2 tau conjugate(tau)=tau+conjugate(tau)+2. Set

\[
z=\frac{\tau}{1-2\tau},\qquad h=1-2\tau.
\]

The matrix defining z has determinant one and maps the upper half-plane to itself. The circle equation gives

\[
5z=-\bar\tau-2. \tag{2}
\]

The standard S and T transformation laws, composed for the matrix [[1,0],[-2,1]], give

\[
(u_2(z),u_3(z),u_4(z))=h(u_2(\tau),u_3(\tau),-u_4(\tau)),
\]

\[
\eta(z)^2=h e^{\pi i/3}\eta(\tau)^2.
\]

Conjugation and translation by minus two, using (2), give

\[
(u_2(5z),u_3(5z),u_4(5z))=
(-\overline{u_2(\tau)},\overline{u_3(\tau)},\overline{u_4(\tau)}),
\]

\[
\eta(5z)^2=e^{-\pi i/3}\overline{\eta(\tau)^2}.
\]

Substituting into (1) therefore gives

\[
h\sum_p |\theta_p(\tau)|^4=8h|\eta(\tau)|^4.
\]

Neither h nor eta vanishes in the upper half-plane, so division proves **F(tau)=8**.

### Recovering the singular values

Every complex symmetric 3-by-3 matrix with zero diagonal can be made entrywise nonnegative off the diagonal by a diagonal unitary congruence. There are precisely three equations for the three rephasing angles. Congruence by a unitary matrix preserves singular values.

Divide the resulting real matrix by 2|eta|^2 and denote its off-diagonal entries by a,b,c. Jacobi's product identity and F=8 give

\[
a^2+b^2+c^2=2,\qquad abc=\tfrac12.
\]

Its characteristic polynomial is

\[
\lambda^3-(a^2+b^2+c^2)\lambda-2abc
=\lambda^3-2\lambda-1
=(\lambda+1)(\lambda^2-\lambda-1).
\]

Its eigenvalues are phi, -1, -phi^(-1); their absolute values, divided by phi, are the stated golden spectrum.

Since F is invariant under SL(2,Z), the same result holds on every modular image of C. **This proves inclusion of those geodesics in the level set F=8. It does not prove the converse that the level set has no other components.** Nor does it supply a dynamical principle selecting C.

## 2. Exact counterexample to universal degeneracy at omega

The PDF's Section 5 table says that every coupling is degenerate at omega=exp(2 pi i/3). This is false for the full T tensor T space admitted later in the same section.

Use the same theta-squared variables u=(u2,u3,u4), with u3^2=u2^2+u4^2. The theta-side representation of the field triplet is

\[
\rho(S)=\zeta_8\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},\quad
\rho(T)=\begin{pmatrix}\zeta_8&0&0\\0&0&\zeta_8^7\\0&\zeta_8^7&0\end{pmatrix},
\qquad \zeta_8=e^{\pi i/4}.
\]

At weight three the symmetric and antisymmetric coupling spaces each have dimension one. An exact polynomial basis is

\[
S_3=\begin{pmatrix}
0&-u_4(2u_2^2+u_4^2)&u_3(u_2^2-u_4^2)\\
-u_4(2u_2^2+u_4^2)&0&u_2(u_2^2+2u_4^2)\\
u_3(u_2^2-u_4^2)&u_2(u_2^2+2u_4^2)&0
\end{pmatrix},
\]

\[
A_3=\begin{pmatrix}
0&u_4^3&u_3(u_2^2+u_4^2)\\
-u_4^3&0&u_2^3\\
-u_3(u_2^2+u_4^2)&-u_2^3&0
\end{pmatrix}.
\]

They satisfy, exactly in the theta ring,

\[
Y(\gamma\tau)=(c\tau+d)^3\rho(\gamma)^{-T}Y(\tau)\rho(\gamma)^{-1},
\quad \gamma=S,T.
\]

Their admissibility is computed as an exact nullspace in the script, not inferred merely from the value of a matrix at one point.

At omega, standard theta branches give

\[
\frac{u_2}{u_4}=\frac{1-i\sqrt3}{2},\qquad
\frac{u_3}{u_4}=\frac{\sqrt3-i}{2}.
\]

For the allowed coupling Y=S3+2A3,

\[
Z=Y(\omega)/u_4(\omega)^3=
\begin{pmatrix}
0&2+i\sqrt3&-\sqrt3-2i\\
-2+i\sqrt3&0&-2-i\sqrt3\\
-\sqrt3+2i&2-i\sqrt3&0
\end{pmatrix}.
\]

Exactly,

\[
\det(\lambda I-Z^\dagger Z)=(\lambda-27)(\lambda-12)(\lambda-3).
\]

The singular values are 3sqrt(3),2sqrt(3),sqrt(3): **3:2:1, all distinct.**

This does not refute a carefully restricted symmetric-only degeneracy statement. It refutes the unqualified statement for every coupling in the full space. It also does not make omega phenomenologically viable: existence of a nondegenerate spectrum is much weaker than a successful mass-and-mixing fit.

## 3. Exact algebraic checks and a missing hypothesis

For the matrices printed in the PDF,

\[
L=\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad
R=\begin{pmatrix}1&0\\1&1\end{pmatrix},\quad
P=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\]

(LP)^2=LR holds. But

\[
RL^{-1}R=\begin{pmatrix}0&-1\\1&0\end{pmatrix},\qquad (RL^{-1}R)^2=-I.
\]

Thus the group containing L,R and their inverses cannot exclude -I on homology. A positive semigroup of physical updates can exclude it; a full modular change-of-marking group cannot. At the free-group level different lifts of the same homology matrix must also be distinguished. B1634 itself records words of homology -I with scalar lifts +i and -i. The appropriate correction is a precise distinction of these notions, not a conclusion that all downstream calculations are wrong.

The Fricke maps

\[
L:(x,y,z)\mapsto(x,z,xz-y),\qquad
R:(x,y,z)\mapsto(z,y,yz-x)
\]

have common fixed points (0,0,0) and (2,2,2), exactly. The first is the quaternion character; the second is the trivial character. Quaternion uniqueness is correct on the relative character surface

\[
\operatorname{tr}[a,b]=-2,\qquad x^2+y^2+z^2-xyz=0,
\]

but not on the unrestricted character variety. The repository includes this hypothesis; the PDF should restore it.

A separate convention caution: with the displayed free-group substitutions, sigma^2 and LR agree on homology and in the outer automorphism group, but the literal automorphisms differ by an inner conjugation. This does not spoil the mapping-torus identification; equalities of lifts should specify their level.

## 4. Representation and coupling counts

Exact enumeration of the theta-side monomial matrices gives order 96. The character norm is exactly one; the inner product with its complex conjugate is zero. Thus this theta representation is irreducible and not equivalent to its conjugate. The central scalar phases are 1,i,-1,-i, and the modular T exponents are 1/8,3/8,7/8.

The script independently reproduces the entire coupling table:

| Weight | Diagonal symmetric | Off-diagonal symmetric | Antisymmetric | Symmetric total | Full total |
|---|---:|---:|---:|---:|---:|
|1|0|1|0|1|1|
|3|0|1|1|1|2|
|5|1|2|1|3|4|
|7|1|2|2|3|5|
|9|2|3|2|5|7|
|11|2|3|3|5|8|

This is exact linear algebra in C[u2,u3,u4]/(u3^2-u2^2-u4^2), with Gaussian-rational coefficients. It is not a numerical rank test. It presupposes the usual identification with the ring of holomorphic modular forms of Gamma(4).

For the theta-squared representation A, the weight-three vector-valued space has dimension one and its generator has a nonzero cusp value, proportional to (0,1,1). Under h=eta^3 f, the required cusp-vanishing condition therefore forces M_(3/2)(rho)=0. This independently verifies the relevant holomorphic zero count. The separate physical assertion about adding one unit of cusp data to obtain a four-dimensional index of three has not been derived in this audit.

The geometric cohomology-to-theta intertwiner, the Hodge-Riemann form, all puncture boundary conditions, the physical Dirac dictionary and the anomaly questions have not all been reconstructed independently here. Verification of the theta-side matrices is not a substitute for those tasks.

## 5. Claim scope found in the repository

The PDF's universal statement that each odd-trace thread's geometric holonomy reduces to the quaternion point at a prime of norm three is stronger than its cited record.

B1601's FINDINGS.md explicitly separates a proved linearized lemma from a census law. The census contains 16 odd-trace and 21 even-trace geometries through primitive word length eight. It explicitly leaves open the general existence, uniqueness and multiplicity-one claim for the norm-three prime. A universal abstract parity/finite-group construction must not be conflated with this stronger arithmetic property of the geometric representation.

The existence of B1636's preregistration commit was checked. A stale ledger row describing it as untracked is not evidence that no preregistration was committed. No full historical audit of preregistration timing or the entire automated test count was performed.

## 6. Physics and current-data boundaries

The three nonzero parity characters are genuinely forced after choosing rank two and reduction modulo two. This is not by itself a derivation of three Standard Model generations. Lambda adds a spacetime/internal-space dictionary, E6 representation content, an identification of holomorphic modes with left-handed matter, and other physical commitments; the cusp unit is another input.

Modular covariance alone does not force holomorphic couplings. Holomorphy, admissible weights, the Higgs representation, kinetic normalization and permitted higher operators must be specified. Nonminimal modular-invariant kinetic terms can change physical mass ratios and mixing. The paper states a minimal Kahler assumption; it should be promoted to the main assumption list.

At weight three, the two-dimensional complex coupling space supports the paper's parameter counting under those assumptions. The audit additionally finds numerical local rank six for an eight-component quark-shape map at a generic six-real-parameter point. This supports local codimension two, not the empirical success of two explicit relations. No quark fit was performed.

JUNO's September 2026 preprint reports sin^2(theta12)=0.3036 +/- 0.0064. For an illustrative sin^2(theta13)=0.022, TM1 gives 0.3183367 and TM2 0.3408316. Their simple one-dimensional Gaussian pulls are about 2.30 and 5.82 respectively. These are not updated global-fit significances; they show why a table relying only on NuFIT 6.0 and the first JUNO result needs a dated update.

## References and provenance

- Supplied PDF, *A Weave of Two Records*, Dritero M., October 2026, especially Sections 1–8.
- Origin Axiom repository, `frontier/B1601_the_common_point_is_the_geometry_mod_3/FINDINGS.md`.
- Origin Axiom repository, `frontier/B1634_w50_on_main/FINDINGS.md`.
- Origin Axiom repository, B1636 verification script and preregistration commit `6d3c2ee30d859a381d9e91db1a657a8a7bad88f1`.
- Mahesh Kumar, Dharmendra and Guruprasad (2017), Lemma 2.7, citing Berndt (1991), Entry 13(i). Publisher PDF: https://pjm.ppu.edu/sites/default/files/papers/PJM_MAR_2017_21.pdf
- NIST Digital Library of Mathematical Functions, Chapter 20, especially Section 20.7: https://dlmf.nist.gov/20.7
- Novichkov, Penedo and Petcov, *Double Cover of Modular S4 for Flavour Model Building*, arXiv:2006.03058, NPB 963 (2021), 115301.
- Liu, Yao, Qu and Ding, *Half-integral weight modular forms and application to neutrino mass models*, arXiv:2007.13706, PRD 102 (2020), 115035.
- Almumin et al., *Metaplectic Flavor Symmetries from Magnetized Tori*, arXiv:2102.11286, JHEP 05 (2021), 078.
- JUNO Collaboration, *Measurement of Neutrino Oscillation Parameters at JUNO and Indication of the Neutrino Mass Ordering*, arXiv:2609.37895v1.

## Run outcome

At 100 decimal digits and 120 sampled points, the maximum observed absolute error in F=8 was about 4.57e-100, and the normalized singular-value error about 6.07e-101. Those are numerical observations, not rigorous error bounds. The analytic proof above is the basis for the whole-axis theorem. Exact algebra supplies the coupling counts and omega counterexample independently of this numerical evidence.
