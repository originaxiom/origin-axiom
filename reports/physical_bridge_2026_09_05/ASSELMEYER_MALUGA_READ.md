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
| 1709.03314 | 36 | pending |
| 1801.10419 | 15 | pending |
| 1812.08158 | 23 | pending |
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

Seven supplied papers, totaling 196 of 448 pages, are now fully read.
The other nine papers and the completed transfer assessment remain.

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
