"""xB034 C1 -- is B1381's cap mechanism a consequence of POSITIVE ENTROPY?

B1381 (SM branch, PROVED): no cyclic cover M_n of m004 has a rank-one character with h^1 = 2, because
the remaining Fox block is s*I - M^n, and M^n is NEVER SCALAR.
xB032: m004's monodromy has topological entropy log(lambda) > 0.
CLAIM TO TEST: for a monodromy M in SL(2,Z),  h_top > 0  (|tr M| > 2, hyperbolic)  ==>  M^n is never
scalar for n >= 1.  So positive entropy is SUFFICIENT for B1381's mechanism.
CONTROLS:  elliptic (finite order) M must hit a scalar power -- the mechanism FAILS there;
           parabolic M has entropy 0 yet is never scalar -- so the converse is FALSE and the claim
           is 'sufficient', not 'equivalent'.  Stating it as an equivalence would be wrong.
"""
import math
import sympy as sp

R = sp.Matrix([[1, 1], [0, 1]]); L = sp.Matrix([[1, 0], [1, 1]])
def word(w):
    M = sp.eye(2)
    for ch in w:
        M = M * (R if ch == 'R' else L)
    return M
def is_scalar(A):
    return A[0, 1] == 0 and A[1, 0] == 0 and A[0, 0] == A[1, 1]
def first_scalar_power(M, N=40):
    P = sp.eye(2)
    for n in range(1, N + 1):
        P = P * M
        if is_scalar(P):
            return n, P.tolist()
    return None, None
def entropy(M):
    tr = abs(int(M.trace()))
    if tr <= 2:
        return 0.0
    return math.log((tr + math.sqrt(tr * tr - 4)) / 2)

cases = [("RL = m004", word("RL"), "hyperbolic")]
for w in ("RRL", "RLL", "RRLL", "RLRRL", "RRRL", "RLRL", "RRLRL"):
    cases.append((w, word(w), "hyperbolic"))
cases += [("R (parabolic)", R, "parabolic"),
          ("[[0,1],[-1,0]] (order 4)", sp.Matrix([[0, 1], [-1, 0]]), "elliptic"),
          ("[[1,1],[-1,0]] (order 6)", sp.Matrix([[1, 1], [-1, 0]]), "elliptic"),
          ("[[0,1],[-1,-1]] (order 3)", sp.Matrix([[0, 1], [-1, -1]]), "elliptic")]
print(f"{'monodromy':28s} {'type':11s} {'|tr|':>4s} {'h_top':>9s}  first scalar power (n <= 40)")
ok = True
for name, M, kind in cases:
    h = entropy(M)
    n, P = first_scalar_power(M)
    print(f"{name:28s} {kind:11s} {abs(int(M.trace())):4d} {h:9.6f}  "
          f"{'NEVER' if n is None else f'n={n}: {P}'}")
    if kind == "hyperbolic" and (h <= 0 or n is not None):
        ok = False
    if kind == "elliptic" and n is None:
        ok = False
    if kind == "parabolic" and (h != 0 or n is not None):
        ok = False
print()
print("  hyperbolic (h_top > 0): M^n never scalar     -- B1381's mechanism HOLDS")
print("  elliptic   (h_top = 0): M^n hits +-I         -- B1381's mechanism FAILS  (control fires)")
print("  parabolic  (h_top = 0): M^n never scalar     -- so the CONVERSE is false")
print(f"\nC1 {'PASS' if ok else 'FAIL'}: positive entropy is SUFFICIENT for B1381's non-scalarity, "
      f"and NOT necessary.")
print("  READING, stated at its width: the generation cap and the thermodynamic side share a")
print("  root -- the monodromy is pseudo-Anosov.  It is the POSITIVITY of the entropy that does the")
print("  work, NOT its golden value and NOT its minimality: every hyperbolic word above caps too.")
