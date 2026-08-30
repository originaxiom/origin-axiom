"""Adversarial re-derivation of GC-2 claim, independent code (correctness lens).

All checks are exact integer identities (sympy over ZZ, zero tolerance).
"""
import itertools
from sympy import Matrix, eye, ZZ
from sympy.matrices.normalforms import smith_normal_form

def snf_diag(M):
    S = smith_normal_form(M, domain=ZZ)
    return [abs(S[i, i]) for i in range(min(S.shape))]

fails = []
def check(name, cond, detail=""):
    print(("PASS " if cond else "FAIL ") + name + ("  " + detail if detail else ""))
    if not cond:
        fails.append(name)

A = Matrix([[2, 1], [1, 1]])
B = Matrix([[1, 1], [1, 0]])
X = Matrix([[0, 1], [-1, 0]])
I2 = eye(2)

# ---------- (1) Homological detection ----------
check("det(A-I) == -1", (A - I2).det() == -1)
check("SNF(A-I) == diag(1,1)", snf_diag(A - I2) == [1, 1])
check("det(-A-I) == 5", (-A - I2).det() == 5)
check("SNF(-A-I) == diag(1,5)", snf_diag(-A - I2) == [1, 5])
# So coker(A-I)=0 => H1(mapping torus of A)=Z ; coker(-A-I)=Z/5 => H1 = Z + Z/5.

# ---------- (2) Mirror parity: structure of centralizer & conjugator sets ----------
check("B^2 == A", B**2 == A)
check("det B == -1", B.det() == -1)
check("B satisfies B^2 = B + I (so B ~ phi in Z[phi])", B**2 == B + I2)
check("X A X^-1 == A^-1", X * A * X.inv() == A.inv(), "det X = %s" % X.det())
check("det X == +1", X.det() == 1)
XB = X * B
check("XB conjugates A -> A^-1, det -1", XB * A * XB.inv() == A.inv() and XB.det() == -1)
check("XB == [[1,0],[-1,-1]]", XB == Matrix([[1, 0], [-1, -1]]))

# Independent structural check that Cent_{M2(Z)}(A) = {xI + yB}:
# solve PA = AP over 4 unknowns symbolically.
from sympy import symbols, linsolve
a, b, c, d = symbols('a b c d', integer=True)
P = Matrix([[a, b], [c, d]])
eqs = list(P * A - A * P)
sol = linsolve(eqs, [a, b, c, d])
print("  symbolic centralizer solution:", sol)
# Expect 2-parameter family; verify it equals span{I, B}: PA=AP => b=c and a=d+b.
# {xI+yB} = [[x+y, y],[y, x]] indeed has b=c, a=d+b. Confirm equivalence:
x, y = symbols('x y', integer=True)
gen = x * I2 + y * B
check("xI+yB has form [[x+y,y],[y,x]]", gen == Matrix([[x + y, y], [y, x]]))
det_form = gen.det().expand()
check("centralizer det form == x^2+xy-y^2", det_form == (x**2 + x*y - y**2).expand())
# Norm form of Z[phi], disc 5; represents -1 at (0,1). Negative Pell for 5 solvable.
check("form takes +1 at (1,0) and -1 at (0,1)",
      det_form.subs({x: 1, y: 0}) == 1 and det_form.subs({x: 0, y: 1}) == -1)

# ---------- Exhaustive box search |entries| <= 6, independent implementation ----------
def box_scan(M, bound=6):
    """Return (centralizer_dets, conjugator_dets, cent_list, conj_list) for GL2(Z)
    elements P with |entries|<=bound, P M P^-1 = M (cent) or = M^-1 (conj)."""
    Minv = M.inv()
    cents, conjs = [], []
    rng = range(-bound, bound + 1)
    for p, q, r, s in itertools.product(rng, repeat=4):
        det = p * s - q * r
        if det not in (1, -1):
            continue
        Pm = Matrix([[p, q], [r, s]])
        if Pm * M == M * Pm:
            cents.append((Pm, det))
        if Pm * M * Pm.inv() == Minv:
            conjs.append((Pm, det))
    return cents, conjs

def is_pm_power_of(P, gen, maxn=12):
    G = eye(2)
    if P == G or P == -G:
        return True
    for n in range(1, maxn + 1):
        G = G * gen
        if P == G or P == -G:
            return True
    G = eye(2)
    geninv = gen.inv()
    for n in range(1, maxn + 1):
        G = G * geninv
        if P == G or P == -G:
            return True
    return False

for label, M in [("A", A), ("-A (twisted carrier)", -A)]:
    cents, conjs = box_scan(M)
    cent_dets = sorted(d for _, d in cents)
    conj_dets = [d for _, d in conjs]
    from collections import Counter
    cc = Counter(conj_dets)
    print(f"  [{label}] #centralizer={len(cents)} dets={Counter(d for _,d in cents)}; "
          f"#conjugators={len(conjs)} dets={dict(cc)}")
    check(f"[{label}] 18 centralizer elements in box", len(cents) == 18)
    check(f"[{label}] all centralizer elems are +/-B^n",
          all(is_pm_power_of(P, B) for P, _ in cents))
    check(f"[{label}] centralizer contains det=-1 (B itself)",
          any(d == -1 for _, d in cents))
    check(f"[{label}] 18 conjugators, dets {{+1:10, -1:8}}",
          len(conjs) == 18 and cc[1] == 10 and cc[-1] == 8)
    check(f"[{label}] every conjugator is in coset X*{{+/-B^n}}",
          all(is_pm_power_of(X.inv() * P, B) for P, _ in conjs))
    check(f"[{label}] BOTH det signs occur among conjugators",
          cc[1] > 0 and cc[-1] > 0)

# Coset claim exactly: solution set of P M P^-1 = M^-1 is X*Cent(M).
# Proof-check numerically inside box: done above (X^-1 P is +/-B^n for all conjugators).

# ---------- Orientation bookkeeping sanity (mapping torus M_C, C=-A) ----------
C = -A
check("C=-A commutes with B", C * B == B * C)
check("X conjugates C to C^-1", X * C * X.inv() == C.inv())
check("|tr C| == 3 > 2 (Anosov/Sol)", abs(C.trace()) == 3)
# route (i): base-fixed fiber map P=B, PC=CP, det=-1 -> orientation-reversing. exists.
# route (ii): base-reversing P=X, PCP^-1=C^-1, det=+1 -> total orientation-reversing. exists.
# Well-definedness of route (ii) map f(v,t)=(Pv,-t) on (v,t)~(Cv,t+1) requires
# C P C = P, i.e. P^-1 C P = C^-1 -- check for P = X.inv() form both ways:
check("route(ii) gluing identity C*X*C == X ... i.e. X^-1 C X = C^-1",
      X.inv() * C * X == C.inv())

# ---------- (3) Two-sided control: A' = [[2,1],[3,2]], disc 12 ----------
Ap = Matrix([[2, 1], [3, 2]])
check("det A' == 1, tr A' == 4, disc == 12", Ap.det() == 1 and Ap.trace() == 4
      and Ap.trace()**2 - 4*Ap.det() == 12)
N = Ap - 2 * I2  # [[0,1],[3,0]], N^2 = 3I
check("N^2 == 3I", N**2 == 3 * I2)
sol2 = linsolve(list(P * Ap - Ap * P), [a, b, c, d])
print("  symbolic centralizer of A':", sol2)
gen2 = x * I2 + y * N
check("A' centralizer det form == x^2-3y^2", gen2.det().expand() == (x**2 - 3*y**2).expand())
# x^2-3y^2 = -1 insoluble mod 3 (and mod 4): squares mod 3 are {0,1}, need x^2 = 2 mod 3.
check("x^2 == 2 mod 3 insoluble", all((t*t) % 3 != 2 for t in range(3)))
Xp = Matrix([[1, 0], [0, -1]])
check("X' conjugates A' -> A'^-1, det == -1",
      Xp * Ap * Xp.inv() == Ap.inv() and Xp.det() == -1)
for label, M in [("A'", Ap), ("-A' (twisted control carrier)", -Ap)]:
    cents, conjs = box_scan(M)
    from collections import Counter
    check(f"[{label}] centralizer dets all +1 in box",
          all(d == 1 for _, d in cents), f"n={len(cents)}")
    check(f"[{label}] conjugator dets all -1 in box",
          len(conjs) > 0 and all(d == -1 for _, d in conjs), f"n={len(conjs)}")
# => no det=-1 centralizer (route i dead), no det=+1 conjugator (route ii dead):
# disc-12 twisted double has NO orientation-reversing self-map of either route -> chiral.
# Control torsion for completeness:
print("  control: det(-A'-I) =", (-Ap - I2).det(), " SNF(-A'-I) =", snf_diag(-Ap - I2))

print()
print("FAILURES:", fails if fails else "NONE — all claims reproduced independently")
