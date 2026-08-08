import sympy as sp
from collections import Counter
E=[(1,3),(3,4),(4,5),(5,6),(2,4)]
A=sp.zeros(6,6)
for i in range(6): A[i,i]=2
for a,b in E: A[a-1,b-1]=A[b-1,a-1]=-1
def orbit(A,hw):
    n=A.rows; seen={tuple(hw)}; fr=[tuple(hw)]
    while fr:
        new=[]
        for c in fr:
            for i in range(n):
                if c[i]!=0:
                    d=tuple(c[j]-c[i]*A[i,j] for j in range(n))
                    if d not in seen: seen.add(d); new.append(d)
        fr=new
    return sorted(seen)
W=orbit(A,[1,0,0,0,0,0]); Ainv=A.inv()
# psi: alpha_i(H)=delta_{i,1}  -> so(10)=D5 on nodes {2,3,4,5,6} is centralized
h=[Ainv[j,0] for j in range(6)]
lev=Counter(sum(sp.Rational(c[j])*h[j] for j in range(6)) for c in W)
print("psi-grading of the 27 (value: multiplicity):", dict(lev))
vals=sorted(lev)
print("normalised so smallest gap = 1 ->", [v/min(abs(x-y) for x in vals for y in vals if x!=y) for v in vals])
print("exotics = 27 - 16 =", 27-16, " ; against a 15-fermion generation:", 27-15)
# is the mass-pairing charge (psi of D + psi of Dbar) matched by any single weight?
psi={c:sum(sp.Rational(c[j])*h[j] for j in range(6)) for c in W}
ten=[c for c in W if psi[c]==min(vals)]; one=[c for c in W if psi[c]==max(vals)]
print("|10-block| =",len(ten)," |1-block| =",len(one),
      " psi(10)+psi(10) =",2*min(vals)," ; -(that) =",-2*min(vals),
      " ; psi(singlet) =",max(vals), " MATCH:", -2*min(vals)==max(vals))
