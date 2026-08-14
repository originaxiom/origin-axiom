import sympy as sp
s=sp.symbols('s'); mu=s**3-12*s-5
def report(expr,tag):
    P=sp.Poly(sp.together(expr),s)
    co=[sp.nsimplify(x) for x in P.all_coeffs()]
    den=sp.lcm([sp.denom(x) for x in co]); co=[sp.Integer(x*den) for x in co]
    g=sp.gcd(co); co=[c//g for c in co]
    ker=sorted(p for p,e in sp.factorint(sp.discriminant(sum(co[i]*s**(3-i) for i in range(4)),s)).items() if e%2)
    print(" %-10s coeffs=%s | P_lead=%s P_const=%s | disc squarefree kernel=%s"%(
        tag,co,sorted(sp.factorint(abs(co[0]))),sorted(sp.factorint(abs(co[-1]))),ker))
report(mu,"c=1")
for c in [13,7,sp.Rational(1,13),sp.Rational(2,3),sp.Rational(3,5)]:
    report(sp.expand(mu.subs(s,s/c)*c**3),"c=%s"%c)
