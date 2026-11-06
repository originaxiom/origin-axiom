"""The web seat, 2026-11-06: THE READ-OUT THE HISTORY'S SYMMETRY FORCES (PREREGISTRATION_READ_OUT.md).

Data-free. PGL(2, Z) geometry of the one-departure history and of closed threads, and SnapPy 3.3.2's shapes of the
layered triangulation. No coupling, no ratio of the six, no theta-bar and no held-out quantity is computed.

  A  the set-wise stabiliser in PGL(2, Z) of the one-departure history, the geodesic from -1/phi to n + 1/phi,
     solved exactly (Q(sqrt5) split into rational parts) for n = 1..12, and its fixed point on the history;
  B  the symmetric points (fixed points of direction-reversing elements) on the axes of the golden loop LR and of the
     closed threads L^n R (LR)^k (n = 5, 6; k = 0..6), counted modulo the axis's own translations;
  C  where the apex sits in the Farey tessellation: on the edge (n/2, oo), or inside a triangle with vertex oo;
  D  the departure's share of a closed thread's period: lengths, and the sampled fraction of the period above Im 2 in
     the standard fundamental domain, against the one-departure arc above Im 2;
  E  SnapPy's layered triangulation b++ L^n R (LR)^k (n = 5, 6; k = 8, 12): the reflections of the cyclic sequence of
     tetrahedra under which the shapes are symmetric (as Z/3 orbits), whether the pairing preserves or conjugates
     shapes, the central shape, its reduction to the fundamental domain, and the highest tetrahedra.

    python3 read_out_check.py
"""
import math
import warnings
from fractions import Fraction as Fr

import mpmath as mp

warnings.filterwarnings("ignore", message="Plink failed to import tkinter")
import snappy  # noqa: E402

mp.mp.dps = 60
L = ((1, 0), (1, 1))
R = ((1, 1), (0, 1))
J0 = ((-1, 0), (0, 1))
I2 = ((1, 0), (0, 1))
SQ5 = mp.sqrt(5)
PHI = (1 + SQ5) / 2
TINY = mp.mpf(10) ** -40

N_RANGE = range(1, 13)                 # part A
B_WORDS = [("golden loop", "LR")] + [("L^%d R (LR)^%d" % (n, k), "L" * n + "R" + "LR" * k)
                                     for n in (5, 6) for k in range(0, 7)]
D_LENGTH_K = (0, 1, 2, 5, 10, 20, 40)
D_SAMPLE = ((5, 5), (6, 5), (5, 20), (6, 20))
D_N = 4000
E_CASES = ((5, 8), (5, 12), (6, 8), (6, 12))


def mul(A, B):
    return ((A[0][0] * B[0][0] + A[0][1] * B[1][0], A[0][0] * B[0][1] + A[0][1] * B[1][1]),
            (A[1][0] * B[0][0] + A[1][1] * B[1][0], A[1][0] * B[0][1] + A[1][1] * B[1][1]))


def det(A):
    return A[0][0] * A[1][1] - A[0][1] * A[1][0]


def inv(A):
    d = det(A)
    assert d in (1, -1)
    return ((A[1][1] * d, -A[0][1] * d), (-A[1][0] * d, A[0][0] * d))


def neg(A):
    return tuple(tuple(-x for x in r) for r in A)


def peq(A, B):
    return A == B or A == neg(B)


def mat(word):
    M = I2
    for ch in word:
        M = mul(M, L if ch == "L" else R)
    return M


def act(g, z):
    """Moebius action for det +1, anti-Moebius (on conj z) for det -1."""
    p, q, r, s = g[0][0], g[0][1], g[1][0], g[1][1]
    w = z if det(g) == 1 else mp.conj(z)
    return (p * w + q) / (r * w + s)


def to_F(z):
    for _ in range(100000):
        z = z - mp.floor(z.real + mp.mpf(1) / 2)
        if abs(z) < 1 - mp.mpf(10) ** -50:
            z = -1 / z
        else:
            return z
    raise RuntimeError("reduction did not stop")


def mirror_dist(x):
    """distance of a real part (reduced to [-1/2, 1/2)) from the mirrors Re = 0 and Re = +-1/2"""
    return min(abs(x), abs(abs(x) - mp.mpf(1) / 2))


# ---------------------------------------------------------------- A
def nullspace(rows):
    """Exact rational nullspace (Gauss-Jordan over Fractions); basis vectors scaled to primitive integer tuples."""
    A = [[Fr(x) for x in r] for r in rows]
    ncols = len(A[0])
    pivots = []
    r = 0
    for c in range(ncols):
        piv = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if piv is None:
            continue
        A[r], A[piv] = A[piv], A[r]
        pv = A[r][c]
        A[r] = [x / pv for x in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
        if r == len(A):
            break
    basis = []
    for fc in [c for c in range(ncols) if c not in pivots]:
        v = [Fr(0)] * ncols
        v[fc] = Fr(1)
        for i, pc in enumerate(pivots):
            v[pc] = -A[i][fc]
        den = math.lcm(*[x.denominator for x in v])
        w = [int(x * den) for x in v]
        g = math.gcd(*w)
        basis.append(tuple(x // g for x in w))
    return basis


def qmul(x, y):
    return (x[0] * y[0] + 5 * x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def stabiliser_exact(n):
    a = (Fr(1, 2), Fr(-1, 2))            # -1/phi = (1 - sqrt5)/2
    b = (Fr(2 * n - 1, 2), Fr(1, 2))     # n + 1/phi = (2n - 1 + sqrt5)/2

    def rows(x, y):                      # g(x) = y  <=>  p x + q - r x y - s y = 0 ; rational and sqrt5 parts
        xy = qmul(x, y)
        return [[x[0], 1, -xy[0], -y[0]], [x[1], 0, -xy[1], -y[1]]]
    return {name: nullspace(rows(*e1) + rows(*e2))
            for name, (e1, e2) in (("swap", ((a, b), (b, a))), ("fix", ((a, a), (b, b))))}


def part_A():
    print("A. THE ONE-DEPARTURE HISTORY'S STABILISER IN PGL(2, Z), solved exactly over Q(sqrt5)")
    print("   (the history is the geodesic from -1/phi to n + 1/phi; g = [[p, q], [r, s]] acts on its ends by")
    print("   x -> (p x + q)/(r x + s); 'swap' exchanges the ends, 'fix' fixes both; rank = dimension of the solutions)")
    for n in N_RANGE:
        res = stabiliser_exact(n)
        line = "   n = %2d: swap rank %d, fix rank %d" % (n, len(res["swap"]), len(res["fix"]))
        if len(res["swap"]) == 1 and len(res["fix"]) == 1:
            p, q, r, s = res["swap"][0]
            g = ((p, q), (r, s))
            fp, fq, fr_, fs = res["fix"][0]
            apex = mp.mpc(mp.mpf(n) / 2, (n - 1 + SQ5) / 2)
            centre, radius = mp.mpf(n) / 2, (n - 1 + SQ5) / 2
            on_history = abs(abs(apex - centre) - radius) < TINY
            fixed = abs(act(g, apex) - apex) < TINY
            line += ("; swap basis %s, det %d; fix basis %s, det %d; the swap fixes the apex %s + %si: %s; "
                     "the apex is on the history: %s" % ((p, q, r, s), det(g), (fp, fq, fr_, fs),
                                                          fp * fs - fq * fr_, mp.nstr(apex.real, 6),
                                                          mp.nstr(apex.imag, 12), fixed, on_history))
        print(line)


# ---------------------------------------------------------------- B
def axis(W):
    a, b, c, d = W[0][0], W[0][1], W[1][0], W[1][1]
    return mp.mpf(a - d) / (2 * c), mp.sqrt(mp.mpf((a + d) ** 2 - 4)) / (2 * abs(c))


def length(W):
    return 2 * mp.acosh(mp.mpf(abs(W[0][0] + W[1][1])) / 2)


def mirror_point(g, c0, rho):
    p, q, r, s = g[0][0], g[0][1], g[1][0], g[1][1]
    assert det(g) == -1 and p + s == 0
    X = mp.mpf(-q) / (2 * p) if r == 0 else (q - r * (rho ** 2 - c0 ** 2)) / (2 * (r * c0 - p))
    Y = mp.sqrt(rho ** 2 - (X - c0) ** 2)
    z = mp.mpc(X, Y)
    assert abs(act(g, z) - z) < TINY
    return z


def half_root(W):
    if W[0][0] + W[1][1] < 0:
        W = neg(W)
    t = W[0][0] + W[1][1]
    for kind, d, E, sq in (("glide (det -1)", -1, ((W[0][0] - 1, W[0][1]), (W[1][0], W[1][1] - 1)), t - 2),
                           ("square (det +1)", 1, ((W[0][0] + 1, W[0][1]), (W[1][0], W[1][1] + 1)), t + 2)):
        if sq <= 0:
            continue
        u = math.isqrt(sq)
        if u * u == sq and all(x % u == 0 for r in E for x in r):
            G = tuple(tuple(x // u for x in r) for r in E)
            if det(G) == d and peq(mul(G, G), W):
                return kind, G
    return None, None


def symmetric_points(word):
    W = mat(word)
    m = len(word)
    c0, rho = axis(W)
    ell = length(W)
    kind, _ = half_root(W)
    ellmin = ell / 2 if kind else ell
    pts = []
    for i in range(m):
        w2 = word[i:] + word[:i]
        C = mat(word[:i])
        W2 = mat(w2)
        for j in range(m + 1):
            P, Qw = w2[:j], w2[j:]
            if P == P[::-1] and Qw == Qw[::-1]:
                g2 = mul(mat(P), J0)
                assert peq(mul(mul(g2, W2), g2), inv(W2)) and peq(mul(g2, g2), I2)
                g = mul(mul(C, g2), inv(C))
                assert peq(mul(mul(g, W), g), inv(W))
                z = mirror_point(g, c0, rho)
                pts.append((mp.asinh((z.real - c0) / z.imag), z))
    classes = []
    for s, z in pts:
        r = s - ellmin * mp.floor(s / ellmin)
        for cl in classes:
            dd = abs(r - cl[0])
            if min(dd, ellmin - dd) < mp.mpf(10) ** -30:
                cl[1].append(z)
                break
        else:
            classes.append([r, [z]])
    return W, ell, kind, ellmin, classes, len(pts)


def part_B():
    print("B. SYMMETRIC POINTS ON CLOSED AXES (fixed points of the direction-reversing reflections P J0 built from the")
    print("   palindromic factorisations of the cyclic word), counted modulo the axis's minimal translation")
    for label, word in B_WORDS:
        W, ell, kind, ellmin, classes, npts = symmetric_points(word)
        print("   %-16s tr %d, length %s, root: %s, minimal translation %s, %d reflections found, %d classes" % (
            label, abs(W[0][0] + W[1][1]), mp.nstr(ell, 10), kind, mp.nstr(ellmin, 10), npts, len(classes)))
        reps = []
        for r, zs in sorted(classes, key=lambda c: -to_F(c[1][0]).imag):
            zf = to_F(zs[0])
            reps.append(r)
            print("      class at %s mod %s: reduced to F |Re| %s, Im %s (members %d)" % (
                mp.nstr(r, 12), mp.nstr(ellmin, 8), mp.nstr(abs(zf.real), 12), mp.nstr(zf.imag, 12), len(zs)))
        if len(reps) == 2:
            sep = abs(reps[0] - reps[1])
            sep = min(sep, ellmin - sep)
            print("      separation of the two classes %s; half the minimal translation %s" % (
                mp.nstr(sep, 15), mp.nstr(ellmin / 2, 15)))


# ---------------------------------------------------------------- C
def part_C():
    print("C. WHERE THE APEX SITS IN THE FAREY TESSELLATION (the mirror Re tau = n/2 of the run's fan of n triangles)")
    for n in range(2, 13):
        where = ("on the Farey edge (%d, oo): the symmetric object is a flip (a tetrahedron)" % (n // 2)
                 if n % 2 == 0 else
                 "inside the Farey triangle (%d, %d, oo): the symmetric object is a triangulation (a surface)"
                 % ((n - 1) // 2, (n + 1) // 2))
        print("   n = %2d: apex Re %s, %s" % (n, Fr(n, 2), where))


# ---------------------------------------------------------------- D
def frac_above(word, y0=2):
    W = mat(word)
    c0, rho = axis(W)
    ell = length(W)
    cnt = 0
    for t in range(D_N):
        s = -ell / 2 + ell * (t + mp.mpf(1) / 2) / D_N
        z = mp.mpc(c0 + rho * mp.tanh(s), rho / mp.cosh(s))
        if to_F(z).imag > y0:
            cnt += 1
    return mp.mpf(cnt) / D_N, ell


def part_D():
    print("D. THE DEPARTURE'S SHARE OF A CLOSED THREAD'S PERIOD")
    ell_gold = length(mat("LR"))
    print("   the golden loop's length l(LR) = %s (= 4 log phi: %s)" % (mp.nstr(ell_gold, 15),
                                                                     mp.nstr(4 * mp.log(PHI), 15)))
    for n in (5, 6):
        r_n = (n - 1 + SQ5) / 2
        A_n = 2 * mp.acosh(r_n / 2)
        print("   n = %d: the one-departure arc above Im 2 has length A_n = 2 acosh(r_n / 2) = %s (r_n = %s)" % (
            n, mp.nstr(A_n, 10), mp.nstr(r_n, 10)))
        for k in D_LENGTH_K:
            ell = length(mat("L" * n + "R" + "LR" * k))
            print("      k = %2d: l = %s, l - k l(LR) = %s, A_n / l = %s" % (
                k, mp.nstr(ell, 12), mp.nstr(ell - k * ell_gold, 12), mp.nstr(A_n / ell, 6)))
    for n, k in D_SAMPLE:
        f, ell = frac_above("L" * n + "R" + "LR" * k)
        A_n = 2 * mp.acosh((n - 1 + SQ5) / 4)
        print("   sampled (%d points, uniform in arclength over one period): L^%d R (LR)^%d fraction above Im 2 = %s;"
              " A_n / l = %s" % (D_N, n, k, mp.nstr(f, 6), mp.nstr(A_n / ell, 6)))


# ---------------------------------------------------------------- E
def z3(z):
    return (z, 1 / (1 - z), 1 - 1 / z)


def d_same(z, w):
    return min(abs(w - u) for u in z3(z))


def d_conj(z, w):
    return min(abs(w - u) for u in z3(1 / mp.conj(z)))


def height(z):
    return to_F(z).imag


def part_E():
    print("E. SNAPPY %s: THE LAYERED TRIANGULATION b++ L^n R (LR)^k" % snappy.__version__)
    for n, k in E_CASES:
        word = "L" * n + "R" + "LR" * k
        M = snappy.ManifoldHP("b++" + word)
        m = M.num_tetrahedra()
        print("   n = %d, k = %2d: %d letters, %d tetrahedra, %s" % (n, k, len(word), m, M.solution_type()))
        if m != len(word):
            print("      PART E VOID for this case: the tetrahedra are not one per letter")
            continue
        sh = [mp.mpc(mp.mpf(str(z.real())), mp.mpf(str(z.imag()))) for z in M.tetrahedra_shapes("rect")]
        syms = []
        for t in range(m):
            dmax = max(d_same(sh[i], sh[(t - i) % m]) for i in range(m))
            syms.append((dmax, t))
        good = [t for dmax, t in syms if dmax < mp.mpf(10) ** -20]
        best_other = min(dmax for dmax, t in syms if t not in good) if len(good) < m else None
        print("      reflections i -> t - i (mod %d) preserving the shapes as Z/3 orbits: %s; the next best fails by %s"
              % (m, good, mp.nstr(best_other, 4) if best_other is not None else "-"))
        heights = [height(z) for z in sh]
        top = max(heights)
        tops = [i for i, h in enumerate(heights) if top - h < mp.mpf(10) ** -20]
        print("      the highest tetrahedra (height = Im of the shape reduced to F): %s, height %s" % (
            tops, mp.nstr(top, 12)))
        for t in good:
            centres = sorted({Fr(t, 2) % m, (Fr(t, 2) + Fr(m, 2)) % m})
            print("      t = %d: centres %s (an integer centre is a tetrahedron fixed by the reflection)" % (
                t, [str(c) for c in centres]))
            for c in centres:
                where = "in the run (letters 0..%d)" % (n - 1) if 0 <= c <= n else "in the alternating block"
                near = sorted(((i, (t - i) % m) for i in range(m) if i != (t - i) % m),
                              key=lambda pr: min(abs(Fr(pr[0]) - c), m - abs(Fr(pr[0]) - c)))
                seen = []
                for i, j in near:
                    if (min(i, j), max(i, j)) not in seen:
                        seen.append((min(i, j), max(i, j)))
                    if len(seen) == 3:
                        break
                print("         centre %s, %s; the three nearest pairs:" % (c, where))
                for i, j in seen:
                    print("            pair (%d, %d): same-orbit distance %s, conjugate-orbit distance %s" % (
                        i, j, mp.nstr(d_same(sh[i], sh[j]), 3), mp.nstr(d_conj(sh[i], sh[j]), 6)))
                if c.denominator == 1:
                    i = int(c)
                    z = sh[i]
                    zm = max(z3(z), key=lambda u: u.imag)
                    zf = to_F(z)
                    print("         central tetrahedron %d: shape %s, highest orbit member %s, reduced to F %s;"
                          " distance of Re from the mirrors %s; conjugate-orbit self-distance %s" % (
                              i, mp.nstr(z, 12), mp.nstr(zm, 12), mp.nstr(zf, 12),
                              mp.nstr(mirror_dist(zf.real), 6), mp.nstr(d_conj(z, z), 6)))


if __name__ == "__main__":
    print("THE READ-OUT THE HISTORY'S SYMMETRY FORCES -- data-free check (the web seat, 2026-11-06)")
    part_A()
    part_B()
    part_C()
    part_D()
    part_E()
    print("read_out_check exit 0")
