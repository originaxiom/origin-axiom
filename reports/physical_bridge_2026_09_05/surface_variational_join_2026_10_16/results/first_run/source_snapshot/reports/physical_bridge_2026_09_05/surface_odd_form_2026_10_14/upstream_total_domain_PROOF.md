# A total selfadjoint realization with the prescribed puncture trace

This is an authored analytic construction for the existing metric and coefficient, not an independent specialist certificate or a physical index theorem. Let X be the smooth universal punctured elliptic family on the stated lifted modular quotient, with the semi-flat metric of total_metric_dirac. All actual flat unitary coefficient and spin transitions are retained. Fix a smooth compatible subbundle Lambda in the positive vertical critical trace, with its complementary negative trace. In particular, the previously used extreme subbundles satisfy this compatibility. This proof does not derive which Lambda or global spin structure is physical.

## The normal operator includes the horizontal symbol

At a point of the marked section choose oriented orthonormal horizontal and normal coordinates. Rotate the normal spin frame and multiply the spinor by r^(1/2), as in puncture_fredholm. The coefficient holonomy is -I6, so the resulting angular functions are periodic. With the same four Clifford matrices as total_metric_dirac the angular-m normal operator is

    N_m(xi)=V_m+M_xi,
    V_m=c3 partial_r+i m c4/r,
    M_xi=i(xi1 c1+xi2 c2).

Here m is any integer and xi is a horizontal covector in orthonormal units. M is Hermitian, M^2=|xi|^2 and it anticommutes with V_m. The coefficients of the full metric which were not displayed are lower order in the section normal limit, not omitted from the actual operator. The mixed spin term from total_metric_dirac is locally bounded and is kept in the perturbation below. A cusp-line connection, when globally defined as already specified, is also smooth and locally bounded at each finite-height section point.

Only m=0 lies in the critical strip. Its trace space is C2_horizontal tensor (C6_vertical_plus direct-sum C6_vertical_minus). Write P_Lambda for its orthogonal coefficient projector and

    P=I_horizontal tensor (p_plus tensor P_Lambda
                         +p_minus tensor (I-P_Lambda)).

This has rank12 in the rank24 trace space. c3 maps its image onto its orthogonal complement, so it is a maximal isotropic plane for the Green form. M_xi preserves it. The full total chirality preserves it too. The horizontal spin factor is essential; imposing an extra half-spin projection is not part of this domain.

## The entire frozen normal family is invertible away from zero covector

On the radial half-line, the m=0 operator V_0 with this trace plane is selfadjoint: its endpoint Green form has precisely this annihilator, and infinity is limit point. For m not zero the roots are plus and minus m; the singular branch is not square integrable in dr. The endpoint is limit point and the minimal closure is the unique selfadjoint realization. This can also be read from the one-dimensional first-order system: at each sign of a nonreal spectral parameter, exactly half the local solutions are integrable at each limit-point endpoint. Smooth compact radial cutoffs and the admitted constant m=0 traces give a core. Summing these angular realizations gives V with the prescribed critical trace.

Since M is bounded on each fixed-xi radial Hilbert space and preserves this domain, N(xi)=V+M is selfadjoint on Dom(V). Anticommutation holds on that domain, not only on formal expressions. Integration by parts therefore gives

    ||N(xi)h||^2=||V h||^2+|xi|^2 ||h||^2.

Consequently every nonzero xi has an onto inverse with norm at most1/|xi|. Surjectivity uses selfadjointness and closed range, not just absence of a nullvector. This includes every angular mode; it is not an m=0-only spectral assertion. Dilation r->r/|xi| gives the same normalized family on the unit covector circle.

For the trace test one can see the complementing condition directly. Let Q=c3 M_xi/|xi|. Then Q is a Hermitian involution and the decaying critical Cauchy space has projector C=(I-Q)/2. Since Q exchanges im(P) and ker(P),

    P C P=P/2,
    (I-P) C (I-P)=(I-P)/2.

Hence the forbidden-trace map I-P restricts to an isomorphism on the decaying Cauchy space. This is the local elliptic boundary-symbol condition, with a uniform angle, for EVERY coefficient subspace Lambda. The finite rank samples in the verifier are not the proof of that quantifier.

The distinction from Green isotropy is real. At one fixed nonzero xi0, choose instead the allowed plane im C(xi0). It is maximal Green-isotropic and total-chirality invariant, but exp(-|xi0|r)h with h in that plane is a nonzero square-integrable normal zero solution. It fails the elliptic condition. This is a local countercontrol, not an assertion that such a plane is compatible with the full physical theory or the earlier vertical grading.

## Derivative control makes freezing legitimate

Squaring V_m in the normalized density gives

    V_m^2=-partial_r^2+(m^2-m GammaV)/r^2,
    GammaV=i c3 c4.

The two coefficients are m(m-1) and m(m+1), nonnegative for integer m. On noncritical modes their boundary terms vanish. For the critical mode there is no inverse-square potential. Integration by parts on the core, followed by graph closure, controls the radial derivative. The one-dimensional Hardy inequality ||h/r||<=2||partial_r h|| on zero-trace components controls the cases |m|=1 where one potential vanishes. For |m|>=2 the potentials themselves control m h/r; m=0 has no angular derivative. Thus a constant independent of m bounds

    ||partial_r h||+||r^-1 partial_theta h||
        <= C (||V h||+||h||)

locally, with the harmless last term accommodating radial cutoffs. Fourier integration of the normal-family identity also controls both horizontal derivatives. These estimates address the full angular complement, not only the critical trace.

On a compact base chart the metric is smooth and nondegenerate across the section, with normal cone angle2pi. In smooth tubular normal coordinates its coefficients agree at the section with the frozen product coefficients; the normal discrepancy is O(r). After the same spin and density normalization, the discrepancy is bounded by epsilon times the model derivatives plus a bounded zeroth-order term, on a sufficiently small chart. Terms O(r) multiplying r^-1 angular derivatives obey that bound. The spin rotation's derivative multiplies the O(r) discrepancy by1/r and is bounded. Smooth base variation is made small by shrinking the base chart. No bound uniform at the modular cusp is claimed here.

A smooth coefficient-unitary transformation locally makes Lambda constant. It commutes with Clifford multiplication and adds only bounded local zeroth-order coefficients. Changes of critical coordinates have the minimal-domain correction proved in fibre_family; they preserve the actual trace plane. Normalize the remaining smooth density unitarily. Both the model and actual expression are then symmetric on the same local core. Extend their small coefficient difference smoothly to zero outside that chart on the auxiliary full model; use the symmetrized first-order expression so this extension remains symmetric. The derivative estimates give relative bound less than one. Kato--Rellich then gives a selfadjoint auxiliary operator on the model domain, with the same core and equivalent graph norms. Its hypotheses and elementary resolvent proof are stated in [Simon, Theorem7.3](https://link.springer.com/article/10.1007/s13373-018-0118-0).

This also supplies local adjoint regularity without assuming a global compact theorem: if u belongs to the adjoint of the actual core, multiply it by a smaller cutoff. Test against the auxiliary core; the cutoff test lies in the actual core, and the commutator is bounded. The localized u therefore belongs to the auxiliary adjoint domain, equal to its selfadjoint domain. Approximate there by core sections and cut off once more. It follows that the localized u belongs to the actual graph closure with the prescribed trace. Ordinary interior charts use the same freezing argument without the radial singularity. Finite orbifold charts are handled equivariantly; restricting an invariant selfadjoint realization to the finite-group invariant Hilbert space preserves selfadjointness.

The abstract boundary-symbol terminology agrees with Mazzeo--Vertman Definition3.2 and Corollary7.4, but their compact theorem is not simply applied to this noncompact total space. Likewise the geometric Witt theorem of Albin--Gell-Redman cannot supply the conclusion: its link gap excludes zero, whereas our actual combined spin/gauge angular link has zero. The prescribed trace, normal-family estimate and localization above do the work here.

## The complete modular cusp requires no additional selfadjoint parameter

Let C_Lambda be the dense core of sections supported over compact base subsets, smooth away from the section and with the local graph-core behavior just constructed. Keep all prescribed global transitions and the actual differential expression. Its operator D0 is symmetric and grading invariant. This is larger than compact support away from the removed section; it already contains the chosen critical traces.

On a modular cusp t=log y satisfies |dt|=1/ell for the full metric, not just its base restriction. Choose scalar cutoffs chi_R on the base, equal to1 on an exhausting compact set and zero above a larger height, with |d chi_R|<=C/(ell R). Extend over the compact core and pull back to X. They preserve Lambda and all coefficient transitions. Their support is compact in the base, while their behavior at the finite-distance section is governed by the existing trace domain. The fibre collapse at t->infinity does not change this gradient estimate.

For u in a deficiency space, D0* u=plus or minus i u, local adjoint regularity shows chi_R u belongs to the graph closure of D0. Formal symmetry there and [D,chi_R]=c(d chi_R) give

    ||chi_R u||^2 <= ||[D,chi_R]u|| ||chi_R u||,
    ||chi_R u|| <= C ||u||/(ell R).

Let R tend to infinity. Dominated convergence gives u=0. Both deficiency spaces vanish, so D0 is essentially selfadjoint. Its closure is the total selfadjoint realization for the specified puncture law, metric, coefficient and spin. This proof allows the cusp degeneration because it never assumes a uniform vertical gap. A bounded or locally bounded symmetric connection term does not change the commutator argument, provided it is included in the local expression and its admitted global bundle is fixed.

There is therefore no further independent selfadjoint extension at the infinitely distant modular cusp in this fixed Hilbert problem. This is NOT uniqueness before Lambda is chosen and is NOT essential selfadjointness of the smaller domain which excludes all section traces. Changing the cusp line, its Hermitian metric/connection or an end source can change the problem; the argument does not select its integer or exclude those physically distinct choices.

## What this closes and what it leaves

The prescribed graded puncture family admits the full horizontal normal operator and a global total selfadjoint closure for the existing metric. That is stronger than a family of separate fibre operators. The analytical argument is authored; the tests verify its finite Clifford, trace, differential and metric inputs, not every functional-analytic step.

Selfadjointness does not imply a Fredholm chiral block, finite-dimensional kernel, compact resolvent or the W46 index. The remaining spectral duty is the full cusp behavior of this SAME operator and its coupling of vertical harmonic profiles to the complement. Nor is it yet identified with a physical parent's Weyl Hessian. Lambda, metric, physical dictionary, nonzero sector and dynamics remain supplied. No physical chirality no-go or full theory is claimed.
