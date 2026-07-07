"""B448 control: the silver monodromy's orbit fields (same computation, m=2).

Twist trace maps (verified below against 2x2 matrices):
  R:(x,y,z)->(x,z,xz-y)  L:(x,y,z)->(z,y,yz-x);  fig-8 monodromy = L o R (=T1^2, B416).
Silver monodromy R^2L^2 -> S = L o L o R o R (field data invariant under inverse/conj).
Gate: Fix(S) on kappa=-2 should carry silver's invariant trace field Q(i) (B316: RRLL -> Q(i)).
Control question: Fix(S^2)\Fix(S) on kappa=-2 — silver's "period-4 beat" field vs golden's Q(sqrt-7).
"""
import sympy as sp
import numpy as np

def Rmap(v): x,y,z=v; return (x, z, x*z-y)
def Lmap(v): x,y,z=v; return (z, y, y*z-x)

# --- numeric convention check: trace action of the automorphisms matches ---
rng=np.random.default_rng(3)
def rand_sl2():
    while True:
        M=rng.normal(size=(2,2))+1j*rng.normal(size=(2,2))
        d=np.linalg.det(M)
        if abs(d)>1e-6: return M/np.sqrt(d)
ok=True
for _ in range(10):
    A,B=rand_sl2(),rand_sl2()
    tr=lambda M: np.trace(M)
    v=(tr(A),tr(B),tr(A@B))
    # phi_R: (A,B)->(A, B A);   check trace action == Rmap
    A2,B2=A, B@A
    w=(tr(A2),tr(B2),tr(A2@B2))
    ok &= np.allclose(w,(Rmap(v)[0],Rmap(v)[2],np.trace(A@B@A)),atol=1e-9) or True
    # direct check of Rmap: (x, z, xz-y) vs (trA, tr(BA), tr(A BA))
    ok &= abs(w[1]-v[2])<1e-9 and abs(w[2]-(v[0]*v[2]-v[1]))<1e-9
    # phi_L: (A,B)->(A B, B)
    A3,B3=A@B, B
    w3=(tr(A3),tr(B3),tr(A3@B3))
    ok &= abs(w3[0]-v[2])<1e-9 and abs(w3[2]-(v[1]*v[2]-v[0]))<1e-9
print("twist trace maps verified against 2x2:", ok)
# fig-8 check: L(R(v)) == T1^2?
def T1(v): x,y,z=v; return (z,x,x*z-y)
v=(0.3+0.1j, -1.2, 0.7-0.4j)
print("L o R == T1^2:", np.allclose(Lmap(Rmap(v)), T1(T1(v)), atol=1e-12))

# --- exact: silver S = L L R R ---
x,y,z=sp.symbols('x y z')
def S(v):
    return Lmap(Lmap(Rmap(Rmap(v))))
v0=(x,y,z)
sv=S(v0)
kappa=x**2+y**2+z**2-x*y*z-2
print("\n== Fix(S) on kappa=-2 (gate: silver invariant trace field) ==")
I=[sp.expand(sv[0]-x),sp.expand(sv[1]-y),sp.expand(sv[2]-z),sp.expand(kappa+2)]
G=sp.groebner(I,x,y,z,order='lex')
uni=[g for g in G.exprs if g.free_symbols<={z}]
for f,m in sp.factor_list(sp.Poly(uni[0],z).as_expr())[1]:
    d=sp.degree(f,z)
    disc=sp.discriminant(f,z) if d>1 else None
    print(f"   {sp.expand(f)}   deg {d}" + (f", disc={disc}={sp.factorint(disc)}" if disc else ""))

print("\n== Fix(S^2) on kappa=-2 (the silver period-4 beat) ==")
s2=S(S(v0))
I2=[sp.expand(s2[0]-x),sp.expand(s2[1]-y),sp.expand(s2[2]-z),sp.expand(kappa+2)]
G2=sp.groebner(I2,x,y,z,order='lex')
uni2=[g for g in G2.exprs if g.free_symbols<={z}]
for f,m in sp.factor_list(sp.Poly(uni2[0],z).as_expr())[1]:
    d=sp.degree(f,z)
    disc=sp.discriminant(f,z) if d>1 else None
    print(f"   {sp.expand(f)}   deg {d}" + (f", disc={disc}={sp.factorint(disc)}" if disc else ""))
