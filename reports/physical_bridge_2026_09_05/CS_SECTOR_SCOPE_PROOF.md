# R82 authored argument: background blindness versus field dynamics

Pre-execution. Standard Chern-Simons mathematics, not a novelty claim.

## C1. Preserve the exact scalar result, change its type label

B1012 substitutes the geometric flat connection's invariant into

    S_geom=-k*CS_geom-sigma*Vol.

When the chosen lift has CS_geom=0, this number is independent of k.
That is a derivative with respect to a coefficient AFTER evaluating
the fields. It says nothing by itself about field derivatives or an
integral over configurations. Even abstractly, S(q;k)=k*q^2 has
S(0;k)=0 and d_q S(0;k)=0 for all k, but Hessian2k.

B1226 already withdrew the equivalence CS=0 iff amphichiral; its
quarter-lattice controls and the surviving value calculation are not
recomputed here. B813/B1226 already distinguish a coupling coefficient
from a functional value. R60 already verifies an action with a nonzero
boundary variation. R82 connects these existing distinctions to B1064's
sector-deletion step; it does not erase the original scalar calculation.

## C2. A local fluctuation works about any smooth flat connection

For an oriented regulator with a smooth matrix connection C, let

    Q(C)=integral tr(C wedge dC+(2/3)C wedge C wedge C).

Invariant trace and the graded Leibniz rule give

    Q(C+a)-Q(C)=integral[2tr(a wedge F_C)+tr(a wedge d_C a)
                       +(2/3)tr(a wedge a wedge a)]
               -integral_boundary tr(C wedge a).

With C flat and a compactly supported in an interior ball, the first
and boundary terms vanish. In that simply connected chart use a smooth
parallel frame, C=0. The fluctuation constructed in this frame is a
bundle-valued one-form in the original frame; it extends by zero
because its support stays strictly inside the chart. It changes no
end data or holonomy at the boundary. It is NOT globally flat.

Choose a nonzero C-infinity real bump f, T=diag(i,-i), and

    alpha=dz+x dy, a=epsilon*T*f*alpha.

The three-form alpha wedge d alpha=dx wedge dy wedge dz. Also
alpha wedge df wedge alpha=0 and a wedge a=0. Consequently

    tr(a wedge da)=-2 epsilon^2 f^2 dx wedge dy wedge dz,
    tr(a wedge a wedge a)=0,
    Q(C+a)-Q(C)=-2 epsilon^2 integral f^2 <0 for epsilon!=0.

The Hessian along this actual compactly supported path is
-4 integral f^2, not zero. Curvature is nonzero: otherwise
tr(a wedge da) would vanish pointwise in the parallel frame. Gauge
transformations of a flat connection stay flat, so this is not merely
a compact or complex gauge copy of C. No numerical approximation or
smoothness at the support edge is supplied by the polynomial fixtures;
the bump-function construction establishes those facts analytically.

For a general complex simple Lie algebra replace the matrix trace by
a fixed nondegenerate invariant bilinear form and select T with nonzero
pairing with itself. The same construction applies. In B715's supplied
principal sl2 inside E6, the adjoint weights of i*diag(1,-1) are
i*(2m-2j), m in{1,4,5,7,8,11}, j=0,...,2m. Their squared trace is
-7488, hence also nonzero. This uses its known principal decomposition;
it neither derives the gauge group nor replaces the actual global
geometric holonomy by a compact one.

The overall 1/(4pi), trace convention and sign converting the usual
functional to B1012's geometric invariant do not affect nonvanishing.
In the usual complex action, the real part has integer coefficient and
the imaginary part has continuous coefficient. Our real change affects
the former. A change small enough to be less than one gauge period is
not removable by a large-gauge shift. A physical integration contour
could restrict the allowed path; it must be stated before reusing this
as physical evidence. We establish a property of the full functional,
not that every physical contour includes this particular path.

## C3. Reflection pairs configurations; it does not zero them individually

On an oriented manifold, an orientation-reversing diffeomorphism r obeys
Q(r* C)=-Q(C), with the usual lift/boundary qualifications. This can
relate two distinct configurations. It cannot force Q(C)=0 for a field
not fixed by r up to an admissible gauge equivalence. The contact-form
pair has equal and opposite nonzero integrals. Replacing the whole
configuration space by individually mirror-fixed fields is an additional
restriction, not a consequence of amphichirality of the base.

Opposite control: C=T*d phi is abelian pure gauge locally and has F=0,
Q=0. Nonzero fields alone do not suffice; the contact fluctuation's
nonzero curvature and quadratic pairing matter.

A periodic comparison, not the actual m004 background, is flat T3 with
x,y,z of period2pi, C=epsilon*T*(cos(x)dy+sin(x)dz). Its Q density is
2epsilon^2 and Q=2epsilon^2(2pi)^3, although the reference C=0 has
Q=0. The local-bump argument above, not this different manifold, proves
the result near the actual geometric connection.

## C4. The correct physical verdict is underdetermination, not attachment

The functional form and distinctions are already explicit in
[Witten, equations2.1--2.5, section4.2.4, section5.1.2](https://arxiv.org/html/1001.2933v4).
Only these and section2.2 were personally read in this pass. His
fluctuation expansion separates a saddle phase from its neighborhood;
it is not a calculation of our E6/m004 boundary theory or a selected
Origin Axiom contour. We do not transfer closed acyclic-bundle formulas
onto a cusped, reducible or singular case.

B1064 leg1 cannot establish deletion of the integer-level functional
from CS_geom=0. Its leg2 still records no supplied rational chiral
algebra attachment. No such attachment is constructed here, and no
central-charge identity becomes a derived physical relation. B1012's
critical-value k-blindness survives. Its extension to all fluctuations,
all spectral information or all quantum observables is not licensed.

Nor does nonconstant Q automatically prove a final partition function
depends on k: measure, contour, cancellations and normalization matter.
Compute an actual gauge-invariant observable with declared boundary
conditions and both level coefficients before claiming physical contact.
Preserve the distinction between this three-dimensional CS action and
the externally supplied seven-dimensional parent and CS superpotential
of our R60/R81 models. They are not interchangeable theories.

The bounded positive is removal of an over-wide premise closing a
physics route. It is not physical chirality, a quantum theory derived
from genesis, the Standard Model, gravity or a TOE. Authored analytic
and physical-scope review remains owed independently of finite controls.
