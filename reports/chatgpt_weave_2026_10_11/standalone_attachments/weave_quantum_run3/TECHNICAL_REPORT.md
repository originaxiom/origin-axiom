# Quantum realization of the weave — run 3
## An explicit faithful Gaussian amplitude and an exact scalar-multiplier mismatch

**Date:** 10 October 2026.  
**Inputs:** *A Weave of Two Records* (October 2026), especially §§2–4, and *Weave Quantum Realization — Run 2*.  
**Scope:** Analytic mathematics and one explicitly specified two-dimensional free-fermion model. No observed particle parameters, no change to the source manuscript or repository, and no claim of a four-dimensional theory or gravitational completion.

## Executive result

The requested phase test can be performed in a fixed, faithful Gaussian model. Its zero-mode-saturated chiral amplitude is, up to a modulus-independent normalization,

\[
\boxed{\mathcal A(z|\tau)=\eta(\tau)
\frac{\bigl(\theta_3(z|2\tau),\theta_2(z|2\tau)\bigr)}
{\sqrt{\theta_1(z|\tau)}}.}
\]

It has the quaternion monodromy and the chosen minimal half-pole at the puncture. It is derived from a free-field charge trace on an index-two cover, not by adjusting an eta factor to the target. Direct theta sums and independently factored oscillator products give the same result.

The puncture residue is

\[
U(\tau)=\frac{\bigl(\theta_3(2\tau),\theta_2(2\tau)\bigr)}{\sqrt{\eta(\tau)}}.
\]

Its three quadratic components are

\[
K(\tau)=\frac{\bigl(\theta_2(\tau)^2,\theta_3(\tau)^2,\theta_4(\tau)^2\bigr)}{\eta(\tau)}.
\]

Relative to the quaternion-normalizer rotation representation \(O\),

\[
\boxed{\rho_K=\chi_{\eta^5}\otimes O,
\qquad \rho_\Phi=\chi_{\eta^3}\otimes O.}
\]

The difference is the order-twelve scalar character \(\chi_{\eta^2}\), with values \(e^{\pi i/6}\) on modular \(T\) and \(-i\) on modular \(S\). The Gaussian quadratic image has order 288, whereas the manuscript's target has order 96. Their Dehn-twist eigenvalues differ, so a constant change of basis cannot repair the mismatch.

The **geometric** zero-mode profile, before its quantum oscillator normalization, does yield the target finite multiplier in its quadratic residues. Its spatial Wronskian is exactly \(-\pi\eta^3\). This is a useful identity, but a Wronskian of two component functions is not the functional determinant of the fermion field. Including the oscillator factor changes the corresponding quantum Wronskian to \(-\pi\eta^5\).

**Verdict:** The direct identification of these minimally prescribed Gaussian puncture amplitudes with the target triplet fails. The faithful quantum amplitudes themselves are explicit and nonzero. This is neither a contradiction of the original cohomology representation nor a no-go theorem for every possible quantum completion.

**Important limitation:** We calculate holomorphic chiral amplitude multipliers in a specified conformal-field-theory determinant trivialization. We do not separately construct the complete Quillen metric/connection, evaluate singular-Dirac spectral zeta functions, or compute Bismut–Freed parallel-transport holonomies. Modular coefficient multipliers must not be advertised as those unperformed calculations.

---

## 1. What is fixed, and what is not derived from the weave

The source specifies a rank-two quaternion representation on a once-punctured torus and a labelled three-parity cohomology construction. Its target is

\[
\Phi=\eta^{21}(\theta_2^2,\theta_3^2,\theta_4^2),
\]

of modular weight \(23/2\), with the exact lifted multiplier stated in the manuscript. Run 2 reduced that multiplier to \(\chi_{\eta^3}\otimes O\), and explicitly left its quantum origin open.

For this calculation we add the following **model assumptions**, rather than claiming that the grammar already dictates a field theory:

- One massless complex rank-two chiral fermion, equivalently two complex or four real chiral fermions, with chiral central charge \(c=2\). Locally its action is the Gaussian action \(\int \widetilde\psi\,\bar\partial_{E}\psi\), with the usual conformal normalization.
- The faithful flat quaternion background on \(E_\tau\setminus\{0\}\), where \(E_\tau=\mathbb C/(\mathbb Z+\tau\mathbb Z)\).
- The odd base spin structure, and the extension allowing the minimal \(z^{-1/2}\) pole. This is the \(E_+\) extension in Run 2, not a classification of all physical puncture domains.
- The coordinate-flat local metric, standard oscillator normal ordering, and prime-form normalization of local operator products. No target-dependent scalar line or spectator theory is included.

The underlying stable rank-two extension has degree one and \((h^0,h^1)=(1,0)\), as proved for this prescription in Run 2. Thus an insertion-free Grassmann integral vanishes, and one fermion insertion saturates its single holomorphic zero mode.

The resulting object is an **unnormalized chiral block with a free gauge index in a fixed puncture background**, not a gauge-invariant vacuum expectation value of an isolated odd fermion operator. No such vacuum expectation is asserted to be nonzero.

The zero mode is **one vector-valued section**. Its two displayed components are not two independent zero modes. Similarly, quadratic functions of those components are not automatically a three-state fermion Fock sector.

A conjugate antichiral copy can be used in a nonchiral local theory. This report calculates only the chiral block in the specified background; it does not establish an autonomous anomaly-free chiral theory on all backgrounds or gauge the quaternion symmetry.

### Conventions

Write \(q=e^{2\pi i\tau}\). Theta functions use an argument \(z\) of period one:

\[
\theta[\alpha,\beta](z|\tau)
=\sum_{n\in\mathbb Z}e^{\pi i\tau(n+\alpha)^2+2\pi i(n+\alpha)(z+\beta)}.
\]

The conventional odd theta is chosen with positive derivative at the origin for purely imaginary \(\tau\), so

\[
\theta_1'(0|\tau)=2\pi\eta(\tau)^3.
\]

DLMF uses a period-\(\pi\) argument in many theta formulas; the extra factor of \(\pi\) in our derivative is intentional [D]. Square roots and fractional prime-form powers are locally analytic and are continued with the stated paths. They are not independently reset after every monodromy loop.

---

## 2. The faithful zero mode can be written explicitly

Let

\[
w(z|\tau)=\begin{pmatrix}\theta_3(z|2\tau)\\\theta_2(z|2\tau)\end{pmatrix},
\qquad
s(z|\tau)=\frac{w(z|\tau)}{\sqrt{\theta_1(z|\tau)}}.
\tag{2.1}
\]

The theta transformation laws give constant monodromy matrices equivalent to

\[
A=iZ,\qquad B=-iX,
\qquad
Z=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\quad
X=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

They satisfy

\[
A^2=B^2=-I,\quad AB=-BA,\quad [A,B]=-I.
\tag{2.2}
\]

The exact matrix script uses \(A=-iZ,B=-iX\); this is conjugate to the above convention by the constant matrix \(B\). It does not alter the equivalence class or the scalar-multiplier conclusion. The direct numerical continuation independently recovers \(A=iZ,B=-iX\) on its declared based loops.

Near the puncture,

\[
s(z|\tau)=\frac{z^{-1/2}}{\sqrt{2\pi\eta(\tau)^3}}
\begin{pmatrix}\theta_3(2\tau)\\\theta_2(2\tau)\end{pmatrix}
+O(z^{3/2}).
\tag{2.3}
\]

This is the allowed minimal half-pole. Its norm behaves as \(r^{-1}\); against the area element \(r\,dr\,d\varphi\), it is locally square integrable. This does not on its own select a self-adjoint singular-Dirac domain; the extension was specified separately.

The numerator has no simultaneous zero in the relevant section problem. Together with the known index and stability result, (2.1) supplies the single holomorphic zero mode of the fixed extension, up to a scalar depending on \(\tau\).

### 2.1 A genuine eta-cubed identity—but not the quantum measure

Define the spatial Wronskian

\[
W_z[s]=s_0s_1'-s_1s_0'.
\]

Since the denominator derivatives cancel,

\[
W_z[s]=
\frac{\theta_3(z|2\tau)\theta_2'(z|2\tau)
-\theta_2(z|2\tau)\theta_3'(z|2\tau)}{\theta_1(z|\tau)}.
\]

The numerator has the transformation law of a degree-one theta section, vanishes at the zero of the denominator, and the quotient is elliptic and holomorphic. It is constant in \(z\). Evaluate at \(z=1/2\), using

\[
\theta_2(1/2|2\tau)=0,\quad
\theta_2'(1/2|2\tau)=-2\pi\eta(2\tau)^3,
\]

\[
\theta_3(1/2|2\tau)=\theta_4(2\tau),\quad
\theta_1(1/2|\tau)=\theta_2(\tau),
\]

and the product identities

\[
\theta_4(2\tau)=\frac{\eta(\tau)^2}{\eta(2\tau)},\qquad
\theta_2(\tau)=\frac{2\eta(2\tau)^2}{\eta(\tau)}.
\]

This gives

\[
\boxed{W_z[s]=-\pi\eta(\tau)^3.}
\tag{2.4}
\]

A Wronskian compares two component solutions of a finite-order differential equation. It does not integrate over the nonzero fermion oscillators. Moreover, replacing \(s\) by \(h(\tau)s\) replaces its Wronskian by \(h(\tau)^2W_z[s]\). Equation (2.4) alone cannot fix the quantum normalization.

### 2.2 Exact differential equation

Because the Wronskian is constant and nonzero, both components satisfy an equation without a first-derivative term. The coefficient \(s_a''/s_a\) has no singularities away from the puncture: at a zero of one component, the nonvanishing Wronskian and its derivative force the apparent pole to be removable.

It is elliptic, has leading term \(3/(4z^2)\), and its constant term vanishes. The last statement follows by inserting the even-numerator expansion \(s_a=z^{-1/2}(a+bz^2+\cdots)\). Therefore

\[
\boxed{s_a''(z)=\frac34\wp(z;\tau)s_a(z).}
\tag{2.5}
\]

This is the \(n=1/2\), zero-accessory-parameter Lamé equation. Finite-monodromy half-integer Lamé equations have established literature [L]; no novelty claim is made for this differential-equation class. Here the explicit theta solutions give the exact quaternion realization needed for the selected problem.

---

## 3. Computing the quantum amplitude, including the oscillators

### 3.1 Abelianization is a change of description, not a new physical sector

The matrices \(A,B\) are monomial: \(A\) preserves two eigenlines and \(B\) exchanges them. The representation is induced from a rank-one local system on the index-two subgroup that keeps an eigenline.

Unfolding the two components produces one complex fermion on

\[
\widehat E_\tau=\mathbb C/(\mathbb Z+2\tau\mathbb Z),
\]

with the puncture lifting to two points, \(0\) and \(\tau\). This is an **unramified two-sheeted cover of the punctured base**, not the eight-sheeted cover of Run 2 and not an additional matter field. The compact covering torus is unramified as well; the field has specified twists at the two marked points.

Choosing this polarization does not select a word of the grammar. Its final formulas are explicitly checked under both modular generators, including the transformation exchanging polarizations.

### 3.2 Charged free-field trace

For a bosonized complex fermion, use \(\psi=e^{i\varphi}\), with \(\varphi(z)\varphi(w)\sim-\log(z-w)\). A vertex of charge \(a\) has weight \(a^2/2\), and its OPE with \(\psi\) produces local monodromy \(e^{2\pi ia}\). Fractional-charge twist intertwiners are standard in free-fermion constructions [FT].

The chosen half-pole extension is represented on the cover by charges

\[
+1\text{ at }z,\qquad -\frac12\text{ at }0,\qquad -\frac12\text{ at }\tau.
\tag{3.1}
\]

Their sum is zero, and their total weight is \(1/2+1/8+1/8=3/4\). The charge \(+1\) insertion saturates the single zero mode. The two half-charge insertions produce the central \(-1\) puncture monodromy.

Let \(T=2\tau\), and let

\[
E_T(z)=\frac{\theta_1(z|T)}{\theta_1'(0|T)}
\]

be the coordinate prime form. The oscillator trace and momentum sum with characteristic \([1/4,0]\) give

\[
\mathcal C_0(z|\tau)=
\frac{\theta[1/4,0](z-\tau/2|2\tau)}{\eta(2\tau)}
\frac{E_{2\tau}(-\tau)^{1/4}}
{E_{2\tau}(z)^{1/2}E_{2\tau}(z-\tau)^{1/2}}.
\tag{3.2}
\]

Here the characteristic is part of the induced holonomy data, not selected to match the target triplet. Its translated theta factor and the continued roots give the monodromies checked in §2. Different constant fermion cocycles change only a modulus-independent normalization on the selected branch.

The general genus-one oscillator/prime-form calculation is explained in Mason–Tuite [MT]. Their even-lattice theorem is not being asserted literally to cover arbitrary fractional charges: the oscillator calculation used here is applied to the specific allowed twisted free-fermion intertwiners, as in [FT]. Equivalently, each oscillator pair can be traced directly; the script compares the resulting independent product formula with the theta/prime-form expression.

A useful explicit oscillator product, for \(Q=e^{2\pi iT}\), is

\[
\frac{\theta[a,0](w|T)}{\eta(T)}
=Q^{a^2/2-1/24}e^{2\pi iaw}
\prod_{n\ge1}
(1+e^{2\pi iw}Q^{n-1/2+a})
(1+e^{-2\pi iw}Q^{n-1/2-a}).
\tag{3.3}
\]

The independently evaluated prime-form product is

\[
E_T(w)=\frac{\sin(\pi w)}{\pi}
\prod_{n\ge1}
\frac{(1-e^{2\pi iw}Q^n)(1-e^{-2\pi iw}Q^n)}{(1-Q^n)^2}.
\tag{3.4}
\]

These products make explicit that (3.2) includes nonzero oscillators, unlike (2.1) alone.

### 3.3 Simplification fixes the scalar factor

The following identities reduce (3.2):

\[
\theta[1/4,0](z-\tau/2|2\tau)
=e^{\pi iz/2-\pi i\tau/8}\theta_3(z|2\tau),
\tag{3.5}
\]

\[
\theta_1(z|2\tau)\theta_1(z-\tau|2\tau)
=-i e^{-\pi i\tau/2+\pi iz}
\frac{\eta(2\tau)^2}{\eta(\tau)}\theta_1(z|\tau),
\tag{3.6}
\]

\[
E_{2\tau}(-\tau)
=-i e^{-\pi i\tau/2}
\frac{\eta(\tau)^2}{2\pi\eta(2\tau)^4}.
\tag{3.7}
\]

Equation (3.5) follows by completing the square in the theta series. Equation (3.6) can be proved by comparing zeros and quasi-periodicity, then fixing the constant at the origin using (3.7) and the theta derivative identity. Equation (3.7) follows by a half-period shift and the theta/eta product identities in §2. Thus these are all-domain analytic identities, not conclusions from a finite sample.

On the declared branch,

\[
\mathcal C_0(z|\tau)
=(2\pi)^{3/4}e^{i\pi/8}\eta(\tau)s_0(z|\tau).
\tag{3.8}
\]

Moving the fermion insertion to the second sheet gives the other component, with its fixed fermionic phase. Absorbing the common, modulus-independent constant into the field normalization gives

\[
\boxed{\mathcal A(z|\tau)=\eta(\tau)s(z|\tau).}
\tag{3.9}
\]

The eta factor is the output of the trace, not an ansatz. Equation (3.9) is a puncture-state matrix element/relative chiral block, not an ordinary insertion-free partition function. Removing it is a modulus-dependent redefinition of the amplitude, not a constant normalization.

### 3.4 Independent ground-energy check

For a complex fermion with twist \(\alpha\), the oscillator vacuum energy is \(\alpha^2/2-1/24\). This follows directly from the two Hurwitz sums at \(1/2\pm\alpha\):

\[
E_{\mathbb C}(\alpha)
=-\frac12\left[\zeta(-1,1/2+\alpha)+\zeta(-1,1/2-\alpha)\right].
\]

With the two quaternion eigen-twists \(\pm1/4\), the total is

\[
E_0=-\frac1{48}.
\]

The first component of the geometric profile has leading behavior \(q^{-1/16}\). Multiplication by \(\eta\sim q^{1/24}\) changes this to \(q^{-1/48}\), exactly the oscillator result. This is a separate check on the normalization, not a substitute for the full product calculation.

---

## 4. Puncture residues and the exact representation mismatch

Define the normalized residue vector

\[
U(\tau)=\sqrt{2\pi}\lim_{z\to0}z^{1/2}\mathcal A(z|\tau)
=\frac1{\sqrt{\eta(\tau)}}
\begin{pmatrix}\theta_3(2\tau)\\\theta_2(2\tau)\end{pmatrix}.
\tag{4.1}
\]

It is a vector of puncture matrix elements in one zero-mode problem. Its components must not be read as two zero modes or elementary particle species.

Using classical duplication identities, its quadratic functions are

\[
\boxed{K=(2U_0U_1,U_0^2+U_1^2,U_0^2-U_1^2)
=\frac{(\theta_2^2,\theta_3^2,\theta_4^2)}{\eta}.}
\tag{4.2}
\]

This uses the natural quadratic identification proposed in Run 2. It does not declare that these products are a two-identical-fermion state space or a complete rational-CFT sector set.

### 4.1 Full generator transformations

Let

\[
H=\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad D_T=\operatorname{diag}(1,i).
\]

Theta transformations, with continued fractional roots, give

\[
\mathcal A(z|\tau+1)=e^{-\pi i/24}D_T\mathcal A(z|\tau),
\tag{4.3}
\]

\[
\mathcal A(z/\tau|-1/\tau)
=e^{-\pi i/8}\tau^{3/4}H\mathcal A(z|\tau).
\tag{4.4}
\]

The residue vector has the same coefficient matrices and weight \(1/4\), since extracting \(z^{-1/2}\) removes half a unit of insertion weight. These quarter-weight blocks require their corresponding chosen fractional lift; it is the half-weight quadratic K that is compared with the manuscript's metaplectic triplet.

In the ordered theta-quadratic basis \((2,3,4)\), set

\[
P=\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix},
\qquad
M=\begin{pmatrix}i&0&0\\0&0&1\\0&1&0\end{pmatrix}.
\]

Then

\[
K(\tau+1)=e^{-\pi i/12}MK(\tau),
\qquad
K(-1/\tau)=e^{-\pi i/4}\tau^{1/2}PK(\tau).
\tag{4.5}
\]

The target coefficient matrices, after extracting its weight \(23/2\), are

\[
\rho_\Phi(T)=e^{7\pi i/4}M,
\qquad
\rho_\Phi(S)=e^{\pi i/4}P.
\tag{4.6}
\]

Consequently

\[
\boxed{\rho_K(T)\rho_\Phi(T)^{-1}=e^{\pi i/6}I,
\qquad
\rho_K(S)\rho_\Phi(S)^{-1}=-iI.}
\tag{4.7}
\]

These are the scalar multipliers of \(\eta^2\). With the fixed intertwiner and rotations from Run 2, the complete matrix identities are

\[
\rho_\Phi=\chi_{\eta^3}\otimes O,
\qquad
\rho_K=\chi_{\eta^5}\otimes O.
\tag{4.8}
\]

Both generators are verified, not just an eigenvalue list.

| datum | manuscript target | computed Gaussian quadratic |
|---|---|---|
| modular weight | 23/2 | 1/2 |
| scalar coefficient character relative to \(O\) | \(\chi_{\eta^3}\) | \(\chi_{\eta^5}\) |
| T exponents modulo one | 1/8, 3/8, 7/8 | 5/24, 11/24, 23/24 |
| finite coefficient-matrix image | 96 | 288 |
| scalar subgroup order | 4 | 12 |
| T order | 8 | 24 |
| fourth power of S | \(-I\) | \(-I\) |

A constant change of basis preserves the T eigenvalues, so it cannot fix the difference. Checking only the genuine metaplectic sign would miss the mismatch.

### 4.2 Why the geometric result looked successful

For the unnormalized profile, its corresponding residue quadratics are

\[
K_{\mathrm{geom}}=\frac{(\theta_2^2,\theta_3^2,\theta_4^2)}{\eta^3}.
\]

The exact relations are

\[
\Phi=\eta^{24}K_{\mathrm{geom}}=\Delta K_{\mathrm{geom}},
\quad
K=\eta^2K_{\mathrm{geom}},
\quad
\Phi=\eta^{22}K.
\tag{4.9}
\]

Since the discriminant \(\Delta=\eta^{24}\) has trivial finite multiplier, the geometric residue quadratics have the target finite representation, although their weight differs by twelve. The nonzero-mode quantum factor changes it.

Likewise,

\[
W_z[\mathcal A]=\eta^2W_z[s]=-\pi\eta^5.
\tag{4.10}
\]

This independently reflects the same scalar-character change.

The mismatch is in the exact lifted amplitude representation, not the projective theta directions. Ratios insensitive to a common scalar are unchanged. Neither the theta duplication geometry nor the original cohomology triplet is disproved.

### 4.3 Normalization and determinant-line scope

The comparison is made in the declared oscillator/OPE trivialization and after extracting each object's displayed modular weight. A holomorphic multiplier is not by itself a gauge-independent measurement of a determinant-line connection.

Multiplying by \(\eta^{22}\) reproduces the target function algebraically. Such a modulus-dependent factor changes the amplitude and its automorphy line; it has not been derived from this action. Conversely, we have not proved that no globally defined line-bundle reidentification or additional physical sector could produce it.

No full Quillen norm, local families-index curvature, conical spectral calculation, or mapping-torus eta-invariant is computed here. The mathematical determinant-line framework for parabolic bundles involves these additional geometric structures [B]. This report must not be cited as an all-metrics anomaly theorem or as a four-dimensional gauge-anomaly computation.

---

## 5. The Fibonacci thread is blind to the mismatch

Use \(L=T\) and \(R=ST^{-1}S^{-1}\) for the consistent homology generators. The relative scalar character obeys

\[
r(L)=e^{\pi i/6},\qquad r(R)=e^{-\pi i/6}.
\]

Thus for a positive word \(w\),

\[
\boxed{r(w)=\exp\!\left[\frac{\pi i}{6}(n_L(w)-n_R(w))\right].}
\tag{5.1}
\]

Every balanced word is blind to the phase discrepancy. More generally, the phase is one exactly when \(n_L-n_R\) is divisible by twelve.

| word | relative phase |
|---|---|
| L | \(e^{\pi i/6}\) |
| R | \(e^{-\pi i/6}\) |
| LR | 1 |
| L²R² | 1 |
| L³R | \(e^{\pi i/3}\) |

The homology matrix of \(L^3R\) has trace five, so the discrepancy is detected even within odd-trace positive threads. Testing only \(LR\), or only balanced examples, would mistakenly suggest agreement.

All 510 nonempty positive words of length at most eight were enumerated exactly: 98 are phase-blind and 412 reveal the difference. Equation (5.1), not that finite census, is the proof for arbitrary words.

This is a concrete use of the source's all-threads rule. The computation has not selected a different thread to serve as the physical universe; it uses another permitted word to test a proposed universal identification.

---

## 6. What has been checked about composition

The free-field construction gives an explicit charged genus-one correlator with a declared twist background. It is not merely a modular matrix representation.

The charge sum in (3.1) vanishes. Local OPE exponents satisfy

\[
ab+(a+b)c=bc+a(b+c),
\]

checked exactly for 343 triples of half-integer charges in the finite test set. A direct degeneration also verifies

\[
V_{-1/2}(0)V_{-1/2}(\epsilon)
\sim(-\epsilon)^{1/4}V_{-1}(0)
\]

inside the torus charge trace, with an off-cut complex approach for the fractional power.

These are elementary consistency/degeneration checks of the selected Gaussian construction. The known free-field theory supplies its oscillator algebra. The report does **not** construct a complete Q8-crossed defect category, classify every allowed junction, or verify all-genus nonabelian sewing. It also does not derive interacting spacetime scattering from the Gaussian correlator.

---

## 7. Computations, independent controls and integrity

### Exact script

`verify_exact.py` contains 28 named checks. These include exact quaternion matrices, the monomial abelianization, charge/index arithmetic, cyclotomic monomial-group enumeration, full generator comparisons, the 510-word character test, rational q-series identities through relative order q^16, and the rational Hurwitz/Bernoulli ground-energy calculation.

The q-series check also verifies

\[
uD v-vD u=\tfrac12\eta^6,
\qquad u=\theta_3(2\tau),\quad v=\theta_2(2\tau),\quad D=q\,d/dq.
\]

This is a **modulus** derivative identity, distinct from the spatial Wronskian in §2. Its finite coefficient check is corroboration, not a substitute for an all-domain proof.

### Numerical script

`verify_amplitudes.py` contains 17 named groups and 124 comparisons per precision. It was run at both 80 and 100 decimal digits at five moduli and two ordinary insertion points. The moduli are

\[
i,\quad0.13+1.2i,\quad-0.21+0.93i,\quad0.21+0.73i,\quad0.31+1.43i.
\]

Direct theta series in tau are compared with separately coded fermionic oscillator products and prime-form products. The Lamé equation uses an independently summed elliptic partial-fraction expression for wp. The full amplitude's S and T laws, puncture residue, both Wronskians and the wrong-target negative control are included.

Based quaternion monodromy is checked by following the phase of theta1 continuously along loops, not by resetting a square root or choosing the closest expected matrix. Refinements with 32 and 64 subdivisions agree on the winding. This is a numerical continuation check, not an interval-certified homotopy computation; the analytic monodromy follows from the theta transformations.

Residuals use norm(left-right)/max(1,norm(right)); they are normalized numerical residuals, not certified relative error bounds. At 100 digits, the largest residual among the strict identities, PDE and monodromy checks is approximately **2.675e-100**. At 80 digits it is approximately **3.136e-80**. The finite-distance OPE limit uses a separately stated weaker tolerance and has residuals approximately **2.087e-50** and **2.087e-40**, respectively. It must not be included in a claim that every residual is of order 1e-100.

The deliberately wrong target T multiplier fails by the exact relative norm

\[
2\sin(\pi/12)\simeq0.517638090205041525,
\]

at every tested modulus. Numerical precision does not shrink that failure.

### Independence and limits

There are **45 named groups in total**, not 45 independent quantum theories or independent researchers. The analytic charge trace and product implementation use the same specified free theory. The oscillator-product evaluation, independent wp sum, exact Casimir calculation and finite matrix enumeration test different parts of the derivation. None is an infinite-dimensional numerical Dirac eigensolver.

The local plan was written and hashed after exploratory reasoning and initial numerical inspection, before the formal scripts. It is not blind or externally timestamped. `CHANGELOG.md` records a symbolic-simplification correction and a fractional-power branch-cut correction. Final logs were regenerated; earlier failing console logs were not retained. The exploratory file uses floating-point inputs and is excluded from high-precision evidence.

No source manuscript or project repository was edited, and no code was imported from the project's calculation modules.

---

## 8. Claim grades and next logical question

| claim | grade |
|---|---|
| Explicit faithful zero-mode profile and its half-pole | **PROVED for the specified extension** |
| Spatial Wronskian and n=1/2 Lamé equation | **ANALYTIC IDENTITIES; independently checked** |
| Oscillator-normalized amplitude A=eta s | **DERIVED in the fixed Gaussian model** |
| Natural quadratic residue multiplier is chi_eta5, not chi_eta3 | **EXACT MISMATCH in the stated trivialization/identification** |
| Fibonacci LR hides the relative scalar but L³R detects it | **PROVED by the scalar character; finite census checked** |
| General no-go for every quantum realization | **NOT CLAIMED** |
| Full Quillen connection and nonabelian all-genus sewing | **NOT CALCULATED** |
| Gauge-chiral matter, gravity, measured constants | **NOT DERIVED** |

This run resolves the proposed first Gaussian test negatively at the exact representation-identification stage, while constructing nonzero faithful amplitudes explicitly. It does not justify treating the geometric Wronskian as the quantum measure.

The next justified question is whether a **specified mechanism already warranted by the weave** changes the determinant contribution or the relevant observable. At the present quadratic level a compensating coefficient character would be chi_eta^(-2). Appending that character or adding fields solely because their determinants cancel the mismatch is not a derivation. Any interacting, constrained, supersymmetric or additional-sector model must first be motivated independently, define its puncture data, and calculate its total amplitude anew.

There is also a logically conservative option: retain the original triplet as geometric coupling data without insisting that it is this particular chiral quantum amplitude. This calculation shows that those roles are different; it does not decide the correct physical dictionary.

---

## Primary references and their role

**[MT]** G. Mason and M. P. Tuite, *Torus Chiral n-Point Functions for Free Boson and Lattice Vertex Operator Algebras*, Commun. Math. Phys. 235 (2003) 47–68, arXiv:math/0204323. Propositions 3.10/3.13 and Theorem 3.14 give oscillator/prime-form and lattice-trace machinery. Fractional-charge twist specialization is derived here using the free-field oscillator construction, not claimed verbatim from its even-lattice theorem. https://arxiv.org/abs/math/0204323

**[FT]** T. Takayanagi and T. Tsuda, *Free Fermion Cyclic/Symmetric Orbifold CFTs and Entanglement Entropy*, arXiv:2209.00206. Sections 3 and 4 give fermionic twists, fractional-charge bosonization, and torus correlator methods. The paper is not being cited as a Q8-specific completion. https://arxiv.org/abs/2209.00206

**[FR]** I. Florakis and J. Rizos, *Free Fermionic Constructions of Heterotic Strings*, arXiv:2407.07034. Background for free fermion central charges, OPEs, spin/twist fields and theta-function traces. No string completion is imported into this calculation. https://arxiv.org/abs/2407.07034

**[D]** NIST DLMF, Chapter 20, especially §§20.4, 20.5 and 20.7: theta derivative, product, shift, duplication and modular identities. Account for its period-pi argument convention when comparing derivatives. https://dlmf.nist.gov/20.4 ; https://dlmf.nist.gov/20.5 ; https://dlmf.nist.gov/20.7

**[L]** Y.-C. Chou, C.-L. Wang and P.-S. Wu, *Characterization and enumeration on Lamé equations with finite monodromy*, arXiv:2402.16286. Prior-art context for finite-monodromy half-integer Lamé equations. The explicit n=1/2 solution in this report is verified directly. https://arxiv.org/abs/2402.16286

**[B]** I. Biswas, *Determinant line bundle on moduli space of parabolic bundles*, arXiv:1012.4551. Distinguishes geometric Hermitian/Quillen determinant-line structures from a holomorphic formula in a chosen trivialization. It does not supply the unperformed Quillen calculation for this run. https://arxiv.org/abs/1012.4551

The known theta functions, free-field machinery, cover methods and Lamé class are not asserted to be novel. The contribution of this run is the explicit fixed-model calculation and scoped comparison with the user's target, including the negative phase test.
