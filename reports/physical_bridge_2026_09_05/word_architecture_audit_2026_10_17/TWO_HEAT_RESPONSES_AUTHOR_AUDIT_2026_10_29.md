# Author audit: full relative heat reduction

October 29, 2026. UNREVIEWED author hand audit of the proof shared at
3596d5bef. This is neither independent review nor execution of new
scientific controls. Preserve that checkpoint and its original custody
hash. This supplement makes its intermediate checks and general-character
formula explicit; it does not replace a source with a retroactive seal.

## 1. Operator normalization, checked directly

Use the same B_a, K_a^0, K_a^1 and complete form realizations as the
parent note. In a uniformizing chart Omega=1/y, integration against the
displayed section/form densities gives

    B_a^dagger = -y^(2-a) D_z y^a,
    K_a^0 = -y^2 Delta + i a y D_bar.

Here a locally parallel frame removes only the flat charge connection;
it does not remove the spin-power metric. Thus

    J_a K_a^1 J_a^-1
      = -y^2 D_bar y^(2-a) D_z y^(a-2)
      = -y^2 Delta + i(a-2)y D_bar + (a-2)
      = K_(a-2)^0 + (a-2).

The norm check is equally necessary:

    Omega^(4-a) |Omega^-2 g|^2 = Omega^-a |g|^2.

It fixes J_a, including its power of Omega. The Serre map has the
separate norm check

    Omega^a |Omega^-a conjugate(g)|^2 = Omega^-a |g|^2.

Conjugating the ordered differential expression by that antiunitary
gives K_(2-a)^0 on the conjugate flat line. No transpose is substituted
for an adjoint. These are identities on the actual weighted spaces,
not assertions about coefficients on a flat measure.

The source's complete Dirac cutoffs, common compact-support cores and
closures remain load-bearing. Unitarity alone would not establish the
operator relation if a different wall realization were assigned to its
two sides. This note supplies no such change of domain.

## 2. What the relative index theorem actually supplies

The source theorem was re-read at Lesch, dg-ga/9607005, III section 3.5,
in particular Definition 3.5.6, Proposition 3.5.7 and Theorem 3.5.8:
https://arxiv.org/pdf/dg-ga/9607005 (accessed October 29).
It relates the relative graded heat integral to an index difference for
the stated Fredholm pair, with the regularity and same-end hypotheses.
It does not make an individual infinite-volume heat operator trace class.

Our application still owes the hypotheses proved in the preceding
authored heat-existence note: complete selfadjoint realizations, bounded
propagation, compact comparison-region estimates, identical ends,
trace-class differences and the gapped infrared bounds. The compact-core
flat interpolation preserves the Fredholm index on its fixed graph
domain. Under these hypotheses the relative graded trace is zero.
This is the justification for replacing a relative form trace by its
relative section trace; cancellation of two divergent absolute traces
would not justify that step.

Independent scrutiny of these infinite-dimensional hypotheses remains
more important than rechecking the short finite polynomial table.

## 3. Count the scalar slots before cancelling them

Recover P_c = H^dagger H + d d^dagger and P_v = d^dagger d from the
same-action real-gauge proof. The compact-real vector, complex FP pair,
gaugino and three chiral slots give the physical weights +1 and -3.
These weights do not follow from the cochain index.

At R=0 the paired A_m/Q_(m+1) block is the normalized complex with
d0=(B_(-m),-k_m), d1=(k_m,B_(-m)), up to constant unitary phases.
The W Hessian acting on R_m gives K_(1-m)^0+k_m^2; its potential
coefficient agrees with k_m^2=(j-m)(j+m+1)/2 because the C2 t-slot
has density 2 and the principal Q is E_raise/2. The source's factor
sqrt(2) in d is retained. No C3 bookkeeping slot becomes matter.

After the relative partner identity, write

    V = sum_(m=-j)^j exp(-s k_m^2) F_(-m),
    A = V,
    Q = V - F_(-j) + F_(j+1),
    R = sum_(m=-j)^j exp(-s k_m^2) F_(1-m).

Therefore A+Q+R-3V is exactly equation (10) of the parent note.
For m and -m-1, the raising mass squares agree and duality reverses
the difference of F's. There is no integer fixed point of this pairing.
The unmatched m=j gives a second copy of the extreme difference:

    Phi_j = 2(F_(j+1)-F_(-j)).

This check retains the massive spectrum until the physical cancellation.
It does not infer a one-loop cancellation from contractible cohomology.
For j=0 it separately recovers A+Q+R-3V=2(O-E). For j=1 it gives
2(E-exp(-s)O), whose infrared limit is the known relative chiral jump
2[delta(L)-1]. The j>=2 relative infrared limits vanish, consistently
with their source kernel counts independent of the flat line.

## 4. Make the unspecialized charge formula explicit

The earlier equation (12) is SPECIALIZED to the order-seven source
line. In particular T_4=T_3 and T_6=T_1 cannot be used for an arbitrary
unitary character. Here is the formula before any such identification.
Use T_q=Phi_2(q), Psi_q=Phi_1(q)+Phi_3(q), and the already-derived
evenness in q. The recovered charge/index table gives

    B21 = (2/5)(Psi_3-Psi_2)
            + (2/5)(7T_1-4T_4-3T_6) - 2 Phi_0(5),

    B31 = (3/5)(Psi_2-Psi_3)
            + (1/5)(9T_1-3T_4-6T_6) - 3 Phi_0(5).

The Psi terms come from the two conjugate gauge-five sectors with
structure V1+V3. The T terms come from the two gauge-ten sectors with
structure V2. The single gauge adjoint supplies Phi_0. This distinction
prevents confusion between a gauge representation and its structure
module. The trace roster is not doubled again after these coefficients.

Consequently, for a general peripheral-trivial unitary line,

    B_C = B31 - (3/2) B21
        = (6/5)(Psi_2-Psi_3)
           + (9/5)T_4 + (3/5)T_6 - (12/5)T_1.

The full gauge-adjoint response cancels. Taking the infrared limit
using Phi_1(q) -> 2[delta(L^q)-1] and Phi_j(q) -> 0 for j>=2 gives

    h_C = (12/5)[delta(L^2)-delta(L^3)].

This establishes the general formula without exporting a sevenfold
shortcut. It retains the +12/5 order-two and -12/5 order-three cases.
For the order-seven source state all nonzero powers here are
nonexceptional, and the parent note's formula is recovered. At a
central gauge holonomy, responses coincide within each complete SU5
representation and both inserted differences vanish, even when the
common central line is not trivial.

## 5. The dependency reduction and its limits

When h_C=0, the stated ultraviolet and gapped infrared bounds make
-integral B_C(s) ds/s convergent. A common rescaling replaces B_C(s)
by B_C(c s); changing variables removes c. A matching switch enters
only multiplied by h_C, so that dependency also disappears.

This constructs a one-loop invariant combination using the model's
derived running. Constructing such combinations is a standard possibility;
the existence of one is not itself a predicted value or a foundational
breakthrough. The common scale remains necessary for other observables.
Independent local kinetic deformations, extra end matter, a different
light EFT or supersymmetry breaking are not eliminated by this argument.
They would need a same-action derivation before comparison.

There is also a necessary full-family countercontrol. The same admitted
parallel phase permits order-two and order-three noncentral characters;
their two defining gauge eigenblocks are distinct, so they need not
restore SU5. A single fixed combination u B21+v B31 cannot remove the
common scale for EVERY spin and EVERY admitted character. Two members
already test that proposed strengthening:

* Nontrivial extending spin, order-seven line: (h21,h31)=(-4,-6).
* Trivial extending spin, nontrivial order-two line:
  Phi_0 has zero infrared limit and (h21,h31)=(-4/5,6/5).

These vectors are linearly independent (determinant -48/5). Thus only
u=v=0 kills both. This does not retract C on the nonexceptional family,
select a spin or exclude another physical construction. It prevents a
generic-state conditional reduction from being advertised as a universal
elimination of the scale across the whole admitted phase family. The
second vector follows from the unspecialized formula above; an order-seven
alias would give the wrong answer here.

The six E/O evaluations are unknown spectral functions of supplied
geometry, spin and Wilson state. They are not adjustable constants,
and replacing many determined operators by two families does not lower
the number of independent foundational premises. That count is unchanged.

## 6. Present verification status

The recurrence, unitary norms, physical slot accounting and finite charge
coefficients above were re-derived by hand against the cited source
operators. No new CAS, scientific test, determinant solver, numerical
prediction or empirical comparison was run. The original proof/source
hashes were checked as metadata and preserved. This is an AUTHOR audit.
Main's separate non-authoring review is requested in the pushed relay;
no independent acceptance of this new proof is claimed. P210's review
and its still-unrun arithmetic checks do not certify this successor.

The independent review should prioritize the global heat/domain argument
and its identification with the real physical Hessians, then use these
finite formulas as controls. Until that review, no result here is banked
and no input is marked removed from the foundational ledger.
