# R15 — global singular Higgs existence and the full regulated charged pair

The R14 field extends through the complete manifold **in the prescribed
commuting source ansatz**. The extension is an analytic parametrix-plus-
resolvent construction, not a computed numerical mesh field or a unique
vacuum. The finite-cutoff charged cohomology has multiplicities **four
and one**, hence net magnitude three. For a compact E6 parent the charged
adjoint sectors are a Spin(10) spinor and its conjugate, not an inserted
27. These are constructive steps along the singular-cusp path. The
normalizable spectrum in the complete singular limit is not yet earned.

## 1. What is specified, and what is proved

Take a connected orientable complete finite-volume hyperbolic 3-manifold
M, curvature length one, and finitely many disjoint properly embedded
geodesic source lines, with constant densities beta_a per proper length.
All beta_a are positive for the boundary-sign application. A rank-two
cusp has metric (abs(dw)^2+dz^2)/z^2, w modulo Z+tau Z, area A=Im(tau).
Choose a topologically trivial compact gauge bundle with W=0 and a
constant Cartan direction u. These are declared modeling data, NOT an
identification with the principal Riley local system or an ADE fibration.

There is a real global F, smooth away from the lines, such that

    Delta F = J,       J = 2*pi*sum_a beta_a delta_(line_a),
    phi = u dF,

with the R14 logarithmic line singularities and the required outward
cusp asymptotics. Delta=div grad; the nonnegative scalar operator is
L=-Delta. J is a locally finite distribution of infinite total charge,
not an integrable source on a closed compact manifold. Thus this does
not contradict the closed-base Gauss constraint. The commuting bracket
terms vanish; closedness and coclosedness hold off the specified sources.

### The global gluing argument

1. On each high cusp use R14's exact periodic solution

       F_i = sum_a beta_a U_i(w-p_a)
             + (pi Q_i/A_i) z^2 log(z/z0_i),
       Q_i = sum of endpoint densities on that cusp.

   In a tubular neighborhood of each compact source segment use
   beta_a log(tanh r). In the exact hyperbolic cylindrical metric,
   its equation is F''+(coth r+tanh r)F'=0 and its flux per unit line
   length is 2*pi*beta_a. Parametrices on an overlap have the same
   singular part and differ smoothly. Patch their regular parts to
   obtain F0 with Delta F0=J+r0, where r0 is smooth and compactly
   supported on the original, unpunctured M.
2. On cusp i choose psi_i=chi_i(z) z^2, zero before a finite transition
   and z^2 afterward. Crucially, psi_i is NOT compactly supported,
   although Delta psi_i is. With s=log z,

       Delta psi_i = z^2 (chi_i''(s)+2 chi_i'(s)),
       integral_M Delta psi_i dvol = 2 A_i.

   Choose constants c_i satisfying

       2 sum_i A_i c_i = -integral_M r0 dvol.

   Then r=r0+sum c_i Delta psi_i is orthogonal to the constants.
3. On the COMPLETE smooth M the scalar L has only constants in its
   kernel, and zero is isolated below its essential spectrum [1,infinity).
   Therefore v=(L restricted to constants-perp)^(-1) r exists in L2.
   Elliptic regularity makes v smooth, including across each source
   after its explicit logarithm was subtracted. Finally

       F = F0 + sum_i c_i psi_i + v

   has Delta F=J. If lambda_*>0 is the scalar gap, the bounds are
   ||v||2<=||r||2/lambda_* and ||dv||2<=||r||2/sqrt(lambda_*).
   No numerical lambda_* or pointwise m202 corrector is claimed.

The scalar spectral input is standard; at n=3, p=1, k=0 its threshold
in (5.14)--(5.15) is 1. It does not give a gap for the one-form or
charged operator. [Golénia--Moroianu, Proposition 5.2](https://arxiv.org/pdf/0705.3559).
An independent radial identity checks the threshold: for s=log z and
f=e^s w, the radial energy minus the scalar norm is the integral of
abs(w')^2 plus the endpoint term [abs(w)^2]. Dirichlet tails have no
negative endpoint contribution.

In the high cusps v is harmonic on the whole torus. Its L2 Fourier
expansion allows a constant and decaying z K1 modes, not a z^2 term.
It therefore cannot cancel F_i's leading z^2 log z radial derivative.
When Q_i>0 all sufficiently high exterior caps have outward dF.
Small tubes around positive sources have inward dF, since the excised
domain's outward normal points toward the source. Choose large finite
caps and small finite tubes: the boundary is E (exterior caps) union
T (source annuli), with their common circular seams retained. Corners
can be rounded while retaining the relative boundary pair's topology.

This fills the **existence** part of core matching in the stated ansatz.
It does not calculate the actual values of c_i or v on a triangulation.
Moreover the allowed differences obey sum A_i delta_c_i=0. There are
s-1 real homogeneous through-flux freedoms for s cusps in this growth
class, plus an irrelevant constant. On m202, one remains. Global
solvability does not select a unique field, source amplitude or vacuum.

## 2. Three proper arcs: topology independent of their detailed pairing

SnapPy's actual m202 presentation is <a,b | aabbAbAABBaB>. Its relator
abelianizes to (0,0), so H1=Z^2, not an assumed family count. The two
cusps and chi(Q)=0 give H2(Q)=Z for the compact core Q. Both order-three
elements in the order-12 symmetry group preserve each cusp, with matrices

    [[0,1],[-1,-1]] and [[-1,-1],[1,0]],

in opposite order on the two cusps. Each self-map has three fixed torus
points; m004's order-eight group has no order-three element. These are
software geometric witnesses, not interval-certified isometry computations.

A nontrivial orientation-preserving order-three isometry has a smooth
one-dimensional fixed set. Its six cusp ends form three proper arc
components. Possible additional closed components are not excluded or
silently charged here. With three endpoints on each of two cusp tori,
at least one proper arc must join distinct cusps. This parity observation
is enough; we do not need R72's detailed numerical axis-pairing census.

Let C be Q minus the interiors of neighborhoods of the three proper arcs,
T their three annular sides and E the remaining two three-punctured tori.
Excision gives H2(Q,C)=Z^3; its other positive relative groups vanish.
The relevant exact sequence is

    0 -> H2(C) -> Z --v--> Z^3 -> H1(C) -> Z^2 -> 0.

The entries of v are oriented intersection numbers with the arcs. A
cross-cusp arc contributes +/-1; a same-cusp arc contributes 0. Hence v
is primitive and nonzero, so H2(C)=0 and H1(C)=Z^4. The meridian map
H1(T)=Z^3 -> H1(C) has kernel Z and image Z^2. The exact sequence for
(C,T), followed by complementary-boundary Poincare--Lefschetz duality,
then gives the complete groups below, over Z and hence over R or C.

| finite pair | b0 | b1 | b2 | b3 | Euler |
|---|---:|---:|---:|---:|---:|
| C, no relative boundary | 1 | 4 | 0 | 0 | -3 |
| (C,T), relative source annuli | 0 | 4 | 1 | 0 | -3 |
| (C,E), relative external surfaces | 0 | 1 | 4 | 0 | +3 |

An independent cell calculation on (T2 minus three disks) x I gives
exactly these groups at two resolutions and heights. This is a CONTROL
with the same homological hypotheses, not a false product identification
of m202 or its drilled fundamental group. One- and two-arc controls give
relative groups (0,k+1,1,0) and (0,1,k+1,0), net magnitude k. Three is
available from this selected locus; the field equation does not force
the choice of this locus over all others in the program.

The table also shows why Euler alone hid the defect: deleting the source
boundary T changes H0 and H2, even though it leaves Euler AND H1 unchanged
in this particular geometry. It is incorrect to infer that the domains
are the same because their Euler values agree.

## 3. What the count is a count of

On a FINITE truncated and excised C, F is bounded and smooth. For real
charged coupling q, the differential d_q=e^(-qF) d e^(qF) is conjugate
to d and preserves the relative boundary subcomplex. The finite mixed-
boundary Hodge problems therefore have the cohomologies just computed.
The sign-reversed, dual problem exchanges T and E. Their H1 multiplicities
are four and one; an orientation/charge choice decides which is labeled
R. Equivalently one may use H1 and H2 of a single pair, but must not
count both descriptions twice. This is the conditional regulated spectrum
implicit in the relative-cohomology mechanism, not just its Euler.
[Pantev--Wijnholt, (3.36)--(3.40)](https://arxiv.org/pdf/0905.1968).

Now choose the compact E6 parent, with u=omega_1^vee in the B351/R13
Cartan convention and long roots of squared length two. Reconstructing
all 72 roots gives the ADJOINT grading

    78 = (45+1)_0 + 16_(+1) + conjugate16_(-1).

The 40 zero roots span D5. Each charged sector is one 16-element orbit
of its Weyl group, with projected weight norm 5/4 and distinct dual
dominant labels. u has norm 4/3. At u=0 all 78 generators are neutral,
as required. This is an actual parent-adjoint check, consistent with the
specified reduction framework. [Braun et al., (B.15)--(B.16) and (B.23)](https://arxiv.org/pdf/1812.06072).

Thus this parent/domain choice has **four spinors and one conjugate**
at finite cutoff (or the reversed labels): net three Spin(10) spinors,
with a vector-like pair retained. There is no extra charged 10+1 from
an arbitrary 27, no inserted E8 family tripling, and no derived mechanism
here that lifts the remaining pair. The gauge Lie algebra is D5+u1;
the global form, physical fibre transport, anomaly cancellation/inflow
and subsequent SM breaking are not selected by this root calculation.

Ordinary flat-local-system cohomology on a smooth manifold is NOT this
charge-dependent relative-domain problem. In particular, a duality of
smooth absolute local systems cannot silently replace the complementary
T/E conditions. This is why the newly received SM-seat B1280 result is
not a test of this singular candidate. Its own computations are preserved
as incoming work, not recertified or globally refuted by this round.

## 4. The exact remaining physical test

The complete singular limit is substantive. As tubes shrink and cusp
caps recede, multiplication by exp(qF) is unbounded. The finite-pair
cohomology is therefore NOT, by that conjugation argument alone, the
normalizable cohomology of the complete charged operator. The scalar
reduced inverse in section 1 cannot be used as its spectral certificate.

The next task on this SAME path is to derive the local charged Witten/
Dirac domain near the logarithmic lines and the high cusps, and test
whether the finite four/one kernel converges to admissible normalizable
states. Keep the effective product q*beta (including the Higgs amplitude
and kinetic conventions), not just an arbitrary integer charge label.
Begin with the twisted de Rham operator in the actual hyperbolic
geodesic-tube metric, all form degrees and both signs of q*beta. Compare
minimal/maximal domains and the domain supplied by a defect completion;
do not choose an extension merely to retain a desired count. Include
nonzero angular modes and the exact R14 cusp asymptotics as controls.
Then compute interactions/pair lifting within that domain and the same
parent. Neither a singular finite-action source completion nor a global
G2 gravity-plus-matter construction follows from the present Poisson proof.
Source selection, the flux freedom, physical action/fibre identification
and distinct empirical predictions remain duties toward the full TOE.

## 5. Verification, custody and honest banking status

Source, design and eleven new tests were sealed in **8e0981a0** before
first execution. [Design](GLOBAL_SINGULAR_DESIGN.md),
[producer](global_singular.py), tests/test_physical_bridge_global_singular.py.
First producer completes in 2.746 seconds, with its full scientific JSON
retained at [first run](global_singular_first_run.json). Exact identities
pass, including two cutoff profiles, the zero-flux cutoff-constant
control, local source normalization, mean-repair and unequal-area failure.
All Betti groups, not merely Euler, agree. The source is unchanged.

The R12--R15 group is **45 passed**, one GUI warning, 16.42 seconds.
[Checks](GLOBAL_SINGULAR_CHECKS.txt). A completed broader regression is
**182 passed, 3 failed, 8 errors**, one warning, 153.93 seconds:

    OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 python3.12 -m pytest
    tests/test_physical_bridge*.py tests/test_b1255_generation_type.py
    tests/test_b1084_g2_cone.py tests/test_b1105_b1106_locks.py
    -q -p no:randomly --tb=short

Failures remain the original G2 NumPy-key exporter and two R7 small-step
Hessian comparisons; errors remain the original R11 QQ/ZZ fixture issue.
Their separate repairs and mathematical controls pass in this run. No
original seal, tolerance or test is replaced. The [regression receipt](GLOBAL_SINGULAR_REGRESSION.txt)
redacts environment path prefixes only; the original byte-faithful failed
capture is retained locally in GLOBAL_SINGULAR_REGRESSION_RAW.local.txt,
explicitly ignored from public Git. Scientific JSON is unredacted.

Initial reporting gates are 27 pass/3 fail, **NOT unchanged in inventory**.
The seal-provenance gate now flags R15's missing literal BANKED IDENTITY:
and PRIOR ART: markers. Registering the older R13/R14 pre-execution seals
as late receipts also exposes their marker omissions. The full inventory
is eight paths, not the five paths printed by that gate's truncated list.
The mathematical design content and the actual earlier commit seals are
retained; no retroactive pre-execution compliance or full green is claimed.
[Gate output](GLOBAL_SINGULAR_INITIAL_GATES.txt),
[complete marker inventory](GLOBAL_SINGULAR_PROVENANCE_INVENTORY.txt).
Attribution and static-vacuity debt remain. Main/independent acceptance
and the full-repository suite are not discharged by this local checkpoint.

Fetched pins: main 506c591f080218c4ced3997b0317703b7f711f9d,
physics 659487bbd93c7990c4686a8b86985b6b66efedc4,
SM c3c3a8ed6fa9e447f8e27d7f5962c48503eed4f0. No new B number,
source-branch merge, PR, push or external message. R15 is path-local.

The final staged-state gate repeat has the same 27 pass/3 fail and
eight-path marker inventory, review-due 105. Its complete output is
GLOBAL_SINGULAR_GATES.txt. The artifact audit before this final receipt
checks 160 latest-path hashes with zero mismatches; hashes are checked
again after adding it. Ordinary git diff --check flags four trailing
spaces copied from the original pytest failure transcript; they are
intentionally preserved. The check passes with only blank-at-eol
disabled. This is not a test failure repaired by changing numeric data.
