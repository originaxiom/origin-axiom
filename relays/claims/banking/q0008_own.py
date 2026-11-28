#!/usr/bin/env python3
"""Banking seat V1 (fam1-v1-unset-04), Q0008: an own recomputation of the two flat E8 connections' peripheral counts,
sharing nothing with the producer's code.  Route: the Weil representation of SL(2, 25) is built as explicit matrices in
the Schrodinger model on functions on F25 = F5[d]/(d^2 - 2); the meridian U(1) and longitude Z U(-2d) are read off as
matrices on the even functions; the spin square of an involution is read from the Fourier involution's eigenvalues, its
sign fixed by det = +1; each order-5 spin lift is found by testing its fifth power; the adjoint 248 = Lambda^2(16) +
S13 (x) S3 is assembled from those eigen-phases; the sheet group is generated as 2 x 2 matrices.
    python3 relays/claims/banking/q0008_own.py                    the decisive run
    python3 relays/claims/banking/q0008_own.py --plant-wrong-lift  the failing control (the longitude's spin sign flipped)
Exit 0 when every value comes out as the card states; 1 otherwise."""
import cmath, itertools, sys
from fractions import Fraction as Fr
import numpy as np

PLANT = sys.argv[1:] == ["--plant-wrong-lift"]
if sys.argv[1:] not in ([], ["--plant-wrong-lift"]):
    print("usage: no argument, or --plant-wrong-lift"); sys.exit(2)

# --- the field F25 = F5[d]/(d^2 - 2): elements (a, b) = a + b d ---
F = [(a, b) for a in range(5) for b in range(5)]
def add(x, y): return ((x[0] + y[0]) % 5, (x[1] + y[1]) % 5)
def neg(x): return ((-x[0]) % 5, (-x[1]) % 5)
def mul(x, y): return ((x[0] * y[0] + 2 * x[1] * y[1]) % 5, (x[0] * y[1] + x[1] * y[0]) % 5)
def tr(x): return (2 * x[0]) % 5                     # trace to F5 of a + b d
def psi(x): return cmath.exp(2j * cmath.pi * tr(x) / 5)
D = (0, 1)
idx = {x: i for i, x in enumerate(F)}
assert len({mul(x, x) for x in F if x != (0, 0)}) == 12   # a field: 12 nonzero squares

# --- the Schrodinger model on C^F25: U(b) f(x) = psi(b x^2) f(x); Z f(x) = chi(-1) f(-x); Fourier for w ---
def U(b): return np.diag([psi(mul(b, mul(x, x))) for x in F])
chi_m1 = 1 if any(mul(x, x) == neg((1, 0)) for x in F) else -1          # -1 is a square in F25
Zm = np.zeros((25, 25), complex)
for x in F:
    Zm[idx[neg(x)], idx[x]] = chi_m1
W = np.array([[psi(mul((2, 0), mul(x, y))) for y in F] for x in F]) / 5.0
# the even functions: basis by orbits {x, -x}
orbits = sorted({tuple(sorted((x, neg(x)))) for x in F})
P = np.zeros((25, len(orbits)), complex)
for k, o in enumerate(orbits):
    for x in set(o):
        P[idx[x], k] = 1 / np.sqrt(len(set(o)))
def on_even(M): return P.conj().T @ M @ P
Mer, Lon = on_even(U((1, 0))), on_even(Zm @ U(mul(neg((2, 0)), D)))
assert np.allclose(Mer, np.diag(np.diag(Mer))) and np.allclose(Lon, np.diag(np.diag(Lon)))
assert np.allclose(Mer @ Lon, Lon @ Mer)
def twentieths(z):
    t = cmath.phase(z) / (2 * cmath.pi) * 20
    n = round(t) % 20
    assert abs(t - round(t)) < 1e-9
    return n
vec13 = [(twentieths(Mer[k, k]), twentieths(Lon[k, k])) for k in range(len(orbits))]
links = int(sum(abs(on_even(W)[0, k]) > 1e-9 for k in range(len(orbits))))
ok = True
def show(label, got, want):
    global ok
    print("DECISIVE: %s %s" % (label, got))
    if got != want:
        ok = False
show("weil even module: dimension, distinct joint labels, nonzero Fourier links to the zero vector",
     (len(orbits), len(set(vec13)), links), (13, 13, 13))

# --- the spin square: the Fourier involution on the even module, sign fixed by det = +1 ---
We = on_even(W)
ev = np.linalg.eigvals(We)
assert np.allclose(We @ We, np.eye(len(orbits)))
if np.real(np.prod(ev)) < 0:
    ev = -ev
n_minus = int(sum(abs(e + 1) < 1e-9 for e in ev))
eps = (-1) ** (n_minus // 2)
show("involution's -1 eigenvalues on the 13 and its spin lift's square", (n_minus, eps), (6, -1))
if PLANT:
    eps = -eps

# --- the planes of the 13 and the spin lift of the commuting pair ---
zero = [v for v in vec13 if v == (0, 0)]
nonzero = [v for v in vec13 if v != (0, 0)]
planes = sorted({min(v, ((-v[0]) % 20, (-v[1]) % 20)) for v in nonzero})
assert len(zero) == 1 and len(planes) == 6
def order5_half(phases):
    """the half-angle sum for the unique spin lift of odd order of an element whose plane angles are given in twentieths
    (all multiples of 4): try the representative half-angles; keep the one whose fifth power is the identity"""
    out = []
    for signs in itertools.product((-1, 1), repeat=len(phases)):
        h = sum(Fr(s * p, 2) for s, p in zip(signs, phases))
        out.append(h)
    if any((5 * h) % 20 != 0 for h in out):
        out = [h + 10 for h in out]
    assert all((5 * h) % 20 == 0 for h in out)
    return [int(h) % 20 for h in out]
spin_m = order5_half([p[0] for p in planes])
spin_l = order5_half([p[1] for p in planes])
spin13 = [(m, (l + (10 if eps == -1 else 0)) % 20) for m, l in zip(spin_m, spin_l)]
# multiplicities of the spin weights by the class of the label in F25 (zero, a square, a non-square), read from the meridian
# and longitude phases: the label y has meridian 4 tr(y)/... here recovered by matching against psi on F25
lab = {}
for y in F:
    lab[(round(cmath.phase(psi(y)) / (2 * cmath.pi) * 20) % 20,
         round(cmath.phase(psi(mul(neg((2, 0)), mul(D, y)))) / (2 * cmath.pi) * 20) % 20)] = y
geo_spin_labels = [lab[(m, l)] for m, l in zip(spin_m, spin_l)]
cnt = {y: geo_spin_labels.count(y) for y in F}
sq = {mul(x, x) for x in F if x != (0, 0)}
show("spin weight multiplicities at zero, on squares, on non-squares",
     (cnt[(0, 0)], sorted({cnt[y] for y in sq}), sorted({cnt[y] for y in F if y != (0, 0) and y not in sq})),
     (4, [3], [2]))

def adjoint(sheet):
    v16 = vec13 + [(0, 0), (10 * sheet, 0), (10 * sheet, 0)]
    ev = [((a[0] + b[0]) % 20, (a[1] + b[1]) % 20) for a, b in itertools.combinations(v16, 2)]
    od = [((m + s * 5 * sheet) % 20, l) for m, l in spin13 for s in (-1, 1)]
    return ev + od
def counts(ch):
    return (sum(l == 0 for m, l in ch), ch.count((0, 0)), sum(l == 10 for m, l in ch), ch.count((0, 10)),
            ch.count((10, 10)))
g, j = adjoint(0), adjoint(1)
show("adjoint dimensions", (len(g), len(j)), (248, 248))
show("geometric: longitude gauge, torus gauge, longitude spin, torus spin periodic, antiperiodic", counts(g),
     (36, 12, 32, 8, 0))
show("joint: longitude gauge, torus gauge, longitude spin, torus spin periodic, antiperiodic", counts(j),
     (36, 8, 32, 0, 0))

# --- the sheet group as matrices, and the central product's order ---
z5 = cmath.exp(2j * cmath.pi / 5)
r, jj = np.array([[z5, 0], [0, 1 / z5]]), np.array([[0, 1], [-1, 0]], complex)
def key(M): return tuple(np.round(M.flatten(), 9))
grp, frontier = {key(np.eye(2)): np.eye(2, dtype=complex)}, [np.eye(2, dtype=complex)]
while frontier:
    nxt = []
    for A in frontier:
        for g_ in (r, jj):
            B = A @ g_
            if key(B) not in grp:
                grp[key(B)] = B; nxt.append(B)
    frontier = nxt
els = list(grp.values())
centre = [A for A in els if all(np.allclose(A @ B, B @ A) for B in els)]
sl2 = sum(1 for a, b, c, dd in itertools.product(F, repeat=4) if add(mul(a, dd), neg(mul(b, c))) == (1, 0))
# the kernel of SL(2, 25) x sheet group -> Spin(13) x Spin(3) acting on S13 (x) S3: central pairs (z, c), z in {I, Z}
# acting on S13 by the spin lift's scalar (eps for Z), c acting on S3 by its scalar; kept when the product acts as 1
kernel = [(zz, int(round(np.real(c[0, 0])))) for zz in (0, 1) for c in centre
          if abs((eps if zz else 1) * c[0, 0] - 1) < 1e-9]
show("sheet group order and centre; the central multiplication kernel; SL(2, 25)'s order; the central product's order",
     (len(els), len(centre), sorted(kernel), sl2, sl2 * len(els) // len(kernel)), (20, 2, [(0, 1), (1, -1)], 15600, 156000))
sys.exit(0 if ok else 1)
