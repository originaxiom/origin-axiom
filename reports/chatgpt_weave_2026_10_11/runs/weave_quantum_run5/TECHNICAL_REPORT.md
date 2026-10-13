# Quantum realization of the weave — Run 5
## A continuous symmetry-preserving family, and rigidity of the exact chiral puncture prescription

**Date:** 10 October 2026.  
**Source basis:** *A Weave of Two Records*, especially §§2–4 and §7; supplied Run 3 and Run 4 technical reports.  
**Scope:** One explicitly specified two-dimensional spin-CFT family. New calculations distinguish a symmetry defect from a particular holomorphic field/domain realization. No Standard Model data, original-file edits, four-dimensional chirality claim, or gravitational completion.

## Executive result

The deformation proposed in Run 4 can be implemented while retaining the **fermionic spin sectors and the original charge-lattice gluing**, not just the bosonic current-algebra control.

Two different tests then have different answers:

1. The quaternion action, its normalizer action on the flavour currents, and the topological sign monodromy of the puncture survive the deformation. Invariant symmetry lines are not removed by the invariant current-current perturbation. This does not preserve a particular endpoint's conformal weights.
2. The precise **holomorphic fermion and equal-sign minimal half-pole realization** used in Run 3 survives only at the undeformed point. The tracked fermion acquires antiholomorphic weight `sinh(t)^2/4`. An all-charge-lattice argument excludes any replacement local NS fermion of weights `(1/2,0)` at a different finite value of t within this family.

The condition therefore **isolates the free point in this one family**, conditional on keeping that strict chiral dictionary. It is not a dynamical stabilization mechanism, an argument that the original grammar forces that dictionary, or uniqueness among every possible quantum theory.

An independent global check uses all four bulk spin-sector torus traces. Their modular covariance persists for every deformation. The periodic-periodic graded trace, zero at the free point, becomes strictly positive at every nonzero real t in the explicitly fixed parity convention. Its leading term is

\[
 Z_{\mathrm{PP}}(\tau;t)
 =8\pi^2(\operatorname{Im}\tau)^2|\eta(\tau)|^8t^2+O(t^4).
\]

These are **bulk spin-sector traces**, not the noncommuting-Q8 punctured partition function. Their role is to verify the spin completion and distinguish theories spectrally.

---

## 1. Inherited question and additional choices

Run 4 reconstructed two commuting current algebras in four real chiral fermions:

\[
\mathfrak{so}(4)_1\cong
\mathfrak{su}(2)_{1,A}\oplus\mathfrak{su}(2)_{1,B}.
\]

The three A currents carry the three quaternion parity characters. The B currents are quaternion singlets. Run 4 proposed the bulk deformation

\[
\delta S=g\int I_3(z)\overline I_3(\bar z)\,d^2z
\]

and explicitly did **not** assert that the full E-plus puncture or fermionic completion survived it.

For this run choose the vectorlike nonchiral spin completion of the original two complex fermions: two complex left-moving fermions and their right-moving partners, with a common spin structure. This is a stated model choice, not a deduction from the source PDF. The currents act on flavour; `I_3` is proportional to the total fermion-number current.

At the reference point bosonize

\[
\psi_1=e^{iH_1},\qquad\psi_2=e^{iH_2},
\]

with canonically normalized bosons. Define

\[
H_A=(H_1-H_2)/\sqrt2,\qquad
H_B=(H_1+H_2)/\sqrt2.
\]

The current deformation changes the B sector and leaves A unchanged. Abelian current-current deformations and their charge-lattice description are established machinery [FR]. Spin structures must be retained: a compact boson partition function alone does not specify a fermionic theory [FNS].

### Coordinates on the deformation

Use a real parameter t for which t=0 is the original free point, and set c=cosh(t), s=sinh(t). We do not identify t with the bare coupling g without a convention-dependent bosonization relation. In a standard circle-momentum convention the boost below corresponds to changing the charge radius by an exponential factor. It is **not** the elliptic modulus tau or a derived spacetime radius.

---

## 2. Exact spin-preserving family

For original left and right charge vectors `(q_L1,q_L2;q_R1,q_R2)`, put

\[
 a_L=(q_{L1}-q_{L2})/\sqrt2,\quad b_L=(q_{L1}+q_{L2})/\sqrt2,
\]

and likewise for the right movers. The finite deformation is

\[
\begin{pmatrix} b_L(t)\\b_R(t)\end{pmatrix}
=\begin{pmatrix}c&s\\s&c\end{pmatrix}
\begin{pmatrix}b_L\\b_R\end{pmatrix},
\qquad a_L(t)=a_L,\quad a_R(t)=a_R.
\]

The conformal weights of a primary are

\[
 h_t=\frac12\{a_L^2+(cb_L+sb_R)^2\},\qquad
 \bar h_t=\frac12\{a_R^2+(sb_L+cb_R)^2\}.
\tag{2.1}
\]

Bosonic oscillator levels add nonnegative integers to these weights. The central charges remain `(2,2)`.

The charge map preserves

\[
 B(q,q')=q_L\cdot q_L'-q_R\cdot q_R',
\tag{2.2}
\]

and hence conformal spin, exchange statistics, and monodromy pairings. This is the O(1,1) current-current deformation mechanism [FR]; it is checked directly here.

### Keeping the fermionic gluing

For local NS fields the starting charge lattice is the odd integral unimodular lattice

\[
(q_L;q_R)\in\mathbb Z^2\oplus\mathbb Z^2.
\]

The fermion parity is

\[
(-1)^F=(-1)^{q_{L1}+q_{L2}+q_{R1}+q_{R2}},
\]

and `2(h-bar h)` has the same parity. In A/B coordinates, writing `d=q_1-q_2` and `u=q_1+q_2`, one must retain `d=u (mod 2)`. Thus A and B are **not** replaced by two unrelated charge lattices.

For a common spatial Ramond boundary condition all four original charges shift by 1/2. Both spatial choices and both temporal parity insertions are kept below. The boost changes the positive-energy splitting, not the lattice labels, cocycles, or parity assignment. Positivity of the weights is manifest in (2.1), for every finite real t.

---

## 3. What happens to the specified puncture

The local bosonized puncture component used to reproduce the equal half-poles of Run 3 has charges

\[
\mathcal P_-:\quad(q_L;q_R)=(-1/2,-1/2;0,0).
\tag{3.1}
\]

The equal-sign choice is important. It is the charge-sector spinor, not the other Ramond polarization.

**Scope of (3.1):** It follows a chiral defect component. Away from the reference point it is not being asserted to be a local scalar in the untwisted bulk spin theory. Full local nonchiral endpoint pairings are given below.

For the two original fermions, (2.1) gives

\[
 \boxed{(h_\psi,\bar h_\psi)
 =\left(\frac12+\frac{s^2}{4},\frac{s^2}{4}\right).}
\tag{3.2}
\]

For the tracked puncture component,

\[
 \boxed{(h_{\mathcal P},\bar h_{\mathcal P})
 =\left(\frac14+\frac{s^2}{4},\frac{s^2}{4}\right).}
\tag{3.3}
\]

The conformal spins remain 1/2 and 1/4. Their new antiholomorphic weights are positive whenever t is nonzero. This is two-dimensional left/right conformal structure, **not** Standard Model gauge chirality.

### Exact local operator product

The fused field `psi_i P_-` is a flavour spinor, with `(h,bar h)=(1/4,0)` at every t. Charge contractions give

\[
\boxed{
 \psi_i(z,\bar z)\mathcal P_-(0)
 \sim z^{-c^2/2}\bar z^{-s^2/2}\mathcal S_i(0)
 =z^{-1/2}|z|^{-s^2}\mathcal S_i(0).
}
\tag{3.4}
\]

A full loop still produces `exp[2 pi i (-c^2/2+s^2/2)]=-1`. Thus the central puncture monodromy survives exactly.

But the original **holomorphic** half-pole is recovered only if `s=0`, hence only at `t=0` for real t. The extra radial factor is not a tau-only normalization: it changes a local scaling exponent. A constant basis change or an eta prefactor cannot remove it.

The first deviation is quadratic in t. A first-order test of the chiral component alone would therefore miss the failure.

### Full nonchiral endpoint controls

Pair the original chiral puncture with its conjugate right component:

\[
\mathcal P_{\rm conj}:\quad(-1/2,-1/2;+1/2,+1/2).
\]

Its weights are

\[
(h,\bar h)=(e^{-2t}/4,e^{-2t}/4).
\tag{3.5}
\]

A same-sign pairing has `(h,bar h)=(e^{2t}/4,e^{2t}/4)`. Both are legitimate tracked scalar disorder/end-point choices in the nonchiral construction; neither becomes the original unchanged chiral state at nonzero t. The fermion's mutual monodromy with the conjugately paired endpoint is still -1 because (2.2) is unchanged.

This avoids treating a purely left Ramond/right NS label as an ordinary local bulk scalar.

### A different spinor is not the same boundary condition

The opposite-sign component

\[
\mathcal P_A:\quad(-1/2,+1/2;0,0)
\]

has B charge zero, so remains chiral with h=1/4 for every t. At the reference point it gives opposite local exponents, -1/2 for one original fermion and +1/2 for the other. It is not the equal-sign half-pole prescription (3.1).

This is another reason bare sign monodromy cannot specify the complete puncture state: distinct polarizations can share a -1 branch while having different local exponents and quantum numbers. This alternative is a control, not a silent replacement of E-plus.

### The geometric index has not changed

The abstract parabolic bundle E-plus in Run 2 still has its geometric Dolbeault kernel/cokernel counts. The deformation does not change those mathematical bundle invariants. What changes is whether the interacting physical field or correlator is governed by that free holomorphic Dirac equation. The present result must not be described as changing the geometric index.

---

## 4. All-radius rigidity: there is no replacement local h=1/2 fermion

Checking only the original field could miss a different local field that becomes holomorphic elsewhere, for example at a rational radius. The full NS charge lattice excludes that possibility in this one-parameter family.

Suppose a local NS state has `(h,bar h)=(1/2,0)`. Nonnegative oscillator energies imply zero oscillator levels. The right flavour charge must vanish, so write

\[
(q_{R1},q_{R2})=(m,m),\qquad m\in\mathbb Z.
\]

Write left sum and difference as

\[
 u=q_{L1}+q_{L2},\qquad d=q_{L1}-q_{L2},\qquad u=d\pmod2.
\]

The invariant spin equation gives

\[
 d^2+u^2-4m^2=2.
\tag{4.1}
\]

Since the nonnegative left flavour contribution is `d^2/4`, h=1/2 requires `d=0,+1,-1`.

If d=0, u is even, and (4.1) is impossible modulo four. If d=+1 or -1, then

\[
 (u-2m)(u+2m)=1.
\tag{4.2}
\]

The only integer possibilities are `u=+1 or -1, m=0`. The remaining right-moving B charge is then `u sinh(t)/sqrt(2)`, which vanishes only at t=0.

Therefore

\[
\boxed{
\text{A local NS holomorphic field of weight }1/2
\text{ exists in this family only at }t=0.
}
\tag{4.3}
\]

At t=0 the four solutions are exactly the two complex fermions and their conjugates. The code independently scans the reduced equation over a bounded integer range as a check; (4.1)–(4.2), not that scan, is the proof for all charges and all finite real t.

**Scope:** This excludes replacement local NS fermions in the stated lattice family. It does not classify all different theories, allow a new orbifold/extension chosen at a rational point, or count arbitrary disorder sectors as local fermions.

---

## 5. Quaternion symmetry and the status of sewing

In the original complex flavour basis use

\[
 A=i\,\mathrm{diag}(1,-1),\qquad
 B=-i\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

They satisfy `A^2=B^2=-I`, `AB=-BA`, and `[A,B]=-I`.

The total-number current is invariant under every unitary flavour matrix, including all eight quaternion elements and both prescribed normalizer lifts. The deformation `I_3 Ibar_3` is therefore invariant. The A currents have B charge zero and their entire su(2)_1 operator algebra is unchanged.

For the vectorlike completion one can retain fixed Q8 transition functions and symmetry cuts: the invariant interaction is well-defined on both sides of a cut and is unchanged as the cut passes a bulk perturbing insertion. In the operator description `D_q O = O D_q` for the perturbation O. This is the standard symmetry-defect preservation mechanism; general discussions of defects commuting with perturbations are given in [CLSWY] and [K].

Thus the **symmetry lines and their group composition are not a mechanism fixing t**. The same normalizer reasoning applies to every word in L and R; no preferred mapping torus is selected. Endpoint states can and do acquire changed conformal data, as §3 computes.

### What is not established about the complete puncture

The exact charge-lattice construction gives a consistent spin-CFT family and transports the charged local/disorder labels described above. It does not evaluate every nonabelian Q8-twisted torus correlator, determine every junction amplitude, or calculate the singular-operator determinant connection. Fermionic defect junctions require their appropriate spin data [CCX]; ordinary bosonic group multiplication alone is not their complete classification.

Accordingly, no claim is made that **all original weave data** survive the deformation. In fact, the strict holomorphic E-plus field realization fails a necessary local condition at every nonzero t. One need not compute all global junctions to establish that failure. Conversely, having a consistent Q8 symmetry defect is weaker than preserving that particular holomorphic realization.

---

## 6. All four bulk spin traces

This is an independent global check that the deformation has not inadvertently replaced the fermionic model by an unrelated bosonic current algebra.

Let a,b be 0 or 1/2. Shift all four original charges by a and insert the temporal parity sign:

\[
\begin{split}
Z_{a,b}(\tau;t)=\frac1{|\eta(\tau)|^4}
\sum_{n_1,n_2,m_1,m_2\in\mathbb Z}
&(-1)^{2b(n_1+n_2+m_1+m_2)}\\
&\times e^{\pi i\tau p_L(t)^2-\pi i\bar\tau p_R(t)^2}.
\end{split}
\tag{6.1}
\]

Here `q_L=(n_1+a,n_2+a)`, `q_R=(m_1+a,m_2+a)` and the p's are the deformed A/B momenta. The parity convention is fixed by (6.1); we do not multiply the odd-spin answer by an extra Arf phase.

At t=0,

\[
\begin{array}{c|c}
(a,b)&Z_{a,b}(\tau;0)\\\hline
(0,0)&|\theta_3/\eta|^4\\
(0,1/2)&|\theta_4/\eta|^4\\
(1/2,0)&|\theta_2/\eta|^4\\
(1/2,1/2)&0.
\end{array}
\tag{6.2}
\]

Poisson resummation of the selfdual odd lattice, with its characteristics retained, gives

\[
 Z_{a,b}(-1/\tau;t)=Z_{b,-a}(\tau;t),
\]

\[
 Z_{a,b}(\tau+1;t)=Z_{a,b+a-1/2}(\tau;t).
\tag{6.3}
\]

For the T equation one can also see the sign directly: with a=0 the integer squared charges produce the temporal parity insertion; with a=1/2, `n(n+1)` is even. For S, preservation of the lattice's bilinear form and covolume under the O(1,1) transformation leaves the characteristic Fourier transform unchanged. The determinant of the Gaussian kernel is independent of t. The general charge-deformation/modular mechanism is described in [FR], while the spin-sensitive fermionic dictionary is emphasized in [FNS].

All four traces were computed at generic complex tau. Both S and T were checked, not just invariance on the imaginary axis. A second implementation sums the original four integer flavour charges, independently of the faster parity regrouping used for high precision.

**Important:** These are unpunctured bulk spin traces. They are not presented as the full Q8-twisted punctured partition functions.

### 6.1 Exact positivity of the formerly zero odd-spin trace

Write `tau=x+iy`,

\[
 f_0=\theta_3(2\tau),\qquad f_1=\theta_2(2\tau),
\qquad \kappa=\pi y\sinh(2t),
\]

and define, for each integer u,

\[
 A_u=(-1)^u f_{1-(u\bmod2)}
 \exp\left(\frac{\pi i x u^2}{2}-\frac{\pi y\cosh(2t)u^2}{2}\right).
\]

The exact parity-regrouped formula is

\[
 Z_{\mathrm{PP}}=\frac1{|\eta|^4}
 \sum_{u,v\in\mathbb Z}A_u\overline A_v e^{-\kappa uv}.
\tag{6.4}
\]

Since `A_{-u}=A_u`, all odd moments vanish. Expanding the exponential gives a nonnegative sum:

\[
\boxed{
 Z_{\mathrm{PP}}=
 \frac1{|\eta|^4}\sum_{k=0}^{\infty}
 \frac{\kappa^{2k}}{(2k)!}
 \left|\sum_{u\in\mathbb Z}A_u u^{2k}\right|^2.
}
\tag{6.5}
\]

The interchange is justified by absolute convergence: `cosh(2t)>|sinh(2t)|` for every finite real t gives Gaussian domination after taking absolute values.

At t=0 only k=0 contributes, and its moment is `f_1 f_0-f_0 f_1=0`.

For t nonzero, kappa is nonzero. If every nonnegative term in (6.5) vanished, all moments of the entire function `F(z)=sum_u A_u exp(uz)` would vanish. Its odd moments already vanish by evenness. It would follow that F is identically zero and hence all its Fourier coefficients vanish. This contradicts `A_0=f_1`, which is nonzero on the upper half-plane. Thus

\[
\boxed{Z_{\mathrm{PP}}(\tau;t)>0\quad
(t\in\mathbb R\setminus\{0\},\ \tau\in\mathbb H)}
\tag{6.6}
\]

in the fixed parity convention of (6.1). Changing an overall odd-spin topological sign changes the sign convention but not the fact that the trace is nonzero.

### 6.2 Leading term

At t=0 the second moment in (6.5) is

\[
 M_2(0)=-2\eta(\tau)^6.
\]

One derivation rewrites it as two independent half-integer charge sums. The zeroth odd theta sum vanishes, while

\[
\sum_n(-1)^n(n+1/2)e^{\pi i\tau(n+1/2)^2}=\eta(\tau)^3
\]

by `theta_1'(0)=2 pi eta^3` in the period-one convention [D]. Only the cross term in the squared total charge remains. This gives the stated factor -2. Also `M_0(t)=O(t^2)` and `kappa=2 pi y t+O(t^3)`. Therefore

\[
\boxed{
Z_{\mathrm{PP}}(\tau;t)=8\pi^2y^2|\eta(\tau)|^8t^2+O(t^4).
}
\tag{6.7}
\]

An independent differentiation of the four-charge Gaussian kernel gives

\[
\partial_t^2 Z_{\mathrm{PP}}\big|_{0}=16\pi^2y^2|\eta|^8,
\]

in agreement. The answer is even in t by right-charge conjugation, with the two-flavour parity gluing retained.

This graded trace is not a supersymmetric protected index. Its lifting does not contradict the geometric E-plus index. It shows that the free three-nonzero-spin-function pattern is additional spectral information, not a general consequence of quaternion symmetry or conformal consistency.

---

## 7. What has and has not been selected

Within the explicitly defined spin-CFT family:

| Requirement | Consequence |
|---|---|
| Q8 action and quaternion current triplet | Every finite t survives |
| Invariant symmetry lines and central -1 puncture monodromy | Do not select t |
| Common-spin local charge lattice and modular covariance | Every finite t survives |
| Exact original holomorphic fermion of weights (1/2,0) | t=0 only |
| Exact tracked equal-sign holomorphic half-pole realization | t=0 only |
| Vanishing bulk periodic-periodic graded trace in this family | t=0 only |
| Exact manuscript metaplectic block, gauge-chiral matter or gravity | Not obtained |

This is **conditional rigidity**, not a potential or RG attraction. The current-current deformation is exactly marginal, so its beta function vanishes along the family. The calculation does not make t a dynamical variable or derive a force driving it to zero.

The source PDF's holomorphic cohomology is a mathematical object. Its identification with physical left-handed matter is part of the stated link Lambda, and the extra cusp unit is separately postulated. Nothing in this run proves that mathematical holomorphy must require fundamental physical fermions to remain a free two-dimensional chiral system.

Likewise, t is an interaction coordinate of this test model. It does not fix the source's tau, its coupling coefficients, a Standard Model constant, or a spacetime vacuum.

The free point is the **same model** tested in Run 3. Isolating it does not repair Run 3's exact coefficient mismatch or Run 4's distinction between products of amplitudes and genuine composite operators.

### A useful conditional local-algebra observation

If one separately insists on four real, mutually local, normalized holomorphic fields of weight 1/2 in a unitary CFT with a unique vacuum, their singular OPE is the free-fermion Clifford OPE. Their canonical stress tensor has c=2. If the total chiral central charge is also two and the standard conformal inclusion holds, the commuting coset stress tensor has c=0 and zero norm; unitarity removes it. There is then no additional propagating chiral sector left in that half of this minimal model.

This observation does not classify global spin pairings or topological sectors. It explains why requiring the entire minimal free holomorphic fermion structure is not, by itself, a mechanism for deriving a new interacting spacetime theory.

---

## 8. Verification and integrity

Scripts:

```
python verify_exact.py
python verify_lattice.py --dps 50
python verify_lattice.py --dps 80
```

The exact script has **40 named checks**, covering the Lorentz charge map, weights, both endpoint pairings, puncture OPE exponents, quaternion/normalizer invariance, spin-statistics gluing, the all-radius proof's arithmetic, and the odd-spin second variation.

Each numerical run has **99 checks**:

- 72 strict numerical identities (free theta limits, modular covariance, reality, reversal, and exact moment identities);
- 12 cutoff-refinement comparisons;
- 8 independent original-four-dimensional-lattice checks at ordinary double precision;
- 3 positive odd-spin evaluations;
- 3 finite-small-deformation comparisons;
- 1 finite positive-moment-series comparison.

At 80 decimal digits the maximum strict normalized residual was `4.17722981616e-80`. The independent double-precision control had maximum residual `1.62442295041e-15`; it is not counted as 80-digit evidence. The finite-small-t comparisons had maximum residual `1.16666666667e-22`. The truncated positive moment series differed by `2.75891675446e-30` at its declared sample. Extra charge cutoffs of three produced no change at the working precisions. None of these statements is an interval-certified truncation bound.

The numerical cutoffs were at most 24 for the parity-sum coordinate in the strict 80-digit sample set. The analytic results are proved in the report, not inferred from finite matrices or sampled moduli.

### Correction retained

The first numerical script mistakenly transcribed the second-moment control as `M_2=-4 eta^6`; it failed. The analytic derivation gives `-2 eta^6`, consistent with the already planned leading coefficient `8 pi^2 y^2 |eta|^8`. The assertion was corrected and both precision runs completed from the beginning. The initial script and failure log are retained. The plan is locally hashed after exploratory reasoning and before the formal scripts, not blind or independently timestamped.

No user repository, source PDF, or previous report was edited. Prior reports were read for definitions; their verification code was not imported. This is not a numerical singular-Dirac eigensolver, a full Quillen connection calculation, or a verification of every Q8 defect junction.

---

## 9. Claim grades and next logical step

| Claim | Grade |
|---|---|
| Spin-preserving O(1,1) family with original charge gluing | CONSTRUCTED using established CFT machinery; exact lattice checks |
| Transported original puncture and fermion weights/OPE | DERIVED EXACTLY in that family |
| No replacement local NS (1/2,0) field away from t=0 | PROVED for the full charge lattice of this family |
| Original equal-sign holomorphic prescription excludes every nonzero t | PROVED as a necessary local condition |
| Bulk odd-spin trace is nonzero for every nonzero t | PROVED from the positive moment series, in the stated parity convention |
| Entire original Q8 puncture/cohomology/metaplectic package selected uniquely | NOT CLAIMED |
| Complete nonabelian junction amplitudes or singular determinant connection | NOT CALCULATED |
| Gauge-chiral Standard Model, spacetime dynamics, gravity | NOT DERIVED |

The next worthwhile construction is an **explicit operator/defect realization of the original cohomology triplet**, with its exact L,R action and connection, that does not assume in advance that the fundamental fields remain free holomorphic fermions. This run tells us why that distinction matters: topology permits an interacting family, whereas retaining the particular free holomorphic dictionary selects the reference point by an additional spectral requirement. The missing question is whether the original weave intrinsically imposes that requirement or instead controls a protected operator sector of an interacting theory.

## Primary references and their limited roles

[FR] S. Förste and D. Roggenkamp, *Current-Current Deformations of Conformal Field Theories, and WZW Models*, JHEP 05 (2003) 071, arXiv:hep-th/0304234, §2 and Appendix A. Charge-lattice O(d,d) deformation, locality, modular behavior and preserved neutral structure. https://arxiv.org/abs/hep-th/0304234

[FNS] H. Fujimura, T. Nishioka and S. Shimamori, *Entanglement Rényi entropy and boson-fermion duality in massless Thirring model*, Phys. Rev. D 108 (2023) 125016, arXiv:2309.11889, §II. The need to retain spin structures in a bosonized interacting fermion model. The paper's one-flavour radius formula is not substituted for our two-flavour charge normalization. https://arxiv.org/abs/2309.11889

[CLSWY] C.-M. Chang, Y.-H. Lin, S.-H. Shao, Y. Wang and X. Yin, *Topological Defect Lines and Renormalization Group Flows in Two Dimensions*, JHEP 01 (2019) 026, arXiv:1802.04445. Symmetry/defect composition and the distinction between defects and attached operators. https://arxiv.org/abs/1802.04445

[K] A. Konechny, *Open topological defects and boundary RG flows*, arXiv:1911.06041, Introduction. Defects commuting with perturbations; not a Q8-specific all-genus calculation. https://arxiv.org/abs/1911.06041

[CCX] C.-M. Chang, J. Chen and F. Xu, *Topological Defect Lines in Two Dimensional Fermionic CFTs*, arXiv:2208.02757. Fermionic endpoint and junction structures require more than ordinary bosonic group multiplication. https://arxiv.org/abs/2208.02757

[D] NIST DLMF §20.4 and §20.7. Odd theta derivative, products and modular formulas; account for the period-one versus period-pi argument convention. https://dlmf.nist.gov/20.4

[M] Y. Moriwaki, *Two-dimensional conformal field theory, full vertex algebra and current-current deformation*, Adv. Math. (2023), arXiv:2007.07327. Nonperturbative current-current deformation framework, not a classification of this fermionic puncture. https://arxiv.org/abs/2007.07327

No novelty claim is made for bosonization, Luttinger/current-current deformation, or enhanced chiral symmetry at the free point. The contribution of this report is the explicit conditional test of the supplied weave construction, the all-charge exclusion of replacement local weight-half fermions, and the spin-trace calculation with its stated scope.
