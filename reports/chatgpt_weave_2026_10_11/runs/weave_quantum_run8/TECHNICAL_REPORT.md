# Quantum realization of the weave — Run 8
## An anomaly-matched junction to propagating degrees of freedom: a neutral triplet with unavoidable companions

**Source basis:** the supplied Run 7 report and *A Weave of Two Records*, especially its distinction between geometric flavour and assumed spacetime matter.

**Scope:** a specified 2+1-dimensional gauge/coset interface with a 1+1-dimensional chiral edge. This is an expanded candidate, not the old theory unchanged, not a derivation of the action from the grammar, and not a 3+1-dimensional matter theory. No measured particle data are used.

## Executive result

Run 7 supplied the quantum puncture line of SU(2)_2, with a singlet inserted block proportional to eta^3. It did not supply a physical three-state matter multiplet. This run tests an actual matter junction rather than an externally tensored representation.

Within the restricted class of co-propagating complex fundamental SU(2) doublets, matching a level-two gauge current requires **two doublets**. One is insufficient. With this explicit addition, the full four-complex-fermion chiral algebra has the conformal embedding

\[
\widehat{\mathfrak{su}}(2)_2\times\widehat{\mathfrak{so}}(5)_1
\subset\widehat{\mathfrak{so}}(8)_1.
\]

The gauge commutant and the corresponding standard coset edge are SO(5)_1, with central charge 5/2. This is known physics [WU, LM, NONNE], independently reconstructed at the current and character levels below. It is not a newly discovered topological phase.

The colour f line can end on the mixed primary sector of the matter theory. After its colour index is contracted with the Wilson endpoint, the lowest residual module has **five** components, of weight 1/2. Under the new copy/flavour SU(2) and number U(1),

\[
\boxed{\mathbf5=\mathbf3_0\oplus\mathbf1_{+2}\oplus\mathbf1_{-2}.}
\]

Thus the model has a genuine neutral triplet of propagating line-endpoint excitations, but also a charged pair. The subscripts are charges of the model's number current, normalized to give the microscopic complex fermion charge one. They are not electromagnetic charges. These are components of one affine vector module, not five topological fusion channels or five torus ground states.

The complete five-Majorana invariant inserted trace is eta^5, not eta^3. The cubic made from only the three neutral components has zero unrefined trace in the full spinor module. The charged pair cannot simply be omitted from that trace or gapped in a purely co-propagating edge while keeping the same anomaly response.

The construction requires the chiral parent/inflow data. It is not a boundary of bare SU(2)_2 with every gravitational/framing response unchanged. Nor is the new copy/flavour SU(2) automatically the original weave's quaternion action. The full source T and Phi have not been identified with the endpoint amplitudes.

---

## 1. Fixed input and added hypotheses

Inherited from Run 7:

- A positive-level SU(2)_2 Chern–Simons sector, its central invertible label f, and the declared conformal-block framing.
- The scalar source character ell(T)=exp(pi i/4), ell(S)=exp(-3pi i/4).
- The original quaternion representation on a complex doublet.
- The old protected flavour current algebra has level one. Its other level-one factor is invariant under the old quaternion action; a naive diagonal is not preserved.

Added for this run:

1. Co-propagating fundamental complex doublets are the allowed microscopic charged matter in the test. No counter-propagating charged fields, higher representations, or extra anomalous sectors are included in the minimal counting.
2. A second such doublet is admitted when level matching requires it. The doublet-copy index is new matter content; it is not identified with the two original record symbols or with observed families.
3. Equal-velocity, massless conformal kinetics and the standard colour coset boundary condition are used. This specifies an exactly solvable conformal candidate, not a generic RG endpoint for all interactions.
4. The parent spin/chiral phase and the gravitational response needed to support the edge are retained. The construction can be formulated as a folded interface or as the standard gauged-fermion/parton coset. It must not be called a transparent interface to the old four-real-fermion theory.

These assumptions are not consequences of the PDF. The source's Lambda, E6, cusp-unit and spacetime hypotheses remain separate.

## 2. Why the old fields cannot furnish the required level-two gauge current without a change

The old weight-one Lie algebra is su(2)_A plus su(2)_B, each at level one. A nonzero Lie algebra homomorphism from simple su(2) into one su(2) factor is an isomorphism. An embedding into the sum therefore projects nontrivially into one factor or both. Its possible current levels in this setting are one and two.

Every level-two embedding is a graph

\[
X\longmapsto (X,\varphi X),
\]

where phi is an automorphism. The original quaternion action is (Ad_q,1). For the graph to be invariant, it would be necessary that

\[
\varphi\operatorname{Ad}_q X=\varphi X
\]

for every X. Since phi is invertible, this would require Ad_q=1. The noncentral quaternion elements do not satisfy it. This excludes **all graph embeddings of this type**, not just one convenient diagonal basis.

Equivalently, a weighted current aJ+bI closes with the same normalized simple-pole bracket only when a^2=a and b^2=b. Rescaling cannot turn a level-one faithful factor into level two without changing its algebra.

This argument is restricted to the old weight-one current algebra and its given action. It does not exclude new matter, defects carrying anomalies, different conformal inclusions, or a nontransparent interface.

## 3. Level matching fixes the copy count within the stated matter class

Write the new fields as psi_{ai}, with colour a=1,2 and copy/flavour i=1,...,N. Normalize fundamental generators t^A=sigma^A/2, so tr(t^At^B)=delta^{AB}/2. The colour current is

\[
J_C^A=\sum_i:\!\psi_i^\dagger t^A\psi_i\!:\, .
\]

Direct Wick contraction gives

\[
J_C^A(z)J_C^B(w)\sim
\frac{N\delta^{AB}}{2(z-w)^2}
+\frac{i\epsilon^{ABC}J_C^C(w)}{z-w}.
\]

Thus its level is N. The same coefficient is the two-dimensional chiral gauge-anomaly coefficient. A folded level-two Chern–Simons inflow cancels the gauge variation exactly when N=2, in this restricted class [MOORE]. Schematically,

\[
S_\partial=\frac{i}{2\pi}\int dt\,dx\,
\sum_{i=1}^{2}\psi_i^\dagger(D_t-vD_x)\psi_i,
\]

paired with the oppositely oriented colour inflow -S_CS,2 and its appropriate parent/invertible response. Boundary polarization counterterms and the overall chirality sign are fixed by the usual gauged chiral theory convention; they do not change the integer condition N=k.

**This is not a four-dimensional SU(2) anomaly calculation.** It also does not derive the original choice k=2. Given that choice from Run 7, it fixes the number of fundamental edge channels in this ansatz.

For N=2 there are four complex, or eight real, chiral fermions, with c=4. The original quaternion matrices act faithfully on each copy: the centre acts as minus one on all eight real fermion components.

## 4. The complete gauge commutant is larger than the neutral SU(2) triplet

The complexified weight-one space of eight real fermions is exterior^2(C^8), dimension 28. The code constructs all 28 states and the exact colour, copy/flavour, and number-charge matrices on them. It does not start with a proposed five-dimensional answer.

The joint decomposition is:

| colour spin | copy/flavour spin | number charge | dimension |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 1 |
| 0 | 1 | 0 | 3 |
| 0 | 1 | +2 | 3 |
| 0 | 1 | -2 | 3 |
| 1 | 0 | 0 | 3 |
| 1 | 1 | 0 | 9 |
| 1 | 0 | +2 | 3 |
| 1 | 0 | -2 | 3 |

The colour-singlet currents have total dimension ten. Besides copy/flavour currents and the number current, they include six pair-creation/pair-annihilation currents. These are genuine gauge singlets. Omitting them would incorrectly replace the commutant by only su(2) plus u(1).

An independent real calculation starts from two copies of the quaternion vector space. Left quaternion multiplication generates the colour su(2). The real skew commutant has basis

\[
S\otimes R_a\quad
(S=I,\sigma_x,\sigma_z;\ a=1,2,3),
\qquad
\begin{pmatrix}0&1\\-1&0\end{pmatrix}\otimes I_4,
\]

where R_a are right quaternion multiplication. Its dimension is ten and all brackets close. It is sp(4), isomorphic to so(5) at the Lie-algebra level. The corresponding affine level is one. The general conformal embedding SO(4N)_1 contains SU(2)_N times Sp(2N)_1 is established in [NONNE]; its N=2 branching is given explicitly in [LM].

The stress tensors obey

\[
T_{\mathrm{parent}}=T_C+T_{\mathrm{coset}},
\qquad
c_{\mathrm{coset}}=4-\frac{3\cdot2}{2+2}=\frac52.
\]

The residual chiral algebra is SO(5)_1 in the standard coset/commutant construction [WU]. It admits a free realization by five Majoranas. This statement is about a conformal algebra and its sectors, not a literal linear change of the eight original fermions into three plus five. The latter would fail the original quaternion centre test.

## 5. Spin and affine sectors are retained

Let O_N, v_N, s_N denote the vacuum, vector and spinor characters of SO(N)_1 for odd N, and retain both spinors s_8,c_8 for SO(8)_1. With the faithful colour embedding, the standard sector branching is

\[
\begin{aligned}
O_8&\longmapsto (1,1)\oplus(f,F),\\
v_8&\longmapsto(\sigma,\Sigma),\\
s_8&\longmapsto(f,1)\oplus(1,F),\\
c_8&\longmapsto(\sigma,\Sigma).
\end{aligned}
\]

Here (1,sigma,f) label SU(2)_2, and (1,Sigma,F) label SO(5)_1. Interchanging the names of the two SO(8) spinors changes only that convention. At zero chemical potentials several character functions coincide, but the labels are **not** identified.

The exact functional identities checked are

\[
O_8=O_3O_5+v_3v_5,
\quad
v_8=s_3s_5,
\quad
s_8=v_3O_5+O_3v_5.
\]

Combinatorial oscillator series establish equality through relative weight eight as a check; the all-weight result is the known conformal embedding, not inferred from truncation. A second numerical implementation uses direct theta sums for SO(8) and oscillator products for SO(3),SO(5).

For example the SO(8) even Ramond ground space has the decomposition

\[
\mathbf1_{-2}\oplus(\mathbf3,\mathbf1)_0
\oplus(\mathbf1,\mathbf3)_0\oplus\mathbf1_{+2}.
\]

Its colour-singlet part is exactly the five-dimensional residual vector. This is another way to see why there are two singlets as well as the triplet.

## 6. An actual line endpoint, with its gauge index contracted

The 28 parent currents split as

\[
\boxed{\mathbf{28}=(\mathbf3,\mathbf1)\oplus(\mathbf1,\mathbf{10})\oplus(\mathbf3,\mathbf5).}
\]

The first term is the colour current itself. The last 15 states are colour-affine primaries, not additional colour-current descendants. Their colour-current OPE has a simple adjoint pole but no double pole. For the neutral nine states, this follows immediately from

\[
\mathcal O_{aA}=2:\!\psi^\dagger(t^a\otimes t^A)\psi\!:\ ,
\qquad
\operatorname{Tr}[(t^b\otimes I)(t^a\otimes t^A)]=0.
\]

The other six are colour-adjoint, flavour-singlet pair operators of number charge +2 or -2. They are nonzero by fermionic antisymmetry: the colour pair is symmetric while its two-copy flavour contraction is antisymmetric.

A gauge-invariant paired observable is

\[
\left\langle
\mathcal O_{a\alpha}(z)
[W_f(\gamma)]^{ab}
\mathcal O_{b\beta}(w)
\right\rangle,
\]

with conjugate charge/polarization where appropriate and a specified Wilson-line framing. The path gamma joins the endpoints. Each colour transformation cancels against the corresponding Wilson endpoint transformation. It is not an uncontracted external gauge vector.

At each endpoint, colour adjoint times colour adjoint contains exactly one singlet. The code constructs the projector explicitly:

\[
(P_0)_{ab,cd}=\frac13\delta_{ab}\delta_{cd}.
\]

Tensoring the remaining multiplicity space gives five gauge-invariant endpoint components. Their coset conformal weight is

\[
\boxed{h_{\mathrm{end}}=1-h_f=1-\frac12=\frac12.}
\]

In the standard coset boundary condition their residual chiral blocks are represented by five Majoranas lambda_alpha, with

\[
\langle\lambda_\alpha(z)\lambda_\beta(w)\rangle
=\frac{\delta_{\alpha\beta}}{z-w}
\]

in real normalization. In the charged basis the two-point tensor pairs +2 with -2. This is a prediction of the specified conformal endpoint theory. It is not a calculation of a general nonconformal microscopic Wilson-line correlator at arbitrary coupling.

Under the surviving copy/flavour SU(2) and number U(1),

\[
\boxed{F:\quad\mathbf5=\mathbf3_0\oplus\mathbf1_{+2}\oplus\mathbf1_{-2}.}
\]

There is now a physical, neutral triplet of line-endpoint excitations. It is not an isolated triplet, not three torus fusion states, and not three gauge-chiral generations in four spacetime dimensions.

### Do not confuse two different quaternion actions

The original quaternion group is embedded in the colour gauge group. Its action cancels in a gauge-invariant paired endpoint observable. The surviving copy/flavour SU(2) is a different symmetry, on the newly admitted copy index. One can embed a quaternion subgroup into that SU(2), obtaining the three parity signs on the neutral vector, but this identification is not forced by the original grammar.

In addition, a mapping-class transformation of the background is not merely a constant colour gauge transformation. This run does not infer its full endpoint block transport from the local cancellation argument. It has not identified T with the neutral three-component endpoint space.

## 7. Framing balance: the extra bulk response cannot be discarded

Gauge-anomaly cancellation does not by itself settle the gravitational/framing response. The parent has c=4, while the colour sector has c=3/2. The residual chiral edge has c=5/2.

A consistent description is the known gauged-fermion/parton coset phase [WU], or a corresponding folded interface. Its inflow retains the parent chiral phase and subtracts the colour response. It is **not** simply the bare Run 7 SU(2)_2 phase with the same edge central charge and line spins. Spin level-rank descriptions require the appropriate gravitational terms and transparent-fermion bookkeeping [HS].

The resulting non-Abelian spinor has

\[
\theta_\Sigma=e^{5\pi i/8},
\]

rather than theta_sigma=exp(3pi i/8) in the source SU(2)_2 phase. The relation

\[
\theta_\Sigma=-\overline{\theta_\sigma}
\]

exhibits the orientation and fermionic dressing; equal fusion rings do not establish equality of topological orders.

An independent locality screen checks the known extension back to SO(8)_1. The pair (f,F) is a boson and can be the extension field. Of the nine product sectors, five are local relative to it and four are nonlocal. The local sectors organize into a vacuum orbit, a fermion orbit, and a fixed (sigma,Sigma) sector that splits into two Abelian sectors. All three nontrivial extended twists are -1, as in SO(8)_1. The total squared quantum dimension changes from 16 to 4. This checks the finite sector bookkeeping; it is not a new construction of all sewing coefficients or a proof of a general interface RG flow.

## 8. The new singlet puncture trace is eta^5

The residual SO(5)_1 vector module has a singlet descendant

\[
H_5\propto:\!\lambda_1\lambda_2\lambda_3\lambda_4\lambda_5\!:\ ,
\qquad h=5/2.
\]

The spinor module has a four-dimensional Ramond ground space. Choose five gamma matrices with {gamma_a,gamma_b}=2delta_ab and product -I. Its zero modes are gamma_a/sqrt2 times oscillator parity. After an overall constant phase choice, the product of all five has scalar ground trace 1/sqrt2 times oscillator parity.

Every term with a nonzero mode of a species has zero diagonal trace unless the oscillator contractions are paired; the quintic contains each species once, so only the all-zero-mode term contributes. Each positive frequency therefore contributes (1-q^n)^5. The vacuum exponent is

\[
h_\Sigma-c/24=5/16-(5/2)/24=5/24.
\]

Consequently,

\[
\boxed{
\operatorname{Tr}_{\mathcal H_\Sigma}
[o(H_5)q^{L_0-c/24}]
\propto q^{5/24}\prod_{n\ge1}(1-q^n)^5=\eta(\tau)^5.
}
\]

This is the same inserted-trace method as Run 7, applied to the full new residual theory. It is not a state-counting character.

The coefficient character relative to the Run 7 line differs by eta squared:

\[
\frac{\rho_{\eta^5}(T)}{\rho_{\eta^3}(T)}=e^{\pi i/6},
\qquad
\frac{\rho_{\eta^5}(S)}{\rho_{\eta^3}(S)}=-i.
\]

This is a comparison of these particular framed inserted blocks after their weights are extracted. It is not a claim that every possible combined bulk/interface amplitude must have the wrong multiplier.

### Why taking only the cubic of the neutral triplet does not restore the old trace

In the full four-dimensional Ramond ground space,

\[
\operatorname{Tr}(\gamma_1\gamma_2\gamma_3)=0.
\]

The neutral cubic leaves the other two zero modes unsaturated. All its nonzero-mode terms also have zero diagonal trace. Its unrefined full SO(5) spinor trace is therefore zero, not eta^3. Selecting a charge subspace, refining by a chemical potential, or supplying additional insertions changes the observable and must be stated explicitly.

This is not a contradiction of Run 7's nonzero three-Majorana trace. Its Hilbert space and oscillators were different.

## 9. Physical predictions and why the two singlets cannot be thrown away

The residual model has the chiral Hamiltonian

\[
H_\mathrm{edge}=-\frac{iv}{2}\int dx\,
\sum_{\alpha=1}^{5}\lambda_\alpha\partial_x\lambda_\alpha.
\]

For an edge circle of circumference L,

\[
E-E_\mathrm{vac}=\frac{2\pi v}{L}(h+n),
\qquad
E_\mathrm{vac}=-\frac{2\pi v}{L}\frac{5}{48}.
\]

The unknown v and L are physical inputs. They are not fixed by the source or by the anomaly calculation. The first degeneracies are

\[
\begin{aligned}
O_5&=q^{-5/48}(1+10q+30q^2+85q^3+\cdots),\\
v_5&=q^{19/48}(5+15q+56q^2+130q^3+\cdots),\\
s_5&=q^{5/24}(4+20q+60q^2+160q^3+\cdots).
\end{aligned}
\]

The values agree with the established SO(5)_1 edge spectrum in [WU]. They were recomputed here by independent oscillator counting. The screenshot of that source's Table II was inspected to cross-check that the primary vector is a triplet plus two singlets, not an isolated triplet.

In an ideal ballistic chiral-edge realization, the thermal conductance satisfies

\[
\frac{\kappa}{T}=\frac52\frac{\pi^2k_B^2}{3h_{\rm Planck}}.
\]

The coefficient is 5/3 times that of a three-Majorana edge. This is the usual central-charge thermal prediction [KF], not a new measured property of the weave or a proposed cosmological temperature.

Keeping only three Majoranas would discard chiral central charge one. A local bilinear of the two remaining co-propagating fields does not supply a mass gap: its one-particle eigenvalues are vk plus or minus m, which still cross zero as momentum varies. A genuine nonchiral mass requires counter-propagating partners. More generally an isolated unitary gapped one-dimensional sector cannot absorb the omitted chiral anomaly while the bulk response is held fixed.

Extra opposite-moving modes, another bulk phase, or a changed boundary completion could change this conclusion, but these would be new physical ingredients. No universal statement about all possible completions is claimed.

## 10. What is improved, and what is still missing

The positive result is not another finite-group coincidence. It is a specified gauge-matter/coset junction with a complete low-energy operator count, an explicit colour-contracted endpoint observable, propagating edge excitations, and definite spectral and response predictions.

The costs are explicit:

- a second fundamental matter channel;
- a conformal coset boundary prescription and its parent/inflow phase;
- five residual components, not only three;
- a copy/flavour symmetry not identified by the original grammar;
- a different residual phase line for the simplest invariant trace.

Neither the new flavour SU(2) nor its neutral triplet is automatically the source T. The source's action on the endpoint block must be calculated as actual mapping-class transport, with gauge compensation, framing and physical gluing included. Assigning the same matrices to the new flavour index is not such a calculation.

The natural next test is now concrete: use the explicit colour-contracted endpoint sector, retain all five components and all framing data, and determine whether source L,R induce the required nontrivial mixing on its neutral subspace without an imposed identification of colour and copy symmetries. A failure would reject this full-T dictionary, not the consistency of the known coset phase.

No Standard Model representations, four-dimensional gauge chirality, mass hierarchy, dynamical spacetime, Newton constant, or gravitational field equations are derived. This calculation has produced controlled lower-dimensional physics, not a full TOE.

## 11. Computation inventory and integrity

Run:

```text
python verify_exact.py
python verify_numerical.py --dps 50
python verify_numerical.py --dps 80
```

The final exact script has **52 named checks**. It includes all 28 weight-one states, their joint Casimir/charge subspaces, an independently constructed real quaternion commutant, complete bracket closure, colour-singlet endpoint projection, character coefficients, Clifford traces, topological locality screening, and negative controls. The general embedding and all-weight character statements are supported by analytic arguments and primary literature, not proved merely by a finite count.

The numerical script has **84 comparisons at each precision**. At 50 digits the largest normalized residual is about 1.2562e-49; at 80 digits it is about 8.6173e-80. A known wrong T multiplier produces the nonshrinking discrepancy 2 sin(pi/12)=0.517638... . Direct analytic exponentials in tau are used, avoiding principal-root-of-nome errors. There are no interval-certified tail bounds.

The initial exact script contained one redundant empty-iterator placeholder check; self-review removed it. The real one-gamma and three-gamma trace checks enumerate every distinct case and remain. The initial script/log are retained in history, and final exact results were regenerated. Five explicit Gauss-projection/primary checks were added after the initial successful exact run and are not represented as blind predictions. The working plan was written after source/literature reading and exploration, not independently preregistered.

No original file, earlier report, or repository was edited. No prior run verification module was imported. The scripts do not simulate a microscopic material Hamiltonian, solve a generic interface RG flow, compute the old singular-Dirac Quillen connection, or construct all original quaternion-crossed endpoint sewing data.

## Primary references

[WU] Y.-H. Wu and H.-H. Tu, *Non-Abelian topological order with SO(5)_1 chiral edge states*, Phys. Rev. B 106 (2022) 115129, arXiv:2205.14044v3. Section II supplies the concrete gauged-parton edge coset, five-Majorana spectrum and primary multiplicities. https://arxiv.org/abs/2205.14044

[LM] P. K. Lim, M. Mulligan and J. C. Y. Teo, *Topological orders with classical Lie group symmetries from coupling electron wires*, arXiv:2410.01094v1. Section IV.B.1 gives the precise symplectic SO(8)_1 embedding, current and sector branching; general wire constructions provide context, not a new Hamiltonian simulated here. https://arxiv.org/html/2410.01094v1

[NONNE] H. Nonne et al., arXiv:1107.0171, equation (19). The established embedding SO(4N)_1 contains SU(2)_N times Sp(2N)_1. https://arxiv.org/abs/1107.0171

[HS] P.-S. Hsin and N. Seiberg, *Level/rank Duality and Chern-Simons-Matter Theories*, JHEP 09 (2016) 095, arXiv:1607.07457. Spin structures, gravitational counterterms and line-spin bookkeeping in level-rank constructions. https://arxiv.org/abs/1607.07457

[MOORE] G. W. Moore, *Introduction to Chern-Simons Theories*, TASI 2019 notes, especially section 4.4. Gauge anomaly and WZW/current-algebra normalization. https://www.physics.rutgers.edu/~gmoore/TASI-ChernSimons-StudentNotes.pdf

[KF] C. L. Kane and M. P. A. Fisher, *Quantized Thermal Transport in the Fractional Quantum Hall Effect*, Phys. Rev. B 55 (1997) 15832, arXiv:cond-mat/9603118. Thermal response of chiral edges. https://arxiv.org/abs/cond-mat/9603118

[DLMF] NIST Digital Library of Mathematical Functions, sections 20.7 and 23.18, eta/theta transformations. https://dlmf.nist.gov/23.18

[INPUT] Supplied Run 7 report and Dritero M., *A Weave of Two Records*. These supply the target and its declared assumptions. The added coset interface is external physics tested against them, not content inferred from the PDF.

**No novelty claim** is made for the conformal embedding, SO(5) edge phase, coset spectrum or anomaly method. The contribution of this packet is the explicitly scoped junction test for the supplied programme, its complete state bookkeeping, and the restrictions it exposes.
