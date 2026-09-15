#!/usr/bin/env python3
"""MEMO-49 CELL: TRACE THREE — where the two ends meet, and the one meridian's
two clocks.

The atlas's top two structural motifs are the golden end (Q(sqrt5), 56%) and
the Eisenstein end (Q(sqrt-3), 53%), identified as one object by the two_ends
unity pattern but never by a single exact mechanism.  This cell exhibits one:

  FACT 1 (the golden end, from dynamics): the fiber tick — the monodromy on
    H1(fiber), rediscovered in-run as the abelianization of the memo-43
    substitution (phi(U)=V, phi(V)=VU^-1VV, found by exact matrix search) —
    has characteristic polynomial  x^2 - 3x + 1:  trace 3, det 1 (a UNIT),
    discriminant 9 - 4 = 5.  Roots phi^2, phi^-2: the golden end.
  FACT 2 (the Eisenstein end, from conservation): the first integral
    kappa = tr[a,b] = 1 + q (memo 41, re-verified in-run) has minimal
    polynomial  X^2 - 3X + 3:  trace 3, norm 3 (the RAMIFIED prime),
    discriminant 9 - 12 = -3.  The Eisenstein end.
  => THE MECHANISM: both ends are monic quadratics of TRACE 3; the only
    difference is the constant term — det 1 (unit) vs norm 3 (ramified) —
    and disc = 9 - 4d gives 5 and -3 respectively.  The object supplies
    both polynomials itself: one from its clock, one from its conserved
    number.  The two ends are the unit answer and the ramified answer to
    the same trace.
  FACT 3 (one meridian, two clocks): the same generator a acts
    - on the FIBER lattice with spectral radius phi^2 (exponential clock,
      entropy 2 log phi > 0), exactly the roots of Fact 1's polynomial;
    - on the CARRIER Psi = C^2 (x) 27 as a UNIPOTENT with nilpotency degree
      EXACTLY 3:  (rho_Psi(a) - I)^2 != 0,  (rho_Psi(a) - I)^3 = 0
      (polynomial clock, zero entropy).  Both factors are 2-step (e_r raises
      the h-weight by 2, so rho27(e)^2 = 0 on the doublets, and the spinor
      factor is 2-step); the carrier composes them to depth 2 + 2 - 1 = 3.
      [The first draft preregistered depth 4 from a mis-set weight ladder;
      the machine refused it — corrected here, error filed in the memo.]
    Matter's internal time is finitely deep; geometric time is hyperbolic.
  FACT 4 (the beat's role): gal fixes Fact 1's polynomial coefficientwise
    (rational) and permutes the roots of Fact 2's within Q(sqrt-3)
    (kappa <-> gal kappa, memo 41): the mirror leaves the golden clock alone
    and stirs only the Eisenstein pair.
"""
import itertools
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- pair-field 2x2 (holonomy) for facts 1-substitution, 2, 4
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
def fsub2(u,v): return (u[0]-v[0],u[1]-v[1])
def m2(X,Y): return [[fadd(fmul(X[i][0],Y[0][j]),fmul(X[i][1],Y[1][j])) for j in range(2)] for i in range(2)]
def inv2x2(X):
    d=fsub2(fmul(X[0][0],X[1][1]),fmul(X[0][1],X[1][0])); assert d==O
    return [[X[1][1],fneg(X[0][1])],[fneg(X[1][0]),X[0][0]]]
A2=[[O,O],[Z,O]]; B2=[[O,Z],[Qp,O]]
dd={'a':A2,'A':inv2x2(A2),'b':B2,'B':inv2x2(B2)}
def word2(w):
    M=[[O,Z],[Z,O]]
    for ch in w: M=m2(M,dd[ch])
    return M
assert word2('abABaBAbaB')==[[O,Z],[Z,O]]

# FACT 1: rediscover the fiber substitution and take its abelianization
U=word2('bA'); V=word2('abAA')
Ui=inv2x2(U); Vi=inv2x2(V)
target=m2(A2,m2(V,inv2x2(A2)))
gens={'U':U,'u':Ui,'V':V,'v':Vi}
found=None
for L in range(1,6):
    for wtuple in itertools.product('UuVv',repeat=L):
        bad=any((wtuple[i],wtuple[i+1]) in (('U','u'),('u','U'),('V','v'),('v','V')) for i in range(L-1))
        if bad: continue
        M=[[O,Z],[Z,O]]
        for ch in wtuple: M=m2(M,gens[ch])
        if M==target: found=''.join(wtuple); break
    if found: break
assert found is not None
nU=found.count('U')-found.count('u'); nV=found.count('V')-found.count('v')
T_fiber=[[0,nU],[1,nV]]
tr_f=T_fiber[0][0]+T_fiber[1][1]; det_f=T_fiber[0][0]*T_fiber[1][1]-T_fiber[0][1]*T_fiber[1][0]
print(f"fiber tick (abelianized substitution phi(V) = {found}): matrix [[0,{nU}],[1,{nV}]]")
print(f"  characteristic polynomial: x^2 - {tr_f}x + {det_f}   trace {tr_f}, det {det_f}, disc {tr_f*tr_f-4*det_f}")
assert (tr_f,det_f)==(3,1)
print("  => the GOLDEN end: disc 5, roots phi^2, phi^-2 (a unit)")

# FACT 2: kappa's minimal polynomial
comm=word2('abAB')
kappa=fadd(comm[0][0],comm[1][1])
assert kappa==(F(1),F(1))
def gal2(u): return (u[0]+u[1],-u[1])
tr_k=fadd(kappa,gal2(kappa)); nm_k=fmul(kappa,gal2(kappa))
print(f"kappa = 1+q: minimal polynomial X^2 - {tr_k[0]}X + {nm_k[0]}   trace {tr_k[0]}, norm {nm_k[0]}, disc {int(tr_k[0]*tr_k[0]-4*nm_k[0])}")
assert tr_k==(F(3),F(0)) and nm_k==(F(3),F(0))
print("  => the EISENSTEIN end: disc -3, (kappa) the ramified prime")
print("\nTHE MECHANISM: both ends solve 'trace 3' — x^2-3x+d with d = det:")
print("  d = 1 (unit)    -> disc  5  -> Q(sqrt5),  the golden end   (the clock)")
print("  d = 3 (ramified)-> disc -3  -> Q(sqrt-3), the Eisenstein end (the integral)")

# FACT 3: the meridian's nilpotency degree on the carrier (rational computation)
r0=ROOTS[0]
E27=rho27_Q(evec(r0))
# A27 = exp(E27) over Q
def matexp_nil(M):
    n=len(M)
    out=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    term=[row[:] for row in out]
    k=1
    while True:
        term=[[sum(term[i][l]*M[l][j] for l in range(n))/k for j in range(n)] for i in range(n)]
        if all(x==0 for row in term for x in row): break
        out=[[a+b for a,b in zip(r1,r2)] for r1,r2 in zip(out,term)]
        k+=1
        assert k<40
    return out
A27q=matexp_nil(E27)
A2q=[[F(1),F(1)],[F(0),F(1)]]
def kronQ(X,Y):
    nx=len(X); ny=len(Y)
    out=[[F(0)]*(nx*ny) for _ in range(nx*ny)]
    for i in range(nx):
        for j in range(nx):
            if X[i][j]==0: continue
            for a in range(ny):
                for b in range(ny):
                    if Y[a][b]==0: continue
                    out[i*ny+a][j*ny+b]=X[i][j]*Y[a][b]
    return out
APsi=kronQ(A2q,A27q)
Nmat=[[APsi[i][j]-(F(1) if i==j else F(0)) for j in range(54)] for i in range(54)]
def mmQ(X,Y):
    n=len(X)
    out=[[F(0)]*n for _ in range(n)]
    for i in range(n):
        for k in range(n):
            if X[i][k]==0: continue
            x=X[i][k]
            for j in range(n):
                if Y[k][j]!=0: out[i][j]+=x*Y[k][j]
    return out
P=Nmat; deg=1
while any(x!=0 for row in P for x in row):
    P=mmQ(P,Nmat); deg+=1
    assert deg<10
print(f"\nmeridian on the CARRIER: (rho_Psi(a) - I)^{deg} = 0 and ^{deg-1} != 0: nilpotency degree EXACTLY {deg}")
assert deg==3
print("meridian on the FIBER lattice: spectral radius phi^2 (the golden root of Fact 1)")
print("=> ONE generator, TWO clocks: 3-step-nilpotent (zero entropy) on matter,")
print("   hyperbolic (entropy 2 log phi) on the geometric fiber.")

# FACT 4
print("\nthe beat (gal): fixes x^2-3x+1 coefficientwise (rational — the golden clock")
print("untouched) and swaps the roots of X^2-3X+3 (kappa <-> gal kappa, memo 41):")
print("the mirror stirs only the Eisenstein pair.")

print("""
TRACE THREE: the record's two arithmetic ends are the unit answer and the
ramified answer to a single equation — trace 3 — with the object supplying
both witnesses itself: its clock's characteristic polynomial (disc 5) and
its conserved number's minimal polynomial (disc -3).  And the one meridian
that drives both reads matter and geometry at different depths: three exact
steps on the carrier, golden exponential on the fiber.  Structure only;
Gate 5 untouched.""")
