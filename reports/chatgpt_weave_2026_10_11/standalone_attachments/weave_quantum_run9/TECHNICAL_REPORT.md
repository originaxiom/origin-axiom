# Quantum realization of the weave — Run 9
## Gauge-invariant endpoint transport: flavour does not mix, and the three handle channels are not the source triplet

**Date:** 10 October 2026.  
**Source basis:** the supplied Run 8 report and *A Weave of Two Records*, especially §§2–4 and §7.  
**Scope:** the already specified equal-velocity SO(5)\(_1\) coset boundary of Run 8, in its standard conformal-block framing. No additional matter, flavour background, colour–flavour locking field, or compensating eta factor is included. No four-dimensional matter or gravitational theory is asserted.

## Executive result

The natural transport in the Run 8 model **does not identify its neutral three-component endpoint multiplet with the source's irreducible triplet T**.

There are two distinct reasons, addressing two different candidate spaces.

1. On the **flavour components**, an original move acts on the surface and the colour background, while the newly added copy/flavour charges are fixed. The physical transport commutes with every fixed global flavour generator. It therefore acts as the identity on the irreducible three-component flavour factor, times a possible matrix on independent conformal-block multiplicities. A compensating colour gauge rotation cancels against the Wilson endpoint; it does not become a new flavour rotation.
2. The **complete three-dimensional pair-only torus block space** does mix under modular transport, but it has projective Dehn-twist order 16, whereas the source T has order 4. This is a mismatch of relative eigenphases and cannot be removed by a common scalar line or a constant change of basis. Keeping the residual central F puncture instead gives a one-dimensional channel space, not three.

We compute explicit endpoint correlators for both the pair-only problem and a nonzero central-puncture problem. In the latter,

\[
\boxed{
\mathcal C_{\alpha\beta}(x,z,w|\tau)
=\delta_{\alpha\beta}\eta(\tau)^5
\left[g(z-w|\tau)-g(x-w|\tau)+g(x-z|\tau)\right],
\quad g=\partial_z\log\theta_1.
}
\]

The formula uses the singlet descendant H\(_5\) in the central F module and two vector endpoints. It includes one common oscillator trace. Both modular generators and the source R move are calculated, with insertion coordinates and weights retained.

The projective spectral obstruction extends to **all complete rank-three ordinary genus-one primary-puncture spaces of odd-Majorana SO(N)\(_1\) theories**. It does not classify arbitrary Q8-crossed defects, selected subspaces of larger block spaces, other theories, or arbitrary redefinitions of the physical dictionary.

The consistent lower-dimensional phase survives; the proposed full-T matter identification does not follow and fails for the natural transport just tested.

---

## 1. Fixed physical dictionary and what is being tested

Run 8 adds two complex fundamental colour doublets, matches their level to the SU(2)\(_2\) colour sector, and uses the established conformal embedding

\[
\widehat{\mathfrak{su}}(2)_2\times\widehat{\mathfrak{so}}(5)_1
\subset\widehat{\mathfrak{so}}(8)_1.
\]

The residual vector F has conformal weight 1/2 and five lowest components,

\[
F:\quad\mathbf5=\mathbf3_0\oplus\mathbf1_{+2}\oplus\mathbf1_{-2}.
\]

The original Q8 is in the colour gauge group. The SU(2) acting on the new neutral triplet is the copy/flavour symmetry. Run 8 expressly left their identification open. The known coset and five-Majorana realization are external physics [WU, LM], not derivations from the source's philosophical postulates.

We retain that precise conformal boundary condition. The original moves act on the marked torus and its colour background. The added copy indices have no flavour holonomy. Coordinates of insertions and Wilson paths are transported with the surface; no independent point-pushing or new flavour rotation is silently appended.

The source uses L=T and R=ST^{-1}S^{-1} on the torus. Its target coefficient matrices in theta order (2,3,4) are

\[
\rho_T(L)=e^{-\pi i/4}
\begin{pmatrix}i&0&0\\0&0&1\\0&1&0\end{pmatrix},
\qquad
\rho_T(S)=e^{\pi i/4}
\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}.
\]

The source T-exponents are 1/8, 3/8, 7/8. Here T denotes the source triplet; a modular Dehn twist will otherwise be written L or as a matrix with a subscript to avoid ambiguity.

This report is **not** a calculation of an arbitrary microscopic Wilson correlator away from the conformal boundary condition. It is also not the old singular rank-two E-plus Dirac problem. The residual central-F insertion used below is the ordinary coset image being tested; unknown additional nonabelian spin-defect junctions are not assumed to have been classified.

## 2. Gauge compensation does not rotate the new flavour labels

The mixed parent operators have colour-adjoint and residual-vector indices,

\[
\mathcal O_{a\alpha},\qquad a=1,2,3,\quad\alpha=1,\ldots,5.
\]

A paired endpoint observable contracts them through an adjoint Wilson line, as in Run 8. At an endpoint the colour-invariant vector is

\[
|\Omega\rangle=\frac1{\sqrt3}\sum_{a=1}^3|a\rangle\otimes|a\rangle,
\qquad P_0=|\Omega\rangle\langle\Omega|.
\]

A colour gauge compensation O acts as O tensor O on these real adjoint indices. For every O in SO(3),

\[
(O\otimes O)|\Omega\rangle=|\Omega\rangle.
\]

In particular this holds for both quaternion-normalizer compensations associated with L and R. Projecting the complete endpoint action gives

\[
\Omega^\dagger(O\otimes O\otimes I_5)\Omega=I_5.
\]

The colour index has been contracted, not relabelled as a flavour index.

### The geometry part requires a separate argument

A mapping-class transformation is not merely a gauge transformation. Its remaining action on the coordinate dependence and handle channels must still be retained.

Let Q\(_F^a\) be the three **fixed microscopic copy/flavour generators**. The colour background, equal-velocity action, Gauss projection, and chosen geometric transport all commute with them. Therefore

\[
[U(\gamma),Q_F^a]=0
\]

for the canonical transport of every allowed word. Coordinate and framing factors may be nontrivial, but they do not rotate the fixed copy generators into each other. A chiral flavour anomaly does not break the constant global flavour rotations at zero flavour background.

On an isotypic component \(\mathcal M\otimes V_3\), where V\(_3\) is the irreducible flavour vector and \(\mathcal M\) is a block/other multiplicity space, Schur's lemma then gives

\[
\boxed{U(\gamma)=U_{\mathcal M}(\gamma)\otimes I_3.}
\]

This does **not** assert that every conformal block is a scalar. It asserts that the nontrivial transport is on the separate multiplicity space, not on the three copy/flavour components.

An isotropic two-point tensor delta\(_{AB}\) alone would not prove this: arbitrary rotations also preserve delta. The commutation with **each fixed flavour charge**, together with the specified source action, is the decisive input. A tau-dependent choice of flavour basis could create apparent matrix connection coefficients; it would not derive a physical holonomy from this scalar action. A multivalued external flavour frame would be new transport data.

The code computes the spin-one commutant directly and finds dimension one. The source's O\(_L\),O\(_R\) fail to commute with the fixed flavour generators. Therefore the source T cannot be this neutral flavour factor under the declared transport.

The same conclusion holds even when extra scalar framing/inflow factors are retained. They multiply U\(_\mathcal M\), not I\(_3\).

## 3. Explicit pair-only torus endpoint amplitudes

We next compute the nontrivial block transport rather than infer it from local colour cancellation.

Use the standard five-Majorana realization of the residual vector fields lambda\(_\alpha\), with OPE

\[
\lambda_\alpha(z)\lambda_\beta(w)\sim\frac{\delta_{\alpha\beta}}{z-w}.
\]

All theta arguments below have period one, and q=exp(2 pi i tau). For the three nonzero even spin structures nu=2,3,4, put

\[
Z_\nu(\tau)=\left(\frac{\theta_\nu(0|\tau)}{\eta(\tau)}\right)^{5/2},
\qquad
S_\nu(u|\tau)=\frac{\theta_\nu(u|\tau)}{\theta_\nu(0|\tau)}
\frac{\theta_1'(0|\tau)}{\theta_1(u|\tau)}.
\]

Fractional powers are defined by analytic oscillator products at the cusp, not reset principal roots. S\(_\nu\) is the torus Szego kernel [TZ]. Wick contraction gives

\[
\boxed{\mathcal B^{(\nu)}_{\alpha\beta}(z,w|\tau)
=\delta_{\alpha\beta}Z_\nu(\tau)S_\nu(z-w|\tau).}
\]

This is the same-theory correlator with one common trace, not a product of two one-insertion amplitudes.

The odd-spin partition function is zero. Two endpoint insertions alone cannot saturate the five odd-spin zero modes, so no fourth pair-only spin function has been omitted.

Write B\(_\nu\)=Z\(_\nu\)S\(_\nu\) and \(b=(B_2,B_3,B_4)^T\). The module/handle basis is

\[
\mathbf B=(B_1,B_F,B_\Sigma)^T
=\left(\frac{B_3+B_4}{2},\frac{B_3-B_4}{2},\frac{B_2}{\sqrt2}\right)^T.
\]

The factor 1/sqrt(2) in the Ramond channel gives the correct four-dimensional spinor ground representation; unrefined spin functions and affine sector labels must not be confused.

The fusion count confirms this complete block rank:

\[
F^2=1,\quad F\Sigma=\Sigma,\quad\Sigma^2=1+F,
\qquad\dim\mathcal V_{1,2}(F,F)=\operatorname{Tr}N_F^2=3.
\]

The endpoints are fused in a small disk and the handle Dehn twist is supported outside it. The three labels are the possible handle channels 1,F,Sigma, not three matter polarizations.

### Full generator transport, including endpoint weights

Theta and eta transformations [D] give

\[
b(u|\tau+1)=
\begin{pmatrix}
e^{5\pi i/12}&0&0\\
0&0&e^{-5\pi i/24}\\
0&e^{-5\pi i/24}&0
\end{pmatrix}b(u|\tau),
\]

\[
b(u/\tau|-1/\tau)=\tau
\begin{pmatrix}0&0&1\\0&1&0\\1&0&0\end{pmatrix}b(u|\tau).
\]

The weight one is the sum of the two endpoint weights. In the affine basis,

\[
S_{\mathrm{pair}}=\frac12
\begin{pmatrix}1&1&\sqrt2\\1&1&-\sqrt2\\\sqrt2&-\sqrt2&0\end{pmatrix},
\]

\[
L_{\mathrm{pair}}=
\operatorname{diag}\left(e^{-5\pi i/24},e^{19\pi i/24},e^{5\pi i/12}\right).
\]

The corresponding R matrix is S L\(^{-1}\) S\(^{-1}\). In the spin basis it sends

\[
(B_2,B_3,B_4)\mapsto
(e^{5\pi i/24}B_3,\ e^{5\pi i/24}B_2,\ e^{19\pi i/12}B_4),
\]

with the full coordinate/weight factor (tau+1) and arguments u/(tau+1), tau/(tau+1). All three transformations are directly tested at generic complex moduli.

The spin-basis coefficient image has order 1152, calculated by exact monomial phase arithmetic. This group order is a check, not the main obstruction.

## 4. The three handle channels fail even projectively

The handle exponents of the pair are

\[
\left\{-\frac5{48},\frac{19}{48},\frac5{24}\right\},
\]

while the source has

\[
\left\{\frac18,\frac38,\frac78\right\}.
\]

The smallest positive power of the source L matrix that is scalar is four. For the pair L matrix it is sixteen:

\[
\boxed{\operatorname{ord}_{\mathrm{proj}}L_T=4,
\qquad\operatorname{ord}_{\mathrm{proj}}L_{\mathrm{pair}}=16.}
\]

For example, normalize the pair eigenvalues by the vacuum one. Their relative phases are

\[
\{1,-1,e^{5\pi i/8}\}.
\]

The last is a primitive sixteenth root. The source relative phases have order four.

A common scalar multiplier, including a tensor factor supplied by the old eta-cubed puncture line, does not change any eigenvalue ratio. No constant basis change changes the spectrum. Orientation reversal inverts phases but does not change the projective order.

This is stronger than the earlier common-scalar coefficient discrepancies: it is a mismatch of **relative Dehn-twist phases** in the fixed framed block transport. L has c=0,d=1, so including different modular weights does not remove this particular relative spectrum test. It is not a claim about all possible holomorphic bundle isomorphisms with newly chosen connections or cusp extensions.

The coset phase is consistent. Its rank-three handle space is simply not the source T.

## 5. Retaining the central puncture: a nonzero explicit block

It would be incorrect to substitute the pair-only problem for the original central-puncture problem. We therefore also retain the ordinary residual central label F in the same coset dictionary.

With that label and two vector endpoints,

\[
\dim\mathcal V_{1,3}(F,F,F)=\operatorname{Tr}N_F^3=1.
\]

Three vector **primary components** give a vanishing unrefined SO(5)-invariant trace. To obtain a nonzero component of this one-dimensional block, use the same singlet descendant in the central module as Run 8,

\[
H_5(x)\propto:\lambda_1\lambda_2\lambda_3\lambda_4\lambda_5:(x),
\qquad h_{H_5}=5/2.
\]

It is a descendant in the same affine F module, not a new puncture label. Its reference trace is eta\(^5\), up to a constant normalization.

Define

\[
g(u|\tau)=\partial_u\log\theta_1(u|\tau),
\]

\[
\mathcal R(x,z,w|\tau)
=g(z-w|\tau)-g(x-w|\tau)+g(x-z|\tau).
\]

The odd-spin zero-mode calculation now gives

\[
\boxed{
\langle H_5(x)\lambda_\alpha(z)\lambda_\beta(w)\rangle_{\rm block}
=\delta_{\alpha\beta}\eta(\tau)^5\mathcal R(x,z,w|\tau).
}
\]

An overall constant phase/normalization is fixed by the OPE residue. There is **one** common oscillator factor eta\(^5\).

### Derivation and checks of the zero-mode structure

If alpha differs from beta, the four/five species have the wrong zero-mode saturation pattern and the Clifford trace vanishes. If alpha=beta, four species saturate their zero mode at x; the fifth has three insertions. The three ways to use its zero mode and contract the other two give the alternating cyclic kernel above.

An independent finite matrix calculation uses a four-dimensional irreducible zero-mode Clifford module and one positive oscillator for each of five species (a 128-dimensional total space). All 25 paired index choices equal delta times the explicit finite mode kernel. The all-frequency result follows from Wick's rule and the convergent oscillator sum, not from that cutoff.

The kernel is elliptic in the endpoint coordinates, antisymmetric under z and w, and obeys

\[
\mathcal R(x,z,w)\sim\frac1{z-w}\quad(z\to w).
\]

Thus the endpoint pair fuses back to the same nonzero central trace. We also verify the poles at the central insertion. The formula is a genuine correlated amplitude, not the square of a previously calculated one-point block.

For ordered cylinder separation -Im(tau)<Im(u)<0, the independent oscillator kernel is

\[
g(u|\tau)=2\pi i\left[
\frac12+\sum_{n\ge1}
\frac{e^{-2\pi inu}-q^n e^{2\pi inu}}{1-q^n}
\right].
\]

This agrees with the theta logarithmic derivative by the triple-product identity. Three such sums give the independently evaluated cyclic kernel.

### Full transport with the central insertion retained

Under S, the anomalous linear term in the logarithmic derivative is

\[
g(u/\tau|-1/\tau)=\tau g(u|\tau)+2\pi i u.
\]

It cancels in the cyclic sum because (z-w)-(x-w)+(x-z)=0. Consequently, with C denoting the scalar part of the paired central amplitude,

\[
C(x,z,w|\tau+1)=e^{5\pi i/12}C(x,z,w|\tau),
\]

\[
C(x/\tau,z/\tau,w/\tau|-1/\tau)
=e^{-5\pi i/4}\tau^{7/2}C(x,z,w|\tau),
\]

\[
C\left(\frac{x}{\tau+1},\frac{z}{\tau+1},\frac{w}{\tau+1}\middle|\frac{\tau}{\tau+1}\right)
=e^{-5\pi i/12}(\tau+1)^{7/2}C(x,z,w|\tau).
\]

The total weight 7/2 includes all three insertions. The coefficient character is still that of eta\(^5\); the extra endpoints have not manufactured a new three-dimensional space or neutral flavour rotation.

These formulas compute the standard residual central-F conformal block selected by the declared coset boundary. They do not claim that every microscopic noncommuting-Q8 spin-defect junction is exhausted by ordinary affine labels. The flavour-commutant obstruction in §2 nevertheless applies to colour-only backgrounds without adding a flavour connection, even if additional scalar/block multiplicities are retained.

## 6. A class-wide obstruction prevents an endless odd-Majorana ladder

The ordinary level-one SO(N) theories for odd N have the same three fusion labels 1,F,Sigma, with

\[
F^2=1,\quad F\Sigma=\Sigma,\quad\Sigma^2=1+F.
\]

Their conformal weights are 0,1/2,N/16 and c=N/2. These follow directly from the free-Majorana NS and Ramond vacua; the associated Ising-type modular categories and their different twists are standard [RSW].

For a torus with n_F vector labels and n_S spinor labels,

\[
\dim\mathcal V_{1}(F^{n_F},\Sigma^{n_S})
=\operatorname{Tr}(N_F^{n_F}N_\Sigma^{n_S}).
\]

The fusion identities yield exactly

\[
\begin{cases}
0,&n_S\text{ odd},\\
2^{n_S/2+1},&n_S>0\text{ even},\\
3,&n_S=0,\ n_F\text{ even},\\
1,&n_S=0,\ n_F\text{ odd}.
\end{cases}
\]

Thus a **complete rank-three ordinary genus-one block space** in this class has no spinor punctures and an even number of F punctures. They fuse to vacuum in a disk, so the relative handle-twist phases are

\[
\{1,-1,e^{\pi iN/8}\}.
\]

For odd N, the last phase is a primitive sixteenth root. Its projective order is 16, never the source's 4.

\[
\boxed{\text{No complete ordinary rank-three genus-one block space in this odd-N class is projectively equivalent to source }T.}
\]

This covers the obvious progression from three to five to seven Majoranas. Increasing that count does not solve the stated identification. The exact code checks N=1,3,...,99 (N=1 is the Ising control); the odd-N number-theoretic argument is not limited to that census.

This does **not** exclude selected invariant subspaces of larger block spaces, nonordinary Q8-crossed spin defects, new orbifolds, coupling bundles, other levels/groups, or nonstandard physical dictionaries. It excludes the complete spaces and canonical handle action specified above.

## 7. A minimal diagnostic for a proposed colour–flavour reference field

The obstruction can be evaded only by changing a relevant assumption. One tempting proposal is an extra field M with a colour-adjoint index and a flavour-vector index, whose background relates the two.

No such field or action is added in this run. We test only a necessary condition for a **covariantly constant** background with trivial flavour holonomy in the original flat Q8 background.

Let

\[
Q_A=\operatorname{diag}(1,-1,-1),\qquad
Q_B=\operatorname{diag}(-1,1,-1).
\]

Parallel transport requires

\[
Q_A M=M,\qquad Q_B M=M.
\]

Their common fixed space is zero, so

\[
\boxed{M=0.}
\]

A nonzero full-rank parallel reference therefore cannot simply be inserted while keeping the same colour holonomies and trivial flavour holonomy. A spatially varying field, additional flavour background, flux or changed holonomy dynamics would define a different physical construction requiring its own action and energy analysis.

As a positive control, imposing matched flavour holonomies changes the equations to Q_A M=M Q_A and Q_B M=M Q_B. Then M=I is allowed. Imposing the same normalizer action leaves a one-dimensional scalar-frame space. This illustrates exactly what additional colour–flavour identification would have been supplied; it does not derive that identification dynamically.

## 8. Physical interpretation

The candidate has propagating endpoint excitations and consistent lower-dimensional amplitudes. Those results from Run 8 are retained. The present test rejects the next proposed identification: **the neutral copy/flavour triplet is not automatically the original weave's geometrically transported T**.

Three different objects must remain separate:

- five physical endpoint components (including a neutral triplet);
- three pair-only handle/spin channels;
- the source's three parity-cohomology lines.

The first has no derived source mixing on its flavour indices. The second has the wrong relative modular phases. Retaining the ordinary central puncture gives one block. Matching any two dimensions would hide these differences.

This is a model/dictionary rejection, not a contradiction of the geometric cohomology and not a universal obstruction to the Origin Axiom programme. The original source explicitly distinguishes its derived representation from its assumed identification with generations and spacetime matter.

For the physics goal, the useful consequence is to stop trying to repair this branch with more odd-Majorana species or a common eta line. Its issue is which degrees of freedom the record moves physically act on after Gauss's law. A different construction must derive a relation to flavour, or explicitly keep the record structure as an ungauged background/matter bundle rather than treating its orientation as colour redundancy. Neither step follows from the present action.

No Standard Model gauge group, four-dimensional chirality, observed mass, dynamical spacetime or gravitational field equation is obtained here.

## 9. Verification and integrity

Run:

```text
python verify_exact.py
python verify_clifford.py
python verify_numerical.py --dps 55
python verify_numerical.py --dps 85
```

The final exact scripts contain **49 named checks**: 40 algebra/transport/fusion checks and 9 Clifford/Fock checks. Some checks contain whole finite arrays (all 25 index pairs, 42 puncture counts, 50 odd-N controls); their enumeration is an implementation check of the stated proofs, not independent discoveries.

The numerical script has **116 comparisons per precision**: 100 strict identities and 16 finite-separation OPE limits, evaluated at four moduli. It checks direct theta kernels against independently summed cylinder modes, oscillator partition products, full S/T/R transport, affine-basis transport, the central-puncture cyclic kernel and fusion residues. Coefficient roots are defined by analytic oscillator products in tau rather than principal powers of the nome.

At 85 digits:

- maximum strict normalized residual: approximately **5.67e-85**;
- maximum finite-limit normalized residual: approximately **8.54e-58**;
- deliberately wrong target T residuals: approximately **0.23–0.36**, independent of working precision.

These are high-precision corroborations, not interval-certified tail estimates. The all-word and all-odd-N conclusions have the analytic arguments above.

### Retained correction

The first finite Clifford script incorrectly demanded exact separated-point antisymmetry at a finite Fourier cutoff. It failed. At that cutoff the anticommutator is a nonzero truncated contact kernel, not the analytically continued meromorphic CFT answer. The assertion was replaced by the correct contact-kernel identity; the source and failure log are retained. All 25 finite paired-trace formulas had already passed. Full meromorphic antisymmetry is separately verified in the theta and mode-continuation calculation.

Three reference-field diagnostics in §7 were added after the initial exact run; they are not described as prior predictions. The plan was hashed after source reading and exploratory reasoning, not independently preregistered. No earlier executable verification module was imported. Source PDF, earlier reports and repository were not edited.

No singular-operator Quillen or Bismut–Freed connection, microscopic interface RG flow, or arbitrary nonabelian defect-category classification is claimed. The transport calculated is the declared conformal-block transport of the exact coset candidate.

## 10. Claim grades

| Claim | Status |
|---|---|
| Natural colour/geometry transport does not mix the fixed neutral flavour triplet | **PROVED within the specified model and symmetry action** |
| Pair-only endpoint blocks and their full S/T/R transformations | **DERIVED; independently checked** |
| Nonzero central-F/H5 paired block, with its oscillator trace | **DERIVED in the five-Majorana boundary realization** |
| Pair-only rank-three block is the source T | **EXCLUDED even projectively** |
| Ordinary odd-Majorana rank-three genus-one ladder can repair this | **EXCLUDED within the stated complete-block class** |
| Nonzero parallel neutral flavour frame in the fixed Q8 colour background | **EXCLUDED under the stated parallel/background assumptions** |
| Every possible physical realization of T fails | **NOT CLAIMED** |
| Four-dimensional matter, gravity or a complete theory of everything | **NOT DERIVED** |

## Primary references and boundaries

[INPUT] Supplied Run 8 `TECHNICAL_REPORT.md`, especially §§1, 6, 8 and 10; Dritero M., *A Weave of Two Records*, §§2–4 and §7. These supply the model being continued, its target and its declared assumptions.

[WU] Y.-H. Wu and H.-H. Tu, *Non-Abelian topological order with SO(5)_1 chiral edge states*, Phys. Rev. B 106 (2022) 115129, arXiv:2205.14044v3. Coset edge, five-Majorana realization and vector/spinor spectra. https://arxiv.org/html/2205.14044v3

[LM] P. K. Lim, M. Mulligan and J. C. Y. Teo, *Topological orders with classical Lie group symmetries from coupling electron wires*, arXiv:2410.01094v2, §IV.2.1. Conformal embedding and current/sector bookkeeping. https://arxiv.org/html/2410.01094v2

[TZ] M. P. Tuite and A. Zuevsky, *Genus Two Partition and Correlation Functions for Fermionic Vertex Operator Superalgebras II*, arXiv:1308.2441, §§2 and 4. Szego kernel, prime form, torus intertwiners and oscillator framework. The specific five-Majorana central insertion is derived here, not quoted as that paper's theorem. https://arxiv.org/abs/1308.2441

[D] NIST Digital Library of Mathematical Functions, §§20.4, 20.7 and 23.18. Theta derivative, product and modular formulas, translated to period-one arguments. https://dlmf.nist.gov/20.7 ; https://dlmf.nist.gov/23.18

[RSW] E. Rowell, R. Stong and Z. Wang, *On classification of modular tensor categories*, arXiv:0712.1377v4, especially §5.3. Ising-type fusion versus its different twists; ordinary modular categories are not all spin/Q8-crossed defects. https://arxiv.org/html/0712.1377v4

[GL] M. R. Gaberdiel and S. Lang, *Modular differential equations for torus one-point functions*, arXiv:0810.0106v2, §2. Return-channel condition and inserted-block transformation laws. https://arxiv.org/html/0810.0106v2

No novelty claim is made for Schur's lemma, free-fermion kernels, ordinary fusion rules or the known coset. The contribution is their explicit transport calculation and scoped falsification of this particular source-to-matter dictionary.
