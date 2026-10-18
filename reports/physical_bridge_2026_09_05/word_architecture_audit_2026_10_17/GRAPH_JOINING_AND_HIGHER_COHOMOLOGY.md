# Graph joining and the information needed for interactions

October 18, 2026. Analytical source audit and proof draft; awaiting
non-authoring review. No new scientific producer or test was executed.
This is not a numbered arc, accepted retraction or experimental admission.

For a specified graph of groups, edge matching and retained loop
transports give a complete representation-level joining rule. They do
not select the graph or a physical action. There is also a concrete
information-loss issue in an existing construction: B1043's presentation
complex has no third cohomology, but the full classifying space of its
triangle group has H³ = C³. Its presentation-level halt therefore cannot
exclude a group-level triple product. A nonzero product is not established
here, and B1043's received ten-class result is preserved at its declared
transport rho(t)=I.

This extends [the pairwise joining analysis](JOINING_LAW_ANALYSIS.md),
not the current seventeen-control verification package. The quantifier
is finite specified graphs with specified vertex and edge data; the
triangle is a diagnostic case, not a selector for the whole programme.

## 1. What a graph joining must retain

Let X be a connected finite graph. At each vertex v specify a group
Gamma_v; at each unoriented edge specify H_e, with injective maps
i_s:H_e -> Gamma_s and i_t:H_e -> Gamma_t. Their markings, including
any geometric gluing, are part of the input. Choose an orientation
e:s->t only to state the formulas.

For a specified coefficient group K, retain vertex representations
rho_v:Gamma_v -> K and transport h_e in K from the source frame to the
target frame. The compatibility equations are

    rho_t(i_t(k)) = h_e rho_s(i_s(k)) h_e^-1,    k in H_e,
    h_reverse(e) = h_e^-1.

Changing vertex frames by g_v in K transforms the data by

    rho_v -> g_v rho_v g_v^-1,
    h_e   -> g_t h_e g_s^-1.

Substitution in the compatibility equation proves covariance. For a
path e_1,...,e_n the transport is h_en ... h_e1; internal frame changes
cancel, leaving the frame changes at its endpoints. For a based loop
the product changes by conjugation, not necessarily to the identity.

Choose a spanning tree. Starting at one vertex, choose frames recursively
so every tree transport becomes I. For an edge directed from a previously
fixed s to a new t this means g_t=g_s h_e^-1. The vertex representations
are conjugated at the same time. With them held fixed, only their
centralizers are permissible frame changes; arbitrary tree normalization
cannot also leave every vertex matrix fixed.

In tree-normalized frames the presentation consists of the vertex
groups, identifying relations on tree edges, and stable letters on the
remaining edges. Map each stable letter to its h_e, using the displayed
orientation convention. A representation of the free product factors
through this presentation exactly when every matching relation holds.
This proves necessity and sufficiency for the specified presentation.
It is the standard graph-of-groups construction, not a new physical
postulate. The presentation and the cohomological restriction maps are
given in [Fernos and Valette, sections 1.2 and 2](https://arxiv.org/pdf/1412.3848).

### A cycle is not automatically a filled face

Take a triangle with all vertex and edge groups trivial. Its fundamental
group is Z, and after tree normalization its one remaining transport may
be any element of K. Requiring its product to be I instead amounts to
adding a relation. A disk filling that triangle would justify such a
relation; the graph alone does not.

Likewise, a Cech cocycle on actual triple overlaps uses the topology of
that cover and its overlap data. It must not be imposed on an arbitrary
assembly loop by analogy. Pure coordinate changes telescope, but a flat
bundle can have nontrivial holonomy around a noncontractible loop.

The residual data include the graph, interface maps, coefficient group,
vertex representations and compatible loop transports modulo frames.
This classification does not derive a measure on these data, a preferred
assembly, spacetime, an end law or a physical interaction functional.

## 2. The exact scope of B1043

B1043 defines an algebraic triangle because three one-cusped pieces
cannot form the proposed smooth cyclic weld using distinct boundary
tori at every vertex. Its preregistration explicitly retains that
distinction. It uses three copies of the figure-eight knot group with
identity peripheral matching, then closes the graph with one stable
letter:

    Pi = < a,b1,b2,b3,t |
           REL(a,b1), REL(a,b2), REL(a,b3),
           L1 L2^-1, L2 L3^-1,
           t a t^-1 a^-1, t L3 t^-1 L1^-1 >.

Here L_i is the specified longitude in vertex i. The representation
sets every b_i to B27, a to A27 and t to I27. The last choice satisfies
the relations; the graph does not force it. With the other matrices
fixed, other admissible t images must centralize the common peripheral
image. Their existence and effect on twisted counts are separate
questions, not computed by B1043's identity-transport run.

The source computes H¹ using Fox constraints and coboundaries. Its
received result is h¹(Pi;27)=10, split as seven connecting classes and
three bulk classes. Passing from a presentation to a classifying space
does not invalidate a group H¹ calculation: the crossed-homomorphism
equations depend on generators, relators and the representation.

W4 does something different. Its producer assigns `n_3cells = 0` for
the presentation 2-complex and prints the halt. It does not construct a
classifying space or compute the triangle group's H³. Its lock tests
the saved output strings and report phrases, not a freshly evaluated
cup product or group H³. No execution of that lock is claimed here.

Thus the literal statement H³(presentation complex;C)=0 is correct.
The extension to absence of a target on the algebraic group needs a
different argument and fails for the group specified above.

## 3. The full triangle has a third cohomology target

Let M be the compact figure-eight knot exterior and T its boundary
torus. The interior is complete hyperbolic, so M is aspherical; the
peripheral inclusion pi_1(T)=Z² -> pi_1(M) is injective. Attach three
edge cylinders T x [0,1] to three vertex copies of M with the same
peripheral identifications as B1043. Call the resulting space Y_X.

This is a graph of spaces, not the impossible smooth cyclic weld. The
same boundary torus can receive two edge cylinders in a graph of spaces;
the resulting neighborhood need not be a manifold. Van Kampen gives
exactly Pi above after choosing two edges as a spanning tree.

The vertex and edge spaces are aspherical and the edge maps inject on
fundamental groups. Hence Y_X is K(Pi,1), by
[Hatcher, Theorem 1B.11](https://pi.math.cornell.edu/~hatcher/AT/AT.pdf),
printed pages 92–95. In Hatcher's convention, subdivide each assembly
edge by a torus vertex and use its two injections. This verifies the
theorem's hypotheses without identifying the graph space with a
3-manifold. A presentation complex with the same pi_1 need not be
homotopy equivalent to this classifying space.

The remaining calculation is an application to these particular inputs,
not a claim that either primary source studied B1043. Ordinary scalar
cohomology over C is

    H^0(M)=C, H^1(M)=C, H^2(M)=H^3(M)=0,
    H^0(T)=C, H^1(T)=C², H^2(T)=C.

For M, Alexander duality for the knot exterior gives the homology of
a circle; the preferred longitude bounds a Seifert surface and is zero
in H_1(M). Consequently H¹(M) restricts to the meridian character of T.

The graph-of-spaces Mayer–Vietoris sequence has the segment

    direct_sum_v H^2(M_v) -> direct_sum_e H^2(T_e)
      -> H^3(Y_X) -> direct_sum_v H^3(M_v).

Both outside groups are zero. There are three edges, so

    H^3(Pi;C) = H^3(Y_X;C) = C³.

This conclusion is independent of B1043's 27-valued numerical output.
It follows from the peripheral graph and ordinary scalar cohomology.

### Lower degree and Euler characteristic controls

In degree zero the vertex-to-edge map is the triangle incidence matrix,
of rank two. In degree one it is the same incidence matrix landing in
the meridian component of each C², again of rank two. Exactness gives

    b0=1,
    b1=(3-2)+(3-2)=2,
    b2=6-2=4,
    b3=3,
    chi(Y_X)=1-2+4-3=0.

More generally, for a connected finite graph with V copies of this
exterior and E torus edges using these same meridian-preserving identity
maps, the incidence rank is V-1 and

    (b0,b1,b2,b3) = (1, E-V+2, 2E-V+1, E),
    chi(Y_X)=0.

These formulas include the single vertex with no edges, (1,1,0,0), and
the two-vertex one-edge double, (1,1,1,1). The latter recovers the
ordinary fundamental class of the closed oriented double. It is a
positive control against inferring group H³=0 from a 2D presentation.
Arbitrary torus markings can change the degree-one incidence map and
are not included in the displayed lower-degree formula.

B1043's particular presentation complex has one 0-cell, five 1-cells
and seven 2-cells, so chi=3. Its scalar b1 is also two: abelianizing
the vertex knot relations identifies each b_i with a, while t remains
free. Thus its b2=4 and b3=0. The spaces agree in pi_1 and scalar H¹,
yet differ in H³ and Euler characteristic. Using only the presentation
was sufficient for W1, not for the intended group-level W4 conclusion.

## 4. A target is not a nonzero interaction

Let V=27 with B1043's specified representation, and let
C:V tensor V tensor V -> C be the received invariant symmetric fibre
tensor. Because the representation preserves C, a correctly typed
candidate is

    T(alpha,beta,gamma) = C_*(alpha cup beta cup gamma)
      in H^3(Pi;C),    alpha,beta,gamma in H^1(Pi;V).

The symmetric fibre tensor does not make this total cohomological map
symmetric: exchanging two degree-one classes contributes a minus sign.
Over C it is alternating. Repeating the same class gives zero, even if
the invariant cubic on the fibre is nonzero. Physical fields or an
additional antisymmetric internal tensor may change the total symmetry,
but that additional structure must be exhibited, not presumed.

There is an immediate negative control: scalar H¹(Pi;C) has dimension
two, so its ordinary triple cup is identically zero despite H³=C³.
For the received ten-dimensional 27-valued H¹, this scalar dimension
argument does not decide the map. One must construct its cochains and
products, check coboundary independence and retain the coefficient
contraction and degree signs. H³=C³ alone neither selects a functional
on H³ nor produces a physical action, coupling value or family count.

The next admitted calculation should therefore test distinct twisted
classes on the full classifying-space model or an equivalent group
resolution. It must recover the double's scalar top class, the
triangle's scalar zero product, alternating signs, and invariance under
coboundary changes. Any nonzero output must be kept as an H³ class
before choosing how, or whether, it is physically integrated.

## 5. Preserve the later positives and narrow the old negative

The SM branch's B1271 addendum and B1273 already pursued an H³-bearing
closing. B1273 reports a nonzero mixed triple coupling on the flat
three-fold branched closing Y3, with three twisted classes, a paired
spectrum and a restrictive tree-level texture. That is prior work on a
different topology and coefficient system, not a new result of this
audit or a fresh reproduction of its producer.

B1271's epsilon contraction on rank-three coefficients illustrates why
the tensor type matters: its antisymmetric internal tensor and the
degree-one exchange sign combine differently from the symmetric 27
fibre contraction above. These two maps must not be equated because
both involve three slots. This note neither validates all later claims
in those reports nor cancels their reported positive construction.

At the fetched main pin, LAW_MAP's arity row carries the presentation
halt into a statement about the algebraic triple. THE_LADDER X24 goes
further and describes the triple pairing as an additional checked
negative. The producer halts before that pairing is evaluated. The
appropriate proposed repair is narrow:

- preserve the sealed presentation, the declared rho(t)=I and the
  received H¹ and invariant-line results;
- preserve H³=0 for the chosen 2-complex;
- do not use that halt as an exclusion of the triangle group's cubic
  target, or as an evaluated zero for its twisted triple product;
- retain the genuinely different later closing and physical-parent
  investigations.

Canonical sources, verdicts and ledgers are not overwritten by this
unreviewed note. Review and controlled verification must precede their
promotion or correction. In particular the R85/R93 joined physical
background is not Y_X: its smooth geometry, fields, action and operator
domain cannot be imported into this triangle by matching a group label.

## 6. Consequence for calculating the whole architecture

The full calculation needs the structure required by the proposed
observable, not merely more constituent words. Keep marked word maps
for composition; retain interfaces and transports for assembly; retain
the appropriate higher topology and coefficient products for
interactions. A quotient adequate for one duty can fail the next.

The graph law above completes a conditional representation-level step.
It does not establish which graphs or coefficients follow from the
foundational principle. The H³ calculation identifies a specific
over-broad exclusion worth testing, without choosing the triangle as
the programme's new root. No complete priced physical input is paid.

## Source custody and review status

Source pins after fetching all configured remotes on October 18:
main `2e5716bd9bea013d69f3cd733f083b61a6f59dbd`; SM
`11ec0144ef25e8848968b909735c205809567fdf`; local checkpoint before this
note `5e0dbc1468242d7a7e6ec8e2677dec98c07abaa4`.

Personally read B1043's complete FINDINGS, PREREGISTRATION, producer,
saved output, verdict and lock. Main/local producer blobs agree at
`9d0e9f912690e2993b12ad1d5d59c11ce9f8a0da`; lock blobs agree at
`bc9582f2bdda58cc0084991d82ed106c0c5d061d`. The producer imports the
older B632 machinery by execution; it was read, not imported here.

Personally read B1036 FINDINGS, B1271's September 6 prior-art addendum,
B1273 FINDINGS, B1062 and B1177 FINDINGS, and the existing R85 and R93
proofs. B632's first 160 lines were inspected for the tensor setup,
not its complete derivation or execution. The targeted main/SM/chat1/
fork/archive searches for B1043, arity void, classifying-space and H³
language are not an exhaustive deleted-history absence certificate.
No claim of novelty or of no possible successor is made.

Primary reading: Hatcher's graph-of-groups discussion, Theorem 1B.11,
its examples and proof, printed pages 91–95; Fernos–Valette sections
1.2 and the relevant section 2 presentation and cohomology construction,
printed pages 2–3 and 5–9. Neither entire book nor entire paper is
claimed read. The application and proof draft above require independent
review. No new scientific test pass, certified count, physical chiral
spectrum or programme-wide exclusion is asserted.
