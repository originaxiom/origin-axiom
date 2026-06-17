#!/usr/bin/env python3
"""INDEPENDENT bronze (m=3) quasicrystal verification -- a NEW data point.

Not a re-run of the handoff: derives the bronze trace map from Cayley-Hamilton,
checks it against the actual transfer matrices, proves it conserves the Fricke
invariant kappa = a^2+b^2+c^2-abc-2 symbolically, and computes the bronze
spectrum measure (expected -> 0, its own rate; ground truth: Damanik-Killip-Lenz,
every Sturmian potential lambda!=0 has zero-measure Cantor spectrum).

metallic-m substitution: a -> a^m b, b -> a ; word s_{k+1}=s_k^m s_{k-1};
matrix recursion M_{k+1}=M_{k-1} M_k^m.  Bronze: m=3.
"""
import sympy as sp, numpy as np
ok=True
def chk(n,c,extra=""):
    global ok; ok=ok and bool(c); print(f"  [{'PASS' if c else 'FAIL'}] {n}"+(f"  {extra}" if extra else ""))

m=3
# ---- A. word ----
def sig(w): return ''.join('aaab' if ch=='a' else 'a' for ch in w)   # a->a^3 b, b->a
s={-1:'b',0:'a'}
for k in range(1,9): s[k]=sig(s[k-1])
wrec=all(s[k+1]==s[k]*m+s[k-1] for k in range(0,8))
L=[len(s[k]) for k in range(0,9)]
bronze_mean=(3+sp.sqrt(13))/2
chk("bronze word recursion s_(k+1)=s_k^3 s_(k-1)", wrec,
    extra=f"lengths {L[:7]} ratio->{L[7]/L[6]:.4f} bronze mean (3+sqrt13)/2={float(bronze_mean):.4f}")

# ---- B. matrix recursion M_(k+1)=M_(k-1) M_k^3 (numeric) ----
def Mw(word,Ev,lm):
    M=np.eye(2)
    for ch in word:
        V=lm*(1.0 if ch=='a' else 0.0)
        M=np.array([[Ev-V,-1.0],[1.0,0.0]])@M
    return M
Ev,lm=0.6,1.0
Mn={k:Mw(s[k],Ev,lm) for k in range(-1,7)}
matrec=all(np.allclose(Mn[k+1],Mn[k-1]@np.linalg.matrix_power(Mn[k],3)) for k in range(0,4))
chk("bronze matrix recursion M_(k+1)=M_(k-1) M_k^3", matrec)

# ---- C. bronze trace map by Cayley-Hamilton, M_k^3 = (b^2-1)M_k - b I ----
a,b,c=sp.symbols('a b c')
# a=trM_{k-1}, b=trM_k, c=tr(M_{k-1}M_k); new (a',b',c')=(trM_k, trM_{k+1}, tr(M_k M_{k+1}))
# M_{k+1}=M_{k-1}M_k^3=(b^2-1)M_{k-1}M_k - b M_{k-1}
ap=b
bp=(b**2-1)*c - b*a                               # tr: (b^2-1)c - b a
# c'=tr(M_k M_{k+1})=(b^2-1)tr(M_k M_{k-1} M_k)-b tr(M_k M_{k-1});
# tr(M_k M_{k-1} M_k)=tr(M_k^2 M_{k-1})=b c - a ;  tr(M_k M_{k-1})=c
cp=(b**2-1)*(b*c-a) - b*c
# verify the derived map against the actual matrices (numeric)
def triple(k): return (np.trace(Mn[k-1]),np.trace(Mn[k]),np.trace(Mn[k-1]@Mn[k]))
mapok=True
for k in range(1,4):
    A_,B_,C_=triple(k); a2,b2,c2=triple(k+1)
    pred=(B_,(B_**2-1)*C_-B_*A_,(B_**2-1)*(B_*C_-A_)-B_*C_)
    if not np.allclose([a2,b2,c2],pred): mapok=False
chk("bronze trace map (b, (b^2-1)c-ab, (b^2-1)(bc-a)-bc) matches matrices", mapok)
Kfr=lambda X,Y,Z: X**2+Y**2+Z**2-X*Y*Z-2
chk("bronze trace map conserves Fricke kappa (symbolic delta=0)",
    sp.simplify(Kfr(ap,bp,cp)-Kfr(a,b,c))==0)
# same generators => same boundary holonomy kappa = 2+lambda^2
E,lam=sp.symbols('E lambda')
Ma=sp.Matrix([[E-lam,-1],[1,0]]); Mb=sp.Matrix([[E,-1],[1,0]])
chk("kappa=tr[Ma,Mb]=2+lambda^2 (same generators, E-independent)",
    sp.simplify(sp.trace(Ma*Mb*Ma.inv()*Mb.inv())-(2+lam**2))==0)

# ---- D. bronze spectrum measure -> 0 (its own rate) ----
def measure(word,lam,NE=400000):
    Es=np.linspace(-(2+lam)-.05,(2+lam)+.05,NE)
    aa=np.ones(NE);bb=np.zeros(NE);cc=np.zeros(NE);dd=np.ones(NE)
    with np.errstate(over='ignore',invalid='ignore'):
        for ch in word:
            V=lam*(1.0 if ch=='a' else 0.0)
            na=(Es-V)*aa-cc; nb=(Es-V)*bb-dd; aa,bb,cc,dd=na,nb,aa.copy(),bb.copy()
        ins=np.abs(aa+dd)<=2.0
    return float(np.mean(ins)*(Es[-1]-Es[0]))
print("  bronze spectrum measure |sigma_k| (lambda=1), grid-checked:")
prev=None; ratios=[]
for k in range(2,7):
    m1=measure(s[k],1.0,400000); m2=measure(s[k],1.0,1200000)
    r=(m1/prev) if prev else None
    if r: ratios.append(r)
    print(f"    k={k} (|s|={len(s[k])}): {m1:.4f} (fine {m2:.4f}, stable={abs(m1-m2)<0.02})"+(f"  x{r:.3f}" if r else ""))
    prev=m1
chk("bronze measure decays geometrically toward 0 (zero-measure Cantor)",
    all(rr<0.95 for rr in ratios) and abs(ratios[-1]-ratios[-2])<0.03,
    extra=f"stable ratio ~ {ratios[-1]:.3f}")

print("\n"+("ALL BRONZE CHECKS PASS" if ok else "SOME FAILED"))
import sys; sys.exit(0 if ok else 1)
