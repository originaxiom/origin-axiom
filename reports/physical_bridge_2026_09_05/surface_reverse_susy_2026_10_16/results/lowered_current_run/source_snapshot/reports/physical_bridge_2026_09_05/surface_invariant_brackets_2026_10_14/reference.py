"""Separate sparse upper-cocycle engine and Euclidean root enumeration.

Shares the declared frame and analysis questions, NOT the native bracket
engine or Weyl root builder. Explicit sign coboundary aligns the bases.
This is implementation diversity, not a nonauthor proof review.
"""
from fractions import Fraction as F
from itertools import combinations,product
import sympy as s
from analysis import SIMPLE_DOUBLED,emit

def inverse(a):
    n=len(a);m=[[F(x) for x in row]+[F(i==j) for j in range(n)] for i,row in enumerate(a)]
    for j in range(n):
        k=next(i for i in range(j,n) if m[i][j]);m[j],m[k]=m[k],m[j]
        d=m[j][j];m[j]=[x/d for x in m[j]]
        for i in range(n):
            if i!=j:
                d=m[i][j];m[i]=[x-d*y for x,y in zip(m[i],m[j])]
    return [row[n:] for row in m]

class Engine:
    def __init__(self):
        S=[[F(SIMPLE_DOUBLED[j][i],2) for j in range(8)] for i in range(8)]
        inv=inverse(S);cartan=[[sum(S[k][i]*S[k][j] for k in range(8)) for j in range(8)] for i in range(8)]
        euclidean=[]
        for i,j in combinations(range(8),2):
            for a,b in product((-1,1),repeat=2):
                r=[F(0)]*8;r[i]=F(a);r[j]=F(b);euclidean.append(r)
        euclidean.extend([[F(x,2) for x in r] for r in product((-1,1),repeat=8) if sum(x<0 for x in r)%2==0])
        rows=[tuple(sum(inv[i][j]*r[j] for j in range(8)) for i in range(8)) for r in euclidean]
        if any(x.denominator!=1 for r in rows for x in r):raise ValueError('root coordinate denominator')
        self.roots=sorted(set(tuple(int(x) for x in r) for r in rows));self.index={r:i for i,r in enumerate(self.roots)}
        self.cartan=cartan
        self.sign={r:(-1)**(sum(int(cartan[i][j])*r[i]*r[j] for i in range(8) for j in range(i+1,8))%2) for r in self.roots}
        self.cache={}
    def eps(self,a,b):
        n=sum(a[i]*b[i] for i in range(8))
        n+=sum(int(self.cartan[i][j])*a[i]*b[j] for i in range(8) for j in range(i+1,8))
        return (-1)**(n%2)
    def e(self,r):
        v=s.zeros(248,1);v[8+self.index[r]]=self.sign[r];return v
    def pair(self,p,q):
        if (p,q) in self.cache:return self.cache[p,q]
        out={}
        if p<8 and q>=8:
            r=self.roots[q-8];x=sum(r[k]*self.cartan[k][p] for k in range(8))
            if x:out[q]=x
        elif p>=8 and q<8:
            r=self.roots[p-8];x=-sum(r[k]*self.cartan[k][q] for k in range(8))
            if x:out[p]=x
        elif p>=8 and q>=8:
            a,b=self.roots[p-8],self.roots[q-8];t=tuple(x+y for x,y in zip(a,b));sgn=self.eps(a,b)
            if not any(t):out={i:F(sgn*x) for i,x in enumerate(a) if x}
            elif t in self.index:out={8+self.index[t]:F(sgn)}
        self.cache[p,q]=out;return out
    def br(self,u,v):
        out={};us={i:F(x) for i,x in enumerate(u) if x};vs={i:F(x) for i,x in enumerate(v) if x}
        for p,x in us.items():
            for q,y in vs.items():
                for k,a in self.pair(p,q).items():out[k]=out.get(k,F(0))+x*y*a
        return s.Matrix([out.get(k,F(0)) for k in range(248)])
    def encode(self,mat):
        # Raw upper-cocycle coordinates map to the declared lower basis.
        return [[i,j,str(mat[i,j]*(1 if i<8 else self.sign[self.roots[i-8]]))]
                for i in range(mat.rows) for j in range(mat.cols) if mat[i,j]!=0]

if __name__=='__main__':raise SystemExit(emit(Engine()))
