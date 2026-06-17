import sympy as sp, numpy as np
rng=np.random.default_rng(0)

# ---------- A. silver substitution a->aab, b->a ----------
def sig(w): return ''.join('aab' if c=='a' else 'a' for c in w)
s={-1:'b',0:'a'}
for k in range(1,11): s[k]=sig(s[k-1])
rec_ok=all(s[k+1]==s[k]+s[k]+s[k-1] for k in range(0,9))   # s_{k+1}=s_k^2 s_{k-1}
L=[len(s[k]) for k in range(0,10)]
print(f"A. word recursion s_(k+1)=s_k^2 s_(k-1): {rec_ok}")
print(f"   lengths {L[:8]}  ratio->{L[7]/L[6]:.4f}  (silver mean 1+sqrt2={1+2**0.5:.4f})")

# ---------- B/C. transfer-matrix recursion and the SILVER trace map ----------
E,lam,a,b,c=sp.symbols('E lambda a b c')
Ma=sp.Matrix([[E-lam,-1],[1,0]]); Mb=sp.Matrix([[E,-1],[1,0]])
# numeric: build M(s_k) and check M_{k+1}=M_{k-1} M_k^2  and the trace map
def Mword_n(word,Ev,lm):
    M=np.eye(2)
    for ch in word:
        V=lm*(1.0 if ch=='a' else 0.0)
        M=np.array([[Ev-V,-1.0],[1.0,0.0]])@M
    return M
Ev,lm=0.6,1.0
Mn={k:Mword_n(s[k],Ev,lm) for k in range(-1,7)}  # need s[-1]='b'->Mb
Mn[-1]=Mword_n('b',Ev,lm)
matrec=all(np.allclose(Mn[k+1],Mn[k-1]@Mn[k]@Mn[k]) for k in range(0,5))
print(f"\nB. transfer matrix recursion M_(k+1)=M_(k-1) M_k^2: {matrec}")
# candidate silver trace map on (a,b,c)=(trM_{k-1},trM_k,tr(M_{k-1}M_k)):
#   a'=b ; b'=tr(M_{k+1})=b*c-a ; c'=tr(M_k M_{k+1})=(b^2-1)c-a b   [derived via Cayley-Hamilton]
def triple(k): return (np.trace(Mn[k-1]),np.trace(Mn[k]),np.trace(Mn[k-1]@Mn[k]))
ok_map=True
for k in range(1,5):
    A_,B_,C_=triple(k); ap,bp,cp=triple(k+1)
    pred=(B_, B_*C_-A_, (B_**2-1)*C_-A_*B_)
    if not np.allclose([ap,bp,cp],pred): ok_map=False
print(f"C. silver trace map (a,b,c)->(b, bc-a, (b^2-1)c-ab) matches matrices: {ok_map}")
ap,bp,cp = b, b*c-a, (b**2-1)*c-a*b
kap=lambda X,Y,Z: X**2+Y**2+Z**2-X*Y*Z-2
print(f"   preserves Fricke kappa=a^2+b^2+c^2-abc-2 ?  delta =", sp.simplify(kap(ap,bp,cp)-kap(a,b,c)))
# kappa = tr[Ma,Mb] (same two generators as golden):
print("   kappa=tr[Ma,Mb] =", sp.simplify(sp.trace(Ma*Mb*Ma.inv()*Mb.inv())), " (independent of E, = 2+lambda^2)")

# ---------- D. SILVER spectrum: zero-measure Cantor set ----------
def measure(word,lam,NE=400000):
    Es=np.linspace(-(2+lam)-.05,(2+lam)+.05,NE)
    aa=np.ones(NE);bb=np.zeros(NE);cc=np.zeros(NE);dd=np.ones(NE)
    with np.errstate(over='ignore',invalid='ignore'):
        for ch in word:
            V=lam*(1.0 if ch=='a' else 0.0)
            na=(Es-V)*aa-cc; nb=(Es-V)*bb-dd; aa,bb,cc,dd=na,nb,aa.copy(),bb.copy()
        ins=np.abs(aa+dd)<=2.0
    return float(np.mean(ins)*(Es[-1]-Es[0]))
print("\nD. SILVER spectrum measure |sigma_k| (lambda=1), grid-checked:")
prev=None
for k in range(2,8):
    m1=measure(s[k],1.0,400000); m2=measure(s[k],1.0,1200000)
    r=f"x{m1/prev:.3f}" if prev else ""
    print(f"   k={k} (|s|={len(s[k])}): {m1:.4f}  (fine grid {m2:.4f}, stable={abs(m1-m2)<0.02})  {r}")
    prev=m1
print("   => silver measure -> 0 (zero-measure Cantor set, like golden but its own rate)")
