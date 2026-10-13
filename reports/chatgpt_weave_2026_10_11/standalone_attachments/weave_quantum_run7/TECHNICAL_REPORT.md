# Quantum realization of the weave — Run 7
## A genuine quantum center-puncture line, and the cost of changing the physical model

**Date:** 10 October 2026.  
**Source:** *A Weave of Two Records*, especially §§2–4 and §7, and the supplied Run 6 report.  
**Scope:** A new, explicitly declared SU(2) Chern–Simons/WZW candidate, compared with the source's cohomology line and with the previous level-one protected theory. No measured particle data, repository edits, Standard Model spectrum, or gravitational completion.

## Executive conclusion

A known, unitary quantum gauge theory has a nonzero central-puncture amplitude whose coefficient multiplier is **exactly** the geometric line found in Run 6:

\[
\ell(T)=e^{\pi i/4},\qquad \ell(S)=e^{-3\pi i/4}.
\]

The candidate is **SU(2) Chern–Simons theory at level two**, with the nontrivial invertible central line as its puncture label. Its boundary SU(2)\(_2\) WZW description permits an independent Clifford/oscillator computation. A weight-3/2 inserted block is

\[
\boxed{\mathcal B(\tau)=\eta(\tau)^3,}
\]

up to a constant normalization. Here eta cubed is calculated from a Ramond trace, including the nonzero oscillators. It is not multiplied into an old amplitude to repair it.

This is **not** the same physical theory as the level-one protected sector in Runs 4–6. Choosing Chern–Simons quantization, its level, its quantum puncture label, and a framing are additional physical choices. The construction realizes the missing **line**, not the full original three-dimensional matter interpretation or the complete weight-23/2 function.

The state count is decisive: the gauge-invariant torus Hilbert space with the specified puncture has dimension **one**, not three. The three-state unpunctured torus Hilbert space has a different modular representation from the manuscript's triplet. Retaining three framed current-polarization indices is not the same as deriving three gauge-invariant matter generations.

Within the specified SU(2)\(_k\) family, a nonzero central-puncture block requires even k. Matching the source's Dehn-twist phase requires k=2 mod 16. Requiring, in addition, that its unique handle ground multiplet be **one copy of the original quaternion doublet** selects k=2. That last identification is an explicit conditional physical dictionary, not a theorem that the grammar uniquely selects Chern–Simons theory.

---

## 1. What is inherited and what changes

Run 6 reconstructed the geometric factorization

\[
T\cong\ell\otimes O,
\]

where O is the three-dimensional rotation representation of the quaternion normalizer. It also proved that the old local protected currents realize O, not the extra scalar line, and that ordinary level-one spinor punctures do not give the missing torus block. The physical realization of ell remained open.

This run does **not** rename those level-one currents as level-two currents. It tests another standard way of turning the rank-two holonomy geometry into quantum physics: quantizing a gauge field whose classical constraint is flatness. Witten's Chern–Simons/WZW correspondence [W] supplies this framework. It is a model choice, not a deduction from the philosophical principle.

The added data are:

1. Compact gauge group SU(2), exploiting the already specified unitary quaternion representation. This SU(2) is **not** identified with the Standard Model weak gauge group.
2. Positive-integer Chern–Simons level k, with the orientation chosen to match the source's chiral sign.
3. A puncture carrying the maximal integrable label J=k, the invertible line implementing the center action on Wilson lines.
4. The standard conformal-block framing convention, with Dehn-twist phases exp[2 pi i(h-c/24)]. Independent framing changes are not silently absorbed into the answer.

The old glued rank-two spin-CFT, its E-plus singular Dirac domain, and its interacting parameter are not transported unchanged into this candidate. No full Q8-crossed defect calculation for that old theory is claimed.

## 2. A physical action and the original quaternion point

With the invariant trace normalized in the usual fundamental SU(2) convention, the action is

\[
S_k[A]=\frac{k}{4\pi}\int_{M_3}
\operatorname{tr}\!\left(A\wedge dA+\frac23 A\wedge A\wedge A\right).
\]

A convention-dependent overall sign is fixed by choosing positive-level chiral SU(2)\(_k\). Large gauge invariance requires integer k. Its local equation away from inserted Wilson lines is F\(_A\)=0. Quantization on a surface therefore uses the moduli of flat connections and gives a finite-dimensional quantum Hilbert space. These are established properties of this action [W, M].

On a once-punctured torus, prescribe the classical central holonomy

\[
ABA^{-1}B^{-1}=-I.
\]

It follows that AB=-BA. Conjugating shows tr A=tr B=0; SU(2) Cayley–Hamilton then gives A²=B²=-I. In unit-quaternion coordinates A and B are perpendicular unit imaginary quaternions. Simultaneous SU(2) conjugation therefore brings them to i and j. Thus the compact central-holonomy locus consists of the quaternion point up to gauge, with central stabilizer.

This is the same compact central commutator data as the source. It is not a proof that the source requires this gauge action, nor that the full SL(2,C) character variety is compact SU(2) phase space.

### The finite-level puncture dictionary must be quantum, not a classical substitution

At finite k, Wilson observables and allowed labels are quantum-deformed. One must not equate every finite-level Wilson eigenvalue with an unshifted classical conjugacy-class angle. We specify the quantum puncture by its exact center action instead.

Label the integrable sectors by r=0,...,k, corresponding to spin r/2. The fusion rule is

\[
r\times s=\{|r-s|,|r-s|+2,\ldots,\min(r+s,2k-r-s)\}.
\]

For J=k,

\[
J\times r=k-r.
\]

Using h\(_r\)=r(r+2)/[4(k+2)], its double-braiding phase with r is

\[
\frac{\theta_{k-r}}{\theta_k\theta_r}
=\exp\left(2\pi i[h_{k-r}-h_k-h_r]\right)
=(-1)^r.
\]

In particular, a fundamental spinor Wilson probe acquires -1 around this puncture. This is the exact quantum central-monodromy criterion used here; it is not merely a choice of a familiar label with three components. Center symmetry lines in Chern–Simons theory are part of the established generalized-symmetry framework [C].

## 3. Quantization gives one puncture state at even level

For a torus with one puncture labelled J, the conformal-block/Hilbert-space dimension is

\[
\dim\mathcal H_k(\Sigma_{1,1};J)
=\sum_{r=0}^{k}N_{Jr}^{\ r}.
\]

The return-channel criterion is standard [GL, W]. Here it is elementary: J sends r to k-r. Therefore

\[
\boxed{
\dim\mathcal H_k(\Sigma_{1,1};J)=
\begin{cases}
0,&k\text{ odd},\\
1,&k\text{ even},
\end{cases}
}
\]

and the unique even-level handle label is r=k/2, or ordinary spin j=k/4.

Consequently the previous level-one ordinary block obstruction is not dismissed: k=1 still gives zero. The first nonzero candidate in this particular family is k=2.

### Dehn-twist phase and the level filter

The chiral central charge is c=3k/(k+2). In the fixed conformal-block framing, the unique handle state contributes

\[
h_{k/2}-\frac{c}{24}
=\frac{k}{16}.
\]

Its T coefficient is therefore

\[
\boxed{t_J=\exp(2\pi i k/16).}
\]

The source needs exp(2 pi i/8). Thus

\[
\boxed{k=2\pmod{16}}
\]

is a necessary phase match in this family and framing. An exact scan to k=80 checks the formula; the congruence is analytic and not limited to the scan. Its positive solutions begin 2,18,34,50,66,... . Phase matching alone does not uniquely select the level.

An optional stronger identification uses the original coefficient doublet. At k=2+16n, the handle ground representation has dimension k/2+1=2+8n. Its restriction to Q8 is 1+4n copies of the unique quaternion doublet (the center is negative and all noncentral quaternion traces vanish). Requiring **exactly one** copy, with no additional handle multiplets, selects k=2. This uses a declared physical identification of the original coefficient doublet with the handle ground multiplet; it is not derived without that identification.

### Gauge-invariant Wilson checks of the quaternion point

On the unique handle channel r=k/2, a Wilson loop of label a around a cycle has eigenvalue

\[
\frac{S_{a,k/2}}{S_{0,k/2}}
=\frac{\sin[(a+1)\pi/2]}{\sin(\pi/2)}.
\]

These are precisely the SU(2) character values on a quaternion unit. In particular, the fundamental Wilson trace is zero and the adjoint trace is -1. The other cycle has the same value because transport on this puncture Hilbert space is scalar. At level two the fusion identity W\(_\sigma\)^2=1+W\(_f\) becomes 0=1-1.

This checks the central-sector quantum character values. The matrix holonomies A,B are not themselves gauge-invariant two-by-two operators acting on a one-dimensional Hilbert space.

## 4. The level-two amplitude, calculated from its quantum oscillators

The chiral SU(2)\(_2\) theory has a free realization by **three real Majorana fermions** [L]. This is different from the four-real-fermion realization used earlier. Let

\[
\chi_a(z)\chi_b(w)\sim\frac{\delta_{ab}}{z-w},\qquad a=1,2,3.
\]

Its currents and a cubic field are

\[
K_a=-\frac{i}{2}\epsilon_{abc}:\chi_b\chi_c:,
\qquad G=-i:\chi_1\chi_2\chi_3:.
\]

Wick contraction gives

\[
K_a(z)K_b(w)\sim\frac{\delta_{ab}}{(z-w)^2}
+\frac{i\epsilon_{abc}K_c(w)}{z-w}.
\]

The double pole is k delta/2 with k=2; this is not the old level-one algebra.

The cubic field is a Virasoro primary of weight 3/2 and obeys

\[
G(z)G(w)\sim\frac{1}{(z-w)^3}+
\frac{2\mathcal T(w)}{z-w},
\qquad
\mathcal T=-\frac12\sum_a:\chi_a\partial\chi_a:.
\]

The leading coefficient is 2c/3=1. This is the familiar local N=1 supercurrent algebra of this free realization; no spacetime supersymmetry is inferred.

### Why G belongs to the correct puncture module

There are three affine sectors, denoted 1, sigma, f. They correspond to spins 0,1/2,1, with

\[
(h_1,h_\sigma,h_f)=(0,3/16,1/2).
\]

The primary ground states of f are the three Majoranas. G is a singlet descendant in the **same affine f module**, one grade above its vector ground multiplet. In particular this does not change the puncture label from f to an unrelated field.

The unique torus return channel is sigma, since f times sigma=sigma. Its Ramond ground states form a two-dimensional spinor representation. An ordinary one-point trace of an individual vector primary is zero by SU(2) invariance. The singlet G has a nonzero block.

### Explicit Clifford/oscillator trace

Represent the three Ramond zero modes by

\[
\chi^a_0=\frac{\sigma_a}{\sqrt2}\otimes P_{\mathrm{osc}},
\]

where P\(_{\mathrm{osc}}\) is nonzero-mode fermion parity. It is needed so that zero modes anticommute with oscillator modes. The zero-mode term in G\(_0\) is

\[
-i\chi^1_0\chi^2_0\chi^3_0
=\frac{1}{2\sqrt2}I_2\otimes P_{\mathrm{osc}}.
\]

All other terms in G\(_0\) have zero diagonal trace: they contain unmatched nonzero modes of distinct species. Thus each positive frequency contributes a parity-weighted factor (1-q\(^n\))³, and tracing the ground spinor gives 2/(2 sqrt2). Since

\[
h_\sigma-c/24=3/16-1/16=1/8,
\]

we obtain

\[
\boxed{
\operatorname{Tr}_{\mathcal H_\sigma}
\bigl(o(G)q^{L_0-c/24}\bigr)
=\frac1{\sqrt2}q^{1/8}\prod_{n\ge1}(1-q^n)^3
=\frac1{\sqrt2}\eta(\tau)^3.
}
\]

Define the normalized block B by multiplying this trace by the **constant** sqrt2. Then B=eta³.

An explicit 16-dimensional Clifford/Fock computation with one positive frequency per species reproduces (1-q)³/sqrt2, including every term of the truncated G\(_0\). Independent Euler-product coefficients and the Jacobi odd-derivative expansion agree through relative q\(^{60}\). The analytic trace argument, not the finite cutoff, proves the all-frequency product.

This is a chiral intertwiner/conformal block. It is not an ordinary vacuum expectation value of an odd fermion in a fully parity-graded Hilbert space. A full nonchiral scalar insertion G times G-bar has the corresponding paired block. The role of inserted traces must be kept distinct from state-counting partition functions [GL].

### A real operator product, not a product of separately evaluated amplitudes

In the same Ramond trace,

\[
\operatorname{Tr}_{\mathcal H_\sigma}
\left(K_a(z)\chi_b(w)q^{L_0-c/24}\right)
\propto\delta_{ab}\eta(\tau)^3.
\]

The nonzero result uses the three zero modes, once each, and a single common oscillator trace. At coincidence K\(_a\)chi\(_a\)=G with the chosen cyclic orientation. The off-diagonal traces vanish. The Clifford matrix check gives delta\(_{ab}\)/sqrt2 for the zero-mode trace.

This supplies actual current-polarization response tensors with the quantum line as their coefficient. It does not create three independent gauge-invariant puncture states: leaving a current/source index open requires a framing or an external probe.

## 5. Both modular generators give the original geometric line

The independent product/Jacobi evaluations give, with the usual half-integral local-coordinate lift,

\[
\mathcal B(\tau+1)=e^{\pi i/4}\mathcal B(\tau),
\]

\[
\mathcal B(-1/\tau)=e^{-3\pi i/4}\tau^{3/2}\mathcal B(\tau).
\]

These are also the standard eta identities [D]. After extracting the displayed insertion weight, the coefficient matrices are

\[
\boxed{\rho_{\mathcal B}(T)=\zeta_8,\qquad
\rho_{\mathcal B}(S)=\zeta_8^{-3}.}
\]

They satisfy

\[
\rho(S)^2=[\rho(S)\rho(T)]^3,\qquad
\rho(S)^4=-1,\qquad\rho(S)^8=1.
\]

Thus the line is exactly equivalent to ell from Run 6 on the declared metaplectic lifts. This is not merely a match of one eigenvalue. The current-polarization rotation factor O remains the same adjoint action; ell tensor O has the source's exact triplet coefficient matrices with the printed Run 6 change of basis, checked independently here.

The minus sign of the central puncture rotation is physically compatible with theta\(_f\)=-1. This is a 2+1-dimensional topological spin, **not** four-dimensional gauge chirality.

### Transport and framing scope

Chern–Simons/WZW gives a projectively flat quantum block bundle; specifying framing/local-coordinate conventions fixes the scalar comparison [W]. The computed amplitude has weight 3/2, whereas ell was introduced as a finite coefficient character. We compare that character after extracting the known weight. We do not call eta³ a weight-zero flat function.

We have not recalculated a singular-Dirac Quillen connection for the old rank-two model. Nor do we assert that the old physical determinant line is this new Chern–Simons block line. The quantum transport here belongs to a different, specified gauge theory.

Within this line, the lifted mapping-cylinder action on any positive word w obeys

\[
U(w)=\zeta_8^{n_L(w)-n_R(w)}.
\]

With the compatible trace/categorical gluing framing, a mapping-torus amplitude with the puncture worldline is the trace of U(w), hence this phase. For example LR gives 1 and L³R gives i. These are amplitudes of the declared TQFT with its label and framing, not unframed partition-function values or measured universal numbers.

## 6. The quantum sewing data really are consistent

The SU(2)\(_2\) fusion and topological data are known [RSW]; this run tests them rather than pretending they were derived from the weave:

\[
\sigma^2=1+f,\qquad f\sigma=\sigma,\qquad f^2=1,
\]

\[
(d_1,d_\sigma,d_f)=(1,\sqrt2,1),
\qquad
(\theta_1,\theta_\sigma,\theta_f)
=(1,e^{3\pi i/8},-1).
\]

In the order (1,sigma,f),

\[
S=\frac12\begin{pmatrix}
1&\sqrt2&1\\
\sqrt2&0&-\sqrt2\\
1&-\sqrt2&1
\end{pmatrix}.
\]

A complete unitary multiplicity-free F/R presentation is that of [RSW, §5.3.5]:

\[
F^{\sigma\sigma\sigma}_{\sigma}
=-\frac1{\sqrt2}\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\qquad
F^{f\sigma f}_{\sigma}=F^{\sigma f\sigma}_f=-1,
\]

with all other allowed F matrices identity, and

\[
R^{\sigma\sigma}_1=-e^{-3\pi i/8},\quad
R^{\sigma\sigma}_f=e^{\pi i/8},\quad
R^{ff}_1=-1,\quad
R^{f\sigma}_{\sigma}=R^{\sigma f}_{\sigma}=i.
\]

A general fusion-tree program checks every nonempty matrix block: **106 pentagon blocks and 66 hexagon blocks**, including non-Abelian channels. Choosing the wrong sign of the nontrivial F matrix while retaining these R values fails two hexagon blocks. Frobenius–Schur indicators are (1,-1,1), as required for the pseudoreal sigma sector.

These checks establish the standard SU(2)\(_2\) topological sewing data. They are **not** a classification of all Q8-crossed spin defects in the old interacting model.

### Actual quantum observables

Two sigma excitations can fuse either to vacuum or to f. In those two channels a double exchange has phases

\[
(R^{\sigma\sigma}_1)^2=e^{-3\pi i/4},\qquad
(R^{\sigma\sigma}_f)^2=e^{\pi i/4}.
\]

For three sigma excitations with total sigma, B\(_1\)=diag(R\(_1\),R\(_f\)) and B\(_2\)=F\(^{\dagger}\)B\(_1\)F. They satisfy the braid relation but do not commute. For 2n sigma excitations with total vacuum, the fusion-state dimension is 2\(^{n-1}\).

These are observable exchange/fusion predictions **of this candidate topological phase**. They are established SU(2)\(_2\) physics, not new predictions for quarks or leptons, and no laboratory realization of the weave is asserted.

## 7. The important negative controls

### 7.1 A one-state puncture is not a three-generation theory

At k=2,

\[
\dim\mathcal H(\Sigma_{1,1};f)=1,
\qquad
\dim\mathcal H(\Sigma_1;\varnothing)=3.
\]

The three unpunctured torus states have T exponents

\[
15/16,\quad1/8,\quad7/16,
\]

whereas the manuscript's triplet has

\[
1/8,\quad3/8,\quad7/8.
\]

There is no scalar shift that makes these multisets equal. Consequently the torus vacuum three-space is not the manuscript triplet, even projectively at the T-spectrum level. Three anyon labels, three current components, three spatial dimensions and three generations must not be identified because their counts happen to agree.

For reference, the exact all-genus dimensions are

\[
\dim\mathcal H(\Sigma_g;\varnothing)=2^{g-1}(2^g+1),\qquad
\dim\mathcal H(\Sigma_{g,1};f)=2^{g-1}(2^g-1).
\]

The source's full function Phi and its weight 23/2 have not been derived. Matching a line with eta³ does not account for the remaining weight-ten vector-valued amplitude.

### 7.2 This is not an unnoticed level-two sector of the old faithful model

The old protected flavour currents had level one. The new currents have level two. With generators and simple-pole brackets normalized alike, their double-pole coefficients differ by a factor of two. A basis relabeling or scalar eta factor does not change that quantized operator-algebra datum.

There is a familiar diagonal level-two embedding in SU(2)\(_1\) times SU(2)\(_1\), but it is not a free identification here. The old Q8 acts on the first current triplet and trivially on the second, so it does not preserve the diagonal subspace J\(_a\)+I\(_a\). Moreover, left quaternion multiplication acts by -I on the old four-real-fermion space at the center, while quaternion conjugation on one scalar plus three imaginary components acts trivially there. Exact matrix/character checks expose both differences.

A transparent identification of the old and new flavour current theories is therefore excluded. An interface, gauging, folding, or added sector would need its own physical definition and anomaly/level bookkeeping. This run does not claim to have built that interface.

### 7.3 The source's physical assumptions remain

The original Lambda link, E6 choice, cusp unit, spacetime interpretation, and matter/generation reading are not removed. Chern–Simons theory in 2+1 dimensions is a real quantum gauge theory but has no local propagating bulk gauge modes in this pure topological action. It does not supply an Einstein metric, a 3+1-dimensional spacetime, a Standard Model spectrum, or a physical mass scale.

The extra mapping-class phase is not itself a measurement of a dimensionful coupling. Framing response does not derive Newton's constant.

## 8. Reproducibility and integrity

Run:

```text
python verify_exact.py
python verify_physical_controls.py
python verify_numerical.py --dps 60
python verify_numerical.py --dps 90
```

- `verify_exact.py`: 322 named exact checks. Most of the count is the systematic level scan through 80; this is an inventory, not 322 separate discoveries. Includes the general fusion-tree coherence calculation, the Clifford/Fock trace, finite coefficients, all-genus state-count checks and source-matrix comparisons.
- `verify_physical_controls.py`: 78 exact checks, including original-versus-diagonal Q8 actions, Wilson character values, the one-doublet selector, current-level tests, Clifford response tensors and cubic Wick signs.
- `verify_numerical.py`: 55 comparisons at each precision, including independent Jacobi derivative vs oscillator product, both scalar and full vacuum modular matrices, the modular differential equation and braid controls.

At 60 digits the largest strict normalized residual is about 1.55e-60. At 90 digits it is about 4.61e-90. These are finite-series/product corroborations, not interval-certified tail bounds or independent research teams. The infinite formulas have the analytic derivations stated above or are attributed to the established Chern–Simons/WZW framework.

The local plan was written after literature reading and exploratory reasoning and before the formal scripts. It is not a blind or externally timestamped preregistration. Two additional groups of physical controls (current-vector/Wick tests and the single-doublet selector) were added after the first successful control run; they are not represented as predeclared predictions. No earlier project's executable verification functions were imported. The input files and repository were not edited.

## 9. Claim grades and next physical test

| Claim | Grade |
|---|---|
| SU(2) central-puncture quantum model with specified action, label and framing | **CONSTRUCTED using established framework; added physical hypothesis** |
| Central-puncture Hilbert rank and unique handle phase at all k | **PROVED within that framework; exact finite checks** |
| Necessary phase-matching levels k=2 mod 16 | **EXACT, in fixed framing and orientation** |
| Exactly one source quaternion doublet selects k=2 | **CONDITIONAL selection, with an additional handle-state dictionary** |
| Nonzero level-two inserted block eta³ from Clifford/oscillator trace | **DERIVED in the declared theory** |
| Quantum line's S,T coefficient character equals source ell | **EXACT** |
| Standard SU(2)\(_2\) fusion/braiding consistency | **RECOMPUTED EXACTLY from cited input data** |
| Full source T is the puncture Hilbert space or the ordinary torus three-space | **NOT TRUE for these Hilbert spaces** |
| Old level-one protected theory transported unchanged into this model | **NOT CLAIMED; naive relabeling excluded** |
| Full Phi, 4d matter, gauge chirality, gravity or measured constants | **NOT DERIVED** |

The physical advance is specific: the geometric coefficient line now has a genuine quantum amplitude realization in a related central-puncture gauge theory, with a known action and nontrivial measurable braid statistics. It is no longer only an externally attached flat line.

The next decisive task is a **physical junction or coupling**, not another eta prefactor: can this level-two puncture sector couple consistently to a matter/current sector so that the full line-times-triplet becomes a well-defined gauge-invariant amplitude or physical state? The level mismatch and gauge-frame issue must be addressed explicitly. A successful line comparison alone does not establish that junction, a selection principle for a complete theory, or unification.

## Primary sources

[W] E. Witten, *Quantum field theory and the Jones polynomial*, Commun. Math. Phys. 121 (1989) 351–399. Chern–Simons action, flat-connection quantization, conformal blocks, Wilson observables and framing. https://webhomes.maths.ed.ac.uk/~v1ranick/papers/witten.pdf

[M] G. W. Moore, *Introduction to Chern–Simons Theories*, TASI lecture notes (2019), especially §§3–4. Quantization and WZW/conformal-block conventions. https://www.physics.rutgers.edu/~gmoore/TASI-ChernSimons-StudentNotes.pdf

[RSW] E. Rowell, R. Stong and Z. Wang, *On classification of modular tensor categories*, arXiv:0712.1377v4, especially §5.3.5. Complete corrected SU(2)\(_2\) F/R data and contrasts with the ordinary Ising category. https://arxiv.org/abs/0712.1377

[GL] M. R. Gaberdiel and S. Lang, *Modular differential equations for torus one-point functions*, arXiv:0810.0106. Inserted traces, return-channel condition and modular weights. The specific three-Majorana calculation is performed in this report, not quoted from that paper. https://arxiv.org/abs/0810.0106

[L] T. Liu et al., *Bridging conformal field theory and parton approaches to SU(n)_k chiral spin liquids*, arXiv:2501.09567v3, published Phys. Rev. B 111 (2025) 205137. The known SU(2)\(_2\) three-Majorana realization; no material identification is imported. https://arxiv.org/abs/2501.09567

[C] C. Closset et al., *One-form symmetries and the 3d N=2 A-model*, arXiv:2405.18141. Background on center symmetry lines in Chern–Simons settings. No supersymmetric bulk theory is imported into this run. https://arxiv.org/abs/2405.18141

[D] NIST DLMF §§20.4 and 23.18. Theta derivative and eta modular identities. https://dlmf.nist.gov/20.4 ; https://dlmf.nist.gov/23.18

The source manuscript and Run 6 supply the target representation and its original interpretation. None of the standard Chern–Simons, WZW, Majorana, fusion or eta mathematics is claimed as newly discovered. The contribution is the explicit scoped quantum-line construction, comparison and falsifiable physical boundaries for this weave programme.
