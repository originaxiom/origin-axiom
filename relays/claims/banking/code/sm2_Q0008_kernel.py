#!/usr/bin/env python3
"""sm2 (fam1-v1-unset-05): an independent recomputation for card Q0008 (the peripheral adjoint spin kernel of one E8
connection on the figure-eight knot exterior, geometric holonomy alone and times its sheet lift). numpy and the standard
library. Written from the card's definitions only.

    python3 relays/claims/banking/code/sm2_Q0008_kernel.py              # the card's choices
    python3 relays/claims/banking/code/sm2_Q0008_kernel.py --no-sheet   # my control: the sheet action dropped
    python3 relays/claims/banking/code/sm2_Q0008_kernel.py --vary       # K7: each declared choice changed

What it checks, each from scratch:
 A. F25 = F5[d]/(d^2-2). The figure-eight group as the 2-bridge knot 5/3: <x, y | w x = y w>, w = x y^-1 x^-1 y, with
    longitude L = wbar w (wbar = w reversed). x -> U(1), y -> lower unitriangular [[1,0],[t,1]]; every t solving the
    relation is found, and L's image is computed and compared with the card's Z U(-2d).
 B. The sheet: x -> j, y -> r^a j in the binary dihedral group of order 20 (r = diag(z, 1/z), z a primitive 10th root of
    unity squared, so r has order 5; j = [[0,1],[-1,0]]); every a that makes it a homomorphism is found, and L's image.
 C. The spin sign: the 13-dimensional even part of the finite Fourier operator with kernel psi(Tr(2xy)) represents the
    involution [[0,1],[-1,0]] of PSL(2,25) up to a scalar. Scaled to square 1 and determinant 1 (the image of a perfect
    group lies in SO(13)), its trace fixes the -1 eigenspace's dimension m; m/2 odd means the Spin(13) cover restricted to
    PSL(2,25) is nonsplit, so the central Z goes to -1 in Spin(13).
 D. The count: 248 = L2(13) + 13x3 + L2(3) + 64x2 under Spin(13) x Spin(3) (the HSpin(16) branching, a named hypothesis).
    Joint eigenvalues of the meridian and longitude are listed on each part, and the torus spin kernel is counted:
    longitude -1 with meridian +1 (periodic) or -1 (antiperiodic).
"""
import cmath, itertools, sys
import numpy as np

P = 5
# ---- F25 as pairs (a, b) = a + b d, d^2 = 2
def add(u, v): return ((u[0] + v[0]) % P, (u[1] + v[1]) % P)
def neg(u): return ((-u[0]) % P, (-u[1]) % P)
def mul(u, v): return ((u[0] * v[0] + 2 * u[1] * v[1]) % P, (u[0] * v[1] + u[1] * v[0]) % P)
def tr(u): return (2 * u[0]) % P                      # Tr(a + b d) = 2a
F = [(a, b) for a in range(P) for b in range(P)]
NZ = [u for u in F if u != (0, 0)]
ONE, ZERO, D = (1, 0), (0, 0), (0, 1)
def inv(u): return next(v for v in NZ if mul(u, v) == ONE)
assert all(mul(D, D) == (2, 0) for _ in [0]) and not any(mul(u, u) == (2, 0) for u in [(a, 0) for a in range(P)])

def mmul(A, B):
    return tuple(tuple(add(mul(A[i][0], B[0][j]), mul(A[i][1], B[1][j])) for j in range(2)) for i in range(2))
def minv(A):  # det 1
    (a, b), (c, e) = A
    return ((e, neg(b)), (neg(c), a))
I2 = ((ONE, ZERO), (ZERO, ONE))
Zm = ((neg(ONE), ZERO), (ZERO, neg(ONE)))
def U(v): return ((ONE, v), (ZERO, ONE))
def word(gens, w, mm, mi, e):
    out = e
    for g in w:
        out = mm(out, gens[g] if g.islower() else mi(gens[g.lower()]))
    return out
W = "xYXy"                      # w = x y^-1 x^-1 y  (capital = inverse)
WBAR = W[::-1]
LONG = WBAR + W
assert sum(1 if c.islower() else -1 for c in LONG) == 0      # exponent sum 0

def geometric():
    sols = []
    for t in NZ:
        g = {"x": U(ONE), "y": ((ONE, ZERO), (t, ONE))}
        w = word(g, W, mmul, minv, I2)
        if mmul(w, g["x"]) == mmul(g["y"], w):
            L = word(g, LONG, mmul, minv, I2)
            assert mmul(L, g["x"]) == mmul(g["x"], L)        # the longitude commutes with the meridian
            sols.append((t, L))
    return sols

# ---- the binary dihedral group of order 20 in SU(2), numerically
z5 = cmath.exp(2j * cmath.pi / 5)
r = np.array([[z5, 0], [0, 1 / z5]])
jm = np.array([[0, 1], [-1, 0]], dtype=complex)
def sheet():
    sols = []
    for a in range(5):
        g = {"x": jm, "y": np.linalg.matrix_power(r, a) @ jm}
        w = word(g, W, lambda A, B: A @ B, np.linalg.inv, np.eye(2))
        if np.allclose(w @ g["x"], g["y"] @ w):
            L = word(g, LONG, lambda A, B: A @ B, np.linalg.inv, np.eye(2))
            sols.append((a, L, g))
    return sols

# ---- C: the spin sign from the Fourier involution on the even Weil module
def spin_sign():
    zeta = cmath.exp(2j * cmath.pi / P)
    K = np.array([[zeta ** tr(mul((2, 0), mul(x, y))) for x in F] for y in F])
    reps = []
    for x in F:
        if neg(x) not in reps: reps.append(x)
    assert len(reps) == 13
    B = np.zeros((25, 13))
    for k, x in enumerate(reps):
        B[F.index(x), k] = 1; B[F.index(neg(x)), k] = 1
        B[:, k] /= np.linalg.norm(B[:, k])
    M = B.T @ K @ B                                          # the even part; K preserves even functions
    assert np.allclose(B @ M, K @ B)
    lam = cmath.sqrt(np.linalg.eigvals(M @ M)[0])
    assert np.allclose(M @ M, lam ** 2 * np.eye(13))
    out = []
    for s in (lam, -lam):
        Ms = M / s
        if np.isclose(np.linalg.det(Ms), 1):
            t = np.trace(Ms).real
            m = round((13 - t) / 2)
            out.append((round(t), m))
    return out

# ---- D: the count
def weights13(vm, vl):
    """joint (meridian, longitude) weights of U(vm), U(vl) on the 13: x mod +-, weight Tr(v 2 x^2)"""
    reps = []
    for x in F:
        if neg(x) not in reps: reps.append(x)
    return [(tr(mul(vm, mul((2, 0), mul(x, x)))), tr(mul(vl, mul((2, 0), mul(x, x))))) for x in reps], reps

def spin_weights(vm, vl):
    """64 joint weights of the odd-order lift of <U(vm), U(vl)> to Spin(13): pairs x ~ ix (i = 2), half-weight 3w"""
    i4 = [(1, 0), (2, 0), (3, 0), (4, 0)]
    seen, pairs = set(), []
    for x in NZ:
        if x in seen: continue
        orb = {mul(c, x) for c in i4}
        seen |= orb
        wm, wl = tr(mul(vm, mul((2, 0), mul(x, x)))), tr(mul(vl, mul((2, 0), mul(x, x))))
        ix = mul((2, 0), x)
        assert (tr(mul(vm, mul((2, 0), mul(ix, ix)))), tr(mul(vl, mul((2, 0), mul(ix, ix))))) == ((-wm) % P, (-wl) % P)
        pairs.append(((3 * wm) % P, (3 * wl) % P))
    assert len(pairs) == 6
    out = []
    for signs in itertools.product((1, -1), repeat=6):
        out.append((sum(s * h[0] for s, h in zip(signs, pairs)) % P, sum(s * h[1] for s, h in zip(signs, pairs)) % P))
    return out

def count(vm, vl, eps, with_sheet):
    z = lambda k: cmath.exp(2j * cmath.pi * k / P)
    w13, _ = weights13(vm, vl)
    # the Spin(3) factor: identity, or the sheet's meridian j (longitude: identity, checked in B)
    j3 = [1, -1, -1] if with_sheet else [1, 1, 1]          # SO(3) image of j: rotation by pi
    j2 = [1j, -1j] if with_sheet else [1, 1]               # j on the 2
    ev = []                                                 # (meridian, longitude) eigenvalue pairs on 248
    for a, b in itertools.combinations(range(13), 2):
        ev.append((z(w13[a][0] + w13[b][0]), z(w13[a][1] + w13[b][1])))
    for a in range(13):
        for c in j3:
            ev.append((z(w13[a][0]) * c, z(w13[a][1])))
    for c1, c2 in itertools.combinations(j3, 2):
        ev.append((c1 * c2, 1))
    for (sm, sl) in spin_weights(vm, vl):
        for c in j2:
            ev.append((z(sm) * c, eps * z(sl)))             # Z goes to eps on the spinors; +1 on the vectors
    assert len(ev) == 248
    near = lambda u, v: abs(u - v) < 1e-9
    per = sum(1 for m, l in ev if near(l, -1) and near(m, 1))
    anti = sum(1 for m, l in ev if near(l, -1) and near(m, -1))
    zero00 = sum(1 for s in spin_weights(vm, vl) if s == (0, 0))
    return per, anti, zero00

if __name__ == "__main__":
    geo = geometric()
    print("A. geometric maps x -> U(1), y -> [[1,0],[t,1]]: t in %s" % [t for t, _ in geo])
    riley = [t for t in NZ if add(add(mul(t, t), neg(t)), ONE) == ZERO]
    print("   the roots of t^2 - t + 1 (Riley's polynomial of the figure-eight): %s; the same: %s"
          % (riley, sorted(riley) == sorted(t for t, _ in geo)))
    vls = []
    for t, L in geo:
        is_card = L == mmul(Zm, U(mul((P - 2, 0), D)))
        v = L[0][1]
        print("   t = %s: longitude = [[%s, %s], [%s, %s]]; equals Z U(-2d): %s; equals Z U(v) with v = %s"
              % (t, L[0][0], L[0][1], L[1][0], L[1][1], is_card, v))
        assert L[0][0] == neg(ONE) and L[1][1] == neg(ONE) and L[1][0] == ZERO
        vls.append(v)
    sh = sheet()
    print("B. sheet lifts x -> j, y -> r^a j that are homomorphisms: a in %s" % [a for a, _, _ in sh])
    for a, L, _ in sh:
        print("   a = %d: longitude image is the identity: %s" % (a, np.allclose(L, np.eye(2))))
    sg = spin_sign()
    print("C. Fourier involution on the even 13, scaled to square 1 and det 1: (trace, m) = %s" % sg)
    assert len(sg) == 1
    eps = -1 if (sg[0][1] // 2) % 2 == 1 else 1
    print("   -1 eigenspace m = %d, m/2 %s: the cover is %s, Z -> %d on the spinors"
          % (sg[0][1], "odd" if eps == -1 else "even", "nonsplit" if eps == -1 else "split", eps))
    vm, vl = ONE, mul((P - 2, 0), D)                         # the card's U(1), Z U(-2d)
    sheet_on = "--no-sheet" not in sys.argv
    g_per, g_anti, z00 = count(vm, vl, eps, False)
    s_per, s_anti, _ = count(vm, vl, eps, True)
    print("D. spin weights of the 64 at joint weight (0,0): %d" % z00)
    print("DECISIVE: geometric alone: periodic %d, antiperiodic %d" % (g_per, g_anti))
    if sheet_on:
        print("DECISIVE: geometric times sheet lift: periodic %d, antiperiodic %d" % (s_per, s_anti))
        ok = (g_per, g_anti, s_per, s_anti) == (8, 0, 0, 0) and any(v == vl for v in vls) \
             and all(np.allclose(L, np.eye(2)) for _, L, _ in sh) and sh and eps == -1
    else:
        print("CONTROL: the sheet dropped from the second construction: periodic %d, antiperiodic %d" % (g_per, g_anti))
        ok = False
    if "--vary" in sys.argv:
        print("K7. each declared choice changed:")
        for name, (a, b) in {"longitude U(+2d)": (ONE, mul((2, 0), D)), "conjugate module d -> -d": (ONE, mul((2, 0), D)),
                             "meridian U(2) (another marking)": ((2, 0), mul((P - 4, 0), D))}.items():
            print("   %-32s geometric %s, with sheet %s" % (name, count(a, b, eps, False)[:2], count(a, b, eps, True)[:2]))
        print("   spin sign split (eps = +1):     geometric %s, with sheet %s"
              % (count(vm, vl, 1, False)[:2], count(vm, vl, 1, True)[:2]))
    print("RESULT: the card's 8 -> 0 %s" % ("holds" if ok else "does not come out"))
    sys.exit(0 if ok else 1)
