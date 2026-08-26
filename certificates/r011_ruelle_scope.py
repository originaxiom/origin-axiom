#!/usr/bin/env python3
"""Logic/domain certificate for the Paper-III Ruelle dictionary scope.

This does not replace the cited analytic continuation theorems.  It certifies
the exact exponent match, the k=2 boundary distinction, and a countercontrol
to the invalid inference 'an infinite product cannot equal a finite object'.
"""

from fractions import Fraction


# Encode exp(-s*ell + i*k*theta) by its exact coefficient pair (-s,k).
def ruelle_exponent(s,k):
    return (-s,k)


def nome_power_exponent(k):
    return (-k,k)


for k in range(2,20):
    assert ruelle_exponent(k,k) == nome_power_exponent(k)

# Absolute Euler-product convergence is supplied only on Re(s)>2.
assert not (2 > 2)
assert all(k > 2 for k in range(3,20))

# A concrete logical countercontrol: an infinite product representation can
# have a finite closed value.  The telescoping product prod_{n=2}^N(1-1/n^2)
# equals (N+1)/(2N), hence tends to 1/2.
def telescoping_product(cutoff):
    result=Fraction(1,1)
    for n in range(2,cutoff+1):
        result *= Fraction(n*n-1,n*n)
    return result


for cutoff in range(2,100):
    assert telescoping_product(cutoff) == Fraction(cutoff+1,2*cutoff)

print("R(s,sigma_k) exponent coefficients: (-s,k)")
print("q^k exponent coefficients: (-k,k)")
print("termwise equality occurs at s=k")
print("absolute-domain check: k=2 is boundary; every integer k>=3 is inside Re(s)>2")
print("countercontrol: prod_(n=2..N)(1-1/n^2)=(N+1)/(2N) -> 1/2")
print("VERDICT: k>=3 DICTIONARY EXACT; n=2 AND NO-FINITE-IDENTITY CLAIMS DO NOT FOLLOW")
