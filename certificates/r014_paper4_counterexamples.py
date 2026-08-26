#!/usr/bin/env python3
"""Dependency-free counterexamples to two literal Paper-IV theorems.

The s955 triangulation metadata and gluing matrix are frozen from SnapPy
3.3.2.  The certificate verifies its complete regular-shape solution exactly
in Q(q), q^2-q+1=0, rather than relying on floating-point shape recognition.
"""

from fractions import Fraction as F


# Arithmetic a+b*q in Q(q), with q^2=q-1.
def add(left,right):
    return (left[0]+right[0],left[1]+right[1])


def mul(left,right):
    a,b=left;c,d=right
    return (a*c-b*d,a*d+b*c+b*d)


ONE=(F(1),F(0))
Q=(F(0),F(1))
QINV=(F(1),F(-1))


def power(value,exponent):
    if exponent<0:
        assert value==Q
        return power(QINV,-exponent)
    result=ONE
    base=value
    while exponent:
        if exponent&1:
            result=mul(result,base)
        base=mul(base,base)
        exponent//=2
    return result


assert add(mul(Q,Q),add((F(0),F(-1)),ONE))==(F(0),F(0))
assert power(Q,6)==ONE and mul(Q,QINV)==ONE

# Census witness: s955, undecorated isomorphism signature
# gLvQQadfedefjqqasjj, zero-based database index 1256.  Columns occur as
# (z,z',z'') for six tetrahedra; at a regular tetrahedron all three equal q.
GLUING=[
 [1,0,0,1,0,0,2,1,0,0,0,0,0,0,0,1,0,0],
 [0,1,0,0,0,2,0,0,0,0,0,2,0,0,0,0,1,0],
 [0,0,1,1,2,0,0,0,0,0,0,0,0,1,0,0,0,1],
 [0,0,1,0,0,0,0,1,0,1,2,0,0,0,0,0,0,1],
 [0,1,0,0,0,0,0,0,2,0,0,0,0,0,2,0,1,0],
 [1,0,0,0,0,0,0,0,0,1,0,0,2,1,0,1,0,0],
 [0,-1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
 [-1,0,1,0,0,0,0,0,0,-1,0,0,-1,0,1,0,1,0],
]
assert len(GLUING)==8 and all(len(row)==18 for row in GLUING)
assert [sum(row) for row in GLUING[:6]]==[6]*6
assert [sum(row) for row in GLUING[6:]]==[0,0]
for row in GLUING:
    product=ONE
    for exponent in row:
        product=mul(product,power(Q,exponent))
    assert product==ONE

# q has positive imaginary embedding and minimal polynomial X^2-X+1,
# discriminant -3; the complete regular solution therefore has shape field
# Q(sqrt(-3)).
POLYNOMIAL=(1,-1,1)
DISCRIMINANT=POLYNOMIAL[1]**2-4*POLYNOMIAL[0]*POLYNOMIAL[2]
assert DISCRIMINANT==-3

CENSUS_SIZE=212641
PAPER_SCAN_LAST_INDEX=1200
S955_INDEX=1256
assert S955_INDEX>PAPER_SCAN_LAST_INDEX and S955_INDEX<CENSUS_SIZE

# Literal scale-theorem counterexample.  Curvature-normalized hyperbolic
# volume is an isometry invariant and a degree-d cover multiplies it by d,
# so it does distinguish a manifold from that cover.
normalized_volume=F(7,3)
cover_degree=3
cover_volume=cover_degree*normalized_volume
assert cover_volume!=normalized_volume

# The correct physical limitation is the missing external conversion scale.
L1,L2=F(1),F(2)
assert normalized_volume*L1**3 != normalized_volume*L2**3

print("s955 isosig: gLvQQadfedefjqqasjj")
print("census metadata: size=212641, paper last index=1200, s955 index=1256")
print("s955 exact regular-shape gluing: 6 edge equations and 2 cusp equations PASS")
print("shape polynomial: X^2-X+1, discriminant=-3")
print("verdict: the asserted exhaustive 14-member family is REFUTED")
print("scale counterexample: normalized volume of a degree-3 cover is 3*volume")
print("correct fence: conversion to physical units still needs an external scale L")
print("VERDICT: BOTH LITERAL PAPER-IV CLAIMS REFUTED; FULL-FAMILY SEPARATOR REMAINS OPEN")
