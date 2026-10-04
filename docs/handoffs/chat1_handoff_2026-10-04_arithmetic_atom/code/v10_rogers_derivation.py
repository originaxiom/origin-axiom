"""The arithmetic atom: R(e^{i pi/3}) = -pi^2/12 + i Cl_2(pi/3).
Re -> CS lattice (1/24)Z.   Im -> vol(regular ideal tetrahedron) = 6 x Bianchi covolume -> L(2,chi_-3)."""
import mpmath as mp
mp.mp.dps=30
z=mp.expjpi(mp.mpf(1)/3); R=mp.polylog(2,z)+mp.log(z)*mp.log(1-z)/2-mp.pi**2/6
L2=(mp.zeta(2,mp.mpf(1)/3)-mp.zeta(2,mp.mpf(2)/3))/9; cov=mp.sqrt(3)*L2/8
print(f"Re R = {mp.nstr(mp.re(R),20)}   -pi^2/12 = {mp.nstr(-mp.pi**2/12,20)}")
print(f"Im R = {mp.nstr(mp.im(R),20)}   6 x covolume = {mp.nstr(6*cov,20)}")
print("=> CS_raw in (pi^2/12)Z ; SnapPy CS = CS_raw/(2pi^2) in (1/24)Z.  24 = 2 x 12, NOT |2T|.")
