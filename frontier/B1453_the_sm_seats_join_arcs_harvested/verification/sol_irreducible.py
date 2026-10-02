#!/usr/bin/env python3
"""sm:B1374 section 3.6, for main's attention: the 0-filling of the figure-eight complement (the Sol torus bundle with
monodromy RL) HAS irreducible SU(2) representations.  Main's verdict of 2026-09-15 marked the opposite TRUE.
Brute force: every assignment of SnapPy's generators of pi_1(m004(0,1)) to elements of the binary dihedral group
Dic_5 < SU(2) (order 20), kept when the relators hold; an image that is not abelian is an irreducible representation."""
import itertools, cmath, math
import snappy
z = cmath.exp(2j * math.pi / 10)
def mul(A, B): return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]), (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))
def inv(A): return ((A[1][1], -A[0][1]), (-A[1][0], A[0][0]))          # determinant one
def close(A, B): return all(abs(A[i][j] - B[i][j]) < 1e-9 for i in range(2) for j in range(2))
D = [((z ** k, 0), (0, z ** -k)) for k in range(10)]; J = ((0, -1), (1, 0)); G = D + [mul(d, J) for d in D]; I2 = ((1, 0), (0, 1))
M = snappy.Manifold("m004(0,1)"); P = M.fundamental_group(); gens = P.generators(); rels = P.relators()
def word(w, rho):
    r = I2
    for ch in w: r = mul(r, rho[ch] if ch.islower() else inv(rho[ch.lower()]))
    return r
homs = irr = 0; example = None
for img in itertools.product(range(20), repeat=len(gens)):
    rho = {g: G[i] for g, i in zip(gens, img)}
    if all(close(word(w, rho), I2) for w in rels):
        homs += 1
        if any(not close(mul(rho[a], rho[b]), mul(rho[b], rho[a])) for a in gens for b in gens):
            irr += 1; example = example or img
print("pi_1(m004(0,1)): generators %s, relators %s" % (gens, rels))
print("homomorphisms into Dic_5: %d; with non-abelian image (irreducible in SU(2)): %d" % (homs, irr))
print("one of them sends the generators to elements number", example, "(0-9 diagonal of order dividing 10, 10-19 off-diagonal)")
print("det(RL + I) = %d: the fibre characters inverted by the monodromy" % (3 * 2 - 1 * 1))
