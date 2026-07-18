"""
DERIVATION A -- the Galois/eigenvalue route (block-eigenvalues ONLY;
NO Nahm state-integral). Exact arithmetic in Q(zeta5).

Question: does the block-decomposed Phi.tauPhi, carrying only Q(sqrt5)
eigenvalue data phi^{4k}, k=-m..m, project the four-class orbit
{1/5,2/5,3/5,4/5} onto {2/5,3/5}?
"""
import sympy as sp

z = sp.exp(2*sp.pi*sp.I/5)            # zeta5
z = sp.rootof(sp.cyclotomic_poly(5, sp.Symbol('x')), 0)  # exact algebraic zeta5
# work in the cyclotomic field via minimal poly relation 1+z+z^2+z^3+z^4=0
x = sp.Symbol('x')
Phi5 = 1 + x + x**2 + x**3 + x**4

def reduce_cyc(poly):
    """reduce a Z-poly in x mod Phi5, return dict class-> coeff on basis
    {x,x^2,x^3,x^4} using 1 = -(x+x^2+x^3+x^4)."""
    r = sp.rem(sp.Poly(poly, x), sp.Poly(Phi5, x)).as_expr()
    r = sp.expand(r)
    p = sp.Poly(r, x)
    # constant term c0 -> spread via 1 = -(x+..+x^4)
    coeffs = {i: p.coeff_monomial(x**i) for i in range(4)}
    c0 = coeffs[0]
    out = {}
    for i in range(1,5):
        ci = p.coeff_monomial(x**i) if i<4 else 0
        # x^4 term: p has degree <=3 after rem, so ci for i=4 is 0
        out[i] = sp.nsimplify(ci - c0)  # subtract c0 (since 1=-(sum x^i))
    # careful: rem gives degree<=3, so only classes 1,2,3 have raw coeff; x^4 via relation
    # recompute cleanly:
    return out

# cleaner: represent element as poly deg<=3, then convert to the 4 fractional
# classes {1,2,3,4} by the reduced-basis rule 1 -> -(z+z^2+z^3+z^4).
def frac_support(poly):
    r = sp.rem(sp.Poly(poly, x), sp.Poly(Phi5, x)).as_expr()
    p = sp.Poly(sp.expand(r), x)
    c = [p.coeff_monomial(x**i) for i in range(4)]  # c0..c3 (deg<=3)
    # class coefficients on z^1..z^4 after eliminating the constant via 1=-(z+z2+z3+z4):
    cls = {1: c[1]-c[0], 2: c[2]-c[0], 3: c[3]-c[0], 4: 0-c[0]}
    return {k: sp.nsimplify(v) for k,v in cls.items()}

# phi = (1+sqrt5)/2 as an element of Q(zeta5): phi = -(z^2+z^3)
phi_poly = -(x**2 + x**3)
# check numerically
val = complex(sp.N(phi_poly.subs(x, sp.exp(2*sp.pi*sp.I/5))))
print("phi as -(z^2+z^3) numeric:", val, " expected", float((1+sp.sqrt(5))/2))

# Gaussian periods
eta0 = x + x**4      # {1,4}
eta1 = x**2 + x**3   # {2,3}
print("eta0 = z+z^4 =", complex(sp.N((x+x**4).subs(x, sp.exp(2*sp.pi*sp.I/5)))), "= 1/phi")
print("eta1 = z^2+z^3=", complex(sp.N((x**2+x**3).subs(x, sp.exp(2*sp.pi*sp.I/5)))), "= -phi")
print("eta0,eta1 roots of t^2+t-1:", sp.simplify((eta0+eta1)), sp.simplify(sp.expand(eta0*eta1) % 1))

# FACT: powers of phi via Fibonacci: phi^j = F_j*phi + F_{j-1}
def phi_power_poly(j):
    Fj = sp.fibonacci(j)
    Fj1 = sp.fibonacci(j-1)
    return sp.expand(Fj*phi_poly + Fj1)   # = F_j*phi + F_{j-1}, phi=-(z^2+z^3)

blocks = {1:[ -1,0,1 ], 4:None,5:None,7:None,8:None,11:None}
ms = [1,4,5,7,8,11]

print("\n=== per-eigenvalue fractional-class support (canonical reduced basis) ===")
occupied_all = set()
for m in ms:
    for k in range(-m, m+1):
        supp = frac_support(phi_power_poly(4*k))
        cls_nonzero = {c for c,v in supp.items() if v != 0}
        occupied_all |= cls_nonzero
        if abs(k) <= 2 and m in (1,4):
            print(f"m={m} k={k:+d}: phi^{4*k}: classes {sorted(cls_nonzero)}  coeffs {supp}")
print("union of all fractional classes occupied by ALL block eigenvalues:", sorted(occupied_all))

# key single powers
print("\nphi^0  classes:", sorted({c for c,v in frac_support(phi_power_poly(0)).items() if v!=0}))
print("phi^1  classes:", sorted({c for c,v in frac_support(phi_power_poly(1)).items() if v!=0}), " (= -eta1, {2,3})")
print("phi^-1 classes:", sorted({c for c,v in frac_support(phi_power_poly(-1)).items() if v!=0}), " (= eta0, {1,4})")
print("phi^2  classes:", sorted({c for c,v in frac_support(phi_power_poly(2)).items() if v!=0}), " (golden monodromy lambda)")
print("phi^4  classes:", sorted({c for c,v in frac_support(phi_power_poly(4)).items() if v!=0}))

# === Galois action ===
# sigma: zeta5 -> zeta5^2 generates (Z/5)*  (order 4). On phi: sqrt5->-sqrt5 so phi -> 1-phi = -1/phi.
# Check the eigenvalue MULTISET {phi^{4k}: k=-m..m} is sigma-stable:
print("\n=== eigenvalue multiset Galois-stability (sigma: phi -> -1/phi) ===")
def canon(j):
    """canonical reduced form of phi^j mod Phi5 as a coeff-tuple (deg<=3)."""
    r = sp.rem(sp.Poly(phi_power_poly(j), x), sp.Poly(Phi5, x)).as_expr()
    p = sp.Poly(sp.expand(r), x)
    return tuple(int(p.coeff_monomial(x**i)) for i in range(4))
for m in ms:
    S      = sorted(canon(4*k)  for k in range(-m,m+1))
    # sigma(phi^{4k}) = (-1/phi)^{4k} = phi^{-4k}
    sigmaS = sorted(canon(-4*k) for k in range(-m,m+1))
    same = (S == sigmaS)
    # trace (sum over the block) -- is it rational (constant poly)?
    tr = sp.rem(sp.Poly(sum(phi_power_poly(4*k) for k in range(-m,m+1)), x),
                sp.Poly(Phi5, x)).as_expr()
    is_rat = sp.Poly(sp.expand(tr), x).degree() <= 0
    print(f"m={m:2d}: sigma-stable multiset={same};  sum_k phi^{{4k}} = {sp.simplify(tr)}  (rational={is_rat})")

# === tau: q->1/q  inverts golden monodromy: phi -> 1/phi, i.e. -eta1 -> eta0.  SWAPS periods ===
print("\n=== tau (q->1/q) action on periods ===")
# phi=-eta1 (period {2,3}); 1/phi = eta0 (period {1,4}); tau sends phi->1/phi
print("tau: phi=-eta1 {2,3}  ->  1/phi=eta0 {1,4}   => tau SWAPS {2,3}<->{1,4}")
print("Phi.tauPhi is tau-symmetric by construction => support must be tau-invariant")
print("=> cannot contain {2,3} without {1,4}  => {2,3}-alone is IMPOSSIBLE for Phi.tauPhi")
