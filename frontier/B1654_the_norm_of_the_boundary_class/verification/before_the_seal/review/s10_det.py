import sympy as sp
a = sp.symbols('a1:4'); u = sp.symbols('u1:4')
A = sp.Matrix(a); U = sp.Matrix(u)
Y = A*U.T + U*A.T - (A.dot(U))*sp.eye(3)
d = sp.expand(Y.det())
claim = sp.expand((A.dot(A))*(U.dot(U))*(A.dot(U)))
print("det Y - (a.a)(u.u)(a.u) =", sp.simplify(d-claim))
# the exploration's guess (two_defects.py)
guess = sp.expand((A.dot(U))*((A.dot(A))*(U.dot(U)) - (A.dot(U))**2))
print("exploration guess differs from det by:", sp.simplify(d-guess) != 0)
# Y u = (u.u) a ; Y a = (a.a) u
print(sp.simplify(Y*U - (U.dot(U))*A), sp.simplify(Y*A - (A.dot(A))*U))
