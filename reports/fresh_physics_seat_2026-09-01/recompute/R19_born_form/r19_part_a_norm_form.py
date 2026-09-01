"""R19 blind recomputation, part (a): degree of the Galois norm form = order of the swap.

Claim (banked, B725 probe 1):
  |psi|^2 = psi * c(psi) = N_{C/R}(psi) = prod_{g in Gal(C/R)} g(psi) = x^2 + y^2, total degree 2,
  and the degree tracks the swap-group order: an order-3 swap (cyclic cubic Q(2cos 2pi/7),
  minpoly t^3 + t^2 - 2t - 1) gives a degree-3 norm form.

Written BLIND (before opening B725's probe scripts). Everything exact via sympy.
"""
import sympy as sp

report = []


def check(name, ok, detail=""):
    report.append((name, bool(ok), detail))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}")


# ---------- order-2 swap: Gal(C/R) ----------
x, y = sp.symbols("x y", real=True)
psi = x + sp.I * y

# c-swap = complex conjugation; the swap group is {id, c}
cpsi = sp.conjugate(psi)
norm2 = sp.expand(psi * cpsi)
check("N_{C/R}(psi) = psi*c(psi) = x^2+y^2", sp.simplify(norm2 - (x**2 + y**2)) == 0, f"norm2={norm2}")

# product over the Galois group {id, c} equals the same thing
prod_gal = sp.expand(psi * cpsi)
check("prod over Gal(C/R) of g(psi) equals |psi|^2", sp.simplify(prod_gal - norm2) == 0)

# degree of the norm form as a polynomial in (x, y)
deg2 = sp.total_degree(sp.Poly(norm2, x, y))
check("degree of N_{C/R} = 2", deg2 == 2, f"deg={deg2}")

# order of the swap: c is an involution and is not the identity
check("c-swap has order 2 (c(c(psi))=psi, c(psi)!=psi)",
      sp.simplify(sp.conjugate(cpsi) - psi) == 0 and sp.simplify(cpsi - psi) != 0)

# ---------- order-3 swap: cyclic cubic Q(2cos 2pi/7) ----------
t, z = sp.symbols("t z")
p = t**3 + t**2 - 2 * t - 1  # banked minpoly

# (i) 2cos(2pi/7) is a root: substitute t = z + 1/z, multiply by z^3, expect the 7th cyclotomic-ish
lhs = sp.expand((p.subs(t, z + 1 / z)) * z**3)
cyc7 = sp.expand(sum(z**k for k in range(7)) - 0)  # z^6+...+1
check("p(z+1/z)*z^3 = 1+z+...+z^6  (so t=2cos(2pi/7) is a root)",
      sp.expand(lhs - cyc7) == 0, f"lhs={lhs}")

# also numeric confirmation
val = p.subs(t, 2 * sp.cos(2 * sp.pi / 7)).evalf(40)
check("p(2cos 2pi/7) ~ 0 numerically", abs(val) < sp.Float(10) ** -35, f"|p|={val}")

# (ii) sigma: t -> t^2 - 2 is an automorphism of the field, of order 3
pp = sp.Poly(p, t)


def red(expr):
    """reduce a polynomial in t modulo p(t)"""
    return sp.rem(sp.Poly(sp.expand(expr), t), pp).as_expr()


sigma1 = t**2 - 2
check("p(sigma(t)) == 0 mod p(t)  (sigma permutes the roots)", red(p.subs(t, sigma1)) == 0)
sigma2 = red(sigma1.subs(t, sigma1))          # sigma^2(t)
sigma3 = red(sigma1.subs(t, sigma2))          # sigma^3(t)
check("sigma^3 = id, sigma != id, sigma^2 != id  (swap order = 3)",
      sigma3 == t and sigma1 != t and sigma2 != t,
      f"sigma^2(t)={sigma2}")

# (iii) the norm form of a generic element xi = x0 + x1*t + x2*t^2
x0, x1, x2 = sp.symbols("x0 x1 x2")
xi = x0 + x1 * t + x2 * t**2
xi_s = xi.subs(t, sigma1)
xi_s2 = xi.subs(t, sigma2)
norm3 = red(sp.expand(xi * xi_s * xi_s2))

check("N(xi) = xi * sigma(xi) * sigma^2(xi) is t-free (lands in Q)",
      not norm3.has(t), f"N={sp.expand(norm3)}")

poly3 = sp.Poly(sp.expand(norm3), x0, x1, x2)
deg3 = sp.total_degree(poly3)
check("degree of cubic norm form = 3", deg3 == 3, f"deg={deg3}")
check("cubic norm form is homogeneous of degree 3", poly3.is_homogeneous)
check("cubic norm has integer coefficients", all(c.is_Integer for c in poly3.coeffs()))

# cross-check with the resultant construction: N(xi) = Res_t(p(t), X - xi(t)) at X -> and read sign
X = sp.Symbol("X")
res = sp.resultant(p, X - xi, t)  # monic p => product over roots of (X - xi(root))
# norm = prod xi(root) = (-1)^3 * value at X=0 of prod (X - xi(root))
norm_from_res = sp.expand(-res.subs(X, 0))
check("resultant construction agrees with sigma-orbit product",
      sp.expand(norm_from_res - norm3) == 0)

# sanity: norm is multiplicative on a couple of concrete elements (exact)
a_el = 1 + 2 * t
b_el = 3 - t + t**2


def norm_of(e):
    return red(sp.expand(e * e.subs(t, sigma1) * e.subs(t, sigma2)))


nab = norm_of(red(sp.expand(a_el * b_el)))
check("N(ab) = N(a)N(b) (multiplicativity spot check)",
      sp.simplify(nab - norm_of(a_el) * norm_of(b_el)) == 0,
      f"N(a)={norm_of(a_el)}, N(b)={norm_of(b_el)}, N(ab)={nab}")

print()
print("degree-vs-swap-order table (computed):")
print("  Gal(C/R): order 2  -> norm form degree", deg2)
print("  cyclic cubic Q(2cos 2pi/7): order 3 -> norm form degree", deg3)
print("  cubic norm form:", sp.expand(norm3))

fails = [r for r in report if not r[1]]
print()
print("PART A RESULT:", "ALL PASS" if not fails else f"{len(fails)} FAILURES")
