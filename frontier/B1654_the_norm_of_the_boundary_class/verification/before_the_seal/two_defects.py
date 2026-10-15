"""C1 exploration (main, unsealed): Y(a, u) = a u^T + u a^T - (a.u) 1 with u NOT isotropic.
Claim to test: the product of the three singular values-squared, det(Y^H Y) = |det Y|^2, and det Y = -(a.u)^... compute exactly,
and read the lightest mass's scaling with the defect u.u at fixed a."""
import sympy as sp
a = sp.symbols('a1:4'); u = sp.symbols('u1:4')
A = sp.Matrix(a); U = sp.Matrix(u)
Y = A*U.T + U*A.T - (A.dot(U))*sp.eye(3)
d = sp.factor(Y.det())
print("det Y =", d)
# check against a guess: det Y = (a.u) * ((a.a)(u.u) - (a.u)^2)  ?
guess = (A.dot(U))*((A.dot(A))*(U.dot(U)) - (A.dot(U))**2)
print("det - (a.u)[(a.a)(u.u)-(a.u)^2] =", sp.simplify(d - guess))
