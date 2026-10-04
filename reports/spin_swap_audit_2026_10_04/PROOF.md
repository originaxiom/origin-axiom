# Normalization and spin torsor checks

This is an authored elementary argument and a bounded application of a
published formula, not an independently reviewed physical derivation.

## Two conjugations and two questions

For a rational function F define coefficient conjugation by
F#(t)=overline(F(overline(t))). At |z|=1, numerical conjugation obeys
overline(F(z))=F#(z^-1), not generally F#(z).
For reciprocal representatives T_s(t^-1)=T_s(t), and a correctly transported
spin partner satisfying T_tau(s)=T_s#, the proposed expression

    D_s(z) = T_s(z) - overline(T_tau(s)(z))

vanishes identically on the unit circle. Nevertheless

    A_s(z) = (T_s(z) - T_tau(s)(z))/(2i)

can be nonzero and changes sign under the spin exchange. D asks whether
equivariance holds; A asks whether the two labeled sectors differ. A is
only usable after compatible representatives and parameter transport are
specified. If a mirror reverses phi, its pullback also acts by t -> t^-1;
the distinction must be carried before making use of reciprocity.

For unrefined representatives F_s=t^k T_s and F_tau(s)=t^k T_tau(s),

    F_s(z)-overline(F_tau(s)(z)) = (z^k-z^-k) T_s(z).

Thus an allowed common unit can make a symmetry-compatible pair fail this
raw test. k=2 suffices, including when the allowed units form only the even
power subgroup. This does not say that a refined torsion cannot be defined;
it says the refinement and its transport must be part of the test.

The L246 kill criterion, as written at the pinned main commit, is unsafe:
a zero of D does not refute a nonzero A. A nonzero unrefined D need not be
new content either. We do not assert that all actual family members have
reciprocal representatives with exactly this transport; that is one of the
hypotheses to check, not a universal negative.

## An explicit published representation family

Dunfield–Friedl–Jackson section 8.1 describes m003 with relator
bab^3aba^-2 and matrices

    A = [[u,1],[-1,0]],  B = [[0,v],[-1/v,1-u^2]],
    u = v/(v^2+1).

Their normalized torsion is T_u=t+2(u^2-1)/u+t^-1.
Our producer checks the group relation and derives the determinant from
Fox derivatives over Q(v,t). The sign character on a exchanges u and -u
at the character level. Both matrices satisfy the same relator, and the
two corresponding normalized polynomials have opposite constant terms.

At the declared point u=(1+i sqrt(3))/2, the constant terms are
plus/minus 2i sqrt(3). The resulting nonzero spin contrast coexists with
the zero D above. On the unit circle the two scalar torsions have equal
absolute value and neither vanishes. This is not a particle count: the
paper's normalization, the character and the spin pairing must be mapped
to the actual physical model before giving them a physical meaning.

Primary source and normalization scope:
https://arxiv.org/html/1108.3045v3#S8.SS1 and section 2.6.
No claim of discovery of this formula or independent identification of
the complete hyperbolic character is made.

## A moved spin structure is not always a fixed point obstruction

Write a spin torsor using an origin as V=H^1(M;F2). A geometric action has
the affine form

    f(x)=A x+delta.

There is a fixed point exactly when delta belongs to image(I-A). Changing
origin to b changes delta to delta+(A-I)b, so its class in coker(I-A)
is independent of the chosen origin. A nonzero delta at one origin is
not the invariant obstruction when A is nontrivial.

Example: A swaps two coordinates and delta=(1,1). Then f(0)=(1,1),
but (1,0) and (0,1) are fixed. A pure nonzero translation with A=I has no
fixed point. When dim V=1, A=I is forced, so the distinction disappears;
this is the setting of B279's two-spin-structure argument, not every
family member. The frozen B1471 table has four sign lifts for s955 and
s957 and eight for s960. Its multiple torsion matches cannot replace the
full affine action or a simultaneous fixed-point test for several mirrors.

For multiple reversing maps, solve all (I-A_j)x=delta_j simultaneously.
Individual existence of fixed points need not give a common one. Conversely,
an orientation-reversing map need not be an involution; no order-two
restriction is imposed in the finite comparator enumeration.

None of these statements establishes that any actual SWAP label is false.
They specify the additional mathematical question needed to interpret it.
