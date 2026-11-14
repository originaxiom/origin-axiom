"""K1. Frame C's channel kernel P_s/R_s is Kronecker's theta function at z_s = (q_L+q_R) w - h_s (the Higgs field's own
hypercharge line, shifted by the channel's half period = spin structure), and R_s = kappa_s Z(c_s) Z(d_s)/(2 pi eta),
Z(c) = vt(c;0)/eta.  Checked against main's bilinear (b1656_funcs, unchanged) at 30 digits on frame C's 24 lines of
order 5, three sectors, four channels, three tau.  Also: multipliers of K_s, sum_s R_s^2 = 0 (Riemann), and the
up sector's R_1 = 0 on every order-5 line ((q_L - q_R) = 5).  Pure mathematics; no data."""
import sys, pathlib
ROOT = next(q for q in pathlib.Path(__file__).resolve().parents if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file())
sys.path.insert(0, str(ROOT / "frontier" / "B1723_the_golden_valley" / "verification"))
_a = sys.argv; sys.argv = ["x"]; import b1656_funcs as B; sys.argv = _a
import mpmath as mp
mp.mp.dps = 20
I = mp.mpc(0, 1); H = mp.mpf(1) / 2
vt = lambda a, b, u, t: B.thc_mp(a, b, u, t)
th1 = lambda u, t: B.th_mp(1, u, t)
def th1p(t): return mp.diff(lambda z: th1(z, t), 0)
def eta(t): return mp.exp(I*mp.pi*t/12)*mp.nprod(lambda n: 1 - mp.exp(2*I*mp.pi*n*t), [1, mp.inf])
HS = {"1": (0, 0), "i": (0, H), "j": (H, 0), "k": (H, H)}          # h_s = A tau + B  as (A, B)
TAUS = [mp.mpc("0.13", "1.07"), mp.mpc("-0.31", "1.45"), mp.mpc("0.5", "0.8660254037844386467637")]
LINES = [(mp.mpf(i)/5, mp.mpf(j)/5) for i in range(5) for j in range(5) if (i, j) != (0, 0)]
US = (mp.mpc("0.211", "0.137"), mp.mpc("-0.37", "0.29"))
worst = {"kernel_vs_bilinear": 0, "kronecker_form": 0, "mult_1": 0, "mult_tau": 0, "R_as_Z": 0, "sumR2_rel": 0,
         "z_vs_Qw_minus_h": 0, "up_R1_rel": 0}
minR = mp.inf
for t in TAUS:
    T1P = th1p(t); ET = eta(t)
    for p1, p2 in LINES:
        w = p1*t - p2
        for sec, (lf, rf) in B.SECTORS.items():
            qL, qR = B.SIXY[lf], B.SIXY[rf]; Q = qL + qR
            x = (qL*p1, -2*qL*p2); y = (qR*p1, -2*qR*p2)               # = twist_of(q w), exact rationals in mp
            ap, am = x[0] + y[0], x[0] - y[0]; bp, bm = (x[1] + y[1])/2, (x[1] - y[1])/2
            e = mp.exp(-2*I*mp.pi*x[0])
            kap = {"1": -I*e, "i": mp.mpf(-1), "j": -e, "k": I}
            cs = {"1": (ap+H, bp+H), "i": (ap+H, bp), "j": (ap, bp+H), "k": (ap, bp)}
            ds = {"1": (am+H, bm+H), "i": (am+H, bm), "j": (am, bm+H), "k": (am, bm)}
            # residues from main's bilinear by contour mean (B1656's definition), 30 digits
            # residues: B1906's closed form (proved there at 30 digits against the contour); here also against
            # main's numpy contour residues (route A), at double precision
            Rm = {s: kap[s]*vt(*cs[s], 0, t)*vt(*ds[s], 0, t)/T1P for s in B.UNITS}
            Rn = B.residues((float(x[0]), float(x[1])), (float(y[0]), float(y[1])), complex(t))
            nRn = sum(abs(Rn[s])**2 for s in B.UNITS)**0.5
            worst["R_vs_numpy_contour"] = max(worst.get("R_vs_numpy_contour", 0), max(abs(complex(Rm[s]) - Rn[s]) for s in B.UNITS)/nRn)
            PU = [{s2: B.pair_mp(Mu, s2) for s2 in B.UNITS} for Mu in [B.bil_mp(x, y, u, t) for u in US]]
            sR2 = mp.fsum(Rm[s]**2 for s in B.UNITS); nR = mp.fsum(abs(Rm[s])**2 for s in B.UNITS)
            worst["sumR2_rel"] = max(worst["sumR2_rel"], abs(sR2)/nR)
            if sec == "up": worst["up_R1_rel"] = max(worst["up_R1_rel"], abs(Rm["1"])/mp.sqrt(nR))
            for s in B.UNITS:
                Rf = kap[s]*vt(*cs[s], 0, t)*vt(*ds[s], 0, t)/T1P
                Rz = kap[s]*(vt(*cs[s], 0, t)/ET)*(vt(*ds[s], 0, t)/ET)/(2*mp.pi*ET)
                if abs(Rm[s]) < mp.mpf(10)**-12 * mp.sqrt(nR):
                    continue                                    # a zero of the zero law: no kernel
                minR = min(minR, abs(Rm[s])/mp.sqrt(nR))
                worst["R_as_Z"] = max(worst["R_as_Z"], abs(Rz/Rm[s] - 1), abs(Rf/Rm[s] - 1))
                al, be = cs[s][0] - H, cs[s][1] - H; z = al*t + be
                # z_s against Q w - h_s, modulo the lattice
                A, Bh = HS[s]; dz = z - (Q*w - (A*t + Bh)); k2 = mp.im(dz)/mp.im(t); k1 = mp.re(dz) - k2*mp.re(t)
                worst["z_vs_Qw_minus_h"] = max(worst["z_vs_Qw_minus_h"], abs(k1 - mp.nint(k1)) + abs(k2 - mp.nint(k2)))
                Kf = lambda u: T1P*vt(*cs[s], u, t)/(vt(*cs[s], 0, t)*th1(u, t))
                Kk = lambda u: mp.exp(2*I*mp.pi*al*u)*T1P*th1(u + z, t)/(th1(u, t)*th1(z, t))
                for iu, u in enumerate(US):
                    Pu = PU[iu][s]
                    worst["kernel_vs_bilinear"] = max(worst["kernel_vs_bilinear"], abs(Pu/(Rm[s]*Kf(u)) - 1))
                    worst["kronecker_form"] = max(worst["kronecker_form"], abs(Kk(u)/Kf(u) - 1))
                    worst["mult_1"] = max(worst["mult_1"], abs(Kf(u + 1)/Kf(u) - mp.exp(2*I*mp.pi*al)))
                    worst["mult_tau"] = max(worst["mult_tau"], abs(Kf(u + t)/Kf(u) - mp.exp(-2*I*mp.pi*be)))
for k, v in worst.items(): print("%-22s %s" % (k, mp.nstr(v, 3)))
print("smallest live |R_s|/|R| %s" % mp.nstr(minR, 3))
# a planted fault: the kernel at the relative line (q_L - q_R) w instead of the Higgs line must fail
t = TAUS[0]; p1, p2 = LINES[6]; qL, qR = 1, 2
x = (qL*p1, -2*qL*p2); y = (qR*p1, -2*qR*p2); am, bm = x[0]-y[0], (x[1]-y[1])/2
z_bad = (am)*t + bm; u = mp.mpc("0.211", "0.137"); T1P = th1p(t)
ap, bp = x[0]+y[0], (x[1]+y[1])/2
Kg = T1P*vt(ap, bp, u, t)/(vt(ap, bp, 0, t)*th1(u, t))
Kb = mp.exp(2*I*mp.pi*(am-H)*u)*T1P*th1(u + z_bad - (t+1)/2, t)/(th1(u, t)*th1(z_bad - (t+1)/2, t))
print("PLANT (relative line used as the kernel's line): rel. diff %s (must be O(1))" % mp.nstr(abs(Kb/Kg - 1), 3))
