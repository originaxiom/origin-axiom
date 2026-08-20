"""
Extra robustness / paranoia checks, independent of the main verify.py
code paths where feasible, to stress-test the item-1/2 conclusions.
"""
import sympy as sp
from sympy import symbols, Poly, ZZ, GF

x = symbols('x')
f_expr = x**3 - 12*x - 5
p = 3

print("="*100)
print("CHECK A: Dedekind's criterion at p=3, with a DIFFERENT (symmetric) lift convention")
print("="*100)
# f mod 3 = (x+1)^3 exactly (in char 3, x^3+1=(x+1)^3 by freshman's dream).
# Previous run used lift g = x+1 (coeffs already in [0,3)). Now deliberately
# use a shifted-by-p lift: g' = x+1-3 = x-2  (same class mod 3, different Z[x] rep),
# and h' correspondingly built from that SAME shifted lift, to confirm the
# criterion's conclusion doesn't change (theory says it must not).
g_alt = Poly(x - 2, x, domain=ZZ)          # x-2 == x+1 mod 3, alternate lift
h_alt = Poly((x-2)**2, x, domain=ZZ)       # lift of (x+1)^2 mod 3 using the SAME alternate lift
gh_alt = g_alt*h_alt
f_poly = Poly(f_expr, x, domain=ZZ)
diff_alt = gh_alt - f_poly
print(f"  alt lift g' = {g_alt.as_expr()}, h' = {h_alt.as_expr()}")
print(f"  g'*h' - f = {diff_alt.as_expr()}")
coeffs = diff_alt.all_coeffs()
assert all(c % 3 == 0 for c in coeffs), "alt lift: g'h' != f mod 3 -- should not happen"
T_alt = Poly([c//3 for c in coeffs], x, domain=ZZ)
print(f"  T' = (g'h'-f)/3 = {T_alt.as_expr()}")
Tbar_alt = Poly(T_alt.as_expr(), x, modulus=3)
gbar_alt = Poly(g_alt.as_expr(), x, modulus=3)
hbar_alt = Poly(h_alt.as_expr(), x, modulus=3)
D_alt = sp.gcd(gbar_alt, hbar_alt)
final_alt = sp.gcd(D_alt, Tbar_alt)
print(f"  D' = gcd(gbar',hbar') = {D_alt.as_expr()},  gcd(D',Tbar') = {final_alt.as_expr()}")
print(f"  => still 3-maximal (gcd is a unit/constant): {final_alt.degree()==0}")
print(f"  MATCHES original-lift conclusion (True): {final_alt.degree()==0}")

print()
print("="*100)
print("CHECK B: independent irreducibility test for f mod 13 and mod 17")
print("(via gcd(f, x^p - x): a cubic is reducible over F_p iff it has a root,")
print(" i.e. iff gcd(f, x^p-x) is non-constant -- a DIFFERENT sympy code path")
print(" than factor_list(), used as a cross-check.)")
print("="*100)
for pp in [13, 17]:
    fp = Poly(f_expr, x, modulus=pp)
    xp_x = Poly(x**pp - x, x, modulus=pp)
    g = sp.gcd(fp, xp_x)
    print(f"  p={pp}: gcd(f, x^{pp}-x) mod {pp} = {g.as_expr()}  "
          f"=> {'HAS a root (reducible)' if g.degree()>=1 else 'NO root in F_p => irreducible (cubic w/o root is irreducible)'}")

print()
print("="*100)
print("CHECK C: numeric cross-validation of ALL class-number generators")
print("(product-over-high-precision-roots norm, vs exact integer norm_func)")
print("="*100)
import mpmath as mp
mp.mp.dps = 50
roots = [sp.CRootOf(f_expr, i) for i in range(3)]
roots_hp = [complex(r.evalf(40)) for r in roots]  # should have ~0 imaginary part
roots_hp_real = [mp.mpf(str(sp.re(r.evalf(40)))) for r in roots]

gens = {
    "p=2,(x+1)":        (-1,-2,1),
    "p=2,(x^2+x+1)":    (-1,-3,-1),
    "p=3,(x+1)^3":      (-6,-2,1),
    "p=5,(x)":          (0,-1,0),
    "p=7,(x-3)":        (-1,-2,0),
    "p=7,(x-2)^2":      (-2,-4,-1),
    "p=11,(x-4)":       (-4,1,0),
    "p=11,(x+2)^2":     (-2,-1,0),
    "u1":               (-4,2,1),
    "u2":               (2,6,3),
}

def norm_form_a_b_c():
    a,b,c = symbols('a b c')
    return sp.expand(sp.resultant(f_expr, a+b*x+c*x**2, x))

nf = norm_form_a_b_c()
a,b,c = symbols('a b c')
for label,(aa,bb,cc) in gens.items():
    exact = int(nf.subs({a:aa,b:bb,c:cc}))
    numeric = mp.mpf(1)
    for r in roots_hp_real:
        numeric *= (aa + bb*r + cc*r**2)
    print(f"  {label:20s} (a,b,c)={ (aa,bb,cc) }: exact N = {exact:5d}   numeric product-over-roots = {float(numeric):.6f}   match: {abs(float(numeric)-exact) < 1e-6}")
