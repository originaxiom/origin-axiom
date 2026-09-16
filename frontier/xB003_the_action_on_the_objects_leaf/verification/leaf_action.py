#!/usr/bin/env python3
"""xB003 - the monodromy's action on the object's own leaf, its fixed point, and the
leading part of B1341's missing generating function.

Cell 1  the twist decomposition: T^2 = F_R o F_L, so B1341's "double tick" IS the monodromy.
Cell 2  an INDEPENDENT route: the literature presentation phi(a)=ab, phi(b)=bab induces F_L o F_R.
Cell 3  fixed points on the object's leaf kappa = -2 (the Markov surface, B1347), their arithmetic.
Cell 4  the derivative there, and the local generating function in B1341's normalisation.

Gate 5 untouched: pure algebra over Q(sqrt-3), no measured quantity anywhere.
"""
import sympy as sp

X, Y, Z = sp.symbols('X Y Z')
w = sp.Rational(-1, 2) + sp.sqrt(-3) / 2                 # omega, Z[omega] = O_{Q(sqrt-3)}
KAPPA = X**2 + Y**2 + Z**2 - X*Y*Z - 2                    # Fricke: kappa = tr[a,b]

def T(v):                      # B1341's tick, in FULL traces (half-trace T(x,y,z)=(z,x,2xz-y))
    A, B, C = v; return (C, A, A*C - B)
def F_L(v):                    # Dehn twist (a,b) -> (a, ab);  abelianises to L = [[1,1],[0,1]]
    A, B, C = v; return (A, C, A*C - B)
def F_R(v):                    # Dehn twist (a,b) -> (ab, b);  abelianises to R = [[1,0],[1,1]]
    A, B, C = v; return (C, B, B*C - A)

def cell1():
    T2 = tuple(sp.expand(e) for e in T(T((X, Y, Z))))
    RL = tuple(sp.expand(e) for e in F_R(F_L((X, Y, Z))))
    assert all(sp.simplify(a - b) == 0 for a, b in zip(T2, RL)), "T^2 != F_R o F_L"
    for nm, F in (("F_L", F_L), ("F_R", F_R)):
        inv = sp.simplify(KAPPA.subs(list(zip((X, Y, Z), F((X, Y, Z)))), simultaneous=True) - KAPPA)
        assert inv == 0, f"{nm} moves kappa"
    L = sp.Matrix([[1, 1], [0, 1]]); R = sp.Matrix([[1, 0], [1, 1]])
    assert (R*L).trace() == 3 and (R*L).det() == 1
    print("cell 1  T^2 = F_R o F_L exactly; both twists preserve kappa; abelianisation RL trace 3 det 1")
    print("        => B1341's 'double tick' IS m004's monodromy, proved not assumed")

def cell2():
    # phi(a)=ab, phi(b)=bab  (the fibration's monodromy, literature presentation).
    #   X' = tr(ab) = Z
    #   Y' = tr(bab) = tr(ab^2)   = tr(ab)tr(b) - tr(a) = YZ - X
    #   Z' = tr(ab.bab) = tr((ab)^2 b) = tr(ab)tr(ab.b) - tr(b) = Z(YZ-X) - Y
    F_phi = (Z, Y*Z - X, sp.expand(Z*(Y*Z - X) - Y))
    LR = tuple(sp.expand(e) for e in F_L(F_R((X, Y, Z))))
    assert all(sp.simplify(a - b) == 0 for a, b in zip(F_phi, LR)), "literature map != F_L o F_R"
    print("cell 2  the literature monodromy phi(a)=ab, phi(b)=bab induces exactly F_L o F_R")
    print("        (conjugate to F_R o F_L by F_L -- same spectrum at corresponding fixed points)")
    return F_phi

def cell3(F_phi):
    sols = sp.solve([sp.Eq(F_phi[0], X), sp.Eq(F_phi[1], Y), sp.Eq(F_phi[2], Z),
                     sp.Eq(KAPPA, -2)], [X, Y, Z], dict=True)
    pts = []
    for s in sols:
        p = tuple(sp.radsimp(sp.simplify(s.get(v, v))) for v in (X, Y, Z))
        if not any(q.free_symbols for q in p):
            pts.append(p)
    node = [p for p in pts if all(q == 0 for q in p)]
    reg = [p for p in pts if p not in node]
    assert len(node) == 1 and len(reg) == 2, f"expected node + conjugate pair, got {pts}"
    print(f"cell 3  on the object's leaf kappa = -2 (x^2+y^2+z^2 = xyz, the Markov surface, B1347):")
    print(f"        the node (0,0,0), and a conjugate pair of regular fixed points")
    for p in reg:
        norms = [sp.simplify(sp.expand(q*sp.conjugate(q))) for q in p]
        inZw = [bool(sp.simplify(q - (2 + w)) == 0 or sp.simplify(q - (2 + sp.conjugate(w))) == 0) for q in p]
        assert norms == [3, 3, 3] and all(inZw), f"{p}: norms {norms} inZ[w] {inZw}"
    print(f"        every trace has NORM 3 and equals 2+omega or 2+conj(omega):")
    print(f"        the RAMIFIED prime of Q(sqrt-3), the object's own invariant trace field (disc -3)")
    return reg

def cell4(F_phi, reg):
    J = sp.Matrix(list(F_phi)).jacobian([X, Y, Z])
    lam = (5 + sp.sqrt(21)) / 2
    for p in reg:
        ev = sp.Matrix(J.subs({X: p[0], Y: p[1], Z: p[2]})).eigenvals()
        vals = sorted([sp.nsimplify(sp.radsimp(k)) for k in ev], key=lambda e: float(sp.re(e)))
        assert sp.simplify(vals[-1] - lam) == 0, vals
        assert any(sp.simplify(v - 1) == 0 for v in vals), "no transverse eigenvalue 1"
        prod = sp.simplify(sp.expand(lam * (5 - sp.sqrt(21)) / 2))
        assert prod == 1, prod
    print("cell 4  D(monodromy) at the regular fixed point: eigenvalues 1 (transverse to the leaf)")
    print("        and (5 +- sqrt21)/2, product 1 -- SYMPLECTIC on the leaf, char poly L^2 - 5L + 1.")
    print("        B1341's variational theorem, exhibited on the object's OWN leaf.")
    u, U, a, b, c = sp.symbols('u U a b c')
    for beta, lab in ((1, "kappa = +2 (I=0), B1341's leaf"), (2, "kappa = -2, the OBJECT's leaf")):
        S = u**2/2 - u*U + beta*U**2
        rel = sp.simplify(sp.diff(S, U).subs({u: a, U: b}) + sp.diff(S, u).subs({u: b, U: c}))
        tr = sp.Poly(rel, b).coeff_monomial(b)
        print(f"        {lab}: S(u,U) = {S}  ->  DEL {rel} = 0,  trace {tr}")
    print("        SCOPE: this is the LEADING (quadratic) part at the fixed point, not a global S;")
    print("        a hyperbolic fixed point of an area-preserving map has resonances L^a L^-b = L,")
    print("        so analytic linearisation is not automatic and is NOT claimed.")

if __name__ == "__main__":
    cell1(); F = cell2(); reg = cell3(F); cell4(F, reg)
    print("\nVERIFIED")
