# Relative winding, magnetic flux and a variational boundary law

2026-11-15. Author derivation. The construction below calculates a
conditional gauge/phase response and its input ledger. The physical
origin of the phase field and its coupling remains a derivation duty.
No completion of SM3 or gravity follows from this sector calculation.

## 1. Recover the relevant prior results

The exact core response, flat relative periods, cut orientations and
fixed-flux sewing in the November 8
`ACTUAL_CORE_MEAN_RESPONSE_AND_FLUX_SEWING_2026_11_08.md` are reused.
The old magnetic stationary family, its energy and its charged bosonic
instability are in `weave_magnetic_stationarity_2026_10_08/PROOF.md`.
These are calculations in a supplied curved gauge parent.

The earlier `REGISTERED_PRINCIPAL_PARTS_AND_GREEN_TRANSPORT.md` retains
the root-coordinate derivative and the full argument action. It
demonstrates that registering data affect the transported operator
problem. Its rank-six local module has a different field type from
the Abelian boundary phase introduced here. An identification requires
an actual map and transported norms and operators.

Main B1641 and B1700 retain a count of three per unit for a specified
modular extension problem. Those results are preserved. Their end
unit and physical operator identification remain separate premises.
The field/domain distinction in B1672 is retained.

## 2. A relative class can reside in the reference alone

Let X be the compact oriented figure-eight knot exterior and Y its
boundary torus. Use the oriented meridian mu and longitude lambda.
The longitude bounds a Seifert surface in X, whereas the meridian
generates H1(X;Z). Thus the restriction map on first cohomology is

\[
 H^1(X;\mathbb Z)\longrightarrow H^1(Y;\mathbb Z),\qquad
 k\longmapsto(k,0).
\]

The long exact sequence, together with ordinary H2 cohomology zero,
gives

\[
 H^2(X,Y;\mathbb Z)\simeq
 \mathbb Z^2/\langle(1,0)\rangle\simeq\mathbb Z.
\]

This agrees with Poincare–Lefschetz duality. The same relative
integer occurs for an oriented compact surface C with one boundary.
[Hatcher, Theorem 3.43](https://pi.math.cornell.edu/~hatcher/AT/ATch3.pdf)

Take a trivial Hermitian line on X, connection `nabla=d-iA`, and a unit
boundary section `s=exp(i phi)`. The local real connection form in this
section is

\[
 \eta=A|_Y-d\phi,\qquad F=dA.
\]

Under a global circle gauge transformation, A changes by d alpha and
phi changes by alpha. Eta and F are invariant. For an oriented relative
surface C whose boundary is lambda, define

\[
 N=\frac1{2\pi}\left(\int_C F-\oint_{\partial C}\eta\right).
                                                        \tag{1}
\]

Stokes gives `N=(1/(2*pi))*integral d phi`, the longitude winding.
A gauge transformation that extends over X cannot change this
longitude winding. It may change the meridian winding, consistently
with the quotient above.

Now choose A=0 and a boundary section of longitude winding n. Then
`F=0`, `eta=-d phi`, and `N=n`. Every relative class occurs with the
same zero bulk curvature. Formula (1) tracks the curvature and the
reference together. Inferring magnetic zero modes from N alone would
discard eta and change the problem.

The boundary phase may be a physical field, a prescribed source or a
reference kept by the measuring apparatus. Its mathematical existence
alone does not choose among these physical roles.

## 3. The leading phase kinetic term gives a gauge-invariant source law

On a compact oriented surface C with one boundary circle, metric g and
positive area A_C, consider a real Abelian connection A in the existing
static commuting gauge channel. Write `F=f*dvol`, `c_H>0` for the
generator norm and `G=g6^2>0`.

Introduce a unit boundary phase exp(i phi), of unit charge in the
specified circle normalization, with positive kinetic coefficient kappa.
The derivative kinetic term of this unit-norm field is
`|D exp(i phi)|^2=|d phi-A|^2`. The candidate action is

\[
 E[A,\phi]=\frac{c_H}{2G}\int_C F\wedge *F+
       \frac\kappa2\oint_{\partial C}\eta\wedge *_Y\eta,
 \qquad\eta=A|_Y-d\phi.                                  \tag{2}
\]

Equation (2) is supplied as a conditional local quadratic action. Gauge
invariance determines its covariant derivative. It leaves kappa, the
field's physical origin and its relation to the full parent open.
For a boundary scalar of fixed norm v, its kinetic normalization
contributes to kappa. Higher interactions and additional fields may
change the response and need their own derivation.

Independent variations of A and phi give

\[
 d*F=0\quad\hbox{in }C,\qquad
 \frac{c_H}{G}i^*(*F)+\kappa *_Y\eta=0\quad\hbox{on }Y,
 \qquad d_Y *_Y\eta=0.                                  \tag{3}
\]

The first boundary term follows by integrating `d(delta A)*F` once.
Varying the phase gives `-kappa integral d(delta phi) *_Y eta` and
hence the last equation. The current `j_Y=kappa eta` is conserved.
The Robin response and the current law therefore follow from a single
action with both fields varied. Holding phi fixed would change the
source problem and must be declared.

## 4. The mean response is exact in the actual core metric

Let `ell_Y` be boundary length, use its positive arclength s, and set

\[
 B=\oint_Y A,\quad\Phi=2\pi n,\quad
 r=\frac{c_H}{G A_C},\quad p=\frac\kappa{\ell_Y}.
\]

For globally defined A, Stokes fixes the curvature integral to B.
Cauchy–Schwarz in the bulk and on the boundary gives

\[
 E[A,\phi]\geq\frac12\{r B^2+p(B-\Phi)^2\}.              \tag{4}
\]

Both bounds can be attained together. Set constant f=B/A_C and prescribe
the constant boundary trace `A|_Y=(B/ell_Y) ds`. The old core proof
constructs its global primitive and corrects its trace by an exact form.
Choose the phase with `d phi=(Phi/ell_Y) ds`. This is a well-defined
circle-valued field when Phi=2*pi*n. Its eta is constant in arclength
and obeys the phase equation. Thus (4) is the exact on-shell reduction
at fixed B and n for this channel.

The stationary circulation and sector energy are

\[
 B_* =\frac p{r+p}\Phi,\qquad
 E_n=\frac12\frac{rp}{r+p}\Phi^2,\qquad
 \partial_B^2E=r+p>0.                                   \tag{5}
\]

Equivalently the response after eliminating B is
`(r^-1+p^-1)^-1`. The residual boundary mismatch is
`B_*-Phi=-r*Phi/(r+p)`. These satisfy (3).

For finite positive p, physical curvature flux is screened,

\[
 \frac1{2\pi}\int_C F=\frac p{r+p}n,
 \qquad
 \frac1{2\pi}\left(\int_C F-\oint_Y\eta\right)=n.         \tag{6}
\]

The stiff-boundary limit p to infinity locks the circulation to Phi.
The limit p to zero has vanishing minimizing curvature while retaining
the relative reference winding. This recovers the control in section 2.

Closed relative one-forms with zero boundary trace survive the reduction.
On the genus-one core their local real dimension is two. Their curvature
energy vanishes, while charged probes and kinetic norms can distinguish
their periods. The reduced circulation Hessian in (5) cannot establish
uniqueness or stability of the complete gauge/Higgs/fermion theory.

## 5. Exact radial recovery control

For a separate recovery model take a flat solid torus
`D_R^2 times S_L^1`, with metric `dr^2+r^2 dtheta^2+dz^2` and
period L for z. Its boundary phase has winding n in theta. This
circle is the nonextendible boundary cycle in this recovery model.
It is a different carrier from the knot exterior.

For `A=a(r)dtheta`, regularity at r=0 and the Maxwell equation give
`a(r)=B0*r^2/R^2`, where B0=a(R). With bulk coefficient `1/(2G)`
and boundary kinetic coefficient kappa, direct integration gives

\[
 E(B0,n)=\frac{2\pi L}{G R^2}B0^2+
         \frac{\pi\kappa L}{R}(B0-n)^2,
 \quad B0_* =\frac{\kappa G R}{2+\kappa G R}n,
 \quad E_n=\frac{2\pi L\kappa}{R(2+\kappa G R)}n^2.        \tag{7}
\]

Its disc curvature flux is 2*pi*B0. This gives an independent smooth
control of screening, the stiff limit and the quadratic sector law.

## 6. An artificial seam and a physical phase source are different data

The old core and tail response with trivial added gluing is

\[
 E_0(b)=\frac{c_H}{2G}\left(\frac{b^2}{A_C}+\frac{b^2}{A_T}\right).
\]

Variation gives b=0. Its nonzero flux-gluing problem instead uses

\[
 E_{\rm glue}(b;\Phi)=\frac{c_H}{2G}
       \left(\frac{(\Phi-b)^2}{A_C}+\frac{b^2}{A_T}\right),
 \quad b_*=\frac{\Phi A_T}{A_C+A_T}.
\]

The resulting uniform curvature and energy depend on total area and
the retained gluing datum, so moving the artificial cut is consistent.
These are existing results.

If a phase action is placed on the seam of the trivially glued problem,
the reduced energy becomes

\[
 E_{\rm source}(b;n)=\frac12\{(r_C+r_T)b^2+p(b-2\pi n)^2\},
 \qquad r_C=\frac{c_H}{G A_C},\quad r_T=\frac{c_H}{G A_T}. \tag{8}
\]

The same Schur complement gives a unique mean circulation. The core
and tail curvature integrals are -b and +b in the old common-coordinate
convention, giving zero total added curvature. The phase carries a
localized current which balances the discontinuity of the response.
This source problem retains different global data from fixed flux
gluing. Identifying its n with the old added total magnetic flux would
erase a term in (1).

A phase term at an arbitrary cut has a position and stiffness. For it
to represent integration of existing physical fields, its functional
must evolve under moving the cut and obey the composition law of the
actual response. That derivation would discharge a source input.

## 7. What the sector equations select

At fixed positive r and p, (5) gives `E_n=C n^2` with C>0. Every integer
is allowed by the relative topology. The minimum is n=0. If an
independently earned condition restricts to nonzero sectors, the minima
are n=+1 and n=-1. Orientation reversal exchanges them. Nothing in this
specific quadratic model selects n=3. The result applies to (2), with
its fixed metric, fields and source assumptions.

Zero additional magnetic winding retains the whole geometric object,
the old background fields and the registering reference. A derivation
which excludes absolute nothingness still needs a map before it can
exclude this populated zero-added-flux sector.

The defining relations alone leave kappa free and permit higher
boundary interactions. Different matter fields or a dynamically
unstable zero-winding background may change the sector equations.
Their full action, admissible variations and physical field map must
decide that question. No universal sector-selection exclusion follows
from (5).

## 8. Preserve the existing route from one end unit to three

The alternative already in the repository earns its factor of three
from a rank-three modular coefficient system and a unit of specified
end data. On a proper curve, a rank-three bundle V satisfies

\[
 \chi(V(mp))-\chi(V)=3m.                                \tag{9}
\]

For m=1, this follows from the exact sequence with the principal-parts
quotient of length three at p. Iterate it for positive m and reverse
the sequence for negative m. The record's modular/orbifold operator
adds its actual weight and lift conditions. B1641 and B1700 already
verify their stated count and do not derive the end unit.

This makes an identified research route available. Derive a physical
end/source law with one minimal nonzero unit, earn the registering
triplet's physical operator representation, and prove that its actual
index is the one calculated by that extension. Then the factor three
can come from the representation and the unit together. It need not
be introduced as degree-three magnetic flux. Equation (9) itself
does not identify the magnetic phase winding n with this end unit m.

The finite-distance puncture lattices, ordinary spin operator and
complete curved four-slot physical operator have distinct domains in
the existing source. The registered field, spin and argument maps
must accompany any claimed identification. Main's M4 asks for
precisely this map. It remains open after the present calculation.

## 9. Input accounting and the next consequential calculation

The new conditional calculation determines the mean connection and
boundary current once the metric, gauge normalization, phase field,
stiffness and winding sector are given. It establishes the relative
curvature/reference map and the response composition explicitly.

The phase's physical origin, kappa and any additional interactions,
its support and full-parent representation, its admissible winding
sectors, the charged fermion domain and the selection of an end unit
remain independent duties. This card removes no foundational input.

The highest-value continuation is to derive the phase/reference
functional from the existing physical core and end fields, retaining
their normalized currents and zero modes. It must then explain whether
the index-changing unit is dynamically preferred, topologically required
or still free. The positive three-per-unit modular count and the
magnetic constructions remain available as separately typed controls.
