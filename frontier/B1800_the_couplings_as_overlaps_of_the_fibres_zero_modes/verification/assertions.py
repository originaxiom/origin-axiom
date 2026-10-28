"""B1800: the closed form's normalisation and the identities, asserted (not fitted).
(1) K(tau) = (Im tau)^(-1/4): every allowed overlap equals (Im tau)^(-1/4) theta[(a_p - a_q + m)/2, b_p - b_q](0, 2 tau)
    e^{2 pi i s_m db} (closed_form.py's prediction, now with K predicted);
(2) theta[1/4, 0](0, 2tau) = theta2(tau/2)/2 and theta[1/4, 1/2](0, 2tau) = e^{i pi/8} theta2((tau+1)/2)/2 (40 digits);
(3) the squares: c32^2 = theta2 theta3 / 2, c34^2 = theta4(2tau)^2 = theta3 theta4, c24^2 = (i/2) theta2 theta4 (40 digits),
    so Y_pq^2 = K^2 kappa_pq theta_p(tau) theta_q(tau) (kappa = 1/2, 1, i/2) and, by Jacobi (theta2 theta3 theta4 = 2 eta^3),
    Y_pq ~ eta^(3/2) theta_r^(-1/2).
    python3 -B assertions.py"""
import numpy as np, mpmath as mp
import overlaps as O, closed_form as CF
mp.mp.dps = 45
def thm(a, b, t, N=60):
    return mp.fsum(mp.exp(1j * mp.pi * (n + a)**2 * t + 2j * mp.pi * (n + a) * b) for n in range(-N, N + 1))
worst1 = 0.0
for t in [complex(a, b) for a, b in ((0.37, 1.2), (0.0, 1.0), (0.45, 2.0), (-0.21, 0.73))]:
    per, ip, ortho, Y = O.run(t, n=96)
    for (p, q, a, b, k), v in Y.items():
        if ip[(p, q, a, b, k)] > 1e-8: continue
        (a1, b1), (a2, b2) = O.CH[p], O.CH[q]; ca, cb = (k + a) / 2, b; pred = 0j
        for m in (0, 1):
            s = (a1 + a2 + m) / 2; da, db = s - ca, (b1 + b2) - cb
            if abs(da - round(da)) < 1e-12 and abs(db - round(db)) < 1e-12:
                pred += CF.thc((a1 - a2 + m) / 2, b1 - b2, 2 * t) * np.exp(2j * np.pi * s * round(db))
        worst1 = max(worst1, abs(v - t.imag**-0.25 * pred))
print("(1) K = (Im tau)^(-1/4) predicted: max |quadrature - prediction| over four tau = %.1e" % worst1); assert worst1 < 1e-12
worst2 = worst3 = mp.mpf(0)
for t in [mp.mpc(0.37, 1.2), mp.mpc(0.0, 1.0), mp.mpc(0.45, 2.0), mp.mpc(-0.21, 0.73), mp.mpc(0.13, 3.1)]:
    th2, th3, th4 = thm(0.5, 0, t), thm(0, 0, t), thm(0, 0.5, t)
    c32, c34, c24 = thm(0.25, 0, 2 * t), thm(0, 0.5, 2 * t), thm(0.25, 0.5, 2 * t)
    worst2 = max(worst2, abs(c32 - thm(0.5, 0, t / 2) / 2), abs(c24 - mp.exp(1j * mp.pi / 8) * thm(0.5, 0, (t + 1) / 2) / 2))
    worst3 = max(worst3, abs(c32**2 - th2 * th3 / 2), abs(c34**2 - th3 * th4), abs(c24**2 - 0.5j * th2 * th4))
print("(2) quarter-characteristic identities: max |diff| %.1e" % float(worst2)); assert worst2 < mp.mpf(10)**-35
print("(3) the squares Y_pq^2 ~ theta_p theta_q: max |diff| %.1e" % float(worst3)); assert worst3 < mp.mpf(10)**-35
print("assertions exit 0")
