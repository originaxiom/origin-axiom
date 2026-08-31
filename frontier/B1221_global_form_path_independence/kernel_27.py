#!/usr/bin/env python3
"""B1221 -- the SM global form from the 27's content alone. SU(5) appears nowhere."""
from fractions import Fraction as F
from itertools import product

# (triality mod 3, duality mod 2, integer hypercharge y = 6Y)
G16 = [(1,1,1),(2,0,-4),(2,0,2),(0,1,-3),(0,0,6),(0,0,0)]     # Q u^c d^c L e^c nu^c
G10 = [(0,1,3),(0,1,-3),(1,0,-2),(2,0,2)]                      # H_u H_d D D^c
C27 = G16 + G10 + [(0,0,0)]


def kernel(comps, N=12):
    out = []
    for a, b in product(range(3), range(2)):
        for n in range(N):
            c = F(n, N)
            if all(((F(a*t,3) + F(b*s,2) + y*c) % 1) == 0 for t, s, y in comps):
                out.append((a, b, c))
    return out


def order(g):
    add = lambda x, y: ((x[0]+y[0]) % 3, (x[1]+y[1]) % 2, (x[2]+y[2]) % 1)
    o, e = 1, g
    while e != (0, 0, F(0)):
        e = add(e, g); o += 1
    return o


if __name__ == "__main__":
    K = kernel(C27)
    assert sum(d for d in (6,3,3,2,1,1,2,2,3,3,1)) == 27, "27 dimension check"
    print(f"kernel on the 27 : order {len(K)}, max element order {max(order(g) for g in K)}")
    assert len(K) == 6 and max(order(g) for g in K) == 6, "expected Z_6"
    print("  -> Gamma = Z_6, cyclic, generator (omega, -1, e^{2pi i/6})")
    print(f"kernel on the 16 : order {len(kernel(G16))}")
    print(f"kernel on the 10 : order {len(kernel(G10))}")
    # MB12 controls: the test must be able to return something else
    adj = [(0,0,0)]*3
    ints = [(0,0,6),(0,0,0),(0,1,-3),(0,1,3)]
    ka, ki = len(kernel(adj)), len(kernel(ints))
    print(f"CONTROL adjoint-only content   : {ka}")
    print(f"CONTROL integer-charge content : {ki}")
    assert ka != 6 and ki != 6, "controls must not also return 6"
    print("CONTROLS PASS -- Z_6 is a discriminating outcome")
    print("\nSU(5) is used NOWHERE above: the kernel depends on the representation, not the path.")
