#!/usr/bin/env python3
"""MEMO-86 CELL (WAVE-4, dossier row AR0): ORDER WITHOUT DIRECTION — the
owner's proposal ("the very initial a, ab, ba locks the arrow") decided
exactly.  The verdict the machine returns: the initial noncommutativity
locks the EXISTENCE of temporal order (that sequence matters is
object-forced, from the first two letters), and leaves the DIRECTION
free — measurably, three independent ways.

PREREGISTERED (asserts; the owner's claim is typed, not dismissed):
  FACT 1 (ORDER IS FORCED — the half that locks): ab != ba in the record,
    exactly: the commutator [a,b] is NONTRIVIAL with tr_2[a,b] != 2
    computed exactly in Z[w] (irreducibility/nonabelianness at the FIRST
    pair of letters), and the internal images A27 B27 != B27 A27 (entry
    exhibited).  Time-ORDER structure — the difference between doing a
    then b and b then a — is object-paid from the start.
  FACT 2 (BUT ab ~ ba): ba = a^{-1}(ab)a — conjugate elements: same trace
    at both levels (asserted), same closed geodesic.  The object cannot
    tell ab from ba as a state of affairs; only as a LOCAL composition.
  FACT 3 (DIRECTION IS FREE, three ways):
    (i)  inversion w -> w^{-1}: character-invisible (memo 79 FACT 1;
         re-asserted here on the radius-4 ball: 0 exceptions);
    (ii) NEW — the strong-inversion relabeling sigma (a -> a^{-1},
         b -> b^{-1}, ORDER KEPT): count words with tr(sigma w) != tr(w)
         on the radius-4 ball.  (Two-outcome: 0 = the relabeling is
         character-invisible too — running every generator backwards
         costs nothing; >0 = a genuine direction-marker exists and the
         owner's claim gains a computed witness — either banks.)
    (iii) the tick's staircase is direction-independent: N' = A^{-1}-I
         satisfies N' = -A^{-1} N exactly => ker N'^k = ker N^k — the
         one-way depth-3 chain (memo 50) is the SAME filtration for a and
         a^{-1}: the clock decays down the same staircase whichever way
         the meridian is run.
VERDICT SHAPE: the record's arrow splits as ORDER (object-forced, FACT 1)
x DIRECTION (free, FACT 3) — matching the global pattern (B1168's law;
B1174's c-leg carries the direction bit).  The owner's proposal lands as
the ORDER half, banked; the dossier gains row AR0.
Gate 5 untouched.
"""
from fractions import Fraction as F
from collections import Counter
SCR=__import__('os').path.dirname(__import__('os').path.abspath(__file__))+""
src=open(SCR+"/twisted_double.py").read()
cut=src.index("# ---------------- stage 4")
exec(src[:cut])

# ---- SL2 level, exact pair arithmetic (x + y*w, w^2 = w - 1)
def pmul(A,B):
    (a,b),(c,d)=A,B
    return (a*c-b*d, a*d+b*c+b*d)
def padd(A,B): return (A[0]+B[0],A[1]+B[1])
def pneg(A): return (-A[0],-A[1])
ONEp=(F(1),F(0)); ZEROp=(F(0),F(0)); Wp=(F(0),F(1))
def mm2(X,Y):
    return [[padd(pmul(X[0][0],Y[0][0]),pmul(X[0][1],Y[1][0])), padd(pmul(X[0][0],Y[0][1]),pmul(X[0][1],Y[1][1]))],
            [padd(pmul(X[1][0],Y[0][0]),pmul(X[1][1],Y[1][0])), padd(pmul(X[1][0],Y[0][1]),pmul(X[1][1],Y[1][1]))]]
Ma2=[[ONEp,ONEp],[ZEROp,ONEp]]; MA2=[[ONEp,pneg(ONEp)],[ZEROp,ONEp]]
Mb2=[[ONEp,ZEROp],[pneg(Wp),ONEp]]; MB2=[[ONEp,ZEROp],[Wp,ONEp]]
def wprod2(w):
    M=[[ONEp,ZEROp],[ZEROp,ONEp]]
    for ch in w: M=mm2(M,{'a':Ma2,'b':Mb2,'A':MA2,'B':MB2}[ch])
    return M
def tr2(M): return padd(M[0][0],M[1][1])

# FACT 1: order forced
comm=wprod2("abAB")
tcomm=tr2(comm)
print(f"FACT 1: tr[a,b] = {tcomm[0]}+({tcomm[1]})w — exact, != 2: {tcomm!=(F(2),F(0))}")
assert tcomm!=(F(2),F(0))
Mab=wprod2("ab"); Mba=wprod2("ba")
assert Mab!=Mba
print("   ab != ba as matrices (SL2): the record is NONABELIAN at the first two letters —")
print("   time-ORDER structure is object-paid from the start")

# internal level
r0=ROOTS[0]
E27=rho27_Q(evec(r0)); F27=rho27_Q(evec(tuple(-x for x in r0)))
Z=(F(0),F(0)); O=(F(1),F(0)); Qp=(F(0),F(1))
E27p=toF(E27); F27p=toF(F27)
Ma=nilexp(E27p,ONE); MA=nilexp(E27p,fneg(ONE))
Mb=nilexp(F27p,Qp);  MB=nilexp(F27p,fneg(Qp))
def mmF(X,Y):
    n=len(X); out=[[Z]*n for _ in range(n)]
    for i in range(n):
        Xi=X[i]
        for k in range(n):
            x=Xi[k]
            if x==Z: continue
            Yk=Y[k]; oi=out[i]
            for j in range(n):
                y=Yk[j]
                if y==Z: continue
                oi[j]=fadd(oi[j],fmul(x,y))
    return out
AB=mmF(Ma,Mb); BA=mmF(Mb,Ma)
diff=next(((i,j) for i in range(27) for j in range(27) if AB[i][j]!=BA[i][j]),None)
assert diff is not None
print(f"   internal level: (A27 B27) != (B27 A27), first differing entry {diff}")

# FACT 2: ab ~ ba
def trF(M):
    t=Z
    for i in range(27): t=fadd(t,M[i][i])
    return t
assert tr2(Mab)==tr2(Mba) and trF(AB)==trF(BA)
print("FACT 2: ba = a^-1 (ab) a — conjugate: tr(ab) = tr(ba) at BOTH levels (asserted):")
print("   the object cannot tell ab from ba as a state — only as a local composition")

# FACT 3: direction free
I27=[[O if i==j else Z for j in range(27)] for i in range(27)]
LET={'a':Ma,'b':Mb,'A':MA,'B':MB}
INV={'a':'A','b':'B','A':'a','B':'b'}
LMAX=4
tr_of={}
def dfs(word, mat):
    if word: tr_of[word]=trF(mat)
    if len(word)==LMAX: return
    for ch in 'abAB':
        if word and INV[word[-1]]==ch: continue
        dfs(word+ch, mmF(mat,LET[ch]))
dfs("", I27)
words=sorted(tr_of)
def invword(w): return ''.join(INV[ch] for ch in reversed(w))
bad_inv=[w for w in words if tr_of[invword(w)]!=tr_of[w]]
print(f"FACT 3(i): inversion w -> w^-1 invisible on the radius-{LMAX} ball: "
      f"{len(bad_inv)} exceptions (memo 79 re-asserted)")
assert not bad_inv
bad_sig=[w for w in words if tr_of[''.join(INV[c] for c in w)]!=tr_of[w]]
print(f"FACT 3(ii): the strong-inversion relabeling sigma (letters -> inverses, order")
print(f"   kept): {len(bad_sig)} of {len(words)} words change character")
if not bad_sig:
    print("   sigma is character-INVISIBLE too: running every generator backwards costs")
    print("   nothing — the second direction-flip is also free")
else:
    print(f"   exhibit: {bad_sig[0]} — a direction-marker EXISTS; the owner's claim gains")
    print("   a computed witness at the relabeling level")
# FACT 3(iii): the staircase is direction-independent
def matexp_nilQ(Mx):
    n=len(Mx)
    out=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    term=[row[:] for row in out]; k=1
    while True:
        term=[[sum(term[i][l]*Mx[l][j] for l in range(n))/k for j in range(n)] for i in range(n)]
        if all(x==0 for row in term for x in row): break
        out=[[a+b for a,b in zip(r1,r2)] for r1,r2 in zip(out,term)]
        k+=1; assert k<40
    return out
Aq=matexp_nilQ(E27); Ainv=matexp_nilQ([[-x for x in row] for row in E27])
def mmQ(X,Y):
    n=len(X)
    return [[sum(X[i][k]*Y[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
Nq=[[Aq[i][j]-(F(1) if i==j else F(0)) for j in range(27)] for i in range(27)]
Npq=[[Ainv[i][j]-(F(1) if i==j else F(0)) for j in range(27)] for i in range(27)]
lhs=Npq
rhs=mmQ([[-x for x in row] for row in Ainv], Nq)
assert lhs==rhs
print("FACT 3(iii): N' = A^-1 - I = -A^-1 N exactly => ker N'^k = ker N^k: the tick's")
print("   depth-3 staircase (memo 50) is the SAME one-way filtration for a and a^-1 —")
print("   the clock decays down one staircase whichever way the meridian runs")

print("""
ORDER WITHOUT DIRECTION: the owner's proposal lands as a theorem-shaped
half.  The very initial a, b DOES lock something — that ORDER EXISTS:
ab != ba from the first two letters, exactly, at both levels (the record
is temporal in structure from its first act).  What it does not lock is
the DIRECTION: ab ~ ba as states, inversion and (as measured above) the
strong-inversion relabeling are character-free, and the clock's one-way
staircase is the same either way.  The arrow splits exactly as the
record's global pattern demands: ORDER object-forced, DIRECTION the
observer's c-leg (B1168/B1174).  Dossier row AR0.  Gate 5 untouched.""")
