# Fourth-root characters recover an exact register bridge

2026-11-09. AUTHOR HAND DERIVATION, UNREVIEWED. No scientific imports,
CAS, enumeration, collection, tests or numerical runs. Sources are the
existing affine D4 and discriminant-cover arguments at physical baseline
b44cdbf646aaab6a275fbac805ee3684279435d4, and AGY's new register argument
at1c6c03333525236886990ac4dc292e74e323936b. This is a conditional
mathematical connection within those specified registers. It supplies
neither a physical field assignment nor three chiral generations.

## 1. Reuse and the exclusion under review

AFFINE_DOUBLET_KERNEL_D4_AND_PARITY_2026_11_08.md already proves the
translation lattice and actual move-induced triality. The companion
DISCRIMINANT_COVER_PERIPHERAL_AND_ORDER_THREE_WILSON_2026_11_08.md already
types its cover, characters, peripheral signs and deck-plus-move action.
Their positive results are reused, including the distinction between
the complete lifted module and its three unsigned labels.

AGY REGISTER_TO_GRADING.md section5 correctly observes that sign
characters of F=F(a,b) restrict trivially to N=ker(rho), but concludes
that no nontrivial discriminant character extends to ANY one-dimensional
character of F. Its argument does not cover fourth-root-valued characters.
In fact all three extend. This repairs a false exclusion without
identifying different full modules merely from their character labels.

Let A=rho(a), B=rho(b), A B=-B A, and A^2=B^2=-I. The known data are

    P_(uv)=P_u+rho(u)P_v, P_a=0, P_b=I,
    N=normal closure of r1=a^4, r2=a^2 b^-2, r3=b^-1 a b a,
    P_r1=0, P_r2=-(I+B), P_r3=B+A B,
    L=P(N)=D4, 2L*=2Z^4 union (2Z+1)^4,
    Kd=(P|_N)^-1(2L*), Adisc=N/Kd=L/(2L*)=(Z/2)^2.

Write d2,d3 for the classes of r2,r3. Their mod-two representatives are
(1,0,1,0) and (0,0,1,1), independent modulo (1,1,1,1), so they generate
Adisc. They are core words, not spatial puncture loops.

## 2. Check the conjugation control needed for extension

The conjugation law is P_(h n h^-1)=rho(h)P_n for n in N. The Q8
action on Adisc is trivial. It suffices to check A,B on the two generators
I+B and B+A B. The differences are

    A(I+B)-(I+B)=(-1,1,-1,1),
    B(I+B)-(I+B)=(-2,0,0,0),
    A(B+A B)-(B+A B)=(0,0,-2,0),
    B(B+A B)-(B+A B)=(-1,1,-1,-1).

Every difference is in 2L*. Thus every discriminant character psi is
invariant under F-conjugation on N. Normal generation by r1,r2,r3 may
therefore be used to verify equality of restrictions on ALL of N.

## 3. Explicit extensions and the all-word bridge

For r,s in Z/4, define the word character

    lambda_(r,s)(a)=i^r, lambda_(r,s)(b)=i^s.

Its values on the normal generators are

    lambda(r1)=1,
    lambda(r2)=(-1)^(r-s), lambda(r3)=(-1)^r.

In the old ordered discriminant-character basis the two sign tables are
D2=(-1,+1,-1), D3=(+1,-1,-1). Hence the three explicit extensions are

| discriminant character | psi(d2) | psi(d3) | lambda(a) | lambda(b) | lambda^2 on (a,b) |
|---|---|---|---|---|---|
| psi1 | -1 | +1 | 1 | i | (+1,-1) |
| psi2 | +1 | -1 | i | i | (-1,-1) |
| psi3 | -1 | -1 | i | 1 | (-1,+1) |

The restrictions agree on all conjugates of the normal generators, so
lambda|_N=psi. In particular each lambda is trivial on Kd and is an
actual character of the same order-32 word quotient, with no new carrier
or continuous phase fitted. Multiplying by any of the four parity
characters gives the four extensions of that same psi. They have order
four, and their squares give the same nontrivial parity character.

More intrinsically put X4=Hom(F,mu4), X2=Hom(F,mu2), with mu_m the
m-th roots of unity. Restriction gives the exact sequence

    1 -> X2 -> X4 --res_N--> Adisc_hat -> 1.

Surjectivity follows from the table. Its kernel consists of characters
factoring through Q8, whose abelianization is (Z/2)^2, hence exactly X2.
Squaring on X4 has the SAME kernel and is onto X2. It therefore induces
the canonical isomorphism

    J: Adisc_hat -> X2,
    J(psi)=lambda^2 for ANY extension res_N(lambda)=psi.

The answer is independent of the extension because multiplying lambda
by a sign character does not change its square. This includes the zero
character and bijects the three nontrivial labels.

The old move-induced lattice maps preserve Kd, so the full admitted
word action acts on every term. Left transport is precomposition with
phi^-1. Restriction and squaring commute with this action. Consequently
J is E-equivariant for ALL admitted composites, not only two matching
generator permutations. The central lift epsilon acts trivially on
these label sets. This does not suppress its nontrivial action on other
registered modules.

The order-32 extension by Adisc can remain nonsplit. Nonsplitting a
group extension does not prohibit extending its particular characters.
Ind_N^F(psi) still has dimension eight. That fact does not exclude the
one-dimensional extensions just constructed.

## 4. What is connected, and what is still missing

The character labels are now joined through actual restriction and
squaring, with the full word action. The larger coefficient range is
derived as a representation of the existing quotient. Its use as a
physical transport law is a separate map, with all fields and norms.

This is not an isomorphism of the complete cohomology and discriminant
modules. Native inner lifts J_n for n in N act trivially on the former,
whereas discriminant deck translations act nontrivially on its three
character lines. A physical identification must specify which action
is intertwined and how deck, inner, central and coefficient phases are
transported. Nor does the existence of four extensions select one of
them as a state or justify dropping any companion.

All spatial cusp loops h[a,b]^2 h^-1 have trivial lambda since lambda is
abelian. The original discriminant cusp control therefore survives.
There is no new boundary condition or chiral projection here. No canonical
physical input is marked paid. The recovered result is a constructive
register bridge that the sign-only exclusion would have missed.

## 5. Correct the coherent physical word products before using this bridge

Keep the physical notation separate from the quaternion A,B above. In
the supplied physical construction put X=A h, Y=D X and z=K_pi=D^2.
For every coherent h, the existing source relations give

    X^2=z, D^4=1, X D X^-1=D^-1.

It follows exactly that

    Y^2=z, X Y=D^-1 X^2=D,
    (X Y)^2=z=Zeta P, [X,Y]=D^-2=z.

Thus the coherent physical images have the Q8 relations, and their
map factors through rho. In particular K_h(N)=1. The BARE lift instead
has (A B)^2=P. Copying that equation into the corrected lift loses Zeta
on all 128 half-root directions. Git history places that copied equation
in the new REGISTER_TO_GRADING.md, not the earlier phase proof. It
changes neither the established commutator nor the shared cusp law.

For L:a->a,b->ab, actual left marking transport is

    K_h composed L^-1 : (a,b) -> (X,X^-1 Y)=(X,D^-1),
    K_h composed R^-1 : (a,b) -> (X Y^-1,Y)=(D^-1,Y).

The orientation vector (1,1) maps DIRECTLY by L to (1,0) and DIRECTLY
by R to (0,1). R fixes (1,0); the chain (1,1)->L(1,0)->R(0,1)
is incorrect. The zero-orbit versus three-orbit classification remains.

Factoring the coherent gauge/flavour data through rho does not erase
the full register or forbid another sector detecting N. The characters
in section3 are explicit possible detectors of the discarded data. Their
interaction with a physical sector, beyond this representation-theoretic
map, is an open earning duty. This is a scoped information comparison,
not a universal exclusion or a claim that an order-four line is matter.
