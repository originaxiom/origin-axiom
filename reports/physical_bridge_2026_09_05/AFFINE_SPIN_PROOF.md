# Affine transport proof and exact failable fixtures (R92)

This is a pre-run handwritten argument with disclosed expected results,
not a first-run certificate. Supplied actions, not a manifold realization.

## 1. Keep the registering relation, not just its sign

For a fixed homomorphism into PSL2(C), two SL2(C) lifts differ by a
central sign character epsilon: the central quotient of their values
is multiplicative. Conversely multiplying a lift by any character gives
a lift. This constructs the lift torsor, whenever a lift exists.

Let sigma be an automorphism and rho(sigma g) be conjugate to
chi_sigma(g) rho(g). For a twist epsilon_x, pullback along sigma sends
its label to epsilon_x composed with sigma, times chi_sigma. Thus the
linear action on characters must accompany the sign defect. Reversing
isometries use conjugate rho; real central signs behave identically.
Pullbacks reverse the automorphism composition order. To avoid hiding
that convention, the fixture uses LEFT MAP composition explicitly:

T_g(x)=A_g x+b_g; T_(g h)=T_g composed with T_h,
A_(g h)=A_g A_h, b_(g h)=b_g+A_g b_h.

Changing origin by u gives b'_g=b_g+(A_g+I)u. The true orbits transform
covariantly. Treating b_g alone as a homomorphism drops the registering
action A_g. In particular the set {b_h:h in H} of preserving defects
is an ORBIT of0, not in general a subgroup of the additive character
space. A generating set of H does not make its raw defects generators
of that orbit under addition. Both are separate coverage statements.

For a fixed reverser r and the complete preserving subgroup H,
reverse labels of0 are {b_r+A_r b_h:h in H}. Actual FIX at the chosen
origin iff this set contains0. For arbitrary spin label x, a reversing
element fixes it iff (I+A_g)x=b_g. Enumerate the FULL reversing set
or earn a complete generating/action argument before a universal claim.

If every A_h=I, preserving defects form a subgroup K. Normality of H
in the tagged group implies A_r K=K; then the reverse orbit is b_r+K.
More generally an ordinary-coset replacement needs a proof that the
actual preserving orbit is exactly the proposed subgroup and that
the relevant linear action preserves it. Nontrivial A alone does not
disprove that replacement; one control below deliberately keeps it valid.

## 2. Exact counterfixture: an orbit is not its additive span

V=F2^3, S={0,e1,e2,e3}, d=e1+e2+e3. Define p by cycling the basis,
and q by translation e1 after the linear map with columns
(e1,e1+e3,e1+e2). On S, p=(e1 e2 e3), q=(0 e1)(e2 e3).
Their restrictions generate A4; four affine-independent points determine
an affine map, so restriction is faithful and |H|12. Both linear parts
fix d. Translation r by d commutes with both generators, lies outside H,
and supplies the declared reversing tag; full group H times C2 has24.

H's orbit of0 is S, whose additive span is V. The reverse orbit is
S+d={d,e2+e3,e1+e3,e1+e2}; it misses0. Replacing S by its additive
span gives V and falsely includes0 in d+V. Thus the shortcut gives
false FIX even with COMPLETE group coverage and exact arithmetic.
For p after q, b_(p q)=e2 whereas b_p+b_q=e1: concrete failure of
the untwisted product rule. This is NOT a claimed isometry group/spin
action of any actual member. Actual additional hypotheses may exclude it.

Rebase at all eight u and solve fixed equations with both elimination
and exhaustive point action. Opposite translation and subgroup-orbit
controls prevent turning this counterexample into an overwide negative.
A separate incomplete-sample fixture illustrates a false SWAP, not an
observation of a missed isometry on main.

## 3. Parent group versus torsion-free member lift

O3 contains Z. S=((0,-1),(1,0)) belongs SL2(O3), S^2=-I and S is not
scalar. Its image in PSL2(O3) has order2; its preimage is {S,-S}, both
with square -I. A homomorphic section would have to send its order-two
generator to an element with square I, impossible. Therefore the usual
central extension SL2(O3) -> PSL2(O3) does not split. This is a standard
central-extension fact, not a novel no-physics theorem.

R=((0,-1),(1,-1)) instead has R^3=I and projective order3. Mapping C3
to its powers is a homomorphic lift. Odd-order torsion is not the same
obstruction. Culler Theorem3.1 and Corollary2.3 agree with these controls.
No claim that each manifold lacks a lift: torsion-free lattice subgroups
do lift. No claim that the CENTRAL EXTENSION cannot be kept as part of
the generated architecture. That alternative is the positive retained
route; physical fermions and descent/join conditions are still unearned.

## 4. Physics boundary

An orientation-odd spin-dependent invariant can evade the m004-only
collapse if the full pair (M,s), rather than M alone, lacks the relevant
fixing mirror. B1475 already registered the correct affine fixed equation.
Nothing here derives a common physical Dirac domain, local interactions,
three generations, anomaly freedom on one configuration, normalized
couplings, gravity, quantum probabilities, qualia or any SM value.
SM degree45 capacity is credited at READING grade only. Capacity is
not a realized index, and the reported pulled-back class remains(0,0).
