# Height-308 holomorphic Yukawa cup-product audit

**Campaign item:** `OA-C1034`  
**Audit date:** 2026-08-24

**R017 provenance note:** copied from the local closure bank on 2026-08-26 so the primary
derivation is no longer single-homed.  The self-contained Python certificate shipped with this
cell covers the exact up-type naturality theorem and the Wilson-sector scope.  The down-sector
Sage chain artifacts discussed below are explicitly not part of R017.

## Verdict

The norm-height-308 map now has the pointwise local-freeness, charged
cohomology/Higgs and all Hoppe-stability gates needed to *define* its
holomorphic Yukawa cup products.  A cohomological naturality argument now
evaluates the entire up-type map:

```text
mu_u = 0,    rank(mu_u) = 0
```

This is an exact zero theorem at the height-308 point (and on any exact-six
branch satisfying the same displayed cohomology gates); it does not depend on
a choice of Čech representatives or on an unnormalised residue.  The
down-type map `mu_d` still has no chain-level evaluation, rank, or nonzero
entry.  Thus the residue machinery remains necessary for `mu_d`, but no
longer for `mu_u`.

This is a narrower result than the earlier character audit: the missing datum
is now identified at chain level, rather than being described only as an
unknown coefficient.

## Fixed input and the two maps

Let `Y` be the selected norm hypersurface on the `C12` cover and let `V_308`
be the rank-five bundle defined by the exact 44-coordinate height-308 map.
The established inputs are

```text
A = H^1(Y,V_308)             = 3 Reg + chi_1+chi_3+chi_7+chi_9+chi_10+chi_11,
B = H^1(Y,Lambda^2 V_308)    = 3 Reg + chi_0+chi_11,
C = H^1(Y,Lambda^2 V_308*)   = chi_0+chi_1.
```

`A` and `C` are pointwise cohomology certificates at the exact-six branch;
the displayed `B` is the stable-branch equivariant index plus Serre-duality
consequence used by the BCDD spectrum calculation.  At height 308 both Hoppe
exterior vanishings have now been certified, so the stability premise needed
for that spectrum statement holds at this point.

With a trivialisation of `det(V_308)` and of the holomorphic three-form, the
two holomorphic maps are

```text
mu_u: Sym^2 A tensor C -> H^3(Y,O_Y),
mu_d: A tensor B tensor B -> H^3(Y,O_Y).
```

The second map is used with its two `B` inputs in the distinct matter/Higgs
roles; if they are identified before that choice, the SU(5) contraction uses
the appropriate antisymmetric same-space sector.  After descent, `mu_u`
gives the `10 10 5_H` coupling, while `mu_d` gives `10 5bar 5bar_H`; the
charged-lepton matrix is the SU(5) transpose of the latter after conventional
basis choices.

These formulas define holomorphic, unnormalised tensors.  They do not define
physical Yukawas.

## Exact Wilson-sector result

For `k=4`, the selected cohomology characters are

```text
u^c: A_4 (dim 3)       Q: A_8 (dim 3)       e^c: A_0 (dim 3)
d^c: B_4 (dim 3)       L/H_d: B_0 (dim 4)   H_u: C_0 (dim 1).
```

For `k=8`, the labels `4` and `8` interchange in the `u^c,Q,d^c` sectors;
the dimensions and conclusions do not change.  Character sums for every
MSSM operator are zero.  Therefore `C12` imposes no family texture zero.
It permits

```text
up:            Sym^2(C^3),        dimension 6,
down/lepton:   C^3 tensor C^3,     dimension 9.
```

The single up-type Higgs is the one-dimensional `C_0`.  The down-type
candidate is not a line: `B_0` is four-dimensional and carries the trivial
`C12` action.  Every line in it is equivariant, so the character data leave a
projective `P^3` of possible `H_d` lines (and a corresponding choice of the
three lepton directions).  No Higgs line is selected.

Thus the precise rank statement is:

```text
rank(Y_u)       0, exactly;
rank(Y_d(h_d))  not computed for every h_d in P^3;
rank(Y_e)       not computed, with Y_e=Y_d^T holomorphically once h_d is chosen.
```

The permitted tensor spaces are not claims of maximal rank or nonzero
coefficients.  In particular, the six-dimensional up selection space is
annihilated by the actual `mu_u` map at this bundle point.

## Why the down-type cup product is still absent

For `mu_d`, the committed exact complexes stop one operation short of the
required calculation:

- `verify_marked_pseudoinverse_cech.sage` gives explicit toric Čech source
  cocycles and the `C^18 -> C^21` connecting map, yielding the two-dimensional
  `C` character space.  It does not build a multiplicative chain map into a
  total complex for `A,A,C`.
- `verify_marked_pseudoinverse_phi.sage` and
  `bundle_low_height_scout.sage` construct quotient presentations sufficient
  for `A`, the `372 -> 312` rank gate, and local freeness.
- `certify_yukawa_down_obstruction_308.sage` now chooses explicit
  `GF(1009)` representatives for the 33-dimensional connecting quotient and
  diagonalises its induced `C12` action.  It does not construct the five
  Serre-dual tail cocycles over `Q(zeta_12)` or their cup-product lifts.
- `verify_hoppe_wedge.sage` and `verify_hoppe_lambda3.sage` prove only the
  `H^0` exterior vanishing maps.  They do not compute the `H^1(B)`
  hypercohomology representatives needed for `mu_d`.

In particular, the index/Serre computation fixes the character of `B`, but
not a basis of `B` nor a chain-level product involving it.  A map between
cohomology dimensions is not its Yoneda/cup product.

The local campaign's long-exact certificate
`certify_yukawa_down_obstruction_308.sage`
now identifies and dimensions the omitted term.  It proves

```text
dim H^0(K) = 60,
rank[H^0(Lambda^2 G) -> H^0(K)] = 27,
immediate connecting quotient dimension = 33.
```

The next term is exactly `H^1(Y,Lambda^2 G)`.  In the BCDD ambient exterior
sequence, the `C^18 -> C^21` map has kernel `chi_10+chi_11` (dimension `2`),
so it has rank `16` and cokernel dimension `5`.  The source line-bundle
vanishings, restriction sequence, and Serre duality identify this cokernel
dually with `H^1(Y,Lambda^2 G)`.  Thus the type-correct abstract
presentation is

```text
B = (33-dimensional connecting quotient) + (5-dimensional Serre-dual coker),
dim B = 38.
```

Equivalently, the restriction ledger is
`h^bullet(Y,Lambda^2 G|Y) = (27,5,2,0)`; the `H^1=5` entry is precisely the
tail entering `B`.

For the untwisted ambient ledger, the coker has characters
`chi_0+chi_4+chi_6+chi_8+chi_10`; its Serre-dual missing term has
`chi_0+chi_2+chi_4+chi_6+chi_8`.  These are character-labelled abstract
basis slots, not explicit toric cocycles.

At the good prime, the connecting quotient is now more concrete.  The
certificate constructs a `672 x 33` representative matrix, verifies that the
27-dimensional image is invariant before passing to the quotient, and finds
the raw character multiplicities

```text
(2,4,3,3,2,3,2,3,2,3,3,3).
```

Adding the five raw tail characters gives
`3 Reg + chi_1 + chi_2`.  The `(3,4)` determinant linearisation on
`Lambda^2 V` is `chi_-2`, so the physical total becomes exactly
`3 Reg + chi_0 + chi_11`, agreeing with the independent index/Serre ledger.
This closes the character convention as well as the dimension gap.  It still
does not provide characteristic-zero tail Čech cocycles or a multiplicative
down-type chain map, so no down-Yukawa rank follows.

The corresponding objection does **not** apply to `mu_u`: its zero follows
before any residue reduction.  Write `L=O_Y(H)` and let

```text
0 -> V -> G_Y -> L -> 0                                      (E)
0 -> K_1 -> Lambda^2 G_Y^* -> Lambda^2 V^* -> 0             (W)
```

be the two exact sequences used in the BCDD construction.  The certified
ambient/restriction cohomology gives

```text
H^1(Y,G_Y) = 0,
dim H^0(Y,L) = 48,
dim H^1(Y,V) = 42,
H^1(Y,K_1) = H^2(Y,K_1) = 0.
```

The first line makes the connecting map in (E) surjective, so every
`a in H^1(Y,V)` maps to zero in `H^1(Y,G_Y)`.  The last line makes the map
`H^1(Y,Lambda^2 G_Y^*) -> H^1(Y,Lambda^2 V^*)` an isomorphism.  Lift a
third input `c` through this isomorphism.  Compatibility of wedge and
contraction with `V -> G_Y` gives

```text
<a cup b, c>
  = < i(a) cup i(b), c_tilde >
  = 0,
```

where `i(a)=i(b)=0` in `H^1(Y,G_Y)`.  This proves every component of
`mu_u: Sym^2 H^1(V) tensor H^1(Lambda^2V^*) -> H^3(O_Y)` is zero, including
the three-family Wilson slices.  The required hypotheses are not genericity
claims: `H^1(G_Y)=0` follows from the BCDD line-bundle restriction sequence,
and `H^1(K_1)=H^2(K_1)=0` follows from the exact height-308 `372 -> 312`
surjectivity gate plus Serre duality.

This is the same derived/diagrammatic naturality principle used to reduce
monad triple pairings to multiplication in the explicit quintic calculation
of [Donagi--Reinbacher--Yau](https://arxiv.org/abs/hep-th/0605203), but here
the certified extension cohomology forces the resulting pairing to vanish.

An exact continuation for `mu_d` must construct, over `Q(zeta_12)`, a common
multigraded toric Čech (or quasi-isomorphic hypercohomology) model for the
two `B` factors and `A`, explicit comparison maps from the monad
complexes, and compatible multiplication/contraction maps to a representative
of `H^3(O_Y)`.  It must then restrict the resulting tensor to the Wilson
sectors above and either derive an `H_d` line or report the matrix pencil
`Y_d(h_d)` over `P^3`.

Until that computation is present, it would be false to infer a generic
nonzero determinant, a rank, a texture relation, or a numerical coefficient
for `mu_d` from the stable bundle or its characters alone.  For `mu_u`, the
exact rank-zero result above is stronger than a selection-rule statement.

## The surviving `P10` is real, but Yukawa nonconstancy is not yet proved

The independent presentation-quotient certificate proves that the
Kodaira--Spencer map of the stable locally-free `P10` map family has rank ten
in descended `Ext^1(V,V)`.  Hence nearby points are genuinely non-isomorphic
stable bundles, not a harmless change of monad presentation; they give ten
physical bundle-modulus directions (and the full hyperExt computation finds
two further invariant directions).

That result is **not** a proof that `mu_d` varies.  A family of non-isomorphic
bundles can in principle have constant selected trilinear tensors, so neither
the positive-dimensional moduli space nor variation of the raw `Phi`
coefficients licenses a flavor claim.  The up-type map is already identically
zero on the certified exact-six branch by the factorisation argument above;
the missing comparison is specifically the down-type evaluator.

The decisive remaining finite test is clear: choose an exact tangent
direction `delta Phi` in the branch, certify two locally-free Hoppe-stable
good-prime points `Phi_0`, `Phi_1`, evaluate their common-basis `mu_d` tensors,
and compare the determinant/minors of the `P3`-linear down-matrix pencil.
Until this test is run, P10 is physically consequential as a bundle-modulus
family, but its specific down-type holomorphic flavor nonconstancy remains
not computed; the up-type tensor remains identically zero throughout the
exact-six cohomological factorisation locus.

## First multiplicative Čech construction

The missing cochain-level construction has a small exact first step.  Let
`U_sigma` range over the 36 maximal toric affine charts (three `C12` orbits).
Writing the local components of the height-308 map as `Phi_a`, the already
certified unit-ideal calculation says

```text
(f, Phi_1, ..., Phi_12) = (1) on every U_sigma.
```

Consequently the principal refinement

```text
U_(sigma,a) = Y intersect U_sigma intersect {Phi_a != 0}
```

covers `Y`.  On each such open the explicit local splitting is simply

```text
s_(sigma,a)(1) = e_a / Phi_a  in B|U_(sigma,a),
Phi(s_(sigma,a)(1)) = 1.
```

Its image in `G=B/(6 O)` splits `Phi:G -> O(H)`.  On a double overlap,

```text
theta_(alpha,beta) = s_beta - s_alpha
```

is a `V`-valued Čech-one cochain because its contraction with `Phi` is zero.
For a global `H`-section `c`, the connecting representative is

```text
delta(c)_(alpha,beta) = theta_(alpha,beta) c.
```

This gives the common multiplicative Čech DGA

```text
C^p(U, Lambda^q V),
d = delta_Cech,
(x,y) -> (-1)^(q p') x wedge y,
```

on the 432 formal principal opens.  To calculate through an exterior monad
resolution `M^bullet`, replace this by the hypercohomology total complex
`Tot C^p(U,M^q)` with differential
`delta_Cech+(-1)^p d_M`.  Thus two representatives obtained from `A=H1(V)`
can now be wedged at cochain level.  The existing two `C` cocycles from the
36-chart construction restrict to this refinement, so this is the correct
starting complex for `mu_u`.

The local campaign's good-prime certificate `attempt_yukawa_cech_308.sage`
checks the three orbit representatives, transports the cover by `C12`, and
verifies the unit-ideal and transition identities.  A good-prime unit ideal
is the same characteristic-zero local-freeness witness used in the existing
certificates; it proves the existence of local splittings over
`Q(zeta_12)` but does not print a prohibitively large characteristic-zero
Bézout vector.

The two ambient Higgs generators are now also chain-level rather than merely
dimension data.  The reconstructed `C18 -> C21` kernel has an explicit
good-prime correction into two nonzero `Lambda2 G^*` Čech-one cocycles.  More
precisely, if `q: Lambda2 B^* -> B^* tensor W^*` is the middle map in the
`K2` sequence, the script lifts the `q`-image boundary through one fixed
linear section of `q` and replaces `c` by `c-delta q^{-1}t`.  It checks both
the Čech cocycle equation and `q(c-delta q^{-1}t)=0`, and prints a nonzero
support witness.  This is a representative of each `C=H1(Lambda2 V^*)`
class after the standard restriction/quotient maps in the BCDD exterior
sequence.

Likewise, the `H1(V)` connecting quotient is now represented explicitly:
the 49 anticanonical Cox monomials are quotiented by `f` and the twelve
`B`-sections (a seven-dimensional relation space).  The resulting 42
polynomial representatives are diagonalised at the good prime.  After the
BCDD determinant twist by `chi_1`, the physical `k=4` `u^c` and `Q` spaces
are the three-dimensional raw-character 3 and 7 quotients, respectively.

The displayed construction is not needed to evaluate `mu_u`: the exact
factorisation argument above proves that its contracted class is a Cech
coboundary for every input.  A global frame-compatible contraction and toric
hypersurface trace `H3(O_Y) -> Q(zeta_12)` are still required for `mu_d`, and
the construction still does not provide `H1(Lambda2 V)` representatives.

There is no ambiguity about the required contraction formula.  In homogeneous
Cox frames, for a quotient polynomial `c` and two refined opens indexed by
components `a,b`, its boundary representative is

```text
d_c(a,b) = x_b*c/Phi_b - x_a*c/Phi_a  in G.
```

Writing a corrected Higgs cochain on a toric double overlap as
`h=sum_(i<j) h_ij/(x_i*x_j) e_i^* wedge e_j^*`, the degree-three up-type
cochain is the ordinary alternating contraction

```text
(d_c1 cup d_c2 cup h)_(alpha,beta,gamma,delta)
 = contraction(h_(gamma,delta),
               d_c1(alpha,beta) wedge d_c2(beta,gamma)).
```

All Cox degrees cancel, so this is a degree-zero rational Čech-three
cochain.  For the up-type inputs the factorisation theorem proves that its
class reduces to zero modulo Čech coboundaries on `Y`; a nonzero value of one
*local rational cochain* would not contradict that result.  For `mu_d`, the
reduction modulo Čech coboundaries and the normalized toric residue remain to
be implemented, so no local rational value is reported as a Yukawa witness.
The hypersurface differential-form/algebraic correspondence of
[Blesneag--Buchbinder--Candelas--Lukas](https://arxiv.org/abs/1512.05322)
and its complete-intersection extension
[Blesneag--Buchbinder--Lukas](https://arxiv.org/abs/1607.03461) supports this
ambient/Koszul-residue strategy, but those works do not themselves evaluate
this toric BCDD monad; the necessary toric comparison and residue maps remain
our explicit next calculation.

## Connecting-sector down evaluator

The 432-open principal refinement now supplies the common chain type

```text
C1(V) x C1(Lambda2V) x C1(Lambda2V)
  -> C3(Lambda5V) -> C3(O_Y) -> H3(O_Y).
```

For the first physical Wilson slice the raw spaces are `A7`, `B6`, `B2` of
dimensions `3,2,3`, becoming physical `(Q8,dc4,Hd0)` after the determinant
twists.  The resulting connecting-only calculation has 18 inputs.  The
certificate checks the Cech cocycle, cup and determinant signs, but identifies
the precise final missing map rather than inventing values:

```text
T_connecting : GF(1009)^18 -> H3(O_Y) -> GF(1009), shape 1 x 18.
```

The absent datum is the common determinant-frame comparison and normalized
toric residue/trace row.  Consequently no nonzero down entry or rank is yet
claimed.  See `YUKAWA_DOWN_CONNECTING_EVALUATOR_308.md` and
`evaluate_yukawa_down_connecting_308.py`.

## Five-dimensional tail: explicit dual quotient, not yet Cech-one classes

The exact good-prime `C18 -> C21` map has rank 16.  Its raw cokernel labels are
`(0,4,6,8,10)`.  Explicit independent quotient lifts and a complete basis of
the left annihilator have now been printed.  Under Serre-dual inverse phase,
the five dual functionals have labels `(0,2,4,6,8)`, matching the long-exact
character ledger.

This closes the abstract quotient-basis problem but not the chain-level one:
the annihilator rows are explicit Serre-dual quotient functionals, not raw
`Lambda2G`-valued Cech-one cocycles.  A chain-level Serre trace/connecting map
is still required before these five slots can enter the down cup evaluator.

## Holomorphic versus physical data

Even an exact evaluation of `mu_u` and `mu_d` would only produce holomorphic
coordinates after choices of cohomology bases and a three-form normalization.
Canonical Yukawas also need matter/Higgs Kähler metrics, a selected vacuum and
`H_d` line, threshold matching and RG evolution.  Schematically,

```text
Y_u,phys = K_10^(-T/2) Y_u,hol K_10^(-1/2) K_Hu^(-1/2),
Y_d,phys = K_10^(-1/2) Y_d,hol K_5bar^(-1/2) K_Hd^(-1/2).
```

Those metric and vacuum data remain outside the present algebraic
certificate.

## Reproduction

```text
PYTHONDONTWRITEBYTECODE=1 python3 \
  certificates/r017_yukawa_primary/verify_yukawa_cup_product_308_scope.py
```

This R017 provenance cell ships the exact up-type naturality proof and its
scope certificate.  The Sage/down-sector artifacts named above remain in the
local campaign bank and are not silently represented as part of this cell;
the down/lepton cup-product evaluator remains open.  The copied report keeps
their results visible as provenance, but only the command above is promised
as a branch-local self-contained reproduction here.
