"""B1985, POST HOC (labelled; written after listen3_run.txt was read; exact): from mod p^2 to mod p^3, the points over the
common point that have lifts on the cusp's leaf are exactly those p*u with u isotropic for x^2 + y^2 + z^2 over F_p (the
tangent cone of the leaf's singular point); at p = 3 the nonzero isotropic u are exactly the 8 cube vertices (+-1, +-1, +-1);
the Markoff point (3, 3, 3) lies on the leaf mod every 3^k and sits over a vertex.
    python3 -B cone_posthoc.py > cone_posthoc_run.txt"""
from itertools import product
for p in (3, 5, 7):
    N2, N3 = p * p, p ** 3
    lifts = set()
    for v in product(range(0, N3, p), repeat=3):
        if (v[0] ** 2 + v[1] ** 2 + v[2] ** 2 - v[0] * v[1] * v[2]) % N3 == 0:
            lifts.add(tuple((c % N2) // p for c in v))
    iso = {u for u in product(range(p), repeat=3) if (u[0] ** 2 + u[1] ** 2 + u[2] ** 2) % p == 0}
    print("p = %d: directions u (mod p) over the common point with lifts to the leaf mod p^3: %d; isotropic for x^2+y^2+z^2 over F_%d: %d; equal sets: %s" % (p, len(lifts), p, len(iso), lifts == iso))
    if p == 3:
        verts = {u for u in product(range(3), repeat=3) if all(c in (1, 2) for c in u)}
        print("   p = 3: the nonzero isotropic directions are exactly the 8 cube vertices (+-1, +-1, +-1): %s" % ((iso - {(0, 0, 0)}) == verts))
m = (3, 3, 3)
on_int = m[0] ** 2 + m[1] ** 2 + m[2] ** 2 == m[0] * m[1] * m[2]
direction = tuple((c // 3) % 3 for c in m)
verts3 = {u for u in product(range(3), repeat=3) if all(c in (1, 2) for c in u)}
print("(3, 3, 3): on the cusp's leaf over the integers (x^2+y^2+z^2 = xyz): %s; its direction over the common point mod 9 is %s, a cube vertex: %s" % (on_int, direction, direction in verts3))
