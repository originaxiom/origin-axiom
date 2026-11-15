# X-FUNNEL source and premise review

2026-11-15. Read at `d6f77f7ff74b9c9e359fac764e6f363262fffa5e` on
`agy/self-consistent-loop-2026-11-11`. The review card is committed at
`97d098208`. The fetched main head is recorded in `SOURCE_RECEIPT.json`.

The campaign provides a conditional magnetic-overlap construction and
several exact distribution identities. Its final synthesis needs
corrections before its stages can support one physical model. An exact
monodromy error changes the proposed order-fifteen selection problem.
The stated averaging measure, the magnetic kinetic operator and the
vacuum determinant also need matching.

## Scope and check state

All four X-FUNNEL result notes were read. The deciding source blocks
were inspected for the magnetic modes, overlap quadrature, modular
checks, torsion projections, Casimir spectrum, matrix averaging and
running examples. The saved JSON outputs and declared hashes were
inspected as data. All eight script/output hash pins match the pinned
bytes.

The new work here consists of source findings and the mathematical
derivations written below. The upstream numerical check state remains
`computed once`. This reading generated no second scientific output.
The receipt records the original failure flags. It supplies custody
evidence only. The earlier campaign, the complete renormalization-group
implementation, its literature benchmarks and every numerical precision
claim remain outside a full independent recomputation in this review.

The branch's four result commits preserve their failed thresholds and
explain them. Every aggregate `stage_n_gate_passed` is false in its
original output. These flags need their stated individual interpretation.
They do not by themselves decide whether an identity is false. Stage two
also closes stage one's reported small-height truncation issue in the
received evidence. This report preserves those disclosures.

## 1. Exact error in the monodromy modulo three

`relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_4_RESULTS.md`, line 62, says

> $M \bmod 3$ has order `8`, acting transitively on all `8` non-zero `3`-torsion points!

For the campaign's own matrix,

\[
 M=\begin{pmatrix}2&1\\1&1\end{pmatrix},\qquad
 M^2=\begin{pmatrix}5&3\\3&2\end{pmatrix}
       \equiv-I\pmod3.
\]

Thus `ord(M mod 3)=4`. Acting on row vectors, its nonzero orbits are

\[
\begin{split}
 &(1,0)\to(2,1)\to(2,0)\to(1,2)\to(1,0),\\
 &(0,1)\to(1,1)\to(0,2)\to(2,2)\to(0,1).
\end{split}
\]

The orientation-reversing root
`J=[[1,1],[1,0]]` satisfies `J^2=M`. It has order eight modulo three
and joins these two orbits. This distinguishes transport under the
monodromy from transport under the larger architecture's odd step.

The same paragraph's fixed-point calculation holds. `det(M-I)=-1`,
so a nonzero fixed point modulo three is excluded. Its inference of
one orbit of eight under `M` fails. Both four-point orbits must be
retained in the selection question until a further rule distinguishes
them. The retained larger action joins them.

A consequence can already be derived without a numerical search. On
the product of the four-point order-five eigenline and the eight nonzero
order-three points, `M` has eight orbits of length four. `J` has four
orbits of length eight. This concerns those 32 order-fifteen points.
The full set has 192 points. A canonical lift still needs a rule.

## 2. The implemented measure is the Poincare measure

`relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_3_RESULTS.md`, line 44, writes

> \operatorname{Vol}_{\mathrm{WP}}(\mathcal{F}) = \pi/3

`relays/x_funnel_3_verify/verify_x_funnel_3.py`, lines 685–718, integrate
with weights `wx * wu`, where `u=1/y`. This is

\[
 dx\,du=\frac{dx\,dy}{y^2}
\]

with the integration limits oriented positively. It is the hyperbolic
Poincare area on the modular fundamental domain. Direct integration gives

\[
 \int_{-1/2}^{1/2}\int_{\sqrt{1-x^2}}^\infty
       \frac{dy\,dx}{y^2}
 =\int_{-1/2}^{1/2}\frac{dx}{\sqrt{1-x^2}}=\frac\pi3.
\]

The Weil–Petersson metric of the hyperbolic once-punctured torus is
different. Wolpert explicitly distinguishes it from a multiple of the
hyperbolic metric on Teichmuller space and calculates its moduli area
as `pi^2/6` in his normalization. His argument addresses the same
once-punctured carrier. This discrepancy concerns the density, so
rescaling the total volume alone does not repair the identification.
The implemented Poincare integral remains a defined conditional
calculation. Its name and its proposed physical origin need correction.
[Wolpert, pages 247 and 253–255](https://macbuse.github.io/M2R_2019/wolpert.pdf)

## 3. The Casimir action uses a different fermion operator

`relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_1_RESULTS.md`, line 36, uses

> magnetic flux $I_L = +3$

Its explicit `cim_landau_mode` in
`relays/x_funnel_1_verify/verify_x_funnel_1.py`, lines 577–602, implements
constant-flux Landau sections. Stage three's
`v_cas_orbit_tau`, lines 316–338, then inserts all 90 fermionic real
degrees into `eisenstein_char_fast`. That function, lines 251–276,
uses the flat character lattice with a Bernoulli-six cusp coefficient.
Its arguments contain the flat twists and omit the magnetic degree.

For a flat compact torus at fixed area `A`, a constant nonzero magnetic
degree `I` gives the scalar covariant-Laplacian levels

\[
 \lambda_r=\frac{2\pi|I|}{A}(2r+1),
\]

with degeneracy `|I|`. Squaring the Dirac operator adds the curvature
term and gives the chiral zero level and oscillator tower. Flat Wilson
twists translate the modes while preserving these free kinetic
eigenvalues. The harmonic-oscillator commutator establishes this
directly. The construction and spectrum are also given in equations
103–109 of Cremades–Ibanez–Marchesano.
[Primary derivation, section 3.3](https://arxiv.org/html/hep-th/0404229)

The flat Epstein spectrum and the magnetic oscillator spectrum therefore
require different determinants. Stage three's rational supertraces
are valid for its declared flat spectral sum. Their use as the
vacuum action of stage one's magnetic fermions requires a new
derivation from those fermions' operator. A puncture, interactions or
end law can change the spectrum. Those changes have to enter that
same calculation. This is the central unresolved connection in the
campaign's physical synthesis.

## 4. The compact index, puncture and source each carry a premise

The stage-one result, line 36, concludes

> yielding $\dim H^0 = 3$ chiral generations by Riemann–Roch

On a compact elliptic curve, a line bundle `L` of degree `I>0`
has `h^0(L)=I`. Indeed `K` is trivial, `h^0(L^-1)=0`, and
Riemann–Roch gives `h^0(L)-h^0(L^-1)=I`. Tensoring by a flat spin
line leaves this count unchanged. This establishes the compact
three-mode count under the supplied choice `I=3`.

The implemented generation indices run from zero to two and the
overlap source uses degree three throughout. Deriving this integer
from the registering principle remains a separate duty. The choice
of a magnetic bundle, its chirality and the embedding of the external
matter representations also remain explicit inputs.

The punctured curve needs a complete operator-domain statement.
The compact sections used by the code provide a possible extension
across the puncture. Riemann–Roch on that extension cannot count the
whole punctured operator's kernel until its metric, growth and domain
conditions have been specified and compared. The campaign's finite
flat quadrature supplies an overlap for the chosen sections.

There is a further distinction between a finite overlap and the scalar
source's variational problem. Line 38 uses a point Green source
`Phi_H=(-Delta_A)^-1 delta_0`. Locally

\[
 \Phi_H\sim c\log r,\qquad
 \int_0^\epsilon r|\log r|^2\,dr<\infty,\qquad
 \int_0^\epsilon r|\partial_r\Phi_H|^2\,dr
       \sim |c|^2\int_0^\epsilon\frac{dr}{r}.
\]

The overlap's local integrability holds. The source action needs its
boundary term or renormalization and admissible variations. A common
stationary action and its source response remain to be constructed.

## 5. Matrix averaging needs a transported family fibre

The stage-three result, line 44, says

> applied at every $(\tau, w)$ node

The implementation in lines 742–749 chooses one triple of Haar
unitaries per trial and passes those same matrices into the entire
quadrature. This checks a constant change of basis. Averaging
Hermitian matrices belonging to different mode spaces additionally
needs an identification of those fibres. The source supplies a Zak
dressing in the flat-twist coordinate, then adds the resulting
entries directly across `tau` in lines 685–718.

The distinction has an elementary algebraic certificate. Embed the
following positive matrices into three dimensions,

\[
 H_+=\begin{pmatrix}2&1\\1&2\end{pmatrix}\oplus(1),
 \quad D=\operatorname{diag}(1,-1,1),\quad H_-=D H_+D^\dagger.
\]

Averaging two copies of `H_+` gives eigenvalues `(3,1,1)`.
Changing the frame of the second fibre by `D` gives
`(H_++H_-)/2=diag(2,2,1)`. Both summands retain their individual
spectra. A common constant unitary would preserve the average's
spectrum in either construction, so the implemented Haar gate cannot
decide this issue.

A Berry connection, an explicit registered reference or another
derived comparison map could define the proposed average. Such a
connection must transform along with a node-dependent frame. The
report's parameter-free reading depends on earning that map.

Likewise the stage-two `R0` check, lines 504–519, compares singular-value
ratios and absolute mixing entries under `S`. It supports those sampled
observable identities. A full operator-valued modular intertwiner,
with its scalar/spin phases, group composition and source transport,
requires additional evidence.

## 6. The running example does not establish the stated exclusion

`relays/AGY_EXP_TO_CC_2026-11-15_X_FUNNEL_4_RESULTS.md`, line 42, says

> two-loop renormalization group running **cannot** generate opposite consecutive skew from an order-`5` boundary condition.

The deciding source, lines 1175–1185, evolves one order-five point at
one modulus with the boundary values in lines 1088–1093. Those values
include `alpha_U=1/42`, `Delta ln mu=-30`, largest up-sector Yukawa
`1/2`, largest other-sector Yukawas `1/50` and `lambda_UV=0`.
The saved outcome supports that example. Its universal wording
requires a bound covering the remaining allowed data.

The stated explanation does not supply such a bound. At one loop,
take coinciding nondegenerate diagonal down and lepton Yukawas at
the initial scale and let `H_u=diag(h1,h2,h3)`. The standard matrix
equations used by the campaign give

\[
 \frac d{dt}\log\frac{(d_i/d_j)}{(e_i/e_j)}
       =-\frac{3}{32\pi^2}(h_i-h_j),\qquad t=\log\mu.
\]

Gauge and common trace terms cancel from these within-sector ratios.
For a small infrared step, `h1>h2<h3` therefore gives opposite
consecutive skew. Choosing `H_u=diag(1/4,1/16,1)` suffices.
This counterexample concerns the inference from equal initial
singular values and the running law. Its membership in the campaign's
specific magnetic-overlap image has not been established here.
A theorem for that restricted image would need to control the up-sector
matrix elements in the down-sector eigenbasis over the full claimed
domain. The single computed example leaves that question open.

The order-fifteen example remains a conditional candidate. Its specified
torsion lift, modulus, initial normalizations and running interval need
their selection laws before they count as independent-input reductions.

## 7. The two-loop validation leaves noncommuting terms untested

The stage-four result, line 21, describes

> on diagonal $3 \times 3$ matrices

Its actual source benchmark, lines 583–593, specializes further to
three aligned rank-one matrices. The Haar control checks basis
covariance. Together these checks leave a known ambiguity.

For example a perturbation

\[
 \delta\beta_{Y_u}=\kappa[H_u,H_d]Y_u,\qquad
 \delta\beta_{Y_d}=\delta\beta_{Y_e}=0
\]

vanishes on every commuting diagonal input and respects the same
left/right unitary covariance. For real `kappa`, it changes a mixed
invariant when the Hermitian matrices fail to commute,

\[
 \delta\frac d{dt}\operatorname{Tr}(H_uH_d)
       =\kappa\operatorname{Tr}([H_u,H_d]^2).
\]

The right side is nonzero for noncommuting Hermitian inputs. Thus a
general noncommuting beta-function benchmark is still owed before
the tests establish the complete two-loop mixing evolution. This
finding identifies a coverage gap. It does not identify an incorrect
coefficient in the source's present beta function.

## 8. The written Zak unitary differs from the implemented one

The stage-two result, line 40, writes

> \delta_{k, l}\exp(2\pi i q_L b (k + 3a))

The implementation in `verify_x_funnel_2.py`, line 479, instead uses

\[
 (D_{\rm Zak})_{ii}
     =\exp[-2\pi i(q_Lb/3)(i+1/2)],\quad i=0,1,2.
\]

The stage-three and stage-four implementations retain this latter
formula. In the displayed integer generation indexing, the ratios
between successive entries are respectively `exp(2 pi i q_L b)`
and `exp(-2 pi i q_L b/3)`. At `q_L=1,b=2/5` these differ. An
overall scalar phase cannot reconcile them. The result note must
give the implemented unitary, or explicitly derive an alternative
index/basis convention and transport it through the calculation.
The saved calculations belong to the implemented convention.

## Positive derivations retained

### The order-five and order-fifteen arithmetic

Modulo five, `N=M+I` obeys `N^2=0` and has rank one. Its nonzero
kernel consists of the four vectors `(k,2k)`, with `k=1,2,3,4`.
For row vectors `w` on that line, `w M^-1=-w`. Multiplication
by `J^-1` takes `k` to `2k`, giving the claimed four-cycle.
The remaining twenty points have monodromy period ten. This proves
the claimed `4+10+10` decomposition.

The decomposition `E[15]=E[5] direct-sum E[3]` gives `24*8=192`
points of exact order fifteen. For numerator vector `p`, the
projections are `w5=2p/5`, `w3=-p/3` modulo the lattice. A flat
character with charge divisible by three is unchanged up to its
bundle identification by adding `w3`. This proves the arithmetic
behind the third sector's blindness. Its norm and interaction
statements retain the corresponding unitary transport premises.

### The determinant product

For flat unit-area torus Laplacians let `zeta_w(s)` denote their
spectral zeta functions, with the zero mode omitted at `w=0`.
Regrouping the lattice gives

\[
 \sum_{w\in E[N]}\zeta_w(s)=N^{2s}\zeta_0(s),\qquad
 \sum_{w\ne0}\zeta_w(s)=(N^{2s}-1)\zeta_0(s).
\]

Since `zeta_0(0)=-1`, differentiation at zero yields

\[
 \sum_{w\ne0}\log\det\Delta_w=2\log N.
\]

Multiplication by a charge coprime to `N` permutes the summands.
This gives stage three's `2 log 5` cancellation under its flat
spectral hypotheses, including the independence from `tau`.

### The rational cusp coefficients

Bernoulli multiplication gives
`sum_{k=0}^{N-1} B6(k/N)=N^-5 B6(0)`.
On the 24 nonzero five-torsion points this implies

\[
 \frac{1}{24}\sum_{w\in P_5}\frac{B_6(a_w)}{B_6(0)}
       =\frac{5^{-4}-1}{24}=-\frac{26}{625}.
\]

On the four-point eigenline the corresponding mean is
`(5^-5-1)/4=-781/3125`. With the supplied flat multiplet weights
`24+4-90`, the two effective coefficients are therefore exactly

\[
 24-86(-26/625)=17236/625,\qquad
 24-86(-781/3125)=142166/3125.
\]

These algebraic values hold for the defined flat Epstein sum. They
remain available as recovery controls when the magnetic determinant
is constructed.

## Consequential follow-up

1. Correct the monodromy modulo three, the measure name and the Zak
   formula. Retain both monodromy orbits and the larger root action.
2. Specify the magnetic fermion and scalar operators, the source/end
   law and domains in one action. Derive its determinant and boundary
   response using that same background.
3. Earn the transport used to average mode-space operators. Include
   the modulus-dependent frame and its connection in the covariance
   check, together with spin and central phases.
4. Derive the magnetic degree and the order-fifteen selection. Record
   the remaining modulus, ultraviolet data and running interval as
   explicit choices until their equations determine them.
5. Narrow the running exclusion to the demonstrated case and add an
   independently sourced noncommuting matrix benchmark for future
   mixing calculations.

The campaign has produced conditional constructions worth retaining.
The ledger of independent physical inputs still needs the derivations
above. Held-out parameter comparisons performed in this review number
zero.
