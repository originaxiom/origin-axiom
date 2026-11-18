# A permitted stabilizer and the fermion price it pays

2026-11-18. P-C8 author hand control, not independently checked.
No scientific code, imports, CAS or tests. This answers a concrete
alternative left by the compact action/roster calculation: can fields
already in that action stabilize the other flux bands? A permitted
mechanism is exhibited, with its state and spectrum cost retained.
It is not selected by genesis or a completed physical model.

## 1. One existing adjoint field can distinguish the two flux bands

Keep C=e1-e3 and the compact flux B C of the preceding control.
Choose the commuting E8 cocharacter

    T=(0,1,0,1,1,1,1,-1), C dot T=0.

It is in the E8 lattice: integer entries with even sum. This is
an exhibited Cartan direction, not a uniqueness theorem or a new
primitive. On the 56 root spaces of C-charge +1, the T weights are

    +3 once, +1 twenty-seven times,
    -1 twenty-seven times, -3 once.                  (1)

The same multiplicities hold at C-charge -1. To check (1), the
24 integer roots of C-charge +1 have T=+1 or -1, twelve each.
The 32 half-integer roots fix opposite signs at coordinates 1,3.
The other six signs have odd minus parity. Multiplying by the one
negative entry of T changes it to even parity. Their T charges are
3,1,-1,-3 with multiplicities 1,15,15,1. All are nonzero. The two
C-charge ±2 roots have T=0. The joint C=T=0 root count is 72:
32 integer roots and 40 half-integer roots. The eight Cartans give
the algebra e6+u1+u1, before further holonomies.
This retains the familiar E7-to-E6 branching as finite algebra, not
an SM field assignment.

For a global constant normal spin field use the trivial spin line
S=O on the flat torus and set

    q0=v T, r0=0, v real.                            (2)

All Cartan Wilson holonomies commute with T. The literal half-period
boundary phases of the source matter modes can instead be carried
by exp(i pi C) on each cycle: it acts as -1 on C-charge-one matter
and +1 on the C-charge-two connection. This gives the same mode
boundary characters with S=O. It is a different spin/gauge allocation,
which must be carried on every field; no equivalence of full theories
is claimed merely from these shared three-point functions. The choice
of these holonomies and spin remains visible in the input account.

The family (2) is stationary in the same action. Dq0=0, [q0,q0†]=0,
and its moment is still B C. That moment is parallel and commutes
with q0, so the full first variation vanishes. Its energy is unchanged
as v varies. The kinetic norm of q0 is proportional to v² and positive;
v is an unfixed physical state amplitude, not a gauge convention.

## 2. The bosonic shift follows from the actual kinetic term

Let a be a transverse lowest negative connection mode in a root of
C-charge q_C and T-charge q_T. The flat-parent rewriting into real
scalars X_I has q0=(X1+i X2)/sqrt(2), hence X1=sqrt(2)v T.
The term one-half integral |D X1|² contributes
v² integral |[a_real,T]|². In the same one-half connection metric,
the resulting physical mass shift is 2v² q_T². Therefore

    m_a²=q_C B+2v² q_T².                            (3)

The mixed connection/spin derivative vanishes on these transverse
profiles: D†[a,T]=[D†a,T]=0 since T is parallel. The accompanying
scalar variations cannot cancel this shift by a longitudinal gauge
relabelling. This is a statement about these exhibited eigenmodes,
not a proof of nonlinear stability of the complete family.

Equations (1)-(3) show a permitted region 2v²>B where all 168
C-charge-minus-one negative modes acquire positive masses, while
the six C-charge-minus-two modes keep mass -2B. Thus a same-action
mechanism can isolate that most negative band at quadratic order.
No new positive contact term or 168 independent projectors is needed.
Neither the Cartan direction nor the inequality's amplitude is forced.
The six remaining modes still need their own nonlinear stationarity.

## 3. The same field also changes the fermion operator

It would be wrong to add (3) to the bosons and retain the earlier
three-mode fermion kernels unchanged. The actual mass map is in
weave_physical_mass_2026_10_08/PROOF.md: its superpotential Hessian,
gaugino coupling, trace-dual target and all four left Weyl slots
remain. The source identity M=Uout T_Hodge Uin does not require
zero D moment. The holomorphic complex still squares to zero at
(2), since Dbar q0=0 and [q0,r0]=0.

In a root of T-charge q_T its algebraic differential is the Koszul
differential with the nonzero scalar v q_T in one direction. Its
algebraic Hodge Laplacian is

    Delta_delta=|v q_T|² I

on all exterior degrees. The section q0 is parallel, so the mixed
Dolbeault/algebraic anticommutators vanish. With the parent's actual
metrics and its sqrt(2) differential normalization,

    ||M psi||²>=2|v q_T|² ||psi||².                  (4)

The same holds on the adjoint block. This is the parallel orthogonal
reduction already used in the source, now applied to a constant normal
Cartan field on the compact surface. No zero-dimensional symbol is
substituted for its global domain. The compact torus has no missing
end condition in this control.

Every flux-three root in (1) has nonzero q_T. Consequently its
previous fermionic zero modes are lifted for every v!=0. In particular
the two three-mode matter factors of the A2 vertex cannot still be
called three massless families while (2) is used to stabilize their
connection partners. Both effects come from one action and operator.
The zero-weight blocks and the six flux-six directions retain their
own kernel and nonlinear duties; no complete SM spectrum is asserted.

## 4. A scoped constraint for the next derivation

The same argument works for any collection of commuting normal,
parallel adjoint spin backgrounds in this flat compact construction.
On a root their gauge-Higgs mass is
2 sum_i |v_i q_i|². If it vanishes so that the original flux-three
fermion zero mode can survive this algebraic reduction, it also
leaves that root's negative connection mass -B unchanged. A Cartan
mass inserted into one operator alone would evade the actual action.

This is a constraint on that specific stabilizer class. Curved spin
connections, nonparallel coupled fields, physical ends/sources,
different holonomy/representation maps and quantum dynamics are
not excluded. They require a new calculation of the common fields,
norms and operator; none inherits (3) with (4) silently omitted.

The gain is constructive: the 168 modes need not force a universal
negative, and an explicit native stabilizer exists. Its spectrum
price prevents calling it an SM repair. The next valuable duty is
a derived stabilizing response that preserves the intended physical
chiral modes, with the full complementary spectrum retained. The
state amplitude and spin/gauge allocation are still supplied choices.
Foundational inputs removed remain zero. Vacuum selection, SM3 and
gravity remain open.
