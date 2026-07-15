import sympy as sp

sp.init_printing()
I = sp.I
pi = sp.pi

phi = (1+sp.sqrt(5))/2

h3 = 1/(2*phi) + I*sp.sin(2*pi/5)/sp.sqrt(5)
h3_abs2 = sp.simplify(sp.re(h3)**2 + sp.im(h3)**2)
h3_abs2 = sp.nsimplify(sp.radsimp(sp.simplify(h3_abs2)))
print("h3 =", h3)
print("|h3|^2 exact:", sp.simplify(h3_abs2), " = ", sp.nsimplify(h3_abs2))
print("|h3|^2 rational check:", sp.Rational(h3_abs2) if h3_abs2.is_rational else "not rational, decimal:", sp.N(h3_abs2,30))

# three E6_2 amplitudes: A_j = -(2/sqrt7) sin(2 pi j'/7) zeta_14^k
# (j',k) = (1,3), (3,-2), (2,-1)
params = [(1,3), (3,-2), (2,-1)]
amp_abs2 = {}
for (jp,k) in params:
    A = -(sp.Rational(2)/sp.sqrt(7))*sp.sin(2*pi*jp/7)*sp.exp(I*2*pi*k/14)
    a2 = sp.simplify(sp.Abs(A)**2)
    a2 = sp.simplify(a2)
    amp_abs2[(jp,k)] = a2
    print(f"A(j'={jp},k={k}) |A|^2 exact:", sp.nsimplify(a2), " decimal30:", sp.N(a2,30))

