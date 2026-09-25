# R48: the conormal map on the actual canonical background

Authored pre-execution argument, September 25, 2026. Conditional on the
named external theorems and inherited R42/R44 applications; not independent
specialist acceptance. Finite tests control formulas, not global geometry.

## 1. Hypotheses, and the step that algebra alone does not give

Fix q>0, q!=1 and the literal real SL4 representation rho_q. Ballas--Long
Theorem 3.3 supplies a properly convex invariant domain and discrete faithful
holonomy; Theorem 4.3 supplies Zariski density. R44's sections 2--3 argue
that ANY invariant proper convex domain for this literal representation
has one type-one generalized cusp and a compact complement. That authored
application, including its external relative compact-core input, is retained
as a load-bearing premise. It is not recertified by this finite suite.

The fundamental group is relatively hyperbolic with respect to its maximal
Z2 cusp subgroup: use its original finite-volume hyperbolic realization,
not a claim that the new metric is hyperbolic. There are nonperipheral
elements. The type-one model B_b in R44 has ideal boundary a projective
segment. To check the last statement directly, homogenize

    z>0,  x0 + c log z - y^2/2 > b,     c>0.

At projective infinity its closure has y=0 and x0,z>=0; every ray in that
two-coordinate quadrant is approached from B_b. Thus the end flat is the
closed segment between e0 and e1, not a two-dimensional face. The sandwich
in R44 transfers the same ideal segment to each actual lifted cusp.

R47's exact symmetric S(q) obeys

    rho(g)^(-T) S = S rho(theta g),
    det S = -q(q^2+q+1)^3/[16(q+1)^4] < 0.                 (1)

Here theta inverts both marked generators. The relator is preserved by
theta up to conjugacy and inversion, and theta squared is identity.
The transformed dual domain S^-1 Omega* is therefore invariant under the
SAME image group. This fact alone does not make it equal to Omega.
The ellipsoid countercontrol in the tests deliberately separates them.

## 2. Why these domains are minimal, hence unique

External input: Cooper--Tillmann, arXiv:2009.06569v1, Theorem 3.5 on printed
p.12. Its hypotheses are a properly convex manifold without boundary,
all ends generalized cusps with compact boundary, relative hyperbolicity
with respect to the ends, and a group not exhausted by peripheral groups.
Section 1 pays these hypotheses through R44 and the original group marking.

We use the statement's parts (1)--(3), (9) and (10): all boundary flats are
contained in the pairwise disjoint end flats; the strongly hyperbolic fixed
points X are dense off those flats; int(CH X) is the unique minimal nonempty
invariant properly convex domain. This is a STATED EXTERNAL theorem, not a
finite computation or a result newly discovered here. The full thirteen-page
preprint was read personally. Its printed proof is terse and its final
paragraph switches to the notation Fr(Omega0); we do not advertise our
reading as an independent proof of its density statement on Fr(Omega).
That exact statement is an explicit review dependency, not an implicit
replacement by the easier closed/strictly-convex uniqueness theorem.

Here there are countably many lifted end flats: Gamma is countable and
there is one cusp orbit. Each is a closed line segment in Fr(Omega), a
topological two-sphere. Each has empty relative interior. The Baire theorem
therefore makes their complement dense in Fr(Omega). The cited density
of X on that complement gives closure(X)=Fr(Omega). In a bounded affine
chart, convexity now gives

    Omega = int(CH X).                                    (2)

For precision, the closed convex hull of X is cl(Omega); a full-dimensional
convex set and its closure have the same interior. The assertion is not
that X equals the boundary, or that the boundary contains no segments.

The same argument applies to S^-1 Omega*: it is an invariant proper convex
domain for the literal image group, so the any-domain cusp/core result of
R44 applies again. Both are therefore the unique minimal invariant domain:

    S^-1 Omega* = Omega.                                  (3)

This argument would require repair for codimension-one end flats with
interior in the boundary, or for a quotient with unaccounted ends. Neither
general finite-volume uniqueness nor all-class uniqueness is being assumed.
The Baire step is analytical/topological; the finite controls do not test it.

## 3. An actual self-isometry and its orientation

Let C be one cone over Omega and L its complete Cheng--Yau affine sphere,
with mean curvature -1. Equation (3) lets us choose the overall sign of S
so S(C)=C*. Set B=S/abs(det S)^(1/4). Then B is symmetric, det B=-1, and
B(C)=C*. Absolute volume preservation suffices for the canonical affine
metric; no positive-definiteness of S or B is claimed.

External input: conormal duality of complete affine spheres, in Loftin's
Survey on Affine Spheres, Propositions 4,5,8 and Theorem 3 (printed pp.12--13,
17--18,21); also the already received 2001 affine-sphere construction. The
conormal map nu:L->L* is characterized by

    nu(f)(f)=1,  nu(f)(df(v))=0,
    dnu(v)(f)=0,  dnu(v)(df(w))=-h(v,w).                   (4)

It is a diffeomorphism and a Blaschke isometry, and dualizes the cubic
tensor's sign. Since B maps normalized affine spheres to normalized affine
spheres, define phi=B^-1 nu:L->L. Radial projection gives a proper complete
self-isometry of Omega, with

    phi(rho(g)x)=rho(theta g)phi(x).                       (5)

Thus it descends to the quotient with the correct group automorphism.
Conormal duality is involutive and is contragrediently equivariant under
linear maps. Hence phi^2=B^-1 B^T=I, not just identity on cohomology.

The coefficient metric H is R42's 1 plus h under (s,v)->s f+df(v).
Equation (4) sends an h-orthonormal affine frame to its dual frame with
three tangent signs reversed. Its ambient determinant sign is (-1)^3.
Multiplication by B^-1 contributes det-sign -1. Thus phi preserves the
orientation of the three-dimensional base. This also follows from the
leading cusp control below; that control alone is not the global proof.

## 4. Positive coefficient norms: no borrowed old-base uniqueness

In an oriented h-orthonormal frame F=(f,df(e1),df(e2),df(e3)), H=F^-T F^-1.
The conormal frame is F^-T diag(1,-1,-1,-1), so its positive coefficient
metric is H^-1. Consequently the actual metrics satisfy

    H_(phi x) = B^T H_x^-1 B.                             (6)

This proves that B: E_(phi x)->E_x* is unitary. It is not a claim that
the indefinite bilinear form B itself is a positive metric. Complexify
the metrics and choose J=exp(i*pi/4)B, giving det J=1 without changing
unitarity. The irrelevant choice among fourth roots is a volume phase.

For a scalar mu4 character chi, chi(theta g)=chi(g)^-1, so (1) also
intertwines rho_chi. These unit phases do not change H. On p-forms set

    U alpha = J phi*alpha.

U is complex linear, same-degree and unitary from the E_chi Hilbert complex
to its actual dual's complex. Flatness gives U d_E=d_E* U on smooth compactly
supported forms. Properness preserves compact supports; unitarity transports
graph closures and adjoint domains, hence

    U d_E^dagger=d_E*^dagger U,  U Delta_E=Delta_E* U.       (7)

This is the complete-domain equality, not a formal matrix transpose of an
unbounded operator. It pairs all spectral measures and harmonic spaces.
The same construction applies to induced tensor/exterior/adjoint bundles.
No spectral gap in the neutral channel is needed for (7).

## 5. The local end check is a shear, not a false coordinate obstruction

The product cone in R44 has u proportional to z^(1/4) r^(3/8),
r=x0-y^2/2. Its projective conormal is proportional to

    (1, 2r/(3z), -y, x0).

Composing with the matrix exchanging coordinates 0 and 3 gives
(x0,z,y)->(x0,2r/(3z),-y). In R=r, y=x, z=exp(-4kt), this is

    (log R,x,t)->(log R,-x,-t-log R/(4k)-log(2/3)/(4k)).

It preserves the leading canonical product metric

    (15/64)d(log R)^2 + (3k/4)d(log R)dt
          + 3k^2 dt^2 + (3/8)R^-1 dx^2.

The simple flip without the logarithmic shear does NOT preserve its mixed
term. This failure cannot kill the actual conormal map. The formula is a
product-cone control, not the exact global map for S(q) or a new boundary
condition. The global argument is (3)--(7), not an asymptotic guess.

## 6. Whole interaction and the scope of the physical consequence

The induced exterior-square map is unitary. The epsilon-volume tensor K
satisfies (wedge^2 J)^T K(wedge^2 J)=(det J)K=K. The phase and determinant
factor must be retained before normalization. Orientation preservation makes
the Hodge star commute with pullback. Thus the whole normalized classical
four--four--six tensor is paired, not just one selected overlap.

F14's parent extension is reused with explicit credit. In the standard E8
root coordinates with D5 on axes 0--4 and A3 on axes 5--7, the simultaneous
sign flip on axes 0,5,6,7 is the product of reflections in
e0+e5,e0-e5,e6+e7,e6-e7. It exchanges the D5 spinor halves and dualizes A3.
The full root-set and reflection identities are checked again here using
the actual R38 root generator. A compact Weyl lift preserves the bracket
and invariant norm. Combined with (6) it acts on the source-free supplied
parent, not just on an unembedded coefficient name.

R46 establishes the L2 bilinear source and positive six-sector gap at the
exceptional points on THIS canonical background. For the correctly paired
source j, (7) and the spectral calculus therefore give the finite equality

    <U6 j,(p^2+2 Delta6_dual)^-1 U6 j>
       = <j,(p^2+2 Delta6)^-1 j>,  p^2>=0.                 (8)

The whole mediator is transformed. Neither (8) nor a nonzero test-vector
control computes the actual global source j or shows it is nonzero.

If the stated hypotheses hold, canonical geometry does not by itself
remove the paired classical spectra/responses of this curve. That is a
same-background constraint and a constructive symmetry, NOT a physical
CP/parity identification or a universal chirality no-go. Spontaneously
asymmetric phases, changed end/source data, different coefficients and
components retain their separate duties. F15--F17 are not premises of
this proof; their newer claims have not been independently rerun here.
The R40/R41 nonsplit/source route remains distinct and is not closed.

## Primary sources and scope

- Cooper--Tillmann (2020 preprint), Theorem 3.5, full source personally read:
  https://arxiv.org/abs/2009.06569v1 . No journal publication is asserted.
- Loftin, Survey on Affine Spheres, cited complete sections personally
  reread; the conormal isometry is credited, not rediscovered:
  https://sites.rutgers.edu/john-loftin/wp-content/uploads/sites/229/2019/08/as-survey.pdf .
  Its received URL and PDF hash are also fixed by the R42 input receipt.
- Ballas--Long, AGT 15 (2015), Theorems 3.3 and 4.3, received/read at R43:
  https://msp.org/agt/2015/15-5/agt-v15-n5-p16-s.pdf .
- R42/R44/R45/R46 and R47's F14 reading copies are hashed inputs. Their
  analytic and external-input limitations remain part of this statement.
