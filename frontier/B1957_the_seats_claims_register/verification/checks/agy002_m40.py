"""B1957: agy-002's note M40 (its standalone second computation of main's B1947): the closed transport law it states for
the twisted Higgs triplet under tau -> tau + 1, checked by main on its own theta functions, and against the component
ratios main's own B1947 run printed.  Data-free.
The triplet (the note's convention D1', representative eps = +1 or -1): with da = q_H a, db = q_H b,
  theta_2 = theta[1/2 + da, db], theta_3 = theta[da, db], theta_4 = theta[da, eps/2 + db]  (theta constants),
  R = (-theta_2/(theta_3 theta_4), -theta_4/(theta_2 theta_3), i theta_3/(theta_2 theta_4)).
The law: R(tau + 1; da, db - da) = exp(i pi/4 + i pi da^2) (R_0, exp(2 pi i eps da) R_2, -exp(-2 pi i eps da) R_1)(tau; da, db)."""
import mpmath as mp
mp.mp.dps = 40


def th(a, b, tau):
    return mp.nsum(lambda n: mp.exp(1j * mp.pi * (n + a) ** 2 * tau + 2j * mp.pi * (n + a) * b), [-mp.inf, mp.inf])


def R(tau, da, db, eps):
    t2, t3, t4 = th(mp.mpf(1) / 2 + da, db, tau), th(da, db, tau), th(da, mp.mpf(eps) / 2 + db, tau)
    return (-t2 / (t3 * t4), -t4 / (t2 * t3), 1j * t3 / (t2 * t4))


if __name__ == "__main__":
    worst = 0
    for tau in (mp.mpc("0.13", "1.45"), mp.mpc("-0.29", "1.18")):
        for (a, b) in ((mp.mpf(1) / 5, mp.mpf(2) / 5), (mp.mpf(2) / 5, mp.mpf(4) / 5), (mp.mpf(3) / 5, mp.mpf(1) / 5)):
            for qH in (3, -3):
                for eps in (1, -1):
                    da, db = qH * a, qH * b; new = R(tau + 1, da, db - da, eps); old = R(tau, da, db, eps); ph = mp.exp(1j * mp.pi / 4 + 1j * mp.pi * da ** 2)
                    pred = (ph * old[0], ph * mp.exp(2j * mp.pi * eps * da) * old[2], -ph * mp.exp(-2j * mp.pi * eps * da) * old[1])
                    worst = max(worst, max(abs(x / y - 1) for x, y in zip(new, pred)))
    print("the transport law, at two moduli, three points, both signs of the Higgs's charge and both representatives: largest relative deviation %s" % mp.nstr(worst, 3))
    for a, main_run in ((mp.mpf(1) / 5, "0.4258+0.9048i, 0.1874-0.9823i, -0.8763-0.4818i"), (mp.mpf(2) / 5, "-0.1874-0.9823i, 0.8763-0.4818i, -0.9921-0.1253i")):
        da = 3 * a; m = [mp.exp(1j * mp.pi * da ** 2), mp.exp(1j * mp.pi * (da ** 2 + 2 * da)), mp.exp(1j * mp.pi * (da ** 2 - 2 * da))]
        print("the law's extra multipliers at q_H = 3, a = %s: %s; main's B1947 run printed: %s" % (mp.nstr(a, 2), ", ".join("%.4f%+.4fi" % (float(z.real), float(z.imag)) for z in m), main_run))
    print("the three multipliers differ from one another unless q_H a is an integer or half-integer, so no single change of basis absorbs them: the twisted triplet is not covariant, which is B1947's negative")
