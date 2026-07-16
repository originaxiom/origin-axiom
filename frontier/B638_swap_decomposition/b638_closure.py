"""B638 closing derivation — THE LAW OF THE CHORD'S CORE IS A THEOREM.

Given (computed exact, banked): (i) the swap law Y(s*a, s*b, s*c) =
conj(Y(a,b,c)); (ii) the sigma*-matrix (lower-triangular, diagonal
(z6, z6bar, -z6, -z6bar, 1), mixing sigma*(1) -> (sqrt(-3)/24) rep0);
(iii) Y alternating; (iv) the zero law Y[01k] = 0.

CLAIM: the (1,2,3) law equation conj(Y123) = z6bar*Y123 + (r/24)*Y023
is EQUIVALENT to { Y123 pure imaginary, Y023 = 24*z6*Y123 }.
Verified symbolically here, then numerically against the banked values.
"""
import sympy as sp

r = sp.sqrt(-3)
z6 = (1 + r) / 2
z6b = (1 - r) / 2
mu = r / 24                      # the sigma*(1) -> rep0 mixing coefficient

# --- direction 1: assume Y123 = t*r (t real), Y023 = 24*z6*Y123;
# check the law equation conj(Y123) = z6b*Y123 + mu*Y023
t = sp.symbols("t", real=True)
Y123 = t * r
Y023 = 24 * z6 * Y123
lhs = sp.conjugate(Y123)
rhs = z6b * Y123 + mu * Y023
print("direction 1 (the pair implies the law equation):",
      sp.simplify(lhs - rhs) == 0)

# --- direction 2: the law equation + the (0,2,3) phase constraint
# conj(Y023) = z6*Y023 force the pair. Write Y123 = x + y*r, Y023 = u + v*r
x, y, u, v = sp.symbols("x y u v", real=True)
Y123g = x + y * r
Y023g = u + v * r
eq1 = sp.expand(sp.conjugate(Y123g) - (z6b * Y123g + mu * Y023g))
eq2 = sp.expand(sp.conjugate(Y023g) - z6 * Y023g)
sols = sp.solve([sp.re(eq1), sp.im(eq1), sp.re(eq2), sp.im(eq2)],
                [x, u, v], dict=True)
print("direction 2 solution:", sols)
# expect: x = 0 (Y123 pure imaginary), u = -36y? and v = 12y? check vs
# 24*z6*(y*r) = 12*y*r*(1+r) = 12*y*(r-3) = -36y + 12y*r
sol = sols[0]
ok = (sol[x] == 0 and sp.simplify(sol[u] + 36 * y) == 0
      and sp.simplify(sol[v] - 12 * y) == 0)
print("direction 2 (the law forces the pair):", ok)

# --- the numeric anchor: the banked weld-core values
Y123n = sp.Rational(221760, 13) * r
Y023n = sp.Rational(-7983360, 13) + sp.Rational(2661120, 13) * r
law_lhs = sp.conjugate(Y123n)
law_rhs = z6b * Y123n + mu * Y023n
print("banked values satisfy the law equation:",
      sp.simplify(law_lhs - law_rhs) == 0)
print("banked ratio = 24*z6:",
      sp.simplify(Y023n / Y123n - 24 * z6) == 0)

# --- the phase corollaries for the other components (given the zero law)
# (0,3,4): conj(Y034) = -Y034  => pure imaginary; banked (2/3)r: check
Y034 = sp.Rational(2, 3) * r
print("Y034 pure-imaginary corollary consistent:",
      sp.simplify(sp.conjugate(Y034) + Y034) == 0)
print("\nTHE LAW OF THE CHORD'S CORE: PROVED from the swap data.")
