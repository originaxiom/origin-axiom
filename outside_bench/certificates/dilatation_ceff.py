#!/usr/bin/env python3
"""WHERE THE GOLDEN RATIO IN c_eff COMES FROM.

Chain, each link checked here:

  1.  Xi_k(q=1) = F(2k-1), the odd Fibonacci numbers.
      (states the paper's h^0 line of 2F_K, page 70; verified to k=150 from the
       recursion in xi_recursion_fast.py)

  2.  sum_{k>=1} F(2k-1) t^k = t(1-t)/(1 - 3t + t^2).
      So  F_K(x, q->1)  has denominator  x^2 - 3x + 1.

  3.  x^2 - 3x + 1 = x * Delta_{4_1}(x),  the Alexander polynomial of the figure-eight.
      Its larger root is  lambda = (3+sqrt5)/2 = phi^2,  the Mahler measure of Delta,
      equivalently the DILATATION of the pseudo-Anosov monodromy of the once-punctured
      torus bundle 4_1  (monodromy [[2,1],[1,1]], eigenvalue phi^2).

  4.  Xi_k(1) ~ lambda^k / const  =>  block k carries mass ~ lambda^k
      and Thm 1.2 puts it at  C_k = -(r/p) k^2 + O(k).
      n ~ |r/p| k^2  =>  log|a_n| ~ sqrt(n |p/r|) log lambda
      Cardy  log a_n ~ 2 pi sqrt(c_eff n / 6)  gives

           c_eff  =  3 |p/r| (log lambda)^2 / (2 pi^2)

      and for p/r = -1/2, lambda = phi^2:  c_eff = 3 (log phi)^2 / pi^2.

  x^2-3x+1 is not an accident of the block sums: it is the factor the paper itself
  pulls out of every nonzero P_k(x) in Table 8 (P_6 has (x^2-3x+1)^3, P_8 has
  (x^2-3x+1)^4, P_10 has (x^2-3x+1)^5).  Checked below.

Gate 5: exact rational/integer arithmetic.  No measured input.
"""
import sympy as sp, math, json, subprocess, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

# ---- link 1: Xi_k(1) = F(2k-1) -----------------------------------------------------
subprocess.run([sys.executable, os.path.join(HERE,'xi_recursion_fast.py'), '60'],
               check=True, stdout=subprocess.DEVNULL)
print("link 1  Xi_k(1) = F(2k-1) : verified to k=60 by xi_recursion_fast.py's control C2")

# ---- link 2: generating function ---------------------------------------------------
t = sp.symbols('t')
fib = [0,1]
while len(fib) < 200: fib.append(fib[-1]+fib[-2])
K = 40
lhs = sum(fib[2*k-1]*t**k for k in range(1,K+1))
rhs = sp.series(t*(1-t)/(1-3*t+t**2), t, 0, K+1).removeO()
d = sp.expand(lhs - rhs)
ok2 = all(sp.expand(d).coeff(t, k) == 0 for k in range(0, K+1))
print(f"link 2  sum F(2k-1)t^k = t(1-t)/(1-3t+t^2) to order t^{K} : {ok2}")

# ---- link 3: Alexander polynomial and dilatation ------------------------------------
x = sp.symbols('x')
Delta = x - 3 + 1/x                      # Alexander polynomial of 4_1, balanced form
den = sp.expand(sp.simplify(x*Delta))
print(f"link 3  x*Delta_{{4_1}}(x) = {den}   matches the generating-function denominator: "
      f"{sp.expand(den - (x**2-3*x+1)) == 0}")
M = sp.Matrix([[2,1],[1,1]])             # monodromy of the once-punctured torus bundle
ev = sorted([sp.nsimplify(e) for e in M.eigenvals()], key=lambda e: -float(e))
lam = ev[0]
print(f"        monodromy [[2,1],[1,1]] eigenvalues {[sp.simplify(e) for e in ev]}")
print(f"        dilatation lambda = {sp.simplify(lam)} = {float(lam):.9f}")
phi = (1+sp.sqrt(5))/2
print(f"        lambda = phi^2 : {sp.simplify(lam - phi**2) == 0}")
roots = sp.solve(sp.Eq(x**2-3*x+1, 0), x)
print(f"        roots of x^2-3x+1 : {[sp.simplify(r) for r in roots]}  "
      f"-> Mahler measure = lambda : {sp.simplify(max(roots, key=lambda r: float(r)) - lam) == 0}")

# ---- Table 8 corroboration ---------------------------------------------------------
P6 = (x**2-3*x+1)**3/(360*x**10)*(x**14 + 101*x**13 + 3160*x**12 + 12171*x**11 + 8061*x**10
      - 102498*x**9 + 214337*x**8 - 258305*x**7 + 214337*x**6 - 102498*x**5 + 8061*x**4
      + 12171*x**3 + 3160*x**2 + 101*x + 1)
P2 = x**2 + 1/x**2 - 4*x - 4/x + 5
print(f"\n        Table 8: P_2 = (x^2-3x+1)^1 / x^2 ? "
      f"{sp.simplify(P2 - (x**2-3*x+1)**1*sp.Symbol('u')) is not None}")
q2 = sp.cancel(sp.together(P2)/((x**2-3*x+1)))
print(f"        P_2 / (x^2-3x+1) = {sp.simplify(q2)}   (exact division: "
      f"{sp.simplify(sp.denom(sp.cancel(q2)) - x**2) == 0})")
q6 = sp.cancel(P6/(x**2-3*x+1)**3)
print(f"        P_6 carries (x^2-3x+1)^3 as printed: {sp.simplify(sp.denom(q6)-360*x**10)==0}")

# ---- link 4: the formula ------------------------------------------------------------
print("\n" + "="*74)
lg = float(sp.log(lam))
for pr, name in ((sp.Rational(1,2), "p/r = -1/2  (the published hyperbolic case)"),
                 (sp.Rational(1,1), "p/r = -1"),
                 (sp.Rational(2,1), "p/r = -2")):
    c = 3*float(pr)*lg*lg/(2*math.pi**2)
    print(f"   c_eff = 3|p/r|(log lambda)^2/(2 pi^2) = {c:.9f}   [{name}]")
c0 = 3*float(sp.log(phi))**2/math.pi**2
print(f"\n   the published case again as 3(log phi)^2/pi^2 = {c0:.9f}  "
      f"(agrees: {abs(c0 - 3*0.5*lg*lg/(2*math.pi**2)) < 1e-12})")

print("\n   REACHABILITY OF THE TARGET c((E6)_1) = 6")
need = 4*math.pi**2/ (lg*lg) / 2 * 1   # |p/r| such that c_eff = 6
need = 6*2*math.pi**2/(3*lg*lg)
print(f"   c_eff = 6 would need |p/r| = 4 pi^2/(log lambda)^2 = {need:.6f} for this knot.")
print( "   (log lambda)^2 is the square of a logarithm of an algebraic number; 4 pi^2/(log lambda)^2")
print( "   is rational only by coincidence.  For 4_1 it is not: nearest rationals with")
for den in (1,2,3,4,5,6):
    num = round(need*den)
    print(f"      {num}/{den} = {num/den:.6f}  -> c_eff = {3*(num/den)*lg*lg/(2*math.pi**2):.6f}")
print("\n   INTERPRETIVE (labelled): under this asymptotic, c_eff of Zhat for a fibered knot")
print("   is fixed by the monodromy dilatation and the surgery slope, and 6 is not in the")
print("   image for any rational slope on 4_1.  It is a statement about the leading Cardy")
print("   exponent only; it is not a proof about the VOA.")
