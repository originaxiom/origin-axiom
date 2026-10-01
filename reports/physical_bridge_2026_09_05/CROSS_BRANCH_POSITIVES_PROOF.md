# R75 — independent algebra and the scope of its physical use

Pre-execution authored argument; October 1, 2026. Finite controls below
test identities, not global analytic or phenomenological acceptance.

Use the R42 literal matrices m,n. F has generators x=n m^-1 and
y=m n m^-2. Conjugation by m gives phi(x)=y, phi(y)=y X y y.
The boundary is lambda=y X Y x; phi fixes it as a reduced word.
For order-two characters the deck map (a,b)->(b,3b-a) cycles the three
nonzero pairs. Its third power fixes them. The cover group is
<x,y,z | z x Z=phi^3(x), z y Z=phi^3(y)>, z=m^3.

A left cocycle obeys c(uv)=c(u)+rho(u)c(v) and
c(u^-1)=-rho(u)^-1 c(u). Applying these identities letter by letter
builds c(phi(g)) directly. Multiplication by m^-1 makes it a cocycle
for the deck-transformed character. Compose three steps to obtain S.
For B(v)=((Vx-I)v,(Vy-I)v), S B=B m^-3. The latter is unipotent;
if B has rank4, its characteristic factor is (s-1)^4. The quotient
characteristic polynomial is therefore obtained by exact division.

The intended exact identity is

    P(q,s)=s^4-8s^3-(q^3+q^-3-16)s^2-8s+1.

At g(q)=q^6-34q^3+1, this is (s+1)^2(s^2-10s+1).
This factorization alone does NOT decide the Jordan block. The finite
field-extension calculation must distinguish nullities1,2,2,2 from
2,2,2,2. The (-1)-primary part intersects B trivially because B has
only eigenvalue1; its Jordan nullities in eight dimensions are thus
exactly the quotient nullities. Both positive roots of g correspond to
q^3=17+/-12sqrt2. Irreducibility and a Sturm positive-root count are
controls, not assumptions about every polynomial in the census.

Take c_F in ker(S+I), with Vz=-m^3 and c(z)=0. The cover cocycle
relations follow from S c_F=-c_F. W(g)=[[V(g),c(g)],[0,1]] is then
an actual determinant-one representation, not just a dimension label.
The code checks its relations again rather than relying on this argument.

For any representation on this finite presentation, the word Jacobian J
gives Z1=ker J and B1=im stacked(rho(g)-I). Restriction to the actual
commuting peripheral words z,lambda is a cochain matrix R. If Z is a
kernel basis, the rank in boundary cohomology is

    r1=rank([R Z, B_boundary])-rank(B_boundary).

This computes a0,a1,t0,t1,r1 independently; the dual gives
b0,b1,s0,s1,q1. I=(a1-r1)-(b1-q1) is cross-checked with
I=(a0-b0)+s0-r1 and r1+q1=t1. No finite-field approximation is used
in this bounded representative. Orbit equality additionally follows
from the peripheral-preserving deck automorphism; it is not a new
physical identification of separate backgrounds with generations.

Lambda has eigenvalues q,q,q,q^-3. The rank-five extension has the
additional eigenvalue1. Its exterior-square longitude has eigenvalues
q^2 and q^-2 (three each), q (three), q^-3 (one); none is1 for
q>0,q!=1. Thus this specified exterior torus complex is acyclic.
This does not classify every singular-end analytic operator domain;
R63/R74 already give the reason the quantifiers differ.

For the two-curve check put directed arrows around the square with
weights d1*c_plus*a_j, d1*c_minus*a_i on the 1–2/3–4 edges, and
d2*d_plus*b_j, d2*d_minus*b_i on 1–3/2–4. Expand its 4x4 determinant,
then set e1=-d1^2*c_plus*c_minus, e2=-d2^2*d_plus*d_minus. It equals

    e1^2*a1*a2*a3*a4 + e2^2*b1*b2*b3*b4
    -e1*e2*(a1*b2*a4*b3 + b1*a3*b4*a2).

At a1=a4=0, b1=b4=Y it reduces to
Y^2*(e2^2*b2*b3-e1*e2*a2*a3). This only certifies the first-order
hopping determinant algebra. The assertion that the actual curved
monodromy has these arrows belongs to B1444/B1445 and is not rerun by
this determinant. In particular neither normalization nor a physical
mass operator is derived here.

Finally apply R41's projector computation to W's invariant rank-four
subbundle, not to R40's different rank-four full flag. In an adapted
orthonormal frame let eta be the upper four-by-one block,
xi=5P-4I=diag(1,1,1,1,-4), Psi=(D+Ddagger)/2 and
A=(D-Ddagger)/2. Direct trace gives

    <Psi,d_A xi>=-(5/2)|eta|^2.

The diagonal blocks do not contribute to this pairing. On a complete
finite-volume base, finite Higgs energy and integrable source projection
allow R41's cutoff argument for I=-2d_A^*Psi=S to give

    integral tr(xi S)=5 integral |eta|^2.

If S=0 and there is no boundary flux, eta vanishes, giving a flat
orthogonal complement and contradicting a nonsplit extension class.
Thus the harmonic metric of the split background cannot be silently
assigned to this nonsplit W. Sources or admitted end flux can change
the balance; a two-sided deformation can remove the invariant subbundle.
Neither option is excluded here. There is no universal chirality kill.
