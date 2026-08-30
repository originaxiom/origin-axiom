# E52 verify-the-verifier: independent re-derivation, larger box (|entries|<=10),
# structural quantifier checks, extra exclusion/positive controls.
import itertools, sympy as sp
from sympy import Matrix, eye
from sympy.matrices.normalforms import smith_normal_form

A  = Matrix([[2,1],[1,1]]); I2 = eye(2)
B  = Matrix([[1,1],[1,0]])
X  = Matrix([[0,1],[-1,0]])

# ---- Part 1: homology (independent) ----
assert (A-I2).det() == -1
assert (-A-I2).det() == 5
s1 = smith_normal_form(A-I2, domain=sp.ZZ); s2 = smith_normal_form(-A-I2, domain=sp.ZZ)
print("SNF(A-I) =", [abs(s1[0,0]),abs(s1[1,1])], " SNF(-A-I) =", [abs(s2[0,0]),abs(s2[1,1])])

# ---- Part 2: exact identities ----
assert B*B == A and B.det() == -1 and A*B == B*A
assert B == A - I2                       # B in Z[A]: commutant(A)=commutant(B)
Ainv = A.inv().applyfunc(sp.nsimplify)
assert X*A*X.inv().applyfunc(sp.nsimplify) == Ainv and X.det() == 1
XB = X*B
assert XB*A*XB.inv().applyfunc(sp.nsimplify) == Ainv and XB.det() == -1
mA = -A; mAinv = mA.inv().applyfunc(sp.nsimplify)
assert X*mA*X.inv().applyfunc(sp.nsimplify) == mAinv        # route (ii) for -A
assert B*mA == mA*B                                          # route (i) for -A
print("identities: B^2=A, detB=-1, B=A-I, XAX^-1=A^-1 (detX=+1), det(XB)=-1; both routes transfer to -A: OK")

# Commutant integrality: xI+yB = [[x+y,y],[y,x]] integral <=> x,y in Z (entries ARE x+y,y,y,x).
# Z[B] ~ Z[phi] is the MAXIMAL order of Q(sqrt5) (disc 5 squarefree) => units {+-phi^n}
# => Cent_GL2(Z)(A) = {+-B^n} EXACTLY (not just in a box).
# Quantifier check for conjugators (structural, covers ALL of GL2(Z)):
#   P A P^-1 = A^-1  =>  (X^-1 P) A (X^-1 P)^-1 = X^-1 A^-1 X = A  => X^-1 P in Cent(A).
Xi = X.inv().applyfunc(sp.nsimplify)
assert Xi*Ainv*X == A   # the pivot identity making the coset argument exact
print("coset quantifier pivot X^-1 A^-1 X = A: OK (solution set == X*Cent(A) over ALL GL2(Z))")

R = 10
cent, conj = [], []
for a,b,c,d in itertools.product(range(-R,R+1), repeat=4):
    det = a*d-b*c
    if det not in (1,-1): continue
    M = Matrix([[a,b],[c,d]])
    if M*A == A*M: cent.append(M)
    if M*A == Ainv*M: conj.append(M)
Bp = {}; P = eye(2)
for n in range(0,15): Bp[n]=P; P=P*B
Pi = eye(2); Binv = B.inv().applyfunc(sp.nsimplify)
for n in range(1,15): Pi = Pi*Binv; Bp[-n]=Pi
pw = set()
for M in Bp.values():
    for s in (1,-1): pw.add(tuple((s*M).tolist()[0]+(s*M).tolist()[1]))
assert all(tuple(M.tolist()[0]+M.tolist()[1]) in pw for M in cent), "cent outside +-B^n"
assert all((Xi*M)*A == A*(Xi*M) for M in conj), "conjugator outside coset X*Cent"
cd = sorted(set(M.det() for M in cent)); jd = sorted(set(M.det() for M in conj))
print(f"box |entries|<=10: {len(cent)} centralizer (dets {cd}), {len(conj)} conjugators (dets {jd}); all in {{+-B^n}} / X*Cent: OK")

# ---- Part 3: controls ----
def routes(C):
    """instrument: or.-reversing routes for monodromy C over box |entries|<=R."""
    Cinv = C.inv().applyfunc(sp.nsimplify)
    r1 = r2 = False; centd=set(); conjd=set()
    for a,b,c,d in itertools.product(range(-R,R+1), repeat=4):
        det = a*d-b*c
        if det not in (1,-1): continue
        M = Matrix([[a,b],[c,d]])
        if M*C == C*M:
            centd.add(det)
            if det == -1: r1 = True
        if M*C == Cinv*M:
            conjd.add(det)
            if det == 1: r2 = True
    return r1, r2, sorted(centd), sorted(conjd)

# exclusion control (deliberately-absent target): disc 12, N=-1 insoluble
Ap = Matrix([[2,1],[3,2]])
assert all((xx*xx) % 3 != 2 for xx in range(3))   # x^2 mod 3 never = -1: Pell -1 insoluble
r1,r2,cdp,jdp = routes(-Ap)   # instrument on the TWISTED disc-12 carrier
print(f"exclusion control -A' (disc 12): route(i)={r1}, route(ii)={r2}; cent dets {cdp}, conj dets {jdp}")
assert not r1 and not r2, "exclusion control FAILED"
# also confirm at least one conjugator/centralizer WAS found (control not vacuous):
assert cdp == [1] and jdp == [-1]

# second positive control on a DIFFERENT norm -1 field: disc 8, Z[sqrt2], N(1+sqrt2)=-1
App = Matrix([[1,2],[1,1]])   # char poly x^2-2x-1, disc 8, det=-1
lam = sp.symbols('lambda')
assert App.det() == -1 and sp.expand(App.charpoly(lam).as_expr()) == lam**2 - 2*lam - 1
r1b,r2b,cb,jb = routes(App)
print(f"second positive control disc-8 C=[[1,2],[1,1]]: route(i)={r1b}, route(ii)={r2b} (cent dets {cb}, conj dets {jb})")
assert r1b or r2b, "instrument failed to fire on independent norm -1 field"
print("ALL LENS CHECKS PASSED")
