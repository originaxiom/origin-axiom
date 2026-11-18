"""B1957: the web seat's W-B1 (frame D and B1936's premise), its identities E1, E2, E5 and the bilinear's flip, on main.
Data-free.  theta[a, b](u, T) = sum_n exp(i pi (n + a)^2 T + 2 pi i (n + a)(u + b)).
 E1  N: theta[-a, -b](u, T) = theta[a, b](-u, T) (holomorphic).  K: conj theta[a, b](u, T) = theta[a, -b](-conj u, -conj T)
     = theta[-a, b](conj u, -conj T).  The plant (K with +b) fails.
 E2  R = (-theta_2^2, -theta_4^2, i theta_3^2)/(theta_2 theta_3 theta_4) under tau -> tau + 1 transforms by
     T_R = [[w, 0, 0], [0, 0, w], [0, w^-3, 0]], w = exp(i pi/4); its eigenvalues are eighth roots of unity, none a fifth.
 E5  the two conjugates N and K agree on the mirror's fixed slice (Re T = 0, u real) when b = 0, and differ at generic points.
 E6  main's own bilinear (frame_mp's bil_mp): bil(-x, -y, u, t) = -bil(x, y, -u, t)."""
import sys, pathlib, functools
import mpmath as mp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent)); import wb2_stage3_on_main as W
mp.mp.dps = 40


def th(a, b, u, T, N=60): return mp.nsum(lambda n: mp.exp(1j * mp.pi * (n + a) ** 2 * T + 2j * mp.pi * (n + a) * (u + b)), [-N, N])
rnd = lambda: mp.mpf(mp.rand()) * 2 - 1

if __name__ == "__main__":
    import random; random.seed(1957)                      # mpmath's rand draws from Python's generator: seeded on 2026-11-18 so that a rerun gives the same digits (the web seat's section 8)
    wN = wK1 = wK2 = 0; plant = mp.inf
    for _ in range(20):
        a, b = rnd(), rnd(); u = mp.mpc(rnd(), rnd() * 0.3); T = mp.mpc(rnd(), 0.6 + mp.rand())
        wN = max(wN, abs(th(-a, -b, u, T) - th(a, b, -u, T))); c = mp.conj(th(a, b, u, T))
        wK1 = max(wK1, abs(c - th(a, -b, -mp.conj(u), -mp.conj(T)))); wK2 = max(wK2, abs(c - th(-a, b, mp.conj(u), -mp.conj(T)))); plant = min(plant, abs(c - th(a, b, -mp.conj(u), -mp.conj(T))))
    print("E1: 20 random points: |theta[-a,-b](u) - theta[a,b](-u)| <= %s; |conj theta[a,b](u,T) - theta[a,-b](-conj u, -conj T)| <= %s; |... - theta[-a,b](conj u, -conj T)| <= %s; the plant with +b: at least %s" % (mp.nstr(wN, 3), mp.nstr(wK1, 3), mp.nstr(wK2, 3), mp.nstr(plant, 3)))
    def R(t):
        h = mp.mpf(1) / 2; t2, t3, t4 = th(h, 0, 0, t), th(0, 0, 0, t), th(0, h, 0, t); d = t2 * t3 * t4; return mp.matrix([-t2 ** 2 / d, -t4 ** 2 / d, 1j * t3 ** 2 / d])   # the theta constants as series in tau (a library's nome would lose the branch of q^(1/4) under tau + 1)
    w = mp.exp(1j * mp.pi / 4); TR = mp.matrix([[w, 0, 0], [0, 0, w], [0, w ** -3, 0]]); t0 = mp.mpc("0.17", "0.83"); ev = mp.eig(TR)[0]
    print("E2: |R(tau + 1) - T_R R(tau)| = %s; the eigenvalues of T_R as powers of w = exp(i pi/4): %s; the fifth power of each differs from 1 by at least %s" % (mp.nstr(mp.norm(R(t0 + 1) - TR * R(t0)), 3), sorted(int(mp.nint(mp.arg(e) / (mp.pi / 4))) % 8 for e in ev), mp.nstr(min(abs(e ** 5 - 1) for e in ev), 3)))
    same = 0; diff = mp.inf
    for _ in range(20):
        a = rnd(); u = mp.mpf(rnd()); T = mp.mpc(0, 0.6 + mp.rand()); same = max(same, abs(th(-a, 0, u, T) - mp.conj(th(a, 0, u, T))))
        a, b = rnd(), rnd(); u = mp.mpc(rnd(), rnd() * 0.3); T = mp.mpc(rnd(), 0.6 + mp.rand()); x, y = th(-a, -b, u, T), mp.conj(th(a, b, u, T)); diff = min(diff, abs(x - y) / max(abs(x), abs(y)))
    print("E5: on the mirror's fixed slice with b = 0: |N - K| <= %s; at 20 generic points the two differ by at least %s (relative)" % (mp.nstr(same, 3), mp.nstr(diff, 3)))
    worst = 0
    for _ in range(12):
        x, y = (rnd(), rnd()), (rnd(), rnd()); u = mp.mpc(rnd() * 0.3, rnd() * 0.2); t = mp.mpc(rnd() * 0.4, 0.8 + mp.rand())
        P = W.B.bil_mp((-x[0], -x[1]), (-y[0], -y[1]), u, t); Q = W.B.bil_mp(x, y, -u, t)
        worst = max(worst, max(abs(P[i][j] + Q[i][j]) / max(abs(Q[i][j]), mp.mpf(10) ** -30) for i in range(2) for j in range(2)))
    print("E6: main's bilinear: |bil(-x, -y, u, t) + bil(x, y, -u, t)| relative, 12 random points: %s" % mp.nstr(worst, 3))
