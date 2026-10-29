# Two canonical heat responses and a scale-free relative coupling

October 29, 2026. UNREVIEWED authored conditional proof. No scientific
producer, CAS, numerical determinant or measured-coupling comparison.
Same supplied curved action, R=0 principal parallel background, hyperbolic
once-punctured elliptic carrier and complete graph realization as the
preceding operator/kernel proofs. This is a parity-even one-loop result
inside that model, not its foundational selection or the observed SM.

## 1. The exact question, and what is not discarded

The preceding bounded contraction computes zero modes. A contractible
pair can still contribute massive states to a loop. Here derive their
actual quadratic operators and their RELATIVE heat traces before making
any cancellation. Keep all angular channels, the compact core, both spin
fields, the gaugino and the real vector/FP weights.

Let L be the supplied unitary flat Y line, trivial on the peripheral,
represented by a compact-core connection. L^q is the actual charge-q
line, not an independently chosen boundary condition. All comparisons
below subtract L^0 on the same underlying Hermitian bundle/domain.

Reuse SAME_ACTION_REAL_GAUGE_FIXING_AND_ONE_LOOP_WEIGHTS.md,
PARALLEL_PHASE_CHIRAL_KERNEL_AND_LIGHT_RUNNING.md and the source's
weave_two_neutral_index, weave_sm_parallel and weave_physical_mass proofs.
The finite raising coefficient k_m below is already fixed by their action.

## 2. Normalize one Dolbeault pair once

For integer a, use the source-normalized Dolbeault map B_a on S^a L^q.
In a hyperbolic chart z=x+iy, Omega=1/y, and a local holomorphic flat
frame for L^q, B_a=Dbar=partial_x+i partial_y. The source section and
rescaled form densities are respectively

  Omega^(2-a)|f|^2 dxdy, Omega^(-a)|g|^2 dxdy.

This corresponds to the physical connection coefficient a_conn/sqrt(2)
in the gauge complex; it is not a new kinetic normalization. Thus

  B_a dagger g=-Omega^(a-2) Dz(Omega^(-a)g),
  K_a^0=B_a dagger B_a, K_a^1=B_a B_a dagger.              (1)

All operators use the closures of the same complete forms. The source's
cusp argument gives Fredholm B_a for every integer a: even a has a
nonzero half-integral zero-angular drift, odd a has no zero-angular mode.
The flat core twist changes no end. The relative heat trace-class and
small/large-time arguments apply to this actual Dolbeault Dirac pair.
Define the FINITE trace

  F_a(q;s)=Tr(exp(-s K_a,q^0)-exp(-s K_a,0^0)).            (2)

It is not an absolute heat trace. K_0 has continuous spectrum; its
individual heat operator is not substituted into an infinite trace.

## 3. A relative partner identity, with the end retained

The two Dolbeault Dirac operators at q and0 are elliptic, have bounded
propagation, coincide outside a compact set, are selfadjoint on the
complete graph domains and are Fredholm. Their indices agree: the
compact-core twist is a norm-continuous graph-compact perturbation along
tC. Local elliptic estimates on the compact comparison region supply
the regularity hypothesis. The relative McKean--Singer theorem therefore
gives, for every s>0,

  Tr[(exp(-s K_a,q^0)-exp(-s K_a,0^0))
       -(exp(-s K_a,q^1)-exp(-s K_a,0^1))]=0.              (3)

The four terms are grouped as trace-class differences. This is not
cyclic cancellation of two divergent absolute traces. Personally read
Lesch, dg-ga/9607005, complete III Section3.5, especially Proposition3.5.7
and Theorem3.5.8, with the compact-region hypotheses above:
https://arxiv.org/pdf/dg-ga/9607005 (October29).
No full-book reading or automatic theorem for other physical domains is
claimed. The source's earlier continuum supertrace remains valid: its
end contribution is the SAME at q and0 and cancels only in this relative
comparison.

## 4. Derive the global spin-power recurrence

The metric gives a complex-linear unitary map J_a from the rescaled
(0,1)-form space of S^a to the section space of S^(a-2). In the stated
frames J_a g=Omega^(-2)g. It is intrinsic metric index raising, with
the constant fixed by the displayed norms. Compute using (1):

  J_a K_a^1 J_a^(-1)
       =-Omega^(-2)Dbar Omega^(a-2)Dz Omega^(2-a)
       =K_(a-2)^0+(a-2),                                 (4)

where the last equality uses curvature -1. For example in Omega=1/y,
the right side on a holomorphic coefficient is

  -y^2(partial_x^2+partial_y^2)
       +i(a-2)y Dbar+(a-2).

The first two terms are exactly K_(a-2)^0. The identity is tensorial,
holds in every uniformizing chart and preserves flat/spin transitions.
It holds on compact-support cores; equality of the closed nonnegative
forms extends it to the complete realizations. A negative displayed
constant does not imply a negative spectrum: (4) then supplies the
corresponding lower bound on K_(a-2)^0. No new end condition is added.

J_a is independent of the charge connection. Apply (4) to the two
operators in the relative trace and use (3):

  F_a(q;s)=exp(-(a-2)s) F_(a-2)(q;s).                    (5)

Consequently the entire integer-spin-power family is determined by
TWO canonical responses E_q=F_0(q;s), O_q=F_1(q;s):

  F_(2r)(q;s)=exp(-r(r-1)s) E_q(s),
  F_(2r+1)(q;s)=exp(-r^2 s) O_q(s), r in Z.              (6)

These are identities of relative spectra, including massive modes.
They are stronger than the line-kernel dimension formulas. Both E_q
and O_q retain the full core/cusp geometry and character dependence;
no scalar torus eta function is guessed for them.

There are also exact charge/duality controls. Complex conjugation of
the ordinary flat scalar operator gives E_q=E_(-q). The actual Serre
antiunitary map on a form coefficient is U_a g=Omega^(-a)bar(g), with
target S^(2-a)L^(-q). Directly from (1), it carries K_a^1 to
K_(2-a)^0. Thus (3) gives F_a(q)=F_(2-a)(-q). At a=1 this gives
O_q=O_(-q); (6) then makes every F_a even in q and

  F_a(q;s)=F_(2-a)(q;s).                                 (7)

The compact spin line eta is not erased: it remains in O_q. Formula
(6) does not assert spin-independent determinant values.

## 5. Derive the FULL physical module trace, not a cochain surrogate

For V_j set m=-j,...,j and

  k_m^2=(j-m)(j+m+1)/2, with k_j=0.                       (8)

The gauge section is E_m=S^(-m)L^q. In canonical norms the actual
paired maps are d0=(B_(-m),-k_m), d1=(k_m,B_(-m)), up to constant
unitary phases. This follows because Q=E_raise/2 and the gauge map
has the source factor sqrt(2): its mass is e_m/sqrt(2)=k_m. The
connection coefficient is rescaled by1/sqrt(2) as in section2.
Their ordered multiplication, with parallel Q, gives

  P_v,m=K_(-m)^0+k_m^2,
  P_(A_m)=K_(-m)^1+k_m^2,
  P_(Q_(m+1))=K_(-m)^0+k_m^2, m<j.                     (9)

The Q-lowest extreme has K_(j+1)^0, and the R_m field has
K_(1-m)^0+k_m^2 for ALL m, including its zero-raising highest extreme.
Equation (9) includes A_j with k_j=0. These sum to one vector section
and THREE chiral slots per original weight count, with no companion
deleted. Their adjoints/domains are those already fixed by the same
action. The zeroth-order raising terms are parallel bundle maps with
constant norm; hence the global derivative cross terms cancel, not
just their frozen radial symbols.

Let Phi_j(q;s) be the actual physical relative heat contribution
r_c-3r_v per gauge component. Using (3) only after (9) gives

  Phi_j=sum_m exp(-s k_m^2)(F_(1-m)-F_(-m))
                       +F_(j+1)-F_(-j).                 (10)

Now pair m with -m-1 in the range -j<=m<=j-1. Their k^2 agree.
By (7), F_(m+2)=F_(-m) and F_(m+1)=F_(1-m), so their terms cancel
EXACTLY in this relative physical trace. The sole unpaired m=j and
the displayed extremes give

  Phi_j(q;s)=2[F_(j+1)(q;s)-F_(-j)(q;s)].                 (11)

This is a derived massive-spectrum cancellation using the actual
spin/FP weights and relative partner theorem. It is not inferred from
contractibility, the index, or a cochain1:2:1 heat identity. The two
extreme operators in (11) still contain their complete massive spectra.

Write x=exp(-s). Equations (6),(11) give the full E8 module list:

| j | Phi_j(q;s) |
|---|---|
| 0 | 2(O_q-E_q) |
| 1 | 2(E_q-x O_q) |
| 2 | 2(x O_q-x^2 E_q) |
| 3 | 2(x^2 E_q-x^4 O_q) |
| 4 | 2(x^4 O_q-x^6 E_q) |

The powers and coefficients are fixed by curvature and the source
raising/moment normalization. They are not fitted Kaluza--Klein masses.
An additional check is the cusp drift: K_a^0 has zero-angular square
(1-a)^2/4 when that angular channel exists. At a=-m, adding (8)
recovers exactly the source's (m+1)^2/4+k_m^2.

## 6. Assemble all SM gauge insertions on the source's character

For the order-seven source line, conjugate characters identify q and-q;
there are three nontrivial power classes, represented by q=1,2,3.
There is no identification between those THREE classes by a Galois or
geometric assumption. Thus six ordinary relative responses E_q,O_q
suffice for the full gauge threshold of this phase.

Put Psi_q=Phi_1(q)+Phi_3(q) for the structure10_b, and T_q=Phi_2(q)
for5_b. The already-derived charge/index table then gives, INCLUDING
both conjugate ten/five sectors and the single real gauge24 sector,

  B21=(2/5)(Psi_3-Psi_2)+(8/5)(T_1-T_3)-2 Phi_0(2),
  B31=-(3/5)(Psi_3-Psi_2)+(3/5)(T_1-T_3)-3 Phi_0(2).      (12)

Gauge-singlet24_b has no insertion. Equation (12) uses the identities
L^(-4)=L^3 and L^6=L^(-1), not equality of distinct geometric characters.
It is a finite exact coefficient map to TWO operator families, rather
than independent correction numbers for the gauge factors.

At large s, E_q ->delta(L^q)-1 and O_q ->delta(eta L^q)-delta(eta).
The table recovers every light-kernel jump of the preceding proof:
Phi_1 ->2(delta(L^q)-1); Phi_j ->0 for j>=2; and Phi_0 retains the
spin/character exception. In particular (12) gives (-4,-6) or (0,0)
according to the previously determined spin case. This is an independent
consistency of the full trace reduction with the extreme zero counts.

## 7. A relative observable loses the common scale for EVERY spin

Define the normalized coupling combination

  C=alpha3^(-1)-(3/2)alpha2^(-1)+(1/2)alpha1^(-1),
  B_C=B31-(3/2)B21.

The common classical SU5-normalized coefficient cancels. Equation (12)
also cancels the ENTIRE gauge24 response, not just its zero modes:

  B_C=-(6/5)(Psi_3-Psi_2)-(9/5)(T_1-T_3).                (13)

For the stated order-seven character h_C=lim_(s->infinity)B_C(s)=0
for ALL four extending spins. The ultraviolet is O(s^N) for every N,
and the remaining infrared terms decay exponentially. Therefore

  L_C=-integral_0^infinity B_C(s) ds/s,
  Delta C=-L_C/(4 pi)                                   (14)

is absolutely convergent without a light matching switch or its scale.
Under a COMMON physical mass-square rescaling P->cP, changing variables
in (14) gives the same L_C. This removes that particular scale/matching
ambiguity without selecting trivial spin. The finite value can still
depend on spin, shape and the Wilson state. No whole-model equivalence
of physical scales or erasure of the measuring sector is asserted.

This is not a hidden exclusion of exceptional characters. For a general
peripheral-trivial unitary line L, the same full coefficient table gives

  h_C=(12/5)[delta(L^2)-delta(L^3)].                       (15)

The ten-sector relative light contribution is zero and the24 contribution
cancels identically; only the five-sector j=1 jump enters (15). Thus the
common scale cancels on the nonexceptional family, including order7,
and also where both deltas agree. A nontrivial order2 or order3 line
instead has a nonzero h_C, with its corresponding light running retained.
The source character is still supplied; it is not chosen after computing
C. The result is one-loop and model-scoped, not a prediction for measured
M_Z couplings of a different light EFT.

## 8. Rejecting controls on the reduction

* If the metric is not constant curvature -1, (4) has a variable
  curvature term; one cannot replace it by the exponential factor (5).
* A nonflat Y connection changes local heat invariants and the curvature
  term in the partner identity. Zero TOTAL flux alone does not restore
  (5). The identity is not transferred to a curvature-insertion frame.
* Omitting the FP pair changes the vector weight from -3 to -8/3.
  The resulting trace differs from (10) by one third of the entire
  vector response, including its non-extreme massive terms.
* Replacing J_a by Omega^(-1) on coefficients fails the displayed norm
  equality; it is not a unitary map of the actual physical spaces.
* An off-shell change of Q at fixed curvature has a nonzero moment
  background and changes the real scalar Hessian. Keeping only its
  F-complex is not a physical extension of this one-loop proof.

These are analytic controls, not claims that new rejecting scripts have
been executed. The exact source assumptions and physical Gaussian weights
are load-bearing, rather than dispensable conventions.

## 9. What has been reduced, and what has not

Before: a full coupled E8 operator/domain calculation, unknown independent
threshold functions by representation, and a common-scale question tied
to the spin choice. After: the complete relative physical trace is fixed
by six evaluations of two canonical ordinary operator families on the
source order-seven line; all mass-polynomial coefficients are derived;
and C has no common-scale/matching-switch ambiguity for any extending
spin on that nonexceptional source state. Massive spectra were retained
through the proof, not replaced by their kernels.

These are conditional reductions inside a supplied model. They do not
remove its independent foundational action, gauge embedding, metric,
spin or Wilson/state inputs. No numerical value of (14), empirical fit,
chiral three-generation spectrum, anomaly/phase completion, quantum UV
theory or gravity is claimed. The finite functions E_q,O_q are the next
objects to evaluate or characterize, with their geometric/state inputs
explicit. A numerical route still requires its own source-complete seal,
independent main review and admitted execution; P210 approval is not
approval of this new scope. All new identities await independent review.

For the input ledger: the two-operator result is a COMPUTATIONAL
reduction; the old representation responses were already determined
by the action, so they were not legitimate independent inputs to count
as removed. E_q,O_q are functions, not two adjustable constants. The
new observable-level dependency reduction is that C needs no common
mass scale or matching switch on the stated nonexceptional family.
That scale remains an independent physical duty for other observables.
No foundational-input row is discharged by this note.
