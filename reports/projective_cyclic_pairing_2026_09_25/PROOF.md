# F18 authored all-degree cyclic-pairing argument

This is a pre-execution proof with explicit finite certificate duties.
Analytic inputs are the previously authored F12--F14/F17 constructions,
not independent specialist acceptance or an experimentally selected theory.

## 1. Earn the marking directly from the relator

Gamma=<m,n | mnMNmNMnmN>. Put t=m, x=nM, y=m n MM=t x t^-1.
Substitute n=x t in the original relator and freely reduce. It becomes

    t x T X X T x t X = y X^2 T x t X.

Here uppercase is inverse. Adjoin the defining generator y=t x T,
conjugate the remaining relator by t, and substitute that definition.
The remaining relation is

    (t y T) Y^2 x Y=1,  equivalently t y T=y X y^2.

These reversible Tietze moves give

    Gamma = F(x,y) semidirect_beta Z,
    beta(x)=y, beta(y)=y X y^2.

It is an automorphism, not an ascending endomorphism: the inverse is
beta^-1(x)=x^2 Y x, beta^-1(y)=x. Both composites freely reduce to the
identity on x,y. Thus H_d=F(x,y) semidirect_beta^d <t^d> for every d>=1.
This earns the actual marking before invoking a monodromy matrix.

On fiber exponent columns beta acts by B=[[0,-1],[1,3]]. On character
columns a=(a_x,a_y), pullback acts by A=B^T=[[0,1],[-1,3]]. This is the
same companion polynomial t^2-3t+1 already banked in B326. The integral
change P=[[1,2],[0,1]] obeys [[2,1],[1,1]] P=P B, det P=1, connecting
the marking to B350's monodromy without identifying unrelated bundles.

## 2. All characters, including the nonextendable free part

A mu4 character of H_d is uniquely specified by

    chi(t^d)=i^c, chi(x)=i^a_x, chi(y)=i^a_y,
    c in Z/4, a in (Z/4)^2, A^d a=a.

This follows immediately from the semidirect presentation; there are
no other relations on the free fiber's abelianized character. Exact
identities give A^3=I mod 4 and det(A-I)=-1, det(A^2-I)=-5, both units
modulo four. Therefore:

    3 does not divide d: a=0, four characters;
    3 divides d: any a, sixty-four characters.

This is a theorem for all positive integers d, not an extrapolated list.
When d is divisible by four, some c cannot be restrictions of base mu4
characters. They must not be omitted. Define on H_d alone

    alpha_c(w)=i^(c exponent(w)/d).

The quotient is integral there; this is a well-defined scalar mu4
character, and every exponent-reversing automorphism inverts alpha_c.
We never require alpha_c to define an SL4 scalar twist on the base.

If 3|d, any fiber character a extends to a character tau of H_3 by
tau(t^3)=1, since A^3 a=a. Then on H_d,

    chi=alpha_c times (tau restricted to H_d).

This factorization handles ALL free phases even when d/3 is even.
If 3 does not divide d, chi=alpha_c alone.

## 3. A finite certificate supplies every needed inversion

Theta inverts m,n, T swaps them. Both theta and thetaT reverse the
meridian exponent and are orientation-preserving base isometries (F14's
exact normalizer/power certificates). They preserve every H_d.
Their actions on fiber character columns, derived from the marked words,
are respectively

    C=[[-3,1],[-8,3]],  -C.

For example theta(x)=beta^-1(X), theta(y)=beta^-2(X), and T has fiber
abelian action -I. Deck conjugation Ad(m^j) composed AFTER either
inversion acts on characters as C A^j or -C A^j. Order matters.
The producer derives these matrices from words, not just these formulas.

For EVERY a in (Z/4)^2, one of the six matrices with j=0,1,2 sends a
to -a. This is the complete 16-element finite certificate; the witness
for each a is retained. Such an inversion also inverts tau on t^3:
theta sends it to t^-3, while thetaT sends it to n^-3. In the abelian
fiber normal form n^3 has vector (I+B+B^2)e_x, which is zero mod 4
because I+B+B^2=0 mod 4. Deck conjugation does not change that zero.
Thus tau composed with the chosen inversion equals tau^-1 on H_3,
not merely on its fiber subgroup.

For 3|d, restrict this equality to H_d and combine with alpha_c:

    chi composed with phi = chi^-1,
    phi = Ad(m^j) theta or Ad(m^j) thetaT.

For 3 not dividing d, theta alone does the job. All selected j are
available cover lifts (j<=2 and d>=3 in the nontrivial fiber case).
Every phi is a genuine cover isometry. No assertion about completeness
of this isometry list is required to exhibit a positive witness.

The prime-19 control demonstrates why the modulus matters. It checks
an eigenline of A^9 for which none of these inversion/deck candidates
inverts a. It is NOT an SL4 scalar character: a scalar zeta_19 has
determinant zeta_19^4 !=1. Nor does candidate failure exclude extra
pairings. We do not promote it to a successful physical escape.

## 4. Actual SL4 bundles and restriction irreducibility

At the four exceptional real q points, F17 recomputes nonsingular
base matrices J_sigma satisfying rho(h)^-T J_sigma=J_sigma rho(sigma h)
for theta and thetaT. For phi=Ad(m^j) sigma set J_phi=J_sigma rho(m)^-j.
The untwisted equation then holds for every h. Multiplying by the
scalar character preserves it exactly because chi(phi h)=chi(h)^-1.
This proves a complex-linear flat-bundle isomorphism for every d,
not just equality of characters, dimensions or traces.

For any unipotent 4x4 matrix U and any positive integer d, let Z=U^d-I.
The exact truncated binomial identity is

    U=I+Z/d+(1-d) Z^2/(2d^2)+(1-d)(1-2d) Z^3/(6d^3).

It follows in Q(d)[X]/X^4 and all denominators are nonzero for d>=1.
H_d contains m^d,n^d. Therefore any subspace invariant under rho(H_d)
is invariant under rho(m),rho(n). F17's full Mat4 word-algebra basis
establishes irreducibility at each exceptional point, hence at EVERY
finite cyclic restriction. Scalar twists do not change it. This is
not the false rule that all finite-index restrictions stay irreducible.

## 5. The actual metric, complete domains and whole parent response

Pull back F12's global harmonic metric to each finite cover; unitary
central twists preserve the same metric equation. These cyclic covers
have one cusp, since the peripheral meridian maps onto Z/d. Its
peripheral group is generated by m^d and the unchanged longitude.
The selected inversion lifts have cusp map (-x+c0,-y+c1,z). F14's
translation-independent reference connection and its unitary duality
matrix obey exactly the same comparison as on the base.

The centralizer of exp(d N) is that of N (finite nilpotent logarithm,
d nonzero). Consequently the bounded reference-frame intertwiner and
inverse estimate is unchanged, with constants allowed to depend on d.
No uniform spectral bound as d tends to infinity is claimed. Normalize
the constant intertwiner determinant to one. Irreducibility from
section 4 and F13's bounded-distance uniqueness identify the actual
pulled-back metric with the transported dual metric.

The resulting unitary map intertwines the complete Hodge complexes and
their closed domains. F11's cusp contraction persists on each finite
cover. Where harmonic modes exist, the same confinement/regularity
argument supplies the product domain used in F13. F14's determinant
volume tensor and parent Weyl lift then pair the full corresponding
classical vertex and scalar-response norms. This is a stronger symmetry
statement than equal zero-mode counts, which F11 already provided.

No all-degree H1 multiplicity, actual nonzero coupling, SM breaking,
quantum state, chiral phase, Lorentzian parity action, scale selection
or gravity is calculated here. The theorem concerns these pulled-back
exceptional SL4 backgrounds and central mu4 characters on cyclic covers.
Noncyclic covers, noncentral data, other holonomies/end laws and quantum
phases are not excluded. The other seat's canonical base metric is
not substituted for the fixed hyperbolic metric in this argument.
