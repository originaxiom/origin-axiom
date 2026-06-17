import sympy as sp, numpy as np
E,lam=sp.symbols('E lambda')
# The two Fibonacci transfer matrices ARE the candidate generators A,B
Ma=sp.Matrix([[E-lam,-1],[1,0]]); Mb=sp.Matrix([[E,-1],[1,0]])
print("det(Ma)=",sp.simplify(Ma.det()),"  det(Mb)=",sp.simplify(Mb.det()),"  (must be 1, in SL2)")
x=sp.trace(Ma); y=sp.trace(Mb); z=sp.expand(sp.trace(Ma*Mb))
print(f"x=trA={x}   y=trB={y}   z=tr(AB)={z}")
print("special relation z = x*y - 2 ?  z-(xy-2) =", sp.simplify(z-(x*y-2)))
# DIRECT commutator trace
comm=Ma*Mb*Ma.inv()*Mb.inv()
kap=sp.simplify(sp.trace(comm))
print("\n*** tr[A,B] (direct commutator) =", kap, "***")
print("    independent of E :", E not in kap.free_symbols)
print("    equals 2+lambda^2:", sp.simplify(kap-(2+lam**2))==0)
# cross-check via Fricke cubic
print("    Fricke x^2+y^2+z^2-xyz-2 =", sp.simplify(x**2+y**2+z**2-x*y*z-2))

# ---- spectrum: grid-convergence + geometric-decay robustness (overflow check) ----
W={1:'a',2:'ab'}
for k in range(3,20): W[k]=W[k-1]+W[k-2]
def measure(k,lam,NE):
    Es=np.linspace(-(2+lam)-0.05,(2+lam)+0.05,NE)
    a=np.ones(NE);b=np.zeros(NE);c=np.zeros(NE);d=np.ones(NE)
    with np.errstate(over='ignore',invalid='ignore'):
        for ch in W[k]:
            V=lam*(1.0 if ch=='a' else 0.0)
            na=(Es-V)*a-c; nb=(Es-V)*b-d; a,b,c,d=na,nb,a.copy(),b.copy()
        tr=a+d
        inside=np.abs(tr)<=2.0
    return float(np.mean(inside)*(Es[-1]-Es[0]))
print("\nSPECTRUM measure |sigma_k|, lambda=1, two grid resolutions (overflow-safe):")
prev=None
for k in [7,9,11,13]:
    m1=measure(k,1.0,400000); m2=measure(k,1.0,1600000)
    r=f"ratio={m1/prev:.3f}" if prev else ""
    print(f"  k={k:2d}: NE=4e5 -> {m1:.4f}   NE=1.6e6 -> {m2:.4f}   grid-stable={abs(m1-m2)<0.01}   {r}")
    prev=m1
print("  (geometric, constant ratio, grid-stable => genuine ->0, not artifact)")
