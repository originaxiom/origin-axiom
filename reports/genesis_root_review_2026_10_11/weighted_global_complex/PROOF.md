# The complete positive flag complex and its compact core

October 13, 2026. Authored analytic argument, not an independently certified theorem. The exact computation accompanying it checks its finite cochain model and algebraic inputs, not the functional analysis. The scope is the supplied nonsplit m135 coefficient, its exterior square and their duals, on the specified complete one-cusp background. It is not a conclusion about all Origin Axiom realizations or all physical chirality mechanisms.

## Inputs and the question

The [noncompact admission argument](../noncompact_admission/PROOF.md) supplies a smooth harmonic metric H_b bounded above and below by the reference K_b for each b>0. The [transport argument](../kernel_transport/PROOF.md) identifies their maximal and minimal differential complexes and reduced cohomology, including induced tensor coefficients. It also removes the positive numerical amplitude from the multiplicity question. Neither prior argument computes those multiplicities or establishes closed range.

Use the complete base metric g=dr^2+exp(-2r/ell)h_T on a whole torus end, ell>0. In a common temporal flat frame, D=dr wedge partial_r+D_T, where D_T is independent of r and preserves the peripheral flag splitting. On W,

    K_b(r)=exp[-2r A + ell b (exp(2r/ell)-1) Xi],
    Xi=diag(1,1,1,1,-4),
    spec(A)=(1,0,0,-1,0)/ell,       [A,Xi]=0.

This is the temporal-frame formula already checked in the transport packet. D_T need not commute with A or with the metric. The splitting is peripheral, not a global direct-sum decomposition of the nonsplit flat bundle. The same distinction applies to its tensor powers.

Write E=E_+ plus E_- on the end by the sign of the induced Xi eigenvalue q. There is no zero q in the four coefficients considered here:

| Coefficient | Growing E_+ | Decaying E_- |
| --- | --- | --- |
| W | V, rank 4, q=1 | line, rank 1, q=-4 |
| exterior-square W | exterior-square V, rank 6, q=2 | V wedge line, rank 4, q=-3 |
| W dual | dual line, rank 1, q=4 | V dual, rank 4, q=-1 |
| exterior-square W dual | dual of V wedge line, rank 4, q=3 | dual of exterior-square V, rank 6, q=-2 |

Neutral sectors of the larger parent can have q=0 and are not covered by this end contraction. Their omission here is a scope boundary, not a claim that the physical parent contains only these coefficients.

## Bounded contraction of the radial complex

For tangential form degree j in {0,1,2}, in a joint A and Xi eigenvector with eigenvalues a and q, the scalar L2 density, apart from a constant factor, is

    w_(j,a,q)(r)=exp[2((j-1)/ell-a)r + ell b (exp(2r/ell)-1)q].

The same weight applies with a preceding dr. Put phi=log(w)/2. Then

    phi'(r)=(j-1)/ell-a+bq exp(2r/ell).

There are finitely many a,q and three tangential degrees. Since b>0 and q is never zero, a sufficiently large R makes phi' at least eta>0 on E_+, and at most -eta on E_-, uniformly in those choices.

On E_+ define K_infinity(alpha+dr wedge beta)=-integral_r^infinity beta(s)ds. After conjugation to unweighted L2, its kernel has norm at most exp[-eta(s-r)] for s>=r. Both Schur integrals are at most 1/eta, so K_infinity is bounded in every degree. The term with constant tangential coefficients is not L2. Distributionally,

    D K_infinity + K_infinity D = I.

One can first prove the identity on smooth compactly supported forms and then on the maximal domain by the weak one-dimensional integration formula. In the latter argument the possible tangential constant at infinity vanishes: pairing with a smooth torus test form, square integrability with the growing weight forces a subsequence of the coefficient to zero. The same identity then supplies D K u in L2 from u and Du; it does not require separately bounding every tangential and radial derivative.

On E_- use K_R(alpha+dr wedge beta)=integral_R^r beta(s)ds. The conjugated kernel has the same exponential bound for r>=s>=R. To avoid unbounded point evaluation, average R over a fixed smooth unit-mass density supported in a finite regular slab. On that slab all weights are equivalent; outside it the preceding Schur bound applies. Denote the averaged operator by K_0 and the averaged tangential trace, extended constantly in the temporal frame, by P. Constant tangential forms of every degree are L2 for q<0, so both the extension and P are bounded. They commute with the r-independent tangential complex, and

    D K_0 + K_0 D = I-P.

Here P kills the dr component; its coefficient is the averaged tangential component. Integration commutes with D_T because D_T is r independent and preserves E_-; no commutation with A is used. These identities hold on the maximal domains. Thus the end complex is boundedly chain-homotopy equivalent to the ordinary torus complex with E_- coefficients. The E_+ part is acyclic, with bounded primitive.

This argument does not extend through b=0, to a reversed flag, or to q=0 merely by continuity. It does not assume a finite total harmonic-map energy.

## Joining to the core and closed range

Cover the complete manifold by a relatively compact core U and a tail V with overlap a finite product collar. Choose a smooth partition of unity with bounded derivatives, supported away from the artificial edges. Restriction gives the de Rham Mayer-Vietoris sequence of maximal graph domains. It is degreewise split by bounded partition-and-extension maps: multiplying by a partition function and extending by zero across the edge where it vanishes is bounded both in L2 and graph norm. The usual mapping-cone homotopy for this split exact sequence therefore identifies the global complex, by bounded chain maps and homotopies, with the homotopy fiber of

    C(U;E) plus C(V;E) --> C(U intersect V;E).

The just-proved tail contraction replaces C(V;E) by C(T;E_-). Radial contraction on the finite collar replaces the overlap by C(T;E). U can be treated as the interior of a compact smooth core with its maximal complex. Its absolute complex, and the torus complex, have finite-dimensional cohomology and bounded Hodge contractions.

The compact input here is [Vertman, Theorem 3.2](https://msp.org/gt/2009/13-4/gt-v13-n4-p04-p.pdf), printed pages 1991-1994 for the setup, theorem and proof. It applies to flat complex bundles with arbitrary smooth Hermitian metrics, not just unitary monodromy: minimal and maximal complexes are Fredholm and compute relative and ordinary cohomology. The four complete relevant pages were read and visually inspected. We use the absolute compact theorem and the explicit end homotopies above; the paper is not being cited as a theorem about our superexponential noncompact metric.

Consequently the global complex is boundedly chain-homotopy equivalent to a finite complex. This implies closed ranges, not only finite reduced cohomology. For clarity, reduce that finite complex once more to its cohomology, with zero differential. The resulting bounded maps p,i and h satisfy I-ip=Dh+hD. On closed vectors, the exact subspace is ker(p), and u in that kernel has the bounded primitive h u. The exact subspace is therefore closed in the closed-vector subspace, hence in the ambient Hilbert space. Harmonic representatives identify ordinary and reduced L2 cohomology. The existing H_b/K_b norm comparison transports all these conclusions to H_b.

No compact-resolvent assertion for the complete operator follows solely from this argument. The conclusion is a Fredholm Hilbert complex with finite harmonic kernel and a gap off zero; it does not determine its positive spectrum.

On smooth cochains the resulting complex is

    Cone[C(core;E) plus C(T;E_-) --(res-inclusion)--> C(T;E)][-1].

Equivalently, cancel the full decaying torus subcomplex, not just its harmonic degree-one part. The answer is

    Cone[C(core;E) --project_+ res--> C(T;E_+)][-1].

This also describes relative tangential trace in E_+ and free tangential data in E_-. It is a coefficient-wise boundary rule on the entire torus; it does not divide the torus into discs or select a subspace of its H1 by a target particle count. Projection is only applied after restriction to the boundary. It is not commuted through the globally nonsplit core connection.

## The actual cellular restriction

Use the supplied marked mapping torus of the punctured torus, with generators a,b,t, relators taTbba and tbTbbabbab, and boundary words p=abAB, q=abt. Capitals mean inverses. Its compact core retracts to the mapping torus of a two-petal graph, giving cochain dimensions (n,3n,2n) for a rank-n coefficient. Define

    B=column(rho(a)-I,rho(b)-I,rho(t)-I),
    F=column(Fox(relator_a),Fox(relator_b)),
    P=rho(p), Q=rho(q), T=rho(t),
    D_T=column(P-I,Q-I), G_T=(I-Q, P-I).

The full restriction is R0=I, R1=column(Fox(p),Fox(q)), and

    R2=-Q (Fox_a(p) T^-1, Fox_b(p) T^-1).

This R2 is reused with attribution from [the earlier full boundary complex proof](../../silver_boundary_complex_2026_10_04/PROOF.md), not obtained by choosing a solution to a matrix equation. For phi(a)=ABB, phi(b)=BABBABB and c=ab, free reduction gives phi(p)=c^-1 p c. The boundary commutator is c r_p^-1 c^-1, where r_p=t p T phi(p)^-1. Expanding r(uv)=r(u)phi(u)r(v)phi(u)^-1 supplies the Fox row and fixes the sign. The producer checks the word identities, R1 B=D_T, R2 F=G_T R1 and F B=G_T D_T=0.

Let S_+ select the positive coefficient basis and m=rank(E_+). In that boundary coefficient, set f0=S_+, f1=diag(S_+,S_+)R1, f2=S_+R2 and let D_+,G_+ be its torus differentials. The quotient cone has dimensions (n,3n+m,2n+2m,m), with

    d0 = column(B,f0),
    d1 = [[F,0],[f1,-D_+]],
    d2 = [f2,-G_+].

All ranks are to be computed exactly, without inferred dual counts. A second implementation constructs the full fiber with C(T;E_-) and its NONZERO differential. Both must agree in every cohomology degree. The earlier selective comparator attached a closed graded subspace with zero differential; that different input is not reused here.

For any flat torus coefficient chi(T;E_+)=0; the core here also has chi(core;E)=n(1-3+2)=0. Hence this whole-torus model has chi=0, independently of the computed ranks. This does not by itself imply equal H1 counts in a coefficient and its dual: H0 and H3 must also be retained. The split controls in particular must not be assumed to have vanishing endpoints. Poincare-Lefschetz pairing predicts h^k(E)=h^(3-k)(E dual), with dual weights reversed; the numerical ranks test that identity rather than use it as input.

## What the result can mean physically

For the complete de Rham operator Q_H=D+D_H*, its kernel is the direct sum of harmonic degree spaces, because its global squared norm is ||Du||^2+||D_H*u||^2. A local mixed-degree Cauchy solution need not extend to such a global kernel vector. The finite complex counts the latter mathematical spaces under this parent/operator interpretation, not automatically Standard-Model multiplets.

The end class, parent action and dictionary linking this construction to the weave remain supplied. The split coefficient is a topological and detector control; the nonsplit stability proof does not admit a global harmonic metric on it by the same argument. No failure or success of this one supplied flag completion is a universal verdict on chirality, the compact selected boundary comparators, or the programme's other physical constructions.
