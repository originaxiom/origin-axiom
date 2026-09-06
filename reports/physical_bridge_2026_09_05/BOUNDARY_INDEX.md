# Path-local R12 — annular zero survives; a cusp-wide chirality kill does not follow

The user's equation is correct for the specified finite pair:

    I_Euler(M,A) = chi(M,A) = chi(M)-chi(A).

For the compact m004 exterior, chi(M)=chi(boundary M)/2=0. Consequently
I_Euler=-chi(A), and a disjoint union of annuli gives zero. This is a
conditional index statement, not a proof that every admissible boundary
is annular, that zero net index means no paired matter, or that a chosen
nonzero index is a derived physical generation count.

The new exact calculation preserves that positive result while checking
main B1290/B1291 and physics-seat R61/R69 against their actual boundary
objects. **Eleven new tests pass.** The source, controls and all raw
outputs were sealed/retained; no main B number is taken.

## 1. The theorem needs the same manifold, coefficient problem and boundary

SnapPy 3.3.2 independently returns one orientable cusp, two generators,
one relator and H1=Z for m004. The Euler argument above uses the compact
3-manifold boundary theorem. Merely knowing a group presentation is not
enough to identify its presentation 2-complex with the manifold: adjoining
a redundant trivial relator leaves the group unchanged but adds a 2-cell
(a wedged S2 in the trivial-relator example). B1290's producer hard-codes
2 and 1; its numerical Euler answer is correct, but its general statement
about arbitrary presentation complexes is too strong.

For the physical application, [Pantev--Wijnholt, eqs. 3.37--3.40](https://arxiv.org/pdf/0905.1968)
specifies a Morse/Higgs boundary problem and identifies h1 and h2 with
conjugate matter sectors. With h0=h3=0, ordinary Euler is h2-h1; defining
particle-minus-antiparticle as h1-h2 reverses the sign, not the zero test.
[Braun et al., section 4.1 and 5.2](https://arxiv.org/pdf/1812.06072)
makes the operator domains and source/boundary conditions explicit.
Different charged sectors can see different boundary subsets. A topological
pair is not by itself a solution of those field equations.

## 2. Three disks were already in the record, and their old dismissal fails

Exact periodic cubical complexes, integer boundary matrices, rational ranks,
and d*d=0 checks give the following ordinary cohomology dimensions:

| selected A in one torus | (b0,b1,b2) | chi(A) | I_Euler if chi(M)=0 |
|---|---|---:|---:|
| two disjoint annuli | (2,2,0) | 0 | 0 |
| three disjoint disks | (3,0,0) | 3 | -3 |
| torus minus the interiors of those disks | (1,4,0) | -3 | 3 |
| inner disk plus outside a larger concentric disk | (2,2,0) | 0 | 0 |

The three disks are centered at (0,0), (1/2,0), (0,1/2) on R2/Z2. Each
is invariant under theta:z->-z; the complement is invariant too. Square
boundaries can be smoothed equivariantly without changing these topologies.
The choice omits the fourth center. Every nontrivial half-period translation
changes this three-disk set: theta invariance is NOT full symmetry invariance
or a proof that the object selects these three centers.

This candidate is **prior art in physics-seat R61, section 4.2**, not a new
proposal here. R61 dismissed it using its theta-even real-representation
argument; R69 subsequently withdrew that argument. This audit restores
the candidate to consideration, not to physical success. A theta-ODD field
whose symmetry exchanges positive and negative regular boundary regions
has a separate zero-index constraint; it must not be substituted for the
theta-even case. The sB1277 leading-annular-mode computation concerns that
different odd/symmetry-constrained setup. Its actual leading coefficient
was not computed by that source and is not certified here.

The last row is a direct counterexample to B1291's claimed iff involving
a null-homotopic dividing circle. Both dividing circles are contractible
(computed winding (0,0)), yet the selected side has chi=0: +1 and -1
cancel. The valid statement is that all-essential regular dividing curves
give only annuli, whereas contractible curves can permit nonzero Euler.
Presence of such a curve does not force it for the chosen partition.
The upstream routine omits nesting/adjacency and tests possibility over
arbitrary subsets, not its stronger asserted iff for the selected side.

## 3. Fixed endpoints are not a generation index — retain the real parity result

For a nonidentity orientation-preserving finite-order hyperbolic isometry,
its proper fixed geodesic lines have two ends. If all ends land at one
cusp, their number there is even. This geometric parity argument survives
as a statement about those fixed endpoints. It does not bound chi(A) for
an arbitrary selected boundary region. Section 2 does NOT exhibit a
three-fixed-point isometry of a one-cusped hyperbolic manifold; it exhibits
a three-disk invariant subset of a torus, a different object.

Two instrument hypotheses also matter:

- |det(A-I)| is a finite fixed-point count only when det(A-I) is nonzero.
  With singular A-I, the translation matters: the identity fixes a torus,
  a half-translation fixes nothing; reflection versus glide gives circles
  versus nothing. Exact rational-grid controls distinguish them. A stored
  determinant 0 must not be read as zero fixed points for the identity.
- A cusp matrix between different cusps is not a self-map. Both
  cusp_images and cusp_maps must be retained before counting fixed points.

**The named two-cusp control survives the stricter check.** On m202,
isometries numbered 2 and 4 in this run preserve both cusps and each gives
three fixed points on each cusp. Their matrices have det(A-I)=3. Other
isometries exchange the cusps and must not be counted the same way, but
that correction does not erase the genuine witnesses. m125 likewise
retains its finite two-point witness. m004's finite isolated count is 4;
s960's singular-linear-part cases are not classified as free translations
without translation data by this run.

Our prior suspected that cusp swaps might invalidate the m202 example.
**They do not.** The example is retained, not killed because the instrument
also has a scope defect. No 1,200-manifold census or all commensurability/
arithmetic claims of B1291 are independently certified by this four-witness
check. In particular, choosing a multi-cusped relative is still a selection
question, not a demonstrated physical compactification.

## 4. Proper-arc excision: the missing external-boundary contribution

Three different objects must not share one Euler label:

| object, given the two-proper-arc geometry in R61 | topology | Euler |
|---|---|---:|
| fixed locus in the 3-manifold | two intervals | 2 |
| its endpoints on the original cusp | four points | 4 |
| lateral frontier of a tubular neighborhood | two annuli | 0 |

Let Q be the compact exterior, N a regular neighborhood of the charge
graph Delta, C=Q minus the relative interior of N, P=N intersect boundary Q,
and T=C intersect N its lateral frontier. Let E=C intersect boundary Q be
the remaining original boundary. With circular seams (Euler zero),

    chi(T) = 2 chi(Delta)-chi(P),
    chi(C) = chi(Q)-chi(N)+chi(T)
           = chi(Q)+chi(Delta)-chi(P).

These follow by boundary duality for N and Euler additivity for Q=C union N.
For k disjoint proper intervals, chi(Delta)=k and chi(P)=2k, hence
chi(C)=chi(Q)-k. The exact solid-torus controls verify this for k=0,1,2,3,
including the gluing identities and full chain complexes. They are not
claimed to be hyperbolic models of Q; the Euler identity is independent
of the knotting of the given proper arcs. R61's particular endpoint
pairing and full field configuration are not re-derived by these controls.

For two arcs, chi(C)=-2 even though chi(T)=0. The remaining cusp surface
is a torus with four disks removed, chi(E)=-4. The complete boundary has
Euler -4, in agreement with 2 chi(C). Thus the user's simplification
I=-chi(A) cannot be reused unchanged after removing the charge arcs.

R69's script explicitly sets A to the positive tubes and the cusp part
to empty, but prints chi(Delta_minus)-chi(Delta_plus) instead of using its
computed chi(C) and chi(A). Rebuilding that actual pair gives:

| arc signs | chi(C,A), cusp part empty | R69 sign-only expression |
|---|---:|---:|
| (+,+) | -2 | -2 |
| (-,-) | -2 | 2 |
| (+,-) | -2 | 0 |

The all-negative empty-A case additionally has h0=1; identifying its
Euler with h2-h1 alone would discard a cohomology group. These discrepancies
do not kill the possible absolute index 2: for A=T, the explicit control
has relative Betti numbers (0,2,0,0); replacing A by the COMPLEMENTARY
boundary E gives (0,0,2,0), reversing the index as it should. It is the
complete boundary condition that reverses, not just the tube labels.

More generally, split Delta into disjoint definite-sign subgraphs and
write A=T_plus union E_plus, with circular overlaps. Then

    I_Euler(C,A) = chi(Q)+chi(Delta_minus)-chi(Delta_plus)
                  -chi(P_minus)-chi(E_plus).

For a closed Q and interior charge graphs, the last two terms vanish,
recovering the usual graph expression. PW's section 3.5 computes that
closed-base setting. With proper arcs ending on an existing cusp, those
terms cannot be dropped without a boundary prescription. For two arcs,
the sign-only answers require chi(E_plus)=0,-4,-2 respectively. The last
assignment, its field equations and its source selection are not supplied
by merely assigning signs to the two arcs.

## 5. What must now be earned toward the physical goal

I-26 must retain the physical-index identification, not only the Euler
subtraction. Specify the charge/Higgs background and unbroken group;
derive rather than choose the relevant graph/regions and all cusp pieces;
establish charge balance, boundary domains/interfaces and normalizability;
then compute the correct charged zero-mode complex and interactions.
An arbitrary region giving 3 does not select three generations. An annular
zero or an endpoint parity theorem does not exclude all such constructions.
This is the next PB-ACTION boundary problem, alongside the actual three-fold
closing/lift/selector audits already registered. Gravity and empirical
contact remain duties of the SAME source-derived theory, not paid here.

## Provenance and reproduction

Scientific design, producer and eleven tests sealed at **0ea46c2b** before
execution. First producer: exit 0 in 1.55 s. Focused tests: **11 passed,
1 GUI warning in 2.31 s**. Combined quiescent regression: **145 passed,
3 failed, 8 errors in 167.93 s**. Failures are the preserved original G2
exporter and R7 small-step controls; the errors are the original R11 QQ/ZZ
fixture. Separate repairs and all R12 tests pass. No new scientific failure,
old-test rewrite, tolerance relaxation, skip or xfail. This is not a
whole-repository green certificate or a completed main banking pass.

Sources were read at main **2901ae9f**, physics seat **f4d74728**, SM seat
**2a7f8855**; no merge/push. Their exact commit and blob hashes are in
[boundary_index_first_run.json](boundary_index_first_run.json).
The source code is read for auditing, never executed by this producer.
[CC's numbering receipt](BANKING_RECEIPT.md) preserves the reservation and
alias rule. Original physical/source claims are not rewritten on their
branches; this local finding awaits receiving-seat adjudication.

Read the named source bodies:
[main B1291](https://github.com/originaxiom/origin-axiom/blob/2901ae9f6dba964870b44d5eb6e01066c62b7f62/frontier/B1291_the_parity_of_the_cusp/FINDINGS.md),
[physics R69](https://github.com/originaxiom/origin-axiom/blob/f4d747281ce9ec65fe2806404c01672cc73deb54/reports/fresh_physics_seat_2026-09-01/R69_ARCS_CUT_CORNERS.md).
Raw successful, focused and combined outputs: [BOUNDARY_INDEX_CHECKS.txt](BOUNDARY_INDEX_CHECKS.txt).

```sh
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m reports.physical_bridge_2026_09_05.boundary_index --output /tmp/oa-boundary-index-new-run.json
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest tests/test_physical_bridge_boundary_index.py -q -p no:randomly
```

Use a fresh output path; existing output is refused. The calculation uses
ordinary rational cohomology. It is an exact topology/instrument audit,
not a solved physical Higgs boundary problem or a TOE.
