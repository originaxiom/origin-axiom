# How much of the carrier the coefficient cohomology sees

2026-10-11. Author: originaxiom. Elementary proofs for review.

Fix F=F(a,b), F'= [F,F], F''=[F',F'] and F'''=[F'',F'']. The canonical quotients G_d=F/F^(d) retain all endomorphisms: an endomorphism maps a commutator to the commutator of its images, and induction preserves every derived subgroup. An automorphism and its inverse descend to inverse automorphisms. No choice of representative is required.

The coefficient system is an explicit input. Nothing here derives why it is physical or should be selected by PF1–PF3.

## Positive descriptions survive these quotients

The affine path homomorphism E constructed in ../positive_carrier/PROOF.md has abelian derived subgroup: all commutators are translations and translations commute. Thus F'' is contained in ker E, as is F'''. If two positive words agree in G_2 or G_3, their E images agree. Sorting the two path polynomials' edge terms by total degree recovers every positive letter, so the two words were equal. Both quotients therefore retain every positive word.

They are proper quotients. The exact verifier freely reduces the explicit words

    c=[a,b], r=[c,a c a^-1], t=[r,a r a^-1]

to nonempty words by two procedures. By construction r belongs to F'' and t belongs to F'''. These are finite, constructive kernel witnesses; no infinite word-problem claim is inferred from an enumeration.

## A general bound for degree one cohomology

Let rho:F→H⊂GL(V), where H is solvable of derived length at most d. For any rho-cocycle z, define

    R_z(w) = (rho(w), z(w)),
    (A,u)(B,v) = (AB, u+A v).

The cocycle identity is exactly the homomorphism law for R_z. Projection of V⋊H onto H has abelian kernel V. The d-th derived subgroup of V⋊H is therefore contained in V and its next derived subgroup is trivial. Consequently R_z kills F^(d+1), for every cocycle z and every generator assignment that defines a cocycle on F.

It follows directly that z descends uniquely to G_(d+1). Indeed, both rho and z vanish appropriately on the kernel, and z(wn)=z(w) whenever n belongs to F^(d+1). Conversely any cocycle on that quotient pulls back to one on F. Coboundaries have the same form (rho(w)-I)v before and after quotienting, so inflation gives an isomorphism

    H1(G_(d+1),V) → H1(F,V).

This proves the isomorphism without invoking a spectral sequence or an external inflation theorem. It is a sufficiency bound, not a claim that d+1 is always minimal.

For an automorphism f and an intertwiner g with rho(f(w))=g rho(w) g^-1, the cohomology operation is [z]→[g^-1 z∘f], with parity transported when needed. Since F^(d+1) is characteristic, this operation commutes with the quotient map. Thus the inflation isomorphism intertwines the actual lifted move action, not merely dimensions. A fixed central-lift sign remains part of that action; it is not removed by this argument.

## Quaternion doublets need more than a metabelian carrier

Use A=rho(a)=diag(i,-i), B=rho(b)=[[0,1],[-1,0]]. They satisfy A²=B²=-I and AB=-BA; their group is Q8, whose derived group is {I,-I}. Parity twists replace A,B by signed versions and preserve all these identities. These representations descend to G_2 because Q8 is metabelian.

Nevertheless their H1 on any metabelian quotient carrying them is zero. More generally, suppose a group K has abelian K' and some c in K' satisfies rho(c)=-I over C. Given a cocycle z, subtract the coboundary with vector -z(c)/2, leaving z(c)=0. For every n in K', nc=cn. Expanding both sides gives z(n)=-z(n), hence z(n)=0. For arbitrary g in K, gcg^-1 lies in K', and expanding its cocycle gives

    0 = z(gcg^-1) = (I-rho(gcg^-1)) z(g) = 2 z(g).

So the normalized cocycle vanishes everywhere; the original was a coboundary. This proves H1(K,V)=0 with its coefficient hypothesis, not a general statement about all metabelian coefficient systems.

There is also a one-relation certificate for the present doublet. Since A-I is invertible, every class on F has a unique representative with z(a)=0 and arbitrary z(b)=v. For c=[a,b],

    rho(c)=-I, z(c)=(A+I)v,
    z(a c a^-1)=A z(c),
    z(r)=z([c,a c a^-1])=2(I-A)z(c)=4v.

Every metabelian quotient imposes r=1. This forces v=0, removing the entire two-dimensional H1. Each of the three parity doublets obeys the same formula, so the complete algebraic six is lost, even though its Q8 point survives. The signed relation has a concrete effect in the record's own coefficient module.

## The full algebraic six does not require all of F2

Q8 has derived length two, so the general bound proves that G_3 retains every doublet cocycle, every coboundary, and hence H1 exactly. On F, generator values z(a),z(b) are arbitrary vectors in C². Coboundaries have dimension two because A-I is invertible. Thus H1 has dimension two for each parity and dimension six for the three nonzero parities. The equivariant inflation above gives the same six-dimensional lifted move representation on G_3. In particular the algebraic central projectors already computed in ../bundle_transport/ have the same ranks and eigenvalues.

This is not a replacement of the surface by a solvable group in the physical model. It proves that this specific algebraic module and move action cannot distinguish F2 from G_3. It preserves neither a surface by construction nor all representations of F2. No claim about a geometric Hodge polarization or physical chiral index follows from it.

Within solvable quotients carrying the prescribed doublet and nonzero H1, derived length three is sufficient and two is impossible. The integer three in that sentence is a derived-series depth, not a generation count.

## The simpler parity modules provide a control

A nontrivial sign character chi has abelian image, so the general bound with d=1 retains H1 already on G_2. On F this H1 has dimension one: two arbitrary scalar generator values modulo a one-dimensional coboundary. On any abelian quotient carrying chi, choose an element c with chi(c)=-1, normalize z(c)=0 and use gc=cg to obtain 2z(g)=0. H1 there vanishes.

Thus the sign-character module needs depth two in this comparison, whereas the quaternion doublet module needs depth three. These are distinct coefficient constructions already present in the record. The difference explains why preserving a representation point or a parity count is weaker than preserving its coefficient cocycles.

## Foundation consequence

The positive-word requirement alone did not specify the extra reversible information. A named downstream cocycle construction now measures part of that information: it detects r but not any element of F'''. This discharges a precise dependency question and allows faithful F2 to be weakened for that algebraic construction alone. It does not derive the coefficient choice, the surface category, Λ, an end unit or an action from the principle.

The next question should concern the remaining geometric and analytic data and their physical justification, not a census of further solvable quotients. There is no claim that every mathematical or physical observable factors through G_3.
