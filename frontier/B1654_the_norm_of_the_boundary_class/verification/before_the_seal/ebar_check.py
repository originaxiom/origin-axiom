"""C1 pre-seal check (main): near the puncture, sum_r R_r^2 |S_r|^2 = (R.R)/|z|^2 - (1/2)(sum R_r^2 e_r) z/zbar
- (1/2)(sum R_r^2 ebar_r) zbar/z + O(|z|^2). Which O(1) coefficient vanishes? (O6 kills the first; the second is real-e only.)"""
import mpmath as mp
mp.mp.dps = 30
for tau in [mp.mpc(0.13, 1.07), mp.mpc(0, 1), mp.mpc(0, 2.2), mp.exp(2j*mp.pi/3)]:
    q = mp.exp(1j*mp.pi*tau); tp = mp.jtheta(1, 0, q, 1)*mp.pi
    th = {r: mp.jtheta(r, 0, q) for r in (2, 3, 4)}
    R = {2: -th[2]**2/tp, 4: -th[4]**2/tp, 3: 1j*th[3]**2/tp}
    def S(r, z): return mp.jtheta(r, mp.pi*z, q)*tp/(th[r]*mp.jtheta(1, mp.pi*z, q))
    z = mp.mpf('1e-6'); e = {r: -(S(r, z)**2 - 1/z**2) for r in (2, 3, 4)}
    nR2 = sum(abs(R[r])**2 for r in R); ne = max(abs(e[r]) for r in e)
    A = sum(R[r]**2*e[r] for r in R); B = sum(R[r]**2*mp.conj(e[r]) for r in R)
    print(mp.nstr(tau, 4), " |sum R^2 e|/(|R|^2 |e|) =", mp.nstr(abs(A)/(nR2*ne), 3), "  |sum R^2 ebar|/(|R|^2 |e|) =", mp.nstr(abs(B)/(nR2*ne), 3))
