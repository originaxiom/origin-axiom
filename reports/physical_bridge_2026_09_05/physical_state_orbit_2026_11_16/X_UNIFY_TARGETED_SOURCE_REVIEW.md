# Targeted source review of the newly fetched X-UNIFY campaign

2026-11-16. Reviewed remote head 645964e59 on the loop branch. All four
result relays were read. The deciding routines for the CRT generators,
anomaly polynomial, claimed CS/strong-CP branch and closure matrix were
personally inspected. This is a source/hand-algebra review, not a complete
review of the four roughly ten-thousand-line combined verifiers. No
upstream scientific code was imported, collected or executed here.

## 1. Preserve the genuine conditional positives

The CRT coordinate x=3u+5v modulo 15 is bijective. Direct expansion gives

    x^2/15 = 3u^2/5+5v^2/3+2uv,

and the analogous bilinear formula has integral cross terms. Thus both
the displayed chirp and Fourier matrix factor under that permutation,
with multipliers 3 modulo 5 and 2 modulo 3. This is a real finite tensor
factorization. It separates two coefficient factors without identifying
either with physical colour or generations.

The supplied chiral Lambda-even(3_a plus 2_b) multiplets have cubic
charge sum

    3(2a)^3+6(a+b)^3+(2b)^3
      +3(2a+2b)^3+2(3a+b)^3
      =4(3a+2b)((3a+b)^2+4b^2).

This expansion is correct. The real nonzero anomaly-free charge ray
therefore has 3a+2b=0. A primitive integer generator has the familiar
(-2,3) charges up to overall orientation. The chosen chiral exterior
prescription, gauge interpretation, charge unit and full physical
operator remain premises of that result.

The campaign also keeps the parity-allowed pi branch as a rejecting
control, negative determinant signs, and alternative Majorana metrics.
Its conservation argument for the determinant phase has a sound
conditional core when the displayed RGE traces are real. A complete
verification of that RGE transcription and its UV premises is separate.
No numerical RGE or corridor range is newly certified by this review.

## 2. The displayed generators need a modular-normalization repair

Stage 1 build_weil_generators_mp, lines 86-96, uses, for odd N and
invertible r,

    T_xx=exp(2pi i r x^2/N),
    S_xy=N^-1/2 exp(-2pi i r xy/N).

The CRT identities above hold for those matrices. Interpreting this
pair as the standard modular S,T requires a separate relation check.
There is an exact Heisenberg control that the displayed pair fails.
Put X|x>=|x+1>, Z|x>=exp(2pi i r x/N)|x>. Up to central scalars,

    S X S^-1=Z^-1, S Z S^-1=X,
    T X T^-1=X Z^2, T Z T^-1=Z.

On the exponent pair (X power,Z power), their induced matrices are

    S0=[[0,1],[-1,0]], T0=[[1,0],[2,1]],
    S0 T0=[[2,1],[-1,0]]=I+N0, N0^2=0.

Consequently (S0 T0)^3=[[4,3],[-3,-2]], whereas S0^2=-I.
Already modulo 5 these differ. The difference is in the noncentral
Heisenberg action, so a common projective scalar cannot fix it. The
source pair does not obey (ST)^3=S^2 even projectively as the usual
modular generators. It can instead be typed as Fourier and doubled
shear operations. That is a different generator assignment.

For the standard modular assignment, one repair is to replace the
quadratic coefficient r by r*inverse(2) modulo N while retaining this
Fourier kernel. Another is to use the matching 2r bilinear Fourier
kernel for the existing quadratic form and rederive conventions and
phases. CRT still works after consistent repair. All claimed Weil,
modular, inversion and gauge/family identifications should be checked
with the repaired relations and central lift. This finding does not
invalidate the finite CRT identity or the anomaly expansion.

## 3. The current CS diagnostic cannot select the YM theta branch

Stage 2 run_part_2b_amphichiral_cs_and_3family_dparity, lines 2026-2035,
defines

    vol_L=D(z1)+D(z2),
    vol_R=-(D(conj(z1))+D(conj(z2))),
    lr_vol_diff=abs(vol_L-vol_R),

where D is the Bloch-Wigner function. Since D(conj(z))=-D(z), this
volume difference vanishes identically for any admissible pair of
shapes. It is not a discriminator of amphichirality. The expression
named cs_plebanski_asymmetry adds holonomy trace residuals, without
evaluating a flattened complex-CS invariant or a four-dimensional
gauge theta term. Computing complete regular shapes does not repair
that observable map.

More directly, line 2115 assigns theta_ym_zero_branch=0 and then tests
the determinant evolution from that chosen branch. The pi control
shows that parity also admits pi. It does not derive rejection of pi
from the parent action. The claimed 7D reduction requires its actual
topological coupling, normalization, allowed bare term, global phase
and branch prescription. No such map is derived by this routine.

This finding leaves the existing geometric CS(m004)=0 fact intact.
It stops the inference from that geometric fact to a selected physical
theta_YM=0 branch. Conditional phase conservation after specifying
theta and the UV determinant sign is still a useful positive.

## 4. The closure matrix overstates its witnesses' scope

Stage 4 run_part_4b_and_4c_master_closure_and_suite, lines 3063-3134,
assigns seven subsystems to I_Unconditionally_Derived. Its M03 row
names all twelve P-C3 methods while the local row witness computes a
two-by-two quaternion commutator norm and a scalar collar inequality.
Stage 1 separately implements analogues of twelve finite controls,
but neither set proves the physical field/domain or index join.

The M01 witness computes Smith invariants of M^4-I. Those are genuine
integer algebra. Interpreting the cokernel as the stated topological
cohomology additionally uses the mapping-torus model. The M02 exterior
matter prescription, M04 supplied gauge/RGE model, M06 theta branch,
and M07 scalar mass functional also retain their own supplied premises.
The numerical witness fields cannot erase those dependencies. M09
itself correctly leaves a physical domain/index duty conditional.

The requested correction is to distinguish algebraic identities inside
a stated model, model-conditioned outputs and foundational derivations.
Preserve the new computations and their controls. Keep the unseen
physical maps and action choices visible rather than placing their
downstream consequences in an unconditional column.

The M10 row also states an "iff" for parity-preserving heavy decoupling.
The two displayed phase examples cannot establish that necessity. At
the matrix level take H=I, L=I, B=i b I, C=i c I with b,c>0. This
heavy-light block is not Hermitian and violates C=B^dagger, while its
Schur light mass is L-B H^-1 C=(1+bc)I. Both its light determinant and
the full determinant are positive real. Thus an asymmetric complex
mixing need not generate a determinant phase. A parity condition can
give a sufficient protective mechanism under specified hypotheses.
An individual counterexample with nonzero phase does not prove an iff.
This control is matrix algebra, without a claim to realize these
matrices in the Origin Axiom parent.

## 5. An orthonormal frame still needs a physical coefficient vector

Stage 2 lines 1893-1905 correctly computes G_Pet^-1/2 and verifies
its orthonormality. It then defines c_lowdin_raw=np.sum(g_inv_sqrt,axis=1).
This last operation is G_Pet^-1/2 applied to the vector (1,1,1).
The comment calls it an isotropic heavy-singlet sum. The metric alone
does not supply that nonzero vector.

The elementary control is G=I. Every orthonormal frame has this same
metric. Its all-ones sum changes under an allowed frame rotation.
More generally an isotropic Hermitian metric is invariant under U3,
whose defining representation has no nonzero fixed vector. A chosen
coefficient vector can come from an action, source, state or marked
interaction. It cannot be deduced from metric isotropy alone. Transport
of a previously supplied vector through a change of frame is valid,
but retains the original vector as input.

The four prescriptions and their different results are useful controlled
sensitivity calculations. They also demonstrate why the coefficient
selection matters. Even a same-action derivation of G_Pet leaves the
vector/direction duty unless that action derives the appropriate source
or interaction as well. Preserve the row-sum prescription as an explicit
candidate. Do not count its two relative weights as physically eliminated
merely by calling its kinetic frame isotropic.

## 6. Effect on this seat's next task

The new campaign offers an independent finite-algebra comparison for
P-C3 and a useful coefficient-factorization control. It does not execute
this seat's sealed checker or provide exact main acceptance. Its fresh
physical-CS and unconditional-closure claims cannot fill the outstanding
state, field/domain, chiral-spectrum or end-selection maps.

Continue the physical action/operator task, preserve the same-action
spin vertex and complete complementary fields, and ask the source
author and SM verification lane to check the exact source issues
above. This is a scoped correction to particular claims and routines,
not a verdict on every calculation in the campaign.
