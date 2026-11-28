"""Endpoint comparison of the card's unshifted Epstein sums, with integer enclosures.

For any y>=1, compare x=0 with x=1/2, both in the fundamental domain.
For each m != 0 represent (m²y²+(n+mx)²)^(-s) as a positive integral of
Gaussians. The Gaussian sum over n has, by Poisson summation, a Fourier
series with strictly positive cosine coefficients. At a half-integer
shift the odd coefficients change sign. The corresponding row is strictly
smaller for odd m and equal for even m. Thus the entire imaginary axis in
the domain is excluded as a minimizing locus for these two positive sums.
For V_RS the product for eta gives the same ordering: every odd product
factor changes from 1-q^k to 1+q^k at fixed y and every even factor stays
fixed. The minus logarithm reverses the increase. This comparison requires
neither the minimizing shape nor a numerical Hessian.
"""
import sys


def enclosure(s,shift):
    radius, scale = 48, 10**12
    lower = count = 0
    for m in range(-radius,radius+1):
        for n in range(-radius,radius+1):
            if m==0 and n==0:
                continue
            denominator = (2*n+shift*m)**2 + 4*m*m
            lower += scale*4**s // denominator**s
            count += 1
    # |m*tau+n|² >= (m²+n²)/2. Shell k has 8k points; replace
    # the decreasing tail sum by the integral starting at radius.
    num, den = 8*2**s*scale, (2*s-2)*radius**(2*s-2)
    return lower, lower+count+(num+den-1)//den


def main():
    shift = 0 if "--no-shear" in sys.argv else 1
    for s in (2,3):
        lo,_ = enclosure(s,0)
        _,hi = enclosure(s,shift)
        if lo<=hi:
            print("FAIL intervals do not certify a strict descent",s)
            return 1
        print("DECISIVE: certified lower bound on square minus shear in trillionths",s,lo-hi)
    return 0


if __name__=="__main__":
    sys.exit(main())
