# The order-ten crossing restores an actual light cubic

Draft begun November 1; source self-review November 2, 2026.
**UNREVIEWED author hand derivation.** No scientific
producer, CAS, module import, collection or test execution. This is an
analytical successor to the generic-roster note, outside the sixteen
frozen finite controls and every earlier review/acceptance.

## 1. Test the exceptional modes in the same physical action

Reuse [the complete physical kernel](PARALLEL_PHASE_CHIRAL_KERNEL_AND_LIGHT_RUNNING.md),
[the source cubic](QUANTUM_NORMALIZATION_AND_WEIGHTED_GAUGE_MATCHING.md),
[the full flat family](FULL_FLAT_FAMILY_METRIC_AND_DISCONNECTED_CENTRALIZER.md)
and [the exact exceptional set](WILSON_FAMILY_KERNEL_AND_LEVEL_FOUR_REGISTER_MAP.md).
The action, principal background, once-punctured elliptic carrier and
complete graph domain are unchanged. None is selected from genesis here.

Let chi have EXACT order ten on the marked elliptic character torus and
choose the nontrivial extending spin eta=chi^5. This is a compatible
allowed state of the same family, not a state-selection law. In
particular chi^5!=1, so the gauge group is still the source SM group.
The flat line L_(+5)=L_(-5)=eta as unitary characters, although their
gauge charges and representations remain conjugate and distinct.

The source spin S extends as eta on the compact elliptic curve X.
Consequently S tensor L_(+5) and S tensor L_(-5) both have trivial
compact extension. Their exact cusp pole bound is b(1)=0. They each
have a single nonzero holomorphic L2 spin section psi_+,psi_-. Choose
their constant frame factors so that

  psi_+ psi_-=omega,

where omega is a nonzero compact elliptic holomorphic one-form. This
chooses mode frames, not the size of a physical Yukawa. Both factors
are nowhere zero as sections of their compact degree-zero lines.
The product uses S^2=K and L_(+5)L_(-5)=O; it is not a square of a
globally nonexistent untwisted spin section.

At principal j=0, charge +/-5, the actual harmonic slots are therefore

  a_0: absent,
  u_0: one copy in each conjugate (3,2) block,
  v_0: one copy in each conjugate (3,2) block.               (1)

Indeed h1_L2(L_(+/-5))=delta(L_(+/-5))=0 while
h0_L2(S L_(+/-5))=delta(eta L_(+/-5))=1. The unbroken gauge directions
retain a_0 but have no u_0 or v_0 for this nontrivial spin. The
principal singlet v_1 proportional to Q0 is still present.

The full physical chiral dimension is now 128 instead of 104, the
vector dimension is still 12 and the R-field dimension is 13 instead
of 1: twelve charged R modes have been added. Their twelve u partners
account for the other half of the 24 extra chiral dimensions. No mode
is counted as both an R field and a separate independent particle.

## 2. An explicit nonzero integral, with admissible profiles

The actual parent vertex is

  W3(a,u,v)=-i integral kappa(u,[a,v]).                    (2)

The earlier generic nontrivial-spin zero used v=c Q0 and
[Q0,a]=0. Equation (1) invalidates its FIRST premise at this crossing;
it does not refute that proof on its declared generic-roster family.

Inside the faithful gauge SU5, let i be a colour index and alpha a
weak index. Use its literal off-diagonal matrices and its old generator

  QY=diag(-2,-2,-2,3,3).

Choose the physical zero modes

  u=psi_+ E_(alpha i),
  v=psi_- E_(i alpha),
  a=bar(omega) QY.                                       (3)

Here u has charge +5, v charge -5 and a charge zero. They have
principal j=0, commute with the principal background and satisfy the
same full linear F and gauge-slice equations. The antiholomorphic form
bar(omega) is the actual harmonic representative on the trivial line:
the two-dimensional one-form norm is conformally invariant and its
coefficient is antiholomorphic. No arbitrary cohomology representative
has replaced a physical harmonic mode.

The Lie coefficient is

  kappa(E_(alpha i),[QY,E_(i alpha)])
       =-5 kappa(E_(alpha i),E_(i alpha)) != 0.            (4)

The spatial product in (2) is a nonzero constant times

  integral_X omega wedge bar(omega) != 0.                (5)

Positivity of i omega wedge bar(omega), up to orientation convention,
establishes nonvanishing. Removing one point changes neither the integral
nor convergence. The common phase convention of W affects its phase,
not whether it vanishes.

These are admissible nonlinear variations, not just a formal trilinear
on uncontrolled L2 functions. Near the puncture, in a compact coordinate
of radius r, the physical norm of psi_+ or psi_- is comparable to
(r abs(log r))^(1/2); the physical one-form norm of bar(omega) is
comparable to r abs(log r). They tend to zero, are bounded on the
whole carrier and have the old finite kinetic norms. The source's
covariant derivatives and commutator residuals are L2; products of
these bounded modes with their L2 partners stay L2. The cubic integral
is absolutely convergent and uses no cusp boundary subtraction.

Canonical normalization multiplies (2) by the inverse square roots
of their positive finite kinetic norms, with the same common action
coefficient. It cannot turn (4)--(5) into zero. Its actual numerical
size depends on the supplied parent, geometry and normalization;
no independent fitted Yukawa or unit-normalization assumption is added.

## 3. The other charged blocks also have a derived pairing

There is more than an isolated gauge-adjoint example. A charged v_0
in (1) acts on each gauge ten and five by its existing SU5 root action.
It changes charge by +/-5 and commutes with the principal SU2, so
it preserves j. The invariant trace pairs an a_j in a representation
with a u_(-j) in its conjugate. For a permitted nonzero Lie coefficient,
charge conservation is L_a L_u L_v=O.

The spatial multiplication then has its ACTUAL source and target

  M_v: H0_L2(S^(j+1)L_u)
            -> H0_L2(S^(j+2)L_a^(-1)),
       u -> u v_0.                                       (6)

The target is exactly the source kernel's Hermitian-Hodge dual of
H1_L2(S^(-j)L_a), not a guessed compact Euler space. The compact
extension of S L_v is trivial, and v_0 has no zero there. The remaining
issue is the exact cusp pole allowance. It is fixed by the existing
endpoint law b(a), with

  b(j+2)-b(j+1) = 0 for even j,
                  1 for odd j>=1.                        (7)

Thus (6) is an isomorphism of section spaces when j is even. When j
is odd it is the injective inclusion obtained by allowing one further
pole order in the target. Multiplication cannot annihilate a nonzero
holomorphic section. These statements use the actual twists transported
in (6), not an identification of lines with equal degree.

For j=2 in the ten sector, both spaces have dimension one and (6)
has rank one. The SU5 matrix E_(i alpha) acts nontrivially, for example
on e_alpha wedge e_j with j a different colour index. It joins the
charge +1 and -4 components; acting on the two-weak-index wedge also
joins +6 and +1. Choose a_j to be the actual Hodge dual of the nonzero
product u v_0. Its integral with that product is a positive nonzero
norm, times the nonzero Lie coefficient and the fixed common phase.
This proves a nonzero physical cubic in those ten/conjugate-ten blocks.

For the five sector's j=3, the source in (6) has dimension one and
the target dimension two, since b(4)=1 and b(5)=2. It has rank one:
one combination of its two a modes couples to the given u and v_0.
The other combination lies in that pairing's annihilator. The root
action on the defining five is nonzero between its colour and weak
components. In its j=1 companion, u has h0_L2(S^2 L_u)=delta(L_u)=0
at exact order ten for charges +/-2,+/-3; it is therefore absent from
this vertex. The companion is retained in the full spectrum rather
than silently given a nonexistent coupling.

The same endpoint bounds control the profiles used here. If f is the
target section in (6), its pole order is at most b(j+2). Its actual
Hodge-dual a has physical norm bounded by a constant times

  r^((j+2)/2-b(j+2)) abs(log r)^((j+2)/2).

For j=2 and j=3 the powers of r are respectively one and one half.
The u profile has the corresponding bound with j+2 replaced by j+1,
whose powers of r are respectively one half and one. Together with
the decaying v_0 profile these modes are bounded and remain in the
old nonlinear product/variation class. In particular the nonzero
Hodge pairing is not rescued by a divergent overlap or a change of
the physical cusp domain.

Equation (6) is a statement of rank for a specified allowed gauge
channel and specified v_0 profile. It is not the full flavour matrix
after arbitrary expectation values, a fermion mass matrix or a claim
that every generated coupling is nonzero. The source cubic's principal
v_1 still gives zero because it is proportional to Q0.

## 4. What this restores, and what it does not select

This is an explicit same-action counterexample to extending the
generic nontrivial-spin zero-cubic statement across all SM holonomies.
It recovers a genuine light interaction without changing the parent,
supplying a boundary multiplet or inserting a new Yukawa tensor.
The earlier source/trivial-spin nonzero control remains valid too.

The price is precise: chi has exact order ten and eta=chi^5. Those
are allowed compatibility conditions, not derived physical selection.
The extra charged modes are vector-like conjugate blocks, and the
complete spectrum remains nonchiral. The mixed representation is
(3,2) of hypercharge magnitude 5/6; it is not the observed Higgs
doublet. A nonzero expectation value in it changes the SM gauge phase,
including colour. This proof does not propose such a vacuum.

The light beta vector is (10,6,4)+(10,6,4)=(20,12,8). Its contraction
with w=(1/2,-3/2,1) is still zero, while the actual cubic is now
nonzero. Neither that contraction nor the spin bit determines the
whole interacting EFT. The earlier generic two-loop expression with
Y_a=0 cannot be reused at this crossing: the new light roster and its
derived Yukawa contributions must both be included. No two-loop
cancellation is asserted here.

## 5. Verification and reduction accounting

This proof was written after the sixteen-control design and source
inventory at ac28256fc. Test sixteen there checks the exceptional
counts/beta insertion, not the present wavefunction integrals or the
map ranks. A future pass of that package must not be described as
verification of this analytical successor. It needs its own genuine
independent proof review; any new scientific executable also needs
its own prospective design, source closure and admission.

The reused action, complete physical kernel, Hodge map and pole law
retain their original analytical review duties. Independently check
global line identifications, all exact endpoint inequalities, physical
domain/kinetic admission, Lie coefficients and the nonzero pairing.
No scientific producer has been imported, collected or executed.

Before: the family classification located extra light modes but did
not evaluate their interactions. After: a nonzero actual-parent cubic
and the permitted ten/five pairing ranks are derived at that same
crossing. The interpretation is an interacting vector-like allowed
state, not a chiral SM construction or removal of a foundational input.
This preserves a positive route within the full admitted family while
retaining the physical state-selection and SM3/gravity obligations.
