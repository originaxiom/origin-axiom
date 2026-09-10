# Asselmeyer--Maluga papers: direct reading and transfer audit

Started 2026-09-09 UTC / September 10 local, at the user's request.
Status: IN PROGRESS. This is not yet a completed literature audit,
a novelty certificate, or a physical derivation.

## Custody and method

The supplied `asselmeyer_maluga_papers.zip` contains a README, an ID
list and sixteen PDFs, totaling 448 PDF pages. All archive integrity
checks passed. Its SHA-256 is
`7f792dfb85dbdf5a700ae90368734a1e1bfd952d493d07e813c37cdb865223e5`.
It was extracted into a fresh sibling directory
`asselmeyer_maluga_read.SwjyZb/am/` under the supplied temp001 directory.
No existing file was overwritten. PDFs stay outside the repository;
the repository will hold our own reading notes and exact file hashes.

Read the papers, not only the archive's summary or the other seat's
review. Separate standard mathematical tools, the authors' physical
identifications, and an actual transfer to the source/domain/gauge
construction in this branch. A matched integer or Lie-algebra
dimension is not a map. A flaw in one inference does not kill the
remaining mathematics. Any new two-outcome numerical/symbolic probe
will be separately designed and sealed before execution.

The current index-stability path remains registered in
INDEX_STABILITY_PRIOR.md; its science has not run. The paper read
will inform that path, not silently replace it.

## Reading coverage (PDF pages, not keyword hits)

| arXiv ID | pages | direct coverage so far |
|---|---:|---|
| 1910.09966 | 37 | complete, 1--37; diagrams on 5--8 visually inspected |
| 1601.06436 | 52 | complete, 1--52, including appendices; equations on 29/33 visually checked |
| 1502.02087 | 27 | complete, 1--27, including appendices |
| 1006.2230 | 32 | complete, 1--32, including appendices |
| 1003.5506 | 16 | complete, 1--16, including appendices and references |
| 1401.4816 | 21 | complete, 1--21; compared boundary argument with 1502.02087 |
| 1811.04464 | 11 | complete, 1--11, including final figure-availability page |
| 1709.03314 | 36 | complete, 1--36, including appendices and references |
| 1801.10419 | 15 | complete, 1--15; printed time expression on 8 visually checked |
| 1812.08158 | 23 | complete, 1--23; equations on 8/9/19 visually checked |
| 1112.4882 | 24 | pending |
| 1211.3012 | 16 | pending |
| 1107.3458 | 35 | pending |
| 1105.1557 | 18 | pending |
| 1001.0882 | 31 | pending |
| 0904.1276 | 54 | pending |

## Questions to settle from the bodies

1. Does the spinor/immersion construction deliver our charged
   four-dimensional chiral modes, or a different boundary Dirac problem?
2. Which framing/APS/Chern--Simons data are genuinely intrinsic, and
   which need a filling, a spin structure, a reference or a normalization?
3. What do branched covers and four-dimensional smoothness prove about
   existence, versus physically selecting a geometry or three families?
4. Are the claimed gauge groups produced with brackets and faithful
   actions, or only with counts of isotopy classes?
5. Can the skein/quantization machinery connect to an already banked
   object, with its deformation parameter and Hilbert structure priced?
6. Which scale formulas follow mathematically, and which additional
   identifications carry their empirical interpretation?

No external contact, main merge, B allocation or publication of the
supplied papers is performed by this reading.

## Direct notes: 1910.09966v1 (2019)

The first complete read distinguishes six different bridges. Sections
2--3 use branched covers, a proposed K3 spacetime and a chosen cork;
4.2--4.3 introduce spinors through immersions; 4.4 turns a CS flow into
an instanton equation and then proposes a gauge group; section 5
identifies a framing defect with charge; section 6 invokes skein
quantization; sections 7--8 propose arithmetic and generation links.
These are not a single proved physical construction.

Useful mathematical routes to investigate directly:

- Pages 18--19, equation (19): CS gradient flow on a product cylinder
  and (anti-)self-duality in four dimensions. This is a possible source
  of actual curvature dynamics, distinct from treating a geometric CS
  saddle value as a quantum level. The equality with a Yang--Mills
  norm is restricted to the self-dual sector; extending a stationary
  identity to the entire action needs its own argument.
- Pages 25--27, equation (22): a relative Pontryagin/signature defect
  with a framing. Investigate its independence from a filling with
  that framing held fixed. This may help organize boundary response;
  it is not yet a Maxwell-charge map or a source-selected framing.
- Pages 27--28: the surface character variety and Kauffman-bracket
  skein algebra are concrete mathematical objects. Their standard
  deformation quantization is a candidate comparator to the repo's
  trace/character face, with parameter, real form and Hilbert-space
  choices still to pay.
- Pages 5--8: branched-cover existence and moves give a way to build
  candidate cobordisms. A theorem representing already-given manifolds
  does not select which filling or spacetime occurs physically.

Important statements to verify before import, not a universal dismissal:

- Page 5's `4g` branch count and claimed degree-three self-cover of a
  knot complement need checking against Riemann--Hurwitz and normalized
  hyperbolic volume. Page 7's printed Hopf-link presentation includes
  an unused generator. The relevant PDF pages were visually inspected
  so these are not assumed extraction errors.
- Pages 9--10 invoke Yau to select a simply connected Ricci-flat
  four-manifold, but reference [35] is a compact KAHLER theorem. The
  missing geometric hypotheses and the smoothness bound's attribution
  must be checked. A smoothness restriction alone is not a generation
  index.
- Page 15 treats self-intersection numbers as double points of immersed
  representatives. Intersection form, Euler number of the normal bundle
  and actual immersion double points must be kept distinct.
- Pages 16--17 explicitly offer two spinor embeddings and choose the
  left-handed one. The displayed harmonic equation is then described
  as parallelism. Read Friedrich [51] for its actual hypotheses;
  neither chirality selection nor normalizable localized modes follow
  from selecting a column of a spinor bundle.
- Pages 20--21 match counts of proposed isotopy classes to generator
  counts 1,3,8. No faithful bracket/action is exhibited there; a scalar
  traced quadratic action is also not literally a Cartan element.
  Any useful topology must survive a separate Lie-algebra identification.
- Pages 23--27 pass from Maxwell flux to Dehn twists, identify the
  modular S operation as a twist, and identify a Hirzebruch defect with
  electric charge. Page 26's quotient `mod 3Z` does not itself specify
  the seven displayed integer representatives or the normalization e/3.
  The framing and duality argument needs the original Atiyah source.
- Section 7, page 29, explicitly names the figure-eight and arithmetic
  Kleinian groups but ends with future work on fermion properties.
  This is relevant prior art; it is not a completed McKay/E6 map.
- Section 8, page 30, explicitly marks its generation discussion as
  speculative. It changes the hyperbolic-plane matrix to an A2 matrix
  only modulo two and assumes one S2xS2 summand per generation.
  It later conflates the rank-22 indefinite K3 intersection lattice with
  a positive-definite rank-24 Niemeier lattice. These cannot be imported
  as an exact chiral three-family computation.

The claimed scale predictions will be evaluated from their dedicated
papers before an audit verdict; no current experimental agreement is
adopted from this review or from the archive README.

## Direct notes: 1502.02087v1 (2015, with Brans)

Pages 5--11 distinguish large/small exotic R4, knot sliceness and
Casson-handle constructions. The central geometric input is a compact
set not surroundable by a standard smooth ball, not the absence of
all local smooth spheres. The chosen surrounding three-manifold is
explicitly nonunique. The Whitehead-double/pretzel example and its
JSJ pieces supply concrete topology, but not an object-selected matter
configuration or a family count.

Pages 12--15 are the load-bearing action argument. The two sides of
the artificial boundary have opposite mean-curvature terms. The
spinorial Gauss relation is used with a selected chiral extension;
normal parallel transport is promoted to a harmonic/parallel spinor,
and a constrained constant-length spinor expression is varied as a
free Dirac action. Those are separate steps requiring separate checks.
The paper itself gives both possible chiral summands. Nothing here
yet computes R18/R19's complete charged Hilbert-domain index.

Pages 18--20 and appendix B discuss geon-type spin from rotations of
configuration space. This is not automatically ordinary spinor-bundle
existence or the statistics of every hyperbolic knot complement.
The cosmological dust argument uses normalized Mostow rigidity and
a chosen surrounding scale; appendix C also contains a critical-density
term depending on Hubble expansion. Its constancy needs checking,
not concealment under the word topology.

Section 5, page 21, explicitly CHOOSES interior metrics so their bulk
action integrals agree before comparing boundary actions. Section 6,
page 22, drops connected-sum extra terms and proposes a bulk extension.
Thus the paper offers an interesting boundary-action construction but
does not on these pages establish equality of full unconstrained
Einstein--Dirac theories, a dynamical source law or a physical chiral
generation count. Section 7 preserves particle-number, interaction and
which-knot duties. Those caveats matter for a fair transfer.

## Direct notes: 1006.2230v6 (2012, with Rose)

Sections 2--4 price topology, smoothness, metric and causality. The
Fintushel--Stern construction actually inserts S1 times a knot
complement along T3, under c-embedded-torus and fundamental-group
hypotheses. The Alexander polynomial distinguishes many resulting
smooth structures, not all knots or all smoothings. This is a real
candidate construction to compare with the repo's 4D existence work;
its choice is not a canonical selector or a count of Weyl families.

The paper's own later qualification at page 10 prevents reading
every nontrivial knot as automatically changing smooth structure.
Its page 11 statement that the standard smooth structure has zero
Seiberg--Witten invariant also needs checking against the standard K3
example before import. Footnote 3 on page 9 conflates a complement
with zero surgery; appendix A correctly gives a torus-boundary
complement, so those two objects must not be merged in our audit.

Sections 4--6 reconstruct an action through several nontrivial changes:
a chosen product metric, a total-curvature bound, a bulk-to-boundary
replacement, a fixed-length surface spinor and a selected chiral bulk
extension. Page 13's use of an 8pi torus-curvature bound must be
checked against the cited Kuiper--Meeks integral: signed Gaussian
curvature and total absolute curvature are different. A lower bound
is also not an exact value of the Einstein--Hilbert functional.

Sections 7--8 and appendix B carry the useful CS/instanton route but
also the assumptions that need payment: boundary/corner terms,
chosen compact real form, a self-dual solution rather than arbitrary
Yang--Mills fields, and extension of the tube field to the whole
manifold. The final gauge-group identification is called a conjecture
in section 9. Appendix B's minimum-CS definition must retain the
flat-connection class, trivial connection, integer lift, endpoint and
orientation choices. A minimum over flat gauge connections is not
automatically the Levi--Civita invariant of an arbitrary metric.

No author-supplied code was executed and no numerical claim was
recertified in these first three full reads. Standard-source checks
and discriminating controls remain part of the ongoing audit.

## Direct notes: 1601.06436v1 (52-page review)

Title: *Smooth quantum gravity: Exotic smoothness and Quantum gravity*.
The supplied arXiv header says v1, January 24, 2016; its title-page
date is April 23, 2018. All 52 PDF pages, including all appendices
and references, are directly read. Pages 29 and 33 were also rendered
and inspected to distinguish the printed equations from extraction
artifacts. Four complete papers now account for 148 of 448 pages.

The review makes a longer chain than the matter papers. Exotic R4
is represented through Casson handles and surrounding 3-manifolds;
a selected foliation supplies a groupoid algebra; skein quantization
is related to its proposed states; modular theory is proposed as
dynamics; a traced operator is interpreted as an action; scaling and
topological transitions are then interpreted as gravity, dimensional
reduction, measurement and cosmology. Each arrow has different data.
An operator algebra, a state on it, a Hamiltonian, a physical time and
a local gravitational field are not interchangeable objects.

Potentially reusable mathematics, still requiring primary-source
checks and a map to the repo's actual construction:

- Sections 6.3 and 9.2, pages 24--27 and 31: the surface character
  algebra, Goldman bracket, skein deformation and quantum-group
  lattice observables. The cited Frohman--Gelca torus embedding is
  especially concrete for a cusp-boundary comparator. The real form,
  star operation, positive state, representation and parameter are
  additional duties; no selected 4D quantum vacuum is yet transferred.
- Section 5, pages 14--15: Cartan/MacDowell--Mansouri formulations
  offer a typed way of comparing curvature actions. The review itself
  chooses a topological action and explicitly sets its scale to the
  Planck length. A gravity action with those inputs is distinct from
  deriving Newton's constant from the originating object.
- Section 9.1, pages 30--31: the CS gradient-flow/instanton relation
  remains useful. A self-dual gauge curvature is not by itself the
  curvature of a gravitational tetrad satisfying all Einstein equations.
  The gauge/frame identification and four-dimensional metric must
  be retained, including the self-dual restriction.
- Section 9.3 and references 74/93: Taubes/Kato analysis on periodic
  or tree-like ends may offer end-operator tools. Such ends are not
  automatically the repo's cusps with drilled source arcs. No Fredholm
  theorem can be imported without the end and domain hypotheses.
- Appendix B records the dependence of the Godbillon--Vey number
  on a foliation, not just on the underlying manifold. Its explicit
  continuous family is a useful warning against treating that number
  as already selected or quantized by topology alone.

Load-bearing claims requiring correction or a missing argument before
physical use (reading flags, not yet sealed executable results):

1. Page 13 calls the generally varying mean curvature in D psi = H psi
   a Dirac eigenvalue. A function multiplying a spinor is not generally
   a constant spectral eigenvalue. Compactness of the boundary does
   not remove that distinction or prove discrete geometry.
2. Pages 17--20 move between algebra types, modular flow, a numerical
   GV invariant and a Hamiltonian. A factor cannot have three nonzero
   central direct-summands and remain a factor; compact operators are
   not the von Neumann algebra B(H). More importantly, a cyclic
   cohomology class or its numerical pairing is not automatically the
   self-adjoint modular generator. The required spectral data and
   state dependence are not supplied by a matched label.
3. Page 20's claim that every SL(2,C) representation defines a
   hyperbolic structure fails for the trivial representation. The
   repeated claim of a unique lift must retain the spin/lift choices.
   Wilson-loop functions and skein elements are not automatically
   normalized positive linear functionals on a C*-algebra.
4. Page 24 calls a general surface fundamental group free abelian;
   that is not true for a higher-genus surface. The standard Goldman
   construction should be checked in its actual free-homotopy setting,
   not rejected together with this erroneous explanatory sentence.
5. Pages 27--29 take a Dixmier trace of a cyclic class and then use
   the curvature heat coefficient for Tr_omega |D|^-2 on a 2D disk.
   The required operator/cocycle pairing and summability data must
   first be defined. Check the second step against Connes' trace
   theorem and the leading Weyl coefficient; an ordinary 2D Dirac
   operator's leading residue and its curvature coefficient differ.
   The printed equation was visually confirmed. This is a specific
   spectral-action audit duty, not a no-go for spectral gravity.
6. Pages 32--34 expressly introduce four assumptions for the black-hole
   metric. Its stated Heaviside coefficients have jumps and vanish
   in a region. Such an expression has not established a smooth,
   nondegenerate Lorentzian metric or a physical 4-to-2 dimensional
   reduction. Fourier--Laplace analysis on an end is a separate tool.
7. Pages 35--36 infer rational Markoff data from a discrete fundamental
   group. Discreteness of a group does not restrict all its complex
   representations to rational traces. Chaotic evolution, finite
   precision and a trace identity do not alone give quantum
   probabilities or the uncertainty relations of a positive state.
8. Pages 36--41 turn finite Casson-tower embedding results into a
   collapse process and then a time. The dynamics, choice of CS lift,
   unit of length and time identification must be derived separately.
   Mostow rigidity of a normalized Riemannian hyperbolic metric does
   not itself give an FRW evolution equation or Lorentzian de Sitter
   dynamics. Page 40's two-critical-point Morse claim for every homology
   3-sphere also needs correction; homology alone is insufficient.

The conclusion on pages 41--42 explicitly leaves the state description
and Hamiltonian-constraint condition conjectural. Those qualifications
are retained. References lead to several papers elsewhere in the
supplied archive; their full bodies are still to be read before the
overall transfer verdict. No 4D chirality, quantum gravity, collapse
time or cosmological prediction is adopted from this review.

## Direct notes: 1003.5506v1 (2010)

Title: *Exotic Smoothness and Quantum Gravity*. All 16 pages are read.
The paper explicitly separates a proposed sum over smooth structures
from an assumed existing integral over geometries. Its section 2
excludes questions of path-integral definition and signature. Conjecture
5.1 assumes all exotic K3 structures arise by knot/link surgery. Thus
the resulting state sum is not presented with a defined gravitational
measure, and the conjecture must not be imported as a classification.

The concrete reusable construction is again Fintushel--Stern surgery.
Page 5 itself qualifies its initial broad nontrivial-knot claim by the
Alexander-polynomial detector's limitations and examples sharing the
same Seiberg--Witten data. It also retains the knot/mirror equivalence
of the resulting smooth 4-manifolds. Summing over knot labels therefore
requires checking multiplicities even after quotienting mirrors; the
map from knots to smooth structures is not proved bijective here.

The proposed action change, pages 6--8, fixes a metric on one piece
and uses a product metric on the replacement piece. Intrinsic flatness
of a boundary T3 does not make its extrinsic GHY contribution vanish.
A smooth metric join, its collar contribution and the off-shell measure
are additional duties. The replacement of the 3D gravity action by
CS must retain the tetrad/connection and real-form conventions, not
identify every such functional with the ordinary Levi--Civita CS number.

Pages 9--13 explicitly choose units for the circle and torus, then use
normalized hyperbolic volume in the expectation value. A topological
volume in curvature-minus-one units is useful, but does not select
the physical length scale. The subsequent area-quantization argument
needs a correctly normalized gauge-invariant CS phase and allowed level;
a coefficient chosen from geometric lengths is not already such a
level. The printed Whitehead-link volume correction subtracts one
unit after stating that two torus neighborhoods are removed: retain
the actual link-surgery construction and normalization before reusing
that formula. No numerical rerun of that example is claimed.

Appendix B has the same minimum-CS-to-Levi--Civita assertion as the
later matter paper. Flat gauge critical points, a metric's gravitational
connection and an instanton interpolation with chosen endpoints must
be distinguished. Section 6's boundary character/skein route is the
most concrete quantum-observable lead, not yet a defined 4D gravity
path integral or a derived chiral matter sector.

## Direct notes: 1401.4816v1 (2014, with Brans)

Title: *Gravitational sources induced by exotic smoothness and fermions
as knot complements*. All 21 pages, including appendices, are read.
This earlier presentation of the 2015 matter route includes an
end-periodic construction and the same selected chiral spinor column.
The constant-normal extension is not a normalizable localized mode
calculation; the physical source and domain questions remain.

There is an important development between the supplied papers, not
just a repeated argument. The 2014 paper's pages 17--18 say two
interface GHY terms fail to cancel when the interface has no
orientation-reversing self-diffeomorphism. The cancellation for a
smooth common metric uses opposite outward normals on the two sides,
not amphichirality of the interface. The 2015 paper instead displays
the opposite-sign decomposition on page 12 and on pages 21--22
compares neighborhoods after choosing equal bulk actions. These later
pages were re-read directly for the comparison. Its later, different
assumptions must be audited on their own; the 2014 defect is not a
blanket rejection of the 2015 argument or all boundary spinor methods.

Other checks before transfer: pages 8--10 pass from general link
surgery to a one-knot/solid-torus description without the needed
restriction on the 3-manifold. Page 12 treats the variable H in
D phi = H phi as a constant eigenvalue and then treats combinations
of eigenspinors as combinations of mean curvatures. This does not
follow from the linear spectral theorem with fixed metric and operator.
Pages 13--14 promote a constrained geometric spinor action to a free
four-dimensional action, while choosing one chiral component. Pages
15--17 use a geon configuration-space spin argument and a dust scaling
claim; neither supplies the charged, normalizable internal-mode index
of R18/R19. Appendix C explicitly retains a Hubble-dependent critical
density in its total energy, so metric rigidity alone does not prove
that entire energy constant. These are specific transfer duties.

## Direct notes: 1811.04464v1 (2018)

Title: *Hyperbolic groups, 4-manifolds and Quantum Gravity*. All 11 PDF
pages are read; page 11 is an arXiv figure-availability notice. The
paper's additional useful lead is Morgan--Shalen compactification:
diverging representation sequences can have projectively rescaled
length-function limits described by group actions on real trees.
That is a potential tool for organizing degenerating character data.
It does not by itself prove a physical drop from four dimensions to
two, a limit of Einstein actions, or a nonsingular black-hole metric.

The account moves from hyperbolic pieces in a JSJ description to the
whole assembled manifold being hyperbolic; that implication requires
an argument. A flat Cartan holonomy, a Levi--Civita holonomy and a
representation with diverging traces are not the same curvature
observable. Section 5's physical large-curvature interpretation needs
a metric family and a rescaling prescription linked to the dynamics.
Those cannot be supplied just by a projective length compactification.

Sections 2--4 also need an actual algebra map. The group construction,
its chosen representation/closure, a Temperley--Lieb inductive system
and a positive state cannot be identified solely because a factor type
is asserted for both. The inference from infinite conjugacy classes
to hyperfiniteness needs more than factoriality. The Jones--Wenzl
root-of-unity truncation, consistent parameter and positive trace must
be retained when discussing a limit over all n. A skein element is
not automatically a normalized positive functional. No quantum state,
unitary 4D theory or physical dimensional reduction is adopted here.

At this checkpoint seven supplied papers, totaling 196 of 448 pages,
had been fully read. Subsequent coverage is recorded below and in the
current coverage table.

## Direct notes: 1709.03314v2 (2017)

Title: *How to obtain a cosmological constant from small exotic R4*.
All 36 pages, including appendices and references, are read. The paper
explicitly revisits earlier choices of Casson handle, cork embedding
and cosmological evolution. Its attempt to remove those choices must
be assessed from this version's argument, not dismissed by repeating
an objection to an earlier paper.

The selected construction uses an embedding of a small exotic R4 into
the standard R4 and into a chosen blown-up K3, with transitions through
Sigma(2,5,7) and P#P. Sections 3--4 describe the end and its successive
three-manifolds. Pages 11--13 infer hyperbolicity of an assembled space
from hyperbolic pieces and introduce a radial embedding and Poincare
metric. These steps require the actual gluing, metric and completeness
hypotheses. Hyperbolic JSJ pieces do not alone prove that their torus
gluing is a complete hyperbolic manifold. The sequence's homology and
its limit must also be distinguished; the later neutrino paper does
make that distinction explicitly.

There is an important two-sided metric check. A smooth open embedding
of a small exotic R4 into standard R4 permits pulling back the Euclidean
metric; the resulting flat metric is incomplete. Pulling back a
hyperbolic metric on an open image similarly preserves a positive
existence possibility without supplying completeness or uniqueness.
Conversely, Cartan--Hadamard excludes a COMPLETE everywhere
nonpositive-sectional-curvature metric on a simply connected exotic
R4. Thus neither "no such local geometry" nor "complete Mostow
rigidity follows from an embedding" is justified. The primary theorem
was checked below. This does not exclude general metrics on exotics.

Pages 14--15 supply a useful Seiberg--Witten/Weitzenbock energy
identity. A nonzero spinor solution can constrain the scalar curvature;
it does not force constant sectional curvature. Negative Einstein
curvature and real hyperbolicity are distinct even in dimension four:
the product of two equal-curvature hyperbolic surfaces has negative
Einstein Ricci curvature but zero mixed sectional curvatures. The
paper's appendix comparison theorem assumes a hyperbolic comparison
manifold already exists and retains rescaling freedom. Neither that
theorem nor a localized smooth-structure change supplies the omitted
metric identification.

Pages 15--23 move from those Riemannian claims to FRW evolution and
a physical time/length scale. The topology of a handle decomposition
also does not by itself establish causal properties of a specified
Lorentzian metric: a homotopy contracting a loop is not a causal
homotopy. The radial/tree parametrization, physical clock, selected
curvature normalization and passage to de Sitter geometry require
their own equations and assumptions.

The CS discussion is more explicit than a mere equality of labels.
Pages 20--22 actually introduce a Cartan connection, an invariant
pairing and a length parameter. This is a positive construction to
retain. Its real form, contraction, torsion restriction and subsequent
rescaling of the connection need checking: multiplying a connection
form by a constant does not preserve its original inhomogeneous gauge
transformation law. Equation (13) also applies a closed signature
formula to a cobordism without its spectral boundary correction.
The actual APS signature theorem is recorded below as a possible
repair, not as a reason to discard relative CS/index methods.

Pages 24--28 turn chosen CS representatives and Planck units into
lengths and a cosmological constant. The reciprocal-CS exponential
requires a declared connection class and lift, not only a periodic
invariant. CS(S3)=0 gives a singular expression before a limiting
prescription is chosen. A proposed quantum multiplier from the cork's
Euler characteristic also requires the action coefficient. The
specified Planck convention uses h, not hbar; no unearned extra 2pi
objection is introduced. The numerical values and historical Hubble
comparison have not been independently recertified or adopted here.

The conclusion itself retains selection and quantum-mechanical
interpretation questions. The useful transfers are a typed 3D gravity
connection, energy identities, end constructions and corrected
relative index data. A physical Lambda prediction does not follow
from importing their names or from a normalized geometric volume.

## Direct notes: 1801.10419v4 (2019)

Title: *A topological approach to Neutrino masses by using exotic
smoothness*. All 15 pages are read. The proposed chain is the same
chosen pair of topological transitions, two inferred energy scales,
a seesaw mass matrix, a spinorial boundary interpretation and a
speculative generation/mixing argument. Those are distinct claims.

Page 3 now explicitly distinguishes the homology of the finite end
approximants from their limiting S3. That correct qualification must
not be lost by treating every version as identical. On page 6, however,
the stated minimum over all CS representations needs a restriction:
the trivial flat connection has zero CS on every such manifold.
An irreducible class, minimum positive value or other selected sector
and lift must be specified before reusing the formula. This is a
definition repair to investigate, not a dismissal of every rational
CS value used in the literature.

Pages 7--8 invoke a three-stage tower result to set a time scale and
then divide a later exponent among three proposed channels. The exact
Freedman theorem cited here must be read before comparing its scope
with the other papers' five-stage statements. Even a tower-embedding
theorem would not by itself identify one stage with a Planck-time
increment or select the physical channels. The printed expression
for the second time interval has the same multiplying factor as the
energy expression, despite the reciprocal time--energy relation used
earlier. Page 8 was rendered and visually checked. This may be a
formula error rather than a failure of the conditional seesaw algebra.

Pages 8--11 again choose one chiral spinor column in an immersion
construction. A mapping-class count is then interpreted as a count
of Dirac operators and handed neutrinos. A map on metrics, spin
structures, operator domains and orientation is needed: transporting
all geometric data by a diffeomorphism gives a unitary-equivalent
Dirac problem, not automatically a second particle species. A homology
3-sphere has a unique spin structure, and a statement about Diff(P)
does not directly establish the same mapping-class statement for P#P.
The latter includes connected-sum structure that must actually be
analyzed. No normalizable charged generation count is supplied by
that identification alone.

The small-eigenvalue seesaw relation M^2/B is useful conditional
algebra; deriving the two entries, their Yukawa normalization and the
mass splittings remains separate. The model's quoted mass and its
experimental comparisons have not been independently adopted. In
particular, a bound on an effective Majorana mass must not silently
become a bound on a sum of neutrino masses. Equal assigned masses
also require a separate account of nonzero oscillation splittings.

Section 6 explicitly labels the three-family and mixing discussion
speculative. Three hyperbolic-plane summands and their permutation
group do not alone produce a flavor representation or PMNS matrix.
Its index-2 observation also needs an operator dictionary. A chiral
spin or Spin-c index is not the index of an entire self-adjoint Dirac
operator, nor automatically a particle--antiparticle asymmetry on
an open spacetime. The blown-up K3 is not spin, but this does NOT
dispose of index 2: a suitable Spin-c determinant class can still
give that integer. The exact bundle, background and boundary/domain
data must be supplied before transferring it to our different model.

## Direct notes: 1812.08158v1 (2018)

Title: *A topological model for inflation*. All 23 pages are read,
including appendices and references. A truncated extraction of page
4 was immediately repaired by reading that page separately. Pages
8, 9 and 19 were rendered and visually inspected. The route is
Morse/Cerf theory to a gradient action, a hyperbolic radial metric,
a claimed inflation potential, a CS scale and boundary-spinor
reheating. Morse theory is relevant to our deformed Dirac problem;
none of those later physical identifications follows merely from
that shared starting point.

The most discriminating audit lead is equations (7)--(12), pages
8--9. With the printed radial metric g_rr=(1-r^2)^(-2) and
h=r^2/2-r^3/3, the squared gradient requires g^rr(h')^2. The paper
instead prints the lower-index factor g_rr(h')^2. The latter gives
a nonzero limiting plateau as r tends to 1, whereas the covariant
gradient expression tends to zero. Its stated logarithmic coordinate
also has derivative 2/(1-r^2), not 1/(1-r^2), so the displayed line
element has a separate factor-four discrepancy. These printed
equations, not an OCR substitution, are the subject of the check.
An overall potential coefficient cannot repair a changed limiting
shape. A different Morse function could change the outcome; this is
not a no-go for inflation or hyperbolic scalar-field models. A bounded
coordinate-covariance control remains to be separately designed and
sealed; no executable scientific certificate is claimed here.

The earlier worldline-to-field step also needs a dictionary. A
gradient trajectory is not already a four-dimensional scalar action,
and a normalized velocity's rank-one product is not a spacetime
metric. A Morse Hessian's signature does not force the curvature of
a cobordism. The subsequent Weyl transformation must retain canonical
field normalization and the chosen potential coefficient before
identifying an R+alpha R^2 theory. The appendix's correct completeness
and finite-volume hypotheses for rigidity must be retained in its
physical applications.

Pages 11--15 again require a boundary-corrected signature formula,
a selected CS lift, a physical clock and curvature normalization.
The total expansion factor is not automatically the e-fold number
between horizon exit and the end of inflation. The printed expression
for alpha on page 19 also changes a reciprocal truncated series to
the series itself while keeping the same small numerical estimate;
its convention and dimensional powers need checking. These may be
correctable formula errors. Historical numerical fits are not new
tests, and no inflation parameter or reheating value is adopted here.

Pages 15--17 offer a boundary-spinor coupling, but explicitly remove
the constant-norm constraint in promoting it to a free field action.
Intrinsic hyperbolic geometry does not fix extrinsic mean curvature.
A Weyl change of that curvature has a normal-derivative contribution;
spinor weights and kinetic normalization must also be kept. Identifying
a CS exponential directly with a Yukawa coupling would require all
those data and the physical normalization, not only a decimal match.

Ten supplied papers, totaling 270 of 448 pages, are now fully read.
Six papers and the completed, cited transfer assessment remain. These
are direct reading notes and source checks, not a new globally banked
arc, a numerical recertification or a completed physical transfer.

## First checks against the cited primary mathematics

[Friedrich, dg-ga/9712021v1](https://arxiv.org/pdf/dg-ga/9712021),
sections 2--3 and Theorem 1, was consulted directly after the matter
papers. Proposition 2 starts with a parallel ambient spinor and a
specified Clifford recombination of its restriction. Remark 2 retains
the normal derivative for a general spinor. Theorem 1 requires constant
nonzero length and gives an immersion of the universal cover; descent
involves periods. It treats H as a smooth function, not necessarily
a spectral constant. This verifies useful spinorial geometry while
restricting the proposed physical transfer; it supplies no charged
4D three-family index. Relevant passages, not the whole primary paper,
were read in this first check.

[Frohman--Gelca, math/9806107v1](https://arxiv.org/pdf/math/9806107),
introduction and Theorem 2 with its proof, were consulted directly.
The theorem gives a specific algebra isomorphism from the torus skein
algebra to the inversion-invariant subalgebra of the quantum torus,
with a Chebyshev-threaded slope mapped to the sum of two opposite
quantum-torus monomials. This is a concrete boundary-algebra map to
compare, not merely a shared factor label. A physical representation,
positive state and identification of the deformation parameter remain
additional tasks. The whole paper and its other theorems have not yet
been claimed read. Both primary checks were accessed September 9 UTC.

Theorem (4-14) and its surrounding discussion in
[Atiyah--Patodi--Singer, *Spectral asymmetry and Riemannian geometry I*](https://webhomes.maths.ed.ac.uk/~v1ranick/papers/aps001.pdf),
1975, printed pages 65--66, were checked directly. For a compact oriented
4k-manifold with product metric near its boundary, signature equals the
integral of the L-form minus the eta invariant of the specified
even-form boundary operator. The metric-dependent spectral correction
is not optional. Its convention differs from the general spin-Dirac
half-eta-plus-kernel formula. This supplies a repair candidate for the
papers' cobordism step, not a theorem about our singular noncompact
ends without additional analysis. Only the cited passages, not this
entire primary paper, have been read for this check.

[Diego Conti, *Notes of Riemannian Geometry*](https://poisson.phc.dm.unipi.it/~lmigliorini/secondo_magistrale/riemanniana/note_conti.pdf),
December 11, 2025, Theorem 9.1 and its proof on printed page 31, were
read directly. Completeness and nonpositive SECTIONAL curvature give
an exponential covering and a universal cover diffeomorphic to R^n.
Our inference for a simply connected exotic R4 uses both hypotheses;
incomplete pullback metrics and mere negative scalar/Ricci curvature
are outside that inference. These two primary checks were accessed
September 10 local. An alternative requested notes PDF did not return
usable content and is not counted as read.
