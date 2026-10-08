# One paired spectral phase prescription

Conditional analytic construction for the supplied parent and complete
domain. It defines a fermionic PHASE on a small external-field chart
by a declared internally nonlocal pairing prescription. It is not the
full renormalized action or a regulator selected by genesis. Its
consistent anomaly is generally nonzero.

## The polar map retains the actual physical fields

Fix the internal stationary background, including n,c,d. In a gauge
isotypical block the previous dictionary gives a closed Fredholm mass
map M:H_plus -> H_minus with the stated adjoint domain. H_minus is the
dual-conjugate of the opposite-charge LEFT fields, not extra matter.
Let P_plus and P_minus be its kernel and adjoint-kernel projections.
The operator polar decomposition gives

    T=(Mdagger M)^(1/2), U=M T^(-1) on (ker M)^perp,
    Udagger U=1-P_plus, U Udagger=1-P_minus,
    M=UT, M Mdagger=U T^2 Udagger on the complements.

Fredholmness gives closed range and a strictly positive lower bound
T>=delta there. Delta can depend on this background; the previously
computed essential threshold does NOT bound every positive discrete
eigenvalue. This distinction is essential to the inverse. Since M and
its domain commute with the admitted unbroken gauge group, the spectral
projections and U intertwine its actual representations. The map acts
also on the continuous spectrum; it is not a count of discrete modes.

The polar change of right-handed basis makes the massive part of the
four-dimensional action vectorlike, with positive self-adjoint mass T.
The external covariant derivative commutes with T and U because the
external fields are internally parallel. Both unpaired finite kernels
are retained as left/right Weyl fields. Using one charge representative,
or half of the full charge-conjugate presentation, retains the original
Grassmann content and gives the old difference ind M_R.

## The regulated Gaussian phase is defined before its current

Choose an increasing finite-dimensional form-core exhaustion E_N in
Dom(T) of the complement, also dense in Dom(T^(1/2)), and use U E_N
for the target. Such
exhaustions exist by separability of the graph/form Hilbert space; take
them in gauge multiplicity space and tensor the whole representation.
The compressed closed form defines a finite Hermitian matrix T_N>=delta.
Galerkin form convergence recovers T in strong resolvent sense; no
claim of trace-norm or determinant-modulus convergence follows.

At finite N, diagonalizing T_N gives masses m_j>0 and actual Dirac
Gaussian factors det(Dslash4_R[A]+m_j). Here Dslash4 is anti-Hermitian
and anticommutes with gamma5. Its nonzero eigenvalues occur in pairs
plus/minus i lambda, whose determinant contribution is

    (m_j+i lambda)(m_j-i lambda)=m_j^2+lambda^2 >0.

Zero eigenvalues, if present, contribute positive powers of m_j.
A vectorlike proper-time or zeta definition preserves this positive
phase; a positive-mass Pauli-Villars ratio does too. Thus, normalized
to A=0, the massive phase is exactly1 at EVERY N, not a limit of
nonzero anomalous currents being cancelled by fiat. Arbitrary extra
massive pairs do not alter it. Its N limit therefore exists as a phase
even though its positive modulus diverges with the internal length.

This specifies the measure by pulling back the standard paired
Gaussian measure through the fixed U. It is not a proof that every
cusp-local measure gives the same phase. U is generally internally
nonlocal and depends on the fixed internal background. Varying that
background, or allowing nonparallel gauge fields, is outside this
argument. A possible Jacobian for a DIFFERENT regularized measure is
not silently set to1. No determinant multiplicativity theorem on the
noncompact full operator is used.

Salcedo [sectionsII.1--II.3](https://arxiv.org/html/0807.1696) defines the
Gaussian determinant and distinguishes vector similarity symmetry
from chiral transformations. Its finite invertible mass assumptions
apply to the compressed massive blocks, not to the kernel sector.

## The unpaired phase and what is supplied in its definition

On the prior spin four-torus use a contractible small-connection chart
with operator perturbation norm below the free gap1/2. For a Weyl
representation use the compact elliptic presentation

    C_R[A]=Dslash4[0]+gamma^mu v_mu P_L, v=-i A,

with its opposite chirality a FREE spectator. In a chiral block frame,
its determinant is the desired Weyl determinant times the fixed free
opposite-chirality determinant; normalize at A=0. The spectator is a
definition of the square elliptic presentation, not an added physical
charged compensating field. The small perturbation of the free normal
operator keeps its spectrum away from the positive real spectral cut.
Choose that cut and define the local phase by the imaginary part of
minus log det_zeta C_R[A]. The usual compact elliptic continuation and
local-counterterm freedom are analytic QFT inputs here.

This is a scalar functional on that chart, so its variation is locally
integrable. It need not be gauge invariant or extend to a globally
single-valued phase on the gauge quotient. In a minimal consistent
representative its perturbative anomaly is the conventional left-Weyl
descent expression. With anti-Hermitian connection a and parameter v,

    Q(v,a)=tr_R v d(a da + a^3/2), delta_u a=du+[a,u].

The universal one-Weyl normalization and the nontriviality of this
local anomaly class are standard four-dimensional input, as derived
in Bilal [section9.3](https://arxiv.org/html/0802.0634v1). We do NOT
pretend to have evaluated a new full-cusp triangle or the finite local
counterterms of the chosen zeta presentation. What follows for our
prescription is the anomaly CLASS and its complete representation
coefficient. A numerical zero-mode truncation alone did not establish
this: the massive Gaussian phase has now been dealt with in one
explicit regulator.

## Consistency is checked rather than renamed

For fixed ordinary gauge parameters u,v, the gauge vector fields have
bracket parameter [u,v]. A local action variation must satisfy

    delta_u Q(v,a)-delta_v Q(u,a)-Q([u,v],a)=d R3.

On the compact external torus the right side integrates to zero.
The native instrument expands noncommuting graded words in a,da,u,du,
v,dv, implements signed cyclic trace, and solves for the exact3-form
R3. It emits a rational witness and verifies its derivative term by
term. The space searched contains every degree3 word with one u/du
and one v/dv and up to three a/da factors. This is an algebraic
identity, not a sampled background test. Changing the cubic coefficient
from1/2 to0, or using the covariant tr(v(da+a^2)^2), must fail the same
exact-form criterion. The overall one-Weyl normalization is NOT fixed
by this homogeneous condition.

## The consistent coefficient and the surviving duty

All positive-mass paired blocks have zero vector gauge anomaly in
this prescription. The finite kernel phase therefore carries

    sum_R (dim ker M_R - dim ker M_Rdagger) Q_R.

The root and tensor reconstructions retain every charged block,
including q=5, endpoints and conjugates. Relative to the earlier
one-left-Weyl conventions, its five coefficients remain

    n>=2: (-3,-6,-6,-1008,-30),
    n=1:  (-1,-5,-9/2,-1002,-24),
    n=0:  (0,0,0,0,0), with sign reversed for negative n.

Unknown additional vectorlike zero-mode pairs do not change this
statement. It is a CONSISTENT anomaly class for the specified paired
phase, not the previous covariant inverse current. It is nonzero at
nonzero n; obtaining integrability has not obtained gauge invariance.

The old heat interpolation remains true in its different common-spatial
cutoff prescription. Its continuum density and the paired prescription
are not interchangeable inside a divergent ordinary trace. The present
construction explicitly records the end/measure choice instead of
silently identifying them. It does not prove the existence of a local
six-dimensional regulator, a finite parity-even action, global anomaly
cancellation, an admitted compensating end system, stable charged
vacuum, three families, or parameter-free foundational selection.
Those remain the next physical duties, not a universal architecture kill.
