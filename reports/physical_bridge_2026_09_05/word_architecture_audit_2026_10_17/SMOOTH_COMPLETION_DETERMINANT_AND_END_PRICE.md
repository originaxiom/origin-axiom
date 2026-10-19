# What a smooth puncture completion must carry

October 19, 2026. Authored analytical source/compatibility audit, pending
independent review. No scientific producer or numerical experiment was
run. The scope is the specified rank-six ordinary-spin elliptic-fibre
problem and a completion realizing its specified holomorphic extension.
It is not a classification of all physical ends, E8 phases or chirality.

## The source question, not a universal cap assumption

The [actual trace calculation](ACTUAL_PUNCTURE_CONNECTING_MAP_AND_TRACE.md)
derives the interior connecting map and both finite-distance kernels.
It does not choose Lambda. This asks what else is required if one tries
to replace that supplied domain by a smooth cap without changing its
claimed coefficient bundle or silently deleting compensating modes.

Relevant source bodies were read directly: the existing finite-distance
Fredholm proof, the full weave_curved_action_2026_10_08/PROOF.md, the
weave_registered_embedding_2026_10_13/PROOF.md and the smooth-boundary
control silver_smooth_boundary_gate_2026_10_05/PROOF.md. The last is a
different problem, not evidence that an elliptic puncture was capped.
The source's interacting action retains its connection, moment map,
spin fields, all fermions and surface terms; it does not supply a
source-free cap or allow a scalar connection ansatz to replace E8.

The read-only already-banked query used `puncture cap determinant degree
traceless`; no settled verdict matched at least three of those five
terms. Its broad findings are not absence evidence for other terms or
other branches. The degree formula d-3 is ALREADY in the puncture proof,
not discovered here. The addition is its explicit determinant and smooth-
completion interpretation, with curvature distinguished from trace flux.

For degree conventions, Definition 33.44.1 and the exact/tensor degree
identities in [Stacks Project 33.44](https://stacks.math.columbia.edu/tag/0AYQ)
were read through Lemma 33.44.7. The local determinant and curvature
calculations below are given explicitly; no numerical source is used.

## The actual determinant line and residue

Let E_Lambda be the source's upper modification in d=dim Lambda of the
six critical plus directions. Its local frame relative to a unitary
multivalued flat frame e is z^(-1/2)e in Lambda and z^(1/2)e in the
complement. A unitary frame adapted to Lambda is a convention, not a
physical selection of it. The determinant of this change is z^(3-d).

The actual flat W has a global parallel determinant section e_det:
all of its a,b matrices have determinant one. In the extended local
determinant frame, e_det has coefficient z^(d-3). It is nowhere zero
away from the single puncture. Thus the stronger line statement is

    det E_Lambda = O_E((d-3)p),
    deg E_Lambda = d-3.                         (1)

This is the original determinant section's zero/pole divisor, not just
an inference from an Euler number. With P_Lambda the constant local
orthogonal projector, the logarithmic connection in this holomorphic
extension frame has residue

    R_Lambda=(1/2)I6-P_Lambda,
    tr R_Lambda=3-d,
    exp(-2pi i R_Lambda)=-I6.                   (2)

Every d=0..6 has the SAME peripheral holonomy. Its determinant is +1.
Hence neither -I6 nor its determinant picks an integer lift of the six
half-exponents. Choosing the upper extreme already chooses the nonzero
degree +3 in (1). It is not free 'regularity without flux' for an
ordinary-spin coefficient. The lower extreme has degree -3 instead.

A compact-bundle gauge transformation preserves (1). A singular
meromorphic frame change that alters its divisor changes the extension;
it cannot be called an innocuous normalization of the same completion.

## A traceless completion imposes a real constraint, not a no-go for E8

Suppose a proposed smooth completion has coefficient bundle E_Lambda
and an SU6 connection defining this holomorphic structure. Its induced
determinant connection is trivial: in local frames it is tr A=0 and
all transition determinants are one. Its determinant holomorphic line
is therefore trivial. Equation (1) forces

    d=3.                                       (3)

The associated ordinary chiral Dirac index on the compact elliptic curve
is then zero, as is the source's d-3 formula. This does not determine
the kernel: Lambda=U and Lambda=U_perp from the previous calculation
give respectively (3,3) and (0,0). Tracelessness alone cannot select
either plane or turn an index-zero operator into three chiral modes.

Necessary qualifications are essential:

- A cap changes the connection inside a neighbourhood. It is not the
  original flat punctured operator, nor is every cap known to produce
  one of these domains in a controlled shrinking limit. Equation (3)
  applies when the claimed extension really is E_Lambda.
- This rank-six bundle has its actual SU6 embedding, retained in the
  registered-embedding source. If a full E8 background preserves that
  principal SU6 coefficient bundle, it cannot give it determinant
  degree three by a traceless gauge change.
- If the background instead decomposes into different charged bundles,
  individual summands can have nonzero degree while the whole has zero
  degree. A complement must carry the compensating determinant. If the
  fields mix, a standalone sector index may not even be defined. The
  full charged operator and its physical reality condition must be used.
- An R/spin-c twist, determinant U1 field, defect/source or genuinely
  different geometric end changes the hypotheses. None is excluded;
  each requires its actual map/action/domain, not a relabelled cap.

In particular E8's total trace constraint is NOT a theorem that E8
cannot support a physical chiral spectrum. Nor does this audit retract
the separate compact silver construction or its conditional charged
three-generation positive.

## The holonomy does force curvature if the puncture is contracted

No flat connection on a smooth simply connected disc can retain the
boundary holonomy -I6: flat parallel transport has identity holonomy on
a contractible loop. Therefore a cap matching that boundary transport
cannot remain flat everywhere. This implication is conditional on
FILLING the puncture; the original punctured flat connection is valid.

Importantly, nonzero curvature does NOT imply nonzero determinant flux.
Here is an explicit local control on a disc of radius R0:

    B=(1/2)diag(1,1,1,-1,-1,-1),
    A=i(r^2/R0^2)B dtheta
     =i B(-y dx+x dy)/R0^2,
    F_A=2i B dx wedge dy/R0^2.                  (4)

The connection is smooth at the centre, anti-Hermitian and traceless.
Its radius-R0 parallel holonomy is exp(-2pi i B)=-I6 and tr F_A=0.
This proves a finite-radius curvature control, NOT a global stationary
solution matching the exterior normal current. Its curvature need not
match the exterior at that circle; such a join must solve the actual
variational problem. No B, profile or cap scale in (4) is derived from
the founding principle. The point is the countercontrol to the false
inference 'nontrivial commutator forces determinant flux three'.

## A nonzero determinant cap has a positive action cost in a fixed model

For a smooth unitary rank-N completion write its curvature
F_A=i H dvol, H Hermitian, and use the convention

    k=deg V=(i/(2pi)) integral tr F_A
           =-(1/(2pi)) integral tr H dvol.       (5)

The identity follows from the induced determinant connection tr A;
tr(A wedge A)=0. The integral of its curvature measures the transition
winding of that determinant line, consistent with (1). It is not the
sum of eigenphases modulo integers.

Suppose all this flux lies in a cap of area A_cap, with the declared
positive Yang--Mills term

    E_YM=(1/(2g^2)) integral tr(H^2) dvol.

Pointwise tr(H^2)>=(tr H)^2/N, followed by Cauchy--Schwarz for the
cap integral, gives

    E_YM >= 2pi^2 k^2/(N g^2 A_cap).            (6)

For N=6 and k=+/-3 this is 3pi^2/(g^2 A_cap). A shrinking-area cap
at fixed coupling cannot hide that trace flux in bounded pure gauge
energy. Trace normalization changes the declared coupling convention,
not the 1/A_cap conclusion. The bound is not a phenomenological value.

Within an ADJOINT U(N) moment-square control, tr[Q,Q dagger]=0, so the
same trace component survives in tr(F_phys+commutators)^2: adjoint
commutators cannot cancel it. This does NOT add a determinant U1 to OA
or prove the bound for an arbitrary charged matter/defect action.
Full E8 fields outside a retained SU6 adjoint, independent sources or
new counterterms require their own complete energy calculation.

This is a price for a specified trace-flux completion, not a proof that
all nontrivial caps require trace flux, divergent energy or instability.
The traceless finite-radius control (4) remains a positive counterexample
to that broader conclusion.

## Spectral bookkeeping and the next physical question

If degree-zero smooth caps were claimed to limit to the source's
upper-domain index +3 while all other modes were discarded, index
invariance would be a diagnostic: a continuous Fredholm interpolation
cannot change its index. One must locate failed continuity/Fredholmness,
compensating modes, a changed twist or a changed determinant bundle.
No such interpolation or decoupling theorem is asserted here.

For a separately supplied line L of degree ell and charge q, the same
elliptic ordinary-spin complex would instead have index
d-3+6q ell. This is a dependency calculation, not a proposed fit. A
physical charged decomposition or higher-dimensional complex has its
own index formula; it cannot inherit this one by matching a number.

The earned constraint is that a physical end must account for the
extension's determinant, curvature, full complement and energy/current
matching. Holonomy, local regularity, a zero-mode trace and a physical
end law are different data. Deriving one does not silently derive all.
No physical-input row is marked fully paid. Independent review and
source-complete admitted controls remain owed; frozen packages and
staged historical evidence are unchanged. No push or goal completion
is claimed.
