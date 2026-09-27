# Authored admission proof, not a chirality result

## 1. Which connected group?

Use the literal regular (SU5_g x SU5_s)/mu5 subgroup of compact E8.
Its kernel, checked on every adjoint weight, is (z,z^-2). E8's adjoint
is faithful since its center is trivial. For h(x)=diag(x^-2 three times,
x^3 twice), send (s,x) in SU5_s x U1 to [(h(x),s)]. If its image is the
identity, h(x) is scalar, so x^5=1, and s=x^-1 I. Conversely these five
pairs act trivially on every parent slot. The kernel is exactly mu5.

The map (s,x)->x s identifies this quotient with U5: every V in U5 has
a pointwise fifth root x of det V and s=x^-1 V in SU5, with precisely
that kernel. These pointwise roots need not be globally multiplicative.
The same construction over C gives GL5; determinant-unitary V keeps the
extra U1 transport compact, with trace-free noncompact Higgs if present.

The literal root check gives 20 commuting roots and a 5-dimensional
commuting Cartan when SU3, SU2 AND Y must commute. The roots are exactly
the structure A4. Thus the embedded connected U5 has the entire centralizer
Lie algebra and equals its identity component. We make no claim about
disconnected components. Omitting Y gives ten additional roots (the e
slot and its dual), a different centralizer of dimension 35.

## 2. Global coefficient dictionary

For every E8 weight, let s_i be its four structure Dynkin labels and q
its integral hypercharge. Its GL5 weight n satisfies

    n_i - n_(i+1) = s_i,        sum_i n_i = q.

The solution is integral exactly because of the common kernel. Check
this for all 248 weights, including Cartan multiplicities. In particular

    Q = V;                       u = V (det V)^-1;
    e = V det V;                 d = Lambda2 V;
    lepton = Lambda2 V (det V)^-1.

Actual opposite parent weights supply actual dual coefficients. The
off-diagonal gauge (3,2) slots carry det(V)^-1 and det(V). The structure
adjoint is End0 V. These describe a single parent representation, not
independently chosen lines for separate particles. A wrong determinant
power must fail the exact weight comparison.

## 3. The flat-lift condition

For ANY group Gamma and representation V:Gamma->GL5(C), a decomposition
V=E L with honest representations E:Gamma->SL5(C) and L:Gamma->C* exists
iff the determinant CHARACTER delta=det V has a fifth-root character.
Necessity follows by determinants; sufficiency is E=V L^-1. If delta is
unitary and a root exists, every such root is unitary, since |L|^5=1.
The choices form a torsor under Hom(Gamma,mu5), not a selected root.

This is a lift of a specified REDUCTION/flat representation. It is not
a classification of principal E8 bundle topology. A nonliftable reduction
can live inside a topologically trivial parent bundle.

On marked M6 let g0=mu and g1,...,g6 be the other Schreier generators.
Their free abelian coefficients are f=(1,0,0,0,0,0,1). Replace g_j by
g_j mu^-f_j in abelianization. The remaining relation matrix A is the
cyclic matrix with -3 on the diagonal and +1 at the neighbors. Its Smith
factors are (1,1,1,1,8,40); the producer independently verifies A and f.
Therefore Hom(Gamma,U1) = U1 x Z8 x Z40 in this splitting. The free U1
always has a fifth root. The fifth-power map on the finite factor has
kernel of order 5 and image of order 64, hence five obstruction classes.
Equivalently, the quotient of the CHARACTER GROUP by fifth powers has
order five. This is not five vacua, five generations or five E8 bundles.

The preferred longitude has zero exponent vector, so EVERY determinant
character is trivial on it. Enumerate all 320 torsion characters from
A^-1 columns; test the 64-element fifth image and each fiber/coset.

## 4. A real existence witness, and what it does not solve

Pick a torsion character delta outside the fifth image, with delta(mu)=1.
Then V(g)=diag(delta(g),1,1,1,1) is an honest U5 representation, satisfies
all group relators and embeds into compact E8 preserving the chosen SM.
Its determinant is delta, so it has NO honest SL5-times-line lift. Powers
of a representative generating the order-five OBSTRUCTION QUOTIENT cover
every obstruction class; the character itself need not have order five.
The producer returns an explicit phase vector and verifies all statements
on the marked words, including the peripheral pair.

It is globally flat unitary: choose its parallel positive metric and
Psi=0. Curvature and moment residuals vanish, and the background Higgs
norm is zero. This construction requires no harmonic-map existence
theorem. It does not promise an EXACT SM centralizer or physical selection.

For any unitary flat coefficient, the parallel Hermitian metric gives an
ANTILINEAR identification with its actual dual, intertwining the real
de Rham operator, positive norm and complete min/max domains. Thus the
normalizable harmonic dimensions in matching degrees agree, as do ordinary
interior dimensions. All five displayed coefficients of this unitary
witness are unitary. Their net chiral differences vanish in this supplied
linear prescription, without computing their separate mode numbers.
This says nothing about nonunitary deformations of the same lift sector,
singular sources, changed end domains or quantum mirror removal.

## 5. Why another scalar scan is not the next computation

If V and an honest SL5 E have conjugate projectivizations, choose the
conjugator once and write V(g)=c(g)E(g). Multiplication forces c to be a
character, so det V=c^5 and the combined lift exists. Conversely a
decomposition plainly gives the same projectivization. Thus every V
with the same projective representation as one of the already studied
honest E(t)'s is liftable. Scalar twisting changes delta by a fifth
power and cannot change its obstruction class. This algebra holds on
any Gamma and is not a claim that we classified new projective families.

The distinct next question is a genuinely different projective/monomial
representation component with this torsion obstruction, its trace-free
harmonic dynamics and coupled physical modes. Admission is paid here;
that construction and chirality remain unpaid.
