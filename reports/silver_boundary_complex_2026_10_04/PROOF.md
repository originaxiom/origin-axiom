# Boundary completion and the retained degrees

This is an authored cochain argument, to be checked by the sealed exact
producer. It does not define an elliptic physical operator or prove that
either chosen completion is selected by Origin Axiom.

## The full restriction map

Let r_g=t g T phi(g)^-1 for g=a,b, p=abAB, q=c t, with
phi(p)=c^-1 p c. Capital letters denote inverse words. The torus relator
[p,q] is c r_p^-1 c^-1, where r_p=t p T phi(p)^-1. Factoring r_p into
conjugates of r_a and r_b gives, after evaluating in a representation,
the two-cell row (T Fox_a(p) T^-1, T Fox_b(p) T^-1). This follows by
successively expanding the letters of p: a positive letter contributes
the transported prefix and an inverse letter its negative next prefix.
The outer inverse and conjugation therefore give

    R2 = -Q (Fox_a(p) T^-1, Fox_b(p) T^-1).

Here T is the stable-letter matrix and Q is the matrix of q. This is the
cellular restriction for the marked boundary torus, not an arbitrary
solution of a linear matrix equation. With global differentials B,F,
boundary differentials D,F_T, and the existing Fox restriction R,

    R B = D,                 R2 F = F_T R.

The producer checks these identities on the full spaces. The boundary
commutator orientation is fixed by F_T=(1-Q,P-1). The relation identity
also fixes the two-cell sign. No rank inferred from duality is used to
construct R2.

## A complete finite cochain model

Choose a graded closed subspace A of the boundary cochains, with inclusion
i and zero differential. In degree one take a complement L to the image
R_H of restriction in H1(T;E), represented by harmonic cocycles in a
supplied positive metric. In other degrees take either

    cone-shaped:       A=(H0(T;E), L, 0),
    reversed endpoint: A=(0, L, H2(T;E)).

H2 representatives are the orthogonal complement to the boundary exact
two-cochains, not the whole cochain space. The first pattern agrees with
the degrees in the untwisted cone formula of ALMP Proposition 7.1; this
is motivation for the comparator, not an application of its analytic
theorem to these coefficients. The second pattern is a separate choice.

For either choice form K^j=C^j(X;E) plus A^j plus C^(j-1)(T;E), with

    d(x,a,z)=(d_X x, 0, R_j x-i_j a-d_T z).

The chain identities and closedness of A prove d squared zero. This is
the homotopy fiber of the restriction-minus-inclusion map. It keeps both
boundary cochains and the attached A cochains; it is not just a condition
on H1(X). Its cohomology follows from the long exact sequence of this
mapping cone. The program instead computes it directly from its matrices
and compares with the sequence predictions.

On the dual coefficient use L_dual=ann(L) for the full boundary cup
pairing. The existing B1509 argument says R_H_dual=ann(R_H), so both L
and L_dual are complements to their respective restriction images. No
independent positive-metric complement is substituted for ann(L).

## Cone-shaped completion

Write a_j=h^j(X;E), t_j=h^j(T;E), and n=dim ker res in degree one.
The H0 boundary map from H0(X) plus A0 onto H0(T) is surjective since
A0=H0(T). Its kernel is H0(X). The H1 map from H1(X) plus L onto
H1(T) is surjective because L complements R_H; its kernel is the
interior kernel of dimension n. Finally A2=0. Hence

    H(K) dimensions = (a0, n, ker_dim res2, coker_dim res2).

The compact-pair long exact sequence and Poincare-Lefschetz duality give
ker_dim res2=n_dual and coker_dim res2=a0_dual. These equalities will be
checked against the explicit degree-two map, not assumed as data.
Thus H1 really can recover the old interior count in a full finite
complex. Omitting A0 but calling the model this cone would add spurious
connecting classes relative to the specified construction.

However the alternating count, with odd minus even convention, is

    J = -a0+n-n_dual+a0_dual = I_interior-(a0-a0_dual).

On the silver W this predicts J=0 despite I_interior=-1; on its exterior
square it predicts J=-1. This is a finite graded count, NOT automatically
the physical chirality. A parent-field dictionary may distinguish these
degrees, but must do so explicitly from its action and reality condition.

## Reversed endpoint completion

Now A0=0, so the cokernel of H0(X)->H0(T) survives as degree-one
connecting classes of dimension t0-a0. In degree one the complement map
is again surjective. A2=H2(T), so the final map is surjective and its
kernel is H2(X). Consequently

    H(K) dimensions = (0, n+t0-a0, a2, 0),    a2=a1-a0.

On the silver inputs t0=t0_dual. The H1 differences therefore predict
(0,-1), distinct from the cone-shaped model's (-1,-1). Both models have
J=dim L-t0 because chi(X;E)=chi(T;E)=0 and t2=t0 on these inputs.
The equality t2=t0 is not asserted for arbitrary nonunitary local systems;
the general torus identity is t2(E)=t0(E_dual).

For both specified patterns the endpoint choices and L/ann(L) are paired
annihilators in complementary boundary degrees. The expected global
dimension pairing is h^j(K_E)=h^(3-j)(K_dual). This will be tested, not
advertised as an explicit constructed nondegenerate global chain pairing.

## What this decides

Different completions of the same H1 rule can give different H1 counts.
The cone-shaped comparator is an opposite control to any claim that
retaining boundary cochains must destroy the interior positive. The
nonzero H0/H3 are an opposite control to identifying that positive with
the total odd/even index. Neither check excludes a physical chiral theory.
The next physical obligation is an operator, domain, parent reality and
same-action end sector explaining which of these classes are fields,
constraints, partners or gauge redundancies. Choosing the grading by the
desired Standard Model answer would not earn that identification.
