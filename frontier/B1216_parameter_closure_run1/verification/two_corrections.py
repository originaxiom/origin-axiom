"""B1216 -- the two corrections the parameter-closure loop made to THIS repo's own record.

Both were surfaced by the loop's adjudication bench and are re-derived here before banking.
"""
from itertools import combinations_with_replacement
import sympy as sp

print("=== CORRECTION 1: B1215's tail-pair enumeration was INCOMPLETE ===")
# The selection law (B1215, independently certified by codex R025): rho + sigma = 3 - chi(A) mod 12.
for chiA, label in ((7, "A_7  (down)"), (11, "A_11 (lepton)")):
    need = (3 - chiA) % 12
    pairs = [(a, b) for a, b in combinations_with_replacement([0, 2, 4, 6, 8], 2)
             if (a + b) % 12 == need]
    equal = [p for p in pairs if p[0] == p[1]]          # repeated 1-dim direction -> skew zero
    surviving = [p for p in pairs if p not in equal]
    print(f"  {label}: need {need:2d} -> pairs {pairs}")
    print(f"           die by skewness (repeated direction): {equal}   SURVIVING: {len(surviving)}")
assert [(a, b) for a, b in combinations_with_replacement([0, 2, 4, 6, 8], 2)
        if (a + b) % 12 == 4] == [(0, 4), (2, 2), (8, 8)]
print("  => B1215 reported the A_11 pairs as {(0,4), (2,2)} and MISSED (8,8), which also")
print("     satisfies 16 = 4 mod 12. (8,8) is likewise a repeated direction, so it also dies.")
print("  => THE COUNT IS 2 SURVIVING (down) vs 1 SURVIVING (lepton). B1215's CONCLUSION IS")
print("     UNCHANGED -- the lepton leg has strictly fewer -- but its enumeration was wrong.")

print("\n=== CORRECTION 2: GC-16's eigenline clause is MB12-VACUOUS ===")
print("  THE CLAUSE (B1192/GC-16, a supporting leg): 'X0 acts as the Galois generator on BOTH")
print("  spectral fields -- the class restricts to c.'")
print("  THE ONE-LINE THEOREM that empties it: for hyperbolic P in SL2(Z), det P = 1, so the")
print("  eigenvalues are {lam, 1/lam} and the Galois conjugate of lam over Q(tr P) IS 1/lam.")
print("  Any X with X P X^-1 = P^-1 carries P's lam-eigenline to P^-1's lam-eigenline, which is")
print("  P's OWN 1/lam-eigenline. So EVERY anti-conjugator swaps the eigenlines, by construction.")

def check(P, X):
    P, X = sp.Matrix(P), sp.Matrix(X)
    if sp.simplify(X * P * X.inv() - P.inv()) != sp.zeros(2, 2):
        return None
    (l1, _, v1), (l2, _, v2) = P.eigenvects()[0], P.eigenvects()[1]
    w = sp.simplify(X * v1[0])
    return sp.simplify(w[0] * v2[0][1] - w[1] * v2[0][0]) == 0

cases = [("the golden A, det X = -1 (the LIVE case)", [[2, 1], [1, 1]], [[-1, 0], [1, 1]]),
         ("a det X = +1 anti-conjugator (the DEAD, mirror-EVEN type)", [[5, 2], [2, 1]], [[0, -1], [1, 0]])]
results = []
for name, P, X in cases:
    r = check(P, X)
    results.append(r)
    print(f"    {name:56s} swaps eigenlines: {r}")
assert all(r is True for r in results), "both must swap, which is the point"
print("  => IT HOLDS FOR THE det +1 CASE TOO -- the mirror-EVEN type the record calls dead.")
print("  => THE CLAUSE HAS NO FAILING BRANCH. It cannot discriminate, so it supports nothing.")
print("     The det = -1 SIGN result is untouched: that one does discriminate.")
print("\nVERIFIED")
