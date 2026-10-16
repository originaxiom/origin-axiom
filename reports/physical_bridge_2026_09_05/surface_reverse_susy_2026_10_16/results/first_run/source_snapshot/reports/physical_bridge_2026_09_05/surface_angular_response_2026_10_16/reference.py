"""Opposite-MW Clifford reconstruction and direct Cauchy-space route."""
import sympy as s
from analysis import source,emit
def main():
    n=s.Matrix([s.Rational(72,125),s.Rational(21,125),s.Rational(12,25),s.Rational(16,25)])
    t=s.Matrix([s.Rational(4,5),0,-s.Rational(12,25),-s.Rational(9,25)])
    J=s.Matrix([[0,-1,0,0],[1,0,0,0],[0,0,0,-1],[0,0,1,0]])
    vv,ext,valid=source('reference')
    return emit(vv,ext,s.Matrix.hstack(n,t,J*t,J*n),valid,'reference')
if __name__=='__main__':raise SystemExit(main())
