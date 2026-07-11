import sympy as sp

z, t, x = sp.symbols('z t x')

# order-7 symmetric-cusp mechanism (our own B479 machinery, trusted):
#   tau_7 = 2 cos(2pi/7), minpoly Psi_7(t) = t^3 + t^2 - 2t - 1  (order-7 cyclotomic trace)
#   order-d cusp point solves  z^2 - tau^2 z + 2 tau^2 = 0
Psi7 = t**3 + t**2 - 2*t - 1
# sanity: is t^3+t^2-2t-1 really the minpoly of 2cos(2pi/7)?
val = 2*sp.cos(2*sp.pi/7)
print("Psi_7(2cos2pi/7) simplifies to 0? ->", sp.simplify(Psi7.subs(t, val)))

cusp = z**2 - t**2*z + 2*t**2

# E_7 = eliminate tau  ->  Res_t(Psi_7, cusp)
E7 = sp.resultant(Psi7, cusp, t)
E7 = sp.expand(E7)
print("\nE_7(z) =", E7)
fac = sp.factor(E7)
print("factored over Q:", fac)
poly = sp.Poly(E7, z)
print("degree:", poly.degree(), " irreducible over Q:", len(sp.factor_list(E7)[1])==1 and sp.factor_list(E7)[1][0][1]==1)

# audit's claim: E7 = z^6 -5z^5 +16z^4 -25z^3 +30z^2 -12z +8
audit_E7 = z**6 -5*z**5 +16*z**4 -25*z**3 +30*z**2 -12*z +8
print("matches audit E7 (up to sign/scale)? ratio =", sp.simplify(E7/audit_E7))

# discriminant of E7 and its squarefree part
disc = sp.discriminant(poly)
print("\ndisc(E7) =", disc, " = factored", sp.factor(disc))
sf = sp.factorint(abs(disc))
sqfree = sp.sign(disc)*sp.prod([p for p,e in sf.items() if e%2==1])
print("squarefree part of disc(E7) =", sqfree, "   (audit says -239)")

# Norm over Q(tau_7) of Delta_7 = tau^2 (tau^2 - 8)
Delta = t**2*(t**2-8)
NormDelta = sp.resultant(Psi7, x - Delta, t)  # product over roots of (x - Delta(root))
NormDelta_poly = sp.Poly(NormDelta, x)
# the norm = product of Delta over the 3 roots = (-1)^deg * constant/leading ... use resultant(Psi7,Delta)
norm_val = sp.resultant(Psi7, Delta, t)/sp.LC(Psi7, t)**sp.degree(sp.Poly(Delta,t))
print("\nNorm_{Q(tau7)/Q}(tau^2(tau^2-8)) =", sp.simplify(sp.resultant(Psi7, Delta, t)), " (audit: -239)")
