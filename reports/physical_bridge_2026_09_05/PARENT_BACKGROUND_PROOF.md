# R39 authored argument: a native background and the fields it requires

2026-09-20. UNSEALED, UNEXECUTED working argument. The specified exact
finite checks are PLANNED, not yet implemented or run. Global descent,
functional-domain and stationarity
statements remain authored mathematics, not independent acceptance.
E8, its action, the embedding and supplied four-dimensional spacetime
are model inputs. No torsion-free G2 completion is asserted.

## 1. The whole D5-singlet algebra

Let v0,...,v3 be the four last-three-coordinate vectors in the design.
They satisfy vi.vj=delta_ij-1/4 and sum vi=0. The twelve differences
vi-vj are exactly the E8 roots orthogonal to the D5 subsystem. This
is A3, with compact real form su4. Its defining weights have charges
(3,-1,-1,-1) under R38's U. The adjoint charge-four row E_(0a) and
its opposite column are not isolated scalars: the zero-charge su3
and central generator belong to their same Lie algebra.

All E8 weights, including all eight Cartan zeros, split as

    (45,1) + (1,15) + (10,6) + (16,bar4) + (bar16,4).

Here the 16 is R38's ACTUAL D5 spinor: its charge-one weights are
in the three entries of bar4, while its charge-minus-three weights
are the remaining entry. Root differences give the algebra map;
the simply connected SU4 integrates it. The presence of its faithful
4 in the E8 adjoint detects every nonidentity central element, so
the compact SU4 map has no kernel. This is not a map of hyperbolic
holonomy into compact SU4. The geometric connection below is complex,
with a positive unitary reduction.

## 2. All equations precede the source projection

Use the Hermitian convention of Braun et al. (2.9),(2.12),(2.17)--(2.19),
https://arxiv.org/pdf/1812.06072v2. Write the complex connection as

    C_i = [ 3 h_i       alpha_i             ]
          [ beta_i     -h_i I3 + B_i        ],    tr B_i=0.

h, alpha, beta and B are complex; alpha is a row and beta a column.
Set dh_ij=partial_i h_j-partial_j h_i and similarly for the other
entries. Matrix multiplication gives the full flatness residual:

    F00 = 3 dh_ij + alpha_i beta_j-alpha_j beta_i,
    F0b = d alpha_ij+4(h_i alpha_j-h_j alpha_i)
                        +alpha_i B_j-alpha_j B_i,
    Fa0 = d beta_ij-4(h_i beta_j-h_j beta_i)
                        +B_i beta_j-B_j beta_i,
    Fab = -dh_ij I3+d B_ij+[B_i,B_j]+beta_i alpha_j-beta_j alpha_i.

The real equation is the FULL matrix

    I = div_g(C+Cdag)+g^ij[C_i,C_jdag] = 0.

These formulas include every D5-singlet field. They do not mean
every possible E8 background is D5-invariant. When the residuals
vanish in this subalgebra, they also vanish in E8; the full positive
residual potential has zero first variation in EVERY regular
compactly supported E8 direction, including those outside the ansatz.
The background four-dimensional fields and all fermions are zero.
An uncomputed quantum action is not covered by this argument.

For the narrower choice h real, B=beta=0, set
G_ab=g^ij conjugate(alpha_ia) alpha_jb. In an orthonormal frame:

    I00 = 6 div h + tr G,
    I0a = div alpha_a - 4 h.alpha_a,
    Iab = -2 div h delta_ab - G_ab.

The opposite off-diagonal block is the Hermitian transpose. Thus
the central equation is 2 div h+tr(G)/3=0 and the remaining su3
equation is G-(tr G)I3/3=0. A nonzero positive Gram matrix of rank
one or two CANNOT be scalar. Three nonzero field components alone
do not help if their internal one-forms remain collinear. A full-rank
isotropic Gram matrix removes this one algebraic obstruction, but
must STILL solve d alpha+4h wedge alpha=0 and the off-diagonal D
equations. With h=df those equations say alpha=e^-4f eta,
d eta=0 and div eta-8 df.eta=0. No arbitrary tube density is allowed.
The beta-only ansatz has the opposite central sign. This must be
matched, not silently identified with R29's added source convention.

## 3. A noncommuting geometric positive control in the actual parent

On hyperbolic upper half-space z>0, g=z^-2 I, let E,F,H be the
normalized Sym3 generators with [H,E]=2E, [E,F]=H, F=Edag.
Set

    C_x=E/z,    C_y=iE/z,    C_z=H/(2z).

The fundamental precursor is q^-1 dq, with

    q = [ sqrt(z)  (x+iy)/sqrt(z) ]
        [ 0         1/sqrt(z)     ].

Its Sym3 derivative is the displayed C. Flatness follows either
from Maurer--Cartan or by computing every component. The curved
divergence is z^3 partial_i(z^-1 (C_i+C_i dagger)); it gives -2H.
The contracted commutator gives +2H. Both are nonzero; their sum
vanishes. The Higgs components do NOT commute, and W has curvature.
Dropping that curvature/commutator is not testing this background.

With phi=(C+Cdag)/2 and the trace in the unitary 4 representation,

    |phi|^2 = g^ij tr(phi_i phi_j) = 15.

This is a normalization in curvature-length units, not a measured
constant or derived physical scale. The positive Higgs L2 norm is
15 Vol(M); a cusp of coordinate torus area A above z=Z contributes
15 A/(2 Z^2). The source-free STATIC residual potential is zero.
Finite background norm is not a proof of a modulus, a mass gap,
quantum stability, or a complete finite gravitational action.

For an oriented quotient M=Gamma\H3 with a chosen SL2 holonomy
lift, q is a section of SL2(C)/SU2. For every gamma,
q(gamma p)=rho(gamma) q(p) k_gamma(p)^-1 with k_gamma in SU2.
Its derivative transforms C by a unitary gauge change; Sym3(k_gamma)
is unitary in the displayed normalized basis. This constructs the
global bundle, positive metric, Higgs and connection explicitly.
It does not apply a compact harmonic-metric existence theorem to a
cusp. A spin/lift choice is priced; no arithmetic-orbifold descent
through torsion is proved here. This works for both arithmetic rows
and nonarithmetic hyperbolic quotients, so it is NOT a selector.

The central-only trap is visible within this exact positive solution.
Its U component is h=dz/(2z); its charge-four row is
alpha_1=sqrt(3)(dx+i dy)/z, alpha_2=alpha_3=0. If one drops the
remaining B fields, the central part of I is STILL ZERO, but

    I_dropped = diag(0,-4,2,2),

and flatness also fails. The retained B fields cancel these residuals
in the actual solution. This is not a localized R29 tube resolution:
the fields fill the bulk and the charge split is not parallel under
the new connection. Neither the old scalar spectrum nor the old
three/zero index transfers without redoing its operator and domain.

## 4. The entire parent contains extra unbroken generators

Do not stop at the D5 centralizer used to DEFINE the construction.
The Sym3 four has no invariant vector; traceless End(4) also has none.
But exterior-square(4) has ONE invariant vector, as a common kernel
of the actual E,F,H matrices, not by an inferred dimension match.
The 248 therefore has 45+10=55 invariant generators.

Relative to the surviving D5 Cartan their weights are its forty
roots +/-ei+/-ej, TEN extra weights +/-ei, and five Cartan zeros.
The complete nonzero weight set is B5, with simple roots
e1-e2,e2-e3,e3-e4,e4-e5,e5. Its rank is five: the zero-weight space
is precisely the five-dimensional Cartan. This identifies the
compact invariant Lie algebra as so(11), not from dimension alone.
No unverified claim about the global gauge-group quotient is needed.

These commuting generators define parallel adjoint sections of the
global background. On a finite-volume complete quotient they have
finite positive norm. They are zero directions of the internal gauge
quadratic form integral (|D_W a|^2+|[phi,a]|^2), with the natural
complete-space form closure: cusp cutoffs approximate them with
vanishing gradient cost. On a compact truncation use compatible
natural, not imposed Dirichlet, data. This is an unavoidable sector
of THIS baseline. Further holonomy or boundary breaking changes it.

## 5. Self-duality is an explicit operator map, with domain conditions

In the normalized basis let J have anti-diagonal (1,-1,1,-1).
Then Jdag J=I, J^t=-J, and X^t J+J X=0 for E,F,H. Hence

    J (d+C) = (d-C^t) J.

J intertwines the fundamental and dual flat bundles globally,
including their positive metrics. Unitarity intertwines the
adjoints as well. Thus the Laplacians in every form degree have
unitarily equivalent spectra on domains carried into one another
by J. In particular the natural minimal/maximal L2 closures are
carried into one another because J maps compactly supported smooth
sections isometrically. Matched boundary conditions work likewise.
This proves equality, not a computed value of either kernel.

The Spin(10) 16 and its conjugate multiply precisely these two
coefficient bundles. This baseline cannot yield unequal multiplicities
under that common physical dictionary/domain. B574's old SL2
self-duality is prior, not rediscovered here; the new duty is to
check its action on THIS positive parent operator. Extra defects,
nonmatched boundary sectors or holonomy leaving this self-dual class
are not covered. A full SL4 generator set has no such bilinear;
adding U to the invariance equations supplies a failable algebra
control, not an exhibited chiral flat background.

Finally the charge-minus-three singlet and charge-one triplet of
bar4 mix through the charged fields. Even where a triangular local
connection happens to preserve a flag, its positive adjoint need
not preserve it, and the full physical operator does not split into
the old independent charge lines. They must be kept together.

## 6. Meaning for the mission

The positive would pay a real but limited debt: a global classical
noncommuting candidate-parent background with no inserted source
density. The same calculation prices its enlarged gauge algebra,
pairing and lack of localized source support. It does not derive
E8, its embedding, a chiral deformation, a source-end completion,
three families, Standard-Model breaking, gravity or measured values.
Next seek a specified admissible non-SL2 deformation or source/end
matching that changes these exact mechanisms, retaining all fields.
Do not discard R29's separate valid action or claim all PW routes
are excluded by the particular geometric baseline.
