"""Fast exact expansion over Q(sqrt-3): elements a+b*s with s^2=-3."""
from fractions import Fraction as F
from math import comb, factorial
import sympy as sp

class K:                                    # Q(sqrt-3)
    __slots__=("a","b")
    def __init__(s,a=0,b=0): s.a=F(a); s.b=F(b)
    def __add__(x,y): return K(x.a+y.a, x.b+y.b)
    def __sub__(x,y): return K(x.a-y.a, x.b-y.b)
    def __mul__(x,y): return K(x.a*y.a-3*x.b*y.b, x.a*y.b+x.b*y.a)
    def scal(x,c): return K(x.a*c, x.b*c)
    def inv(x):
        d=x.a*x.a+3*x.b*x.b
        return K(x.a/d, -x.b/d)
    def __repr__(s): return f"({s.a}+{s.b}s)"
    def is_rat(s): return s.b==0

def Vk(kmax):
    """V^(k)(u0) exactly as K elements, via w-algebra in Q[w]/(w^2-w+1). s = sqrt(-3)."""
    w=sp.Symbol('w'); P=2-w-1/w
    R={2: sp.simplify(-(w*sp.diff(P,w))/P)}
    for k in range(3,kmax+1): R[k]=sp.simplify(w*sp.diff(R[k-1],w))
    w0=sp.Rational(1,2)+sp.sqrt(-3)/2
    out={}
    for k in range(2,kmax+1):
        v=sp.expand(sp.simplify(sp.radsimp(sp.simplify(R[k].subs(w,w0)))))
        a=sp.nsimplify(sp.simplify(sp.re(v)))
        b=sp.nsimplify(sp.simplify(sp.im(v)/sp.sqrt(3)))
        out[k]=K(F(str(sp.Rational(a))),F(str(sp.Rational(b))))
    return out

def phihat(order):
    KMAX=2*order+2
    V=Vk(KMAX); A=V[2]
    assert A.a==0 and A.b==1, f"V''(u0) must be sqrt(-3); got {A}"
    u={k: V[k].scal(F(1,factorial(k))) for k in range(3,KMAX+1)}
    Ainv=A.inv()
    # D[r][T] = sum over ordered r-tuples (k_i>=3, sum=T) of prod u_{k_i}
    maxT=6*order+2
    D=[dict() for _ in range(2*order+1)]
    D[0][0]=K(1,0)
    for r in range(1,2*order+1):
        cur={}
        for T0,c0 in D[r-1].items():
            for k,uk in u.items():
                T=T0+k
                if T>maxT: continue
                cur[T]=cur.get(T,K(0,0))+c0*uk
        D[r]=cur
    coeffs=[]
    for n in range(order+1):
        tot=K(0,0)
        for r in range(0,2*n+1):
            T=2*(n+r)
            if T> maxT or T not in D[r]: continue
            m=T//2
            dfact=1
            for j in range(1,T,2): dfact*=j          # (T-1)!!
            term=D[r][T].scal(F((-1)**r,factorial(r))*dfact)
            p=K(1,0)
            for _ in range(m): p=p*Ainv              # (1/A)^{T/2}
            tot=tot+term*p
        coeffs.append(tot)
    return coeffs

if __name__=="__main__":
    import sys
    ORDER=int(sys.argv[1]) if len(sys.argv)>1 else 14
    c=phihat(ORDER)
    # symmetrised: Phat(h)*Phat(-h)
    S=[K(0,0)]*(ORDER+1)
    for i in range(ORDER+1):
        for j in range(ORDER+1-i):
            t=c[i]*c[j].scal(F((-1)**j))
            S[i+j]=S[i+j]+t
    print(f"{'n':>3} {'coefficient':>26} {'v3':>4} {'v2':>4} {'other':>10}  v3/n")
    pts=[]
    for n in range(0,ORDER+1):
        z=S[n]
        if z.a==0 and z.b==0: continue
        assert z.is_rat(), f"n={n} not rational: {z}"
        q=z.a
        if q==0: continue
        den=q.denominator
        v3=0
        d=den
        while d%3==0: d//=3; v3+=1
        v2=0
        while d%2==0: d//=2; v2+=1
        pts.append((n,v3))
        print(f"{n:>3} {str(q)[:26]:>26} {v3:>4} {v2:>4} {d:>10}  {v3/n if n else 0:.3f}")
    fit=[(n,v) for n,v in pts if n>=4]
    if len(fit)>=3:
        sl=sum(n*v for n,v in fit)/sum(n*n for n,_ in fit)
        print(f"\n  v3 ~ {sl:.4f}*n   =>  n=100 gives 3^{sl*100:.0f}    B685 read: 3^146")
