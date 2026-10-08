# Form kernels and physical fermion interpretation

Conditional authored argument, sealed before execution. Finite exact
checks support its algebra; they are not a machine proof of a global
PDE, nonauthor review or a complete physical compactification.

## Quaternion cover and complete form kernels

Let the monodromies of a and b be i and j in Q8. Their commutator is -1.
The regular cover of the punctured elliptic curve has eight squares, with
right gluing q -> qi and upper gluing q -> qj. Its four vertices after
compactification are the pairs {q,-q}. Horizontal and vertical oriented
edges give C1 of dimension16; C2 has eight faces and C0 four vertices.
Face q has boundary h(q)+v(qi)-h(qj)-v(q). Each edge boundary uses its
endpoint pair. Thus d1 d2=0. The ranks are predicted 3 and7, giving H1
dimension6. Each lifted puncture has branch order2. Riemann--Hurwitz:
2g-2=8(2*1-2)+4=4, hence g=3.

Left deck multiplication acts on this complex and preserves orientation.
H0 and H2 are trivial. The alternating chain trace therefore gives H1
character (6,-2,2,2,2,2,2,2), ordered 1,-1,i,-i,j,-j,k,-k. This is
2*1+2*rho_Q. Holomorphic deck-invariant differentials descend to the
elliptic quotient and have dimension1. The holomorphic space has dimension
g=3 and no nontrivial one-dimensional summand can occur in full H1.
Its remaining two dimensions must be a single rho_Q. Accordingly
H^(1,0)(cover)=1+rho_Q, and the conjugate Hodge space has the same Q8
character. This does not erase the nonreal MOVE character carried by
W21's triplet: the gauge group, Q8 and move group are different actions.

For the complete cusp, the L2 norm of a holomorphic one-form is conformally
invariant. Upstairs a holomorphic one-form on a punctured disc is L2 iff
its Laurent expansion has no negative powers, so it extends across the
filled point. Constants are finite-norm scalar zero modes because the
cusp has finite area; a holomorphic pole in a scalar is not L2. The
complete unitary differential operator uses its closed complete-manifold
domain; an L2 harmonic scalar is parallel, by the cutoff energy argument.
These facts identify its harmonic scalar and one-form kernels with the
compact-cover invariant constants and regular differentials. No finite
puncture projector is supplied.

Taking Q8-equivariant coefficients, a rank-six 3*rho bundle has three
one-forms of either Hodge type and no scalar zero sections. For the FULL
adjoint, the already-recorded character (248,24,28,28,28,28,28,28) gives
55 invariant constants, 56 rho multiplicities and27 of each nontrivial
character. Therefore the form kernels are

    scalar:55, holomorphic one-form:55+56=111,
    antiholomorphic one-form:111, volume-form:55.

The rank-six triplet is already inside the multiplicity calculation;
111 is not to be multiplied by three. The Dolbeault harmonic Euler
number is 55-111=-56, while full de Rham parity gives55-222+55=-112.
Opposite holomorphic-degree Dolbeault blocks give opposite Euler numbers.
These different gradings are not freely interchangeable physical chirality
definitions. This packet reports KERNEL/EULER data, not an independently
certified global Fredholm theorem for the full physical parent.

## Physical parent and reality

Use the (1,1) gauge-multiplet Lorentz/R-symmetry decomposition from
Andrews--Dorey, section3 and AppendixA. In charge units where a vector
has charge2, the independent left Weyl fields are

| Slot | Q45 | QA | QT=Q45+QA | Internal type |
|---|---|---|---|---|
| lambda plus | 1 | 1 | 2 | one-form |
| lambda minus | 1 | -1 | 0 | scalar |
| psi B1 | -1 | 0 | -1 | ordinary spin |
| psi B2 | -1 | 0 | -1 | ordinary spin |

Every right slot is its conjugate with opposite charges, paired by the
parent Majorana condition. Counting those conjugates as four more
independent left fields would be incorrect. Choice of internal orientation
interchanges the holomorphic and antiholomorphic naming of the one-form
slot, not its complete gauge dimension. The bosonic companions are the
four-dimensional gauge field, real internal connection one-form and four
real R-symmetry scalars that become internal spin fields. The latter and
the psi sector are retained as obligations, not silently removed or
declared massive using a spherical spectrum on our punctured torus.

The lambda block has the scalar/form coupled first-order kinetic operator.
In Kähler notation its symbol is that of sqrt(2)(bar partial_A plus its
adjoint); squaring gives the corresponding nonnegative Laplacian. Its
one-form coefficients inherit the one-form norm, not the ordinary-spin
conformal weight. For z=w^2, z^(-1/2)dz pulls back to2dw, proving that
the branch-supported coefficient can be a regular finite-norm form.

For g=dt^2+exp(-2t)dtheta^2 the scalar Laplacian zero-angular block is
-partial_t^2+partial_t. The unitary change u=exp(-t/2)f converts it to
-partial_t^2+1/4. The matching scalar/form first-order block is

    [[0, -partial_t+1/2], [partial_t+1/2, 0]],

whose square is that operator on both entries. Hence its zero-angular
block does not reproduce the massless ordinary-spin cusp block squared
-partial_t^2 from the preceding packet. This is local spectral data;
global graph/Fredholm acceptance and the full companion sector remain
separate duties. No spinor obstruction is retracted outside its scope.

Source: https://arxiv.org/abs/hep-th/0601098, section3, AppendixA and the
coupled fermion explanation at the end of section6. That paper constructs
an abelian spherical benchmark, not this full nonabelian cusp theory.

## Complete gauge roster and a mass protection positive

Let H=SU(3)_color x SU(2)_weak x SU(3)_family, a subgroup of the compact
Q8 centralizer K in E8. Under the standard SU(3)xSU(2)xSU(6) branching
and 6=2_Q tensor3_family, the invariant55 is

    (8,1,1)+(1,3,1)+(1,1,8)+(3,1,6)+(bar3,1,bar6).

The rho multiplicity56 is

    (3,2,bar3)+(bar3,2,3)+(1,2,8)+2(1,2,1).

Conventions for6 versusbar6 may swap the two conjugate coloured blocks;
both remain. The exterior identity Lambda^3(2 tensor3)=(4,1)+(2,8)
explains the two singlet-family doublets: Q8 restriction of the spin3/2
four is TWO rho copies. Dropping those copies changes the mass/anomaly
roster. Restricting a hypercharge Cartan to diag(f1,f2,f3), sum fi=0,
each coloured weak weight has its conjugate; the six family-adjoint
root weights fi-fj pair, with four neutral doublets. All complex SM
charge asymmetries of the full FORM sector are zero. This does NOT
assert that the uncomputed companion, flux, defect or other architecture
can never provide a complex chiral spectrum.

There is nevertheless a genuine Weyl mass distinction. A quadratic mass
of independent left Weyl fields uses a SYMMETRIC gauge bilinear. On
R=(1,2,8_family), the only H-invariant complex bilinear is epsilon_2
tensor Killing_8. It is nondegenerate and SKEW; its symmetric projection
vanishes. This is verified by solving actual invariant-bilinear equations
for sl2 and the sl3 adjoint, not merely labelling the representation.
There is one R summand in the form roster and no other isomorphic partner.
At an H-preserving origin these sixteen complex field coefficients have
no bare quadratic Weyl mass. Since H is a subgroup of K, a K-invariant
mass cannot evade this H obstruction. This is a LOWER BOUND, not a
determination of all K-invariant masses or a complete protected52 claim.

In contrast, the two(1,2,1) copies admit the symmetric full-rank bilinear
epsilon_flavour tensor epsilon_weak. A single pseudoreal Weyl doublet
is not ruled out by its Hermitian conjugate, though an isolated odd weak
doublet fails the usual mod-two anomaly test. Our FORM roster has28 weak
doublets counting colour and family multiplicities, hence even. Cubic
complex-charge traces cancel because the complete roster is self-conjugate.
This does not certify the global form of K, all global anomalies, the
companion sector or a quantum UV completion.

## Supplied interacting control and unearned physics

A four-dimensional N=1 EFT can be specified for the full K gauge field
and all111 form chiral coefficients with the positive L2 Kähler Gram,
covariant gauge kinetic term and W=0. It has positive kinetic terms,
nonzero charged gauge vertices and a stationary origin with D=F=0.
For example the family adjoint generator acts nontrivially on R above;
this interaction is not removed to preserve a cohomology count. This
EFT is supplied as a control, NOT a proof that retaining these modes is
a consistent full KK truncation, nor a derivation of W=0 or a complete
curved (1,1) nonabelian supersymmetric action. Products of harmonic
profiles need not stay harmonic, so massive modes cannot be dismissed.

The R-symmetry twist, physical dimensional interpretation, compact E8,
metric and action/coupling choices remain explicit inputs. No actual
SM hypercharge normalization, Yukawa texture, vacuum selection, family
count, gravity, observer or qualia law is derived. The kinetic positive
and protected pseudoreal sector are opportunities, not a complete TOE.
