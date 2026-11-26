"""B2011, A1, A2, A6, A7 (main, 2026-11-26; data-free): agy's C60 level claims rebuilt on main's own code.
A1 mod 135 and A2 mod 45: exact sector polynomials (sectors_exact.py), the gcd of p_neutral(2x)/2^d with the charged
polynomial, and what is left unpaired on each side, factored. Whether rho factors through G_135: the orbit mod 135 reduces
onto the orbit mod 27 (checked), so every word trivial mod 135 is trivial mod 27, and rho factors through G_27 (B2005).
A6: the order of the permutation [C^-1, sigma]^3 on the orbit at mod 27, 81, 243. A7: P6 against p_neutral at mod 81.
    python3 -B c60_levels.py > c60_levels_run.txt"""
import pathlib, sys, time, math
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import flint, mpmath as mp
from sectors_exact import leaf, sector_data, exact_charpolys, halved_monic
t0 = time.time()
log = lambda s: print(s + "  [%.0f s]" % (time.time() - t0), flush=True)
X = flint.fmpz_poly([0, 1])


def pairing(N):
    d = sector_data(N)
    log("mod %d, orbit of (3,3,3): %d points; C fixes %d; neutral dimension %d, charged (q = 1) dimension %d" % (N, d["n"], d["fixed"], d["d0"], d["d1"]))
    pn, pc = exact_charpolys(d, log)
    h = halved_monic(pn)
    g = h.gcd(pc)
    un_c, r1 = divmod(pc, g); un_n, r2 = divmod(h, g)
    assert r1 == 0 and r2 == 0
    fac = lambda f: [([int(c) for c in q.coeffs()], e) for q, e in f.factor()[1]] if f.degree() > 0 else []
    log("    degree of gcd(p_neutral(2x)/2^d, S): %d of the charged %d" % (g.degree(), pc.degree()))
    log("    charged left unpaired: degree %d; factors (constant first, multiplicity): %s" % (un_c.degree(), fac(un_c)))
    log("    neutral left unpaired (in x = half the neutral eigenvalue): degree %d; factors: %s" % (un_n.degree(), fac(un_n)))
    if g.degree() <= 12:
        log("    the gcd itself: %s" % fac(g))
    return d, pn, pc, g, un_c, un_n


# A1: mod 135
d135, pn135, pc135, g135, unc135, unn135 = pairing(135)
pts135, _, _ = leaf(135); pts27, _, _ = leaf(27)
red = {(a % 27, b % 27, c % 27) for a, b, c in pts135}
log("    reduction mod 27 maps the mod-135 orbit onto the mod-27 orbit: %s (so rho factors through G_135, via G_27)" % (red == set(pts27)))
want = flint.fmpz_poly([-2, -2, 1]) * flint.fmpz_poly([-2, 2, 1]) * flint.fmpz_poly([-1, -3, 0, 1]) * flint.fmpz_poly([1, -3, 0, 1])
log("    A1: the charged unpaired part equals (x^2 - 2x - 2)(x^2 + 2x - 2)(x^3 - 3x - 1)(x^3 - 3x + 1): %s" % (unc135 == want))

# A2: mod 45
d45, pn45, pc45, g45, unc45, unn45 = pairing(45)
log("    A2: gcd == x^2 (x - 2)(x + 2): %s" % (g45 == X * X * flint.fmpz_poly([-2, 1]) * flint.fmpz_poly([2, 1])))

# A6: [C^-1, sigma]^3
for N in (27, 81, 243):
    pts, _, C = leaf(N); idx = {v: i for i, v in enumerate(pts)}
    Ci = lambda v: (v[2], v[0], v[1])
    sig = lambda v, N=N: (v[1], v[0], (v[0] * v[1] - v[2]) % N)
    comm = lambda v: Ci(sig(C(sig(v))))          # C^-1 sigma C sigma (sigma an involution), applied right to left
    w = lambda v: comm(comm(comm(v)))
    perm = [idx[w(v)] for v in pts]
    seen = [False] * len(perm); order = 1
    for i in range(len(perm)):
        if seen[i]:
            continue
        L = 0; j = i
        while not seen[j]:
            seen[j] = True; j = perm[j]; L += 1
        order = order * L // math.gcd(order, L)
    moved = sum(1 for i, p in enumerate(perm) if p != i)
    log("A6: mod %d: [C^-1, sigma]^3 has order %d on the orbit; points moved %d of %d" % (N, order, moved, len(pts)))

# A7: P6 at mod 81
d81 = sector_data(81); pn81, _ = exact_charpolys(d81)
P6 = flint.fmpz_poly([-4672, 0, 1008, 0, -60, 0, 1])
q, r = divmod(pn81, P6)
mp.mp.dps = 40
roots = mp.polyroots([1, 0, -60, 0, 1008, 0, -4672], maxsteps=200, extraprec=200)
top = max(mp.re(z) for z in roots)
val = 2 * mp.sqrt(5 + 4 * mp.cos(mp.pi / 9))
mult = 0; f = pn81
while True:
    qq, rr = divmod(f, P6)
    if rr != 0:
        break
    f = qq; mult += 1
log("A7: P6 divides p_neutral at mod 81: %s (multiplicity %d); its largest root %s; 2 sqrt(5 + 4 cos(pi/9)) = %s; difference %s" % (r == 0, mult, mp.nstr(top, 25), mp.nstr(val, 25), mp.nstr(abs(top - val), 3)))
log("    Phi_18(-2) = %d, Phi_6(-2) = %d" % ((-2) ** 6 - (-2) ** 3 + 1, (-2) ** 2 - (-2) + 1))
