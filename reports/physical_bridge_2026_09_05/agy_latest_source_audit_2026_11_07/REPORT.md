# AGY's latest work: exact source and hand audit

2026-11-07. Non-authoring review of AGY source at
`1bd310f38fdcf4a9f70d468c8bf914ed27d83f08`.
Physical bridge branch: `audit/physical-bridge-2026-09-05`.

## Verdict and scope

**Corrections required before the inspected claims support a physical
derivation. Preserve the conditional mathematics.** The newest ledger
explicitly says **0 of 19 confirmed**, prices choices and withdraws the
claimed corner-asymmetry solution. This is a material improvement over the
older closure language. It is not a derivation of nineteen SM parameters.

This is a targeted load-bearing review, not a certification of all 156
numbered functions. Directly inspected: Theorems 141, 145, 147, 149, 150,
153–156, their relevant test assertions, the master entry point and older
cell-selection/physical-output paths. Latest-stage source contains both
new computations and historical replay. Their statuses must stay distinct.

Method: Git source reading; elementary hand derivations below; standard
library AST/hash inspection. **No AGY module was imported, collected or
executed. No new empirical prediction, comparison or scientific pass.**
The source receipt pins the reviewed code and upstream records. This report
does not supply execution admission, main's acceptance, or a global gate pass.

## F1. Ordinary and mirror-twisted homology are conflated

At `src/origin_axiom/toe_closure.py:25115` Theorem 141 assigns
`H_1(M_LR)=Z + Z/5` to `M_LR=m004`. Its returned description repeats the
torsion-linking account at lines 25249–25253. The cited SM seat's actual
Criterion K, relay section 355, explicitly assigns this torsion to the
**mirror-twisted carrier**, not m004.

The distinction is exact. In the declared convention

    A = LR = [[2,1],[1,1]],
    A-I = [[1,1],[1,0]],       det(A-I) = -1,
    A+I = [[3,1],[1,2]],       det(A+I) = 5.

Abelianizing a punctured-torus mapping-torus group gives
`H_1(M_A)=Z + coker(A-I)`. The first matrix is unimodular, so
`H_1(m004)=Z`. For monodromy `-A`, the cokernel is that of `A+I`, with
Smith factors `(1,5)`. The source's own Theorem 69 comment at line 11978
already distinguishes m004's `Z` from m003's `Z + Z/5`.

**Survives:** `SNF(A+I)=(1,5)`, the twisted fixed-point group, denominator-five
arithmetic and `q(2v)=-q(v)` for a specified quadratic form on `Z/5`.
**Does not follow:** a torsion-linking sector of m004's ordinary homology.
Criterion K remains conditional on its stated carrier/sector and physical
reading; correcting the carrier does not refute its arithmetic.

Repair: name the mirror-twisted carrier and its map to the coupling sector;
retain the spherical/branched-cover carrier separately. Add a control that
actually distinguishes `A-I` from `A+I`. The present tests at lines
2725–2743 check Smith factors and level output, not this identification.

## F2. Correct periodic-point counts are joined to incorrect coordinates

Theorem 145 correctly uses `A=[[2,1],[1,1]]` and determinant counts, but at
lines 26005, 26068–26088 identifies its two period-two orbits as
`{+-(1/5,0)}` and `{+-(2/5,0)}`. These are not the actual orbits in that
marking:

    A(1,0) = (2,1) mod 5, not -(1,0).
    (A+I)(x,y)=0 mod 5  iff  y=2x mod 5.

Thus the four nonzero points are

    (1,2)/5, (2,4)/5, (3,1)/5, (4,3)/5,

with the two orbits `+-(1,2)/5` and `+-(2,4)/5`. The count of four points
and two orbits survives exactly. Row-character versus column-vector action
does not fix this particular error: A is symmetric and the eigenvalue is -1.

The source then computes elliptic residues on `(p1,p2)=(0.2,0)` and
`(0.4,0)` at the unchanged purely imaginary tau. Those can remain legitimate
conditional frame calculations. They have not thereby become calculations
on the natural periodic orbits just counted. The tests at lines 2805–2823
assert counts and residue comparisons, without checking `Av=-v` on the
claimed points. This is a regression of the kind already acknowledged in
Phase 1's corrected eigenline comments.

One may change marking. For example, on column vectors,

    B=[[1,0],[-2,1]],    B A B^-1=[[4,1],[-5,-1]],

takes the eigenline to the horizontal line. But it also changes the
monodromy and the marked complex/field data. The modulus, characters,
theta/spin lifts, operators, norms and measuring data must be transported
together. A horizontal point at the old tau is not that complete move.

**Repair:** either use the actual eigenline in the retained marking or
exhibit the entire marking intertwiner. Recheck invariants on the joined
data after sealing the corrected scientific design. Do not erase the
older horizontal-frame results or call their identities false.

The separate claim that the two twins are "occupied in the universe" is
stronger than the code. Its Boolean tests the supplied `SIXY` charge table
modulo five. This proves a pattern within that field assignment; it does
not derive the field content or a dynamical occupation state.

## F3. The CP ablation changes two independent ingredients

Theorem 155's `build_flank_yukawa`, lines 28617–28624, does this when
`include_quadratic_q_phase=False`:

    q5_half = exp(-pi*Im(tau)/5)
    zeta5 = 1

It removes both the real-tau phase and the Weil root of unity. Case 2 at
lines 28677–28680 is consequently not a test of removing only the former
while retaining the latter. In fact the compared matrices become the same
real matrix by construction. Their vanishing CP invariant cannot establish
which removed phase was responsible for the original result.

This is a causal-comparison error identifiable from source, independently
of the numerical value of J. It does not prove that J vanishes when only
the geometric phase is removed; that comparison was not performed here.

**Repair:** independent controls for the geometric and Weil phases, with
all other data fixed, yielding all four combinations. State exactly what
each difference can establish. Seal that revised comparison before running
it; do not relabel the current two-input ablation after the fact.

## F4. A supplied texture is not the physical Yukawa calculation

The same helper constructs a handwritten 3-by-3 matrix from `eps1=s`,
`eps2=s**2`, `eps3=s**3`, absolute values and powers of `zeta5`. It does not
call the B1656 residue construction, `quaternionic_4d_yukawa`, or a
normalized overlap of physical operator modes. The description's
`n**2` Fourier-phase mechanism is not derived by assigning the three
powers `1,2,3` to entries.

Main's P-716 entry already recorded the texture problem and corner-symmetry
failure, citing the web seat. AGY's latest version correctly preserves
`breaks_13_vs_31_corner_symmetry=False`. This review **reconfirms** that
scope; it is not a new discovery of the earlier objection.

There is a genuine general algebraic positive. If, in a specified common
left-handed frame, `Yd=conj(Yu)` and singular values are nondegenerate and
ordered together, write `Yu=U D V†`. Then

    Ud=conj(U) up to column phases,
    Vmix=U† conj(U) up to rephasings,
    (U† conj(U))^T=U† conj(U).

Equal singular values and symmetric mixing magnitudes follow. They do not
depend on the template's particular coefficients. Nonzero J in a chosen
texture would not overcome that symmetry or select observed parameters.

**A correctly scoped negative:** this identity-conjugation sewing cannot
supply an asymmetric pair of corner magnitudes. It is not an exclusion
of every possible two-flank construction.

To extend the conclusion, compute the actual common-left-field transport.
If a relative intertwiner W is physically required, the comparison is
`Vmix=U† W conj(U)`, not automatically the preceding expression. Supplying
an arbitrary W would add an input. Nor does merely allowing W remove the
obstruction: if the full antiunitary sewing squares to one, its unitary
part satisfies `W conj(W)=I`, hence `W^T=W`, and the symmetry returns.
The actual lift, action, fields and common measuring frame decide which
statement applies. This is a conditional hand clarification, not a new
physical mechanism or an admitted spectrum.

## F5. Readback, numerical consistency and independent review differ

Theorem 154's dictionary at lines 28377–28413 assigns the level-surface
moduli and error bars literally. Theorem 156 reuses a literal high-precision
SnapPy complex length at lines 28872–28876. Those are imported numerical
inputs. Transforming them or checking consistency can be useful, but is
not a fresh meshing calculation or an interval certificate.

The Re-tau argument's identification of the tube fibre relies on the
upstream geometrical/numerical identification. Main B1852 explicitly says
so. The exact involution-class fact and numerical imaginary modulus have
different evidence grades. They should not be compressed into a single
unqualified "FORCED" value.

`G6_independent_cross_verification` and "hostile referee" functions are
author-written internal checks. A different precision or matrix basis is
not a non-authoring reviewer. Similarly a literal `data_looks: 0`, string
`0 of 19` or Boolean cannot certify the full execution's provenance.
The existing separately committed reviews retain their actual authorship
and scope; these internal checks must not impersonate them.

Repair: distinguish imported pin, recomputation, analytical proof,
numerical consistency, interval certificate and separately authored review
in the output schema. Preserve source values with exact producing pins.
No certificate should be inferred solely from a field's reassuring name.

## F6. A restricted sum is not the full interacting weave

Theorem 149's single-run sums have the declared population `n=6+5m`.
Its `z_b_multi` adds exactly two multirun examples, `(6,6)` and `(6,1,6)`.
That is not a normalization over every allowed cluster, separation and
history. A dominant individual saddle and its probability in an exhaustive
ensemble are different claims. Its displayed percentages need that
population in their names; they are not whole-weave probabilities.

The per-run congruence is genuine elementary mathematics. For the source's
upper-triangular L, `L^a(2,1)=(2+a,1)`. Its determinant with `(1,2)` is
`2a+3`, zero mod five exactly when `a=1 mod 5`. The R statement is alike.
This equivalence does **not** derive the requirement to compare at each run
boundary. Chat1's `PI2_IS_A_RATIONALE_NOT_A_DERIVATION` explicitly prices
that requirement and the clock/level readings.

Newer main work matters to both positives and negatives: B1855 reports an
all-defect excess-length result for charge at five without imposing the
stronger per-run restriction, while recording counterexamples to the
universal lcm-depth law from lcm 12 onward. B1856 gives a conditional quantum
reason to distinguish charge invisibility from mere dynamical symmetry.
This audit read those reports and the explore seat's proof account; it did
not rerun the exhaustive search or certify its code. Reuse that work rather
than promote old finite-range exclusions or demand Pi2 in every route.

The remaining physical premise is substantial: the level-five Weil state
space must be the physical registering sector, with the stated observables.
Minimization versus a normalized sum remains a choice unless derived.
The volume-weighted-sum obstruction in B1853 concerns its bounded-excess
ensemble, not every measure on all histories or every interacting action.

## Hand-verified positives that should remain

1. **Twisted Smith factors:** with the U and V supplied in Theorem 141,
   `U(A+I)V=diag(1,5)` and both changes of basis are unimodular. Thus the
   nonzero twisted fixed points at level N require `5|N`. Selecting the
   least such level, or requiring the finite triangle ladder, are named
   additional conditions. Ordinary finite congruence quotients are not
   the same thing as finite universal triangle quotients.
2. **Two periodic orbits:** `det(A-I)=-1`, `det(A+I)=5`, and
   `det(A²-I)=-5`. Removing the origin leaves four points in two period-two
   orbits. Their correct coordinates were derived above.
3. **Per-run congruence:** the determinant calculation above proves the
   all-a statement without relying on checking only a=1..25.
4. **Exact finite-level Kashaev value:** set `s=sqrt(5)`,
   `a=(5-s)/2`, `b=(5+s)/2`. In the declared figure-eight product-sum at
   N=5, the five terms are `1,a,5,5b,25`. Their sum is `46+2sqrt(5)`.
   The finite sum is given on printed page 4 of
   [Murakami's primary paper](https://arxiv.org/pdf/math/0008027).
   This is an exact knot invariant in the specified convention, not a
   measured coupling or a scale. Replacing it by its large-N leading
   exponential at N=5 is not an identity.
5. **Conjugate-pair mixing symmetry:** the SVD argument above supports the
   scoped corner obstruction and equal spectra, while leaving general
   physical sewing as an explicit duty.

No statement here upgrades the geometric all-k identities merely because
five stored benchmarks agree. Their global trace/gluing proofs and geometry
remain separate obligations. A trace identity such as
`tr(W)^2/(tr(W)^2-4 det(W))=coth²(length/2)` is exact once its hypotheses
hold; identifying that ratio with a named tetrahedron is an additional
geometric identification, not the trace identity alone.

## What should happen next

First repair F1–F3 and the evidence labels, preserving historical versions.
Then compute on the **joined** natural eigenline, modulus, spin/field
transport and kinetic normalization. The CP comparison must use the actual
coupling or explicitly stay a texture control. Audit negative conclusions
against their carrier, action, domain and sewing assumptions.

The promising input-reduction direction is to derive the physical
register/readout law that could justify charge invisibility and a state
distribution, rather than choosing a level-five space, readout and saddle
measure separately. Do not combine that proposed quantum readout with the
physical bridge's E8/spin/flavour mass complex without exhibiting the map.

All LR-specific claims keep their quantifier. For another allowed word,
`A=L²R=[[3,2],[1,1]]`, `det(A+I)=6`; the integer five is not a theorem about
every allowed word. This is not a programme-wide negative. It identifies
exactly where the distinguished root/sector enters and what an architectural
selection or interaction must explain.

Main's temporary unavailability does not turn these findings into main
acceptance. The independent source-complete review of the physical bridge's
own thirteen-check packet is also still pending: its reviewer hit a service
usage limit. No one has waived either execution requirement.
