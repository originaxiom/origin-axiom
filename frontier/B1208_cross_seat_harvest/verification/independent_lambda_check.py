"""INDEPENDENT check of cloud memo 128's load-bearing claim, written without their code.

Their run reads rank 2 off memo 80's construction. What DECIDES B1206's candidate (iii) is the
structural claim that rank 1 is IMPOSSIBLE (so the preregistered fork had an empty branch). Memo
128 states that implication as: "C conserves t3, so the Hu x Hd block is forced ANTIDIAGONAL, so
its rank lies in {0, 2} and RANK 1 IS IMPOSSIBLE." This probe tests that chain step by step.
"""
from itertools import product
from fractions import Fraction as F
import sympy as sp

def rank2(M):
    a, b, c, d = M[0][0], M[0][1], M[1][0], M[1][1]
    if a == b == c == d == 0: return 0
    return 2 if a * d - b * c != 0 else 1

t3_Hu = [-1, +1]      # memo 80's roster: one SU(2) doublet
t3_Hd = [-1, +1]
vals = [F(-3), F(-1), F(0), F(1), F(2)]

print("=== STEP 1. what t3-conservation ALONE gives ===")
allowed = [(i, j) for i, j in product(range(2), range(2)) if t3_Hu[i] + t3_Hd[j] == 0]
ranks = set()
witness = None
for x in vals:
    for y in vals:
        M = [[0, 0], [0, 0]]
        for (i, j), v in zip(allowed, (x, y)):
            M[i][j] = v
        r = rank2(M)
        ranks.add(r)
        if r == 1 and witness is None:
            witness = [row[:] for row in M]
print(f"    allowed positions: {allowed} (antidiagonal, as the memo says)")
print(f"    ranks attainable: {sorted(ranks)}")
print(f"    RANK-1 WITNESS, t3-conserving and antidiagonal: {witness}")
print("    => THE MEMO'S STATED IMPLICATION IS INCOMPLETE. 'Antidiagonal' permits one entry to")
print("       vanish, which is rank 1. t3-conservation is the CARTAN only; it does not exclude it.")
assert 1 in ranks

print("\n=== STEP 2. what FULL SU(2) invariance gives (the hypothesis the claim actually needs) ===")
a, b, c, d = sp.symbols('a b c d')
B = sp.Matrix([[a, b], [c, d]])
J3 = sp.Rational(1, 2) * sp.Matrix([[1, 0], [0, -1]])
Jp, Jm = sp.Matrix([[0, 1], [0, 0]]), sp.Matrix([[0, 0], [1, 0]])
eqs = [e for X in (J3, Jp, Jm) for e in list(X.T * B + B * X)]
sol = sp.solve(eqs, [a, b, c, d], dict=True)[0]
Binv = sp.simplify(B.subs(sol))
free = sorted(Binv.free_symbols, key=str)
print(f"    invariant bilinears on 2 (x) 2: {Binv.tolist()}, free parameters: {len(free)}")
assert len(free) == 1, "the singlet space must be 1-dimensional"
k = free[0]
print(f"    => ONE-dimensional, spanned by {Binv.subs(k, 1).tolist()} = epsilon (antisymmetric)")
print(f"    det = {sp.simplify(Binv.det())}  =>  nonzero whenever the coefficient is")
print("    => rank in {0, 2}: RANK 1 IS IMPOSSIBLE. The claim HOLDS, on SU(2), not on t3.")

print("\n=== STEP 3. CONTROL -- the exclusion must be a fact about the DOUBLET ===")
# If the two Hu states were not an SU(2) doublet (both t3 = -1), the Cartan gate would allow a
# COLUMN, and rank 1 would be reachable even before asking about invariance.
bad = [(i, j) for i, j in product(range(2), range(2)) if (-1) + t3_Hd[j] == 0]
r = set()
for x in vals:
    for y in vals:
        M = [[0, 0], [0, 0]]
        for (i, j), v in zip(bad, (x, y)):
            M[i][j] = v
        r.add(rank2(M))
print(f"    hypothetical non-doublet Hu (t3 = [-1,-1]): allowed {bad}, ranks {sorted(r)}")
assert 1 in r
print("    => the enumeration CAN produce rank 1, so step 2's exclusion is not an artifact.")

print("\n=== STEP 4. the observed block is exactly epsilon ===")
obs = [[0, 1], [-1, 0]]
print(f"    memo 80's block: {obs}; antisymmetric: {obs[0][1] == -obs[1][0]}; rank {rank2([[F(x) for x in row] for row in obs])}")
print("    => consistent with step 2 and NOT merely with step 1.")

print("""
VERDICT OF THIS PROBE
  CONFIRMED: rank 1 is impossible, the fork's R-1 branch is empty, and the number of
             gauge-invariant functionals is ONE. Memo 128's CONCLUSION stands, and with it
             the negative close of B1206's candidate (iii).
  CORRECTED: the memo derives that impossibility from t3-conservation ("forced ANTIDIAGONAL,
             so rank in {0,2}"). Antidiagonal alone gives rank in {0,1,2} -- witness above.
             The exclusion needs FULL SU(2) invariance (the block is proportional to epsilon,
             so its two entries are not independent), which the object supplies since the
             cubic is E6-invariant. The gap is in the stated chain, not in the result.
VERIFIED""")
