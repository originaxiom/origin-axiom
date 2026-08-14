import sympy as sp
from itertools import product

def cartan(kind,n):
    A=sp.zeros(n,n)
    for i in range(n): A[i,i]=2
    if kind=='A':
        for i in range(n-1): A[i,i+1]=A[i+1,i]=-1
    if kind=='E6':
        # Bourbaki: 1-3-4-5-6 chain, 2 attached to 4
        E=[(1,3),(3,4),(4,5),(5,6),(2,4)]
        A=sp.zeros(6,6)
        for i in range(6): A[i,i]=2
        for a,b in E: A[a-1,b-1]=A[b-1,a-1]=-1
    return A

def orbit(A,hw):
    n=A.rows
    seen={tuple(hw)}; frontier=[tuple(hw)]
    while frontier:
        new=[]
        for c in frontier:
            for i in range(n):
                if c[i]!=0:
                    d=list(c)
                    for j in range(n): d[j]-=c[i]*A[i,j]
                    d=tuple(d)
                    if d not in seen: seen.add(d); new.append(d)
        frontier=new
    return sorted(seen)

# E6, 27 = orbit of omega_1
A=cartan('E6',6)
W=orbit(A,[1,0,0,0,0,0])
print("E6 dim of orbit(omega_1) =",len(W))
h=sp.symbols('h1:7')
lin=sp.expand(sum(sum(c[j]*h[j] for j in range(6)) for c in W))
cub=sp.expand(sum(sp.expand(sum(c[j]*h[j] for j in range(6)))**3 for c in W))
print("27: sum lambda(H)      =",sp.simplify(lin))
print("27: sum lambda(H)^3    =",sp.simplify(cub))

# MB12 FAILURE CONTROLS
A2=cartan('A',2); T3=orbit(A2,[1,0])
g=sp.symbols('g1:3')
print("A2 3: dim",len(T3),
      "| sum lam =",sp.simplify(sp.expand(sum(sum(c[j]*g[j] for j in range(2)) for c in T3))),
      "| sum lam^3 =",sp.factor(sp.expand(sum(sp.expand(sum(c[j]*g[j] for j in range(2)))**3 for c in T3))))
A4=cartan('A',4); k=sp.symbols('k1:5')
for name,hw in [("5",[1,0,0,0]),("10",[0,1,0,0])]:
    O=orbit(A4,hw)
    c3=sp.expand(sum(sp.expand(sum(c[j]*k[j] for j in range(4)))**3 for c in O))
    print("A4 %s: dim %d | sum lam = %s | sum lam^3 = %s"%(name,len(O),
        sp.simplify(sp.expand(sum(sum(c[j]*k[j] for j in range(4)) for c in O))), sp.factor(c3)))
