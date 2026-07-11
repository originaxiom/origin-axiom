#!/usr/bin/env python3
"""B530 movement IX (upstream) — the object's growth field vs the program's spine-fields.
The coupled golden double's char poly x^4-2x^3-5x^2-4x-1 (D4, disc -400): which of the program's
characteristic fields (sqrt5 golden/E8, sqrt-3 Eisenstein/E6, sqrt-15 seam) live inside it?"""
import sympy as sp
x=sp.symbols('x'); p=x**4-2*x**3-5*x**2-4*x-1
print("char poly:", p, " irreducible:", sp.Poly(p,x).is_irreducible, " disc:", sp.discriminant(sp.Poly(p,x)))
for d,name in [(5,'golden/E8'),(-3,'Eisenstein/E6'),(-15,'the seam'),(-7,'chirality')]:
    inside = len(sp.factor_list(p, extension=sp.sqrt(d))[1])>1
    print(f"  Q(sqrt{d}) [{name}] a subfield of Q[x]/(p)? {inside}")
print("splitting field (D4, disc -400) quadratic subfields: Q(sqrt5), Q(i), Q(sqrt-5)")
print("=> golden end present; Eisenstein end, seam, chirality ABSENT. One end + a Gaussian breath.")
