"""Closed-coframe tube and radius transformation route, shared algebra."""
import sympy as s
from analysis import a,b,ell,emit
def main():
    N=s.Matrix([2*a*b/ell,(b*b-a*a)/ell,2*a,2*b]);D=s.Matrix([[b/ell,0],[-a/(2*ell),b/(2*ell)],[1,0],[0,1]])
    rows={(0,1,0):-1/ell,(1,2,2):1/(2*ell),(0,3,2):-1/ell,(1,3,3):-1/(2*ell)}
    rows.update({(j,i,k):-z for (i,j,k),z in list(rows.items())})
    C=[[[rows.get((i,j,k),s.Integer(0)) for k in range(4)] for j in range(4)] for i in range(4)]
    x,p,q=s.symbols('x p q',real=True);y=s.Symbol('y',positive=True)
    f=(p+x*q)**2/y+y*q*q
    t=s.simplify(f.subs({x:x+1,p:p-q},simultaneous=True)-f)
    z=s.simplify(f.subs({x:-x/(x*x+y*y),y:y/(x*x+y*y),p:q,q:-p},simultaneous=True)-f)
    return emit(N,D,C,True,t==0 and z==0)
if __name__=='__main__':raise SystemExit(main())
