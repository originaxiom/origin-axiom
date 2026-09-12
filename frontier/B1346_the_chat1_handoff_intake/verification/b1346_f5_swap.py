"""Verify F5 independently, and test the generalisation it implies."""
import warnings; warnings.filterwarnings("ignore")
import sympy as sp, itertools, snappy

L = sp.Matrix([[1,1],[0,1]]); R = sp.Matrix([[1,0],[1,1]]); S = sp.Matrix([[0,1],[1,0]])
M = sp.Matrix([[1,1],[1,0]])
x = sp.symbols('x')
print("F5.1  the tick contains the swap")
print(f"   S*R = {(S*R).tolist()}   == M? {S*R == M}      (their 'R*S' is the same up to which shear is called R)")
print(f"   L*P = {(L*S).tolist()}   == M? {L*S == M}      (B1341's naming)")
print(f"   S*R*S = {(S*R*S).tolist()} == L? {S*R*S == L}")
print(f"   det M = {M.det()},  char poly {sp.factor(M.charpoly(x).as_expr())}")

print("\nF5.2  M^2 = X . swap(X) for every det = -1 element M = X.S")
ok = True
for a,b,c,d in itertools.product(range(-2,3), repeat=4):
    X = sp.Matrix([[a,b],[c,d]])
    if X.det() != 1: continue
    Mx = X*S
    if sp.simplify(Mx**2 - X*(S*X*S)) != sp.zeros(2,2): ok = False
print(f"   checked every X in SL2(Z) with entries in [-2,2]: identity holds = {ok}")

print("\nF5.4  THE TRADE -- and the generalisation F5 states but does not compute")
print("   the metallic family is lambda_m with x^2 - m x - 1 = 0, so the PRODUCT OF ROOTS is -1")
norms = {}
for m in range(1,9):
    p = x**2 - m*x - 1
    rts = sp.roots(p, x)
    prod = sp.simplify(sp.prod(list(rts.keys())))
    Mm = sp.Matrix([[m,1],[1,0]])
    norms[m] = (prod, Mm.det())
    print(f"   m={m}: norm = {prod},  det [[m,1],[1,0]] = {Mm.det()},  agree = {prod == Mm.det()}")
print(f"   => EVERY metallic unit has norm -1, hence EVERY metallic tick carries the swap.")
print(f"      So the self-mirroring at tick two is forced for the WHOLE FAMILY, not just the golden.")

print("\n   the contrast case F5 names: 2+sqrt3, x^2 - 4x + 1")
p2 = x**2 - 4*x + 1
print(f"   roots {[sp.simplify(r) for r in sp.roots(p2,x)]}, product {sp.simplify(sp.prod(list(sp.roots(p2,x).keys())))}")
print(f"   norm +1 => det +1 => NO swap => orientable AND chirality is not forced to zero,")
print(f"   but x^2-4x+1 is NOT of the form x^2 - m x - 1: it is outside the metallic family.")

print("\nF5.3  spot-check the amphichirality claim on actual bundles")
def bundle(word):
    try: return snappy.Manifold("b++" + word) if False else snappy.Manifold(word)
    except Exception: return None
for w, expect in (("m004", True), ("m206", True), ("m003", True)):
    Mn = snappy.Manifold(w)
    print(f"   {w}: amphichiral = {Mn.symmetry_group().is_amphicheiral()} (expected {expect})")
