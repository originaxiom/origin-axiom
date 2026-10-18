# Composition retains a relation; joining needs its interface

October 18, 2026. Unreviewed analytical proofs and source-scope flags.
No new scientific producer run, independent acceptance or numbered claim.
Read with [TYPED_ARCHITECTURE.md](TYPED_ARCHITECTURE.md). The aim is to
derive the laws available from stated data, not introduce a selected
interaction, weighting or replacement physical parent.

## 1. Shared-frame composition is already determined

For maps acting on the same marked record pair, AB is an unambiguous
composition (B first). The admitted shared fibre supplies the relative
placement. No new alignment parameter is needed for this operation.

Simultaneous change of frame is compatible with multiplication:

    (gAg^-1)(gBg^-1) = g(AB)g^-1.

Independent change of frames is not. Thus one may discard the common
frame of a pair while retaining its simultaneous-conjugacy class, but
in general may not replace that pair by two unrelated conjugacy classes
and expect multiplication to descend. Associativity holds before this
information loss; it does not repair it afterwards.

## 2. Exact relative-position classification

Fix a specified group G and elements A,B. Consider ordered pairs with
components in their respective G-conjugacy classes, modulo simultaneous
G-conjugation. Each pair has a representative

    (A, h B h^-1),   h in G.

Its remaining relative-position datum is the double coset

    C_G(A) \ G / C_G(B),

where C denotes centralizer. Proof: replacing h by a h b, with a in
C_G(A) and b in C_G(B), conjugates the pair by a. Conversely, if a
conjugacy takes two representatives to each other, it fixes A and
h'^{-1} a h centralizes B. This is exactly the displayed equivalence.

The product conjugacy class [A h B h^-1] is well-defined on this double
coset space, but need not distinguish every double coset. The result
classifies possibilities; it chooses no h. It applies only to the stated
equivalence group. SL2(Z), GL2(Z), SL2(C), and based free-group lifts are
not interchangeable choices of G. A theory admitting fewer reframings
must use its actual equivalences, not all complex conjugacies.

For three or more factors, keep the full simultaneous configuration
until composing. Replacing an intermediate product by an isolated class
can again discard its placement relative to the next factor.

### An exact family, not a finite scan

Take A=LR=[[2,1],[1,1]] and h_n=L^n=[[1,n],[0,1]]. Multiplication gives

    h_n A h_n^-1 = [[2+n, 1-n-n^2], [1, 1-n]],
    tr(A h_n A h_n^-1) = 7-n^2.

The latter follows by summing the two diagonal entries
5+2n and 2-2n-n^2. Each input still has the same conjugacy class [A].
For nonnegative integers n the product traces are all distinct, so
there are infinitely many distinguishable relative placements at this
level. This is an SL2(Z) statement with inverse moves allowed, not a
claim that every displayed representative is a positive word.

At n=0 the product has trace 7. At n=-1, h_n A h_n^-1=RL and the product
has trace 6: the earlier control is recovered. For this pair's character,
the Fricke commutator trace is

    kappa_n = 3^2+3^2+(7-n^2)^2-9(7-n^2)-2
            = n^4-5n^2+2.

At n=0 it is 2; at n=+-1 or +-2 it is -2. Imposing the extra equation
kappa=-2 with individual traces 3 would permit product traces 3 and 6;
it would not uniquely select one join. This kappa belongs to this matrix
pair. It is not, by notation alone, the knot-meridian holonomy invariant.

## 3. A complete all-word trace tool already exists

For a specified pair U,V in SL2(C), all finite-word traces are polynomials
in x=tr U, y=tr V, z=tr UV. The reduction uses

    tr(XY)+tr(XY^-1)=tr X tr Y,
    tr[U,V]=x^2+y^2+z^2-xyz-2.

The triple classifies irreducible pairs up to simultaneous complex
conjugacy; on the reducible locus it can lose extension data. It does not
classify integral markings, based lifts or physical domains. This is
classical Fricke–Vogt theory, already native to the programme, not a new
discovery: [Goldman, Theorem A and section 2.2](https://arxiv.org/html/0901.1404v1).
The individual traces x,y omit the relation z. More words do not restore
information already lost by the full trace character.

### Recover B1192's integral relational positive

Main's GC-16 source already uses

    A=[[2,1],[1,1]],   M=[[2,3],[1,2]]=L R L.

Both are generated positive matrices; this is not an imported arbitrary
partner. Recheck its first simultaneous-reversal result directly. Write
X=[[a,b],[c,d]] and require XA=A^-1 X and XM=M^-1 X. The first equation
gives d=-a and c=-a-b. The second gives d=-a and b=-3c. Together,

    X=t [[2,-3],[1,-2]],  t in Z,
    det X=-t^2.

This exhausts the integral solutions. The unimodular ones have t=+-1
and determinant -1; none has determinant +1. Consequently the ordered
pairs (A,M) and (A^-1,M^-1) are inequivalent under SL2(Z) conjugacy,
although equivalent under GL2(Z). Multiplying this realizer by i gives
an SL2(C) realizer, so all word traces agree. Independently, the trace
triples agree: (3,4,10), with kappa=3.

This preserves an existing relational distinction which complex traces
cannot see, and recovers it without the producer's general lattice-basis
routine. Clearing denominators in a rational nullspace is not in general
a saturation algorithm; the displayed direct rank-one solution avoids
assuming that general claim. The source's other cases are not newly
certified by this one proof. No physical handedness, selected coupling,
fermion index or preferred orientation follows from the distinction.

### B1248 already contains the general nondegenerate law

Following the predecessor forward finds B1248, not a missing general
classification. Its corrected integral formula can be recovered with
its necessary scope made explicit. For A,M in SL2(Z), set

    C=AM-MA,   kappa=tr(AMA^-1M^-1).

Cayley–Hamilton gives CA+AC=(tr A)C and CM+MC=(tr M)C, hence
CA=A^-1C and CM=M^-1C. Also

    det C = det(AM) det(I-(AM)^-1 MA) = 2-kappa.

For kappa!=2, C is invertible and the pair is irreducible over C. Any
other reversing solution differs from C by a simultaneous centralizer,
which is scalar. Let g be the positive entry-gcd of C. The integral
solutions are exactly t C/g with t in Z: a rational scalar times a
primitive integral matrix is integral only when the scalar is integral
(Bezout applied to its entries). Their determinants are

    t^2 D,   D=(2-kappa)/g^2.

Thus D=+1 admits determinant-positive realizers, D=-1 admits only
determinant-negative unimodular realizers, and |D|>1 admits no integral
unimodular realizer. This is B1248's corrected law, not a new discovery.
For the preceding A,M example, C=-[[2,-3],[1,-2]], g=1 and D=-1.

The kappa=2 locus must be handled separately. B1248's general prose
row “module rank 2, both signs” overextends its homogeneous golden
control. For a counterexample still inside the generated positive
hyperbolic grammar, take A=M=[[2,3],[1,2]]=LRL. Then kappa=2 and all
reversing matrices are

    X=[[a,-3c],[c,-a]],   det X=3c^2-a^2.

Determinant +1 would require a^2=-1 modulo 3, impossible; determinant
-1 occurs at a=1,c=0. Hence this homogeneous pair does not have both
signs. This does not alter the previously checked homogeneous golden
pair, or the kappa!=2 formula. Nor is kappa=2 alone a sufficient general
rank statement: at A=M=I the linear solution space has dimension four.

B1248's report and producer header also retain a later sentence saying
the squarefree formula is unaffected, despite their explicit earlier
correction rejecting that formula. The current `classify` implementation
uses the entry-gcd formula, not the stale prose. Its degenerate branch
reports a rank; it does not test the general “both signs” assertion.
The analytical counterexamples above and this source flag are unreviewed;
no historical source, data or banked verdict is overwritten here.

## 4. Conditional joining law for actual interfaces

Suppose the carrier/join specification provides groups Gamma_1, Gamma_2,
an interface group H and maps i_j:H -> Gamma_j, with the second map
already incorporating the specified geometric gluing. Suppose its joined
group is given by the amalgamated presentation Gamma_1 *_H Gamma_2.
We do not derive this choice of carriers or interface from word closure.

For a supplied coefficient group G, flat coefficient data on the join
are exactly pairs of representations with matching interface values:

    rho_1(i_1(k)) = rho_2(i_2(k))  for every k in H.

Proof: representations of the free product are uniquely specified by
representations of each factor. They factor through the amalgamated
presentation exactly when the additional identifying relators map to
the identity. This establishes necessity, sufficiency and uniqueness for
the fixed, common-frame data. Only interface generators need checking
when a generating set for H is given.

If the pieces were described in separate coefficient frames, retain an
intertwiner h and require instead

    rho_1(i_1(k)) = h rho_2(i_2(k)) h^-1.

Changing the two frames by g1,g2 sends

    rho_j -> g_j rho_j g_j^-1,   h -> g1 h g2^-1.

The equation is covariant under exactly that transformation. This is
why an unbased join retains the matching map and automorphisms, rather
than only matching two lists of invariants. Nontrivial cycles in an
assembly can carry additional holonomy; they must not be set to identity
merely because a change of local coordinates has a cocycle law.

This is a complete representation-level rule for the supplied
amalgamated presentation. It is not yet a law selecting the joining
graph, interface maps, coefficient group, metric or physical action.
It also does not cover every conceivable join: self-gluing and other
presentations must retain their own stable-letter relations and data.

## 5. B144: keep mirror closure, narrow the inference and the test

B144 treats amphichiral pieces with actual orientation-reversing boundary
actions h1,h2 and an allowed torus gluing phi. Its transformed gluing

    phi_mirror = h2 phi h1^-1

stays integral unimodular, with the same determinant as phi. If the
allowed gluing set is closed under this transformation, the constructed
family is mirror-closed. This algebraic positive is retained. The
application still needs those h_i to be realized by the actual pieces.

Two stronger uses need separate justification:

1. The producer's `chiral_composites_exist` counts literal inequalities
   phi != h2 phi h1^-1 and labels them chiral composites. That comparison
   does not test equivalence under all boundary actions extending over
   the pieces, nor piece exchange when permitted. Inequality excludes
   one exact match, not every oriented homeomorphism. Its generic h_i
   are not derived there from the actual two pieces. The test asserting
   `most_are_chiral` repeats this predicate rather than independently
   certifying chirality. This flag does not prove those composites are
   achiral, and does not retract B128's different construction.
2. Mirror closure of a family is not a proof that each member is
   achiral, or a no-go for all symmetry-breaking dynamics. A precise
   surviving restriction is: a single-valued mirror-equivariant
   selector from mirror-fixed input must select a mirror-fixed output.
   Proof: f(s)=f(m s)=m f(s). A set-valued pair of non-fixed outcomes
   does not contradict it. The grammar supplies no selection dynamics
   here; neither a mechanism nor its universal impossibility is proved.

B144's mathematical family closure therefore survives while its broad
physical redirect needs a narrower scope. The proposed repair is not
an adoption of spontaneous breaking as the OA mechanism. It is a duty
to test any actual candidate action and its solution space. Canonical
B144 files have not been edited, and no corrected census is claimed.

## 6. The same physical construction must carry the result

The existing [action audit](../ACTION_PARENT_SPECIFICATION_2026_10_16.md)
already separates native update actions from supplied physical parents.
Its positives must remain beside the unresolved joining law:

| Existing result | What can be reused | What this analysis does not derive |
|---|---|---|
| R28 multiplier action | A stationary variational encoding of the actual update, without a universal anti-symplectic no-go | Positive physical kinetic terms, spacetime, a measure or fermions |
| R94/R95 registered trace sector | Local generating primitive and its explicitly scaled map into a supplied E8 Chern–Simons sector | The parent, embedding, coefficient, side-wall law, or an identification with the separate joined SM phase |
| R85/R93 joined phase | A specified non-self-dual join and a conditionally admitted SM gauge background | Selection of that join/Wilson direction; a chiral physical spectrum on it |
| B1036 double | Received evidence that a compatible join adds classes; its computed symmetric seam sector remains restricted | A generation count or a universal obstruction to all interactions |
| Actual end/operator work | Boundary currents, domains and coefficient transports under their named assumptions | A unique physical end law from a matrix product or a matching relation alone |

The boundary variation of an admitted action constrains stationarity;
the class of allowed variations and any source/end functional must be
derived or declared too. Algebraic representation matching is necessary
for the indicated flat join, not sufficient for a stationary interacting
physical vacuum with the complete desired spectrum.

## 7. Verdict of this analytical step and next control set

The shared action is a genuine existing relational asset. Independent
thread classes can lose it; all-word complex traces can still lose its
integral orientation layer. Neither loss is repaired by a larger random
word census. The natural computation retains the relevant structure,
uses composition on it, and takes only quotients passing the declared
update/output/domain tests.

What remains undetermined by the equations above is a physically selected
joining arrangement and its action, end data, interpretation and weighting.
No full priced-input row is paid. These are scoped outstanding derivations,
not proof that physics is impossible from an enlarged foundation.

Before execution, the source-complete admission package should bind:

- the partial-future quotient proof, with distinct-domain/same-output
  and same-domain/different-future-output controls;
- the based-lift comparator in LIFT_SCOPE_NOTE, including an output
  insensitive to its inner difference and one sensitive to it;
- the double-coset equivalence and 7-n^2 family, with shared-frame
  covariance and a deliberately invalid independent-class product;
- the B1192 exact linear comparator, and complex versus integral
  equivalence without treating either as physical parity by definition;
  B1248's nondegenerate entry-gcd law and separate degenerate controls,
  rejecting the general “both signs” assertion without discarding the
  original homogeneous golden control;
- representation matching on a named existing join, rejecting a
  deliberately incompatible boundary generator;
- a B144 test-scope repair based on actual extendable boundary actions,
  not a new inequality census dressed as manifold certification.

These are proposed controls, not a sealed design, run or independent
review. The mathematical proofs and the physical transfer duty require
separate acceptance. Existing historical failures remain in the register.

## Source custody and reading coverage

Main source pin: `2e5716bd9bea013d69f3cd733f083b61a6f59dbd`.
Local source pin before this note: `1b62acd0788eec7496af4eef29e35c55ae374701`.
Personally read in this pass:

- B144 FINDINGS, complete producer and tests. Local/main producer blobs
  both `b0ad96de675e8e3e8532dd99b369090a4bfd3821`; test blobs both
  `f47a0972d882eb45ad8a44be3b9bddbf82211be1`. No execution.
- Main B1192 `verification/gc16_hetero_coupling.py`, complete; B1036
  FINDINGS, complete, not its producers; B363 FINDINGS, complete, not
  a new certification of its lift-sensitive seam computations.
- Main B1248 FINDINGS and `verification/norm_classification.py`, complete.
  Its existing corrected formula and field-level scope repair are
  predecessors, not missing work. B221 FINDINGS was also read during a
  broader content/gcd search; its CFT claims are not used in this note.
- Local TRACE_PARENT_PROOF, JOINED_WILSON report,
  ACTION_PARENT_SPECIFICATION, ACT_REGISTER_PROOF and operational
  contract, complete. They are authored/received sources, not independent
  proof acceptance or fresh execution.
- Goldman's cited theorem, trace reduction and irreducible-character
  discussion; selected sections, not a full reading of the paper.

A broad earlier `double coset gluing` search and direct source search
found these predecessors. No exhaustive historical-absence or novelty
claim is made. The distinct compact-group fusion literature was inspected
as a possible benchmark, but no imported fusion action is adopted here.
