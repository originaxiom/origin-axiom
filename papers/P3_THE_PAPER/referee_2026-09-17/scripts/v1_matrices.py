"""Referee check 1: the genesis matrix identities and the square-root claim."""
from sympy import Matrix, eye, symbols, factor, expand, Poly, sqrt, Rational
import itertools

L = Matrix([[1,1],[0,1]]); R = Matrix([[1,0],[1,1]])
P = Matrix([[0,1],[1,0]])           # the swap
M = Matrix([[1,1],[1,0]])           # golden substitution matrix (a->ab, b->a)
A = L*R
print("L*R =", A.tolist(), " M^2 =", (M*M).tolist(), " equal:", (M*M)==A)
print("R*L =", (R*L).tolist())
print("det M =", M.det(), " det(LR) =", A.det(), " tr(LR) =", A.trace())

# claim: F = L*P is an integer square root of LR, orientation-REVERSING
F = L*P
print("F = L*P =", F.tolist(), "det F =", F.det(), "F^2 =", (F*F).tolist(), "== LR:", F*F==A)

# claim: unique up to sign in GL(2,Z); no orientation-preserving square root of LR
sols_neg, sols_pos = [], []
N = 12
for a,b,c,d in itertools.product(range(-N,N+1), repeat=4):
    X = Matrix([[a,b],[c,d]])
    dt = X.det()
    if dt not in (1,-1): continue
    if X*X == A:
        (sols_pos if dt==1 else sols_neg).append(X.tolist())
print("orientation-reversing square roots found (|entries|<=%d):"%N, sols_neg)
print("orientation-preserving square roots found:", sols_pos)

# Cayley-Hamilton argument: X^2 = tX - det(X) I  => X^2 = A means tX = A + det(X) I
# det(X)=+1 would need t^2 = det(A + I) = det([[3,1],[1,2]]) = 5, not a square.
print("det(LR + I) =", (A+eye(2)).det(), "(square? no) ; det(LR - I) =", (A-eye(2)).det())

# claim: L_a R_b admits an orientation-reversing integer square root iff a == b
def has_or_rev_sqrt(a,b,N=14):
    T = Matrix([[1,a],[0,1]])*Matrix([[1,0],[b,1]])
    out=[]
    for p,q,r,s in itertools.product(range(-N,N+1),repeat=4):
        X=Matrix([[p,q],[r,s]])
        if X.det()==-1 and X*X==T: out.append(X.tolist())
    return out
eq  = [(a,a) for a in range(1,5)]
neq = [(a,b) for a in range(1,5) for b in range(1,5) if a!=b]
print("\nL_a R_b with a==b:")
for a,b in eq: print("  a=b=%d:"%a, "roots:", has_or_rev_sqrt(a,b))
print("L_a R_b with a!=b (12 control pairs):")
bad=[]
for a,b in neq:
    r=has_or_rev_sqrt(a,b)
    if r: bad.append((a,b,r))
print("  pairs with a root (should be none):", bad, " count of control pairs:", len(neq))
