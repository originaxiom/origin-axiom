# A sufficient register must preserve the law, not only the allowed maps

2026-11-18. Author hand continuation under `6941e2b1b`.
Not independently checked. No scientific code, CAS, enumeration, numerical
experiment or data comparison. This is a finite classical conditional
comparison; it is not adopted as a foundation for quantum physics.

## 1. Existing deterministic criterion and its new duty

AR1/AR2 already establish when updates and outputs descend through a
surjection q:X->Y. The primitive comparison already shows a register
can be needed because an admitted update exposes a discarded variable.
Those are reused results.

With probabilistic choice of updates there is another duty. Supplying
the same allowed maps and a deterministic quotient of each map does
not determine the probabilities of the next coarse outcome. If these
probabilities depend on a discarded variable, the reduced state is
insufficient for the same predictive law.

## 2. Exact criterion, with a direct proof

Let X and Y be finite sets, q:X->Y onto, and K(x,x') a stochastic
matrix on X. It acts on column functions by

    (K f)(x)=sum_(x') K(x,x') f(x').

A stochastic Kbar on Y obeys

    K(q^* F)=q^*(Kbar F) for every F:Y->R            (1)

if and only if, for every y', the quantity

    sum_(x':q(x')=y') K(x,x')                        (2)

depends on x only through q(x). Necessity follows by inserting the
indicator F=1_(y'). Conversely, define Kbar(y,y') by (2) using any
x with q(x)=y. The hypothesis makes it well-defined; nonnegativity
and unit row sums descend. Substituting an arbitrary F proves (1).
Surjectivity makes Kbar unique.

Induction gives K^n q^*=q^* Kbar^n for every n. This does more than
match one stationary distribution. For finite recorded sequences,
multiplication by each coarse outcome indicator also intertwines with
q^*. Composing those multiplication operators with K between observation
times proves equality of all the corresponding cylinder probabilities
for every initial distribution after pushforward by q. Thus the complete
finite coarse-outcome process is preserved under these stated tests.

This is standard strong lumpability for finite Markov chains, not a new
generic theorem. The direct proof above uses no eigenvalue assumptions.
Theorem 1 and equation (2.1) of Nilsson Jacobi and Gornerup,
*A dual eigenvector condition for strong lumpability of Markov chains*,
give the same block-transition criterion. Their introduction and main
result were personally read, including the separate diagonalizability
assumption of their spectral Theorem 2, which is not imported here.
[Primary paper](https://arxiv.org/html/0710.1986v2).

For supplied labeled updates T_a and one-step probabilities p_a(x),
the kernel is

    K(x,x')=sum_(a:T_a x=x') p_a(x).

Therefore the actual coarse-law test is

    sum_(a:q(T_a x)=y') p_a(x)
       is constant on every fibre of q.             (3)

Even when each q T_a descends separately, (3) need not hold.

## 3. An internal-register countercontrol using the old maps

Reuse X={(x,r):x,r in Z/2Z} and the already specified reversible maps

    V(x,r)=(x+1,r),  U(x,r)=(x,r+x),
    q(x,r)=x.                                       (4)

Both V and U descend through q, respectively to a flip and the identity.
The sole instantaneous readout x descends too. Every prescribed word
of these maps has an x outcome independent of the starting r, so the
old deterministic quotient is adequate for that controlled-word duty.

Now additionally supply a stochastic law

    p_V(x,r)=p_r, p_U(x,r)=1-p_r,
    0<p_0,p_1<1, p_0!=p_1.                          (5)

All finite label histories remain in the support. Nevertheless

    Pr[next coarse x = x+1 | complete state (x,r)]
           =p_r.                                   (6)

Two complete states with the same q have different next-outcome
probabilities. No Kbar satisfying (1) exists for every initial complete
state. The omitted register affects the predictive law; U also lets x
change r, so r is not merely an unrelated fixed label. This is an
explicit internal feedback model with supplied probabilities, not an
observer or physical interaction derived from the founding principle.

Opposite control: p_0=p_1=p gives the well-defined coarse matrix
with diagonal 1-p and off-diagonal p. The general condition admits a
proper sufficient quotient when the rates make it sufficient. It does
not require keeping every microscopic distinction.

The failure at unequal p does not contradict AR1/AR2. The uncontrolled,
state-dependent update selection in (5) is an additional operation of
the predictive model. It was not among the old controlled-word tests.
The definition of an adequate record must include the actual duties.

## 4. If the register records which act occurred, keep that instrument

If the labels a are themselves observed records, retaining only K is
not enough. Retain each instrument operator

    (K_a f)(x)=p_a(x) f(T_a x).                      (7)

For preservation of coarse outcomes and the same label records, require
K_a q^*=q^* Kbar_a for each a. Summing gives (1), but the converse
need not hold. Necessity again follows by indicator tests that also
fix the label. Sufficiency follows by composing the individual K_a
and coarse indicator multiplication operators along a recorded sequence.

An elementary opposite control is two differently labeled identity maps
with state-dependent probabilities summing to one. The unlabeled kernel
is always the identity, even when the label distribution depends on a
hidden register. A coarse description can then preserve all unlabeled
state observations and still lose the recorded act. If no physical
readout detects those labels, retaining them is not required by this
criterion. Observability has not been silently imposed on formal syntax.

## 5. Consequence for the architecture and physical bridge

A needed extra layer has an exact witness: two reduced-identical states
produce different admitted future-record distributions under the same
law. A sufficient reduction has an equally exact test, (1)-(3), or (7)
when act labels remain observable. These are tests after the law and
readouts are specified, not derivations of those choices.

The law can therefore be the place a registering relation was lost even
when every individual update was transported correctly. The converse
also matters: if (1) holds, the finite coarse-outcome predictions can be
retained without carrying the discarded coordinates. A larger register
is not automatically a more physical or a more economical explanation.

No failure of this finite classical control excludes the supplied E8
candidate or quantum theories. For the actual physics construction,
the corresponding duty is to derive its own fields, dynamics, norms,
readouts and complete domains and prove the appropriate transport.
This comparison does not substitute a Markov kernel for that action.
It sharpens the registering requirement without selecting Q8, E8, a
carrier, vacuum, three chiral families, gravity or qualia.
