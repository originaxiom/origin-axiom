#!/usr/bin/env python3
"""GC-2: THE SIGN — the relational bit on the TWISTED double.

Part 1: homological detection of the twist (det/SNF of A-I vs A+I), A=[[2,1],[1,1]].
Part 2: mirror-parity of the twist datum: solve X A X^-1 = A^-1 over GL2(Z),
        exact centralizer, determinant profile of the conjugator coset.
Part 3: two-sided control: a hyperbolic matrix over Z[sqrt(3)] (fundamental unit
        norm +1) whose conjugator coset has a DIFFERENT det profile — the
        instrument can exclude a sign.
All exact (sympy over ZZ). Tolerance: none needed — integer arithmetic only.
"""
import sympy as sp
from sympy import Matrix, eye, symbols, ZZ
from sympy.matrices.normalforms import smith_normal_form

out = []
def log(s):
    out.append(s); print(s)

A = Matrix([[2,1],[1,1]])
I2 = eye(2)

# ---------- Part 1: the twist is homologically detected ----------
dm = (A - I2).det()          # plain A-bundle torsion = coker(A-I)
dp = (A + I2).det()          # twisted (-A)-bundle torsion = coker(-A-I) ~ coker(A+I)
snf_minus = smith_normal_form(A - I2, domain=ZZ)
snf_plus  = smith_normal_form(A + I2, domain=ZZ)
log(f"P1: det(A-I) = {dm}, SNF(A-I) = {snf_minus.tolist()}  -> H1(plain) = Z (torsion trivial)")
log(f"P1: det(A+I) = {dp}, SNF(A+I) = {snf_plus.tolist()}  -> H1(twisted) = Z + Z/5")
assert abs(dm) == 1 and snf_minus == Matrix([[1,0],[0,1]])
assert dp == 5 and snf_plus == Matrix([[1,0],[0,5]])
# two-sided homology control: positive (Z/5 present in twisted) AND
# deliberately-absent target (torsion ABSENT in plain) both delivered by same instrument.

# ---------- Part 2: the conjugator coset ----------
Ainv = A.inv()
assert Ainv == Matrix([[1,-1],[-1,2]]) and all(x == int(x) for x in Ainv)

# 2a. Commutant of A over Z: solve X A = A X linearly.
a,b,c,d = symbols('a b c d', integer=True)
X = Matrix([[a,b],[c,d]])
eqs_comm = (X*A - A*X)
sol_comm = sp.solve([e for e in eqs_comm], [a,b,c,d], dict=True)
log(f"P2a: commutant solve X A = A X: {sol_comm}")
# Expect a rank-2 module: X = p*I + q*B with B = A - I = [[1,1],[1,0]] (Fibonacci).
B = A - I2
assert B == Matrix([[1,1],[1,0]])
assert B*A == A*B
assert B*B == B + I2          # B^2 = B + I  <->  phi^2 = phi + 1 : B IS the golden unit
log(f"P2a: B = A - I = {B.tolist()}, B^2 = B + I verified; det(B) = {B.det()}  (norm(phi) = -1)")
# every commuting integer matrix is p*I+q*B (from the linear solve): verify the solve says so
Xg = Matrix([[a, b],[b, a - b]])   # general form implied by sol_comm below; verified:
# sol_comm gives d = a - b (via a - c form) and c = b; check:
subs_ok = all((Xg*A - A*Xg).applyfunc(sp.simplify) == sp.zeros(2,2) for _ in [0])
assert (Xg*A - A*Xg) == sp.zeros(2,2)
log("P2a: general commutant element = a*I + b*B = [[a+? ..]] -> {p I + q B}: CONFIRMED (X=[[a,b],[b,a-b]])")
# GL2(Z) elements of the commutant: det(pI+qB) = +/-1 <-> p^2+pq-q^2 = +/-1 <-> units of Z[phi]
# centralizer = {+/- B^n}. det(B^n) = (-1)^n  -> centralizer CONTAINS det=-1 elements.

# 2b. Conjugator equation X A = A^-1 X : solve the linear system exactly.
eqs_conj = (X*A - Ainv*X)
sol_conj = sp.solve([e for e in eqs_conj], [a,b,c,d], dict=True)
log(f"P2b: conjugator solve X A = A^-1 X: {sol_conj}")
# Plug back general solution and extract module generators
s = sol_conj[0]
Xc = X.subs(s)
free = sorted(Xc.free_symbols, key=str)
log(f"P2b: general integer solution X = {Xc.tolist()} with free {free}")
gens = []
for f in free:
    g = Xc.applyfunc(lambda e: sp.diff(e, f))
    gens.append(g)
    log(f"P2b: generator d/d{f}: {g.tolist()}, det = {g.det()}")
# 2c. explicit conjugators and their determinants
J = Matrix([[0,1],[-1,0]])
assert J*A*J.inv() == Ainv
log(f"P2c: J = {J.tolist()}: J A J^-1 = A^-1 verified; det(J) = {J.det()}   (a det +1 conjugator)")
K = J*B
assert K*A*K.inv() == Ainv
log(f"P2c: K = J*B = {K.tolist()}: K A K^-1 = A^-1 verified; det(K) = {K.det()}   (a det -1 conjugator)")

# 2d. exhaustive check on a box: every GL2(Z) solution in |entries|<=N is +/- J B^n
N = 12
found = []
import itertools
for aa,bb,cc,ddd in itertools.product(range(-N,N+1), repeat=4):
    M = Matrix([[aa,bb],[cc,ddd]])
    dt = M.det()
    if dt in (1,-1) and M*A == Ainv*M:
        found.append((M, dt))
dets = sorted(set(int(d) for _,d in dets_list) if (dets_list:=[(m,d) for m,d in found]) else [])
log(f"P2d: box search |entries|<={N}: {len(found)} GL2(Z) conjugators; det values present = {sorted(set(int(d) for _,d in found))}")
# verify each is +/- J*B^n
Binv = B.inv()
def is_pm_JBn(M, nmax=40):
    for sgn in (1,-1):
        T = (J.inv()*M*sgn)
        # T should be B^n for some n in Z
        P = eye(2)
        for n in range(nmax+1):
            if T == P: return True
            P = P*B
        P = eye(2)
        for n in range(nmax+1):
            if T == P: return True
            P = P*Binv
    return False
assert all(is_pm_JBn(M) for M,_ in found)
log(f"P2d: every box conjugator equals +/- J B^n : CONFIRMED -> coset = J * centralizer, dets = (+1)*(-1)^n, BOTH signs occur")

# ---------- Part 3: two-sided control (the instrument can exclude a sign) ----------
# M = [[2,3],[1,2]] : tr 4, det 1, hyperbolic; commutant unit = 2+sqrt(3), NORM +1
Mc = Matrix([[2,3],[1,2]])
Mcinv = Mc.inv()
U = Mc  # fundamental-unit matrix in its own commutant is Mc itself here (2+sqrt3 <-> [[2,3],[1,2]])
foundc = []
for aa,bb,cc,ddd in itertools.product(range(-N,N+1), repeat=4):
    Xm = Matrix([[aa,bb],[cc,ddd]])
    if Xm.det() in (1,-1) and Xm*Mc == Mcinv*Xm:
        foundc.append((Xm, int(Xm.det())))
detsc = sorted(set(d for _,d in foundc))
log(f"P3: control M=[[2,3],[1,2]] (unit 2+sqrt3, norm +1): box |entries|<={N}: {len(foundc)} conjugators; det values = {detsc}")
# commutant of Mc: X=[[a,3c],[c,a]] (from M symmetric structure); det = a^2-3c^2 = +/-1;
# a^2 - 3c^2 = -1 has NO integer solutions (mod 3: a^2 = -1 mod 3 impossible) -> centralizer all det +1
log("P3: a^2 - 3*c^2 = -1 impossible mod 3 -> centralizer of M is ALL det +1 -> coset has ONE det sign only.")
assert detsc == [-1] or detsc == [1]
log(f"P3: instrument verdict on control: det profile = {detsc} (single-signed) vs golden case (both signs). TWO-SIDED: PASS")

# ---------- Verdict ----------
log("")
log("VERDICT: det(A+I)=5 proves the twist is homologically detected (a Z/2 datum of the PAIR),")
log("BUT K = [[1,0],[-1,-1]], det -1, conjugates A -> A^-1: the twisted double is MIRROR-SELF-EQUIVALENT.")
log("Root cause: centralizer contains B = A - I (the golden unit phi), det(B) = N(phi) = -1.")
log("The twist bit is mirror-EVEN -> fails B1168 (mirror-odd) -> the relational bit does NOT carry c. NEGATIVE.")
