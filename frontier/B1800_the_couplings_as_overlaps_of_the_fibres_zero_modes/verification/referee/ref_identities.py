"""Referee B1800: the theta-constant identities behind the off-diagonal overlaps, at 40 digits (mpmath, own series in tau;
no nome branch).
  (i)   theta[1/4,0](0,2t)   = theta2(t/2)/2                       (the arc's claim)
  (ii)  theta[1/4,1/2](0,2t) = (1/2) e^{i pi/8} theta2((t+1)/2)     (referee: a closed form the arc does not state)
  (iii) the squares: c32^2 = theta2 theta3 / 2, c34^2 = theta3 theta4, c24^2 = (i/2) theta2 theta4  (referee)
        with c32 = theta[1/4,0](0,2t), c34 = theta4(2t), c24 = theta[1/4,1/2](0,2t)
  so |c_pq|^2 = kappa |theta_p theta_q| = kappa' |eta|^3/|theta_r|  (Jacobi theta2 theta3 theta4 = 2 eta^3)
    python3 -B ref_identities.py"""
import mpmath as mp
mp.mp.dps = 40

def th(a, b, T, N=60):
    s = mp.mpc(0)
    for n in range(-N, N + 1):
        x = n + a
        s += mp.exp(1j*mp.pi*x*x*T + 2j*mp.pi*x*b)
    return s

def eta(T, N=60):
    q = mp.exp(2j*mp.pi*T); p = mp.mpc(1)
    for n in range(1, 400): p *= (1 - q**n)
    return mp.exp(2j*mp.pi*T/24)*p

worst = {k: mp.mpf(0) for k in ("i", "ii", "c32", "c34", "c24", "jacobi")}
taus = [mp.mpc(0.37, 1.2), mp.mpc(-0.21, 0.83), mp.mpc(0.05, 1.7), mp.mpc(0.49, 0.6), mp.mpc(-0.4, 2.3), mp.mpc(0.0, 1.0)]
for t in taus:
    t2, t3, t4 = th(0.5, 0, t), th(0, 0, t), th(0, 0.5, t)
    c32, c34, c24 = th(0.25, 0, 2*t), th(0, 0.5, 2*t), th(0.25, 0.5, 2*t)
    th2half = th(0.5, 0, t/2); th2shift = th(0.5, 0, (t + 1)/2)
    worst["i"] = max(worst["i"], abs(c32 - th2half/2))
    worst["ii"] = max(worst["ii"], abs(c24 - 0.5*mp.exp(1j*mp.pi/8)*th2shift))
    worst["c32"] = max(worst["c32"], abs(c32**2 - t2*t3/2))
    worst["c34"] = max(worst["c34"], abs(c34**2 - t3*t4))
    worst["c24"] = max(worst["c24"], abs(c24**2 - 0.5j*t2*t4))
    worst["jacobi"] = max(worst["jacobi"], abs(t2*t3*t4 - 2*eta(t)**3))
for k, v in worst.items(): print("%-7s worst |diff| over %d tau: %s" % (k, len(taus), mp.nstr(v, 3)))
print("ref_identities exit 0")
