"""B1974: main'''s own check of the agy lane's C13 (2026-11-24; data-free; main's frame code, no seat code).
 H1  the Halphen-Serre identity: 24 eta^3 (c0, c1, -i c2) = (-th2^2 (th3^4 + th4^4), th4^2 (th2^4 + th3^4), th3^2 (th2^4 - th4^4)),
     c_k = frame C's Higgs coefficients (te.ev of B[1], B1940's frame).
 H2  whether eta * c_k lies in M_2(Gamma(2)) = span(th2^4, th4^4) (q = e^{i pi tau}), by a least-squares fit at many tau.
 H3  the transformation of the triplet under T: tau -> tau+1 and S: tau -> -1/tau, solved as 3x3 matrices at several tau
     (constant if the triplet is a vector-valued form), with the weight 3/2 automorphy factor."""
import sys, pathlib
ROOT = next((q for q in [*pathlib.Path(__file__).resolve().parents, pathlib.Path.cwd()] if (q / "frontier").is_dir() and (q / "GENESIS.md").is_file()))
sys.path.insert(0, str(next((ROOT / "frontier").glob("B1945_*")) / "verification"))
import determinant_law as DL
mp = DL.mp; te = DL.FM.te
mp.mp.dps = 40
def c3(t): return [te.ev(cc, t) for cc in te.B[1]]
def th(k, t): return mp.jtheta(k, 0, mp.exp(1j * mp.pi * t))
def eta(t): return mp.exp(1j * mp.pi * t / 12) * mp.qp(mp.exp(2j * mp.pi * t))
taus = [mp.mpc(x, y) for x, y in ((0.13, 1.1), (-0.31, 0.9), (0.4, 1.7), (0.05, 2.3), (-0.45, 1.3))]
worst = 0
for t in taus:
    c = c3(t); e3 = 24 * eta(t) ** 3
    lhs = [e3 * c[0], e3 * c[1], -1j * e3 * c[2]]
    t2, t3, t4 = th(2, t), th(3, t), th(4, t)
    rhs = [-t2 ** 2 * (t3 ** 4 + t4 ** 4), t4 ** 2 * (t2 ** 4 + t3 ** 4), t3 ** 2 * (t2 ** 4 - t4 ** 4)]
    worst = max(worst, max(abs(a - b) / abs(b) for a, b in zip(lhs, rhs)))
print("H1: the Halphen-Serre identity, worst relative residual over %d tau: %s" % (len(taus), mp.nstr(worst, 3)))
# H2: is eta * c_k in span(th2^4, th4^4)?
many = [mp.mpc(x, y) for x in (-0.4, -0.1, 0.2, 0.35) for y in (0.8, 1.2, 1.9)]
for k in range(3):
    A = mp.matrix([[th(2, t) ** 4, th(4, t) ** 4] for t in many]); b = mp.matrix([eta(t) * c3(t)[k] for t in many])
    x = mp.lu_solve(A.H * A, A.H * b); r = mp.norm(A * x - b) / mp.norm(b)
    print("H2: eta * c_%d = %s th2^4 + %s th4^4 ; relative residual %s" % (k, mp.nstr(x[0], 8), mp.nstr(x[1], 8), mp.nstr(r, 3)))
# H3: transformation matrices
def solve_rho(gamma, factor):
    rows = []
    for t in many[:6]:
        g = gamma(t); rows.append((c3(g), [factor(t) * z for z in c3(t)]))
    # c(g t) = factor(t) * R c(t): solve R row by row from 6 equations
    R = mp.zeros(3, 3); res = 0
    for i in range(3):
        A = mp.matrix([[r[1][j] for j in range(3)] for r in rows]); b = mp.matrix([r[0][i] for r in rows])
        x = mp.lu_solve(A.H * A, A.H * b); res = max(res, mp.norm(A * x - b) / mp.norm(b))
        for j in range(3): R[i, j] = x[j]
    return R, res
RT, rT = solve_rho(lambda t: t + 1, lambda t: 1)
RS, rS = solve_rho(lambda t: -1 / t, lambda t: (t) ** mp.mpf(1.5) * mp.exp(-1j * mp.pi * 3 / 4))
print("H3: c(tau+1) = R_T c(tau): residual %s; R_T =" % mp.nstr(rT, 3), [[mp.nstr(RT[i, j], 6) for j in range(3)] for i in range(3)])
print("H3: c(-1/tau) = (tau^(3/2) e^(-3 pi i/4)) R_S c(tau): residual %s; R_S =" % mp.nstr(rS, 3), [[mp.nstr(RS[i, j], 6) for j in range(3)] for i in range(3)])
