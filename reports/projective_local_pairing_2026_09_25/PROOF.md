# F16: an explicit convergent local argument

This proof is authored, not an independent specialist review. Its finite
hypotheses are certified by the accompanying exact computation. It is
not an assertion that a finite jet calculation proves convergence.

## 1. Statement and domain of the result

Let rho0=(M,N) be any one of the four exceptional points of F15, with
its symmetric invertible F14 matrix J. There is a neighborhood U of
rho0 in X=SL(4,C)^2 such that EVERY representation A=(A_m,A_n) in U
of Gamma=<m,n | r=mnMNmNMnmN> admits a symmetric invertible J_A with

    A_m^T J_A=J_A A_m,    A_n^T J_A=J_A A_n.                 (1)

J_A can be chosen analytically on the representation locus by
restriction of an analytic construction in the ambient U, and J_rho0=J.
Consequently A is equivalent to its theta-pulled contragredient, where
theta(m)=m^-1 and theta(n)=n^-1. Fixed central fourth-root twists also
obey the result. This is an existential LOCAL neighborhood statement,
with no claimed explicit radius or global connected-component scope.

## 2. The actual group operation

Flipping every letter's case defines an involution of the free group.
Free reduction gives theta(r)=n^-1 r^-1 n. Hence it preserves the normal
closure of r in both directions, so induces an automorphism of Gamma.
This proves descent for every representation, not just the faithful
Riley one or a sampled matrix family.

On the ambient pair space set F(A)_g=J^-1 A_g^T J. Since J^T=J,
F^2=id and F(rho0)=rho0. On representations this equals

    F(A)(w)=J^-1 A(theta(w))^-T J.                          (2)

Inverse-transpose is a group homomorphism; it must not be confused
with transpose alone. Thus F preserves the full representation locus.

For a gauge change A_g=h^-1 S_g h, define sigma(h)=J^-1 h^-T J.
Then F(A)=sigma(h)^-1 F(S) sigma(h). This is the exact equivariance,
not ordinary equivariance with an unchanged gauge element. Its gauge
Lie algebra action is S0(X)=-J^-1 X^T J.

## 3. An explicit analytic chart, with no linearization black box

Use left logarithmic coordinates u=(u_m,u_n) in V=sl4^2:

    Psi(u)_g=exp(u_g) rho0_g.

Near u=0 this is a holomorphic coordinate chart, inverse
u_g=log(A_g rho0_g^-1), with the matrix logarithm branch near identity.
All logarithms are tracefree: det=1 and the trace is continuous and
zero at identity. Let C(X)=J^-1 X^T J and T(u)_g=Ad(rho0_g)C(u_g).
Using transpose's reversed multiplication order gives the EXACT identity

    F(Psi(u))_g
      =rho0_g exp(C(u_g))
      =exp(Ad(rho0_g)C(u_g)) rho0_g
      =Psi(Tu)_g.                                        (3)

Thus this chart already linearizes F to all orders. The exponential
is convergent; (3) is not inferred from a finite expansion. T^2=I and
T B=B S0 are also certified by F15/F16, where

    B X=(Ad(M)X-X, Ad(N)X-X).

## 4. Remove conjugation by a finite-dimensional coordinate map

The checked B has rank 15. Write V=im B direct-sum W, choosing W
T-invariant by taking complements separately in V_+ and V_-. Exact
certificates give dim W_+=12 and dim W_-=3. W has dimension 15.

Define the ambient analytic map

    Phi(X,w)_g=exp(-X) Psi(w)_g exp(X),
    X in sl4, w in W.

Its derivative at (0,0), in left logarithmic coordinates, is B X+w.
The exhibited 30x30 matrix [B,W_+,W_-] has nonzero determinant.
The ordinary holomorphic inverse function theorem therefore makes Phi
a local biholomorphism after shrinking its domain. It supplies unique
small X(A),w(A) for EVERY ambient pair A near rho0. This does NOT
assert a global quotient, a proper gauge action, or a global slice.

If A is a representation, so is Psi(w(A)), because it is conjugate to A.
Thus it remains to understand the invariant analytic subset

    Y={w in W : Psi(w)(r)=I}.

By (2)--(3), w in Y implies Tw in Y. Restrict domains symmetrically
under the finite involution when necessary.

## 5. The odd variables vanish on every actual nearby solution

Define the analytic residual f(w)=coordinates(log(Psi(w)(r))) in sl4.
It vanishes exactly on Y locally, and its derivative at zero is R|W,
where R is the independently checked relator differential of F15.

Write w=(e,o) in W_+ direct-sum W_-, dimensions 12 and 3. The checked
15x3 matrix R W_- has rank three. Select the three residual components
whose 3x3 derivative minor is explicitly nonzero. Denote those components
by f0(e,o). The implicit function theorem gives a UNIQUE small solution

    f0(e,o)=0  iff  o=eta(e).                              (4)

We do not assert that solving these three equations solves the remaining
relator equations. Rather, take ANY w=(e,o) that solves ALL of them.
Then w and Tw=(e,-o) both belong to Y, so both solve f0=0. By uniqueness
in (4), o=eta(e)=-o, hence o=0. Therefore

    Y is contained in W_+; F(Psi(w))=Psi(w) for every w in Y. (5)

This reasoning does not assume that Y is smooth, that its tangent
directions integrate, or that it has dimension three. The residual
even equations can still be singular or obstructed. It establishes
the symmetry of every actual solution that exists nearby.

## 6. Recover the actual variable intertwiner

For a nearby representation A, write g=exp X(A) and S=Psi(w(A)), so
A=g^-1 S g. By (5), S_g^T J=J S_g for each group generator. Set

    J_A=g^T J g.                                         (6)

Direct substitution proves (1). This J_A is symmetric, analytic and
invertible, with det J_A=det J because det g=1. A constant nonzero
fourth-root rescaling may normalize its determinant to one if needed.
Equation (2), equivalently

    A(w)^-T J_A=J_A A(theta(w)),                           (7)

then holds for every word, since BOTH sides define the corresponding
representation intertwining condition. Equation (1) does NOT mean
A(w)^T J_A=J_A A(w) for every word; that would falsely force commuting
matrices. For products, transpose reverses the word.

For a fixed scalar character chi with chi^4=1, theta changes chi to
chi^-1, just as dualization does. The same (7) holds for chi A. All
these statements are complex analytic. The construction can also be
restricted to real nearby pairs by choosing the real invariant
complements supplied by the exact real base matrices; uniqueness in
the implicit solves respects complex conjugation.

## 7. Physical interpretation is conditional on a different gate

This upgrades F15's tangent fact to a genuine local representation
pairing. It excludes an algebraic geometric-duality escape by ANY
sufficiently small flat SL4 deformation at these points, including
ones whose first nonzero change appears at higher order. It does not
exclude other components, large deformations, covers/additional
characters, changed topology or nonflat/source-coupled backgrounds.

J_A is a BILINEAR intertwiner, not a positive harmonic metric. F14's
unitary completed-operator conclusion also needed compatible cusp
reference norms and F13 uniqueness in the same bounded-distance class.
Those analytic end hypotheses were earned for the original backgrounds,
not arbitrary nearby representations. If they hold for a proposed new
background, the same uniqueness argument upgrades (7) to its physical
unitary pairing. This conditional sentence is not proof that they do
hold throughout U. Asymmetric allowed end/source data or a spontaneously
asymmetric interacting state remain different possible mechanisms.

F15's two-dimensional first-order matter-retention kernel is neither
integrated nor removed by this proof. Any actual local family it may
produce necessarily has (7), but it still owes existence, admissible
end behavior and normalizable modes. No physical quantum chirality,
empirical value or TOE completion follows.

## Literature placement, not an imported proof

Local equivariant normal forms are established machinery. The selected
[Diez--Rudolph section 4.1](https://link.springer.com/article/10.1007/s10455-021-09777-2)
discusses separating a group action from an invariant local model and
states properness/linearization hypotheses. We do not invoke its full
theorem for this noncompact complex action: (3), the checked derivative
of Phi, and (4) give the required narrower finite-dimensional argument
directly. This is an application, not a claim of a new general theorem.
