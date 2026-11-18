"""B1957: the web seat's note 'the weave's own action on tau, graded by the clause' (2026-11-10): the mathematics it
states, checked on main.  Nothing in the note is computed by the seat (it grades the record); these are the facts its
grading leans on.  Data-free.
 S1  STATIONARITY (its section 3, proved there in two lines; the proof holds: a linear form fixed by a rotation of
     order 2 or 3 is zero).  Numerically, for three invariant functions (log(y |eta|^4), E(tau, 3), E(tau, 2)): the
     gradient at i and at omega, and at a generic point as the control.
 S2  THE KINDS OF THE CRITICAL POINTS: y|eta|^4 has a saddle at i and its maximum at omega; E(tau, 3) and E(tau, 2)
     have a saddle at i and their minimum at omega, and grow to the cusp.
 S3  KRONECKER'S LIMIT (its row D): the constant term of the Epstein sum at s = 1 is -pi log(y |eta|^4) + 2 pi (gamma - log 2).
 S4  THE FOUR IN SIX DIMENSIONS (its row C0): the three parity lines' sum is -(15/16) E(tau, 3) times the trivial
     line's normalisation, i.e. sum over the three non-zero half-period characters chi of sum' chi(m, n) |m tau + n|^-6
     = -(15/16) sum' |m tau + n|^-6.
 S5  McSHANE'S IDENTITY (its row B) on the modular torus: the sum of 1/(1 + e^l) over the simple closed geodesics is
     1/2 (traces 3m over the Markoff numbers m, each geodesic once).
 S6  THE SYSTOLE (its row G): on the once-punctured torus of the Markoff triple (3, 3, 3) the three shortest
     geodesics have trace 3, length 2 arccosh(3/2)."""
import functools, itertools
import mpmath as mp
mp.mp.dps = 30
print = functools.partial(print, flush=True)
I = mp.mpc(0, 1); OM = mp.mpc(-0.5, mp.sqrt(3) / 2); GEN = mp.mpc("0.137", "1.213")
eta = lambda t: mp.exp(mp.pi * I * t / 12) * mp.nprod(lambda n: 1 - mp.exp(2 * mp.pi * I * n * t), [1, mp.inf])
f_eta = lambda x, y: mp.log(y * abs(eta(mp.mpc(x, y))) ** 4)


def eis(s, N=60):
    """the direct lattice sum over a square box (used only as a control of the Fourier form)"""
    def f(x, y):
        t = mp.mpc(x, y); tot = mp.mpf(0)
        for m in range(-N, N + 1):
            for n in range(-N, N + 1):
                if m or n: tot += y ** s / abs(m * t + n) ** (2 * s)
        return tot
    return f


def E_fourier(t, s, R=40):
    """sum' y^s |m tau + n|^-2s by its Fourier expansion in x"""
    x, y = t.real, t.imag; first = 2 * mp.zeta(2 * s) * y ** s + 2 * mp.sqrt(mp.pi) * mp.gamma(s - mp.mpf(1) / 2) / mp.gamma(s) * mp.zeta(2 * s - 1) * y ** (1 - s); b = mp.mpf(0)
    for n in range(1, R + 1):
        sig = sum(mp.mpf(d) ** (2 * s - 1) for d in range(1, n + 1) if n % d == 0)
        b += n ** (mp.mpf(1) / 2 - s) * sig * mp.besselk(s - mp.mpf(1) / 2, 2 * mp.pi * n * y) * mp.cos(2 * mp.pi * n * x)
    return first + 8 * mp.pi ** s * mp.sqrt(y) / mp.gamma(s) * b


def grad_hess(f, p, h=mp.mpf("1e-5")):
    x, y = p.real, p.imag
    gx = (f(x + h, y) - f(x - h, y)) / (2 * h); gy = (f(x, y + h) - f(x, y - h)) / (2 * h)
    fxx = (f(x + h, y) - 2 * f(x, y) + f(x - h, y)) / h ** 2; fyy = (f(x, y + h) - 2 * f(x, y) + f(x, y - h)) / h ** 2
    fxy = (f(x + h, y + h) - f(x + h, y - h) - f(x - h, y + h) + f(x - h, y - h)) / (4 * h ** 2)
    ev = mp.eigsy(mp.matrix([[fxx, fxy], [fxy, fyy]]), eigvals_only=True)
    return mp.sqrt(gx ** 2 + gy ** 2), sorted(float(v) for v in ev)


if __name__ == "__main__":
    Ef = lambda sv: (lambda x, y: E_fourier(mp.mpc(x, y), mp.mpf(sv)))
    for name, f in (("log(y |eta|^4)", f_eta), ("E(tau, 3)", Ef(3)), ("E(tau, 2)", Ef(2))):
        out = []
        for pn, p in (("i", I), ("omega", OM), ("a generic point", GEN)):
            g, ev = grad_hess(f, p); out.append("%s: |grad| %.1e, Hessian eigenvalues %s" % (pn, g, ["%.4f" % v for v in ev]))
        print("S1, S2: %s: %s" % (name, "; ".join(out)))
    E3 = Ef(3); print("S2: E(tau, 3) at i, at omega, at 2i, at 4i: %s (the least at omega, growing to the cusp)" % [mp.nstr(E3(p.real, p.imag), 8) for p in (I, OM, 2 * I, 4 * I)])
    # S3: Kronecker by the Fourier expansion at s = 1 +- d
    d = mp.mpf("1e-7"); worst = 0
    for t in (I, OM, GEN):
        const = (E_fourier(t, 1 + d) + E_fourier(t, 1 - d)) / 2; kron = -mp.pi * mp.log(t.imag * abs(eta(t)) ** 4) + 2 * mp.pi * (mp.euler - mp.log(2)); worst = max(worst, abs(const - kron))
    chk = abs(E_fourier(GEN, mp.mpf(3)) - eis(3, 60)(GEN.real, GEN.imag))
    print("S3: the constant term at s = 1 against -pi log(y |eta|^4) + 2 pi (gamma - log 2), at i, omega and a generic point: largest difference %.1e (the Fourier form against the direct sum at s = 3: %.1e)" % (worst, chk))
    # S4: the three half-period characters
    t = GEN; N = 40; tot0 = mp.mpf(0); totc = mp.mpf(0)
    for m in range(-N, N + 1):
        for n in range(-N, N + 1):
            if m or n:
                v = 1 / abs(m * t + n) ** 6; tot0 += v; totc += v * ((-1) ** m + (-1) ** n + (-1) ** (m + n))
    print("S4: the three parity characters' sum over the trivial sum at s = 3: %s (-15/16 = %s); exactly: sum of the three characters is 3 on the even sublattice and -1 off it, and the even sublattice carries 2^-6 of the sum, so 3/64 - (1 - 1/64) = -60/64" % (mp.nstr(totc / tot0, 12), mp.nstr(mp.mpf(-15) / 16, 12)))
    # S5: McShane on the modular torus through the Markoff tree
    # a simple closed geodesic is a region of the Markoff tree; its trace is 3 times the region's Markoff number, and 1/(1 + e^l) = (1 - sqrt(1 - 4/trace^2))/2
    g = lambda m: (1 - mp.sqrt(1 - mp.mpf(4) / (9 * mp.mpf(m) ** 2))) / 2
    # the three regions of the root triple (1, 1, 1), then one new region at each step down the tree
    total = 3 * g(1); count = 3; frontier = [((1, 1, 1), i) for i in range(3)]; steps = 0
    while frontier:
        (a, b, c), i = frontier.pop(); tr = [a, b, c]; new = 3 * tr[(i + 1) % 3] * tr[(i + 2) % 3] - tr[i]; tr[i] = new
        if new > 10 ** 14: continue
        total += g(new); count += 1; steps += 1
        for j in range(3):
            if j != i: frontier.append((tuple(tr), j))
    print("S5: McShane's sum over the simple closed geodesics of the modular torus (Markoff numbers to 1e14, %d geodesics): %s (the theorem: 1/2; one half minus the sum: %.1e)" % (count, mp.nstr(total, 12), float(mp.mpf(1) / 2 - total)))
    print("S6: the shortest geodesics have trace 3: length 2 arccosh(3/2) = %s" % mp.nstr(2 * mp.acosh(mp.mpf(3) / 2), 12))
