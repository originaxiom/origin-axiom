#!/usr/bin/env python3
"""C5 / QP-1: DOES THE BOUNDARY DETERMINE THE INTERIOR?  Exact, on the Riley
family of m004.

The Markov-blanket quartet's last open item: is the interior character-variety
point recoverable from boundary (cusp) data alone?  Concretely, on the Riley
family A = [[m,1],[0,1/m]], B = [[m,0],[s,1/m]]:
  - the relator R(A,B) = I cuts the Riley curve phi(m,s) = 0 (compute exactly;
    for fixed generic m it is QUADRATIC in s: two interior points over one
    meridian eigenvalue);
  - boundary data = the peripheral character (tr mu, tr lambda) with
    lambda = b A B a a B A b (the banked longitude word);
  - QP-1: do the two interior points over the same m give DIFFERENT tr lambda
    (boundary separates the interior fiber: the self-report is injective), or
    the same (boundary blind to the interior bit)?
Method (exact, sympy): phi = the s-resultant-free direct computation from the
relator; write tr_lambda(m,s); reduce modulo phi to compare its two branch
values:  tr_lambda(s1) - tr_lambda(s2) = (s1 - s2) * S(m)  with S computed by
exact polynomial algebra (division of the antisymmetric part by (s1 - s2) via
the symmetric functions of phi).  If S(m) is not identically zero, the boundary
determines the interior for all but the finitely many exact zeros of S — list
them and identify them.
PREREGISTERED two-outcome: S != 0 (QP-1 closes POSITIVE: generic injectivity,
exceptional locus exact) or S == 0 (QP-1 closes NEGATIVE: a hidden interior
bit invisible to the cusp — a surprise worth its own hunt).
"""
import sympy as sp

m, s = sp.symbols('m s')
A=sp.Matrix([[m,1],[0,1/m]])
B=sp.Matrix([[m,0],[s,1/m]])
Ai=A.inv(); Bi=B.inv()
d={'a':A,'A':Ai,'b':B,'B':Bi}
def word(w):
    M=sp.eye(2)
    for ch in w: M=M*d[ch]
    return sp.simplify(M)

R=word('abABaBAbaB')
# R = I on the curve: entries' numerators give the defining ideal; take the (1,0) entry
E=sp.simplify(R-sp.eye(2))
polys=[sp.factor(sp.together(E[i,j])) for i in range(2) for j in range(2)]
# common curve: use numerator of E[1,0] (classically the Riley polynomial x m-units)
num=sp.numer(sp.together(E[1,0]))
phi=sp.factor(num)
print("relator (1,0)-entry numerator, factored:")
print("  ", phi)
# strip monomial units and s-free factors; keep the factor containing s
facs=sp.factor_list(phi)
cands=[f for f,mult in facs[1] if f.has(s) and sp.degree(sp.Poly(f,s))>0 and f!=s]
print("candidate irreducible factors (s-dependent, excluding s=0 reducible locus):")
for f in cands: print("   ", f)
# a factor is a genuine rep-variety component iff ALL FOUR entries of R - I vanish mod it
def kills_relator(f):
    Pf=sp.Poly(sp.expand(f), s)
    for p in polys:
        nm=sp.numer(sp.together(p))
        r=sp.rem(sp.Poly(sp.expand(nm*sp.denom(sp.together(p))**0), s), Pf).as_expr()
        # allow m-unit denominators: clear them
        r=sp.simplify(sp.together(r))
        if r!=0:
            num_r=sp.numer(r)
            if sp.simplify(sp.rem(sp.Poly(sp.expand(num_r),s), Pf).as_expr())!=0:
                return False
    return True
comps=[f for f in cands if kills_relator(f)]
print("factors on which the FULL relator vanishes (true components):", comps)
assert len(comps)>=1
# the geometric component: contains the parabolic Riley root at m=1 (s^2 - s + 1)
geo=[f for f in comps if sp.simplify(sp.factor(f.subs(m,1)) - sp.expand(s**2-s+1))==0 or sp.expand(f.subs(m,1))==sp.expand(s**2-s+1)]
print("components reducing to the Riley quadratic s^2-s+1 at m=1:", geo)
assert len(geo)>=1
phi=sp.expand(geo[0])
Pphi=sp.Poly(phi, s)
print("GEOMETRIC component phi(m,s) =", phi, "; degree in s:", Pphi.degree())
assert Pphi.degree()==2
NONGEO=[f for f in comps if sp.expand(f)!=phi]

# discrete rep check: at m = 1 (parabolic) phi(1,s) should have the Riley root q (s^2 - s + 1)
print("phi at m=1:", sp.factor(phi.subs(m,1)))

# boundary data
lam=word('bABaaBAb')
trl=sp.simplify(sp.trace(lam))
trl=sp.together(trl)
trl_num=sp.expand(sp.numer(trl)); trl_den=sp.denom(trl)
print("tr(lambda) denominator (m-units only):", trl_den)
assert not trl_den.has(s)

# the two branches: phi = c2 s^2 + c1 s + c0;  s1+s2 = -c1/c2, s1 s2 = c0/c2
c2=Pphi.nth(2); c1=Pphi.nth(1); c0=Pphi.nth(0)
# antisymmetric part: T(s1)-T(s2) = (s1-s2)*S where S = sum over odd-part expansion;
# compute by polynomial identity: write T(s) mod phi as alpha(m) + beta(m) s  (deg<2);
# then T(s1)-T(s2) = beta * (s1 - s2)  => S = beta.
Trem=sp.rem(sp.Poly(trl_num, s), Pphi)
Trex=sp.expand(Trem.as_expr())
beta=sp.expand(sp.collect(Trex, s).coeff(s,1))
alpha=sp.expand(sp.collect(Trex, s).coeff(s,0))
print("tr(lambda)*den reduced mod phi:  alpha(m) + beta(m) s")
Sfac=sp.factor(beta)
print("S(m) = beta(m), factored:", Sfac)
iszero = sp.simplify(beta)==0
print("S identically zero (boundary blind):", iszero)
assert iszero   # PREREGISTERED RED BRANCH REALIZED: the character is blind
# THE MECHANISM: per interior point, the longitude eigenvalue on the meridian's
# m-eigenvector; across the fiber the two values must multiply to 1.
mv=sp.Rational(7,5)
ph=sp.Poly(phi.subs(m,mv), s)
rts=list(sp.roots(ph))
Ls=[]
for r_ in rts:
    lam_v=lam.subs([(m,mv),(s,r_)])
    lam_v=sp.Matrix(2,2, lambda i,j: sp.simplify(lam_v[i,j]))
    # the meridian's m-eigenvector is e1-direction-ish: A=[[m,1],[0,1/m]] has
    # eigenvector (1,0) for eigenvalue m; lambda commutes with A so it is
    # upper-triangular in the same basis: its (0,0) entry IS L on that line
    comm=sp.simplify(lam_v*A.subs(m,mv).subs(s,r_) - A.subs(m,mv)*lam_v)
    assert all(sp.simplify(comm[i,j])==0 for i in range(2) for j in range(2))
    assert sp.simplify(lam_v[1,0])==0
    Ls.append(sp.simplify(lam_v[0,0]))
prod=sp.simplify(Ls[0]*Ls[1]); diff=sp.simplify(Ls[0]-Ls[1])
print(f"oriented longitude eigenvalues at m = {mv}:")
print("   L1 * L2 =", prod, "  (1 = the fiber swaps L <-> 1/L)")
print("   L1 == L2:", sp.simplify(diff)==0, " (False = the ORIENTED eigenvalue separates)")
assert prod==1 and sp.simplify(diff)!=0
# the two fiber points are complex conjugates at real m (the swap = conjugation):
disc=sp.discriminant(ph.as_expr(), s)
print(f"fiber discriminant at m = {mv}: {disc}  (< 0: the two interior points are complex conjugate)")
assert disc<0
print("at m = 1 the fiber is {q, qbar} (s^2 - s + 1): the parabolic case, same structure")
print("""
QP-1 CLOSES ON THE PREREGISTERED SECOND BRANCH, WITH THE MECHANISM EXACT:
the cusp CHARACTER (tr mu, tr lambda) is IDENTICALLY BLIND to one interior
bit — tr(lambda) reduces mod phi to a function of m alone (beta = 0), so the
two interior points over every meridian eigenvalue are boundary-
indistinguishable.  The hidden bit is exact and named: the two points carry
oriented longitude eigenvalues L and 1/L (product = 1, verified), they are
complex conjugates of each other over real m (disc < 0), and L <-> 1/L with
the meridian fixed is PRECISELY the beat's action on the cusp lattice
(memo 31: beta(mu) = +mu, beta(lambda) = +lambda^-1).  The Markov blanket's
self-report hides exactly one bit, and it is the beat's mirror bit — the
same Z/2 that selects the spin structure.  Oriented boundary data (m, L)
separates the fiber; the trace forgets the orientation of the reflection.""")
