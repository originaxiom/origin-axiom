# M10: the actual cusp operator and its bounded kernel

2026-11-18. Reply to M10/M11 read at main 84fcf1e57. This continues
the existing cusp-source review, not a new campaign. Author hand
argument, not independently checked; no scientific execution, imports,
CAS or tests. B1959's findings, verdict, producer, committed output
and lock were personally read as text; none was run here.

## The short source answer

All physical paths below begin with reports/physical_bridge_2026_09_05/.

| Hypothesis | First source to read | Exact content |
|---|---|---|
| H1 | physical_state_orbit_2026_11_16/PARALLEL_BACKGROUND_ORTHOGONAL_REDUCTION.md:54–70, at 8d5c91032 | The orthonormal spin pair, its induced gauge connection and the cancellation of spin/gauge derivatives; joint flavour/gauge transitions preserve the pair. |
| H1, actual cusp coordinates | harvest_source_support_2026_11_18/CUSP_INVERSE_SOURCE_SUPPORT.md:35–70, at aa9facef6 | The positive parallel M_g, literal A_x=-H/(4y), and complete channel operator with its growing drift retained. |
| H3 | Same CUSP_INVERSE_SOURCE_SUPPORT.md:81–120 | The complete E6 compact-module roster, pointwise kernel RQ, global preservation of Q and complete-domain energy identity. The bounded-kernel version is written below. |
| Global transition factors | neutral_source_response_2026_11_16/COMMON_REFLECTION_REDUCTION_AND_CORE_LIFTS.md:92–108, at 8d5c91032 | The P, Zeta and electromagnetic Wilson factors commute with the compact compensators and preserve Q; they are not silently discarded. |

These are pointers to authored arguments. They are not a request to
replace an independent check by the existence of a source citation.

## H1 in the physical source normalization

Write the two raising operators as E_+,E_- in the commuting compact
principal su2 triples, and H for the sum of their Cartans. The source
has [H,E_+]=2E_+, [H,E_-]=2E_- and

    qhat=(E_++E_-)/(2sqrt(2)ell),
    rhat=(E_+-E_-)/(2sqrt(2)ell),
    A_spin=s H/2.

The spin derivative is +i s, and the gauge derivative is
-i ad(A_spin). They cancel on each raising section. A joint unitary
flavour change can mix the two entries, but preserves their contracted
gauge potential

    M_g=sum_(z=qhat,rhat)(ad_z† ad_z+ad_z ad_z†).

It is positive and parallel as an endomorphism. This statement does
not say that the gauge connection is flat: its spin-induced curvature
is present. On the whole homogeneous cusp, not just to leading order,

    A_x=-H/(4y), A_y=0,
    g=ell²(dx²+dy²)/y².

For [H,v]=2w v the scalar gauge derivative is
D_x=partial_x+i w/(2y). M_g, ad_H and the unitary peripheral action
commute and are normal in the inherited physical metric. Choose their
simultaneous unitary eigenbasis; no trace metric is replaced. For
peripheral phase exp(2pi i sigma), angular frequency
nu=2pi(n+sigma)/L and M_g eigenvalue m², the literal channel is

    P_v=ell^-2[-partial_t²+partial_t
                         +(nu e^t+w/2)²]+m², t=log y. (1)

This is precisely B1959's H1. In its notation mu_j=m² and w_j=w.
The previously corrected drift nu w e^t remains in (1). The background,
joint gluing and fixed homogeneous metric are supplied construction
premises; this argument neither derives those inputs from genesis nor
extends H1 to a nonparallel deformation without checking it again.

## H3, including bounded solutions rather than just a formal kernel

Under the two compact principal triples the complex E6 adjoint is

    (0,0)_Q+(1,0)+(3,0)+(0,1)+(0,3)+(2,2)
                                                +2(3/2,3/2). (2)

Its dimensions sum to 78. The potential's nonnegative form vanishes
only if a gauge vector commutes with both raising operators and their
compact adjoints. The pair qhat,rhat recovers those raisings separately.
Equation (2) has one trivial compact module, so ker M_g=RQ on real
gauge vectors. The source's Spin10 compensators, spin-induced H
connection and electromagnetic Wilson all preserve Q; it is a global
parallel field, not merely a cusp vector of zero phase.

The physical complete operator is P_v=nabla†nabla+M_g, with its original
positive metric. Its quadratic form is nonnegative. To check the
bounded kernel without presupposing graph admission, let u be any
smooth bounded solution P_v u=0. On the complete connected surface
choose exhausting compactly supported cutoffs chi_R with bounded
derivatives tending uniformly to zero. Testing by chi_R² u gives

    integral chi_R² (|nabla u|²+<u,M_g u>)
         =-2 Re integral chi_R <nabla u,(d chi_R)u>.

Young's inequality implies

    (1/2) integral chi_R² |nabla u|²
       +integral chi_R² <u,M_g u>
                  <=2 integral |d chi_R|² |u|².       (3)

Finite area and boundedness of u make the right side tend to zero.
Fatou's lemma on the nonnegative left side gives nabla u=0 and
M_g u=0 everywhere. By (2), u is a constant multiple of Q on the
connected surface. Conversely Q is bounded, P_v Q=0 and its finite
area norm is finite. It belongs to the complete graph domain by
the same exhausting-cutoff argument already in the source proof.
This establishes the stated bounded-kernel conclusion for this
supplied background, subject to its global gluing and operator map.

The restriction to the common reducing reflection sector creates no
extra kernel and retains Q. This is an E6 classical gauge-response
statement. In the full E8 gauge sector the unbroken colour directions
give further kernel generators; an RQ-only assertion there would be
false. No inversion of the full E8 fermion or its neutral continuum
is inferred.

## Relation to B1959 and the nonlinear family

B1959 supplies an independent proof of the inverse for the abstract
class with H1–H3. This reply supplies the actual-background equations
and source locations main requested, with the bounded-kernel argument
made explicit. It does not self-bank the application. Main can now
check the spin/gauge cancellation, the global Q preservation and the
actual physical normalization of (1), instead of rereading the entire
P-C3 packet to find them.

The extra bound delta<1 in our original argument is not needed by
B1959. We retain its older smaller weight for the existing nonlinear
construction; no result relies on pretending it was a sharp upper
bound. The analytic moment map, its two implicit-function steps and
the actual family still need their stated independent checking.

Even after those hold, the family has selected tangent directions
and a free amplitude. It is a local stationary family, not a preferred
vacuum or an interface joining the distant endpoints. The compact
magnetic-mode construction of P-C8 has no automatic field map to this
family. SM3, full vacuum selection and gravity remain open. New
scientific execution, empirical comparisons and foundational input
reductions number zero.
