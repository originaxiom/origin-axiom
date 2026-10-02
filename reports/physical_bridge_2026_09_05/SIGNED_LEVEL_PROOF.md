# Signed-level proof audit (authored; independent review pending)

October 2, 2026, R78. This is a preregistered deduction, not a report
that its computational or geometric checks have already run.

## S1: sign and cover do not commute

Let A=LR=[[2,1],[1,1]] and eps in {+1,-1}. A cyclic degree n cover
of the mapping torus of eps A has monodromy (eps A)^n=eps^n A^n.
Central signing after that cover gives -eps^n A^n instead. In
particular U=-A^2=[[-5,-3],[-3,-2]] is not (-A)^2=A^2; traces
are -7 and +7. This distinction survives GL(2,Z) conjugacy.

## S2: exact fibre homology and cubic characters

For a once-punctured-torus mapping torus M(B), the homology sequence
gives H1(M(B);Z)=Z + coker(B-I). For a full-rank integer 2x2
matrix D, its Smith factors are gcd(entries D), |det D|/gcd.
For U, U-I=-[[6,3],[3,3]], giving (3,3). For A^2 the factors
are (1,5). Thus U has Z+C3+C3 whereas the incorrectly substituted
positive cyclic double cover has Z+C5. Mod 3, U=I, so all nine
fibre characters into C3 are monodromy-fixed; eight are nonzero.
This is neither an index nor a physical generation count. The free
base character has been set trivial, not selected by a new principle.

## S3: U is not a proper matrix power

Suppose B^n=U, B in GL(2,Z), n>=2. If n is even, B either has
real eigenvalues whose even powers are nonnegative, or conjugate
nonreal eigenvalues. In the latter case det B=1 and both have
modulus one. Neither possibility gives U's two negative real
eigenvalues of unequal modulus, one outside the unit circle.

If n is odd, det B=1 and B must be hyperbolic with negative real
eigenvalues. Its integer trace has absolute value >=3. Write its
eigenvalue magnitudes as r,r^-1 with r>1. Then
r^n+r^-n >= r^3+r^-3 = |tr B|^3-3|tr B| >=18,
contradicting |tr U|=7. No such B exists. This proof is not based
on a finite root search. Elliptic even powers are explicitly outside
the hyperbolic hypothesis.

## S4: primitive unsigned seeds cannot encode U even at level one

Any mixed positive L/R word can be cyclically rotated to start LR.
All entries of that product are positive. Appending L increases
trace by the lower-left entry >=1; appending R increases trace by
the upper-right entry >=1. Thus a mixed word of length l has
trace >=l+1. To have trace 7 it has length <=6.

The finite exhaustive check in signed_level.py lists every such
word. The trace-7 primitive words, if the preregistered enumeration
confirms this step, have cyclic/swap representative LLLLLR. Its
negative matrix has cokernel C9, not C3+C3. The other trace-7
class is the unsigned proper power LRLR. The resulting invariant
exclusion, together with S3, shows U is not GL-conjugate to ANY
ordinary cyclic level of a signed primitive unsigned mixed seed.
The enumeration is a stated proof obligation, not assumed complete
because a few examples agreed. Trace does not by itself distinguish
these two cases.

## S5: corrected coordinates and actual relations

Store (w,k,eps) as eps A(w)^k. Ordinary cyclic cover degree n maps
it to (w,kn,eps^n); a legal central sign change maps eps to -eps.
For negative sign and k=2^r m with m odd, the same matrix is
(-A(w)^(2^r))^m. This is the natural signed-power seed alternative;
there is no claim that all such seeds are matrix-power primitive
in the whole mapping-class group.

For U=-A^2, U^2=A^4. Therefore its mapping torus and M(A^2)
have the same degree-two cyclic cover M(A^4), within the assumed
surface realization. This supplies a real architecture relation;
sharing cubic homology alone would not. The geometric checks test
hyperbolicity and named carriers, not derive surface realization
from the philosophical principle or certify physical interactions.

## Scope

B1516's reduction to eps A(w) may be correct while its next signed
seed/level identification is wrong. The original 758 census is
preserved as a restricted family. No assertion that U is absent
from the repository, its census databases, or every other finite
population is made. This audit does not choose U as a new root or
vacuum, derive couplings, overturn same-domain chirality results,
or prove a globally complete geometry catalog.
