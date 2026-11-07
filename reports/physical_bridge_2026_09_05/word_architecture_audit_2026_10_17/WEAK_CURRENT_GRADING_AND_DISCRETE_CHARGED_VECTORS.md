# The weak current crosses the two spectral blocks

2026-11-07. **UNREVIEWED conditional hand argument.** No scientific
imports, collection, CAS or producer execution. This addresses the actual
weak-current duty in the supplied coupled quaternion E8 parent. It does
not assign observed W/Z masses, select a weak SU2, count generations or
derive the physical parent from genesis.

## 1. Reuse the full charge and grading maps

The full-root construction and [Pin2 proof](PIN2_COMPENSATOR_COHERENCE_AND_ELECTROMAGNETIC_PHASE.md)
retain the actual electromagnetic Cartan

    Q=(2/3)(e1+e2+e3).

The source involution Zeta is +1 on the integer-root/Cartan 120 and -1
on the half-root 128. Both background Higgs fields and the connection
are even; transitions commute with this grading. The [sector proof](CONFINED_HALF_ROOT_SECTOR_AND_SURVIVING_CONTINUUM.md)
establishes the two reducing **linear** fermion sectors and a discrete
128 sector alongside the centralizer continuum. It already retains
`[128,128] subset 120` and `[120,128] subset 128`.

Here Zeta is also the particular electromagnetic rotation `exp(3 pi i Q)`:
the Pin2 proof gives `h^4=Zeta` with `h=exp(3 pi i Q/4)`. This is not an
additional independently selected discrete charge or a new symmetry.

The point here is their consequence for a charge-one vector and its
actual fermion vertex. It is not a claim to discover the Z2 grading.
A source search in this report directory found the bracket and general
interaction duty in that earlier proof, not a calculation of this vertex.
No repository-wide novelty or absence certificate is asserted.

## 2. Charge one forces odd grading

An integer E8 root is `+-ei +-ej`. Its Q charge is

    0, +-2/3, or +-4/3.

For a half root `(epsilon1,...,epsilon8)/2`,

    Q(root)=(epsilon1+epsilon2+epsilon3)/3,

so its charge is `+-1` or `+-1/3`. Therefore every adjoint vector with
electromagnetic charge +1 or -1 lies in 128. This is an exact root/Cartan
statement in the stipulated charge normalization. A W candidate with
that charge cannot be an arbitrary vector from the 120 block.

For a gauge-vector profile w in that odd charge-one sector, its adjoint
action reverses the grading. In the source's positive kinetic inner
product the two grading subspaces are orthogonal. Thus for any two
fermion profiles both in 128, or both in 120,

    sum_i integral h_i kappa(psi_i,m† [w,psi_i,n])=0,     (1)

where `i=(lambda,a,u,v)` and
`h_i=(Omega²,1/2,Omega,Omega)`. The trace-dual/conjugate charged partners
are retained. The same zero follows directly from invariance of the
trace under Zeta. It is pointwise before any profile approximation.

Only opposite-grading profiles can give this single-vector current.
With source-normalized profiles the candidate coefficient is

    g_mn(w)=g6 sum_i integral h_i
                       kappa(psi_i,m† [w,psi_i,n]).     (2)

Normalize the vector with `integral dvol kappa(w†w)=1` and the fermions
with their actual four-slot kinetic norm. Equation (2) is the same-action
gauge vertex, not a new fitted matrix. It still requires the actual
solutions and their integral. The grading fixes its possible blocks,
not their rank or numerical entries.

There are nonzero **algebraic** allowed channels. Take

    w_root=(1,1,1,1,1,1,1,1)/2,
    d_root=(1,-1,-1,1,-1,-1,-1,-1)/2.

Both have an even number of minus signs, their dot product is -1, and
their sum is the integer root e1+e4. Their charges are +1, -1/3 and
+2/3. The root bracket is nonzero by the usual root string/Jacobi
normalization already exhibited in the source cubic proof. Likewise
`[E_w,E_-w]=H_w` is a nonzero neutral even channel for the charge-minus-one
half root. These are possible down/up and charged/neutral channels;
their existence is not a normalized low-mode overlap or a neutrino
identification.

The source's [old parallel gauge embedding](../weave_sm_parallel_2026_10_08/PROOF.md)
already proposes this very `w_root` as its weak raising root, with
`T3=w_root/2` and `Y=(5,5,5,-3,-3,-3,-3,-3)/12`. Direct addition gives
`T3+Y=Q`. Thus the example respects that existing embedding; it does not
introduce a new weak root to obtain the charge pattern. The new core
holonomies can mix its root direction with other charge-one directions.
A fixed local root vector is consequently not the global normalized
massive vector profile. That profile must solve Pv's full bundle problem.

## 3. The charge-one vector problem itself is discrete and massive

Reuse the same-action real gauge fixing, rather than transfer the fermion
spectrum just because both operators use the adjoint representation.
At W'=0 and moment zero the source identities are

    d=sqrt(2)k,
    H d=0,
    Pv=d†d=2k†k,
    M†M=diag(Pv,Pc).                                   (3)

They were derived in
[the real gauge proof](SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md).
Their hypotheses hold for the new stationary bundle: all local residuals
vanish, the actual unitary transitions preserve the superpotential,
moment map, compact real structure and kinetic norms, and the same
complete cutoffs remove the surface term. No old heat trace, relative
determinant or running formula is inferred for the new end.

The coefficient grading commutes with (3). Compact resolvent of the
doubled operator on the entire 128 block implies compact resolvent of
its square, hence of the reducing gauge-parameter/gaugino block Pv there.
This inference uses the actual identity (3), not equality of dimensions
or an analogy between a vector and a Dirac operator. The form-domain
identity in (3) supplies its domain; no new boundary condition is chosen.

Its kernel is zero independently of the new finite-kernel successor.
Pv preserves the compact real structure at moment zero. A real element
of its kernel satisfies `k epsilon=0`: Dbar_A epsilon=0 and both Higgs
commutators vanish. Compact conjugation gives Dz_A epsilon=0 and both
adjoint-Higgs commutators vanish. Thus it is parallel and lies in the
pointwise compact centralizer of the two triples. That centralizer is
A3, entirely in 120. There is no nonzero such vector in 128. Decomposing
a complex kernel element into real and imaginary parts gives the same
conclusion. Elliptic regularity makes the distributional kernel argument
legitimate on the complete form realization.

Consequently Pv on either charge-one block has discrete spectrum with
a strictly positive lowest eigenvalue for each fixed admitted carrier.
The two conjugate charges have matching spectra by the compact real
structure. This provides a well-posed **massive charged-vector tower**
in the same conditional model, not its computed eigenvalues or an
identification of one state as the observed W. No uniform lower bound
through modulus degeneration or change of cusp covering parity is given.

## 4. What the physical calculation must retain

An interacting weak-current calculation cannot use the discrete 128
fermions alone: its charge-one vector couples them to the even sector.
The latter has its own bound-state problem and an essential continuum.
Neither (1) nor (3) proves that every such vector couples to every
continuum channel, or that a bound state is unstable. Those are actual
overlap and dynamical questions.

The [candidate half-root kernel](COUPLED_HALF_ROOT_KERNEL_AND_CORE_LIFT_SENSITIVITY.md)
does not count weak doublets by itself. Its conjugate U3 charges and
zero index remain compatible with different possible weak-current
structures. To establish weak chirality, compute the normalized current
on both independent left-charge sectors, reconstruct its right-handed
Dirac interpretation, and test the selected low-state current matrices.
The weak SU2 algebra and the neutral-vector sector must also be joined
to this same operator/action, not imported from a different construction.

Before: an abstract duty to compute weak vertices and an unspecified
weak-vector profile problem. After, conditionally: the charge-one vector
must be odd, its spectrum is discrete and strictly massive, and its
single-vector fermion current must cross the spectral grading. No extra
coupling coefficient, mode truncation or boundary projector was supplied.

These are within-model consequences. The physical E8 parent, spin/flavour
identification, metric/end, electromagnetic reading and state selection
remain hypotheses. The global registering-sector identification, full
physical spectrum, three generations, observed parameters and gravity
remain open. Both the vector-domain transfer and kernel argument need
independent review before acceptance. No scientific pass is claimed.
