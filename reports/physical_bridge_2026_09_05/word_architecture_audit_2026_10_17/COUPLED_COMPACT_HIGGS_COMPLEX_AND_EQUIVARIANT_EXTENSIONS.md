# The coupled compact complex retains a derived extension family

October 27, 2026. UNREVIEWED author proof, no scientific execution.
This extends the conditional ordinary rank-two compact model, not its
identification with the physical surface/Majorana-Weyl theory. It does
not derive a Standard Model generation count or an observed parameter.

## 1. Recovery, scope and the calculation that replaces a supplied kernel

Reuse EQUIVARIANT_NILPOTENT_DIVISOR_AND_LOCALIZED_MODE_DUTY: on the fixed
smooth genus-three Q8 cover, a stable nonzero nilpotent rank-two Higgs
pair with trivial determinant and preserved full Q8 symmetry has kernel
L with L^2=K^(-1). Put S=L^(-1), and V=S tensor E. There is an exact
sequence, not necessarily split,

  0 -> O -> V -> K -> 0.                                  (1)

The induced ordinary Higgs map phi:V->V tensor K factors through the
quotient K and identifies it with the subbundle O tensor K of the target.
The scalar normalization here uses the original nowhere-zero Higgs map,
not a freely chosen extra mass. It does not make this K-valued map a
physical scalar Yukawa without the actual Clifford/field identification.

The previous B1767 audit gave a split-bundle Higgs-complex control.
Here we compute the entire same compact complex WITHOUT that split
assumption, and exhibit its equivariant background freedom. The scope
is this ordinary complex on a closed curve, not a boundary-index result
for the full generated architecture. Earlier paired physical results
and their domains are not replaced by this complex.

## 2. The actual coupled equations and its compact operator

The two-term holomorphic complex is C=[V --phi--> V tensor K] in
sheaf degrees 0 and 1. Its Dolbeault total resolution on Y has

  C0=Omega^(0,0)(V),
  C1=Omega^(0,1)(V) plus Omega^(0,0)(V tensor K),
  C2=Omega^(0,1)(V tensor K),
  D0 s=(dbar_V s,phi s),
  D1(a,h)=dbar_(VK) h-phi a.                              (2)

Holomorphy of phi gives D1 D0=0. These equations include the companion
connection/form component; they do not select only canonical forms.
After choosing smooth positive metrics, D+D^dagger is the compact
selfadjoint elliptic operator with its standard closed domain. At a
nonzero real cotangent vector the Dolbeault symbol on a complex curve
is an isomorphism from degree zero to degree one; the phi terms are
order zero. Thus the total symbol sequence is exact. Compact elliptic
Hodge theory identifies its harmonic subspaces with the hypercohomology
of C. This assertion fixes an ordinary mathematical operator, not the
physical spin grading or a surface reduction that has not been shown.

The coupled adjoint fluctuation complex is different:
C_ad=[End_0(E) --ad_Phi--> End_0(E) tensor K]. It includes the actual
connection/Higgs deformation modulo infinitesimal gauge transformations.
Its total differential is as in (2) with ad_Phi in place of phi.
Both complexes keep their own bundles and their own counts below.

## 3. Counts that do not require splitting the bundle

In (1), ker(phi)=O and coker(phi)=K^2 because image(phi) is the whole
subbundle K in V tensor K. The sheaf-cohomology spectral sequence has
only these two rows. On a curve all possible d2 targets lie in sheaf
cohomology degree at least two and vanish. It follows that

  Hhyper^0(C)=H0(O),
  0 -> H1(O) -> Hhyper^1(C) -> H0(K^2) -> 0,
  Hhyper^2(C)=H1(K^2)=0.                                  (3)

The exact sequence does NOT supply a canonical orthogonal splitting.
At genus three Riemann-Roch and Serre duality give

  dim Hhyper^0=1, dim Hhyper^1=3+6=9, dim Hhyper^2=0.       (4)

As a consistency check chi(V)=deg(V)+2(1-g)=4-4=0,
chi(VK)=12-4=8, so chi(C)=-8=1-9. The even/odd Fredholm
index of this stated total complex is -8. This is its INTERNAL grading,
not a derived four-dimensional chiral charge index. At phi=0 the sheaf
complex changes and (3) does not apply; this is a nonzero zero-free
nilpotent calculation, not a zero-Higgs approximation.

For the adjoint, local nilpotent matrix algebra gives
ker(ad_Phi)=K^(-1). Trace duality identifies its cokernel with K^2:
the annihilator of im(ad_Phi) in the target dual is the centralizer,
and the trace pairing and the K twist supply precisely these lines.
Equivalently, in local frames ad_N maps E_- to H and H to -2E_+;
only the lower target component survives. This calculation glues,
independently of the splitting in (1). Thus

  Hhyper^0(C_ad)=0,
  0 -> H1(K^(-1)) -> Hhyper^1(C_ad) -> H0(K^2) -> 0,
  Hhyper^2(C_ad)=0,
  dim Hhyper^1(C_ad)=6+6=12.                              (5)

The Euler check is chi(End_0 E)-chi(End_0 E tensor K)
=-6-6=-12. Equations (3) and (5) retain the global bulk pieces that
a local torsion-only analysis would omit. They are compatible with the
previous constant-root local cokernel having no torsion. The count is
extension-independent; harmonic profiles and physical norms are not.

## 4. Full Q8 representations, not a guessed surviving triplet

Use the established canonical representation H0(K)=1 plus rho, where
rho is the faithful two-dimensional quaternion representation. The
multiplication map Sym^2 H0(K)->H0(K^2) is an isomorphism on this curve.
It can be checked without assuming it for every genus-three curve:
with omega0=dx/w^2, omega1=dx/w^3, omega2=x dx/w^3, a linear relation
among their six pair products, after division by dx^2/w^6, would give

  A w^2+(B+C x)w+D+E x+F x^2=0.

The smooth superelliptic function field has basis 1,w,w^2,w^3 over C(x);
P_3(x) has simple zeros, so w^4=P_3(x) is irreducible over C(x).
All coefficients therefore vanish. The products are holomorphic and
dim H0(K^2)=6, proving the isomorphism for this carrier.

For Q8, Sym^2 rho is the sum of its three nontrivial one-dimensional
characters chi_i,chi_j,chi_k. For example the centre acts trivially,
while an element i has symmetric-square trace -1, giving the three
nontrivial characters of Q8/{1,c}. Hence

  A := H0(K^2) = 1 plus rho plus chi_i plus chi_j plus chi_k. (6)

Its invariant dimension is one, agreeing with our earlier independent
quotient-divisor calculation. Serre duality gives H1(K^-1)=A^*,
while H1(O)=H0(K)^*. These Q8 representations are self-dual up to
isomorphism. Finite-group complex representations are semisimple,
so (3) and (5) imply REPRESENTATION isomorphisms

  Hhyper^1(C) = 2*1 plus 2*rho plus chi_i plus chi_j plus chi_k,
  Hhyper^1(C_ad) = 2*A.                                   (7)

Thus each degree-one INVARIANT subspace has dimension two under these
canonical combined actions. The total fundamental complex also has its
one invariant degree-zero mode. Neither selecting just H0(K), nor
asserting that quotient invariance leaves three of these modes, follows
from this calculation. A different charged bundle, character or physical
grading must be computed explicitly. This does not exclude physical
three-family sectors elsewhere in the architecture.

## 5. A genuine equivariant extension family survives the fibre equations

There is more than an unclassified possible extension. Let beta be a
smooth dbar-closed (0,1)-form valued in K^-1. On the smooth split bundle
O plus K define

  dbar_beta = [[dbar_O,beta],[0,dbar_K]],
  phi = [[0,id_K],[0,0]] : V_beta -> V_beta tensor K.        (8)

The beta terms commute with this upper nilpotent phi (both relevant
products vanish), so phi is holomorphic for dbar_beta. The Dolbeault
operator is integrable on the curve. Its extension class is [beta] in
H1(K^-1). A nonzero class gives a nonsplit holomorphic sequence (1).
This is an explicit holomorphic construction, not a numerical ansatz.

Choose a Q8-invariant metric and a harmonic representative of an invariant
class. Since the induced Laplacian commutes with the finite group, this
representative is invariant. The canonical Q8 action on O plus K then
preserves both dbar_beta and phi. By (6) and Serre duality,

  dim H1(K^-1)^Q8=1.                                     (9)

Every such class therefore supplies a combined-equivariant pair in (8).
Untwist by a chosen S with S^2=K to get E_beta=V_beta tensor S^-1 with
trivial determinant. The only saturated invariant line for a nonzero
rank-one nilpotent Phi is its kernel S^-1, of degree -2; any invariant
line has its generic fibre there. Thus the pair is stable for every
beta. The already-used compact Hitchin existence theorem supplies a
harmonic solution for each fixed holomorphic pair, unique within that
orbit. It does not choose one beta from the family. A standalone honest
Q8 action on S or E is not asserted: (8) constructs the honest COMBINED
bundle action, with the previous spin/gauge-lift qualifications intact.

Distinct cohomology classes cannot be identified by a pair isomorphism
preserving this normalized phi. Its intrinsic kernel must be preserved,
so in smooth splittings it is upper triangular. Its diagonal maps on O
and K are constants p,q; intertwining the identity Higgs component
forces p=q. The remaining upper entry changes beta by a dbar-exact
K^-1-valued term. Hence it leaves [beta] unchanged. This proves a
one-complex-parameter family of inequivalent normalized combined pairs;
the unchosen scale of a BASIS in that line is a coordinate convention,
not an extra numerical physical parameter. Character twists or a demand
for a different standalone lift need their own equivariant test.

A finite-dimensional positive metric on this family is not supplied by
(9). Its actual harmonic metrics and mode overlaps vary with the class.
The FULL surface equations may couple beta(tau) to horizontal fields,
characters, regularity and the end. The fibre theorem proves neither
that arbitrary beta(tau) is a surface solution nor that the end allows
all constant or growing classes. Those are the next physical duties.

## 6. Primary reading and the correct bridge to the surface

Personally read all of Appendix D of T-Branes and Monodromy,
https://arxiv.org/html/1010.5780, equations D.1–D.24 (October 27).
The surface source uses the mapping cone of ad_Phi and dbar. Its reduction
to global sections of a quotient has cohomology hypotheses, not just a
local nilpotent matrix. This supports the need to retain bulk and gauge
companions. It does not identify the ordinary CURVE complex (2) with
that SURFACE complex, whose Higgs takes values in K_X rather than K_Y.
The earlier compact Hitchin theorem remains the theorem for the curve.

The next calculation is therefore the relative/horizontal and end
completion of this derived fibre family in the admitted physical parent,
including its charged sectors and real structure. A full solution would
supply the family dynamics and the actual vertex/kinetic maps. Simply
setting beta=0, retaining only three canonical forms, or renaming the
curve index as physical chirality would restore supplied inputs.

## 7. Dependency ledger and verification status

Retained: generated carrier and its full Q8 action; specified ordinary
rank-two action/complex; stable nonzero nilpotent branch; correlated spin
root and combined action; smooth compact metrics/domain. These are
conditional hypotheses, not paid foundational rows.

Reduced: the mode COUNT and Q8 representation of the stated compact
coupled complexes no longer depend on a supplied split extension.
The earlier degree/divisor reduction is retained. Exhibited remaining
freedom: an actual one-complex-dimensional invariant extension family,
with compact harmonic solutions but uncomputed physical metric and full
surface/end dynamics. No physical parameter is claimed predicted.

Verification is author hand derivation, with algebraic Euler, local-rank,
product-basis and invariant-dimension cross-checks above. No claim of an
independent review or executed scientific test is made. Searches of the
current report tree and main's frontier/docs for 'hypercohom' and 'Higgs
complex' recovered the previous split control and old cup-product memos;
this is source location, not an exhaustive novelty/absence certificate.
Earlier execution packages, reviews and historical failures are unchanged.
