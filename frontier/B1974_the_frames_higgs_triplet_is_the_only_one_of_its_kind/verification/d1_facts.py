"""B1974: facts the D-1 uniqueness proof uses, checked numerically on main's frame code (2026-11-24).
 F1  c_0 = -th2^2 (th3^4 + th4^4) / (24 eta^3) (the identity's first component) and E = th3^4 + th4^4 vanishes at (1+i)/2.
 F2  the cusp orders: |c_0| ~ |q|^(1/8), |c_1|, |c_2| ~ |q|^(-1/8) (q = e^{2 pi i tau}), from heights 20 and 30.
 F3  (read from c13_check.py's R_T and R_S: T and S T^2 S fix component 0, so its stabilizer is Gamma_0(2)).
 F4  zeros of c_0 in a fundamental domain of Gamma_0(2): the argument principle around a box, against the elliptic point."""
import sys, pathlib
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp; te = DL.FM.te
mp.mp.dps = 30
def c3(t): return [te.ev(cc, t) for cc in te.B[1]]
def th(k, t): return mp.jtheta(k, 0, mp.exp(1j * mp.pi * t))
E = lambda t: th(3, t) ** 4 + th(4, t) ** 4
print("F1: |E((1+i)/2)| =", mp.nstr(abs(E(mp.mpc(0.5, 0.5))), 3), "| |E(i)| =", mp.nstr(abs(E(mp.mpc(0, 1))), 6))
for y1, y2 in ((20, 30),):
    mp.mp.dps = 40 + 2 * y2
    a, b = c3(mp.mpc(0.13, y1)), c3(mp.mpc(0.13, y2))
    rates = [float(-(mp.log(abs(b[k])) - mp.log(abs(a[k]))) / (2 * mp.pi * (y2 - y1))) for k in range(3)]
    print("F2: |q|-orders of c_0, c_1, c_2 between heights 20 and 30:", [round(r, 6) for r in rates])
mp.mp.dps = 30
# F4: argument principle for c_0 on a contour around the elliptic point and a larger box in Gamma_0(2)'s domain
def winding(f, pts, n=2000):
    tot = mp.mpf(0); prev = f(pts[0]); m = len(pts)
    for i in range(m):
        z0, z1 = pts[i], pts[(i + 1) % m]
        for k in range(1, n // m + 1):
            z = z0 + (z1 - z0) * k / (n // m); cur = f(z); tot += mp.im(mp.log(cur / prev)); prev = cur
    return tot / (2 * mp.pi)
f0 = lambda t: c3(t)[0]
small = [mp.mpc(0.5 + 0.1 * mp.cos(2 * mp.pi * k / 16), 0.5 + 0.1 * mp.sin(2 * mp.pi * k / 16)) for k in range(16)]
print("F4: zeros of c_0 inside a circle of radius 0.1 about (1+i)/2:", mp.nstr(winding(f0, small, 1600), 6))
box = [mp.mpc(-0.49, 0.62), mp.mpc(0.49, 0.62), mp.mpc(0.49, 2.5), mp.mpc(-0.49, 2.5)]
print("F4: zeros of c_0 in the box -0.49 < Re < 0.49, 0.62 < Im < 2.5:", mp.nstr(winding(f0, box, 3200), 6))
