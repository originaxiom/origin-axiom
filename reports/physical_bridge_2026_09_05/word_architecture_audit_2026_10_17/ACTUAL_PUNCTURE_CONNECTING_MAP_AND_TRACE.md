# The actual connecting map: solution traces are not a boundary condition

October 19, 2026. Authored analytical calculation, pending independent
review. No mathematical producer, test or numerical experiment was run.
This uses one FIXED marked elliptic fibre, the existing rank-six flat
coefficient, odd extending spin and specified finite-distance operator.
It is neither an index for the complete cusp nor a physical SM count.

## Source recovery and hypotheses

Read directly in this continuation:

- The [finite-distance Fredholm proof](../surface_odd_form_2026_10_14/upstream_puncture_fredholm_PROOF.md),
  including its actual Green quotient, compact extension lattices,
  kernel/cokernel correspondence and extreme-domain multiplicities.
- The [earlier puncture proof](../weave_puncture_operator_2026_10_08/PROOF.md),
  [form parent](../weave_form_parent_2026_10_08/PROOF.md) and
  [complete companion roster](../weave_companion_roster_2026_10_08/PROOF.md).
- The [exterior response](EXTERIOR_RESPONSE_AND_JOINING.md) and the
  [joint theta-root action](JOINT_ROOT_ACTION_AND_AUTOMORPHY.md).
- B1642's complete residue producer, read without importing or executing
  it. Its theta bilinear/residue work is prior art, not recomputed here.
  The literal raw skew tensor is not promoted to a physical Yukawa.

The read-only already-banked query used `principal parts connecting
residue theta puncture`. Its broad hits include B1195/B1248; their
findings concern different couplings/norm classes, not the map below.
The targeted source-body search found the existing sheaf sequence and
its duality argument; these are reused. No whole-repository absence or
first-discovery claim follows from that search.

For the duality input the primary [Stacks Project 53.4](https://stacks.math.columbia.edu/tag/0E31)
was read, especially Lemma 53.4.1 and Remark 53.4.3: on a smooth proper
curve H1(V) is dual to H0(V* tensor K). Its general duality theorem is
used here; the explicit residue calculation is supplied below rather
than attributed to that section's wording.

Let E=C/(Z+tau Z), p=0, and X=E-p. Use a constant unitary intertwiner
to write the source's three equivalent parity/quaternion blocks as
W=C3 tensor rho, rho(a)=i, rho(b)=j. Its puncture holonomy is -I6.
This is a declared common FLAT coefficient frame, not an identification
with every local move-module frame. Transport of that intertwiner,
physical metric and all field types remains mandatory.

Let E0 have local frame z^(1/2)e and E6=E0(p) have frame z^(-1/2)e.
The extending odd elliptic spin line S is holomorphically trivial;
fix its sqrt(dz) trivialization for the ordinary-spin comparison.
The finite-distance operator uses the earlier smooth metric and scalar
parallel coefficient norm. These hypotheses are supplied, not derived.
The earlier Fredholm proof is an authored application of a cone-domain
theorem, still awaiting independent specialist acceptance. Its analytic
hypotheses are retained here; this continuation is not a new numerical
or independent global-PDE certification of that application.

## The cover derives different lattices for different field types

On the actual Q8 cover use z=u^2 near a ramification point. Its local
inertia C sends u to -u and acts as -I in rho. An equivariant regular
function f_up obeys f_up(-u)=-f_up(u). It is therefore
u h(u^2), giving downstairs coefficient z^(1/2)h(z): the E0 lattice.

For an equivariant one-form alpha=t(u)du, the condition C*alpha=-alpha
instead says t(-u)=t(u). Thus

    alpha=h(u^2)du=(1/2)z^(-1/2)h(z)dz.         (1)

Regular one-forms give E6 tensor K_E, not E0 tensor K_E. These local
identifications glue: they are the rho-equivariant pushforwards of
O_Y and K_Y, respectively. The unramified charts carry the original
flat coefficient and all four branch lifts have the same inertia law.
They do not introduce a new finite projector in the complete form problem.

Ordinary spin cannot be substituted for (1). Away from ramification,
f(z)sqrt(dz) becomes f(u^2)sqrt(2u)sqrt(du); for f~z^(-1/2) its
coefficient behaves as u^(-1/2), not a regular spin coefficient.
The square root of 2u itself has a branch. Equivalently
K_Y=pi* K_E tensor O(R), with R the four-point ramification divisor;
pi* S has degree zero and is not already a spin line of degree two
on this genus-three Y. A spin/R/Spin-c lift can change the problem,
but must be exhibited. This is not a no-go for the existing twisted
form parent or other admissible spin constructions.

Thus 'regular upstairs' is not an untyped universal boundary law.
Once the field type is given, however, these two lattices are derived
from the stated cover, not six separately adjustable local choices.

## Actual principal-parts cohomology

The determinant calculation in the source gives deg E0=-3. Each block
has its preserved complex symplectic epsilon, so E6 is isomorphic to
E0* after that flat identification: the inverse local power is precisely
the dual lattice. Hence deg E6=3. The actual sheaf sequence is

    0 -> E0 -> E6 -> C_p^6 -> 0.                (2)

In particular the quotient length is SIX. It is not the number of
global theta modes. H0(E0)=0: in a unitary flat gauge the squared norm
of such a section is subharmonic, tends to zero at p, and extends across
p. Compactness forces it to vanish. The same applies to the dual flat
coefficient's lower lattice. Serre duality gives H1(E6)=0; genus-one
Riemann--Roch then gives h0(E6)=3 and h1(E0)=3.

These recover the source's extreme multiplicities. The long exact
sequence of (2) becomes the ACTUAL principal-parts sequence

    0 -> H0(E6) --tr--> C6 --delta--> H1(E0) -> 0,
              dim3       dim6          dim3.    (3)

This is distinct from the abstract pointwise Koszul sequence in the
previous checkpoint. Its middle is a puncture quotient, not a freely
identified bulk bundle over the whole modular surface.

## Derive the connecting map from the existing profiles

Use the actual common doublet

    F=(i theta_2(z|2tau),theta_3(z|2tau))^T/sqrt(theta_1(z|tau)),
    v=(i theta_2(0|2tau),theta_3(0|2tau))^T,
    d=partial_z theta_1(0|tau), b=v/sqrt(d).

The previously retained branch/normal calculation gives
F=z^(-1/2)b+O(z^(3/2)), with b!=0. Its three separate-copy sections
F_p=e_p tensor F are independent in H0(E6), hence a basis by (3).
Their trace is

    tr(x)=x tensor b.                          (4)

Their symplectic dual one-forms eta_p=e_p* tensor (F^T epsilon)dz
form a basis of H0(E0* tensor K_E). Here epsilon=[[0,1],[-1,0]];
it is a complex bilinear duality, not a Hermitian conjugation.

For u=(u_p) in C6, lift its principal part by a cutoff times
z^(-1/2)u. Applying bar-partial gives a representative of delta(u)
in H1(E0). Pair it with eta_p and integrate by parts across the cutoff
annulus. With the contour orientation and Serre trace normalized by
(2pi i)^-1, the result is the residue at zero of

    (z^(-1/2)b^T epsilon+O(z^(3/2)))
                         (z^(-1/2)u_p) dz.

Therefore, in the Serre-dual target basis,

    delta(u)_p=b^T epsilon u_p.                 (5)

Changing the common nonzero Serre normalization changes no kernel or
rank. Equation (5) derives the actual connecting map, rather than infer
one from matching dimensions. It has rank three because b!=0 and
epsilon is nondegenerate. Its kernel is exactly

    U=im tr=C3 tensor span(b).                 (6)

Equations (4)-(6) explain why the earlier theta-constant rank-three maps
appeared. Here their meaning is earned at this FIXED fibre, with the
derivative factor retained: U is the space of principal parts of actual
global zero solutions. It is not yet a chosen selfadjoint domain.

This does not assert that the target H1(E0), the principal-part fibre
and the previous full-E line-weighted modules have already been globally
identified. Such a family comparison must retain transported puncture
lifts, the normal half-order frame, d, the Serre pairing and all
automorphy factors. Resetting the puncture lift to zero would forget
the registering action that the preceding proof recovered.

## Both finite-distance kernels for an actual Lambda

Reuse the source's authored closed-domain correspondence for a specified
grading-invariant selfadjoint finite-distance extension with plus trace
Lambda and minus trace Lambda_perp. Its Green pairing is
u dagger v'+v dagger u'. Put d_L=dim Lambda and

    r_L=rank(delta restricted to Lambda).

H0(E0)=0 makes the positive trace injective, so its kernel dimension is
dim(U intersect Lambda)=d_L-r_L. The source's Fredholm theorem and index
d_L-3 therefore give the other dimension as well:

    dim ker D_Lambda^+       =d_L-r_L,
    dim ker (D_Lambda^+)^*   =3-r_L.            (7)

There is a direct Green/duality control. The three negative zero traces
span C3 tensor span(epsilon^T conjugate(b))=U_perp. Their intersection
with Lambda_perp has dimension 6-dim(U+Lambda)=3-d_L+dim(U intersect
Lambda), agreeing with (7). This checks the adjoint traces instead of
declaring every negative coefficient an independent extra field.

| Supplied plus domain | d_L | r_L | positive, adjoint kernel dimensions |
|---|---:|---:|---|
| 0 | 0 | 0 | 0,3 |
| C6 | 6 | 3 | 3,0 |
| U, the actual positive solution-trace space | 3 | 0 | 3,3 |
| U_perp in the stated unitary frame | 3 | 3 | 0,0 |

These follow symbolically from (5)-(7), not a new numerical sample.
They are mode dimensions in this specified operator, not SM generations.
In particular choosing the theta IMAGE as the boundary condition would
give a paired kernel, not the upper extreme's chiral index. Three
positive modes with zero adjoint kernel require d_L=6 in THIS model.
The distinction between a three-dimensional Cauchy image and six allowed
critical coefficients cannot be dropped.

For a domain spanned by columns of an actual 6-by-d_L matrix Z, (7)
reduces the remaining zero-mode calculation to rank(delta Z). Rank
changes are the vanishing loci of its minors, not generic-sample counts.
The matrix Z must come from the admitted physical domain or exterior
response; selecting it to obtain an index is still a supplied choice.
Nothing here computes the different silver-cover connecting map.

## How this changes the physical next step

The mathematical interior now supplies more than an Euler number: it
supplies its actual zero-energy trace U and an explicit obstruction map
delta for extending puncture data. A proposed exterior/end response can
be compared against those, with its full Green pairing and kernel data
retained as required by the existing exterior-response analysis.

This does not remove the complete-cusp ordinary-spin continuum or make
that operator Fredholm. Its different norm rejects the same half-pole;
the finite-distance theorem cannot be transferred to it. The supplied
twisted form parent retains its positive modes, but its full roster and
ordinary-spin companion continuum remain as established in the source.
Regularity of one form alone cannot delete those interacting companions.

The remaining task is the SAME physical action's generated end/geometry,
field-type/twist assignment and exterior response, followed by its full
stationary charged spectrum, interactions and anomalies. This note
removes an arbitrary interior trace-map ansatz in the specified fibre;
it does not derive Lambda, four-dimensional spacetime, a Standard Model
dictionary, normalized parameters, gravity, observer or qualia.
Independent proof review and prospective runtime controls remain owed.
No complete input row, publication certificate or goal completion is
claimed; the existing historical and staged evidence is unchanged.
