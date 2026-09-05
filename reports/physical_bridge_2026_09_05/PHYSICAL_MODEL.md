# A conditional physical calculation built on the banked 27

2026-09-05; baseline `f06d3405`. R1/R2 were designed before execution.
R3 was explicitly designed after seeing R1/R2; see EXTENSION_1.md.

## 1. What crosses from algebra into physics here

The repository already contains the branching `27 = 16 + 10 + 1`, the exotic
triplet/doublet charges, and the invariant cubic. This work does not rediscover
them. Sources opened: B884's FINDINGS, B970's original scout and WORK, B1148's
certificates, and B1150's FINDINGS. The new calculation gives the declared
spectrum physical statistics, kinetic terms, explicit masses and RG equations.
These are **imports**, not consequences of a dimension count or a group name.

Choose a four-dimensional Lorentzian spin spacetime, conventional local QFT,
canonical positive kinetic normalization, and `hbar=c=1`. Below a matching
scale, take three SM chiral families (with neutral sterile singlets), one complex
Higgs doublet, and n vectorlike pairs of each type:

| left-handed Weyl field | SU(3), SU(2), Y | multiplicity per copy |
|---|---|---|
| D | (3,1,-1/3) | 1 |
| Dbar | (3bar,1,+1/3) | 1 |
| Lextra | (1,2,-1/2) | 1 |
| Lbar | (1,2,+1/2) | 1 |

The two doublets are **fermions** here; the letter H used for their gauge
representations in some banked branching tables does not make them scalars.
The light scalar Higgs is a separate field. Neutral singlets do not affect the
one-loop gauge coefficients. Three families and n copies are chosen inputs.

A renormalizable effective Lagrangian realizing this content is

```text
L = -1/4 sum_i F_i^a(mu,nu) F_i^a(mu,nu)
    + i sum_f f† bar-sigma^mu D_mu f + (D_mu H)† D^mu H - V(H)
    - [SM Yukawa terms + D M_D Dbar + epsilon_ab Lextra^a M_L Lbar^b + h.c.].
```

The displayed gauge terms use canonical gauge fields; the couplings appear in
`D_mu = partial_mu - i g3 T·G_mu - i g2 t·W_mu - i gY Y B_mu`.
Choose a bounded Higgs potential, for example `V=-m_H^2 H†H+lambda(H†H)^2`
with `lambda>0`. Its parameters, the SM Yukawa matrices, and `M_D,M_L` remain
inputs. The new calculation neither selects a vacuum nor derives those matrices.
Bare masses are allowed in this **broken-phase SM effective theory**, not in
an unbroken single-27 E6 theory; the latter needs the mass-generating VEV.

Additional exotic interactions are set to zero in the mass-running check.
Their absence, possible protecting symmetries, exotic decays, and matching to
an E6 scalar potential require separate model building. Anomaly cancellation
and gauge-coupling meeting alone do **not** establish phenomenological viability.

## 2. Representation-to-running interface

Conventions: `Q=T3+Y`, `alpha1=(5/3) alphaY`, `x_i=1/alpha_i`,
`t=log(mu/MZ)`, index order `(1,2,3)`.

```text
b_i = -11 C2(G_i)/3 + 2 sum_Weyl T_i/3 + sum_complex_scalar T_i/3
dx_i/dt = -b_i/(2*pi)                       (one loop)
```

These standard QFT coefficients and threshold conventions were checked against
[Bhattacherjee et al., Eqs. (2.1)–(2.6)](https://doi.org/10.1007/JHEP05(2018)090).
Their b has the opposite sign convention. The rational representation indices
are recomputed in `spectrum.py`, including spectator multiplicities, rather
than assigning the desired beta coefficients to labels.

| spectrum contribution | b1 | b2 | b3 |
|---|---:|---:|---:|
| three SM families + one complex Higgs | 41/10 | -19/6 | -7 |
| D + Dbar, one copy | 4/15 | 0 | 2/3 |
| Lextra + Lbar, one copy | 2/5 | 2/3 | 0 |
| complete equal-threshold pair | 2/3 | 2/3 | 2/3 |

The perturbative SU(3)^3, SU(3)^2Y, SU(2)^2Y, Y^3 and mixed gravitational-Y
anomalies vanish; so does the ordinary SU(2) mod-two obstruction on a spin
spacetime. Tests include a deliberately anomalous spectrum, an isolated weak
doublet, scalar-versus-fermion counting, higher-representation indices and
hypercharge rescaling. This is not a classification of all possible global
anomalies on other spacetime structures or group quotients.

For explicit thresholds, the leading-log equation is

```text
x_i(MU) = x_i(MZ) - b_i tU/(2*pi)
          - sum_a delta_b_i(a) log(MU/M_a)/(2*pi).
```

The piecewise implementation and the direct formula agree to about `7.1e-15`
in the fitted examples. Equal-threshold complete multiplets shift all three
inverse couplings equally: they cannot change **one-loop coupling differences**.
This statement says nothing about an intermediate gauge group, a different
spectrum, unequal physical thresholds, or higher-order matching.

## 3. A mass requirement, not a prediction

Use all three values from **B915's historical numerical fixture**:
`1/alpha_em=127.951`, `sin²theta=0.23122`, `alpha_s=0.1180`, with
`MZ=91.1876 GeV`. This is an audit of an already-exposed target, not a new
measurement, a check of current world averages, or an out-of-sample success.

Let `r = sum_a log(M_L,a/M_D,a)`. Since `delta_b_D+delta_b_L` is common to
all gauge factors, subtracting the matching equations gives exactly

```text
2*pi (x1-x2) = (b1-b2) tU + (delta_b_D1-delta_b_D2) r
2*pi (x2-x3) = (b2-b3) tU + (delta_b_D2-delta_b_D3) r.
```

The two-by-two inverse problem yields

```text
tU = 27.0455236403
MU = 5.0775880435e13 GeV
sum log(M_D/M_L) = 43.4476952316.
```

Equivalently, a mechanism must supply the product of triplet-to-doublet
threshold mass ratios whose logarithm is 43.4476952316. For flavor matrices
this involves products of singular values, not signs of matrix eigenvalues.

For the **whole range** `MZ <= M_a <= MU`, feasibility requires and, at this
order, permits `|r| <= n*tU`. Thus one copy cannot do it; two and three can.
An explicit positive witness chooses equal splitting per copy and the
otherwise-free common geometric mean at the logarithmic midpoint:

| copies | M_D (GeV) | M_L (GeV) | common inverse UV coupling |
|---|---:|---:|---:|
| 2 | 3.5487074e12 | 1.3047372e3 | 38.0409303 |
| 3 | 9.4982954e10 | 4.8746964e4 | 36.6061207 |

These are **illustrative fitted masses**. The common mass placement is not
determined by the two differences. The meeting scale is likewise inferred
from the target under the chosen spectrum; it is not independently emitted
by the mathematical program. No proton lifetime or collider viability is
claimed for these examples.

## 4. Do not confuse equal UV masses with equal thresholds

B884's cubic contains `1·10·10`, and B970 already identifies S as the
single-27 VEV direction giving the exotic sector mass. At an SU(5)-symmetric
boundary, that contribution acts identically on the triplet and doublet
blocks, with canonical kinetic normalization.

R3 verifies the finite-dimensional part directly: the commutant of all 24
fundamental SU(5) generators is one-dimensional, spanned by `I5`. The SM
subalgebra's commutant is two-dimensional, spanned by `diag(I3,0)` and
`diag(0,I2)`. With several families, a common flavor matrix tensors with
`I5`; this argument does not force degenerate masses **between families**.

Running can split an initially common triplet/doublet mass. We include that
escape using the gauge part of the one-loop mass equation:

```text
d log m/dt = -6 sum_i C_i alpha_i/(4*pi)
C(D) = (1/15, 0, 4/3); C(L) = (3/20, 3/4, 0).
```

The imported equation follows from the mass-matrix anticommutator in
[Luo, Wang and Xiao, Eq. (62)](https://arxiv.org/pdf/hep-ph/0211440).
The decoupling masses obey `M=m(M)` at this leading-log order.
No finite pole-mass matching or exotic Yukawa terms are included.

An exhaustive bound replaces a scan over convenient common masses. For at
most three copies, color remains asymptotically free, so
`alpha3(t) <= alpha3(MZ)`. The maximum abelian beta coefficient is
`41/10+2*n/3`, which bounds `alpha1` throughout the interval. Positivity of
the doublet enhancement then bounds the splitting generated from equal UV
singular values:

```text
log(MD/ML) = integral_gamma_D - integral_gamma_L
           <= tU * [(2/5) alpha1_max + 8 alpha3(MZ)]/(4*pi).
```

| copies | upper bound on sum log(M_D/M_L) | required by matching |
|---|---:|---:|
| 1 | 2.0540499 | 43.4476952 |
| 2 | 4.1117013 | 43.4476952 |
| 3 | 6.1739004 | 43.4476952 |

Therefore **a common UV mass plus gauge-only one-loop running is insufficient
in this specific effective theory**. This is not a no-go for the singlet VEV
in a theory with other interactions or thresholds. The analytic integrals and
independent numerical quadrature agree within `2.3e-16` in the examples.
The three-copy witness would still require a UV log mass ratio about
`14.6074207` per equal copy; gauge running does not explain its hierarchy.

## 5. The next physical task

Construct mass matrices from a specified breaking sector and its actual
invariant tensors, without choosing their singular values to hit §3. Start
with the already-banked S coupling and explicitly priced departures: additional
VEVs/representations, mixing with the second 5bar in the 27, or an intermediate
gauge phase. Check the vacuum, remaining gauge factors, chirality, kinetic
normalization and exotic decays, then compute the thresholds it really emits.

A useful acceptance criterion is: **the mechanism gives the determinant ratio
and a consistent spectrum from a stated finite input budget, and predicts a
separate observable or relation not used to set that budget**. Failure of one
specified mechanism leaves the others open. Success of the inverse fit alone
does not meet that criterion.

For a primary model-building comparator, not an adopted solution, Babu, Bajc
and Susič explicitly specify a `650+351'+27` scalar sector and study several
E6 intermediate stages. Their work illustrates the additional dynamical
content hidden by a subgroup diagram; it does not show those scalar choices
are forced by this repository. [JHEP 06 (2024) 018](https://doi.org/10.1007/JHEP06(2024)018).

Gravity, the physical Lorentz-spin identification, a continuum limit, SM flavor,
neutrino parameters and cosmology are **not delivered by this effective model**.
Their existing repository results and open identifications remain in scope for
the larger program, not silently replaced by this one gauge-sector calculation.

## 6. R4 continuation: test the proposed action, not only a mass ansatz

[VACUUM_MODEL.md](VACUUM_MODEL.md) now constructs an explicit positive,
renormalizable classical E6 scalar potential, a global minimum with the SM
gauge algebra, the exact mixed singlet-VEV fermion mass matrix, and the full
186-coordinate scalar Hessian. Its 77 zero modes consist of 66 gauge modes
and eleven additional real adjoint modes. No massless physical Higgs doublet
remains at that representative vacuum. All those consequences are retained.

That model therefore **does not have the effective spectrum assumed in §1**.
Its extra scalar/Yukawa interactions also lie outside R3's gauge-only running
bound. Do not apply §3's fitted threshold requirement as if it were a test of
all of R4. The next step is vacuum selection, scalar lifting and the light
doublet, followed by matching the actual spectrum. No original result is erased.
