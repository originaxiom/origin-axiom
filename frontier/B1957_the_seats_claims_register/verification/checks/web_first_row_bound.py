"""B1957: the web seat's first-row check (2026-10-14): its data-free mathematics, on main.
The check's own subject is a quantity of a held-out target (the lepton mixing's first row).  NOTHING OF THAT IS
COMPUTED OR COMPARED HERE: no mixing matrix is formed and no measured value appears.  What is checked is the bound the
note proves and the three facts about the theta triplet it uses.
 B1  for u, v in C^n with sigma(w) = |w.w|/|w|^2 (w.w the bilinear form):
         |<u, v>|^2/(|u|^2 |v|^2) <= (1 + sigma_u sigma_v + sqrt((1 - sigma_u^2)(1 - sigma_v^2)))/2.
     Proof (the note's): complex conjugation is an isometry of the Fubini-Study metric d, d(x, conj x) = arccos sigma(x),
     and the triangle inequality gives d(u, v) >= |alpha_u - alpha_v| with alpha = arccos(sigma)/2.
     Checked on 3 x 10^5 random pairs in C^2, C^3, C^5 (four kinds), by 300 maximisations, and on the sharp pairs
     u = cos(a) x + i sin(a) y, v = cos(b) x + i sin(b) y at an 11 x 11 grid.
 B2  the case used: an isotropic direction (sigma = 0) against a real one (sigma = 1) overlaps by at most 1/2.
 B3  the theta triplet R = (-theta_2^2, -theta_4^2, i theta_3^2) is isotropic at every tau (Jacobi), and its largest
     overlap with a real unit vector is 1/2; on tau = iy, theta_3^4/(theta_2^4 + theta_3^4 + theta_4^4) = 1/2, and
     (theta_3^4 + theta_4^4)/(4 theta_3^4) = 3/8 at tau = i."""
import functools, math
import numpy as np
import mpmath as mp
print = functools.partial(print, flush=True)
rng = np.random.default_rng(11)
sig = lambda w: abs(np.sum(w * w)) / np.sum(np.abs(w) ** 2)
ratio = lambda u, v: abs(np.vdot(u, v)) ** 2 / (np.sum(np.abs(u) ** 2) * np.sum(np.abs(v) ** 2))
bound = lambda su, sv: 0.5 * (1 + su * sv + math.sqrt(max(0.0, (1 - su * su) * (1 - sv * sv))))


def draw(n, kind):
    g = lambda: rng.normal(size=n) + 1j * rng.normal(size=n)
    if kind == "gaussian": return g(), g()
    if kind == "isotropic against real":
        x = rng.normal(size=n); y = rng.normal(size=n); x /= np.linalg.norm(x); y -= x * (x @ y); y /= np.linalg.norm(y); return x + 1j * y, rng.normal(size=n).astype(complex)
    if kind == "near isotropic":
        x = rng.normal(size=n); y = rng.normal(size=n); x /= np.linalg.norm(x); y -= x * (x @ y); y /= np.linalg.norm(y); return x + 1j * y + 1e-3 * g(), g()
    return rng.normal(size=n) + 1e-3j * rng.normal(size=n), g()


if __name__ == "__main__":
    worst = -1.0; count = 0
    for n in (2, 3, 5):
        for kind in ("gaussian", "isotropic against real", "near isotropic", "near real"):
            for _ in range(25000):
                u, v = draw(n, kind); worst = max(worst, ratio(u, v) - bound(sig(u), sig(v))); count += 1
    print("B1: %d random pairs in C^2, C^3, C^5: the largest value of (overlap - bound): %.1e" % (count, worst))
    adv = -1.0
    for trial in range(300):
        n = (2, 3, 5)[trial % 3]; u = rng.normal(size=n) + 1j * rng.normal(size=n); v = rng.normal(size=n) + 1j * rng.normal(size=n); best = ratio(u, v) - bound(sig(u), sig(v))
        for it in range(400):
            du = 0.05 * (rng.normal(size=n) + 1j * rng.normal(size=n)); dv = 0.05 * (rng.normal(size=n) + 1j * rng.normal(size=n)); val = ratio(u + du, v + dv) - bound(sig(u + du), sig(v + dv))
            if val > best: u, v, best = u + du, v + dv, val
        adv = max(adv, best)
    print("B1: 300 maximisations of (overlap - bound) by random ascent: the largest reached %.1e" % adv)
    x = np.array([1.0, 0, 0]); y = np.array([0, 1.0, 0]); sharp = 0.0
    for a in np.linspace(0, math.pi / 4, 11):
        for b in np.linspace(0, math.pi / 4, 11):
            u = math.cos(a) * x + 1j * math.sin(a) * y; v = math.cos(b) * x + 1j * math.sin(b) * y; sharp = max(sharp, abs(ratio(u, v) - bound(sig(u), sig(v))))
    print("B1: the sharp pairs on an 11 x 11 grid attain the bound to %.1e; B2: at sigma_u = 0, sigma_v = 1 the bound is %.3f" % (sharp, bound(0.0, 1.0)))
    mp.mp.dps = 30; out = []
    for t in (mp.mpc(0, 1), mp.mpc(0, "1.5"), mp.mpc(0, 2), mp.mpc(0, 4), mp.mpc(-0.5, mp.sqrt(3) / 2), mp.mpc("0.3", "1.1"), mp.mpc("-0.2", "0.9"), mp.mpc("0.45", "2.5")):
        q = mp.exp(mp.pi * 1j * t); th2 = 2 * mp.nsum(lambda n: q ** ((n + mp.mpf(1) / 2) ** 2), [0, mp.inf]); th3 = 1 + 2 * mp.nsum(lambda n: q ** (n * n), [1, mp.inf]); th4 = 1 + 2 * mp.nsum(lambda n: (-1) ** n * q ** (n * n), [1, mp.inf])
        R = [-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]; iso = abs(sum(r * r for r in R)) / sum(abs(r) ** 2 for r in R)
        Rn = np.array([complex(r) for r in R]); Rn /= np.linalg.norm(Rn); A = np.outer(Rn.real, Rn.real) + np.outer(Rn.imag, Rn.imag); cap = float(np.linalg.eigvalsh(A)[-1])
        out.append((mp.nstr(t, 4), float(iso), cap))
    print("B3: (tau, |R.R|/|R|^2, the largest overlap of R with a real unit vector): %s" % [(a, "%.0e" % b, round(c, 12)) for a, b, c in out])
    t = mp.mpc(0, 1); q = mp.exp(mp.pi * 1j * t); th2 = 2 * mp.nsum(lambda n: q ** ((n + mp.mpf(1) / 2) ** 2), [0, mp.inf]); th3 = 1 + 2 * mp.nsum(lambda n: q ** (n * n), [1, mp.inf]); th4 = 1 + 2 * mp.nsum(lambda n: (-1) ** n * q ** (n * n), [1, mp.inf])
    print("B3: at tau = i: theta_3^4/(theta_2^4 + theta_3^4 + theta_4^4) = %s; (theta_3^4 + theta_4^4)/(4 theta_3^4) = %s" % (mp.nstr((th3 ** 4 / (th2 ** 4 + th3 ** 4 + th4 ** 4)).real, 12), mp.nstr(((th3 ** 4 + th4 ** 4) / (4 * th3 ** 4)).real, 12)))
