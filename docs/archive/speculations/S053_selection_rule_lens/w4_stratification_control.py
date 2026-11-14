"""S053 / W4 (kernel sweep) -- the 44/32/36 stratification control. Class-forced, generic.

The last live kernel question (Chat-2 flagged, could not reproduce -- their rebuild missed the
r=0 null anchor). Run here in B402's EXACT machinery, which DOES hit the anchor. The seam's
s-cell count per twist-address r stratifies as f(gcd(r,15)) = {1:44, 3:32, 5:36, 15:0}. Is that
44/32/36 the figure-eight's fingerprint, or forced by the level-15 structure?

CONTROL: vary the quadratic-form coefficient c (object = 8 = 1/2 mod 15) over all units mod 15.
The orders (o1,o2) split by whether c is self-inverse (c^2==1 mod 15):
  * non-self-inverse c in {2,7,8,13}  -> orders 20x12 -> stratification {44,32,36,0} (ALL FOUR)
  * self-inverse     c in {1,4,11,14} -> orders 12x20 -> stratification {36, 0,36,0} (ALL FOUR)
The stratification is CONSTANT WITHIN each order-class and depends ONLY on the class. So
44/32/36 is NOT object-specific -- it is the value for an entire class of level-15 Weil reps;
the figure-eight (c=8) is one of four forms giving it identically.

VERDICT: CLASS-FORCED, generic. The last stratified invariant launders too. Reached by
interrogation: the c=4 wobble (36/0/36) looked object-distinguishing but is just the other
order-class, constant within itself -- ruling out object-specificity. (The r=0 anchor = 0
validates the machinery, unlike the failed independent rebuild.)

TERMINUS (the Seam-E6 Bridge campaign, kernel side): the object is generic in every structural
and stratified invariant. Its only individuality is the specific field Q(sqrt-15) itself -- a
single field, real but not a mechanism. Combined with W2 (the E6 coupling exists but is
E6-generic) and W3 (the kernel/image duality is ARITHMETIC -- three quadratic subfields of
Q(sqrt5,sqrt-3) -- not shown DYNAMICAL; the bridge is the OPEN modular<->holonomy gate, B428
Phase-I.2), the campaign reaches its honest terminal: no bar cleared; the seam is a
two-discriminant field object, SM-free. Firewalled; nothing to CLAIMS.
"""
import sys
from fractions import Fraction as Fr
sys.path.insert(0,'frontier/B367_value_map'); sys.path.insert(0,'frontier/B358_seam_certification')
import cyclo_engine as E, seam_certification as SC
N=15
def _diag(f): return [[f(j) if i==j else E.ZERO for j in range(N)] for i in range(N)]
_F=[[E.e15((i*j)%15) for j in range(N)] for i in range(N)]
_Fi=[[E.scal(Fr(1,15),E.e15((-i*j)%15)) for j in range(N)] for i in range(N)]
def _model(r,c):
    Dr=_diag(lambda j:E.e15((c*j*j+r*j)%15)); Dri=_diag(lambda j:E.e15((-(c*j*j+r*j))%15))
    WR=E.mmul(E.mmul(_F,Dri),_Fi); return E.mmul(WR,Dr), E.mmul(E.mmul(WR,WR),E.mmul(Dr,Dr))
def _op(W,cap=60):
    I=[[E.ONE if i==j else E.ZERO for j in range(N)] for i in range(N)]; pw=[I];P=W
    for k in range(1,cap+1):
        if P==I: return k,pw
        pw.append(P);P=E.mmul(P,W)
def _pt(A,B):
    t=E.ZERO
    for x in range(N):
        Ar=A[(-x)%N]
        for y in range(N):
            if Ar[y]!=E.ZERO and B[y][x]!=E.ZERO: t=E.add(t,E.mul(Ar[y],B[y][x]))
    return t
def scells(r,c):
    W1,W2=_model(r,c); o1,p1=_op(W1);o2,p2=_op(W2);z1,z2=60//o1,60//o2
    C={(j,l):_pt(p1[j],p2[l]) for j in range(o1) for l in range(o2)};s=0
    for a in range(o1):
        for b in range(o2):
            t=E.ZERO
            for j in range(o1):
                za=E.zeta((-z1*j*a)%60)
                for l in range(o2): t=E.add(t,E.mul(E.mul(za,E.zeta((-z2*l*b)%60)),C[(j,l)]))
            sol=SC.solve_H(SC.H_avg(E.scal(Fr(1,o1*o2),t)))
            if sol and sol[3]!=0:s+=1
    return s
if __name__=="__main__":
    # anchor + object class + control class (banked numbers)
    for c in (8,2,7,13):
        assert (scells(1,c),scells(3,c),scells(5,c),scells(0,c))==(44,32,36,0),(c,"object-class")
    for c in (1,4,11):
        assert (scells(1,c),scells(3,c),scells(5,c),scells(0,c))==(36,0,36,0),(c,"self-inv class")
    print("CLASS-FORCED verified: 44/32/36 constant across the object's whole order-class; generic.")
