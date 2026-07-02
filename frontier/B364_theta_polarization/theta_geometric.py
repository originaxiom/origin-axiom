"""L57 decisive computation: is the theta lift THE geometric lift -- the transformation action
on level-15 theta functions of the fiber torus?

The family: f_j(z, tau) = sum_{n = j mod 15} q^{E(n)} e(n z),  E(n) = n(n-1)/30,  q = e(tau).
  T-side (analytic, verified numerically here): E(n+15)-E(n) = n+7 in Z  =>  T-stable with
     f_j(z, tau+1) = e(E(j)) f_j(z, tau) = zeta_15^{j(j-1)/2} f_j -- EXACTLY the theta lift's D.
  S-side (this computation): f_j(z/tau, -1/tau) = C(tau) * e(c z^2/tau) * sum_k S_geo[j,k] f_k(z,tau)
     -- fit c from candidates, solve S_geo by least squares over a z-grid, and compare S_geo
     (up to one global phase) with the theta-lift representation of S^-1 = R L^-1 R, i.e.
     M_lift = W_R W_L^-1 W_R  (theta generators W_L = D, W_R = F D^-1 F^-1).
If S matches: the geometric (theta-bundle) lift IS the theta lift; geometry hands ONE lift map to
the whole mapping class group, so both slots of any pair observable are forced into the theta
class SIMULTANEOUSLY -- the L57 forcing shape.
"""
import cmath
import numpy as np

N = 15


def e(x):
    return cmath.exp(2j * cmath.pi * x)


def f_theta(j, z, tau, K=40):
    s = 0
    for m in range(-K, K + 1):
        n = 15 * m + j
        s += e((n * (n - 1) / 30) * tau + n * z)     # combined exponent: the Gaussian dominates
    return s


def T_side_check(tau=0.31 + 1.13j, zs=(0.17 + 0.05j, -0.23 + 0.11j)):
    worst = 0
    for j in range(N):
        mult = e(j * (j - 1) / 30)
        for z in zs:
            lhs = f_theta(j, z, tau + 1)
            rhs = mult * f_theta(j, z, tau)
            worst = max(worst, abs(lhs - rhs) / max(abs(rhs), 1e-30))
    return worst


def S_side_matrix(tau=0.31 + 1.13j, nz=40, seed=5):
    """Fit f_j(z/tau, -1/tau) = C e(c z^2 / tau) sum_k S[j,k] f_k(z,tau) over candidate c."""
    rng = np.random.default_rng(seed)
    zs = [complex(0.35 * rng.standard_normal() + 0.05, 0.30 * rng.standard_normal()) for _ in range(nz)]
    F = np.array([[f_theta(k, z, tau) for k in range(N)] for z in zs])          # nz x N
    best = None
    for c in (15 / 2, 15, 15 / 4, 30, 7.5 / 2):
        L = np.array([[f_theta(j, z / tau, -1 / tau) / e(c * z * z / tau) for j in range(N)] for z in zs])
        # solve L[:, j] = F @ S[j, :]^T  for each j; residual
        S = np.zeros((N, N), complex)
        resid = 0
        for j in range(N):
            sol, res, _, _ = np.linalg.lstsq(F, L[:, j], rcond=None)
            S[j] = sol
            resid += (np.linalg.norm(F @ sol - L[:, j]) / np.linalg.norm(L[:, j])) ** 2
        resid = resid ** 0.5
        if best is None or resid < best[1]:
            best = (c, resid, S)
    return best


def theta_lift_Sinv():
    z15 = e(1 / 15)
    D = np.diag([z15 ** ((j * (j - 1) // 2) % 15) for j in range(N)])
    F = np.array([[z15 ** (i * j) for j in range(N)] for i in range(N)]) / (15 ** 0.5)
    Fi = np.array([[z15 ** ((-i * j) % 15) for j in range(N)] for i in range(N)]) / (15 ** 0.5)
    WR = F @ np.linalg.inv(D) @ Fi
    WL = D
    return WR @ np.linalg.inv(WL) @ WR          # rep of S^-1 = R L^-1 R


def compare(S_geo, M_lift):
    """S_geo should equal (global phase) * M_lift possibly up to the direction convention
    (S vs S^-1, transpose). Try the 4 variants; return the best (variant, phase, deviation)."""
    outs = []
    for name, M in (("M", M_lift), ("M^-1", np.linalg.inv(M_lift)),
                    ("M^T", M_lift.T), ("M^-T", np.linalg.inv(M_lift).T)):
        # fit global phase: phase = argmax entry ratio
        idx = np.unravel_index(np.argmax(np.abs(M)), M.shape)
        if abs(S_geo[idx]) < 1e-12:
            continue
        ph = S_geo[idx] / M[idx]
        dev = np.max(np.abs(S_geo - ph * M)) / np.max(np.abs(S_geo))
        outs.append((name, ph, dev))
    return min(outs, key=lambda t: t[2])


def main():
    tw = T_side_check()
    print(f"T-side: worst relative deviation of f_j(tau+1) vs zeta15^(j(j-1)/2) f_j: {tw:.3e}")
    c, resid, S_geo = S_side_matrix()
    print(f"S-side fit: best c = {c}, lstsq residual = {resid:.3e}")
    M = theta_lift_Sinv()
    name, ph, dev = compare(S_geo, M)
    print(f"compare with theta-lift rep: best variant {name}, |phase| = {abs(ph):.6f}, "
          f"phase arg/2pi = {cmath.phase(ph)/(2*cmath.pi):.6f}, max relative deviation = {dev:.3e}")
    print("VERDICT:", "GEOMETRIC LIFT = THETA LIFT (up to one global phase)" if dev < 1e-6
          else "MISMATCH -- the geometric lift is NOT the theta lift as constructed")


if __name__ == "__main__":
    main()
