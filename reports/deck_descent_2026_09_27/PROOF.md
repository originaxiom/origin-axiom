# Holonomy, deck action and the one-versus-three comparison

Authored analytic check, 2026-09-27. Standard mathematics, no literature
novelty claim, no independent specialist review. Finite controls are
specified separately and their outcome is not presumed here.

## 1. The total-space action

Let p:Y->X be a regular three-sheeted covering and E a flat vector bundle
on X. In the pullback definition,

    p*E = {(y,e): p(y)=pi_E(e)},

the generator delta of Deck(p) acts by D(y,e)=(delta(y),e). Consequently
D^3=Id, without any assumption that the monodromy of E is semisimple.
It preserves the pulled-back flat connection. A metric pulled back from E
is also preserved, whether or not it solves a harmonic-metric equation.
This does not assert existence of a physically admissible harmonic metric.

Equivalently let H normal in Gamma have index three, t generate Gamma/H,
and rho:Gamma->GL(W). With the convention

    E_Y = (X_tilde x W)/H,
    h.(x,w) = (h x, rho(h) w),

the lift is D_t[x,w]=[t x,rho(t)w]. It is well defined since tHt^-1=H.
Its cube is [t^3 x,rho(t^3)w]=[x,w], because t^3 belongs to H. In contrast,
the matrix T=rho(t) acts in the chosen model fibre W and satisfies
T^3=rho(t^3), not necessarily Id. The two identities are compatible.

No splitting Gamma = H semidirect C3 is assumed or needed. No root of
rho(t^3), change of its Jordan form or semisimplification has been used.

## 2. Application at exactly the scope supported by B1384

Take X=M2, Y=M6, H=Gamma6, Gamma=Gamma2, t=a^2 and
E corresponding to Ind_H^Gamma V. B1384's implementation uses precisely
T=(Ind V)(a^2), so its T^3=(Ind V)(a^6) is a HOLONOMY statement. The
pulled-back rank-six bundle p*E has the strict geometric action in section 1.
By the recorded Mackey decomposition it is the orbit sum of the rank-two
seed and its two deck transforms. The construction preserves nonsplitting.

Thus the quoted nontrivial cube is not, by itself, an obstruction to a
strict geometric C3 action on the orbit sum. A strict action on one model
fibre, an action on the total bundle, and an internal symmetry of a
four-dimensional physical theory are different requests. This clarification
neither retracts the recorded cube nor establishes the last request.

It also has nothing to do with filling M6 to the CLOSED Y6. Extension over
a filled meridian requires that meridian's holonomy to become trivial.
Our construction leaves that holonomy nontrivial and does not evade B1379's
filling obstruction. The two uses of “descent” must not be confused.

## 3. What counting on the quotient actually means

Over characteristic zero, averaging 1,D,D^2 projects the full pulled-back
de Rham complex onto invariant forms, naturally identified with forms on
X with coefficients E. It commutes with the differential. Exactness of
finite-group averaging gives the corresponding invariant cohomology
statement; the same construction applies to a preserved boundary pair.

With pulled-back positive base/bundle metrics, the L2 norm squared of a
pulled-back form is three times its downstairs norm squared. The rescaled
pullback is unitary onto the invariant subspace. Promoting this to a
physical spectral statement requires the actual action, constraints and
operator domains to be the compatible ones. A different metric, source,
boundary condition or non-invariant state must be checked separately.

Keep three objects apart:

    (M6,V), rank 2;
    (M2,p_*V), rank 6;
    (M6,p*p_*V), rank 6, three deck-related summands.

Shapiro compares the FIRST TWO cohomologies. Pullback then produces the
THIRD, not a passive relabeling of the first. Accepting the recorded seed
I=-1, the recorded whole-orbit I=-3 and downstairs I=-1 are compatible.
Counting all cover modes and counting deck-invariant modes are different
prescriptions. This is not proof that three physical families are either
present or impossible. No M6 numerical index is independently rerun here.

## 4. Why the finite comparator is decisive about the conflation only

For the companion T in DESIGN, model the covering circle as x modulo 3
with (x,w) identified with (x+3,T^3 w). The global action is
[x,w] -> [x+1,Tw]. On representatives x=0,1,2 the last step requires
the seam identification T^-3, hence the blocks T,T,T^-2. Omitting that
identification deliberately replaces the geometric action with three
parallel-transport factors; its cube keeps T^3.

For c nonzero, M-I has rank one, so T^3-I has rank three. Solving T w=w
identifies the three rank-two components and requires Mv=v; its kernel
has dimension one. These give the predicted cover/base H0 dimensions
three/one. On ker(T^3-I), T^3=Id even though this fails on the entire model
fibre. Circle H1 is the cokernel of the same square matrix and has the
same dimension. This comparator has no chiral index and no claim to be M6.

## 5. Unpaid physics

This supplies a well-defined mathematical deck action on a particular
pullback, not a selected physical quotient or a gaugeable quantum symmetry.
It proves no anomaly cancellation, positive physical light spectrum,
harmonic-background existence, generation selection or spacetime dynamics.
It removes only an incorrect inference from T^3!=Id to “no geometric C3
without destroying the nonsplit extension.” The broader mission still
requires the common-model contract in the accompanying assessment.
