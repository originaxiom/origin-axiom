"""B1957: agy-002's gate 6, recomputed by main.  Data-free: every input is the seat's stated benchmark.
G6.1  the three symmetric tensors J_0, J_1, J_2 built from the triple overlap at zero Wilson line and the six Higgs modes
      at the origin: symmetry, covariance, ranks, span; what they leave free.
G6.2  the first column (2, -1, -1)/sqrt(6): put in by construction; how far |U_e1|^2 moves under the neutrino operator's
      running (Antusch et al., hep-ph/0108005, equation (21), read by main), for the seat's three histories.
G6.3  the Pati-Salam stage's two-loop gauge coefficients from the field content, and the 243 histories on main's own
      two-loop Standard Model running: the phase of the determinant, the gauge residual, sqrt(2 lambda) at the bottom."""
import sys, pathlib, math, itertools, functools
from fractions import Fraction as F
import numpy as np, mpmath as mp
from scipy.integrate import solve_ivp
print = functools.partial(print, flush=True)
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import cim_closed as CC, cim_overlap as C, sm_rge_matrix as R


def basis(tau):
    Yt = CC.Y(tau, 0j); v0 = C.psi(6, 0.0, 0.0, np.array([0j]), tau, 0.0)[:, 0]; G6 = np.einsum("ijk,ijl->kl", Yt.conj(), Yt)
    J0 = np.einsum("ijk,k->ij", Yt, v0); J1 = np.einsum("ijk,k->ij", Yt, G6 @ v0); return J0, J1, J1 @ J1.conj().T @ J1


if __name__ == "__main__":
    # G6.1
    tau = 0.23 + 1.41j; UT = C.transport(3, 0.5, 0.5, tau, 0.0, "T"); US = C.transport(3, 0.5, 0.5, tau, 0.0, "S")
    J = basis(tau); JT = basis(tau + 1); JS = basis(-1 / tau)
    sym = max(np.abs(m - m.T).max() for m in J); eT = max(np.abs(b - UT @ a @ UT.T).max() for a, b in zip(J, JT)); eS = max(np.abs(b - US @ a @ US.T).max() for a, b in zip(J, JS))
    rk = [int(np.linalg.matrix_rank(m, tol=1e-10)) for m in J]; span = int(np.linalg.matrix_rank(np.array([m.ravel() for m in J]), tol=1e-8))
    r = lambda M: (lambda s: s[1] / s[0])(np.linalg.svd(M, compute_uv=False))
    print("G6.1: the three tensors: symmetric to %.1e; J(tau + 1) and J(-1/tau) against U J U^T: %.1e, %.1e; ranks %s; they span %d dimensions of the six of symmetric matrices" % (sym, eT, eS, rk, span))
    print("      a change of the relative phase of the second coefficient from 1 to i moves s2/s1 of J0 + c J1 + J2/5 by %.4f (the seat: 0.0107): the coefficients are free, two complex ratios and a scale" % abs(r(J[0] + J[1] + J[2] / 5) - r(J[0] + 1j * J[1] + J[2] / 5)))
    print("      J_0 has rank one because the six modes at the origin reproduce the product of the two matter sections there: J_0 = psi(0) psi(0)^T to %.1e" % np.abs(J[0] - np.outer(C.psi(3, 0.5, 0.5, np.array([0j]), tau, 0.0)[:, 0], C.psi(3, 0.5, 0.5, np.array([0j]), tau, 0.0)[:, 0])).max())
    # G6.2
    u1 = np.array([2, -1, -1]) / 6 ** 0.5; u2 = np.ones(3) / 3 ** 0.5; u3 = np.array([0, 1, -1]) / 2 ** 0.5; ph = math.asin(0.25); cp = np.exp(0.7j)
    R23 = np.array([[1, 0, 0], [0, math.cos(ph), math.sin(ph) * cp], [0, -math.sin(ph) * cp.conjugate(), math.cos(ph)]]); U = np.column_stack([u1, u2, u3]) @ R23
    k0 = U @ np.diag([1 / 50, 1 / 10, 1 / 2]) @ U.T
    ue1 = lambda k: abs(np.linalg.eigh(k @ k.conj().T)[1][0, 0]) ** 2
    print("G6.2: the start: |U_e1|^2 - 2/3 = %.1e and |U_e3|^2 - 1/48 = %.1e: both by construction (the first column is typed in; the third is sin^2(asin(1/4))/3)" % (abs(ue1(k0) - 2 / 3), abs(abs(U[0, 2]) ** 2 - 1 / 48)))
    for yt, seat in ((1 / 100, 9.939198210462408e-06), (1 / 20, 0.0002483152180887682), (1 / 5, 0.003932049146647576)):
        He = np.diag([(yt / 200) ** 2, (yt / 16) ** 2, yt ** 2]).astype(complex)
        f = lambda t, v: (R.K * (-1.5) * (He @ v.view(complex).reshape(3, 3) + v.view(complex).reshape(3, 3) @ He.T)).ravel().view(float)
        k1 = solve_ivp(f, (0, -30.0), k0.astype(complex).ravel().view(float), method="DOP853", rtol=1e-13, atol=1e-16).y[:, -1].view(complex).reshape(3, 3)
        print("      y_tau = %-5g: after 30 e-folds down |U_e1|^2 has moved by %.6e (the seat: %.6e)" % (yt, abs(ue1(k1) - 2 / 3), seat))
    print("      the seat's flow keeps the charged leptons' matrix fixed and drops the flavour-blind term, which does not move the mixing")
    # G6.3: the Pati-Salam two-loop gauge coefficients from the content (Machacek and Vaughn's general formula; checked on the Standard Model's -26)
    C2G = {"4": F(4), "L": F(2), "R": F(2)}; C2f = {"4": F(15, 8), "L": F(3, 4), "R": F(3, 4)}
    ferm = 3 * [{"4": 1, "L": 1, "R": 0, "dim": {"4": 4, "L": 2, "R": 1}}, {"4": 1, "L": 0, "R": 1, "dim": {"4": 4, "L": 1, "R": 2}}]
    scal = [{"4": 0, "L": 1, "R": 1, "dim": {"4": 1, "L": 2, "R": 2}}, {"4": 1, "L": 1, "R": 0, "dim": {"4": 4, "L": 2, "R": 1}}, {"4": 1, "L": 0, "R": 1, "dim": {"4": 4, "L": 1, "R": 2}}]
    def S2(rep, i): return F(1, 2) * F(math.prod(rep["dim"].values()), rep["dim"][i]) if rep[i] else F(0)
    def Bij(i, j):
        if i == j: return -F(34, 3) * C2G[i] ** 2 + sum(F(1, 2) * (4 * C2f[i] + F(20, 3) * C2G[i]) * S2(f_, i) for f_ in ferm) + sum((4 * C2f[i] + F(2, 3) * C2G[i]) * S2(s_, i) for s_ in scal)
        return sum(F(1, 2) * 4 * C2f[j] * S2(f_, i) for f_ in ferm if f_[j]) + sum(4 * C2f[j] * S2(s_, i) for s_ in scal if s_[j])
    Bps = [[Bij(i, j) for j in "4LR"] for i in "4LR"]
    sm33 = -F(34, 3) * 9 + F(1, 2) * (4 * F(4, 3) + F(20, 3) * 3) * 6
    print("G6.3: the two-loop gauge coefficients of the Pati-Salam stage, from three generations, one complex bidoublet and scalars (4, 2, 1) + (4, 1, 2): %s (the seat: [[-117/2, 15/2, 15/2], [75/2, 50/3, 3], [75/2, 3, 50/3]]); the same formula gives the Standard Model's %s" % ([[str(x) for x in row] for row in Bps], sm33))
    bps = np.array([-10, -7 / 3, -7 / 3]); Bn = np.array([[float(x) for x in row] for row in Bps])
    def ps(gu, d):
        if d == 0: return np.array([gu, gu, gu])
        return solve_ivp(lambda t, g: g ** 3 * (R.K * bps + R.K ** 2 * (Bn @ (g * g))), (0, -d), [gu] * 3, method="DOP853", rtol=1e-13, atol=1e-15).y[:, -1]
    cx = lambda rows: np.array([[complex(*e) for e in row] for row in rows])
    Au = cx([[(2 / 25, 3 / 100), (1 / 20, -1 / 50), (3 / 50, 3 / 100)], [(-1 / 50, 1 / 25), (7 / 25, 1 / 20), (9 / 100, -3 / 50)], [(3 / 100, -1 / 50), (2 / 25, 3 / 50), (1, 1 / 25)]])
    Ad = cx([[(3 / 50, -1 / 50), (2 / 25, 1 / 20), (-1 / 25, 3 / 50)], [(1 / 25, 1 / 20), (1 / 4, -1 / 20), (9 / 100, 2 / 25)], [(-3 / 100, 3 / 100), (7 / 100, -3 / 50), (11 / 20, -3 / 100)]])
    Hu = Au @ Au.conj().T; Hu = Hu / np.linalg.svd(Hu, compute_uv=False)[0]; Hd = Ad @ Ad.conj().T; Ye = np.diag([1 / 1000, 1 / 50, 3 / 20])
    dl, sl, th, jm, lmin = [], [], 0.0, 1.0, 1.0
    for aui, dps in itertools.product((52, 60, 68), (0, 2, 4)):
        g4, g2l, g2r = ps(math.sqrt(4 * math.pi / aui), dps); g1 = math.sqrt(4 * math.pi / (0.6 * 4 * math.pi / g2r ** 2 + 0.4 * 4 * math.pi / g4 ** 2))
        for dsm, yt, c2b in itertools.product((26, 28, 30), (0.5, 0.7, 0.9), (0, 0.5, 1)):
            # the seat's matrices act on the left with H = Y Y^dagger; main's solver takes the adjoint (rows: right-handed)
            v = R.run(R.pack([g1, g2l, g4], (yt * Hu).conj().T, Hd.conj().T, Ye, 2 * 0.25 * g2l ** 2 * c2b), -float(dsm), rtol=1e-11)
            g, H, FD, FL, lam = R.unpack(v); a1, a2, a3 = 4 * math.pi / g ** 2; aem = 5 / 3 * a1 + a2
            dl.append(a2 / aem - (23 / 134 + 109 / 201 * a3 / aem + 506 / 201 / math.pi * dps / aem)); sl.append(math.sqrt(lam)); lmin = min(lmin, lam / 2)
            th = max(th, abs(np.angle(np.linalg.det(H) * np.linalg.det(FD))))
            Vu = np.linalg.eigh(H.conj().T @ H)[1]; Vd = np.linalg.eigh(FD.conj().T @ FD)[1]; V = Vu.conj().T @ Vd; jm = min(jm, abs((V[0, 0] * V[1, 1] * V[0, 1].conj() * V[1, 0].conj()).imag))
    print("      %d histories on main's running: |arg det(Y_u Y_d)| at the bottom at most %.1e, the Jarlskog invariant at least %.4f (the seat: 6.5e-14, 0.0054)" % (len(dl), th, jm))
    print("      the gauge residual lies in [%.7f, %.7f] (the seat: [0.0007265, 0.0027548]; its envelope [7/10000, 3/1000])" % (min(dl), max(dl)))
    print("      sqrt(2 lambda) at the bottom lies in [%.6f, %.6f], the least quartic %.5f (the seat: [0.370482, 0.771511], 0.06863; its envelope [35/100, 78/100])" % (min(sl), max(sl), lmin))
    print("      planted: six generations in place of three shift 1/alpha_3 by 4 x 28 / (2 pi) = %.3f (the seat: 17.825); D(z) + D(conj z) at z = 3/5 + 4i/5 is %.1e: the identity holds for every z, so it cannot pick a sign" % (4 * 28 / (2 * math.pi), abs(complex(mp.im(mp.polylog(2, mp.mpc(0.6, 0.8))) + mp.arg(1 - mp.mpc(0.6, 0.8)) * mp.log(abs(mp.mpc(0.6, 0.8))) + mp.im(mp.polylog(2, mp.mpc(0.6, -0.8))) + mp.arg(1 - mp.mpc(0.6, -0.8)) * mp.log(abs(mp.mpc(0.6, -0.8)))))))
