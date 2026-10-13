# Quantum realization of the complete weave: run 1

**Date:** 10 October 2026  
**Input:** *A Weave of Two Records*, Dritëro M., October 2026, especially Sections 2–4.  
**Scope:** Independent mathematics and a conditional two-dimensional quantum-field-theory construction. No Standard Model parameters, fitted data, project code, or repository edits.

## Executive result

The complete function

\[
\Phi(\tau)=\eta(\tau)^{21}(\theta_2(\tau)^2,\theta_3(\tau)^2,\theta_4(\tau)^2)
\]

has a concrete realization as the span of unrefined torus one-point blocks in a known unitary tensor-product CFT. This is stronger than the previously noted partition-function identity, but it does **not** realize the complete weave: the insertion supplying the eta multiplier does not implement the quaternion puncture in the four-fermion factor.

Two exact obstructions sharpen the search:

1. The natural three-function projection cannot itself be promoted to three simple sectors of an ordinary unitary rational CFT. It yields the Ising fusion ring with an inadmissible twist and Frobenius–Schur indicator \(-\sqrt2\).
2. All three character twists \(\chi_p\rho_Q\) are unitarily equivalent. Accordingly, free Dirac operators with identical gauge-covariant domains are conjugate, and their insertion-free determinant magnitudes cannot provide the three varying theta blocks in the fixed parity-labelled basis.

The faithful Q8 cover is also constructed explicitly. It has eight sheets, four lifted punctures, and genus three after compactification. Both grammar generators preserve its defining kernel. This supplies a concrete, all-threads geometric domain for the next puncture-state calculation, not a calculated quantum completion.

---

## 1. Fixed conventions

Set \(q=e^{2\pi i\tau}\), and define

\[
\Psi_p=\theta_p^2/\eta^2,\qquad \Phi=\eta^{23}\Psi.
\]

The vector order is \((2,3,4)\). Write \(P_{24}\) for the permutation exchanging entries 2 and 4 while fixing 3. Direct theta transformations give

\[
\Psi(-1/\tau)=P_{24}\Psi(\tau),
\]

\[
\Psi(\tau+1)=e^{-\pi i/6}
\begin{pmatrix}i&0&0\\0&0&1\\0&1&0\end{pmatrix}\Psi(\tau).
\]

Thus

\[
\Phi(-1/\tau)=(-i\tau)^{23/2}P_{24}\Phi(\tau),
\]

\[
\Phi(\tau+1)=e^{7\pi i/4}
\begin{pmatrix}i&0&0\\0&0&1\\0&1&0\end{pmatrix}\Phi(\tau).
\]

With the standard automorphy factor \(\tau^{23/2}\), the S multiplier is
\(e^{\pi i/4}P_{24}\). Its fourth power is \(-I\). Exact enumeration over monomial matrices with eighth-root phases gives image order 96 and scalar center \(\{1,i,-1,-i\}\). The T eigenvalue exponents modulo 1 are \(1/8,3/8,7/8\).

This confirms the functional multiplier in the input. It does not independently reconstruct the original Hodge/cohomology identification.

## 2. The four-sector control and its complete pointed coherence data

The reference theory is the even chiral algebra of four real free fermions, \(\mathfrak{so}(4)_1\), with central charge 2. Its four labelled characters at zero chemical potentials are

\[
O=\frac{\Psi_3+\Psi_4}{2},\quad
V=\frac{\Psi_3-\Psi_4}{2},\quad
S=C=\frac{\Psi_2}{2}.
\]

The last equality is an equality of **unrefined functions**, not an identification of sectors. The diagonal partition function satisfies

\[
Z=|O|^2+|V|^2+|S|^2+|C|^2
=\frac12\sum_{p=2,3,4}|\Psi_p|^2.
\]

In the order \((O,V,S,C)\),

\[
S_4=\frac12\begin{pmatrix}
1&1&1&1\\
1&1&-1&-1\\
1&-1&-1&1\\
1&-1&1&-1
\end{pmatrix},\qquad
T_4=e^{-\pi i/6}\operatorname{diag}(1,-1,i,i).
\]

Verlinde multiplication gives the group \(\mathbb Z_2^2\):

\[
V^2=S^2=C^2=O,\qquad VS=C,\ VC=S,\ SC=V.
\]

A complete unitary pointed associator/braiding presentation uses
\(G=\mathbb F_2^2\), with labels
\(O=(0,0),V=(1,1),S=(1,0),C=(0,1)\), and

\[
\omega(a,b,c)=(-1)^{a_1b_1c_1+a_2b_2c_2},
\qquad R(a,b)=i^{a_1b_1+a_2b_2}.
\]

The twists are \(R(a,a)=(1,-1,i,i)\). All 256 scalar pentagon equations and all 128 scalar hexagon equations were checked exactly. Setting the associator incorrectly to 1, while keeping the braiding, fails 28 hexagon equations. This is an intentional negative control.

These checks establish coherence for the chosen four-sector control data. They are not checks of unknown Q8-twisted defects of the weave.

The four Frobenius–Schur indicators are \((1,1,-1,-1)\). Independent fermionic oscillator products and a D2-lattice enumeration reproduce the same character coefficients through relative order \(q^{16}\). The first terms are

\[
\begin{aligned}
O&=q^{-1/12}(1+6q+17q^2+38q^3+\cdots),\\
V&=q^{5/12}(4+8q+28q^2+56q^3+\cdots),\\
S=C&=q^{1/6}(2+8q+20q^2+48q^3+\cdots).
\end{aligned}
\]

## 3. An exact obstruction to the three-simple-sector interpretation

Restrict the four-dimensional torus representation to
\((O,V,X)\), where formally \(X=(S+C)/\sqrt2\). Then

\[
S_3=\frac12\begin{pmatrix}
1&1&\sqrt2\\
1&1&-\sqrt2\\
\sqrt2&-\sqrt2&0
\end{pmatrix},\qquad
T_3=e^{-\pi i/6}\operatorname{diag}(1,-1,i).
\]

These matrices obey \(S_3^2=(S_3T_3)^3=I\). Their formal Verlinde coefficients are nonnegative integers:

\[
V^2=O,\quad VX=X,\quad X^2=O+V.
\]

However, this does not suffice for consistent quantum sectors. The candidate quantum dimensions are \((1,1,\sqrt2)\), with total squared dimension 4. The Frobenius–Schur indicator is

\[
\nu_k=\frac{1}{\mathcal D^2}\sum_{a,b}N_{ab}^{k}d_a d_b
\left(\frac{\vartheta_a}{\vartheta_b}\right)^2.
\]

For the self-dual candidate X, four terms contribute, from
\((O,X),(X,O),(V,X),(X,V)\). Every twist ratio squared is \(-1\). Therefore

\[
\nu_X=\frac{4(-\sqrt2)}4=-\sqrt2.
\]

A self-dual simple sector requires \(\nu_X=+1\) or \(-1\). This candidate therefore cannot be the modular data of a bosonic unitary modular tensor category, or the complete three-primary modular data of an ordinary unitary rational CFT.

There is a simpler warning: the normalized merged function has leading coefficient \(2\sqrt2\), not an integer state multiplicity. Retaining an integer normalization instead loses the requisite symmetric normalized S matrix.

**Scope:** This is not an obstruction to three spin-structure functions, a three-dimensional flavour representation, an invariant subspace of a larger theory, or punctured conformal blocks. It is not a contradiction of the input's cohomology triplet. Multiplying all functions by a scalar eta power does not change their relative T eigenvalue phases, and cannot repair this particular promotion to vacuum-sector data.

The valid ordinary Ising twist \(e^{\pi i/8}\), with the same S and fusion ring, returns \(\nu_X=1\) in the independent positive control.

## 4. A unitary quantum origin for eta^23, as an insertion rather than a partition factor

Gaberdiel and Lang, equations (3.13)–(3.15), show that the Ising h=1/2 torus one-point chiral block satisfies

\[
\left(q\frac{d}{dq}-\frac{E_2}{24}\right)f=0,
\qquad f(\tau)=\eta(\tau)
\]

up to the normalization of the inserted field. The trace runs through the h=1/16 module, consistent with \(\psi\times\sigma=\sigma\).

This suggests the explicit, deliberately nonminimal control

\[
\mathcal C=\mathrm{Ising}^{\otimes23}\otimes\mathfrak{so}(4)_1,
\qquad \mathcal O=\psi^{\otimes23}\otimes\mathbf1.
\]

Its chiral central charge is \(23/2+2=27/2\), and the insertion has weight \(23/2\). Tensor factorization produces four labelled one-point blocks

\[
\mathcal B_a=\eta^{23}\chi_a^{\mathfrak{so}(4)_1},\qquad a=O,V,S,C.
\]

Their internal channel weights are \(23/16+h_a\). Consequently their q exponents are

\[
23/16+h_a-(27/2)/24
=7/8,\ 11/8,\ 9/8,\ 9/8.
\]

The combinations \(2\mathcal B_S,\mathcal B_O+\mathcal B_V,\mathcal B_O-\mathcal B_V\) are **exactly** the three components of Phi, not just functions with the same eigenvalue exponents. The known eta transformation laws provide the entire multiplier including its metaplectic central action.

A full local nonchiral realization is obtained by taking the diagonal full theory and the product of 23 Ising energy fields. It is a scalar local insertion with weights \((23/2,23/2)\). Its unnormalized one-point function is proportional to
\(|\eta|^{46}Z_{\mathfrak{so}(4)_1}\); normalization factors can be fixed by field normalization. The chiral construction is not being asserted to be a standalone anomaly-free chiral theory on every background.

This is a construction using known unitary CFTs, not a new claim that eta itself is an ordinary vacuum character. Indeed,

\[
\eta^{23}O=q^{7/8}(1-17q+109q^2+\cdots),
\]

which cannot count ordinary Hilbert-space degeneracies. Operator-inserted traces can have signed coefficients.

The eta recurrence and Euler product were checked by independent exact coefficient calculations through q^16. This finite check corroborates the analytic identity; it is not its proof.

**What this does not do:** it does not force 23 extra factors, predict an E6 representation, construct a critical string, or supply the quaternion puncture in the four-fermion factor. The insertion acts as the identity on that factor. Matching Phi as quantum blocks is therefore insufficient for a faithful weave completion.

## 5. Quaternion holonomy, ordinary spin fields, and a restricted puncture obstruction

On the real vector space underlying the quaternions, the matrices

\[
A=\begin{pmatrix}0&-1&0&0\\1&0&0&0\\0&0&0&-1\\0&0&1&0\end{pmatrix},
\qquad
B=\begin{pmatrix}0&0&-1&0\\0&0&0&1\\1&0&0&0\\0&-1&0&0\end{pmatrix}
\]

are in SO(4), satisfy \(A^2=B^2=-I\), and anticommute. Thus \([A,B]=-I\). They preserve the free-fermion OPE \(\psi^a(z)\psi^b(w)\sim\delta^{ab}/(z-w)\). Their real commutant has dimension 4, while its symmetric part has dimension 1.

This gives an exact faithful symmetry representation in the four-fermion control. It does not automatically give a consistent punctured quantum amplitude with the required lifts.

The four standard Ramond spin components have bosonized charges \((\pm1/2,\pm1/2)\), so h=1/4. Their OPE with a vector fermion has a sign branch monodromy. In the bosonic SO(4)_1 category the two spinor labels both have monodromy -1 against the vector label. The labels remain distinguishable by their behavior against other fields and by a chosen Spin(4) lift.

For an **ordinary untwisted** one-punctured torus, the block count with a primary a is

\[
\dim\mathcal V_{1,1}(a)=\sum_bN_{ab}^{b}=\mathrm{Tr}(N_a).
\]

In the four-sector pointed theory this gives \((4,0,0,0)\). Translation by a nonidentity element of \(\mathbb Z_2^2\) has no fixed points, proving the zeros.

Therefore appending a single ordinary S or C insertion to the factorized eta^23 construction gives zero torus blocks. This rejects that simple repair.

**Scope:** This is not a calculation of the Q8-twisted conformal blocks with noncommuting holonomies. Nonabelian symmetry-defect networks or other correctly specified backgrounds can change the relevant block problem. The zero above must not be advertised as a universal obstruction to the quaternion puncture.

## 6. Stronger free-determinant limitation: all parity twists are conjugate

In a separately implemented complex representation use

\[
A=\operatorname{diag}(i,-i),\qquad B=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
\]

Conjugation gives

\[
\begin{aligned}
A:(A,B)&\longmapsto(A,-B),\\
B:(A,B)&\longmapsto(-A,B),\\
AB:(A,B)&\longmapsto(-A,-B).
\end{aligned}
\]

These implement all three nontrivial characters of the two parity records. The intertwiners are constant and unitary. Hence

\[
\chi_p\otimes\rho_Q\simeq\rho_Q\quad\text{for each }p.
\]

Suppose a candidate free Dirac operator uses the same geometry, massless kinetic prescription, and gauge-covariant puncture domain for each bundle. Bundle isomorphisms then give

\[
D_{\chi_p\rho_Q}=U_pD_{\rho_Q}U_p^{-1}.
\]

The spectra of \(D^\dagger D\), kernel dimensions, and gauge-invariant determinant magnitudes agree. This remains true for consistently defined nonzero-mode determinants when zero modes occur. Chiral phase choices and anomalies require their own analysis; the equality of singular spectra is unaffected.

In contrast,

\[
\left|\frac{\Psi_2(i)}{\Psi_3(i)}\right|=\frac1{\sqrt2},
\qquad
\lim_{\operatorname{Im}\tau\to\infty}\left|\frac{\Psi_2(\tau)}{\Psi_3(\tau)}\right|=0.
\]

The first identity follows from S symmetry and Jacobi's quartic identity at i; the limit follows from the leading theta series. These ratios vary, so no fixed monomial rescaling of equal-norm parity determinants reproduces the theta triplet as parity-labelled vacuum amplitudes. The common eta^23 factor does not change the ratios.

**This is a conditional theorem against a specific interpretation**, not against the mathematical triplet. Isomorphic local systems can still carry a nontrivial action on a labelled direct sum, and correlators involving different states or insertions are not determined by the vacuum determinant. Parity-specific noncovariant boundary data also escape the hypotheses, but then constitute additional input that must be disclosed.

## 7. The faithful Q8 cover is concrete and respects every grammar move

The kernel of the surjective map \(F_2\to Q_8\) defines an eight-sheeted cover of the punctured torus. Use the regular action of Q8 on itself to label the sheets.

The peripheral element \([A,B]=-1\) has order two and no fixed sheet. Its permutation has four cycles of length two, so there are four lifted punctures. The Euler characteristic of the punctured cover is \(-8\); after filling the four ends it is \(-4\). Thus its compact genus is three. Riemann–Hurwitz independently gives

\[
2g-2=8(2\cdot1-2)+4(2-1)=4.
\]

The grammar maps \(L:(A,B)\mapsto(A,AB)\) and \(R:(A,B)\mapsto(AB,B)\) are automorphisms of Q8. Each is checked on all 64 products and fixes the central peripheral element. Consequently both preserve the kernel of \(F_2\to Q_8\), so both lift to the cover. This holds for every word in the allowed generators, not only the Fibonacci thread.

This does not choose a spin structure, puncture state, determinant normalization, or a physical mode interpretation. Pullback trivializes the flat monodromy away from the branch points, but fermion spin/ramification data must still be handled; it is not valid to replace the problem by arbitrary untwisted fermions on a compact genus-three surface. Genus three is not a derivation of three generations.

## 8. The next bounded calculation

The next object should be the **puncture-state conformal blocks** or operator matrix elements in the Q8-twisted free-fermion system, not three gauge-invariant vacuum determinants.

One concrete implementation is to construct the chiral Dirac problem on the eight-sheeted cover, retain the appropriate Q8-equivariant sector, and track its determinant line and zero-mode insertion space under the lifted L and R. The puncture-state dimension must be computed, not preset to three. Every spin or boundary choice must be enumerated or separately declared.

Promotion requires a nonzero block space whose lifted mapping-class action matches the original triplet, including the central phase, with an explicit map from the original cohomology/puncture states. Recovering only the normalized three theta functions is insufficient. Inserting eta^23 by spectator tensor factors is now available as a comparison control, not a derivation.

Failure could be a zero block space, a wrong representation, a phase mismatch, an uncancelled obstruction, or unconstrained extra choices. These are branch-specific outcomes. Four-dimensional chirality, spacetime dynamics, gravity and empirical predictions remain outside this run.

## 9. Reproduction and integrity

Run `verify.py`, `verify_cover.py`, and `verify_parity_conjugacy.py`. There are 34 main named test groups, 10 cover groups, and 8 parity-conjugacy groups. Within these are the complete 256/128 pointed coherence checks, finite modular-image enumeration, lattice/fermion coefficient comparisons and exact finite-group tests.

The numerical part was run at 80 and 100 decimal digits at six base points, including their S and T transforms. At 100 digits the largest reported relative residual across the numerical tests was about 3.67e-100. These are high-precision checks, not interval-arithmetic proofs or certified truncation-error bounds.

The initial local plan was hashed before its executable run, but was not independently timestamped or committed. Cover and parity tests were added later and labelled as addenda. One instrumentation-only correction is documented in CHANGELOG.md: integer twists are sympified before division to prevent accidental floating-point constants. All final symbolic data were rerun with a no-Float check. No result depended on Standard Model values or on choosing a special thread.

## Primary references

- Florakis and Rizos, *Free Fermionic Constructions of Heterotic Strings*, arXiv:2407.07034, Sections 2–4: free-fermion OPE, central charge, spin fields, theta determinants and consistency conditions. https://arxiv.org/abs/2407.07034
- Gaberdiel and Lang, *Modular differential equations for torus one-point functions*, arXiv:0810.0106, especially (2.15), (3.13)–(3.15): Ising one-point eta block and inserted-trace modular weight. https://arxiv.org/abs/0810.0106
- Bantay, *The Frobenius-Schur indicator in Conformal Field Theory*, hep-th/9610192, equation (1): indicator formula and allowed values. https://arxiv.org/abs/hep-th/9610192
- Rowell, Stong and Wang, *On classification of modular tensor categories*, arXiv:0712.1377, Example 2.2, Proposition 2.3 and Section 5.3: distinction between modular symbols and coherent category data; semion and Ising controls. https://arxiv.org/abs/0712.1377
- Angelantonj and Sagnotti, *Open Strings*, hep-th/0204089: orthogonal level-one characters. https://arxiv.org/abs/hep-th/0204089

These sources provide the known quantum frameworks and consistency theorems. The present factorized construction, exact projections, finite computations, and scoped conclusions are derived in this report. No claim of literature novelty is made.
