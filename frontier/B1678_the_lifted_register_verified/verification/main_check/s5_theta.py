import mpmath as mp
mp.mp.dps = 30


def analytic_jtheta(k, z, tau, terms=32):
    """Holomorphic Jacobi theta_k(pi*z | tau) on all Im(tau) > 0 via explicit
    quarter-nome w = exp(i*pi*tau/4), avoiding mpmath.jtheta(2, u, q)'s principal
    fourth-root branch cuts on Re(tau) in -1 + 2Z (P-670)."""
    if mp.im(tau) <= 0:
        raise ValueError("tau must lie in the upper half-plane Im(tau) > 0")
    u = mp.pi * z
    w = mp.exp(1j * mp.pi * tau / 4)
    q = w ** 4
    if k == 1:
        s = mp.mpc(0)
        for n in range(terms):
            s += ((-1) ** n) * (w ** ((2 * n + 1) ** 2)) * mp.sin((2 * n + 1) * u)
        return 2 * s
    if k == 2:
        s = mp.mpc(0)
        for n in range(terms):
            s += (w ** ((2 * n + 1) ** 2)) * mp.cos((2 * n + 1) * u)
        return 2 * s
    if k == 3:
        s = mp.mpc(1)
        for n in range(1, terms + 1):
            s += 2 * (q ** (n * n)) * mp.cos(2 * n * u)
        return s
    if k == 4:
        s = mp.mpc(1)
        for n in range(1, terms + 1):
            s += 2 * ((-1) ** n) * (q ** (n * n)) * mp.cos(2 * n * u)
        return s
    raise ValueError(f"invalid Jacobi index k={k}")


def th(k, z, tau):
    return analytic_jtheta(k, z, tau)


def _naive_nome_th(k, z, tau):
    q = mp.exp(1j * mp.pi * tau)
    return mp.jtheta(k, mp.pi * z, q)


# Includes original points plus planted controls at Re(tau) = 0.6 (Re(2*tau) = 1.2 > 1)
# and Re(tau) = 1.3 (Re(2*tau) = 2.6 > 1) where naive mp.jtheta(2, u, q) flips sheet (P-670).
TAUS = [1j * 0.9, 0.3 + 1.1j, -0.5 + mp.sqrt(3) / 2 * 1j, 0.17 + 0.6j, 0.6 + 1.1j, 1.3 + 1.1j]
for tau in TAUS:
    # numerator vector N(z)=(i th2(z|2tau), th3(z|2tau))
    N = lambda z: mp.matrix([1j * th(2, z, 2 * tau), th(3, z, 2 * tau)])
    v = N(0); d = mp.diff(lambda z: th(1, z, tau), 0)
    b = v / mp.sqrt(d)
    # (1) F = z^-1/2 b + O(z^3/2): check F z^{1/2} - b ~ z^2
    errs = []
    for z in [mp.mpf('0.02'), mp.mpf('0.01')]:
        F = N(z) / mp.sqrt(th(1, z, tau))
        errs.append(mp.norm(F * mp.sqrt(z) - b))
    ratio = errs[0] / errs[1]  # expect 4 for O(z^2)
    # (2) F(z+tau) constant-matrix relation: N(z+tau) = c(z)*T*N(z), T=[[0,i],[-i,0]]
    T = mp.matrix([[0, 1j], [-1j, 0]])
    z0 = mp.mpc('0.23', '0.11')
    A = N(z0 + tau); B = T * N(z0)
    c1 = A[0] / B[0]; c2 = A[1] / B[1]
    z1 = mp.mpc('-0.31', '0.07'); A1 = N(z1 + tau); B1 = T * N(z1)
    r_z0 = c1 / c2
    r_z1 = (A1[0] / B1[0]) / (A1[1] / B1[1])
    assert abs(r_z0 - 1) < mp.mpf('1e-12') and abs(r_z1 - 1) < mp.mpf('1e-12'), (tau, r_z0, r_z1)
    print("tau", mp.nstr(tau, 5), "|b|", mp.nstr(mp.norm(b), 6), "O(z^2) ratio", mp.nstr(ratio, 6),
          " c1/c2 at z0", mp.nstr(r_z0, 8), " at z1", mp.nstr(r_z1, 8))
    # N(z+1)
    Ap = N(z0 + 1)
    per_err = mp.norm(Ap - mp.matrix([[-1, 0], [0, 1]]) * N(z0))
    assert per_err < mp.mpf('1e-12'), (tau, per_err)
    print("   N(z+1) = diag(-1,1)N? err", mp.nstr(per_err, 5))

# Planted P-670 branch-cut control: naive nome jtheta fails N(z+tau) = c(z)*T*N(z) at Re(2*tau) > 1
for tau_ctrl in (0.6 + 1.1j, 1.3 + 1.1j):
    N_bad = lambda z: mp.matrix([1j * _naive_nome_th(2, z, 2 * tau_ctrl), _naive_nome_th(3, z, 2 * tau_ctrl)])
    z0 = mp.mpc('0.23', '0.11')
    T = mp.matrix([[0, 1j], [-1j, 0]])
    A_bad = N_bad(z0 + tau_ctrl); B_bad = T * N_bad(z0)
    bad_ratio = (A_bad[0] / B_bad[0]) / (A_bad[1] / B_bad[1])
    assert abs(bad_ratio - (-1)) < mp.mpf('1e-12') and abs(bad_ratio - 1) > 1.5, (tau_ctrl, bad_ratio)
