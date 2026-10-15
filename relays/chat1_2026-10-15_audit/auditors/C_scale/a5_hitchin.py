# Independent check of the local Hitchin model (own conventions, written from scratch):
# Hitchin: -d_z d_zbar log h_i (diag Chern curvature, dz^dzbar coefficient) + [A, A*_h] = 0, A* = H^-1 conj(A)^T H.
import sympy as sp
z, zb = sp.symbols('z zb')                       # treat z, zbar as independent
b = sp.symbols('b', real=True)
L = -sp.log(z*zb)
def hitchin(h1, h2, A, Abar):                   # Abar = entrywise conjugate of A (in z <-> zb)
    H = sp.diag(h1, h2); Astar = H.inv()*Abar.T*H
    F = sp.diag(*[-sp.diff(sp.log(h), z, zb) for h in (h1, h2)])
    return (F + A*Astar - Astar*A).applyfunc(sp.simplify)
E12 = sp.Matrix([[0,1],[0,0]]); E21 = sp.Matrix([[0,0],[1,0]])
print("nilpotent, h=diag(1/L, L):", hitchin(1/L, L, E12/z, E12/zb))
print("nilpotent, h=diag(1/(L+b), L+b):", hitchin(1/(L+b), L+b, E12/z, E12/zb))
print("nilpotent, h=diag(L, 1/L) (wrong order):", hitchin(L, 1/L, E12/z, E12/zb))
lam = sp.symbols('lam', positive=True)
print("semisimple, flat h:", hitchin(sp.Integer(1), sp.Integer(1), sp.diag(lam,-lam)/z, sp.diag(lam,-lam)/zb))
# uniformising: Phi = E21 dz, h = diag(g^-1/2, g^1/2); with g = 1/(|z|^2 L^2) it must solve; Gaussian curvature of g|dz|^2
g = 1/(z*zb*L**2)
print("uniformising with cusp g:", hitchin(g**sp.Rational(-1,2), g**sp.Rational(1,2), E21, E21))
K = sp.simplify(-4/g*sp.diff(sp.log(g), z, zb)/2)   # K = -(2/g) d_z d_zbar log g  (Delta = 4 d_z d_zbar)
print("Gaussian curvature of g|dz|^2:", sp.simplify(-(2/g)*sp.diff(sp.log(g), z, zb)))
# pointwise norms on unit vectors of the complete metric 4|dz|^2/(|z|^2 L^2): |dz(e)| = |z| L / 2
r = sp.symbols('r', positive=True); Lr = -2*sp.log(r)
dz_over_z = Lr/2
print("pointwise |theta|, nilpotent model:", sp.simplify((1/Lr)*dz_over_z), "; b-family:", sp.simplify(dz_over_z/(Lr+b)),
      "; semisimple:", sp.simplify(lam*dz_over_z))
