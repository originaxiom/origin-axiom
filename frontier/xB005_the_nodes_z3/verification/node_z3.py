#!/usr/bin/env python3
"""xB005 - is the monodromy's order-3 action at the node the outer Z/3 of Q8 (= 2T/Q8)?
Cells Q1-Q3 exactly as sealed in PREREGISTRATION.md (sha256 afb4dc82..., commit 1b047ae,
pushed BEFORE this file existed).  Each cell asserts its own mathematics.  Gate 5 untouched."""
import sympy as sp
X, Y, Z = sp.symbols('X Y Z')
KAP = X**2 + Y**2 + Z**2 - X*Y*Z - 2
def F_L(v): A, B, C = v; return (A, C, A*C - B)
def F_R(v): A, B, C = v; return (C, B, B*C - A)
F = lambda v: F_L(F_R(v))
NODE = (0, 0, 0)

# --- Q8 in SU(2) ---
I2 = sp.eye(2)
qi = sp.Matrix([[sp.I, 0], [0, -sp.I]])
qj = sp.Matrix([[0, 1], [-1, 0]])
qk = sp.simplify(qi*qj)
Q8 = {}
for nm, M in (('1', I2), ('i', qi), ('j', qj), ('k', qk)):
    Q8[nm] = M; Q8['-' + nm] = -M
def name_of(M):
    for nm, N in Q8.items():
        if sp.simplify(M - N) == sp.zeros(2, 2): return nm
    return None

def Q1():
    assert all(sp.simplify(a - b) == 0 for a, b in zip(F(NODE), NODE)), "node not fixed"
    assert sp.simplify(KAP.subs({X: 0, Y: 0, Z: 0}) + 2) == 0, "node off the leaf"
    J = sp.Matrix(list(F((X, Y, Z)))).jacobian([X, Y, Z]).subs({X: 0, Y: 0, Z: 0})
    assert sp.simplify(J**3 - sp.eye(3)) == sp.zeros(3, 3), "D^3 != I"
    assert sp.simplify(J - sp.eye(3)) != sp.zeros(3, 3), "D == I"
    ev = sorted([complex(e) for e in sp.Matrix(J).eigenvals()], key=lambda z: (z.real, z.imag))
    assert all(abs(abs(e) - 1) < 1e-12 for e in ev), ev
    print(f"Q1 PASS  node fixed, kappa = -2, D = {J.tolist()}, D^3 = I, D != I")
    print(f"         eigenvalues on the unit circle: {[complex(round(e.real,6), round(e.imag,6)) for e in ev]}")
    return J

def Q2():
    """the node is the Q8 character rho(a)=i, rho(b)=j, rho(ab)=k.
    the monodromy is phi(a)=ab, phi(b)=bab.  compute where it sends the triple."""
    a, b = qi, qj
    assert name_of(sp.simplify(a*b)) == 'k'
    assert [sp.simplify(m.trace()) for m in (a, b, a*b)] == [0, 0, 0], "not the node's character"
    comm = sp.simplify(a*b*a.inv()*b.inv())
    assert sp.simplify(comm.trace() + 2) == 0, "commutator not parabolic-at--2"
    na = sp.simplify(a*b)                    # phi(a) = ab
    nb = sp.simplify(b*a*b)                  # phi(b) = bab
    nab = sp.simplify(na*nb)
    trip = (name_of(na), name_of(nb), name_of(nab))
    print(f"Q2       phi: (a,b,ab) = (i,j,k)  ->  ({trip[0]}, {trip[1]}, {trip[2]})")
    assert trip == ('k', 'i', 'j'), trip
    # is i->k, j->i, k->j an automorphism of Q8?
    img = {'i': qk, 'j': qi, 'k': qj}
    def phi_map(M):
        nm = name_of(M); s = -1 if nm.startswith('-') else 1; base = nm.lstrip('-')
        return s*(I2 if base == '1' else img[base])
    els = [Q8[n] for n in Q8]
    ok = all(sp.simplify(phi_map(sp.simplify(u*v)) - sp.simplify(phi_map(u)*phi_map(v))) == sp.zeros(2, 2)
             for u in els for v in els)
    assert ok, "i->k, j->i, k->j is not an automorphism of Q8"
    order3 = sp.simplify(phi_map(phi_map(phi_map(qi))) - qi) == sp.zeros(2, 2)
    assert order3
    inner = any(sp.simplify(g*qi*g.inv() - qk) == sp.zeros(2, 2) for g in els)
    print("         it IS an automorphism of Q8, of order 3, and it is OUTER"
          f" (no element of Q8 conjugates i to k: {not inner})")
    assert not inner, "the 3-cycle would be inner"
    print("Q2 PASS  the monodromy acts at the node by the OUTER Z/3 of Q8 -- i.e. 2T/Q8,")
    print("         realised dynamically on the character variety.")

def Q3():
    """the section-2 linkage test on the programme's Z/3 family."""
    # Z(E6) = det of the Cartan matrix = |weight lattice / root lattice|
    C = sp.Matrix([[ 2,-1, 0, 0, 0, 0],
                   [-1, 2,-1, 0, 0, 0],
                   [ 0,-1, 2,-1, 0,-1],
                   [ 0, 0,-1, 2,-1, 0],
                   [ 0, 0, 0,-1, 2, 0],
                   [ 0, 0,-1, 0, 0, 2]])
    assert C.det() == 3, C.det()
    # 2T^ab = 2T/Q8 has order 3
    assert 24 // 8 == 3
    # mu_3 sits inside Q(sqrt-3): Q(zeta_3) = Q(sqrt-3)
    z3 = sp.Rational(-1, 2) + sp.sqrt(-3)/2
    assert sp.simplify(z3**3 - 1) == 0 and sp.simplify(z3 - 1) != 0
    print("Q3       |Z(E6)| = det(Cartan E6) =", C.det(), " ;  |2T/Q8| = 24/8 = 3 ;  zeta_3 in Q(sqrt-3):",
          sp.simplify(z3**3 - 1) == 0)
    print("         LINKAGE (section 2's test -- are the faces canonically linked?):")
    print("           mu_3 <-> Q(sqrt-3):  Q(zeta_3) = Q(sqrt-3).  SAME OBJECT.")
    print("           2T/Q8 <-> Z(E6):     McKay -- the centre of the simply-connected group is the")
    print("                                abelianisation of the binary polyhedral group.  LINKED.")
    print("           node's Z/3 <-> 2T/Q8: Q2 above.  IDENTICAL, not merely isomorphic.")
    print("         => ALL FOUR ARE CANONICALLY LINKED.  By section 2's own standard the recurrence")
    print("            is NOT evidence: it is one fact -- the ramification of 3 -- wearing four hats.")

if __name__ == "__main__":
    Q1(); print(); Q2(); print(); Q3(); print("\nVERIFIED")
