"""B365 (W2.1) -- the S-side identification: which polarization is modular-closed at level 15?

Poisson prediction: the TRIANGULAR family (E = n(n-1)/30, the half-characteristic lattice) is
S-closed on its own 15-dim span (dual reindexing lands back on E_tri with argument shift tau/30);
the SQUARE family (E = n^2/15) is NOT (its dual carries k^2 tau/60 -- 30 characteristics).

Test: for each family, compute g_j(z) = f_j(z/tau, -1/tau) on a z-grid, strip the derived
j-dependent Gaussian prefactor, and least-squares-project onto span{f_k(z + gamma, tau)}.
Closure <=> residual at numerical precision. The closed family = the geometric polarization.
"""
import cmath
import numpy as np

N = 15


def e(x):
    return cmath.exp(2j * cmath.pi * x)


def fam(j, z, tau, E, K=60):
    s = 0
    for m in range(-K, K + 1):
        n = 15 * m + j
        s += e(E(n) * tau + n * z)
    return s


E_tri = lambda n: n * (n - 1) / 30
E_sq = lambda n: n * n / 15

TAU = 0.31 + 1.13j


def closure_residual(E, pref_exponent, gammas, nz=45, seed=9):
    """pref_exponent(j, z) = the exponent (in e(.) units) of the derived Gaussian prefactor to strip.
    Returns (best_gamma, residual, S_matrix)."""
    rng = np.random.default_rng(seed)
    zs = [complex(0.30 * rng.standard_normal() + 0.03, 0.25 * rng.standard_normal()) for _ in range(nz)]
    best = None
    for gamma in gammas:
        F = np.array([[fam(k, z + gamma, TAU, E) for k in range(N)] for z in zs])
        resid_tot = 0
        S = np.zeros((N, N), complex)
        for j in range(N):
            L = np.array([fam(j, z / TAU, -1 / TAU, E) / e(pref_exponent(j, z)) for z in zs])
            sol, _, _, _ = np.linalg.lstsq(F, L, rcond=None)
            S[j] = sol
            resid_tot += (np.linalg.norm(F @ sol - L) / np.linalg.norm(L)) ** 2
        resid = (resid_tot / N) ** 0.5
        if best is None or resid < best[1]:
            best = (gamma, resid, S)
    return best


def main():
    # triangular: prefactor from Poisson: e((15z - (2j-1)/2)^2 / (30 tau)); shift gamma = tau/30 (derived)
    pref_tri = lambda j, z: ((15 * z - (2 * j - 1) / 2) ** 2) / (30 * TAU)
    g_tri = [TAU / 30, 0, -TAU / 30, TAU / 30 + 0.5, TAU / 30 - 0.5]
    gam, res, S = closure_residual(E_tri, pref_tri, g_tri)
    print(f"TRIANGULAR family: best gamma = {gam}, closure residual = {res:.3e}")
    tri_res = res

    # square: prefactor e((15z - 2j)^2 / (60 tau)); try the analogous shifts
    pref_sq = lambda j, z: ((15 * z - 2 * j) ** 2) / (60 * TAU)
    g_sq = [TAU / 60, 0, -TAU / 60, TAU / 30, TAU / 60 + 0.5, 0.5]
    gam2, res2, S2 = closure_residual(E_sq, pref_sq, g_sq)
    print(f"SQUARE family:     best gamma = {gam2}, closure residual = {res2:.3e}")

    print()
    if tri_res < 1e-8 and res2 > 1e-3:
        print("VERDICT: the TRIANGULAR (half-characteristic / theta-lift) polarization is the")
        print("modular-closed one at level 15; the square family does NOT close on its own span.")
    elif tri_res < 1e-8 and res2 < 1e-8:
        print("VERDICT: both close -- the discriminator fails; deeper test needed.")
    else:
        print("VERDICT: unexpected pattern -- inspect.")

    # W2.2 anchor: half-period vanishing signature (the odd spin structure's fingerprint)
    print()
    print("half-period values (|f_j| minima over j) -- the odd-vanishing signature:")
    for name, E in (("triangular", E_tri), ("square", E_sq)):
        for zname, z0 in (("z=0", 0), ("z=1/2", 0.5), ("z=tau/2", TAU / 2), ("z=(1+tau)/2", (1 + TAU) / 2)):
            vals = [abs(fam(j, z0, TAU, E)) for j in range(N)]
            jmin = int(np.argmin(vals))
            print(f"  {name:10s} {zname:12s}: min |f_j| = {vals[jmin]:.3e} at j={jmin}"
                  f"   (max = {max(vals):.3e})")


if __name__ == "__main__":
    main()
