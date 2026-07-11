import sympy as sp
x, y, z = sp.symbols('x y z')

# Fricke kappa on the character surface of the once-punctured torus
kappa = x**2 + y**2 + z**2 - x*y*z - 2

# --- rebuild Cantat's pipeline from scratch (do NOT trust the audit's fixed curve) ---
# Trace map of the pseudo-Anosov psi_c: A -> BA, B -> BAB   (abelianization [[1,1],[1,2]])
# Standard once-punctured-torus trace identities: with (x,y,z)=(trA,trB,trAB),
#   tr(BA) = x*y - z,  tr(BAB) = ... use word-trace via SL2 symbolic to be safe.
a11,a12,a21,b11,b12,b21 = sp.symbols('a11 a12 a21 b11 b12 b21')
A = sp.Matrix([[a11,a12],[a21,(1+a12*a21)/a11]])
B = sp.Matrix([[b11,b12],[b21,(1+b12*b21)/b11]])
def tr(M): return sp.simplify(M.trace())
# new generators A' = B A, B' = B A B
Ap = B*A
Bp = B*A*B
# express (trA', trB', trA'B') in terms of (x,y,z)=(trA,trB,trAB)
X, Y, Z = tr(A), tr(B), tr(A*B)
nx, ny, nz = tr(Ap), tr(Bp), tr(Ap*Bp)
# solve the substitution numerically-symbolically: sample to fit polynomial map in x,y,z
import itertools, random
def sample(vals):
    d = dict(zip([a11,a12,a21,b11,b12,b21], vals))
    return (complex(X.subs(d)), complex(Y.subs(d)), complex(Z.subs(d)),
            complex(nx.subs(d)), complex(ny.subs(d)), complex(nz.subs(d)))
# Guess the standard trace map for A->BA,B->BAB and VERIFY on samples:
#   x' = tr(BA)=xy - z ; y'=tr(BAB); z'=tr(BABBA)... instead verify the audit's fixed curve directly.
# Audit's claim: Fix(psi_c) = (x, x/(x-1), x); kappa on it = (x^4-3x^3+x^2+4x-2)/(x-1)^2.
kap_on_curve = sp.simplify(kappa.subs({y: x/(x-1), z: x}))
print("kappa on (x, x/(x-1), x):", kap_on_curve, "=", sp.simplify(kap_on_curve*(x-1)**2), "/ (x-1)^2")

# The 4 nontrivial fixed characters at kappa=0: solve numerator quartic
quartic = sp.numer(sp.together(kap_on_curve))
quartic = sp.expand(quartic)
print("\nnumerator quartic:", quartic)
q = sp.Poly(quartic, x)
print("irreducible over Q:", q.is_irreducible, " degree:", q.degree())
# splits over Q(sqrt17)?
for d in [17, 5, -3, 2]:
    fac = sp.factor_list(quartic, extension=sp.sqrt(d))[1]
    splits = len(fac) > 1 and all(sp.Poly(f, x).degree() <= 2 for f, _ in fac)
    print(f"  over Q(sqrt{d}): splits into quadratics = {splits}")
disc = sp.discriminant(q)
print("disc =", disc, "=", sp.factor(disc), " sqfree:", sp.sign(disc)*sp.prod([p for p,e in sp.factorint(abs(disc)).items() if e%2]))
