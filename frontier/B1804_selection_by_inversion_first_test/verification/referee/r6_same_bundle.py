"""Referee B1804, check 6: the factor-index action I_H (x) A_W and the draft's diagonal action A + A are the SAME
monodromy on Z^4 up to a lattice change of basis (the perfect shuffle swapping the tensor factors).  The two frames
differ only in where the complex structure sits relative to A: in the draft's frame the elliptic factors are the two
A-stable planes; in the factor-index frame A is holomorphic (on tau' = tau).  Also: is there an SL(4, Z) conjugator
(orientation-preserving) as well as the GL(4, Z) shuffle?"""
import sympy as sp
L = sp.Matrix([[1, 0], [1, 1]]); R = sp.Matrix([[1, 1], [0, 1]]); A = L * R
diag = sp.diag(A, A)                                  # (x1, y1, x2, y2): A on each factor's (x, y)
fidx = sp.Matrix(sp.BlockMatrix([[A[i, j] * sp.eye(2) for j in range(2)] for i in range(2)]))  # mixes x1,x2 and y1,y2
P = sp.Matrix([[1, 0, 0, 0], [0, 0, 1, 0], [0, 1, 0, 0], [0, 0, 0, 1]])   # shuffle (x1, y1, x2, y2) -> (x1, x2, y1, y2)
print("P diag P^-1 == factor-index action:", P * diag * P.inv() == fidx, "; det P =", P.det())
# an orientation-preserving conjugator: compose P with an element of the centraliser of diag of det -1, e.g. diag(J, J)?
J = sp.Matrix([[0, 1], [1, 0]])
for name, C in (("diag(I, -I)", sp.diag(sp.eye(2), -sp.eye(2))), ("diag(J, J)", sp.diag(J, J)), ("diag(A, I)", sp.diag(A, sp.eye(2))), ("diag(A - I, I) [A - I = golden unit, det -1, commutes with A]", sp.diag(A - sp.eye(2), sp.eye(2)))):
    Q = P * C
    print("  P*%s: det %s, conjugates diag to factor-index: %s" % (name, Q.det(), Q * diag * Q.inv() == fidx))
print("r6 exit 0")
