"""Locks for B425 -- the GEOMETRIC Reidemeister torsion at rho_geo (Eisenstein) vs B423's
DYNAMICAL zeta (golden): the object's two torsions = the two cornerstone sides.

Loads the banked JSON for the full claims, and INDEPENDENTLY recomputes the decisive facts
(holonomy forces u=omega; adjoint geometric torsion = -3; sqrt(-3) cancels by Galois-invariance)
so the lock does not merely trust the JSON."""
import json, os, sys

HERE = os.path.join(os.path.dirname(__file__), "..", "frontier", "B425_geometric_torsion")
R = json.load(open(os.path.join(HERE, "geometric_torsion.json")))
sys.path.insert(0, HERE)
import geometric_torsion as G


# ---- claims from the banked JSON ----
def test_holonomy_is_eisenstein():
    # rho(relator)=I forces u^2+u+1=0  => u=omega, trace field Q(sqrt-3)
    assert R["holonomy_forces"] == "u**2 + u + 1"

def test_alexander_sanity():
    # trivial rep must reproduce the ordinary Alexander polynomial of 4_1 = t^2-3t+1
    assert R["alexander_sanity"] == "(t**2 - 3*t + 1)/(t*(t - 1))"

def test_two_torsions_split_the_two_discriminants():
    assert R["adjoint_geometric"] == "-3"   # disc Q(sqrt-3), Eisenstein (holonomy side)
    assert R["adjoint_dynamical"] == "-5"    # disc Q(sqrt5),  golden    (monodromy side)

def test_sqrt_m3_cancels_all_exponents():
    # the geometric torsion is Galois-invariant under Gal(Q(sqrt-3)/Q) at every E6 exponent
    assert R["sqrt_m3_cancels_all_exponents"] is True
    assert all(R["galois_invariant"][str(m)] for m in (1, 4, 5, 7, 8, 11))

def test_eisenstein_present_in_fox_matrix_but_cancels_in_torsion():
    # sqrt(-3) survives in the Fox matrix (trace complex) at every exponent...
    assert all(R["eisenstein_presence"][str(m)]["eisenstein_present"] for m in (1,4,5,7,8,11))
    # ...yet the torsion (determinant) is rational: NOT the golden dynamical value
    assert R["adjoint_geometric"] != R["adjoint_dynamical"]

def test_adjoint_polynomial_is_3_governed_not_golden():
    # geometric adjoint numerator t^2-5t+1: roots in Q(sqrt21) (disc 21=3*7), not golden
    assert R["geom_polys"]["1"] == "(t - 1)*(t**2 - 5*t + 1)/t**3"


# ---- independent recomputation (does not trust the JSON) ----
PRIMES = [p for p in range(1000003, 1002000) if p % 3 == 1 and G.is_prime(p)][:6]

def test_independent_adjoint_is_minus_three():
    W = G.geom_TA(2, PRIMES)                 # Sym^2 twisted Alexander at rho_geo
    assert str(G.reg_at_1(W)) == "-3"

def test_independent_galois_invariance_m1_and_m11():
    # the crux: sqrt(-3) cancels (Galois-fixed determinant) -- check the cheapest and the
    # hardest exponent independently
    assert G.galois_invariant(2, PRIMES) is True     # m=1
    assert G.galois_invariant(22, PRIMES) is True     # m=11 (where full-poly CRT overflows)

def test_dynamical_zeta_is_golden_by_construction():
    # B423's object: det(I - Sym^{2m}(A)), A = golden cat map => -5 at m=1
    assert str(G.dyn_zeta(1)) == "-5"


def test_raw_eigenvalue_product_is_not_an_invariant():
    """Guard against the cross-chat '-25-13w / prime 67' claim: the product of the two
    nonzero Fox eigenvalues is NOT a knot invariant -- it is rational for dr/da, complex
    for dr/db, and t-dependent. Only the NORMALIZED determinant (=-3) is the invariant."""
    import sympy as sp
    w = sp.Rational(-1,2) + sp.sqrt(3)/2*sp.I
    ra = sp.Matrix([[1,1],[0,1]]); rb = sp.Matrix([[1,0],[-w,1]])
    def sym2(M):
        x,y = sp.symbols('x y'); nx = M[0,0]*x+M[0,1]*y; ny = M[1,0]*x+M[1,1]*y
        cols = []
        for i in range(3):
            p = sp.expand(nx**i*ny**(2-i)); cols.append([p.coeff(x,j).coeff(y,2-j) for j in range(3)])
        return sp.Matrix([[cols[c][r] for c in range(3)] for r in range(3)])
    RA, RB = sym2(ra), sym2(rb)
    def inv(word): return [(g,-e) for g,e in reversed(word)]
    A=[('a',1)]; B=[('b',1)]; wd=B+inv(A)+inv(B)+A; r=A+wd+inv(B)+inv(wd)
    def fox(word,x):
        ts=[]; pre=[]
        for (g,e) in word:
            if e==1:
                if g==x: ts.append((list(pre),1))
                pre=pre+[(g,1)]
            else:
                pre=pre+[(g,-1)]
                if g==x: ts.append((list(pre),-1))
        return ts
    def foxmat(deriv,tv):
        S=sp.zeros(3,3)
        for (word,sign) in fox(r,deriv):
            M=sp.eye(3)
            for (g,e) in word:
                base=RA if g=='a' else RB; M=M*(base**e)
            texp=sum(e for (g,e) in word)
            S += sign*M*(tv**texp)
        return S
    def e2(M): return sp.simplify((M.trace()**2-(M*M).trace())/2)
    # dr/da eigenvalue-product is RATIONAL; dr/db is COMPLEX -> not intrinsic
    ea1 = sp.simplify(e2(foxmat('a', sp.Integer(1))))
    eb1 = sp.simplify(e2(foxmat('b', sp.Integer(1))))
    assert ea1 == -3 and sp.im(ea1) == 0            # rational for dr/da
    assert sp.im(eb1) != 0                           # complex for dr/db (presentation artifact)
    # it VARIES with t (not an invariant)
    assert sp.simplify(e2(foxmat('a', sp.Integer(2)))) != ea1
    # the NORMALIZED determinant IS the invariant = -3
    t = sp.symbols('t')
    W = sp.cancel(foxmat('b', t).det() / (RA*t - sp.eye(3)).det())
    assert sp.factor(W) == sp.factor((t-1)*(t**2-5*t+1)/t**3)
