"""The period phase (Theorem 4 of the note) on closed geodesics. D = -theta_3^4 h(lambda) / (4 pi eta^6),
lambda = theta_2^4 / theta_3^4, h(l) = l log|l| + (1-l) log|1-l|. Along the axis of gamma (a positive word in
L = [[1,1],[0,1]] and R = [[1,0],[1,1]]), parametrised by arclength s, psi(s) = D(z(s)) (dz/ds)^(-1/2), with the square root
continued along [s, s + l]. The check: psi(s + l) / psi(s) = i^(#L - #R), the branch sign +1, at three start points."""
import mpmath as mp
mp.mp.dps = 30
def D(tau):
    q = mp.exp(1j * mp.pi * tau); t2, t3 = mp.jtheta(2, 0, q), mp.jtheta(3, 0, q)
    lam = t2 ** 4 / t3 ** 4; h = lam * mp.log(abs(lam)) + (1 - lam) * mp.log(abs(1 - lam))
    q2 = mp.exp(2j * mp.pi * tau); eta = mp.exp(2j * mp.pi * tau / 24) * mp.qp(q2)
    return -t3 ** 4 * h / (4 * mp.pi * eta ** 6)
Lm = mp.matrix([[1, 1], [0, 1]]); Rm = mp.matrix([[1, 0], [1, 1]])
worst = 0
for word in ("LR", "LLR", "LRR", "LLLR", "LLRR", "LRLLR", "LLLLRRL", "LRRRRR"):
    g = mp.eye(2)
    for ch in word: g = g * (Lm if ch == "L" else Rm)
    a, b, c, d = g[0, 0], g[0, 1], g[1, 0], g[1, 1]
    disc = mp.sqrt((a + d) ** 2 - 4)
    fp = [((a - d) + sgn * disc) / (2 * c) for sgn in (1, -1)]
    lam1 = (a + d + disc) / 2                                    # the larger eigenvalue
    att = [x for x in fp if abs(c * x + d - lam1) < 1e-20][0]   # attracting: cx+d = lam1, derivative (cx+d)^-2 = lam1^-2 < 1
    rep = [x for x in fp if x != att][0]
    cen, rad = (att + rep) / 2, abs(att - rep) / 2
    sgn = 1 if att > rep else -1
    z = lambda s: cen + sgn * rad * mp.tanh(s) + 1j * rad / mp.cosh(s)
    dz = lambda s: sgn * rad / mp.cosh(s) ** 2 - 1j * rad * mp.tanh(s) / mp.cosh(s)
    ell = 2 * mp.acosh(abs(a + d) / 2)
    phase_expected = 1j ** (word.count("L") - word.count("R"))
    for s0 in (-0.7, 0.1, 1.3):
        # continue (dz/ds)^(-1/2) along [s0, s0 + ell]: unwrap the argument of dz/ds
        n = 400; args = []; prev = None
        for k in range(n + 1):
            v = dz(s0 + ell * k / n); a_ = mp.arg(v)
            if prev is not None:
                while a_ - prev > mp.pi: a_ -= 2 * mp.pi
                while a_ - prev < -mp.pi: a_ += 2 * mp.pi
            args.append(a_); prev = a_
        r0 = abs(dz(s0)) ** -0.5 * mp.exp(-0.5j * args[0]); r1 = abs(dz(s0 + ell)) ** -0.5 * mp.exp(-0.5j * args[-1])
        ratio = D(z(s0 + ell)) * r1 / (D(z(s0)) * r0)
        err = abs(ratio - phase_expected); worst = max(worst, err)
    print(f"{word:>8}: i^(#L-#R) = {mp.nstr(phase_expected, 3)}, worst return error over three starts {mp.nstr(err, 3)}")
print(f"worst error: {mp.nstr(worst, 3)}"); assert worst < 1e-15; print("all checks pass")
