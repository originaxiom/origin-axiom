"""B1957: the web seat's zero-free Higgs directions (its notes of 2026-10-23): the data-free facts about the directions
themselves, on main.  The notes' subject is how these directions FIT measured numbers in main's frame; nothing of that
is computed here and no measured value appears.
 D1  F_a = eta^(3 - a) (eps theta_2^a, eps theta_4^a, i theta_3^a), a = 2 mod 4, eps = i^((a + 2)/2), twist r = 2a mod 24:
     the ten members with one unit of end data, their eps and r.
 D2  F_2's direction is the theta triplet R's, and it is isotropic (Jacobi).
 D3  the two isotropic components v+ = v.(0, 1, i) = eps theta_4^a - theta_3^a and v- = v.(0, 1, -i) = eps theta_4^a + theta_3^a;
     complex conjugation exchanges them; theta_3^a - theta_4^a is 4 a e^(i pi tau) near the cusp (the note: to 6e-5 at
     0.4 + 2.5i for all ten a, and only to 12 per cent at 0.1 + 1.3i for a = 26).
 D4  the tick's lines of the sealed rule: the points of order 5 fixed up to sign by LR are the multiples of (1, 2), and
     by RL the multiples of (1, 3), modulo 5.
 D5  for SU(2) matrices, eps conj(Q) eps^T = Q with eps = i sigma_2 (so the second reading is the first on the
     conjugate vector)."""
import functools
import mpmath as mp
import numpy as np
mp.mp.dps = 30
print = functools.partial(print, flush=True)


def thetas(t):
    q = mp.exp(mp.pi * 1j * t)
    return (2 * mp.nsum(lambda n: q ** ((n + mp.mpf(1) / 2) ** 2), [0, mp.inf]), 1 + 2 * mp.nsum(lambda n: q ** (n * n), [1, mp.inf]), 1 + 2 * mp.nsum(lambda n: (-1) ** n * q ** (n * n), [1, mp.inf]))


if __name__ == "__main__":
    members = [-10, 2, 14, 26, -6, 6, 18, -2, 10, 22]
    eps = lambda a: {0: 1, 1: 1j, 2: -1, 3: -1j}[((a + 2) // 2) % 4]
    print("D1: (a, eps, r): %s; every a is 2 mod 4: %s" % ([(a, int(eps(a).real), (2 * a) % 24) for a in members], all(a % 4 == 2 for a in members)))
    t = mp.mpc("0.3", "1.4"); th2, th3, th4 = thetas(t); F2 = [eps(2) * th2 ** 2, eps(2) * th4 ** 2, 1j * th3 ** 2]; R = [-th2 ** 2, -th4 ** 2, 1j * th3 ** 2]
    print("D2: F_2 = R componentwise: %s; R.R/|R|^2 = %.0e" % (all(abs(a - b) < mp.mpf("1e-25") for a, b in zip(F2, R)), abs(sum(x * x for x in R)) / sum(abs(x) ** 2 for x in R)))
    out = {}
    for name, tt in (("0.4 + 2.5i", mp.mpc("0.4", "2.5")), ("0.1 + 1.3i", mp.mpc("0.1", "1.3"))):
        th2, th3, th4 = thetas(tt); lead = mp.exp(mp.pi * 1j * tt); out[name] = {a: float(abs((th3 ** a - th4 ** a) / (4 * a * lead) - 1)) for a in members}
    print("D3: |(theta_3^a - theta_4^a)/(4 a e^(i pi tau)) - 1|: at 0.4 + 2.5i the largest over the ten a: %.1e; at 0.1 + 1.3i for a = 26: %.2f" % (max(out["0.4 + 2.5i"].values()), out["0.1 + 1.3i"][26]))
    th2, th3, th4 = thetas(mp.mpc("0.4", "2.5")); ok = True
    for a in members:
        v = [eps(a) * th2 ** a, eps(a) * th4 ** a, 1j * th3 ** a]; vp = v[1] + 1j * v[2]; vm = v[1] - 1j * v[2]; vb = [mp.conj(x) for x in v]
        ok &= abs(vp - (eps(a) * th4 ** a - th3 ** a)) < mp.mpf("1e-20") and abs(vm - (eps(a) * th4 ** a + th3 ** a)) < mp.mpf("1e-20") and abs((vb[1] + 1j * vb[2]) - mp.conj(vm)) < mp.mpf("1e-20")
    print("D3: v+ and v- as stated, and conjugation exchanges them, for all ten a: %s" % ok)
    LR = np.array([[2, 1], [1, 1]]); RL = np.array([[1, 1], [1, 2]])
    fix = lambda M: sorted((a, b) for a in range(5) for b in range(5) if (a, b) != (0, 0) and tuple((M @ np.array([a, b])) % 5) in ((a, b), ((-a) % 5, (-b) % 5)))
    print("D4: fixed up to sign by LR (acting on columns): %s; by RL: %s" % (fix(LR), fix(RL)))
    rng = np.random.default_rng(2); e = np.array([[0, 1], [-1, 0]]); worst = 0.0
    for _ in range(100):
        a, b = rng.normal(size=2) + 1j * rng.normal(size=2); n = np.sqrt(abs(a) ** 2 + abs(b) ** 2); Q = np.array([[a, b], [-np.conj(b), np.conj(a)]]) / n; worst = max(worst, np.max(np.abs(e @ Q.conj() @ e.T - Q)))
    print("D5: eps conj(Q) eps^T = Q on 100 random SU(2) matrices: largest difference %.1e" % worst)
