"""A cylinder proof for the stated Farey operator on continuous functions.

Assume a strictly positive continuous eigenfunction h at a positive eigenvalue
lambda. Write p=2s>0. The two inverse branches are A=x/(1+x), B=1/(1+x).
Each term of F^n h(x) is (cx+d)^(-p) h(w(x)), (c,d) the word's bottom row.
The image interval has diameter 1/[d(c+d)] by unimodularity. Appending a
letter on the right increases d(c+d) by at least one, hence every diameter
is <=1/(n+1). Freeze each h(w(x)) at h(w(0)) and divide by lambda^n.
The uniform error is <= modulus_h(1/(n+1))*h(0)/min(h), by comparison
with the sum of weights at zero. These frozen sums therefore converge to h.

Every frozen summand is decreasing or constant. Among words of length n+2
take wBA, with w of length n. Their slopes c'/d' lie in [1,2]. Their
total frozen weight at zero after division is exactly h(1)/lambda^2:
BA(0)=1 and both suffix denominators have value one along that itinerary.
For 0<=x<y<=1 their normalised kernels (1+tx)^(-p) drop by at least
p*(y-x)/3^(p+1) for 1<=t<=2. Consequently h(x)-h(y) is at least
(h(1)/lambda^2)*p*(y-x)/3^(p+1). This covers any s>0 admitting that h.

For s<t, apply F_s^2 and F_t^2 to h_t. Every term is ordered; at x>0
the outer weight is strictly larger and at zero the B branch visits 1.
The minimum ratio F_s^2 h_t / h_t exceeds lambda_t^2 by compactness.
Comparison at a maximizer of h_t/h_s gives lambda_s^2 at least that
minimum. Thus lambda_s>lambda_t whenever both such eigenfunctions exist.
No existence or assertion about the rest of the spectrum is used here.
"""
from fractions import Fraction
import sys


def extend(row, letter):
    c, d = row
    return (c+d,d) if letter == "A" else (d,c+d)


def main():
    rows = [(0,1)]
    suffix = "B" if "--short-suffix" in sys.argv else "BA"
    for n in range(11):
        for c,d in rows:
            if d*(c+d) < n+1:
                print("FAIL cylinder diameter", n,c,d)
                return 1
            u,v = c,d
            for letter in suffix:
                u,v = extend((u,v),letter)
            if v != c+d or not v <= u <= 2*v:
                print("FAIL selected slope or suffix weight",n,c,d,u,v)
                return 1
            # Check the exact finite-difference version at p=1, including
            # both endpoints; the derivative estimate above applies for p>0.
            for i in range(8):
                x,y = Fraction(i,8), Fraction(i+1,8)
                drop = v/(v+u*x) - v/(v+u*y)
                if drop < (y-x)/9:
                    print("FAIL kernel drop",n,c,d,i)
                    return 1
        rows = [extend(row,l) for row in rows for l in "AB"]
    print("DECISIVE: cylinder diameter, suffix slope and suffix weight hold for 2047 word prefixes")
    print("DECISIVE: exact finite differences hold on eight intervals per prefix at exponent one")
    return 0


if __name__ == "__main__":
    sys.exit(main())
