# Local fixed-meridian splitting: the scope needed to avoid both false kills and false hopes

This is an authored proof conditional on the exact Jacobian check, not
an independently reviewed theorem or a classification of the relative
SL5 character variety. The neighborhood is complex analytic and its
radius is not quantitatively estimated.

## 1. The relevant block system

Diagonalize Reg(C3) over K(omega), K=Q(zeta5). Then the native E0 has
three G2-invariant blocks A3=rho2+1, L+=eta and L-=eta^-1. Its meridian
has one eigenvalue-one generalized eigenspace A3, and the two simple
cubic eigenlines. The off-block endomorphisms decompose as

    (rho tensor eta + rho tensor eta^-1)
    + its dual
    + (eta + eta^-1) + its dual + (eta + eta^-1).

The first two terms connect the doublet to the two nontrivial family
lines, the next two connect the trivial family line to those lines,
and the last connects the two nontrivial lines to each other. Rank is
4+4+2+2+2=14. The remaining two mixed directions connecting rho to the
trivial line are INSIDE A3, not in this off-block system.

The rational companion of x^2+x+1 implements the paired characters
without choosing a floating root. This is the full rank-14 module after
extending scalars, not a projection deleting a family. An independent
trace comparison with End(E)-End(A3)-C-C checks the decomposition on
literal group words. The decomposition itself follows from Hom(B,A),
not from traces alone, so no extension class is inferred from a character.

## 2. Fixed-meridian tangent matrix

G2 has three generators and two relators, with its first generator the
meridian. For infinitesimal changes written u(g)=delta rho(g) rho(g)^-1,
the relator linearization is the usual Fox differential in the adjoint
coefficient system. Fixing the meridian sets u(g1)=0. The remaining
off-block unknowns are u(g2),u(g3), dimension 28. Their equations are
the two relators' off-block entries, also dimension 28. The producer
forms this square matrix directly from Fox columns 2 and 3.

The meridian minus identity is invertible on every off-block Hom, due
to disjoint spectra. Hence there is no residual off-block conjugation
fixing the meridian. A full-rank square Jacobian genuinely removes all
off-block infinitesimal directions; it is not just removing gauge.

For comparison the older rank-six mixed module includes the live rho
to trivial-line direction. There H1 has dimension one, its meridian
restriction is zero, and H0 of the meridian is one while global H0 is
zero. Thus the raw fixed-meridian Jacobian kernel has dimension TWO:
one cohomology direction and one residual gauge direction. That does
not contradict zero torus-relative H1.

## 3. Why the exact tangent computation controls a neighborhood here

Keep the MERIDIAN CONJUGACY CLASS fixed, not just its trace/eigenvalues.
A local analytic conjugation gauge sets that matrix exactly equal to
the seed meridian. Its three distinct generalized eigenspaces then
give a fixed 3+1+1 block decomposition.

Near the seed, use local analytic coordinates for each other SL5 matrix
as exp(X_off) B_diag. Off-block X has dimension 14 and the block-diagonal
Levi factor has dimension 10, together the full dimension 24. Taking
the off-block entries of the two relators gives 28 analytic equations
in the 28 off-block variables, with the remaining block entries as
parameters. The checked Fox matrix is their derivative up to invertible
coordinate changes.

For ANY nearby block-diagonal parameters, setting X_off=0 solves all
off-block equations identically: products and inverses of block-diagonal
matrices are block diagonal. If the derivative is invertible, the
analytic implicit-function theorem makes this the UNIQUE nearby
solution of the off-block equations. Imposing the remaining diagonal
relator equations cannot create another off-block solution. Therefore
every sufficiently nearby actual fixed-meridian representation remains
block diagonal 3+1+1. The longitude was never fixed in this argument.

This is stronger than citing a bare vanishing tangent space without
checking which variables/equations it controls. No formal-to-analytic
or reductive-GIT assertion is needed. It does not rule out distant
components, a change of meridian Jordan class, or different boundary
conditions. The smaller block A3 may still deform nontrivially.

## 4. Central twists and a scoped index corollary

Multiplying all parent matrices by a central character cancels out of
their adjoint action. Thus the off-block local result applies to every
one of the five E_q seeds; direct conjugation tests verify that cancellation.

In the fixed-meridian neighborhood the two one-dimensional summands
remain characters of G2 with meridian omega and omega^-1, respectively,
times the fixed torsion factors of the seed. Since H1(G2)=Z+Z/5 and the
meridian is primitive in its free part, fixing its value leaves only
discrete torsion choices, constant in a sufficiently small neighborhood.
These lines are finite-order and have zero interior index, also on G6.

The active A3 block has meridian J2+1 and its cube has the same partition,
so each of its meridian invariant bounds on G6 is two. IF its global H0
and dual H0 are balanced, the earlier boundary identity gives

    |I(M6; A3)| <= 2, hence |I(M6; E5)| <= 2.

Balance is an explicit hypothesis, for example satisfied by a reductive
background (including restriction to the finite-index cover). It is not
asserted for every nonsplit deformation. The character summands have
balanced H0, so balance of the full E on G6 is equivalent here to balance
of A3. No automatic physical use is made of reductivity or finite Higgs
energy: those requirements must come from the actual action/domain.

## Practical consequence

If the exact test passes, relaxing joint peripheral conjugacy does NOT
open a nearby irreducible SL5 parent here, despite a genuine smaller-block
meridian-relative direction. The next irreducible search must leave this
neighborhood or change the stated meridian class; a physical source/nonflat
mechanism is another separately priced possibility. The actual partial
positive (0,3) remains valid and is not retracted.
