"""B211's 'Phi is 40a1' -- derive Phi's Jacobian from Phi itself (no cited member).
Phi(x,z) = z^2 - (x^2+1) z + (2x^2-1) = 0  <=>  (2z - x^2 - 1)^2 = (x^2+1)^2 - 4(2x^2-1) = x^4 - 6x^2 + 5.
A genus-1 quartic w^2 = x^4 - 6x^2 + 5 with a rational point (x=1,w=0) is birational over Q to its Jacobian."""
import sympy as sp
from snappy.pari import pari
x,z,w = sp.symbols('x z w')
Phi = z**2 - (x**2+1)*z + (2*x**2-1)
assert sp.expand((2*z-x**2-1)**2 - ((x**2+1)**2 - 4*(2*x**2-1))) == sp.expand(4*Phi)
q = sp.expand((x**2+1)**2 - 4*(2*x**2-1)); print("quartic:", q, "=", sp.factor(q))
J = pari("ellfromeqn(w^2 - (x^4 - 6*x^2 + 5))"); print("Jacobian (ellfromeqn):", J)
E = pari(f"ellinit({J})"); Emin = E.ellminimalmodel(); print("minimal model a-invariants:", Emin[0:5] if hasattr(Emin,'__getitem__') else Emin)
print("j(Jac Phi) =", E.j(), "| conductor =", pari(f"ellglobalred(ellinit({J}))")[0])
E1 = pari("ellinit([0,0,0,-7,-6])"); print("j(40a1 = y^2=x(x-1)(x-5)) =", E1.j())
E3 = pari("ellinit([0,0,0,-2,1])");  print("j(40a3 = B509's Y^2=X^3-2X+1) =", E3.j())
iso = pari("ellisomat(ellinit([0,0,0,-7,-6]))"); js=[pari(f"ellinit([0,0,0,{m[0][0]},{m[0][1]}])").j() for m in iso[0]]
print("40a class j's:", js, "| degree matrix:", iso[1])
print("Jac(Phi) isomorphic over Q-bar to 40a1:", E.j()==E1.j(), "| to 40a3:", E.j()==E3.j())
# over Q: same j and same minimal model up to twist? check ellisomorphism via minimal models
print("minimal model of Jac(Phi):", pari(f"ellminimalmodel(ellinit({J}))")[0:5])
print("minimal model of 40a3 [0,0,0,-2,1]:", pari("ellminimalmodel(ellinit([0,0,0,-2,1]))")[0:5])
print("torsion Jac(Phi):", pari(f"elltors(ellinit({J}))"), "| 40a1 torsion:", pari("elltors(ellinit([0,0,0,-7,-6]))"), "| 40a3 torsion:", pari("elltors(ellinit([0,0,0,-2,1]))"))
# and the B211 point count identity is isogeny-invariant: a_p equal across the class
for p in (3,7,11,13):
    print(f"a_{p}: Jac(Phi)={E.ellap(p)}  40a1={E1.ellap(p)}  40a3={E3.ellap(p)}")

# ---- the map itself, exhibited (the identification rule: map + action) --------------------------
# (1) X^{na} = {Phi=0} IS the square-time curve d^2 = (c^2-1)(c^2-5) in the chart c = x, d = 2z - x^2 - 1
#     (a linear change of the z coordinate, so an isomorphism of plane curves over Q; B509's c is the same
#     meridian-trace coordinate: its geometric point (c=2, d^2=-3) is Phi's complete-structure point x=2,
#     where Phi(2,z) = z^2-5z+7 gives (2z-5)^2 = -3).
c, d = sp.symbols('c d')
sub = {c: x, d: 2*z - x**2 - 1}
lhs = sp.expand((d**2 - (c**2-1)*(c**2-5)).subs(sub))
print("d^2-(c^2-1)(c^2-5) at (c,d)=(x,2z-x^2-1) equals 4*Phi:", sp.expand(lhs - 4*Phi) == 0)
print("Phi(2,z):", sp.factor(Phi.subs(x, 2)), " -> (2z-5)^2 =", sp.expand((2*z-5)**2 - 4*Phi.subs(x, 2)))
# (2) 40a1 is the QUOTIENT of X^{na}: (x,z) -> (X,Y) = (x^2, x(2z-x^2-1)) lands on Y^2 = X(X-1)(X-5) on Phi=0
X, Y = x**2, x*(2*z - x**2 - 1)
rel = sp.expand(Y**2 - X*(X-1)*(X-5))
q_, r_ = sp.div(sp.Poly(rel, z), sp.Poly(Phi, z))
print("Y^2 - X(X-1)(X-5) is divisible by Phi (remainder 0):", r_.is_zero, " quotient:", sp.factor(q_.as_expr()))
# the deck involution of that quotient: sigma(x,z) = (-x, x^2+1-z) preserves Phi and has no affine fixed point
sig = Phi.subs({x: -x, z: x**2 + 1 - z}, simultaneous=True)
print("sigma preserves Phi:", sp.expand(sig - Phi) == 0)
fp = sp.solve([sp.Eq(-x, x), sp.Eq(x**2 + 1 - z, z)], [x, z], dict=True)
print("sigma fixed points (affine):", fp, " Phi there:", [Phi.subs(s) for s in fp], "(nonzero => fixed-point-free on X^na)")
# (3) the four rational points of X^na over Q are the four torsion points of 40a3 (B509's Rationality Theorem, now
#     a statement about the character variety itself): (x,z) = (+-1, 1) and the two points at infinity.
print("Phi(1,1), Phi(-1,1):", Phi.subs({x: 1, z: 1}), Phi.subs({x: -1, z: 1}))
E3 = pari("ellinit([0,0,0,-2,1])")
print("40a3 rank (ellrank bounds) :", pari(f"ellrank({E3})"), " torsion:", pari(f"elltors({E3})"))
