"""C1 pre-design check (main, unsealed exploration): the Szegő-kernel 'tame Higgs' S_r in the two typings.
(0,1) typing: phi = dbar S_r is pi*delta_0 (a point current AT the puncture); the contour coupling is Res_0(S_r v_r).
Claim: S_r v_r = R_r S_r^2 = R_r (wp - e_r) has zero residue, so the coupling vanishes identically.
Density typing: int v_r conj(S_r) d^2z over |z|>eps grows like 2 pi R_r log(1/eps) (log divergence)."""
import mpmath as mp
mp.mp.dps = 30
tau = mp.mpc(0.13, 1.07); q = mp.exp(1j*mp.pi*tau)
th = lambda r, z: mp.jtheta(r, mp.pi*z, q)
th1p = mp.jtheta(1, 0, q, 1)*mp.pi
def S(r, z): return th(r, z)*th1p/(th(r, 0)*th(1, z))
# residue of S_r^2 at 0 via a small contour
for r in (2, 3, 4):
    eps = mp.mpf('0.05')
    res = mp.quad(lambda t: S(r, eps*mp.exp(1j*t))**2*1j*eps*mp.exp(1j*t), [0, 2*mp.pi])/(2j*mp.pi)
    # finite part of S_r at 0: S_r(z) - 1/z at small z (odd => -> 0)
    fp = S(r, mp.mpf('1e-8')) - 1/mp.mpf('1e-8')
    print(f"r={r}: Res0 S_r^2 = {mp.nstr(abs(res),3)} ; S_r(z)-1/z at z=1e-8: {mp.nstr(abs(fp),3)}")
# density typing: annulus integral of S_r conj(S_r) between eps and a fixed outer radius: log growth
for r in (3,):
    def ann(eps, Rout=mp.mpf('0.3')):
        f = lambda rho, t: abs(S(r, rho*mp.exp(1j*t)))**2*rho
        return mp.quad(f, [eps, Rout], [0, 2*mp.pi])
    a1, a2 = ann(mp.mpf('1e-2')), ann(mp.mpf('1e-4'))
    print(f"density |S_3|^2 annulus: eps=1e-2 -> {mp.nstr(a1,6)}, eps=1e-4 -> {mp.nstr(a2,6)}, diff {mp.nstr(a2-a1,6)} vs 2*pi*ln(100) = {mp.nstr(2*mp.pi*mp.log(100),6)}")
