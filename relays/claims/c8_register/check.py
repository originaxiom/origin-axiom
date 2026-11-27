"""Exact character calculation for the two C8 flat connections. No measured inputs."""
from collections import Counter
from itertools import combinations, product
import sys


# a+b*d in F_5[d]/(d^2-2). Characters are indexed using the field trace.
ZERO = (0, 0)
FIELD = list(product(range(5), repeat=2))


def scale(n, x):
    return (n * x[0] % 5, n * x[1] % 5)


def mul(x, y):
    a, b = x
    c, d = y
    return ((a*c + 2*b*d) % 5, (a*d + b*c) % 5)


def pair(x):
    return min(x, scale(-1, x))


def check(label, actual, expected):
    if actual != expected:
        print(f"FAIL {label}: observed {actual} expected {expected}")
        raise SystemExit(1)
    print(f"DECISIVE: {label} {actual}")


def peripheral(y):
    # Exponents in twentieth roots, in meridian, longitude order.
    # tr(y)=2a and tr(-2*d*y)=-8b.
    return (8*y[0] % 20, -32*y[1] % 20)


def spectra(weights, spin, sheet):
    vector = [peripheral(w) for w in weights]
    vector += [(0, 0), (10*sheet, 0), (10*sheet, 0)]
    even = [((a+c) % 20, (b+d) % 20)
            for (a, b), (c, d) in combinations(vector, 2)]
    odd = []
    for y in spin:
        m, l = peripheral(y)
        for sign in (-1, 1):
            odd.append(((m+sign*5*sheet) % 20, (l+10) % 20))
    return even + odd


def main(args):
    if args not in ([], ["--omit-sheet-action"]):
        raise SystemExit("expected no arguments or --omit-sheet-action")
    reps = sorted({pair(x) for x in FIELD})
    weights = [scale(2, mul(x, x)) for x in reps]
    # Joint unipotent eigencharacters separate the basis. Even Fourier
    # couples the zero basis vector to each index (nonzero orbit size / 5).
    orbit_sizes = [sum(pair(x) == r for x in FIELD) for r in reps]
    check("weil distinct labels and nonzero Fourier links",
          (len(set(weights)), sum(n != 0 for n in orbit_sizes)), (13, 13))
    # The split involution permutes +/- pairs by multiplication by 2.
    # Its Weil scalar is +1 since 2=d^2. Each transposition is a negative
    # eigenline. A half-turn in each negative two-plane squares to -1.
    negative = sum(pair(scale(2, r)) != r for r in reps) // 2
    check("negative eigenlines and spin square", (negative, (-1)**(negative//2)), (6, -1))
    planes = sorted({pair(y) for y in weights if y != ZERO})
    spin = []
    for signs in product((-1, 1), repeat=len(planes)):
        # 3 is the inverse of 2 modulo 5. The odd-order lift is unique.
        spin.append(tuple(3*sum(s*y[i] for s, y in zip(signs, planes)) % 5
                          for i in range(2)))
    mult = Counter(spin)
    squares = {mul(x, x) for x in FIELD if x != ZERO}
    check("spin multiplicities zero square nonsquare",
          (mult[ZERO], sorted({mult[x] for x in squares}),
           sorted({mult[x] for x in FIELD if x != ZERO and x not in squares})),
          (4, [3], [2]))
    geometric = spectra(weights, spin, 0)
    joined = spectra(weights, spin, int(not args))
    check("adjoint sizes", (len(geometric), len(joined)), (248, 248))
    for name, chars, expected in (("geometric", geometric, (36, 12, 32, 8, 0)),
                                  ("joint", joined, (36, 8, 32, 0, 0))):
        check(name+" longitude gauge torus gauge longitude spin torus spin both meridian signs",
              (sum(l == 0 for m, l in chars), chars.count((0, 0)),
               sum(l == 10 for m, l in chars), chars.count((0, 10)),
               chars.count((10, 10))), expected)
    # Dihedral lifts r^a j^b, j^2 the spin scalar, computed as group pairs.
    lifts = list(product(range(5), range(4)))
    def compose(x, y):
        a, b = x
        c, d = y
        return ((a + (-1)**b*c) % 5, (b+d) % 4)
    center = [x for x in lifts if all(compose(x,y) == compose(y,x) for y in lifts)]
    # In the product of the two spin blocks a central bit from either
    # factor acts by -1 on S13 tensor S3. The even row sees neither.
    kernel = [(e, b) for e in range(2) for a, b in center if (-1)**(e+b//2) == 1]
    check("sheet center and central multiplication kernel", (center, kernel),
          ([(0, 0), (0, 2)], [(0, 0), (1, 2)]))
    check("central product order", 25*(25**2-1)*len(lifts)//len(kernel), 156000)


if __name__ == "__main__":
    main(sys.argv[1:])
