# A normalizable centralizer kernel alongside the threshold continuum

2026-11-07. **UNREVIEWED conditional hand proof.** No scientific
implementation, imports, collection, CAS or tests. Quantifier: the A3
centralizer part of the same coupled quaternion stationary bundle on
the complete once-punctured elliptic curve. The supplied parent, metric,
spin/flavour assignment and old nontrivial order-three Wilson remain.

The earlier [cusp proof](COUPLED_QUATERNION_STATIONARY_BUNDLE_AND_CUSP_LAW.md)
exhibits the centralizer spin continuum reaching zero. It does not decide
its global L2 kernel. The actual A3 block commutes with q,r and their
adjoints, so the source physical mass operator splits there into the
scalar/form pair and the spin/flavour Dolbeault pair, with no Higgs mixing.

## 1. Derive the centralizer spin kernel directly

Let C be the compact elliptic curve, p its puncture. An extending spin
line S is a flat order-two line on C in its holomorphic structure; choose
an auxiliary smooth unitary flat metric on it. This is a comparison metric
for the following maximum principle, not a replacement of the physical
hyperbolic kinetic norm.

In an A3 coefficient, the remaining gauge line L is unitary flat, with
trivial peripheral transport. The physical flavour bundle F is unitary
flat on C minus p with peripheral -I2. A spin zero mode is exactly an
L2 holomorphic section of

    S tensor F tensor L.                               (1)

This follows from the actual invertible epsilon_F mass pairing and Dbar,
not from an index or a proposed fermion quotient. The separate u,v local
coefficients are this one global rank-two spin/flavour field.

Choose a compact puncture coordinate w, r=|w|. The physical hyperbolic
metric has conformal factor comparable to `1/(r log(1/r))`. In the compact
spin frame sqrt(dw), the physical spin kinetic measure is consequently
comparable to

    |f(w)|² dr dtheta / log(1/r).                       (2)

Since F's unitary peripheral is -I, in its flat local frame each component
has a half-integer Laurent expansion

    f(w)=sum_(n in Z) c_n w^(n+1/2).

Angular orthogonality and (2) show that the n-th term has radial norm

    |c_n|² integral r^(2n+1)/log(1/r) dr.

All n<=-1 are forbidden. In particular n=-1 is the exact logarithmically
divergent endpoint `integral dr/[r log(1/r)]`; it is not admitted merely
because the power is critical. Thus any L2 holomorphic section has
`f(w)=w^(1/2) g(w)` with g holomorphic at p. Its norm in the auxiliary
flat S/F/L metric tends uniformly to zero at p.

That squared norm is globally subharmonic on C minus p: the tensor
connection is unitary flat and the section is holomorphic. On C minus
a small disc, the maximum principle bounds it by its boundary maximum.
Let the radius tend to zero; that maximum tends to zero by the preceding
expansion. Hence the section vanishes identically.

Therefore the actual A3 **spin-field L2 kernel is zero**, for every
extending spin and every old Wilson coefficient L. This proof makes
no closed-range or Fredholm assumption at the essential threshold.

## 2. Keep the scalar/form modes and the continuum

F does not enter the scalar gaugino or connection/form slot in A3.
Their source equations are the old flat scalar/form equations. The old
complete line calculation gives one scalar and one form zero mode when
L is trivial, and none for a nontrivial degree-zero unitary L. The latter
statement uses the actual compact elliptic canonical line and strict L2
pole bound, not a genus-zero substitution.

The local endpoint is also directly visible. The scalar norm has radial
weight `dr/[r log(1/r)^2]`, admitting a bounded constant but no pole. The
form norm is conformally invariant; a simple pole has divergent `dr/r`
norm, so its antiholomorphic form extends across p. Compact elliptic
degree-zero flat scalars and K-valued forms each have one section for
L trivial and none otherwise. These checks retain the physical scalar
and form densities separately.

The old order-three Wilson fixes nine A3 directions, the unbroken su3
and u1, and gives nontrivial characters to the other six. Thus the
candidate complete A3 physical left kernel has

    9 gaugino modes + 9 connection/form modes,
    0 spin modes.                                     (3)

These are counts of four-dimensional left Weyl profiles; conjugate right
antiparticles are not additional independent left fields. The A3 block
still has zero in its essential spectrum from the spin tail. The scalar/
form zeros in (3) therefore coexist with a continuum at threshold.
One cannot infer disappearance of every normalizable state from the
escaping spin sequence, nor infer a gap from the finite kernel.

This does not calculate the rest of the integer-root 120 block. The D5
and `(10,6)` sectors have nonzero Higgs commutators and require their own
equivariant complexes. In particular this is not a total neutral or up-type
matter roster, a weak-current overlap, or a viability claim.

## 3. A rejecting control and input account

If F is trivial and S tensor L is trivial, constant spin sections have
finite physical norm. The old two spin zero modes per such coefficient
survive. Their auxiliary flat norm does not tend to zero at p, so the
maximum-principle argument just used does not apply. Removing the flavour
peripheral sign while retaining the vanishing conclusion would be wrong.

The spin-line flat metric used in the proof is auxiliary. All physical
L2 restrictions came from the actual hyperbolic kinetic density. The
elliptic genus and extending spin are essential hypotheses; no higher-
genus or alternative-end exclusion is inferred. No new boundary
projector, mass term or state-selection law was supplied.

Before: the actual free centralizer tail, with its global kernel undecided.
After, as a candidate hand result: no normalizable centralizer spin zero
mode, while the old scalar/form kernel remains. Independent review must
check the Laurent convention, logarithmic endpoint, tensor holomorphic
structures, maximum principle and complete mass-map interpretation.
No physical input or measured parameter is marked paid.
