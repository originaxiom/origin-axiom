# Conditional nonlinear action with its registering relation retained

Authored before execution; standard symplectic/discrete-variational
mathematics applied to the declared genesis moves. Independent analytic
review remains owed. R28 already corrects the broad no-action claim.

## 1. Data, conventions and full moves

Use FULL traces x=tr A,y=tr B,z=tr AB, not the half traces of B37.
K=x^2+y^2+z^2-xyz=kappa+2; the fiber's parabolic leaf is K=0.
The Poisson bivector has entries Pxy=2z-xy,Pyz=2x-yz,Pzx=2y-zx.
On a regular chart its inverse leaf form is omega=dx wedge dy/(2z-xy),
up to the conventional overall sign; we FIX this displayed convention.
The source of that normalization is the retained Goldman invariant
trace pairing, not a measured action unit. B21/B448 bank this dictionary.

Word automorphisms L:(a,b)->(a,ab), R:(a,b)->(ab,b), P:(a,b)->(b,a)
act by the trace substitutions

    fL=(x,z,xz-y), fR=(z,y,yz-x), fP=(y,x,z).

These are PULLBACK operations: f_(MN)=f_N composed with f_M. Thus
T=fP composed with fL=(z,x,xz-y) corresponds to LP, not PL, and
T^2=fR composed with fL corresponds to LR. All maps preserve K;
fL/fR preserve the Poisson structure, fP reverses it. The inverse
maps are literal inverse substitutions. Native checks retain all
three bivector components, not only one convenient bracket.

For a surface realization, Goldman's cup-product pairing changes sign
with the surface orientation. Thus any admitted word/group element g
with orientation character epsilon(g) transports omega by epsilon(g).
The extension beyond the checked generators follows by composition,
not a finite-word census. The grammar's physical legality/carrier is
still supplied; no PF1-PF3 implication is proved here.

## 2. The minimal sign register and the safe quotient

Let the tracked state be (p,s), s=+/-1, with Omega_s=s omega and
update ghat(p,s)=(g.p,epsilon(g)s). Then

    ghat^*Omega = epsilon(g)s * g^*omega = s omega.

Its composition law retains the determinant character, including all
orientation-negative moves rather than deleting them. The register has
two values because epsilon has image C2; for a nonzero form f(s)omega
its transport law requires f(-s)=-f(s). One fixed nonzero scalar form
cannot satisfy this particular anti-symplectic map's same-form condition.
This is minimal for THIS ordinary-form lift, not a theorem that nature's
observer has one bit or that other enlargements/domains are impossible.

Projection (p,s)->p DOES descend the updates: T remains a perfectly
valid anti-symplectic map. But the deck exchange s->-s sends Omega to
-Omega, so Omega is not basic as an ordinary scalar-valued form. If the
quotient retains the orientation coefficient line, the line-valued form
is well defined. Thus the precise loss is a variational output/type,
not a failure of the underlying dynamics. This is ACT_REGISTER AR1
applied to tensor data, with the safe typed alternative kept.

Initial sign is a choice of frame; changing it negates the classical
action and leaves its stationarity equations unchanged. This does not
derive self-signing, a Born probability or a quantum phase convention.

## 3. A Darboux chart on the NONLINEAR parabolic leaf

Put q>0,p real and write c=cosh(q),u=sinh(q):

    x=2c, y=2(c/u)cosh(p), z=2(c/u)cosh(p+q).

Direct substitution gives K=0. The pullback of omega is dq wedge dp
where the displayed x,y projection is regular; it extends across
p=0 using another leaf chart. This is NOT the K=4 abelian leaf whose
half-step is Fibonacci in linear coordinates. r=exp(q),b=exp(p) makes
all three displayed coordinates rational, permitting exact checks.

To express T in (q,Q), let v=sinh(Q),C=cosh(Q),

    Delta=u^2 v^2-1, h=sqrt(Delta),
    a=(C u+h)/c, b=(c v+h)/C,
    p(q,Q)=log(a)-q, P(q,Q)=log(b).

On the real branch q,Q>0,Delta>0 take h>0 and real logs. Then p+q>0,
P>0. Reconstructing (x,y,z) above and the target chart (Q,P) gives
EXACTLY (z,x,xz-y), in all three coordinates. The second square-root
branch is also legitimate if used consistently; mixing branches is not.
The formulas analytically continue on any small simply connected complex
chart with nonzero c,C,u,v,h and nonzero log arguments, using matched
local logs. This is a LOCAL action, not a global branch-free function.

The cross derivatives are

    partial_Q p = partial_q P = u v/h,

nonzero in this chart. The proof is rational differentiation with
c^2-u^2=C^2-v^2=1,h^2=u^2v^2-1. These are the exact polynomial identities
tested by the native producer; finite real evaluations do not replace
the holomorphic/local branch argument. Hence p dq+P dQ is closed.

On a rectangle about q0=Q0=log(3), define

    F(q,Q)=integral_(q0)^q p(t,Q0)dt + integral_(Q0)^Q P(q,t)dt.

Then F_q=p,F_Q=P, and F_qQ=uv/h is nonzero. The basepoint changes an
additive constant, not the map or a vacuum selector. On complex local
charts the same primitive exists by the holomorphic Poincare lemma.
No global period, exactness, singular crossing or quantum contour is
claimed. This explicit construction is stronger than assigning a
multiplier action to an arbitrary recurrence, but not a spacetime theory.

## 4. The actual stationary action and its first variation

For consecutive lifted half-steps s_(n+1)=-s_n, set

    L_s(q,Q)=-s F(q,Q), S=sum_n L_(s_n)(q_n,q_(n+1)).

The canonical momentum on sheet s is r=s p. The type-I discrete
Legendre equations r=-partial_q L_s=s p and R=partial_Q L_s=-s P
are exactly the target momentum on sheet -s. Interior stationarity is

    partial_2 L_(-s)(q_prev,q)+partial_1 L_s(q,q_next)
      = s (P_prev-p_next)=0.

This glues the nonlinear maps, not just the values of a static invariant.
Its regular mixed derivative is -s uv/h. Keeping s fixed instead gives
a sum of momenta and fails the same orbit. For two steps the eliminated
intermediate generating function is -s F(q,Q)+s F(Q,R), stationary in Q;
it generates T^2 on the original sheet whenever the local elimination is
nondegenerate. No global elimination or positive minimum is asserted.

Discrete generating functions and the DEL boundary signs are standard
Marsden-West section1.3 mathematics. The two-sheet lift is autonomous
with respect to its declared discrete register; expressed on the base
alone its Lagrangian is period-two/time-dependent. Both preserve R28's
scope qualification of B1341. They do not erase that autonomous same-
state real regular DEL maps preserve an ordinary area form.

## 5. Retain the actual nonreal monodromy-fixed characters

Let x=(3+i sqrt(3))/2,y=z=(3-i sqrt(3))/2, or their conjugates. Then
K=0,T exchanges them,T^2 fixes them; x^2-3x+3=0 and xy=3. B448 already
identifies this pair with the complete discrete-faithful restriction.
Here the exact orbit is rechecked, NOT its discreteness or every lift.

The leaf is regular: grad K is nonzero and 2z-xy=+/-i sqrt(3).
With cosh(q)=x/2,cosh(Q)=z/2 the discriminant is Delta=-3/16, NOT zero.
For the first point the compatible h is i sqrt(3)/4, since the old
y=2cC-2h. The other matched branch gives the other possible old y;
silently mixing it with the prescribed point is rejected. Thus the local
holomorphic variational chart reaches neighborhoods of BOTH geometric
characters. It is not only a real Markov illustration.

DT^2 at either point has a unit eigenvalue in the full three-dimensional
space (K is conserved). The exact characteristic polynomial is
(t-1)(t^2-5t+1); the restriction to the regular two-dimensional leaf is
t^2-5t+1, since the nonunit eigenvectors lie in ker dK. This is a
dynamical derivative, NOT the golden record matrix's spectrum or a
physical mass/kinetic matrix. The singular fixed origin fails the leaf
regularity assumptions; it cannot silently stand for this pair.

## 6. How far this moves the physics goal

The supplied genesis dynamics can retain a minimal orientation relation
and a regular LOCAL nonlinear variational structure without forcing the
orientation-preserving sector by action existence alone. The mathematically
reversing state remains in the declared architecture. Canonical SE2 is
still CHOSEN; whether the register is physically generated remains FK12.

This pays one action/register compatibility duty. It does NOT transport
F into the R93 E8 field functional, select the SM cocharacter/phase,
generate a fermion end law/source, or derive a quantum state. R93's
conditional admitted SM gauge phase, paired charged modes and light
moduli remain. FK8/FK10/FK11 need an ACTUAL common map, not shared labels.
No parameter prediction, gravity, full SM/TOE or qualia is obtained.
