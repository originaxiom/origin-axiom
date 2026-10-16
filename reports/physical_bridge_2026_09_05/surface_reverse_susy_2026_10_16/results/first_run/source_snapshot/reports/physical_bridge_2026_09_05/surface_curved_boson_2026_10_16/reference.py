"""Credited closed-frame and canonical power route, no metric solve."""
import sympy as s
from analysis import emit
def main():
    x,u,v=s.symbols('x u v',real=True);y=s.Symbol('y',positive=True)
    rows={(0,1,0):-s.Integer(1),(1,2,2):s.Rational(1,2),(0,3,2):-s.Integer(1),(1,3,3):-s.Rational(1,2)}
    rows.update({(j,i,k):-c for (i,j,k),c in list(rows.items())})
    C=[[[rows.get((i,j,k),s.Integer(0)) for k in range(4)] for j in range(4)] for i in range(4)]
    div=[-sum(C[i][j][j] for j in range(4)) for i in range(4)]
    q=[s.Rational(3,2),0,0,0];f=[[-sum(C[i][j][k]*q[k] for k in range(4)) for j in range(4)] for i in range(4)]
    E=s.Matrix([[y,0,0,0],[0,y,0,0],[0,0,s.sqrt(y),0],[0,0,-x/s.sqrt(y),1/s.sqrt(y)]])
    return emit(C,div,f,-s.Integer(3),E,(x,y,u,v),True)
if __name__=='__main__':raise SystemExit(main())
