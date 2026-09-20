# F04: the controlled-growth constraint reaches the full rank-four bundle

2026-09-20. **The induced-rank-two restriction can be removed.** The actual
nonsplit coefficient bundle admits a direct flag argument for arbitrary
positive Hermitian rank-four metrics, including metrics outside the
symmetric-cube image. A hypothetical smooth source-free global harmonic
metric still has to develop exponentially large angular variation of its
root scales along the cusp.

This is a precisely scoped mathematical constraint, not a physical
realization, universal exclusion, or retraction of the exact algebraic
index I(V)=1. The unrestricted rapidly angle-varying case and coupled
source equations remain open. The full TOE goal is not achieved.

[Preregistered design](DESIGN.md), [complete argument](PROOF.md),
[exact tests](test_verify.py), [execution receipt](RECHECKS.md).
Design, proof and controls were sealed at `9d366599` before first execution.
**20 new controls passed; 42 unchanged antecedent controls passed.** All
19 checked seal entries match. The infinite-domain conclusion rests on the
authored argument, not on finite test counts or an independent expert review.

## Why this addresses a real gap

F03 explicitly did not decide arbitrary metrics on V=Sym^3(rho) tensor chi.
An induced rank-two metric occupies only part of the rank-four metric space.
F04 uses instead the full Cholesky factorization

    H=N^dagger diag(exp(t_1),...,exp(t_4))N,  sum t_i=0,

with all six complex entries of upper-unitriangular N free. These are all
15 real determinant-one metric degrees of freedom. An arbitrary central
factor is removed using the harmonic equation, not by imposing a new
finite-energy or constant-determinant assumption.

The representation itself fixes a full invariant flag, and the modulus-one
diagonal characters make its three heights b_r=sum_(i<=r)t_i global.
The full metric equations imply

    Delta b_r=sum_(i<=r<j) exp(t_i-t_j)|(dN N^-1)_ij|^2 >=0.

The regular unipotent peripheral action supplies nonzero additive periods
for each simple root. Extra mixing coordinates contribute nonnegative
terms; they do not cancel these fluxes. This is why the argument can be
made directly in the full bundle.

## The precise result

Use the complete one-cusped hyperbolic metric dr^2+exp(-2r)h0, without a
finite-distance boundary or source. Define

- L=sum_r average_T b_r;
- h_i=t_i-t_(i+1), Omega_i=average_T h_i-min_T h_i;
- W=(3/2)Omega_1+2 Omega_2+(3/2)Omega_3;
- K=|d(x1-x2)|^2_(h0)>0 and reference torus area A0.

The flag flux makes L eventually positive and bounds it below by
Q0 exp(2r)/(2A0), up to a constant, for positive integrated flag density
Q0 on any fixed sufficiently large compact truncation. The A3 Cartan
weights give the coupled inequality

    L''-2L' >=10K exp(2r+(L-W)/5).

If W/L stayed strictly below one, an elementary exponential-ODE comparison
would force blow-up at finite proper distance. Consequently every
hypothetical global harmonic metric must satisfy

    limsup W/L >=1,
    limsup exp(-2r)W >=Q0/(2A0)>0.

In particular, W=o(exp(2r)) is excluded. Bounded or polynomial angular
variation is insufficient, even with infinite total harmonic energy.
These are necessary conditions along a sequence, not a solution or a
uniform statement on every high torus. The proof also gives a corresponding
at-least-exp(3r) subsequential lower growth bound on the metric derivative,
in its stated trace-metric normalization. Physical backreaction has not
been calculated from that bound.

## Positives and contrary controls preserved

1. The exact local harmonic cusp still solves the FULL rank-four matrix
   equation. Its outer flux is negative and its inner-boundary flux is
   essential. It is not discarded for failing a global condition it never
   claimed to satisfy.
2. The metric test includes generic Cholesky data violating induced
   rank-two scale ratios. It also distinguishes the correct right form
   dN N^-1 from the incorrect left form N^-1dN.
3. With zero peripheral translation, a local diagonal metric has infinite
   radial growth and zero harmonic residual. The obstruction does not
   follow from rank alone.
4. F03's smooth weighted-energy counterexample passes unchanged. It blocks
   the tempting invalid step of using the mean in place of the minimum.
   Therefore F04 does not erase the angular loophole by averaging.
5. The algebraic I(V)=1, its dual behavior, and the distinction from the
   semisimplification remain the existing exact R27 result. This checkpoint
   rechecks the representation, not the entire cohomology computation.

## Physical consequence and work order

The uncertainty has become more specific, not disappeared. Moving to a
general rank-four metric with controlled angular scales does not by itself
solve the source-free global background problem. The remaining options are
to analyze the necessary rapidly angle-varying class under the declared
physical action, or derive a compensating representation-valued current
from the coupled parent equations. Neither option has been constructed here.

F02 still prevents equating infinite background map energy with an undefined
fermion operator or with infinite residual-square static potential. Before
calling the remaining growth physically inadmissible, the action, allowed
end data, boundary variation law and backreaction must say so. A relative
topological index cannot substitute for the same background's normalizable
charged spectrum and its resolved-core partners.

The next useful join is therefore not another cohomology census or an
arbitrarily chosen cusp domain. It is the background/source equation in one
specified parent theory, followed by its actual L2 spectrum, anomaly and
interaction tests. Existing R28/R29/R38 work must be reused with its supplied
parameters and limitations stated. No unsealed R39 draft was executed.

## Literature boundary

Wu--Zhang's general harmonic-metric equivalence still assumes a compact
base; its generality about connections does not settle this noncompact
case. The accessible introduction/main statement was checked, not the
whole paper. [Primary publisher text](https://www.sciencedirect.com/science/article/pii/S0001870826000216).
Collins--Jacob--Yau's Poisson-metric work addresses punctured curves with
parabolic data. Only its abstract was read in this check, and no theorem
from it supplies a three-dimensional existence or exclusion claim here.
[Primary abstract](https://arxiv.org/abs/1403.7825).

The matrix decomposition, variational argument and ODE comparison above are
written out rather than attributed to a literature result with unchecked
hypotheses. No claim of mathematical novelty follows from the repository
searches. This remains a local checkpoint, not a completed banking pass.
