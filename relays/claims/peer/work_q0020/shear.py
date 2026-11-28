"""Test exactly which part of a fivefold class count follows from T-covariance.

At height y consider exp(-pi*y*(2+cos(2*pi*(b+a*x)))). On the
nonvertical order-30 pairs choose the representative with 0<a<1/2.
It exists uniquely there, and b is taken mod 1. Under T^k the column
x moves to x+k and b to b-ka. This positive observable is exactly
covariant and its exponential rate is exactly 2+cos(2*pi*(b+a*x)).
Testing equality of cosines only needs rational phases modulo sign.
It is a counterexample to inferring rates at a common column solely
from T covariance. No identification with a physical Yukawa is used.
"""
from fractions import Fraction
from math import gcd
import sys


def mark(j,k):
    a = (j%30,k%30)
    return min(a,((-j)%30,(-k)%30))


def shift(pair,h):
    j,k = pair
    return mark(j,k-h*j)


def cosphase(pair,x):
    j,k = pair
    angle = (k+j*x)/30
    return min(angle%1,(-angle)%1)


def main():
    marks = {mark(j,k) for j in range(30) for k in range(30) if gcd(gcd(j,k),30)==1}
    subset = {v for v in marks if v[0]%5}
    act = {v for v in subset if (v[1]-2*v[0])%5==0}
    fibers = [{shift(v,6*i) for i in range(5)} for v in act]
    if set().union(*fibers)!=subset or any(len(f)!=5 or len(f&act)!=1 for f in fibers):
        print("FAIL act-line section or orbit size")
        return 1
    x = Fraction(13,100)
    # One shear by six preserves both coordinates mod 6 and cycles all
    # five nonvertical slopes mod 5. Test a joint transport and then hold x.
    delta = 0 if "--hold-column" in sys.argv else 6
    agree = sum(cosphase(v,x)==cosphase(shift(v,6),x+delta) for v in subset)
    if agree!=len(subset):
        print("FAIL joint transport lost", len(subset)-agree, "equalities")
        return 1
    fixed = sum(cosphase(v,x)==cosphase(shift(v,6),x) for v in subset)
    if fixed==len(subset):
        print("FAIL fixed-column example did not discriminate")
        return 1
    print("DECISIVE: sign pairs, nonvertical pairs, act-line representatives",len(marks),len(subset),len(act))
    print("DECISIVE: five-element translation orbits",len(fibers))
    print("DECISIVE: equal model rates on transported and fixed columns",agree,fixed)
    return 0


if __name__=="__main__":
    sys.exit(main())
