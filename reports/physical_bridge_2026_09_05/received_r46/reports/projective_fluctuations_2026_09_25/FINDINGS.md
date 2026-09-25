# F13: a unique background with a defined matter-interaction channel

September 25, 2026. Local fork `audit/fork-2026-09-20`.
Scientific seal **3237af91**, made before any new test execution.

## Verdict

F12's exceptional global harmonic backgrounds now have a uniqueness
argument in their specified end class. Their actual charged matter
profiles have an analytic decay bound sufficient for parent interaction
integrals. The six-dimensional coefficient sector that mediates the
4--4--6 interaction is exactly acyclic at all the exceptional parameters,
and has a positive complete-space spectral gap (not numerically measured).

This establishes a better-defined **classical interacting candidate**
inside the supplied parent theory. It does not establish a nonzero
coupling, unequal matter--mirror responses, a quantum phase, chirality,
three observed generations or a physical theory of everything.

**Verification grade:** 21 new exact/control tests passed; 149 unchanged
predecessor and parent-vertex tests passed. The global uniqueness,
regularity, decay and functional-domain applications are **authored
analytic proofs**, not independently reviewed theorems or numerical
PDE solutions. Finite checks must not be used to inflate that grade.
No failed F11 prior or earlier source version was removed.

## 1. The arbitrary core extension no longer picks the answer

Two determinant-one harmonic metrics in F12's bounded-distance cusp
class have bounded squared target distance. It is subharmonic. Complete
cutoffs and finite base volume force it to be constant, without assuming
finite total Higgs energy. The distance second variation then gives a
parallel commuting endomorphism between the two metrics. F12's verified
full `Mat4` holonomy algebra makes it scalar; determinant one removes
the scalar freedom. The two metrics are equal.

Thus the arbitrary smooth reference extension over the compact core
was a construction aid, not an extra background-selection parameter.
The representation, q, twist, base geometry and asymptotic class remain
choices. This uniqueness statement is not extended to other end classes
or to unverified irreducibility on every cover. Constant unequal metrics
for the trivial representation supply the necessary failure control.

## 2. Exact spectrum of the actual mediator coefficient

The parent sector is `(10,6)`, with `6 = exterior-square E_chi`.
Its twist is **chi squared**, not an independent sign.

| Exceptional matter data | Six twist | rank B | rank J | H1 of six |
|---|---:|---:|---:|---:|
| q = 7 +/- 4 sqrt(3), chi = +/-i | -1 | 6 | 6 | 0 |
| q = 17 +/- 12 sqrt(2), chi = -1 | +1 | 6 | 6 | 0 |

The computations take place in the exact quadratic fields, so they
certify BOTH roots, not a floating sample. Fox derivatives agree with
an independently composed affine-block cocycle calculation; the group
relation and `J B=0` are explicitly checked. Nonzero minor witnesses:

    p14, six=-1: det B_minor = 64; det J_minor = 24064.
    p34, six=+1: det B_minor = -18q-18;
                det J_minor = 2822400-80640q.

The indicated determinants are coprime to their quadratic polynomials.
Both opposite-character controls also have H1=0 at these loci, while
the trivial one-dimensional coefficient correctly recovers H1=1.
The [complete witnesses](EXACT_WITNESSES.txt) retain row/column choices.
This is four exact field/character cases, not a family census.

The six's longitude has eigenvalues q^2 and q^-2, neither equal to one.
Its explicit all-frequency inverse and full radial Cartan homotopy give
ordinary--L2 comparison and compact resolvent for the actual F12 metric.
Hence zero H1 implies a strictly positive smallest one-form eigenvalue
delta6. We have **not computed delta6**, and F09's older `Delta>=1`
estimate belongs to another background and is not imported.

The four, its dual and six have no invariant zero-forms; the traceless
adjoint four has no flat invariant by irreducibility. Finite base volume
keeps the commuting 45 gauge zero-forms normalizable. This gives exactly
the unbroken **gauge algebra so(10)** in the adopted parent, not the
Standard Model group or a newly derived global group quotient.

## 3. The fluctuation operator really comes from the parent action

Keeping the published noncommuting action's normalizations, write
C=A+Psi, and a variation u=a+psi. Its curvature variation is `d_C u`;
the linear moment variation is `delta_A psi + [Psi_i,a_i]`. The other
real component of `d_C^dagger u` is precisely the compact-gauge condition
`delta_A a + [Psi_i,psi_i]`.

After this explicit background gauge fixing, the quadratic potential is

    (2/g7^2) (||d_C u||_2^2 + ||d_C^dagger u||_2^2).

This earns the Hodge operator as the **internal scalar block of the
actual Hessian**, rather than renaming a holonomy eigenvalue a mass.
The form-norm factors and first-jet signs are tested, including a wrong-
sign control. Full gauge-vector mixing, ghosts and quantum corrections
are not computed; the block inverse is not a complete physical propagator.

With the displayed kinetic normalization its positive Euclidean block
obeys `||(p^2+2 Delta6)^-1|| <= 1/(p^2+2 delta6)`. This is a qualitative
controlled inverse, not an absolute mass or measured coupling prediction.

## 4. The modes belong to a legitimate nonlinear domain

A sufficient fixed-end domain is the complete `d_C+d_C^dagger` graph
domain intersected with L4. Products of two variations then lie in L2,
so the full curvature and moment residuals define a finite differentiable
positive potential. Complete cutoffs supply compactly supported dense
approximants; the linear Green identities have no remaining end flux in
this class. The BPS background is stationary there despite its infinite
total Higgs norm. No physical infinity was subtracted.

Importantly, this domain does not simply exclude the matter modes.
The shrinking cusp homotopy gives a quadratic confinement estimate;
the Clifford IMS identity and an Agmon multiplier yield

    integral z^2 exp(2 epsilon z) |alpha|^2 < infinity.

Scaled interior estimates, using the ACTUAL harmonic metric's bounded
distance to the explicit reference, improve this to bounded pointwise
profiles and Lp for every p>=2. The matter modes therefore are L4.
L2 alone would not suffice: the explicit cusp function z^(3/4) is L2
but not L4, and that countercontrol is retained.

Consequently the parent's bilinear six-valued source J built from two
matter profiles belongs to L2. Its scalar-block response is finite:

    0 <= <J,(p^2+2 Delta6)^-1 J>
       <= ||J||_2^2/(p^2+2 delta6).

This establishes convergence, **not J != 0**, nor a different response
for the dual modes. F09's real-Codazzi cofactor argument is inapplicable
to this nonparallel background; a rank-one-profile zero-source control
prevents importing that conclusion by name.

## 5. The next discriminating questions

1. **Before computing coupling sizes, test all relevant base-isometry
   plus bundle-duality pairings.** F10 excludes flat fiberwise pairings,
   not these nonlocal ones. If an isometry preserves the background
   class and exchanges the dual sectors, the uniqueness just earned may
   force equality of the complete interaction tensors. That would be a
   scoped constraint on this background, not a universal chirality kill.
2. If no such complete pairing survives, construct normalized spatial
   profiles and compare the full parent response tensors, with error
   control and all gauge constraints. Absence of a pairing alone would
   still not prove selectivity or nonzero overlap.
3. A justified quantum mechanism and anomaly/gauge-compatible phase,
   generation count and symmetry breaking remain further requirements.
   Fixed-end admissibility here is not derivation or dynamical selection
   of the parent, representation, q, geometry or physical end theory.

The historical B1279 symmetry table was personally reread from commit
6f077ef2 during the unchanged-source runs, and the producer's part (a)
was inspected. Its geometry search uses floating arithmetic despite the
report's broad exact wording. It is useful candidate input for item 1,
**not** independent exact verification of those automorphisms here.
Its vacuum census and CP claims are not adopted or rerun in F13.

The complete proof and boundary qualifications are in [PROOF.md](PROOF.md).
Primary sources: [Braun et al., section 2 and Appendix B.1](https://arxiv.org/html/1812.06072v2),
[Riestenberg--Smillie, local distance variation](https://arxiv.org/html/2511.11469v3#S5.SS1).
Source inspection and run custody are in [RECHECKS.md](RECHECKS.md).
No new all-head absence claim, main-bank certification or publication.
